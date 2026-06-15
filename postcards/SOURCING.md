# 老照片明信片 · 蔣集指南 · Postcards sourcing guide

把荷蘭各城市的**老照片**做成 app 裡可收集的明信片。
**最高原則：只用版權安全的圖（CC0／公眾領域／CC-BY），逐張確認，並標註來源。**

> ⚠️ 製作者（在沙箱環境）無法連外下載圖片，需由你在有網路的環境蔣集、下載，並透過 **GitHub 網頁介面上傳**（拖放圖檔；二進位圖檔只能這樣進 repo）。

---

## 1. 只用這三類授權

| 授權 | 可用？ | 說明 |
|---|---|---|
| **CC0 / Public Domain（PD）** | ✅ 最佳 | 可自由使用，建議仍標來源 |
| **CC-BY / CC-BY-SA** | ✅ 需標註 | 一定要標作者＋授權＋連結 |
| 「保留所有權利 / © …」 | ❌ 不要 | 多數檔案館掃描屬此類，跳過 |

判斷方法：在每張圖的頁面找 **Rights / Licentie / 授權** 欄位，看到 **CC0 / Publiek domein / Public Domain** 才下載。

---

## 2. 三個來源 + 每座城市的搜尋入口

### A. Rijksstudio（荷蘭國家博物館）— 幾乎全是 CC0
- 入口：`https://www.rijksmuseum.nl/nl/zoeken?q=<城市>+gezicht&st=Objects&ii=0`
- 範例查詢：`Amsterdam gezicht`、`Rotterdam haven`、`Maastricht`、`gezicht op <城市>`
- 篩選：勾選 **「Alleen met afbeelding」** 與可下載；按每張的 **Download** 鈕（CC0）。
- 標註：`Rijksmuseum, Amsterdam · CC0`

### B. Wikimedia Commons — PD / CC，**逐張看授權**
- 入口：`https://commons.wikimedia.org/w/index.php?search=<城市>+history+old+photo`
- 分類常見：`Category:Historical images of <城市>`、`Category:Old photographs of <城市>`
- 只挑授權為 **PD-old / CC0 / CC-BY / CC-BY-SA** 的；下載原圖。
- 標註：`<作者>, via Wikimedia Commons · <授權>`

### C. Nationaal Archief / Het Geheugen — 多為 CC0
- 入口：`https://www.nationaalarchief.nl/onderzoeken/fotocollectie?searchTerm=<城市>`
- **特別推薦：Fotocollectie ANEFO** —— 20 世紀荷蘭新聞照，**整批 CC0**，城市街景很多。
  查詢加上 `Anefo`，例如 `Amsterdam Anefo`。
- Het Geheugen：`https://geheugen.delpher.nl`（搜尋 `<城市>`，看授權）。
- 標註：`Nationaal Archief / Anefo · CC0`

---

## 3. 把一張明信片加進 app 的流程

1. 找到一張 **CC0／PD** 的老照片，記下：標題、年份、來源機構、授權、原始頁面連結。
2. 下載圖檔，建議壓到**長邊 ≤ 1600px、JPG**（明信片不需原始巨檔）。
3. 在 GitHub 網頁：**Add file → Upload files**，上傳到 `postcards/<城市id>/<檔名>.jpg`
   （城市 id 同 app，如 `amsterdam`、`rotterdam`、`maastricht`…）。
4. 在 `postcards/postcards.json` 加一筆（格式見該檔），填好年份／標題／來源／授權／檔名。
5. 告訴我，我把明信片**接進 app 的明信片牆**（顯示、燈箱、版權標註；要做「走到附近自動顯影」也可以，需要填經緯度）。

---

## 4. 命名與數量建議

- 每座城市先 **1–3 張**（街景、地標、運河／港口最有「今昔感」）。
- 檔名用英數小寫，如 `amsterdam/dam-1900.jpg`、`rotterdam/haven-1925.jpg`。
- 年份盡量取**整十年**或照片標註年份，方便和時光滑桿呼應。

有了第一批圖（哪怕先 3–5 張），我就能把明信片功能完整接起來。
