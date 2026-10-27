# RAM-Net Paper Companion — Style Reference

> A scholar's reading copy on oatmeal paper: Georgia display type, pale sky-blue pencil marks, and a quiet chapter index pinned to the top.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, color share) and the 1440 screenshots, checked against assets/site.css and the palette file it reads (data/palette.json, injected as CSS variables by assets/palette.js). Both families are system fonts (Georgia and Segoe UI), so `fonts_loaded` is empty; the Windows render is described. Part of the article width is set at runtime by script, so rendered boxes are used for widths.

## Overview

RAM-Net is an interactive "visual research story" on a warm beige paper ground (#e8e2d3) with soft charcoal ink (#373737) and one pale sky-blue accent (#82afe6, inked as #36669f). A 78px header with a 9-dot grid logo, "RAM-Net" in Segoe UI semibold and an EN/中文 switch sits over a hairline. The hero is a two-column grid: on the left a tiny uppercase eyebrow with a blue dot, a 108px Georgia "RAM-Net" with very tight tracking, a 35px Georgia subtitle, a gray deck line, a pale blue "Explore the method ↓" button, a text link and three tinted resource chips; on the right an SVG of slot grids with dashed blue routes to a "current token" tag. A two-column "THE IDEA, IN BRIEF" summary closes the hero. Below, a sticky chapter bar lists eleven numbered sections in 11px text. Each section opens with a large pale-blue Georgia numeral over a small indigo label, a 43px Georgia h2, a blue subtitle, then interactive exhibits (a five-panel tinted comparison, animated architecture diagrams), 16px gray prose at line-height 1.9 and hairline tables with the RAM-Net row tinted blue. Body text is small and low contrast by design.

## First Viewport

Color share of the 1440×900 viewport: #e8e2d3 78% (paper), #e0dbce 10% (the slot cells of the hero diagram), #b4b3ae 5% (cell strokes and gray text), #e9e2d3, #eae4d5, #e8e2d2 together 6% (paper variants), #e2e3df 1%. The fold is almost uniformly beige; the only color is the pale blue button, chips, dot and diagram routes.

Anatomy in DOM order (hero 1240px wide, x 100–1340):

1. **Header** `header.site-header`: 78px tall, max-width 1328px, padding 0 44px, 1px #cdcdcd bottom border. Left: 25px 3×3 dot-grid logo in #82afe6 + "RAM-Net" Segoe UI 18px/650, letter-spacing -.6px, #373737. Right: "A visual research story" 11px #767676, then the language switch (EN selected: 12px/650 #36669f on rgba(130,175,230,.15), radius 4px, padding 6px 9px; 中文 12px #767676). Gap 78px to the hero content (hero padding-top).
2. **Eyebrow** `.eyebrow`: "SEQUENCE MODELING · EFFICIENT ATTENTION", 10px/550 uppercase, letter-spacing 1.7px, #587393, with a 6px #82afe6 dot. Gap 25px.
3. **Title** `h1`: "RAM-Net" Georgia 108px/400 (clamp 70px, 7.6vw, 108px), line-height .97, letter-spacing -6px, #373737, left. Inside it, `h1 span` subtitle "Linear-Time Sequence Modeling with Sparsely Addressable State" on two lines: Georgia 35px, line-height 1.25, letter-spacing -1.2px, 25px below the name, max-width 610px. Gap 22px.
4. **Deck** `p.hero-deck`: 16px Segoe UI, line-height 1.8, #5d5d5d, max-width 420px. Gap 28px.
5. **Actions**: primary "Explore the method ↓" (42px tall, #82afe6 fill, #203c60 12px text, radius 4px, padding 13px 19px, 28px gap to the arrow); "See the results ↗" 12px #5d5d5d underlined, 20px to its right. Gap 18px.
6. **Resource chips**: arXiv ↗, GitHub ↗, Hugging Face ↗; 40px tall, 12px #36669f on #dae5f2, 1px #a8bbcf border, radius 4px, padding 8px 12px, brand logo 16px left, 8px apart.
7. **Hero visual** (right column, from x ≈ 820): "SPARSELY ADDRESSABLE STATE" micro label, "Many slots. A few selected." in 12px gray, then eight 4×4 groups of rounded cells (#e0dbce-like fill, thin gray stroke) in brackets, with dashed 1.5px #6995cc routes converging on a "current token" tag.
8. **Summary** `.hero-summary` (y ≈ 666): 1px #cdcdcd top rule, 24px padding-top; grid 210px / 1fr, gap 34px; label "THE IDEA, IN BRIEF" 10px/550 uppercase #767676; text 14px, line-height 1.85, #5d5d5d, max-width 860px, with a two-item bullet list (bold lead-ins in #373737).
9. **Chapter bar** at y 907, just below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Oat Paper | #e8e2d3 | --color-paper | page background, sticky chapter bar (at 96%) |
| Paper Edge | #c8c0af | --color-paperEdge | table header bottom rules, equation and note tints (mixed at 15%) |
| Ink | #373737 | --neutral-0 | title, h2, h3, wordmark, strong text, table first column |
| Body Gray | #5d5d5d | --neutral-3 | prose, deck, summary, table cells, text link |
| Muted Gray | #767676 | --neutral-5 | header meta, inactive language, chapter links, table headers, footer |
| Hairline | #cdcdcd | --neutral-12 | header and section rules, summary rule, table row rules, chapter bar borders |
| Sky Accent | #82afe6 | --color-pageAccent | primary button, eyebrow dot, logo dots, active chapter underline, equation left border, reading progress bar |
| Sky Tone | #6995cc | --tone-sky | dashed routes in the hero diagram, insight-note left border |
| Sky Ink | #36669f | --tone-sky-ink | resource chip text, selected language, section subtitles, highlighted text, citations, RAM-Net table row label |
| Action Ink | #203c60 | --color-actionInk | primary button label |
| Chip Fill | #dae5f2 | (mix 75% white + 25% sky) | resource chips, RAM-Net table row, noscript note |
| Chip Border | #a8bbcf | (mix 50% sky + 50% paper) | resource chip borders |
| Section Number | #94a9c6 | --color-sectionNumber | large Georgia section numerals |
| Kicker Indigo | #5e6097 | (mix of --tone-indigo-ink) | small section names under numerals ("MOTIVATION") |
| Eyebrow Ink | #587393 | --color-eyebrowInk | hero eyebrow |
| Result Gold | #947346 | --color-resultGoldBorder | selected cell outline in the results table |

The five-panel comparison and the diagrams also draw on the palette's muted tones (red #ba736d, green #5a9971, orange #b37a53, purple #967bb5, sky #6995cc), each paired with a darker ink.

## Tokens — Typography

- **Serif (display)**: declared `Georgia, "Times New Roman", serif`; renders Georgia (system). Substitute: Gelasio (metric-compatible with Georgia).
- **Sans (UI and body)**: declared `"Segoe UI", -apple-system, BlinkMacSystemFont, Arial, sans-serif`; renders Segoe UI on Windows, San Francisco on macOS. Substitute: Inter.

| Role | Selector | Size at 1440 (clamp) | Weight | Line-height | Tracking |
|---|---|---|---|---|---|
| Title | `.hero h1` | 108px (70px, 7.6vw, 108px) | 400 serif | .97 | -6px |
| Closing heading | `.closing h2` | 78px (46px, 6vw, 78px) | 400 serif | 1.12 | -.04em |
| Section numeral | `.section-number` | 44–64px (by viewport height) | 400 serif | 1 | -3px |
| Section heading | `h2` | 43px (30px, 3.3vw, 43px) | 400 serif | 1.2 | -1.1px |
| Hero subtitle | `.hero h1 span` | 35px (30px ≤1050px) | 400 serif | 1.25 | -1.2px |
| Subheading | `.prose h3` | 24px | 400 serif | 1.9 | -.4px |
| Equation | `.equation` | 23px serif | 400 | 2 | 0 |
| Wordmark | `.wordmark` | 18px | 650 | normal | -.6px |
| Body / deck | `.prose`, `.hero-deck` | 16px | 400 | 1.9 / 1.8 | 0 |
| Section subtitle | `.section-subtitle` | 15px | 600 | 1.5 | 0 |
| Summary, notes | `.hero-summary p`, `.insight-note` | 14–15px | 400 | 1.85 | 0 |
| Buttons, chips, tables | `.button-link`, `.resource-link`, `table` | 12px | 400 | 1.65 | 0 |
| Section name | `.section-name-text` | 12px uppercase | 700 | 1.15 | .04em |
| Chapter links | `.chapter-links a` | 11px (numerals 9px) | 400 | normal | 0 |
| Eyebrow, micro labels | `.eyebrow`, `.micro` | 10px uppercase | 550 | normal | 1.7px |
| Table header | `th` | 9px uppercase | 700 | 1.65 | 1px |

## Tokens — Spacing & Shapes

- **Radius**: 4px on buttons, chips, language switch, autoplay toggle and insight notes; diagram cells are slightly rounded inside the SVG.
- **Shadows**: none except a 2px sky ring on the pressed autoplay toggle.
- **Borders**: 1px #cdcdcd for all rules; 1px #c8c0af under table headers; 2px #82afe6 underline on the active chapter link; 2px #82afe6 left border on equations; 3px #6995cc left border on insight notes.

## Layout Metrics

- **Header**: max-width 1328px, padding 0 clamp(20px, 3.5vw, 44px) = 44px, height 78px.
- **Hero**: max-width 1240px centered (x 100–1340), padding 78px 0 70px; grid 1.25fr / 1fr with 48px gap; summary 57px below with a 210px label column and 34px gap.
- **Chapter bar**: sticky at top, 1px rules above and below, inner max-width 1240px, min-height 56px, 18px gaps.
- **Article**: `main.article` width calc(100% − clamp(40px, 7vw, 88px)), max-width 1160px, further limited at runtime (rendered 965px, x 238–1203). Text inset clamp(36px, 4.5vw, 60px) = 60px, so prose, tables and figures are 845px wide (x 298–1143).
- **Sections**: padding top clamp(24px, 12vh − 72px, 82px) (36px at 900px tall), bottom 76px, 1px #cdcdcd bottom border; opening block margin-bottom 48px; heading grid 88px numeral column + 32px gap + h2.
- **Tables**: margin 28px 0; header cells 13px 17px; body cells 16px 17px; first column 21% wide.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| >1350px | 44px | 16px | 7.6vw, max 108px | hero 1.25fr / 1fr |
| ≤1350px | 3.5vw | 16px | 7.6vw | hero, chapter bar and footer get side margins; hero padding-top 62px |
| ≤1250px | 3.5vw | 16px | 7.6vw | chapter bar hides its label and link numerals |
| ≤1050px | 3.5vw | 16px | 7.6vw (70px floor) | hero gap 20px; subtitle 30px; numeral column 72px |
| compact layout (script-set class) | 16–22px | 16px | 70px | 64px header without the meta text; single-column hero; text inset 0 |

## Components

- **Primary button** `.button-link.primary`: padding 13px 19px, radius 4px, #82afe6 fill, #203c60 Segoe UI 12px, trailing "↓" 28px from the label; hover lightens toward white.
- **Text link** `.text-link`: 12px #5d5d5d, 1px underline 4px below, trailing "↗".
- **Resource chip** `.resource-link`: min-height 40px, padding 8px 12px, 1px #a8bbcf border, radius 4px, #dae5f2 fill, #36669f 12px text, 16px logo left, "↗" right; hover border #82afe6.
- **Chapter bar link**: 11px #767676 with a 9px numeral at 60% opacity, padding 21px 0 18px, 2px transparent bottom border; current and hover #36669f with a #82afe6 underline. A 4px #82afe6 reading-progress line runs along its top.
- **Section opening**: numeral in Georgia 44–64px #94a9c6 stacked over a 12px/700 uppercase #5e6097 name in an 88px column; h2 Georgia 43px #373737 to its right; subtitle 15px/600 #36669f.
- **Comparison table**: 12px, header 9px/700 uppercase #767676 with 1px #c8c0af below, body cells 16px 17px with 1px #cdcdcd rules, first column 550 #373737; the last row (RAM-Net) filled #dae5f2 with its label in #36669f.
- **Five-panel comparison exhibit**: five equal tinted cards (red, green, orange, purple, sky tones at low alpha) each with a title in the tone's ink, a small token-bar diagram and a two-line caption.
- **Insight note** `.insight-note`: tinted sky fill (22% sky into white), 3px #6995cc left border, radius 4px, padding 18px 22px, 15px/1.85 #5d5d5d with a #36669f bold lead.
- **Equation block**: Georgia 23px, 15% paper-edge tint, 2px #82afe6 left border, padding 20px 28px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top nav | yes, non-standard | header with wordmark and language switch; section navigation is the sticky chapter bar below the hero |
| Title block | yes | huge Georgia name with a serif subtitle, left column |
| Authors / affiliations | absent from the hero | not shown in the first screen |
| Link buttons | yes | one pale blue button, a text link and tinted resource chips |
| Teaser | yes, non-standard | animated SVG of slot grids with dashed routes |
| TL;DR | yes | two-column "THE IDEA, IN BRIEF" |
| Chapter nav | yes | sticky numbered section bar with reading progress |
| Interactive figures | yes | embedded exhibits with autoplay toggle and timelines |
| Comparison panels | yes | five-panel tinted cards |
| Tables | yes | hairline tables with a tinted last row; an experiment table with tabs |
| References | yes | numbered 13px muted list |
| BibTeX | absent from the source | no code block |
| Footer | yes | 12px muted line with a top rule |

## Adapting to Other Content

- **Authors**: add a line under the deck in 12px Segoe UI #5d5d5d, names in #373737, affiliations as 9px superscripts in #36669f; keep it inside the 420px deck width or let it run to 610px.
- **Results table**: reuse the comparison table: 9px uppercase headers, 12px cells, hairlines; tint the proposed row #dae5f2 and set its label in #36669f; numbers right-aligned.
- **Long publication list**: a references-style list, 13px #767676, line-height 1.75, with titles in #373737 and venues in italics.
- **News**: a section with the numeral-plus-label opening ("09 NEWS"), then dated rows in 12px with dates in #36669f.
- **Raising contrast**: if readability matters more than the mood, set prose to #373737 at 17px; keep the paper and the pale accent.

## Do's and Don'ts

- Do keep the warm beige paper (#e8e2d3) everywhere; there are no white surfaces.
- Do use Georgia only for display (title, numerals, h2, h3, equations) and Segoe UI for everything else.
- Do open each section with a pale blue serif numeral and a small indigo label.
- Do keep the accent pale (#82afe6 fill, #36669f text); never saturate it.
- Don't add shadows or cards with borders; tinted fills and hairlines carry structure.
- Don't make buttons large; controls are 12px with 4px radii.
- Don't use more than one tinted row per table.

## Surfaces

Beige paper #e8e2d3 throughout; #dae5f2 chip and highlight fills; translucent paper for the sticky chapter bar; faint paper-edge tints for equations and notes. No white panels.

## Imagery

Custom animated SVG diagrams (slot arrays, routing lines, architecture blocks, bar arrays) in the paper palette; a five-panel comparison of attention variants in muted tones; result charts and tables. No photos.

## Layout

Two-column hero, then a sticky chapter bar and a single narrower article column (965px, text inset 60px) of numbered sections with interactive exhibits. About 18,300px tall, the longest page in this batch.

## Agent Prompt Guide

Quick colors: paper #e8e2d3, ink #373737, body #5d5d5d, muted #767676, hairline #cdcdcd, accent #82afe6, accent ink #36669f, button ink #203c60, chip #dae5f2 with #a8bbcf border, numeral #94a9c6, kicker #5e6097.

1. "Build a hero on #e8e2d3: eyebrow 10px/550 uppercase, letter-spacing 1.7px, #587393 with a 6px #82afe6 dot; h1 Georgia 108px weight 400, line-height .97, letter-spacing -6px, #373737; a Georgia 35px subtitle (line-height 1.25, -1.2px) 25px below; a 16px #5d5d5d deck at line-height 1.8, max 420px."
2. "Build hero actions: a button with #82afe6 fill, #203c60 Segoe UI 12px, padding 13px 19px, radius 4px and a trailing ↓; a 12px #5d5d5d underlined text link; below, chips 40px tall with #dae5f2 fill, 1px solid #a8bbcf, radius 4px, padding 8px 12px, #36669f 12px text and a 16px logo."
3. "Build a section opening: an 88px column with a Georgia numeral (44–64px, #94a9c6, letter-spacing -3px) over a 12px/700 uppercase #5e6097 label; 32px gap; h2 Georgia 43px/400 #373737, letter-spacing -1.1px; subtitle 15px/600 #36669f; prose 16px/1.9 #5d5d5d."

## Similar Pages

- Interactive "explorable" paper companions with sticky chapter navigation and animated diagrams.
- Warm paper-toned scholarly pages that pair Georgia display type with a system sans.

## Quick Start

```css
:root {
  --paper: #e8e2d3;
  --paper-edge: #c8c0af;
  --ink: #373737;
  --body: #5d5d5d;
  --muted: #767676;
  --line: #cdcdcd;
  --accent: #82afe6;
  --accent-ink: #36669f;
  --action-ink: #203c60;
  --chip: #dae5f2;
  --chip-border: #a8bbcf;
  --section-number: #94a9c6;
  --kicker: #5e6097;
  --eyebrow-ink: #587393;
  --serif: Georgia, "Times New Roman", serif;
  --sans: "Segoe UI", -apple-system, BlinkMacSystemFont, Arial, sans-serif;
}
body { background: var(--paper); color: var(--ink); font-family: var(--sans); }
```

## Provenance

- **URL**: https://muoncat.github.io/ramnet_web/
- **Paper**: RAM-Net: Linear-Time Sequence Modeling with Sparsely Addressable State (arXiv 2602.11958), Kaicheng Xiao et al.
- **Venue**: NeurIPS 2026.
- **Selection reason**: the arXiv comment states acceptance at NeurIPS 2026 and links this page.
- **Template credit**: custom page; no template credit shown.
- **Evidence used**: computed_style.py render at 1440×900 (computed styles, empty fonts_loaded because only system fonts are used, color share), the 1440 screenshot and tall capture, assets/site.css and data/palette.json read directly. Captured 2026-10-28.
