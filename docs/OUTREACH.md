# Outreach drafts — institutional & media

> Owner sends these from a personal address. Adjust names before sending.
> Tone: concrete, modest, license-respecting. The app is the portfolio; the ask is small
> (a conversation / a retweet / a pointer), not a job in the first email.

## Targets (in priority order)

| # | Who | Why | Entry point |
|---|---|---|---|
| 1 | **Kadaster / Topotijdreis team** | We build directly on their CC-BY data; they love showcases and have retweeted community projects | info via kadaster.nl contact form; X @Het_Kadaster; PDOK forum geoforum.nl |
| 2 | **Amsterdam Time Machine (UvA/CREATE)** | Exactly this research space: historical geo-data + public interfaces | amsterdamtimemachine.nl → contact; CREATE Lab UvA |
| 3 | **TU Delft — Urbanism / GIS technology** | PhD positions in geo-visualization; strong Kadaster ties | staff pages, 3D geoinformation group |
| 4 | **VU Amsterdam CLUE+ / spatial humanities** | Historical GIS research institute | clue.vu.nl |
| 5 | **Netherlands eScience Center** | Funds research software engineering; fellowship calls | esciencecenter.nl |
| 6 | **Media: historiek.net, Tweakers, NRC/Volkskrant tech desks, NPO Kennis** | Dutch audiences love "toen/nu" map stories | tips@ addresses / X DMs |

## Email 1 — Kadaster/Topotijdreis (NL)

**Onderwerp:** Community-project op Topotijdreis-data: oude kaarten als wandel-app (CC-BY netjes vermeld)

Beste team Topotijdreis,

Als bedankje voor twee eeuwen prachtige open kaartdata: ik bouwde een gratis web-app
die uw historische kaarten (1815–2021) over de straten van nu legt, met een tijdschuif,
kunst-ansichtkaarten uit de collecties van het Rijksmuseum/Mauritshuis (publiek domein)
en architectuurwandelingen door alle 21 steden (32 rijksmonumenten, van gotische
kathedralen tot de Amsterdamse School en De Stijl), elk met een eigen bronpagina.

https://yunching0513.github.io/Netherlands-historical-map/

Technisch mogelijk interessant: de RD-tegels worden client-side naar Web Mercator
gereprojecteerd, en per stad/jaar zijn er offline PMTiles-archieven gebakken uit
TOPraster (CC-BY 4.0, attributie in beeld).

Twee vragen: (1) klopt de bronvermelding zo naar uw smaak? (2) mag ik dit project
ergens bij u laten zien — bv. het PDOK-forum of een demo-moment?

Met vriendelijke groet,
吳昀慶 Yunching Wu

## Email 2 — Amsterdam Time Machine / CLUE+ (EN)

**Subject:** Independent project: 200 years of Dutch topo maps as a mobile "time-walk" — looking for an academic home

Dear [name],

I'm an independent developer/researcher from Taiwan. Over the past months I built an
open web app that overlays the Kadaster Topotijdreis series (1815–2021) on today's
streets: time-slider, on-location "postcard" collection of public-domain Dutch art,
architecture walks across all 21 cities (32 verified landmarks, Gothic cathedrals to
Amsterdam School to De Stijl, each with its own citable page), trilingual
(NL/EN/zh-Hant), offline-first (pre-baked PMTiles reprojected from EPSG:28992).

https://yunching0513.github.io/Netherlands-historical-map/
Method & sources: see the colofon page. Code is public on GitHub.

Your work on [specific ATM/CLUE+ project] is exactly the conversation I'm hoping to
have: I'd like to develop this into doctoral research on public interfaces for
historical geo-data, and I'd value 30 minutes of your advice on whether it fits your
group — or where it might.

Best regards,
Yunching Wu

## Email 3 — media pitch (NL, short)

**Onderwerp:** Tip: app die 200 jaar oude kaarten over je wandeling legt (gratis, van een Taiwanese maker)

Hoi [naam],

