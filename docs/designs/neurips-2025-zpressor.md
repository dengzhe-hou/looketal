# ZPressor Dusty Pastel Serif — Style Reference

> A museum placard in soft humanist capitals, three words of its title washed in rose, steel blue and dusty pink.

**Theme:** light

Measured from the rendered page at 1440×900 in headless Chrome (`computed_style.py`, screenshot and tall capture), then checked against `css/theme.css`, `css/highlight-kw.css`, the edited `css/bootstrap-4.4.1.css` and inline styles in `index.html` (Lior Yariv's template, the same Bootstrap edit used by the ZJU 4K4D pages). Where stylesheet and render disagree, the render is reported. Pixel values are at the 1440px viewport unless a breakpoint is named.

## Overview

A Bootstrap 4 jumbotron page with a pale blue-grey band (`#ebf0f1`) for the hero and white below. Its identity comes from Philosopher, a humanist display face with flared strokes, used for the title and (because the declared `optima` is not installed on most systems) for all text. Three title fragments are tinted in muted pastels: the "Z" in rose `#e9908b`, "Bottleneck-Aware" in steel blue `#97adba` and "Scalable" in dusty pink `#d4b1af`. A small isometric Z logo sits above the title. Below the band, sections in a 920px column open with a left-aligned 28px heading and a hairline rule. The TL;DR shows a three-way image comparison with a PSNR-versus-time bubble chart, and the abstract repeats the steel blue and dusty pink on two keywords. The comparison sections use before/after video sliders with dark label chips and rows of steel-blue or rose "Scene" tabs. A grey rounded BibTeX block and a centred footer close the page. Document height is about 5,011px.

## First Viewport

Color share of the first 1440×900 viewport: `#ebf0f1` 40.4% (hero band), `#ffffff` 32.8% (page), `#929aa2` 15.4% (building facade and sky in the TL;DR teaser), `#ebf0eb` 4.5% and `#f5f7f5` 3.5% (pale green panels in the TL;DR diagram), `#eaf0f0` 1.7%, `#ebf0f2` 1.0%, `#eff0ed` 0.5%.

Anatomy in DOM order (centred unless noted):

1. Hero band `div.jumbotron`, full width, `#ebf0f1`, padding 64px 32px, bottom margin 16px.
2. Logo `assets/favicon.svg`, 50×50px at y=64, inline with a 20px right margin. Gap 0.
3. Title `h1` (wrapped in `b`), Philosopher 40px/700, `#212529`, line-height 48px, two lines from y=114; tinted spans at 900 weight: "Z" `#e9908b`, "Bottleneck-Aware" `#97adba`, "Scalable" `#d4b1af`. Gap 8px.
4. Venue `h4` "NeurIPS 2025", 24px/500, `#5a6268`. Gap 16px.
5. `hr`, 1px `rgba(0,0,0,0.1)`, 920px wide. Gap 16px.
6. Authors, six `a` links in one line, 16px/300, `#007bff`, numeric superscripts, `&nbsp;` separators.
7. Affiliations `p`, 16px/300, `#595959`. Gap 16px.
8. Buttons row: Paper, Code, Models black buttons, 38px tall, 6px apart. Band ends at y=430.
9. Gap 32px, then `h3` "TL;DR" at y=446, 28px/500 `#212529`, left-aligned, followed by an `hr` (margin-top 0).
10. Lead `p.text-left` at y=504, 16px/300 `#595959` with "ZPressor" in bold.
11. TL;DR teaser image at y=544, 920×501px: three renders with serif captions above a pipeline diagram and a bubble chart; it runs past the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Mist Band | `#ebf0f1` | `.jumbotron` background | Hero band |
| Bootstrap Ink | `#212529` | Bootstrap body color | Title, section `h3`s, BibTeX text |
| Slides Grey | `#595959` | `p` (theme.css) | All paragraphs: affiliations, TL;DR lead, abstract, captions |
| Rose | `#e9908b` | inline span; `.video-btn-re10k` | "Z" in the title; RealEstate10K scene tabs |
| Steel Blue | `#97adba` | inline span; `.video-btn` | "Bottleneck-Aware" in the title, "lightweight" in the abstract; DL3DV scene tabs |
| Dusty Pink | `#d4b1af` | inline span | "Scalable" in the title, "architecture-agnostic" in the abstract |
| Slate | `#5a6268` | inline style | Venue `h4` |
| Link Blue | `#007bff` | Bootstrap `a` | Author names, footer links |
| Button Black | `#090f15` | `.btn-light` (edited) | Paper, Code, Models button fill |
| Button Label | `#e2e2e2` | `.btn-light` (edited) | Button text and icons |
| Button Edge | `#f8f9fa` | `.btn-light` border | 1px button border |
| Button Hover | `#bec3c7` | `.btn-light:hover` | Hero button hover fill (label `#212529`, border `#dae0e5`) |
| Button Hover Edge | `#dae0e5` | `.btn-light:hover` | Hero button hover border |
| Code Grey | `#e9eeef` | inline style on `pre` | BibTeX block |
| Rule | `rgba(0,0,0,0.1)` | Bootstrap `hr` | Hero rule and rules under section heads |
| Label Chip | `rgba(0,0,0,0.7)` | inline style | "DepthSplat", "MVSplat + ZPressor" labels on comparison videos |
| Slider Line | `#ffffff29` (white at 16%) | inline style | Vertical divider on the before/after videos |
| Page | `#ffffff` | `body` | Everything below the band |

## Tokens — Typography

- **Declared:** `body { font-family: 'optima', 'Philosopher'; font-size: medium }`; `h1 { font-family: 'Philosopher' }`. Philosopher 400/700 (and italics) from Google Fonts.
- **Rendered:** Philosopher 400 and 700 loaded (`fonts_loaded`); Optima is not present on the capture machine, so all body text renders in Philosopher. On a Mac with Optima installed, body text would render in Optima while the title stays Philosopher. Substitute: Marcellus or Optima nova; Marcellus is the closer free match for Philosopher's flared humanist strokes.
- **Mono:** Bootstrap `SFMono-Regular, Menlo, Monaco, Consolas, …` in the BibTeX block.
- Figures inside images use a Times-style serif for captions ("DepthSplat (36 views)"), which harmonises with Philosopher.

| Role | Selector | Size | Weight | Line height | Colour |
|---|---|---|---|---|---|
| Title | `h1 > b` | 40px | 700 (tinted spans 900) | 48px | `#212529` + pastels |
| Venue | `h4` | 24px | 500 | 28.8px | `#5a6268` |
| Section head | `h3` | 28px | 500 | 33.6px | `#212529`, left |
| Body | `body`, `p` | 16px | 300 | 24px | `#595959` |
| Authors | `a` | 16px | 300 | 24px | `#007bff` |
| Buttons | `.btn` | 16px | 400 (label in `b`) | 24px | `#e2e2e2` |
| Scene tabs | `button.video-btn` | 16px | 400 | 24px | `#ffffff` |
| Video label chip | inline `div` | 16px | 700 | 24px | `#ffffff` |
| BibTeX | `pre` | 14px | 300 | 21px | `#212529` |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Hero band | 0.3rem (4.8px) |
| Hero buttons | 8px |
| BibTeX `pre` | 15px |
| Scene tabs, video label chips | 4px |
| Videos | 5px (`video` rule in theme.css) |
| Carousel arrows (declared) | 50% |

- **Shadows:** none rendered on buttons or cards. The edited `.btn` declares a `0 0 0 0.2rem` grey ring, which is not visible in the render.
- **Borders:** hero buttons 1px `#f8f9fa`; scene tabs have no border.
- **Motion:** scene tabs switch opacity (active 1, inactive 0.7 for DL3DV and 0.5 for RealEstate10K, set by script); `.zoom-element:hover` is `scale(1.)`, so no zoom happens.

## Layout Metrics

- **Container:** Bootstrap `.container` (1140px at ≥1200px, 15px padding) with a `.col-10` centred by `margin: auto`, so the content column is 920px (x=260 to 1180 at 1440px).
- **Hero:** full-bleed `.jumbotron` padding 64px 32px at ≥576px; band height 430px.
- **Sections:** no section padding; each starts with an `h3` (5px top padding from `.col-12 > h3` does not apply, as the column is `.col-10`) and an `hr` with `margin-top: 0`. Sections sit about 30px apart.
- **Figures:** TL;DR and method images span the full 920px column; the DL3DV slider renders 460×259 and the two RealEstate10K sliders render 373×373 each, in a 90%-wide flex row with 10px gap. A script sets these sizes inline from the video aspect; the CSS declarations (50% / 450px and 45% / 400px) are overridden.
- **Scene tabs:** flex row, centred, 10px gap, 20px below the slider.

| Breakpoint | Container | Column | Body size | Title size | Grid change |
|---|---|---|---|---|---|
| ≥1200px | 1140px | 920px | 16px | 40px | sliders side by side |
| 992–1199px | 960px | 770px | 16px | 40px | same |
| 768–991px | 720px | 570px | 16px | 40px | same |
| 576–767px | 540px | 420px | 16px | 40px | RealEstate10K sliders wrap; script resizes slider heights |
| <576px | fluid, 15px gutters | 10/12 of width | 16px | 40px | hero padding drops to 0 (the template comments out Bootstrap's mobile padding) |

## Components

- **Pastel-word title.** Philosopher 40px/700 in `#212529`, with exactly three fragments tinted `#e9908b`, `#97adba`, `#d4b1af` at 900 weight; a 50px logo above.
- **Black hero button.** `a.btn.btn-large.btn-light`: `#090f15` fill, `#e2e2e2` label in bold, 1px `#f8f9fa` border, 8px radius, padding 6px 24px; icon left (Academicons `ai-arxiv`, Font Awesome `fa-code`, `fa-gamepad`). Hover: fill `#bec3c7`, label `#212529`, border `#dae0e5`.
- **Ruled section head.** Left-aligned `h3` 28px/500 `#212529` with a full-width `hr` (1px `rgba(0,0,0,0.1)`, margin-top 0) directly beneath.
- **Before/after video slider.** Two stacked `video`s with `object-fit: cover`, a 2px `#ffffff29` divider the user drags, and `rgba(0,0,0,0.7)` label chips (white 16px bold, padding 8px 15px, 4px radius) pinned 20px from the top-left and top-right corners.
- **Scene tabs.** `button.video-btn`: `#97adba` fill, white 16px label, no border, 4px radius, padding 8px 15px; inactive tabs at 0.7 opacity. The RealEstate10K set uses `#e9908b` with inactive tabs at 0.5.
- **Keyword tint.** Abstract keywords wrapped in `<span style="color: …"><strong>` using the same pastels as the title.
- **BibTeX block.** `pre.selectable` with `#e9eeef` fill, 21px padding, 15px radius, `user-select: all` for one-click copying.
- **Footer.** Centred plain text crediting Lior Yariv's template and the HSMR and 4K4D pages.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / author block | Yes | Mist band, logo, pastel-word title, blue author links |
| Venue badge | Yes, as text | `h4` "NeurIPS 2025" in `#5a6268` (press badges are commented out in the source) |
| Link buttons | Paper, Code, Models | Black 8px-radius buttons (SupMat and Colab buttons commented out) |
| TL;DR | Yes | Ruled `h3`, lead sentence, composite teaser with bubble chart |
| Abstract | Yes | Ruled `h3`, justified-intent paragraph with tinted keywords |
| Method | Yes | Full-width diagram and bold-led caption |
| Comparison sliders | Yes, non-standard | Before/after video sliders with scene tabs |
| Analysis | Yes | Efficiency and ablation figures |
| Results table | Absent from the source (results appear as figures) | |
| BibTeX | Yes | Rounded `#e9eeef` `pre` |
| Footer | Yes | Centred credits |
| Carousel | Absent (carousel CSS is present but unused) | |

## Adapting to Other Content

- **More authors:** keep a single centred run of 16px `#007bff` links separated by `&nbsp;`; it wraps naturally inside the 920px column.
- **More buttons:** add `.column > p.mb-5` black buttons; do not tint them, the pastels belong to text and tabs.
- **A results table:** under a ruled `h3`, 16px Philosopher body in `#595959`, header row 700 `#212529`, best result in `#e9908b` and second in `#97adba`, matching the title's pastel order.
- **More comparisons:** add more slider boxes with label chips and a row of scene tabs; alternate steel-blue and rose tab sets per dataset, as the page does.
- **News:** a short list under the band, 16px `#595959`, dates in bold `#212529`.

## Do's and Don'ts

- Do tint only three title fragments, each in a different muted pastel, and reuse those pastels on abstract keywords and tabs.
- Do keep Philosopher for the title; if you set body in Optima, also load a web fallback, or it silently becomes Philosopher.
- Do keep the hero band flat `#ebf0f1` and every section head left-aligned with a hairline.
- Don't use saturated accents; the only bright colour is Bootstrap link blue on author names.
- Don't add borders or shadows to figures; the white page and hairline rules carry the structure.

## Surfaces

One flat `#ebf0f1` hero band, then a white page. The BibTeX `pre` is `#e9eeef` with a 15px radius. Label chips on videos are the only dark surfaces besides the hero buttons.

## Imagery

Rendered views of outdoor and indoor scenes for feed-forward 3D Gaussian splatting, comparing baseline and ZPressor side by side; a pipeline diagram with pale green and lavender panels; a PSNR-versus-inference-time bubble chart; method diagram with pastel circles. Comparison videos are `.mov` files with spinner posters.

## Layout

A centred 920px column in a Bootstrap container. Text is left-aligned below the hero; figures fill the column; sliders are centred at half width or as a pair.

## Agent Prompt Guide

Quick colors: band `#ebf0f1`, ink `#212529`, body `#595959`, pastels `#e9908b`, `#97adba`, `#d4b1af`, venue `#5a6268`, link `#007bff`, button `#090f15` with `#e2e2e2` label, code `#e9eeef`.

1. "Build a hero band in `#ebf0f1` with 64px 32px padding: a 50px logo, then a two-line Philosopher 40px/700 title in `#212529` where three words are tinted `#e9908b`, `#97adba` and `#d4b1af` at 900 weight, a 24px/500 `#5a6268` venue line, a 1px `rgba(0,0,0,0.1)` rule, 16px/300 `#007bff` author links and 16px `#595959` affiliations."
2. "Make section heads: left-aligned Philosopher 28px/500 `#212529` followed immediately by a full-width 1px `rgba(0,0,0,0.1)` rule with no top margin; body 16px/300 `#595959`."
3. "Create a before/after video slider 460px wide at the video's aspect ratio (about 460×259) with a draggable 2px `#ffffff29` divider, `rgba(0,0,0,0.7)` label chips (white 16px bold, padding 8px 15px, 4px radius) in the top corners, and a centred row of `#97adba` scene tabs (white label, 4px radius, padding 8px 15px, 10px gap, inactive at 0.7 opacity)."

## Similar Pages

4DGT (NeurIPS 2025) in this batch uses the same edited Bootstrap jumbotron, `#ebf0f1` band and black buttons, with Jost instead of Philosopher and two accents instead of three. The ZJU 4K4D and HSMR pages credited in the footer share the lineage.

## Quick Start

```css
:root {
  --band: #ebf0f1;
  --ink: #212529;
  --text: #595959;
  --rose: #e9908b;
  --steel: #97adba;
  --dusty-pink: #d4b1af;
  --venue: #5a6268;
  --link: #007bff;
  --btn: #090f15;
  --btn-label: #e2e2e2;
  --btn-hover: #bec3c7;
  --code-bg: #e9eeef;
  --rule: rgba(0, 0, 0, 0.1);
  --font-display: 'Philosopher', 'Marcellus', serif;
  --font-body: 'Optima', 'Philosopher', sans-serif;
  --radius-btn: 8px;
  --radius-code: 15px;
  --radius-tab: 4px;
}
body { font-family: var(--font-body); font-weight: 300; }
p { color: var(--text); }
h1 { font-family: var(--font-display); }
```

## Provenance

- **URL:** https://lhmd.top/zpressor
- **Paper:** ZPressor: Bottleneck-Aware Compression for Scalable Feed-Forward 3DGS (arXiv 2505.23734), Weijie Wang, Donny Y. Chen, Zeyu Zhang, Duochao Shi, Akide Liu, Bohan Zhuang (ZIP Lab, Zhejiang University; Monash University).
- **Venue:** NeurIPS 2025 (shown on the page).
- **Selection reason:** the arXiv comment states acceptance at NeurIPS 2025 and links the project page.
- **Template credit:** footer thanks Lior Yariv for the website template, and the HSMR and 4K4D pages.
- **Evidence used:** `computed_style.py` render at 1440×900 with first-viewport color share, the 1440 screenshot and tall capture, `css/theme.css`, `css/highlight-kw.css`, the edited `css/bootstrap-4.4.1.css` and inline styles. Captured 2026-10-28.
