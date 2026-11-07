#!/usr/bin/env node
/**
 * Demo namespace regression. Creates a temporary nested fixture, proves
 * build-dist keeps it, then deletes the fixture. No network calls.
 */
'use strict';

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const ROOT = path.join(__dirname, '..');
const SLUG = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
const errors = [];
const fail = (msg) => { errors.push(msg); console.log('FAIL\t' + msg); };
const pass = (msg) => console.log('PASS\t' + msg);

function read(rel) {
  return fs.readFileSync(path.join(ROOT, rel), 'utf8');
}

function walkHtml(dir, acc) {
  for (const name of fs.readdirSync(dir)) {
    const abs = path.join(dir, name);
    if (fs.statSync(abs).isDirectory()) walkHtml(abs, acc);
    else if (name.endsWith('.html')) acc.push(abs);
  }
  return acc;
}

const reserved = ['demo/index.html', 'demo/nicky-billou/index.html', 'demo/demo.css'];
for (const rel of reserved) {
  if (!fs.existsSync(path.join(ROOT, rel))) fail('missing ' + rel);
}
if (!SLUG.test('nicky-billou')) fail('nicky-billou is not a valid slug');
for (const bad of ['Nicky', 'nicky_billou', 'nicky--billou', '-nicky', 'nicky-']) {
  if (SLUG.test(bad)) fail('slug accepted ' + bad);
}
pass('reserved routes and slug rule');

const banned = ['GTM-', 'clarity', 'tel:', '<form', 'dataLayer', 'landing.css', 'site.css', 'audience-', 'nav-cta', 'click_to_call', 'form_cta_click', 'guarantee', '$'];
for (const abs of walkHtml(path.join(ROOT, 'demo'), [])) {
  const html = fs.readFileSync(abs, 'utf8');
  const rel = path.relative(ROOT, abs);
  if (!html.includes('<meta name="robots" content="noindex, nofollow">')) fail(rel + ' missing noindex');
  if (!html.includes('name="viewport"')) fail(rel + ' missing viewport');
  for (const token of banned) {
    if (html.includes(token)) fail(rel + ' contains ' + token);
  }
}
const client = read('demo/nicky-billou/index.html');
if (!client.includes('href="../demo.css"') || !client.includes('href="../"')) fail('client page relative links missing');
if (!read('demo/index.html').includes('href="demo.css"')) fail('demo index relative stylesheet missing');
if (read('demo/index.html').includes('nicky-billou')) fail('demo index lists a client');
pass('demo HTML is noindex and has no marketing chrome');

const sitemap = read('sitemap.xml');
if (sitemap.includes('/demo')) fail('sitemap contains a demo URL');
else pass('sitemap has no demo URL');
const robots = read('robots.txt');
if (/Disallow:\s*\/demo/.test(robots)) fail('robots.txt disallows /demo');
else pass('robots.txt does not block /demo');

const header = path.join(ROOT, 'templates/partials/header.html');
if (fs.existsSync(header) && read('templates/partials/header.html').includes('/demo')) fail('header links to /demo');
if (read('index.html').includes('href="/demo')) fail('home links to /demo');
pass('marketing nav does not link to /demo');

const fixture = path.join(ROOT, 'demo', '_fixture', 'nested-asset-check');
const distAsset = path.join(ROOT, 'dist', 'demo', '_fixture', 'nested-asset-check', 'assets', 'mark.txt');
try {
  fs.mkdirSync(path.join(fixture, 'assets'), { recursive: true });
  fs.writeFileSync(path.join(fixture, 'index.html'), '<!DOCTYPE html><html><head><meta name="robots" content="noindex, nofollow"></head><body><img src="assets/mark.txt" alt=""></body></html>');
  fs.writeFileSync(path.join(fixture, 'assets', 'mark.txt'), 'fixture-mark');
  const built = spawnSync(process.execPath, [path.join(ROOT, 'scripts', 'build-dist.js')], { cwd: ROOT, encoding: 'utf8' });
  if (built.status !== 0) fail('build-dist failed with nested fixture\n' + (built.stderr || built.stdout));
  else if (fs.readFileSync(distAsset, 'utf8') !== 'fixture-mark') fail('nested fixture asset missing from dist');
  else if (!fs.existsSync(path.join(ROOT, 'dist', 'demo', 'index.html'))) fail('dist missing demo/index.html');
  else if (!fs.existsSync(path.join(ROOT, 'dist', 'demo', 'nicky-billou', 'index.html'))) fail('dist missing client index');
  else pass('build-dist retained nested demo index and asset');
} finally {
  fs.rmSync(path.join(ROOT, 'demo', '_fixture'), { recursive: true, force: true });
  fs.rmSync(path.join(ROOT, 'dist'), { recursive: true, force: true });
}

if (fs.existsSync(path.join(ROOT, 'demo', '_fixture'))) fail('temporary fixture was left in demo/');
if (errors.length) {
  console.error(errors.length + ' demo hosting checks failed.');
  process.exit(1);
}
console.log('All demo hosting checks passed.');
