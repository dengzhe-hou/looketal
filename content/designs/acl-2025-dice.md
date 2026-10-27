# Pastel Pill Nerfies — Style Reference

> A Nerfies page with a game-box cover: a charcoal dice banner stamps the identity, then pastel brand-tinted pills and a grey carousel strip carry you into a quiet two-column method read.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (`tools/computed_style.py`: computed styles of the nav, language buttons, title, authors, link buttons, star button, sections, `pre` and footer, first-viewport anatomy, loaded fonts and color share), the first-viewport screenshot and the full-page capture, and the page's own `static/css/index.css` over Bulma 0.9 and bulma-carousel from the Nerfies template. Positions are document coordinates at 1440px wide.

## Overview

DICE-BENCH keeps the Nerfies skeleton but changes three things. A centered Bulma navbar (home icon, "More Research" dropdown) carries three small grey pill language switchers (EN, 中文, 한국어) pinned to the top right; every text block is tagged `data-i18n` and swaps language in place. The link row uses translucent brand-tinted pills instead of the usual black ones: grey for GitHub (with a small white "Star 26" counter card stacked beneath it), yellow for Hugging Face, grey for X, blue for LinkedIn, red for arXiv. And the teaser is a bold graphic banner: a charcoal (#282828) panel with a white 3D die (one red pip) and "DICE-BENCH" in heavy white sans, 912px wide. Below it a #f5f5f5 band holds a three-up figure carousel with bordered, rounded slides and dot pagination. The rest is plain Nerfies typography: a centered 32px semibold "Abstract" over 768px justified text, a two-column row pairing "Data Generation Pipeline" (text plus figure) with "DICE-SCORE Metric" (text plus a MathJax formula), a three-column validation stage list, a #f5f5f5 "Dataset Format" section with a JSON `pre`, BibTeX and a #fafafa footer with social icons.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): white #ffffff 67.0%, banner charcoal #282828 11.2%, light grey #edeeed 7.6% (die faces, language and GitHub pills), mid grey #b2b1b1 6.0% (die shading and text antialiasing), dark warm grey #49403f 3.9%, banner black #252525 1.9%, remainder under 2%. The pastel pills and the blue first-author link are the only colors before the banner's red pip.

Anatomy in DOM order (y = top of element box):

1. **Navbar** (`nav.navbar`), y 0, height 52, white, no border or shadow; centered `navbar-start` with a Font Awesome home icon (x 618) and the "More Research" `navbar-link` (16px Noto Sans #4a4a4a, Bulma chevron in #3273dc).
2. **Language pills** (`.lang-container button.button.is-light.is-rounded.is-small.lang-btn`), y 8, absolutely positioned 16px from the right; EN 47px, 中文 56px, 한국어 68px wide, 30px tall, #f5f5f5 fill, rgba(0,0,0,.7) text 12px in the system font (Segoe UI), padding 5px 15px. Gap to title 48px from the nav bottom.
3. **Title** (`h1.title.is-1.publication-title`), y 100, 960px wide, three lines, Google Sans 48px/54px weight 600, #363636, centered. Gap 24px.
4. **Authors** (`.publication-authors`, `is-size-5`), y about 289, two lines of Google Sans 20px/30px #4a4a4a; only the first author is a link (#209cee); superscript affiliation numbers. No gap.
5. **Affiliations** (second `.publication-authors`), y about 349, two lines 20px/30px #4a4a4a, forced break after the second affiliation. Gap about 24px.
6. **Link row** (`.publication-links`, flex, wrap, centered, 8px gap), y 442: the "Code" pill (100×40) with the "Star 26" card (94×34) under it at y 493; the other four pills (Data 96px, X 70px, LinkedIn 126px, arXiv 98px) centered against that stack at y 464. All pills Noto Sans 16px/400, padding 7px 20px, 1px #dbdbdb border, full radius, small logo icon on the left. Hero ends at y 592.
7. **Banner image** (`section.hero.teaser img`), y 592, 912×356, charcoal graphic with die and wordmark. Gap 6px.
8. **Banner subtitle** (`h2.subtitle.has-text-centered`), y 954, 912px, two lines Google Sans 20px/25px #4a4a4a, centered. The teaser section ends at y 1053, and the #f5f5f5 carousel band starts directly after it; the fold falls inside the banner.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Heading Ink | #363636 | Bulma `.title` | Paper title, section headings, stage headings |
| Body Grey | #4a4a4a | Bulma body | Authors, affiliations, subtitle, body text, `pre` text, nav link |
| Author Blue | #209cee | `.publication-authors a` | First-author link |
| Link Blue | #3273dc | Bulma `a`, `.navbar-link` arrow | In-text links (dataset card), navbar chevron |
| Banner Charcoal | #282828 | banner image pixels | Teaser banner background |
| Grey Band | #f5f5f5 | `.hero.is-light`, inline `background-color`, `.is-light` | Carousel band, Dataset Format section, language pills, `pre` fill |
| Footer Wash | #fafafa | Bulma `.footer` | Footer band |
| Pill Border | #dbdbdb | Bulma `.button` | 1px border of the link pills |
| Slide Border | #bbbbbb | `.results-carousel .item` | 1px carousel slide border |
| GitHub Ink | #24292e | `.button.is-github` | Code pill text; fill is rgba(36,41,46,.15), about #dedfe0 on white |
| HF Yellow Tint | #fff3bf | `.button.is-hf` rgba(255,207,0,.25) on white | Data pill fill (text #000000) |
| X Grey Tint | #d9d9d9 | `.button.is-x` rgba(0,0,0,.15) on white | X pill fill (text #000000) |
| LinkedIn Blue | #0a66c2 | `.button.is-linkedin` | LinkedIn pill text; fill rgba(10,102,194,.2), about #cee0f3 |
| arXiv Red | #b31b1b | `.button.is-arxiv` | arXiv pill text; fill rgba(179,27,27,.2), about #f0d1d1 |
| Star Text | #495057 | `.star-button`, `.star-text` | Star counter label and count |
| Star Border | #e9ecef | `.star-button` | 2px star card border |
| Star Gold | #ffcc00 | `.star-icon .fa-star` | Star icon (hover #ffe135) |
| Star Hover Gold | #ffd700 | `.star-button:hover` | Star card border on hover |
| Star Card Tint | #f8f9fa | `.star-button` gradient end | Star card background (white to #f8f9fa) |
| White | #ffffff | page | Page, hero, abstract, method sections |

Declared but not visible: `.interpolation-panel` (#f5f5f5, 10px radius) is unused; `.lang-btn` declares `rgba(0,0,0,.05)` but the Bulma `is-light` fill #f5f5f5 is what renders.

## Tokens — Typography

- **Title, authors, teaser subtitle**: declared `'Google Sans', sans-serif`. Rendered: Google Sans 400 only (`fonts_loaded`), so the 600 title is synthesized. Substitute: Figtree.
- **Body and headings**: declared `'Noto Sans', sans-serif` on `body`. Rendered: Noto Sans 400 only; 600 headings are synthesized. Substitute: Noto Sans with real 600.
- **Language pills**: Bulma buttons fall back to `BlinkMacSystemFont, -apple-system, "Segoe UI", …` here (Segoe UI on Windows).
- **Math**: MathJax 3 CHTML (MJXTEX); **code**: generic `monospace` (Consolas on Windows).

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title` | 48px / 54px | 600 | #363636 |
| Section heading | `h2.title.is-3` | 32px / 36px | 600 | #363636 |
| BibTeX heading | `h2.title` | 32px / 36px | 600 | #363636 |
| Authors, affiliations | `.publication-authors` | 20px / 30px | 400 | #4a4a4a, link #209cee |
| Teaser subtitle | `.teaser h2.subtitle` | 20px / 25px | 400 | #4a4a4a |
| Stage heading | `.content h4 strong` | 20px | 700 | #363636 |
| Body | `.content p` | 16px / 24px | 400 | #4a4a4a, justified in abstract and validation |
| Link pill | `.button.is-normal` | 16px / 24px | 400 | per brand |
| Star counter | `.star-button` | 13.6px / 20.4px | 500 (count 600) | #495057 |
| Code | `pre code` | 14px / 21px | 400 | #4a4a4a |
| Language pill | `.button.is-small` | 12px / 18px | 400 | rgba(0,0,0,.7) |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link pill | 290486px | 1px solid #dbdbdb | none; hover deepens the tint by 0.1 alpha |
| Language pill | 290486px | 1px transparent | none |
| Star card | 8px | 2px solid #e9ecef (hover #ffd700) | 0 2px 4px rgba(0,0,0,.1); hover 0 4px 8px rgba(0,0,0,.15), lift 1px |
| Carousel slide | 10px | 1px solid #bbbbbb | none |
| Banner, figures | 0 | none | none |
| `pre` | 0 | none | none |

## Layout Metrics

- **Container**: `.container.is-max-desktop`, 960px (x 240–1200) for hero, teaser and text sections; the carousel uses the full Bulma `.container`, 1344px at ≥1408px.
- **Hero**: Bulma `.hero-body` padding 48px 24px; title margin-bottom 24px; links block in a `.column` (12px padding).
- **Teaser**: `.teaser .hero-body` padding 0 24px 48px; banner 912px wide.
- **Carousel band**: `hero is-light is-small`, #f5f5f5, padding 24px (`is-small`), three slides visible (`slidesToShow: 3`, no autoplay), each slide 5px margin, dot pagination below.
- **Sections**: `.section` padding 48px 24px. Abstract in a four-fifths column (768px). Method row: two equal columns of 468px with 24px between them; validation stages: three equal columns.
- **Dataset Format**: full-width #f5f5f5 section, `pre` 960px with padding 17.5px 21px.
- **Footer**: #fafafa, padding 48px 24px 96px, centered icon links (25px) and a template credit.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px | 960px container | 16px | 48px | as described; navbar menu and language pills visible |
| 769–1023px | fluid, 24px section padding | 16px | 48px | navbar collapses to a burger, which also hides the language pills; columns still side by side |
| ≤768px | fluid | 16px | 48px | columns stack (method row, validation stages); carousel shows fewer slides |

## Components

- **Brand-tint pill**: Bulma `.button.is-normal.is-rounded`, 40px tall, padding 7px 20px, 1px #dbdbdb border, 16px Noto Sans, a 1em logo image left; fill is the brand color at 15–25% alpha with full-strength brand text (GitHub #24292e, LinkedIn #0a66c2, arXiv #b31b1b, HF and X black). Hover adds 0.1 alpha. The row is a centered wrapping flex with 8px gaps.
- **Star counter card**: stacked under the Code pill, 8px radius, 2px #e9ecef border, white-to-#f8f9fa gradient, padding 8px 12px, min-width 85px, #ffcc00 star icon with a soft glow, "Star 26" 13.6px/500 #495057 (count 600, filled by script); hover border #ffd700, warm gradient, lift and star rotation.
- **Language switcher**: three `is-small is-rounded is-light` buttons, #f5f5f5, 12px text at 70% black, 30px tall, absolute top 8px right 16px; the active one darkens to rgba(0,0,0,.15).
- **Graphic banner**: one full-width image at 912px with no frame, followed by a centered 20px Google Sans subtitle in which the product name is set in small caps (`.dnerf`).
- **Figure carousel**: #f5f5f5 band, three bordered slides (1px #bbbbbb, 10px radius, overflow hidden), round white arrow buttons, dot pagination.
- **Two-column method block**: each column opens with a 32px/600 #363636 heading, then 16px #4a4a4a text, then a figure or a centered MathJax display formula at 1.2em.
- **Code block**: `pre` #f5f5f5, padding 17.5px 21px, 14px monospace #4a4a4a, no radius; on the grey Dataset Format band it merges into the background.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navigation | yes | centered Bulma navbar with home icon and dropdown |
| Language switcher | yes | three small grey pills, top right |
| Title, authors, affiliations | yes | Google Sans, centered; only the first author linked |
| Link buttons | present but non-standard | translucent brand-tinted pills plus a star counter |
| Teaser | yes | graphic banner image with a subtitle |
| Figure carousel | yes | three-up grey band |
| Abstract | yes | 768px justified |
| Method and metric | yes | two-column text with figure and formula |
| Validation stages | yes | three-column text with bold `h4`s |
| Dataset example | yes | JSON `pre` on a grey band |
| BibTeX | yes | Bulma `pre` |
| Results table | absent from the source | results appear only as carousel images |
| Footer | yes | #fafafa, social icons and credit |

## Adapting to Other Content

- **More authors**: keep the centered 20px line; link names in #209cee and let the line wrap, then affiliations on a separate block with a manual break between institutions.
- **More links**: add pills to the flex row using the same recipe and a brand color at 15–25% alpha; keep text in the full brand color.
- **A results table**: inside the 960px container, a Bulma `.table.is-fullwidth` at 16px #4a4a4a with a 600 #363636 header and 1px #dbdbdb rules, placed on white; put a second table on the #f5f5f5 band if it needs separation.
- **News**: a short bulleted list in a `.content` block under the link row, 16px, dates bold; do not add a colored banner, the teaser image already carries identity.
- **Long publication lists**: a single 960px column of 16px entries with titles in #363636 600 and links in #3273dc.
- **More languages**: add another `is-small` pill to the switcher and tag every text node with `data-i18n`.

## Do's and Don'ts

- Do let one graphic banner carry the brand; keep the rest of the page typographic.
- Do tint link pills with each service's own color at low alpha.
- Do keep the 960px column and 48px section padding of Nerfies.
- Do alternate white and #f5f5f5 bands to separate media from text.
- Don't make the pills opaque or saturated; the translucency is the style.
- Don't add shadows to figures or slides; slides get a 1px #bbbbbb border only.
- Don't hide content in the navbar on desktop; on tablets the burger also hides the language pills, so offer the switcher elsewhere if it matters.

## Surfaces

White page and hero; a charcoal #282828 banner image as the single dark surface; #f5f5f5 for the carousel band, the Dataset Format section and code; #fafafa footer. No cards apart from the small star counter.

## Imagery

A charcoal banner with a glossy white 3D die and a red pip next to a heavy white wordmark and subtitle, then paper figures: pipeline diagrams in pastel blue and green boxes, a LaTeX comparison table with check marks, and line plots with shaded bands. Figures sit unframed in text columns and framed (1px border, 10px radius) in the carousel.

## Layout

A centered 960px Nerfies column for hero, teaser and text, interrupted by a full-width grey carousel band. The method area uses two equal columns, the validation stages three. Rendered height is about 4,360px at 1440px.

## Agent Prompt Guide

Quick colors: headings #363636, body #4a4a4a, author link #209cee, grey band #f5f5f5, footer #fafafa, banner #282828, pill border #dbdbdb, brand texts #24292e, #0a66c2, #b31b1b.

1. "Build a Nerfies hero in a 960px column: centered Google Sans 48px/54px weight 600 #363636 title, 24px below a 20px/30px #4a4a4a author line (first author #209cee) and a 20px affiliation block; then a centered wrapping flex row with 8px gaps of 40px pills: padding 7px 20px, 1px solid #dbdbdb, full radius, 16px Noto Sans, a 1em logo left, fills rgba(36,41,46,.15) with #24292e text, rgba(255,207,0,.25) with black, rgba(10,102,194,.2) with #0a66c2, rgba(179,27,27,.2) with #b31b1b."
2. "Add a language switcher: three 30px pill buttons (EN, 中文, 한국어), #f5f5f5 fill, 12px system-font text at rgba(0,0,0,.7), padding 5px 15px, absolutely positioned 8px from the top and 16px from the right of a white 52px navbar."
3. "Add a figure carousel band: full-width #f5f5f5, padding 24px, three slides visible, each with a 1px solid #bbbbbb border, 10px radius and overflow hidden, dot pagination below; follow it with a white section, padding 48px 24px, centered 32px/600 #363636 'Abstract' and 16px #4a4a4a justified text in a 768px column."

## Similar Pages

- Nerfies-template pages (Bulma, Google Sans titles, Noto Sans body).
- Multilingual project pages with in-page language toggles.

## Quick Start

```css
:root {
  --heading: #363636;
  --text: #4a4a4a;
  --author-link: #209cee;
  --link: #3273dc;
  --band: #f5f5f5;
  --footer: #fafafa;
  --banner: #282828;
  --pill-border: #dbdbdb;
  --pill-github: rgba(36, 41, 46, .15);
  --pill-hf: rgba(255, 207, 0, .25);
  --pill-linkedin: rgba(10, 102, 194, .20);
  --pill-arxiv: rgba(179, 27, 27, .20);
  --font-title: 'Google Sans', Figtree, sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --container: 960px;
  --section-pad: 48px 24px;
}
```

## Provenance

- **URL**: https://hcc.snu.ac.kr/DICE-Bench/ (snuhcc.github.io/DICE-Bench redirects here)
- **Paper**: DICE-BENCH: Evaluating the Tool-Use Capabilities of Large Language Models in Multi-Round, Multi-Party Dialogues (arXiv 2506.22853), Kyochul Jang et al.
- **Venue**: ACL 2025.
- **Selection reason**: the arXiv 2506.22853 comment states ACL 2025 Vienna; the project page is linked in the abstract. Chosen for the bold graphic banner, the figure carousel band, two-column text with formula and pipeline figure, the multi-tinted link pills and the language switcher.
- **Template credit**: footer says "Page template from NERFies."
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and fonts, the first-viewport screenshot and full-page capture, `static/css/index.css`, `static/js/index.js` (carousel options) and the HTML. Date 2026-10-28.
