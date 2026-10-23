#!/usr/bin/env node
/**
 * Build flat HTML from templates/pages + partials.
 *
 * Edit the header in templates/partials/header.html.
 * The {{cta}} slot is call or consultation, taken from that page's original nav button.
 * Edit the footer in templates/partials/footer.html.
 * Edit a call bar in templates/partials/sticky-call.html or sticky-assessment.html.
 * Edit the phone conversation and About / Terms / Privacy look in assets/site.css.
 * Edit About, Terms or Privacy copy in templates/pages/<file>.html, then rebuild.
 * Page <head> blocks are copied through unchanged.
 *
 *   node scripts/build-pages.js           write HTML next to the site root
 *   node scripts/build-pages.js --check   fail if committed HTML is stale
 *
 * Cloudflare Pages should keep serving the committed HTML. No build command change.
 */
'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const PAGE_ROOT = path.join(ROOT, 'templates', 'pages');
const PARTIALS = path.join(ROOT, 'templates', 'partials');
const SHELLS = path.join(ROOT, 'templates', 'shells');

const LANDING = new Set([
  'index.html',
  'missed-call-text-back.html',
  'ai-receptionist.html',
  'ai-receptionist-for-salons.html',
  'google-review-requests.html',
  'google-review-requests-for-salons.html',
  'quote-follow-up-win-back.html',
  'website-chat-to-text.html',
  'text-to-pay.html',
  'contractor-websites.html',
  'for-home-services.html',
  'for-appointment-businesses.html',
  'for-law-firms-accountants-and-advisors.html',
  'ai-governance.html',
  'fractional-ai-officer.html',
  'ai-support-agent.html',
]);
const INFO = new Set(['about.html', 'terms.html', 'privacy.html']);
const PAGE = new Set([
  '404.html',
  'margin-leakage-calculator.html',
  'ai-exposure-score.html',
  'ai-automation-roi-guide.html',
]);

const CALL = '<a href="tel:+16473605774" class="btn-primary" onclick="window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:\'click_to_call\'});">Call (647) 360-5774</a>';

const HEADER_CTAS = {
  call: '<a href="tel:+16473605774" class="nav-cta" aria-label="Call (647) 360-5774" onclick="window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:\'click_to_call\'});">Call (647) 360-5774</a>',
  consultation: '<a href="/fractional-ai-officer#assessment" class="nav-cta gov-form-cta" onclick="window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:\'form_cta_click\'});"><span class="cta-full">Book My AI Consultation</span><span class="cta-short">Book My AI Consultation</span></a>',
};

function headerVariant(source, rel) {
  const navAt = source.indexOf('<nav');
  const navEnd = source.indexOf('</nav>', navAt);
  if (navAt < 0 || navEnd < 0) throw new Error(rel + ' is missing a nav');
  const nav = source.slice(navAt, navEnd);
  const found = Object.keys(HEADER_CTAS).filter((name) => nav.includes(HEADER_CTAS[name]));
  if (found.length !== 1) {
    throw new Error(rel + ' header CTA must be exactly one of call or consultation');
  }
  const other = found[0] === 'call' ? 'consultation' : 'call';
  if (nav.includes(HEADER_CTAS[other])) {
    throw new Error(rel + ' header has both a call button and a form CTA');
  }
  return found[0];
}

function headerPartial(variant) {
  const raw = partial('header.html');
  if ((raw.match(/\{\{cta\}\}/g) || []).length !== 1) {
    throw new Error('templates/partials/header.html must contain one {{cta}} slot');
  }
  return raw.replace('{{cta}}', () => HEADER_CTAS[variant]);
}

function read(file) {
  return fs.readFileSync(file, 'utf8');
}

function partial(name) {
  return read(path.join(PARTIALS, name)).replace(/\s+$/, '');
}

function shell(name) {
  return read(path.join(SHELLS, name + '.html'))
    .split('\n')
    .filter((line) => !line.startsWith('<!-- shell:'))
    .join('\n')
    .trim();
}

function walkPages(dir, acc = []) {
  for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, ent.name);
    if (ent.isDirectory()) walkPages(p, acc);
    else if (ent.name.endsWith('.html')) acc.push(p);
  }
  return acc;
}

