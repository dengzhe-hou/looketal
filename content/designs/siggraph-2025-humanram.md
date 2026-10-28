# HumanRAM — Style Reference

> A pale blue-gray marquee where the acronym is spelled in three paints, and every later caption reuses the same blue, green and clay to say which task it shows.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), extra computed-style probes of the jumbotron, buttons, carousel controls, videos and figures, the 1440×900 and full-page screenshots, and the page's `index.html` (inline `<style>` block and inline colour spans) and its customised `css/bootstrap-4.4.1.css` read directly. The page is built on Lior Yariv's Bootstrap 4 template with LongVolCap add-ons; the customised Bootstrap file overrides `.btn-light` to a near-black button and `.jumbotron` to #ebf0f1. The serif "We propose HumanRAM…" text visible under the Abstract heading is part of a video, not HTML.

## Overview

A Bootstrap page in Jost (500 for text, 900 for the title). The header is a full-width jumbotron tinted #ebf0f1 with 4.8px rounded corners: a centred two-line 45px title in which "R", "A", "M" and the matching words "Reconstruction", "Animation", "Model" are painted #6589bf blue, #78aa58 green and #c68b5b clay, a gray (#5a6268) 24px "SIGGRAPH 2025" line, a hairline rule, Bootstrap-blue (#007bff) author links with superscripts, a 20px affiliation block and three near-black (#090f15) buttons with 8px radius and PDF icons. Below, on white, sections in a 1140px Bootstrap container open with a left-aligned 30px/700 heading and a 1px rgba(0,0,0,0.1) rule: an Abstract that starts with a 1110px rounded video (animated serif text plus input grids framed in light green), a 13px caption, a justified 20px paragraph; then Sparse-view and Single-view result carousels of 16:9 videos with 50px translucent round arrows and 15px dots; a Method section with two figures; an application carousel; a full demo video; and a BibTeX block in a #e9eeef well with 20px radius.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 46.0% (plus #fffefc and #fffffe 1.0%); jumbotron blue-gray #ebf0f1 38.6% (plus #edf1f2 1.7%); gray #9a9fa1 7.6% (anti-aliased text, rules and the person renders); pale green #dff1de 3.2% and #f2f7f4 1.9% (the green frames around the input grids in the abstract video). The three title paints cover too little area to form clusters.

Anatomy in DOM order (desktop 1440px, centred inside the 1140px container at x=150, content x=165–1275):

