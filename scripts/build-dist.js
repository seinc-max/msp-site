#!/usr/bin/env node
// Copies only the public site into dist/ for Cloudflare Pages.
// Build sources (templates/, scripts/, docs/, src/), Pages Functions (functions/,
// which Pages reads from the repo root), and repo files (README, package files,
// Tailwind config, .gitignore) stay out of the deployed output.
// Pages setting this needs: Build command `node scripts/build-dist.js`,
// Build output directory `dist`. Root directory stays empty.
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "dist");
const EXCLUDE_TOP = new Set([
  ".git", ".github", "node_modules", "dist", "templates", "scripts", "docs",
  "src", "functions", "README.md", "package.json", "package-lock.json",
  "tailwind.config.js", ".gitignore", "wrangler.toml", "wrangler.json", "wrangler.jsonc",
]);
const EXCLUDE_ANY = (name) => name === ".DS_Store" || name.endsWith(".py") || name === "__pycache__";

function copy(src, dst) {
  const st = fs.statSync(src);
  if (st.isDirectory()) {
    fs.mkdirSync(dst, { recursive: true });
    for (const name of fs.readdirSync(src)) {
      if (EXCLUDE_ANY(name)) continue;
      copy(path.join(src, name), path.join(dst, name));
    }
  } else {
    fs.copyFileSync(src, dst);
  }
}

fs.rmSync(OUT, { recursive: true, force: true });
fs.mkdirSync(OUT);
let n = 0;
for (const name of fs.readdirSync(ROOT).sort()) {
  if (EXCLUDE_TOP.has(name) || EXCLUDE_ANY(name)) continue;
  copy(path.join(ROOT, name), path.join(OUT, name));
  n++;
}
for (const must of ["index.html", "404.html", "_redirects", "_headers", "llms.txt", "sitemap.xml", "robots.txt", "assets", "blog"]) {
  if (!fs.existsSync(path.join(OUT, must))) { console.error("missing in dist: " + must); process.exit(1); }
}
console.log("dist: " + n + " top-level entries copied");
