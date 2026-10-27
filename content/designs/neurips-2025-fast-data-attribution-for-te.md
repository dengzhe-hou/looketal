# FastGDA Plain Paper — Style Reference

> A preprint pinned to a corkboard: plain grey Helvetica, blue bracketed links, and the plots doing all the talking.

**Theme:** light

Measured from the rendered page at 1440×900 in headless Chrome (`computed_style.py`, screenshot and tall capture), then checked against the single inline `<style>` block in `index.html`. The page has no external stylesheet and loads no web fonts. Where stylesheet and render disagree, the render is reported. Pixel values are at the 1440px viewport.

## Overview

The classic table-layout academic page (the Phillip Isola and Richard Zhang lineage used across CMU and Berkeley graphics labs). A fixed 1100px body is centred on white, every block centred with `<center>` and laid out with HTML tables. The title is a plain 32px line. Authors sit in a five-cell table in link blue `#1367a7`, affiliations in a second table, and two bracketed text links "[Code]" and "[Paper (NeurIPS 2025)]" in a third. A 960px pipeline teaser follows. Sections are divided by `hr`s drawn as a 1px horizontal gradient that fades out at both ends, and each section has a centred light-weight `h2`. The Results section is the core of the page: large, legible plots (a throughput-versus-attribution scatter with "~437,000x speedup" arrows, a before/after mAP bar chart) and wide qualitative retrieval grids, each introduced by a bold lead-in sentence. A Paper section with a layered-paper thumbnail, acknowledgements and a light-grey BibTeX block close the page. Document height is about 6,276px.

## First Viewport

Color share of the first 1440×900 viewport: `#ffffff` 68.8% (page), `#a9afb9` 9.9% (blue-grey panels in the teaser diagram), `#79716d` 6.1% (training-image photos), `#eaedee` 5.0% (light grey teaser panel), `#d0d8d4` 4.6% (pale green "Distill" arrow), `#f6f6f5` 3.8%, `#fdffff` 1.0%, `#fffffc` 0.7%.

Anatomy in DOM order (all centred in a 1100px body starting at x=170):

1. `<br>`, then title `span` "Fast Data Attribution for Text-to-Image Models", 32px, weight 300 declared (renders as Arial regular, see Typography), `#000000`, top at y=29. Two `<br>`s follow (gap about 22px).
2. Authors table, 850px wide, five cells: names as `a` at 20px, `#1367a7`, superscript numbers in `#000000`; "Aaron Hertzmann" wraps to two lines in its 175px cell (y=87 to 144).
3. Affiliations table, 700px wide: "¹Carnegie Mellon University", "²Adobe Research", "³UC Berkeley" at 20px `#000000`; the first wraps to two lines (y=144 to 201).
4. Links table, 500px wide, each cell starting with a `<br>`: "[Code]" and "[Paper (NeurIPS 2025)]" at 20px `#1367a7` (y=221). Gap about 25px.
5. Teaser table, 1000px wide, holding `files/teaser.jpg` at 960×422px (y=271 to 693): the slow unlearning teacher above, the fast learned embedding below, a pale green "Distill by Learning to rank" arrow at right.
6. `hr` (gradient fade line) at about y=705.
7. `h2` "Abstract", 27px, weight 300, centred, at y=729; justified 18px abstract paragraph starts about y=780 and runs past the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Ink | `#000000` | default text | Title, headings, body text, affiliations, superscripts |
| Link Blue | `#1367a7` | `a:link, a:visited` | Author names, [Code], [Paper], inline citations, [Bibtex] |
| Link Teal | `#208799` | `a:hover` | Link hover colour (no underline at any state) |
| Page | `#ffffff` | browser default | Page background |
| Rule Fade | `rgba(0,0,0,0.75)` | `hr` gradient centre | Section dividers fading to transparent at both ends |
| Code Grey | `#d3d3d3` | inline style on `code` | BibTeX block |
| Paper Shadow | `rgba(0,0,0,0.35)` | `.layered-paper-big` | Stacked-sheet outline around the paper thumbnail |
| Disclaimer Grey | `#eeeeee` | `.disclaimerbox` | Declared callout fill and border, unused on this page |

## Tokens — Typography

- **Declared:** `body { font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif; font-weight: 300; font-size: 18px; text-align: justify }`; `h1, h2 { font-weight: 300 }`; `b, strong { font-weight: 700 }`.
- **Rendered:** no web fonts load (`fonts_loaded` is empty). On the Windows capture machine the stack resolves to Arial, which has no 300 weight, so all "light" text renders at Arial regular. On macOS the same CSS renders in Helvetica Neue Light, which is visibly thinner. Substitute: Helvetica Neue Light where available; on the web, Inter at 300 gives the same neutral grotesque at light weight.
- **Mono:** browser `monospace` (Consolas / Courier New) in the BibTeX `code`.

