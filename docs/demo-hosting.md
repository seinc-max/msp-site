# Demo hosting

Demos are staging only. Never production. Prospects use the staging URL. A paying client's real site goes on that client's own domain, never on this one.

`noindex` and leaving a URL out of the sitemap are discovery hygiene. They are not the release gate, and they are not authentication or a privacy guarantee.

## Release guard

Cloudflare runs `node scripts/build-dist.js` and sets `CF_PAGES_BRANCH` to the branch it is deploying. `main` is production.

If that branch is `main` and `demo/` contains any file, the build fails before it copies the site. It also deletes `dist/`, so a main deploy cannot keep demo artifacts.

Do not merge `demo/` into `main`. A staging-to-main merge that still contains `demo/` fails the production Pages build.

A local build that does not set `CF_PAGES_BRANCH` still copies `demo/`, so staging work can be checked on a machine. That local copy is not a production deploy.

## Addresses

| Public URL | File |
| --- | --- |
| `/demo/` | `demo/index.html` |
| `/demo/<client-slug>/` | `demo/<client-slug>/index.html` |
| `/demo/<client-slug>/<project-type>/` | `demo/<client-slug>/<project-type>/index.html` |

There is no extra demonstration-name folder. The project type is the last public segment. One folder under the client holds one demo project.

Reserved now:

- `/demo/` is an empty state and does not list clients.
- `/demo/nicky-billou/` is an empty state. `nicky-billou` is the folder id, not the business name on the demo site. The page does not list project types.
- `/demo/nicky-billou/website/` is an empty scaffold. The visible sample name is Sample Workshop, marked DEMO. It is not a real business, and it is not a finished website.

Someone who knows a project address can open it.

## Where a future project goes

Create `demo/<client-slug>/<project-type>/index.html`. Put every artifact for that project inside that same directory: other HTML, styles, assets, and subfolders. Link them with relative URLs. Do not use a root marketing path, Trueline templates, `assets/site.css`, or `assets/landing.css`. The hosting parent pages may use `demo/demo.css`. A client website does not.

`node scripts/build-dist.js` copies the whole `demo/` tree into `dist/` except when `CF_PAGES_BRANCH` is `main`. Do not add demo files to `scripts/dist-manifest.txt`.

Do not add the project to `sitemap.xml`, the site nav, or `templates/`. Do not give it a marketing header, offer, guarantee, form, or call button. This document does not set a price. Do not change marketing prices from it.

## What a finished demo is

A finished demo is a whole sample website for a prospect: home, services, work or gallery, reviews, about, and contact. It is the prospect's sample site, not a Trueline sales page.

Clone an already-live website in the client's industry. Muse finds that site with the four LLMs and gives you the URL. Do not clone a Trueline page. Do not invent the reference URL, and do not install a site builder.

No already-live industry URL was supplied, so nothing here is that clone. The reserved website folder is only an empty scaffold.

Use a sample business name, marked DEMO. Never use a real business name. Do not invent testimonials or statistics. If there are no genuine approved reviews, the reviews page stays an empty demo state. Write in plain English, to the reader.

## Slug rules

A client slug and a project-type slug are the same shape: lowercase letters, digits, and single hyphens. The pattern is `^[a-z0-9]+(?:-[a-z0-9]+)*$`.

- `nicky-billou` is a valid client slug. `website` is a valid project type.
- `Sample_Demo`, `Nicky`, `client name`, and `demo--one` are not.
- The folder name is the public slug. Do not put a person's contact details, credentials, or private files in the folder name or in the page.

## Page requirements

Every HTML file under `demo/` includes `<meta name="robots" content="noindex, nofollow">` and a viewport tag. It does not load the marketing tag manager or Clarity.

Parent routes load their `index.html`. A folder without `index.html` is not a working route. Use the trailing-slash address (`/demo/nicky-billou/website/`) so relative links and assets resolve inside that folder.

## Audience

These pages are outside the offer-to-audience map. They are not trades, salons, or professional offer pages, and they do not add those offers to the menu.
