# Thin-Rule Light Sans — Style Reference

> A clean lecture handout where the headings whisper and the figures speak.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the title, author list, link headings, video, section headings, list text, rules and BibTeX block, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the page's own `css/app.css` plus the site-wide `../../stylesheet.css` over Bootstrap 3.3.5. Positions are document coordinates at 1440px wide.

## Overview

Flow Q-Learning is a hand-built Bootstrap 3 page from the author's personal site, credited to templates by Michaël Gharbi and Jon Barron. It has no header band, no buttons and no color fields. A heavy 64px bold title in #333333 sits centered on white, followed by three authors in a small centered list (blue names over black affiliations) and two plain blue words, "Paper" and "Code", set as 24px headings. An autoplaying contour-plot video comes next, and then the story runs in sections whose headings are large and light: 48px at weight 300, left-aligned, separated by 1px #e6e6e6 rules. Body copy is Source Sans 3 at 18px in bulleted lists with bold lead-ins. The only accent is one blue (#598be7) for links and toggles, which the pale-blue contour figures echo. Long details hide behind "Click to see…" collapse toggles.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): white #ffffff 75.1%, pale figure blue #f3f7fb 7.4%, near-white #fefefe 7.2%, mid grey #9ea2a8 5.0% (text and figure lines), light figure blue #e6eaf0 4.1%, remainder under 1.5%. There is no background band; the figure's pale blue panels supply the only tint.

Anatomy in DOM order (y = top of element box):

1. **Title** (`h1.text-title.text-center.top20`), y 20, "Flow Q-Learning", Source Sans 3 64px/700, line-height 70.4px, #333333, centered. Gap to authors 20px.
2. **Author list** (`ul.list-inline`, centered), y 110, three inline items 18px apart: name link 18px/400 #598be7 on the first line, "UC Berkeley" 18px/400 #333333 on the second (line-height 25.7px). Gap 21px.
3. **Link headings** (`a > h3.top10.text-toplink`), y 182, "Paper" and "Code" side by side, 24px/400 #598be7, no icon, no border. Gap 42px.
4. **Teaser video** (`video.center-block`), y 250, 710×316, autoplay loop muted, centered in an 8/12 column; two square contour panels (BC flow policy, One-step policy). Gap 40px.
5. **Section heading** (`h1`), y 606, "Overview", 48px/300, line-height 52.8px, #333333, left-aligned at x 150. Gap 20px.
6. **Bullet list**, y 679, 18px/400 #333333 with bold (700) lead-ins and italic terms, text starting at x 190. The first 1px rule sits at y 864, just inside the fold.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Graphite | #333333 | Bootstrap body color | Title, section headings, body text, affiliations, BibTeX text |
| Link Blue | #598be7 | `a`, `.text-blue` | Author names, "Paper" and "Code", inline links, collapse toggles |
| Link Hover | #9bb9f1 | `a:hover` | Every link on hover (no underline) |
| Rule Grey | #e6e6e6 | `hr` border | 1px section dividers |
| Code Wash | #f6f8fa | `.codebox-pre` | BibTeX block background |
| Statement Blue | #dee8fa | `.block-statement` | Declared callout fill (not used on this page) |
| Alert Red | #f54254 | `.text-red` | Declared red text class (not visible on this page) |
| Figure Pale Blue | #f3f7fb | figure pixels | Contour-plot panel backgrounds in the teaser and figures |
| White | #ffffff | `body` | Page background |

