# Omegance — Style Reference

> A Swiss poster set in a research lab: one giant black wordmark, a single electric-blue dot, and every column hung from a 3px black rule.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's own `static/css/index.css?v=12` and `index.html`. The nav highlights the section in view (a script adds `.is-active`), so the full-page shot shows "OVERVIEW" filled blue while the first-viewport shot shows no active item. The slider demos swap images by script; at load every frame shows the "ORIGINAL" label.

## Overview

A custom, editorial page (about 5,040px tall) in the Swiss tradition: white ground, near-black ink #0b0b0b, one accent, electric blue #1f4bff. Space Grotesk carries everything from the 184px wordmark to body text; IBM Plex Mono, uppercase and slightly tracked, labels the nav, metadata columns, section numbers and image tags. Under a sticky 54px bar with a 3px black bottom rule, the hero is a left-aligned wordmark "Omegance." whose period is blue, then a 12-column metadata grid (paper title / authors / resource links) below another 3px rule. A full-bleed blue TL;DR band follows, then four numbered sections (01 Continuous Output, 02 Before & After, 03 Video Generation, 04 Citation), each opened by a 3px black rule and an asymmetric head: in 01 and 03 a blue mono number in 3 columns, 44.8px headline in 5 and a short note in 4; 02 and 04 have no note, so the headline spans 9 columns (864px) beside the 3-column number. Content columns step 296px in from the left, and alternate sections ("is-flip") mirror the layout to the right. A black footer holds the contact block. There are no radii, no shadows and no gradients anywhere.

## First Viewport

Color share (quantized 1440×900 shot): white #ffffff 50.5% (plus #fdffff 2.8% and #fffffd 0.7%); blue #1f4bff 32.2% (plus #1e4bff 3.3%), which is the TL;DR band from y=554 to the fold; #9aa7dc 5.6% and #4b4b4d 4.9% are anti-aliased white-on-blue text and black type edges.

Anatomy in DOM order (desktop 1440px, `.wrap` content box x=140 to 1300):

