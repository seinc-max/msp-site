# Demo hosting

Public client demonstrations live under `/demo/` on the static site. This namespace is not a marketing page, a client directory, or an access control system.

## Addresses

| Public URL | File |
| --- | --- |
| `/demo/` | `demo/index.html` |
| `/demo/<client-slug>/` | `demo/<client-slug>/index.html` |
| `/demo/<client-slug>/<demo-slug>/` | `demo/<client-slug>/<demo-slug>/index.html` |

Reserved now: `/demo/` and `/demo/nicky-billou/`. Both are empty states. No demonstration slug has been supplied, so nothing is published under `demo/nicky-billou/` except that empty state.

`/demo/` does not list clients. `/demo/nicky-billou/` does not list demonstrations. Someone who knows a demonstration address can open it. `noindex` is discovery hygiene, not a lock.

## Where a future demonstration goes

Create `demo/<client-slug>/<demo-slug>/index.html`. Put that demonstration's files beside it, or in a folder inside it, and link them with relative URLs (`assets/board.png`, not a root `/assets/` marketing path).

`node scripts/build-dist.js` copies the whole `demo/` tree into `dist/`. Do not add those files to `scripts/dist-manifest.txt`. Marketing pages stay on the manifest. A new demonstration directory is included because it is under `demo/`.

Do not add the demonstration to `sitemap.xml`, the site nav, or `templates/`. Do not give it a marketing header, offer, price, guarantee, form, or call button.

## Slug rules

A client slug and a demonstration slug are the same shape: lowercase letters, digits, and single hyphens. The pattern is `^[a-z0-9]+(?:-[a-z0-9]+)*$`.

- `nicky-billou` is a valid client slug.
- `Sample_Demo`, `Nicky`, `client name`, and `demo--one` are not.
- One client, one folder. One demonstration, one folder under that client.
- The folder name is the public slug. Do not put a person's contact details, credentials, or private files in the folder name or in the page.

## Page requirements

Every HTML file under `demo/` includes `<meta name="robots" content="noindex, nofollow">` and a viewport tag. It does not load the marketing tag manager, Clarity, `assets/site.css`, or `assets/landing.css`. Shared hosting styles, if needed, are `demo/demo.css`, linked relatively.

Parent routes load their `index.html`. A folder without `index.html` is not a working route. Use the trailing-slash address (`/demo/nicky-billou/`) so relative links and assets resolve inside that folder.

## Audience

These pages are outside the offer-to-audience map. They are not trades, salons, or professional offer pages, and they do not add those offers to the menu.
