#!/usr/bin/env python3
"""Bake a Topotijdreis historical era into a single .pmtiles raster archive.

The Netherlands historical map tiles only exist in RD (EPSG:28992). The web app
reprojects each tile to Web Mercator (EPSG:3857) on a <canvas> at runtime. This
script does that same reprojection ahead of time and packs the result into one
serverless .pmtiles file, so the app can read tiles locally with zero network.

The reprojection math is a 1:1 port of histTileGeom()/createTile() in index.html
(same RD proj4 string, same origin, same resolution ladder) so baked tiles line
up pixel-for-pixel with the online fallback.

Source data: Kadaster TOPraster / Topotijdreis, licensed CC-BY 4.0.

Usage:
    python tools/bake_pmtiles.py --service 1900 --lat 52.3731 --lng 4.8922 \
        --half-lat 0.018 --half-lng 0.028 --min-zoom 12 --max-zoom 16 \
        --out pmtiles/amsterdam-1900.pmtiles
"""
import argparse, io, json, math, os, sys, threading
from concurrent.futures import ThreadPoolExecutor

import requests
from PIL import Image
from pyproj import Transformer
from pmtiles.writer import Writer
from pmtiles.tile import TileType, Compression, zxy_to_tileid

# ── Constants ported verbatim from index.html ───────────────────────────────
RD_PROJ4 = ('+proj=sterea +lat_0=52.15616055555555 +lon_0=5.38763888888889 '
            '+k=0.9999079 +x_0=155000 +y_0=463000 +ellps=bessel '
            '+towgs84=565.4171,50.3319,465.5524,-0.398957,0.343988,-1.8774,4.0725 '
            '+units=m +no_defs')
RD_ORIGIN_X, RD_ORIGIN_Y, RD_TILE_SIZE = -30515500, 31112400, 256
RD_RESOLUTIONS = [3251.206502413005, 1625.6032512065026, 812.8016256032513,
                  406.40081280162565, 203.20040640081282, 101.60020320040641,
                  50.800101600203206, 25.400050800101603, 12.700025400050801,
                  6.350012700025401, 3.1750063500127004, 1.5875031750063502]
ARC = 'https://tiles.arcgis.com/tiles/nSZVuSZjHpEZZbRo/arcgis/rest/services/'
R_MERC = 20037508.342789244  # Leaflet EPSG3857 half-extent (pi * 6378137)

_to_rd = Transformer.from_crs('EPSG:3857', RD_PROJ4, always_xy=True)
_to_merc = Transformer.from_crs(RD_PROJ4, 'EPSG:3857', always_xy=True)

_session = requests.Session()
_tile_cache = {}
_cache_lock = threading.Lock()


def merc_x(px, z): return px / (RD_TILE_SIZE * 2 ** z) * (2 * R_MERC) - R_MERC
def merc_y(py, z): return R_MERC - py / (RD_TILE_SIZE * 2 ** z) * (2 * R_MERC)
def px_x(mx, z): return (mx + R_MERC) / (2 * R_MERC) * (RD_TILE_SIZE * 2 ** z)
def px_y(my, z): return (R_MERC - my) / (2 * R_MERC) * (RD_TILE_SIZE * 2 ** z)


def hist_tile_geom(x, y, z):
    """Which RD source tiles does one 3857 tile need? Mirrors histTileGeom()."""
    nw_merc = (merc_x(x * RD_TILE_SIZE, z), merc_y(y * RD_TILE_SIZE, z))
    se_merc = (merc_x((x + 1) * RD_TILE_SIZE, z), merc_y((y + 1) * RD_TILE_SIZE, z))
    nw_rd = _to_rd.transform(*nw_merc)
    se_rd = _to_rd.transform(*se_merc)
    min_x, max_x = min(nw_rd[0], se_rd[0]), max(nw_rd[0], se_rd[0])
    min_y, max_y = min(nw_rd[1], se_rd[1]), max(nw_rd[1], se_rd[1])
    target_res = (max_x - min_x) / RD_TILE_SIZE
    # Coarsest RD level still fine enough for this zoom. (index.html's online
    # path picks the finest level for every zoom — correct but wasteful; here
    # we sample at the matching resolution, which aligns identically and keeps
    # the archive small.)
    lvl = len(RD_RESOLUTIONS) - 1
    for i in range(len(RD_RESOLUTIONS)):
        if RD_RESOLUTIONS[i] <= target_res * 1.5:
            lvl = i
            break
    rd_tile_m = RD_RESOLUTIONS[lvl] * RD_TILE_SIZE
    col_min = math.floor((min_x - RD_ORIGIN_X) / rd_tile_m)
    col_max = math.floor((max_x - RD_ORIGIN_X) / rd_tile_m)
    row_min = math.floor((RD_ORIGIN_Y - max_y) / rd_tile_m)
    row_max = math.floor((RD_ORIGIN_Y - min_y) / rd_tile_m)
    tiles = [(c, r) for r in range(row_min, row_max + 1)
             for c in range(col_min, col_max + 1)]
    return lvl, rd_tile_m, tiles


