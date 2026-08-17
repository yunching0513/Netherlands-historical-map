# Launch copy pack — ready to paste

> Loop writes; owner posts (and adjusts tone/handle mentions to taste before sending).
> Live app: https://yunching0513.github.io/Netherlands-historical-map/
> Suggested screenshot/GIF: the compare-slider on Amsterdam Dam square, 1900 vs today,
> or the postcard lightbox with a Van Gogh piece. A short then/now clip (see B-10) will
> outperform a static screenshot once it exists — until then, the slider mid-drag is the
> single best still frame.

General guidance for the owner when posting:
- Post from a personal account, not a throwaway — Reddit/HN both penalize link-only
  accounts. Have a comment ready in the thread (see "first comment" blocks below).
- Space postings out over a few days rather than all at once; cross-posting the same
  link everywhere same-day reads as spam to some mod teams (especially r/thenetherlands).
- Check each subreddit's self-promotion rule before posting — some want a 9:1 ratio of
  participation to self-posts. If in doubt, comment in a few threads first.

---

## Reddit — r/thenetherlands (NL audience, Dutch-language map nerds)

**Title (NL):** Ik bouwde een gratis app die 200 jaar Nederlandse topografische kaarten (Kadaster) over je huidige locatie legt

**Body (NL):**

Hoi allemaal,

De afgelopen maanden heb ik in mijn vrije tijd een web-app gebouwd die de historische
TOPraster-kaarten van het Kadaster (1815 tot nu) laadt op basis van je locatie, met een
schuifbalk om tussen kaartjaren te bladeren. Werkt offline voor 20 steden (Amsterdam,
Rotterdam, Den Haag, Utrecht, Leiden, Delft, Haarlem, Gouda, Dordrecht, Amersfoort,
Groningen, Leeuwarden, Zwolle, Deventer, Arnhem, Nijmegen, 's-Hertogenbosch, Eindhoven,
Maastricht, Middelburg) — handig als je onderweg bent en slechte ontvangst hebt.

Een paar dingen erin:
- Tijdschuif tussen kaartlagen per stad (verschilt per stad hoeveel jaren er zijn)
- Kunstansichtkaarten uit publiek-domein collecties (Rijksmuseum e.a.) die op de
  bijbehorende locatie "verschijnen" als je er wandelt
- Architectuurwandelingen: Amsterdamse School-gebouwen met foto + korte geschiedenis
- Wandelregistratie met GPS-track en een deelbare kaart aan het eind
- Alles gratis, geen account, werkt in de browser

https://yunching0513.github.io/Netherlands-historical-map/

Databron is netjes vermeld: Kadaster Topotijdreis/TOPraster (CC-BY 4.0). Ik ben zelf
geen Nederlander (kom uit Taiwan) maar ben gefascineerd door hoe goed jullie historische
kaartdata open beschikbaar is — in veel landen bestaat zoiets niet eens. Feedback,
bugs, en suggesties voor welke steden ik als volgende moet bakken zijn welkom.

**First comment (NL, post immediately after submitting):**

Techniek voor de nieuwsgierigen: de RD-tegels (EPSG:28992) worden client-side
gereprojecteerd naar Web Mercator, en per stad zijn er PMTiles-archieven gebakken zodat
alles ook zonder netwerk werkt. Colofon met methode en broncodelink staat onderaan de
app.

---

## Reddit — r/MapPorn (visual, international, no need for Dutch)

**Title (EN):** I built a free app that layers 200 years of Dutch topographic maps (1815–today) over your real location, GPS-synced

**Body (EN):**

https://yunching0513.github.io/Netherlands-historical-map/

