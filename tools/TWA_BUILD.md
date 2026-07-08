# Google Play TWA Build Guide

## Prerequisites
- Node.js 18+, Java 11+, Android Studio (or just Android SDK)
- Google Play Developer Account ($25 one-time)
- Keystore file for signing

## Step 1 — Install bubblewrap

```bash
npm install -g @bubblewrap/cli
```

## Step 2 — Init TWA project

Run from a working directory OUTSIDE this repo:

```bash
mkdir twa-build && cd twa-build
bubblewrap init --manifest https://yunching0513.github.io/Netherlands-historical-map/manifest-en.webmanifest
```

Bubblewrap will prompt for:
- **Application ID (package name)**: e.g. `com.yunching.netherlandsmap`  ← remember this
- **App version name / code**: start at `1.0` / `1`
- **Signing key**: create new or use existing keystore

## Step 3 — Fill in assetlinks.json

After init, bubblewrap shows your SHA-256 fingerprint. Copy it into the repo:

```
.well-known/assetlinks.json
```

Replace the two `TODO_` placeholders:
- `package_name`:  the Application ID you chose (e.g. `com.yunching.netherlandsmap`)
- `sha256_cert_fingerprints`: the fingerprint bubblewrap printed (format `AA:BB:CC:...`)

Then commit and push so GitHub Pages serves the file at:
`https://yunching0513.github.io/Netherlands-historical-map/.well-known/assetlinks.json`

**Note for GitHub Pages:** Pages doesn't serve `.well-known/` by default on project pages.
Add a `_config.yml` with:
```yaml
include:
  - .well-known
```

## Step 4 — Build and test

```bash
bubblewrap build
# Produces app-release-signed.apk

# Test on device/emulator before uploading
adb install app-release-signed.apk
```

Verify TWA is working (no browser chrome should be visible — full standalone mode).

## Step 5 — Upload to Google Play

1. Google Play Console → Create app
2. Internal testing → Upload APK/AAB
3. Set content rating, pricing (free), target countries
4. Submit for review (~1-3 days)

## Checklist before submission

- [ ] `assetlinks.json` live at the `.well-known/` URL above
- [ ] PWA passes Chrome Lighthouse PWA audit (score ≥ 90)
- [ ] App works offline (test with airplane mode — PMTiles archives cover Amsterdam/Rotterdam/Den Haag/Utrecht)
- [ ] Privacy policy URL (required by Play Store)
- [ ] Store listing screenshots (Phone + Tablet)
- [ ] All three manifest files (`manifest-nl/en/zh.webmanifest`) accessible

## iOS Capacitor (separate track)

```bash
npm install @capacitor/core @capacitor/ios
npx cap init "Old-Map Stroll" com.yunching.netherlandsmap
npx cap add ios
# Copy index.html + all assets into www/
npx cap sync
npx cap open ios   # opens Xcode
```

In Xcode: set bundle ID, version, signing team, then Archive → Distribute.
Ensure `WKWebView` allows `file://` range requests for PMTiles local files
(Capacitor's WKWebViewEngine handles this by default in Capacitor 5+).
