# DataEnvGym Spotlight Serif — Style Reference

> A Merriweather broadsheet with one gold award ribbon pinned under the masthead.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide screenshots, the page's inline `<style>` block and inline attributes, and Bulma 0.9.4 from jsDelivr. Bulma supplies colors and spacing that the page does not override. Color share is measured on the first 1440×900 viewport.

## Overview

A Nerfies-derived Bulma page re-typeset in two Google families: Merriweather (serif) for title, headings, body and button labels, and DM Sans for the author lines, navbar, venue pill and footer. The hero is centred: a 40px bold two-line serif title in #363636, a gold gradient pill reading "⭐ ICLR 2025 Spotlight ⭐", blue DM Sans author links, a grey affiliation, and a row of six dark #363636 pill buttons (arXiv, Code, Leaderboard, HuggingFace, BibTeX, Thread). The teaser is a large flat diagram (grey panels with yellow, green, blue and orange boxes) at 864px, captioned by a 20px left-aligned serif paragraph with bold key terms. The body runs in a 900px column: a justified light-weight Merriweather abstract, bulleted features with blue links, more large diagrams with italic figure captions, a tabbed leaderboard table, a four-up gallery of qualitative examples, and a grey BibTeX block over a #fafafa footer.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 70.5%; light grey #e5e6e7 9.1% (the teaser's environment and agent panels), khaki-grey #c6c4b5 7.7% and charcoal #676764 5.5% (diagram strokes and text, button fills blended), pale gold #f0e9c2 3.0% (the spotlight pill and yellow boxes), pale blue-grey #eff2f5 2.1%.

Anatomy in DOM order:

