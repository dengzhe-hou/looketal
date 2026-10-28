# CrossMAE — Style Reference

> A clean lab poster pinned to a white wall: a rounded wordmark, three big black icons, and figures that do all the talking.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of the rendered elements, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's own `style.css?v=v2` and `index.html` (which sets the wordmark and icon sizes inline). Font Awesome 4.7 and Google Fonts (Open Sans, Varela Round) are the only external styles. The credit line says the design is adapted from the NeRF, DeepMotionEditing and related pages. There is no dark mode.

## Overview

A short (4,000px), centred, figure-first page on plain white in the classic "icon-link" academic layout. A 980px column holds everything. The wordmark "CrossMAE" is set in Varela Round 50px (synthesised bold) in mid grey #4d4d4d, with the full title below in Open Sans 27px regular-weight grey with 1px tracking. Authors sit in two underlined rows on a float grid (five 20% cells, then four 25% cells), followed by an affiliation/notes row. Three large black Font Awesome 4 icons (file, GitHub, graduation cap) at 50–55px with bold 14px labels act as the links. A one-line bold "TL;DR:" statement leads to a 784px annotated teaser (a pale blue panel holding input and masked image, attention maps, reconstructions and stats, all inside the image). The rest is a sequence of centred 24px section titles ("Overview", "Cross-Attention, Partial Masking, and Inter-block Attention", "Visualizations") with 784px diagrams, left-aligned 16px paragraphs with bold key sentences, a dense two-up grid of reconstruction visualisations, and a #eaeaea rounded citation box. Text is #333333 throughout; links are not colored.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 75.4% plus #fdffff / #fffffd 1.2%; deep plum #472a3e 7.6% (the purple attention-map backgrounds in the teaser); brown #6c5844 5.0% (the fox photographs); greys #d7d8d6 4.6% and #b1b1ae 4.2% (text anti-aliasing, the masked-input grey); pale blue-grey #f0f2f3 2.0% (the teaser's input panel).

Anatomy in DOM order (desktop 1440px, everything centred in `.container`, max-width 980px at x=230; `.section` adds 30px side margins):

1. **Wordmark** (`h1.title.main-title`, y=20, 50px line): "CrossMAE", Varela Round 50px/700 (inline style; only the 400 face loads, so the bold is synthesised), letter-spacing 1px, #4d4d4d. The `.title-row` margin of 20px sets the top.
2. **Full title** (`h1.title.main-title`, y=70, 50px line): Open Sans 27px/400, letter-spacing 1px, #4d4d4d; `.title-row` margin-bottom 20px.
3. **Author rows** (`.author-row`, y=140 and y=165, 25px each, max-width 700px): Open Sans 16px #333333 underlined names, 10px superscripts (1*, 1, 1,2†, 1†); first row five cells of 20%, second row four cells of 25%.
4. **Affiliation row** (`.affiliation-row`, y=190, 25px, max-width 650px): four 25% cells, 16px: "¹UC Berkeley", "²UCSF", "*Equal Contribution", "†Equal Advising".
5. **Icon links** (`.link-labels`, y=220, 500px wide, three 33.3% cells): Font Awesome 4 file-text 50px, GitHub 55px and graduation-cap 55px, #333333, line-height 100px; the anchors have -14px bottom margin.
6. **Link labels** (y=311, 5px below): "Paper", "Code", "Citation" in Open Sans 14px/700 #333333, no underline.
7. **TL;DR** (`h1.tldr`, y=361, 30px below): Open Sans 18px/500, line-height 24px, #333333, centred; "TL;DR" bold 700.
8. **Teaser** (`img.img`, y=395, 10px below): 784 × 435px (80% of 980px via `.base-row img`), x=328, no border or radius; the light blue-grey input panel and labels are part of the image.

