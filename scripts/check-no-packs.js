#!/usr/bin/env node
// No packs or bundles anywhere on the site.
// Ben 2026-11-25 6:41 PM ET: no packs or bundles anywhere on the site.
// RCA: /workspace/trueline-atlas/rca/no-packs-bundles-20261126/RCA.md.
//
// Fails (exit 1) if any scanned file contains:
// - $179
// - quote-follow-up-win-back#pack, id="pack", or front-pack
// - the product name "Quote Follow-Up + Google Review Requests"
// - the words bundle(s) or combo(s)
// Scans templates/, js/, llms.txt, sitemap.xml and the built top-level *.html.
// Skips node_modules/, .git/, dist/, demo/ and *.min.* vendor files.
//
// Allowlist (2026-11-26, brief 8): only known non-product text, listed below.
// Note: "pack up" and "package" are not matched by the patterns above, so they
// need no strip. Any future false positive must be added to ALLOW with a dated
// comment, never by loosening a pattern.
//
//   node scripts/check-no-packs.js
"use strict";
const fs = require("fs");
const path = require("path");
const ROOT = path.join(__dirname, "..");

const PATTERNS = [
  ["$179", /\$179/],
  ["#pack link", /quote-follow-up-win-back#pack/],
  ['id="pack"', /id=["']pack["']/],
  ["front-pack", /front-pack/],
  ["pack product name", /Quote Follow-Up \+ Google Review Requests/i],
  ["bundle", /\bbundles?\b/i],
  ["combo", /\bcombos?\b/i],
];
// Allowlisted exact snippets (2026-11-26, Ben brief 8): none currently match.
// "You finish, pack up, and forget to ask." and "package is due" are verbs/deliverables.
const ALLOW = [];

const SKIP_DIRS = new Set(["node_modules", ".git", "dist", "demo"]);
const EXT = /\.(html|txt|xml|js)$/;
const hits = [];

function scanFile(f) {
  if (/\.min\./.test(f) || !EXT.test(f)) return;
  let text = fs.readFileSync(f, "utf8");
  for (const a of ALLOW) text = text.split(a).join("");
  text.split("\n").forEach((line, i) => {
    for (const [label, re] of PATTERNS) {
      if (re.test(line)) hits.push(`${path.relative(ROOT, f)}:${i + 1} [${label}] ${line.trim().slice(0, 120)}`);
    }
  });
}
function walk(d) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    if (SKIP_DIRS.has(e.name)) continue;
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p);
    else scanFile(p);
  }
}
walk(path.join(ROOT, "templates"));
walk(path.join(ROOT, "js"));
for (const e of fs.readdirSync(ROOT, { withFileTypes: true })) {
  if (e.isFile() && (e.name.endsWith(".html") || e.name === "llms.txt" || e.name === "sitemap.xml")) scanFile(path.join(ROOT, e.name));
}
if (hits.length) {
  console.error("check-no-packs: FAIL (Ben 2026-11-25 6:41 PM ET: no packs or bundles)");
  hits.forEach((h) => console.error("  " + h));
  process.exit(1);
}
console.log("check-no-packs: ok (0 hits)");
