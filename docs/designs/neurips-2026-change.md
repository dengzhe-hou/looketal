# CROSS Swiss Grid — Style Reference

> A Zurich transit poster for a robot that never gets lost: one giant black word, red pencil notes, and hairlines everywhere.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share) and the 1440 screenshots, checked against the page's own stylesheets (assets/css/chrome.css for tokens, site.css for components, home.css for the hub page). The page also ships a full dark theme (toggle in the top bar and `prefers-color-scheme`); everything below describes the light theme that rendered. Sizes are fluid (`clamp()` with vw or container units), so each size is given as rendered at 1440 with the clamp in parentheses.

## Overview

CROSS is a Swiss-style product site rather than a paper page. A 34px black bar sits on top, then a warm off-white (#fafaf7) canvas with no container: everything hangs on a window-wide 12-column grid with 20px margins and 16px gutters. The masthead is a 283px Inter Tight "CROSS" wordmark that fills seven columns, with the words of the acronym (Change-, Robust, Online, Spatial memory, System) set at 13px in red (#c22914) inside the letters. Section titles are enormous (104px, weight 400, -0.05em tracking) between two 1px black rules. There are no radii and no shadows anywhere. Color arrives in full-bleed bands (yellow #f6ee1f, pink #f5a3b7, mint #a3e4d7, blue #1f61d6) in the Overview, and in the red square that marks the clip playing now.

## First Viewport

Color share of the 1440×900 viewport: #08090e 34% (the dark highlight video and black bar), #fafaf7 33% (canvas), #e6e6e4 13% and #616466 9% (light and grey frames inside the video), #fdfdfb 8%, #fbf7f1 3%. The ink is near-black on off-white; the only chroma above the fold is the red annotations.

Anatomy in DOM order (x positions at 1440):

1. **Top bar** `header.sh`: sticky, 34px tall, #000000, full width. Brand "CROSS" left (x 20), 13px/500 #f0efea. Centered nav (Benchmark, Full results, Replays, Docs, Papers) 13px/400 at rgba(240,239,234,.74), 18px apart. Right: "Paper ↗", "Code ↗" and a theme toggle. Gap to masthead: 10px (masthead top padding).
2. **Wordmark** `span.wm-mark`: "CROSS", Inter Tight 283px/400, line-height .73, letter-spacing -0.065em, #111110, left-aligned at x 11, spans columns 1–7 (815px wide, 207px tall).
3. **Acronym words** `span.wm-word`: absolutely placed inside the letters, 13px/400, -0.02em, #c22914.
4. **Strengths list** `ul.mast-points` (under the wordmark, columns 1–7): 4-column grid, 1px #111110 top rule, each item 15px/400 with 6px/5px padding and a 1px #d9d9d3 bottom hairline; notes ("soon", "every map node is an RGB image") 12.5px #66665f. Starts 19px below the wordmark.
5. **Title** `h1` (columns 8–12, x 846, top 48): 44px/400 (clamp 30px, 3.05vw, 60px), line-height 1.02, letter-spacing -0.04em, #111110, left-aligned, two lines. Gap 14px.
6. **Subtitle** `p.mast-sub`: 18px/300 (clamp 16px, 1.25vw, 24px), line-height 1.3, -0.015em, max-width 34em. Gap 13px.
7. **Links** `p.mast-links`: Get started, Benchmark, NeurIPS 2026 paper, Code ↗ as 16px/400 text links with a 1px underline drawn by a background gradient, 20px apart. Gap 56px (the install line is pushed to the column foot with `margin-top: auto`).
8. **Install line** `p.mast-install`: `bash install.sh --stereo` in JetBrains Mono 13px on #f2f2ef, 28px tall, 0 10px padding, butted against a black Copy button. Its baseline lines up with the bottom rule of the strengths list.
9. **Highlights section** at y 400: 1px #111110 top border. Left: the playlist video (928×522, x 20). Right column (x 964): "Highlights" 76px/400 (clamp 48px, 5.4cqw, 96px), line-height .9, "Every clip is a real run" 21px, then the now-playing label (red 0.6em square + "01 Relocalization", place name right in #66665f), the clip title 29px/400 -0.035em, a 17.5px/300 description, and grouped run-in lists of numbered clips.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #fafaf7 | --bg | page canvas (html, body), table header cells |
| Ink | #111110 | --ink, --rule | all text, h1, section titles, 1px section rules, Copy button fill |
| Bar Black | #000000 | (literal) | sticky top bar `header.sh` |
| Bar Ink | #f0efea | --night-ink | top bar brand and hovered nav links (nav at 74% alpha) |
| Stone | #66665f | --ink-3 | secondary text: place names, mast notes, stat captions, table headers |
| Hairline | #d9d9d3 | --line | row hairlines: strengths list, table rows |
| Code Wash | #f2f2ef | --surface-2, --code-bg | install chip, inline code, code blocks |
| Signal Red | #e4321b | --accent | now-playing square, active progress segment, focus outline, CROSS row bar in tables |
| Annotation Red | #c22914 | --accent-ink, --accent-hover | acronym words in the wordmark, Copy button hover |
| Band Yellow | #f6ee1f | --band-yellow | Overview band 1 (Best multi-session relocalization) |
| Band Pink | #f5a3b7 | --band-pink | Overview band 2 (Accurate tracking) |
| Band Mint | #a3e4d7 | --band-mint | Overview band 3 |
| Band Blue | #1f61d6 | --band-blue | Overview band 4, with white text |
| Good Green | #0b7040 | --good | Copy button after copying, string tokens in code |

Declared but not visible: --surface #ffffff, --accent-soft #fbe5e1, the dark-theme set (bg #0e0e0e, accent #ffc400), and the per-system chart colors (--c-orbslam3 #2a78d6 and others), which only appear inside benchmark charts.

## Tokens — Typography

- **Sans**: declared `"Inter Tight", "Helvetica Neue", Helvetica, Arial, sans-serif`; renders Inter Tight (variable, weights 200–700 loaded). Substitute: Inter Display, or Inter with tracking tightened by a further 0.02em.
- **Mono**: declared `"JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`; renders JetBrains Mono 400. Substitute: IBM Plex Mono.

| Role | Selector | Size at 1440 (clamp) | Weight | Line-height | Tracking |
|---|---|---|---|---|---|
| Wordmark | `.wm-mark` | 283px (fills 7 columns) | 400 | .73 | -0.065em |
| Section title | `.sx-h` | 104px (44px, 9.6vw, 104px) | 400 | 1 | -0.05em |
| Highlights title | `.hl-head .sx-h` | 76px (48px, 5.4cqw, 96px) | 400 | .9 | -0.05em |
| Stat figure | `.fig-v` | 101px (52px, 7vw, 108px) | 200 | .9 | -0.06em |
| Paper title | `.mast h1` | 44px (30px, 3.05vw, 60px) | 400 | 1.02 | -0.04em |
| Statement | `.sx-statement` | 40px (22px, 2.75vw, 40px) | 200, bold spans 600 | 1.14 | -0.03em |
| Overview name | `.ov-name` | 37px (24px, 2.6vw, 38px) | 400 | 1.05 | -0.035em |
| Clip title | `.hl-now-t` | 29px | 400 | 1.05 | -0.035em |
| Section aside / mid | `.sx-mid` | 21px | 400 | 1.2 | -0.02em |
| Subtitle | `.mast-sub` | 18px | 300 | 1.3 | -0.015em |
| Body | `body` | 16px | 400 | 1.45 | -0.005em |
| Table cell | `.table td` | 15px | 400 | 1.45 | -0.01em |
| Table head, captions, footer | `.table thead th`, `.sx-cap`, `.sf` | 13px | 400 | 1.25–1.45 | 0 |
| Acronym words | `.wm-word` | 13px | 400 | 1 | -0.02em |
| Code | `.code pre` | 13.5px mono | 400 | 1.75 | 0 |

Hierarchy is built from size and tracking alone; weights stay at 200–400 and bold (600) appears only inside statements.

## Tokens — Spacing & Shapes

- **Radius**: 0 everywhere (`--radius: 0px`): buttons, code, frames, tables.
- **Shadows**: none (`--shadow: none`). The only inset "shadow" is the 3px red bar `inset 3px 0 0 #e4321b` on the CROSS row of tables.
- **Rules**: 1px #111110 for section heads (top and bottom), stat tops, step tops, table tops and the footer; 1px #d9d9d3 for rows. Code blocks have a 3px #111110 left border.
- **Spacing unit**: page margin `--m` 20px, gutter `--g` 16px; vertical rhythm from clamps (36px above section content, about 94px below).

## Layout Metrics

- **Container**: none. `.container` is `width: 100%; max-width: none; padding-inline: 20px`. Content runs on `.sx-grid`, 12 columns of `minmax(0,1fr)` with 16px gaps, so a column is (100vw − 40px − 176px) / 12 ≈ 102px at 1440.
- **Masthead**: 12-column grid, padding 10px 20px 34px (bottom clamp 22px, 2.6vw, 34px); wordmark columns 1–7, title column 8–12, row gap 18px.
- **Section head**: `.sx-head` full-bleed, 1px rules top and bottom, padding .02em 20px .06em.
- **Section body**: padding-top 36px (clamp 20px, 2.6vw, 36px), padding-bottom 94px (clamp 52px, 6.5vw, 104px).
- **Stats**: `.figures` 3 columns, column gap 16px, top margin 64px, each stat with 1px #111110 top rule and 8px top padding.
- **Overview bands**: full-bleed; text row padding .5rem 20px 1.6rem, name in columns 1–4 and sentence in 5–12; clip grid below, 4 across (or 3), gap 1.1rem 16px, 16:9 frames.
- **Highlights**: at ≥1200px the player takes about 8 columns (928px) and the list the rest.
- **Method steps**: 4 across (`span 3`), 1px top rule, 32px row gap.

| Breakpoint | Margin / gutter | Body | Title (h1) | Grid change |
|---|---|---|---|---|
| ≥1200px | 20px / 16px | 16px | 3.05vw, max 60px | player left, list right |
| ≤1199px | 20px / 16px | 16px | 3.05vw | highlights stack |
| ≤1000px | 20px / 16px | 16px | 30px floor | masthead stacks to one column; strengths 2 across; method steps 2 across |
| ≤900px | 20px / 16px | 16px | 30px | top-bar nav becomes a menu button; footer 2 columns |
| ≤760px | 12px / 10px | 16px | 30px | grid becomes 4 columns; clip grids 2 across; steps 1 across |
| ≤640px | 12px / 10px | 16px | 30px | stats 1 across |

## Components

- **Top bar**: sticky `header.sh`, height 34px, #000000, 13px Inter Tight, line-height 1. Nav links rgba(240,239,234,.74), hover #f0efea, current page underlined (1px, 4px offset). External links carry "↗".
- **Text link** `.sx-link`: #111110, no text-decoration; underline is `background-image: linear-gradient(currentColor,currentColor)` at `100% 1px` on the baseline; hover shrinks it to `0% 1px` over .25s. Overview "link-arrow" variant appends "→".
- **Copy button** `.copy`: 28px tall, padding 0 10px, radius 0, #111110 fill, #ffffff 12.5px text with a 13px stroke icon on the left; hover #c22914; after copy #0b7040.
- **Section head**: full-bleed 1px #111110 rules above and below, 104px title flush left, optional aside (21px) at its baseline on the right.
- **Stat** `.figures li`: 1px #111110 top rule, 8px padding-top; figure 101px weight 200, -0.06em, tabular numerals; label 16.6px; comparison line 13px #66665f.
- **Overview band** `.sx-band--yellow|pink|mint|blue`: full-bleed fill, ink forced to #111110 (white on blue), 37px name left, 37px sentence right with 600-weight phrases, then 16:9 clip frames with 13px captions.
- **Playlist progress** `.sx-track`: segments 2px tall in 16% ink, 3px apart; the playing segment fills #e4321b; on hover segments grow to 6px.
- **Now-playing label**: 15px, a 0.6em #e4321b square before the number, place name right-aligned in #66665f.
- **Text tabs** `.sx-tabs`: 1px #111110 top rule, tabs are bare 30px text at 60% ink; selected and hover go to full #111110.
- **Table** `.table`: 15px, top rule 1px #111110 on the wrapper, header 13px #66665f on #fafaf7 (sticky) with a 1px #111110 bottom rule, rows 9px 12px 9px 0 padding with 1px #d9d9d3 hairlines, hover 4% ink tint; CROSS row tinted 7% red with a 3px red inset bar.
- **Code block** `.code`: #f2f2ef, 3px #111110 left border, radius 0, JetBrains Mono 13.5px/1.75, prompt in #c22914, Copy button top-right at 8px.
- **Method step**: 1px top rule, 66px weight-200 numeral, 29px h3, 15.5px/300 text.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top nav | yes | sticky 34px black bar with centered links |
| Title block | yes, non-standard | giant wordmark with red acronym notes; the real title is a 44px h1 in a right column |
| Authors / affiliations | absent from the masthead | authors appear only in the Papers section and BibTeX |
| Link buttons | yes, non-standard | underlined text links, no pills |
| Install snippet | yes | mono chip with black Copy button in the masthead |
| Teaser video | yes | playlist player with segmented progress and grouped clip list |
| Summary + stats | yes | 40px light statement, three 101px stat figures |
| Overview bands | yes | four full-bleed color bands with clip grids |
| Benchmark charts | yes | text tabs over SVG charts with hairline grids, per-system colors |
| Video tour | yes | chaptered video with a timestamp list |
| Method | yes | four numbered steps with illustrations |
| Getting started | yes | text plus code blocks and a sensor-mode table |
| Papers list | yes | papers listed as rows under the section head |
| BibTeX | yes | code block with Copy |
| Footer | yes | 1px top rule, 12-column footer, 13px |

## Adapting to Other Content

- **More authors**: put them in a 13–15px row under the h1 in the title column, separated by 20px gaps like `.mast-links`; affiliations in #66665f. Do not put them in the wordmark area.
- **Results table**: use `.table` exactly: 15px cells, 13px #66665f headers, black top rule, #d9d9d3 hairlines, and tint the proposed method's row 7% red with the 3px red inset bar. Numbers right-aligned in tabular numerals.
- **Long publication list**: one `.sx-row` per paper (2.2em number column, title, venue right), 1px #d9d9d3 hairline between rows, 15–16px text.
- **News**: a run-in list under a 104px "News" section head; date in tabular numerals left, text 16px; no cards.
- **No acronym**: set the project name as the wordmark anyway; if it is long, let it fill the 7-column cell (font-size from container width) and drop the red annotations.

## Do's and Don'ts

- Do set everything in one family (Inter Tight) and build hierarchy from size and negative tracking.
- Do keep radii at 0 and shadows off; separate with 1px #111110 rules.
- Do let section titles run at 104px between two full-bleed rules.
- Do reserve red (#e4321b / #c22914) for marking: now playing, annotations, the proposed method row.
- Do use the four band colors only as full-bleed section backgrounds with black text.
- Don't use pill or filled link buttons; links are underlined text.
- Don't center content; everything is flush left on the grid.
- Don't add a max-width container; the grid spans the window with 20px margins.
- Don't use bold for headings; 400 at large sizes is the look.

## Surfaces

Off-white #fafaf7 canvas; #000000 top bar; #f2f2ef for code and the install chip; full-bleed yellow, pink, mint and blue bands in Overview; dark video frames. No cards and no elevation.

## Imagery

Screen recordings of a dark sci-fi-styled SLAM dashboard (night vs. day maps, comparison panels), 16:9 clip grids with 13px captions, SVG benchmark charts with hairline grids, and line illustrations in the method steps. Media is never rounded or framed.

## Layout

Window-wide Swiss grid: masthead split 7/5, then alternating full-bleed section heads and grid content (split player/list, three stats, banded clip grids, charts, four steps, table). The page is about 9,200px tall.

## Agent Prompt Guide

Quick colors: canvas #fafaf7, ink #111110, bar #000000 with #f0efea text, secondary #66665f, hairline #d9d9d3, code #f2f2ef, accent #e4321b, annotation #c22914, bands #f6ee1f / #f5a3b7 / #a3e4d7 / #1f61d6.

1. "Build a section head: full-bleed, 1px solid #111110 border top and bottom, padding .02em 20px .06em; h2 in Inter Tight 104px weight 400, letter-spacing -0.05em, line-height 1, color #111110, flush left; optional 21px aside right-aligned at the baseline."
2. "Build a stat row: 3-column grid with 16px gaps; each item has a 1px solid #111110 top border and 8px padding-top; value in Inter Tight 101px weight 200, letter-spacing -0.06em, line-height .9, tabular numerals; label 16.6px #111110; note 13px #66665f."
3. "Build a masthead: 12-column grid, padding 10px 20px 34px, 16px gaps; columns 1–7 hold the project name at 283px weight 400, line-height .73, letter-spacing -0.065em, with 13px #c22914 words placed inside the letters; columns 8–12 hold a 44px/400 h1 (line-height 1.02, -0.04em), an 18px/300 subtitle, and 16px text links underlined with a 1px background-gradient line that shrinks on hover."

## Similar Pages

- Swiss/International-style product sites with one-family grotesk typography and a 12-column full-bleed grid.
- Research software pages that read like a product launch (benchmark, docs and replays sections) rather than a paper abstract page.

## Quick Start

```css
:root {
  --bg: #fafaf7;
  --ink: #111110;
  --ink-3: #66665f;
  --line: #d9d9d3;
  --rule: #111110;
  --bar: #000000;
  --bar-ink: #f0efea;
  --code-bg: #f2f2ef;
  --accent: #e4321b;
  --accent-ink: #c22914;
  --good: #0b7040;
  --band-yellow: #f6ee1f;
  --band-pink: #f5a3b7;
  --band-mint: #a3e4d7;
  --band-blue: #1f61d6;
  --radius: 0px;
  --m: 20px;
  --g: 16px;
  --header-h: 34px;
  --font: "Inter Tight", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}
@media (max-width: 760px) { :root { --m: 12px; --g: 10px; } }
```

## Provenance

- **URL**: https://jiaming.im/CROSS/
- **Paper**: Change-Robust Online Topological Memory for Long-Term Relocalization and Semantic Navigation (arXiv 2605.02227), Jiaming Wang et al.
- **Venue**: NeurIPS 2026.
- **Selection reason**: the arXiv comment states acceptance at NeurIPS 2026 and the abstract links this page.
- **Template credit**: custom site; no template credit in the footer.
- **Evidence used**: computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440 screenshot and tall capture, and the page's chrome.css, site.css and home.css read directly. Captured 2026-10-28.
