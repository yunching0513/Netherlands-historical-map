# HANDOFF — 荷蘭古地圖散策 / Oude-Kaart Wandeling door Nederland

> 給下一個 Claude Code session 的交接筆記。**請先讀完這份再動工。**
> 使用者以**繁體中文**溝通、且非工程背景：回覆請用繁中、步驟要簡單、能自動做的就自動做。
> 使用者很在意**版權**：只用 Public Domain / CC0；每張圖都要顯示來源與授權。

Live: https://yunching0513.github.io/Netherlands-historical-map/
Repo: `yunching0513/netherlands-historical-map`，部署分支 **main**（GitHub Pages：Deploy from a branch → main / root）。

---

## 立刻先做：確認網路出口已開
使用者剛把環境 network egress 改成 Custom/Full，加入 `*.wikimedia.org`（+ rijksmuseum）。
**第一步在新 session 重測**：
```
curl -s -o /dev/null -w "%{http_code}\n" "https://commons.wikimedia.org/w/api.php?action=query&format=json&meta=siteinfo"
```
- 200 → 可以開始抓圖。
- 403「Host not in allowlist」→ egress 還沒生效，請使用者確認改的是**這個環境**、選 Full/Custom 並 Save，必要時再開一個新 session。

---

## 部署方式（重要，務必照做）
- **這個沙箱沒有 git push 憑證**。所有提交用 **GitHub MCP 工具**（`mcp__github__push_files` / `create_or_update_file`）直接推到遠端 **main**。
- `index.html` 是**單一自包含檔（~48KB）**。要改它就得用 push_files **重送整份檔**（純文字）。
- **每次推完都要驗證**：curl `https://raw.githubusercontent.com/yunching0513/Netherlands-historical-map/main/index.html` → 抽出 `<script>` → `node --check` → 檢查 i18n 三語齊全、關鍵字串沒亂碼。
- **二進位圖檔（jpg/png）不能用 MCP 工具 commit（會壞）**。圖片只能：(a) **hotlink** 外部 CORS 友善來源（Wikimedia `upload.wikimedia.org` 有 CORS，OK），或 (b) 請使用者用 GitHub 網頁上傳。
- 本機 `/home/user/nl-map` 可能過時，以**遠端 main 為準**（`git fetch origin main && git reset --hard origin/main`）。

## 架構事實（別重推導）
- 地圖 **EPSG:3857 Web Mercator**；Leaflet 1.9.4 + **proj4**（沒用 proj4leaflet）。
- 底圖（PDOK, 3857）：`brt`(街道)、`grijs`(簡圖，**預設**)、`luchtfoto`(空照)。
- 歷史圖層：Kadaster/Esri-NL ArcGIS `Historische_tijdreis_<year>`，**只有 RD(EPSG:28992) 網格**；用自訂 canvas GridLayer `createTopotijdreisLayer(serviceId, opts)` 逐塊從 RD 重投影到 3857。RD 參數：origin `[-30515500, 31112400]`、12 級解析度（level 0–11，最細 1.5875 m/px）。tile URL：`https://tiles.arcgis.com/tiles/nSZVuSZjHpEZZbRo/arcgis/rest/services/Historische_tijdreis_<id>/MapServer/tile/{z}/{y}/{x}`。
- 年份滑桿 1815–2021，吸附到 `AVAIL` 裡 ~90 個真實年份（含 `1823_1829` 這種區段），用 `nearestService(year)`。
- **Service worker 已停用**（sw.js 是 kill switch；index.html 會 unregister SW 並清快取）。沒理由別重開。
- i18n：`I18N` 物件含 nl/en/zh；**每個 `data-i18n` 與 `t('...')` 的 key 三語都要有**。作者名字必須是 **吳昀慶**（昀 = U+6600，不是 昃 U+6603）。
- main 上檔案：index.html, manifest.webmanifest, sw.js, privacy.html, credits.html, banner.svg, icons/(svg), postcards/(postcards.json, SOURCING.md), .nojekyll, README.md。

---

## 目前任務：荷蘭名畫明信片 (Dutch masterpiece postcards)
把重要荷蘭藝術家的**名畫**（畫家過世數百年 → **公眾領域 PD**）做成 app 裡每座城市可收集的「明信片」。

### 做法
1. 用 **Wikimedia Commons API**（`action=query&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth=1000`）找每張畫的檔案，**驗證授權**：看 `extmetadata.LicenseShortName` / `extmetadata.PermissionScore`，**只收 Public Domain / PD / CC0**。擷取：縮圖 URL（`thumburl`，寬約 800–1200）、Artist、標題、年代、Credit、授權、Commons 檔案頁連結。
2. 把畫對應到城市（清單見下）。
3. 寫進 `postcards/postcards.json` 的 `items[]`：`img` 直接放 `upload.wikimedia.org` 的縮圖網址（hotlink），填 credit/license/sourceUrl，**只放 PD**。
4. 在 `index.html` 加「**明信片牆**」：面板新增一段，每城顯示該城明信片縮圖，點開**燈箱**顯示 圖＋標題＋年代＋畫家＋來源＋授權。GPS「走到附近自動顯影」為**選配**（postcards.json 已有 lat/lng）；**做之前先問使用者要 GPS 收集版還是單純展示版**。
5. 照「部署方式」推送並驗證。

### 城市 ↔ 名畫起始清單（皆 PD；每張再確認 Commons 實際檔名）
- **amsterdam**：Rembrandt — The Night Watch (1642)；Vermeer — The Milkmaid (~1660)
- **delft**：Vermeer — View of Delft (~1660–61)；Vermeer — The Little Street (Het Straatje)
- **denhaag**：Vermeer — Girl with a Pearl Earring；Rembrandt — The Anatomy Lesson of Dr Nicolaes Tulp（Mauritshuis）
- **haarlem**：Frans Hals — 民兵連宴會群像；Jacob van Ruisdael — View of Haarlem
- **denbosch**：Hieronymus Bosch — The Garden of Earthly Delights（波希為當地人）
- **rotterdam**：Pieter Bruegel the Elder — The Tower of Babel（Boijmans）
- **eindhoven**：Van Gogh — The Potato Eaters (1885，鄰近 Nuenen 所繪)
- **leiden**：Rembrandt 早期作；Jan Steen 風俗畫
- **zwolle / kampen 一帶**：Hendrick Avercamp — Winter Landscape with Ice Skaters
- **utrecht**：Gerard van Honthorst / Hendrick ter Brugghen（Utrecht 卡拉瓦喬畫派）
- **dordrecht**：Aelbert Cuyp — 河岸風景
（其餘城市可挑合適 PD 作品或先略過。）

每張明信片標註格式建議：`畫家, 標題 (年代) — 館藏 · Public Domain, via Wikimedia Commons` + Commons 檔案頁連結。
