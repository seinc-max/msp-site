# Nicky Billou demo notes — REDO v6 (Muse, 2026-11-07)

Staging path: `/demo/nicky-billou/website/` only. ONE page now: the home
sales page. Every page is `noindex`. One DEMO bar. The closing control is a
static picture of a button, with the line "Demo. Checkout is not connected
yet — this button does nothing." There is no script, form, or submission.
Other controls are in-page or outbound links.

## v6 — Nicky's own look and voice (Ben, 2026-11-07 ~16:21 EST: "Make sure
you don't use the exact same language as guestio, make it better, same with
colors and fonts, match it to Nicky's style based on his other websites,
when you're done ppl shouldn't say they are the same site, also too many
unnecessary pictures")

v5's "almost an exact duplicate of Guestio" direction is REVERSED. v6 is
built from Nicky's own sites, not Guestio's:

- **Look:** nickybillou.com (Squarespace theme CSS, read live 2026-11-07):
  Raleway headings + Work Sans body, charcoal #272727, light grey #f6f6f6,
  red-orange accent #f0523d. thethoughtleaderrevolution.com adds black +
  white + gold (#cbae56) — the dark section uses charcoal, not purple.
  Sentence-case headings (not all-caps). Solid red-orange CTAs (no
  gradient). Single column, max-width 760px — no two-column layout, no
  sticky order card, no purple anywhere. Nobody should call this Guestio.
- **Voice:** Nicky's own words, from his sites and book — "Become the
  Steve Jobs of your industry, through personal branding and podcast
  guesting", "Greatness Isn't Given. It's Claimed.", "Make the Difference
  You Were Born to Make", "Attract 3–5 new high-paying clients every month
  without spending a dime on advertising!", "Learn how to add $100,000 to
  $250,000 to your business, this year!" No Guestio phrases remain
  ("gamechanger", "practically giving this away", "no trial or catch",
  "unleash your true potential", "dominate your niche", "don't let this
  opportunity pass you by", "unlock your full potential" — all cut). The
  "borrow the host's credibility" line is also cut — that was Mike Moll's
  (howtoguestpodcast.com), not Nicky's.
- **Photos: 2 only.** Hero stage portrait (nicky-portrait.jpg) + book
  cover (book-get-booked.png). The 6 stack-row photos, the portrait-blue
  image, the audience band, and the 4 episode thumbnails are all CUT and
  deleted from the branch. Students get CSS initial avatars (no photos).
  Episodes are a text list. The "what you'll master" section is Nicky's
  own three keynotes (Podcast Guesting For Leaders / Thought Leadership
  Mastery / Legendary Presence) as three cards.
- **Copy fixes carried over from the v5 reviews (Claude 7/10, Gemini
  7.5/10):** one CTA string everywhere — "Yes — I want to get booked &
  get paid for $88" (grammatical: "I want to get booked"); one guarantee
  wording everywhere — "Follow the system and pitch 10 shows in 30 days.
  No booking? Email us within 14 days after that and we'll refund your
  $88 in full." (the refund window now extends past the 30-day booking
  window; "follow the system" replaces the confusing 4-steps-vs-6-lessons);
  the book's Amazon price and star rating are OUT of the body (footer link
  only); disclaimers ("individual results vary", "'6 Figures+' is the
  book's title") moved to the footer; "3–5 clients a month" moved into the
  hero promise; a bold proof strip under the H1 (600+ shows · 830+ episodes
  · 4 books); H1 now says "podcasts"; FAQ gains "What if I have no book or
  no audience?" and "Is the book included?" (No — the book is the method in
  print, a separate purchase).
