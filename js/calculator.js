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
  // Discrete counts (jobs, bookings, appointments) show as whole numbers (Ben 2026-11-19 9:35 PM ET).
  // The $ result still uses the unrounded count, as every calculator already did.
  function whole(n) {
    return String(Math.round(Number(n) || 0)).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
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
      f: function (v) { var jobs = v.calls * pct(v.book) * W; var m = jobs * v.job; return { main: m, t: { jobs: whole(jobs) } }; },
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
      f: function (v) { var jobs = v.calls * pct(v.book) * W; var m = jobs * v.job; return { main: m, t: { jobs: whole(jobs) } }; },
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
      f: function (v) { var n = v.calls * pct(v.book) * W; var m = n * v.visit; return { main: m, t: { n: whole(n) } }; },
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
        { k: 'win', label: 'Quiet quotes you\u2019d win back', min: 0, max: 50, step: 1, v: 10, u: 'pct' },
        { k: 'job', label: 'Your average quote value', min: 100, max: 25000, step: 100, v: 2500, u: 'money' }
      ],
      f: function (v) { var jobs = v.quotes * pct(v.quiet) * pct(v.win); var m = jobs * v.job; return { main: m, t: { jobs: whole(jobs) } }; },
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
      f: function (v) { var jobs = v.visits * pct(v.ask) * pct(v.book); var m = jobs * v.job; return { main: m, t: { jobs: whole(jobs) } }; },
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
      f: function (v) { var jobs = v.visits * pct(v.call) * pct(v.book); var m = jobs * v.job; return { main: m, t: { jobs: whole(jobs) } }; },
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
      f: function (v) { var jobs = v.leads * pct(v.cold) * pct(v.book); var m = jobs * v.job; return { main: m, t: { jobs: whole(jobs) } }; },
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
      f: function (v) { var n = v.appts * pct(v.ns) * W; var m = n * v.visit; return { main: m, t: { n: whole(n) } }; },
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
    },
    'speed-to-lead': {
      title: 'What are the leads you answer too late worth?',
      inputs: [
        { k: 'leads', label: 'New leads each month', min: 0, max: 300, step: 1, v: 30, u: 'n' },
        { k: 'late', label: 'Leads you can\u2019t answer in minutes', min: 0, max: 100, step: 5, v: 40, u: 'pct' },
        { k: 'book', label: 'Of those, how many would book with a fast first reply', min: 0, max: 100, step: 5, v: 25, u: 'pct' },
        { k: 'job', label: 'Your average job or visit value', min: 20, max: 5000, step: 10, v: 450, u: 'money' }
      ],
      f: function (v) { var jobs = v.leads * pct(v.late) * pct(v.book); var m = jobs * v.job; return { main: m, t: { jobs: whole(jobs) } }; },
      sub: 'About {jobs} {jobs|booking|bookings} a month, or {year} a year.',
      formula: 'Leads a month × % you can\u2019t answer in minutes × % who would book × average job or visit value'
    },
    'overdue-invoice-reminders': {
      title: 'How much of your money runs late?',
      lead: 'About',
      tail: 'sits in late invoices.',
      inputs: [
        { k: 'inv', label: 'Invoices you send each month', min: 0, max: 200, step: 1, v: 40, u: 'n' },
        { k: 'late', label: 'Invoices that run past due', min: 0, max: 100, step: 5, v: 20, u: 'pct' },
        { k: 'amt', label: 'Your average invoice', min: 50, max: 10000, step: 50, v: 600, u: 'money' }
      ],
      f: function (v) { var n = v.inv * pct(v.late); return { main: n * v.amt, t: { n: whole(n) } }; },
      sub: 'About {n} late {n|invoice|invoices} a month.',
      formula: 'Invoices a month × % that run past due × average invoice'
    },
    'ai-estimate-drafts': {
      title: 'What does writing quotes by hand cost you?',
      lead: 'Your time on them is worth',
      tail: '',
      inputs: [
        { k: 'q', label: 'Quotes you write each month', min: 0, max: 100, step: 1, v: 20, u: 'n' },
        { k: 'mins', label: 'Minutes each one takes', min: 5, max: 180, step: 5, v: 45, u: 'min' },
        { k: 'rate', label: 'What an hour of your time is worth', min: 20, max: 300, step: 5, v: 75, u: 'money' }
      ],
      f: function (v) { var h = v.q * v.mins / 60; var m = h * v.rate; return { main: m, t: { h: count(h) } }; },
      sub: 'About {h} {h|hour|hours} a month, or {year} a year.',
      formula: 'Quotes a month × minutes each ÷ 60 × your hourly value'
    },
    'ai-sales-agent': {
      title: 'What are the leads you can\u2019t call back worth?',
      inputs: [
        { k: 'leads', label: 'Leads who ask about a job each month', min: 0, max: 300, step: 1, v: 30, u: 'n' },
        { k: 'miss', label: 'Leads you don\u2019t reach in time', min: 0, max: 100, step: 5, v: 30, u: 'pct' },
        { k: 'book', label: 'Of those, how many would book', min: 0, max: 100, step: 5, v: 25, u: 'pct' },
        { k: 'job', label: 'Your average job value', min: 50, max: 5000, step: 25, v: 500, u: 'money' }
      ],
      f: function (v) { var jobs = v.leads * pct(v.miss) * pct(v.book); var m = jobs * v.job; return { main: m, t: { jobs: whole(jobs) } }; },
      sub: 'About {jobs} {jobs|job|jobs} a month, or {year} a year.',
      formula: 'Leads a month × % you don\u2019t reach in time × % who would book × average job value'
    },
    'job-scheduling-dispatch': {
      title: 'What does scheduling by phone cost you?',
      lead: 'Your time on it is worth',
      tail: '',
      inputs: [
        { k: 'hrs', label: 'Hours a week you spend scheduling jobs and sending crews', min: 0, max: 30, step: 0.5, v: 6, u: 'hrs' },
        { k: 'rate', label: 'What an hour of your time is worth', min: 20, max: 300, step: 5, v: 75, u: 'money' }
      ],
      f: function (v) { var h = v.hrs * W; var m = h * v.rate; return { main: m, t: { h: count(h) } }; },
      sub: 'About {h} {h|hour|hours} a month, or {year} a year.',
      formula: 'Hours a week × your hourly value × 4.3 weeks'
    },
    'google-business-profile-optimization': {
      title: 'What could more calls from Google Maps be worth?',
      inputs: [
        { k: 'calls', label: 'Extra calls from Google Maps each month', min: 0, max: 40, step: 1, v: 5, u: 'n' },
        { k: 'book', label: 'Callers who book', min: 0, max: 100, step: 5, v: 40, u: 'pct' },
        { k: 'job', label: 'Your average job or visit value', min: 20, max: 5000, step: 10, v: 400, u: 'money' }
      ],
      f: function (v) { var jobs = v.calls * pct(v.book); var m = jobs * v.job; return { main: m, t: { jobs: whole(jobs) } }; },
      sub: 'About {jobs} {jobs|booking|bookings} a month, or {year} a year.',
      formula: 'Extra calls a month × % who book × average job or visit value'
    },
    'google-business-profile-for-professionals': {
      title: 'What could more people reaching out be worth?',
      cta: 'consult',
      inputs: [
        { k: 'asks', label: 'Extra inquiries each month', min: 0, max: 40, step: 1, v: 4, u: 'n' },
        { k: 'win', label: 'Inquiries who become clients', min: 0, max: 100, step: 5, v: 30, u: 'pct' },
        { k: 'val', label: 'Your average value of a new client', min: 100, max: 100000, step: 100, v: 2000, u: 'money' }
      ],
      f: function (v) { var n = v.asks * pct(v.win); var m = n * v.val; return { main: m, t: { n: whole(n) } }; },
      sub: 'About {n} new {n|client|clients} a month, or {year} a year.',
      formula: 'Extra inquiries a month × % who become clients × average value of a new client'
    },
    'document-automation': {
      title: 'What do routine documents cost your team?',
      lead: 'Your team\u2019s time on them is worth',
      tail: '',
      cta: 'consult',
      inputs: [
        { k: 'docs', label: 'Documents your team drafts each month', min: 0, max: 300, step: 5, v: 30, u: 'n' },
        { k: 'mins', label: 'Minutes each one takes', min: 5, max: 240, step: 5, v: 40, u: 'min' },
        { k: 'rate', label: 'Hourly cost of the person drafting', min: 20, max: 300, step: 5, v: 60, u: 'money' }
      ],
      f: function (v) { var h = v.docs * v.mins / 60; var m = h * v.rate; return { main: m, t: { h: count(h) } }; },
      sub: 'About {h} staff {h|hour|hours} a month, or {year} a year.',
      formula: 'Documents a month × minutes each ÷ 60 × hourly cost'
    },
    'inbox-management': {
      title: 'What does sorting your inbox cost you?',
      lead: 'Your time on it is worth',
      tail: '',
      cta: 'consult',
      inputs: [
        { k: 'hrs', label: 'Hours a week you spend sorting and answering email', min: 0, max: 30, step: 0.5, v: 6, u: 'hrs' },
        { k: 'rate', label: 'What an hour of your time is worth', min: 20, max: 300, step: 5, v: 90, u: 'money' }
      ],
      f: function (v) { var h = v.hrs * W; var m = h * v.rate; return { main: m, t: { h: count(h) } }; },
      sub: 'About {h} {h|hour|hours} a month, or {year} a year.',
      formula: 'Hours a week × your hourly value × 4.3 weeks'
    },
    // 2026-11-26 (Ben t1825u): Property Managers group. Example inputs only; every number is the visitor's own.
    'ai-contract-review-for-property-managers': {
      title: 'What does reading every contract cost you?',
      lead: 'Your time on it is worth',
      tail: '',
      inputs: [
        { k: 'n', label: 'Leases and contracts you read each month', min: 0, max: 100, step: 1, v: 12, u: 'n' },
        { k: 'mins', label: 'Minutes each one takes', min: 5, max: 240, step: 5, v: 45, u: 'min' },
        { k: 'rate', label: 'What an hour of your time is worth', min: 20, max: 300, step: 5, v: 75, u: 'money' }
      ],
      f: function (v) { var h = v.n * v.mins / 60; var m = h * v.rate; return { main: m, t: { h: count(h) } }; },
      sub: 'About {h} {h|hour|hours} a month, or {year} a year.',
      formula: 'Contracts a month × minutes each ÷ 60 × your hourly value'
    },
    'accounts-payable-automation-for-property-managers': {
      title: 'What do vendor invoices cost you in time?',
      lead: 'Your time on them is worth',
      tail: '',
      inputs: [
        { k: 'n', label: 'Vendor invoices you handle each month', min: 0, max: 400, step: 5, v: 60, u: 'n' },
        { k: 'mins', label: 'Minutes each one takes', min: 1, max: 60, step: 1, v: 10, u: 'min' },
        { k: 'rate', label: 'What an hour of your time is worth', min: 20, max: 300, step: 5, v: 60, u: 'money' }
      ],
      f: function (v) { var h = v.n * v.mins / 60; var m = h * v.rate; return { main: m, t: { h: count(h) } }; },
      sub: 'About {h} {h|hour|hours} a month, or {year} a year.',
      formula: 'Invoices a month × minutes each ÷ 60 × your hourly value'
    },
    'ai-sales-agent-for-property-managers': {
      title: 'What could your missed owner leads be worth?',
      lead: 'About',
      per: '',
      tail: 'in first-year fees is at stake each month.',
      inputs: [
        { k: 'leads', label: 'Owner leads you get each month', min: 0, max: 100, step: 1, v: 10, u: 'n' },
        { k: 'miss', label: 'Owner leads you don’t reach in time', min: 0, max: 100, step: 5, v: 30, u: 'pct' },
        { k: 'sign', label: 'Share of owner leads you would sign', min: 0, max: 100, step: 5, v: 20, u: 'pct' },
        { k: 'fees', label: 'Your first-year fees from one owner', min: 100, max: 50000, step: 100, v: 3000, u: 'money' }
      ],
      f: function (v) { var o = v.leads * pct(v.miss) * pct(v.sign); var m = o * v.fees; return { main: m, t: { n: whole(o) } }; },
      sub: 'About {n} {n|owner|owners} a month, or {year} a year.',
      formula: 'Owner leads a month × % you don’t reach in time × % who would sign × first-year fees from one owner'
    },
    'job-scheduling-dispatch-for-property-managers': {
      title: 'What does scheduling by phone cost you?',
      lead: 'Your time on it is worth',
      tail: '',
      inputs: [
        { k: 'hrs', label: 'Hours a week you spend scheduling maintenance jobs and sending vendors', min: 0, max: 30, step: 0.5, v: 6, u: 'hrs' },
        { k: 'rate', label: 'What an hour of your time is worth', min: 20, max: 300, step: 5, v: 75, u: 'money' }
      ],
      f: function (v) { var h = v.hrs * W; var m = h * v.rate; return { main: m, t: { h: count(h) } }; },
      sub: 'About {h} {h|hour|hours} a month, or {year} a year.',
      formula: 'Hours a week × your hourly value × 4.3 weeks'
    },
    'ai-concierge-for-property-managers': {
      title: 'What do resident questions cost your team?',
      lead: 'Your team’s time on them is worth',
      tail: '',
      inputs: [
        { k: 'q', label: 'Resident questions and requests your team handles each week', min: 0, max: 400, step: 5, v: 60, u: 'n' },
        { k: 'mins', label: 'Minutes each one takes', min: 1, max: 60, step: 1, v: 5, u: 'min' },
        { k: 'rate', label: 'What an hour of your team’s time is worth', min: 20, max: 300, step: 5, v: 50, u: 'money' }
      ],
      f: function (v) { var h = v.q * v.mins / 60 * W; var m = h * v.rate; return { main: m, t: { h: count(h) } }; },
      sub: 'About {h} {h|hour|hours} a month, or {year} a year.',
      formula: 'Questions a week × minutes each ÷ 60 × your hourly value × 4.3 weeks'
    },
    'google-business-profile-for-property-managers': {
      title: 'What could more calls from Google Maps be worth?',
      inputs: [
        { k: 'calls', label: 'Extra calls from Google Maps each month', min: 0, max: 40, step: 1, v: 5, u: 'n' },
        { k: 'win', label: 'Callers who become a client', min: 0, max: 100, step: 5, v: 30, u: 'pct' },
        { k: 'fees', label: 'Your first-year fees from one new client', min: 100, max: 20000, step: 50, v: 1500, u: 'money' }
      ],
      f: function (v) { var c = v.calls * pct(v.win); var m = c * v.fees; return { main: m, t: { n: whole(c) } }; },
      sub: 'About {n} new {n|client|clients} a month, or {year} a year.',
      formula: 'Extra calls a month × % who become a client × first-year fees from one client'
    },
    'speed-to-lead-for-property-managers': {
      title: 'What do slow replies cost you?',
      inputs: [
        { k: 'leads', label: 'Rental inquiries and owner leads each month', min: 0, max: 300, step: 5, v: 40, u: 'n' },
        { k: 'late', label: 'Leads you can’t answer in minutes', min: 0, max: 100, step: 5, v: 40, u: 'pct' },
        { k: 'win', label: 'Leads who would sign a lease or sign with you', min: 0, max: 100, step: 5, v: 20, u: 'pct' },
        { k: 'val', label: 'Your average value of one new lease or owner', min: 100, max: 20000, step: 100, v: 1800, u: 'money' }
      ],
      f: function (v) { var n = v.leads * pct(v.late) * pct(v.win); var m = n * v.val; return { main: m, t: { n: whole(n) } }; },
      sub: 'About {n} new {n|lease or owner|leases or owners} a month, or {year} a year.',
      formula: 'Leads a month × % you can’t answer in minutes × % who would sign × average value of one new lease or owner'
    },
    'appointment-reminders-for-property-managers': {
      title: 'What do missed showings cost you?',
      inputs: [
        { k: 'n', label: 'Showings and appointments each month', min: 0, max: 300, step: 5, v: 40, u: 'n' },
        { k: 'ns', label: 'People who don’t show up', min: 0, max: 60, step: 1, v: 20, u: 'pct' },
        { k: 'days', label: 'Extra days a unit sits empty after a missed showing', min: 0, max: 30, step: 1, v: 3, u: 'days' },
        { k: 'rent', label: 'Rent for one unit for one day', min: 10, max: 500, step: 5, v: 50, u: 'money' }
      ],
      f: function (v) { var n = v.n * pct(v.ns); var m = n * v.days * v.rent; return { main: m, t: { n: whole(n) } }; },
      sub: 'About {n} missed {n|showing|showings} a month, or {year} a year.',
      formula: 'Showings a month × % who don’t show × extra days empty × rent for one unit for one day'
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

  var api = { CALCS: CALCS, WEEKS: W, money: money, count: count, whole: whole, defaults: defaults, result: result, clamp: clamp };
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
  // 2026-11-19: at phone widths the sticky call bar covered the calculator small print.
  // While the result panel (with its own call button) is on screen, hide the sticky bar.
  function watchSticky(list) {
    if (!root.IntersectionObserver || !document.documentElement.classList) return;
    var seen = 0;
    var io = new root.IntersectionObserver(function (entries) {
      entries.forEach(function (e) { seen += e.isIntersecting ? 1 : (e.target._tlSeen ? -1 : 0); e.target._tlSeen = e.isIntersecting; });
      if (seen < 0) seen = 0;
      document.documentElement.classList.toggle('tl-calc-visible', seen > 0);
    }, { threshold: 0 });
    for (var i = 0; i < list.length; i++) {
      var r = list[i].querySelector('.tl-calc-result');
      if (r) io.observe(r);
    }
  }
  function start() {
    var list = document.querySelectorAll('section.tl-calc-section[data-calc]');
    for (var i = 0; i < list.length; i++) wire(list[i]);
    watchSticky(list);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})(typeof window !== 'undefined' ? window : this);
