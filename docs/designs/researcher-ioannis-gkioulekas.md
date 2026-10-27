# Ioannis Gkioulekas — Style Reference

> A specimen drawer of computational imaging: Avenir on white, one blue, and seventy-odd square thumbnails lined up like slides on a light box.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, DOM-order anatomy, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the lab's shared `/shared/style.css` (its own `:root` palette) and the page markup read directly. Avenir Next Pro loads from the lab's licensed MyFonts kit in 400 and 700 (the "Demi" cut) and renders everywhere; Lato is declared only as a fallback and does not load. Font Awesome 7 supplies the small icons in the contact list.

## Overview

A plain 960px column on white with 16px body padding. "Ioannis Gkioulekas" sits at the top left in Avenir 32px bold black, with the lab's 64px dark-red aperture logo floated to the right. Below, a 150px square portrait (no rounding) is paired with a two-column list of bold blue #1772d0 links, each led by a small fixed-width Font Awesome icon: email, CV, Google scholar, ORCID, publications, then teaching, writing, code and the lab. Sections open with 20px bold black headings at the left margin while their content is indented 16px. The About text is justified and hyphenated. The Publications section is the heart of the page: 73 `figure.entry` rows, each an 80px square cover-cropped thumbnail beside a three-line caption (bold blue title, authors with his name bold and asterisk or dagger marks, plain venue and year). Three entries carry an award tag, a small rounded label in burnt orange #b35500 on cream #fff3e0. Teaching reuses the same rows; Writing and Code are single paragraphs. There is no footer and no navigation bar.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): #ffffff 80.8% (page), #a8b2bf 6.8% and #cfd8e0 3.7% (cool tones in the thumbnails and anti-aliased text), #6b6364 2.8% (portrait), #f0eeed 2.7% (light thumbnail areas), #fafbfb 2.2%. Blue #1772d0 and the logo's dark red are each under 1%.

Anatomy in DOM order (desktop 1440px; body max-width 960px at x=240, padding 16px):

1. **Logo** (`#logo`, floated right, x≈1136, y≈37): 64×64 SVG, margin-left 2em, links to the lab.
2. **Name** (`header > a > h1`, x=240, y=37): Avenir Next Pro 32px/700, line-height 1.3, #000000 (the h1 overrides the link color), margin 21.44px 0. Gap 21px.
3. **Portrait** (`#personal > img`, x=256, y=100): 150×150, no radius, margin 0 0 16px 16px; `#personal` is a flex row, align-items center.
4. **Contact list** (`#personal > ul`, x=422): flex column-wrap with max-height 150px, so it breaks into two columns; row gap 8px, column gap 16px; items Avenir 16px/700 #1772d0, each with a `fa-sm fa-fw` icon and a non-breaking space. Header ends at y=266; gap 24px.
5. **"About"** (`h2`, x=240, y=290): Avenir 20px/700 #000000, margin 24px 0 10px.
6. **About paragraphs** (`p`, x=256, y=326 and 405, 944px wide): Avenir 16px/400, line-height 1.3 (20.8px), #000000, text-align justify, hyphens auto, `text-wrap: pretty`, margin 0 0 16px 16px; links #1772d0. Gap 24px.
7. **"Publications"** (`h2`, y=554). Gap 10px.
8. **Publication rows** (`figure.entry`, x=256, y=590, 686, 782, 878; 80px tall, 16px apart): 80×80 thumbnail, then the caption at x=356; rows continue past the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Ink | #000000 | --text | name, section headings, body, authors, venues |
| Link Blue | #1772d0 | --link | contact list, inline links, publication and course titles |
| Burnt Orange | #b35500 | --accent | link hover, focus and active color; award tag text; trophy icons |
| Award Cream | #fff3e0 | --award-bg | award tag background |
| Surface | #f0f0f0 | --surface | code backgrounds, table headers and zebra rows (other pages); skip-link background |
| Hover Grey | #d0d0d0 | --button-hover | table row hover, copy button hover (other pages) |
| White | #ffffff | (default) | page |

