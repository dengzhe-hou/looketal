# AEON Night Serif — Style Reference

> An observatory at dusk: a small-caps serif name on deep navy, an amber thread through the controls, and pale reading rooms below.

**Theme:** both

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share) and the 1440 screenshots, checked against the page's only stylesheet, static/css/aeon.css. The page alternates two scoped color schemes (`.sec--night` and the day `.sec`), so the theme is "both": a navy hero and gallery around light reading sections. Where the stylesheet and the render disagree (the venue line), the render is used.

## Overview

AEON opens on a full-viewport navy (#0b1430) hero with a faint amber radial glow behind an interactive 4D viewer. On the left, a 160px "AEON" wordmark in Spectral SC Light (the markup says "Aeon"; the small-caps face renders it as capitals), a 32px Spectral Light subtitle, a grotesk lede, underlined author names and outlined pill buttons. On the right, a 448px square canvas with a split RGB/Depth/Normal comparison, a column of eight thumbnails, a tick-mark timeline and a segmented mode switch. Below, the page turns to a cool off-white (#f2f4f8) single 960px column with Spectral Light section titles, justified Schibsted Grotesk text, method figures on white rounded plates, and a paradigm table. A second navy band holds a 62-tile gallery of generated worlds; the page ends on a light BibTeX section.

## First Viewport

Color share of the 1440×900 viewport: #0b1430 58% (hero ground), #14192f 15% (glow and dark video areas), #9f9379 14% (the amber-lit balloon video), #0b142f 4%, #0b1431 4%, #0c1126 2%. The fold is almost entirely navy with one warm image.

Anatomy in DOM order (hero grid is 1240px wide, x 100–1340, vertically centered):

1. **Top bar** `nav.topbar`: fixed, 56px tall, transparent over the hero (turns to 84% navy with 14px blur once scrolled). Links Abstract, Method, Results, Worlds, BibTeX right-aligned, Schibsted Grotesk 14px/500, #8d9ab8, 26px apart; hover #eef2fa. A Spectral SC mark fades in on scroll.
2. **Venue** `p.venue`: "NeurIPS 2026", 14px/500, letter-spacing .02em, #c5cfe3, left. Gap 22px.
3. **Wordmark** `h1.wordmark`: Spectral SC 160px/300, line-height .8, letter-spacing .012em, #eef2fa, left with a -.045em hanging indent. Gap 22px.
4. **Subtitle** `p.subtitle`: Spectral 32px/300, line-height 1.18, #eef2fa. Gap 21px.
5. **Lede** `p.lede`: Schibsted Grotesk 17px/400, line-height 1.62, #c5cfe3, max-width 33em (561px). Gap 33px.
6. **Authors** `ul.authors`: 16px/400 #eef2fa, each name with a 1px rgba(197,207,227,.30) bottom border, 18px apart; corresponding-author daggers in #f0b054. Gap 8px.
7. **Affiliation** `p.affiliation`: 14.5px #8d9ab8, plus "† Corresponding authors" note 14px to the right. Gap 28px.
8. **Buttons** `.links .btn`: Paper, arXiv, Code, BibTeX, 40px outlined pills, 8px apart.
9. **Hero figure** (right column, x 827): 448×448 canvas with 6px radius and a deep drop shadow; RGB/Depth/Normal labels as dark translucent pills; two circular drag grips; a column of 49px thumbnails 8px apart (selected one ringed in #f0b054); below, a 36px circular play button, a tick-mark scrubber with amber progress and "44 / 81" in Spectral numerals; a pill segmented switch (Split, RGB, Depth, Normal); and the condition image with an italic Spectral prompt.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Night Navy | #0b1430 | --bg (night) | hero, worlds gallery band, top bar when solid, html ground |
| Night Deep | #070d20 | --bg-deep (night) | deep panels inside night sections |
| Starlight | #eef2fa | --fg (night) | wordmark, subtitle, author names, button labels, selected mode pill fill |
| Mist | #c5cfe3 | --fg-soft (night) | lede, venue line, world prompt; at 30% alpha the pill and author borders |
| Dusk Grey | #8d9ab8 | --muted (night) | top-bar links, affiliation, unselected modes, condition label, readout |
| Lantern Amber | #f0b054 | --accent (night) | author daggers, selected thumbnail ring, scrubber progress, button and play hover, hero glow at 13% |
| Void | #02040a | (literal) | viewer stage and gallery tile ground behind media |
| Overlay Ink | rgba(6,10,24,.55) | (literal) | band-label pills and drag grips (at 50%) over the viewer |
| Caption Shade | rgba(3,6,16,.86) | (literal) | bottom of the gradient behind gallery tile captions |
| Day Paper | #f2f4f8 | --bg (day) | Abstract, Method, Results, Applications, BibTeX sections |
| Day Panel | #e7ebf2 | --bg-deep (day) | BibTeX block, explainer stage |
| Day Ink | #10172b | --fg (day) | section titles (h2, h3), table row headers |
| Day Text | #2e3852 | --fg-soft (day) | body paragraphs, BibTeX text |
| Day Muted | #5c6682 | --muted (day) | figure captions, table headers |
| Copper | #9a5b0e | --accent (day) | stage numbers, table check marks, focus and hover accents in day sections |
| Plate White | #ffffff | --plate (day) | figure plates |

Declared but not visible: `.venue` is declared in --accent (#f0b054) but renders #c5cfe3. Plot colors --p1/--p2/--p3 (#b9700f, #5c6682, #2f6fb8 on day) appear only inside the method explainer SVG.

## Tokens — Typography

- **Wordmark**: declared `"Spectral SC", "Spectral", Georgia, serif`; renders Spectral SC 300. Substitute: Cormorant SC Light.
- **Display serif**: declared `"Spectral", Georgia, "Times New Roman", serif`; renders Spectral 300, 300 italic, 400, 400 italic. Substitute: Source Serif 4 Light.
- **UI and body**: declared `"Schibsted Grotesk", system-ui, -apple-system, "Segoe UI", "PingFang SC", sans-serif`; renders Schibsted Grotesk 400, 500, 600. Substitute: Hanken Grotesk.
- **Code**: `ui-monospace, "SF Mono", Menlo, Consolas, monospace` (system mono).

| Role | Selector | Size at 1440 (clamp) | Weight | Line-height | Tracking |
|---|---|---|---|---|---|
| Wordmark | `.wordmark` | 160px (92px, 11.4vw, 160px) | 300 | .8 | .012em |
| Section title | `h2` | 46px (32px, 4.2vw, 46px) | 300 | 1.08 | -.012em |
| Subtitle | `.subtitle` | 32px (24px, 2.35vw, 32px) | 300 | 1.18 | 0 |
| Stage number | `.stage-num` | 32px Spectral | 300 | 1 | 0 |
| Subsection | `h3` | 26px (22px, 2.3vw, 26px) | 400 | 1.2 | 0 |
| Body | `body` | 17px (16px under 720px) | 400 | 1.62; 1.7 in sections | 0 |
| World prompt | `.world-caption .prompt` | 17px Spectral italic | 300 | 1.5 | 0 |
| Authors | `.authors` | 16px | 400 | 1.62 | 0 |
| Step heading | `h4` | 16px | 600 | 1.35 | 0 |
| Table | `.paradigms` | 15px; header 13px/500 | 400 | 1.62 | 0 |
| Buttons, captions | `.btn`, `.figure figcaption` | 14.5px | 500 / 400 | 1 / 1.55 | 0 |
| Nav, venue | `.topbar-links a`, `.venue` | 14px | 500 | 1 | 0 / .02em |
| BibTeX | `.bibtex pre` | 12.5px mono | 400 | 1.75 | 0 |

Paragraphs in day sections are justified with hyphenation above 720px so text edges match figure edges.

## Tokens — Spacing & Shapes

- **Radius**: 999px for buttons, mode switch, copy button and band labels; 50% for play button, grips and dialog close; 8px for figure plates, explainer stage and BibTeX; 6px for the viewer stage; 4px for thumbnails and gallery tiles; 3px for condition images.
- **Shadows**: viewer stage `0 40px 90px -40px rgba(0,0,0,.75)`; selected thumbnail ring `0 0 0 1.5px #0b1430, 0 0 0 3px #f0b054`; dialog `0 40px 120px rgba(0,0,0,.5)`.
- **Borders**: 1px rgba(197,207,227,.30) on night pills; 1px rgba(16,23,43,.10) on day hairlines (table rows, stage list, BibTeX); 1px rgba(16,23,43,.24) under table headers.

## Layout Metrics

- **Containers**: reading column `.col` = `min(100% - 2*pad, 960px)` centered (x 240–1200 at 1440); hero and top bar `min(100% - 2*pad, 1240px)`. Side pad `clamp(20px, 4vw, 40px)`.
- **Hero**: `min-height: min(100vh, 1040px)`, content vertically centered; padding-top 101px (56px bar + clamp(28px, 5vh, 64px)), padding-bottom 54px (clamp 40px, 6vh, 80px). Grid: text column `1fr`, figure column stage + thumb + 16px (513px), gap clamp(32px, 5vw, 80px) → 72px.
- **Viewer**: stage `clamp(300px, min(58vh, 40vw), 448px)` = 448px; thumbnails (stage − 56px) / 8 = 49px; figure gaps 12px × 16px.
- **Sections**: `padding-block: clamp(64px, 7.5vw, 104px)` = 104px; consecutive light sections drop their top padding to 8px so they read as one flow.
- **Headings**: h2 margin-bottom 22px; h3 margin-top 64px, bottom 12px.
- **Figures**: plate full column width (960px) with clamp(10px, 1.6vw, 22px) padding; caption 14px below; figure margin-top 40px.
- **Worlds gallery**: grid `repeat(auto-fill, minmax(176px, 1fr))`, 10px gap, square tiles.

| Breakpoint | Side pad | Body | Wordmark | Grid change |
|---|---|---|---|---|
| ≥1021px | 40px | 17px | 160px | hero split: text left, viewer right |
| ≤1020px | 40px | 17px | 11.4vw | hero stacks; viewer below text, no min-height |
| ≤720px | 20–29px | 16px | 92px floor at ≤807px | top-bar links hidden (mark shown); thumbnails become a horizontal row of 48px; mode switch full width; gallery 2 columns; text ragged-right |

## Components

- **Outline pill button** `.btn`: 40px tall, padding 0 15px 0 12px, radius 999px, 1px rgba(197,207,227,.30) border, transparent fill, #eef2fa Schibsted Grotesk 14.5px/500, 17px stroke icon (1.5px) on the left with 7px gap; hover border and text #f0b054. "Soon" variant: dashed border, #8d9ab8, appended "soon".
- **Mode switch** `.viewer-modes`: inline pill track, 3px padding, 1px border at 14% Mist, 2px gaps; buttons 12.5px/500 #8d9ab8, padding 7px 12px, radius 999px; selected fill #eef2fa with #0b1430 text.
- **Play button** `.play`: 36px circle, 1px rgba(197,207,227,.30) border, #eef2fa icon; hover #f0b054.
- **Tick scrubber** `.timeline`: 36px tall; minor ticks 1px every 1/80 at 26% Mist, major ticks every 1/5 at 60%; the played part repaints ticks in #f0b054; thumb is a 2px × 26px amber line. Readout in Spectral tabular numerals, 14.5px #8d9ab8.
- **Thumbnail picker**: 49px squares, radius 4px, 50% opacity, 85% on hover; selected at 100% with a 3px #f0b054 ring.
- **Band label**: 12px/500 white on rgba(6,10,24,.55) with 6px blur, padding 6px 9px, radius 999px.
- **Figure plate** `.plate`: #ffffff, radius 8px, padding 22px; caption 14.5px/1.55 #5c6682, justified, bold lead-in #2e3852.
- **Training stages** `.stages li`: grid 46px + 1fr, 20px vertical padding, 1px hairline top (and bottom on the last); numeral Spectral 32px/300 #9a5b0e; h4 16px/600 #10172b.
- **Paradigm table** `.paradigms`: 15px, cells 15px 12px centered; header 13px/500 #5c6682 over a 1px rgba(16,23,43,.24) line; row hairlines 1px rgba(16,23,43,.10); checks are 18px masked icons in #9a5b0e, crosses in #5c6682 at 65%; the AEON row tinted rgba(240,176,84,.16).
- **Gallery tile**: square, radius 4px, #02040a ground; image scales 1.03 on hover; caption slides up over a gradient to rgba(3,6,16,.86), 13px.
- **BibTeX**: #e7ebf2 block, 1px hairline, radius 8px, padding 20px 22px, 12.5px/1.75 mono #2e3852; Copy pill 13px/500 with 1px border, hover #9a5b0e.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top nav | yes | fixed transparent bar, becomes frosted navy on scroll |
| Title block | yes | small-caps serif wordmark, serif subtitle, grotesk lede, left-aligned in the hero |
| Authors / affiliations | yes | underlined names in one row, single affiliation line |
| Link buttons | yes | outlined pills with stroke icons |
| Teaser | yes, non-standard | interactive 4D viewer (canvas split view, thumbnails, scrubber, mode switch) instead of a video |
| Abstract | yes | justified 17.5px text in the 960px column |
| Method figure | yes | white rounded plate with caption, plus an interactive SVG explainer |
| Numbered stages | yes | hairline list with copper serif numerals |
| Results table | yes | paradigm comparison with check/cross icons and a tinted AEON row |
| Applications | yes | figures with captions under "What an explicit 4D world supports" |
| Gallery | yes | 62-tile navy gallery opening a dialog viewer |
| BibTeX | yes | tinted block with Copy pill |
| Footer | absent from the source | the page ends with BibTeX |

## Adapting to Other Content

- **More authors**: keep one wrapping row (gap 6px 18px) of underlined 16px names; move affiliations to numbered superscripts in #f0b054 and list them on the 14.5px #8d9ab8 line.
- **Results table**: reuse `.paradigms` with numbers in place of icons: right-align numeric cells, keep 13px/500 #5c6682 headers, tint the proposed row rgba(240,176,84,.16), bold the best value in #10172b.
- **Long publication list**: in the light column, use the `.stages` pattern: hairline-separated rows, year in Spectral 32px/300 copper on the left, title 16px/600 and venue 14.5px #5c6682.
- **News**: a hairline list in a light section, date in Spectral italic #5c6682, text 17px #2e3852.
- **No interactive viewer**: put a 448px square video in the same right column with the 6px radius and the deep drop shadow; keep the amber glow behind it.

## Do's and Don'ts

- Do keep the wordmark in a small-caps light serif at 160px; it is the identity.
- Do pair a light serif for titles with a grotesk for everything functional.
- Do use amber (#f0b054) only for state: selected, playing, hovered.
- Do alternate night and day sections with the same 104px rhythm.
- Do justify body text in the light column so it aligns with figure edges.
- Don't fill buttons; they are outlined pills that light up amber on hover.
- Don't widen the reading column beyond 960px; only the hero uses 1240px.
- Don't put figures straight on the gray ground; seat them on white 8px-radius plates.

## Surfaces

Navy #0b1430 hero with a 13% amber radial glow; frosted navy top bar on scroll; cool off-white #f2f4f8 reading sections; white #ffffff figure plates; #e7ebf2 BibTeX and explainer panels; a second navy band for the gallery.

## Imagery

Generated 4D worlds (cinematic landscapes, characters) shown as square renders with RGB, depth and normal splits; a method diagram on a white plate; an animated SVG timeline explainer; square gallery thumbnails that play on hover.

## Layout

Two-column hero (text left, viewer right) centered in 1240px, then a single 960px column for all reading content, with full-bleed scheme changes between sections. About 8,900px tall.

## Agent Prompt Guide

Quick colors: night #0b1430, text #eef2fa, soft #c5cfe3, muted #8d9ab8, accent #f0b054; day #f2f4f8, ink #10172b, text #2e3852, muted #5c6682, day accent #9a5b0e, plate #ffffff.

1. "Build a hero on #0b1430: venue line Schibsted Grotesk 14px/500 #c5cfe3, 22px gap, wordmark in Spectral SC 160px weight 300, line-height .8, letter-spacing .012em, #eef2fa; 22px gap; subtitle Spectral 32px/300 #eef2fa; lede 17px/1.62 #c5cfe3 max 33em; author names 16px #eef2fa with a 1px rgba(197,207,227,.30) bottom border."
2. "Build outline pill buttons: height 40px, padding 0 15px 0 12px, radius 999px, 1px solid rgba(197,207,227,.30), transparent, #eef2fa Schibsted Grotesk 14.5px/500, 17px stroke icon left with 7px gap; hover border and text #f0b054."
3. "Build a light reading section: background #f2f4f8, padding 104px 0, centered 960px column; h2 Spectral 46px/300, line-height 1.08, #10172b, 22px below; paragraphs 17px/1.7 #2e3852, justified; figures on #ffffff plates with 8px radius and 22px padding, caption 14.5px #5c6682."

## Similar Pages

- Dark-hero research pages with an interactive viewer beside the title (3D/4D generation projects).
- Editorial pages pairing a light serif display with a neutral grotesk on alternating dark and light bands.

## Quick Start

```css
:root {
  --night-bg: #0b1430;
  --night-deep: #070d20;
  --night-fg: #eef2fa;
  --night-soft: #c5cfe3;
  --night-muted: #8d9ab8;
  --night-accent: #f0b054;
  --day-bg: #f2f4f8;
  --day-deep: #e7ebf2;
  --day-fg: #10172b;
  --day-soft: #2e3852;
  --day-muted: #5c6682;
  --day-accent: #9a5b0e;
  --plate: #ffffff;
  --font-mark: "Spectral SC", "Spectral", Georgia, serif;
  --font-display: "Spectral", Georgia, "Times New Roman", serif;
  --font-ui: "Schibsted Grotesk", system-ui, -apple-system, "Segoe UI", sans-serif;
  --body-size: 17px;
  --body-lh: 1.62;
  --col: 960px;
  --col-full: 1240px;
  --pad: clamp(20px, 4vw, 40px);
  --sec-space: clamp(64px, 7.5vw, 104px);
  --topbar-h: 56px;
}
```

## Provenance

- **URL**: https://weiqi-zhang.github.io/AEON/
- **Paper**: AEON: Unifying Video and 3D World Models (arXiv 2610.28631), Weiqi Zhang, Wenyuan Zhang, Yu-Shen Liu, Junsheng Zhou.
- **Venue**: NeurIPS 2026.
- **Selection reason**: existing verified entry; the arXiv comment reads "Accepted to NeurIPS 2026. Project Page: https://weiqi-zhang.github.io/AEON".
- **Template credit**: custom page; no template credit shown.
- **Evidence used**: computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440 screenshot and tall capture, and static/css/aeon.css read directly. Captured 2026-10-28.
