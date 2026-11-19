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
// - claims texts come from the client's own number (BANNED_SENDER);
// - has a sample figcaption that is not italic or does not start "Just a sample";
// - has a tel: link other than tel:+16473605774.
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
const BANNED = [/per[\s\u00a0-]+location/i];
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

if (errors.length) {
  console.error("check-site-consistency: FAIL (" + errors.length + ")\n- " + errors.join("\n- "));
  process.exit(1);
}
console.log("check-site-consistency: OK. " + pages.length + " pages: full nav (" + (homeLinks || []).length + " links) on every page, one guarantee badge form, no banned phrases, hero cancel/price/call consistent.");
