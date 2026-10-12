#!/usr/bin/env python3
"""Bake a 1200x630 Open Graph share image per city from its local 1900 PMTiles
archive (Kadaster Topotijdreis, CC-BY 4.0). Output: assets/og/<city>.jpg.
Run with the .venv-pmtiles interpreter (needs pillow + pmtiles)."""
import json, math, os, sys
from PIL import Image, ImageDraw, ImageFont
from pmtiles.reader import Reader, MmapSource

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PM = os.path.join(ROOT, "pmtiles")
OUT = os.path.join(ROOT, "assets", "og")
W, H, Z = 1200, 630, 15
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def px(lon, lat, z):
    n = 256 * 2 ** z
    x = (lon + 180) / 360 * n
    y = (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n
    return x, y


def main():
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    from build_city_pages import CITIES
    man = json.load(open(os.path.join(PM, "manifest.json")))["archives"]
    os.makedirs(OUT, exist_ok=True)
    for a in man:
        if a["service"] != "1900":
            continue
        cid = a["city"]
        b = a["bounds"]
        cx, cy = px((b[0] + b[2]) / 2, (b[1] + b[3]) / 2, Z)
        img = Image.new("RGB", (W, H), (238, 230, 213))
        with open(os.path.join(PM, a["url"]), "rb") as f:
            r = Reader(MmapSource(f))
            x0, y0 = cx - W / 2, cy - H / 2
            for tx in range(int(x0 // 256), int((x0 + W) // 256) + 1):
                for ty in range(int(y0 // 256), int((y0 + H) // 256) + 1):
                    d = r.get(Z, tx, ty)
                    if d:
                        import io
                        t = Image.open(io.BytesIO(d)).convert("RGB")
                        img.paste(t, (round(tx * 256 - x0), round(ty * 256 - y0)))
        o = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(o)
        d.rectangle([0, H - 190, W, H], fill=(31, 26, 20, 215))
        d.rectangle([0, H - 190, 10, H], fill=(178, 58, 36, 255))
        img = Image.alpha_composite(img.convert("RGBA"), o)
        d = ImageDraw.Draw(img)
        name = CITIES[cid]["en"]
        d.text((48, H - 170), name, font=ImageFont.truetype(FB, 64), fill=(247, 241, 228))
        d.text((48, H - 85), "Oude-Kaart Wandeling · historical map ~1900 vs today",
               font=ImageFont.truetype(FR, 27), fill=(226, 214, 190))
        d.text((48, H - 44), "Map: © Kadaster, CC-BY 4.0 (Topotijdreis)",
               font=ImageFont.truetype(FR, 20), fill=(190, 178, 156))
        img.convert("RGB").save(os.path.join(OUT, cid + ".jpg"), quality=82, optimize=True)
        print(cid, os.path.getsize(os.path.join(OUT, cid + ".jpg")) // 1024, "KB")


if __name__ == "__main__":
    main()
