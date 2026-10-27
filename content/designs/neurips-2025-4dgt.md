# 4DGT Mist Band — Style Reference

> A lab notebook bound in pale blue-grey cloth, its title stamped in copper and denim ink.

**Theme:** light

Measured from the rendered page at 1440×900 in headless Chrome (`computed_style.py`, screenshot and tall capture), then checked against the inline `<style>` block and the page's locally edited `css/bootstrap-4.4.1.css` (Zhen Xu's longvolcap template). Where the stylesheet and the render disagree, the render is reported. Pixel values are at the 1440px viewport unless a breakpoint is named.

## Overview

A Bootstrap 4 jumbotron page set entirely in Jost 500 at a large 20px base. The hero is a full-width pale blue-grey band (`#ebf0f1`) holding a three-line centred title: a grey "4DGT" wordmark at 56px/800, then two 40px/700 lines in near-black where the key phrases are tinted copper (`#c68b5b`) and denim (`#6589bf`). A slate venue line, a hairline rule, Bootstrap-blue author links and two black arXiv/Code buttons close the band. Below, on white, a bold grey-blue caption introduces a rounded 16:9 pipeline teaser video, then a second caption and a carousel of six-panel result videos with round translucent arrows. The abstract repeats the copper and denim colours on the same phrases as the title, which ties text to title. The rest is short: Method and Results heads with hairline rules, Bootstrap-blue "Click to Expand" collapse buttons for extra video grids, a rounded grey BibTeX block and a plain text footer. Document height is about 3,855px with the collapses closed.

## First Viewport

Color share of the first 1440×900 viewport: `#ebf0f1` 45.4% (hero band), `#fcfdfd` 16.7% (white page), `#616367` 15.3% (dark frames in the teaser video), `#d9dce0` 9.9% (teaser panel greys), `#ebf0ef` 6.2%, `#edf0f1` 3.1%, `#ebf0f2` 2.3% (teaser light-grey panel backgrounds), `#e6f2ed` 1.1%.

Anatomy in DOM order (all centred):

1. Hero band `div.jumbotron`, full width, `#ebf0f1`, padding 64px 32px; content starts at y=64. 
2. Wordmark "4DGT", `span` inside `h1`, Jost 56px/800, `#6c6c6c`, line-height 67px. Gap 0 (line break).
3. Title line 1 "Learning a 4D Gaussian Transformer", 40px/700, `#212529` with "4D Gaussian Transformer" in `#c68b5b`; line-height 48px.
4. Title line 2 "Using Real-World Monocular Videos", 40px/700, `#212529` with the phrase in `#6589bf`. Gap 8px.
5. Venue `h4` "NeurIPS 2025 (Spotlight)", 24px/700, `#5a6268`. Gap 16px to the rule.
6. `hr`, 1px `rgba(0,0,0,0.1)`, the width of the 1110px column. Gap 16px.
7. Authors, six `a` links in one line, 20px/500, `#007bff`, numeric superscripts.
8. Affiliations `p`, 20px/500, `#212529`; second line footnote "*Work done during internship at Meta." at 0.9em (18px) `#5a6268`. Gap 16px.
9. Buttons row: "arXiv" and "Code" black buttons, 107×38px, 6px apart, centred. Band ends about 32px below them (y≈473).
10. Gap 16px (jumbotron margin), then teaser caption in bold `#8899a5`, 20px, centred (y≈520).
11. Teaser video `video.a16x9`, 1090×488px at x=175, radius 22px, autoplay pipeline animation; it fills the rest of the viewport.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Mist Band | `#ebf0f1` | `.jumbotron` background | Hero band behind title, authors and buttons |
| Bootstrap Ink | `#212529` | Bootstrap body color | Title lines, affiliations, body text, headings, BibTeX text |
| Wordmark Grey | `#6c6c6c` | inline style | "4DGT" in the title and every "4DGT" mention in the abstract and method text (800 weight) |
| Copper | `#c68b5b` | inline style | "4D Gaussian Transformer" in the title; "4D Gaussian-based Transformer model" in the abstract |
| Denim | `#6589bf` | inline style | "Real-World Monocular Videos" in the title; "real-world monocular posed videos" in the abstract |
| Slate | `#5a6268` | inline style | Venue `h4`, internship footnote |
| Caption Blue-Grey | `#8899a5` | inline style on `b` | Bold captions above the teaser and the carousel |
| Link Blue | `#007bff` | Bootstrap `a`, `.btn-primary` | Author names, dataset links, footer links; "Click to Expand" button fill |
| Link Hover | `#0056b3` | Bootstrap `a:hover` | Link hover colour (with underline) |
| Button Black | `#090f15` | `.btn-light` (edited) | arXiv and Code button fill |
| Button Label | `#e2e2e2` | `.btn-light` (edited) | arXiv and Code button text and icons |
| Button Edge | `#f8f9fa` | `.btn-light` border | 1px border of arXiv and Code buttons |
| Button Hover | `#bec3c7` | `.btn-light:hover` | Hero button hover fill (label turns `#212529`) |
| Button Hover Edge | `#dae0e5` | `.btn-light:hover` border | Hero button hover border |
| Unrendered Ring | `rgba(52,58,64,0.5)` (`#343a40` at 50%) | `.btn` box-shadow | Declared on all buttons, not visible in the render |
| Code Grey | `#e9eeef` | inline style on `pre` | BibTeX block |
| Rule | `rgba(0,0,0,0.1)` | Bootstrap `hr` | Hero rule, rules under section heads |
| Control Scrim | `rgba(0,0,0,0.5)` | `.carousel-control-*`, `.indicator-dot` | Round carousel arrows and dots |
| Page | `#ffffff` | `body` | Everything below the hero |