| Role | Selector | Size | Weight | Line height | Colour |
|---|---|---|---|---|---|
| Title | `center > span[style*=32px]` | 32px | 300 | normal | `#000000` |
| Section head | `center > h2` | 27px (1.5em) | 300 | normal | `#000000`, centred |
| Acknowledgements head | `h2` inside a table cell | 24px (table resets the 18px base) | 300 | normal | `#000000` |
| Authors, affiliations, links | `span[style*=20px]` | 20px | 400 (table cells reset weight) | normal | names `#1367a7`, rest `#000000` |
| Body | `body`, `p` | 18px | 300 | normal (about 1.15) | `#000000`, justified |
| Lead-in | `p > b` | 18px | 700 | normal | `#000000` |
| Paper citation | `span[style*=12pt]` | 16px | 300 / 700 for title | normal | `#000000` |
| [Bibtex] link | `span[style*=22px]` | 22px | 400 | normal | `#1367a7` |
| BibTeX | `code` | 18px | 300 | normal | `#000000` |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Everything rendered | 0 (square) |
| `img.rounded`, `img.header-img`, `.disclaimerbox` (declared, unused) | 10px |

- **Shadows:** only the paper thumbnail, `.layered-paper-big`: a 1px `rgba(0,0,0,0.35)` outline repeated with white sheets at 5px offsets up to 25px, so the first page looks like a stack of six sheets.
- **Borders:** none; `hr` is `border: 0; height: 1px` with `linear-gradient(to right, rgba(0,0,0,0), rgba(0,0,0,0.75), rgba(0,0,0,0))`.
- **Motion:** none.

## Layout Metrics

- **Container:** `body { width: 1100px; margin: 8px auto }`, so content runs x=170 to 1270 at 1440px. No max-width or fluid behaviour.
- **Header tables:** authors 850px, affiliations 700px, links 500px, teaser 1000px, all `align="center"`.
- **Figures:** set by `width` attributes: teaser 960px, scatter and bar plots 900px, qualitative grids 1100px (full body width).
- **Vertical rhythm:** `<br>` and `<hr>` pairs between sections; `h2` margins 22.4px top and bottom; paragraphs use default 18px margins.
- **Paper block:** a 700px table with a 175px-tall thumbnail (10px left, 45px right margin) beside three 12pt lines.

| Breakpoint | Container | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|---|
| ≥1116px | 1100px | (viewport − 1100) / 2 | 18px | 32px | none |
| <1116px | 1100px (fixed) | 0; page scrolls horizontally | 18px | 32px | none; there are no media queries |

## Components

- **Plain title block.** Centred 32px light title, then tables of 20px author links in `#1367a7` with black superscripts, affiliations in black, and bracketed text links; no buttons, no icons.
- **Fade rule.** `hr` with `border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0,0,0,0), rgba(0,0,0,0.75), rgba(0,0,0,0))`, spanning the 1100px body.
- **Section head.** `<center><h2>` at 27px, weight 300, no rule or colour.
- **Result block.** A `p` with a bold lead-in sentence ("Attribution performance vs. throughput (MSCOCO Models).") followed by a plain explanation, then a centred figure at 900px or 1100px. The plots carry their own colour (green and orange bars, blue speedup arrows).
- **Layered-paper thumbnail.** `img.layered-paper-big` 175px tall, stacked-sheet shadow, linked to arXiv, beside the citation in 12pt with the paper title bold.
- **BibTeX block.** `code` with `display: block; background: #d3d3d3`, no padding, no radius, lines broken by `<br>` and `&nbsp;`.
- **Declared but not visible.** `#toggleButton` (bold 26pt underlined `darkorchid` "Click here for more results"), `.disclaimerbox` (`#eeeeee`, 10px radius, 20px padding), `video.header-vid` and `img.header-img` (1px black border, 10px radius). None appear in the markup.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / author block | Yes | Centred tables, blue name links |
| Venue badge | As link text | "[Paper (NeurIPS 2025)]" |
| Link buttons | Present but non-standard | Bracketed text links [Code], [Paper (NeurIPS 2025)]; Slides and Poster links commented out |
| Teaser | Yes | 960px pipeline figure |
| Abstract | Yes | Justified 18px paragraph |
| Results plots | Yes | Scatter with speedup arrows, bar chart, at 900px |
| Qualitative grids | Yes | MSCOCO and LAION retrieval grids at 1100px |
| Method section, related works | Commented out in the source | |
| Paper thumbnail | Yes | Layered-paper shadow |
| BibTeX | Yes | `#d3d3d3` block; also a [Bibtex] link to a .txt file |
| Acknowledgements | Yes | Centred `h2` and paragraph in a table |
| Video, carousel, slider, results table | Absent from the source | |