Declared but not visible: `.block-statement` (2px #598be7 border on #dee8fa, 10px radius) and `.text-red` exist in `app.css` but no element on this page uses them.

## Tokens — Typography

- **Text and headings**: declared `'Source Sans 3', 'Lato', Verdana, Helvetica, sans-serif`, loaded from Google's woff2 as a variable face (weights 300–700, roman and italic). Rendered: Source Sans 3 300–700 (`fonts_loaded`). Substitute: Lato (the declared second choice, near-identical width).
- **Mono**: `'Source Code Pro'` for `.text-tt` labels and the BibTeX block (400 loaded).
- **Math**: MathJax 3 CHTML fonts (MJXTEX) for inline and display equations, at 110% via `.text-equation`.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Paper title | `h1.text-title` | 64px / 70.4px | 700 | #333333 |
| Section heading | `h1` | 48px / 52.8px | 300 | #333333 |
| Subsection | `h2` | 32px / 35.2px | 300 | #333333 |
| Link heading, toggle | `h3.text-toplink`, `h3` | 24px / 26.4px | 400 | #598be7 (inside links) |
| Video caption | `.text-caption` with `.text-tt` | 20px / 28.6px | 400 | #333333, Source Code Pro |
| Body, lists | `body, p, li, a` | 18px / 25.7px | 400 | #333333 |
| Bold lead-in | `b` | 18px | 700 | #333333 |
| Strong | `strong` | 18px | 600 | #333333 |
| BibTeX | `.codebox-pre code` | 17px / 24.3px | 400 | #333333 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Section rule (`hr`) | 0 | 1px solid #e6e6e6 top, margin 21px 0 | none |
| BibTeX block (`.codebox-pre`) | 0 | none | none |
| Video and images | 0 | none | none |
| Author list item | 0 | none | none; padding 0 5px, margin 0 9px |

The page has no shadows, no rounded corners and no filled controls.

## Layout Metrics

- **Container**: Bootstrap 3 `.container#main`, 1170px at ≥1200px (margin 0 135px at 1440px), padding 0 15px, so content spans x 150–1290 (1140px).
- **Title block**: no band. Title margin 20px top; author list and links centered; the link row is a `col-md-4 col-md-offset-4` (380px) column.
- **Teaser**: `col-md-8 col-md-offset-2` with 15px padding, so the video is 710px wide and centered.
- **Sections**: each starts with `hr` (1px #e6e6e6, 21px margins) then an `h1` with 30px top and 20px bottom margin. Lists use the default 40px indent.
- **Figures**: centered `img` blocks at their natural size inside `col-md-8` or `col-md-10` columns (730px and 920px measured).
- **Task gallery**: six `col-md-2 col-xs-6` cells, 160px square videos with a 20px Source Code Pro caption beneath.
- **Collapses**: "Click to see…" toggles reveal hidden blocks, the algorithm in a centered `col-md-6`.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1200px | container 1170px | 18px | 64px | 12-column grid as described |
| 992–1199px | container 970px | 18px | 64px | same columns, narrower |
| 768–991px | container 750px | 16px | 44px | `h1` 40px; `.desktop-only` blocks hidden; equations 100% |
| <768px | 15px padding, fluid | 16px | 44px | columns stack; task videos two per row (`col-xs-6`) |

## Components

- **Plain link heading**: an `<a>` wrapping `h3.text-toplink`, Source Sans 3 24px/400, #598be7, no background, no icon, no underline; hover #9bb9f1. Used for Paper and Code and for "Click to see…" collapse toggles.
- **Author list**: `ul.list-inline` centered, items inline-block with 0 5px padding and 9px side margins; name link #598be7 18px, `<br>`, affiliation #333333 18px.
- **Light section heading**: `h1` 48px/300 #333333, left-aligned, preceded by a 1px #e6e6e6 rule with 21px margins.
- **Bulleted claim list**: `ul` with 40px indent, 18px/25.7px #333333, each item opening with a bold (700) sentence, inline MathJax.
- **Video tile**: `video.center-block` width 100% inside a grid cell, autoplay loop muted playsinline, caption below in Source Code Pro 20px, centered.
- **Citation block**: `pre.codebox-pre`, background #f6f8fa, no border, padding 10px, Source Code Pro 17px, highlight.js disabled with `nohighlight`.
- **Footer note**: after a final rule, one justified 18px paragraph crediting Michaël Gharbi and Jon Barron.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title and authors | yes | centered bold title, inline author list with affiliations under names |
| Link buttons | present but non-standard | two blue text headings, no button shape |
| Teaser video | yes | 710px autoplay video |
| Overview bullets | yes | in place of an abstract |
| Abstract | absent from the source | the Overview bullets replace it |
| Method explanation and equations | yes | bullets with MathJax, collapsible full algorithm |
| Figures | yes | centered contour-plot diagrams in pale blue |
| Task video gallery | yes | six 160px square videos with mono captions |
| Results | yes | result plots, with detailed tables in collapses |
| Results table | present but non-standard | tables appear as images inside collapses, not HTML tables |
| BibTeX | yes | #f6f8fa `pre` |
| Navigation, footer band | absent from the source | only a one-line template credit |

## Adapting to Other Content

- **More authors**: keep the inline list with the affiliation under each name; it wraps to new centered lines. For many authors with shared affiliations, switch to superscript numbers and one affiliation line in 18px #333333.
- **A results table**: an HTML table inside the 1140px column, 18px Source Sans 3, header weight 600, 1px #e6e6e6 horizontal rules only, best numbers in bold 700; no fills.
- **More links**: add more 24px #598be7 text headings to the inline row; do not introduce pills or icons.
- **Long publication lists**: plain bulleted list, bold titles, venue in regular weight, links in #598be7.
- **News**: a short dated bullet list under an "Updates" `h1`, the date in bold.
- **A highlighted claim**: the declared `.block-statement` (#dee8fa fill, 2px #598be7 border, 10px radius, 20px bold) is the one sanctioned callout.

## Do's and Don'ts

- Do let the weight contrast carry hierarchy: 700 for the title, 300 for section headings, 400 body, 700 lead-ins.
- Do keep one accent, #598be7, and make figures echo it.
- Do separate sections with a 1px #e6e6e6 rule and nothing heavier.
- Do push secondary detail into collapse toggles rather than lengthening the page.
- Don't add buttons, cards, shadows or rounded corners.
- Don't center section headings; only the title block is centered.
- Don't tint the background; white is the only surface besides the code wash.

## Surfaces

White only. The BibTeX block is #f6f8fa. Figures bring their own pale blue (#f3f7fb) panels. No cards, bands or shadows.

## Imagery

Square contour-plot panels with nested blue ellipses and black frames, animated as autoplay videos, plus simulation videos of robotic tasks (mazes, cube and puzzle manipulation) in small square tiles, and line plots of results. Everything sits unframed and centered.

## Layout

A single 1140px Bootstrap column. The title block, teaser and media are centered; text sections are left-aligned and full container width, which makes lines long (about 150 characters at 1440px). Rendered height is about 5,430px at 1440px with collapses closed.

## Agent Prompt Guide

Quick colors: text #333333, links #598be7, hover #9bb9f1, rules #e6e6e6, code #f6f8fa, white page.

1. "Build a minimal title block on white: centered 'Source Sans 3' 64px/700 #333333 title; below, an inline list of authors (name link 18px #598be7, line break, affiliation 18px #333333), items 9px apart; then 'Paper' and 'Code' as 24px/400 #598be7 text links side by side, hover #9bb9f1, no buttons."
2. "Create a section: a 1px solid #e6e6e6 rule with 21px vertical margins, then a left-aligned h1 in Source Sans 3 48px/300 #333333 with 30px top and 20px bottom margin, followed by a bulleted list at 18px/25.7px where each item starts with a bold (700) sentence."
3. "Add a citation block: `pre` with background #f6f8fa, no border, padding 10px, Source Code Pro 17px #333333."

## Similar Pages

- Jon Barron-derived personal-site project pages (Bootstrap 3, Lato or Source Sans, light headings).
- Other projects on seohong.me (HIQL, METRA, OGBench) share the same stylesheet.

## Quick Start

```css
:root {
  --text: #333333;
  --link: #598be7;
  --link-hover: #9bb9f1;
  --rule: #e6e6e6;
  --code-bg: #f6f8fa;
  --callout-bg: #dee8fa;
  --font: 'Source Sans 3', 'Lato', Verdana, Helvetica, sans-serif;
  --font-mono: 'Source Code Pro', monospace;
  --title-size: 64px;
  --h1-size: 48px;
  --h1-weight: 300;
  --body-size: 18px;
  --container: 1170px;
}
```

## Provenance

- **URL**: https://seohong.me/projects/fql/
- **Paper**: Flow Q-Learning (arXiv 2502.02538), Seohong Park, Qiyang Li, Sergey Levine (UC Berkeley).
- **Venue**: ICML 2025.
- **Selection reason**: existing verified entry in entries.json; the arXiv 2502.02538 comment says ICML 2025. Chosen for restrained academic minimalism: heavy bold title, light large section headings with thin rules, and blue contour figures.
- **Template credit**: the footer says the template was partly borrowed from Michaël Gharbi and Jon Barron.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share, targeted computed-style probes of container, rules, list text, captions, images and video, the first-viewport screenshot and scaled full-page capture, `css/app.css`, the site `stylesheet.css` and the HTML. Date 2026-10-28.