## Tokens — Typography

- **Declared:** `body { font-family: 'Jost'; font-weight: 500; font-size: 1.25em }` from Google Fonts (weights 300–900 requested). Bootstrap's own stack is overridden.
- **Rendered:** Jost 400, 500, 700, 800, 900 loaded (`fonts_loaded`); icons from FontAwesome 4.7 and Academicons. Substitute: Futura PT, or Outfit for a free geometric sans with the same round "o" and short x-height.
- **Mono:** Bootstrap `SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace` in the BibTeX block (Consolas on Windows).

| Role | Selector | Size | Weight | Line height | Colour |
|---|---|---|---|---|---|
| Wordmark | `h1 > span` (inline 1.4em) | 56px | 800 | 67.2px | `#6c6c6c` |
| Title lines | `h1` (inline 2.0em) | 40px | 700 | 48px | `#212529` + tinted spans |
| Venue | `h4` | 24px | 700 | 28.8px | `#5a6268` |
| Section head | `h3` (1.5em) | 30px | 700 | 36px | `#212529`, 30px padding-top |
| Collapse row label | `h5` | 20px (Bootstrap 1.25rem, root-relative) | 700 | 1.2 | `#212529` |
| Body, authors, abstract | `body`, `p` | 20px | 500 | 30px | `#212529`; abstract justified |
| Caption | `b[style*=8899a5]` | 20px | 700 (bolder) | 30px | `#8899a5`, centred |
| Footnote | inline 0.9em | 18px | 500 | 30px | `#5a6268` |
| Buttons | `.btn` | 16px | 400 (label in `b`, 700) | 24px | see Components |
| BibTeX | `pre` (inline 0.75em) | 15px | 500 | 22.5px | `#212529` |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Hero band `.jumbotron` | 0.3rem (4.8px), visible only as softened corners at the band's bottom |
| Hero buttons and "Click to Expand" | 8px (Bootstrap `.btn` edited to 0.5rem) |
| Teaser video | 22px (inline 1.1em) |
| Other videos, comparison canvases | 10px |
| BibTeX `pre` | 20px |
| Carousel arrows | 50% (50px circles); dots 10px radius on 15px squares |

- **Shadows:** none rendered. The edited `.btn` rule declares `box-shadow: 0 0 0 0.2rem rgba(52,58,64,0.5)`, but the computed style shows none on the hero buttons (see Declared but not visible under Components).
- **Borders:** hero buttons 1px `#f8f9fa`; `hr` 1px `rgba(0,0,0,0.1)`.
- **Motion:** `.zoom-element` rows scale to 1.25 on hover with a 0.2s ease-in-out transform. This applies to the teaser and to the expandable video grids.

## Layout Metrics

- **Container:** Bootstrap `.container`, `max-width: 1140px` at ≥1200px with 15px side padding, so text columns are 1110px wide (x=165 to 1275 at 1440px).
- **Hero:** full-bleed `.jumbotron` (not inside the container), padding 64px 32px at ≥576px, margin-bottom 16px; band height about 473px at 1440px.
- **Sections:** no section padding; section heads get 30px top padding from `.col-12 > h3` and an `hr` with `margin-top: 0` beneath. Collapse rows (`.results-section`) have 30px bottom padding. Two `<br>` precede the Citation head.
- **Video grids:** `.row.sm-gutters` with 5px margins and 5px column padding, so tiles sit 10px apart; teaser 1090px wide (column minus 10px), result grids in `col-md-6` (two up) or `col-md-4` (three up), aspect ratios fixed by classes (`.a16x9`, `.a32`, `.a4x3` …).
- **Carousel:** full column width; arrows 50px circles 25px in from each side, vertically centred; indicator dots at 10% from the bottom, 90% from the left.

