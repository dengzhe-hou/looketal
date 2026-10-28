# RenderFormer-V2 — Style Reference

> A lab notebook typeset by a Swiss printer: square black buttons, one cobalt rule over the masthead, and every section tagged with the color of the primitive it explains.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, plus targeted probes of the hero, stat strip, section heads, tables and cards), the 1440×900 shot and a full-page capture, and the page's compiled Next.js stylesheet (`_next/static/css/9ee14831dd2b4b3f.css`) and `index.html`. Root font size is 16px, so `rem` values below are converted at 16px; the body itself is 17px. Section kicker and tab colors are set per section through an inline custom property, so they were probed on each rendered section.

## Overview

A long (16,555px) single-column page built from alternating full-width bands: pale sage paper #f4f6f2 and white #ffffff, separated by 1px #d4dad4 rules. A translucent sticky nav (58px) sits above a 6px cobalt band (#1f6fb2) that caps the white hero. The hero is a two-column grid: left, an "ECCV 2026" kicker with a 34px cobalt dash, an 800-weight Manrope title "RenderFormer V2" with "V2" in cobalt, a 22.7px subtitle, a short pitch, authors, affiliations and two rows of square buttons (filled ink for arXiv and Paper, outlined for the rest); right, a 490px square 3×3 plate of rendered scenes. Under it, a "HIGHLIGHTS" strip of five ruled stat columns (34.4px/800 numbers, two in cobalt). Each section opens with a 62×4px color tab and a tracked uppercase kicker ("01 / ARCHITECTURE") in that section's primitive color, then a 36.8px/800 headline. Content uses square-marker bullet lists, flat bordered cards and diagrams with no radius, a V1-vs-V2 comparison table with a cobalt-washed V2 column, three line charts, a 3- and 4-column image gallery, a poster and a BibTeX block. Almost nothing is rounded and nothing casts a shadow at rest.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 63.0% (hero card) plus near-whites #f7f8f5 7.2%, #f5f2f4 3.0% and #fffffe 1.9%; dark render backgrounds and ink #181315 9.5%; mid gray #656562 8.7% and pale gray-green #c3cbca 6.5% from the render plate and stat strip; a trace of green #91ff90 0.1% from the Cornell-box render. Cobalt covers too little area to form its own cluster.

Anatomy in DOM order (desktop 1440px):

