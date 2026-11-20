#!/usr/bin/env node
// Writes the shared calculator block into each service page template, directly after
// section 2 (the problem section, the second <section> in <main>), between
// <!-- tl-calc --> and <!-- /tl-calc -->. Copy and inputs come from js/calculator.js CALCS.
// check-site-consistency.js re-renders every block and fails the build on any drift.
//
//   node scripts/calc-markup.js           update templates/pages, then run build-pages.js
//   require('./calc-markup').render(id)    expected markup for one page
"use strict";
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const ROOT = path.resolve(__dirname, "..");
const JS = path.join(ROOT, "js", "calculator.js");
const calc = require(JS);

// Page file -> calculator id. Pages left out are listed in SKIPPED with the reason.
const PAGES = {
  "missed-call-text-back.html": "missed-call-text-back",
  "ai-receptionist.html": "ai-receptionist",
  "ai-receptionist-for-salons.html": "ai-receptionist-for-salons",
  "google-review-requests.html": "google-review-requests",
  "google-review-requests-for-salons.html": "google-review-requests-for-salons",
  "quote-follow-up-win-back.html": "quote-follow-up-win-back",
  "website-chat-to-text.html": "website-chat-to-text",
  "text-to-pay.html": "text-to-pay",
  "contractor-websites.html": "contractor-websites",
  "lead-follow-up.html": "lead-follow-up",
  "appointment-reminders.html": "appointment-reminders",
  "cold-outreach.html": "cold-outreach",
  "crm-setup.html": "crm-setup",
  "custom-dashboards.html": "custom-dashboards",
  "ai-support-agent.html": "ai-support-agent",
};
const SKIPPED = {
  "index.html": "home routes to several offers; no single service to price",
  "for-home-services.html": "hub page; routes to the offer pages that carry calculators",
  "for-appointment-businesses.html": "hub page; routes to the offer pages that carry calculators",
  "for-law-firms-accountants-and-advisors.html": "hub page; the professional lane already has /ai-exposure-score and /margin-leakage-calculator",
  "ai-governance.html": "risk value would need breach-cost statistics we can't source; /ai-exposure-score already covers it",
  "fractional-ai-officer.html": "engagement price is set per agreement; /margin-leakage-calculator already covers the value case",
};

const CALL = '<a href="tel:+16473605774" class="btn-primary tl-calc-cta" onclick="window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:\'click_to_call\'});">Call (647) 360-5774</a>';
const CONSULT = '<a href="#discovery-form" class="btn-primary gov-form-cta tl-calc-cta" onclick="window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:\'form_cta_click\'});">Book My AI Consultation</a>';

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
const UNIT = {
  n: { pre: "", suf: "" }, pct: { pre: "", suf: "%" }, money: { pre: "$", suf: "" },
  hrs: { pre: "", suf: " hrs" }, min: { pre: "", suf: " min" }, days: { pre: "", suf: " days" },
};

function version() {
  return crypto.createHash("sha256").update(fs.readFileSync(JS)).digest("hex").slice(0, 10);
}

