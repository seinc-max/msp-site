/* Trueline service-page calculators (Ben 2026-11-19 t1217u). One shared, dependency-free
   component. Each <section class="tl-calc-section" data-calc="<id>"> is filled in by
   scripts/calc-markup.js from CALCS below and wired here. The visitor's own numbers drive
   every result; defaults are example inputs. Results are the value at stake, never a claim
   of what Trueline recovers. Formulas are unit-tested by scripts/test-calculators.js.
   Tracking: one optional dataLayer push {event:'calculator_interact'} per calculator on
   first use. No other tracking; tel and form tracking are untouched. */
(function (root) {
  'use strict';
  var W = 4.3; // weeks in a month, shown in the formula text

  function money(n) {
    n = Math.round(Number(n) || 0);
    return '$' + String(Math.abs(n)).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  }
  function count(n) {
    var r = Math.round((Number(n) || 0) * 10) / 10;
    return String(r).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  }
  var pct = function (p) { return (Number(p) || 0) / 100; };

  // Input units: n = plain number, pct = percent, money = dollars, hrs = hours, min = minutes, days = days.
  var CALCS = {
    'missed-call-text-back': {
      title: 'What are your missed calls worth?',
      inputs: [
        { k: 'calls', label: 'Missed calls a week', min: 0, max: 40, step: 1, v: 5, u: 'n' },
        { k: 'book', label: 'Missed callers who would have booked', min: 0, max: 100, step: 5, v: 30, u: 'pct' },
        { k: 'job', label: 'Your average job value', min: 50, max: 5000, step: 25, v: 350, u: 'money' }
      ],
      f: function (v) { var jobs = v.calls * pct(v.book) * W; var m = jobs * v.job; return { main: m, t: { jobs: count(jobs) } }; },
      sub: 'About {jobs} {jobs|job|jobs} a month, or {year} a year.',
      formula: 'Missed calls a week × % who would have booked × average job value × 4.3 weeks'
    },
    'ai-receptionist': {
      title: 'What are the calls you can\u2019t pick up worth?',
      inputs: [
        { k: 'calls', label: 'Calls you can\u2019t pick up each week', min: 0, max: 50, step: 1, v: 8, u: 'n' },
        { k: 'book', label: 'Callers who would book a job', min: 0, max: 100, step: 5, v: 25, u: 'pct' },
        { k: 'job', label: 'Your average job value', min: 50, max: 5000, step: 25, v: 450, u: 'money' }
      ],
      f: function (v) { var jobs = v.calls * pct(v.book) * W; var m = jobs * v.job; return { main: m, t: { jobs: count(jobs) } }; },
      sub: 'About {jobs} {jobs|job|jobs} a month, or {year} a year.',
      formula: 'Calls you can\u2019t pick up a week × % who would book × average job value × 4.3 weeks'
    },
    'ai-receptionist-for-salons': {
      title: 'What are your missed booking calls worth?',
      inputs: [
        { k: 'calls', label: 'Booking calls you miss each week', min: 0, max: 60, step: 1, v: 10, u: 'n' },
        { k: 'book', label: 'Callers who would have booked', min: 0, max: 100, step: 5, v: 50, u: 'pct' },
        { k: 'visit', label: 'Your average visit value', min: 20, max: 500, step: 5, v: 85, u: 'money' }
      ],
      f: function (v) { var n = v.calls * pct(v.book) * W; var m = n * v.visit; return { main: m, t: { n: count(n) } }; },
      sub: 'About {n} {n|booking|bookings} a month, or {year} a year.',
      formula: 'Missed booking calls a week × % who would have booked × average visit value × 4.3 weeks'
    },
    'google-review-requests': {
      title: 'What one more booked job could be worth to you?',
      inputs: [
        { k: 'extra', label: 'Extra booked jobs a month', min: 0, max: 10, step: 1, v: 1, u: 'n' },
        { k: 'job', label: 'Your average job value', min: 50, max: 5000, step: 25, v: 350, u: 'money' }
      ],
      f: function (v) { return { main: v.extra * v.job, t: {} }; },
      sub: 'That\u2019s {year} a year.',
      formula: 'Extra booked jobs a month × average job value'
    },
    'google-review-requests-for-salons': {
      title: 'What more booked clients could be worth to you?',
      inputs: [
        { k: 'extra', label: 'Extra booked clients a month', min: 0, max: 20, step: 1, v: 2, u: 'n' },
        { k: 'visit', label: 'Your average visit value', min: 20, max: 500, step: 5, v: 85, u: 'money' }
      ],
      f: function (v) { return { main: v.extra * v.visit, t: {} }; },
      sub: 'That\u2019s {year} a year.',
      formula: 'Extra booked clients a month × average visit value'
    },
    'quote-follow-up-win-back': {
      title: 'What are your quiet quotes worth?',
      inputs: [
        { k: 'quotes', label: 'Quotes you send each month', min: 0, max: 100, step: 1, v: 20, u: 'n' },
        { k: 'quiet', label: 'Quotes that go quiet', min: 0, max: 100, step: 5, v: 50, u: 'pct' },
        { k: 'win', label: 'Quiet quotes you\u2019d win with a follow-up', min: 0, max: 50, step: 1, v: 10, u: 'pct' },
        { k: 'job', label: 'Your average quote value', min: 100, max: 25000, step: 100, v: 2500, u: 'money' }
      ],
      f: function (v) { var jobs = v.quotes * pct(v.quiet) * pct(v.win); var m = jobs * v.job; return { main: m, t: { jobs: count(jobs) } }; },
      sub: 'About {jobs} {jobs|job|jobs} a month, or {year} a year.',
      formula: 'Quotes a month × % that go quiet × % you\u2019d win back × average quote value'
    },
    'website-chat-to-text': {
      title: 'What are the visitors who leave your site worth?',
      inputs: [
        { k: 'visits', label: 'Website visitors each month', min: 0, max: 5000, step: 50, v: 500, u: 'n' },
        { k: 'ask', label: 'Visitors who leave with a question', min: 0, max: 20, step: 1, v: 3, u: 'pct' },
        { k: 'book', label: 'Of those, how many would book', min: 0, max: 100, step: 5, v: 25, u: 'pct' },
        { k: 'job', label: 'Your average job value', min: 50, max: 5000, step: 25, v: 400, u: 'money' }
      ],
      f: function (v) { var jobs = v.visits * pct(v.ask) * pct(v.book); var m = jobs * v.job; return { main: m, t: { jobs: count(jobs) } }; },
      sub: 'About {jobs} {jobs|job|jobs} a month, or {year} a year.',
      formula: 'Visitors a month × % who leave with a question × % who would book × average job value'
    },
    'text-to-pay': {
      title: 'How much of your money is waiting on unpaid invoices?',
      lead: 'About',
      per: '',
      tail: 'is tied up while you wait to get paid.',
      inputs: [
        { k: 'inv', label: 'Invoices you send each month', min: 0, max: 200, step: 1, v: 40, u: 'n' },
        { k: 'amt', label: 'Your average invoice', min: 50, max: 10000, step: 50, v: 600, u: 'money' },
        { k: 'days', label: 'Days until you get paid', min: 1, max: 90, step: 1, v: 21, u: 'days' }
      ],
      f: function (v) { var perDay = v.inv * v.amt / 30; return { main: perDay * v.days, t: { day: money(perDay) } }; },
      sub: 'Every day you wait holds about {day} more.',
      formula: 'Invoices a month × average invoice × days until you get paid ÷ 30 days'
    },
    'contractor-websites': {
      title: 'What are the calls your website is missing worth?',
      inputs: [
        { k: 'visits', label: 'People who visit your site each month', min: 0, max: 5000, step: 50, v: 300, u: 'n' },
        { k: 'call', label: 'Visitors who would call you', min: 0, max: 20, step: 1, v: 5, u: 'pct' },
        { k: 'book', label: 'Callers who book a job', min: 0, max: 100, step: 5, v: 40, u: 'pct' },
        { k: 'job', label: 'Your average job value', min: 50, max: 5000, step: 25, v: 400, u: 'money' }
      ],
      f: function (v) { var jobs = v.visits * pct(v.call) * pct(v.book); var m = jobs * v.job; return { main: m, t: { jobs: count(jobs) } }; },
      sub: 'About {jobs} {jobs|job|jobs} a month, or {year} a year.',
      formula: 'Visitors a month × % who would call × % who book × average job value'
    },
    'lead-follow-up': {
      title: 'What are the leads that go cold worth?',
      inputs: [
        { k: 'leads', label: 'New leads each month', min: 0, max: 300, step: 1, v: 40, u: 'n' },
        { k: 'cold', label: 'Leads that go cold before you reply', min: 0, max: 100, step: 5, v: 30, u: 'pct' },
        { k: 'book', label: 'Of those, how many would book with a fast reply', min: 0, max: 100, step: 5, v: 25, u: 'pct' },
        { k: 'job', label: 'Your average job value', min: 50, max: 5000, step: 25, v: 500, u: 'money' }
      ],
      f: function (v) { var jobs = v.leads * pct(v.cold) * pct(v.book); var m = jobs * v.job; return { main: m, t: { jobs: count(jobs) } }; },
      sub: 'About {jobs} {jobs|job|jobs} a month, or {year} a year.',
      formula: 'Leads a month × % that go cold × % who would book × average job value'
    },
    'appointment-reminders': {
      title: 'What do no-shows cost you?',
      inputs: [
        { k: 'appts', label: 'Appointments each week', min: 0, max: 400, step: 5, v: 80, u: 'n' },
        { k: 'ns', label: 'Clients who don\u2019t show up', min: 0, max: 40, step: 1, v: 8, u: 'pct' },
        { k: 'visit', label: 'Your average visit value', min: 20, max: 500, step: 5, v: 85, u: 'money' }
      ],
      f: function (v) { var n = v.appts * pct(v.ns) * W; var m = n * v.visit; return { main: m, t: { n: count(n) } }; },
      sub: 'About {n} empty {n|appointment|appointments} a month, or {year} a year.',
      formula: 'Appointments a week × % who don\u2019t show × average visit value × 4.3 weeks'
    },
    'cold-outreach': {
      title: 'What could one more commercial client be worth to you?',
      lead: 'About',
      per: '/year',
      tail: 'is at stake.',
      inputs: [
        { k: 'clients', label: 'New commercial clients won', min: 0, max: 10, step: 1, v: 1, u: 'n' },
        { k: 'job', label: 'Your average commercial job value', min: 500, max: 100000, step: 500, v: 6000, u: 'money' },
        { k: 'rep', label: 'Times a year a commercial client books you', min: 1, max: 12, step: 1, v: 2, u: 'n' }
      ],
      f: function (v) { var year = v.clients * v.job * v.rep; return { main: year, t: { one: money(v.job), rep: count(v.rep), year: money(year), clientYear: money(v.job * v.rep) } }; },
      sub: 'One client is worth about {one} per job, or {clientYear} a year at {rep} {rep|booking|bookings}.',
      formula: 'New commercial clients won × average commercial job value × times a year they book you'
    },
    'crm-setup': {
      title: 'What do slipped quotes and lost time cost you?',
      inputs: [
        { k: 'slip', label: 'Quotes or leads that slip through each month', min: 0, max: 20, step: 1, v: 2, u: 'n' },
        { k: 'job', label: 'Your average job value', min: 50, max: 10000, step: 50, v: 800, u: 'money' },
        { k: 'hrs', label: 'Hours a week you spend looking for job details', min: 0, max: 20, step: 0.5, v: 3, u: 'hrs' },
        { k: 'rate', label: 'What an hour of your time is worth', min: 20, max: 300, step: 5, v: 75, u: 'money' }
      ],
      f: function (v) { var a = v.slip * v.job; var b = v.hrs * v.rate * W; return { main: a + b, t: { a: money(a), b: money(b) } }; },
      sub: '{a} in slipped jobs plus {b} of your time.',
      formula: 'Slipped jobs a month × average job value + hours a week × your hourly value × 4.3 weeks'
    },
    'custom-dashboards': {
      title: 'What does pulling your numbers by hand cost you?',
      lead: 'Your time on it is worth',
      tail: '',
      inputs: [
        { k: 'hrs', label: 'Hours a week you spend pulling your numbers', min: 0, max: 20, step: 0.5, v: 3, u: 'hrs' },
        { k: 'rate', label: 'What an hour of your time is worth', min: 20, max: 300, step: 5, v: 75, u: 'money' }
      ],
      f: function (v) { var h = v.hrs * W; var m = h * v.rate; return { main: m, t: { h: count(h) } }; },
      sub: 'About {h} {h|hour|hours} a month, or {year} a year.',
      formula: 'Hours a week × your hourly value × 4.3 weeks'
    },
    'multi-location': {
      title: 'What are missed calls across your locations worth?',
      note: 'An estimate from your numbers only. It shows the value at stake, not what we will recover. Multi-location sets up and reports on your services. It does not answer calls on its own. Nothing you enter is sent.',
      inputs: [
        { k: 'locs', label: 'Locations', min: 2, max: 20, step: 1, v: 3, u: 'n' },
        { k: 'calls', label: 'Missed calls a week at each location', min: 0, max: 30, step: 1, v: 4, u: 'n' },
        { k: 'book', label: 'Missed callers who would have booked', min: 0, max: 100, step: 5, v: 30, u: 'pct' },
        { k: 'job', label: 'Your average job value', min: 50, max: 5000, step: 25, v: 350, u: 'money' }
      ],
      f: function (v) { var jobs = v.locs * v.calls * pct(v.book) * W; var m = jobs * v.job; return { main: m, t: { jobs: count(jobs) } }; },
      sub: 'About {jobs} {jobs|job|jobs} a month across your locations, or {year} a year.',
      formula: 'Locations × missed calls a week × % who would have booked × average job value × 4.3 weeks'
    },
    'ai-support-agent': {
      title: 'What do routine client questions cost your team?',
      lead: 'Your team\u2019s time on them is worth',
      tail: '',
      cta: 'consult',
      inputs: [
        { k: 'q', label: 'Routine client questions each week', min: 0, max: 300, step: 5, v: 40, u: 'n' },
        { k: 'mins', label: 'Minutes each one takes', min: 1, max: 30, step: 1, v: 6, u: 'min' },
        { k: 'rate', label: 'Hourly cost of the person answering', min: 20, max: 300, step: 5, v: 60, u: 'money' }
      ],
      f: function (v) { var h = v.q * v.mins / 60 * W; var m = h * v.rate; return { main: m, t: { h: count(h) } }; },
      sub: 'About {h} staff {h|hour|hours} a month, or {year} a year.',
      formula: 'Questions a week × minutes each ÷ 60 × hourly cost × 4.3 weeks'
    }
  };

  function defaults(id) {
    var v = {};
    CALCS[id].inputs.forEach(function (i) { v[i.k] = i.v; });
    return v;
  }
  function result(id, v) {
    var c = CALCS[id];
    var r = c.f(v);
    var main = Math.max(0, Math.round(Math.round(r.main * 1e6) / 1e6));
    var t = r.t;
    t.year = t.year === undefined ? money(main * 12) : t.year;
    // {k} inserts a token; {k|one|many} picks the word for the token's number.
    var sub = c.sub.replace(/\{(\w+)(?:\|([^|}]*)\|([^}]*))?\}/g, function (_, k, one, many) {
      if (one === undefined) return t[k];
      return t[k] === '1' ? one : many;
    });
    return { main: main, mainText: money(main), sub: sub };
  }
  function clamp(x, i) {
    x = Number(x);
    if (!isFinite(x)) x = i.v;
    return Math.min(i.max, Math.max(i.min, x));
  }

  var api = { CALCS: CALCS, WEEKS: W, money: money, count: count, defaults: defaults, result: result, clamp: clamp };
  if (typeof module === 'object' && module.exports) module.exports = api;
  if (typeof document === 'undefined') return;

  function fill(range, i) {
    var p = (Number(range.value) - i.min) / (i.max - i.min) * 100;
    range.style.setProperty('--p', p + '%');
  }
  function wire(sec) {
    var id = sec.getAttribute('data-calc');
    var c = CALCS[id];
    if (!c) return;
    var out = sec.querySelector('[data-out="main"]');
    var sub = sec.querySelector('[data-out="sub"]');
    var used = false;
    function update() {
      var v = {};
      c.inputs.forEach(function (i) {
        var r = sec.querySelector('input[type="range"][data-k="' + i.k + '"]');
        v[i.k] = clamp(r.value, i);
      });
      var res = result(id, v);
      out.textContent = res.mainText;
      sub.textContent = res.sub;
    }
    c.inputs.forEach(function (i) {
      var r = sec.querySelector('input[type="range"][data-k="' + i.k + '"]');
      var n = sec.querySelector('input[type="number"][data-k="' + i.k + '"]');
      if (!r || !n) return;
      fill(r, i);
      function first() {
        if (used) return;
        used = true;
        root.dataLayer = root.dataLayer || [];
        root.dataLayer.push({ event: 'calculator_interact', calculator_id: id });
      }
      r.addEventListener('input', function () { n.value = r.value; r.setAttribute('aria-valuetext', (n.getAttribute('data-prefix') || '') + n.value + (n.getAttribute('data-suffix') || '')); fill(r, i); update(); first(); });
      n.addEventListener('input', function () {
        if (n.value === '') return;
        r.value = clamp(n.value, i); r.setAttribute('aria-valuetext', (n.getAttribute('data-prefix') || '') + r.value + (n.getAttribute('data-suffix') || '')); fill(r, i); update(); first();
      });
      n.addEventListener('change', function () { n.value = clamp(n.value, i); r.value = n.value; fill(r, i); update(); });
    });
    sec.classList.add('tl-calc-ready');
    update();
  }
  function start() {
    var list = document.querySelectorAll('section.tl-calc-section[data-calc]');
    for (var i = 0; i < list.length; i++) wire(list[i]);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})(typeof window !== 'undefined' ? window : this);
