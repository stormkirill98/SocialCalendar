/**
 * Welcome to your Workbox-powered service worker!
 *
 * You'll need to register this file in your web app and you should
 * disable HTTP caching for this file too.
 * See https://goo.gl/nhQhGp
 *
 * The rest of the code is auto-generated. Please don't update this file
 * directly; instead, make changes to your Workbox build configuration
 * and re-run your build process.
 * See https://goo.gl/2aRDsh
 */

importScripts("https://storage.googleapis.com/workbox-cdn/releases/4.3.1/workbox-sw.js");

importScripts(
<<<<<<< HEAD
  "/precache-manifest.afc9edffee1dad3b5353dd60524dfafc.js"
=======
<<<<<<< HEAD
  "/precache-manifest.3fdce86dc1997fb27c5ac405df84a440.js"
=======
<<<<<<< HEAD
  "/precache-manifest.b200a04fcf3700d8c39c74a1ada96045.js"
=======
<<<<<<< HEAD
  "/precache-manifest.d94400f2545df0fbfe1f129359a8aaf6.js"
=======
  "/precache-manifest.5e450c431dd006e70e38e7fe5a0e3eee.js"
>>>>>>> 47a862af6bae75c3923dc1bd605ed67a0da7ad96
>>>>>>> 22e5b7aa12248a536b873a6b5e2b8ca9972eda96
>>>>>>> 3654aaedbdee393a3f084dbb2590479df7a3946e
>>>>>>> 7a5a8052641c8f891d098f236ff4bd1f98a0750b
);

self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

workbox.core.clientsClaim();

/**
 * The workboxSW.precacheAndRoute() method efficiently caches and responds to
 * requests for URLs in the manifest.
 * See https://goo.gl/S9QRab
 */
self.__precacheManifest = [].concat(self.__precacheManifest || []);
workbox.precaching.precacheAndRoute(self.__precacheManifest, {});

workbox.routing.registerNavigationRoute(workbox.precaching.getCacheKeyForURL("/index.html"), {
  
  blacklist: [/^\/_/,/\/[^/?]+\.[^/]+$/],
});
