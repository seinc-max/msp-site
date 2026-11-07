# Demo hosting

Public client projects live under `/demo/` on the static site. This namespace is not a marketing page, a client directory, or an access control system. `noindex` only asks crawlers not to list the pages. It is not authentication or a privacy guarantee.

## Addresses

| Public URL | File |
| --- | --- |
| `/demo/` | `demo/index.html` |
| `/demo/<client-slug>/` | `demo/<client-slug>/index.html` |
| `/demo/<client-slug>/<project-type>/` | `demo/<client-slug>/<project-type>/index.html` |

There is no extra demonstration-name folder. The project type is the last public segment.

Reserved now:

- `/demo/` is an empty state and does not list clients.
- `/demo/nicky-billou/` is an empty state and does not list project types.
- `/demo/nicky-billou/website/` is an empty state. No website files were supplied, so that folder has only its own index and stylesheet.

Someone who knows a project address can open it.

## Where a future project goes

Create `demo/<client-slug>/<project-type>/index.html`. Put every artifact for that project inside that same directory: other HTML, assets, and subfolders. Link them with relative URLs (`assets/board.png`, not a root `/assets/` marketing path, and not a file outside the project directory).

`node scripts/build-dist.js` already copies the whole `demo/` tree into `dist/`. Do not add those files to `scripts/dist-manifest.txt`. Marketing pages stay on the manifest.

Do not add the project to `sitemap.xml`, the site nav, or `templates/`. Do not give it a marketing header, offer, price, guarantee, form, or call button.

## Slug rules

A client slug and a project-type slug are the same shape: lowercase letters, digits, and single hyphens. The pattern is `^[a-z0-9]+(?:-[a-z0-9]+)*$`.

- `nicky-billou` is a valid client slug. `website` is a valid project type.
- `Sample_Demo`, `Nicky`, `client name`, and `demo--one` are not.
- One client, one folder. One project type, one folder under that client.
- The folder name is the public slug. Do not put a person's contact details, credentials, or private files in the folder name or in the page.

## Page requirements

Every HTML file under `demo/` includes `<meta name="robots" content="noindex, nofollow">` and a viewport tag. It does not load the marketing tag manager, Clarity, `assets/site.css`, or `assets/landing.css`.

`demo/demo.css` is only for the hosting parent pages. A project page uses styles and assets that live in its own project-type directory.

Parent routes load their `index.html`. A folder without `index.html` is not a working route. Use the trailing-slash address (`/demo/nicky-billou/website/`) so relative links and assets resolve inside that folder.

## Audience

These pages are outside the offer-to-audience map. They are not trades, salons, or professional offer pages, and they do not add those offers to the menu.