1. **Sticky top bar** (`header.top`, 0–57px): white, 54px tall plus 3px #0b0b0b bottom border. Left "Omegance" in Space Grotesk 16px/700 (`b`); right six mono links (OVERVIEW … CONTACT) 12.48px/400 uppercase, letter-spacing 0.04em, each padding 0 16px, full 54px height, separated by 1px #dddddd left borders. Hover #f2f2f2; active white on #1f4bff.
2. **Hero padding**: `.hero` padding-top 64px, so the wordmark box starts at y=121.
3. **Wordmark** (`.hero h1`, y=121–277): "Omegance." 184px/700, line-height 0.85 (156.4px), letter-spacing -0.055em (-10.12px), #0b0b0b, left-aligned; the period is a `span` in #1f4bff. Gap 40px (`.hero-grid` margin-top).
4. **Hero rule** (y=317): 3px solid #0b0b0b top border of `.hero-grid`, padding 24px 0 48px; the grid has 12 columns with 24px gaps, split 5 / 4 / 3.
5. **Column 1, paper** (y=344): mono label "PAPER" 12.48px #0b0b0b followed by the venue tag "ICCV 2025" (mono 12.48px/500, white on #1f4bff, padding 2.4px 8px, 6.4px left margin, square). Below at y=376 the subtitle `.subtitle` 25.6px/500, line-height 1.2, #0b0b0b, three lines.
6. **Column 2, authors** (x=633, y≈352): mono label "AUTHORS", then names at 16.8px/400 line-height 1.6 with a 2px #1f4bff bottom border each (hover: white on blue); affiliation line "S-Lab, Nanyang Technological University" in #6b6b6b, 6.4px above-margin.
7. **Column 3, resources** (x=1028): mono label "RESOURCES", then `.linklist` rows arXiv / Paper / Code, each 17.6px/500, padding 8.8px 0, 1px #0b0b0b bottom rule, icon on the left (Academicons arXiv, Font Awesome file-pdf, github) and a Font Awesome arrow-right on the far right. Rows sit at y=371, 416, 461; the grid ends at y=506 and its 48px bottom padding brings the hero to y=554.
8. **TL;DR band** (`section.band`, y=554–993): full-bleed #1f4bff, white text, padding 64px 0. Left 3 columns: mono "TL;DR" at 85% opacity. Right 9 columns (x=436): the sentence `p.big` at y=618, 33.6px/500, line-height 1.2, letter-spacing -0.015em, "Omegance" bold. Then a `details` toggle "▸ READ THE FULL ABSTRACT" (mono 12.8px uppercase, 28.8px top margin), then four tick items in a 4-column grid under a 1px rgba(255,255,255,0.5) rule (16px/500 with Font Awesome check icons). The ticks cross the fold at y≈740.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Ink | #0b0b0b | --ink | body text, wordmark, h2, 3px section and hero rules, link-list rules, image outlines, slider track, image label fill, copy button, footer background |
| Electric Blue | #1f4bff | --blue | wordmark period, venue tag, author underlines and hover fill, active nav item, TL;DR band, section numbers, slider thumbs, compare handle, accent image labels, BibTeX left bar, footer "Star" button, link-list hover text |
| Paper | #ffffff | (literal) | page and top-bar background, text on blue and black |
| Muted | #6b6b6b | --muted | affiliation line, compare hint text |
| Note Gray | #333333 | (literal, `.sec-head p`) | short section notes beside h2; 1px rule above the footer credit line |
| Nav Divider | #dddddd | (literal) | 1px left borders between nav links |
| Hover Gray | #f2f2f2 | (literal) | nav link hover fill |
| Code Well | #f4f4f4 | (literal, `pre`) | BibTeX block background |
| Periwinkle | #8aa2ff | (literal) | "05 CONTACT" mono number in the black footer |
| Footer Text | #cfcfcf | (literal) | contact paragraph in the footer |
| Credit Gray | #8a8a8a | (literal, `.credit`) | footer credit line, above a 1px #333333 rule |
| Band Rule | rgba(255,255,255,0.5) | (literal) | 1px line above the TL;DR ticks |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display / text | 'Space Grotesk', system-ui, sans-serif | Space Grotesk 400, 500, 700 (Google Fonts) | Archivo |
| Labels / code | 'IBM Plex Mono', monospace | IBM Plex Mono 400, 500 | JetBrains Mono |
| Icons | Font Awesome 6.5.2, Academicons 1 | Font Awesome 6 Free 400/900, Brands 400, Academicons 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Wordmark | `.hero h1` | clamp(4rem, 13vw, 11.5rem) → 184px / 700 / 0.85, letter-spacing -0.055em | #0b0b0b, period #1f4bff |
| Section headline | `.sec-head h2` | 2.8rem = 44.8px / 700 / 1, letter-spacing -0.03em | #0b0b0b |
| TL;DR sentence | `.band p.big` | 2.1rem = 33.6px / 500 / 1.2, letter-spacing -0.015em | #ffffff |
| Paper subtitle | `.subtitle` | 1.6rem = 25.6px / 500 / 1.2 | #0b0b0b |
| Resource link | `.linklist a` | 1.1rem = 17.6px / 500 / 1.5 | #0b0b0b, hover #1f4bff |
| Authors | `.people` | 1.05rem = 16.8px / 400 / 1.6 | #0b0b0b |
| Section note | `.sec-head p` | 1.02rem = 16.3px / 400 / 1.5 | #333333 |
| Body | `body` | 16px / 400 / 1.5 | #0b0b0b |
| Mono label | `.mono` | 0.78rem = 12.48px / 400, uppercase, letter-spacing 0.04em | #0b0b0b; section numbers #1f4bff |
| Image tag | `.demo-label` | IBM Plex Mono 0.72rem = 11.5px uppercase | #ffffff on #0b0b0b or #1f4bff |
| BibTeX | `pre` | IBM Plex Mono 0.85rem = 13.6px / 1.65 | #0b0b0b |
| Copy button | `.copy-btn` | IBM Plex Mono 0.75rem = 12px uppercase | #ffffff |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| All elements | 0 (no rounded corners anywhere) | — | none |
| Top bar | 0 | 3px solid #0b0b0b bottom | none |
| Hero grid, every `.sec` | 0 | 3px solid #0b0b0b top | none |
| Resource rows | 0 | 1px solid #0b0b0b bottom | none |
| Image frames, compare panes, thumbs | 0 | outline 1px solid #0b0b0b; active thumb outline 3px #1f4bff | none |
| BibTeX `pre` | 0 | 6px solid #1f4bff left | none |
| Slider | 0 | track 3px #0b0b0b, thumb 18×18px #1f4bff square | none |
| Compare handle | 0 | 3px #1f4bff vertical bar with a 22×22px square knob | none |