1. **Sticky nav** (`nav.nav`, 0–58px): background rgba(244,246,242,.86) with `backdrop-filter: saturate(1.6) blur(12px)`, 1px #d4dad4 bottom border. Inner row max 1120px with 32px gutters (content x 192–1248). Left: 26px logo image (4px radius) + "RenderFormer V2" 14.4px/700 #16202b with "V2" in #1f6fb2. Right: links 13.28px/600 #44535f, 22px gaps, padding 4px 0, 2px transparent bottom border; "More ⌄" dropdown last.
2. **Hero band** (`.hero-band`, y 58–64): 6px solid #1f6fb2 across the full width; the hero below is white with a 1px #d4dad4 bottom border.
3. **Hero grid** (`.hero-grid`): padding 62px 32px 54px, columns minmax(0,1.02fr) minmax(0,.98fr), gap 56px → text column 510px at x=192, figure 490px at x=758.
4. **Venue kicker** (`.venue`, y=133): 11.52px/700 uppercase, letter-spacing .16em, #1f6fb2, preceded by a 34×3px #1f6fb2 dash (10px gap). Margin-bottom 22px.
5. **Title** (`h1.title`, y=174): 54.4px/800, line-height 1.04, letter-spacing -0.028em, #16202b; "V2" #1f6fb2. Gap 16px.
6. **Subtitle** (`.subtitle`, y=246): 22.72px/600, line-height 1.28, letter-spacing -0.012em, #16202b, two lines. Gap 16px.
7. **Pitch** (`.pitch`, y=320): 16.64px/400 #44535f, max 46ch (467px). Gap 30px.
8. **Authors** (`.authors`, y=404): 15.84px/600 #16202b, gaps 6px 20px, two rows; superscripts .66em #78868f; hover #1f6fb2 with a 1px #1f6fb2 underline. Gap 12px.
9. **Affiliations** (`.affils`, y=476): 14.08px #78868f, gaps 4px 20px. Gap 28px.
10. **Buttons** (`.links`, y=526): two rows of 40px square buttons, 8px gap; arXiv and Paper filled #16202b with white 14.4px/600 text; Supplement, Code, Model, Poster outlined (#d4dad4 border, #44535f text); each has a 16px line icon on the left.
11. **Hero figure** (y=126): 490×490 square plate (3×3 renders), 1px #d4dad4 border on #ecefea; caption 13.12px #78868f, 10px below. Hero ends at y=724.
12. **Highlights strip** (`section.stats`, from y=724): white; "HIGHLIGHTS" eyebrow 11.2px/700 #78868f with padding 22px 0 12px and a 1px #d4dad4 rule; five stat columns starting at y=803.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #f4f6f2 | --paper | body background, alternate section bands, cards and charts inside white sections |
| Card White | #ffffff | --card | hero, highlights strip, `.section--card` bands, footer, button text on filled buttons |
| Panel | #ecefea | --panel | image backgrounds behind renders (hero plate, gallery tiles) |
| Ink | #16202b | --ink | title, subtitle, section headlines, sub-titles, authors, stat values, filled button fill, table top and bottom 2px rules |
| Ink 2 | #44535f | --ink2 | body text, nav links, bullets, outline button text |
| Ink 3 | #78868f | --ink3 | eyebrows, affiliations, captions, stat notes, table header text, footer text, Limitations kicker |
| Rule | #d4dad4 | --rule | nav and hero borders, section dividers, outline button borders, image borders, sub-title underline |
| Rule Soft | #e4e8e2 | --rule-soft | table row rules, card/chart/diagram borders inside white sections |
| Cobalt | #1f6fb2 | --accent | hero band, venue kicker and dash, "V2", accented stat values, Overview/Attention/Poster kickers and tabs, link text, button hover fill, V2 table column header |
| Cobalt Wash | rgba(31,111,178,0.07) | --accent-wash | V2 column in the comparison table, best-row cells, table row hover |
| Triangle Blue | #4f88c1 | --c-tri | Architecture kicker and tab, triangle tokens in diagrams |
| Volume Green | #5bb163 | --c-vol | Coverage kicker and tab |
| Environment Violet | #8e4fd0 | --c-env | Material kicker and tab, material-code block fill |
| Camera Red | #d9432f | --c-cam | Evaluation kicker and tab, V1 lines in charts |
| Light Gold | #dfae0c | --c-light | Gallery kicker and tab, light tokens |
| Summary Orange | #e8863b | --c-sum | summary tokens in the attention diagram |
| Register Gray | #8d989f | --c-reg | register tokens in the attention diagram |
| Violet Ink | #6d33ab | (literal, `.mop`) | operator box text in the material flow, on rgba(142,79,208,.11) |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans | "Avenir Next", Avenir, "Manrope", system-ui, -apple-system, "Segoe UI", sans-serif | Manrope 400, 500, 600, 700, 800 (web font); Avenir Next would win on macOS where installed | Manrope |
| Mono | "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace | IBM Plex Mono 400 | IBM Plex Mono |

| Role | Selector | Size / weight / line-height / tracking | Color |
|---|---|---|---|
| Title | `.title` | clamp(2.2rem, 4.4vw, 3.4rem) → 54.4px / 800 / 1.04 / -0.028em | #16202b, `em` #1f6fb2 |
| Subtitle | `.subtitle` | clamp(1.12rem, 1.9vw, 1.42rem) → 22.72px / 600 / 1.28 / -0.012em | #16202b |
| Section headline | `.sec-title` | clamp(1.65rem, 3vw, 2.3rem) → 36.8px / 800 / 1.14 / -0.024em, max 26ch | #16202b |
| Section kicker | `.sec-kicker` | .74rem = 11.84px / 700 / uppercase / .19em | per-section color |
| Sub-title | `.sub-title--rule` | 1.18rem = 18.88px / 700 / -0.012em, 12px padding + 1px #d4dad4 underline | #16202b |
| Eyebrow | `.eyebrow` | .7rem = 11.2px / 700 / uppercase / .16em | #78868f |
| Body | `body` | 17px / 400 / 1.62 | #44535f |
| Lead | `.lead` | 1.06rem = 16.96px | #44535f |
| Bullets | `.bullets li` | 1.02rem = 16.32px, 9px square marker | #44535f |
| Nav link | `.nav-links` | .83rem = 13.28px / 600 | #44535f |
| Button | `.btn` | .9rem = 14.4px / 600 | white or #44535f |
| Stat value | `.stat-value` | clamp(1.7rem, 2.6vw, 2.15rem) → 34.4px / 800 / 1 / -0.03em, tabular | #16202b or #1f6fb2 |
| Stat note | `.stat-note` | .82rem = 13.12px / 1.42 | #78868f, `b` #44535f 600 |
| Table | `.table` | .9rem = 14.4px tabular; head .78rem / 700 uppercase / .05em | body #44535f, head #78868f |
| Compare table | `.table--compare` | .88rem = 14.08px; row labels 600 #78868f | V2 column #16202b |
| Caption | `.figcap`, `.hero-figure figcaption` | .84rem / .82rem | #78868f |
| BibTeX | `.bib pre` | IBM Plex Mono .81rem = 12.96px / 1.65 | #44535f |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow / effect |
|---|---|---|---|
| Buttons | 0 | 1px #16202b (filled) or #d4dad4 (outline) | hover translateY(-1px) |
| Hero plate, gallery images | 0 | 1px #d4dad4 | gallery hover scale(1.014) |
| Cards, diagrams, charts | 0 | 1px #d4dad4 (on paper) or #e4e8e2 (inside white sections) | none |
| Flow steps (`.mstep`), material block | 3px | 1px #d4dad4 | none |
| Nav logo | 4px | none | none |
| Bullet markers, chips | 1px / 2px | none | none |
| Nav "More" menu | 0 | 1px #d4dad4 | `0 14px 34px rgba(22,32,43,.11)` |
| Chart tooltip | 0 | 1px #d4dad4 | `0 8px 22px rgba(22,32,43,.13)` |
| Poster link | 0 | 1px #d4dad4 | hover `0 12px 32px rgba(22,32,43,.14)`, translateY(-2px) |

