# Leaderboard-First Nerfies — Style Reference

> A benchmark that leads with its scoreboard: a fish-logo small-caps wordmark, a gradient venue line, then a full-width grey-headed leaderboard with zebra rows and blue model links.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (`tools/computed_style.py`: computed styles of the navbar, wordmark title, subtitle, author links, venue span, buttons, sections, leaderboard `th` and `td`, `pre` and footer, first-viewport anatomy, loaded fonts and color share), the first-viewport screenshot, the full-page capture, a 1440×8300 headless capture of the middle sections, and the page's own `static/css/index.css` and `static/css/leaderboard.css` plus an inline `<style>` for code, over Bulma 0.9. The footer says the site is adapted from Video-MME. Positions are document coordinates at 1440px wide.

## Overview

TUNA is a Video-MME-derived Bulma page. A white centered navbar with a 🔥 "More Research" dropdown sits above a centered wordmark: a 77px fish logo followed by "TUNA" set as a 48px Google Sans "T" and a 40px "UNA" to imitate small caps. Under it a 32px regular #4a4a4a subtitle runs two lines, then ten #209cee author links with superscripts, a corresponding-author note, affiliations, and "ACL 2025 Main" in 24px bold text filled with a #0077be → #00c9a7 gradient. Four dark (#363636) pill buttons follow, two with emoji (🤗 Dataset, 🏆 Leaderboard). After a justified abstract in a 1070px column, the page puts the leaderboard first: a full-width (1344px) Arial table with a two-row grouped header on #dddddd, 1px #dddddd cell borders, #f5f5f5 zebra rows, a rank column, bold #3273dc model links with 12px grey organization names beneath, and hover rows in #dddddd. Major parts are announced by short #f5f5f5 bands with 48px bold small-caps titles ("Benchmark", "Method", "Analysis"), and each part holds Bulma `.box` cards with carousels of videos or figures. A #f4f4f4 rounded BibTeX block and a #fafafa footer close the page.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): white #ffffff 83.4%, light grey #c1c7cb 5.9% (logo and text antialiasing), pale blue-grey #dee5ea 3.0% (fish logo), warm off-white #f6f5f4 2.6%, mid grey #848586 2.3% (text and buttons), #fcfcfc 2.0%, remainder under 0.5%. The only saturated pixels are the blue author links, the teal-blue gradient venue and the fish logo.

Anatomy in DOM order (y = top of element box):

