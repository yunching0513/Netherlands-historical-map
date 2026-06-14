/* Service worker — Oude-Kaart Wandeling door Nederland
 * App-shell wordt vooraf gecached. Kaarttegels gebruiken stale-while-revalidate:
 * eerder geziene tegels komen direct uit de cache (snel), terwijl ze op de
 * achtergrond ververst worden. Historische kaarten veranderen toch niet. */
const SHELL_CACHE = 'nlmaps-shell-v2';
const TILE_CACHE  = 'nlmaps-tiles-v2';
const TILE_MAX    = 1200;

const SHELL = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icon.svg',
  'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',
  'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(SHELL_CACHE)
      .then(c => Promise.allSettled(SHELL.map(u => c.add(u))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.filter(k => k !== SHELL_CACHE && k !== TILE_CACHE).map(k => caches.delete(k))
    )).then(() => self.clients.claim())
  );
});

function isTile(url) {
  return /topotijdreis\.nl|service\.pdok\.nl|basemaps\.cartocdn\.com|tile\.openstreetmap/.test(url);
}

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = req.url;

  if (isTile(url)) {
    // Stale-while-revalidate: cache eerst (snel), op de achtergrond verversen.
    e.respondWith(
      caches.open(TILE_CACHE).then(cache =>
        cache.match(req).then(cached => {
          const fetching = fetch(req).then(res => {
            if (res && res.ok) { cache.put(req, res.clone()); trimCache(cache); }
            return res;
          }).catch(() => cached);
          return cached || fetching;
        })
      )
    );
    return;
  }

  // App-shell: cache-first.
  e.respondWith(
    caches.match(req).then(hit => hit || fetch(req).then(res => {
      if (res && res.ok && (url.startsWith(self.location.origin) || url.indexOf('unpkg.com') > -1)) {
        const copy = res.clone();
        caches.open(SHELL_CACHE).then(c => c.put(req, copy));
      }
      return res;
    }).catch(() => caches.match('./index.html')))
  );
});

async function trimCache(cache) {
  const keys = await cache.keys();
  if (keys.length > TILE_MAX) {
    for (let i = 0; i < keys.length - TILE_MAX; i++) await cache.delete(keys[i]);
  }
}
