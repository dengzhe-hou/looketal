# COSTGRAD Lab Notebook — Style Reference

> A clean instrument panel: four live monitors in a row, monospace channel labels, and one brick-red switch.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share) and the 1440 screenshots, checked against the page's stylesheet /assets/costgrad/style.css. The font stack is the system UI stack, so `fonts_loaded` is empty and the Windows render uses Segoe UI; on macOS the same CSS gives San Francisco.

## Overview

COSTGRAD is a compact, functional page on pure white in a 1000px shell. The header is centered and small: a two-line 38px semibold title, a 14px gray tagline, two underlined author names, a bold "NeurIPS 2026", and a single brick-red (#b74732) "Read paper ↗" button with "Code forthcoming" beside it. The demos are in the first viewport: four square recorded rollouts in dark frames (#272c29) with task names and 8px monospace category labels, a legend line, and a three-up stat strip separated by hairlines. Below, sections open with 10px monospace indices ("01 / IN ACTION", "02 / THE IDEA"), 27px semibold headings and a right-aligned gray aside; results are a clean hairline table whose COSTGRAD column is tinted #f7f7f4, bold, and headed in the accent red. Everything else is gray hairlines (#e1e2dc).

## First Viewport

Color share of the 1440×900 viewport: #ffffff 76% (page), #493a37 7%, #141b21 6% and #9e9286 4% (the dark demo frames and their content), #e3e7e3 3% (light demo pixels and hairlines), #fafaf9 3%. The fold is white with a single band of four dark squares across the middle; the red button is the only saturated UI color.

Anatomy in DOM order (shell x 220–1220, header centered):

1. **Title** `h1`: two lines ("…Visual World Models / via Cost Gradients"), 38px/650 (clamp 26px, 3vw, 38px), line-height 1.2, letter-spacing -.025em, #252823, centered, top at 32px. Gap 14px.
2. **Tagline** `p.hero-tagline`: 14px/400, line-height 1.65, #62665f, centered, max-width 650px. Gap 14px.
3. **Authors** `.authors`: two names 15px #252823, each with a 1px #c7c9bf bottom border, 16px gaps around a #a3a59b middle dot. Gap 9px.
4. **Venue** `p.venue`: "NeurIPS 2026", 14px/600 #252823. Gap 16px.
5. **Actions**: "Read paper ↗" button (44px tall, #b74732, white 14px/600, radius 5px) and "Code forthcoming" 12px #62665f, 16px apart. Hero padding-bottom 28px.
6. **Section index** `span.section-index`: "01 / IN ACTION", mono 10px, letter-spacing .08em, #62665f, 8px above the heading.
7. **Heading row** `.section-topline`: "Keep what matters for the goal." 26px/600 left; "Ⅱ Pause demos" text button right (12px, 1px #b8bab0 underline). Gap 20px.
8. **Demo grid**: 4 columns × 238px, 16px gaps; each a #272c29 frame with 8px padding and 6px radius around a 222px square (2px radius); caption row 13px/550 task name left and 8px uppercase mono label right in #62665f.
9. **Legend line**: 10px #62665f with 8px swatches (#d5d7cd kept with a #989c90 border, #434a43 dropped) left, "Recorded rollouts · 50% tokens · retrained predictors" right.
10. **Stat strip** `.stats-strip`: 26px below, 1px #e1e2dc top rule, three centered columns split by 1px hairlines, padding 24px 0 32px; values 30px/500, -.04em ("128/256", "2.6×", "1"), unit 20px #62665f; labels 11px #62665f.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Page | #ffffff | (literal) | body background, button label |
| Ink | #252823 | --ink | title, headings, body text, table text |
| Muted | #62665f | --muted | tagline, section indices, asides, captions, stat labels, table subheads |
| Hairline | #e1e2dc | --line | section borders, table rules, stat dividers, cards and details borders |
| Brick | #b74732 | --accent | Read paper button, COSTGRAD table header, link and button hover, footer brand period, focus outline |
| Brick Hover | #973a29 | (literal) | Read paper button hover |
| Gain Green | #3e6355 | --green | positive deltas in the results table |
| Column Tint | #f7f7f4 | (literal) | COSTGRAD column cells |
| Code Wash | #f6f6f3 | (literal) | BibTeX block |
| Demo Frame | #272c29 | (literal) | frames around the demo rollouts |
| Author Rule | #c7c9bf | (literal) | author name underlines |
| Dot Grey | #a3a59b | (literal) | separator dot between authors |
| Button Rule | #b8bab0 | (literal) | underline of text buttons (Pause demos, Copy BibTeX) |
| Link Rule | #b9bdae | (literal) | underline of inline links |
| Kept Swatch | #d5d7cd | (literal) | legend "retained tokens" swatch (border #989c90) |
| Dropped Swatch | #434a43 | (literal) | legend "discarded tokens" swatch |
| Swatch Border | #989c90 | (literal) | border of the kept swatch |

## Tokens — Typography

- **Sans**: declared `-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`; renders Segoe UI on Windows (system font, not listed in fonts_loaded) and San Francisco on macOS. Weights 400, 500, 550, 600, 650 are used. Substitute: Inter.
- **Mono**: declared `"SFMono-Regular", Consolas, "Liberation Mono", monospace`; renders Consolas on Windows. Substitute: JetBrains Mono.

| Role | Selector | Size at 1440 | Weight | Line-height | Tracking |
|---|---|---|---|---|---|
| Title | `h1` | 38px (clamp 26px, 3vw, 38px; 27px ≤560px) | 650 | 1.2 | -.025em |
| Stat value | `.stats-strip strong` | 30px, unit 20px | 500 | 1.2 | -.04em |
| Section heading | `h2` | 27px (first section 26px; 23px ≤560px) | 600 | 1.25 | -.02em |
| Subheading | `h3` | 18px (16px in cards) | 550 | 1.3 | 0 |
| Body | `body` | 16px | 400 | 1.65 | 0 |
| Authors | `.authors` | 15px | 400 | 1.65 | 0 |
| Intro paragraphs | `.section-intro` | 15px #62665f | 400 | 1.85 | 0 |
| Tagline, venue, button, table | `.hero-tagline`, `.venue`, `.paper-button`, `table` | 14px | 400 / 600 / 600 / 400 | 1.65 | 0 |
| Demo caption | `.demo-card figcaption` | 13px | 550 | 1.65 | 0 |
| Table header, aside, text buttons | `th`, `.section-aside`, `.text-button` | 12px | 550 / 400 / 400 | 1.65–1.7 | 0 |
| Stat label, notes | `.stats-strip p`, `.table-note` | 11px | 400 | 1.65–1.85 | 0 |
| Section index | `.section-index` | 10px mono | 400 | 1.5 | .08em |
| Task label | `.task-label` | 8px mono uppercase | 400 | 1.5 | .05em |
| BibTeX | `.citation-section pre` | 12px mono | 400 | 1.85 | 0 |

## Tokens — Spacing & Shapes

- **Radius**: 6px for demo frames (2px on the inner image); 5px for the Read paper button; 4px for the BibTeX block, details panels, effects card and dialog buttons; 8px for the figure dialog.
- **Shadows**: none.
- **Borders**: 1px #e1e2dc everywhere (section block borders, table head top and bottom, row bottoms, stat dividers, detail panels, footer); 1px underlines in #c7c9bf, #b8bab0 or #b9bdae for links and text buttons.

## Layout Metrics

- **Container**: `.shell` = `min(1000px, 100% - 48px)` centered (x 220–1220 at 1440); 100% − 40px at ≤800px.
- **Hero**: centered text, padding 32px 0 28px; tagline max-width 650px.
- **Sections**: `.section-space` padding 38px 0 (28px ≤560px). The method and findings sections span the full width with 1px #e1e2dc top and bottom borders; their content sits in the shell.
- **Section top line**: flex, index + h2 left, aside right (12px, right-aligned), 20px below.
- **Demo grid**: 4 × `minmax(0,1fr)`, gap 16px; frame padding 8px.
- **Stat strip**: 3 columns, margin-top 26px, padding 24px 0 32px.
- **Method figure**: max-width 840px centered, 28px top margin; caption max-width 720px.
- **Findings**: 2 columns, gap 45px.
- **Table**: full shell width; cells 15px 12px.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| >800px | 24px | 16px | 3vw, max 38px | demos 4 across; findings 2 columns; asides shown |
| ≤800px | 20px | 16px | 3vw (26px floor) | demo gap 12px, frame padding 6px; task label stacks under name; section asides and footer link hidden |
| ≤560px | 20px | 16px | 27px | demos 2 across; h2 23px; stats 26px; findings 1 column; table scrolls (min-width 565px); touch targets 44px |

## Components

- **Paper button** `.paper-button`: min-height 44px, padding 10px 20px, radius 5px, #b74732 fill, #ffffff 14px/600, "↗" 16px after the label; hover #973a29.
- **Text button** `.text-button`: no fill, 1px #b8bab0 bottom border, padding 5px 0, 12px, icon or arrow with 10px gap; hover text and border #b74732.
- **Section index**: mono 10px, .08em tracking, #62665f, "NN / LABEL" in uppercase.
- **Demo tile**: #272c29 frame, 8px padding, 6px radius; image square with 2px radius; caption row with 13px/550 name and 8px mono category.
- **Stat strip**: hairline top, three centered stats with 1px dividers; 30px/500 value, 20px muted unit, 11px muted label.
- **Results table**: 14px tabular numerals; caption 12px #62665f above; thead framed by 1px #e1e2dc top and bottom; header 12px/550 with a 10px muted subline (token counts); numbers right-aligned; rows divided by 1px #e1e2dc; the COSTGRAD column has #f7f7f4 cells, 650-weight values and a #b74732 header; positive deltas #3e6355.
- **Details panel** `.checkpoint-results`: 1px #e1e2dc border, radius 4px, summary 14px/550 with padding 16px 20px and a 20px "+" that rotates 45° when open.
- **Effects card**: padding 22px, 1px #e1e2dc, radius 4px; definition list 13px.
- **BibTeX**: #f6f6f3, radius 4px, padding 24px, 12px/1.85 mono.
- **Footer**: 1px top rule, padding 22px 0; wordmark "COSTGRAD." 14px/650 with a #b74732 period.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top nav | absent from the source | no nav bar |
| Title block | yes | centered, compact two-line title |
| Authors / affiliations | yes, non-standard | two underlined names; no affiliations line |
| Venue | yes | bold 14px line |
| Link buttons | yes | one red Paper button, code marked "forthcoming" |
| Teaser | yes, non-standard | four live demo tiles in dark frames instead of a single teaser |
| Stat strip | yes | three-up hairline strip |
| Method figure | yes | 840px diagram, click to enlarge in a dialog |
| Results table | yes | hairline table with a tinted, accent-headed method column |
| Plots | yes | performance figure under the table |
| Findings | yes | two-column copy plus bordered effects card |
| Collapsible details | yes | bordered details panels with "+" |
| BibTeX | yes | tinted block with a text Copy button |
| Footer | yes | wordmark with red period |

## Adapting to Other Content

- **More authors**: keep the centered flex row with dots; allow wrapping (gap 6px 16px) and add a 14px #62665f affiliation line under it before the venue.
- **Teaser video**: one 16:9 video in the same #272c29 frame (8px padding, 6px radius) spanning the 1000px shell, with a 13px/550 caption row.
- **More results tables**: repeat the table recipe; always tint only the proposed method's column (#f7f7f4) and head it in #b74732.
- **Long publication list**: rows separated by 1px #e1e2dc, index in 10px mono on the left, title 15px #252823, venue 12px #62665f right-aligned.
- **News**: a section with index "NN / NEWS" and a list of 14px lines, each with a 10px mono date.

## Do's and Don'ts

- Do show results in the first viewport (demos and stats before any prose).
- Do label every section with a 10px monospace index.
- Do keep a single red accent and use it for the primary action and the proposed column only.
- Do separate everything with 1px #e1e2dc hairlines, never shadows.
- Don't use a hero image or gradient; the header is plain white text.
- Don't bold whole tables; only the proposed column is 650 weight.
- Don't add more filled buttons; secondary actions are underlined text buttons.

## Surfaces

White #ffffff throughout; #272c29 demo frames; #f7f7f4 table column tint; #f6f6f3 BibTeX; hairline-bordered panels. No bands of color.

## Imagery

Recorded planning rollouts (maze, wall, PushT, MetaWorld) with token-mask overlays in square dark frames; a method pipeline diagram; matplotlib-style performance plots with red COSTGRAD markers.

## Layout

Compact centered header, then a 1000px left-aligned shell with full-width hairline-bounded sections; grids of 4 (demos), 3 (stats) and 2 (findings). About 3,900px tall.

## Agent Prompt Guide

Quick colors: page #ffffff, ink #252823, muted #62665f, line #e1e2dc, accent #b74732 (hover #973a29), column tint #f7f7f4, frame #272c29, positive #3e6355, code #f6f6f3.

1. "Build a compact centered header on #ffffff: h1 38px weight 650, line-height 1.2, letter-spacing -.025em, #252823; 14px #62665f tagline (max 650px); 15px author names with 1px #c7c9bf underlines; 'NeurIPS 2026' 14px/600; a 44px button with #b74732 fill, radius 5px, padding 10px 20px, #ffffff 14px/600 and a trailing ↗, hover #973a29."
2. "Build a demo row: 4-column grid, 16px gap; each tile has a #272c29 frame with 8px padding and 6px radius around a square image with 2px radius; below, a caption row with 13px/550 name left and an 8px uppercase monospace label in #62665f right."
3. "Build a results table: 14px tabular numerals, header 12px/550 with 10px #62665f sublines, 1px #e1e2dc rules on thead and every row, cells 15px 12px, numbers right-aligned; the proposed column has #f7f7f4 background, weight 650 values and a #b74732 header; positive deltas #3e6355."

## Similar Pages

- Minimal research pages built on system fonts with monospace section indices and hairline tables.
- Pages that lead with a strip of live demo tiles rather than a single teaser.

## Quick Start

```css
:root {
  --page: #ffffff;
  --ink: #252823;
  --muted: #62665f;
  --line: #e1e2dc;
  --accent: #b74732;
  --accent-hover: #973a29;
  --green: #3e6355;
  --column-tint: #f7f7f4;
  --code-bg: #f6f6f3;
  --frame: #272c29;
  --sans: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --mono: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
  --shell: min(1000px, calc(100% - 48px));
}
body { background: var(--page); color: var(--ink); font: 16px/1.65 var(--sans); }
```

## Provenance

- **URL**: https://ycxuyingchen.github.io/costgrad/
- **Paper**: Sparse Planning in Visual World Models via Cost Gradients (arXiv 2610.10274), Yingchen Xu and Edward Grefenstette.
- **Venue**: NeurIPS 2026.
- **Selection reason**: the arXiv comment states acceptance at NeurIPS 2026 and links this page.
- **Template credit**: custom page; no template credit shown.
- **Evidence used**: computed_style.py render at 1440×900 (computed styles, empty fonts_loaded because only system fonts are used, color share), the 1440 screenshot and tall capture, and style.css read directly. Captured 2026-10-28.
