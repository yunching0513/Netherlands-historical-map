# Submission targets — drafts ready to adapt & send

> B-22. These are **drafts**, not final copy — application windows for all three targets
> below are either closed or not yet announced as of 2026-08-24 (checked live). Nothing here
> needs to be sent today; the point is to have strong copy ready the moment a window opens,
> instead of writing it under deadline pressure. Re-verify the live CFP/call page for exact
> word limits and dates before submitting — conference/fund sites change these between cycles.

## Reusable one-paragraph pitch (EN)

Old Map Stroll (荷蘭古地圖散策) is a free, open-source web app that overlays two centuries
of Dutch topographic maps (Kadaster Topotijdreis, 1815–2021, CC-BY 4.0) onto today's streets
across 20 cities, with a time slider, GPS-triggered "postcard" collection of public-domain
Dutch art tied to real locations, architecture walking routes (Amsterdam School, De Stijl),
and offline-first delivery via client-side RD(EPSG:28992)→Web Mercator reprojection baked into
PMTiles archives. Built solo, trilingual (NL/EN/zh-Hant), MIT-licensed code, citable via Zenodo
DOI `10.5281/zenodo.21924251`. Live: https://yunching0513.github.io/Netherlands-historical-map/
— method & sources: the in-app colofon (`about.html`).

## 1. DH Benelux (digital humanities conference, Benelux region)

**Status checked 2026-08-24:** no 2027 edition announced yet (dhbenelux.org's own front page is
stale, still showing 2023 news at fetch time); the conference has run yearly, most recently
2025 at VU Amsterdam (3–6 June). Watch dhbenelux.org and journal.dhbenelux.org for the 2027 CFP
— historically DH Benelux CFPs open ~5–6 months before the June conference, so expect one
around Q4 2026 or Q1 2027.

**Track fit:** short paper / demo, not a long research paper — this is a working tool + a
methods contribution (client-side historical-CRS reprojection, PMTiles-based serverless
delivery of raster map archives), not a completed research study with results to report. DH
conferences standardly accept long papers (~750–1500 words), short papers (~300–750 words),
and posters/demos (~300 words) — confirm exact counts against the live CFP; they vary by year.

**Draft short-paper / demo abstract (EN, ~420 words — trim to fit the actual limit):**

> **Title: Old Map Stroll — a client-side pipeline for serving two centuries of historical
> topographic maps as an offline, location-triggered walking app**
>
> We present an open-source, single-page web application that lets users compare Dutch
> topographic maps from six historical epochs (1815, 1850, 1900, 1925, 1975, 2021, sourced from
> Kadaster's Topotijdreis series, CC-BY 4.0) against the present-day street grid, across 20
> cities, on a mobile device with no server backend and no network connection required after an
> initial download.
>
> Two technical contributions may interest a DH/geohumanities audience. First, a **client-side
> reprojection pipeline**: Topotijdreis tiles are natively served in the Dutch national grid
> (RD, EPSG:28992, a stereographic projection tuned for the Netherlands' shape), which is
> incompatible with the Web Mercator (EPSG:3857) tiling scheme every mainstream web map library
> assumes. Rather than running a tile-reprojection server, we reproject on a `<canvas>` at
> request time in the browser (and, for offline use, ahead-of-time into pre-baked archives),
> using the same coordinate math either way — this keeps the whole system static-hostable
> (served today from GitHub Pages) with no PostGIS/Mapnik/tile-server infrastructure, which we
> think is a reproducible pattern for other small historical-map projects working with
> non-standard national grids (many European national mapping agencies use a country-specific
> CRS for their historical raster series).
>
> Second, a **PMTiles-based offline distribution model**: baked reprojected tiles are packed
> into single-file PMTiles archives (one HTTP range-request-addressable file per city/era),
> letting the whole "1900 Amsterdam" layer — megabytes, not gigabytes — be cached for
> zero-network walking use, addressing a real access barrier for public-facing historical-GIS
> tools (unreliable mobile data while actually walking a historical route).
>
> On top of this base layer sit two humanities-facing features: a GPS-triggered collection game
> that surfaces public-domain Dutch artworks (Rijksmuseum/Mauritshuis collections, verified
> Public Domain via the Wikimedia Commons `imageinfo` API before use) tied to the real location
> they depict or were made near, and curated architecture-history walking routes (Amsterdam
> School, De Stijl) with sourced landmark information and Wikipedia deep links.
>
> We'll demo the live app, walk through the reprojection/baking pipeline (open-sourced as
> `tools/bake_pmtiles.py`), and discuss what public-facing, offline-first delivery of historical
> map data could look like for other national contexts and other digital-humanities projects
> constrained to static hosting.
>
> *Keywords: historical GIS, web cartography, coordinate reference systems, offline-first,
> public history, cultural heritage, open data*

**Before sending:** trim to the live CFP's actual word limit; add author affiliation (owner
currently independent — DH Benelux accepts independent/non-affiliated submissions, common in
the DH community, but double check the live CFP for any registration-fee waiver process for
unaffiliated presenters).

## 2. FOSS4G-NL (Dutch open-source GIS conference, run by OSGeo.nl)

**Status checked 2026-08-24:** FOSS4G-NL 2026 (8–9 July, Groningen) already happened — its CFP
on pretalx closed before this check. No 2027 edition is announced yet. Watch osgeo.nl and
pretalx.com/foss4gnl for the next CFP; FOSS4G-NL has run annually, so expect a mid-2027 edition
with a CFP opening several months prior (spring, going by the 2026 pattern).

