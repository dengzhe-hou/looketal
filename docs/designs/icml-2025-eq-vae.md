# Teal Typewriter Pills — Style Reference

> A tidy lab report stamped with a teal monospace logo and a row of fat candy buttons.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the title, authors, affiliations, the four hero buttons, teaser, abstract band, carousel controls, method text, citation box and footer, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the page's inline `<style>` blocks and `static/css/index.css` over Bulma 0.9.1 (Academic Project Page Template). Positions are document coordinates at 1440px wide.

## Overview

EQ-VAE runs on the Academic Project Page Template (Nerfies lineage) and makes three moves that give it its own look. The method name in the title is set in Consolas teal (#008080) while the rest of the 48px title stays Google Sans charcoal. Body text is pushed up to Ubuntu 20px with `!important`, so the whole page reads large and friendly. The hero ends in a row of four oversized fully rounded Bulma buttons, 60px tall with 24px labels: two dark (Code, arXiv), one yellow (Models) and one blue venue button (ICML 2025). A two-panel teaser follows (latent PCA grids on the left, a teal and blue training curve on the right) with a left-aligned 16px caption carrying inline code chips. Then a #f5f5f5 band holds the justified abstract, and a Bulma carousel of latent visualisations with round white arrows and black dots comes next. The method and results sections are white with centered Ubuntu titles, and the page ends in a bordered BibTeX box with a blue Copy button and a #fafafa footer.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): white #ffffff 71.9%, teal grey #75918f 7.3% (title mark, curves, latent images), dark grey #555160 6.5% (title, buttons), pale teal #b4c9c5 5.2% (plot lines and images), off-white #f9fafa 4.1%, sand #ebe5cd 3.6% (Models button and images), remainder 1.4%. No background bands are visible above the fold.

Anatomy in DOM order (y = top of element box):

1. **Title** (`h2.title.is-1.publication-title`), y 48, three centered lines in a 960px box, Google Sans 48px/600, line-height 54px, #363636; the leading "EQ-VAE" is a `span.texttt` in Consolas 48px teal #008080. Gap 31px.
2. **Authors** (`.is-size-4.publication-authors`), y 241, one centered line, Google Sans 24px/700, line-height 36px; names #209cee, superscripts and commas #4a4a4a. Gap 35px (a `<br>`).
3. **Affiliations** (`.is-size-6.publication-authors`), y 306, one centered line, Google Sans 16px/400 #4a4a4a, numbered "1. … | 2. …" with pipe separators. Gap 19px.
4. **Buttons** (`a.external-link.button.is-large.is-rounded`), y 345, 60px tall, centered row: Code (#363636, GitHub icon), arXiv (#363636, Academicons arXiv icon), Models (#ffdd57, question-circle icon, dark text), ICML 2025 (#3298dc, scroll icon). Hero ends at y 470.
5. **Teaser image** (`section.hero.teaser img`), y 470, 960×321, a latent PCA grid (Image, SD-VAE, +Ours, SDXL-VAE, +Ours) beside a gFID training-curve plot. Gap 9px.
6. **Teaser caption** (`h2.subtitle.has-text-left`, inline 1rem), y 800, 960px wide, Google Sans 16px/20px #4a4a4a, left-aligned; bold lead-ins ("Latent Space Structure (Left)"), inline `code` chips in black on #f5f5f5, one #3273dc link. The fold sits just below; the #f5f5f5 abstract band starts at y 908.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Teal Mark | #008080 | `.texttt { color: teal }` | "EQ-VAE" in the title |
| Charcoal | #363636 | Bulma `$text-strong`, `.is-dark` | Title, white-section titles, Code and arXiv button fill |
| Graphite | #4a4a4a | Bulma `$text` | Body text on white, affiliations, teaser caption, footer |
| Light Section Ink | rgba(0,0,0,0.7) | Bulma `.hero.is-light` | Abstract title and text; Models button label |
| Author Sky | #209cee | template `.publication-authors a` | Author names |
| Link Blue | #3273dc | Bulma `$link` | "(See Table)" and footer links |
| Warning Yellow | #ffdd57 | Bulma `.is-warning` | Models button fill |
| Info Blue | #3298dc | Bulma `.is-info` | ICML 2025 button fill |
| Dark Hover | #2f2f2f | Bulma `.is-dark:hover` | Code and arXiv hover fill |
| Yellow Hover | #ffdb4a | Bulma `.is-warning:hover` | Models hover fill |
| Info Hover | #2793da | Bulma `.is-info:hover` | ICML 2025 hover fill |
| Light Band | #f5f5f5 | Bulma `$light`, `.code-container` | Abstract band, inline code chips, BibTeX box |
| Box Border | #dddddd | `.code-container` border | BibTeX box 1px border |
| Copy Blue | #007bff | `.copy-btn` | Copy button fill |
| Copy Hover | #0056b3 | `.copy-btn:hover` | Copy button hover fill |
| Carousel Shadow | rgba(50,50,50,0.1) | bulma-carousel | Arrow and dot shadow |
| Footer Haze | #fafafa | Bulma footer | Footer band |
| Ink | #000000 | `code { color: black !important }`, carousel dots | Inline code text, pagination dots |
| White | #ffffff | page | Page, button labels on dark and blue, carousel arrows |

## Tokens — Typography

- **Body**: `index.css` sets `body { font-family: 'Ubuntu', sans-serif; font-size: 20px !important }`, overriding both the template's Noto Sans rule and an inline 10px rule. Rendered: Ubuntu 400 and 700 from Google Fonts (`fonts_loaded`). Substitute: Ubuntu is free on Google Fonts; if replacing it, use Nunito Sans.
- **Title, authors, teaser**: `'Google Sans', sans-serif` on `.publication-title`, `.publication-authors` and `.teaser`. Rendered: Google Sans 400 only, so the 600 title and 700 authors are synthesized bold. Substitute: Albert Sans.
- **Method mark**: `.texttt { font-family: Consolas }` with no fallback, so it renders as Consolas on Windows and as the browser default font elsewhere. Substitute: Inconsolata (keeps the monospace look on every platform).
- **Inline code**: browser `monospace` at 14px, forced black.
- **Math**: MathJax 3 CHTML.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Paper title | `h2.title.is-1.publication-title` | 48px / 54px | 600 | #363636, mark #008080 |
| Authors | `.is-size-4.publication-authors` (inline 2rem overridden by `is-size-4 !important`) | 24px / 36px | 700 | #209cee |
| Affiliations | `.is-size-6.publication-authors` | 16px / 24px | 400 | #4a4a4a |
| Hero button | `.button.is-large` | 24px / 36px | 400 | white or rgba(0,0,0,0.7) |
| Teaser caption | `h2.subtitle` (inline 1rem) | 16px / 20px | 400, lead-ins 700 | #4a4a4a |
| Section title | `h2.title.is-3` | 32px / 36px | 600 | #363636, rgba(0,0,0,0.7) in the band |
| Carousel column label | `.carousel .title` | 20px / 22.5px | 600 | #363636 |
| Body | `.content p` | 20px / 30px | 400, bold 700 | #4a4a4a or rgba(0,0,0,0.7) |
| Inline code | `code` | 14px | 400 | #000000 on #f5f5f5 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Hero button | 9999px (`is-rounded`) | 1px solid transparent | none |
| Inline code chip | 4px (Bulma `code`) | none | none |
| Carousel arrow | 50% (42px circle) | 1px solid white | `0 2px 5px rgba(50,50,50,0.1)` |
| Carousel dot | 50%, 10px (active 14px) | none | `0 2px 5px rgba(50,50,50,0.1)` |
| BibTeX box (`.code-container`) | 5px | 1px solid #dddddd | none |
| Copy button | 5px | none | none |

## Layout Metrics

- **Container**: Bulma `.container`, 1344px at ≥1408px. The hero column holds a 960px title box at x 240. The teaser container is inline `max-width: 80%; padding: 0 5%`, and its image renders 960px wide.
- **Hero**: Bulma hero-body padding 48px 24px; hero height 470px at 1440px.
- **Teaser**: `.teaser .hero-body` padding 0 top, 48px bottom.
- **Abstract band**: `section.section.hero.is-light`, padding 48px 24px, column `is-three-quarters` (1002px text at x 219), justified.
- **Carousel**: `section.hero.is-small`, full container width (1344px) with arrows at the container edges (x 48 and x 1350); items padding 20px, three images per slide row.
- **Sections**: `section.section` padding 48px 24px; section titles 24px bottom margin; method text in the same 1002px column.
- **Citation**: 960px `.code-container`, padding 10px, `pre` padding-right 170px to clear the Copy button pinned 10px from the top right.
- **Footer**: #fafafa, padding 48px 24px 96px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1408px | container 1344px | 20px | 48px | as described |
| 1216–1407px | container 1152px | 20px | 48px | none |
| 1024–1215px | container 960px | 20px | 48px | none |
| 769–1023px | 24px (hero-body and section padding) | 20px | 48px | container becomes fluid |
| ≤768px | 24px | 20px | 48px (no override in `index.css`) | columns stack; the four 60px buttons wrap onto two or more lines |

## Components

- **Teal method mark**: a `span.texttt` inside the title, Consolas at 1em, color teal (#008080), letter-spacing 0, followed by a colon in the title font.
- **Large rounded button**: `a.external-link.button.is-large.is-rounded`, 60px tall, padding 11px 30px, Ubuntu 24px/400, fully rounded, 1px transparent border, icon left (Font Awesome or Academicons in a Bulma `.icon` span). Variants: `is-dark` #363636 with white label (hover #2f2f2f), `is-warning` #ffdd57 with rgba(0,0,0,0.7) label (hover #ffdb4a), `is-info` #3298dc with white label (hover #2793da). Rows sit with 5px vertical margins and Bulma's 4px-ish spacing between link blocks.
- **Captioned teaser**: a single wide PNG with two panels, followed by a left-aligned 16px caption in which each panel gets a bold lead-in and identifiers appear as black-on-#f5f5f5 code chips.
- **Abstract band**: full-width #f5f5f5 section, centered 32px/600 "Abstract" in rgba(0,0,0,0.7), justified 20px/30px text, bold claims ("×7 speedup"), code chips for model names.
- **Latent carousel**: bulma-carousel, white 42px round arrows with a soft shadow outside the content, black pagination dots below, slides of three columns labelled "Image / SD-VAE / +EQ-VAE" in 20px/600.
- **Citation box**: #f5f5f5 box, 1px #dddddd border, 5px radius, padding 10px, `pre` BibTeX; Copy button #007bff, white 13px system font, padding 5px 10px, 5px radius, hover #0056b3.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title, authors, affiliations | yes | centered Google Sans with a teal Consolas mark |
| Link buttons | yes | four 60px fully rounded Bulma buttons in three colors |
| Venue | present but non-standard | a blue button ("ICML 2025") instead of a text line |
| Teaser figure and caption | yes | two-panel PNG with left-aligned captions |
| Abstract | yes | #f5f5f5 band, justified |
| Carousel | yes | latent visualisations of video frames |
| Method | yes | bold run-in heads ("Motivation"), MathJax, figures |
| Results | yes | figures and tables as images |
| Results table (HTML) | absent from the source | tables are images |
| BibTeX | yes | bordered box with a Copy button |
| Footer | yes | #fafafa template credit |

## Adapting to Other Content

- **More authors**: keep 24px/700 Google Sans names in #209cee on centered lines; at more than six authors, drop to Bulma `is-size-5` (20px) rather than wrapping into three lines.
- **More links**: stay with the large rounded button, but cap colors at three variants (dark, yellow, blue); extra links take the dark variant.
- **A results table**: in a white section, Bulma `table is-fullwidth is-hoverable` at 20px Ubuntu with #363636 header text, model names as black-on-#f5f5f5 code chips, best numbers bold.
- **News**: a short list inside the #f5f5f5 abstract band, above "Abstract", with the date in bold.
- **Long publication lists**: plain list in the 1002px column, titles as #3273dc links.
- **A different method name**: keep one `span` in Consolas teal; only the method name gets the color.

## Do's and Don'ts

- Do color only the method name teal (#008080) and only in the title.
- Do keep body text at 20px Ubuntu; the large size is part of the identity.
- Do use the large (60px) rounded Bulma buttons with icons.
- Do write identifiers as inline code chips in captions and text.
- Don't add more than three button colors.
- Don't center long captions; the teaser caption is left-aligned while titles are centered.
- Don't rely on Consolas alone; give it a monospace fallback outside Windows.

## Surfaces

White page with one #f5f5f5 band for the abstract, #f5f5f5 code chips and BibTeX box, white carousel arrows with soft shadows, and a #fafafa footer.

## Imagery

Grids of PCA-colored latent maps (purple, green, magenta noise textures) beside the source photo, line plots in teal and blue, and reconstruction comparisons. Figures are wide PNGs at container width with no frame.

## Layout

A single centered column: 960px hero and teaser, a 1002px abstract and method column inside a 1344px container, and a full-width carousel. Rendered height about 6,270px at 1440px.

## Agent Prompt Guide

Quick colors: title #363636 with the method name in #008080, body #4a4a4a, authors #209cee, links #3273dc, buttons #363636 / #ffdd57 / #3298dc, band and code #f5f5f5, BibTeX border #dddddd, Copy #007bff, footer #fafafa.

1. "Build a hero: centered Google Sans 48px/600 title in #363636 (line-height 54px) whose first word is a span in Consolas, color #008080; authors 24px/700 #209cee; affiliations 16px #4a4a4a joined by ' | '; then a centered row of 60px fully rounded buttons (padding 11px 30px, Ubuntu 24px, icon left): two #363636 with white text, one #ffdd57 with rgba(0,0,0,0.7) text, one #3298dc with white text."
2. "Add an abstract band: full-width #f5f5f5 section, padding 48px 24px, centered 32px/600 'Abstract' in rgba(0,0,0,0.7), justified Ubuntu 20px/30px text in a three-quarter column, model names as black monospace 14px chips on #f5f5f5 with 4px radius."
3. "Create a citation box: #f5f5f5, 1px solid #dddddd, 5px radius, padding 10px, BibTeX in a `pre`; a Copy button pinned 10px from the top right, #007bff fill, white text, padding 5px 10px, 5px radius, hover #0056b3."

## Similar Pages

- Academic Project Page Template pages (Bulma, Google Sans titles) with dark rounded link buttons.
- Nerfies-lineage pages that switch the body face to a rounder humanist sans.

## Quick Start

```css
:root {
  --title: #363636;
  --mark: #008080;
  --text: #4a4a4a;
  --light-ink: rgba(0, 0, 0, 0.7);
  --author: #209cee;
  --link: #3273dc;
  --btn-dark: #363636;
  --btn-dark-hover: #2f2f2f;
  --btn-yellow: #ffdd57;
  --btn-yellow-hover: #ffdb4a;
  --btn-blue: #3298dc;
  --btn-blue-hover: #2793da;
  --band: #f5f5f5;
  --box-border: #dddddd;
  --copy: #007bff;
  --copy-hover: #0056b3;
  --footer: #fafafa;
  --font-body: 'Ubuntu', sans-serif;
  --font-display: 'Google Sans', 'Albert Sans', sans-serif;
  --font-mark: Consolas, 'Inconsolata', monospace;
  --body-size: 20px;
  --btn-height: 60px;
}
```

## Provenance

- **URL**: https://eq-vae.github.io/
- **Paper**: EQ-VAE: Equivariance Regularized Latent Space for Improved Generative Image Modeling (arXiv 2502.09509), Theodoros Kouzelis, Ioannis Kakogeorgiou, Spyros Gidaris, Nikos Komodakis.
- **Venue**: ICML 2025.
- **Selection reason**: existing verified entry in entries.json; the arXiv 2502.09509 comment says ICML 2025. Chosen for the teal title accent, the row of large varied pill buttons, the well-captioned two-part teaser, the grey abstract band and the latent carousel.
- **Template credit**: footer says the page was built using the Academic Project Page Template (adopted from Nerfies).
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share, targeted computed-style probes of the carousel, text column, citation box and footer, the first-viewport screenshot and scaled full-page capture, the inline `<style>` blocks, `index.css` and the HTML. Date 2026-10-28.
