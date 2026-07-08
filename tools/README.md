# Offline historical tiles (PMTiles)

The Topotijdreis historical maps only exist in RD (EPSG:28992); the app normally
reprojects each tile to Web Mercator on a `<canvas>` at runtime, which needs the
network. `bake_pmtiles.py` does that reprojection **ahead of time** and packs the
result into a single serverless `.pmtiles` file, so the app can read tiles locally
with zero network — the basis for app-store builds (Capacitor / TWA).

**Source & license:** Kadaster TOPraster / Topotijdreis, **CC-BY 4.0**. Baked tiles
carry the attribution `© Kadaster, CC-BY 4.0`, shown by the app when an archive is
active.

## Bake an archive

```bash
python3 -m venv .venv-pmtiles
. .venv-pmtiles/bin/activate
pip install pyproj pillow pmtiles requests

python tools/bake_pmtiles.py \
  --service 1900 --city amsterdam \
  --lat 52.3731 --lng 4.8922 --half-lat 0.018 --half-lng 0.028 \
  --min-zoom 12 --max-zoom 16 \
  --format webp --quality 82 \
  --out pmtiles/amsterdam-1900.pmtiles
```

- `--service` is the Topotijdreis year id (see `AVAIL` in `index.html`).
- `--city` is the app's city id (used in the manifest entry).
- `--format webp` keeps tiles ~8× smaller than PNG at near-identical quality.
- Each run merges/updates an entry in `pmtiles/manifest.json`.

## How the app consumes it

At startup the app fetches `pmtiles/manifest.json` and opens each `.pmtiles` with
the `pmtiles` JS library. For every historical tile, `createTopotijdreisLayer`
first asks `pmtilesFor(service, coords)` whether a bundled archive covers it
(matching year + bounds + zoom). If yes it draws the local WEBP tile directly
(already 3857 — no reprojection); if not, it falls back to the online Topotijdreis
service exactly as before. Missing library / manifest → everything stays online.

## Reference PoC

`pmtiles/amsterdam-1900.pmtiles` — Amsterdam, 1900, z12–16, ~3.2 MB, 192 tiles
(~17 KB/tile). Verify by scrubbing the year to 1900 in Amsterdam.
