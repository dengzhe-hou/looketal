# Sky-to-Blush Token Ladder — Style Reference

> A cotton-candy dawn over a lab bench, with a dial that tells the story long or short.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the hero, navigation, buttons, summary box, overview tiles, related-work cards and footer, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the page's own `static/css/index.css` on top of Bulma 0.9.1. Where the stylesheet and the render disagree, the render is reported. Pixel positions are document coordinates at 1440px wide.

## Overview

FlexTok is a Nerfies-family Bulma page that has been given a clear identity. A full-width horizontal gradient from baby blue (#bde0fe) to blush pink (#ffafcc) fills the title band, and a fixed 52px navigation bar sits on top of it in the same gradient at 63% opacity with a 10px backdrop blur, so the band reads as one continuous pastel sheet. The navigation has three Bulma dropdowns (Method, Tokenization, Generation) with blue chevrons. The title is Google Sans 48px/600 in #363636, author names are sky-blue links (#209cee), and four grey Bulma light buttons (#f5f5f5) close the band. Below it a white teaser band holds the token-count figure (1 to 256 tokens) and a justified 18.4px caption. Then a #f5f5f5 section carries the signature interaction, a TL;DR-to-Detailed range slider that swaps the summary text inside a bordered grey box, followed by three white shadowed overview tiles. The rest is a calm white long read in the system sans with diagrams, and it ends with related-work cards and a #fafafa footer. The method name "FlexTok" is set in a separate serif span everywhere it appears.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): white #ffffff 28.8%, pink #ebbfdb 20.1%, pale blue #d6e1f1 19.1%, lavender #d0cae2 10.9%, dark text and image tones #4c433d 10.2%, dusty pink #ddb0c5 7.5%, near-white remainder 3.4%. The gradient band covers the top 433px (48% of the viewport); the rest is the white teaser band with the dog-photo figure.

Anatomy in DOM order (y = top of element box):

1. **Navigation bar** (`nav.navbar.is-fixed-top.glass-overlay`), y 0, height 52px, full width, left-aligned items: Home, Overview, Method ▾, Tokenization ▾, Generation ▾, Conclusions, Related Projects. System sans 16px/400 #4a4a4a, item padding 8px 12px (dropdown triggers 8px 40px 8px 12px to make room for the chevron). Chevrons are #3273dc. Gap to title 8px.
2. **Paper title** (`h1.title.is-1.publication-title`), y 60, two centered lines, Google Sans 48px/600, line-height 54px, #363636, 984px wide box. Gap to authors 24px.
3. **Authors** (`.publication-authors`), y 192, two centered lines, Google Sans 20px/400, line-height 30px; names #209cee, superscript markers (`*1,2`) #4a4a4a. Gap 0.
4. **Affiliations**, y 261, one centered line, Google Sans 20px/400 #4a4a4a with superscript numerals (Apple, EPFL). Gap 10px.
5. **Footnote** (`.publication-footnote`), y 306, "* Equal contribution", system sans 14.4px/400 #4a4a4a, centered. Gap 12px.
6. **Venue line**, y 343, "ICML 2025", Google Sans 20px/600 #4a4a4a, centered. Gap 10px.
7. **Link buttons**, y 383, height 40px, centered row of four: Paper (arXiv icon), Code & weights (GitHub icon), Demo (Hugging Face emoji), Related Projects ▾ (sitemap icon, opens a dropdown). Gap to band edge 10px; band ends at y 433.
8. **Teaser figure** (`section.hero.teaser img`), y 465, 912×343, SVG figure with "1 token … 256 tokens" column labels in a serif. Gap 8px.
9. **Teaser caption** (`h2.subtitle.has-text-justified`), y 816, 912px wide, Google Sans 18.4px/400, line-height 23px, #4a4a4a, justified, padding 16px 0 8px; "FlexTok" in the serif `.dmethod` span. The fold cuts through this paragraph.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Baby Blue | #bde0fe | `.headline` gradient start | Title band left edge; nav bar left edge at alpha 0.627 |
| Blush Pink | #ffafcc | `.headline` gradient end | Title band right edge; nav bar right edge at alpha 0.627 |
| Graphite | #4a4a4a | Bulma `$text` | Body text, nav items, affiliations, venue line, teaser caption, footer |
| Charcoal Title | #363636 | Bulma `$text-strong` | Paper title (h1), section titles and h2.is-4 subsection titles on white sections |
| Light Section Ink | rgba(0,0,0,0.7) | Bulma `.hero.is-light` color | "Summary" and "Overview" titles, summary text, overview tile text, link-button labels |
| Author Sky | #209cee | `hsl(204,86%,53%)`, `.dlink` | Author names, related-card titles, related-mini titles |
| Sky Hover | #1086d5 | `hsl(204,86%,45%)` | Related-card title hover, related tag text |
| Bulma Link Blue | #3273dc | Bulma `$link` | Inline body links (TiTok, ElasticTok, LlamaGen), nav dropdown chevrons |
| Light Grey | #f5f5f5 | Bulma `$light` | Link buttons, Summary/Overview section band, summary text box, inline code background |
| Box Border | #dbdbdb | Bulma `$border` | Summary text box 1px border, slider track |
| Card Hairline | #e6e6e6 | literal | Related mini-card border, related-projects dropdown border |
| Media Frame | #e2e2e2 | literal | Related-card media frame border |
| Carousel Edge | #bbbbbb | literal | Results-carousel item border |
| Button Hover | #eeeeee | Bulma `.button.is-light:hover` | Link-button fill on hover |
| Venue Grey | #888888 | literal | Venue text on related cards |
| Shadow Ink | rgba(10,10,10,0.1) | Bulma `$shadow` | Overview tile shadow (with a 0.02 alpha 1px ring) |
| Footer Haze | #fafafa | Bulma footer | Footer band |
| Code Red | #da1039 | Bulma `$code` | Inline `<code>` tokens such as [SOI] |
| White | #ffffff | literal | Page, teaser band, overview tiles, related cards, dropdown menus |

## Tokens — Typography

- **Display**: declared `'Google Sans', sans-serif` on `.publication-title`, `.publication-authors` and `.teaser`. Rendered: Google Sans, but only the 400 face loaded (`fonts_loaded`: Google Sans 400), so the 600 title and venue line are browser-synthesized bold. Substitute: Albert Sans (similar round geometric proportions, real 600 weight).
- **Body**: Bulma system stack `BlinkMacSystemFont, -apple-system, "Segoe UI", Roboto, …`. Rendered as Segoe UI on Windows and San Francisco on macOS. Substitute: Inter.
- **Method name**: `.dmethod` declares `'American Typewriter', serif` at 1em. American Typewriter ships only with macOS, so on Windows and Linux the render falls back to the default serif (Times New Roman here). Substitute: Courier Prime if you want the typewriter look everywhere, or keep the serif fallback deliberately.
- **Icons**: Font Awesome 5.15.3 (Free 900 and Brands 400) and Academicons, both loaded.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title` | 48px / 54px | 600 | #363636 |
| Authors, affiliations | `.publication-authors` | 20px / 30px | 400 | #209cee names, #4a4a4a rest |
| Venue line | `.is-size-5.has-text-weight-semibold.publication-title` | 20px / 30px | 600 | #4a4a4a |
| Teaser caption | `h2.subtitle.has-text-justified` | 18.4px / 23px | 400 | #4a4a4a |
| Section title | `h2.title.is-3` | 32px / 36px | 600 | rgba(0,0,0,0.7) on the light band, #363636 on white |
| Subsection / tile title | `h2.title.is-4`, `p.title.is-4` | 24px / 27px | 600 | #363636 (white), rgba(0,0,0,0.7) (tiles) |
| Related-card title | `.related-card-title` | 21.6px (1.35rem) / 1.25 | 700 | #209cee |
| Body | `.content p` | 16px / 24px | 400 | #4a4a4a or rgba(0,0,0,0.7) |
| Footnote | `.publication-footnote` | 14.4px / 21.6px | 400 | #4a4a4a |
| Nav dropdown item | `.navbar-dropdown .navbar-item` | 14px / 21px | 400 | #4a4a4a |
| Inline code | `code` | 14px monospace | 400 | #da1039 on #f5f5f5 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link button (`.button.is-light`) | 4px | 1px solid transparent | none |
| Summary text box (`#sentenceDisplay`) | 10px | 1px solid #dbdbdb | none |
| Overview tile (`a.tile.box`) | 6px | none | `0 8px 16px -2px rgba(10,10,10,0.1), 0 0 0 1px rgba(10,10,10,0.02)` |
| Related card (`.related-card`) | 12px | none | `0 2px 10px rgba(0,0,0,0.06)`; hover `0 8px 22px rgba(0,0,0,0.12)` and translateY(-3px) |
| Related mini-card (`.related-mini`) | 10px | 1px solid #e6e6e6 | `0 2px 10px rgba(0,0,0,0.05)`; same hover |
| Related-projects dropdown | 8px | 1px solid #e6e6e6 | `0 6px 20px rgba(0,0,0,0.15)` |
| Nav dropdown (`.navbar-dropdown.is-boxed`) | 6px | none | Bulma boxed dropdown shadow |
| Results carousel item | 10px | 1px solid #bbbbbb | none |

## Layout Metrics

- **Container**: Bulma `.container.is-max-desktop`, `max-width: 960px` at viewports ≥1024px, centered. In the hero, `.has-text-centered { padding: 0 }` removes the column padding, so the title box is 984px (the column's negative margins show). Body sections place content at x 240–1200 at 1440px.
- **Title band**: `section.hero.headline`, height 433px at 1440px; Bulma hero-body padding 48px 24px plus `.headline-container` padding-top 24px; title starts at y 60 under the fixed nav.
- **Teaser band**: `.teaser .hero-body` padding 32px top and bottom, 24px sides, so the figure and caption are 912px wide.
- **Sections**: `section.section` padding 48px 24px. Section title margin-bottom 24px.
- **Summary column**: `.column.is-four-fifths` inside the 960px container, so the slider row and the text box are 763px wide.
- **Overview tiles**: three `.tile.is-parent` columns, each tile 304px wide with 24px gaps, 218px tall, padding 20px.
- **Figures**: full-width figures fill 960px; `.flextok-train-tok-figure` has 10% side margins (768px), `.flextok-train-ar-figure` 30% side margins (384px).
- **Related projects**: two featured cards at 468px each with a 24px gap, then mini-cards at 304px in rows of three.
- **Footer**: padding 48px 24px 96px, #fafafa.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1408px | container 960px centered | 16px | 48px | as described |
| 1024–1407px | container 960px centered | 16px | 48px | none |
| 769–1023px | 24px (hero-body and section padding) | 16px | 48px | navbar collapses to the burger; container becomes fluid |
| ≤768px | 24px | 16px | 32px (`.title.is-1 { font-size: 2rem }`) | authors and venue drop to 0.9em; link buttons wrap with a 10px gap, 14px text, 10px padding; sections padding 24px vertical; TL;DR/Detailed labels move under the slider; slider labels 11.2px; training figures go full width; mini-card thumbnails hidden |

## Components

- **Glass navigation bar**: `nav.navbar.is-fixed-top`, height 52px, background `linear-gradient(to right, #bde0fea0, #ffafcca0)` with `backdrop-filter: blur(10px)`. Items system sans 16px/400 #4a4a4a, padding 8px 12px; hover keeps the background transparent (`!important` override). Dropdown triggers carry Bulma's #3273dc chevron on the right; menus are white boxed dropdowns with 14px items, padding 6px 48px 6px 16px.
- **Link button**: `a.external-link.button.is-normal.is-light`, height 40px, padding 7px 16px, background #f5f5f5, label rgba(0,0,0,0.7) system sans 16px/400, 4px radius, 1px transparent border, icon left (Font Awesome or Academicons in a Bulma `.icon` span). Bulma hover darkens the fill to #eeeeee. The row sits with 10px top margin and a -30px bottom margin hack on desktop.
- **Related Projects dropdown button**: same recipe as the link button plus a caret; on hover or focus a 220px white menu opens below, 8px radius, 1px #e6e6e6 border, `0 6px 20px rgba(0,0,0,0.15)`. Items padding 9px 16px, 16px/600 in `hsl(204,86%,40%)`, hover background `hsl(204,86%,96%)`.
- **Length slider summary**: a row of "TL;DR" (bold) | slider | "Detailed" (bold), with five token labels (21, 50, 117, 180, 292 tokens) spaced across the top in 16px rgba(0,0,0,0.7). The `bulma-slider` range input is full width with a #dbdbdb track and a white round thumb, default at the Detailed end. Below, `#sentenceDisplay` is a #f5f5f5 box with 1px #dbdbdb border, 10px radius, padding 16px, justified 16px/24px text, `transition: all 0.3s ease` as the text swaps.
- **Overview tile**: `a.tile.is-child.box`, white, 6px radius, padding 20px, Bulma box shadow, centered `p.title.is-4` 24px/600 then a 16px/24px description in rgba(0,0,0,0.7). Whole tile is an anchor to the matching section.
- **Method-name span**: `.dmethod` wraps every "FlexTok" in a serif (American Typewriter where present) at the surrounding size, so the name reads like a typeset product mark.
- **Related card**: `.related-card`, white, 12px radius, padding 20px, `0 2px 10px rgba(0,0,0,0.06)`; title 1.35rem/700 #209cee with underline on hover; media frame at 12:5 with 1px #e2e2e2 border and 8px radius; a small outlined tag (1px #209cee border, 4px radius, 0.66rem/700) beside a #888888 venue.
- **Footer**: #fafafa band, centered 16px #4a4a4a text crediting the Nerfies template.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky navigation with dropdowns | yes | glass gradient bar, 52px, three Bulma boxed dropdowns |
| Title, authors, affiliations, venue | yes | centered on the blue-to-pink band, Google Sans |
| Link buttons | yes | four Bulma light buttons, one opening a related-projects menu |
| Teaser figure and caption | yes | 912px SVG figure, justified 18.4px caption |
| Abstract | present but non-standard | replaced by the five-step length slider over a grey text box |
| Overview / jump cards | yes | three white Bulma box tiles linking to sections |
| Method figures | yes | centered figures at 100%, 80% or 40% width |
| Interactive explorer | yes | FSQ first-token explorer with range sliders beside an image grid |
| Video | yes | one video plus a results carousel (10px radius, #bbbbbb border) |
| Results table | absent from the source | figures carry the quantitative results |
| Related projects | yes | featured cards and mini-cards with hover lift |
| BibTeX | yes | Bulma `pre` with a copy button pinned top right |
| Footer | yes | #fafafa template credit |

## Adapting to Other Content

- **More authors**: keep the centered 20px Google Sans lines and break with `<br>` every five names, as the source does; the band grows downward and the gradient stretches with it.
- **A results table**: put it in a white `section.section` inside the 960px container, Bulma `table is-fullwidth is-striped` with 16px text, header #363636 600, and highlight the best row with the #f5f5f5 fill rather than a new color.
- **Long publication or related-work lists**: reuse the mini-card grid (304px, 1px #e6e6e6 border, 10px radius) in rows of three; it already collapses to a stacked list without thumbnails on phones.
- **News or updates**: a short list inside the #f5f5f5 band above Summary, 16px text, dates in 600 weight; avoid adding another gradient.
- **No interactive summary**: fall back to a plain abstract in the same #f5f5f5 box with 1px #dbdbdb border and 10px radius so the band keeps its focal object.

## Do's and Don'ts

- Do run the #bde0fe → #ffafcc gradient left to right across the full width, and repeat it at 0.627 alpha with blur in the fixed nav.
- Do keep author names #209cee and inline body links #3273dc; the two blues are distinct on the page.
- Do set the method name in its own serif span every time it appears.
- Do use Bulma light buttons (#f5f5f5, 4px radius) rather than dark pills on the pastel band.
- Don't add color to section backgrounds beyond #f5f5f5 and #fafafa; the pastel belongs to the header only.
- Don't use the gradient behind body text or figures.
- Don't rely on American Typewriter being present; decide on the fallback.

## Surfaces

Three levels. The pastel gradient title band (and its translucent copy in the nav), white for the teaser and long-read sections, and #f5f5f5 for the Summary/Overview band, the link buttons and the summary text box. Raised surfaces are white tiles and cards with soft shadows. The footer is #fafafa.

## Imagery

Vector diagrams with mint and cyan blocks (encoder, quantization, decoder), grids of dog photographs reconstructed at increasing token counts, generation grids, and an interactive image grid. Figures sit on white without frames; carousel items get a 10px radius and #bbbbbb border.

## Layout

A single 960px centered column under a fixed nav. The header band is full width; everything else is constrained. The order is title band, teaser, grey Summary/Overview band, then long white sections with h2.is-3 titles and h2.is-4 subsections, related projects, BibTeX and footer. Total rendered height is about 13,750px at 1440px.

## Agent Prompt Guide

Quick colors: band gradient #bde0fe → #ffafcc, text #4a4a4a, title #363636, authors #209cee, body links #3273dc, light surfaces #f5f5f5 with #dbdbdb border, footer #fafafa, inline code #da1039.

1. "Build a title band: full-width section with `background: linear-gradient(to right, #bde0fe, #ffafcc)`, padding 48px 24px; centered title in Google Sans 48px/600, line-height 54px, #363636; authors Google Sans 20px/400 with #209cee name links; venue line 20px/600 #4a4a4a; a row of light buttons (#f5f5f5, 4px radius, padding 7px 16px, 40px tall, rgba(0,0,0,0.7) 16px labels, icon left). Fix a 52px nav on top with the same gradient at alpha 0.627 and `backdrop-filter: blur(10px)`."
2. "Create a length-slider summary: a 763px column with bold 'TL;DR' and 'Detailed' at the ends of a full-width range input (#dbdbdb track, white round thumb), five token-count labels above in 16px rgba(0,0,0,0.7); below, a #f5f5f5 box with 1px solid #dbdbdb border, 10px radius, padding 16px, justified 16px/24px text that swaps with `transition: all 0.3s ease`."
3. "Add three overview tiles: white anchors, 304px wide with 24px gaps, padding 20px, 6px radius, shadow `0 8px 16px -2px rgba(10,10,10,0.1), 0 0 0 1px rgba(10,10,10,0.02)`; centered 24px/600 title and 16px/24px description in rgba(0,0,0,0.7), on a #f5f5f5 section band."

## Similar Pages

- Nerfies-template pages (Bulma 0.9 with Google Sans titles), here recolored with a pastel gradient header.
- Pages from the same EPFL VILAB group (4M, related FlexTok follow-ups) that reuse the glass navigation and related-project cards.

## Quick Start

```css
:root {
  --band-start: #bde0fe;
  --band-end: #ffafcc;
  --nav-bg: linear-gradient(to right, #bde0fea0, #ffafcca0);
  --text: #4a4a4a;
  --title: #363636;
  --light-ink: rgba(0, 0, 0, 0.7);
  --author: #209cee;
  --author-hover: #1086d5;
  --link: #3273dc;
  --light: #f5f5f5;
  --border: #dbdbdb;
  --hairline: #e6e6e6;
  --footer: #fafafa;
  --code: #da1039;
  --font-display: 'Google Sans', 'Albert Sans', sans-serif;
  --font-body: BlinkMacSystemFont, -apple-system, 'Segoe UI', Roboto, sans-serif;
  --font-method: 'American Typewriter', serif;
  --container: 960px;
  --nav-h: 52px;
  --radius-button: 4px;
  --radius-box: 10px;
  --radius-tile: 6px;
  --radius-card: 12px;
}
```

## Provenance

- **URL**: https://flextok.epfl.ch/
- **Paper**: FlexTok: Resampling Images into 1D Token Sequences of Flexible Length (arXiv 2502.13967), Roman Bachmann, Jesse Allardice, David Mizrahi et al. (Apple, EPFL).
- **Venue**: ICML 2025.
- **Selection reason**: the arXiv 2502.13967 comment states acceptance at ICML 2025 and links the project page. Chosen for the pastel gradient header with sticky dropdown navigation, the token-count teaser, the TL;DR-to-detailed slider and the overview cards.
- **Template credit**: footer credits the Nerfies website template; the gradient, glass nav, slider summary and related-card styles are the authors' own (`static/css/index.css`).
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share, targeted computed-style probes of the summary box, tiles, cards and footer, the first-viewport screenshot and scaled full-page capture, `index.css`, `index.js` and the HTML. Date 2026-10-28.
