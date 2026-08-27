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

- Pageviews: **instrumented 2026-08-13** via GoatCounter (site `yunching`, script tag live
  in index.html). No historical data yet — check https://yunching.goatcounter.com for counts
  going forward; update this section once there's a real number to report against the 5M goal.
- Secondary: PWA installs, share-card downloads, GitHub stars, inbound links.

## Backlog

Status: `todo` / `doing` / `done` / `BLOCKED(user)` — keep sorted by priority.

### P0 — measurement & distribution readiness
| id | item | status | notes |
|---|---|---|---|
| B-1 | Analytics: owner creates free GoatCounter account, gives site code; loop adds the script tag | done | 2026-08-13 — owner gave site code `yunching`; script tag added to index.html `<head>`; privacy.html updated to disclose it |
| B-2 | OG image + twitter card + canonical + JSON-LD | done | 2026-07-03 |
| B-3 | sitemap.xml + robots.txt (25 URLs) | done | 2026-07-03 |
| B-4 | Launch-post copy pack: Reddit (r/thenetherlands, r/MapPorn, r/dataisbeautiful, r/Amsterdam), Show HN, Tweakers, X/Bluesky threads — NL + EN versions ready to paste | done | 2026-08-17 — see `docs/LAUNCH_COPY.md`; owner posts |
| B-5 | Per-city landing anchor content for SEO (short NL text per city rendered in a crawlable `<noscript>`/details block) | done | 2026-08-13 |

