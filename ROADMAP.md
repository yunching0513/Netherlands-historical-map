# ROADMAP — 荷蘭古地圖散策 · Old-Map Stroll

> **This file is the single source of truth for the autonomous AI development loop.**
> Each loop iteration: read this file → pick the top unblocked backlog item(s) →
> implement & verify → push to `claude/peaceful-gauss-axvnhn` → update statuses →
> append to the Loop Log. Never break the live app; never violate the licensing rules
> (only CC0 / Public Domain / CC-BY assets, always attributed).

## North-star goals (owner: Yunching Wu)

1. **5,000,000 pageviews by 2026-12-31.** (~27k/day sustained, or a few viral spikes
   plus a steady base. Realistically requires: Dutch media pickup + Reddit/HN front
   page moments + institutional retweets. The loop builds the product & assets;
   distribution moments need the owner to press "post/send".)
2. **Institutional support in NL** (Kadaster / university lab / heritage org) leading
   to a job or PhD position. Vehicle: the app as a demonstrated research artifact +
   outreach (see `docs/OUTREACH.md`).

## Operating metrics

- Pageviews: **NOT YET MEASURED** — blocked on analytics (see B-1). Until then the
  5M goal is unfalsifiable; this is the single most urgent user action.
- Secondary: PWA installs, share-card downloads, GitHub stars, inbound links.

## Backlog

Status: `todo` / `doing` / `done` / `BLOCKED(user)` — keep sorted by priority.

### P0 — measurement & distribution readiness
| id | item | status | notes |
|---|---|---|---|
| B-1 | Analytics: owner creates free GoatCounter account, gives site code; loop adds the script tag | **BLOCKED(user)** | Without this, no view counting. ~5 min task. |
| B-2 | OG image + twitter card + canonical + JSON-LD | done | 2026-07-03 |
| B-3 | sitemap.xml + robots.txt (25 URLs) | done | 2026-07-03 |
| B-4 | Launch-post copy pack: Reddit (r/thenetherlands, r/MapPorn, r/dataisbeautiful, r/Amsterdam), Show HN, Tweakers, X/Bluesky threads — NL + EN versions ready to paste | todo | owner posts; loop writes |
| B-5 | Per-city landing anchor content for SEO (short NL text per city rendered in a crawlable `<noscript>`/details block) | done | 2026-08-13 |