function render(id) {
  const c = calc.CALCS[id];
  if (!c) throw new Error("no calculator " + id);
  const r = calc.result(id, calc.defaults(id));
  // 2026-11-19 3-AI review: "About $X /month is at stake." not "leaving $X on the table".
  const lead = c.lead === undefined ? "About" : c.lead;
  const per = c.per === undefined ? "/month" : c.per;
  const tail = c.tail === undefined ? "is at stake." : c.tail;
  const note = c.note || "An estimate from your numbers only. It shows the value at stake, not what we will recover. Nothing you enter is sent.";
  const fields = c.inputs.map((i, n) => {
    const u = UNIT[i.u];
    const fid = "tlc-" + i.k;
    return [
      '      <div class="tl-calc-field">',
      '        <label class="tl-calc-label" for="' + fid + '">' + esc(i.label) + "</label>",
      '        <div class="tl-calc-row">',
      '          <input type="range" id="' + fid + '" data-k="' + i.k + '" min="' + i.min + '" max="' + i.max + '" step="' + i.step + '" value="' + i.v + '" aria-valuetext="' + esc(u.pre) + i.v + esc(u.suf) + '">',
      '          <span class="tl-calc-box">' + (u.pre ? '<span class="tl-calc-pre" aria-hidden="true">' + esc(u.pre) + "</span>" : "") +
        '<input type="number" data-k="' + i.k + '" min="' + i.min + '" max="' + i.max + '" step="' + i.step + '" value="' + i.v + '" inputmode="decimal" aria-label="' + esc(i.label) + '"' + (u.pre ? ' data-prefix="' + esc(u.pre) + '"' : "") + (u.suf ? ' data-suffix="' + esc(u.suf) + '"' : "") + ">" +
        (u.suf ? '<span class="tl-calc-suf" aria-hidden="true">' + esc(u.suf.trim()) + "</span>" : "") + "</span>",
      "        </div>",
      "      </div>",
    ].join("\n");
  }).join("\n");
  return [
    "<!-- tl-calc -->",
    '<section class="tl-calc-section" data-calc="' + id + '" aria-labelledby="tl-calc-title">',
    '  <div class="tl-calc">',
    '    <h2 class="tl-calc-title" id="tl-calc-title">' + esc(c.title) + "</h2>",
    '    <p class="tl-calc-intro">Move the sliders or type your own numbers. The starting numbers are example inputs you can change.</p>',
    '    <div class="tl-calc-grid">',
    '    <div class="tl-calc-inputs">',
    fields,
    "    </div>",
    '    <div class="tl-calc-result">',
    '      <p class="tl-calc-lead">' + esc(lead) + "</p>",
    '      <p class="tl-calc-big" aria-live="polite" aria-atomic="true"><span data-out="main">' + r.mainText + "</span>" + (per ? '<span class="tl-calc-per">' + esc(per) + "</span>" : "") + "</p>",
    tail ? '      <p class="tl-calc-tail">' + esc(tail) + "</p>" : null,
    '      <p class="tl-calc-sub" data-out="sub">' + esc(r.sub) + "</p>",
    '      <p class="tl-calc-formula"><span>How it works:</span> ' + esc(c.formula) + "</p>",
    '      <p class="tl-calc-note">' + esc(note) + "</p>",
    "      " + (c.cta === "consult" ? CONSULT : CALL),
    "    </div>",
    "    </div>",
    "  </div>",
    '  <script src="/js/calculator.js?v=' + version() + '" defer></script>',
    "</section>",
    "<!-- /tl-calc -->",
  ].filter((x) => x !== null).join("\n");
}

// Index just after the end of the second <section> inside <main>.
function afterSection2(html) {
  const main = html.indexOf("<main");
  const re = /<section\b|<\/section>/g;
  re.lastIndex = main;
  let depth = 0, top = 0, m;
  while ((m = re.exec(html))) {
    if (m[0] === "</section>") { depth--; if (depth === 0 && top === 2) return m.index + m[0].length; }
    else { if (depth === 0) top++; depth++; }
  }
  throw new Error("no second section");
}

function apply(html, id) {
  const block = render(id);
  html = html.replace(/\n?<!-- tl-calc -->[\s\S]*?<!-- \/tl-calc -->\n?/, "\n");
  const at = afterSection2(html);
  return html.slice(0, at) + "\n\n" + block + "\n" + html.slice(at).replace(/^\n+/, "\n");
}

module.exports = { PAGES, SKIPPED, render, afterSection2, version };

if (require.main === module) {
  for (const [f, id] of Object.entries(PAGES)) {
    const p = path.join(ROOT, "templates", "pages", f);
    const before = fs.readFileSync(p, "utf8");
    const after = apply(before, id);
    if (after !== before) fs.writeFileSync(p, after);
    console.log("calc-markup: " + f + " -> " + id);
  }
}
