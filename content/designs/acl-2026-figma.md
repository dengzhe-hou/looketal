# Warm Paper Editorial — Style Reference

> A music journal on warm paper: a heavy Newsreader headline under a red kicker, big red serif numerals for the results, and figures resting in soft cream frames.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (`tools/computed_style.py`: computed styles of the sticky header, brand, nav links, kicker, `h1`, venue badge, authors, hero description, buttons, key-results items, section overlines and headings, tables, inline code and footer, first-viewport anatomy, loaded fonts and color share), the first-viewport screenshot, the full-page capture, a 1440×6100 headless capture of the dataset and results sections, and the page's hand-written `styles.css`, which defines every token as a CSS custom property on `:root`. Positions are document coordinates at 1440px wide.

## Overview

FIGMA is a hand-built editorial page, not a template. The background is warm paper (#edeae3) everywhere. A 60px sticky header, translucent paper with a 12px backdrop blur and a hairline bottom border, holds an uppercase "FIGMA" brand with a "University of Maryland" suffix after a thin divider, five 14px section links and a bold "Paper PDF" link underlined in red. The hero is left-aligned in a 1120px column: a small red uppercase kicker with a 24px red dash, a 60px Newsreader bold headline in near-black ink (#181814) capped at 20 characters wide, a red-tinted "ACL 2026" badge, a plain author line and a grey affiliation line. A hairline then opens a two-column hero body (5fr / 4fr): a 15.5px summary with one black pill button and three outlined pills on the left; "KEY RESULTS" with three big red Newsreader numerals (73.3%, 21.4%, ~22M) and short descriptions on the right. Each later section repeats one rhythm: a red overline with a dash, then an asymmetric intro grid (2fr serif heading, 3fr prose), then figures in cream (#f5f2ed) cards with a 10px radius and hairline border, some pulled 32px wider than the column. Results use cream-carded tables with uppercase grey headers on #e6e2da, best scores in bold red, second best underlined, and green check marks. A three-cell stat strip in red serif numerals and a hairline footer complete the page.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): paper #edeae3 75.4%, darker paper #e5e1da 7.3% (badge tint, button and rule antialiasing), paper #edeae4 5.9%, warm grey #928e87 4.4% (text pixels), light paper #f0ede6 3.1%, remainder under 2.5%. Ink and red occupy little area but carry all the contrast.

Anatomy in DOM order (y = top of element box):

1. **Sticky header** (`header.site-header`), y 0, height 60, full width, `rgba(237,234,227,.94)` with `backdrop-filter: blur(12px)`, 1px rgba(24,24,20,.12) bottom border, padding 0 40px.
2. **Brand** (`a.brand`), x 40, y 18, "FIGMA" General Sans 14.1px/600 uppercase, letter-spacing 0.07em, #181814; `::after` adds "University of Maryland" in 13.1px #8a8880 after a 1px divider and 12px padding.
3. **Nav links** (`nav.nav-links a`), y 18, five links at 14.1px/400 #4a4840, 32px apart, hover #c04030; then `a.nav-cta` "Paper PDF" 14.1px/600 #181814 with a 2px #c04030 bottom border. Gap to kicker 80px (hero top padding).
4. **Kicker** (`p.hero-kicker`), x 160, y 140, "FINE-GRAINED MUSIC RETRIEVAL", 11.2px/500 uppercase, letter-spacing 0.18em, #c04030, led by a 24×1.5px #c04030 dash and a 12px gap. Gap 20px.
5. **Headline** (`h1`), y 178, 784px (max 20ch), two lines, Newsreader 60px/64.8px weight 700, letter-spacing -1.2px, #181814, left-aligned. Gap 32px.
6. **Venue badge** (`span.venue-badge`), y 340, 98×36, "ACL 2026", 14.7px/600 #c04030 on rgba(192,64,48,.08), 1px rgba(192,64,48,.2) border, 4px radius, padding 4.8px 13.6px. Gap 16px.
7. **Authors** (`p.authors`), y 392, 15.2px/24.3px #181814, superscript asterisks. Gap 6px.
8. **Affiliation** (`p.affil`), y 427, 13.6px #8a8880, items separated by " · ", underlined email link in #8a8880. Gap 32px to a 1px rgba(24,24,20,.12) rule, then 32px padding.
9. **Hero body grid** (`.hero-body`, 5fr 4fr, column gap 80px), y about 485: left `p.hero-desc` y 517, 578px wide, 15.5px/26.4px #4a4840; buttons y 646, 42px tall: "Paper" filled #181814 with #edeae3 text, then "Code", "Model", "Benchmark" outlined. Right column x 818: `h4` "KEY RESULTS" 11.2px/600 uppercase #8a8880 y 517, then three rows from y 551, each a Newsreader 22.4px/700 #c04030 numeral and a 14.1px #4a4840 description, 8px apart horizontally and 12px between rows.
10. **Section rule**, y 760, 1px full-width hairline; the next section's overline sits at y 833 ("THE PROBLEM") and its heading at y 867, just inside the fold.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #edeae3 | `--bg` | Page background; header base (94% alpha); primary-button text |
| Card Paper | #e6e2da | `--bg-card` | Table header row, inline `code` fill |
| Cream | #f5f2ed | `--bg-white` | Figure cards, table wrappers, stat cells, mobile nav panel |
| Ink | #181814 | `--ink` | Headline, section headings, brand, authors, primary button fill, bold prose |
| Ink 2 | #4a4840 | `--ink-2` | Body prose, hero summary, nav links, table cells, key-result descriptions |
| Ink 3 | #8a8880 | `--ink-3` | Affiliation, brand suffix, "KEY RESULTS" label, captions, table headers, footer |
| Accent Red | #c04030 | `--accent` | Kickers and overlines with dashes, venue badge text, key numerals, stat values, links, best scores, nav-cta underline, button hover |
| Accent Soft | rgba(192,64,48,.08) | `--accent-soft` | Venue badge fill, table row hover |
| Hairline | rgba(24,24,20,.12) | `--border` | Header border, section rules, ghost-button border, figure and table borders |
| Faint Line | rgba(24,24,20,.07) | `--border-2` | Table row rules, inline code border |
| Check Green | #1d7c4a | `.check` | Check marks in the dataset table |

## Tokens — Typography

- **Display**: declared `"Newsreader", Georgia, serif` (`--font-serif`), loaded from Google Fonts with optical size 6..72 at 400/600/700. Rendered: Newsreader 600 and 700 (`fonts_loaded`). Substitute: Source Serif 4 (also an optical-size text serif).
- **Text**: declared `"General Sans", system-ui, sans-serif` (`--font-sans`) from Fontshare at 400/500/600. Rendered: General Sans 400, 500, 600. Substitute: Satoshi, or Inter with slightly tighter tracking.
- **Code**: `"JetBrains Mono", monospace` declared for inline code (not loaded as a web font, falls back to the system mono). **Math**: KaTeX.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Headline | `h1` | 60px (clamp 2.4rem, 5vw, 3.75rem) / 1.08, letter-spacing -0.02em | 700 | #181814 |
| Section heading | `h2` | 38.4px (clamp 1.75rem, 3vw, 2.4rem) / 1.15, -0.02em | 700 | #181814 |
| Sub-heading | `h3` | 19.2px / 31.7px, -0.01em | 600 | #181814 |
| Stat value | `.stat-value` | 36px / 1.1 | 700 serif | #c04030 |
| Key numeral | `.key-result-item .num` | 22.4px / 1 | 700 serif | #c04030 |
| Prose | `.prose`, `.hero-desc` | 15.5px / 1.75 (hero 1.7) | 400 | #4a4840 |
| Authors | `.authors` | 15.2px / 1.6 | 400 | #181814 |
| Venue badge | `.venue-badge` | 14.7px, letter-spacing 0.02em | 600 | #c04030 |
| Nav, brand | `.nav-links a`, `.brand` | 14.1px | 400 / 600 uppercase 0.07em | #4a4840 / #181814 |
| Affiliation | `.affil` | 13.6px | 400 | #8a8880 |
| Button | `.btn` | 13.4px | 600 | per variant |
| Table cell, caption | `td`, `figcaption` | 13.1px | 400 | #4a4840 / #8a8880 |
| Table header | `thead th` | 11.5px uppercase, 0.07em | 600 | #8a8880 |
| Kicker, overline | `.hero-kicker`, `.overline` | 11.2px uppercase, 0.18em | 500 | #c04030 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Button | 999px | 1.5px solid (#181814 filled; rgba(24,24,20,.12) ghost) | none |
| Venue badge | 4px | 1px solid rgba(192,64,48,.2) | none |
| Figure card | 10px (`--radius`) | 1px solid rgba(24,24,20,.12) | none |
| Figure image | 6px (`--radius-sm`) | none | none |
| Table wrapper | 10px | 1px solid rgba(24,24,20,.12) | none |
| Stat strip | 10px | 1px hairline, cells separated by 1px gaps | none |
| Inline code | 4px | 1px solid rgba(24,24,20,.07) | none |
| Header | 0 | 1px bottom hairline | none (blur 12px behind) |

`--shadow` (0 2px 16px rgba(24,24,20,.07)) is declared but not applied to any element.

## Layout Metrics

- **Container**: `--max` 1200px for `.hero` and `main`, padding 0 40px, so content spans x 160–1280 (1120px).
- **Header**: sticky, 60px (`--nav-h`), padding 0 40px, full width.
- **Hero**: padding 80px 40px 72px; kicker margin-bottom 20px; `h1` margin-bottom 32px; meta block margin-bottom 32px; `.hero-body` margin-top 32px, padding-top 32px with a top hairline, grid 5fr 4fr with an 80px column gap (578px and 462px).
- **Sections**: `section` padding-top 72px, separated by full-width `hr.section-rule` hairlines; overline margin-bottom 16px; `.section-intro` grid 2fr 3fr with an 80px gap (416px heading, 624px prose), margin-bottom 32px.
- **Figures**: `.figure` margin 32px 0; `.figure.wide` pulls out 32px each side at ≥900px (1184px wide), image padding 20px, images capped at 380–420px tall with `object-fit: contain`; captions padding 13.6px 16px 16px.
- **Tables**: full column width in a cream wrapper, cells padding 9.6px 12px, tabular numerals.
- **Results side-by-side**: `.results-side` grid 3fr 2fr, gap 32px 48px.
- **Footer**: 1px top hairline, padding 32px 40px 48px, flex space-between.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥900px | 40px | 15.5px prose | 60px | wide figures bleed 32px |
| 861–899px | 40px | 15.5px | 43–45px (5vw) | wide figures bleed 16px |
| 768–860px | header 20px; content 40px | 15.5px | 38.4–43px | nav collapses to a toggle with a cream drop-down panel; brand suffix hidden |
| 721–767px | 40px | 15.5px | 38.4px (floor) | results-side stacks |
| ≤720px | 20px (`main`, hero padding 48px 20px) | 15.5px | 38.4px floor (2.4rem) | hero body and section intros become one column |

## Components

- **Sticky paper header**: 60px, rgba(237,234,227,.94) with blur(12px), hairline bottom; uppercase brand with a hairline-separated suffix; 14px links 32px apart, hover #c04030; a bold "Paper PDF" link with a 2px #c04030 underline.
- **Kicker and overline**: 11.2px uppercase 500 #c04030 with 0.18em tracking, preceded by a 22–24px × 1.5px #c04030 dash and a 12px gap.
- **Venue badge**: inline-block, 14.7px/600 #c04030 on rgba(192,64,48,.08), 1px rgba(192,64,48,.2) border, 4px radius, padding 4.8px 13.6px.
- **Pill button**: inline-flex, padding 8.8px 17.6px, 999px radius, 13.4px/600, 1.5px border. Primary: #181814 fill and border, #edeae3 text; hover #c04030 fill with white text. Ghost: transparent with a rgba(24,24,20,.12) border and #181814 text; hover border and text #c04030. 10.4px gaps.
- **Key results list**: an uppercase 11.2px #8a8880 label, then rows of a serif 22.4px #c04030 numeral and a 14.1px #4a4840 description on one baseline.
- **Asymmetric section intro**: 2fr serif heading left, 3fr prose right, 80px gap.
- **Figure card**: #f5f2ed fill, 1px hairline border, 10px radius, 16–20px image padding, 6px image radius, 13.1px #8a8880 caption with a bold #4a4840 lead.
- **Results table**: cream wrapper with hairline border and 10px radius; header row #e6e2da with 11.5px uppercase #8a8880 labels and group headers ("TEXT-TO-AUDIO", "AUDIO-TO-TEXT"); 13.1px cells with faint row rules; numbers right-aligned; best scores bold #c04030, second best underlined; method row in bold; row hover rgba(192,64,48,.08).
- **Stat strip**: three cream cells separated by 1px hairlines inside a 10px-radius border; 36px serif #c04030 values over 11.2px uppercase #8a8880 labels.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navigation | yes | sticky translucent paper header with section links |
| Kicker, title | yes | red dash kicker, 60px serif headline |
| Venue | yes | red-tinted badge |
| Authors, affiliation | yes | one plain line each, left-aligned |
| Summary and links | yes | left hero column with pill buttons |
| Key results | yes | right hero column with red serif numerals |
| Teaser figure | present but non-standard | the first figure appears in the Problem section, not the hero |
| Problem, approach, dataset sections | yes | overline plus asymmetric intro |
| Method equations | yes | KaTeX display blocks |
| Stat strip | yes | three-cell cream strip |
| Results tables | yes | cream-carded tables with red best scores |
| Results plus figure | yes | 3fr / 2fr side-by-side |
| BibTeX | absent from the source | |
| Footer | yes | hairline, brand and links |

## Adapting to Other Content

- **More authors**: keep a single left-aligned 15.2px line that wraps; move institutions into the grey affiliation line with superscripts.
- **More key results**: add rows to the right hero column; keep numerals short (≤6 characters) so the baseline row stays tidy, and move longer claims into the stat strip.
- **A BibTeX block**: a cream card (#f5f2ed, hairline border, 10px radius) under a "CITATION" overline, monospace 13px #4a4840, padding 16px.
- **News**: an overline "UPDATES" and a two-column list (date in 11.2px uppercase #8a8880, text in 15.5px #4a4840) separated by faint rules.
- **Long publication lists**: the same date-plus-text rows, titles in Newsreader 19.2px/600 #181814.
- **Video**: inside a figure card with the image padding and 6px radius, captioned like figures.

## Do's and Don'ts

- Do keep the page on #edeae3 paper and use cream #f5f2ed only for cards.
- Do reserve #c04030 for kickers, numerals, best scores, links and hover; never for body text.
- Do pair a serif heading with sans prose in a 2fr / 3fr grid for every section.
- Do separate sections with full-width hairlines, not bands of color.
- Don't add drop shadows; the declared `--shadow` stays unused and borders do the work.
- Don't center headings; everything aligns to the left edge of the 1120px column.
- Don't let figures exceed about 420px in height; they are `object-fit: contain` in their cards.

## Surfaces

Warm paper #edeae3 for the page and header, cream #f5f2ed for figure cards, table wrappers and stat cells, #e6e2da for table headers and inline code. Edges are 1px hairlines at 12% or 7% ink; no shadows.

## Imagery

Paper figures with flat pastel blocks (green, blue, peach, pink) and bold arrows, waveform glyphs, matplotlib line and bar charts in default blue, orange and green. Each sits in a cream card with rounded corners, sometimes widened beyond the text column.

## Layout

A sticky header over a left-aligned 1120px editorial column: a two-tier hero (headline block, then a 5fr / 4fr summary and results grid), then sections built on a 2fr / 3fr intro grid with full-width figures and tables. Rendered height is about 6,020px at 1440px.

## Agent Prompt Guide

Quick colors: paper #edeae3, cream #f5f2ed, card #e6e2da, ink #181814, body #4a4840, muted #8a8880, red #c04030, red tint rgba(192,64,48,.08), hairline rgba(24,24,20,.12), check #1d7c4a.

1. "Build a left-aligned editorial hero on #edeae3 inside a 1120px column: an 11.2px uppercase General Sans kicker in #c04030 with 0.18em tracking and a 24×1.5px red dash before it; a Newsreader 60px/1.08 bold #181814 headline with -0.02em tracking, max 20ch; a 'ACL 2026' badge (14.7px/600 #c04030 on rgba(192,64,48,.08), 1px rgba(192,64,48,.2) border, 4px radius); a 15.2px #181814 author line and a 13.6px #8a8880 affiliation line."
2. "Below a 1px rgba(24,24,20,.12) rule, make a 5fr/4fr grid with an 80px gap: left a 15.5px/1.7 #4a4840 summary and pill buttons (padding 8.8px 17.6px, 999px radius, 13.4px/600; primary #181814 with #edeae3 text, hover #c04030; ghost with a rgba(24,24,20,.12) border, hover red); right an 11.2px uppercase #8a8880 'KEY RESULTS' label and rows of Newsreader 22.4px bold #c04030 numerals with 14px #4a4840 descriptions."
3. "Create a results table in a #f5f2ed card with a 1px rgba(24,24,20,.12) border and 10px radius: header row #e6e2da with 11.5px uppercase #8a8880 labels, body 13.1px #4a4840 with rgba(24,24,20,.07) row rules and right-aligned tabular numbers, best values bold #c04030, second best underlined, row hover rgba(192,64,48,.08)."

## Similar Pages

- Editorial research microsites built with custom CSS variables and a serif display face over a warm off-white ground.
- Magazine-style landing pages (newsreader serif headlines, uppercase kickers, red accent).

## Quick Start

```css
:root {
  --bg: #edeae3;
  --bg-card: #e6e2da;
  --bg-white: #f5f2ed;
  --ink: #181814;
  --ink-2: #4a4840;
  --ink-3: #8a8880;
  --accent: #c04030;
  --accent-soft: rgba(192, 64, 48, 0.08);
  --border: rgba(24, 24, 20, 0.12);
  --border-2: rgba(24, 24, 20, 0.07);
  --radius: 10px;
  --radius-sm: 6px;
  --font-sans: "General Sans", system-ui, sans-serif;
  --font-serif: "Newsreader", Georgia, serif;
  --max: 1200px;
  --nav-h: 60px;
}
```

## Provenance

- **URL**: https://nishitanand.github.io/figma-website/
- **Paper**: FIGMA: Towards FIne-Grained Music retrievAl (arXiv 2606.06615), Nishit Anand, Ashish Seth, Sreyan Ghosh, Dinesh Manocha, Ramani Duraiswami (University of Maryland, College Park).
- **Venue**: ACL 2026.
- **Selection reason**: the arXiv 2606.06615 comment states acceptance at ACL 2026 and links the page. Chosen for the editorial look: serif display headline on warm paper, small red kicker labels, a two-column hero pairing the summary with key results in big red serif numerals, asymmetric section headings and figures in soft frames.
- **Template credit**: none; hand-written `styles.css` with CSS custom properties.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and fonts, the first-viewport screenshot, full-page capture and a 1440×6100 headless capture, `styles.css` and the HTML. Date 2026-10-28.