"Overview" starts at y=857, just below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | (body) | page background |
| Text | #333333 | (body) | authors, affiliations, icons, link labels, TL;DR, paragraphs, citation text, credit |
| Title Grey | #4d4d4d | `.title` | wordmark, full title, section titles |
| Citation Grey | #eaeaea | `.citation` | citation box background |
| Default Link Blue | #0000ee | (browser default) | anchor color inherited by icon blocks; not visible because icons and labels set #333333 |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Wordmark | 'Varela Round', sans-serif (inline) | Varela Round 400; rendered at 700 as synthesised bold | Nunito |
| Text / titles | 'Open Sans', sans-serif | Open Sans 400, 500, 700 (Google Fonts) | Noto Sans |
| Code | monospace | system monospace (Consolas on Windows) | Source Code Pro |
| Icons | FontAwesome 4.7 | FontAwesome normal | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Wordmark | `h1.title.main-title` (inline style) | Varela Round 50px / 700 / 50px, letter-spacing 1px | #4d4d4d |
| Full title | `h1.title.main-title` | 27px / 400 / 50px, letter-spacing 1px | #4d4d4d |
| Section title | `h1.title` | 24px / 500 / 50px, letter-spacing 1px, margin-top 16.08px | #4d4d4d |
| TL;DR | `h1.tldr` | 18px / 500 / 24px; "TL;DR" 700 | #333333 |
| Paragraph | `p.paragraph` | 16px / 400 / 24px, left-aligned; key sentences `b` 700 | #333333 |
| Author | `a.author-text` | 16px / 400 / 20px, underlined | #333333 |
| Superscript | `sup` | 10px | #333333 |
| Affiliation | `.affiliation-col` | 16px / 400 / 20px | #333333 |
| Icon | `i.main-icon` | 50px (paper) / 55px (code, citation), line-height 100px | #333333 |
| Icon label | `.link-labels-text` | 14px / 700 | #333333 |
| Citation heading | `.citation > h1` | 24px / 700 / 20px | #333333 |
| BibTeX | `.citation > pre` | monospace 12px / 20px | #333333 |
| Body base / credit | `body`, `.credit` | 12px / 400 / 20px | #333333 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Figures | 0 | none | none |
| Citation box | 10px | none | none |
| Icons | n/a | none | none |
| Authors | 0 | underline (text-decoration) | none |

The page has no shadows, no borders and no colored fills apart from the citation box.

## Layout Metrics

- **Column**: `.container { max-width: 980px; margin: 0 auto }` inside `.section { margin: 0 30px; text-align: center }` → x=230–1210 at 1440.
- **Header rhythm**: title row margin 20px 0; wordmark and full title each on a 50px line; author and affiliation rows fixed at 25px height; icon block 100px tall with -14px pull-up; labels 5px below; TL;DR 30px below the labels; teaser 10px below the TL;DR.
- **Figures**: `.base-row img { width: 80% }` → 784px centred; the visualisation grid uses inline `width: 50%; max-width: 800px` images (490px each, two per row).
- **Sections**: blocks separated by `.add-large-top-padding` (25px) and `.add-top-padding` (10px) margins; section titles have a 16.08px top margin and a 50px line; paragraphs margin-bottom 20px.
- **Citation**: full 980px, #eaeaea, radius 10px, padding 5px 0; heading and `pre` indented 10px with 10px padding; 25px above.
- **Credit**: 12px centred line, margin 12px 0.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1040px (incl. 1440) | 980px column + 30px section margins | 12px base, 16px paragraphs | 50px wordmark, 27px title | float grid of author cells |
| 551–1040px | 30px | same | same | column shrinks with the viewport; cells keep percentages |
| ≤550px | 30px | 12px | 50px wordmark | author names 12px; author rows 35px tall; icons 50px (`!important`); link-label rows 100% width |

## Components

- **Rounded wordmark**: the project name alone in Varela Round 50px, bold, 1px tracking, #4d4d4d, on its own 50px line; the descriptive title sits under it in Open Sans 27px/400.
- **Author grid**: rows of equal float cells (20% or 25%) inside 700px; names underlined 16px #333333 with tight 10px superscripts; affiliations and contribution notes share one row of 25% cells.
- **Icon link** (`.link-block` + `.main-icon`): a 100px-tall centred Font Awesome 4 glyph (file-text 50px, github 55px, graduation-cap 55px) in #333333, with a separate row of bold 14px labels underneath, three per 500px row.
- **TL;DR line**: one centred sentence, 18px/500, with "TL;DR" in bold.
- **Figure block**: an 80%-width image (784px) with all annotation drawn into the image, followed by a left-aligned 16px paragraph whose key claim is bold.
- **Citation box** (`.citation`): #eaeaea, radius 10px; "Citation" heading 24px/700, a 16px invitation line, and a 12px monospace `pre`, all left-aligned.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Wordmark + title | yes | rounded bold wordmark over a light 27px title |
| Authors / affiliations | yes | underlined names in a percentage grid, notes row |
| Link icons | yes | three large black FA4 icons with bold labels |
| TL;DR | yes | centred 18px sentence |
| Teaser | yes | 784px annotated figure with stats inside the image |
| Abstract | present but non-standard | no Abstract heading; "Overview" paragraphs replace it |
| Method diagrams | yes | 784px figures with paragraphs |
| Visualisation grid | yes | two 50%-width image grids side by side |
| Results tables | absent from the source | numbers appear only inside figures |
| Videos | absent from the source | `#main-video` is declared in CSS but unused |
| Citation | yes | grey rounded box with `pre` |
| Credit footer | yes | 12px centred line |

