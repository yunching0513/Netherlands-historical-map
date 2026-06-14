/* Service worker — Oude-Kaart Wandeling door Nederland
 * App-shell wordt vooraf gecached; kaarttegels gaan via het netwerk
 * (network-first met cache-fallback) zodat de kaart offline grofweg blijft werken. */
const SHELL_CACHE = 'nlmaps-shell-v1';
const TILE_CACHE  = 'nlmaps-tiles-v1';

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
    // Network-first, val terug op gecachete tegel; bewaar tot ~600 tegels.
    e.respondWith(
      fetch(req).then(res => {
        if (res && res.ok) {
          const copy = res.clone();
          caches.open(TILE_CACHE).then(c => { c.put(req, copy); trimCache(TILE_CACHE, 600); });
        }
        return res;
      }).catch(() => caches.match(req))
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

async function trimCache(name, max) {
  const c = await caches.open(name);
  const keys = await c.keys();
  if (keys.length > max) {
    for (let i = 0; i < keys.length - max; i++) await c.delete(keys[i]);
  }
}
