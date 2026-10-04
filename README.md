# Alex Mercer — Multi-page Creative Portfolio
Original fictional designer portfolio inspired by the user-supplied jjettas.com recording.

## Run locally
Serve `dist` using `python3 -m http.server 8080 --directory dist` and open http://localhost:8080. No npm dependencies or bundler required.

## Pages
- `/`: cinematic homepage
- `/work/`: filterable project archive
- `/work/sonor/`, `/work/vanta-form/`, `/work/other-realities/`, `/work/form-digital/`: individual case studies
- `/about/`: designer biography and principles
- `/practice/`: disciplines and creative process
- `/journal/`: Field Notes index
- `/journal/finding-form/`, `/journal/different-reality/`: articles
- `/contact/`: locally downloadable project brief, with no email submission

## Edit
`build-pages.py` generates all HTML from the homepage template in `content/home.html`, project data in `content/projects.json`, and page copy in the generator. Run `python3 build-pages.py` after changing those sources. CSS and browser behaviour are edited directly in `dist/style.css` and `dist/app.js`. `content/practices.js` records the starting discipline copy; runtime copy is in app.js.

Replace the fictional identity, original AI-generated imagery, example case studies and contact placeholder before launching for a real designer. No real client claims or external message delivery are implied. The contact form downloads a text brief on the visitor's device; it does not transmit or persist form data.

The homepage retains desktop scroll-linked projects, portrait parallax and an interactive image stack. Every project has a real link and direct URL. Mobile has a compact project layout. Motion respects reduced-motion preferences. Fonts use Google Fonts with system fallbacks.

Deploy the `dist` directory to a static host supporting directory index files. The `.openai/hosting.json` belongs to this specific Site and should not be reused for another installation.

## Project galleries
Each case study contains five distinct work images, including its cover. Gallery source, alt text, captions and portrait/landscape layout are defined in `content/projects.json`. Images retain their natural proportions, with paired portraits and full-width landscapes on desktop and a single column on small phones. Each case study has a Back to projects button at the top and after the gallery. FORM / DIGITAL images are AI-generated interface concept mockups, not screenshots of a shipped website.