Inactive demo thumbnails use `filter: grayscale(1)` and opacity 0.6.

## Layout Metrics

- **Container**: `.wrap { max-width: 1240px; margin: 0 auto; padding: 0 2.5rem }` → content box x=140 to 1300 (1160px) at 1440.
- **12-column grids**: hero, band, section heads and footer all use `repeat(12, 1fr)` with a 1.5rem (24px) gap; one column ≈ 74.7px.
- **Content indent**: everything in a `.sec` other than its head gets `margin-left: calc((100% + 1.5rem) / 4)` = 296px, so images and video start at x=436 (the 4th column). `.is-flip` sections (02 and 04) swap this to `margin-right` and move the head's mono number to columns 10–12, right-aligned. A head without a note makes `h2:last-child` span 9 columns (`grid-column: span 9`, or `1 / span 9` when flipped), giving a 3 / 9 split in 02 and 04 (mirrored to 9 / 3) against the 3 / 5 / 4 split of 01 and 03.
- **Hero**: padding-top 64px; wordmark 156px tall; 40px gap; grid padding 24px top, 48px bottom; total 497px (y=57 to 554).
- **TL;DR band**: padding 64px 0; 439px tall at load (abstract collapsed).
- **Sections**: padding 72px 0, 3px top rule; `.sec-head` margin-bottom 40px; `.grid2` two equal columns with 24px gap (each 420px wide inside the 864px indented column); case blocks 48px apart.
- **Footer**: #0b0b0b, padding 72px 0 32px; credit line 64px below the contact row.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1415px | 40px inside 1240px | 16px | 184px (cap) | 12-column layouts, 296px content indent |
| 900–1415px | 40px | 16px | 13vw (e.g. 117px at 900) | same |
| ≤900px | 19.2px (`.wrap` padding 1.2rem) | 16px | 13vw down to 64px floor | nav links hidden; all grid children full width; indent removed; `.grid2` and ticks 1 column; compare footer stacks |

## Components

