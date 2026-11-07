# Nicky Billou demo notes

Staging path: `/demo/nicky-billou/website/`. This is a demo. It is not a checkout.

## Reference

Structure follows https://go.guestio.com/ only: one long offer page, a single next step, stacked sections, a dark hero, a light detail area, and questions near the close. Guestio’s name, prices, guarantee, people, and testimonials are not used. This job does not use the older six-page trade outline.

## Sources

| Source | Used |
| --- | --- |
| https://www.nickybillou.com/ and /about | Bio lines, stage photo, book cover. Treated as his published bio, not a second-source check. |
| http://www.ecircleacademy.com/getbooked | Workshop name, May 14–15, 2026, 11 a.m.–5 p.m. Eastern, Zoom. Income lines on that page were not copied. |
| https://www.ecircleacademy.com/ | Audience list (coaches, consultants, authors, speakers, trainers). Published client quotes were not copied. |
| https://www.thethoughtleaderrevolution.com/ | Recent episode number EP831 was visible on the home page on November 7, 2026. |
| https://a.co/d/9h1Hgt6 | Kindle title, authors, Thought Leader Books, August 29, 2024, 90 pages, ASIN B0DFQL291X. |
| https://finishlinethinking.com/ | Opened. No extra biography was clear enough to use. |

Images:

- `assets/images/nicky-portrait.jpg` from `Photo_Nicky_01.jpg` on nickybillou.com. Saved as JPEG.
- `assets/images/book-get-booked.png` from `Book_GetBookedGetPaid.png` on nickybillou.com/about.

## Omitted on purpose

Price, money-back guarantee, income totals, client counts, and testimonials. The demo button does not submit, store, or show a fake success. No analytics.

## Criteria pass

- One goal: show the public podcast-guesting offer and one next step.
- Mobile nav wraps, targets are at least 44px, the demo button states that nothing was sent.
- Copy speaks to “you” and names podcast guesting, not a vague success plan.
- No commercial terms were added beyond the dates and format his page states.
- No ad tracking. The workshop link matches the page the dates came from.
- Checklist: noindex on both pages, relative CSS and images, no Trueline stylesheet, sources named, demo disclosure in the header.
- Page text is static. The button does not call a network.
- Hook, short bio, offer, then one next step. No upsell pages.
- Ads and AI features: not applicable.

## Checks

`node scripts/check-textback-copy.js`, `node scripts/build-pages.js --check`, and `node scripts/check-pages.js` were run for the rest of the site. This folder is outside those marketing checks.