function templateFor(rel) {
  if (rel.startsWith('blog/')) return 'blog';
  if (LANDING.has(rel)) return 'landing';
  if (INFO.has(rel)) return 'info';
  if (PAGE.has(rel)) return 'page';
  throw new Error('No template for ' + rel);
}

function elementEnd(html, start, tag) {
  const lower = html.toLowerCase();
  const open = '<' + tag.toLowerCase();
  const close = '</' + tag.toLowerCase() + '>';
  let i = html.indexOf('>', start) + 1;
  let depth = 1;
  while (depth > 0 && i < html.length) {
    const nextClose = lower.indexOf(close, i);
    if (nextClose < 0) throw new Error('Unclosed <' + tag + '>');
    let realOpen = -1;
    let scan = lower.indexOf(open, i);
    while (scan >= 0 && scan < nextClose) {
      const after = lower[scan + open.length] || '';
      if (!/[a-z0-9]/.test(after)) {
        realOpen = scan;
        break;
      }
      scan = lower.indexOf(open, scan + open.length);
    }
    if (realOpen >= 0) {
      depth += 1;
      i = html.indexOf('>', realOpen) + 1;
    } else {
      depth -= 1;
      i = nextClose + close.length;
    }
  }
  if (depth !== 0) throw new Error('Unclosed <' + tag + '>');
  return i;
}

function replaceElement(html, tag, replacement, which) {
  const re = new RegExp('<' + tag + '\\b', 'gi');
  const starts = [];
  let m;
  while ((m = re.exec(html))) starts.push(m.index);
  if (!starts.length) throw new Error('Missing <' + tag + '>');
  const start = which === 'last' ? starts[starts.length - 1] : starts[0];
  const end = elementEnd(html, start, tag);
  return html.slice(0, start) + replacement + html.slice(end);
}