1. **Jumbotron** (`div.jumbotron.text-center`, 0–434px): #ebf0f1, padding 64px 32px, radius 4.8px (0.3rem), margin-bottom 16px.
2. **Title** (`h1 > b`, y=64, 108px, two lines): Jost 45px, rendered weight 900, line-height 54px, #212529; spans "R" and "Reconstruction" #6589bf, "A" and "Animation" #78aa58, "M" and "Model" #c68b5b. Gap 8px.
3. **Venue** (`h4`, y=180, 29px): "SIGGRAPH 2025", Jost 24px/700, #5a6268 (inline style). Gap 8px + 16px.
4. **Rule** (`hr`, y≈225): 1px solid rgba(0,0,0,0.1), margins 16px; spans the 1110px column. Gap 16px.
5. **Authors** (y=242, 29px): five inline `a` elements, Jost 20px/500 #007bff, superscripts "1*", "2*", "3", "1x", "3x" in the same blue; about 12px apart.
6. **Affiliations and notes** (`p`, y=272, 60px): "¹Mathematics, HKUST ²Huawei ³State Key Lab of CAD&CG, Zhejiang University" and "* Equal contribution  x Corresponding authors", Jost 20px/500 #212529, centred. Gap 16px.
7. **Buttons** (`a.btn.btn-large.btn-light`, y=348, 38px): ArXiv, Paper, Supplementary; #090f15 fill, #e2e2e2 text, labels bold Jost 16px, 1px solid #f8f9fa border, radius 8px, padding 6px 24px, Font Awesome 4 `fa-file-pdf-o` icon at left; about 6px apart. Jumbotron ends at 434.
8. **Abstract heading** (`h3`, y=450): Jost 30px/700 #212529, left-aligned, padding-top 5px; 1px rule below with margin-top 0. Gap 25px.
9. **Abstract video** (`video`, y=516, 1110×624, radius 10px): animated serif abstract text with green-framed input grids and reconstructions.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Marquee Mist | #ebf0f1 | (`.jumbotron` override) | header band |
| Ink | #212529 | (Bootstrap `$body-color`) | title base text, headings, body text, affiliations, BibTeX text |
| Reconstruction Blue | #6589bf | (inline span) | "R" and "Reconstruction" in the title; "reconstruction" in the abstract video |
| Animation Green | #78aa58 | (inline span) | "A" and "Animation" in the title; "animation" in the abstract video |
| Model Clay | #c68b5b | (inline span) | "M" and "Model" in the title |
| Venue Gray | #5a6268 | (inline style) | "SIGGRAPH 2025" line |
| Link Blue | #007bff | (Bootstrap `$primary`) | author names, footer links |
| Button Night | #090f15 | (`.btn-light` override) | button fill |
| Button Text | #e2e2e2 | (`.btn-light` override) | button label |
| Button Hover | #bec3c7 | (`.btn-light:hover`) | button fill on hover (text #212529) |
| Code Mist | #e9eeef | (inline style on `pre`) | BibTeX well |
| Rule | rgba(0,0,0,0.1) | (Bootstrap `hr`) | rule under the venue line and under every section heading |
| Control Shade | rgba(0,0,0,0.5) | (inline `<style>`) | carousel arrow circles and indicator dots |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text and display | 'Jost' (Google Fonts, weights 300–900) | Jost 400, 500, 700, 900 | Futura PT |
| Code | SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace | Consolas on Windows | JetBrains Mono |
| Icons | Font Awesome 4.7 and 6.7 | FontAwesome (4.7) | — |
| Math | KaTeX 0.13 | not used above the fold | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Title | `h1` (2.25em of 20px) with inner `<b>` | 45px / 900 rendered / 54px | #212529 with painted words |
| Venue | `h4` | 24px / 700 / 28.8px | #5a6268 |
| Section heading | `h3` (1.5em) | 30px / 700 / 36px, left | #212529 |
| Body | `body` (1.25em) | 20px / 500 / 30px; paragraphs justified inter-word | #212529 |
| Authors | `.jumbotron a` | 20px / 500 | #007bff |
| Figure caption | `p[style="font-size: small"]` | 13px / 500 / 19.5px | #212529 |
| Button | `.btn.btn-large` with `<b>` label | 16px, label bold / 24px | #e2e2e2 |
| BibTeX | `pre` | 17.5px (87.5%) / 500 / 26.25px | #212529 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Jumbotron | 4.8px (0.3rem) | none | none |
| Buttons | 8px | 1px solid #f8f9fa | none |
| Videos and iframes | 10px | none | none |
| Comparison canvases | 0px, padding 10px | none | none |
| Carousel arrows | 50%, 50×50px | none | none; whole control at opacity 0.5 |
| Indicator dots | 10px on a 15×15px dot | none | none |
| BibTeX `pre` | 20px | none | none |
| Section rules | — | 1px solid rgba(0,0,0,0.1) | none |

`.zoom-element:hover { transform: scale(1.25) }` with a 0.2s ease-in-out transition is declared for zoomable media.

## Layout Metrics

- **Container**: Bootstrap `.container` max-width 1140px at ≥1200px, padding 0 15px → content x=165–1275 (1110px).
- **Jumbotron**: full width (outside the container), padding 64px 32px; title 64–172, venue 180–209, rule, authors 242, affiliation block 272–332, buttons 348–386; total height 434.
- **Sections**: each `section > .container > .row > .col-12` starts with an `h3` (margin-bottom 8px) and an `hr` with margin-top 0 and margin-bottom 16px; consecutive sections render 30px apart (Abstract ends at y=1550, Sparse-view Results starts at 1580); the declared `.results-section { padding-bottom: 30px }` class is not used in the markup.
- **Abstract**: 1110×624 video, a 13px caption, then a 20px justified paragraph across the full 1110px.
- **Carousels**: one 16:9 video per slide, 1090×613 (10px gutters from `.sm-gutters`); arrows 50px, 25px inside the container edges, vertically centred; dots 15px with 50px spacing (li margin 0 25px) centred under the slide.
- **Method figures**: images at 45% (500px) and 80% (888px) of the column, centred.
- **BibTeX**: `pre` full column width, padding 26.25px, radius 20px.
- **Footer**: centred two-line credit, margin-bottom 10px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1200px | container 1140px | 20px | 45px | as described |
| 992–1199px | container 960px | 20px | 45px | same, narrower videos |
| 768–991px | container 720px | 20px | 45px | `col-md-4` result triples stay three across |
| 576–767px | container 540px | 20px | 45px | `col-md-*` columns stack |
| <576px | 15px | 20px | 45px | jumbotron padding drops to Bootstrap's 32px 16px |