1. **Navbar** (`nav.navbar`), y 0, 52px, white, no border; centered 🔥 emoji (18px) and "More Research" `navbar-link` (16px #4a4a4a, Bulma chevron #3273dc). Gap 48px.
2. **Wordmark title** (`h1.title.is-1.publication-title.is-bold`), y 100, 77px tall: a 77×77 fish logo (`width: 1.6em`), then "T" at Google Sans 48px/600 and "UNA" in a 40px span, all #363636, centered. Gap 4px.
3. **Subtitle** (`h2.subtitle.is-3.publication-subtitle`), y 181, 960px, two lines, Noto Sans 32px/40px weight 400, #4a4a4a, centered (margin -20px 0 20px). Gap 26px.
4. **Authors** (`.publication-authors`), y 287, two lines of Google Sans 20px/30px, #209cee links with superscript affiliation and † marks.
5. **Note and affiliations**, about y 352 and y 380: "†Corresponding Author" in a smaller line, then "¹Northeastern University, ²Kuaishou Technology" at 20px #4a4a4a. Gap about 27px.
6. **Venue** (`span.publication-venue`), y 437, 166×33, "ACL 2025 Main", Noto Sans 24px/36px weight 700, text filled with `linear-gradient(to right, #0077be, #00c9a7)` via `background-clip: text`. Gap 76px.
7. **Link buttons** (`a.external-link.button.is-normal.is-rounded.is-dark`), y 513, arXiv 98px, Code 100px, 🤗 Dataset 119px, 🏆 Leaderboard 157px; 40px tall, #363636, white Noto Sans 16px/400, padding 7px 20px. The hero ends at y 618.
8. **Abstract** (`section.section`), y 618, padding 48px 24px; heading y 666, Noto Sans 32px/36px 600 #363636, centered; text below in a 1070px four-fifths column, 16px/24px justified #4a4a4a. The fold falls inside the abstract.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Heading Ink | #363636 | Bulma `.title`, `strong` | Wordmark, section headings, table header labels, bold text |
| Body Grey | #4a4a4a | Bulma body | Subtitle, affiliations, abstract, table numbers, captions |
| Band Title | rgba(0,0,0,.7) | Bulma `.hero.is-light` | Small-caps band titles (Benchmark, Method, Analysis) |
| Author Blue | #209cee | `.publication-authors a` | Author names |
| Link Blue | #3273dc | Bulma `a`, `.ext-link` | Model names in the leaderboard, navbar chevron, footer links |
| Org Grey | #858383 | inline `color` | Organization names under model names |
| Venue Start | #0077be | inline gradient | "ACL 2025 Main" gradient text, left |
| Venue End | #00c9a7 | inline gradient | "ACL 2025 Main" gradient text, right |
| Header Grey | #dddddd | `thead { background: #ddd }`, `#results th/td` border, `#results tr:hover` | Leaderboard header fill, cell borders, hover row |
| Zebra | #f5f5f5 | `#results tr:nth-child(even)`, `.hero.is-light` | Even leaderboard rows, part-title bands |
| Sorted Column | #ddeeee | `table#results.js-sort-N … td` | Tint on the column the table is currently sorted by |
| Best Score Red | #c6011f | `.best-score-text` | Declared class for best scores |
| Code Wash | #f4f4f4 | inline `pre` style | BibTeX block |
| Code Pink | #d63384 | inline `code` style | Code text color in the BibTeX block |
| Button Dark | #363636 | `.button.is-dark` | Link buttons (white text) |
| Footer Wash | #fafafa | `.footer` | Footer band |
| White | #ffffff | page, `.box` | Page and card backgrounds |
| Box Shadow | #0a0a0a | Bulma `.box` shadow at 10% and 2% alpha | Soft shadow and hairline around media boxes |

Declared but not visible: `#results th` sets `background-color: var(--UCLA-darkblue)` and `color: white`, but the variable is undefined, so the header shows the `thead` #dddddd fill and the labels inside `<strong>` render #363636. The `CustomFont` (Gilroy Bold Italic) `@font-face` and `.mathvista` class are unused.

## Tokens — Typography

- **Title, authors**: declared `'Google Sans', sans-serif`. Rendered: Google Sans 400 only (`fonts_loaded`); the 600 wordmark is synthesized. Substitute: Figtree.
- **Body, headings, subtitle, venue**: declared `'Noto Sans', sans-serif`. Rendered: Noto Sans 400 only; bold weights synthesized.
- **Leaderboard**: `#results` declares `Arial, Helvetica, sans-serif` (Arial renders on Windows).
- **Code**: `Consolas, "Courier New", monospace`.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Wordmark | `h1.publication-title` + span | 48px "T" / 40px "UNA", 54px line | 600 | #363636 |
| Band title | `h1.title.is-1.mathvista_other` | 48px / 54px, small caps | 700 | rgba(0,0,0,.7) |
| Subtitle | `h2.subtitle.is-3` | 32px / 40px | 400 | #4a4a4a |
| Section heading | `h2.title.is-3` | 32px / 36px | 600 | #363636 |
| Venue | `span.publication-venue` | 24px / 36px | 700 | gradient #0077be → #00c9a7 |
| Authors | `.publication-authors` | 20px / 30px | 400 | #209cee |
| Body | `.content` | 16px / 24px | 400 | #4a4a4a, justified |
| Table header | `#results th strong` | 16px / 24px Arial | 700 | #363636 |
| Table cell | `#results td` | 16px / 24px Arial | 400 | #4a4a4a |
| Model link | `a.ext-link` in `b` | 16px Arial | 700 | #3273dc |
| Org name | `p` inline | 12px Arial | 400 | #858383 |
| Code | `pre code` | 14px / 21px | 400 | #d63384 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link button | 290486px | 1px transparent | none |
| Leaderboard table | 0 | outer and cell borders 1px solid #dddddd | none |
| Content box (`.box`) | 6px | none | Bulma: 0 0.5em 1em -0.125em rgba(10,10,10,.1), 0 0 0 1px rgba(10,10,10,.02) |
| BibTeX `pre` | 5px | 1px solid #dddddd | none |
| Part-title band | 0 | none | none |

## Layout Metrics

- **Containers**: hero and BibTeX use `.container.is-max-desktop`, 960px (x 240–1200). Abstract, leaderboard and content sections use the full Bulma `.container`, 1344px at ≥1408px (x 48–1392); text sits in four-fifths columns (1070px), and the Data Examples column is stretched to `width: 110%`.
- **Hero**: navbar 52px, `.hero-body` padding 48px 24px; subtitle pulled up 20px; venue in its own block; buttons 76px below the venue.
- **Sections**: `.section` padding 48px 24px. Part-title bands are `hero is-light is-small` (padding 24px), about 102–107px tall.
- **Leaderboard**: `#results` 100% of the 1344px container, header cells padding 12px 8px, body cells 8px (model cells 2px 10px), rows about 47px; column widths set inline (rank 50px, model 215px, metrics 100–110px).
- **Boxes and carousels**: `.box.m-5` (20px margin) holding a bulma-carousel; videos 800×480 with justified captions below.
- **Footer**: #fafafa, padding 48px 24px 96px, text in an `is-8` column.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1408px | 960px hero, 1344px content | 16px | 48px | as described |
| 1216–1407px | content container 1152px | 16px | 48px | leaderboard narrows |
| 1024–1215px | content container 960px | 16px | 48px | leaderboard columns compress |
| ≤1023px | fluid; navbar collapses to a burger | 16px | 48px | leaderboard wider than the screen; columns full width at ≤768px; `#org-banners` stacks |

## Components

- **Logo wordmark**: an inline logo image at 1.6em, then the name with the first letter at full size and the rest at about 83% to fake small caps, Google Sans 600 #363636.
- **Gradient venue text**: a bold 24px span with `background: linear-gradient(to right, #0077be, #00c9a7)`, `-webkit-background-clip: text`, transparent fill.
- **Dark pill button**: Bulma `.button.is-dark.is-rounded`, #363636, white 16px, padding 7px 20px, icon or emoji left.
- **Leaderboard table**: Arial 16px, centered numbers; two-row header with `colspan` groups ("Dynamic Element Type (%)", "Visual Characteristic (%)") on #dddddd with bold #363636 labels, padding 12px 8px; 1px #dddddd borders on every cell; even rows #f5f5f5; hover row #dddddd; rank numbers in the first column; model cell left-aligned with a bold #3273dc link and a 12px #858383 organization line; sortable headers underline on hover; sorted column tinted #ddeeee; legend and footnotes in 16px below.
- **Part-title band**: full-bleed #f5f5f5 strip, 24px padding, centered 48px bold small-caps title in rgba(0,0,0,.7).
- **Media box**: Bulma `.box` (white, 6px radius, soft shadow, 20px padding) with a carousel of an 800px video or a figure, a bold-label metadata line, a justified caption and dot pagination.
- **BibTeX block**: `pre` #f4f4f4, 1px #dddddd border, 5px radius, Consolas 14px in #d63384.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navigation | yes | centered navbar with emoji and dropdown |
| Logo and wordmark | yes | fish logo and faux small caps |
| Subtitle | yes | 32px regular grey |
| Authors, affiliations | yes | blue links, superscripts, note line |
| Venue | yes | gradient bold text |
| Link buttons | yes | four dark pills, two with emoji |
| Abstract | yes | 1070px justified |
| Results table | yes | full-width sortable leaderboard |
| Part-title bands | yes | grey strips with small-caps titles |
| Data examples | yes | boxed video carousel with captions |
| Statistics and comparison tables | present but non-standard | LaTeX tables as images inside boxes |
| Method figure | yes | boxed carousel |
| BibTeX | yes | grey rounded `pre`, pink code |
| Footer | yes | #fafafa credit |

## Adapting to Other Content

- **More authors**: keep the centered 20px lines with superscripts; put the corresponding-author note and affiliations on their own lines below.
- **A second results table**: reuse the leaderboard recipe: Arial 16px, #dddddd header and borders, #f5f5f5 zebra, #dddddd hover, bold #3273dc names with a 12px #858383 sub-line, and mark best scores with `.best-score-text` (#c6011f).
- **News**: a white `.box` under the buttons with a dated 16px list; keep the gradient only on the venue line.
- **Long publication lists**: inside a four-fifths column, 16px rows with bold titles and #3273dc links.
- **More parts**: open each with a #f5f5f5 part-title band and put its content in `.box` cards.
- **Video-heavy content**: carousels inside boxes, videos at 800px with metadata and justified captions.

## Do's and Don'ts

- Do put the leaderboard directly after the abstract at the full container width.
- Do group metric columns under `colspan` headers and keep numbers centered.
- Do use Arial for the table and Google Sans or Noto Sans elsewhere, as the page does.
- Do separate major parts with short grey small-caps bands.
- Don't rely on undefined CSS variables for header colors; set the header fill explicitly.
- Don't add a second gradient; the venue line is the only one.
- Don't stretch content columns past 100% (`width: 110%`) in new pages.

## Surfaces

White page and hero; #dddddd table header; #f5f5f5 zebra rows and part-title bands; white `.box` cards with soft shadows; a #f4f4f4 BibTeX block; #fafafa footer.

## Imagery

A cartoon blue fish logo with a friendly face; film and sports video stills inside the example carousel; LaTeX-rendered statistics and comparison tables with red crosses and green ticks; a pastel construction diagram with numbered panels and stock-site logos.

## Layout

A centered 960px hero and a full 1344px content container, with text in 1070px four-fifths columns and the leaderboard spanning the container. Rendered height is about 8,290px at 1440px.

## Agent Prompt Guide

Quick colors: headings #363636, body #4a4a4a, authors #209cee, model links #3273dc, org #858383, table header and borders #dddddd, zebra #f5f5f5, venue gradient #0077be → #00c9a7, buttons #363636, best score #c6011f.

1. "Build a hero in a 960px column: a centered wordmark with a 77px logo then the name in Google Sans 48px weight 600 #363636 (first letter full size, the rest at 40px); a two-line Noto Sans 32px/40px regular #4a4a4a subtitle; 20px #209cee author links with superscripts; the venue as 24px bold text filled with linear-gradient(to right, #0077be, #00c9a7) via background-clip text; then four #363636 pill buttons, white 16px, padding 7px 20px."
2. "Make a full-width leaderboard: Arial 16px, centered; header two rows with colspan groups on #dddddd, bold #363636 labels, padding 12px 8px; every cell bordered 1px solid #dddddd with 8px padding; even rows #f5f5f5, hover #dddddd; first column rank numbers; model cell left-aligned with a bold #3273dc link and a 12px #858383 organization line under it."
3. "Add a part divider: full-bleed #f5f5f5 strip with 24px padding and a centered 48px bold small-caps title in rgba(0,0,0,.7), followed by a white box (6px radius, shadow 0 0.5em 1em -0.125em rgba(10,10,10,.1)) holding a carousel of 800px videos with justified 16px captions."

## Similar Pages

- Video-MME and its derivatives (MathVista-style leaderboards with small-caps band titles).
- Video and MLLM benchmark pages with sortable `js-sort-table` leaderboards.

## Quick Start

```css
:root {
  --heading: #363636;
  --text: #4a4a4a;
  --band-title: rgba(0, 0, 0, .7);
  --author: #209cee;
  --link: #3273dc;
  --org: #858383;
  --venue-gradient: linear-gradient(to right, #0077be, #00c9a7);
  --table-head: #dddddd;
  --table-border: #dddddd;
  --zebra: #f5f5f5;
  --best: #c6011f;
  --code-bg: #f4f4f4;
  --font-title: 'Google Sans', Figtree, sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --font-table: Arial, Helvetica, sans-serif;
  --container-hero: 960px;
}
```

## Provenance

- **URL**: https://friedrichor.github.io/projects/TUNA/
- **Paper**: TUNA: Comprehensive Fine-grained Temporal Understanding Evaluation on Dense Dynamic Videos (arXiv 2505.20124), Fanheng Kong et al., Northeastern University and Kuaishou Technology.
- **Venue**: ACL 2025 (Main).
- **Selection reason**: existing verified entry; the arXiv 2505.20124 comment states acceptance at ACL 2025 Main and links the page. Chosen for the logo wordmark with small-caps branding, the tidy centered header and the full-width leaderboard with grouped headers, zebra rows and blue model links.
- **Template credit**: footer says the website is adapted from Video-MME (Nerfies lineage, Bulma).
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and fonts, the first-viewport screenshot, full-page capture and a 1440×8300 headless capture, `static/css/index.css`, `static/css/leaderboard.css`, the inline styles and the HTML. Date 2026-10-28.