## Adapting to Other Content

- **More authors:** add cells to the authors table and widen it toward 1100px; at 175px per cell long names wrap to two lines, as "Aaron Hertzmann" does, so widen cells before adding a second row.
- **More links:** add bracketed `[Slides]`, `[Poster]`, `[Data]` cells to the links table at 20px `#1367a7`.
- **A results table:** a centred HTML table at 900px with 18px body text, a bold header row, 1px black top and bottom rules only, and the best number in bold; keep it plain to match the page.
- **More results:** repeat the result-block pattern (bold lead-in, explanation, centred 900px figure) separated by fade rules.
- **News:** a short `ul` of dated items under the links table, 18px with bold dates.

## Do's and Don'ts

- Do let the figures carry colour and hierarchy; the page itself is black, white and one link blue.
- Do open every result with a bold lead-in sentence that states the finding.
- Do separate sections with the gradient fade `hr`, never a solid line.
- Do declare a web font if the light weight matters; without Helvetica Neue the page renders in regular-weight Arial.
- Don't add buttons, cards or background bands.
- Don't expect it to reflow: the 1100px fixed body scrolls sideways on phones.

## Surfaces

A single white surface. The only other fills are the `#d3d3d3` BibTeX block and the white sheets of the layered-paper shadow.

## Imagery

A pipeline diagram (orange model blocks, blue embedding band, green distillation arrow), result plots exported as JPEGs at high resolution (a log-scale scatter with labelled methods and memory sizes, an mAP bar chart with error bars), and qualitative retrieval grids of training images in rows labelled "DINO + CLIP Text", "Ours" and "Ground Truth".

## Layout

One fixed 1100px centred column built from HTML tables and `<center>` tags. Figures are sized by `width` attributes and centred; text is justified to the full 1100px.

## Agent Prompt Guide

Quick colors: text `#000000`, link `#1367a7`, hover `#208799`, page `#ffffff`, code `#d3d3d3`, rule `rgba(0,0,0,0.75)` fading to transparent.

1. "Build a centred header in a fixed 1100px body: a 32px weight-300 Helvetica Neue title, a table of five 20px author links in `#1367a7` with black superscripts, a table of affiliations in black, and bracketed text links [Code] and [Paper] at 20px `#1367a7`, hover `#208799`, no underline."
2. "Separate sections with `hr { border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0,0,0,0), rgba(0,0,0,0.75), rgba(0,0,0,0)); }` and centred 27px weight-300 `h2` headings."
3. "Write a result block: an 18px justified paragraph opening with a bold lead-in sentence, then a centred 900px plot image with no border, radius or shadow."

## Similar Pages

The same template appears on many CMU (Jun-Yan Zhu) and Berkeley (Efros, Isola) project pages, for example pix2pix and CycleGAN. In this NeurIPS 2025 batch, it is the plainest page; GOATex is the next most restrained.

## Quick Start

```css
:root {
  --ink: #000000;
  --link: #1367a7;
  --link-hover: #208799;
  --page: #ffffff;
  --code-bg: #d3d3d3;
  --font: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, sans-serif;
}
body { font-family: var(--font); font-weight: 300; font-size: 18px; width: 1100px; margin: 8px auto; text-align: justify; color: var(--ink); }
a:link, a:visited { color: var(--link); text-decoration: none; }
a:hover { color: var(--link-hover); }
h2 { font-weight: 300; text-align: center; }
hr { border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0)); }
```

## Provenance

- **URL:** https://peterwang512.github.io/FastGDA/
- **Paper:** Fast Data Attribution for Text-to-Image Models (arXiv 2511.10721), Sheng-Yu Wang, Aaron Hertzmann, Alexei A. Efros, Richard Zhang, Jun-Yan Zhu (Carnegie Mellon University, Adobe Research, UC Berkeley).
- **Venue:** NeurIPS 2025 (the page's paper link reads "[Paper (NeurIPS 2025)]").
- **Selection reason:** the arXiv comment states acceptance at NeurIPS 2025 and links the project page.
- **Template credit:** no credit on the page; the markup and `layered-paper` CSS are the widely reused Isola/Zhang project-page template.
- **Evidence used:** `computed_style.py` render at 1440×900 with first-viewport color share, the 1440 screenshot and tall capture, and the inline `<style>` block and markup of `index.html`. Captured 2026-10-28.
