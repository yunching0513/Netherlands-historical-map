#!/usr/bin/env python3
"""Generate static, crawlable HTML pages for every architecture-walk landmark.

The main app (index.html) renders landmarks from landmarks/landmarks.json
entirely client-side, so search engines never see the rich per-building text
already written and verified for the app (name/architect/year/style/description
in zh/en/nl, licensed photo, Wikipedia links). This script bakes one static
page per landmark under landmark/<id>.html, plus a landmark/index.html hub
page, so each building gets its own indexable URL and JSON-LD entry.

Usage: python3 tools/build_landmark_pages.py
Re-run after any edit to landmarks/landmarks.json; output is fully
regenerated (idempotent) and should be committed like any other static asset.
"""
import json
import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANDMARKS_JSON = os.path.join(ROOT, "landmarks", "landmarks.json")
OUT_DIR = os.path.join(ROOT, "landmark")
SITE = "https://yunching0513.github.io/Netherlands-historical-map"

# Kept in sync by hand with the CITIES array in index.html (id -> zh/en name).
CITIES = {
    "amsterdam":  {"zh": "阿姆斯特丹", "en": "Amsterdam"},
    "rotterdam":  {"zh": "鹿特丹", "en": "Rotterdam"},
    "denhaag":    {"zh": "海牙", "en": "Den Haag"},
    "utrecht":    {"zh": "烏特勒支", "en": "Utrecht"},
    "leiden":     {"zh": "萊頓", "en": "Leiden"},
    "delft":      {"zh": "台夫特", "en": "Delft"},
    "haarlem":    {"zh": "哈勒姆", "en": "Haarlem"},
    "gouda":      {"zh": "豪達", "en": "Gouda"},
    "dordrecht":  {"zh": "多德雷赫特", "en": "Dordrecht"},
    "amersfoort": {"zh": "阿默斯福特", "en": "Amersfoort"},
    "hilversum":  {"zh": "希爾弗瑟姆", "en": "Hilversum"},
    "groningen":  {"zh": "格羅寧根", "en": "Groningen"},
    "leeuwarden": {"zh": "呂伐登", "en": "Leeuwarden"},
    "zwolle":     {"zh": "茲沃勒", "en": "Zwolle"},
    "deventer":   {"zh": "代芬特爾", "en": "Deventer"},
    "arnhem":     {"zh": "阿納姆", "en": "Arnhem"},
    "nijmegen":   {"zh": "奈梅亨", "en": "Nijmegen"},
    "denbosch":   {"zh": "斯海爾托亨博斯", "en": "'s-Hertogenbosch"},
    "eindhoven":  {"zh": "埃因霍溫", "en": "Eindhoven"},
    "maastricht": {"zh": "馬斯特里赫特", "en": "Maastricht"},
    "middelburg": {"zh": "米德爾堡", "en": "Middelburg"},
}

PAGE_CSS = """
  body { font-family:'Noto Sans TC',system-ui,sans-serif; max-width:760px; margin:0 auto;
         padding:40px 24px 96px; color:#1F1D19; background:#F1EFE9; line-height:1.85; font-weight:300; }
  a { color:#C15F3C; }
  .crumb { font-size:12.5px; color:#807C73; letter-spacing:0.02em; margin-bottom:18px; }
  .crumb a { color:#807C73; text-decoration:underline; }
  h1 { font-family:'Noto Serif TC',Georgia,serif; font-size:26px; letter-spacing:0.03em;
       border-bottom:3px solid #C15F3C; padding-bottom:12px; margin-bottom:4px; }
  .h1-sub { font-family:'EB Garamond','Cormorant Garamond',Georgia,serif; font-style:italic;
            color:#807C73; font-size:15px; margin-bottom:24px; }
  .meta { display:flex; flex-wrap:wrap; gap:6px 14px; font-size:12.5px; color:#565347;
          margin-bottom:22px; }
  .meta span b { color:#1F1D19; font-weight:500; }
  figure { margin:0 0 22px; }
  img { width:100%; height:auto; display:block; border:1px solid #DAD7CC; }
  figcaption { font-size:11.5px; color:#807C73; margin-top:6px; }
  h2 { font-size:14px; margin-top:30px; color:#565347; letter-spacing:0.06em;
       border-top:1px solid #DAD7CC; padding-top:20px; text-transform:uppercase; font-weight:500; }
  p.desc { margin-top:10px; }
  .links { margin-top:26px; font-size:13.5px; }
  .links a { display:inline-block; margin-right:16px; }
  .cta { margin-top:36px; padding:16px 18px; background:#EAE8E2; border-left:3px solid #C15F3C; }
  .cta a { font-weight:500; }
  .foot { margin-top:48px; font-size:11.5px; color:#807C73; border-top:1px solid #DAD7CC; padding-top:16px; }
"""


