# SpatialLLM Distill Article — Style Reference

> A clean research article on white paper, its contents list pinned in the margin like a printed journal.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 screenshot, scrolled captures of the full 4,895px page, renders at 1100, 900 and 390px for the responsive table, the page's own `style.css` and the inline `<style>` in the markup. The article body is the Distill template (`template.v2.js`, custom elements `d-article`, `d-contents`, `d-figure`, `d-cite`, `d-appendix`); the header and buttons are the authors' CSS, adapted from the Image Sculpting page. No web fonts load: every role uses the system UI stack. Color share is measured on the first 1440×900 viewport.

## Overview

The page reads like a well-set paper. A plain white header centres a bold 32px title, a bold "CVPR 2025" with "(highlight)" in pure red, bold dark-blue author names spaced with em-spaces, blue affiliation links and two chunky pill buttons in pale sky blue with a near-black 2px outline and a drop shadow. A full-width hairline then opens the Distill article: a "CONTENTS" list sits in the left margin with a hairline to its right, beside a 704px justified reading column at 16.96px with 1.7 line height. Figures fill the column with grey 13px captions led by a bold "Figure N.", section heads are 36px semibold with a hairline underneath, findings are set as bold justified sentences (one ending in a coral "=> 3D awareness of visual encoder is important!"), and results tables appear as LaTeX-typeset images. Data & Code uses small GitHub and Hugging Face badges, and the Distill appendix at the end sets BibTeX, Notes and References in a grey two-column grid.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 83.0%, warm grey #b4b3ae 4.5% and pale sage #d5d9d6 4.0% (the teaser figure's photo and pastel boxes), charcoal #484748 3.5% (text), off-whites #f1f3f2 2.3% and #fcfbf7 1.2% (figure boxes), traces under 1%. The sky-blue buttons and the red "(highlight)" are each under 1%.

Anatomy in DOM order (`.header-container` flex, padding 50px; `.header-content` max-width calc(50% − 20px) = 650px, centred at x=395):

1. **Title** — `.header-content h1` (inline `font-size: 2em`), 32px / 700 / line-height 38.4px, system UI (Segoe UI on the capture machine), #000000, centred, three lines (y=71–186). Gap 19px.
2. **Venue** — `h3`, "CVPR 2025" 18.72px / 700 #000000 with `<span style="color: red;">(highlight)</span>` in #ff0000 (y=205–231). Gap 19px.
3. **Authors and affiliations** — one `p`, 16px / 25.6px, centred; names are `<a><b>…</b><sup>n</sup></a>` in #004276 bold separated by `&emsp;`, two names on the first line and three on the second; affiliations on a third line as #004276 regular links (y=250–327). Gap 20px.
4. **Buttons** — `.button-container a.button` "arXiv" and "Data & Code", 16px / 700 #000000 on #aed6f1, 2px solid #231f19, radius 25px, padding 10px 20px, margin 5px, shadow `0 4px 8px rgba(0,0,0,0.2)`; each 50px tall (y=347–397). Gap 55px.
5. **Article rule** — `d-article` starts at y=452 with a 1px rgba(0,0,0,0.1) top border across the full width, then 32px padding.
6. **Contents** — `d-contents` in grid columns 1–3, right-aligned to the text: "CONTENTS" 14px / 600 uppercase, then four links 13px / 600 rgba(0,0,0,0.8), one per row; padding-right 50.88px, 1px rgba(0,0,0,0.1) right border (x=167–336, y=490–681). Not sticky in the render; it stays at the top of the article.
7. **Lead paragraph** — 16.96px / 28.83px justified rgba(0,0,0,0.8), 704px column from x=368 (y=485–629), "SpatialLLM" bold. Gap 43px.
8. **Figure 1** — `d-figure > figure > img` max-height 360px, 704px wide (y=672–1032), caption below at y=1039. The fold cuts the figure.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | `.header-container`, Distill default | page and header background |
| Ink | #000000 | `.header-container` color | title, venue, button labels |
| Article Ink | rgba(0,0,0,0.8) | Distill `d-article` color | body text, section heads, contents links, list items |
| Caption Grey | rgba(0,0,0,0.6) | Distill `figcaption` | figure captions |
| Appendix Grey | rgba(0,0,0,0.5) | Distill `d-appendix` | appendix text (headings rgba(0,0,0,0.65)) |
| Hairline | rgba(0,0,0,0.1) | Distill borders, `d-contents` | article top rule, h2 underline, contents right rule, appendix top rule |
| Author Navy | #004276 | Distill global `a` color | author names, affiliation links |
| Button Sky | #aed6f1 | `.button-container a.button` | button fill |
| Button Edge | #231f19 | `.button-container a.button` | 2px button border |
| Button Hover | #3498db | `.button-container a.button:hover` | hover fill (text turns #ffffff) |
| Hover Gold | #ffcc00 | inline `.button:hover span` | hover color declared for button spans and Bulma-style links |
| Highlight Red | #ff0000 | inline `style="color: red;"` | "(highlight)" in the venue line |
| Finding Coral | #f66b4d | inline `style="color: #F66B4D;"` | the "=> 3D awareness of visual encoder is important!" emphasis |
| Figure Grey | #b4b3ae | (screenshot) | dominant non-white tone of the first viewport (teaser photo) |

