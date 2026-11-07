#!/usr/bin/env node
/**
 * COPY-322-01: missed-call text-back must not say the text comes from the
 * business number on the home FAQ (visible and JSON-LD) or the trades hub.
 * Other offers keep their own business-number lines. No network calls.
 */
'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const OLD = 'from your business number';
const NEW = 'from a separate text-back number';
const errors = [];
const fail = (msg) => { errors.push(msg); console.log('FAIL\t' + msg); };
const pass = (msg) => console.log('PASS\t' + msg);

function read(rel) {
  return fs.readFileSync(path.join(ROOT, rel), 'utf8');
}

function isStaleTextbackClaim(text) {
  return text.includes(OLD);
}

const staleFaq = 'A text from your business number within minutes';
const fixedFaq = 'A text from a separate text-back number within minutes';
if (!isStaleTextbackClaim(staleFaq)) fail('detector missed the old FAQ claim');
else pass('detector rejects the old FAQ claim');
if (isStaleTextbackClaim(fixedFaq)) fail('detector flagged the corrected FAQ claim');
else pass('detector accepts the corrected FAQ claim');

function findCallerAnswer(node) {
  if (!node) return '';
  if (Array.isArray(node)) {
    for (const item of node) {
      const hit = findCallerAnswer(item);
      if (hit) return hit;
    }
    return '';
  }
  if (typeof node === 'object') {
    if (node.name === 'What does my caller see?' && node.acceptedAnswer && node.acceptedAnswer.text) {
      return node.acceptedAnswer.text;
    }
    for (const value of Object.values(node)) {
      const hit = findCallerAnswer(value);
      if (hit) return hit;
    }
  }
  return '';
}

function callerAnswer(html, kind) {
  if (kind === 'json') {
    const blocks = [...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)];
    for (const block of blocks) {
      try {
        const hit = findCallerAnswer(JSON.parse(block[1]));
        if (hit) return hit;
      } catch (err) {
        continue;
      }
    }
    return '';
  }
  const match = html.match(/<summary>What does my caller see\?<\/summary><p class="faq-answer">([^<]*)<\/p>/);
  return match ? match[1] : '';
}

for (const file of ['index.html', 'templates/pages/index.html']) {
  const html = read(file);
  const visible = callerAnswer(html, 'visible');
  const schema = callerAnswer(html, 'json');
  if (!visible || !schema) fail(file + ' is missing the caller FAQ');
  else if (visible !== schema) fail(file + ' FAQ text and JSON-LD disagree');
  else if (isStaleTextbackClaim(visible) || !visible.startsWith('A text ' + NEW)) fail(file + ' caller FAQ still has the old number claim');
  else if (!visible.includes('Hi, this is Mike from Lakeside Heating.')) fail(file + ' sample wording changed');
  else pass(file + ' FAQ text and schema agree');
}
if (callerAnswer(read('index.html'), 'visible') !== callerAnswer(read('templates/pages/index.html'), 'visible')) {
  fail('home FAQ template and generated page disagree');
}

const hubLine = '<li>Your caller gets a text within minutes, ' + NEW + '.</li>';
for (const file of ['for-home-services.html', 'templates/pages/for-home-services.html']) {
  const html = read(file);
  if (!html.includes(hubLine) || html.includes(OLD)) fail(file + ' hub text-back line is stale or missing');
  else pass(file + ' hub text-back line uses the separate text-back number');
}
if (!read('templates/pages/for-home-services.html').includes(hubLine)) fail('hub template is not corrected');

const kept = [
  ['quote-follow-up-win-back.html', 'Texts go out from your business number.'],
  ['website-chat-to-text.html', 'reply from your business number'],
  ['website-chat-to-text.html', 'Chats arrive as texts on your business number.'],
  ['website-chat-to-text.html', 'Every new chat arrives as a text on your business number.'],
  ['text-to-pay.html', 'from your business number'],
  ['missed-call-text-back.html', 'get a text back from a separate number'],
  ['missed-call-text-back.html', 'sent from a separate number'],
];
for (const [file, sentence] of kept) {
  if (!read(file).includes(sentence)) fail(file + ' lost protected wording: ' + sentence);
}
pass('other offers and the missed-call page keep their own number wording');

if (errors.length) {
  console.error(errors.length + ' text-back copy checks failed.');
  process.exit(1);
}
console.log('All text-back copy checks passed.');
