#!/usr/bin/env python3
"""Generate static, crawlable long-form landing pages for every city.

The main app (index.html) only ever mentions a city's history in one short
paragraph inside a single shared <noscript> block (all 21 cities in one
page, aggregated for accessibility, not indexing depth) or client-side inside
the SPA. This script bakes one static page per city under city/<id>.html,
plus a city/index.html hub, aggregating what the app already knows about that
city — its historical map coverage, its architecture-walk landmarks (with
links to their own B-25 static pages), and its art postcards — into one
crawlable, citable URL per city. Same "bake static output, commit it like any
other asset" pattern as tools/build_landmark_pages.py.

Usage: python3 tools/build_city_pages.py
Re-run after any edit to landmarks/landmarks.json, postcards/postcards.json,
or pmtiles/manifest.json; output is fully regenerated (idempotent) and should
be committed like any other static asset.
"""
import json
import html
import os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANDMARKS_JSON = os.path.join(ROOT, "landmarks", "landmarks.json")
POSTCARDS_JSON = os.path.join(ROOT, "postcards", "postcards.json")
MANIFEST_JSON = os.path.join(ROOT, "pmtiles", "manifest.json")
OUT_DIR = os.path.join(ROOT, "city")
SITE = "https://yunching0513.github.io/Netherlands-historical-map"

# Kept in sync by hand with the CITIES array in index.html.
CITIES = {
    "amsterdam":  {"zh": "阿姆斯特丹", "en": "Amsterdam",       "region": "randstad", "lat": 52.3731, "lng": 4.8922},
    "rotterdam":  {"zh": "鹿特丹",     "en": "Rotterdam",       "region": "randstad", "lat": 51.9225, "lng": 4.4792},
    "denhaag":    {"zh": "海牙",       "en": "Den Haag",        "region": "randstad", "lat": 52.0799, "lng": 4.3113},
    "utrecht":    {"zh": "烏特勒支",   "en": "Utrecht",         "region": "randstad", "lat": 52.0908, "lng": 5.1222},
    "leiden":     {"zh": "萊頓",       "en": "Leiden",          "region": "randstad", "lat": 52.1589, "lng": 4.4937},
    "delft":      {"zh": "台夫特",     "en": "Delft",           "region": "randstad", "lat": 52.0116, "lng": 4.3571},
    "haarlem":    {"zh": "哈勒姆",     "en": "Haarlem",         "region": "randstad", "lat": 52.3814, "lng": 4.6375},
    "gouda":      {"zh": "豪達",       "en": "Gouda",           "region": "randstad", "lat": 52.0115, "lng": 4.7104},
    "dordrecht":  {"zh": "多德雷赫特", "en": "Dordrecht",       "region": "randstad", "lat": 51.8133, "lng": 4.6901},
    "amersfoort": {"zh": "阿默斯福特", "en": "Amersfoort",      "region": "randstad", "lat": 52.1561, "lng": 5.3878},
    "hilversum":  {"zh": "希爾弗瑟姆", "en": "Hilversum",       "region": "randstad", "lat": 52.2233, "lng": 5.1719},
    "groningen":  {"zh": "格羅寧根",   "en": "Groningen",       "region": "noord",    "lat": 53.2194, "lng": 6.5665},
    "leeuwarden": {"zh": "呂伐登",     "en": "Leeuwarden",      "region": "noord",    "lat": 53.2012, "lng": 5.7999},
    "zwolle":     {"zh": "茲沃勒",     "en": "Zwolle",          "region": "noord",    "lat": 52.5168, "lng": 6.0830},
    "deventer":   {"zh": "代芬特爾",   "en": "Deventer",        "region": "noord",    "lat": 52.2552, "lng": 6.1639},
    "arnhem":     {"zh": "阿納姆",     "en": "Arnhem",          "region": "noord",    "lat": 51.9851, "lng": 5.8987},
    "nijmegen":   {"zh": "奈梅亨",     "en": "Nijmegen",        "region": "noord",    "lat": 51.8126, "lng": 5.8372},
    "denbosch":   {"zh": "斯海爾托亨博斯", "en": "'s-Hertogenbosch", "region": "zuid", "lat": 51.6978, "lng": 5.3037},
    "eindhoven":  {"zh": "埃因霍溫",   "en": "Eindhoven",       "region": "zuid",     "lat": 51.4416, "lng": 5.4697},
    "maastricht": {"zh": "馬斯特里赫特", "en": "Maastricht",    "region": "zuid",     "lat": 50.8514, "lng": 5.6910},
    "middelburg": {"zh": "米德爾堡",   "en": "Middelburg",      "region": "zuid",     "lat": 51.4988, "lng": 3.6111},
}

