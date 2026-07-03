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
| B-5 | Per-city landing anchor content for SEO (short NL text per city rendered in a crawlable `<noscript>`/details block) | todo | GH Pages is JS-heavy; give crawlers real text |

### P1 — product depth (share loops & retention)
| id | item | status | notes |
|---|---|---|---|
| B-10 | "Then/now" animated GIF/WebM export of the compare slider (highly shareable) | todo | canvas capture, ~few sec loop |
| B-11 | Bake remaining Randstad cities 1900 (leiden, delft, haarlem, gouda, dordrecht, amersfoort) as PMTiles z12–16 | todo | tools/bake_pmtiles.py ready; watch repo size (<1 GB) |
| B-12 | Amsterdam full era ladder: add 1815, 2021 archives | todo | completes the time-travel story offline |
| B-13 | More landmarks: Rotterdam (Kiefhoek, Sonneveld House), Utrecht (Werkbond), Hilversum (Zonnestraal, Dudok Raadhuis) | todo | verify coords + PD/CC images via Commons API |
| B-14 | More postcards: Van Gogh (Amsterdam/Otterlo), Frans Hals (Haarlem), Vermeer View of Delft (already?), Mondriaan (Den Haag) | todo | licensing rules in postcards/SOURCING.md |
| B-15 | Wikipedia deep links per landmark (nl/en/zh) | todo | low effort, high credibility |

### P2 — institutional / academic track
| id | item | status | notes |
|---|---|---|---|
| B-20 | `about.html` / colofon: method (RD→3857 reprojection, PMTiles), data sources & licenses, citation block (BibTeX), contact | todo | academics check the colofon first |
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

- **2026-07-03** — Loop bootstrapped. Shipped: og:image (baked-map postcard style),
  twitter cards, canonical, JSON-LD, sitemap.xml (25 URLs), robots.txt, this roadmap,
  outreach drafts (docs/OUTREACH.md). Next: B-4 launch copy pack, B-5 SEO anchors,
  B-10 GIF export. Blockers for owner: B-1 analytics (urgent), B-23, B-30/31.