### P1 — product depth (share loops & retention)
| id | item | status | notes |
|---|---|---|---|
| B-10 | "Then/now" animated GIF/WebM export of the compare slider (highly shareable) | done | 2026-08-20 — shipped as WebM/MP4 (MediaRecorder + canvas.captureStream), see Loop Log |
| B-11 | Bake remaining Randstad cities 1900 (leiden, delft, haarlem, gouda, dordrecht, amersfoort) as PMTiles z12–16 | done | 2026-08-27 — all 6 baked z12–17, see Loop Log |
| B-12 | Amsterdam full era ladder: add 1815, 2021 archives | todo | completes the time-travel story offline |
| B-13 | More landmarks: Rotterdam (Kiefhoek, Sonneveld House), Utrecht (Werkbond), Hilversum (Zonnestraal, Dudok Raadhuis) | doing | 2026-08-17 — Rotterdam pair shipped (Kiefhoek, Sonneveld House), both Public Domain via Commons API. Hilversum isn't in the app's `CITIES` list yet (no tiles baked), so Zonnestraal/Dudok Raadhuis need Hilversum added as a city first — out of scope for a landmarks-only pass. Utrecht "Werkbond" target unclear (no canonical building of that name found); needs the owner to confirm which building was meant, or drop it. |
| B-14 | More postcards: Van Gogh (Amsterdam/Otterlo), Frans Hals (Haarlem), Vermeer View of Delft (already?), Mondriaan (Den Haag) | doing | 2026-08-27 — shipped 2 more verified: Jan van Goyen "View of Nijmegen" (c.1649, depicts the city itself) and Balthasar van der Ast "Fruit Still Life with Shells and Tulip" (c.1620, born in Middelburg). 6 zero-coverage cities remain (groningen, leeuwarden, deventer, arnhem, maastricht, gouda) — see Loop Log. |
| B-15 | Wikipedia deep links per landmark (nl/en/zh) | done | 2026-08-13, nl+en (all 10 landmarks verified via API); zh skipped — no zh articles exist for these niche buildings |
| B-16 | Walk recording (散策記錄) ported from taiwan-historical-maps: GPS trace + live stats + saved walks + GeoJSON export + 1080×1920 share card with map composite | done | 2026-07-03 |
| B-17 | Walk photos along route (camera + IndexedDB) + photo strip on share card, as in Taiwan app | todo | follow-up to B-16 |
| B-18 | City stamps/seals for completed walks (Taiwan app's 22-county seal wall → 20 NL cities) | done | 2026-08-24 — see Loop Log |
| B-19 | β 3D walk mode ported from taiwan-historical-maps/beta: perspective canvas ground, compass rotation, GPS scroll | done | 2026-07-08, verified in headless Chromium |
| B-19b | Vendor leaflet/proj4/pmtiles locally (drop unpkg CDN dependency) | done | 2026-07-08, needed for offline/app-store builds anyway |

### P2 — institutional / academic track
| id | item | status | notes |
|---|---|---|---|
| B-20 | `about.html` / colofon: method (RD→3857 reprojection, PMTiles), data sources & licenses, citation block (BibTeX), contact | done | 2026-08-13 |
| B-21 | Outreach emails NL/EN drafted (Kadaster, Amsterdam Time Machine/UvA, TU Delft, CLUE+ VU, Netherlands eScience Center) | done | see docs/OUTREACH.md — owner sends |
| B-22 | Submission targets: DH Benelux 2027, FOSS4G-NL, Stimuleringsfonds Creatieve Industrie open call | done | 2026-08-24 — see `docs/SUBMISSIONS.md` and Loop Log |
| B-23 | Zenodo DOI for the repo (citable artifact) | done | 2026-08-13 — published. Concept DOI (always latest) `10.5281/zenodo.21924251`, v1 DOI `10.5281/zenodo.21924252`. Both verified resolving. Wired into about.html (3 languages) + README badge + BibTeX. Also added a MIT LICENSE file with a third-party data carve-out, which the deposit needed. |

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

- **2026-08-27** — Shipped B-11 (fully closes the row) and made further progress on B-14, both
  flagged "next up" for two loops running. B-11: set up a fresh `.venv-pmtiles` (pyproj/pillow/
  pmtiles/requests) and baked all 6 remaining Randstad cities — leiden, delft, haarlem, gouda,
  dordrecht, amersfoort — at 1900/z12–17/webp-q82, matching the exact parameters (half-lat
  0.018, half-lng 0.028) already used for amsterdam/rotterdam/denhaag/utrecht so archive
  coverage lines up with each city's default view. Every single planned tile in every archive
  rendered non-empty (no gaps in source coverage): leiden 672/672, delft 650/650, haarlem
  673/673, gouda 672/672, dordrecht 633/633, amersfoort 683/683. `pmtiles/manifest.json` now
  lists 13 archives; total `pmtiles/` size grew from 42 MB to 75 MB, comfortably under the
  ~300 MB ceiling. Verified two ways: (1) a headless-Chromium pass against the real app on a
  local static server confirmed the manifest loads (13 archives), the new files are reachable,
  and at least one tile request for Leiden/1900 hit the local `.pmtiles` archive successfully
  with no errors specific to it (further attempts to force more tile churn via pan/zoom/year-
  scrub hit this *sandbox's* known browser-cache/timing quirks rather than any app bug — same
  category of sandbox-only flakiness flagged in the 2026-08-20 and 2026-08-24 entries); (2) a
  direct Python read of each new archive via `pmtiles.reader` decoded a real, non-blank WEBP
  tile both at the archive's center zoom (z12) and at the app's default city zoom (z15) for all
  6 files — the strongest and most sandbox-independent confirmation that the bakes are correct.
  B-14: continued the "8 zero-coverage cities" gap flagged 2026-08-20/08-24, this time with
  actual research budget instead of guessing. Found and verified two solid, well-documented
  connections rather than forcing weak ones: Jan van Goyen's *View of Nijmegen* (c. 1649,
  Gemäldegalerie Berlin) — a direct depiction of the city itself (Nijmegen, the Netherlands'
  oldest city, seen across the Waal with the Valkhof castle), the same "painting *of* the city"
  pattern as Delft/Vermeer rather than a birthplace tie; and Balthasar van der Ast's *Fruit
  Still Life with Shells and Tulip* (c. 1620, Mauritshuis) — van der Ast was born in Middelburg,
  a VOC chamber city and the literal port of entry for the exotic shells/tulips/fruit that
  define his still lifes, a genuinely documented city↔artist connection (not the "guessed and
  got it wrong" risk flagged for Utrecht's "Werkbond" in B-13). Both verified Public Domain via
  the Wikimedia Commons `imageinfo` API (`Copyrighted: False`, `LicenseShortName: Public
  domain`) before writing copy; both artists died in the 1650s, well past any copyright term.
  Hit persistent `429`s from `upload.wikimedia.org` on first attempts to fetch the Van der Ast
  thumbnail (not a licensing issue — a transient rate-limit on that specific image's CDN shard
  via this sandbox's shared-IP proxy) — confirmed by retrying with backoff until it returned
  200, and cross-checking that other thumbnails resolved fine throughout, so this was correctly
  treated as "retry", not "file is broken" or "give up". Wrote full zh/en/nl narrative `desc`
  blocks for both (matching the Mondriaan/Amersfoort entry's house style: connect the artist to
  the city with real, specific facts, not generic Wikipedia summary). Left 6 cities alone
  (groningen, leeuwarden, deventer, arnhem, maastricht, gouda) — spent real search budget on
  Groningen (Cornelis Springer did paint Groningen townscapes but no specific, well-documented
  Commons-verified file surfaced) and Maastricht (no Golden-Age-caliber painting of the city
  found) rather than forcing a weak match; Leeuwarden's most famous native artist is M.C.
  Escher, whose work is firmly still in copyright (died 1972) and explicitly out of scope.
  Verified before push: all 4 JSON files in the repo parse (postcards now 87 items, up from 85;
  pmtiles manifest now 13 archives), both inline `<script>` blocks pass `node --check` (index.html
  itself wasn't touched this pass — B-11 is pure asset addition, B-14 is pure JSON addition), and
  a headless-Chromium pass confirmed both new postcards render on their city's Cards tab with the
  artist name visible and zero console errors. Next up: B-14 remaining 6 cities (worth another
  research pass, ideally with the owner's own knowledge of any city↔artist ties this loop
  missed), B-17 walk photos (natural follow-up to B-18's stamp wall, but camera+IndexedDB is
  hard to verify headlessly — worth flagging to the owner as a manual-test item once shipped),
  B-12 Amsterdam era ladder (1815/2021). Blockers unchanged — see end-of-run report.
- **2026-08-24** — Shipped B-18 (retention loop) and B-22 (institutional-track content), one
  P1 product feature and one P2 academic-track deliverable. B-18: added a "city stamps" wall
  to the walk pane (More tab, right below the existing walk-recording list) — a 20-cell grid,
  one seal per NL city, that fills in (vermilion ink-stamp styling matching the app's existing
  aesthetic) the first time the walker finishes a recorded walk of ≥200 m in that city (a small
  floor to keep a stray GPS blip from earning a stamp). Reuses the existing `savedTraces`
  localStorage data — no new storage, no new permissions, purely a derived view — computed as
  `earnedCityIds()` from trace distance+cityId and re-rendered on every trace mutation (stop
  recording, delete) and on language switch. Tapping any stamp (earned or not) jumps the map to
  that city via the existing `selectCity()`, nudging exploration toward the 12 not-yet-walked
  cities. Trilingual labels added to all three `I18N` blocks. Verified in headless Chromium
  against the live app on a local static server: grid renders all 20 cities, progress counter
  reads "0 / 20 stamped" on a fresh profile, injecting a synthetic 500 m Delft trace into
  `localStorage` and reloading correctly flips exactly the Delft cell to `.earned` and updates
  the counter to "1 / 20" — confirms the earn logic, not just the render. No new console errors
  (the only console noise was pre-existing `ERR_CONNECTION_RESET` on tile fetches, the same
  sandbox-only outbound-proxy flakiness to PDOK/ArcGIS noted in the 2026-08-20 entry, unrelated
  to this change and confirmed separately not to affect the real network). B-22: researched the
  three named submission targets live rather than drafting blind — found DH Benelux's own site
  serving stale (2023) cached content and no 2027 CFP announced yet; FOSS4G-NL's 2026 edition
  (8–9 July, Groningen) already happened and its CFP is closed, no 2027 posted; both of
  Stimuleringsfonds Creatieve Industrie's 2026 "Digitale cultuur" rounds (Feb, Aug) are also
  already closed. So none of the three drafts in the new `docs/SUBMISSIONS.md` can be submitted
  today — the deliverable is ready-to-fire copy for the next cycle of each, so writing happens
  ahead of deadline pressure instead of during it: a DH Benelux short-paper/demo abstract on the
  RD→Web Mercator client-side reprojection + PMTiles offline-distribution pattern (the two
  technical contributions likely to interest a DH/geohumanities audience), a Dutch-language
  FOSS4G-NL talk proposal aimed at OSGeo.nl practitioners, and a Stimuleringsfonds phase-I grant
  pitch. Flagged one real blocker found during the research, not invented: the Stimuleringsfonds
  route requires Dutch KVK (Chamber of Commerce) registration for phase-I materials, which the
  fund's own page doesn't clarify for a non-resident applicant — recommended the owner either
  confirm eligibility directly with the fund or route the application through a Dutch academic
  partner (dovetails with the existing B-21 outreach targets) before investing time in a full
  phase-II plan. Verified before push: both inline `<script>` blocks pass `node --check`, all
  JSON files in the repo parse. Next up: B-11 bake remaining Randstad PMTiles (pmtiles/ still
  only 42 MB, plenty of headroom under 300 MB; outbound connectivity to the ArcGIS tile source
  was spot-checked working this session, so this is a good next target), B-14 continue on the
  8 zero-postcard-coverage cities flagged 2026-08-20, B-17 walk photos (natural follow-up to
  B-18's stamp wall — same "make a completed walk feel rewarding" thread). Blockers unchanged —
  see end-of-run report.
- **2026-08-20** — Shipped B-10 (highest-shareability item, flagged "next up" for three
  loops running) and made progress on B-14. B-10: added a "Toen/nu-video" / "Then/now
  video" button next to the existing compare toggle. It composites the current map
  viewport twice into 1080×1080 canvases (base-only "now", base+historical "then") using
  the same tile pipeline as the walk-share card (`offlineTileSrc` + `renderHistTileCanvas`,
  PMTiles-first), then animates a vermilion wipe divider between them (two ease-in-out
  sweep cycles, ~6s) on an output canvas recorded via `canvas.captureStream` +
  `MediaRecorder` — encoded straight to WebM (VP9/VP8, feature-detected) or MP4 on Safari,
  no external GIF/video-encoding library needed. Shares via the Web Share API when
  available, otherwise downloads. Verified two ways: (1) headless Chromium against the
  real app — confirmed the button, mime-type detection, and `captureStream` support all
  present, and the export correctly reaches a "Making video…" busy state with no thrown
  errors; (2) headless Chromium with all cross-origin tile requests stubbed to an instant
  1×1 PNG (to route around this *build sandbox's* flaky outbound proxy to PDOK/ArcGIS,
  confirmed separately via plain `curl` to be fine — a sandbox/headless-browser quirk, not
  a real-network issue) — this produced an actual playable 1080×1080 VP9 WebM,
  ffprobe-verified at ~5.96s duration, and the button correctly disabled during export and
  restored after. B-14: audited actual postcard coverage vs. the backlog's suggested
  targets and found Frans Hals/Haarlem, Vermeer *View of Delft*/Delft, and Van Gogh/Den
  Haag were already shipped in earlier passes (the row just hadn't been updated) — Delft
  alone has 36 Vermeer postcards. The real content gap is elsewhere: **9 of 20 cities have
  zero postcards** (groningen, leeuwarden, deventer, arnhem, nijmegen, maastricht,
  middelburg, gouda, amersfoort), which is a bigger hole in "content depth" than adding
  more paintings to already-deep cities. Shipped one fix: Piet Mondriaan's *Windmill near
  Tall Trees with Woman at the Wash Stoop* (1907, early naturalistic period, RKD catalogue
  raisonné A423) for Amersfoort — his birthplace (Mondriaanhuis museum is there today).
  Verified Public Domain via the Commons `imageinfo`/`extmetadata` API before adding
  (`Copyrighted: False`, `LicenseShortName: Public domain` — note a *different*,
  visually-similar Mondrian windmill file on Commons is CC-BY-SA 4.0, a photographer's own
  photo of the canvas, not PD-Art, and was correctly rejected); downloaded and
  visually inspected the actual painting before writing copy. Left the other 8 cities
  alone rather than force weak/guessed attributions into them — several (Groningen,
  Leeuwarden, Deventer, Arnhem, Nijmegen, Maastricht, Middelburg, Gouda) don't have an
  obvious, well-documented Golden-Age-or-equivalent PD masterpiece tied to them the way
  Amersfoort has Mondriaan; forcing one in risks the exact "guessed and got it wrong"
  failure mode flagged in earlier loop entries (B-13's Utrecht "Werkbond" case). Flagging
  this as a good target for either owner input (does the owner know of a real
  city↔painting connection for any of these?) or a future loop pass with more research
  budget. Verified before push: both inline `<script>` blocks pass `node --check`, all
  JSON files (landmarks, postcards ×85 items, 4 manifests) parse. Next up: continue B-14
  (remaining 8 zero-coverage cities, carefully), B-11 bake remaining Randstad PMTiles
  (pmtiles/ still well under the 300 MB ceiling), B-22 submission-target abstracts (B-20
  colofon prerequisite is done). Blockers unchanged — see end-of-run report.
- **2026-08-17** — Shipped B-4 and started B-13 (distribution + content-depth cluster).
  B-4: `docs/LAUNCH_COPY.md` — ready-to-paste launch posts for r/thenetherlands,
  r/MapPorn, r/dataisbeautiful, r/Amsterdam, Show HN, Tweakers.net, and X/Bluesky threads,
  NL+EN, matching the tone already established in `docs/OUTREACH.md`; includes a "first
  comment" for each Reddit/HN post and posting-etiquette notes (space out postings, don't
  cross-post same-day, check each sub's self-promo rule) since a spammy launch would burn
  the accounts needed for the 5M-pageview push. B-13: added two Rotterdam landmarks to
  `landmarks/landmarks.json` — Kiefhoek (J.J.P. Oud, 1925–1930, worker housing, New
  Functionalism) and Sonneveld House (Brinkman & Van der Vlugt, 1933, same firm as the
  already-listed Van Nelle Factory). Both images verified Public Domain via the Wikimedia
  Commons `imageinfo` API (same photographer, Wikifrits, for both — consistent sourcing),
  coordinates verified via Wikipedia `coordinates` API, Wikipedia deep links verified to
  exist before adding (Kiefhoek has nl+en articles; Sonneveld House only has a dedicated nl
  article, so `wiki` carries nl only — same "don't guess" rule as B-15). B-13 stays `doing`,
  not `done`: the other two targets in that row need input the loop can't supply alone —
  Hilversum (Zonnestraal, Dudok Raadhuis) isn't buildable yet because Hilversum isn't in the
  app's `CITIES` list or PMTiles set (adding a landmark there first requires baking a new
  city, which is really B-11-adjacent scope, not a landmarks-only edit), and Utrecht
  "Werkbond" doesn't resolve to any canonical building in Commons/Wikipedia searches — likely
  a shorthand the owner had a specific building in mind for; flagging for clarification
  rather than guessing and risking a wrong/unverifiable entry. Verified before push: both
  inline `<script>` blocks pass `node --check`, all JSON files (landmarks, postcards,
  4 manifests) parse. Next up: B-10 then/now GIF export (highest-shareability item left),
  B-14 more postcards, B-11 bake remaining Randstad cities (pmtiles/ is still only ~42 MB,
  plenty of budget under the 300 MB ceiling). Blockers unchanged — see end-of-run report.
  Also re-confirmed: `origin/main` is still stale relative to this branch's earlier work
  history (diverged, not an ancestor) — everything shipped since 2026-08-13 is live only on
  `claude/peaceful-gauss-axvnhn` until a PR merges it, which is outside this loop's mandate.
- **2026-08-13 (4)** — B-23 closed. The earlier 404 is explained: the owner had selected
  "No, I need one" in Zenodo, which *reserves* a DOI that only starts resolving on publish —
  so the id was correct all along and holding it out of the citation block was the right call.
  Deposit is now published: concept DOI `10.5281/zenodo.21924251` (always resolves to the
  latest version) and v1 DOI `10.5281/zenodo.21924252`; both verified 200 via doi.org and the
  Zenodo API (title "Old Map Stroll", licence mit-license, 1 file). Wired the concept DOI into
  about.html's citation section in all three languages (visible DOI line + BibTeX upgraded from
  `@misc` to `@software` with `publisher`/`doi` fields), and added a DOI + MIT badge and new
  Citation/Licence sections to README.md. Prerequisite shipped in the same pass: a MIT LICENSE
  file (the repo had none, and Zenodo requires a licence) carrying an explicit carve-out that
  MIT covers source code only, with Kadaster/PDOK CC BY 4.0 map data and Wikimedia Commons
  imagery keeping their own terms. Note: the Zenodo record lists the creator as "WU, YUNCHING"
  in all caps — cosmetic, owner may want to fix it on the record for a cleaner citation.
  **Still not deployed:** everything from today remains on `claude/peaceful-gauss-axvnhn`;
  `origin/main` is stale at f9e9c1a, so about.html 404s live and GoatCounter is not yet counting.
- **2026-08-13 (3)** — Owner sent a Zenodo DOI (`10.5281/zenodo.21924252`) intended to close
  B-23. Verified it before touching any files: `curl -L https://doi.org/...`, the DataCite
  API, and `zenodo.org/api/records/21924252` all return 404. Sanity check confirmed network/
  tooling was fine (a known-good Zenodo DOI resolved 200, and record id 14,000,000 exists) —
  21,924,252 is simply outside Zenodo's current allocated id range, so this is very likely a
  typo/transcription error or a draft deposit that was never actually published. Did **not**
  add it to about.html's BibTeX block — a dead DOI in a citation aimed at academics would be
  worse than no DOI. B-23 stays BLOCKED(user); left a note in the backlog row above asking
  the owner to confirm the Zenodo record is published and re-send the id.
- **2026-08-13 (2)** — B-1 unblocked: owner supplied GoatCounter site code (`yunching`).
  Added the GoatCounter script tag (`data-goatcounter`, async, cookieless) to index.html's
  `<head>`; excluded from the inline-script `node --check` sweep because it uses `src=`.
  Updated privacy.html (NL/EN/ZH) to honestly disclose the new analytics — removed the blanket
  "no tracking" claim and added a bullet describing GoatCounter as privacy-friendly/cookieless
  aggregate-only pageview counting, with a link to GoatCounter's own privacy policy. Updated
  Operating metrics: pageviews are now instrumented but no historical data exists yet — next
  loop (or the owner) should check https://yunching.goatcounter.com and report a real number
  once there's traffic to look at. No other backlog items touched this pass.
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
