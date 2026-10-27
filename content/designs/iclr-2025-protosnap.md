# ProtoSnap — Style Reference

> A museum label beside a clay tablet: plain system type, link-blue names, and one hand-annotated figure doing all the talking.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's `index.html`, which uses stock Bootstrap 4.6.0 plus one inline rule. The page links a `style.css` that returns 404, so nothing beyond Bootstrap defaults and inline attributes styles the render. The handwritten-looking labels and colored crop frames are part of the teaser image, not text.

## Overview

A plain Bootstrap 4 page with no custom stylesheet; its character comes from the figures. The body itself is the container (max-width 1050px, inline). A 40px regular-weight title in the system UI font opens the page, followed by six author names in bold Bootstrap blue (#007bff) with black superscripts, a line of bold blue affiliation links, a bold "* Equal Contribution" note, "ICLR 2025" at 28px regular weight, and two small outlined blue buttons (arXiv, Code) with icons. The 800px teaser shows a photographed clay tablet on black with three sign crops framed in red, blue and green, dashed leader lines, the black font prototype, the colored skeleton and the aligned output, all captioned in a handwriting font baked into the image. An italic bold-ish TL;DR line and a light Bootstrap `<hr>` follow. Each later section is a centred bold 24px heading, a paragraph (the abstract is justified in an 800px column; method text runs the full 1020px), and an 800px or smaller figure with an italic caption.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): #ffffff 74.8% (plus #f6f8f9 / #fffffd / #faffff 4.6%); clay brown #9a6542 8.7% and #e1cdb8 2.7% (tablet and sign crops); dark umber #3c2d25 4.8% (tablet shadows and black backing); gray #a7a7a1 4.4% (text and figure lines). Bootstrap blue is present only as thin text and button outlines.

Anatomy in DOM order (desktop 1440px; body content x=210–1230, centred):

1. **Title** (`p.h1.font-weight-normal`, y=48, one line): system UI 40px/400, line-height 1.2, #212529, centred; 48px top margin from Bootstrap `mt-5`. Gap 8px + 15px.
2. **Authors** (y=119): six names as `col-md-4` spans laid out inline, 16px/700, links #007bff, superscripts #212529. Gap about 6px.
3. **Affiliations** (y=146): four numbered institution links, 16px/700 #007bff.
4. **Equal contribution** (y=173): 16px/700 #212529. Gap 24px.
5. **Venue** (`p.h3.font-weight-normal`, y=218): "ICLR 2025", 28px/400 #212529. Gap about 30px.
6. **Buttons** (y=283, 38px tall): `btn btn-outline-primary`, arXiv (Academicons) and Code (Font Awesome GitHub), icon left, side by side and centred. Gap 24px.
7. **Teaser** (y=345, 800×414px): `<img width="800">` centred; handwriting captions inside the image.
8. **TL;DR** (y=763): `p.h6` italic, 16px/500 #212529, centred, wrapped at 800px.
9. **Rule and Abstract** (y≈820): Bootstrap `<hr>` (1px rgba(0,0,0,.1)), then "Abstract" 24px/700 centred and the justified abstract, which starts at the bottom of the viewport.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | (Bootstrap `body`) | page background |
| Bootstrap Ink | #212529 | (Bootstrap `body`) | title, venue, section headings, body text, superscripts, TL;DR |
| Bootstrap Blue | #007bff | `--primary` | author and affiliation links, inline links, outline button text and border |
| Hover Blue | #0056b3 | (Bootstrap `a:hover`) | link hover color |
| Rule | rgba(0,0,0,.1) | (Bootstrap `hr`) | section dividers |

The red, blue, green, yellow and purple used for crop frames and skeleton strokes live inside the figures, not in CSS.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| UI sans | Bootstrap system stack: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif | no web font loaded; Segoe UI on Windows, San Francisco on macOS | Inter |
| Mono | SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace | Consolas on Windows | JetBrains Mono |
| Icons | Font Awesome 4.7, Academicons | loaded | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `p.h1.font-weight-normal` | 2.5rem = 40px / 400 / 1.2 | #212529 |
| Venue | `p.h3.font-weight-normal` | 1.75rem = 28px / 400 / 1.2 | #212529 |
| Section heading | `p.h4.font-weight-bold.title` | 1.5rem = 24px / 700 / 1.2, centred | #212529 |
| Authors / affiliations | `div.h6.font-weight-bold` | 1rem = 16px / 700 / 1.2 | links #007bff |
| TL;DR and captions | `p.h6` with `<em>` | 16px / 500 italic / 1.2, centred | #212529 |
| Body | `body`, `p.abstract` | 16px / 400 / 1.5 (abstract justified) | #212529 |
| Button | `.btn` | 16px / 400 / 1.5 | #007bff |
| BibTeX | `pre` | 14px / 1.5 | #212529 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Outline buttons | 4px (.25rem) | 1px #007bff | focus ring 0 0 0 .2rem rgba(0,123,255,.5) |
| Section rules | 0 | 1px rgba(0,0,0,.1) top, margin 1rem 0 | none |
| Figures | 0 | none | none |
| BibTeX block | 0 | none | none |

Outline buttons fill with #007bff and turn white on hover (Bootstrap default).

## Layout Metrics

- **Container**: `<body class="container" style="max-width:1050px">`, so content is 1020px wide after 15px padding (x=210–1230 at 1440). The abstract row uses an inline `.container { max-width: 800px }` rule and sits at x=320–1120 with 15px padding.
- **Header spacing**: title row `mt-5 mb-3` (48px / 16px); author rows `mb-2`; equal-contribution row `mb-4`; buttons row `mb-4`.
- **Figures**: fixed `width` attributes, 800px for the teaser, results grid, similarity-volume diagram and data-flow figure; 500px for the evaluation plot; 600px for the OCR chart. All centred in `.row.justify-content-center`.
- **Sections**: each ends with an `<hr>` (16px margins); headings carry Bootstrap's 0.5rem bottom margin.
- **Page**: about 4,000px tall at 1440 wide.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1080px | (100% − 1050px)/2 + 15px | 16px | 40px | author spans inline on one line |
| 768–1079px | 15px | 16px | 40px | author spans `col-md-4` start wrapping |
| <830px | 15px | 16px | 40px | 800px figures are wider than the viewport, because Bootstrap 4 does not cap `img` width and the markup fixes `width="800"`; measured at 700px the document is 750px wide, and a 390px phone viewport lays the page out at 595px and zooms out |
| <576px | 15px | 16px | 40px | title wraps to several lines; buttons stay inline |

## Components

- **Outline button** (`a.btn.btn-outline-primary`): inline-block, padding 6px 12px (.375rem .75rem), 1px #007bff border, 4px radius, #007bff 16px/400 text with an icon left (Academicons arXiv, Font Awesome GitHub); hover background #007bff with white text.
- **Author row**: each author a `col-md-4 col-xs-6 pb-2` span used inline, bold 16px blue link plus a black numeric superscript; asterisks for equal contribution inside the link text.
- **Section heading**: `p.h4.font-weight-bold.title`, 24px/700, centred inline style, no rule above other than the previous section's `<hr>`.
- **Figure + italic caption**: `<img width="800">` centred, then `p.h6` with `<em>` (bold lead words in `<b>`), centred, wrapped at 800px by an extra `.container`.
- **BibTeX**: plain `<pre>` 14px mono on white, no box.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / authors / affiliations | yes | stock Bootstrap headings, bold blue links |
| Venue | yes | plain 28px "ICLR 2025" line |
| Link buttons | yes | two outlined Bootstrap buttons |
| Teaser | yes | 800px annotated figure with colored crops and handwriting labels |
| TL;DR | yes | italic centred line under the teaser |
| Abstract | yes | justified paragraph in an 800px column |
| Method figures | yes | similarity-volume diagram and data-flow strip |
| Results | yes | sample grid, evaluation plot, OCR chart (images, no HTML tables) |
| Acknowledgements | yes | plain paragraphs |
| BibTeX | yes | unboxed `<pre>` |
| Navigation, footer, video | absent from the source | — |

## Adapting to Other Content

- **More authors**: keep the inline bold blue names; beyond eight, drop to 15px and allow two lines rather than the `col-md-4` grid.
- **Responsive figures**: add `class="img-fluid"` (Bootstrap's `max-width: 100%; height: auto`) to every `<img width="800">` so figures stop overflowing on phones.
- **A results table**: use Bootstrap `table table-sm` at 800px, bold best values, no color fills; keep the italic caption below.
- **Long publication or news lists**: a Bootstrap `list-unstyled` list in the 800px column with dates in bold and links in #007bff.
- **A video**: Bootstrap `embed-responsive embed-responsive-16by9` at 800px, centred, with an italic caption.

## Do's and Don'ts

- Do let the figures carry the visual language: colored crop frames, dashed leader lines and hand-lettered labels inside the images.
- Do keep the chrome stock Bootstrap: system font, #212529 text, #007bff links, outlined buttons.
- Do centre headings and captions; justify only the abstract.
- Don't add color or background bands to the page; it stays white.
- Don't place figures wider than 800px.
- Don't keep fixed `width` attributes on images without `img-fluid` if the page must work on phones.

## Surfaces

White only. Separation comes from Bootstrap `<hr>` rules; no cards, fills or shadows.

## Imagery

Photographs of cuneiform tablets and sign crops in warm clay browns on black, black prototype glyphs, and skeletons drawn in saturated red, blue, green, yellow and purple; a results grid with rotated row labels (Prototype, Input, Global, +Refinement); a technical diagram of diffusion features and a 4D similarity volume; bar and line charts. Captions in the teaser and method strip use a handwriting typeface inside the images.

## Layout

Single centred column at up to 1020px: title block, buttons, teaser, TL;DR, then Abstract, How does it work?, Evaluation, Boosting Downstream OCR Performance, Acknowledgements and Citation, each separated by a rule. About 4,000px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: page #ffffff, text #212529, link #007bff, hover #0056b3, rule rgba(0,0,0,.1).

1. "Build a Bootstrap 4 header: body as `.container` with max-width 1050px; centred title in the system font at 40px/400 #212529 with 48px top margin; authors as bold 16px #007bff links with #212529 superscripts; affiliations the same; venue line 28px/400."
2. "Add outline buttons: `btn btn-outline-primary`, padding 6px 12px, 1px #007bff border, 4px radius, 16px #007bff text with an icon left; hover fills #007bff with white text; centred in one row."
3. "Present a figure: centred image at 800px (with `img-fluid`), then an italic 16px/500 #212529 caption centred and wrapped at 800px, then an `<hr>` with 1px rgba(0,0,0,.1)."

## Similar Pages

- Minimal Bootstrap project pages from university vision labs (TAU VAILab) where an annotated teaser is the main design element.
- Digital-humanities project pages that pair artefact photographs with computational overlays.

## Quick Start

```css
:root {
  --text: #212529;
  --link: #007bff;
  --link-hover: #0056b3;
  --rule: rgba(0, 0, 0, 0.1);
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  --font-mono: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --page-max: 1050px;
  --figure-max: 800px;
  --btn-radius: 4px;
}
img { max-width: 100%; height: auto; }
```

## Provenance

- **URL**: https://tau-vailab.github.io/ProtoSnap/
- **Paper**: ProtoSnap: Prototype Alignment for Cuneiform Signs (arXiv 2502.00129), Rachel Mikulinsky, Morris Alper, Shai Gordin, Enrique Jimenez, Yoram Cohen, Hadar Averbuch-Elor.
- **Venue**: ICLR 2025.
- **Selection reason**: the arXiv comment states acceptance at ICLR 2025 and links this project page.
- **Template credit**: none stated; stock Bootstrap 4.6.0 with Font Awesome 4.7 and Academicons; the linked `style.css` is missing (404).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, and the page HTML read directly, on 2026-10-28.