def esc(s):
    return html.escape(s or "", quote=True)


def truncate(s, n):
    s = s or ""
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0]
    return cut.rstrip(",.;") + "…"


def loc3(obj, key):
    """Return (zh, en, nl) tuple from a {zh,en,nl} field, falling back sensibly."""
    if not obj:
        return "", "", ""
    zh = obj.get("zh", "")
    en = obj.get("en", "")
    nl = obj.get("nl", en)
    return zh, en, nl


def build_landmark_page(item, city_name):
    lid = item["id"]
    city = item["city"]
    name_zh, name_en, name_nl = loc3(item.get("name"), "name")
    arch_zh, arch_en, arch_nl = loc3(item.get("architect"), "architect")
    style_zh, style_en, style_nl = loc3(item.get("style_label"), "style_label")
    desc_zh, desc_en, desc_nl = loc3(item.get("desc"), "desc")
    year = item.get("year", "")
    address = item.get("address", "")
    img = item.get("img", "")
    credit = item.get("credit", "")
    license_ = item.get("license", "")
    source_url = item.get("sourceUrl", "")
    wiki = item.get("wiki") or {}
    names_for_title = [n for n in (name_nl, name_en, name_zh) if n]
    seen = []
    for n in names_for_title:
        if n not in seen:
            seen.append(n)
    page_title = f"{' — '.join(seen)} | {city_name['en']} · Oude-Kaart Wandeling"
    description = truncate(desc_en or desc_nl or desc_zh, 300)
    canonical = f"{SITE}/landmark/{lid}.html"
    app_link = f"{SITE}/?city={city}&landmark={lid}"
    h1_variant = f' <span style="color:#807C73;font-weight:300;">/ {esc(name_en)}</span>' if name_en and name_en != name_nl else ""

    wiki_links = []
    for code, label in (("nl", "Wikipedia (NL)"), ("en", "Wikipedia (EN)")):
        if wiki.get(code):
            wiki_links.append(f'<a href="{esc(wiki[code])}" target="_blank" rel="noopener">{label} ↗</a>')

    ld = {
        "@context": "https://schema.org",
        "@type": "LandmarksOrHistoricalBuildings",
        "name": name_en or name_nl,
        "alternateName": [n for n in (name_nl, name_zh) if n and n != name_en],
        "description": description,
        "image": img,
        "address": address,
        "geo": {"@type": "GeoCoordinates", "latitude": item.get("lat"), "longitude": item.get("lng")},
        "url": canonical,
    }
    if wiki.get("en"):
        ld["sameAs"] = wiki["en"]

    html_out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{esc(page_title)}</title>
<meta name="description" content="{esc(description)}" />
<link rel="canonical" href="{esc(canonical)}" />
<link rel="icon" type="image/svg+xml" href="../icons/icon.svg" />
<meta property="og:type" content="article" />
<meta property="og:title" content="{esc(name_nl)} — {esc(name_en)}" />
<meta property="og:description" content="{esc(description)}" />
<meta property="og:image" content="{esc(img)}" />
<meta property="og:url" content="{esc(canonical)}" />
<meta name="twitter:card" content="summary_large_image" />
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@500;700&family=Noto+Sans+TC:wght@300;400;500&family=EB+Garamond:ital@1&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{PAGE_CSS}</style>
</head>
<body>
  <div class="crumb"><a href="../index.html">Oude-Kaart Wandeling</a> &rsaquo;
    <a href="index.html">Landmarks</a> &rsaquo;
    <a href="../index.html?city={esc(city)}">{esc(city_name['en'])}</a> &rsaquo;
    {esc(name_en)}</div>
  <h1>{esc(name_nl)}{h1_variant}</h1>
  <div class="h1-sub">{esc(name_zh)} · {esc(city_name['en'])}, the Netherlands</div>
  <div class="meta">
    <span>{esc(year)}</span>
    <span><b>{esc(style_en or style_nl)}</b></span>
    <span>{esc(address)}</span>
  </div>
  <figure>
    <img src="{esc(img)}" alt="{esc(name_en)} — {esc(arch_en or arch_nl)}" loading="lazy" />
    <figcaption>{esc(credit)} · {esc(license_)} · <a href="{esc(source_url)}" target="_blank" rel="noopener">source ↗</a></figcaption>
  </figure>

  <h2>NL</h2>
  <p class="desc">{esc(desc_nl)}</p>
  <p class="desc"><em>Architect:</em> {esc(arch_nl)} &middot; <em>Stijl:</em> {esc(style_nl)}</p>

  <h2>EN</h2>
  <p class="desc">{esc(desc_en)}</p>
  <p class="desc"><em>Architect:</em> {esc(arch_en)} &middot; <em>Style:</em> {esc(style_en)}</p>

  <h2>中文</h2>
  <p class="desc">{esc(desc_zh)}</p>
  <p class="desc"><em>建築師：</em>{esc(arch_zh)} &middot; <em>風格：</em>{esc(style_zh)}</p>

  <div class="links">{' · '.join(wiki_links) if wiki_links else ''}</div>

  <div class="cta">
    <a href="{esc(app_link)}">→ View {esc(name_en)} on the interactive historical map ↗</a>
  </div>

  <div class="foot">
    Part of <a href="../index.html">Oude-Kaart Wandeling / 荷蘭古地圖散策</a>, an open-data
    overlay of Dutch historical topographic maps (1815–2021, Kadaster/Topotijdreis, CC-BY 4.0)
    with a self-guided architecture walk across {len(CITIES)} cities.
    Photo licensed {esc(license_)}, credit {esc(credit)}, via
    <a href="{esc(source_url)}" target="_blank" rel="noopener">Wikimedia Commons</a>.
    See the <a href="../about.html">colofon &amp; method</a> for citation details.
  </div>
