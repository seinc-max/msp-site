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

const reserved = ['demo/index.html', 'demo/nicky-billou/index.html', 'demo/demo.css', 'demo/nicky-billou/website/index.html', 'demo/nicky-billou/website/site.css'];
for (const rel of reserved) {
  if (!fs.existsSync(path.join(ROOT, rel))) fail('missing ' + rel);
}
if (!SLUG.test('nicky-billou') || !SLUG.test('website')) fail('reserved slug rejected');
for (const bad of ['Nicky', 'nicky_billou', 'nicky--billou', '-nicky', 'nicky-']) {
  if (SLUG.test(bad)) fail('slug accepted ' + bad);
}
pass('reserved routes and slug rule');

const banned = ['GTM-', 'clarity', 'tel:', '<form', 'dataLayer', 'assets/landing.css', 'assets/site.css', 'audience-', 'nav-cta', 'click_to_call', 'form_cta_click', 'guarantee', '$'];
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
if (client.includes('website')) fail('client page lists a project type');
if (!read('demo/index.html').includes('href="demo.css"')) fail('demo index relative stylesheet missing');
if (read('demo/index.html').includes('nicky-billou')) fail('demo index lists a client');
const website = read('demo/nicky-billou/website/index.html');
if (!website.includes('href="site.css"') || !website.includes('href="../"')) fail('website page relative links missing');
if (website.includes('../demo.css') || website.includes('/assets/')) fail('website page uses an asset outside its folder');
if (!website.includes('DEMO') || !website.includes('Sample Workshop')) fail('website page is not marked as a sample demo');
if (/nicky|billou/i.test(website)) fail('website page uses the client id as the business');
if (!client.includes('not the business name')) fail('client page presents the folder id as the business');
const doc = read('docs/demo-hosting.md');
if (!doc.includes('already-live') || !doc.includes('Do not clone a Trueline page')) fail('doc misses the live-industry clone rule');
if (!doc.includes('CF_PAGES_BRANCH')) fail('doc misses the release guard');
if (doc.includes('499') || website.includes('499') || client.includes('499')) fail('demo docs or pages carry a price');
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

const fixture = path.join(ROOT, 'demo', '_fixture', 'website');
const distAsset = path.join(ROOT, 'dist', 'demo', '_fixture', 'website', 'assets', 'mark.txt');
try {
  fs.mkdirSync(path.join(fixture, 'assets'), { recursive: true });
  fs.writeFileSync(path.join(fixture, 'index.html'), '<!DOCTYPE html><html><head><meta name="robots" content="noindex, nofollow"></head><body><img src="assets/mark.txt" alt=""></body></html>');
  fs.writeFileSync(path.join(fixture, 'assets', 'mark.txt'), 'fixture-mark');
  const built = spawnSync(process.execPath, [path.join(ROOT, 'scripts', 'build-dist.js')], {
    cwd: ROOT,
    encoding: 'utf8',
    env: Object.assign({}, process.env, { CF_PAGES_BRANCH: 'staging' }),
  });
  if (built.status !== 0) fail('build-dist failed with nested fixture\n' + (built.stderr || built.stdout));
  else if (fs.readFileSync(distAsset, 'utf8') !== 'fixture-mark') fail('project-type asset missing from dist');
  else if (!fs.existsSync(path.join(ROOT, 'dist', 'demo', 'nicky-billou', 'website', 'index.html'))) fail('dist missing website index');
  else if (!fs.existsSync(path.join(ROOT, 'dist', 'demo', 'nicky-billou', 'website', 'site.css'))) fail('dist missing website stylesheet');
  else pass('build-dist retained project-type index, stylesheet, and nested asset');
} finally {
  fs.rmSync(path.join(ROOT, 'demo', '_fixture'), { recursive: true, force: true });
  fs.rmSync(path.join(ROOT, 'dist'), { recursive: true, force: true });
}

if (fs.existsSync(path.join(ROOT, 'demo', '_fixture'))) fail('temporary fixture was left in demo/');

const mainBuild = spawnSync(process.execPath, [path.join(ROOT, 'scripts', 'build-dist.js')], {
  cwd: ROOT,
  encoding: 'utf8',
  env: Object.assign({}, process.env, { CF_PAGES_BRANCH: 'main' }),
});
if (mainBuild.status === 0) fail('CF_PAGES_BRANCH=main published demo/');
else if (!/staging-only/.test(mainBuild.stderr || '')) fail('main build failed without the demo guard: ' + (mainBuild.stderr || mainBuild.stdout));
else if (fs.existsSync(path.join(ROOT, 'dist', 'demo'))) fail('main build left demo artifacts in dist/');
else pass('CF_PAGES_BRANCH=main refuses demo/ and leaves no demo artifacts');
fs.rmSync(path.join(ROOT, 'dist'), { recursive: true, force: true });
if (errors.length) {
  console.error(errors.length + ' demo hosting checks failed.');
  process.exit(1);
}
console.log('All demo hosting checks passed.');
