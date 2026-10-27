#!/usr/bin/env node
// Copies only the public site into dist/ for Cloudflare Pages (Tracker row 62).
// Pages settings this needs: Build command `node scripts/build-dist.js`,
// Build output directory `dist`, Root directory empty.
//
// Fails the build (exit 1) when:
// - a top-level entry is in neither ALLOW nor KNOWN_EXCLUDED (a new file or
//   folder at the root must be added to one list on purpose);
// - any path is a symlink (never followed);
// - dist/ doesn't hold exactly the files in scripts/dist-manifest.txt.
"use strict";
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "dist");
const MANIFEST = path.join(__dirname, "dist-manifest.txt");

// Public top-level entries. Adding a page means adding it here and to the manifest.
const ALLOW = new Set([
  "404.html", "_headers", "_redirects", "about.html", "ai-automation-roi-guide.html",
  "ai-exposure-score.html", "ai-governance.html", "ai-receptionist.html", "ai-receptionist-for-salons.html",
  "ai-support-agent.html", "assets", "blog", "contractor-websites.html",
  "favicon.ico", "favicon.png", "favicon.svg", "for-appointment-businesses.html",
  "for-home-services.html", "for-law-firms-accountants-and-advisors.html",
  "fractional-ai-officer.html", "google-review-requests.html", "google-review-requests-for-salons.html", "index.html", "js",
  "llms.txt", "margin-leakage-calculator.html", "missed-call-text-back.html",
  "og-image-professional.jpg", "og-image-trades.jpg", "og-image.jpg", "og-image.png",
  "privacy.html", "quote-follow-up-win-back.html", "robots.txt", "sitemap.xml", "688213215a3247df8b5797e268fbd61b.txt",
  "terms.html", "text-to-pay.html", "website-chat-to-text.html",
]);

// Known non-public entries. Never copied. Pages reads functions/ from the repo root.
const KNOWN_EXCLUDED = new Set([
  ".git", "node_modules", "dist", "docs", "templates", "scripts", "src", "functions",
  "README.md", "package.json", "package-lock.json", "tailwind.config.js", ".gitignore",
]);

function fail(msg) {
  console.error("build-dist: FAIL: " + msg);
  process.exit(1);
}

const copied = [];
function copy(src, dst, rel) {
  const st = fs.lstatSync(src);
  if (st.isSymbolicLink()) fail("symlink not allowed: " + rel);
  if (st.isDirectory()) {
    fs.mkdirSync(dst, { recursive: true });
    for (const name of fs.readdirSync(src).sort()) {
      copy(path.join(src, name), path.join(dst, name), rel + "/" + name);
    }
  } else if (st.isFile()) {
    fs.copyFileSync(src, dst);
    copied.push(rel);
  } else {
    fail("not a regular file or folder: " + rel);
  }
}

// 1. Check every top-level entry before copying anything.
const top = fs.readdirSync(ROOT).sort();
const unknown = top.filter((n) => !ALLOW.has(n) && !KNOWN_EXCLUDED.has(n));
if (unknown.length) fail("unknown top-level entries (add to ALLOW or KNOWN_EXCLUDED): " + unknown.join(", "));
for (const n of top) {
  if (fs.lstatSync(path.join(ROOT, n)).isSymbolicLink()) fail("symlink not allowed: " + n);
}
const missingTop = [...ALLOW].filter((n) => !top.includes(n));
if (missingTop.length) fail("missing public entries: " + missingTop.join(", "));

// 2. Copy the allowed entries.
fs.rmSync(OUT, { recursive: true, force: true });
fs.mkdirSync(OUT);
for (const n of top) {
  if (ALLOW.has(n)) copy(path.join(ROOT, n), path.join(OUT, n), n);
}

// 3. Compare against the manifest.
const expected = fs.readFileSync(MANIFEST, "utf8").split("\n").map((s) => s.trim()).filter(Boolean);
const want = new Set(expected);
const got = new Set(copied);
const missing = expected.filter((f) => !got.has(f));
const extra = copied.filter((f) => !want.has(f));
if (missing.length || extra.length) {
  fs.rmSync(OUT, { recursive: true, force: true });
  fail("dist/ does not match scripts/dist-manifest.txt. Missing: [" + missing.join(", ") + "] Extra: [" + extra.join(", ") + "]");
}
console.log("dist: " + copied.length + " files copied (manifest " + expected.length + "), " + top.filter((n) => ALLOW.has(n)).length + " top-level entries");