function splitPage(html) {
  const bodyAt = html.indexOf('<body');
  if (bodyAt < 0) throw new Error('Missing body');
  const bodyOpenEnd = html.indexOf('>', bodyAt) + 1;
  const navAt = html.indexOf('<nav', bodyOpenEnd);
  const navEnd = elementEnd(html, navAt, 'nav');
  const footerAt = html.indexOf('<footer', navEnd);
  const footerEnd = elementEnd(html, footerAt, 'footer');
  const between = html.slice(navEnd, footerAt);
  const stickyAt = between.search(/<div class="sticky-mobile-cta\b/);
  if (stickyAt < 0) throw new Error('Missing sticky call bar');
  const stickyEnd = elementEnd(between, stickyAt, 'div');
  return {
    head: html.slice(0, bodyAt),
    bodyOpen: html.slice(bodyAt, bodyOpenEnd),
    preamble: html.slice(bodyOpenEnd, navAt),
    beforeSticky: between.slice(0, stickyAt),
    afterSticky: between.slice(stickyEnd),
    stickyKind: between.slice(stickyAt, stickyEnd).includes('sticky-assessment') ? 'assessment' : 'call',
    trail: html.slice(footerEnd),
  };
}

function renderConvo({ name, sub, avatar, wide, messages }) {
  const who = name
    ? `<div class="tl-convo-header"><div class="tl-convo-avatar" aria-hidden="true">${avatar || 'T'}</div><div><div class="tl-convo-name">${name}</div>${sub ? `<div class="tl-convo-sub">${sub}</div>` : ''}</div></div>`
    : '';
  const bubbles = messages
    .map((msg) => `<div class="tl-convo-bubble tl-convo-${msg.side}">${msg.html}</div>`)
    .join('');
  return `<div class="tl-convo${wide ? ' tl-convo-wide' : ''}"><div class="tl-convo-ear" aria-hidden="true"></div><div class="tl-convo-screen">${who}<div class="tl-convo-thread">${bubbles}</div></div></div>`;
}

function businessName(text) {
  const names = [
    'Northside Heating & Cooling',
    'Northside Heating',
    'Lakeside Plumbing',
    'Lakeside Heating',
    'North Nail Salon',
    'Trueline text-back',
  ];
  return names.find((name) => text.includes(name)) || '';
}

function renderFromMock(block) {
  const name = (block.match(/class="mock-name">([\s\S]*?)<\/div>/) || [])[1] || '';
  const sub = (block.match(/class="mock-sub">([\s\S]*?)<\/div>/) || [])[1] || '';
  const avatar = (block.match(/class="mock-avatar">([\s\S]*?)<\/div>/) || [])[1] || 'T';
  const messages = [...block.matchAll(/<div class="bubble bubble-(them|us)">([\s\S]*?)<\/div>/g)].map((m) => ({
    side: m[1],
    html: m[2],
  }));
  if (!messages.length) return block;
  const wide = /max-width:\s*520px/.test(block) || messages.some((m) => m.html.includes('Receptionist:'));
  return renderConvo({
    name: name || businessName(messages.map((m) => m.html).join(' ')),
    sub,
    avatar,
    wide,
    messages,
  });
}

function replaceMockPhones(html) {
  let out = '';
  let i = 0;
  const needle = '<div class="mock-phone';
  while (i < html.length) {
    const start = html.indexOf(needle, i);
    if (start < 0) {
      out += html.slice(i);
      break;
    }
    out += html.slice(i, start);
    const end = elementEnd(html, start, 'div');
    const block = html.slice(start, end);
    out += block.includes('class="bubble') ? renderFromMock(block) : block;
    i = end;
  }
  return out;
}

function listMessage(htmlInner) {
  // "Mike, Lakeside Heating:" marks the outgoing side. The name stays in a
  // screen-reader span so the visible SMS is the text itself.
  const owner = htmlInner.match(/^([^:\n]{1,40}, [^:\n]{1,80}):\s*([\s\S]*)$/);
  if (owner) return { side: 'us', html: owner[2].trim(), kind: 'owner', label: owner[1].trim() };
  if (htmlInner.startsWith('Your business:') || htmlInner.startsWith('Receptionist:')) {
    return { side: 'us', html: htmlInner, kind: 'label' };
  }
  if (htmlInner.startsWith('Caller:')) {
    return { side: 'them', html: htmlInner.replace(/^Caller:\s*/, ''), kind: 'caller', full: htmlInner };
  }
  return { side: 'them', html: htmlInner, kind: 'them' };
}

function replaceConversationLists(html) {
  return html.replace(/<ul>(?:\s*<li>(?:Caller|Your business|Receptionist|[^<:\n]{1,40}, [^<:\n]{1,80}):[\s\S]*?<\/li>)+\s*<\/ul>/g, (block) => {
    const parsed = [...block.matchAll(/<li>([\s\S]*?)<\/li>/g)].map((m) => listMessage(m[1].trim()));
    const ownerThread = parsed.some((item) => item.kind === 'owner');
    const messages = parsed.map((item) => {
      if (ownerThread && item.label) {
        return { side: item.side, html: `<span class="sr-only">${item.label}:</span> ${item.html}` };
      }
      if (ownerThread && item.kind === 'caller') {
        return { side: item.side, html: `<span class="sr-only">Caller:</span> ${item.html}` };
      }
      if (item.kind === 'caller') return { side: item.side, html: item.full };
      return { side: item.side, html: item.html };
    });
    const joined = messages.map((m) => m.html).join(' ');
    const call = messages.some((m) => m.html.startsWith('Receptionist:'));
    return renderConvo({
      name: businessName(joined),
      sub: call ? '' : 'Your business number',
      avatar: 'T',
      wide: call,
      messages,
    });
  });
}

function applyConversations(html) {
  return replaceConversationLists(replaceMockPhones(html));
}

function expandIncludes(html) {
  return html.replace(/<!--\s*include:([a-z0-9-]+)\s*-->/g, (match, name) => {
    const file = path.join(PARTIALS, name + '.html');
    if (!fs.existsSync(file)) throw new Error('Missing partial ' + name);
    return read(file).trim();
  });
}

function stripStyle(html) {
  return html.replace(/\sstyle="[^"]*"/g, '');
}

function inner(html, tag) {
  const start = html.indexOf('<' + tag);
  const openEnd = html.indexOf('>', start) + 1;
  const end = elementEnd(html, start, tag);
  return html.slice(openEnd, end - ('</' + tag + '>').length);
}

function sharedInfoHero() {
  const about = read(path.join(PAGE_ROOT, 'about.html'));
  const main = inner(about.slice(about.indexOf('<main')), 'main');
  const promise = must(main, /<p class="hero-promise">([\s\S]*?)<\/p>/, 'about promise');
  const trusts = [...main.matchAll(/<div class="trust-item">\s*(<svg[\s\S]*?<\/svg>)\s*([^<]+?)\s*<\/div>/g)].map((m) => ({
    icon: m[1],
    text: m[2].trim(),
  }));
  if (trusts.length !== 4) throw new Error('Expected 4 trust chips, got ' + trusts.length);
  return { promise, trusts };
}

function infoHero(model) {
  const shared = sharedInfoHero();
  const chips = shared.trusts.map((item) => `<div class="trust-item">${item.icon}${item.text}</div>`).join('\n');
  return `<header class="info-hero">
  <div class="info-wrap">
    <p class="info-kicker">${model.kicker}</p>
    <h1>${model.title}</h1>
    <p class="info-lede">${model.lede}</p>
    <div class="hero-actions">${CALL}</div>
    <p class="hero-promise">${shared.promise}</p>
    <div class="hero-trust">
${chips}
    </div>
  </div>
</header>`;
}

function infoArticle(inner) {
  return `<article class="info-body">\n  <div class="info-wrap">\n${inner.trim()}\n  </div>\n</article>`;
}

function infoCta(model) {
  const sub = model.ctaSub ? `\n    <p>${model.ctaSub}</p>` : '';
  return `<section class="info-cta" id="contact-cta">
  <div class="info-wrap">
    <p class="info-label">${model.ctaLabel}</p>
    <h2>${model.ctaHeading}</h2>${sub}
    <p>${CALL}</p>
    <p class="info-cta-note">${model.ctaNote}</p>
  </div>
</section>`;
}

function infoMain(model) {
  return `<main id="main" tabindex="-1">
${infoHero(model)}
${model.body}
${model.closingHtml !== undefined ? model.closingHtml : infoCta(model)}
</main>`;
}

function aboutBand(id, label, h2, rest) {
  const idAttr = id ? ` id="${id}"` : '';
  const labelHtml = label ? `<p class="info-label">${label}</p>\n` : '';
  if (/<details\b/.test(rest)) {
    return `<section class="info-faq"${idAttr}>
  <div class="info-wrap">
    ${labelHtml}<h2>${h2}</h2>
    <div class="faq-list">
${rest.trim()}
    </div>
  </div>
</section>`;
  }
  let body = rest.trim();
  if (body.includes('class="contact-form"')) {
    const note = (body.match(/<p style="margin-top:12px;font-size:0\.95rem;">([\s\S]*?)<\/p>/) || [])[1] || '';
    const prose = body.replace(/<div class="contact-form"[\s\S]*<\/div>\s*$/, '').trim();
    const noteHtml = note ? `\n    <p class="info-card-note">${note}</p>` : '';
    body = `${prose}\n  <div class="info-card">\n    <p>${CALL}</p>${noteHtml}\n  </div>`;
  }
  return `<section class="info-band"${idAttr}>
  ${labelHtml}<h2>${h2}</h2>
  ${body}
</section>`;
}

function must(html, re, label) {
  const m = html.match(re);
  if (!m) throw new Error('Missing ' + label);
  return m[1];
}

function aboutModel(html) {
  const main = inner(html.slice(html.indexOf('<main')), 'main');
  const kicker = must(main, /<div class="hero-pre">([\s\S]*?)<\/div>/, 'about kicker');
  const title = must(main, /<h1>([\s\S]*?)<\/h1>/, 'about title');
  const lede = must(main, /<p class="hero-sub">([\s\S]*?)<\/p>/, 'about lede');
  const shared = sharedInfoHero();
  if (lede.includes(shared.promise)) throw new Error('About lede should not repeat the promise line');
  const blocks = [...main.matchAll(/<section class="(contact-section|hub-section)"([^>]*)>([\s\S]*?)<\/section>/g)];
  const parts = [];
  for (const block of blocks) {
    const kind = block[1];
    const attrs = block[2];
    const chunk = block[3];
    const label = (chunk.match(/<p class="section-label">([\s\S]*?)<\/p>/) || [])[1] || '';
    const h2 = (chunk.match(/<h2>([\s\S]*?)<\/h2>/) || [])[1] || '';
    const rest = chunk.slice(chunk.indexOf('</h2>') + 5);
    const id = (attrs.match(/\sid="([^"]+)"/) || [])[1] || '';
    if (kind === 'hub-section') {
      parts.push({
        kind: 'light',
        html: `<section class="info-block"${id ? ` id="${id}"` : ''}>\n${label ? `<p class="info-label">${label}</p>\n` : ''}<h2>${h2}</h2>\n${rest.trim()}\n</section>`,
      });
    } else {
      parts.push({ kind: 'band', html: aboutBand(id, label, h2, rest) });
    }
  }
  const aside = must(main, /<p class="minor-audience" id="firms">([\s\S]*?)<\/p>/, 'firms aside');
  const salonsAt = parts.findIndex((part) => part.html.includes('id="salons"'));
  if (salonsAt < 0) throw new Error('Missing salons section');
  parts.splice(salonsAt + 1, 0, { kind: 'aside', html: `<p class="minor-audience" id="firms">${aside}</p>` });
  let body = '';
  let light = [];
  const flush = () => {
    if (!light.length) return;
    body += infoArticle(light.join('\n')) + '\n';
    light = [];
  };
  for (const part of parts) {
    if (part.kind === 'light') light.push(part.html);
    else {
      flush();
      body += part.html + '\n';
    }
  }
  flush();
  if ((body.match(/id="contact"/g) || []).length !== 1) throw new Error('About should keep a single id="contact"');
  if (body.includes('<p>' + shared.promise + '</p>')) throw new Error('Promise line duplicated in the About body');
  if (body.includes('<li>' + shared.trusts[0].text)) throw new Error('Trust list duplicated in the About body');
  return {
    kicker,
    title,
    lede,
    body: body.trim(),
    closingHtml: '',
  };
}

function topLevelElements(html) {
  const out = [];
  let i = 0;
  while (i < html.length) {
    while (i < html.length && /\s/.test(html[i])) i += 1;
    if (i >= html.length) break;
    if (html.startsWith('<!--', i)) {
      const j = html.indexOf('-->', i);
      out.push(html.slice(i, j + 3));
      i = j + 3;
      continue;
    }
    if (html[i] !== '<') {
      const j = html.indexOf('<', i);
      const end = j < 0 ? html.length : j;
      out.push(html.slice(i, end));
      i = end;
      continue;
    }
    const tagMatch = /^<([a-zA-Z0-9]+)/.exec(html.slice(i));
    if (!tagMatch) throw new Error('Bad markup at ' + i);
    const tag = tagMatch[1];
    const end = elementEnd(html, i, tag);
    out.push(html.slice(i, end));
    i = end;
  }
  return out;
}

function unwrapLegal(main) {
  let out = '';
  for (const node of topLevelElements(main)) {
    if (!node.startsWith('<section')) {
      out += node.trim() + '\n';
      continue;
    }
    for (const child of topLevelElements(inner(node, 'section'))) {
      if (child.startsWith('<div')) out += inner(child, 'div').trim() + '\n';
      else out += child.trim() + '\n';
    }
  }
  return out;
}

function legalModel(html, which) {
  let main = stripStyle(inner(html.slice(html.indexOf('<main')), 'main'));
  const title = must(main, /<h1>([\s\S]*?)<\/h1>/, which + ' title');
  const kicker = must(main, /<p>(Last updated:[^<]*)<\/p>/, which + ' updated');
  main = main.replace(/<h1>[\s\S]*?<\/h1>/, '').replace(/<p>Last updated:[^<]*<\/p>/, '');
  const question = must(main, /<p>(Questions\?[\s\S]*?)<\/p>/, which + ' questions');
  main = main.replace(/<p>Questions\?[\s\S]*?<\/p>/, '');
  let lede = '';
  if (which === 'terms') {
    const intro = main.match(/<p>(This page is the whole agreement[\s\S]*?)<\/p>/);
    if (!intro) throw new Error('Terms intro paragraph missing');
    lede = intro[1];
    main = main.replace(intro[0], '');
  }
  if (which === 'privacy') {
    lede = 'We do not sell your personal information to third parties.';
    if (!main.includes(lede)) throw new Error('Privacy lede sentence missing from the policy');
  }
  main = unwrapLegal(main);
  main = main.replace(/<p><strong>(The short version|On this page)<\/strong><\/p>/g, '<h2>$1</h2>');
  const q = question.replace(/\s+/g, ' ').trim();
  const expected = 'Questions? Call (647) 360-5774. Leave a message and you\'ll get our text within minutes, and a call back fast.';
  if (q !== expected) throw new Error(which + ' questions changed: ' + q);
  return {
    kicker,
    title,
    lede,
    body: infoArticle(main.trim()),
    ctaLabel: 'Questions?',
    ctaHeading: 'Call (647) 360-5774.',
    ctaSub: '',
    ctaNote: '',
  };
}

function buildOne(rel) {
  const source = read(path.join(PAGE_ROOT, rel));
  const template = templateFor(rel);
  const parts = splitPage(source);
  let beforeSticky = parts.beforeSticky;
  let bodyOpen = parts.bodyOpen;
  if (template === 'info') {
    const model = rel === 'about.html' ? aboutModel(source) : legalModel(source, rel.replace('.html', ''));
    beforeSticky = replaceElement(beforeSticky, 'main', infoMain(model));
    bodyOpen = bodyOpen.replace('<body', '<body class="info-page"');
  }
  beforeSticky = expandIncludes(beforeSticky);
  beforeSticky = applyConversations(beforeSticky);
  const variant = headerVariant(source, rel);
  const header = headerPartial(variant);
  const footer = partial('footer.html');
  const sticky = partial(parts.stickyKind === 'assessment' ? 'sticky-assessment.html' : 'sticky-call.html');
  const slots = {
    head: parts.head,
    bodyOpen,
    style: '',
    preamble: parts.preamble,
    header,
    beforeSticky,
    sticky,
    afterSticky: parts.afterSticky,
    footer,
    trail: parts.trail,
  };
  const rendered = shell(template).replace(/\{\{(\w+)\}\}/g, (match, key) => {
    if (!Object.prototype.hasOwnProperty.call(slots, key)) throw new Error('Unknown slot ' + key);
    return slots[key];
  });
  return { rel, template, html: rendered, sourceHead: headOf(source), headerVariant: variant };
}

function headOf(html) {
  const start = html.indexOf('<head');
  const end = html.indexOf('</head>');
  if (start < 0 || end < 0) throw new Error('Missing head');
  return html.slice(start, end + 7);
}

function buildAll() {
  return walkPages(PAGE_ROOT)
    .map((file) => path.relative(PAGE_ROOT, file).split(path.sep).join('/'))
    .sort()
    .map(buildOne);
}

function main() {
  const check = process.argv.includes('--check');
  const pages = buildAll();
  const stale = [];
  for (const page of pages) {
    const outPath = path.join(ROOT, page.rel);
    const nextHead = headOf(page.html);
    if (nextHead !== page.sourceHead) {
      throw new Error('Head changed while building ' + page.rel);
    }
    if (check) {
      const current = fs.existsSync(outPath) ? read(outPath) : '';
      if (current !== page.html) stale.push(page.rel);
    } else {
      fs.mkdirSync(path.dirname(outPath), { recursive: true });
      fs.writeFileSync(outPath, page.html);
    }
  }
  if (check) {
    if (stale.length) {
      console.error('Generated HTML is stale:\n' + stale.join('\n'));
      process.exit(1);
    }
    console.log('Fresh: ' + pages.length + ' pages match the templates.');
    return;
  }
  console.log('Wrote ' + pages.length + ' pages.');
}

if (require.main === module) main();

module.exports = { buildAll, headOf, templateFor, HEADER_CTAS };