1. **Navbar** — `nav.navbar`, 52px tall, white, a single Font Awesome home icon at the left (`a.navbar-item`, padding 8px 12px, #4a4a4a). Hero body starts below with 48px top padding.
2. **Title** — `h1.title.is-1.publication-title`, 40px (2.5rem `!important`) / 700 / line-height 45px, #363636, Merriweather, centred, two lines (y=100–190); "DataEnvGym" in `<strong>`. Gap 24px.
3. **Spotlight pill** — inline-styled `span`, "⭐ ICLR 2025 Spotlight ⭐", DM Sans 17.6px / 700, #1a1a1a on `linear-gradient(135deg, #ffd700, #ffed4e)`, padding 0.6rem 1.5rem, radius 50px, 2px solid #f0c800 border, shadow `0 4px 15px rgba(255,215,0,0.4)`; 278×50 at y=214. Gap 18px.
4. **Authors** — `.publication-authors.is-size-5`, four DM Sans 20px / 400 links in #485fc7, comma-separated, centred (y=282). Line 30px.
5. **Affiliation** — "UNC Chapel Hill", DM Sans 20px, #4a4a4a (y=312). Gap 24px.
6. **Buttons** — `.publication-links` flex row, centred, gap 10px: six Bulma `button is-normal is-rounded is-dark`, 40px tall, padding 7px 20px, #363636 fill, #ffffff Merriweather 16px labels, icons left (Academicons arXiv, FA GitHub, trophy, copy) or emoji (🤗, 🧵); y=362–402. The BibTeX `<button>` renders in Bulma's system sans because form controls do not inherit the body font. Gap 60px.
7. **Teaser** — `section.hero.teaser`, image 864×315 at y=462 (`.hero-body` padding-top 0, sides 24px inside the 960px container).
8. **Teaser caption** — `h2.subtitle.has-text-left`, Merriweather 20px / 400 / 25px, #4a4a4a, bold runs; y=783–908, running past the fold.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | Bulma `html` background | page, navbar, table background |
| Heading Ink | #363636 | Bulma `$text-strong`, `.title` | title, section titles, dark pill buttons, table text |
| Body Grey | #4a4a4a | Bulma `$text` | body text, abstract, affiliation, teaser caption |
| Link Blue | #485fc7 | Bulma 0.9.4 `$link` | author names, inline links in features and prose |
| Spotlight Gold | #ffd700 | inline gradient start | venue pill fill (to #ffed4e) |
| Spotlight Light | #ffed4e | inline gradient end | venue pill fill |
| Spotlight Edge | #f0c800 | inline border | 2px pill border |
| Pill Text | #1a1a1a | inline color | venue pill label |
| Table Rule | #dbdbdb | Bulma `.table.is-bordered` | 1px cell borders of the environment comparison table |
| Code Grey | #f5f5f5 | Bulma `pre` | BibTeX block |
| Footer Grey | #fafafa | Bulma `.footer`, striped rows | footer band; alternate rows in striped tables |
| Panel Grey | #e5e6e7 | (image) | dominant panel tone of the teaser diagram |

## Tokens — Typography

- **Serif:** declared `'Merriweather', serif` on body, headings, `.content`, `.abstract`; Google Fonts 300/400/700 with italics. Rendered: Merriweather 300, 400, 700, 400i, 700i. Substitute: Source Serif 4 (slightly narrower; keep sizes).
- **Sans:** declared `'DM Sans', sans-serif` on `.author-block`, `.teaser`, `.navbar`, `.footer` and the venue pill. Rendered: DM Sans 400 and 700. Substitute: Inter.
- **Mono:** Bulma `monospace` for `pre` (14px).
- **Icons:** Font Awesome 5.3.1 (SVG), Academicons.

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `.publication-title` | 40px / 700 / 45px |
| Venue pill | inline span | DM Sans 17.6px (1.1rem) / 700 |
| Authors, affiliation | `.publication-authors.is-size-5 .author-block` | DM Sans 20px / 400 / 30px |
| Teaser caption | `.teaser h2.subtitle` | 20px / 400 / 25px, left |
| Section title | `h2.title.is-3` | 32px / 600 / 36px |
| Subsection | `h3.title.is-4` | 24px / 600 / 27px |
| Abstract | `.content.abstract` | 16px / 300 / 24px, justified |
| Body, lists | `.content` | 16px / 400 / 24px |
| Buttons | `.button.is-normal` | 16px / 400 |
| Tab labels | `.tab-text` | 17.6px (1.1rem) / 600 |
| Figure captions | `figcaption` with `<em>` | 16px italic, centred |
| Table | `.table` | 16px; `th` 700 |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Pill buttons | radius 9999px (`is-rounded`), 1px transparent border, height 40px, padding 7px 20px |
| Venue pill | radius 50px, 2px #f0c800 border, shadow `0 4px 15px rgba(255,215,0,0.4)` |
| Tabs | Bulma `is-boxed`: top corners 4px, active tab white with #dbdbdb border; link padding 0.75rem 1.5rem |
| Tables | square, 1px #dbdbdb in bordered table; `is-striped` rows #fafafa |
| Code block | Bulma `pre`, no radius, padding 17.5px 21px |
| Shadows | only the venue pill |

## Layout Metrics

- **Container:** Bulma `.container.is-max-desktop`, max-width 960px at ≥1024px; body sections add `.content-block` max-width 900px (x=270–1170 at 1440).
- **Hero:** `.hero-body` padding 48px 24px; hero column centred; buttons block margin-top 10px with column padding 12px.
- **Teaser:** `.teaser .hero-body` padding 0 24px 48px; image 864px (960 − 2×24 − 2×24 column padding).
- **Sections:** `section.section` padding 48px 24px; h2.title margin-bottom 24px; h3 32px above.
- **Gallery:** `.example-column` 24% each, `space-between`, 16px bottom margin.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1024px | (viewport − 960)/2 | 16px | 40px | 6 buttons in one row; gallery 4-up |
| 769–1023px | 24px (section) + 12px (column) | 16px | 40px | container goes fluid; buttons wrap |
| ≤768px | 24px | 16px | 40px | buttons stack in a column, each max 200px wide; tabs one per line with square corners; table cells 0.9rem; gallery 2-up |
| ≤480px | 24px | 16px | 40px | gallery 1-up; table cells 0.8rem |

## Components

- **Dark pill button:** Bulma `button is-dark is-rounded`, #363636 fill, #ffffff 16px Merriweather label, 9999px radius, 40px tall, padding 7px 20px, icon (1.5em box) left of label; Bulma hover darkens the fill by 2.5%.
- **Spotlight pill:** inline-block span, 135° gold gradient #ffd700 → #ffed4e, #1a1a1a DM Sans 700 at 17.6px, padding 0.6rem 1.5rem, 50px radius, 2px #f0c800 border, warm glow shadow; star emoji either side.
- **Copy-citation button:** a `<button>` styled like the others that copies BibTeX to the clipboard.
- **Boxed tabs:** Bulma `tabs is-boxed` with FA icons (image, square-root, code, wrench) and 17.6px / 600 labels; active tab white with #dbdbdb border.
- **Leaderboard table:** `table is-striped is-hoverable`, fixed layout, columns 25/20/25/20/10%, cells padding 0.5rem, `nowrap` with ellipsis, min-width 600px inside a horizontally scrolling `.table-container`; rows filled by JavaScript.
- **Feature table:** `table is-bordered is-striped is-narrow`, 1px #dbdbdb, check marks in cells.
- **Gallery column:** thumbnail opening Lightbox2, centred caption "Figure 6: GQA Examples" with a `<small>` "(click to zoom)", and a full-width `button is-small` "Open in new tab" with an external-link icon.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navbar | Present but non-standard | a lone home icon, no links |
| Title / authors / affiliation | Yes | serif title, DM Sans author lines |
| Venue badge | Yes | gold gradient Spotlight pill |
| Link buttons | Yes | six dark pills incl. Leaderboard, HuggingFace, Thread |
| Teaser | Yes | large flat diagram + 20px caption |
| Abstract | Yes | justified Merriweather 300 |
| Features list | Yes | bullets with blue links |
| Method / environment figures | Yes | full-width diagrams with italic captions |
| Results figures | Yes | three h3 subsections with figures |
| Leaderboard | Yes | boxed tabs + striped table |
| Qualitative gallery | Yes | 4-up thumbnails with lightbox |
| Video | No (absent from the source) | |
| BibTeX | Yes | Bulma pre + copy button in hero |
| Footer | Yes | #fafafa band, "Website template adapted from Nerfies" |

## Adapting to Other Content

- **More authors:** keep the comma-separated DM Sans 20px line; add superscript numbers and a second affiliation line in the same size.
- **Oral or award:** reuse the pill recipe and keep gold only for award status; a plain acceptance can use the same pill shape in white with a 2px #dbdbdb border.
- **Results table:** use the leaderboard recipe (striped, hoverable, 0.5rem cells) under an h2.title.is-3; bold the best row.
- **News list:** a `.content` bullet list in 16px Merriweather with the date in DM Sans 700.
- **Long abstracts:** narrow the abstract to about 720px or raise it to 17px; at 900px and 16px the measure is long.

## Do's and Don'ts

- Do pair a bold serif title with a geometric sans for people and metadata.
- Do keep buttons uniform dark pills; let emoji or icons do the labelling.
- Do reserve the gold gradient for the single venue badge.
- Don't add more accent colors; blue is only for links.
- Don't forget to set the font on `<button>` elements; the BibTeX button falls back to the system sans.
- Don't set long text in Merriweather 300 at a 900px measure; it is the weakest part of the page.

## Surfaces

White throughout, with one #fafafa footer band, a #f5f5f5 code block, striped table rows in #fafafa and the gold pill. The teaser diagram brings its own light grey panels.

## Imagery

Large flat vector diagrams with rounded grey panels and pastel boxes (yellow evaluation, green policy, blue training, orange engine) and black arrows; plots in the results sections; screenshot-style qualitative example sheets in the gallery.

## Layout

Centred hero in a 960px container, then 900px left-aligned content sections, each `section.section` stacked without bands. Rendered height about 7,700px.

## Agent Prompt Guide

Quick colors: headings #363636, body #4a4a4a, links #485fc7, buttons #363636 with #ffffff text, spotlight gradient #ffd700 → #ffed4e with #f0c800 border and #1a1a1a text, table rule #dbdbdb, code #f5f5f5, footer #fafafa.

1. "Create a hero: a centred Merriweather 40px / 700 title in #363636 on two lines; below it a pill badge with a 135° gradient from #ffd700 to #ffed4e, 2px solid #f0c800 border, 50px radius, padding 0.6rem 1.5rem, DM Sans 17.6px bold #1a1a1a text, shadow 0 4px 15px rgba(255,215,0,0.4); then DM Sans 20px author links in #485fc7 and an affiliation in #4a4a4a."
2. "Add a row of link buttons: flex, centred, gap 10px; each a 40px-tall pill with 9999px radius, #363636 fill, white 16px Merriweather label, padding 7px 20px, icon left; stack them in a column with max width 200px under 768px."
3. "Build a leaderboard: boxed tabs with icons and 17.6px / 600 labels, then a striped hoverable table with 0.5rem cell padding, fixed column widths 25/20/25/20/10%, alternate rows #fafafa, inside a horizontally scrolling wrapper."

## Similar Pages

- Nerfies-derived Bulma pages (the stated base) that swap in a serif display face.
- UNC MURGe-Lab project pages by the same group with dark pill button rows.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --heading: #363636;
  --text: #4a4a4a;
  --link: #485fc7;
  --button: #363636;
  --badge-from: #ffd700;
  --badge-to: #ffed4e;
  --badge-border: #f0c800;
  --badge-text: #1a1a1a;
  --rule: #dbdbdb;
  --code-bg: #f5f5f5;
  --footer: #fafafa;
  --font-serif: 'Merriweather', serif;
  --font-sans: 'DM Sans', sans-serif;
  --title-size: 2.5rem;
  --container: 960px;
  --content: 900px;
}
```

## Provenance

- **URL:** https://dataenvgym.github.io/
- **Paper:** DataEnvGym: Data Generation Agents in Teacher Environments with Student Feedback (arXiv 2410.06215), Zaid Khan, Elias Stengel-Eskin, Jaemin Cho, Mohit Bansal.
- **Venue:** ICLR 2025, marked Spotlight on the page.
- **Selection reason:** arXiv comment states acceptance at ICLR 2025; project page linked in the comment.
- **Template credit:** footer reads "Website template adapted from Nerfies".
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share, 1440 screenshots (first viewport and tall), inline style block and inline attributes, Bulma 0.9.4 defaults; 2026-10-28.