- **Mono label** (`.mono`): IBM Plex Mono 12.48px, uppercase, letter-spacing 0.04em; section numbers ("01 CONTINUOUS OUTPUT") in #1f4bff with 9.6px top padding to align with the headline cap height.
- **Venue tag** (`.venue`): inline-block, #1f4bff fill, white mono 12.48px/500, padding 2.4px 8px, square corners.
- **Author link**: no text-decoration; 2px #1f4bff bottom border; hover fills #1f4bff with white text.
- **Resource row** (`.linklist a`): flex, space-between; 17.6px/500 #0b0b0b; padding 8.8px 0; 1px #0b0b0b bottom border; leading icon 19.2px wide, trailing Font Awesome arrow-right; hover text #1f4bff.
- **Nav link** (`.top nav a`): full-height flex cell, padding 0 16px, 1px #dddddd left border; hover #f2f2f2; active (scroll-spy) #1f4bff fill, white text.
- **Image frame** (`.frame`): 1px #0b0b0b outline, no radius; top-left tag `.demo-label` (padding 4px 8.8px, #0b0b0b fill, white mono 11.5px uppercase); `.is-right` moves it top-right, `.is-accent` fills it #1f4bff.
- **Omega slider** (`.omega-range`): native range restyled; 3px #0b0b0b track, 17.6px top margin; 18px square #1f4bff thumb. A mono legend row ("ω > 0 SMOOTHER / MIDDLE = ORIGINAL / ω < 0 RICHER") sits under a 1px #0b0b0b rule, 25.6px below the grid.
- **Before/after compare** (`.compare`): base and top image with the top clipped by `clip-path: inset(0 calc(100% - var(--pos)) 0 0)`; 3px #1f4bff handle with a 22px square knob; an invisible full-size range input drives `--pos`; ew-resize cursor. Scene thumbnails 56px wide, gray and 60% opaque until active.
- **BibTeX**: `pre` #f4f4f4, 6px #1f4bff left border, padding 25.6px, mono 13.6px/1.65; COPY button absolutely top-right, #0b0b0b with white mono 12px uppercase, padding 7.2px 14.4px, hover #1f4bff.
- **Star button** (footer `.star`): #1f4bff, white 700 text, padding 12.8px 19.2px, gap 9.6px with a GitHub icon and star count; hover white fill with #0b0b0b text.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky nav with scroll-spy | yes | 54px white bar, 3px black rule, mono links with gray dividers, blue active cell |
| Wordmark title | yes | 184px Space Grotesk with a blue period |
| Metadata columns (paper / authors / resources) | yes | 12-column grid under a 3px rule, mono labels |
| TL;DR | yes | full-bleed blue band with a 33.6px sentence and four check ticks |
| Abstract | present but non-standard | collapsed inside a `details` toggle in the blue band |
| Interactive slider demo | yes | 2×2 framed images with square blue thumbs |
| Before/after comparison | yes | clip-path compare panes with a blue handle and thumbnail picker |
| Video results | present but non-standard | animated GIFs in framed 2-column grids with mono model names and quoted prompts; no `<video>` element |
| Results tables | absent from the source | — |
| BibTeX | yes | gray well with a blue left bar and black COPY button |
| Footer / contact | yes | black band with periwinkle mono number, email links, blue Star button |

## Adapting to Other Content

