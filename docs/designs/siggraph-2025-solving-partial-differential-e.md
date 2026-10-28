# Volumetric Walk on Spheres — Style Reference

> A lab's house letterhead: Avenir type, a small brick-red seal in the corner, blue links, and a dense figure that does all the explaining.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), extra computed-style probes of the logo, nav items and teaser caption, the 1440×900 and full-page screenshots, and the page's `index.html` plus the shared lab stylesheet `/shared/style.css` (CMU Computational Imaging) read directly. The page is short (1702px at 1440) and uses the lab's common template rather than a per-paper design. The title is an `h1` wrapped in a link; the stylesheet gives `h1` its own `color: var(--text)`, so it renders black, not link blue.

## Overview

A narrow, text-first page: the `body` itself is the column (max-width 60em = 960px, padding 1em), so content runs from x=240 to x=1200 at 1440. Everything is left-aligned in Avenir Next Pro. The header has a two-line 32px/700 black title, a 64px brick-red (#93281e) lab logo floated right, a 20px/700 author line with names as blue (#1772d0) links, a 20px/700 black venue line, and a row of three bold 17.6px icon links (paper, code, citation) with Font Awesome glyphs. A 944px annotated teaser figure follows with a justified 14.4px italic caption. Below, four 20px/700 `h2` sections (Abstract, Resources, Citation, Acknowledgments) carry justified 16px text indented 16px from the headings; the BibTeX sits in a #f0f0f0 `pre` with a 1px #dddddd border, 3.6px radius and a small copy button. There are no section bands, cards or footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 69.2% (plus #fbfbfc 3.3%, #fdffff and #fffffe 2.1%); gray #abadaf 9.3% and light gray #d7d9db 5.9% (anti-aliased text and the teaser's gray membrane and lipid rendering); mauve #95667a 5.7% (the teaser's red/blue potential fields and proteins blended); pale pink #f4f0f1 4.6%. The brick-red logo and blue links cover too little area to form clusters.

Anatomy in DOM order (desktop 1440px, left edge x=240):

1. **Body column** (`body`): max-width 960px, margin auto, padding 16px → content x=240–1200, top at y=16.
2. **Lab logo** (`img#logo`, x=1136, y=37, 64×64): CMU Computational Imaging mark, white shutter glyph on #93281e, floated right with margin-left 32px, linked to the lab site.
3. **Title** (`header > a > h1`, y=37, 83px, two lines): Avenir Next Pro 32px/700, line-height 41.6px, #000000, `text-wrap: balance`; margin 21.44px 0. Gap 22px.
4. **Authors** (`p.authors`, y=142, 26px): 20px/700, line-height 26px; four names as #1772d0 links separated by black commas. Gap 17px.
5. **Venue** (`p.venue`, y=185, 26px): "ACM Transactions on Graphics (SIGGRAPH) 2025", 20px/700 #000000. Gap 17px.
6. **Icon links** (`nav > ul`, y=227, 32px): three inline items, 17.6px/700 #1772d0, each a fixed-width Font Awesome icon (`fa-file-pdf`, `fa-github`, `fa-quote-left`) plus a non-breaking space and a lowercase word; items 17.6px apart. Gap 18px.
7. **Teaser figure** (`figure#teaser`, x=256, y=277, 944px wide): image 944×248 with 8px bottom margin, then a justified italic caption in 14.4px/18.72px #000000 (y=539–633); its `<em>` terms are italic like the rest, so they do not stand out. Gap 24px.
8. **Abstract heading** (`h2`, y=657): 20px/700 #000000, margin 24px 0 10px; paragraph from y=693 at x=256, 16px/400, line-height 20.8px, justified.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | (browser default) | page background |
| Ink | #000000 | --text | title, venue, headings, body text, figure caption |
| Link Blue | #1772d0 | --link | author names, icon links, inline links in Resources |
| Burnt Orange | #b35500 | --accent | link hover, focus and active color |
| Brick Seal | #93281e | (SVG fill in `/shared/imaging.svg`) | lab logo square |
| Code Surface | #f0f0f0 | --surface | BibTeX `pre`, copy button, table header fills (declared) |
| Soft Border | #dddddd | --border-soft | BibTeX `pre` border |
| Button Hover | #d0d0d0 | --button-hover | copy button hover |

`--border-strong` (#c0c0c0) and `--award-bg` (#fff3e0) are declared for tables and award tags; neither appears on this page.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text | 'Avenir Next Pro', 'Lato', Verdana, Helvetica, sans-serif (`--body-font`) | Avenir Next Pro 400, 700 (Demi), 400 italic, self-hosted MyFonts kit | Nunito Sans |
| Code | ui-monospace, SFMono-Regular, Menlo, Consolas, monospace | Consolas on Windows | JetBrains Mono |
| Icons | Font Awesome 7 (solid, brands) | Font Awesome 7 Free 900, Brands 400 | — |

Avenir Next Pro is licensed and not freely redistributable; Nunito Sans matches its geometric proportions more closely than Lato, the page's own fallback.

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Title | `h1` | 32px / 700 / 41.6px, balanced wrap | #000000 |
| Authors | `p.authors` | 20px (125%) / 700 / 26px | names #1772d0 |
| Venue | `p.venue` | 20px / 700 / 26px | #000000 |
| Icon links | `nav > ul` | 17.6px (110%) / 700 / 22.88px | #1772d0 |
| Section heading | `h2` | 20px (125%) / 700 / 26px | #000000 |
| Body | `p` | 16px / 400 / 20.8px (1.3), justified, hyphens auto | #000000 |
| Teaser caption | `#teaser > figcaption` | 14.4px (90%) / 400 italic / 18.72px | #000000 |
| BibTeX | `pre` | 14.4px (90%) / 400 / 18.72px monospace | #000000 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| BibTeX `pre` | 0.25em = 3.6px | 1px solid #dddddd | none |
| Copy button (`.copy`) | 0.25em = 3.33px | none | none |
| Teaser and logo | 0px | none | none |
| Links | — | no underline (hover none) | none |

## Layout Metrics

- **Column**: `body { max-width: 60em; margin: auto; padding: 1em }` → 960px of content at x=240–1200; there is no wrapper element.
- **Indent system**: `p, ul, ol, iframe, table, figure, pre { margin: 0 0 1em 1em; width: calc(100% - 1em) }`, so body blocks start 16px right of the headings (x=256); `pre` is `calc(100% - 3em)` wide plus 1em padding.
- **Header vertical sum**: 16 body padding + 21.44 h1 margin → title at 37; 83 title + 21.44 → authors at 142; 26 + 16.6 → venue at 185; 26 + 16.6 → nav at 227; nav 32 + li bottom margin 8.8 + ul margin → teaser at 277.
- **Teaser**: image 100% of the 944px figure, 8px below it the caption; figure margin-bottom 0.
- **Sections**: `h2` margin 24px 0 10px (1.2em 0 0.5em); paragraphs 16px apart; list items margin 0 0 8px 16px.
- **Logo**: 64×64, `float: right; margin-left: 2em`, aligned with the title's top.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >768px (48em) | 16px body padding inside the 960px column | 16px | 32px | justified text |
| ≤768px | same | 16px | 32px | `p, ul, ol, iframe, table, figure, pre` switch to left-aligned text |
| print | full paper width | 16px | 32px | links black and underlined; copy button and videos hidden |

## Components

- **Icon link row** (`nav > ul`): unstyled list, items `inline-block` with 17.6px right margin, 17.6px/700 #1772d0, each a Font Awesome `fa-fw` icon then `&nbsp;` then a lowercase label; hover #b35500, no underline.
- **Author line** (`p.authors`): 20px/700, names as #1772d0 links separated by black commas; no superscripts or affiliations.
- **Venue line** (`p.venue`): 20px/700 #000000 plain text.
- **Teaser figure** (`figure#teaser`): full-width image, then an italic 14.4px justified caption; indented 16px like all body blocks.
- **Resource entries**: paragraphs that start with a Font Awesome icon and a bold label ("Paper:", "Presentation:", "Code:") followed by a sentence with inline #1772d0 links.
- **BibTeX block** (`pre`): #f0f0f0, 1px solid #dddddd, 3.6px radius, padding 14.4px, 14.4px monospace; a `.copy` icon button floated right inside it (padding 0.4em, radius 0.25em, hover #d0d0d0).

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Lab logo | yes | 64px brick-red square floated right |
| Title / authors / venue | yes | left-aligned, 32px black title, 20px bold blue names, 20px bold venue |
| Link row | yes | three bold blue icon links, not buttons |
| Teaser | yes | 944px annotated figure with italic caption |
| Affiliations | absent from the source | only names are listed |
| Abstract | yes | justified 16px text under a 20px heading |
| Resources | yes | icon-led paragraphs with inline links |
| Video | absent from the source | slides are linked, not embedded |
| Results figures / tables | absent from the source | the page has only the teaser |
| BibTeX | yes | gray `pre` with copy button |
| Acknowledgments | yes | justified paragraph |
| Footer | absent from the source | page ends after Acknowledgments |

## Adapting to Other Content

- **More authors**: keep one 20px/700 line of blue names; at about eight names it wraps within the 960px column. Add affiliations as a separate 16px/400 black line rather than superscripts.
- **A results table**: use the stylesheet's own table recipe: border-collapse, 1px solid #c0c0c0 cells with 4px padding, `th` bold on #f0f0f0, a 2px rule under the header row, even rows #f0f0f0; indented 16px like other blocks, up to 944px wide.
- **Long publication or news lists**: the lab's `figure.entry` recipe: an 80px (5em) square thumbnail beside a caption paragraph, one per row; or a plain list with 8px item spacing.
- **More figures**: add `figure.full` blocks at 944px with 14.4px captions; for galleries use `figure.gallery` (two per row, images 240px tall).
- **Videos**: `video` or `iframe.video` at 944px with `aspect-ratio: 16 / 9`, 16px left indent.

## Do's and Don'ts

- Do keep the whole page in one 960px column with headings flush left and body blocks indented 16px.
- Do use Avenir Next Pro (or Nunito Sans) at 700 for title, authors, venue, nav and headings, 400 for text.
- Do keep links #1772d0 without underline and turn them #b35500 on hover.
- Do justify paragraphs and captions at desktop widths.
- Don't add buttons, pills or badges; links are bold icon text.
- Don't centre the header; the logo floats right and everything else is left-aligned.
- Don't add background bands or cards; the only filled surface is the #f0f0f0 code block.

## Surfaces

Plain white page; #f0f0f0 only in the BibTeX block and copy button; the #93281e logo is the only solid colour block.

## Imagery

One dense, labelled teaser: a rendered biomembrane with coloured proteins and red/blue ion particles on the left, two framed red-white-blue electric-potential field plots with inset line graphs on the right, all with thin black callout arrows and gray labels on white.

## Layout

A single 960px column: right-floated logo, left-aligned header block, a full-width teaser figure, then four short sections with 24px heading gaps. The page is about 1700px tall at 1440.

## Agent Prompt Guide

Quick colors: background #ffffff, text #000000, links #1772d0, hover #b35500, logo #93281e, code surface #f0f0f0, code border #dddddd.

1. "Make the body the column: max-width 960px, margin auto, padding 16px, font 'Avenir Next Pro', 'Nunito Sans', sans-serif, 16px, line-height 1.3, color #000000. Headings flush left; p, figure and pre get margin 0 0 16px 16px and width calc(100% - 16px), text justified."
2. "Build the header: a 64px square logo (#93281e) floated right with 32px left margin; h1 32px/700 #000000 with text-wrap balance; an authors line 20px/700 with names as #1772d0 links; a venue line 20px/700 #000000; then a row of inline icon links at 17.6px/700 #1772d0 (Font Awesome icon + non-breaking space + lowercase word), 17.6px apart, hover #b35500."
3. "Add a teaser figure at full column width with an italic 14.4px justified caption 8px below, and a BibTeX pre: background #f0f0f0, 1px solid #dddddd, radius 3.6px, padding 14.4px, 14.4px monospace, with a small copy button floated right (hover #d0d0d0)."

## Similar Pages

- Lab-template paper pages from the same group (CMU Computational Imaging) and other single-stylesheet lab sites.
- Classic graphics-paper pages with a left-aligned header, a teaser and a few text sections.

## Quick Start

```css
:root {
  --text: #000000;
  --link: #1772d0;
  --accent: #b35500;
  --surface: #f0f0f0;
  --border-soft: #dddddd;
  --button-hover: #d0d0d0;
  --logo: #93281e;
  --body-font: "Avenir Next Pro", "Nunito Sans", Lato, Verdana, Helvetica, sans-serif;
}
body { max-width: 60em; margin: auto; padding: 1em; font-family: var(--body-font); line-height: 1.3; color: var(--text); }
p, figure, pre { margin: 0 0 1em 1em; width: calc(100% - 1em); text-align: justify; }
```

## Provenance

- **URL**: https://imaging.cs.cmu.edu/volumetric_walk_on_spheres/
- **Paper**: Solving partial differential equations in participating media (arXiv 2506.08237), Bailey Miller, Rohan Sawhney, Keenan Crane, Ioannis Gkioulekas.
- **Venue**: SIGGRAPH 2025 (page: "ACM Transactions on Graphics (SIGGRAPH) 2025"; the arXiv comment reads "SIGGRAPH 2025. Project page ...", a weak acceptance wording flagged in selection).
- **Selection reason**: a compact, typographic academic page with a crisp sans face, inline icon links, a dense annotated teaser and a lab logo top right; a distinct minimalist style.
- **Template credit**: the CMU Computational Imaging group's shared lab stylesheet (`/shared/style.css`, Avenir Next Pro via a MyFonts kit, Font Awesome 7); no third-party template.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), extra computed-style probes, the 1440×900 and full-page screenshots, and `index.html`, `/shared/style.css` and `/shared/imaging.svg` read directly, on 2026-10-28.