## Layout Metrics

- **Container**: `.wrap`, `.nav-inner`, `.hero-grid`, `.stats-inner`: max-width 1120px, margin auto, padding 0 32px → content x 192–1248 (1056px) at 1440. Prose max 74ch (`--prose`).
- **Hero**: padding 62px 32px 54px; grid 1.02fr / .98fr with 56px gap (510px + 490px); hero 666px tall including the 6px band.
- **Highlights**: label padding 22px 0 12px; grid 5 equal columns, padding 26px 0 32px; each stat padding 0 24px with a 1px #d4dad4 left rule (first has none).
- **Sections**: padding 84px 0, 1px #d4dad4 bottom border, alternating #f4f6f2 and #ffffff (`.section--card`); head margin-bottom 34px; tab 62×4px, 14px above the kicker; headline 10px below the kicker; lead 18px below; sub-blocks 62px apart.
- **Grids**: gap 26px; `.grid-2/3/4/6` (6 uses 14px); charts row 3 × 340px with 18px gap; gallery 4 columns (22px row, 20px column gap), `.gallery--wide` 3 columns; mask grid 1.3fr / 1fr with 40px gap.
- **Footer**: white, 1px #d4dad4 top, padding 34px 0, 13.6px #78868f, nav links 600 #44535f with 20px gaps.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1180px | 32px | 17px | 54.4px | full nav |
| ≤1180px | 32px | 17px | 51.9px (4.4vw) at 1180 | Results, Gallery, Poster, BibTeX links hidden (kept in More) |
| ≤1080px | 32px | 17px | 47.5px | hero single column (gap 40px, padding-top 48px); stats 3 columns; gallery and grid-6 3 columns; charts 2 + 1 |
| ≤940px | 32px | 17px | 41.4px | all nav text links hidden, More only |
| ≤860px | 22px | 17px | 37.8px | sections padding 60px; grid-2/3/4 → 2 columns; charts, mask and material grids 1 column; token rows stack |
| ≤620px | 22px | 16px | 35.2px (2.2rem floor) | stats 2 columns (last spans 2); all galleries 2 columns; buttons stretch |

## Components

