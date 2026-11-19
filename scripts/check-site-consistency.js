#!/usr/bin/env node
// Cross-page consistency guard (RCA menu-guarantee-consistency-20261119).
// Ben 2026-11-19: the guarantee badge differed across pages and many pages
// shipped without the menu. This script fails the build/release when shared
// elements differ across the pages build-dist ships.
//
// Fails (exit 1) when any shipped HTML page:
// - lacks the full home nav: same link set as index.html's nav (all Services
//   entries incl. the 6 new pages), no tl-nav-gated, and one nav CTA;
// - has a guarantee badge whose text is not exactly CANON_BADGE;
// - contains a banned phrase (BANNED) anywhere in shipped text files, or a
//   banned hero lead-in (BANNED_HERO, e.g. "For trades.");
// - has a repeated hero element that differs from the site majority:
//   cancel line, price-line format, hero call button text;
// - has a "call and hang up" test prompt (BANNED_HANGUP);
// - claims texts come from the client's own number (BANNED_SENDER);
// - has a sample figcaption that is not italic or does not start "Just a sample";
// - has a tel: link other than tel:+16473605774;
// - is a call-only landing page (body.landing-call) without exactly one call line
//   (<p class="call-line">) directly above its hero call button, under 12 words,
//   different from the H1 and sub, and unique across pages (Ben t1215u/t1216u);
// - has a call line anywhere else;
// - says "under a sink" (Ben t1202u: trade-inclusive wording);
// - speaks about the visitor in the third person in landing copy outside the
//   sample mockups (heuristic THIRD_PERSON list, Ben t1223u);
// - has a service-page calculator that differs from scripts/calc-markup.js, sits anywhere
//   but directly after section 2, has the wrong CTA, or js/calculator.js fails its tests.
//
//   node scripts/check-site-consistency.js            check repo root pages
//   node scripts/check-site-consistency.js <dir>      check a built folder (e.g. dist)
"use strict";
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const DIR = path.resolve(process.argv[2] || ROOT);
const MANIFEST = path.join(__dirname, "dist-manifest.txt");

const CANON_BADGE = "✓ 30-day money-back guarantee";
const TEL = "tel:+16473605774";
const CAPTION_START = "Just a sample";
const NEW_PAGES = ["/lead-follow-up", "/appointment-reminders", "/cold-outreach", "/crm-setup", "/custom-dashboards", "/multi-location"];
// Ben 2026-11-19 t1207u: no "per location" anywhere on the site.
const BANNED = [/per[\s\u00a0-]+location/i,
  // Ben 2026-11-19 t1202u: copy must include all trades; no single-trade "under a sink" image.
  /under (?:a|the) sink/i];
