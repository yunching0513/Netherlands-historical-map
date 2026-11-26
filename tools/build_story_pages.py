#!/usr/bin/env python3
"""Generate static, crawlable "map story" pages from stories/stories.json.

Each story is a short trilingual (NL/EN/ZH) then/now narrative whose "views"
are deep links into the interactive map (?city=&year=&lat=&lng=&z=&compare=1),
so every page is both an SEO anchor and an entry point that lands the visitor
on the exact historical view the text describes. Output: stories/<id>.html and
a stories/index.html hub. Same bake-and-commit pattern as build_city_pages.py.

Usage: python3 tools/build_story_pages.py
"""
import html, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://yunching0513.github.io/Netherlands-historical-map"
SRC = os.path.join(ROOT, "stories", "stories.json")
OUT = os.path.join(ROOT, "stories")
LANDMARKS = os.path.join(ROOT, "landmarks", "landmarks.json")
DOI = "10.5281/zenodo.21924251"

CITY_NAMES = {
    "amsterdam": "Amsterdam", "rotterdam": "Rotterdam", "utrecht": "Utrecht",
    "middelburg": "Middelburg", "nijmegen": "Nijmegen", "denhaag": "Den Haag",
    "leiden": "Leiden", "delft": "Delft", "haarlem": "Haarlem", "arnhem": "Arnhem", "hilversum": "Hilversum",
}

STYLE = """  body { font-family:'Noto Sans TC',system-ui,sans-serif; max-width:760px; margin:0 auto;
         padding:40px 24px 96px; color:#1F1D19; background:#F1EFE9; line-height:1.85; font-weight:300; }
  a { color:#C15F3C; }
  .crumb { font-size:12.5px; color:#807C73; margin-bottom:18px; }
  .crumb a { color:#807C73; }
  h1 { font-family:'Noto Serif TC',Georgia,serif; font-size:25px; border-bottom:3px solid #C15F3C;
       padding-bottom:12px; margin-bottom:6px; }
  .sub { font-family:'EB Garamond',Georgia,serif; font-style:italic; color:#807C73; font-size:15.5px; margin:2px 0; }
  h2 { font-size:14px; margin-top:30px; color:#565347; letter-spacing:0.06em; border-top:1px solid #DAD7CC;
       padding-top:18px; text-transform:uppercase; font-weight:500; }
  .views { display:flex; flex-wrap:wrap; gap:10px; margin:22px 0 6px; }
  .views a { display:inline-block; padding:9px 14px; background:#1F1D19; color:#F1EFE9; text-decoration:none;
             font-size:13.5px; border-radius:2px; }
  .views a:hover { background:#C15F3C; }
  .cite { font-size:12px; color:#565347; background:#EAE8E2; padding:12px 14px; border-left:3px solid #C15F3C;
          margin-top:30px; word-break:break-word; }
  ul.list { padding-left:18px; } ul.list li { margin:8px 0; }
  .foot { margin-top:44px; font-size:11.5px; color:#807C73; border-top:1px solid #DAD7CC; padding-top:16px; }
  @media (prefers-color-scheme: dark) {
    body { background:#1B1A17; color:#E8E5DC; } h2 { color:#B8B3A6; border-color:#3A3833; }
    .cite { background:#26241F; color:#C9C4B6; } .views a { background:#E8E5DC; color:#1B1A17; }
  }"""

HEAD_FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@500;700&'
              'family=Noto+Sans+TC:wght@300;400;500&family=EB+Garamond:ital@1&display=swap" rel="stylesheet">')

FOOT = """  <div class="foot">
    Part of <a href="../index.html">Oude-Kaart Wandeling / 荷蘭古地圖散策</a>, an open-data overlay of
    Dutch historical topographic maps. Historical maps © Kadaster, CC-BY 4.0 (Topotijdreis).
    Text by Yunching Wu, CC-BY 4.0. See the <a href="../about.html">colofon &amp; method</a> ·
    <a href="index.html">all map stories</a> · <a href="../city/index.html">city guides</a>.
  </div>"""


def esc(s): return html.escape(s, quote=True)


def view_url(city, v, rel=True):
    q = f"city={city}&year={v['year']}&lat={v['lat']}&lng={v['lng']}&z={v['z']}"
    if v.get("compare"): q += "&compare=1"
    return ("../index.html?" if rel else SITE + "/?") + q


