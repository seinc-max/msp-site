#!/usr/bin/env node
/**
 * Regression checks for the Nov 7 staging review fixes.
 * No calls, form posts, or network writes.
 */
'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const read = (rel) => fs.readFileSync(path.join(ROOT, rel), 'utf8');
const errors = [];
const fail = (msg) => { errors.push(msg); console.log('FAIL\t' + msg); };
const pass = (msg) => console.log('PASS\t' + msg);

function nav(html) {
  const start = html.indexOf('<nav');
  const end = html.indexOf('</nav>', start);
  return html.slice(start, end);
}

const audienceOf = {
  'index.html': '',
  'about.html': '',
  'privacy.html': '',
  'terms.html': '',
  '404.html': '',
  'for-home-services.html': 'trades',
  'missed-call-text-back.html': 'trades',
  'ai-receptionist.html': 'trades',
  'quote-follow-up-win-back.html': 'trades',
  'website-chat-to-text.html': 'trades',
  'text-to-pay.html': 'trades',
  'contractor-websites.html': 'trades',
  'google-review-requests.html': 'trades',
  'for-appointment-businesses.html': 'salons',
  'ai-receptionist-for-salons.html': 'salons',
  'google-review-requests-for-salons.html': 'salons',
  'for-law-firms-accountants-and-advisors.html': 'professional',
  'ai-governance.html': 'professional',
  'fractional-ai-officer.html': 'professional',
  'ai-support-agent.html': 'professional',
  'ai-exposure-score.html': 'professional',
  'ai-automation-roi-guide.html': 'professional',
  'margin-leakage-calculator.html': 'professional',
  'blog/voice-ai-law-accounting-confidentiality.html': 'professional',
  'blog/is-your-business-pipeda-compliant.html': 'professional',
  'blog/what-sovereign-ai-actually-means.html': 'professional',
  'blog/sovereign-zapier-alternatives-compliance.html': 'professional',
  'blog/financial-integration-insurance-vulnerabilities.html': 'professional',
  'blog/20-shadow-ai-audits-2026.html': 'professional',
};

const proOfferHrefs = ['/ai-governance', '/fractional-ai-officer', '/ai-support-agent'];
const bannedForTrades = ['/for-appointment-businesses', '/ai-receptionist-for-salons', '/google-review-requests-for-salons'].concat(proOfferHrefs);
const bannedForSalons = ['/missed-call-text-back', '/quote-follow-up-win-back', '/website-chat-to-text', '/text-to-pay', '/contractor-websites'].concat(proOfferHrefs);
const bannedForPro = ['/missed-call-text-back', '/for-home-services', '/for-appointment-businesses', '/ai-receptionist', '/quote-follow-up-win-back', '/website-chat-to-text', '/text-to-pay', '/contractor-websites', '/google-review-requests'].concat(proOfferHrefs);

function bodyClass(html) {
  return (html.match(/<body[^>]*\bclass="([^"]*)"/) || [])[1] || '';
}

function assertNav(file, banned, must) {
  const n = nav(read(file));
  for (const href of banned) {
    if (n.includes('href="' + href + '"')) fail(file + ' nav still links ' + href);
  }
  for (const href of must) {
    if (!n.includes('href="' + href + '"')) fail(file + ' nav missing ' + href);
  }
}

const files = Object.keys(audienceOf);
if (files.length !== 29) fail('audience map does not cover 29 pages, got ' + files.length);
for (const file of files) {
  const html = read(file);
  const want = audienceOf[file];
  const cls = bodyClass(html);
  const got = cls.includes('audience-trades') ? 'trades' : cls.includes('audience-salons') ? 'salons' : cls.includes('audience-professional') ? 'professional' : '';
  if (got !== want) fail(file + ' audience is ' + (got || 'neutral') + ', expected ' + (want || 'neutral'));
}
pass('29 pages classified: 5 neutral, 8 trades, 3 salons, 13 professional');

for (const file of files.filter((f) => audienceOf[f] === 'trades')) {
  assertNav(file, bannedForTrades, ['/missed-call-text-back', '/ai-receptionist', '/google-review-requests']);
}
for (const file of files.filter((f) => audienceOf[f] === 'salons')) {
  assertNav(file, bannedForSalons, ['/ai-receptionist-for-salons', '/google-review-requests-for-salons', '/for-appointment-businesses']);
}
for (const file of files.filter((f) => audienceOf[f] === 'professional')) {
  assertNav(file, bannedForPro, ['/for-law-firms-accountants-and-advisors']);
}
pass('targeted pages, including professional blogs and tools, omit NO-map offers');

