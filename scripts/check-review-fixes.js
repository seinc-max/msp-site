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

const trades = ['for-home-services.html', 'missed-call-text-back.html', 'quote-follow-up-win-back.html', 'text-to-pay.html'];
const salons = ['for-appointment-businesses.html', 'ai-receptionist-for-salons.html'];
const pros = ['ai-governance.html', 'fractional-ai-officer.html', 'ai-support-agent.html'];
const bannedForTrades = ['/for-appointment-businesses', '/ai-receptionist-for-salons', '/google-review-requests-for-salons', '/ai-governance', '/fractional-ai-officer', '/ai-support-agent'];
const bannedForSalons = ['/missed-call-text-back', '/quote-follow-up-win-back', '/website-chat-to-text', '/text-to-pay', '/contractor-websites', '/ai-governance'];
const bannedForPro = ['/missed-call-text-back', '/for-home-services', '/for-appointment-businesses', '/ai-receptionist'];

function assertNav(file, banned, must) {
  const n = nav(read(file));
  if (!read(file).includes('audience-')) fail(file + ' missing audience class');
  for (const href of banned) {
    if (n.includes('href="' + href + '"')) fail(file + ' nav still links ' + href);
  }
  for (const href of must) {
    if (!n.includes('href="' + href + '"')) fail(file + ' nav missing ' + href);
  }
}

for (const f of trades) assertNav(f, bannedForTrades, ['/missed-call-text-back', '/ai-receptionist', '/google-review-requests']);
for (const f of salons) assertNav(f, bannedForSalons, ['/ai-receptionist-for-salons', '/google-review-requests-for-salons', '/for-appointment-businesses']);
for (const f of pros) assertNav(f, bannedForPro, ['/ai-governance', '/fractional-ai-officer', '/ai-support-agent', '/for-law-firms-accountants-and-advisors']);

const homeNav = nav(read('index.html'));
if (homeNav.includes('nav-pro-offer" href="/ai-governance"') && !homeNav.includes('audience-professional')) {
  if (read('index.html').includes('audience-professional')) fail('home should not be audience-professional');
}
if (!homeNav.includes('href="/for-home-services"') || !homeNav.includes('href="/for-appointment-businesses"') || !homeNav.includes('href="/for-law-firms-accountants-and-advisors"')) {
  fail('home menu dropped an audience hub');
} else pass('home menu still routes all three audiences');
pass('audience menus checked');

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
