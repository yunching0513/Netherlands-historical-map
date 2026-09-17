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
| B-12 | Amsterdam full era ladder: add 1815, 2021 archives | done | 2026-08-31 — baked both, see Loop Log |
| B-13 | More landmarks: Rotterdam (Kiefhoek, Sonneveld House), Utrecht (Werkbond), Hilversum (Zonnestraal, Dudok Raadhuis) | done | 2026-09-07 — closed out. Rotterdam + Hilversum targets were already shipped (2026-08-17 / 2026-09-03). Utrecht "Werkbond" is dropped from this row rather than left open indefinitely: three separate research passes (2026-08-17, 2026-08-31, 2026-09-07) across Wikipedia/Commons found no canonical Utrecht building actually named/known as "Werkbond" — the closest real entity, the Nederlandsche Werkbond (est. 1924, Dutch sibling of the Deutscher Werkbund), was a design-reform association, not a building, and didn't commission a specific Utrecht landmark under that name. Forcing a guessed building in would repeat the exact wrong-attribution risk this backlog has flagged since 2026-08-17. If the owner had a specific building in mind, re-add it as a fresh backlog row with the real name/architect once known — that's a cleaner path than an indefinitely-`doing` row. |
| B-14 | More postcards: Van Gogh (Amsterdam/Otterlo), Frans Hals (Haarlem), Vermeer View of Delft (already?), Mondriaan (Den Haag) | done | 2026-09-07 — row fully closed: all 20 originally-in-scope cities now have ≥1 verified postcard. Shipped the last 4: Jan van Goyen "Gezicht op Arnhem" (1643, Museum Arnhem, PD), Wybrand de Geest self-portrait (1629, Rijksmuseum/on loan to Fries Museum Leeuwarden, PD), Jozef Israëls "Alleen op de wereld" watercolor (Rijksmuseum, PD, Groningen birthplace), and an anonymous 1673 Siege-of-Maastricht print (Rijksmuseum, CC0). See Loop Log for how groningen/leeuwarden/maastricht — flagged empty after 2+ prior passes each — finally got fresh, solid hits. |
| B-15 | Wikipedia deep links per landmark (nl/en/zh) | done | 2026-08-13, nl+en (all 10 landmarks verified via API); zh skipped — no zh articles exist for these niche buildings |
| B-16 | Walk recording (散策記錄) ported from taiwan-historical-maps: GPS trace + live stats + saved walks + GeoJSON export + 1080×1920 share card with map composite | done | 2026-07-03 |
| B-17 | Walk photos along route (camera + IndexedDB) + photo strip on share card, as in Taiwan app | done | 2026-08-31 — see Loop Log |
| B-18 | City stamps/seals for completed walks (Taiwan app's 22-county seal wall → 20 NL cities) | done | 2026-08-24 — see Loop Log |
| B-19 | β 3D walk mode ported from taiwan-historical-maps/beta: perspective canvas ground, compass rotation, GPS scroll | done | 2026-07-08, verified in headless Chromium |
| B-19b | Vendor leaflet/proj4/pmtiles locally (drop unpkg CDN dependency) | done | 2026-07-08, needed for offline/app-store builds anyway |
| B-24 | Landmark coverage is very uneven: only 5 of 21 cities (amsterdam, rotterdam, denhaag, utrecht, hilversum) have any architecture-walk landmarks; 16 have zero. Add 1–2 verified landmarks each to the strongest candidate cities first (delft: Nieuwe Kerk/Oude Kerk, denbosch: Sint-Janskathedraal, nijmegen: Waalbrug, eindhoven: Van Abbemuseum/Philips heritage, leiden: Pieterskerk) | doing | 2026-09-17 — shipped 5 more landmarks across 5 new cities: Gouda (Sint-Janskerk), Dordrecht (Grote Kerk), Groningen (Der Aa-kerk), Leeuwarden (Oldehove), Maastricht (Sint-Servaasbasiliek). Coverage now 16 of 21 cities, up from 11. Remaining at zero (5): amersfoort, zwolle, deventer, arnhem, middelburg — all 5 already have research-agent-sourced, Wikidata-coordinate-verified, Commons-license-verified candidates ready to write up next pass (amersfoort's Onze Lieve Vrouwetoren image just needs a re-attempted download — see Loop Log). Row stays `doing`. |
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

- **2026-09-17** — Continued B-24 (landmark coverage gap), same row flagged "next up" since
  2026-09-14. Delegated research on all 10 remaining zero-coverage cities (gouda, dordrecht,
  amersfoort, groningen, leeuwarden, zwolle, deventer, arnhem, maastricht, middelburg) to a
  background subagent in one pass, rather than the usual 3-city batch, since the row had enough
  candidates queued up to be worth front-loading the research; picked the 6 strongest,
  best-documented results to independently verify and ship this session (gouda, dordrecht,
  amersfoort, groningen, leeuwarden, maastricht), leaving zwolle/deventer/arnhem/middelburg's
  already-researched candidates ready for a future pass without needing fresh research budget.
  Independently re-verified every claim before writing, not taken on the agent's word: re-ran
  Wikidata `EntityData` P625 lookups directly for all 6 candidates (Q848290 Sint-Janskerk, Q2024749
  Grote Kerk Dordrecht, Q2245047 OLV toren Amersfoort, Q2255378 Der Aa-kerk, Q2018608 Oldehove,
  Q253935 Sint-Servaasbasiliek) — all 6 coordinates matched the agent's report exactly to 5+ decimal
  places; independently re-ran the Commons `imageinfo` API on all 6 images and confirmed licenses
  matched exactly (Gouda CC-BY-SA 4.0, Dordrecht CC-BY-SA 4.0, Amersfoort Public Domain, Groningen
  Public Domain, Leeuwarden CC-BY-SA 3.0, Maastricht CC-BY-SA 4.0); live-checked all 12 nl/en
  Wikipedia URLs (200 each, including confirming "Sint_Janskerk" isn't a disambiguation stub by
  pulling its actual extract); independently confirmed one specific flagged fact against the primary
  source rather than trusting either the agent's claim or dropping it — fetched the Dutch Wikipedia
  Onze Lieve Vrouwetoren article directly and confirmed word-for-word that the tower's spire is the
  literal origin point of the Rijksdriehoeksmeting national coordinate grid. Downloaded and visually
  inspected 5 of 6 images at full/near-full resolution before writing copy (all clean, unobstructed,
  recognizable exteriors — Gouda's tower/gable, Dordrecht's famous lean visibly captured, Groningen's
  Akerk tower and apse, Leeuwarden's Oldehove against open sky, Maastricht's Romanesque apse with
  both towers) — hit the same shared-IP Commons rate-limiting flagged repeatedly since 2026-08-27,
  but this time it was unusually persistent: Groningen and Leeuwarden needed one retry each and came
  through, while Amersfoort's original-resolution image stayed hard-429'd through 15+ retries over
  roughly 10 minutes of backoff, across 3 different thumbnail sizes and even the exact tracked URL
  from the imageinfo API response — a longer, more stubborn block than any prior loop's "retry once
  or twice and it clears" pattern. Rather than ship Amersfoort without the visual-inspection step
  this discipline has required every prior session, left it out of this push: its coordinates and
  license are independently verified and ready, it just needs someone to re-attempt the image
  download (very likely to succeed once the block lifts, per every prior instance of this pattern).
  Caught and fixed one real bug of my own mid-session: the Maastricht entry's `year` field
  originally read "1039–12世紀", mixing Chinese text into a field the app displays unlocalized in
  all three UI languages (`item.year` is a shared plain string, not a `{zh,en,nl}` object per the
  schema) — would have shown Chinese characters in the English/Dutch UI; caught this by actually
  running the headless-browser render pass and reading its output rather than just checking JSON
  parses, then fixed it to "1039–1200" (numeric-only, matching every other item's year format).
  Also caught and fixed a self-inflicted formatting bug before it reached git: a first attempt at
  writing the JSON used a wholesale `json.dump(..., indent=2)` re-serialization, which reformatted
  the *entire* file's existing 22 items (compact one-line `{zh,en,nl}` objects blown out to
  multi-line) alongside the 5 new ones, producing a 719-line diff for what should've been a
  ~110-line addition — caught via `git diff --stat` before committing, reverted with `git checkout
  --`, and redid it as a text-level splice (custom formatter matching the file's existing compact
  style exactly) that produced a clean, minimal diff instead. Introduced 2 new style-taxonomy
  buckets, both genuine distinct regional styles not already covered: `brick-gothic` (Baksteengotiek)
  for Groningen's Der Aa-kerk — the Northern Netherlands/Hanseatic brick-Gothic tradition, distinct
  from the existing `gothic` bucket (Delft/Leiden/Nijmegen's stone-detailed Gothic) — and
  `romanesque` for Maastricht's Sint-Servaasbasiliek, the first Romanesque-era building in the app's
  taxonomy (everything else so far is Gothic-or-later); reused the existing `gothic` and
  `brabantine-gothic` buckets for Gouda/Amersfoort/Leeuwarden and Dordrecht respectively, where the
  style genuinely matches what's already there — safe per the standing finding (re-confirmed by grep
  this session) that `style` ids are pure JSON data with no hardcoded legend to extend. Verified
  before push: `landmarks.json` parses (27 items, up from 22, no duplicate ids), `postcards.json`
  and `pmtiles/manifest.json` still parse (untouched), both inline `<script>` blocks in `index.html`
  pass `node --check` (index.html itself wasn't touched — pure landmarks-data addition, same pattern
  as recent B-24 passes). A real headless-Chromium pass was available this session (playwright +
  the pre-installed `/opt/pw-browsers` Chromium) — rendered all 5 shipped cities
  (`?city=gouda/dordrecht/groningen/leeuwarden/maastricht`) with cross-origin requests stubbed to a
  1×1 PNG, confirmed the `#arch-grid` shows exactly one correctly-titled/attributed/styled card for
  each, then went one step further and exercised the lightbox click-through for the Maastricht card
  (had to first dismiss a "daily card" modal intercepting clicks and switch to the Cards tab, neither
  of which is landmarks-specific — just how the app's UI is structured), confirming title and a
  working Wikipedia deep-link populate correctly — zero app-specific console errors in any pass (the
  only console noise was the test harness's own request-stubbing misserving the GoatCounter script,
  the same artifact flagged in every recent entry). Also re-checked the standing GoatCounter
  Operating-metrics to-do: still a login wall with no public dashboard configured (`HTTP 200` to
  `/user/new`), unchanged since 2026-09-07 — still needs the owner to either log in and check real
  numbers or enable GoatCounter's public-dashboard setting. Next up: retry Amersfoort's image
  download (candidate fully verified otherwise, just needs the Commons rate-limit to clear), then
  the 4 still-untouched candidates from this session's research batch — Zwolle (Sassenpoort or
  Peperbus), Deventer (Lebuïnuskerk or the Waag), Arnhem (Sint-Eusebiuskerk or Duivelshuis),
  Middelburg (Stadhuis or the Abdij) — all already researched with coordinates/licenses/facts ready,
  just need the same independent-verification pass this session gave its 6. That would close B-24
  entirely (21 of 21 cities covered). Blockers unchanged — see end-of-run report.
- **2026-09-14** — Continued B-24 (landmark coverage gap): closed the "denhaag worth prioritizing
  next" gap flagged in the 2026-09-10 entry, plus finished both of this row's original Eindhoven
  candidates. Delegated initial research to a background subagent for three cities (denhaag,
  nijmegen, eindhoven) — same pattern as recent B-14/B-24 entries — then independently re-verified
  every claim before writing, not taken on the agent's word: re-ran Wikidata `EntityData` lookups
  for all 5 candidate buildings (Q834448 Vredespaleis, Q221092 Mauritshuis, Q1146466 St. Stevenskerk,
  Q2039118 De Witte Dame, Q106106048 Van Abbemuseum) — all 5 coordinates matched the agent's report
  exactly; independently re-ran the Commons `imageinfo` API on all 5 images and confirmed licenses
  matched exactly (Vredespaleis CC-BY 4.0, Mauritshuis CC-BY 2.0, St. Stevenskerk CC0, De Witte Dame
  CC0, Van Abbemuseum CC-BY-SA 4.0 — no bad-license candidates, unusually clean batch); live-checked
  all 9 nl/en Wikipedia URLs (200 each, including confirming De Witte Dame genuinely has no English
  article rather than trusting the agent's claim); downloaded and visually inspected all 5 images at
  full/near-full resolution before writing copy — all clean, unobstructed, recognizable modern
  exteriors (one image, St. Stevenskerk, needed a retry after Wikimedia's shared-IP rate limiter
  returned an HTML error page instead of the JPEG on the first attempt — the same 429/rate-limit
  pattern flagged repeatedly since 2026-08-27, correctly treated as retry-with-backoff rather than
  "broken file"). Cross-checked the agent's own flagged uncertainties against primary sources rather
  than either asserting or silently dropping them: fetched the full nl.wikipedia St. Stevenskerk
  article text directly and confirmed, word-for-word, the WWII bombing narrative (22 Feb 1944 USAAF
  raid, tower spire collapse onto the west aisle and Stikke Hezelstraat houses, 5 air-defense
  watchmen killed, Mari Andriessen's "de Engel" memorial) and the 1272/1273 Albertus Magnus
  consecration story; fetched the full en.wikipedia Peace Palace article and confirmed the Carnegie
  funding chain, the 1905 216-entry competition won by Cordonnier, and van der Steur's budget-driven
  tower cuts, all matching the agent's report precisely. For the two flagged uncertainties that
  *didn't* fully resolve — Pieter Post's disputed co-architect credit on the Mauritshuis (English
  Wikipedia asserts it, Wikidata's P84 doesn't) and Louis Kalff's unconfirmed architect credit on De
  Witte Dame (Wikidata-only, not in the nl.wikipedia article text) — wrote the copy to reflect that
  uncertainty honestly (Post mentioned as an English-language-sourced claim, not asserted as fact;
  Kalff dropped entirely from the shipped entry) rather than picking a side or silently omitting the
  nuance. Corrected one framing error inherited from the agent's brief: De Witte Dame was a Philips
  radio-tube (vacuum valve) factory from the outset, not the literal lightbulb factory (a separate,
  nearby building in the same Emmasingel complex) — fixed in the shipped description. Deliberately
  did not add Nijmegen's Waalbrug despite it being this row's original suggestion: the agent's own
  research confirmed it has a real named designer (Gerrit van Heukelom) but is still infrastructure,
  not a building, the same "not really an architecture-walk landmark" judgment call flagged for
  Utrecht's dropped "Werkbond" target in B-13 — St. Stevenskerk was the stronger, on-pattern
  Nijmegen candidate and is what shipped instead. Introduced 3 new style-taxonomy buckets (safe per
  the established finding, re-confirmed by grep this session, that `style` ids are pure JSON data
  with no hardcoded legend to extend): `neo-renaissance` reused for Vredespaleis (a second entry
  alongside 's-Hertogenbosch's earlier Witte Huis-style bucket, with its own clean label), plus two
  genuinely new ones — `dutch-classicism` for the 17th-century Mauritshuis (distinct from the
  already-used `dutch-renaissance` bucket, which covers the earlier, more ornate style) and
  `delft-school` for the Van Abbemuseum's 1936 traditionalist Kropholler wing. Verified before push:
  `landmarks.json` parses (22 items, up from 17 — caught and fixed two unescaped `"` characters
  inside English description text, `"de Engel"` and `"Eerste gloeilampenfabriek"`, that broke the
  first parse attempt), `postcards.json` and `pmtiles/manifest.json` still parse (untouched), both
  inline `<script>` blocks in `index.html` pass `node --check` (index.html itself wasn't touched —
  pure landmarks-data addition, same as the 2026-09-10 pass). A real headless-Chromium pass was
  available this session (playwright + the pre-installed `/opt/pw-browsers` Chromium) — used it more
  thoroughly than the 2026-09-10 baseline: rendered all 3 new cities (`?city=denhaag/nijmegen/
  eindhoven`) with cross-origin requests stubbed to a 1×1 PNG, confirmed the `#arch-grid` shows the
  correct card count/titles/architects/style-tags for each (denhaag: 2, nijmegen: 1, eindhoven: 2),
  then went one step further and exercised the lightbox click-through for the Nijmegen card,
  confirming title/artist/style/description/credit/Wikipedia-link all populate correctly with the
  right resolved URL — zero app-specific console errors in any pass (the only console noise was the
  test harness's own request-stubbing misserving the GoatCounter script, same artifact flagged
  2026-09-10). Also re-checked the standing GoatCounter Operating-metrics to-do: still a login wall
  with no public dashboard configured (`HTTP 303` → `/user/new`), unchanged since 2026-09-07 — still
  needs the owner to either log in and check real numbers or enable GoatCounter's public-dashboard
  setting. Next up: B-24's remaining 10 zero-coverage cities (gouda, dordrecht, amersfoort,
  groningen, leeuwarden, zwolle, deventer, arnhem, maastricht, middelburg) — none yet researched for
  landmarks specifically (as opposed to postcards, which B-14 already covered for all of them);
  worth a fresh research pass with the same discipline used this session rather than forcing weak
  matches. Blockers unchanged — see end-of-run report.
- **2026-09-10** — Started B-24 (landmark coverage gap, opened 2026-09-07 but not yet worked).
  Picked the 3 of its 5 named starting candidates with the strongest, most famous, best-documented
  buildings — Delft's Nieuwe Kerk, 's-Hertogenbosch's Sint-Janskathedraal, and Leiden's
  Pieterskerk — rather than trying all 5 in one pass; nijmegen (Waalbrug) and eindhoven
  (Van Abbemuseum/Philips heritage) are more speculative fits for the app's existing "architecture
  walk" framing (civic/religious/housing landmarks, not infrastructure or corporate heritage) and
  were deliberately left for a future pass with more research budget rather than rushed in weak.
  Delegated the initial research to a background subagent (same pattern B-14's 2026-09-07 entry
  used) to keep this session's own context free for independent verification, then re-verified
  every claim before writing: confirmed all 3 coordinates via direct Wikidata `EntityData` lookups
  (Q678611, Q2050553, Q1537972) — all matched the agent's report exactly; confirmed all 6
  Wikipedia URLs (nl+en for each building) resolve 200; independently re-ran the Commons
  `imageinfo` API on all 3 images (hit the same `upload.wikimedia.org`/API 429 rate-limiting this
  sandbox's shared IP has flagged repeatedly since 2026-08-27 — resolved with a backgrounded
  retry-with-backoff script rather than treating the first 429 as failure) and confirmed licenses
  independently: Delft CC-BY-SA 4.0 (W. Bulach), 's-Hertogenbosch CC-BY 4.0 (Acediscovery), Leiden
  CC-BY-SA 3.0 (Jan van Galen/RCE) — all matching the agent's report; then downloaded and visually
  inspected all 3 images directly rather than trusting filenames/metadata, confirming each is a
  genuine, clean, recognizable modern exterior photo (Delft: straight-on tower/facade; 's-Hertogenbosch:
  dramatic transept-and-tower view; Leiden: full west-facade shot) — none are interior shots,
  fragments, or old prints, the failure mode the agent's own report flagged it had already screened
  a rejected 's-Hertogenbosch candidate for. Added a new `gothic` style bucket (Delft's Nieuwe
  Kerk, Leiden's Pieterskerk) and a more specific `brabantine-gothic` bucket ('s-Hertogenbosch's
  Sint-Jan, genuinely a distinct regional style, not just "generic Gothic") — safe to introduce
  since the style taxonomy is pure JSON data with no hardcoded legend to extend (confirmed via
  grep, same finding as the 2026-09-03 entry). Wrote honest zh/en/nl copy strictly from the
  verified facts (construction dates, master builders across multi-century building campaigns,
  the Delft church's role as the Orange-Nassau royal crypt since William the Silent's 1584
  assassination, the Leiden church's Pilgrim Fathers/John Robinson connection and other notable
  burials, the 's-Hertogenbosch restoration history including its well-known modern angel-with-
  mobile-phone statue) rather than the agent's own prose. Verified before push: `landmarks.json`
  parses (17 items, up from 14, 8 cities up from 5 — also caught and logged in the backlog row
  that the row's own "5 covered cities" list had a latent error, denhaag not haarlem, unrelated to
  this session's new work but worth fixing while touching the row), `postcards.json` and
  `pmtiles/manifest.json` still parse (untouched), both inline `<script>` blocks in `index.html`
  pass `node --check` (index.html itself wasn't touched — this was pure landmarks-data addition).
  Unlike recent prior entries, a real headless-Chromium pass **was** available this session
  (`playwright` + a pre-installed Chromium at `/opt/pw-browsers`, globally on `npm -g`) — ran it
  against a local static server for all 3 new cities (`?city=delft/denbosch/leiden`), with all
  cross-origin requests stubbed to a 1×1 PNG to route around this sandbox's outbound-network
  flakiness to tile/analytics hosts: confirmed each city's Cards-tab architecture grid renders
  exactly one card with the correct title/architect/year, and that opening the lightbox shows the
  correct style label, description text, and a working Wikipedia deep-link — zero app-specific
  console errors (the only console noise was from the request-stubbing itself misserving the
  GoatCounter analytics script, an artifact of the test harness, not the app). This closes the gap
  the 2026-08-31/09-03 entries flagged (no browser available then) — worth keeping this heavier
  verification bar now that the tooling exists. Next up: B-24 remaining candidates — nijmegen and
  eindhoven (the row's own suggestions, needs a "does this fit the architecture-walk framing"
  judgment call first) plus completely uncovered cities with no candidate yet researched at all
  (groningen, leeuwarden, zwolle, deventer, arnhem, maastricht, middelburg, gouda, dordrecht,
  amersfoort, denhaag — notably denhaag itself, a capital-region Randstad city with obvious
  candidates like the Vredespaleis or Mauritshuis, is a surprising gap worth prioritizing next).
  Blockers unchanged — see end-of-run report.
- **2026-09-07** — Closed both P1 rows that had been "doing" since 2026-08-17/09-03 (B-13,
  B-14), plus opened one new backlog row after an audit. B-13: dropped the unresolvable Utrecht
  "Werkbond" target after a third research pass (this session's own web search, not just re-reading
  prior loop notes) confirmed no Utrecht building is actually named/known as "Werkbond" — the only
  real match, the Nederlandsche Werkbond (est. 1924), was a design-reform association, not a
  building. Rotterdam and Hilversum targets in the same row were already done, so the row closes
  as `done` rather than staying open on an unresolvable third of it; re-openable as a fresh row if
  the owner ever names the actual building. B-14: delegated fresh research (via a background
  subagent, to keep this session's own context free for verification rather than search) on the
  4 remaining zero-coverage cities — groningen, leeuwarden, arnhem, maastricht — each of which had
  already absorbed 2+ prior research passes with no hit (except arnhem, genuinely untouched until
  now). The agent came back with 4 real candidates; every one was independently re-verified in this
  session before writing to `postcards.json`, not taken on the agent's word — and re-verification
  caught one real error the agent's own report got wrong: it credited Jozef Israëls' Groningen
  postcard to "Mesdag Collection, The Hague" and described it as a 125×200cm oil, but the actual
  Commons file for that image (used for the img/sourceUrl) is a different, smaller Rijksmuseum
  watercolor study (33×49.5cm, brush on paper, accession SK-A-2613) — the credit/technique in the
  shipped entry describes what the cited image actually is, not what the agent assumed it was.
  Also cross-checked the Leeuwarden self-portrait's "on loan to Fries Museum since 1948" claim
  against the Rijksmuseum's own object page directly (a Commons metadata field made it look like
  that loan had an end date around 2005, which the primary source didn't confirm) before writing
  it as current. Final 4 shipped, all verified PD/CC0 via the Commons `imageinfo` API and cross-
  checked against Wikipedia/Rijksmuseum for the underlying facts: Jan van Goyen's *Gezicht op
  Arnhem* (1643, Museum Arnhem/NK-collectie — one of ~20 documented Van Goyen views of Arnhem, the
  same prolific-town-portraitist pattern as his existing Nijmegen entry); Wybrand de Geest's 1629
  self-portrait (Leeuwarden-born-and-died "Frisian Apelles," on loan from the Rijksmuseum to the
  Fries Museum in his own city since 1948, with a documented 1634 studio visit from Rembrandt via
  his marriage to a niece of Saskia van Uylenburgh); Jozef Israëls' *Alleen op de wereld* watercolor
  study (Groningen-born Hague School founder, Rijksmuseum, described honestly as the study it is);
  and an anonymous 1676 print of the 1673 Siege of Maastricht (Rijksmuseum, CC0, notable as the
  siege where the real d'Artagnan — the historical basis for Dumas's Three Musketeers — died, and
  where Vauban first used the parallel-trench siege method that became the European standard).
  This closes B-14 completely: all 20 originally-in-scope cities now have ≥1 verified postcard
  (93 items total, up from 89). B-24 (new): while auditing postcard city-coverage the same way
  B-14's own log entries have for months, ran the identical audit against `landmarks.json` and
  found a much bigger, previously undocumented gap — only 5 of 21 cities have any landmark at all
  (amsterdam, rotterdam, denhaag, utrecht, hilversum); 16 cities have zero architecture-walk
  content. Opened this as a new P1 row with 5 concrete starting candidates (Delft, Den Bosch,
  Nijmegen, Eindhoven, Leiden) rather than starting the work this session — B-13/B-14 were already
  a full session's worth of finish-what's-open work, and starting a third, larger item risked
  under-delivering on all three instead of fully closing the two that were already `doing`. Also
  checked https://yunching.goatcounter.com per the standing Operating-metrics to-do: it's a login
  wall with no public stats page configured, so still no real pageview number to report — this
  needs either the owner logging in themselves or enabling GoatCounter's public-dashboard setting;
  noting it explicitly rather than repeating the same unresolved to-do silently every loop.
  Verified before push: all JSON files parse (postcards now 93 items, landmarks unchanged at 14),
  both inline `<script>` blocks pass `node --check`. Headless-browser verification wasn't available
  this session (no Playwright/browser install in this sandbox), so instead traced the actual render
  path in `index.html` (`loadPostcards()` → `CARDS_BY_CITY` keyed purely by each item's `city`
  field, no hardcoded per-city whitelist) to confirm the 4 new entries will render on their city's
  Cards tab without needing a live-browser pass — flagging this as a lighter verification bar than
  prior loops' headless-Chromium passes, so worth a real browser check next time the tooling is
  available. Next up: B-24 (new, landmark coverage — start with Delft or Den Bosch, both have an
  obvious, well-documented candidate). Blockers unchanged — see end-of-run report.
- **2026-09-03** — Shipped B-13 (fully unblocks the Hilversum half of the row) and made further
  progress on B-14, both flagged "next up" repeatedly in prior entries. B-13: the row had been
  stuck since 2026-08-17 because Hilversum wasn't in the app's `CITIES` list or PMTiles set, so
  its two requested landmarks (Zonnestraal, Dudok Raadhuis) had nowhere to attach — this pass
  added Hilversum as a full new city rather than treating that as out of scope. Set up a fresh
  `.venv-pmtiles` (pyproj/pillow/pmtiles/requests) and confirmed the Topotijdreis 1900 ArcGIS
  service actually covers Hilversum (a probe render at z15 came back non-empty) before committing
  to the bake. Picked a bounding box (center 52.215, 5.1618, half-lat 0.018, half-lng 0.028 — the
  same half-extents every other single-era city uses) deliberately sized to include both landmark
  coordinates rather than just the old town center: Zonnestraal sits ~3 km south of the Raadhuis,
  outside a naively-centered box. Baked `hilversum-1900.pmtiles` at z12–17: 677/677 planned tiles
  rendered non-empty (no source-coverage gaps), and a direct `pmtiles.reader` read decoded real
  WEBP tiles at both z12 and z15 — the same sandbox-independent check used for B-11/B-12. `pmtiles/`
  grew from 85 MB to 91 MB, still well under the 300 MB ceiling. Added the `CITIES` entry (region
  `randstad`, alongside Amsterdam/Utrecht/Amersfoort which it sits closest to), a noscript SEO
  paragraph, and a `sitemap.xml` row — then swept `docs/LAUNCH_COPY.md` and `docs/SUBMISSIONS.md`
  for every "20 steden / 20 cities" count and enumerated city list, bumping them to 21 so the
  ready-to-paste launch copy (still unposted per B-4) doesn't undercount the app the day it's
  used. For the landmarks themselves: researched both properly rather than reusing whatever image
  ranked first. Dudok Raadhuis — rejected an interior shot (chairs/windows, not identifiable as
  the building) in favor of "Raadhuis Hilversum2022.jpg", a clean unobstructed facade view; wrote
  copy from Wikipedia's account of Dudok's 1915 appointment as Hilversum's Director of Public
  Works, the 1923 land purchase, the 1924 first sketches, and the Frank Lloyd Wright Prairie-style
  influence noted in both English and Dutch sources. Zonnestraal — used the Dutch Wikipedia
  article (richer than the English one, which is just a disambiguation stub) for precise facts:
  the Hoofdgebouw opened 12 June 1928, architects Jan Duiker/Bernard Bijvoet/Jan Gerko Wiebenga,
  originally built to treat diamond-cutters with tuberculosis, and an official UNESCO World
  Heritage List candidacy from 2010–2018 that was ultimately withdrawn (correcting an initial
  assumption, drawn from the English article's vaguer "1995 nomination" framing, that would have
  understated how recent and formal that candidacy was) — coordinates for the same entry came
  from Wikidata (Q2743329) since neither Wikipedia infobox carries geo-coordinates for it. Both
  images verified CC-BY-SA 4.0 (not PD, but explicitly permitted for landmark photography by this
  file's own `_schema` comment and consistent with 8 of the 12 pre-existing landmark entries) via
  the Commons `imageinfo` API before writing copy; both landmarks tagged `new-functionalism`,
  the same style bucket as Van Nelle/Kiefhoek/Sonneveld, since the style taxonomy is pure JSON
  data with no hardcoded legend list to extend. B-14: found and verified two more solid,
  well-documented connections using the same discipline as the 2026-08-27/08-31 entries (real
  facts, not forced guesses) — Salomon van Ruysdael's "Riviergezicht bij Deventer" (1645,
  Rijksmuseum SK-A-3259), a genuine "painting of the city" in the same vein as the existing Van
  Goyen/Nijmegen entry, showing Deventer's church spires across the IJssel; and Cornelis Ketel's
  "Queen Elizabeth's Porter" (1580, Royal Collection, RCIN 406799), a birthplace connection —
  Ketel was born in Gouda in 1548 and later pioneered the Dutch civic-guard group portrait, the
  same genre as Rembrandt's Night Watch already in the app for Amsterdam, a detail worth surfacing
  since it lets the two postcards talk to each other across cities. Deliberately kept the Ketel
  copy to facts confirmed via Wikipedia/Commons (birthplace, London period 1573–1581, the
  inscription visible on the canvas itself) rather than speculating about the sitter's identity,
  since the Royal Collection's own curatorial page returned a 403 and couldn't be used to verify
  claims about who the "giant porter" actually was. Both images verified Public Domain via the
  Commons `imageinfo` API; downloaded and visually inspected both paintings before writing copy
  (repeated 429s from `upload.wikimedia.org` mid-session — the same shared-IP proxy rate-limiting
  flagged in the 2026-08-27 entry — resolved with the same fix: retry with backoff, not "file is
  broken"). 4 cities remain zero-coverage for postcards (groningen, leeuwarden, arnhem,
  maastricht); groningen and maastricht already absorbed two research passes each with no solid
  hit, and leeuwarden's obvious candidate (M.C. Escher) is out on copyright (died 1972) — arnhem
  is the one still genuinely unexplored. Verified before push: both inline `<script>` blocks pass
  `node --check`, all JSON files parse (landmarks now 14 items, postcards now 91, pmtiles manifest
  now 16 archives). Headless-Chromium passes against the real app (cross-origin tile requests
  stubbed to an instant 1×1 PNG, per the established sandbox workaround) confirmed: `?city=
  hilversum` resolves to a "Hilversum" city-current label with correct coordinates, the city
  picker lists it, both new landmarks render on the Hilversum architecture-walk grid with correct
  names/years/style, and both new postcards render on their city's Cards tab with the artist name
  visible — zero app-specific console errors in any pass. Next up: B-14's remaining Arnhem gap
  (fresh research angle, not yet attempted), B-13's Utrecht "Werkbond" still needs owner
  clarification or should be dropped. Blockers unchanged — see end-of-run report.
- **2026-08-31** — Shipped B-12 and B-17, both flagged "next up" for two loops running (P1
  product depth + the time-travel-story completeness item). B-12: baked `amsterdam-1815` and
  `amsterdam-2021` into `pmtiles/` — Amsterdam now has the full six-era ladder (1815, 1850,
  1900, 1925, 1975, 2021), matching the app's own advertised "1815–2021" time-slider range for
  its flagship city. Used the exact same bbox/zoom params as the four existing Amsterdam
  archives (lat 52.3731, lng 4.8922, half-lat 0.018, half-lng 0.028, z12–17) with
  `tools/bake_pmtiles.py`, after confirming via the ArcGIS `?f=json` service-metadata endpoint
  that `Historische_tijdreis_1815` and `_2021` are real, documented services in the same
  "1815–heden" tiled-service collection Kadaster describes (an earlier plain tile-URL probe
  had returned 404, but that traced to a badly-guessed row/col for the RD tiling scheme, not a
  missing service — the *known-good* 1900 service 404'd identically at those same made-up
  coordinates, which is what exposed the mistake). Both bakes rendered every single planned
  tile non-empty (675/675 each — no source-coverage gaps), and a direct `pmtiles.reader` read
  (the most sandbox-independent check, per the 2026-08-27 entry's rationale) decoded real,
  non-blank WEBP tiles for both archives at z12 and z15. No `index.html` changes were needed —
  same as B-11, the app discovers archives purely from `pmtiles/manifest.json`
  (`pmtilesFor()`/`pmtilesCityMap()` are fully data-driven), so this was pure asset addition.
  `pmtiles/` grew from 75 MB to 85 MB, still comfortably under the 300 MB ceiling. B-17: added
  walk photos, the natural follow-up to B-18's stamp wall flagged in the last two entries.
  During an active recording, a new "📷 Foto/Photo/拍照" button (native `<input type=file
  capture=environment>` — the simplest reliable camera-access pattern for a single-file PWA,
  avoiding a hand-rolled getUserMedia/live-preview UI) downscales the shot to max 1280px/JPEG
  q0.82 on a canvas and stores it in a new IndexedDB database (`nlOldMapsPhotos`, not
  localStorage — photo blobs are too large for that), keyed to the in-progress trace's id, with
  a live thumbnail strip under the recording stats. Past walks show a "📷 N" badge in the trace
  list (only when photos exist, via an async `photosForTrace()` pass after each render) that
  opens a small photo-grid viewer (reusing the app's existing `.lightbox` CSS pattern) with
  per-photo delete; deleting a whole walk (`deleteTrace`) now also purges its photos so nothing
  orphans in IndexedDB. `buildWalkCard()` — the 1080×1920 share-card canvas — now draws up to 4
  evenly-sampled photos as a square-cropped strip; this reused roughly 300px of canvas space
  that was already blank below the existing footer text (the card's fixed 1920px height had
  headroom the whole time), so no existing layout had to be reflowed, and a walk with zero
  photos renders byte-identical to before. Verified in headless Chromium against the real app
  on a local static server, in three passes, each checking a different layer: (1) DOM presence
  of the new photo button/input/viewer elements, plus confirmed the manifest now lists all six
  `amsterdam-*` services (1815/1850/1900/1925/1975/2021); (2) the read/UI path — seeded a
  synthetic trace into `localStorage` and a matching photo blob directly into IndexedDB (the
  same "inject real storage state, then assert on render" technique the B-18 entry used for the
  stamp wall), reloaded, and confirmed the "📷 1" badge appears, the viewer opens showing that
  photo, and clicking delete removes it from both the viewer DOM and (implicitly) IndexedDB;
  (3) the write/render path — triggered the actual share button with cross-origin tile requests
  stubbed to an instant 1×1 PNG (routing around this *sandbox's* known flaky outbound proxy to
  ArcGIS/PDOK, the same workaround the 2026-08-20 entry used for B-10's video export — confirmed
  separately not a real-network issue) and confirmed `buildWalkCard()`'s full async chain,
  including the new photo-strip drawing code, completed with zero page errors and produced a
  real ~90 KB JPEG blob. Camera capture itself (the actual device permission prompt and photo
  picker) can't be exercised headlessly — flagging this as a manual-test item for the owner,
  same caveat the 2026-08-27 entry raised for B-17 up front. Verified before push: both inline
  `<script>` blocks pass `node --check`, all JSON files in the repo parse (postcards/landmarks/
  manifest untouched by this pass — B-17 is pure `index.html`, B-12 is pure `pmtiles/`+manifest).
  Next up: B-14's remaining 6 zero-coverage cities (groningen, leeuwarden, deventer, arnhem,
  maastricht, gouda) — two prior loops already spent real research budget here without a solid
  hit, so this needs either fresh research angles or the owner's own knowledge of a city↔artist
  tie; B-13's Utrecht "Werkbond" still needs the owner to confirm which building was meant, or
  it should be dropped from the backlog row. Blockers unchanged — see end-of-run report.
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