Free web app, no login. Pick any of 20 Dutch cities, drag a slider through historical
topographic surveys (Kadaster's open TOPraster series, 1815 → present), and — if you're
physically there — it tracks your GPS so the old map moves with you as you walk.

Also has: public-domain art postcards that "appear" when you're near the real-world
spot they were painted, Amsterdam School architecture walks with photos, and offline
GPS walk recording with a shareable route card at the end.

Data: Kadaster Topotijdreis/TOPraster (CC-BY 4.0), Wikimedia Commons for imagery, all
attributed on the about/colofon page. Method: RD (EPSG:28992) tiles reprojected
client-side to Web Mercator, pre-baked PMTiles for offline use. Source on GitHub.

**First comment (EN):**

If you want to try it without traveling to the Netherlands, most cities have a
"free-look" mode — you don't need to be standing there, GPS-follow is optional. Amsterdam
has the deepest map coverage if you want to see the biggest before/after (Dam square
especially).

---

## Reddit — r/dataisbeautiful (data/viz framing)

**Title (EN):** [OC] 200 years of Dutch topographic surveys, reprojected and overlaid on today's streets — an interactive time-slider map

**Body (EN):**

Source: Kadaster (Dutch national land registry/cadastre) Topotijdreis series, CC-BY 4.0.
Tool: a web app I built that reprojects the historical RD (EPSG:28992) raster tiles to
Web Mercator client-side and renders them as a draggable time-slider over a live Leaflet
basemap, city by city (20 Dutch cities covered so far, more coming).

https://yunching0513.github.io/Netherlands-historical-map/

Full methodology, data sources and licenses: [about/colofon page linked in-app]. Code is
public. Not a static visualization — it's meant to be used standing in the actual
street, GPS-synced, so the "data" is also a walking tour.

**First comment (EN):**

Happy to answer questions about the reprojection pipeline — RD (Dutch national grid) to
EPSG:3857 isn't a simple affine transform since it's a very local, high-precision datum
(originally surveyed to a few cm accuracy), so I get it as close as I can with proj4 and
bake the results into PMTiles per city/year rather than reprojecting live for every user.

---

## Reddit — r/Amsterdam (city-specific, casual tone)

**Title (EN):** Made a free app to see what your street looked like 100+ years ago, GPS-synced as you walk

**Body (EN):**

https://yunching0513.github.io/Netherlands-historical-map/

Walk around Amsterdam and drag a slider to see the historical Kadaster maps (going back
to 1815) fade in over the current streets, synced to your real GPS position. Also has
old art postcards that pop up when you're near where they were painted, and a
self-guided Amsterdam School architecture walk (Het Schip, De Dageraad, Scheepvaarthuis,
etc.) with photos and short histories.

Free, no account, works offline once loaded (good for the metro). Data is Kadaster
Topotijdreis (open license, credited in-app). If you try the architecture walk and
know a building that should be on it, let me know — happy to add more.

---

## Hacker News — Show HN

**Title:** Show HN: 200 years of Dutch topographic maps, GPS-synced to your real location

**Body (post as a top-level comment on the Show HN submission, per HN convention):**

Hi HN — I built this over the past couple months. It's a single-page web app
(Leaflet + proj4 + PMTiles, no backend, no build step beyond baking tiles) that overlays
Dutch national cadastre (Kadaster) historical topographic surveys — 1815 through today —
on the streets you're actually standing on, with a time-slider between years.

https://yunching0513.github.io/Netherlands-historical-map/

Technical bits that might interest this crowd:
- The historical tiles are in RD (EPSG:28992), the Dutch national grid; I reproject
  client-side with proj4 and then bake per-city, per-year archives into PMTiles so the
  app works fully offline once a city is loaded (no server, static hosting on GitHub
  Pages).
- 20 Dutch cities so far, each with a different span of surveyed years depending on what
  Kadaster has digitized.
- A couple of "extra" layers on top of the core map: public-domain art postcards
  (Rijksmuseum etc.) geolocated to where the scene was painted, so they surface as you
  physically approach the spot; and a self-guided Amsterdam School architecture walk with
  photos sourced/licensed from Wikimedia Commons.
- GPS walk recording with noise filtering (drops readings with >80m accuracy or <3m
  step), local storage of past walks, GeoJSON export, and a composited share-card image.
- No account, no tracking beyond a cookieless pageview counter (GoatCounter). Trilingual
  (NL/EN/zh-Hant) since I'm documenting the build process for a non-Dutch audience too.
- Source, methodology, and full data/license table: linked from the in-app "about" page.

I'm not Dutch (I'm from Taiwan) — this started as a personal fascination with how much
historical geo-data the Netherlands has made genuinely open, and turned into wanting to
build something that makes it walkable rather than just downloadable. Feedback on the
reprojection accuracy, UX, or which cities to bake next very welcome.

---

## Tweakers.net (NL tech community — post as a forum topic or via a tip to the tips@ desk)

**Title (NL):** Oude Kadaster-kaarten (1815–nu) als GPS-gesynchroniseerde wandel-app

**Body (NL):**

Voor de kaart-nerds hier: een gratis, open-source web-app die de TOPraster-reeks van het
Kadaster (CC-BY 4.0) client-side reprojecteert van RD (EPSG:28992) naar Web Mercator en
als tijdschuif over de huidige straten legt, gesynchroniseerd met je live GPS-positie.

https://yunching0513.github.io/Netherlands-historical-map/

Techniek: Leaflet + proj4 + PMTiles, geen backend — alles is statisch gehost (GitHub
Pages) en per stad/jaar vooraf gebakken tot offline-werkende PMTiles-archieven. 20 steden
tot nu toe. Broncode en methodiek (incl. hoe de RD-reprojectie is aangepakt) staan
gelinkt vanuit de "about"-pagina in de app.

Ben benieuwd of de reprojectie-nauwkeurigheid klopt voor mensen die de originele kaarten
kennen — feedback welkom, ook over performance op oudere toestellen.

---

## X / Twitter thread (EN, 4 tweets)

**1/**
Built a free app that layers 200 years of Dutch topographic maps over the street
you're actually standing on — synced to your GPS, offline-capable.

https://yunching0513.github.io/Netherlands-historical-map/

🧵

**2/**
Data: @Het_Kadaster's open Topotijdreis series (1815→today), CC-BY 4.0, reprojected
client-side from the Dutch national grid (RD/EPSG:28992) to Web Mercator, then baked
per-city into offline PMTiles archives.

20 cities covered so far — Amsterdam has the deepest year range.

**3/**
Extra layers: public-domain art postcards that "develop" as you walk toward the real
spot they were painted, and a self-guided Amsterdam School architecture walk with
photos + short histories, sourced/licensed via Wikimedia Commons.

**4/**
No account, no ads, cookieless analytics only. Free and open — methodology + full
data/license table on the in-app "about" page, source on GitHub.

Would love feedback from anyone who knows these maps well: does the overlay line up
where you'd expect?

---

## Bluesky (EN, single post — shorter format, no thread needed)

Built a free app that overlays 200 years of Dutch Kadaster topographic maps (1815→today)
on the street you're standing on, GPS-synced, works offline. 20 cities, CC-BY data,
fully attributed, open source.

https://yunching0513.github.io/Netherlands-historical-map/

---

## Bluesky (NL, single post)

Gratis app die 200 jaar Nederlandse Kadaster-kaarten (1815–nu) over je huidige locatie
legt, GPS-gesynchroniseerd, werkt offline. 20 steden, CC-BY data netjes vermeld,
open source.

https://yunching0513.github.io/Netherlands-historical-map/