def fetch_rd_tile(service, lvl, row, col):
    key = (service, lvl, row, col)
    with _cache_lock:
        if key in _tile_cache:
            return _tile_cache[key]
    url = f'{ARC}Historische_tijdreis_{service}/MapServer/tile/{lvl}/{row}/{col}'
    img = None
    for attempt in range(3):
        try:
            r = _session.get(url, timeout=20)
            if r.status_code == 200 and r.content:
                img = Image.open(io.BytesIO(r.content)).convert('RGBA')
            break
        except Exception:
            if attempt == 2:
                break
    with _cache_lock:
        _tile_cache[key] = img
    return img


def render_tile(service, x, y, z):
    """Reproject RD source tiles into one 256px 3857 tile. Mirrors createTile()."""
    lvl, rd_tile_m, tiles = hist_tile_geom(x, y, z)
    canvas = Image.new('RGBA', (RD_TILE_SIZE, RD_TILE_SIZE), (0, 0, 0, 0))
    nw_px = (x * RD_TILE_SIZE, y * RD_TILE_SIZE)
    painted = False
    for col, row in tiles:
        src = fetch_rd_tile(service, lvl, row, col)
        if src is None:
            continue
        x0, y0 = RD_ORIGIN_X + col * rd_tile_m, RD_ORIGIN_Y - row * rd_tile_m

        def rd_to_px(rx, ry):
            mx, my = _to_merc.transform(rx, ry)
            return px_x(mx, z) - nw_px[0], px_y(my, z) - nw_px[1]

        ax, ay = rd_to_px(x0, y0)
        bx, by = rd_to_px(x0 + rd_tile_m, y0 - rd_tile_m)
        w, h = round(bx - ax), round(by - ay)
        if w <= 0 or h <= 0:
            continue
        resized = src.resize((w, h), Image.BILINEAR)
        canvas.alpha_composite(resized, (round(ax), round(ay)))
        painted = True
    return canvas if painted else None


