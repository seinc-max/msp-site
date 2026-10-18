#!/usr/bin/env node
/**
 * Proves generated pages are fresh and that every page <head>
 * (title, description, canonical, Open Graph, JSON-LD, and tracking)
 * matches the source page byte for byte, and that each page's header
 * CTA text, href, and tracking attribute match that page's original nav.
 *
 *   node scripts/check-pages.js
 */
'use strict';

const crypto = require('crypto');
const fs = require('fs');
const { spawnSync } = require('child_process');
const path = require('path');
const { buildAll, headOf, HEADER_CTAS } = require('./build-pages');

function navHtml(html) {
  const start = html.indexOf('<nav');
  const end = html.indexOf('</nav>', start);
  if (start < 0 || end < 0) return '';
  return html.slice(start, end + 6);
}

function headerCta(html) {
  const nav = navHtml(html);
  const anchors = [...nav.matchAll(/<a\b[^>]*\bclass="[^"]*\bnav-cta\b[^"]*"[^>]*>[\s\S]*?<\/a>/g)];
  if (anchors.length !== 1) {
    return { error: anchors.length + ' header nav-cta anchors', nav };
  }
  const tag = anchors[0][0];
  const href = (tag.match(/\bhref="([^"]*)"/) || [])[1] || '';
  const onclick = (tag.match(/\bonclick="([^"]*)"/) || [])[1] || '';
  const event = (onclick.match(/event:'([^']*)'/) || [])[1] || '';
  const text = tag.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
  const variant = Object.keys(HEADER_CTAS).find((name) => nav.includes(HEADER_CTAS[name])) || '';
  const both = nav.includes(HEADER_CTAS.call) && nav.includes(HEADER_CTAS.consultation);
  return { href, onclick, event, text, variant, both, nav };
}

function sha(s) {
  return crypto.createHash('sha256').update(s).digest('hex').slice(0, 12);
}

function extract(head) {
  const take = (re) => [...head.matchAll(re)].map((m) => m[0]);
  return {
    title: take(/<title>[\s\S]*?<\/title>/g),
    description: take(/<meta name="description"[^>]*>/g),
    canonical: take(/<link rel="canonical"[^>]*>/g),
    robots: take(/<meta name="robots"[^>]*>/g),
    openGraph: take(/<meta property="og:[^"]+"[^>]*>/g),
    twitter: take(/<meta name="twitter:[^"]+"[^>]*>/g),
    jsonLd: take(/<script type="application\/ld\+json">[\s\S]*?<\/script>/g),
    scripts: take(/<script[\s\S]*?<\/script>/g),
  };
}

function main() {
  const fresh = spawnSync(process.execPath, [require('path').join(__dirname, 'build-pages.js'), '--check'], {
    encoding: 'utf8',
  });
  if (fresh.status !== 0) {
    process.stderr.write(fresh.stdout || '');
    process.stderr.write(fresh.stderr || '');
    process.exit(fresh.status || 1);
  }
  process.stdout.write(fresh.stdout);

  const pages = buildAll();
  let failed = 0;
  console.log('Head and tracking check (' + pages.length + ' pages)');
  for (const page of pages) {
    const outHead = headOf(page.html);
    const same = outHead === page.sourceHead;
    const src = extract(page.sourceHead);
    const out = extract(outHead);
    const blocks = Object.keys(src).filter((key) => JSON.stringify(src[key]) !== JSON.stringify(out[key]));
    const gtm = (outHead.match(/GTM-W663FFHP/g) || []).length;
    const clarity = (outHead.match(/ywo318ii9u/g) || []).length;
    const status = same && !blocks.length ? 'PASS' : 'FAIL';
    if (status === 'FAIL') failed += 1;
    console.log(
      status +
        '\t' + page.rel +
        '\thead ' + sha(outHead) +
        '\ttitle ' + src.title.length +
        '\tdesc ' + src.description.length +
        '\tcanonical ' + src.canonical.length +
        '\tog ' + src.openGraph.length +
        '\ttwitter ' + src.twitter.length +
        '\tjsonld ' + src.jsonLd.length +
        '\tscripts ' + src.scripts.length +
        '\tgtm ' + gtm +
        '\tclarity ' + clarity +
        (blocks.length ? '\tmismatch ' + blocks.join(',') : '')
    );
  }
  if (failed) {
    console.error(failed + ' pages failed the head check.');
    process.exit(1);
  }
  console.log('All ' + pages.length + ' heads match, including tracking and meta.');

  const byVariant = { call: [], consultation: [] };
  let ctaFailed = 0;
  console.log('Header CTA check (' + pages.length + ' pages)');
  for (const page of pages) {
    const sourcePath = path.join(__dirname, '..', 'templates', 'pages', page.rel);
    const source = fs.readFileSync(sourcePath, 'utf8');
    const expected = headerCta(source);
    const actual = headerCta(page.html);
    const reasons = [];
    if (expected.error) reasons.push('source ' + expected.error);
    if (actual.error) reasons.push('output ' + actual.error);
    if (actual.both || expected.both) reasons.push('header has both a call button and a form CTA');
    if (expected.href !== actual.href) reasons.push('href ' + actual.href + ' != ' + expected.href);
    if (expected.onclick !== actual.onclick) reasons.push('tracking ' + actual.onclick + ' != ' + expected.onclick);
    if (expected.text !== actual.text) reasons.push('text ' + actual.text + ' != ' + expected.text);
    if (expected.event !== actual.event) reasons.push('event ' + actual.event + ' != ' + expected.event);
    if (page.headerVariant !== expected.variant || actual.variant !== expected.variant) {
      reasons.push('variant ' + actual.variant + ' != ' + expected.variant);
    }
    const status = reasons.length ? 'FAIL' : 'PASS';
    if (status === 'FAIL') ctaFailed += 1;
    else byVariant[expected.variant].push(page.rel);
    console.log(
      status + '\t' + expected.variant + '\t' + page.rel +
        '\thref ' + actual.href +
        '\tevent ' + actual.event +
        '\ttext ' + actual.text +
        (reasons.length ? '\t' + reasons.join('; ') : '')
    );
  }
  if (ctaFailed) {
    console.error(ctaFailed + ' pages failed the header CTA check.');
    process.exit(1);
  }
  console.log('All ' + pages.length + ' header CTAs match the original text, href, and tracking.');
  console.log('call (' + byVariant.call.length + '): ' + byVariant.call.join(', '));
  console.log('consultation (' + byVariant.consultation.length + '): ' + byVariant.consultation.join(', '));
}

main();
