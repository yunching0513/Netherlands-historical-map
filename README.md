# 荷蘭古地圖散策 · Oude-Kaart Wandeling door Nederland

> **把 1815 年以來的荷蘭歷史地圖，疊在今日的街道上。**
> Schuif door twee eeuwen Nederlandse topografische kaarten, over de straten van vandaag.

一個單頁、免安裝的網頁應用：拉動時間滑桿，從 **1815 年**走到 **2023 年**，看你腳下的荷蘭城市如何在運河、圳田與鐵路之間慢慢長成今天的樣子。仿照 [taiwan-historical-maps](https://github.com/yunching0513/taiwan-historical-maps) 的歷史疊圖架構，換上荷蘭的圖資。

## ✨ 特色 · Functies

- 🗺️ **兩世紀時光滑桿**：荷蘭國家地形圖（[Topotijdreis](https://www.topotijdreis.nl) / Kadaster）1815→2023，逐年疊在現代街道上
- 🧭 **三種底圖**：PDOK BRT 街道圖、灰階圖、實景空照（Luchtfoto），無法連線時自動退回 CartoDB
- ↔️ **今昔對照**：拖曳分隔線左右滑動，比對 **TOEN / NU**（昔 / 今）
- 📍 **GPS 定位**：在荷蘭實地散步時定位自己，看百年前同一地點的模樣
- 🏙️ **20 座城市快速跳轉**：阿姆斯特丹、鹿特丹、海牙、烏特勒支、萊頓、台夫特、馬斯特里赫特……
- 🌗 **紙色／墨色雙主題**，可深連結 `?city=&year=`
- 🌏 **三語介面**：Nederlands · English · 繁體中文
- 📱 **PWA 免安裝**：開瀏覽器就能用，也可裝成手機 App，圖磚離線快取

## 結構 · Structuur

```
netherlands-historical-map/
├── index.html             # 全部的應用程式（HTML + CSS + JS，單檔）
├── manifest.webmanifest   # PWA 應用程式清單
├── sw.js                  # Service worker（離線快取）
├── privacy.html           # 隱私權說明
├── icons/                 # 應用程式圖示（SVG）
└── .nojekyll
```

單一 HTML 檔，**無需 build、無需 npm install**。Leaflet 透過 CDN 載入，歷史圖磚直接打 Topotijdreis tile server，底圖打 PDOK。

## 使用 · Gebruik

直接用瀏覽器打開 `index.html`，或用本地 server：

```bash
python3 -m http.server 8000   # 開 http://localhost:8000
```

部署到 GitHub Pages 即可（已含 `.nojekyll`）。

### 深連結 · Deep link

```
index.html?city=amsterdam&year=1900
index.html?city=maastricht&year=1850
```

## 圖資來源 · Bronnen

| 圖層 | 來源 | 授權 |
|------|------|------|
| 歷史地形圖 1815–heden | [Topotijdreis](https://www.topotijdreis.nl) · Kadaster | CC BY 4.0 |
| 街道／灰階底圖（BRT） | [PDOK](https://www.pdok.nl) · Kadaster | open data |
| 空照圖（Luchtfoto） | [PDOK](https://www.pdok.nl) · Beeldmateriaal Nederland | open data |
| 退回底圖 | OpenStreetMap · CARTO | ODbL |

歷史地圖由荷蘭土地測量局（**Kadaster**）透過 Topotijdreis 計畫提供，包含：

- **TMK** — Topographische en Militaire Kaart 1:50.000（1815–1854）
- **Bonnebladen** — 1:25.000 套色地形圖（1855–1933）
- **Topografische kaart** 1:25.000（1934–1990）
- **Actuele topografie**（1991–heden）

## 設計 · Ontwerp

沿用《昃慶手拙》個人設計風格：清水混凝土系灰階配朱（vermilion `#C15F3C`）單一強調色，Noto Serif TC + EB Garamond italic + JetBrains Mono 三套字體。

---

設計・製作 · Ontwerp & bouw — [吳昃慶 Yunching Wu](https://github.com/yunching0513)
