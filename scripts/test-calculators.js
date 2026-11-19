#!/usr/bin/env node
// Unit tests for the service-page calculator formulas (js/calculator.js).
// Hand-worked expected values; fails (exit 1) on any mismatch or if the JS throws.
"use strict";
const path = require("path");
let calc;
try { calc = require(path.join(__dirname, "..", "js", "calculator.js")); }
catch (e) { console.error("test-calculators: FAIL js/calculator.js throws: " + e.message); process.exit(1); }

const cases = [
  // id, inputs (merged over defaults), expected monthly $, expected sub (or null)
  ["missed-call-text-back", {}, 2258, "About 6.5 jobs a month, or $27,096 a year."],       // 5 x 0.30 x 350 x 4.3 = 2257.5
  ["missed-call-text-back", { calls: 10, book: 50, job: 400 }, 8600, null],                  // 10 x .5 x 400 x 4.3
  ["missed-call-text-back", { calls: 0 }, 0, "About 0 jobs a month, or $0 a year."],
  ["ai-receptionist", {}, 3870, "About 8.6 jobs a month, or $46,440 a year."],             // 8 x .25 x 450 x 4.3
  ["ai-receptionist-for-salons", {}, 1828, null],                                            // 10 x .5 x 85 x 4.3 = 1827.5
  ["google-review-requests", {}, 350, "That\u2019s $4,200 a year. You finish about 21 jobs a month without asking for a review."],
  ["google-review-requests", { extra: 3, job: 500 }, 1500, null],
  ["google-review-requests-for-salons", {}, 170, null],                                      // 2 x 85
  ["quote-follow-up-win-back", {}, 2500, "About 1 job a month, or $30,000 a year."],       // 20 x .5 x .1 x 2500
  ["quote-follow-up-win-back", { quotes: 40, quiet: 60, win: 15, job: 4000 }, 14400, null], // 40 x .6 x .15 x 4000
  ["website-chat-to-text", {}, 1500, null],                                                  // 500 x .03 x .25 x 400
  ["text-to-pay", {}, 16800, "Every day you wait holds about $800 more."],                 // 40 x 600 x 21 / 30
  ["text-to-pay", { inv: 10, amt: 300, days: 30 }, 3000, null],
  ["contractor-websites", {}, 2400, null],                                                   // 300 x .05 x .4 x 400
  ["lead-follow-up", {}, 1500, null],                                                        // 40 x .3 x .25 x 500
  ["appointment-reminders", {}, 2339, null],                                                 // 80 x .08 x 85 x 4.3 = 2339.2
  ["cold-outreach", {}, 6000, "If each client books you 2 times a year, one month of new clients is worth $12,000 a year."],
  ["cold-outreach", { rep: 1 }, 6000, "If each client books you 1 time a year, one month of new clients is worth $6,000 a year."],
  ["crm-setup", {}, 2568, "$1,600 in slipped jobs plus $968 of your time."],               // 2 x 800 + 3 x 75 x 4.3
  ["custom-dashboards", {}, 968, null],                                                      // 3 x 75 x 4.3 = 967.5
  ["multi-location", {}, 5418, null],                                                        // 3 x 4 x .3 x 350 x 4.3
  ["ai-support-agent", {}, 1032, "About 17.2 staff hours a month, or $12,384 a year."],     // 40 x 6/60 x 60 x 4.3
];
const fails = [];
for (const [id, over, want, sub] of cases) {
  const v = Object.assign(calc.defaults(id), over);
  const r = calc.result(id, v);
  if (r.main !== want) fails.push(id + " " + JSON.stringify(over) + ": got " + r.main + ", want " + want);
  if (sub !== null && r.sub !== sub) fails.push(id + " sub: got \"" + r.sub + "\", want \"" + sub + "\"");
  if (r.mainText !== calc.money(want)) fails.push(id + " text " + r.mainText);
}
// Every calculator: defaults inside range, finite results across min/max corners, money format.
for (const id of Object.keys(calc.CALCS)) {
  const c = calc.CALCS[id];
  for (const i of c.inputs) if (i.v < i.min || i.v > i.max) fails.push(id + "." + i.k + " default outside range");
  for (const corner of ["min", "max"]) {
    const v = {}; c.inputs.forEach((i) => { v[i.k] = i[corner]; });
    const r = calc.result(id, v);
    if (!isFinite(r.main) || r.main < 0 || /NaN|undefined/.test(r.sub + r.mainText)) fails.push(id + " bad result at " + corner + ": " + r.mainText + " / " + r.sub);
  }
}
if (calc.money(1234567.4) !== "$1,234,567") fails.push("money format");
if (calc.clamp("abc", { min: 0, max: 10, v: 4 }) !== 4 || calc.clamp(99, { min: 0, max: 10, v: 4 }) !== 10) fails.push("clamp");
// DOM run: execute the shipped file in a stub browser so a runtime error in the wiring code
// fails the build too. Moving a slider must update the big number and the number box.
{
  const fs = require("fs"), vm = require("vm");
  const src = fs.readFileSync(path.join(__dirname, "..", "js", "calculator.js"), "utf8");
  const el = (attrs) => { const h = {}; return { value: String(attrs.value || ""), textContent: "", attrs, style: { setProperty() {} }, classList: { add() {} },
    getAttribute: (k) => (k in attrs ? attrs[k] : null), setAttribute(k, v) { attrs[k] = String(v); },
    addEventListener: (t, fn) => { (h[t] = h[t] || []).push(fn); }, fire(t) { (h[t] || []).forEach((fn) => fn()); } }; };
  const sections = Object.keys(calc.CALCS).map((id) => {
    const c = calc.CALCS[id], q = {};
    c.inputs.forEach((i) => { q['input[type="range"][data-k="' + i.k + '"]'] = el({ value: i.v }); q['input[type="number"][data-k="' + i.k + '"]'] = el({ value: i.v }); });
    q['[data-out="main"]'] = el({}); q['[data-out="sub"]'] = el({});
    const sec = el({ "data-calc": id }); sec.querySelector = (s) => q[s] || null; sec.q = q; sec.id = id; return sec;
  });
  const win = { dataLayer: [] };
  win.window = win;
  win.document = { readyState: "complete", querySelectorAll: () => sections, addEventListener() {} };
  try { vm.runInNewContext(src, win, { filename: "calculator.js" }); }
  catch (e) { fails.push("calculator.js throws in a browser context: " + e.message); }
  for (const sec of sections) {
    const c = calc.CALCS[sec.id];
    const main = sec.q['[data-out="main"]'];
    if (main.textContent !== calc.result(sec.id, calc.defaults(sec.id)).mainText) { fails.push(sec.id + " DOM: initial result " + main.textContent); continue; }
    const i = c.inputs[0];
    const r = sec.q['input[type="range"][data-k="' + i.k + '"]'], n = sec.q['input[type="number"][data-k="' + i.k + '"]'];
    r.value = String(i.max); r.fire("input");
    const v = calc.defaults(sec.id); v[i.k] = i.max;
    if (main.textContent !== calc.result(sec.id, v).mainText || n.value !== String(i.max)) fails.push(sec.id + " DOM: slider did not update result/box");
    n.value = String(i.max * 10); n.fire("change");
    if (String(r.value) !== String(i.max) || String(n.value) !== String(i.max)) fails.push(sec.id + " DOM: typed value not clamped");
  }
  if (win.dataLayer.filter((e) => e.event === "calculator_interact").length !== sections.length) fails.push("DOM: calculator_interact should fire once per calculator");
}
if (fails.length) { console.error("test-calculators: FAIL (" + fails.length + ")\n- " + fails.join("\n- ")); process.exit(1); }
console.log("test-calculators: OK. " + cases.length + " formula cases, " + Object.keys(calc.CALCS).length + " calculators range-checked.");
