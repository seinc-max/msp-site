/* Cookie choice banner (self-hosted, no third party, no cost).
   Google Consent Mode v2: the inline snippet in every page <head> sets the consent
   default BEFORE Google Tag Manager loads (granted, or denied if the visitor declined
   earlier). This file shows the banner until the visitor chooses, and applies the choice.
   Decline: denies analytics_storage, ad_storage, ad_user_data, ad_personalization,
   stops Microsoft Clarity, PostHog and HubSpot tracking now, and the head snippets skip loading them on
   later pages. The choice is kept in localStorage key "tl_consent". */
(function () {
  var KEY = 'tl_consent';
  var KEYS = ['analytics_storage', 'ad_storage', 'ad_user_data', 'ad_personalization'];
  function store(v) { try { localStorage.setItem(KEY, v); } catch (e) {} window.__tlConsent = v; }
  function read() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function gtagSafe() {
    window.dataLayer = window.dataLayer || [];
    if (typeof window.gtag !== 'function') window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag.apply(null, arguments);
  }
  function apply(v) {
    var state = {};
    KEYS.forEach(function (k) { state[k] = v === 'denied' ? 'denied' : 'granted'; });
    gtagSafe('consent', 'update', state);
    window.dataLayer.push({ event: 'tl_consent_' + (v === 'denied' ? 'denied' : 'granted') });
    try { window._hsq = window._hsq || []; window._hsq.push(v === 'denied' ? ['doNotTrack'] : ['doNotTrack', { track: true }]); } catch (e) {}
    if (v === 'denied') {
      try { if (typeof window.clarity === 'function') { window.clarity('consent', false); window.clarity('stop'); } } catch (e) {}
      try { if (window.posthog && typeof window.posthog.opt_out_capturing === 'function') window.posthog.opt_out_capturing(); } catch (e) {}
    }
  }
  var css = '#tl-consent{position:fixed;left:12px;right:12px;bottom:12px;z-index:10000;max-width:560px;margin:0 auto;' +
    'background:#fff;color:#1f2937;border:1px solid #cbd5e1;border-radius:8px;padding:10px 12px;box-sizing:border-box;' +
    'font:14px/1.4 "DM Sans","DM Sans Fallback",system-ui,sans-serif;display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px}' +
    '#tl-consent p{margin:0;flex:1 1 220px}#tl-consent a{color:#1d4ed8;text-decoration:underline}' +
    '#tl-consent .tl-consent-btns{display:flex;gap:8px;flex:0 0 auto}' +
    '#tl-consent button{font:inherit;font-weight:600;min-height:40px;min-width:88px;padding:6px 14px;border-radius:6px;cursor:pointer;' +
    'border:1px solid #1f2937;background:#fff;color:#1f2937}' +
    '#tl-consent button:focus-visible{outline:2px solid #1d4ed8;outline-offset:2px}@media print{#tl-consent{display:none}}';
  function place(box) {
    var bar = document.querySelector('.sticky-mobile-cta');
    var off = 12;
    if (bar) {
      var cs = getComputedStyle(bar);
      if (cs.display !== 'none' && cs.visibility !== 'hidden' && cs.position === 'fixed') {
        var r = bar.getBoundingClientRect();
        if (r.height > 0 && r.top < window.innerHeight) off = Math.ceil(window.innerHeight - r.top) + 8;
      }
    }
    box.style.bottom = off + 'px';
  }
  function show() {
    if (document.getElementById('tl-consent')) return;
    if (!document.getElementById('tl-consent-css')) {
      var st = document.createElement('style'); st.id = 'tl-consent-css'; st.textContent = css; document.head.appendChild(st);
    }
    var box = document.createElement('div');
    box.id = 'tl-consent'; box.setAttribute('role', 'region'); box.setAttribute('aria-label', 'Cookie choice');
    box.innerHTML = '<p>This site uses cookies for analytics and ads. <a href="/privacy#cookies">Learn more</a></p>' +
      '<div class="tl-consent-btns"><button type="button" data-tl-choice="granted">Accept</button>' +
      '<button type="button" data-tl-choice="denied">Decline</button></div>';
    box.addEventListener('click', function (e) {
      var b = e.target.closest ? e.target.closest('[data-tl-choice]') : null;
      if (!b) return;
      var v = b.getAttribute('data-tl-choice');
      store(v); apply(v);
      window.removeEventListener('resize', onResize);
      box.parentNode && box.parentNode.removeChild(box);
    });
    document.body.appendChild(box);
    var onResize = function () { place(box); };
    place(box);
    window.addEventListener('resize', onResize);
  }
  function init() {
    if (!read()) show();
    document.addEventListener('click', function (e) {
      var t = e.target.closest ? e.target.closest('[data-tl-consent-open]') : null;
      if (t) { e.preventDefault(); show(); }
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
