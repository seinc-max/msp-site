#!/usr/bin/env node
/**
 * Proves generated pages are fresh and that every page <head>
 * (title, description, canonical, Open Graph, JSON-LD, and tracking)
 * matches the source page byte for byte.
 *
 *   node scripts/check-pages.js
 */
'use strict';

const crypto = require('crypto');
const { spawnSync } = require('child_process');
const { buildAll, headOf } = require('./build-pages');

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
}

main();