## Components

- **Painted title**: the whole h1 in Jost 900 #212529; acronym letters and their expanded words each wrapped in an inline span coloured #6589bf (R / Reconstruction), #78aa58 (A / Animation) and #c68b5b (M / Model). The same blue and green colour "reconstruction" and "animation" inside the abstract video.
- **Tinted header band** (`.jumbotron`): full-width #ebf0f1, padding 64px 32px, 4.8px radius, all content centred, a 1px rgba(0,0,0,0.1) rule between venue and authors.
- **Dark button** (`.btn.btn-large.btn-light`, overridden): #090f15 fill, #e2e2e2 bold 16px Jost label, 1px solid #f8f9fa border, radius 8px, padding 6px 24px, Font Awesome 4 PDF icon at left; hover fill #bec3c7 with #212529 text.
- **Section header**: left-aligned `h3` 30px/700 #212529, padding-top 5px, then a full-width 1px rgba(0,0,0,0.1) rule with no top margin.
- **Bordered input/result panel** (inside videos): input views tiled 2×2 or single in square frames with a 2px pale green border (#dff1de family), "Input Image(s)" label in bold serif above, "Reconstruction" label in #6589bf below, and a large reconstruction render on white.
- **Video carousel**: Bootstrap carousel, one 16:9 rounded video per slide; prev/next controls are 50px circles of rgba(0,0,0,0.5) at 50% opacity with white chevrons, 25px from the edges; indicators are 15px rgba(0,0,0,0.5) dots.
- **BibTeX**: #e9eeef `pre`, 20px radius, padding 26.25px, 17.5px monospace, `white-space: pre-wrap`.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Tinted header band | yes | #ebf0f1 jumbotron, centred |
| Title with colour-coded concepts | yes | three paints on acronym letters and words |
| Venue | yes | gray 24px h4 |
| Authors / affiliations | yes | #007bff names, 20px affiliation and contribution notes |
| Link buttons | yes | three near-black 8px-radius buttons |
| Abstract | present but non-standard | opens with an animated video of the abstract sentence, then a short caption and the full paragraph |
| Results carousels | yes | three carousels of rounded 16:9 videos |
| Method figures | yes | 45% and 80% width images with justified text |
| Demo video | yes | rounded iframe |
| Results tables | absent from the source | results are videos only |
| BibTeX | yes | rounded #e9eeef well |
| Footer | yes | centred template credit |

## Adapting to Other Content

- **More authors**: keep inline #007bff names at 20px in the jumbotron; the centred line wraps at about seven names in the 1110px column; keep the contribution note line below the affiliations.
- **A results table**: put it under an `h3` + rule header in the 1110px column; Bootstrap `.table` at 20px Jost, header 700 #212529 with a 2px bottom border rgba(0,0,0,0.1); colour method names with the concept paints only when they name reconstruction (#6589bf) or animation (#78aa58) settings.
- **Long publication or news lists**: a section with the h3 + rule header and a 20px list, dates in 700; no cards.
- **More concepts**: give each new concept its own paint and use it in both the title and the captions; keep to at most four hues so the code stays readable.
- **More results**: add carousel slides (one 16:9 rounded video each) rather than grids.

## Do's and Don'ts

- Do colour-code the acronym letters and their expanded words in the title, and reuse the same colours in figure labels.
- Do keep the header a full-width #ebf0f1 band with everything centred.
- Do open each section with a left-aligned 30px heading and a 1px rgba(0,0,0,0.1) rule.
- Do round all videos at 10px and the BibTeX well at 20px.
- Don't use Bootstrap's default light button; buttons are #090f15 with #e2e2e2 labels.
- Don't use the three paints for links or UI chrome; links stay #007bff.
- Don't set the title below 900 weight; the painted words need the heavy Jost.

## Surfaces

A #ebf0f1 header band with slight rounding, then plain white sections; the BibTeX well #e9eeef; video frames have white backgrounds so the renders sit directly on the page.

## Imagery

Rendered clothed humans (full body, white background) shown as sparse input views in pale green square frames next to large novel-view and novel-pose reconstructions; method diagrams with neural texture maps; volumetric video applications. Media is presented as rounded 16:9 videos.

## Layout

A full-width centred header band, then a 1110px column of left-headed sections: Abstract, Sparse-view Results, Single-view Results, Method, Applications on Volumetric Video, Full Demo Video and BibTeX, each separated by a hairline rule under its heading.

## Agent Prompt Guide

Quick colors: band #ebf0f1, ink #212529, paints #6589bf / #78aa58 / #c68b5b, venue #5a6268, links #007bff, buttons #090f15 with #e2e2e2 text (hover #bec3c7), code well #e9eeef, rules rgba(0,0,0,0.1).

1. "Build a full-width header band: background #ebf0f1, padding 64px 32px, radius 4.8px, centred. Title Jost 45px weight 900 line-height 54px #212529, with the acronym letters and their expanded words coloured #6589bf, #78aa58 and #c68b5b. Below: 'SIGGRAPH 2025' Jost 24px/700 #5a6268, a 1px rgba(0,0,0,0.1) rule, author links Jost 20px/500 #007bff with superscripts, a 20px affiliation paragraph."
2. "Make dark buttons: background #090f15, label #e2e2e2 bold Jost 16px, border 1px solid #f8f9fa, radius 8px, padding 6px 24px, PDF icon at left; hover background #bec3c7 and text #212529."
3. "Create sections in a 1140px container: left-aligned h3 Jost 30px/700 #212529 with padding-top 5px, then a 1px rgba(0,0,0,0.1) rule with no top margin; 20px/500 justified body; videos at full column width with 10px radius; carousels with 50px rgba(0,0,0,0.5) round arrows at 50% opacity 25px inside the edges and 15px dots."

## Similar Pages

- Lior Yariv-template and ZJU3DV project pages (Bootstrap 4, jumbotron header, Jost or Source Sans).
- Pages that colour-code concept words in the title and carry the colours into figures.

## Quick Start

```css
:root {
  --band: #ebf0f1;
  --ink: #212529;
  --paint-reconstruction: #6589bf;
  --paint-animation: #78aa58;
  --paint-model: #c68b5b;
  --venue: #5a6268;
  --link: #007bff;
  --button: #090f15;
  --button-text: #e2e2e2;
  --button-hover: #bec3c7;
  --code-well: #e9eeef;
  --rule: rgba(0, 0, 0, 0.1);
  --font: "Jost", "Futura PT", sans-serif;
  --container: 1140px;
  --radius-media: 10px;
}
body { font-family: var(--font); font-weight: 500; font-size: 1.25em; color: var(--ink); }
```

## Provenance

- **URL**: https://zju3dv.github.io/humanram/
- **Paper**: HumanRAM: Feed-forward Human Reconstruction and Animation Model using Transformers (arXiv 2506.03118), Zhiyuan Yu, Zhe Li, Hujun Bao, Can Yang, Xiaowei Zhou.
- **Venue**: SIGGRAPH 2025 (Conference Track); the arXiv comment states "Accepted by SIGGRAPH 2025 (Conference Track)".
- **Selection reason**: a tinted header band and a multi-colour title that encodes the concepts, with the colours carried into the captions, plus bordered input/result panels and carousels.
- **Template credit**: footer thanks Lior Yariv for the website template and the LongVolCap project page for add-ons (Bootstrap 4.4.1 customised, Jost, Font Awesome 4.7 and 6.7, KaTeX).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), extra computed-style probes, the 1440×900 and full-page screenshots, and the page's `index.html` and `css/bootstrap-4.4.1.css` read directly, on 2026-10-28.