def build_story(s, lm_by_id):
    city = s["city"]; cname = CITY_NAMES.get(city, city.title())
    canonical = f"{SITE}/stories/{s['id']}.html"
    t = s["title"]
    desc = s["lede"]["nl"]
    if len(desc) > 300: desc = desc[:297].rsplit(" ", 1)[0] + "…"
    og_image = f"{SITE}/assets/og/{city}.jpg"
    views = "\n".join(
        f'    <a href="{esc(view_url(city, v))}">→ {esc(v["label"]["nl"])} · {esc(v["label"]["en"])} · {esc(v["label"]["zh"])}</a>'
        for v in s["views"])
    lms = [lm_by_id[i] for i in s.get("landmarks", []) if i in lm_by_id]
    lm_html = ""
    if lms:
        items = "".join(
            f'<li><a href="../landmark/{esc(l["id"])}.html">{esc(l["name"].get("nl") or l["name"].get("en"))}</a>'
            f' ({esc(l.get("year",""))})</li>' for l in lms)
        lm_html = f'  <h2>Landmarks in this story</h2>\n  <ul class="list">{items}</ul>\n'
    sections = ""
    for code, label in (("nl", "NL"), ("en", "EN"), ("zh", "中文")):
        sections += (f'  <h2>{label}</h2>\n  <p lang="{code if code!="zh" else "zh-Hant"}">{esc(s["lede"][code])}</p>\n'
                     f'  <p lang="{code if code!="zh" else "zh-Hant"}">{esc(s["body"][code])}</p>\n')
    ld = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": t["nl"], "alternativeHeadline": [t["en"], t["zh"]],
        "inLanguage": ["nl", "en", "zh-Hant"], "description": desc, "url": canonical,
        "image": og_image, "author": {"@type": "Person", "name": "Yunching Wu"},
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "about": {"@type": "City", "name": cname},
        "isPartOf": {"@type": "WebSite", "name": "Oude-Kaart Wandeling", "url": SITE + "/"},
        "citation": f"https://doi.org/{DOI}",
    }
    cite = (f"Wu, Y. (2026). {t['en']}. In <i>Oude-Kaart Wandeling / 荷蘭古地圖散策</i>. "
            f"{canonical}. https://doi.org/{DOI}. Historical maps © Kadaster, CC-BY 4.0.")
    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{esc(t['nl'])} | Oude-Kaart Wandeling</title>
<meta name="description" content="{esc(desc)}" />
<link rel="canonical" href="{canonical}" />
<link rel="icon" type="image/svg+xml" href="../icons/icon.svg" />
<meta property="og:type" content="article" />
<meta property="og:title" content="{esc(t['nl'])}" />
<meta property="og:description" content="{esc(desc)}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:image" content="{og_image}" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="{esc(cname)}: Kadaster Topotijdreis map c. 1900" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="{og_image}" />
{HEAD_FONTS}
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>
{STYLE}
</style>
</head>
<body>
  <div class="crumb"><a href="../index.html">Oude-Kaart Wandeling</a> &rsaquo; <a href="index.html">Kaartverhalen · Map stories</a> &rsaquo; <a href="../city/{city}.html">{esc(cname)}</a></div>
  <h1>{esc(t['nl'])}</h1>
  <p class="sub">{esc(t['en'])}</p>
  <p class="sub">{esc(t['zh'])}</p>
  <div class="views">
{views}
  </div>
{sections}{lm_html}  <div class="cite"><b>Citeer / Cite:</b> {cite}</div>
{FOOT}
</body>
</html>
"""


def build_index(stories):
    canonical = f"{SITE}/stories/index.html"
    items = "\n".join(
        f'    <li><a href="{esc(s["id"])}.html">{esc(s["title"]["nl"])}</a><br>'
        f'<span class="sub">{esc(s["title"]["en"])} · {esc(s["title"]["zh"])}</span></li>' for s in stories)
    desc = ("Kaartverhalen: korte then/now-verhalen bij historische Kadaster-kaarten van Nederlandse steden, "
            "elk met directe links naar de exacte kaartweergave. / Map stories: short then/now narratives "
            "on Dutch historical maps, each linking straight into the exact map view.")
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Kaartverhalen · Map stories",
          "url": canonical, "description": desc,
          "hasPart": [{"@type": "Article", "headline": s["title"]["nl"],
                       "url": f"{SITE}/stories/{s['id']}.html"} for s in stories]}
    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Kaartverhalen — Nederlandse steden toen en nu | Oude-Kaart Wandeling</title>
<meta name="description" content="{esc(desc)}" />
<link rel="canonical" href="{canonical}" />
<link rel="icon" type="image/svg+xml" href="../icons/icon.svg" />
<meta property="og:type" content="website" />
<meta property="og:title" content="Kaartverhalen · Map stories · 地圖故事" />
<meta property="og:description" content="{esc(desc)}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:image" content="{SITE}/assets/og-image.jpg" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="{SITE}/assets/og-image.jpg" />
{HEAD_FONTS}
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>
{STYLE}
</style>
</head>
<body>
  <div class="crumb"><a href="../index.html">Oude-Kaart Wandeling</a> &rsaquo; Kaartverhalen · Map stories</div>
  <h1>Kaartverhalen · Map stories · 地圖故事</h1>
  <p>Korte verhalen over hoe Nederlandse steden veranderden, elk met knoppen die de interactieve kaart
  openen op precies het jaar en de plek waarover het gaat. · Short stories of how Dutch cities changed,
  each with buttons that open the interactive map at exactly the year and place described. ·
  荷蘭城市變遷的短篇故事，每篇都附有按鈕，直接打開互動地圖上對應的年代與地點。</p>
  <ul class="list">
{items}
  </ul>
{FOOT}
</body>
</html>
"""


def main():
    stories = json.load(open(SRC, encoding="utf-8"))["items"]
    lm = {l["id"]: l for l in json.load(open(LANDMARKS, encoding="utf-8"))["items"]}
    for s in stories:
        with open(os.path.join(OUT, f"{s['id']}.html"), "w", encoding="utf-8") as f:
            f.write(build_story(s, lm))
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_index(stories))
    print(f"wrote {len(stories)} stories + index")


if __name__ == "__main__":
    main()