## Adapting to Other Content

- **More authors**: add another `.author-row` of equal cells (20% for five per row, 25% for four) inside the 700px block; keep the 25px row height and underline.
- **More links**: keep three icons per 500px row (33.3% cells); add a second row with the same 100px icon line and bold 14px labels rather than shrinking icons.
- **A results table**: centre it at 784px (80%), 16px #333333 text, header bold with a 1px #333333 bottom rule, no fills; caption as a left-aligned 16px paragraph with the key claim in bold.
- **Videos**: use the declared `#main-video` recipe: width 90% (882px), border-radius 15px, 10px below.
- **News or a publication list**: left-aligned 16px paragraphs (line-height 24px) with bold dates, 20px apart, inside the 980px column.

## Do's and Don'ts

- Do keep the palette to #333333 and #4d4d4d on white; let figures supply the color.
- Do set the project name alone as a rounded bold wordmark above the full title.
- Do use large monochrome icons with bold labels for links instead of buttons.
- Do draw annotations and numbers into the figures themselves.
- Don't add colored links, fills or shadows; the only filled shape is the #eaeaea citation box.
- Don't widen figures past 80% of the column (784px).
- Don't center paragraphs; titles and figures are centred, body text is left-aligned.

## Surfaces

White everywhere. The single tinted surface is the #eaeaea citation box with a 10px radius. Colored panels (the pale blue input panel, purple attention maps) exist only inside the figures.

## Imagery

Annotated research figures: a fox photograph with masked patches, purple attention maps and reconstructions beside large figures for FLOPs, training time and accuracy; flat block diagrams with light blue boxes and grey token stacks; a dense grid of ImageNet reconstructions (zebra, bus, golf ball, hot dog, tiger, etc.) comparing Original, Masked, MAE and CrossMAE.

## Layout

One centred 980px column: wordmark, title, authors, icons, TL;DR, teaser, then three titled sections with 784px figures and left-aligned paragraphs, a visualisation grid, the citation box and a credit line. Vertical rhythm comes from fixed 50px title lines and 10–30px margins.

## Agent Prompt Guide

Quick colors: background #ffffff, text #333333, titles #4d4d4d, citation box #eaeaea.

1. "Build a centred header in a 980px column: the project name in Varela Round 50px bold, letter-spacing 1px, #4d4d4d, on a 50px line; under it the full title in Open Sans 27px/400, letter-spacing 1px, #4d4d4d; then author rows of equal percentage cells inside 700px with underlined 16px #333333 names and 10px superscripts, and a 16px affiliation row."
2. "Make icon links: three 33.3% cells in a 500px row, each a Font Awesome icon at 50–55px in #333333 with line-height 100px, and a second row of bold Open Sans 14px #333333 labels (Paper, Code, Citation) 5px below; no buttons, no underlines."
3. "Add a TL;DR and figure: a centred Open Sans 18px/500 sentence with 'TL;DR' in bold, 30px below the links; then an 80%-width (784px) figure with no border, followed by a left-aligned 16px/24px #333333 paragraph with the key claim in bold; section titles are Open Sans 24px/500 #4d4d4d on a 50px line."

## Similar Pages

- The NeRF / DeepMotionEditing family of icon-link project pages: centred column, large icons, figure-first.
- Berkeley vision and robotics project pages that reuse this template with a custom wordmark.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #333333;
  --title: #4d4d4d;
  --citation-bg: #eaeaea;
  --font-text: "Open Sans", sans-serif;
  --font-wordmark: "Varela Round", sans-serif;
  --column: 980px;
  --figure-width: 80%;
  --title-line: 50px;
  --radius-citation: 10px;
}
```

## Provenance

- **URL**: https://crossmae.github.io/
- **Paper**: Rethinking Patch Dependence for Masked Autoencoders (CrossMAE), Letian Fu, Long Lian, Renhao Wang, Baifeng Shi, Xudong Wang, Adam Yala, Trevor Darrell, Alexei A. Efros, Ken Goldberg (UC Berkeley; UCSF); arXiv 2401.14391.
- **Venue**: TMLR 2025 (OpenReview JT2KMuo2BV, April 2025).
- **Selection reason**: linked from the jmlr.org/tmlr/papers accepted list; curl returned 200 text/html.
- **Template credit**: credit line states the design is adapted from the NeRF and DeepMotionEditing project pages, among others; Font Awesome 4.7, Google Fonts Open Sans and Varela Round.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), additional computed-style probes of the icons, labels, author rows, TL;DR, paragraphs, images, citation box and credit, the 1440×900 and full-page screenshots, and `style.css` and `index.html` read directly, on 2026-10-28.
