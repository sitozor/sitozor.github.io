// Russian root page only: send visitors whose browser prefers another language to /en/
// once, unless they picked a language before. Crawlers are never redirected.
(function () {
  var saved = null;
  try { saved = localStorage.getItem("lang"); } catch (e) {}
  if (/bot|crawl|spider|slurp|yandex|google|bing|duckduck/i.test(navigator.userAgent)) return;
  var preferred = (navigator.languages && navigator.languages[0]) || navigator.language || "";
  if (saved === "en" || (!saved && preferred && !/^ru\b/i.test(preferred))) {
    location.replace("/en/" + location.hash);
  }
})();