## Tokens — Typography

- **UI stack:** Distill's `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", Arial, sans-serif`; no web fonts are loaded (`fonts_loaded` is empty), so it renders Segoe UI on Windows and San Francisco on macOS. Substitute: Inter. Despite the paper-like layout there is no serif face anywhere.
- **Math:** KaTeX 0.10.2 CSS is linked for inline math.
- **Code:** BibTeX in the appendix uses Distill's monospace `pre` at appendix size.

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `.header-content h1` (inline 2em) | 32px / 700 / 38.4px, centred |
| Venue | `.header-content h3` | 18.72px / 700 |
| Authors | `.header-content p a b` | 16px / 700 / 25.6px |
| Buttons | `.button-container a.button` | 16px / 700 |
| Contents heading | `d-contents nav h4` | 14px / 600, uppercase |
| Contents links | `d-contents nav > div > a` | 13px / 600 |
| Section heads | `d-article h2` | 36px / 600 / 45px, 16px padding-bottom, 1px hairline below |
| Body | `d-article p`, `li` | 16.96px (1.06rem) / 400 / 28.83px (1.7), justified (inline) |
| Findings | `p > b` (inline justified) | 16.96px / 700 |
| Captions | `figcaption` | 13px / 400 / 19.5px, "Figure N." in 700 |
| Appendix headings | `d-appendix h3` | 15px / 500 |
| Appendix text | `d-appendix` | 12.8px / 400 / 21.76px |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Buttons | radius 25px, 2px solid #231f19, padding 10px 20px, margin 5px, shadow `0 4px 8px rgba(0,0,0,0.2)` |
| Section heads | 1px rgba(0,0,0,0.1) bottom border, padding-bottom 16px, margin 32px 0 24px |
| Contents | 1px rgba(0,0,0,0.1) right border, padding 0 50.88px 0 33.92px |
| Figures | square, no border, no shadow; margin 25.44px 0 42.4px |
| Badges | small two-tone shields (GitHub black/white, Hugging Face yellow) as images |
| Article and appendix | full-width 1px hairline at the top of each |

## Layout Metrics

- **Header:** `.header-container` padding 50px; content max-width calc(50% − 20px), centred (650px at 1440).
- **Article grid:** Distill `d-article` grid at ≥1180px: 1fr side gutters, then 60px columns with 32px gaps; the text column spans eight columns = 704px (x=368–1072); `d-contents` sits in columns 1–3 to its left.
- **Section rhythm:** h2 32px above / 24px below; paragraphs 16.96px bottom margin; figures 25.44px above, 42.4px below.
- **Figures:** column width (704px), teaser capped at 360px high.
- **Appendix:** `d-appendix` margin-top 60px, padding 60px 0 48px, same grid with headings in the left columns (152px) and content in the text column.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1180px | 1fr (368px at 1440) | 16.96px | 32px | 60px columns, 32px gaps, text 704px; contents in the left margin |
| 1000–1179px | 1fr | 16.96px | 32px | 50px columns, 16px gaps, text 512px; contents still in the margin |
| 768–999px | 1fr | 16px | 32px | 45px columns, 16px gaps, text 472px; contents moves above the text; h2 drops to 24px |
| ≤767px | 16px | 14px | 28px | single column (358px at 390); header padding 20px; contents stacks above; h2 24px |

## Components

- **Outline pill button:** inline-block, #aed6f1 fill, #000000 16px / 700 label, 2px solid #231f19, radius 25px, padding 10px 20px, margin 5px, shadow `0 4px 8px rgba(0,0,0,0.2)`; hover fill #3498db with #ffffff text over 0.3s.
- **Margin contents:** "CONTENTS" label 14px / 600 uppercase, links 13px / 600 rgba(0,0,0,0.8) with no underline (hover underline rgba(0,0,0,0.6)), a 1px hairline on the right.
- **Hairline section head:** 36px / 600 rgba(0,0,0,0.8), 16px padding then a 1px rgba(0,0,0,0.1) rule.
- **Numbered figure:** image at column width, caption 13px rgba(0,0,0,0.6) beginning with bold "Figure N."
- **Bold finding sentence:** a whole paragraph in bold, justified, optionally ending in a #f66b4d phrase introduced by "=>".
- **Citation:** Distill `d-cite` renders bracketed numbers that open a hover card and link to the References list.
- **Badge list:** bullet items each starting with a small shield image (3DSRBench, GitHub, Hugging Face) followed by a sentence.
- **Appendix:** Distill grey appendix with BibTeX, Notes ("This website template is adapted from Image Sculpting") and numbered References in two columns.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / venue / authors / affiliations | Yes | centred bold header, red "(highlight)" |
| Link buttons | Yes | two sky outline pills |
| Table of contents | Yes | margin list beside the lead paragraph |
| Teaser figure | Yes | Figure 1 at column width |
| Abstract | Yes (non-standard) | an unlabelled lead paragraph |
| Method | Yes | "SpatialLLM Framework" with figures and a bullet list |
| Results tables | Yes (non-standard) | LaTeX tables embedded as images with numbered captions |
| Key findings | Yes | bold justified sentences |
| Data & Code | Yes | shield-badge bullet list |
| BibTeX / references | Yes | Distill appendix |
| Video | No (absent from the source) | |
| Footer | No (absent from the source) | the appendix ends the page |

