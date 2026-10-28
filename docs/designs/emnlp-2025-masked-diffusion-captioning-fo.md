# Masked Diffusion Captioning — Style Reference

> A grey gallery wall with one framed print: a quiet Poppins caption on the left, a glowing diagram on the right, and Charter prose waiting below.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and top-of-page tall screenshots, and the page's own `assets/stylesheets/main_free.css`, `clarity/clarity.css`, `assets/scripts/navbar.js` and `index.html`. The page is built on Shikun Liu's Clarity template. `main_free.css` declares its type scale twice; the second block (from about line 1260) wins in the cascade, so the title renders at weight 400 and section headings at 600 rather than the 500/700 of the first block. The hero grey is an inline `style="background-color: #E0E4E6"` on `#first-content`, not a template value.

## Overview

A long, quiet single-column article page on white. The top is a full-width cool-grey band (#e0e4e6) split into two equal columns: on the left a light 30px Poppins title, italic author and affiliation lines, a TL;DR paragraph, two translucent uppercase buttons and an uppercase venue line; on the right the method teaser image with a blurred copy of itself behind it, which throws a soft coloured glow. Below the band the body narrows to a 749px column with Poppins section headings and 18px Charter text in light dark grey (#353535). Full-bleed #f6f6f6 bands carry figures and captions, a three-dot slideshow shows result images, MathJax renders formulas in Gyre Pagella, and the page ends with a Fira Code BibTeX well and a #fafafa footer. There is no colour accent at all: hierarchy comes from typeface changes (Poppins vs Charter), weight and band colour.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): hero grey #e0e4e6 43.3%, white #ffffff 39.1%, mid grey #c4c5c6 8.8% (text antialiasing and the blurred teaser glow), #e3e7e9 3.2%, #f6f6f2 2.4%, #e3e5e4 1.7%, pale blue #d5ebf7 0.9% (teaser boxes), #fffff9 0.6%.

Anatomy in DOM order (desktop 1440px; the hero container has 216px side padding = 15vw and 54px top padding = 6vh; `.blog-intro` adds 45px = 5vh top padding; the two grid columns are 475px wide with a 57.6px = 4vw gap):

1. **Contents widget** (`.nav-container`, fixed at left 20px, top 5%): injected by `navbar.js`, opacity 0 until the reader scrolls; its collapse button sits at x=62, y=57 but is invisible in the first viewport.
2. **Title** (`h1.title`, y=99, x=216, 475px wide): Poppins 30px / 400 / line-height 36px, #353535, left aligned, wraps to two lines; padding-bottom 9px (1vh). Gap 0.
3. **Authors** (`p.author`, y=180): Poppins 15.3px (85%) italic 400, line-height 18.36px, #353535; names are links with no underline; superscript affiliation numbers at 0.65em. Padding 4px 0 10px.
4. **Affiliations** (second `p.author`, y=217): same style, one institution per line with superscript numbers, padding-top 0, padding-bottom 10px.
5. **TL;DR** (`p.abstract`, y=282): Poppins 15.3px / 400 / line-height 24.48px (1.6), #353535, padding 9px 0, starts with the plain text "TL;DR:". 
6. **Buttons** (`.info a.button.icon`, y=373, 35px tall): PAPER and CODE, 18px apart (two `&nbsp;`). Margin-bottom 10px.
7. **Venue line** (`.info p`, y=418): "EMNLP 2025 (FINDINGS)", Poppins 15.3px / 500 uppercase, letter-spacing 1px, #353535, padding-top 10px.
8. **Teaser** (`.blog-cover`, right column): the image renders 428×222 at x=796, y=164, vertically centred against the text column; a second copy (`img.background`) is stacked under it with `filter: blur(24px)`, giving the green/purple halo.

The grey band ends at about y=496. The Abstract heading (`h1`, 26px/600) starts at y=550 after the `.first` margin-top 36px (4vh) and the `.main` top padding 18px (2vh); the abstract text begins at y=600.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Hero Grey | #e0e4e6 | (inline style on `#first-content`) | full-width hero band behind title and teaser |
| Ink | #353535 | (literal) | title, authors, TL;DR, buttons text, venue line, section headings, body text, selection background |
| Paper | #ffffff | (body) | page background, text sections |
| Band Grey | #f6f6f6 | (`.container.blog.gray`) | full-bleed figure bands (method figure, slideshow, plots) |
| Footer Grey | #fafafa | (`footer`) | footer band, BibTeX code well background |
| Glass White | rgba(255,255,255,0.2) | (inline on `.button`) | PAPER / CODE button fill on the hero grey |
| Code Border | #c6c6c6 | (rendered on `code.hljs`) | 1px border of the BibTeX well |
| Dot Grey | #c6c6c6 | (`.slide-menu .dots .dot`) | inactive slideshow dots |
| Dot Rose | #e2a3a3 | (`.dot.active`) | active slideshow dot |
| Code Text | #000000 | (rendered on `code.hljs`) | BibTeX text |
| Nav Glass | rgba(255,255,255,0.5) | (`navbar.js`) | floating contents widget, once visible |
| Nav Muted | #666666 | (`navbar.js`) | contents links; active link #000000 / 500 |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display / UI | "Poppins", serif (headings, hero), "Poppins", sans-serif (buttons) | Poppins 300, 400, 400 italic, 500, 600 from Google Fonts | Montserrat |
| Body | "Charter", sans-serif on `p.text` | Charter regular and italic (self-hosted woff2) | Bitstream Charter / XCharter |
| Code | "Fira Code", monospace | Fira Code 400 | JetBrains Mono |
| Math | MathJax 2.7.1 HTML-CSS, Gyre Pagella | GyrePagellaMathJax family | — |
| Icons | Font Awesome 6 Free | Font Awesome 6 Free 900 (solid) | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.title` | 30px / 400 / 36px | #353535 |
| Authors, affiliations | `.blog-intro p.author` | 85% = 15.3px / 400 italic / 1.2 | #353535 |
| TL;DR | `.blog-intro p.abstract` | 85% = 15.3px / 400 / 1.6 | #353535 |
| Venue line | `.blog-intro .info p` | 85% = 15.3px / 500 uppercase, letter-spacing 1px | #353535 |
| Button | `.button` | 0.65em = 11.7px / 500 uppercase, letter-spacing 0.075em = 0.8775px | #353535 |
| Section heading | `.container.blog h1` | 26px / 600 / 1.2, padding 9px 0 | #353535 |
| Subsection | `h2` | 20px / 600 / 1.2, padding 9px 0 | #353535 |
| Body | `.container.blog p.text` | Charter 18px / 300 (renders as regular) / 27px | #353535 |
| Caption | `.container.blog p.caption` | Poppins 70% = 12.6px / 400 / 1.2; `b` 600 | #353535 |
| BibTeX | `pre code` | Fira Code 13.5px / 300 / 20.25px | #000000 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow / filter |
|---|---|---|---|
| Hero buttons | 10px | none | none; hover `opacity: 0.8`, active `opacity: 0.5` |
| Teaser glow copy | 0 | none | `filter: blur(24px)` on `img.background` |
| BibTeX well | 10px | 1px solid rgb(198,198,198) | none |
| Slideshow dots | 50%, 10×10px, margin 15px | none | hover `transform: scale(1.4)`; active also scale(1.4) |
| Contents widget | 16px | none | `backdrop-filter: blur(10px)` |
| Figures, bands | 0 | none | none |

## Layout Metrics

- **Container**: `.container` padding-left 15vw and padding-right calc(15vw - scrollbar) at ≥1200px, so the hero content spans x=216 to 1224 (1008px).
- **Hero**: `#first-content` padding-top 6vh = 54px; `.blog-title` grid `1fr 1fr`, column-gap 4vw = 57.6px, two 475px columns; `.blog-intro` padding 5vh 0 = 45px; `.blog-cover` padding 5vh 0, flex, centred vertically, justified to the right. Rendered hero height about 496px.
- **Text sections**: `.container.blog.main` padding 2vh 24vw = 18px 345.6px, giving a 749px measure at x=346. `.first` adds margin-top 4vh = 36px.
- **Wider bands**: `.large` 2vh 16vw, `.extra-large` and `.extra-extra-large` 2vh 12vw (the slideshow band is `.extra-large`, 1008px wide). Images inside bands are sized inline (40%, 60%, 70%, 80% of the column).
- **Grids**: `.columns-2` to `.columns-12` with column-gap 2vw = 28.8px.
- **Footer**: padding 4vh 0 = 36px, #fafafa, rendered 99px tall.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥2400px | 24vw | 20px | 36px | — |
| ≥1600px | 18vw; text column 38vw sides | 18px | 36px | footer padding 5vh |
| ≥1200px (1440 renders this) | 15vw = 216px; text column 24vw = 346px | 18px | 30px | hero two columns 1fr 1fr, gap 4vw |
| ≥992px | 12vw | 16px | 26px | hero single column (cover below intro) |
| ≥769px | 8.5vw | 16px | 26px | — |
| <769px | 6vw | 15px | 26px | `.columns-2` → 1 column; `.columns-12` → 3; contents widget becomes a full-width top bar (rgba(255,255,255,0.5), blur) |

## Components

- **Translucent hero button** (`a.button.icon`): inline-flex, background rgba(255,255,255,0.2) over #e0e4e6 (reads as a barely lighter chip), radius 10px, padding 0.75em 1em = 8.775px 11.7px, Poppins 11.7px / 500 uppercase, letter-spacing 0.8775px, #353535, no border, no shadow. Font Awesome solid icon on the right (book-open for Paper, code for Code) at 1.2em with 0.5em left padding. Hover opacity 0.8.
- **Glow teaser** (`.blog-cover`): two identical `<img>` elements; the front one at z-index 2, the back one absolutely positioned at z-index 1 with `filter: blur(24px)` so the figure's own colours bleed around it.
- **Venue line**: plain paragraph in uppercase Poppins 15.3px / 500 with 1px tracking, sitting under the buttons; no pill or badge.
- **Grey figure band** (`.container.blog.main.gray`): full-bleed #f6f6f6, inner column 749px, image at an inline width, caption in Poppins 12.6px with a bold lead sentence.
- **Slideshow** (`.slide-menu` + `.slide-content`): three 10px dots centred above the slides, #c6c6c6 with the active one #e2a3a3 and scaled 1.4; slides toggle `display`.
- **BibTeX** (`pre code.plaintext`): Fira Code 13.5px / 300, #000000 on #fafafa, 1px #c6c6c6 border, radius 10px, padding 13.5px 21.6px, under an `h1` "Citation".
- **Floating contents** (`.nav-container`, from `navbar.js`): fixed at left 20px, 300px wide, padding 15px, radius 16px, rgba(255,255,255,0.5) with `backdrop-filter: blur(10px)`; Poppins 14px links in #666666, sub-items 12px with 15px indent, active link #000000 / 500; fades in (1.3s) after the hero scrolls away and can collapse to a 50px chip.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Split hero (text + teaser) | yes | #e0e4e6 band, 1fr 1fr grid, blurred-copy glow behind the teaser |
| Title / authors / affiliations | yes | Poppins 30px / 400 title; italic 15.3px author lines |
| TL;DR | yes | plain 15.3px Poppins paragraph prefixed "TL;DR:" |
| Link buttons | yes | two translucent uppercase chips with Font Awesome icons |
| Venue | yes | uppercase tracked line, no badge |
| Abstract | yes | `h1` "Abstract" + Charter 18px paragraph in the 749px column |
| Method figure | yes | full-bleed #f6f6f6 band with Poppins caption |
| Results slideshow | yes | three-dot switcher in a wider grey band |
| Plots and ablations | yes | images at 40–80% width, alternating white and grey bands |
| Math | yes | MathJax with Gyre Pagella |
| Floating contents | present but non-standard | hidden until scroll; glass panel at the left edge |
| Results tables | absent from the source | table rules exist in the CSS (zebra #ececec rows) but no table renders |
| Video | absent from the source | — |
| BibTeX | yes | Fira Code well with 10px radius |
| Footer | yes | #fafafa band with template credit |

## Adapting to Other Content

- **More authors**: keep them in the left hero column at 15.3px italic; the 475px column wraps a long list onto more lines, so keep affiliations as one per line beneath.
- **A results table**: use the template's declared table style inside the 749px column: Poppins 85% of 18px = 15.3px cells, zebra rows #ececec, thead weight 500, no vertical rules. Keep it in a #f6f6f6 band only if it is a figure-like summary.
- **No teaser image**: switch `.blog-title` to `.no-cover` (single column, intro padded 6vh 9vw) instead of leaving the right column empty.
- **Long publication or news lists**: set them as Charter 18px list items in the 749px column with Poppins 20px / 600 `h2` year headings; do not add cards.
- **Extra links** (slides, demo): add more `.button.icon` chips on the same row, 18px apart, same rgba(255,255,255,0.2) fill.

## Do's and Don'ts

- Do keep the hero band a single flat cool grey and the body white; alternate full-bleed #f6f6f6 bands only for figures.
- Do pair Poppins (title, headings, captions, UI) with Charter (running text); the contrast between them is the design.
- Do keep the title light (400) at 30px; weight comes from the 600 section headings, not the title.
- Do give the teaser the blurred duplicate behind it; it is the only colour effect on the page.
- Don't introduce a brand accent; every text colour is #353535 except the BibTeX black and the #666666 contents links; the rose active dot is the only tint.
- Don't add borders or shadows to buttons or figures.
- Don't widen the reading column past 749px at 1440.

## Surfaces

Three flat greys and white: hero #e0e4e6, figure bands #f6f6f6, footer and code well #fafafa, everything else #ffffff. The only non-flat surfaces are the blurred teaser copy and the glass contents panel.

## Imagery

Method diagrams and plots exported from the paper (pastel blue and yellow boxes, purple bar charts) placed as plain images without frames; the teaser carries a blur halo. Result images sit in two-column grids inside the slideshow. No photography or decorative art beyond the paper figures.

## Layout

Two-column hero, then a narrow centred reading column (24vw side padding) broken by full-bleed grey figure bands; sections are separated by heading padding and band changes rather than rules. About 6,400px tall.

## Agent Prompt Guide

Quick colors: hero #e0e4e6, page #ffffff, figure band #f6f6f6, footer #fafafa, ink #353535, code border #c6c6c6, active dot #e2a3a3.

1. "Build a split hero: full-width #e0e4e6 band, padding 54px 216px 0, grid 1fr 1fr with a 57.6px gap. Left: Poppins 30px / 400 #353535 title, italic 15.3px author and affiliation lines, a 15.3px / 400 TL;DR paragraph at line-height 1.6, then uppercase buttons and a 15.3px / 500 uppercase venue line with 1px tracking. Right: the teaser image with an identical copy behind it using filter: blur(24px)."
2. "Create a translucent button: background rgba(255,255,255,0.2), radius 10px, padding 8.775px 11.7px, Poppins 11.7px / 500 uppercase, letter-spacing 0.8775px, color #353535, Font Awesome solid icon on the right with 0.5em left padding; hover opacity 0.8."
3. "Lay out a text section: padding 18px 345.6px (24vw), Poppins 26px / 600 #353535 heading with 9px vertical padding, Charter 18px / line-height 27px #353535 paragraphs; place figures in a full-bleed #f6f6f6 band with a Poppins 12.6px caption whose lead sentence is weight 600."

## Similar Pages

- Other Clarity-template project pages (Shikun Liu's template) with a coloured `#first-content` band and blurred teaser.
- Editorial ML blogs that pair a geometric sans heading face with a book serif body.

## Quick Start

```css
:root {
  --hero-bg: #e0e4e6;
  --bg: #ffffff;
  --band: #f6f6f6;
  --footer: #fafafa;
  --ink: #353535;
  --code-border: #c6c6c6;
  --dot-active: #e2a3a3;
  --btn-fill: rgba(255, 255, 255, 0.2);
  --font-display: "Poppins", sans-serif;
  --font-body: "Charter", "XCharter", Georgia, serif;
  --font-mono: "Fira Code", monospace;
  --radius: 10px;
  --gutter: 15vw;
  --text-gutter: 24vw;
}
```

## Provenance

- **URL**: https://cfeng16.github.io/mdlm4vfl/
- **Paper**: Masked Diffusion Captioning for Visual Feature Learning (arXiv 2510.26799), Chao Feng, Zihao Wei, Andrew Owens.
- **Venue**: EMNLP 2025 Findings.
- **Selection reason**: the arXiv comment states acceptance at EMNLP 2025 Findings and links this project page.
- **Template credit**: footer reads "This website is built on the Clarity Template, designed by Shikun Liu".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and tall screenshots, and `main_free.css`, `clarity.css`, `navbar.js` and `index.html` read directly, on 2026-10-28.