for (const file of ['index.html', 'about.html', 'privacy.html', 'terms.html']) {
  const n = nav(read(file));
  for (const href of ['/for-home-services', '/for-appointment-businesses', '/for-law-firms-accountants-and-advisors']) {
    if (!n.includes('href="' + href + '"')) fail(file + ' dropped audience hub ' + href);
  }
  for (const href of proOfferHrefs) {
    if (n.includes('href="' + href + '"')) fail(file + ' nav added professional offer ' + href);
  }
}
const notFound = read('404.html');
if (bodyClass(notFound)) fail('404 should stay a neutral recovery page');
const notFoundNav = nav(notFound);
for (const href of proOfferHrefs) {
  if (notFoundNav.includes('href="' + href + '"')) fail('404 nav added professional offer ' + href);
}
if (!notFound.includes('href="/for-home-services"') || !notFound.includes('href="/for-appointment-businesses"') || !notFound.includes('href="/for-law-firms-accountants-and-advisors"')) {
  fail('404 dropped an audience recovery link');
}
pass('neutral pages keep the three hubs and do not add professional offer links');

for (const f of [
  'blog/sovereign-zapier-alternatives-compliance.html',
  'blog/financial-integration-insurance-vulnerabilities.html',
  'blog/voice-ai-law-accounting-confidentiality.html',
  'blog/20-shadow-ai-audits-2026.html',
  'terms.html',
]) {
  const html = read(f);
  const regions = [...html.matchAll(/<div class="table-scroll"[^>]*>/g)].map((m) => m[0]);
  if (!regions.length) fail(f + ' has no table-scroll');
  for (const tag of regions) {
    if (!tag.includes('tabindex="0"') || !tag.includes('aria-label=')) fail(f + ' table region not keyboard-labelled: ' + tag.slice(0, 80));
  }
}
pass('table scroll regions are focusable and labelled');

const calc = read('margin-leakage-calculator.html');
if (!/calculateMargin\(\);\s*<\/script>/.test(calc)) fail('calculator does not run on load');
else pass('calculator calls calculateMargin on load');
if (calc.includes('id="out-leakage">—')) pass('calculator placeholder remains until the script runs');

const css = read('assets/site.css');
if (!css.includes('@keyframes tlRise{from{opacity:1')) fail('bubble animation still starts invisible');
else pass('bubble animation stays opaque');
if (!css.includes('@keyframes fadeUp{from{opacity:1')) fail('hero fade still starts invisible in site.css');
else pass('shared fadeUp stays opaque');
if (css.includes('nav-pro-offer')) fail('header still has a professional-offer nav exception');
const heroRule = '.hero-inner > *{\n    opacity: 1;\n    animation: none;\n  }';
for (const file of ['index.html', 'about.html', 'privacy.html', 'terms.html', 'ai-exposure-score.html', 'ai-automation-roi-guide.html']) {
  const html = read(file);
  if (!html.includes(heroRule)) fail(file + ' hero rule is not opaque with animation none');
  if (/hero-inner > \*\{[^}]*opacity:\s*0/.test(html)) fail(file + ' hero children still start at opacity 0');
}
pass('hero children are opaque before any animation delay');

const option = read('ai-exposure-score.html');
if (!option.includes('min-height: 44px')) fail('exposure options missing 44px hit area');
else pass('exposure option labels set a 44px minimum');

const mctb = read('missed-call-text-back.html');
if (!mctb.includes("How many calls ring out while you're on a job?") && !mctb.includes('How many calls ring out while you’re on a job?')) {
  fail('locked missed-call heading changed');
}
if (!mctb.includes("Call us and we'll estimate what missed calls are costing you, from your own numbers.")) {
  fail('missed-call estimate card was not clarified');
}
if (mctb.includes('text back from a separate number') === false) fail('staged text-back wording missing');
else pass('estimate clarification kept the locked heading and staged text-back wording');

if (errors.length) {
  console.error(errors.length + ' review-fix checks failed.');
  process.exit(1);
}
console.log('All review-fix checks passed.');