- **More authors**: keep them in the 4-column middle cell; at 16.8px about 5 names fit per two lines. Past eight authors, move affiliations into a second mono-labelled cell and let the paper column shrink to 4 spans.
- **A results table**: put it in the indented content column (864px at x=436), header row in IBM Plex Mono 12.48px uppercase under a 3px #0b0b0b rule, body 16px with 1px #0b0b0b row rules, best value set in #1f4bff 700. No fills, no radius.
- **Long publication or news lists**: reuse the `.linklist` row (17.6px/500, 1px #0b0b0b rule, trailing arrow) with a mono 12.48px date on the left.
- **More sections**: number them sequentially in blue mono and alternate `.sec` and `.sec.is-flip` so the indent swaps sides.
- **A second accent** is not needed; for states use #0b0b0b fills (labels, copy button) rather than a new hue.

## Do's and Don'ts

- Do set the project name as a giant tight wordmark (184px, -0.055em) and color only its final period #1f4bff.
- Do open every block with a 3px #0b0b0b rule and a mono label; structure comes from rules, not boxes.
- Do keep all corners square, including slider thumbs and the compare knob.
- Do use one full-bleed #1f4bff band for the key message only.
- Don't add shadows, gradients or rounded cards.
- Don't center headings; everything hangs from the left edge of a 12-column grid.
- Don't use the mono face for long text; it is for labels, tags and code.

## Surfaces

Three flat surfaces: white page, one full-bleed #1f4bff band, and the #0b0b0b footer. The BibTeX well (#f4f4f4) is the only tinted panel. Images sit inside 1px black outlines with black or blue corner tags.

## Imagery

Square fantasy and sci-fi text-to-image samples (phoenix, underwater city, mushroom house, fjord village, astronaut) in 2-column grids, each with an ω slider or a before/after split; GIF video samples in the video section. No method diagram on the page.

## Layout

Left-anchored, asymmetric 12-column grid in a 1240px container. Sections stack on 3px rules with 72px padding; heads use a 3 / 5 / 4 column split when they carry a note (01, 03) and 3 / 9 when they do not (02, 04), and content indents one quarter of the width, mirrored on alternate sections, which gives the page a zig-zag editorial rhythm.

## Agent Prompt Guide

Quick colors: page #ffffff, ink #0b0b0b, accent #1f4bff, muted #6b6b6b, note #333333, code well #f4f4f4, footer number #8aa2ff.

1. "Build a Swiss-style hero: sticky 54px white bar with a 3px #0b0b0b bottom border, mono uppercase links (IBM Plex Mono 12.48px, letter-spacing 0.04em, padding 0 16px, 1px #dddddd dividers). Below, padding-top 64px, a left-aligned wordmark in Space Grotesk 184px/700, line-height 0.85, letter-spacing -0.055em, #0b0b0b, with a #1f4bff period. Then a 12-column grid (gap 24px) under a 3px #0b0b0b rule, padding 24px 0 48px: paper subtitle 25.6px/500 in 5 columns, authors with 2px #1f4bff underlines in 4, resource rows in 3."
2. "Make a TL;DR band: full-bleed #1f4bff, white text, padding 64px 0; mono 'TL;DR' label in the first 3 columns at 85% opacity; a 33.6px/500 sentence (line-height 1.2, letter-spacing -0.015em) in the other 9; four check-icon ticks in a 4-column grid under a 1px rgba(255,255,255,0.5) rule."
3. "Create a numbered section: 3px #0b0b0b top border, padding 72px 0; head row with a #1f4bff mono number in 3 columns, a 44.8px/700 headline (letter-spacing -0.03em) in 5, a 16.3px #333333 note in 4 (with no note, the headline spans 9); content indented by calc((100% + 24px) / 4). Images in 1px #0b0b0b outlines, square corners, with white mono tags on #0b0b0b in the top-left corner."

## Similar Pages

- Editorial, grid-first project pages that use a single saturated accent and oversized display type, in the manner of Swiss poster design.
- Pages that replace the Nerfies-style centred header with ruled metadata columns.

## Quick Start

```css
:root {
  --ink: #0b0b0b;
  --blue: #1f4bff;
  --muted: #6b6b6b;
  --paper: #ffffff;
  --code-well: #f4f4f4;
  --font-sans: 'Space Grotesk', system-ui, sans-serif;
  --mono: 'IBM Plex Mono', monospace;
  --wrap: 1240px;
  --gutter: 2.5rem;
  --gap: 1.5rem;
  --rule: 3px solid var(--ink);
  --title: clamp(4rem, 13vw, 11.5rem);
  --h2: 2.8rem;
}
```

## Provenance

- **URL**: https://itsmag11.github.io/Omegance/
- **Paper**: Omegance: A Single Parameter for Various Granularities in Diffusion-Based Synthesis (arXiv 2411.17769), Xinyu Hou, Zongsheng Yue, Xiaoming Li, Chen Change Loy (S-Lab, NTU).
- **Venue**: ICCV 2025.
- **Selection reason**: the arXiv comment states acceptance at ICCV 2025 and links this project page.
- **Template credit**: none visible; a custom build (`static/css/index.css?v=12`, `static/js/index.js`) with Google Fonts, Font Awesome 6.5.2 and Academicons.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, and the page's `index.css` and `index.html` read directly, on 2026-10-28.