Declared but not visible on this page: `--border-strong` #c0c0c0 and `--border-soft` #dddddd (tables and code), which other pages of the shared lab stylesheet use.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (everything) | 'Avenir Next Pro', 'Lato', Verdana, Helvetica, sans-serif (self-hosted MyFonts kit) | Avenir Next Pro 400, 700 (Demi) | Nunito Sans |
| Icons | Font Awesome 7 (solid, brands) | Font Awesome 7 Free 900, Brands 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `h1` | 2em = 32px / 700 / 1.3 | #000000 |
| Section heading | `h2` | 125% = 20px / 700 / 1.3, `text-wrap: balance` | #000000 |
| Body | `body`, `p` | 16px / 400 / 1.3, justified | #000000 |
| Contact link | `#personal > ul a` | 16px / 700 | #1772d0 |
| Publication title | `figure.entry figcaption a strong` | 16px / 700 | #1772d0 |
| Authors | `figcaption p` | 16px / 400; own name `strong` 700; marks `sup` | #000000 |
| Venue | `figcaption p` (third line) | 16px / 400 | #000000 |
| Award tag | `.award` | 16px / 400 | #b35500 on #fff3e0 |
| Teaching role | `figcaption strong` | 16px / 700 | #000000 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Portrait | 0 | none | none |
| Publication thumbnail | 0 | none | none |
| Award tag | 0.25em (4px) | none | none |
| Logo | 0 (square artwork) | none | none |

## Layout Metrics

- **Column**: `body` max-width 60em (960px), margin auto, padding 1em (16px); content x=240–1200 at 1440.
- **Indent rule**: `p, ul, ol, figure, …` all get `margin: 0 0 1em 1em` and `width: calc(100% - 1em)`, so content sits 16px right of the headings.
- **Headings**: h2 margin 1.2em 0 0.5em (24px 0 10px).
- **Header**: logo float right with 2em left margin; `#personal` flex, centred; contact list column-wrap at max-height 9.375em (150px), gap 0.5em row and 1em column.
- **Publication row**: `figure.entry` margin 0 0 16px 16px; thumbnail 5em × 5em (80px) object-fit cover, vertical-align middle; caption inline-block at `calc(100% - 1em - 5em)`, its `p` margin-left 16px, margin-bottom 0.
- **Page height**: 7,887px at 1440.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >768px | 16px body padding inside 960px | 16px | 32px | portrait beside a two-column contact list; justified text |
| ≤48em (768px) | 16px | 16px | 32px | `#personal` stacks: portrait centred above a single-column contact list; text switches from justified to left-aligned |

## Components

- **Contact list with icons**: unbulleted, bold 16px #1772d0 links, each preceded by a small fixed-width Font Awesome icon (envelope, file, graduation cap, ORCID, book, chalkboard, pen, GitHub, camera) and a non-breaking space; flows into columns 150px tall. Hover #b35500.
- **Publication row** (`figure.entry`): 80px square thumbnail (cover-cropped, no border or radius) linked to the project, vertically centred against a three-line caption: bold #1772d0 title, author line with own name bold and `*` / `†` superscripts, venue and year. 16px between rows.
- **Award tag** (`span.award`): inline after the title, #b35500 text on #fff3e0, padding 0.2em 0.4em, radius 0.25em, margin-left 0.5em, regular weight ("best paper award", "best student paper award").
- **Section heading**: 20px bold black at the left edge, balanced wrapping, content indented 16px beneath it.
- **Links**: #1772d0, no underline; hover, focus and active #b35500.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Name and lab logo | yes | bold 32px name, 64px logo floated right |
| Portrait and contact links | yes | square photo beside an icon link list |
| About | yes | justified hyphenated paragraphs |
| Publications | yes | 73 thumbnail rows, one per paper |
| Award tags | yes | cream rounded tags with burnt-orange text |
| Teaching | yes | same thumbnail rows with a bold role line |
| Writing, Code | yes | single paragraphs |
| News | absent from the source | — |
| Navigation bar | present but non-standard | in-page anchors inside the contact list |
| Footer | absent from the source | page ends after Code |

## Adapting to Other Content