REGION_LABEL = {
    "randstad": {"zh": "蘭斯塔德都會區", "en": "Randstad"},
    "noord":    {"zh": "北部與東部",     "en": "North & East"},
    "zuid":     {"zh": "南部",           "en": "South"},
}

# Translated verbatim from the shared <noscript> block in index.html (same
# facts, three languages) — no new historical claims, pure presentation-layer
# translation of copy already reviewed and shipped for B-5.
BLURBS = {
    "amsterdam": {
        "nl": "De grachtengordel (1613 e.v.) en de latere uitbreidingen — van Plan Zuid (Berlage) tot de naoorlogse Westelijke Tuinsteden — zijn goed te volgen op de historische kaartseries van 1815 tot nu.",
        "en": "The canal ring (from 1613 onward) and later expansions — from Plan Zuid (Berlage) to the postwar Western Garden Cities — can be traced clearly across the historical map series from 1815 to today.",
        "zh": "阿姆斯特丹運河帶（始於1613年）及其後續擴張——從貝爾拉赫規劃的南區（Plan Zuid）到戰後的西部花園城市——都能在1815年至今的歷史地圖圖層中清楚追溯。",
    },
    "rotterdam": {
        "nl": "Het centrum werd in mei 1940 grotendeels verwoest en daarna modernistisch herbouwd; de kaarten van voor en na 1940 laten dit contrast scherp zien.",
        "en": "The city centre was largely destroyed in May 1940 and rebuilt in a modernist style afterward; the maps from before and after 1940 show this contrast sharply.",
        "zh": "鹿特丹市中心在1940年5月的轟炸中大部分被摧毀，戰後以現代主義風格重建；1940年前後的地圖鮮明地呈現了這種對比。",
    },
    "denhaag": {
        "nl": "Regeringszetel met negentiende- en twintigste-eeuwse stadsuitbreidingen zoals het Statenkwartier en Zeeheldenkwartier, duidelijk zichtbaar in de Bonnebladen en topografische kaarten.",
        "en": "Seat of the Dutch government, with 19th- and 20th-century urban expansions such as the Statenkwartier and Zeeheldenkwartier districts, clearly visible in the Bonneblad and topographic map series.",
        "zh": "海牙是荷蘭政府所在地，19、20世紀的城市擴張，如國會議員區（Statenkwartier）與海軍英雄區（Zeeheldenkwartier），在邦內地圖（Bonneblad）與地形圖系列中清晰可見。",
    },
    "utrecht": {
        "nl": "Middeleeuwse grachtenstad met unieke werven; de historische kaartlagen tonen de groei rond de Domtoren en latere Rietveld-architectuur.",
        "en": "A medieval canal city with its distinctive wharf cellars; the historical map layers show growth around the Dom Tower and the later Rietveld architecture.",
        "zh": "烏特勒支是擁有獨特碼頭地窖（werven）的中世紀運河城市；歷史地圖圖層展現了圍繞主教座堂塔（Domtoren）的城市成長，以及後來的里特費爾德建築。",
    },
    "leiden": {
        "nl": "Universiteitsstad sinds 1575 met een compacte grachtenring en textielindustrieverleden, terug te zien in de kaarten van de negentiende eeuw.",
        "en": "A university town since 1575 with a compact canal ring and a textile-industry past, traceable in the 19th-century map series.",
        "zh": "萊頓自1575年起即為大學城，擁有緊湊的運河環與紡織工業歷史，可在19世紀的地圖系列中追溯。",
    },
    "delft": {
        "nl": "Grachtenstad met een historische kern die opvallend gaaf bewaard is gebleven — de kaartlagen laten zien hoe weinig het stratenpatroon sinds 1815 is veranderd.",
        "en": "A canal town whose historic core has remained remarkably intact — the map layers show how little the street pattern has changed since 1815.",
        "zh": "台夫特是一座運河城鎮，其歷史核心保存得異常完整——地圖圖層顯示自1815年以來街道格局幾乎沒有改變。",
    },
    "haarlem": {
        "nl": "Stad aan het Spaarne met een middeleeuwse kern rond de Grote Markt; de kaartseries tonen de negentiende-eeuwse vestingwerken en hun latere ontmanteling.",
        "en": "A city on the river Spaarne with a medieval core around the Grote Markt; the map series shows the 19th-century fortifications and their later dismantling.",
        "zh": "哈勒姆位於斯帕恩河畔，中世紀核心圍繞著大市集廣場（Grote Markt）；地圖系列顯示了19世紀的城防工事及其後來的拆除。",
    },
    "gouda": {
        "nl": "Bekend om de kaasmarkt en het gotische stadhuis; de historische kaarten volgen de grachten en veenontginning rond de stad.",
        "en": "Known for its cheese market and Gothic town hall; the historical maps trace the canals and peat reclamation around the city.",
        "zh": "豪達以起司市場與哥德式市政廳聞名；歷史地圖追溯了城市周邊的運河與泥炭地開墾過程。",
    },
    "dordrecht": {
        "nl": "De oudste stad van Holland (stadsrecht 1220), gelegen op een eiland bij de samenvloeiing van rivieren — de kaarten tonen de karakteristieke eilandvorm.",
        "en": "The oldest city in Holland (city rights granted in 1220), situated on an island at the confluence of rivers — the maps show its distinctive island shape.",
        "zh": "多德雷赫特是荷蘭省最古老的城市（1220年獲得城市權），坐落在河流匯流處的一座島上——地圖呈現出其獨特的島嶼形狀。",
    },
    "amersfoort": {
        "nl": "Middeleeuwse ommuurde stad met twee concentrische grachtenringen die de historische stadsuitbreiding markeren, goed zichtbaar op de oudste kaartlagen.",
        "en": "A walled medieval town with two concentric canal rings marking its historical expansion, clearly visible on the oldest map layers.",
        "zh": "阿默斯福特是一座有城牆的中世紀城鎮，擁有兩道同心運河環，標示著歷史上的城市擴張，在最古老的地圖圖層中清晰可見。",
    },
    "hilversum": {
        "nl": "Mediastad met een internationaal invloedrijk modernistisch erfgoed — Willem Marinus Dudoks raadhuis (1931) en Jan Duikers Zonnestraal-sanatorium (1928) liggen beide over het bosrijke, dorpse stratenpatroon van de kaart van 1900, van vóór hun bouw.",
        "en": "A media town with internationally influential modernist heritage — Willem Marinus Dudok's town hall (1931) and Jan Duiker's Zonnestraal sanatorium (1928) both sit over the wooded, village-like street pattern of the 1900 map, drawn before either was built.",
        "zh": "希爾弗瑟姆是一座媒體之城，擁有國際知名的現代主義建築遺產——威廉·馬里努斯·杜多克（Dudok）設計的市政廳（1931年）與揚·杜伊克（Duiker）設計的桑內斯特爾療養院（Zonnestraal，1928年），兩者都座落在1900年地圖所繪、建成前的林間村落式街道格局之上。",
    },
    "groningen": {
        "nl": "Noordelijke universiteitsstad met vroegere stervormige vestingwerken; de kaarten tonen hoe de bolwerken plaatsmaakten voor parken zoals rond de Ossenmarkt.",
        "en": "A northern university city with former star-shaped fortifications; the maps show how the bastions gave way to parks such as the one around the Ossenmarkt.",
        "zh": "格羅寧根是北方的大學城，曾擁有星形城防工事；地圖顯示了稜堡如何讓位給公園，例如奧森市場（Ossenmarkt）周邊的公園。",
    },
    "leeuwarden": {
        "nl": "Hoofdstad van Friesland met een grachtenpatroon rond de scheve Oldehove-toren, te volgen door de kaartseries sinds 1815.",
        "en": "The capital of Friesland, with a canal pattern around the leaning Oldehove tower, traceable through the map series since 1815.",
        "zh": "呂伐登是菲士蘭省的首府，運河格局圍繞著傾斜的奧德霍夫塔（Oldehove），可透過1815年以來的地圖系列追溯。",
    },
    "zwolle": {
        "nl": "Hanzestad met een ring van vestingwallen die nu een parkgordel vormen — duidelijk herkenbaar op de historische kaarten.",
        "en": "A Hanseatic city with a ring of fortress walls that now forms a park belt — clearly recognizable on the historical maps.",
        "zh": "茲沃勒是漢薩同盟城市，其城防牆環現已成為公園帶——在歷史地圖上清晰可辨。",
    },
    "deventer": {
        "nl": "Een van de oudste Hanzesteden aan de IJssel, met een middeleeuws stratenpatroon dat op de kaarten nauwelijks is gewijzigd.",
        "en": "One of the oldest Hanseatic cities on the IJssel river, with a medieval street pattern barely changed on the maps.",
        "zh": "代芬特爾是艾瑟爾河畔最古老的漢薩城市之一，其中世紀街道格局在地圖上幾乎沒有變化。",
    },
    "arnhem": {
        "nl": "Stad die zwaar beschadigd raakte tijdens de Slag om Arnhem (1944) en daarna herbouwd werd; de naoorlogse kaartlagen tonen de wederopbouw.",
        "en": "A city heavily damaged during the Battle of Arnhem (1944) and rebuilt afterward; the postwar map layers show the reconstruction.",
        "zh": "阿納姆在1944年的阿納姆戰役中嚴重受損，戰後重建；戰後的地圖圖層展現了這段重建過程。",
    },
    "nijmegen": {
        "nl": "De oudste stad van Nederland (Romeins Noviomagus), ook zwaar getroffen door bombardementen in 1944 — de kaartseries tonen eeuwen stadsontwikkeling en wederopbouw.",
        "en": "The oldest city in the Netherlands (Roman Noviomagus), also heavily hit by bombing in 1944 — the map series shows centuries of urban development and reconstruction.",
        "zh": "奈梅亨是荷蘭最古老的城市（羅馬時代的諾維奧馬古斯），1944年也曾遭受嚴重轟炸——地圖系列展現了數個世紀的城市發展與戰後重建。",
    },
    "denbosch": {
        "nl": "Geboortestad van schilder Jheronimus Bosch, met een vestingstad-plattegrond van grachten en bastions die op de historische kaarten goed te herkennen is.",
        "en": "Birthplace of the painter Hieronymus Bosch, with a fortress-town layout of canals and bastions clearly recognizable on the historical maps.",
        "zh": "斯海爾托亨博斯是畫家耶羅尼米斯·波希（Hieronymus Bosch）的出生地，擁有運河與稜堡構成的要塞城鎮格局，在歷史地圖上清晰可辨。",
    },
    "eindhoven": {
        "nl": "Groeide in de twintigste eeuw van dorp tot industriestad dankzij Philips; de kaartserie 1900–2021 toont deze snelle stedelijke expansie.",
        "en": "Grew from a village into an industrial city during the 20th century thanks to Philips; the 1900–2021 map series shows this rapid urban expansion.",
        "zh": "埃因霍溫在20世紀因飛利浦公司而從村莊發展為工業城市；1900年至2021年的地圖系列展現了這段快速的城市擴張。",
    },
    "maastricht": {
        "nl": "De oudste continu bewoonde stad van Nederland, met Romeinse wortels aan de Maas; de kaarten tonen eeuwen vestingbouw rond het Vrijthof.",
        "en": "The oldest continuously inhabited city in the Netherlands, with Roman roots on the river Maas; the maps show centuries of fortress-building around the Vrijthof.",
        "zh": "馬斯特里赫特是荷蘭持續有人居住最久的城市，源於馬士河畔的羅馬時代聚落；地圖展現了圍繞自由廣場（Vrijthof）數個世紀的城防建設。",
    },
    "middelburg": {
        "nl": "Hoofdstad van Zeeland en VOC-kamerstad, in 1940 zwaar getroffen door bombardementen en nadien in oude stijl herbouwd — te volgen op de historische kaartlagen.",
        "en": "Capital of Zeeland and a VOC chamber city, heavily hit by bombing in 1940 and afterward rebuilt in its old style — traceable across the historical map layers.",
        "zh": "米德爾堡是澤蘭省的首府，也是荷蘭東印度公司（VOC）的分部所在城市，1940年遭受嚴重轟炸，戰後依原有風格重建——可在歷史地圖圖層中追溯這段歷程。",
    },
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
            color:#807C73; font-size:15px; margin-bottom:22px; }
  .stats { display:flex; flex-wrap:wrap; gap:8px 16px; font-size:12.5px; color:#565347; margin-bottom:22px; }
  .stats span b { color:#1F1D19; font-weight:500; }
  h2 { font-size:14px; margin-top:32px; color:#565347; letter-spacing:0.06em;
       border-top:1px solid #DAD7CC; padding-top:20px; text-transform:uppercase; font-weight:500; }
  p.desc { margin-top:10px; }
  .cards { display:grid; grid-template-columns:repeat(auto-fill,minmax(160px,1fr)); gap:14px; margin-top:14px; }
  .card { display:block; text-decoration:none; color:inherit; }
  .card img { width:100%; height:110px; object-fit:cover; display:block; border:1px solid #DAD7CC; }
  .card .cap { font-size:12px; margin-top:5px; color:#1F1D19; }
  .card .sub { font-size:10.5px; color:#807C73; }
  .cta { margin-top:36px; padding:16px 18px; background:#EAE8E2; border-left:3px solid #C15F3C; }
  .cta a { font-weight:500; }
  .foot { margin-top:48px; font-size:11.5px; color:#807C73; border-top:1px solid #DAD7CC; padding-top:16px; }
  .empty { font-size:13px; color:#807C73; font-style:italic; margin-top:10px; }
"""


def esc(s):
    return html.escape(s or "", quote=True)


def truncate(s, n):
    s = s or ""
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0]
    return cut.rstrip(",.;") + "…"


def loc(obj, fallback_key="en"):
    if not obj:
        return ""
    return obj.get(fallback_key) or obj.get("en") or obj.get("nl") or ""


def build_city_page(city_id, cname, blurb, years, landmarks, postcards):
    canonical = f"{SITE}/city/{city_id}.html"
    app_link = f"{SITE}/?city={city_id}"
    region = REGION_LABEL.get(cname["region"], {"zh": "", "en": ""})
    page_title = f"{cname['en']} — historical maps, landmarks & postcards | Oude-Kaart Wandeling"
    description = truncate(
        f"{blurb['en']} Historical topographic maps ({'–'.join(years) if len(years) > 1 else years[0]}) "
        f"overlaid on {cname['en']}, with {len(landmarks)} architecture-walk landmark(s) and "
        f"{len(postcards)} art postcard(s).",
        300,
    )

    landmark_cards = "\n".join(
        f'      <a class="card" href="../landmark/{esc(it["id"])}.html">\n'
        f'        <img src="{esc(it.get("img",""))}" alt="{esc(loc(it.get("name")))}" loading="lazy" />\n'
        f'        <div class="cap">{esc(loc(it.get("name")))}</div>\n'
        f'        <div class="sub">{esc(it.get("year",""))} · {esc(loc(it.get("style_label")))}</div>\n'
        f'      </a>'
        for it in landmarks
    )
    postcard_cards = "\n".join(
        f'      <a class="card" href="{esc(pc.get("sourceUrl",""))}" target="_blank" rel="noopener">\n'
        f'        <img src="{esc(pc.get("img",""))}" alt="{esc(loc(pc.get("title")))}" loading="lazy" />\n'
        f'        <div class="cap">{esc(loc(pc.get("title")))}</div>\n'
        f'        <div class="sub">{esc(loc(pc.get("artist")))}, {esc(pc.get("year",""))}</div>\n'
        f'      </a>'
        for pc in postcards
    )

    ld = {
        "@context": "https://schema.org",
        "@type": "City",
        "name": cname["en"],
        "alternateName": [cname["zh"]],
        "description": description,
        "url": canonical,
        "geo": {"@type": "GeoCoordinates", "latitude": CITIES[city_id]["lat"], "longitude": CITIES[city_id]["lng"]},
        "containedInPlace": {"@type": "Country", "name": "Netherlands"},
    }

    years_label = " · ".join(years)
    landmarks_section = (
        f'  <h2>Architecture-walk landmarks ({len(landmarks)})</h2>\n'
        f'  <div class="cards">\n{landmark_cards}\n  </div>'
        if landmarks else
        '  <h2>Architecture-walk landmarks</h2>\n  <p class="empty">None catalogued yet for this city.</p>'
    )
    postcards_section = (
        f'  <h2>Art postcards ({len(postcards)})</h2>\n'
        f'  <div class="cards">\n{postcard_cards}\n  </div>'
        if postcards else
        '  <h2>Art postcards</h2>\n  <p class="empty">None catalogued yet for this city.</p>'
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{esc(page_title)}</title>
<meta name="description" content="{esc(description)}" />
<link rel="canonical" href="{esc(canonical)}" />
<link rel="icon" type="image/svg+xml" href="../icons/icon.svg" />
<meta property="og:type" content="article" />
<meta property="og:title" content="{esc(cname['en'])} — Oude-Kaart Wandeling">
<meta property="og:description" content="{esc(description)}" />
<meta property="og:url" content="{esc(canonical)}" />
<meta name="twitter:card" content="summary" />
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@500;700&family=Noto+Sans+TC:wght@300;400;500&family=EB+Garamond:ital@1&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{PAGE_CSS}</style>
</head>
<body>
  <div class="crumb"><a href="../index.html">Oude-Kaart Wandeling</a> &rsaquo;
    <a href="index.html">Cities</a> &rsaquo;
    {esc(cname['en'])}</div>
  <h1>{esc(cname['en'])} <span style="color:#807C73;font-weight:300;">{esc(cname['zh'])}</span></h1>
  <div class="h1-sub">{esc(region['en'])} · the Netherlands</div>
  <div class="stats">
    <span>Historical maps: <b>{esc(years_label)} → today</b></span>
    <span>Landmarks: <b>{len(landmarks)}</b></span>
    <span>Postcards: <b>{len(postcards)}</b></span>
  </div>

  <h2>NL</h2>
  <p class="desc">{esc(blurb['nl'])}</p>
  <h2>EN</h2>
  <p class="desc">{esc(blurb['en'])}</p>
  <h2>中文</h2>
  <p class="desc">{esc(blurb['zh'])}</p>

{landmarks_section}

{postcards_section}

  <div class="cta">
    <a href="{esc(app_link)}">→ Explore {esc(cname['en'])} on the interactive historical map ↗</a>
  </div>

  <div class="foot">
    Part of <a href="../index.html">Oude-Kaart Wandeling / 荷蘭古地圖散策</a>, an open-data
    overlay of Dutch historical topographic maps (Kadaster/Topotijdreis, CC-BY 4.0) with a
    self-guided architecture walk and art-postcard trail across 21 Dutch cities.
    See the <a href="../about.html">colofon &amp; method</a> for citation details.
  </div>
</body>
</html>
"""


def build_index_page(rows_by_region, totals):
    sections = []
    for region_id in ("randstad", "noord", "zuid"):
        entries = rows_by_region.get(region_id)
        if not entries:
            continue
        label = REGION_LABEL[region_id]
        links = "\n".join(
            f'      <li><a href="{esc(cid)}.html">{esc(CITIES[cid]["en"])}</a>'
            f' <span style="color:#807C73;">{esc(CITIES[cid]["zh"])} — {n_land} landmark(s), {n_pc} postcard(s)</span></li>'
            for cid, n_land, n_pc in entries
        )
        sections.append(
            f'    <h2>{esc(label["en"])} <span style="color:#807C73;font-weight:300;">{esc(label["zh"])}</span></h2>\n'
            f'    <ul>\n{links}\n    </ul>'
        )
    body = "\n".join(sections)
    canonical = f"{SITE}/city/index.html"
    description = (
        f"Index of all {totals['cities']} Dutch cities covered by Oude-Kaart Wandeling — historical "
        f"topographic maps, {totals['landmarks']} architecture-walk landmarks, and {totals['postcards']} "
        f"art postcards, each with sourced history and licensed imagery."
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>City guides index | Oude-Kaart Wandeling</title>
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
  <div class="crumb"><a href="../index.html">Oude-Kaart Wandeling</a> &rsaquo; Cities</div>
  <h1>City guides</h1>
  <div class="h1-sub">{totals['cities']} Dutch cities, {totals['landmarks']} landmarks,
  {totals['postcards']} postcards — each city's historical maps, architecture walk and
  art-postcard trail on one page.</div>
{body}
  <div class="foot">
    Part of <a href="../index.html">Oude-Kaart Wandeling / 荷蘭古地圖散策</a>. See the
    <a href="../about.html">colofon &amp; method</a> for licensing and citation.
  </div>
</body>
</html>
"""


def main():
    landmarks = json.load(open(LANDMARKS_JSON, encoding="utf-8"))["items"]
    postcards = json.load(open(POSTCARDS_JSON, encoding="utf-8"))["items"]
    archives = json.load(open(MANIFEST_JSON, encoding="utf-8"))["archives"]

    landmarks_by_city = defaultdict(list)
    for it in landmarks:
        landmarks_by_city[it["city"]].append(it)
    postcards_by_city = defaultdict(list)
    for pc in postcards:
        postcards_by_city[pc["city"]].append(pc)
    years_by_city = defaultdict(set)
    for a in archives:
        years_by_city[a["city"]].add(a["service"])

    os.makedirs(OUT_DIR, exist_ok=True)
    rows_by_region = defaultdict(list)
    totals = {"cities": 0, "landmarks": 0, "postcards": 0}
    missing_maps = []

    for city_id, cname in CITIES.items():
        blurb = BLURBS[city_id]
        years = sorted(years_by_city.get(city_id, []))
        if not years:
            missing_maps.append(city_id)
            years = ["—"]
        cl = sorted(landmarks_by_city.get(city_id, []), key=lambda i: i.get("year", ""))
        cp = sorted(postcards_by_city.get(city_id, []), key=lambda i: i.get("year", ""))
        page = build_city_page(city_id, cname, blurb, years, cl, cp)
        with open(os.path.join(OUT_DIR, f"{city_id}.html"), "w", encoding="utf-8") as f:
            f.write(page)
        rows_by_region[cname["region"]].append((city_id, len(cl), len(cp)))
        totals["cities"] += 1
        totals["landmarks"] += len(cl)
        totals["postcards"] += len(cp)

    index_page = build_index_page(rows_by_region, totals)
    with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_page)

    print(f"Wrote {totals['cities']} city pages + index.html to {OUT_DIR}")
    if missing_maps:
        print(f"WARNING: no baked PMTiles archive for: {missing_maps}")


if __name__ == "__main__":
    main()
