#!/usr/bin/env node
/**
 * Isolated browser checks. External requests, analytics, dials, and form posts are blocked.
 * Hero opacity is read at animation currentTime 0, which is inside animation-delay.
 * The calculator is executed, not string-matched.
 */
'use strict';

const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const PORT = 8765;
const DEBUG_PORT = 9333;
const HERO_PAGES = ['/', '/about', '/privacy', '/terms', '/ai-exposure-score', '/ai-automation-roi-guide'];

function fail(msg) {
  console.error('FAIL\t' + msg);
  process.exitCode = 1;
}
function pass(msg) {
  console.log('PASS\t' + msg);
}

function startServer() {
  const types = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.ico': 'image/x-icon' };
  return http.createServer((req, res) => {
    const url = new URL(req.url, 'http://127.0.0.1');
    let rel = decodeURIComponent(url.pathname);
    if (rel.endsWith('/')) rel += 'index.html';
    let file = path.normalize(path.join(ROOT, rel));
    if (!file.startsWith(ROOT)) {
      res.writeHead(404);
      res.end('missing');
      return;
    }
    if (!fs.existsSync(file) && fs.existsSync(file + '.html')) file += '.html';
    if (!fs.existsSync(file) || fs.statSync(file).isDirectory()) {
      res.writeHead(404);
      res.end('missing');
      return;
    }
    res.writeHead(200, { 'content-type': types[path.extname(file)] || 'application/octet-stream', 'cache-control': 'no-store' });
    fs.createReadStream(file).pipe(res);
  }).listen(PORT, '127.0.0.1');
}

class Cdp {
  constructor(ws) {
    this.ws = ws;
    this.next = 1;
    this.pending = new Map();
    this.events = [];
    ws.addEventListener('message', (ev) => {
      const raw = typeof ev.data === 'string' ? ev.data : Buffer.from(ev.data).toString();
      const msg = JSON.parse(raw);
      if (msg.id && this.pending.has(msg.id)) {
        const { resolve, reject } = this.pending.get(msg.id);
        this.pending.delete(msg.id);
        if (msg.error) reject(new Error(msg.error.message || JSON.stringify(msg.error)));
        else resolve(msg.result || {});
      } else this.events.forEach((fn) => fn(msg));
    });
  }
  send(method, params = {}, sessionId) {
    const id = this.next++;
    const payload = { id, method, params };
    if (sessionId) payload.sessionId = sessionId;
    return new Promise((resolve, reject) => {
      this.pending.set(id, { resolve, reject });
      this.ws.send(JSON.stringify(payload));
    });
  }
  on(fn) { this.events.push(fn); }
}

const MEASURE = `(() => {
  const measure = () => {
    const nodes = Array.from(document.querySelectorAll('.hero-inner > *'));
    const h1 = document.querySelector('.hero-inner h1, .hero h1, h1');
    const rows = (nodes.length ? nodes : [h1]).filter(Boolean).map((el) => {
      const anims = el.getAnimations();
      anims.forEach((a) => { a.pause(); a.currentTime = 0; });
      const cs = getComputedStyle(el);
      return {
        tag: el.tagName,
        opacity: cs.opacity,
        visibility: cs.visibility,
        delay: cs.animationDelay,
        name: cs.animationName,
        anims: anims.length
      };
    });
    window.__hero = { rows, text: h1 ? h1.textContent.trim().slice(0, 90) : '' };
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', measure, { once: true });
  else measure();
})();`;