</body>
</html>
"""
    return html_out


def build_index_page(items_by_city):
    rows = []
    for city_id in sorted(items_by_city.keys(), key=lambda c: CITIES.get(c, {}).get("en", c)):
        cname = CITIES.get(city_id, {"zh": city_id, "en": city_id})
        entries = items_by_city[city_id]
        links = "\n".join(
            f'      <li><a href="{esc(it["id"])}.html">{esc((it.get("name") or {}).get("en") or it["id"])}</a>'
            f' <span style="color:#807C73;">— {esc((it.get("style_label") or {}).get("en", ""))}, {esc(it.get("year",""))}</span></li>'
            for it in entries
        )
        rows.append(
            f'    <h2>{esc(cname["en"])} <span style="color:#807C73;font-weight:300;">{esc(cname["zh"])}</span></h2>\n'
            f'    <ul>\n{links}\n    </ul>'
        )
    body = "\n".join(rows)
    total = sum(len(v) for v in items_by_city.values())
    canonical = f"{SITE}/landmark/index.html"
    description = (
        f"Index of {total} verified architecture-walk landmarks across "
        f"{len(items_by_city)} Dutch cities — churches, town halls, and modernist landmarks, "
        f"each with sourced history, architect, style, and a CC-licensed photo."
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Architecture landmarks index | Oude-Kaart Wandeling</title>
<meta name="description" content="{esc(description)}" />
<link rel="canonical" href="{esc(canonical)}" />
<link rel="icon" type="image/svg+xml" href="../icons/icon.svg" />
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@500;700&family=Noto+Sans+TC:wght@300;400;500&display=swap" rel="stylesheet">
<style>{PAGE_CSS}
  ul {{ list-style:none; padding:0; margin:6px 0 0; }}
  li {{ padding:4px 0; font-size:14px; }}
</style>
</head>
<body>
  <div class="crumb"><a href="../index.html">Oude-Kaart Wandeling</a> &rsaquo; Landmarks</div>
  <h1>Architecture landmarks</h1>
  <div class="h1-sub">{total} verified buildings across {len(items_by_city)} Dutch cities — sourced from
  the Dutch/English Wikipedia and Wikimedia Commons, each independently verified.</div>
{body}
  <div class="foot">
    Part of <a href="../index.html">Oude-Kaart Wandeling / 荷蘭古地圖散策</a>. See the
    <a href="../about.html">colofon &amp; method</a> for licensing and citation.
  </div>
</body>
</html>
"""


def main():
    with open(LANDMARKS_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    items = [i for i in data["items"] if i.get("img") and i.get("city")]
    os.makedirs(OUT_DIR, exist_ok=True)

    by_city = {}
    for item in items:
        by_city.setdefault(item["city"], []).append(item)
        city_name = CITIES.get(item["city"], {"zh": item["city"], "en": item["city"]})
        page = build_landmark_page(item, city_name)
        out_path = os.path.join(OUT_DIR, f"{item['id']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page)

    index_page = build_index_page(by_city)
    with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_page)

    print(f"Wrote {len(items)} landmark pages + index.html to {OUT_DIR}")
    unknown_cities = sorted(set(i["city"] for i in items) - set(CITIES.keys()))
    if unknown_cities:
        print(f"WARNING: unknown city ids not in this script's CITIES table: {unknown_cities}")


if __name__ == "__main__":
    main()