- **Filled button** (`.btn`): height 40px, padding 0 15px, 14.4px/600 white on #16202b, 1px #16202b border, radius 0, 8px gap to a 16px left icon (X logo for arXiv, document for Paper). Hover: fill and border #1f6fb2, translateY(-1px).
- **Outline button** (`.btn-ghost`): same box, transparent, #44535f text, 1px #d4dad4 border, icons paperclip, GitHub, model, poster. Hover: #16202b fill, white text.
- **Venue kicker** (`.venue`): 34×3px #1f6fb2 dash (lifted 4px) + 10px gap + 11.52px/700 uppercase #1f6fb2 text, .16em tracking.
- **Stat column** (`.stat`): 34.4px/800 tabular value (superscripts .5em), accented values #1f6fb2, note 13.12px #78868f 11px below with bold fragments in #44535f; columns divided by 1px #d4dad4 rules.
- **Section head** (`.sec-head`): 62×4px tab and 11.84px/700 kicker in the section color (#1f6fb2, #4f88c1, #5bb163, #8e4fd0, #d9432f, #dfae0c, or #78868f for Limitations), 36.8px/800 headline max 26ch.
- **Square bullets** (`.bullets li`): 24px left padding, 9×9px marker (1px radius) at .56em, colored with the section's color (cobalt by default).
- **Rule sub-title** (`.sub-title--rule`): 18.88px/700 #16202b, 12px bottom padding, 1px #d4dad4 underline, 22px margin below.
- **Comparison table** (`.table--compare`): left-aligned; header 12.48px/700 uppercase #78868f with a 2px #16202b top rule and 1px #d4dad4 bottom; row labels 600 #78868f at 21% width; V2 column on rgba(31,111,178,0.07) with 14px side padding, header in #1f6fb2, cells #16202b; rows separated by 1px #e4e8e2; final row closes with a 2px #16202b rule.
- **Results table** (`.table`): numbers right-aligned, padding 10px 14px; best row on the cobalt wash, 700 #16202b; hover row wash.
- **Card / diagram / chart**: flat, 1px border, padding 26px 28px (card), 20px (diagram), 18px 18px 12px (chart); on white sections they switch to #f4f6f2 fill with #e4e8e2 border. Chart titles .94rem/700 #16202b, subtitles .79rem #78868f; series V2 #1f6fb2, V1 #d9432f, Cycles dashed gray.
- **Gallery tile** (`.shot`): square image with 1px #d4dad4 border on #ecefea, 14.08px/600 #16202b name 10px below, .79rem #78868f note.
- **BibTeX** (`.bib`): max 820px; pre on white (or paper inside white sections), 1px #d4dad4, padding 22px 24px, IBM Plex Mono 12.96px; copy button top-right 32px tall, .79rem/600 #44535f, 1px #d4dad4, hover #1f6fb2 text and border.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky nav with More menu | yes | translucent paper with blur and 1px rule |
| Accent band | yes | 6px #1f6fb2 strip above the hero |
| Title / authors / affiliations | yes | left column of a two-column hero |
| Link buttons | yes | square filled + outline buttons with left icons |
| Teaser | yes | 490px square 3×3 render plate |
| Stat strip | yes | five ruled columns under a "HIGHLIGHTS" eyebrow |
| Abstract | present but non-standard | the Overview section's lead paragraphs serve as the abstract |
| Comparison table | yes | V1 vs V2 with cobalt-washed V2 column |
| Method diagrams | yes | inline SVG diagrams and an HTML flow in flat bordered boxes |
| Results charts and tables | yes | three line charts with data-table disclosures; numeric tables with best-row wash |
| Gallery | yes | square clips and stills in 3 and 4 columns |
| Poster | yes | bordered image link with hover lift |
| Limitations | yes | gray-kicker section |
| BibTeX | yes | mono block with copy button |
| Footer | yes | white bar with links and copyright |

## Adapting to Other Content

- **More authors**: keep the flex-wrapped 15.84px/600 row with 6px 20px gaps; it wraps inside the 510px column, adding about 33px per row.
- **A results table**: use `.table` at the 1056px content width: 14.4px tabular cells, 2px #16202b top and bottom rules, 1px #e4e8e2 row rules, best row on rgba(31,111,178,0.07) in 700 #16202b. Do not round or shadow it.
- **Long publication or news lists**: use the square-bullet list (16.32px #44535f, 9px cobalt markers, 11px gaps) or rule sub-titles (18.88px/700 with a 1px #d4dad4 underline) per year.
- **More sections**: alternate #f4f6f2 and #ffffff bands at 84px padding and give each a 62×4px tab and kicker; pick its color from the primitive palette only when the section is about that primitive, otherwise #1f6fb2.
- **More stats**: the strip holds five columns at 1440; a sixth should start a second row rather than squeeze the 34.4px values.

## Do's and Don'ts

- Do keep every corner square except the 3px flow steps and the 4px logo.
- Do let cobalt #1f6fb2 carry identity: band, kicker, "V2", accented stats, link text, button hovers.
- Do color-code section tabs and kickers by the scene primitive they describe, using the --c-* palette.
- Do separate bands with 1px #d4dad4 rules and alternating paper/white fills instead of shadows.
- Don't round buttons or cards, and don't add drop shadows at rest.
- Don't use the primitive colors for body text or large fills; they appear as tabs, markers, chart lines and diagram tokens.
- Don't center the hero; it is left-aligned against a square figure.

## Surfaces

Sage paper #f4f6f2 page with white #ffffff bands for the hero, highlights, every second section and the footer; inside white bands, cards, charts, diagrams and code switch to paper fill with #e4e8e2 borders. The nav is paper at 86% opacity with `saturate(1.6) blur(12px)`. The only solid color fills are the 6px cobalt band, filled ink buttons and the violet material-code block.

## Imagery

Square path-traced style renders (Cornell boxes, glossy spheres on a neon floor, teapots, smoky bunnies, room interiors) on black, shown in a 3×3 hero plate and in 3- and 4-column galleries; flat vector diagrams (attention mask with gray, gold, orange and blue token columns) and thin line charts in blue and red; an academic poster.

## Layout

A 1056px left-aligned column throughout: two-column hero, five-column stat strip, then sections of headline, bullets and one wide module (table, diagram pair, chart triple or gallery). Rhythm comes from 84px band padding and full-width 1px rules.

## Agent Prompt Guide

Quick colors: paper #f4f6f2, card #ffffff, panel #ecefea, ink #16202b, body #44535f, muted #78868f, rule #d4dad4, soft rule #e4e8e2, cobalt #1f6fb2, primitive tabs #4f88c1 / #5bb163 / #8e4fd0 / #d9432f / #dfae0c.

1. "Build a white hero under a 6px #1f6fb2 band: 1120px container with 32px gutters, padding 62px 32px 54px, grid 1.02fr / .98fr with 56px gap. Left: a 34×3px #1f6fb2 dash and 11.52px/700 uppercase kicker (.16em, #1f6fb2), a 54.4px/800 Manrope title (#16202b, letter-spacing -0.028em) with the version in #1f6fb2, a 22.72px/600 subtitle, a 16.64px #44535f pitch, 15.84px/600 authors and 14.08px #78868f affiliations. Right: a square image with a 1px #d4dad4 border."
2. "Make square buttons: height 40px, padding 0 15px, 14.4px/600, radius 0, 8px gaps, 16px left icon. Filled: #16202b fill and border, white text, hover #1f6fb2. Outline: transparent, #44535f text, 1px #d4dad4 border, hover #16202b fill with white text."
3. "Create a section head and stat strip: a 62×4px tab and 11.84px/700 uppercase kicker (.19em) in the section color, then a 36.8px/800 #16202b headline (max 26ch). Stat strip: 5 columns, each padding 0 24px with a 1px #d4dad4 left rule; value 34.4px/800 tabular #16202b or #1f6fb2; note 13.12px #78868f 11px below."

## Similar Pages

- Swiss-style graphics research pages with square buttons, a thin accent band and a stat strip.
- Next.js project pages that alternate paper and white bands and color-code sections.

## Quick Start

```css
:root {
  --paper: #f4f6f2;
  --card: #ffffff;
  --panel: #ecefea;
  --ink: #16202b;
  --ink2: #44535f;
  --ink3: #78868f;
  --rule: #d4dad4;
  --rule-soft: #e4e8e2;
  --accent: #1f6fb2;
  --accent-wash: rgba(31, 111, 178, 0.07);
  --c-tri: #4f88c1;
  --c-vol: #5bb163;
  --c-light: #dfae0c;
  --c-env: #8e4fd0;
  --c-cam: #d9432f;
  --c-reg: #8d989f;
  --c-sum: #e8863b;
  --font-sans: "Avenir Next", Avenir, "Manrope", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  --measure: 1120px;
  --prose: 74ch;
  --gutter: 32px;
  --nav-h: 58px;
}
```

## Provenance

- **URL**: https://renderformer.github.io/v2/
- **Paper**: RenderFormer-V2: Neural Rendering with Heterogeneous Scene Primitives (arXiv 2609.05738), Chong Zeng, Yue Dong, Pieter Peers, Lvmin Zhang, Maneesh Agrawala.
- **Venue**: ECCV 2026.
- **Selection reason**: the arXiv comment states acceptance at ECCV 2026 and links this project page.
- **Template credit**: none stated; a custom Next.js static export; footer reads "© 2026 The Authors".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted probes of hero, stats, per-section kickers and tabs, tables, cards and footer, the 1440×900 shot and a full-page capture, and the compiled stylesheet and `index.html` read directly, on 2026-10-28.