## Adapting to Other Content

- **More authors:** keep the em-spaced bold names and break lines manually by affiliation group; past about eight, drop to 14px.
- **Results table as HTML:** use the page's own `.data-table` rules: 12px tabular numerals, 2.5px border-spacing, `.tb-hdr` header cells on #f2f2f2, best row `.highlight-green` #e6ffe6 bold, and a 13px "Table N." caption to match figures.
- **Abstract heading:** if you need one, use the same 36px hairline h2 and add it to the contents list.
- **Long publication or news lists:** plain bullet lists in the 704px column at body size; dates bold.
- **Video:** place it as a `d-figure` at column width with a numbered caption; avoid a separate hero.

## Do's and Don'ts

- Do keep the reading column at 704px and justify the body text, as a paper would.
- Do number every figure and lead its caption with bold "Figure N."
- Do keep color to two moments: the red "(highlight)" and the coral finding.
- Don't add cards, bands or shadows inside the article; the only shadow is on the header buttons.
- Don't expect the contents list to follow the reader; it is not sticky here. Add `position: sticky; top: 0` if you want that.
- Don't mix the hover gold #ffcc00 with the sky buttons; the rendered hover is the #3498db fill.

## Surfaces

White throughout. Hairlines (rgba(0,0,0,0.1)) separate the header from the article, sit under each h2, beside the contents and above the appendix. The sky buttons are the only filled shapes.

## Imagery

A teaser that mixes a street photo with pastel labelled boxes (green, orange, yellow) and a semicircle gauge, VQA examples with chat bubbles, a small pipeline diagram, and two results tables typeset in Times-like LaTeX as images.

## Layout

A centred header, then the Distill article grid: a margin contents list on the left and a 704px text column, with the appendix in the same grid at the end. Rendered height about 4,900px.

## Agent Prompt Guide

Quick colors: title #000000, article text rgba(0,0,0,0.8), captions rgba(0,0,0,0.6), hairlines rgba(0,0,0,0.1), authors #004276, buttons #aed6f1 with #231f19 borders (hover #3498db), highlight #ff0000, finding #f66b4d.

1. "Create a centred header with 50px padding and a 650px max-width: a 32px bold system-UI title in #000000, a 18.72px bold venue line with '(highlight)' in #ff0000, bold author links in #004276 separated by em-spaces, and two pill buttons: #aed6f1 fill, 2px solid #231f19, radius 25px, padding 10px 20px, 16px bold black text, shadow 0 4px 8px rgba(0,0,0,0.2), hover #3498db with #ffffff text."
2. "Lay out the article as a grid: 60px columns with 32px gaps and a 704px text column; in the left margin put a 'CONTENTS' label (14px, weight 600, uppercase) and 13px weight-600 links in rgba(0,0,0,0.8) with a 1px rgba(0,0,0,0.1) right border."
3. "Style the body: 16.96px text with 1.7 line height, justified, rgba(0,0,0,0.8); 36px weight-600 section heads with 16px padding and a 1px rgba(0,0,0,0.1) rule beneath; figures at column width with 13px rgba(0,0,0,0.6) captions starting 'Figure N.' in bold."

## Similar Pages

- Distill-template project pages (Image Sculpting, which this page adapts, and other Distill-based research write-ups).
- Paper-like project pages with a margin table of contents.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --ink: #000000;
  --text: rgba(0, 0, 0, 0.8);
  --caption: rgba(0, 0, 0, 0.6);
  --rule: rgba(0, 0, 0, 0.1);
  --author: #004276;
  --button: #aed6f1;
  --button-border: #231f19;
  --button-hover: #3498db;
  --highlight: #ff0000;
  --finding: #f66b4d;
  --font-ui: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --title-size: 32px;
  --h2-size: 36px;
  --body-size: 16.96px;
  --body-lh: 1.7;
  --caption-size: 13px;
  --radius-button: 25px;
  --text-column: 704px;
}
```

## Provenance

- **URL:** https://3d-spatial-reasoning.github.io/spatial-llm/
- **Paper:** SpatialLLM: A Compound 3D-Informed Design towards Spatially-Intelligent Large Multimodal Models (arXiv 2505.00788), Wufei Ma, Luoxin Ye, Celso M de Melo, Jieneng Chen, Alan Yuille.
- **Venue:** CVPR 2025, highlight (stated in the header).
- **Selection reason:** arXiv 2505.00788 comment states acceptance at CVPR 2025 (highlight); project page linked in the abstract.
- **Template credit:** the appendix notes say the template is adapted from Image Sculpting; the article body is the Distill template.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share, the 1440×900 screenshot, scrolled full-page captures, renders at 1100, 900 and 390px, `style.css`, the inline `<style>` and page HTML; 2026-10-28.