| Breakpoint | Container | Hero padding | Body size | Title size | Grid change |
|---|---|---|---|---|---|
| ≥1200px | 1140px | 64px 32px | 20px | 40px (wordmark 56px) | `col-md-*` grids side by side |
| 992–1199px | 960px | 64px 32px | 20px | 40px | same |
| 768–991px | 720px | 64px 32px | 20px | 40px | same |
| 576–767px | 540px | 64px 32px | 20px | 40px | `col-md-*` tiles stack to one column; mobile video sources (`_x0.5.mp4`) swapped in by script |
| <576px | fluid, 15px gutters | 0 (the template commented out Bootstrap's 2rem 1rem) | 20px | 40px | one column |

## Components

- **Two-tone title.** `h1` at 2.0em/700 with a `<br>`-split structure: grey 1.4em/800 wordmark, then two lines whose key phrases carry `#c68b5b` and `#6589bf`. Use exactly two accent hues and repeat them on the same phrases in the abstract.
- **Black hero button.** `a.btn.btn-large.btn-light`: `#090f15` fill, `#e2e2e2` label, 1px `#f8f9fa` border, 8px radius, padding 6px 24px, Jost 16px with the label in bold; icon left (Academicons `ai-arxiv`, FontAwesome `fa-github`). Hover: fill `#bec3c7`, label `#212529`, border `#dae0e5`. Each button sits in its own `.column > p.mb-5`.
- **Caption line.** Bold 20px `#8899a5` centred sentence above a figure; dataset names inside it are italic bold `#007bff` links.
- **Zoom video row.** `video` in a `.row.sm-gutters.zoom-element`, autoplay muted loop, `img/spinner.svg` poster, 10px radius (22px for the teaser), whole row scales 1.25× on hover.
- **Result carousel.** Bootstrap `.carousel.slide`, 100s interval; 50px round `rgba(0,0,0,0.5)` arrows with white chevrons; 15px `rgba(0,0,0,0.5)` dots. Each slide is a six-panel video (Normal, Render, Reference over flow, motion and depth).
- **Expand button.** `button.btn.btn-primary` "Click to Expand" (text switches by script): `#007bff` fill and border, white 16px label, 8px radius, padding 6px 12px, inline at the start of an `h5` that names the datasets.
- **Section head.** `h3` 30px/700 `#212529` with 30px top padding, immediately followed by an `hr` (`margin-top: 0`).
- **BibTeX block.** `pre` with `#e9eeef` fill, 22.5px padding, 20px radius, 15px mono `#212529`, `white-space: pre-wrap`.
- **Footer.** Plain `footer` text at 20px/500 in the container: template credit (Zhen Xu, longvolcap) and acknowledgements, links in `#007bff`.
- **Declared but not visible.** `.btn` box-shadow `0 0 0 0.2rem rgba(52,58,64,0.5)` (computed none); `.bibtexsection` Courier 16px style (unused class).

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / author block | Yes | Mist band, two-tone title, blue author links, affiliations and footnote |
| Venue badge | Yes, as text | Slate bold `h4` "NeurIPS 2025 (Spotlight)" |
| Link buttons | arXiv, Code | Black 8px-radius buttons; a Demo button is commented out in the source |
| Teaser | Yes | 16:9 autoplay pipeline video, 22px radius, zoom on hover |
| Result carousel | Yes | Six-panel videos with round translucent controls |
| Abstract | Yes, no heading | Justified 20px paragraph with copper and denim emphasis |
| Method | Yes | `h3` + rule, justified text, method video |
| Extra results | Yes | Four "Click to Expand" collapses with two- or three-up video grids |
| Results table | Absent from the source | |
| BibTeX | Yes | Rounded `#e9eeef` `pre` |
| Footer | Yes | Plain text acknowledgements |
| Navbar, sliders, 3D viewer, math | Absent (KaTeX is loaded but no formula renders on the page) | |

## Adapting to Other Content

- **More authors:** keep one centred run of 20px `#007bff` links and let it wrap; move affiliations to a second line and keep the 0.9em `#5a6268` footnote under them.
- **More buttons:** add more `.column > p.mb-5` black buttons; they stay 6px apart and wrap as a centred row.
- **A results table:** place it under an `h3` + `hr` head, 20px Jost body, bold header row in `#212529`, best scores in `#c68b5b`, second-best in `#6589bf`, so the table reuses the title's two accents; put it on white, not on the band.
- **Long galleries:** follow the page's own pattern of collapsed sections behind `#007bff` "Click to Expand" buttons with `sm-gutters` two- or three-up video rows.
- **News or updates:** a short list just above the teaser caption, 20px/500 `#212529` with bold dates in `#5a6268`, no card.

## Do's and Don'ts

- Do keep the hero as one flat `#ebf0f1` band and the rest of the page white.
- Do limit accent colour to `#c68b5b` and `#6589bf`, and repeat each on the same phrase in title and abstract.
- Do keep Jost at 500 for body text; the medium weight is part of the look.
- Do round all media (10px, teaser 22px) and keep 10px gaps between tiles.
- Don't give the black hero buttons a coloured fill; the only coloured buttons are the blue expand toggles.
- Don't add section bands or cards below the hero; separation comes from `h3` + hairline rules.

## Surfaces

One flat `#ebf0f1` hero band across the full width, then white for the whole page. The only other surface is the `#e9eeef` BibTeX block with a 20px radius. Media carry their own colour; light-grey panels inside the teaser video account for much of the first-viewport grey.

## Imagery

Autoplay MP4 videos of egocentric scenes (Ego-Exo4D, AEA, Aria datasets): a pipeline teaser animation, six-panel normal/render/reference/flow/mask/depth composites, and two- or three-up comparison videos. A spinner SVG is used as the poster while each video loads.

## Layout

Single 1110px centred column inside a Bootstrap container. The hero band is full-bleed; everything else is in the column, with media spanning its full width and grids splitting it into halves or thirds.

## Agent Prompt Guide

Quick colors: band `#ebf0f1`, text `#212529`, wordmark `#6c6c6c`, accents `#c68b5b` and `#6589bf`, venue `#5a6268`, caption `#8899a5`, link `#007bff`, button `#090f15` with `#e2e2e2` label, code `#e9eeef`.

1. "Build a full-width hero band in `#ebf0f1` with 64px 32px padding: a centred 56px/800 Jost wordmark in `#6c6c6c`, then two 40px/700 title lines in `#212529` with one phrase coloured `#c68b5b` and one `#6589bf`, a 24px/700 venue line in `#5a6268`, a 1px `rgba(0,0,0,0.1)` rule, and 20px/500 author links in `#007bff`."
2. "Make hero buttons: `#090f15` fill, `#e2e2e2` bold Jost 16px label with a left icon, 1px `#f8f9fa` border, 8px radius, padding 6px 24px; hover fill `#bec3c7` with `#212529` label."
3. "Add a figure block: a bold 20px `#8899a5` centred caption, then a 16:9 autoplay video at full column width with 22px radius that scales to 1.25 on hover over 0.2s."

## Similar Pages

Other pages on Zhen Xu's longvolcap template (ZJU 3DV group) share the jumbotron band, Jost type and black buttons. Within this NeurIPS 2025 batch, BlurDM also uses a coloured full-width hero band, but with a gradient and white type.

## Quick Start

```css
:root {
  --band: #ebf0f1;
  --ink: #212529;
  --wordmark: #6c6c6c;
  --accent-1: #c68b5b;
  --accent-2: #6589bf;
  --venue: #5a6268;
  --caption: #8899a5;
  --link: #007bff;
  --link-hover: #0056b3;
  --btn: #090f15;
  --btn-label: #e2e2e2;
  --btn-hover: #bec3c7;
  --code-bg: #e9eeef;
  --rule: rgba(0, 0, 0, 0.1);
  --font: 'Jost', 'Outfit', sans-serif;
  --fs-body: 20px;
  --radius-btn: 8px;
  --radius-media: 10px;
  --radius-teaser: 22px;
  --radius-code: 20px;
}
body { font-family: var(--font); font-weight: 500; font-size: var(--fs-body); color: var(--ink); }
.hero { background: var(--band); padding: 64px 32px; text-align: center; }
```

## Provenance

- **URL:** https://4dgt.github.io/
- **Paper:** 4DGT: Learning a 4D Gaussian Transformer Using Real-World Monocular Videos (arXiv 2506.08015), Zhen Xu, Zhengqin Li, Zhao Dong, Xiaowei Zhou, Richard Newcombe, Zhaoyang Lv (Reality Labs Research, Meta; Zhejiang University).
- **Venue:** NeurIPS 2025 Spotlight (shown on the page as "NeurIPS 2025 (Spotlight)").
- **Selection reason:** existing entry; the arXiv comment states acceptance at NeurIPS 2025 and links the project page.
- **Template credit:** footer thanks Zhen Xu for the template (zju3dv longvolcap).
- **Evidence used:** `computed_style.py` render at 1440×900 with first-viewport color share, the 1440 screenshot and tall capture, the inline `<style>` block and the edited `css/bootstrap-4.4.1.css`. Captured 2026-10-28.
