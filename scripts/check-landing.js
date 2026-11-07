#!/usr/bin/env node
/**
 * Pre-staging landing gate.
 * Shared template adoption, source/output parity, frozen visible text,
 * lead wiring, family/action mapping, and duplicate hero calls.
 *
 *   node scripts/check-landing.js
 */
'use strict';

const { spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const PAGES = {
  'index.html': 'landing-call landing-home',
  'for-home-services.html': 'landing-call landing-hub',
  'for-appointment-businesses.html': 'landing-call landing-hub',
  'for-law-firms-accountants-and-advisors.html': 'landing-form landing-hub',
  'missed-call-text-back.html': 'landing-call landing-offer',
  'ai-receptionist.html': 'landing-call landing-offer',
  'ai-receptionist-for-salons.html': 'landing-call landing-offer',
  'quote-follow-up-win-back.html': 'landing-call landing-offer',
  'website-chat-to-text.html': 'landing-call landing-offer',
  'text-to-pay.html': 'landing-call landing-offer',
  'contractor-websites.html': 'landing-call landing-offer',
  'google-review-requests.html': 'landing-call landing-offer',
  'google-review-requests-for-salons.html': 'landing-call landing-offer',
  'ai-governance.html': 'landing-form landing-offer',
  'fractional-ai-officer.html': 'landing-form landing-offer',
  'ai-support-agent.html': 'landing-form landing-hub',
};
const NON_LANDING = ['about.html', 'privacy.html', 'terms.html', 'blog/what-sovereign-ai-actually-means.html', 'ai-exposure-score.html'];

function read(rel) {
  return fs.readFileSync(path.join(ROOT, rel), 'utf8');
}

function texts(html) {
  let body = html
    .replace(/<style[\s\S]*?<\/style>/g, '')
    .replace(/<script[\s\S]*?<\/script>/g, '');
  body = body.replace(/<nav\b[\s\S]*?<\/nav>/g, '').replace(/<footer\b[\s\S]*?<\/footer>/g, '');
  return [...body.matchAll(/>([^<]+)</g)]
    .map((m) => m[1].replace(/\s+/g, ' ').trim())
    .filter(Boolean)
    .map((t) => t
      .replace("Call us and we'll estimate what missed calls are costing you, from your own numbers.", "Using your own numbers, we'll estimate how much missed calls may be costing your business.")
      .replace("Call us and we'll estimate the monthly leak and what better call coverage could recover, from your own numbers.", "Using your own numbers, we'll estimate the monthly leak and what better call coverage could recover."));
}

function fail(errors, msg) {
  errors.push(msg);
  console.log('FAIL\t' + msg);
}

function main() {
  const errors = [];
  const fresh = spawnSync(process.execPath, [path.join(__dirname, 'build-pages.js'), '--check'], {
    cwd: ROOT,
    encoding: 'utf8',
  });
  if (fresh.status !== 0) {
    fail(errors, 'build --check is not idempotent\n' + (fresh.stdout || '') + (fresh.stderr || ''));
  } else {
    console.log('PASS\tbuild --check (29 pages match sources)');
  }

  for (const [file, klass] of Object.entries(PAGES)) {
    for (const rel of [file, 'templates/pages/' + file]) {
      const html = read(rel);
      if (!html.includes('href="/assets/landing.css"')) fail(errors, rel + ' missing landing.css');
      const tokens = klass.split(' ');
      if (!tokens.every((token) => new RegExp('class="[^"]*\\b' + token + '\\b').test(html))) {
        fail(errors, rel + ' missing body class ' + klass);
      }
      if (html.includes('1.75rem!important') || html.includes('height:57px!important')) {
        fail(errors, rel + ' still has a page-level !important headline or button lock');
      }
      const hero = (html.match(/<section class="(?:hero|hub-hero)"[\s\S]*?<\/section>/) || [''])[0];
      const calls = [
        ...hero.matchAll(/class="(?:hero-call|btn-primary)"[^>]*>\s*Call \(647\) 360-5774/g),
        ...hero.matchAll(/class="hub-cta"[^>]*href="tel:[^"]*"[^>]*>/g),
      ].length;
      const family = klass.includes('landing-call') ? 'call' : 'form';
      if (family === 'call' && calls !== 1) fail(errors, rel + ' hero Call actions ' + calls + ' (want 1)');
      if (family === 'form' && /class="(?:hero-call|btn-primary)"[^>]*>\s*Call \(647\) 360-5774/.test(hero)) {
        fail(errors, rel + ' form page has a hero Call button');
      }
      if (family === 'form' && file !== 'for-law-firms-accountants-and-advisors.html') {
        if (!html.includes('id="discovery-form"')) fail(errors, rel + ' missing discovery-form');
      }
    }
    const served = texts(read(file));
    let previous = '';
    try {
      previous = require('child_process').execFileSync('git', ['show', 'HEAD:' + file], { cwd: ROOT, encoding: 'utf8' });
    } catch (err) {
      fail(errors, file + ' has no HEAD copy to freeze against');
      continue;
    }
    const before = texts(previous);
    const lost = before.filter((t) => !served.includes(t));
    const gained = served.filter((t) => !before.includes(t));
    if (lost.length || gained.length) {
      fail(errors, file + ' visible text changed: -' + lost.slice(0, 3).join(' | ') + ' +' + gained.slice(0, 3).join(' | '));
    } else {
      console.log('PASS\t' + file + ' visible text unchanged from staging base');
    }
  }

  for (const rel of NON_LANDING) {
    const html = read(rel);
    if (html.includes('landing.css') || html.includes('landing-call') || html.includes('landing-form')) {
      fail(errors, rel + ' picked up landing template markers');
    } else {
      console.log('PASS\t' + rel + ' not on the landing stylesheet');
    }
  }

  if (errors.length) {
    console.error(errors.length + ' landing checks failed.');
    process.exit(1);
  }
  console.log('All landing template checks passed.');
}

main();