- **Very long publication lists**: this page already holds 73 entries; keep one 80px thumbnail per paper and the same three caption lines so the list scans as a grid of squares. Add year `h3` subheads (110%, indented 1em, defined in the stylesheet) if grouping is needed.
- **Papers without a figure**: still reserve the 80px square (use the venue logo or a neutral crop) so captions stay aligned.
- **More awards**: one `.award` tag per paper after the title; add a second tag rather than a sentence.
- **News**: a plain indented list with a bold date; no thumbnails.
- **Students**: `figure.person` from the same stylesheet gives circular 10em photos in a two-up gallery.

## Do's and Don'ts

- Do keep everything in one Avenir family at two weights, 16px for nearly all text.
- Do indent all content 16px under flush-left headings.
- Do keep thumbnails square and unrounded; the rounded award tag is the only soft shape.
- Don't add color beyond #1772d0 for links and #b35500 / #fff3e0 for awards.
- Don't add cards, rules or shadows between publications; the 16px gap and the thumbnails make the rhythm.
- Don't justify text below 768px; the stylesheet switches to left-aligned there.

## Surfaces

One white surface with no bands, borders or shadows. The only fills are the cream award tags and, on other lab pages, #f0f0f0 code and table cells.

## Imagery

A square portrait and the lab's red aperture logo, then a long column of colourful square crops: renders of light transport, lenses, point clouds, smoke, interferometry fringes, colour-mapped PDE solutions and textured objects.

## Layout

Header (name, logo, portrait, contact list), About, Publications, Teaching, Writing, Code, all in one 960px column. About 7,887px tall at 1440.

## Agent Prompt Guide

Quick colors: text #000000, links #1772d0, hover and award text #b35500, award background #fff3e0, surface #f0f0f0, page #ffffff.

1. "Build a header: body max-width 960px, padding 16px; a 64px logo floated right; name in Avenir Next Pro (fallback Nunito Sans) 32px/700 #000000; below, a flex row with a 150×150 square portrait (margin 0 0 16px 16px) and an unbulleted list in column-wrap with max-height 150px, row gap 8px, column gap 16px, items 16px/700 #1772d0 each led by a small fixed-width icon; hover #b35500."
2. "Make a publication list: each entry a figure with margin 0 0 16px 16px; an 80×80 object-fit cover thumbnail, vertically centred beside a caption block of width calc(100% - 96px) with 16px left margin: title 16px/700 #1772d0, authors 16px/400 #000000 with the owner in 700, venue and year on the third line."
3. "Create an award tag: inline span after the title, margin-left 0.5em, padding 0.2em 0.4em, radius 0.25em, color #b35500, background #fff3e0, regular weight."

## Similar Pages

- Lab-wide shared stylesheets that also style course and project pages.
- Graphics and imaging faculty pages with very long, thumbnail-per-paper lists.

## Quick Start

```css
:root {
  --text: #000000;
  --link: #1772d0;
  --accent: #b35500;
  --surface: #f0f0f0;
  --award-bg: #fff3e0;
  --body-font: 'Avenir Next Pro', 'Nunito Sans', Verdana, Helvetica, sans-serif;
}
body { max-width: 60em; margin: auto; padding: 1em; font: 400 1em/1.3 var(--body-font); color: var(--text); }
h2 { font-size: 125%; margin: 1.2em 0 0.5em 0; }
p, ul, figure { text-align: justify; margin: 0 0 1em 1em; width: calc(100% - 1em); }
a { color: var(--link); text-decoration: none; } a:hover { color: var(--accent); }
figure.entry img { width: 5em; height: 5em; object-fit: cover; vertical-align: middle; }
.award { color: var(--accent); background: var(--award-bg); margin-left: 0.5em; padding: 0.2em 0.4em; border-radius: 0.25em; }
```

## Provenance

- **URL**: https://imaging.cs.cmu.edu/igkioule/
- **Person**: Ioannis Gkioulekas (computational imaging, graphics).
- **Venue / award**: CVPR 2024 Best Student Paper Honorable Mention, "Objects as Volumes: A Stochastic Geometry View of Opaque Solids".
- **Selection reason**: award rule (first/last author). https://cvpr.thecvf.com/Conferences/2024/News/Awards
- **Template credit**: the CMU Computational Imaging lab's shared stylesheet (`/shared/style.css`), used across its course and project pages.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), the 1440×900 and full-page screenshots, and `/shared/style.css` and the markup read directly, on 2026-10-28.