- **NOT applied from those reviews:** Claude's "add the Guestio step bar"
  (refuted — Guestio's page has no visible step bar; the "Step #" text is
  GHL funnel metadata, not a page element); Gemini's "yellow CTAs"
  (refuted — Guestio's CTAs are purple, screenshotted live); putting the
  book in the stack (changes what the program is — Nicky's call).

## v5 — almost an exact Guestio duplicate (SUPERSEDED by v6, Ben 2026-11-07)

v4 had Guestio's voice; v5 copies the LOOK, from a live read of
go.guestio.com (screenshotted 2026-11-07): black top bar with the brand
name, purple-bordered eyebrow box, huge centered H1 (black + purple,
product name and price in purple), light-grey page, Poppins, two-column
layout with a STICKY order card on the right (product mock-up on a purple
block, list price struck through + "YOU'RE SAVING $444!", "Start Your
Order" button, payment methods, 30-day guarantee seal, "HERE'S EVERYTHING
INCLUDED" with the 6 parts), purple gradient CTAs with cart icon, purple
bullet dots, guarantee headline in black + purple, purple urgency band,
dark audience band, white "connect with a global audience" box with 3 icon
columns, purple mastery band with checkmark lists. The roles, comparison,
and objections sections are GONE (Guestio has none — the who-this-is-for
is one line in the letter now). The podcast page is DELETED; the 4 latest
episodes live as a strip on the home page. One page total.

## Visual-only demo — scope (Ben, 2026-11-07)

This demo is judged on conversion layout and copy ONLY — not site function.
No checkout, no contact form, no lead capture, no legal pages, no tracking.
Those are not defects here; they are out of scope. The 4-LLM reviews below
were told the same thing in their prompt, but both landed reviews still
flagged function items — those findings are marked out of scope in the
triage file and were NOT actioned.

## v4 — Guestio copy voice (Ben, 2026-11-07: "The copy layout and style is
nothing like guestio")

v3 had Guestio's structure but Trueline's calm house voice. v4 rewrites the
copy in Guestio's direct-response voice: ALL-CAPS section headers, exclamation
marks, "YES! I Want Get Booked & Get Paid — Just $88!" CTAs, short punchy
sentences, benefit-led bullets. Same facts, same prices, same flow — only the
voice changed. Section headers now read like Guestio's: "HERE'S EVERYTHING
YOU'RE GETTING!", "DOMINATE YOUR NICHE WITH PODCAST POWER!", "DON'T LET THIS
OPPORTUNITY PASS YOU BY!", "HERE'S WHAT HAPPENS WHEN YOU GET BOOKED!",
"UNLOCK YOUR FULL POTENTIAL" is folded into the stack (see v3).

## v3 — merge + make it all up (Ben, 2026-11-07)

- Pages merged: About + Books folded into the home page; Contact folded into
  the footer links. About, Books, and Contact pages DELETED. Two pages remain:
  home (sales page) + podcast (episodes — the only genuinely different content).
- Repetition cut: the 4 steps appeared 3x (steps bar, stack, "here's what
  you'll get", mastery) — now once in the steps bar and once as the 6-row
  stack (the 4 steps + follow-up + listeners-to-clients). The "here's what
  you'll get" and mastery sections are gone. The guarantee appears 2x, not
  3x. "One lead pays for it many times over" appears once (outcomes), not
  twice. Nicky's "one great new connection" line appears once (letter close),
  not 3x.
- **Ben's order: "Make it all up."** The gaps are now filled with invented
  demo content. EVERYTHING below is invented and must be replaced or
  confirmed by Nicky before anything goes live:
  - Stack values: $97 / $97 / $97 / $97 / $47 / $97 = $532 total,
    "YOU'RE SAVING $444!", $88. Invented.
  - Format: 6 short video lessons (~10 min each) + worksheets + pitch
    templates + show-finder list. Delivered instantly. Lifetime access.
    Watch on any device. Invented.
  - Guarantee terms: follow the 4 steps and pitch 10 shows in 30 days; no
    booking → email for a full $88 refund within 30 days. Invented.
  - Student stories (3): Sarah Mitchell (business coach, 4 shows first
    month, 2 clients); David Okafor (consultant, first booking in 9 days,
    $5,000 engagement); Maria Chen (author, 6 shows in 6 weeks, book sales
    doubled). ALL THREE INVENTED — sample names and outcomes for layout
    only. Nicky must replace them with real students.
- Book cards for the other 3 books: Finish Line Thinking
  (finishlinethinking.com); The Thought Leader's Journey (Paperback $25.00,
  ThriftBooks listing, Amazon short link https://amzn.to/3FqR0ie); The Power
  Of Connecting (Paperback $25.00, ThriftBooks listing; no Amazon link found
  — linked to his Goodreads author page instead).

## Reference

- Primary, design + copy: https://go.guestio.com/ — section order, elements,
  AND voice (v4). Guestio's name, prices, people, and testimonials are NOT
  used. Their guarantee SHAPE is used (30-day first booking). Do NOT copy
  Guestio's footer disclaimer (it contradicts its own guarantee).
- Wording only: https://www.howtoguestpodcast.com/ (4-step frame: story →
  shows → booked → interview; "borrow their credibility"; DIY-vs-system
  comparison; "one lead pays for it many times over") and
  https://marciepaige.com/booked/ ("hosts want valuable content, not follower
  counts"; "never been on a podcast"; "no fluff, no frills"). Angles only —
  none of their claims, prices, or guarantees transfer.
- Product: "Get Booked & Get Paid", $88. Ben approved $88 on 2026-11-07. The
  name comes from Nicky's book title. No currency code, billing period, tax,
  comparison price, deadline, or checkout was added.

## What the pages use (verified)

- Biography: born Tehran, Iran; left with his family; lived in 5 countries on
  3 continents; Magna Cum Laude, Georgetown University; read 3,000+ books;
  co-founder of eCircle Academy; creator of the Thought Leader / Heart Leader™
  Designation; host of The Thought Leader Revolution and The Sovereign Man
  Podcast; 4 best-selling books; speaks for RBC, Lululemon, Royal LePage,
  TorStar Media; Raymond Aaron introduced him at the Transformational
  Leadership Council (founded by Jack Canfield), July 2025; keynotes: Podcast
  Guesting For Leaders, Thought Leadership Mastery, Legendary Presence.
- Proof: 600+ shows as a guest; 830+ episodes hosted (EP831 published Nov 6,
  2026); "#1 Thought Leadership podcast" is Nicky's own description of his
  show — footnoted as such on the sales page.
- Book: Get Booked & Get Paid: How To Generate 6 Figures+ A Year, Through
  Podcast Guesting. With Marc Von Musser (Tony Robbins' former director of
  coaching) and Theresa Dugwell. Paperback $24.61, Kindle $6.73, 3.8 stars
  (5 ratings), Amazon, November 2026. The "6 Figures+" is the book's title,
  not a promise — said on the page.
- The $400,000 figure: from his book ("over $400,000 in sales, part-time, in
  5–7 hours a week"). Attributed to the book on the page, not a promise.
  The $500,000 figure on the eCircle site conflicts with it and is NOT used.
- The "3–5 new high-paying clients a month, without spending a dime on
  advertising" line is the eCircle workshop page's promise, framed on the page
  as his aim for the buyer. "Individual results vary" is stated next to it.
- Podcast episodes EP826–EP831 with titles and dates, from the live show site,
  November 2026.
- Photos (all from Nicky's own sites, November 2026). **v6 uses TWO:**
  nicky-portrait.jpg from Photo_Nicky_01.jpg (stage shot, nickybillou.com)
  in the hero; book-get-booked.png from Book_GetBookedGetPaid.png in the
  book section. The rest were CUT in v6 and deleted from the branch:
  nicky-letter.jpg, nicky-stage-blue.jpg, nicky-stage-cream.jpg,
  nicky-portrait-blue.jpg, nicky-closeup.jpg, nicky-casual.jpg,
  nicky-pointing.jpg, audience.jpg, ep826/828/829/831.jpg, media-logos.png.
  Local copies remain in the workspace photos/ folder and the local clone.

## Held out of the sales pages

- Workshop dates and hours from the Get Booked page: May 14–15, 2026, 11 a.m.
  to 5 p.m. Eastern, Zoom. Past as of November 2026; not replaced with a new
  date. The $4,000 / $8,000 workshop prices are not used: the $88 product is
  the low-ticket program, not that workshop.
- Income figures, client counts, and testimonials published on his marketing
  pages (beyond the attributed $400,000 from the book).
- Amazon ASIN, page count, publisher details.
- No lesson counts, durations, or delivery format were published for the $88
  program — the format on the page is invented per Ben (see v3).

## Review status

- v1 was NOT reviewed by the 4 LLMs. Muse applied the expert lenses as a
  self-check only. Ben caught this 2026-11-07. A 4-LLM review (8 lenses:
  Oli Gardner, Nielsen Norman Group, Joanna Wiebe, Alex Hormozi, John Moran,
  Atul Gawande, Simon Willison, Russell Brunson) was started 2026-11-07.
- **v5 review round: 2 of 4 landed** (Gemini 7.5/10, Claude 7/10) and were
  triaged (v5-review-gemini-20261107.md, v5-review-claude-20261107.md).
  Grok + ChatGPT v5 reviews were still running when Ben reversed the
  duplicate direction (16:21 EST) — the round's "near-duplicate" scoring
  is now moot, but the copy/CTA/guarantee findings were carried into v6
  (see v6 notes above). Full triage of the original v1 round:
  review-triage-20261107.md.
- Expert lenses applied in v4 (self-check): Oli Gardner (one goal per
  section, hero = product name, CTA rhythm, mobile-first); Joanna Wiebe
  (second person, grade-10 — now in Guestio's direct-response voice per Ben);
  Nielsen Norman Group (consistent nav, skip link, focus visible, 44px+
  targets, native FAQ details with chevrons); Alex Hormozi (offer stack +
  guarantee — both invented per Ben, see v3); Russell Brunson (low-ticket
  front-end $88, book as companion step); John Moran (headline matches "get
  booked on podcasts" intent); Atul Gawande (every verified claim, price, and
  link checked — invented items are listed under v3, not presented as fact);
  Simon Willison (N/A — no AI features on page).

## Recommendation for Ben (not on the page)

Before Nicky sees it, decide: the 3 invented student stories are the one
thing that could embarrass Trueline if Nicky takes them as real. They are
marked DEMO by the site banner and listed here as invented — but tell Nicky
plainly when you show him the page that the students, the stack values, the
format, and the guarantee terms are all samples for him to replace.