// Ben 2026-11-19 t1223u: landing copy speaks to the visitor as "you". Heuristic only:
// these phrases describe the visitor in the third person. Checked on landing pages
// (body.landing-*) in visible copy, FAQ JSON-LD and meta descriptions, after removing
// the sample mockups (<figure>, sample-call partials) where a fake customer talks.
const THIRD_PERSON = [
  /\b(?:owners?|business owners?|contractors|buyers|teams|trades|salons|clinics|shops) (?:who|that|whose|with|using|ready|happy|opening|without)\b/i,
  /\bbusinesses (?:that (?:want|need|already|pay|take|send|use)|whose|using|ready|happy|opening|without|with (?:one|an?|two))\b/i,
  /\b(?:the|an?) owner\b(?! of)/i,
  /\bwork(?:s)? directly with owners\b/i,
  /\btheir (?:customers|clients|business|software|booking software|field-service software|ads)\b/i,
  /\bthey (?:miss|own|lose)\b/i,
  /\b(?:anyone|buyers?) who (?:wants?|needs?|only)\b/i,
];
// Lines that match a heuristic but are not about the visitor. Keep short; each needs a reason.
const THIRD_PERSON_OK = [
  /The owner asks whether the ticket was opened/, // ai-support-agent: the property owner is the client's customer
  /Firms that bill for the work/,                 // law hub: a label for a group of business types
  /answer to the owner, and the file/,            // law hub: the owner is the client whose file it is
];
// Ben 2026-11-19 t1214u: no "call and hang up" test prompts. Only the problem line
// "Many hang up instead of leaving a voicemail" (callers' behaviour) is allowed.
const BANNED_HANGUP = /\bhang[\s\u00a0-]+up\b/gi;
const HANGUP_OK = /Many hang up instead of leaving a voicemail/;
// Ben 2026-11-19 t1208u: no "For trades." lead-in in the top hero.
const BANNED_HERO = [/>\s*For trades(?: on the job)?[.,]/i];
// Ben 2026-11-19 t1213u: texts come from a SEPARATE number, never the client's own.
// Lines only about forwarding the client's calls are allowed (no text/reply/link/request wording).
const BANNED_SENDER = [
  /\b(?:from|on|via) your (?:business|own|existing) number\b/i,
  /\b(?:texts?|texted|reply|replies|messages?|links?|requests?|chats?|invoices?)\b[^.<"]{0,60}\b(?:from|on|via) (?:your number|the number you already use)\b/i,
  /\ball on the number you already use\b/i,
];
// Approved per-page differences in the price-line format. Keep this list short.
// Each is an approved offer shape (Ben-approved prices), not a wording drift.
const PRICE_FORMAT_EXCEPTIONS = {
  "contractor-websites.html": "<strong>$N/mo</strong>. No setup fee.",
  "custom-dashboards.html": "<strong>$N/mo</strong> +&nbsp;$N&nbsp;build.",
  "multi-location.html": "<strong>$N/mo</strong> for each location +&nbsp;$N&nbsp;setup.<span class=\"hero-price-sub\">Charged on top of the services you run.</span>",
};

const files = fs.readFileSync(MANIFEST, "utf8").split("\n").map((s) => s.trim()).filter(Boolean);
const pages = files.filter((f) => f.endsWith(".html"));
const textFiles = files.filter((f) => /\.(html|txt|xml)$/.test(f));
const errors = [];
const err = (f, m) => errors.push(f + ": " + m);
const read = (f) => fs.readFileSync(path.join(DIR, f), "utf8");
const decode = (s) => s.replace(/&nbsp;/g, " ").replace(/&amp;/g, "&").replace(/\s+/g, " ").trim();

function navOf(html) {
  const m = html.match(/<nav class="tl-nav[^"]*"[\s\S]*?<\/nav>/);
  return m ? m[0] : "";
}
function navLinks(nav) {
  const m = nav.match(/<div class="nav-links">[\s\S]*<\/details>\s*<\/div>/);
  if (!m) return null;
  return [...new Set([...m[0].matchAll(/href="([^"]+)"/g)].map((x) => x[1]))].sort();
}

// 1. Nav parity with home.
const homeNav = navOf(read("index.html"));
const homeLinks = navLinks(homeNav);
if (!homeLinks) err("index.html", "home nav has no nav-links block");
for (const n of NEW_PAGES) if (homeLinks && !homeLinks.includes(n)) err("index.html", "Services menu missing " + n);
for (const f of pages) {
  const nav = navOf(read(f));
  if (!nav) { err(f, "no <nav class=\"tl-nav\">"); continue; }
  if (/tl-nav-gated/.test(nav)) err(f, "nav is gated (menu hidden)");
  const links = navLinks(nav);
  if (!links) { err(f, "nav has no Services menu (nav-links/details)"); continue; }
  if (homeLinks && links.join("|") !== homeLinks.join("|")) {
    const miss = homeLinks.filter((l) => !links.includes(l));
    const extra = links.filter((l) => !homeLinks.includes(l));
    err(f, "nav links differ from home. Missing [" + miss.join(", ") + "] Extra [" + extra.join(", ") + "]");
  }
  const ctas = (nav.match(/class="nav-cta/g) || []).length;
  if (ctas !== 1) err(f, "nav must have exactly one nav-cta, found " + ctas);
}

// 2. Guarantee badge, banned phrases, tel links, collected hero elements.
const groups = { cancel: {}, priceFormat: {}, heroCall: {} };
const add = (g, key, f) => { (groups[g][key] = groups[g][key] || []).push(f); };
for (const f of textFiles) {
  const raw = read(f);
  const text = raw.replace(/<[^>]+>/g, " ");
  for (const m of text.matchAll(BANNED_HANGUP)) {
    const around = text.slice(Math.max(0, m.index - 10), m.index + 50);
    if (!HANGUP_OK.test(around)) err(f, "banned test prompt \"" + around.replace(/\s+/g, " ").trim() + "\"");
  }
  for (const re of BANNED_SENDER) {
    const m = text.match(re);
    if (m) err(f, "sender claim \"" + m[0] + "\" (texts come from a separate number)");
  }
  for (const re of BANNED) {
    const m = text.match(re) || raw.match(re);
    if (m) err(f, "banned phrase \"" + m[0] + "\"");
  }
}
for (const f of pages) {
  const html = read(f);
  for (const m of html.matchAll(/✓\s*30-day money-back guarantee[^<]*/g)) {
    if (decode(m[0]) !== CANON_BADGE) err(f, "guarantee badge \"" + decode(m[0]) + "\" is not \"" + CANON_BADGE + "\"");
  }
  for (const m of html.matchAll(/<p class="(?:hero-guarantee|guarantee-line)"[^>]*>([\s\S]*?)<\/p>/g)) {
    const t = decode(m[1].replace(/<[^>]+>/g, ""));
    if (t !== CANON_BADGE) err(f, "guarantee badge \"" + t + "\" is not \"" + CANON_BADGE + "\"");
  }
  // Ben 2026-11-19 t1209u/t1212u: every sample caption is italic and starts "Just a sample".
  for (const c of html.matchAll(/<figcaption[^>]*>([\s\S]*?)<\/figcaption>/g)) {
    const inner = c[1].trim();
    const t = decode(inner.replace(/<[^>]+>/g, ""));
    if (!/^<em>[\s\S]*<\/em>$/.test(inner) || !t.startsWith(CAPTION_START)) err(f, "sample caption \"" + t + "\" must be italic (<em>) and start \"" + CAPTION_START + "\"");
  }
  const hero = (html.match(/<section class="(?:hero|hub-hero)[^"]*"[\s\S]*?<\/section>/) || [""])[0];
  for (const re of BANNED_HERO) { const m = hero.match(re); if (m) err(f, "hero has banned lead-in \"" + m[0].replace(/^>\s*/, "") + "\""); }
  for (const m of html.matchAll(/href="(tel:[^"]*)"/g)) if (m[1] !== TEL) err(f, "tel link " + m[1]);
  for (const m of html.matchAll(/<p class="hero-cancel">([\s\S]*?)<\/p>/g)) add("cancel", decode(m[1]), f);
  for (const m of html.matchAll(/<p class="hero-price-note">([\s\S]*?)<\/p>/g)) {
    const fmt = m[1].trim().replace(/\$[\d,]+/g, "$N");
    if (PRICE_FORMAT_EXCEPTIONS[f] === fmt) continue;
    if (!/\$N/.test(fmt)) continue; // text-only price notes on professional pages are not the $ price line
    add("priceFormat", fmt.replace(/<span class="hero-price-sub">[\s\S]*?<\/span>/, ""), f);
  }
  for (const m of html.matchAll(/<a [^>]*class="hero-call[^"]*"[^>]*>([\s\S]*?)<\/a>/g)) add("heroCall", decode(m[1].replace(/<[^>]+>/g, "")), f);
}

// 4. Call line (Ben t1215u/t1216u) and second person (Ben t1223u).
const callLines = {};
for (const f of pages) {
  const html = read(f);
  const body = (html.match(/<body[^>]*class="([^"]*)"/) || [, ""])[1];
  const all = [...html.matchAll(/<p class="call-line">([\s\S]*?)<\/p>/g)];
  const hero = (html.match(/<section class="(?:hero|hub-hero)[^"]*"[\s\S]*?<\/section>/) || [""])[0];
  if (/\blanding-call\b/.test(body)) {
    const m = hero.match(/<p class="call-line">([^<]*)<\/p>\s*(<a href="tel:\+16473605774" class="hero-call"|<a class="hub-cta" href="tel:\+16473605774"|<div class="hero-actions">\s*<a href="tel:\+16473605774")/);
    if (all.length !== 1 || !m) err(f, "needs exactly one <p class=\"call-line\"> directly above the hero call button (found " + all.length + ")");
    if (m) {
      const t = decode(m[1]);
      const words = t.split(" ").filter(Boolean).length;
      if (words >= 12) err(f, "call line has " + words + " words (must be under 12): \"" + t + "\"");
      const h1 = decode((hero.match(/<h1[^>]*>([\s\S]*?)<\/h1>/) || [, ""])[1].replace(/<[^>]+>/g, ""));
      const sub = decode((hero.match(/<p class="(?:hero-sub|subhead)"[^>]*>([\s\S]*?)<\/p>/) || [, ""])[1].replace(/<[^>]+>/g, ""));
      if (t === h1 || t === sub) err(f, "call line repeats the H1 or sub");
      if (!/\byou(?:r|'re|'ve)?\b/i.test(t)) err(f, "call line must speak to the visitor (you/your): \"" + t + "\"");
      (callLines[t] = callLines[t] || []).push(f);
    }
  } else if (all.length) err(f, "call line on a page that is not a call-only landing page");
  if (/\blanding-/.test(body)) {
    const metas = [...html.matchAll(/<meta (?:name|property)="(?:description|og:description|twitter:description)" content="([^"]*)"/g)].map((x) => x[1]).join(" \n ");
    const ld = [...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)].map((x) => x[1]).join(" \n ");
    const visible = html.replace(/<head>[\s\S]*?<\/head>/, " ")
      .replace(/<(script|style|nav|footer|figure|noscript)[\s\S]*?<\/\1>/g, " ")
      .replace(/<div class="sample-call[\s\S]*?<!-- \/sample-call -->/g, " ")
      .replace(/<[^>]+>/g, " ");
    const text = decode(metas + " \n " + ld + " \n " + visible);
    for (const re of THIRD_PERSON) {
      for (const m of text.matchAll(new RegExp(re.source, "gi"))) {
        const around = text.slice(Math.max(0, m.index - 60), m.index + 80);
        if (THIRD_PERSON_OK.some((ok) => ok.test(around))) continue;
        err(f, "third person about the visitor \"" + around.trim() + "\" (write it as 'you')");
      }
    }
  }
}
for (const [t, fs] of Object.entries(callLines)) if (fs.length > 1) err(fs.join(", "), "same call line on more than one page: \"" + t + "\"");

// 3. Any repeated hero element that differs across pages is a failure.
const report = [];
for (const [g, variants] of Object.entries(groups)) {
  const keys = Object.keys(variants);
  if (keys.length <= 1) continue;
  if (g === "heroCall") {
    // Approved CTA labels only (website-release-qc approved list).
    for (const k of keys) if (!["Call (647) 360-5774", "Book My AI Consultation"].includes(k)) err(variants[k].join(", "), "hero button text \"" + k + "\" is not an approved CTA label");
    continue;
  }
  keys.sort((a, b) => variants[b].length - variants[a].length);
  for (const k of keys.slice(1)) err([...new Set(variants[k])].join(", "), g + " differs from the majority form \"" + keys[0] + "\": \"" + k + "\"");
  report.push(g + ": " + keys.length + " variants");
}

// 4. Service-page calculators (Ben 2026-11-19 t1217u). Same block on every listed page,
// byte-equal to scripts/calc-markup.js render(), placed as the third top-level <section> in
// <main> (directly after section 2), right CTA for the page type, nowhere else, and the
// shared JS loads and passes its unit and DOM tests.
let calcCount = 0;
{
  const cm = require(path.join(__dirname, "calc-markup.js"));
  const calcJs = require(path.join(ROOT, "js", "calculator.js"));
  const t = require("child_process").spawnSync(process.execPath, [path.join(__dirname, "test-calculators.js")], { encoding: "utf8" });
  if (t.status !== 0) err("js/calculator.js", "calculator tests fail: " + (t.stderr || t.stdout).trim());
  if (!files.includes("js/calculator.js")) err("scripts/dist-manifest.txt", "js/calculator.js is not shipped");
  for (const id of Object.keys(calcJs.CALCS)) if (!Object.values(cm.PAGES).includes(id)) err("js/calculator.js", "calculator " + id + " is on no page");
  for (const f of pages) {
    const html = read(f);
    const n = (html.match(/<section class="tl-calc-section"/g) || []).length;
    const id = cm.PAGES[f];
    if (!id) { if (n) err(f, "has a calculator but is not in calc-markup.js PAGES"); continue; }
    if (n !== 1) { err(f, "needs exactly one calculator, found " + n); continue; }
    const m = html.match(/<!-- tl-calc -->[\s\S]*?<!-- \/tl-calc -->/);
    if (!m || m[0] !== cm.render(id)) err(f, "calculator markup differs from scripts/calc-markup.js (run node scripts/calc-markup.js && node scripts/build-pages.js)");
    // 2026-11-19 3-AI review: disclaimer sits above the Call button; no "on the table".
    if (m) {
      const noteAt = m[0].indexOf('class="tl-calc-note"');
      const ctaAt = m[0].indexOf("tl-calc-cta");
      if (noteAt < 0 || ctaAt < 0 || noteAt > ctaAt) err(f, "calculator disclaimer must sit above the Call button");
      if (/on the table/i.test(m[0])) err(f, "calculator still says \"on the table\"; use \"is at stake\" or the page's own honest result line");
    }
    const at = html.indexOf('<section class="tl-calc-section"');
    const re = /<section\b|<\/section>/g; re.lastIndex = html.indexOf("<main"); let depth = 0, top = 0, k, pos = -1;
    while ((k = re.exec(html))) { if (k[0] === "</section>") depth--; else { if (depth === 0) { top++; if (k.index === at) pos = top; } depth++; } }
    if (pos !== 3) err(f, "calculator must sit directly after section 2 (it is top-level section " + pos + ")");
    const body = (html.match(/<body[^>]*class="([^"]*)"/) || [, ""])[1];
    const call = /tel:\+16473605774" class="btn-primary tl-calc-cta"[^>]*>Call \(647\) 360-5774</.test(m ? m[0] : "");
    const consult = /href="#discovery-form" class="btn-primary gov-form-cta tl-calc-cta"[^>]*>Book My AI Consultation</.test(m ? m[0] : "");
    if (/\blanding-call\b/.test(body) && !call) err(f, "call-only page calculator needs the Call (647) 360-5774 button");
    if (/\blanding-form\b/.test(body) && (!consult || !/id="discovery-form"/.test(html))) err(f, "form page calculator needs the Book My AI Consultation button to #discovery-form");
    // 2026-11-19 section-2 polish: where the calculator's call button sits
    // directly after section 2, section 2 must not also show a call button
    // (hero, sticky and later CTAs stay).
    if (/\blanding-call\b/.test(body) && call) {
      const prevHtml = html.slice(0, at);
      const prev = (prevHtml.match(/<section class="pain-section[^"]*"[\s\S]*?<\/section>/g) || []).pop() || "";
      if (/href="tel:\+16473605774"[^>]*>Call \(647\) 360-5774/.test(prev)) {
        err(f, "section 2 must not show a call button when the calculator's call button follows it");
      }
    }
    calcCount++;
  }
}

if (errors.length) {
  console.error("check-site-consistency: FAIL (" + errors.length + ")\n- " + errors.join("\n- "));
  process.exit(1);
}
console.log("check-site-consistency: OK. " + pages.length + " pages: full nav (" + (homeLinks || []).length + " links) on every page, one guarantee badge form, no banned phrases, hero cancel/price/call consistent, " + Object.keys(callLines).length + " call lines, no third-person landing copy, " + calcCount + " calculators consistent.");