### P1 — product depth (share loops & retention)
| id | item | status | notes |
|---|---|---|---|
| B-10 | "Then/now" animated GIF/WebM export of the compare slider (highly shareable) | todo | canvas capture, ~few sec loop |
| B-11 | Bake remaining Randstad cities 1900 (leiden, delft, haarlem, gouda, dordrecht, amersfoort) as PMTiles z12–16 | todo | tools/bake_pmtiles.py ready; watch repo size (<1 GB) |
| B-12 | Amsterdam full era ladder: add 1815, 2021 archives | todo | completes the time-travel story offline |
| B-13 | More landmarks: Rotterdam (Kiefhoek, Sonneveld House), Utrecht (Werkbond), Hilversum (Zonnestraal, Dudok Raadhuis) | todo | verify coords + PD/CC images via Commons API |
| B-14 | More postcards: Van Gogh (Amsterdam/Otterlo), Frans Hals (Haarlem), Vermeer View of Delft (already?), Mondriaan (Den Haag) | todo | licensing rules in postcards/SOURCING.md |
| B-15 | Wikipedia deep links per landmark (nl/en/zh) | done | 2026-08-13, nl+en (all 10 landmarks verified via API); zh skipped — no zh articles exist for these niche buildings |
| B-16 | Walk recording (散策記錄) ported from taiwan-historical-maps: GPS trace + live stats + saved walks + GeoJSON export + 1080×1920 share card with map composite | done | 2026-07-03 |
| B-17 | Walk photos along route (camera + IndexedDB) + photo strip on share card, as in Taiwan app | todo | follow-up to B-16 |
| B-18 | City stamps/seals for completed walks (Taiwan app's 22-county seal wall → 20 NL cities) | todo | retention loop |
| B-19 | β 3D walk mode ported from taiwan-historical-maps/beta: perspective canvas ground, compass rotation, GPS scroll | done | 2026-07-08, verified in headless Chromium |
| B-19b | Vendor leaflet/proj4/pmtiles locally (drop unpkg CDN dependency) | done | 2026-07-08, needed for offline/app-store builds anyway |

### P2 — institutional / academic track
| id | item | status | notes |
|---|---|---|---|
| B-20 | `about.html` / colofon: method (RD→3857 reprojection, PMTiles), data sources & licenses, citation block (BibTeX), contact | done | 2026-08-13 |
| B-21 | Outreach emails NL/EN drafted (Kadaster, Amsterdam Time Machine/UvA, TU Delft, CLUE+ VU, Netherlands eScience Center) | done | see docs/OUTREACH.md — owner sends |
| B-22 | Submission targets: DH Benelux 2027, FOSS4G-NL, Stimuleringsfonds Creatieve Industrie open call | todo | loop drafts abstracts when B-20 done |
| B-23 | Zenodo DOI for the repo (citable artifact) | BLOCKED(user) | needs owner's ORCID/Zenodo login |

### P3 — app-store track (owner-driven, guides ready)
| id | item | status | notes |
|---|---|---|---|
| B-30 | TWA build + Play listing | BLOCKED(user) | tools/TWA_BUILD.md; needs keystore + $25 account |
| B-31 | iOS Capacitor build | BLOCKED(user) | same guide, needs macOS/Xcode |

## Loop protocol

1. `git pull` latest branch state first; work only on `claude/peaceful-gauss-axvnhn`.
2. Pick top unblocked item(s) sized to one session (1–3 items max, finish > start).
3. Verify before push: extract inline scripts (skip `application/ld+json`) → `node --check`;
   JSON files → parse check; if the app's behavior changed, sanity-check the affected flow.
4. Push with `git push -u origin claude/peaceful-gauss-axvnhn` (retry w/ backoff on network fail).
5. Update backlog statuses above + append Loop Log entry below (date, shipped, next, blockers).
6. Licensing: only CC0/PD/CC-BY, attribution required, verify via Wikimedia Commons
   `imageinfo` API or PDOK/Kadaster license pages. When in doubt, skip the asset.
7. Keep `pmtiles/` total under ~300 MB (GitHub soft limits; Pages serves fine below that).
8. Anything needing owner action → mark `BLOCKED(user)` with a one-line instruction;
   the loop's final chat message should list all BLOCKED items as the owner's to-do list.

## Loop Log

- **2026-08-13** — Shipped B-5, B-20, B-15 (SEO + academic-credibility cluster, per the
  "compounds toward the north-star goals" bias). B-5: added a `<noscript>` block right after
  `<body>` with an h1 + per-city (all 20) NL paragraphs describing each city's historical-map
  story — gives non-JS crawlers real indexable text without touching the live app's visual
  layout (body has `overflow:hidden`, everything else is absolutely positioned). B-20: new
  standalone `about.html` colofon (trilingual NL/EN/ZH) covering the RD(EPSG:28992)→3857
  canvas-reprojection method, the PMTiles baking pipeline, a data-sources/licences table, a
  BibTeX citation block, and contact info; linked from the in-app about-modal footer,
  credits.html, privacy.html, and sitemap.xml. B-15: added verified Wikipedia deep links
  (nl+en) to all 10 architecture landmarks in landmarks.json (new `wiki` field) and wired a
  new "Wikipedia ↗" link into the landmark lightbox (`lc-wiki`, keyed by current UI language
  with en/nl fallback). Every URL was confirmed to exist via the MediaWiki `action=query`
  API (batched, paced ~15s apart — the proxy's shared IP hits Wikipedia's rate limiter often)
  before being written; zh Wikipedia has no articles for these specific buildings so zh links
  were omitted rather than guessed. Verified: both inline `<script>` blocks pass
  `node --check`, all JSON files parse, about.html parses cleanly. Next up: B-4 launch copy
  pack, B-10 then/now GIF export, B-13/B-14 more landmarks/postcards. Blockers unchanged:
  B-1 analytics, B-23 Zenodo DOI, B-30/B-31 app-store builds — all need owner action (see
  end-of-run report).
- **2026-07-08** — B-19 shipped: β 3D walk mode (street-view stroll on the old map)
  ported from taiwan-historical-maps/beta. Single-canvas tile ground (base +
  historical via renderHistTileCanvas: PMTiles-first), rotateX(60°) perspective,
  compass rotateZ with absolute-heading discipline, GPS lerp + deadzones, fog band,
  dynamic plane sizing (iOS Safari camera-plane fix). Also vendored leaflet/proj4/
  pmtiles into vendor/ (B-19b) — no more unpkg dependency. Verified in headless
  Chromium with mocked GPS at Dam square: ANNO 1900 ground renders from local
  PMTiles, zero network. Fixed [hidden] vs display:flex bug on rec readout.
- **2026-07-03 (2)** — B-16 shipped: walk recording ported from the owner's
  taiwan-historical-maps (GPS trace w/ noise filter >80m acc & <3m step, wake lock,
  live dist/time/points, saved walks in nlOldMaps.traces, replay on map, GeoJSON
  export, delete, 1080×1920 share card compositing base+historical tiles with the
  vermilion route). Follow-ups queued: B-17 photos, B-18 city seals.
- **2026-07-03** — Loop bootstrapped. Shipped: og:image (baked-map postcard style),
  twitter cards, canonical, JSON-LD, sitemap.xml (25 URLs), robots.txt, this roadmap,
  outreach drafts (docs/OUTREACH.md). Next: B-4 launch copy pack, B-5 SEO anchors,
  B-10 GIF export. Blockers for owner: B-1 analytics (urgent), B-23, B-30/31.
