/* Google Ads phone-click conversion (AW-18016129581). Fires on any tel: link click.
   Non-blocking: does not preventDefault or delay the tel: navigation. */
(function () {
  var SEND_TO = 'AW-18016129581/uiT3COvGwZodEK2k4Y5D';
  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest ? e.target.closest('a[href^="tel:"]') : null;
    if (!a) return;
    try {
      if (typeof window.gtag === 'function') {
        window.gtag('event', 'conversion', {
          send_to: SEND_TO, value: 1.0, currency: 'CAD', transport_type: 'beacon'
        });
      }
    } catch (err) {}
  }, true);
})();