Korte tip: een Taiwanese ontwikkelaar bouwde een gratis web-app waarmee je in
20 Nederlandse steden door twee eeuwen topografische kaarten schuift terwijl je
loopt — inclusief kunst-ansichtkaarten die "ontwikkelen" als je er fysiek langs
wandelt. Data: Kadaster/PDOK (open), Rijksmuseum (publiek domein).

https://yunching0513.github.io/Netherlands-historical-map/

Leuk voor een "toen/nu"-stuk? Screenshots/gifs lever ik graag aan.

Groet, Yunching

## Posting pack (owner presses "post")

- **Show HN:** "Show HN: Walk through 200 years of Dutch maps — client-side RD→Mercator reprojection, offline PMTiles" + 2-para comment on the reprojection trick.
- **r/thenetherlands (NL text!):** focus on "loop door je eigen straat in 1850/1900/1950"; ask which city to bake offline next (engagement hook).
- **r/MapPorn / r/dataisbeautiful:** lead with a then/now GIF (B-10), link in comment.
- Best posting windows: Tue–Thu 17:00–21:00 CET for NL subs; weekday morning US/PT for HN.

## Email 4 — heritage organisations / local history societies (NL, embed + map story)

Targets: Stadsarchief Rotterdam, Het Utrechts Archief, Zeeuws Archief (Middelburg), Regionaal Archief Nijmegen, Erfgoedvereniging Heemschut afdelingen, local historische verenigingen. One email per org, linking the matching map story.

Story ↔ archive pairing (send Email 4 with the matching URL, base `https://yunching0513.github.io/Netherlands-historical-map/stories/`):

| Archive / organisation | Story file(s) |
|---|---|
| Stadsarchief Rotterdam | `rotterdam-1940.html` |
| Stadsarchief Amsterdam | `amsterdam-plan-zuid.html`, `amsterdam-centraal.html` |
| Het Utrechts Archief | `utrecht-catharijnesingel.html` |
| Zeeuws Archief (Middelburg) | `middelburg-1940.html` |
| Regionaal Archief Nijmegen | `nijmegen-1944.html` |
| Haags Gemeentearchief | `denhaag-vredespaleis.html`, `denhaag-scheveningen.html` |
| Regionaal Historisch Centrum Eindhoven | `eindhoven-groot-eindhoven.html` |
| Groninger Archieven | `groningen-vestingwet.html` |
| Noord-Hollands Archief (Haarlem) | `haarlem-haarlemmermeer.html` |
| Regionaal Historisch Centrum Limburg (Maastricht) | `maastricht-vesting.html` |
| Stadsarchief Delft / TU Delft Library | `delft-tu-wijk.html` |
| Gelders Archief (Arnhem) / Airborne Museum Hartenstein | `arnhem-1944.html` |
| Erfgoed Leiden en Omstreken | `leiden-buskruitramp.html` |
| Gemeentearchief Hilversum / Museum Hilversum | `hilversum-dudok.html` |

> **Onderwerp:** Gratis interactieve kaart "toen en nu" voor [stad] — in te sluiten op uw website
>
> Beste [naam],
>
> Ik heb een open, gratis webkaart gemaakt die de historische topografische kaarten van het Kadaster (Topotijdreis, CC-BY 4.0) over de huidige kaart legt, met een schuifregelaar tussen toen en nu. Voor [stad] heb ik een kort verhaal geschreven met directe links naar de juiste kaartbeelden: [story-URL, bv. https://yunching0513.github.io/Netherlands-historical-map/stories/rotterdam-1940.html].
>
> U kunt de kaart ook met één regel code op uw eigen website insluiten (zie https://yunching0513.github.io/Netherlands-historical-map/press.html#embed); bronvermelding van het Kadaster zit er automatisch in. Het project is citeerbaar via DOI 10.5281/zenodo.21924251.
>
> Correcties of aanvullingen op het verhaal vanuit uw collectie zijn zeer welkom — ik vermeld uw organisatie dan graag als bron.
>
> Met vriendelijke groet,
> Yunching Wu