**Track fit:** standard talk (OSGeo.nl's own framing explicitly welcomes "smaller practical
examples, creative hacks or surprising workflows," not just production GIS deployments) —
this project is exactly that: PMTiles + proj4 + Leaflet solving a real non-standard-CRS
distribution problem, built and shipped solo.

**Draft talk proposal (NL, ~180 words — this audience is Dutch-speaking OSGeo.nl practitioners):**

> **Titel: Twee eeuwen Kadaster-kaarten offline op je telefoon: RD→Web Mercator on the fly, en
> waarom PMTiles de aangewezen distributievorm is**
>
> Topotijdreis levert prachtige CC-BY historische kaarten — maar in RD (EPSG:28992), niet in de
> Web Mercator-tegelstructuur die Leaflet/MapLibre verwachten. Voor "Old Map Stroll", een gratis
> wandel-app die 1815–2021 over 20 Nederlandse steden legt, loste ik dit client-side op:
> herprojectie op een `<canvas>`, zowel realtime in de browser als vooraf gebakken in PMTiles-
> archieven voor offline gebruik tijdens het wandelen zelf. Geen tile-server, geen PostGIS —
> alles static hostable (GitHub Pages).
>
> In deze talk: de proj4-wiskunde achter de herprojectie, hoe PMTiles' range-request-model een
> hele stad-per-jaar-laag in één bestand van een paar MB perst, en de afwegingen tussen
> realtime herprojectie (altijd actueel, netwerk nodig) versus vooraf bakken (offline, statisch).
> Code en bake-tool (`tools/bake_pmtiles.py`) zijn open source.
>
> *Voor: GIS-ontwikkelaars die met niet-standaard CRS'en werken, of interesse hebben in
> offline-first kaart-apps.*

**Before sending:** confirm talk-length slot on the live CFP (20 min is typical for this event
based on past editions but wasn't independently confirmed here) and adjust the abstract's
depth to match.

## 3. Stimuleringsfonds Creatieve Industrie — Regeling Digitale cultuur

**Status checked 2026-08-24:** this is a **grant**, not a paper submission — funds €10,000–
€25,000 for a solo applicant (€10k–€50k with partners), minimum 20% cofinancing, two-phase
process (short phase-I pitch, then a full phase-II project plan if invited). Both 2026 rounds
(26 Feb–4 Mar, 12–19 Aug) are already closed; the fund's page didn't list 2027 dates yet — watch
stimuleringsfonds.nl/subsidies/regeling-digitale-cultuur for the next round announcement
(historically announced a few weeks ahead of each opening).

**⚠️ Eligibility gate the loop cannot verify — flagging for the owner, not drafting around it:**
phase-I materials require a CV and **Chamber of Commerce (KVK) registration**. This implies the
applicant needs a registered presence in the Netherlands (as a freelancer/ZZP'er or via an
organization) — the fund's own page doesn't spell out whether a non-resident/foreign national
can apply directly. **Before investing time in a full phase-II plan, the owner should confirm
with the fund (or a Dutch academic/institutional partner willing to be the formal applicant)
whether this route is open at all without Dutch KVK registration** — this is exactly the kind
of institutional-partner question B-21's outreach emails are already trying to open a door to;
a partner institution (e.g. an interested UvA/TU Delft group) could also apply as lead with the
owner as the named maker/researcher.

**Draft phase-I pitch (NL, short-pitch format — adapt to whatever the live phase-I form asks):**

> **Werktitel: Old Map Stroll — twee eeuwen Nederlandse topografie als locatief digitaal
> erfgoedwerk**
>
> Old Map Stroll is een bestaande, gratis, open-source web-app (20 steden, 1815–2021, Kadaster
> Topotijdreis CC-BY 4.0) die historische kaarten fysiek aan de wandelaar koppelt: een
> tijdschuif over de eigen locatie, een GPS-gestuurde verzameling publiek-domein kunstwerken op
> hun originele plek, en architectuurwandelingen. Het project bestaat al en trekt organisch
> gebruik; deze aanvraag is niet voor het bouwen van een MVP, maar voor het **verdiepen** ervan
> tot een volwaardig digitaal-cultureel werk: (1) professioneel ontworpen visuele identiteit en
> UX-polish voorbij de huidige solo-ontwikkelaar-esthetiek, (2) een uitgebreide
> foto-/verhalenlaag per wandelroute (bewonersherinneringen, mondelinge geschiedenis, gekoppeld
> aan locaties — vergelijkbaar met, maar aanvullend op, de bestaande kunstwerk-laag), (3)
> toegankelijkheidsaudit en -verbetering (screenreader-ondersteuning voor de kaartinteractie is
> op dit moment beperkt), en (4) een evaluatietraject met een erfgoedinstelling of gemeente over
> gebruik in een educatieve/toeristische context.
>
> Begroting (indicatie, 20%+ cofinanciering eigen bijdrage): €15.000–€20.000 solo, of tot
> €50.000 in samenwerking met een culturele/academische partner (zie hieronder).
>
> *Let op: dit onderdeel van het fonds vereist KVK-registratie — zie de blocker-notitie
> hierboven. Deze pitch is gereed zodra dat is opgelost, of om samen met een NL-partner in te
> dienen.*

**Before sending:** this is the most speculative of the three — resolve the KVK/residency
question first (a five-minute email to the fund, or ask a prospective academic partner from
B-21's outreach list whether they'd co-apply), then flesh out the phase-I form's actual
required fields (this draft assumes a free-text pitch; the real form may be structured
differently).

## Summary for the owner

All three drafts are ready to copy-paste-adapt. None can be submitted *today* — DH Benelux 2027
and FOSS4G-NL 2027 CFPs aren't open yet (watch the two sites), and both 2026 Digitale cultuur
rounds already closed. The one genuine action item, if the owner wants to pursue the grant
route seriously: **check whether Digitale cultuur is reachable without Dutch KVK
registration**, since that gates whether the phase-I pitch above is usable solo or needs a
Dutch partner institution first.