async function main() {
  const server = startServer();
  const chrome = spawn('google-chrome', [
    '--headless=new', '--disable-gpu', '--no-sandbox', '--disable-dev-shm-usage',
    '--remote-debugging-port=' + DEBUG_PORT, '--user-data-dir=/tmp/tl-chrome-behavior',
    '--window-size=1440,900', 'about:blank'
  ], { stdio: 'ignore' });
  const blocked = [];
  let cdp;
  let sessionId;
  try {
    let version;
    for (let i = 0; i < 40; i++) {
      try {
        version = await fetch('http://127.0.0.1:' + DEBUG_PORT + '/json/version').then((r) => r.json());
        break;
      } catch (e) {
        await new Promise((r) => setTimeout(r, 150));
      }
    }
    if (!version) throw new Error('Chrome did not open a debugging port');
    const ws = new WebSocket(version.webSocketDebuggerUrl);
    await new Promise((resolve, reject) => { ws.addEventListener('open', resolve); ws.addEventListener('error', reject); });
    cdp = new Cdp(ws);
    const target = await cdp.send('Target.createTarget', { url: 'about:blank' });
    const attached = await cdp.send('Target.attachToTarget', { targetId: target.targetId, flatten: true });
    sessionId = attached.sessionId;
    cdp.on((msg) => {
      if (msg.method !== 'Fetch.requestPaused' || msg.sessionId !== sessionId) return;
      const { requestId, request } = msg.params;
      let host = '';
      try { host = new URL(request.url).hostname; } catch (e) { host = ''; }
      const local = host === '127.0.0.1' || host === 'localhost' || request.url.startsWith('data:');
      const call = local
        ? cdp.send('Fetch.continueRequest', { requestId }, sessionId)
        : (blocked.push(request.method + ' ' + request.url), cdp.send('Fetch.failRequest', { requestId, errorReason: 'BlockedByClient' }, sessionId));
      call.catch((err) => console.error('request control failed', err.message));
    });
    await cdp.send('Page.enable', {}, sessionId);
    await cdp.send('Runtime.enable', {}, sessionId);
    await cdp.send('Fetch.enable', { patterns: [{ urlPattern: '*' }] }, sessionId);
    await cdp.send('Page.addScriptToEvaluateOnNewDocument', { source: MEASURE }, sessionId);

    for (const route of HERO_PAGES) {
      await cdp.send('Page.navigate', { url: 'http://127.0.0.1:' + PORT + route }, sessionId);
      let hero = null;
      for (let i = 0; i < 40; i++) {
        const result = await cdp.send('Runtime.evaluate', { expression: 'window.__hero || null', returnByValue: true }, sessionId);
        if (result.exceptionDetails) console.error(route, JSON.stringify(result.exceptionDetails).slice(0, 300));
        hero = result.result && result.result.value;
        if (hero) break;
        await new Promise((r) => setTimeout(r, 50));
      }
      if (!hero || !hero.rows || !hero.rows.length) {
        fail(route + ' did not expose a hero measurement');
        continue;
      }
      const hidden = hero.rows.filter((row) => Number(row.opacity) < 1 || row.visibility === 'hidden');
      const pending = hero.rows.filter((row) => row.name !== 'none' && row.anims === 0);
      if (hidden.length) fail(route + ' hidden during delay: ' + JSON.stringify(hidden));
      else if (pending.length) fail(route + ' animation was not paused at delay start: ' + JSON.stringify(pending));
      else pass(route + ' H1 visible at delay start (' + hero.rows.length + ' hero children, opacity 1) "' + hero.text.slice(0, 48) + '"');
      await cdp.send('Runtime.evaluate', { expression: 'delete window.__hero', returnByValue: true }, sessionId);
    }

    await cdp.send('Page.navigate', { url: 'http://127.0.0.1:' + PORT + '/margin-leakage-calculator' }, sessionId);
    let calc = null;
    for (let i = 0; i < 40; i++) {
      const result = await cdp.send('Runtime.evaluate', {
        expression: `(() => {
          const leak = document.getElementById('out-leakage');
          const risk = document.getElementById('out-risk-events');
          if (!leak || leak.innerText === '—') return null;
          const before = { leak: leak.innerText, risk: risk.innerText };
          const input = document.getElementById('employees');
          input.value = '26';
          input.dispatchEvent(new Event('input', { bubbles: true }));
          const form = document.getElementById('discovery-form');
          return { before, after: { leak: leak.innerText, risk: risk.innerText }, formVisible: !form || getComputedStyle(form).display !== 'none' };
        })()`,
        returnByValue: true
      }, sessionId);
      calc = result.result && result.result.value;
      if (calc) break;
      await new Promise((r) => setTimeout(r, 50));
    }
    if (!calc) fail('calculator did not produce a result');
    else if (calc.before.leak !== '$59,766' || calc.before.risk !== '135') fail('default result ' + JSON.stringify(calc.before));
    else if (calc.after.leak !== '$62,156' || calc.after.risk !== '140') fail('input change result ' + JSON.stringify(calc.after));
    else if (!calc.formVisible) fail('calculator form was submitted');
    else pass('calculator default $59,766 / 135, then 26 employees -> $62,156 / 140, form not submitted');

    const shots = [
      ['/', '/opt/cursor/artifacts/local-candidate-NOT-deployed-home-hero.png', ''],
      ['/privacy', '/opt/cursor/artifacts/local-candidate-NOT-deployed-privacy-hero.png', ''],
      ['/ai-exposure-score', '/opt/cursor/artifacts/local-candidate-NOT-deployed-exposure-hero.png', ''],
      ['/blog/voice-ai-law-accounting-confidentiality', '/opt/cursor/artifacts/local-candidate-NOT-deployed-voice-blog-menu.png', 'document.querySelector("details.nav-services").open=true'],
      ['/margin-leakage-calculator', '/opt/cursor/artifacts/local-candidate-NOT-deployed-calculator.png', 'document.getElementById("out-leakage").scrollIntoView({block:"center"})']
    ];
    for (const [route, file, prepare] of shots) {
      await cdp.send('Page.navigate', { url: 'http://127.0.0.1:' + PORT + route }, sessionId);
      await cdp.send('Runtime.evaluate', {
        expression: 'new Promise((resolve) => { if (document.readyState === "complete") resolve(1); else addEventListener("load", () => resolve(1), { once: true }); })',
        awaitPromise: true,
        returnByValue: true
      }, sessionId);
      if (prepare) await cdp.send('Runtime.evaluate', { expression: prepare }, sessionId);
      const png = await cdp.send('Page.captureScreenshot', { format: 'png' }, sessionId);
      fs.mkdirSync(path.dirname(file), { recursive: true });
      fs.writeFileSync(file, Buffer.from(png.data, 'base64'));
      pass('local candidate screenshot ' + path.basename(file));
    }

    const probe = await cdp.send('Runtime.evaluate', {
      expression: `fetch('https://www.google-analytics.com/g/collect',{method:'POST',body:'x'}).then(()=>'sent').catch(()=>'blocked')`,
      awaitPromise: true,
      returnByValue: true
    }, sessionId);
    const probeResult = probe.result && probe.result.value;
    if (probeResult !== 'blocked') fail('external POST was not blocked (' + probeResult + ')');
    else pass('external analytics POST blocked (' + blocked.length + ' requests failed before the network)');
    if (!process.exitCode) console.log('All behavior checks passed.');
  } finally {
    try { if (cdp) cdp.ws.close(); } catch (e) {}
    if (chrome) chrome.kill('SIGKILL');
    server.close();
    setTimeout(() => process.exit(process.exitCode || 0), 50);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
