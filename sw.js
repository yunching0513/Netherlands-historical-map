/* Kill switch — verwijdert zichzelf en wist alle caches.
 * Tijdelijk: offline-cache is uitgeschakeld terwijl we de kaart afronden. */
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => {
  e.waitUntil((async () => {
    for (const k of await caches.keys()) await caches.delete(k);
    await self.registration.unregister();
    for (const c of await self.clients.matchAll()) c.navigate(c.url);
  })());
});