def tiles_in_bbox(lat, lng, half_lat, half_lng, z):
    def lat_to_py(deg):
        s = math.sin(math.radians(deg))
        my = R_MERC / math.pi * 0.5 * math.log((1 + s) / (1 - s))
        return px_y(my, z)
    def lng_to_px(deg):
        return px_x(deg / 180.0 * R_MERC, z)
    x_min = math.floor(lng_to_px(lng - half_lng) / RD_TILE_SIZE)
    x_max = math.floor(lng_to_px(lng + half_lng) / RD_TILE_SIZE)
    y_min = math.floor(lat_to_py(lat + half_lat) / RD_TILE_SIZE)
    y_max = math.floor(lat_to_py(lat - half_lat) / RD_TILE_SIZE)
    return [(x, y) for x in range(x_min, x_max + 1)
            for y in range(y_min, y_max + 1)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--service', required=True, help='Topotijdreis service id, e.g. 1900')
    ap.add_argument('--lat', type=float, required=True)
    ap.add_argument('--lng', type=float, required=True)
    ap.add_argument('--half-lat', type=float, default=0.018)
    ap.add_argument('--half-lng', type=float, default=0.028)
    ap.add_argument('--min-zoom', type=int, default=12)
    ap.add_argument('--max-zoom', type=int, default=16)
    ap.add_argument('--out', required=True)
    ap.add_argument('--format', choices=['png', 'webp'], default='webp')
    ap.add_argument('--quality', type=int, default=82, help='WEBP quality 1-100')
    ap.add_argument('--workers', type=int, default=8)
    ap.add_argument('--city', help='city id, for the manifest entry (e.g. amsterdam)')
    ap.add_argument('--manifest', default='pmtiles/manifest.json',
                    help='manifest the app reads to discover archives')
    args = ap.parse_args()

    jobs = []
    for z in range(args.min_zoom, args.max_zoom + 1):
        for x, y in tiles_in_bbox(args.lat, args.lng, args.half_lat, args.half_lng, z):
            jobs.append((z, x, y))
    print(f'Planning {len(jobs)} output tiles (z{args.min_zoom}-{args.max_zoom})', flush=True)

    results = {}
    done = [0]
    lock = threading.Lock()

    def work(job):
        z, x, y = job
        data = None
        img = render_tile(args.service, x, y, z)
        if img is not None:
            buf = io.BytesIO()
            if args.format == 'webp':
                img.save(buf, format='WEBP', quality=args.quality, method=6)
            else:
                img.save(buf, format='PNG', optimize=True)
            data = buf.getvalue()
        with lock:
            done[0] += 1
            if data:
                results[(z, x, y)] = data
            if done[0] % 25 == 0 or done[0] == len(jobs):
                print(f'  {done[0]}/{len(jobs)} rendered, {len(results)} non-empty', flush=True)

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        list(ex.map(work, jobs))

    if not results:
        print('No tiles rendered — check service id / bbox.', file=sys.stderr)
        sys.exit(1)

    with open(args.out, 'wb') as f:
        w = Writer(f)
        for (z, x, y) in sorted(results, key=lambda k: zxy_to_tileid(*k)):
            w.write_tile(zxy_to_tileid(z, x, y), results[(z, x, y)])
        e7 = lambda v: int(v * 1e7)
        header = {
            'tile_type': TileType.WEBP if args.format == 'webp' else TileType.PNG,
            'tile_compression': Compression.NONE,
            'min_lon_e7': e7(args.lng - args.half_lng),
            'min_lat_e7': e7(args.lat - args.half_lat),
            'max_lon_e7': e7(args.lng + args.half_lng),
            'max_lat_e7': e7(args.lat + args.half_lat),
            'center_zoom': args.max_zoom,
            'center_lon_e7': e7(args.lng),
            'center_lat_e7': e7(args.lat),
        }
        meta = {
            'attribution': '© Kadaster, CC-BY 4.0',
            'name': f'Topotijdreis {args.service}',
            'source': 'Kadaster TOPraster / Topotijdreis',
            'license': 'CC-BY 4.0',
        }
        w.finalize(header, meta)

    size = os.path.getsize(args.out)
    print(f'\nWrote {args.out}')
    print(f'  tiles: {len(results)} non-empty / {len(jobs)} planned')
    print(f'  size:  {size/1048576:.2f} MB ({size} bytes)')
    print(f'  avg:   {size/max(1,len(results))/1024:.1f} KB/tile')

    # Merge an entry into the manifest the app reads at startup.
    entry = {
        'id': f'{args.city or "city"}-{args.service}',
        'city': args.city,
        'service': args.service,
        'url': os.path.relpath(args.out, os.path.dirname(args.manifest) or '.'),
        'bounds': [args.lng - args.half_lng, args.lat - args.half_lat,
                   args.lng + args.half_lng, args.lat + args.half_lat],
        'minzoom': args.min_zoom,
        'maxzoom': args.max_zoom,
        'format': args.format,
        'attribution': '© Kadaster, CC-BY 4.0',
    }
    manifest = {'archives': []}
    if os.path.exists(args.manifest):
        try:
            manifest = json.load(open(args.manifest))
        except Exception:
            pass
    manifest['archives'] = [a for a in manifest.get('archives', [])
                            if a.get('id') != entry['id']] + [entry]
    os.makedirs(os.path.dirname(args.manifest) or '.', exist_ok=True)
    json.dump(manifest, open(args.manifest, 'w'), ensure_ascii=False, indent=2)
    print(f'  manifest: {args.manifest} ({len(manifest["archives"])} archive(s))')


if __name__ == '__main__':
    main()
