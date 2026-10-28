# Event-Driven Video Generation — Style Reference

> A lab bench with a strip of film pinned above it: off-white paper, heavy navy type, and a black filmstrip frame that turns four sample clips into a contact sheet.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, plus targeted probes of the hero, filmstrip teaser, idea cards, comparison grid, sample browser and BibTeX), the 1440×900 shot and a full-page capture, and the page's own `styles.css` and `index.html`. Comparison videos load on demand and show a "Loading" placeholder in the full-page capture. Inter is declared but no web font is loaded, so the page renders in the system UI face.

## Overview

A compact, product-like research page (8,235px) on off-white #fbfbf8 with navy ink #172033 and heavy weights (700–900) throughout. A 63px translucent header holds a 44px navy square logo "EVD" and four 15.2px/700 gray links. The hero is centred: a blue-tinted "ECCV 2026 Oral" tag with 6px radius, a two-line 67.2px/700 title, a 19.5px subtitle, blue author links and three 46px buttons with 6px radius (navy filled "Paper PDF", outlined "arXiv" and "Code"). The teaser is the signature: a 1180px white card with a soft shadow whose top is a #111827 filmstrip, white sprocket holes drawn with repeating gradients along both edges, framing four square video cards with bold captions, and a gray caption bar below. Sections are left-aligned in the same 1180px column: an orange uppercase eyebrow, a 35.2px/700 heading and a gray lead. "Core idea" shows four white cards, each topped with a 32×6px colored tab (blue, orange, green, red). The curated comparisons repeat a four-column grid per prompt (Sora, Movie Gen, DiT, EVD) where the EVD card is outlined in green with a green label. Below come filter chips and a 4-column sample browser with green tags, a full-width method figure (1320px) and a dark BibTeX block.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): paper #fbfbf8 / #fafbf8 / #fbfbf7 / #fbfbf9 / #fcfbf8 together 60.4% plus white #fefefd 4.4%; warm dark #504b3d 20.1% (the filmstrip frame, navy title and video content blended); light gray #d9d8d5 15.1% (video backgrounds, card borders and text antialiasing).

Anatomy in DOM order (desktop 1440px, column width min(1180px, 100% − 32px) → x 130–1310):

1. **Sticky header** (`header.site-header`, 0–63px): rgba(251,251,248,0.94) with `backdrop-filter: blur(14px)`, 1px rgba(217,222,232,0.75) bottom border; nav min-height 62px. Logo `a.nav-logo` at x=130: 44×44px #172033 square, 6px radius, white "EVD" 16px/800. Links right: 15.2px/700 #5a6578, 22px gaps; hover #172033.
2. **Hero** (`section.hero`, 63–1003): padding 52px 0 38px; copy block max 940px centred, margin-bottom 28px.
3. **Venue tag** (`p.venue`, y=115, 149×37): 16px/800 #1554b7 on rgba(21,84,183,0.07), 1px rgba(21,84,183,0.22) border, padding 5px 13px, 6px radius. Gap 14px.
4. **Title** (`h1`, y=166, 138px, two lines): 4.2rem = 67.2px/700, line-height 1.03, letter-spacing 0, #172033, centred. Gap 18px.
5. **Subtitle** (`p.subtitle`, y=322, two lines): 1.22rem = 19.52px/400 #30394a, line-height 1.55, max 810px. Gap 18px.
6. **Authors** (`p.authors`, y=401): 16px/700, gaps 10px 16px, links #1554b7. Gap 24px.
7. **Buttons** (`.actions`, y=450, 46px, 12px gaps): padding 0 18px, 6px radius, 1px #172033 border, 16px/800; "Paper PDF" #172033 fill with white text; "arXiv" and "Code" white with #172033 text; hover translateY(-1px). Gap 28px.
8. **Filmstrip teaser** (`figure.teaser`, y=524, 1180×441): white, 1px #d9dee8, 8px radius, shadow `0 18px 45px rgba(23, 32, 51, 0.12)`. Inside, `.hero-teaser-grid` (y=525, 387px tall): #111827, radius 8px 8px 0 0, padding 34px 18px, 4 columns with 14px gap; sprocket rows 18px tall at 8px from top and bottom: `repeating-linear-gradient(90deg, transparent 0, transparent 14px, rgba(255, 255, 255, 0.82) 14px, rgba(255, 255, 255, 0.82) 26px, transparent 26px, transparent 40px)` at opacity 0.9. Video cards 273px square (white, 1px #d9dee8, 7px radius) with 44px caption bars in 11.52px/700 #172033. Caption bar (y=912): padding 14px 18px, 1px #d9dee8 top, 15.04px #5a6578, centred. Hero ends at y=1003; the Core Idea section starts below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #fbfbf8 | --paper | body, header base |
| Surface | #ffffff | --surface | cards, teaser card, outline buttons, filter chips, video card captions |
| Navy Ink | #172033 | --ink | title, headings, logo tile, primary button fill, button borders, active filter chip |
| Muted | #5a6578 | --muted | nav links, section leads, captions, card text, inactive chips, footer |
| Subtitle Ink | #30394a | (literal) | hero subtitle |
| Label Ink | #2e3748 | (literal) | baseline video labels |
| Line | #d9dee8 | --line | card borders, teaser caption rule, sample-block rules, footer rule |
| Blue | #1554b7 | --blue | venue tag text, author links, Causal Initiation tab, inspector "+" |
| Orange | #d86419 | --orange | section eyebrows, Event Realization tab |
| Green | #16723f | --green | EVD card label, sample tags, Stable Postconditions tab |
| Red | #b3262f | --red | Contact Stability tab |
| Violet | #4b3ca8 | --violet | declared, not visible in the first screens |
| Film Black | #111827 | (literal) | filmstrip frame, BibTeX background |
| Code Text | #eef2f7 | (literal) | BibTeX text |
| Video Placeholder | #e9edf3 | (literal) | square video wells before load |
| Ours Outline | rgba(22,114,63,0.55) | (literal) | EVD card border, plus a 2px rgba(22,114,63,0.12) ring |
| Blue Wash | rgba(21,84,183,0.07) | (literal) | venue tag fill (border at 0.22) |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| UI / text | Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif | no web font loaded; the OS UI face renders (Segoe UI on Windows, SF Pro on macOS; Inter only where installed) | Inter |
| Code | browser monospace | Consolas / Courier New default | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Title | `h1` | 4.2rem = 67.2px / 700 / 1.03 | #172033 |
| Section heading | `.section-heading h2` | 2.2rem = 35.2px / 700 / 1.12 | #172033 |
| Eyebrow | `.eyebrow` | 0.82rem = 13.12px / 900 / uppercase, no tracking | #d86419 |
| Section lead | `.section-heading p` | 1.02rem = 16.32px / 400 | #5a6578 |
| Subtitle | `.subtitle` | 1.22rem = 19.52px / 400 / 1.55 | #30394a |
| Body | `body` | 16px / 400 / 1.55 | #172033 |
| Venue tag | `.venue` | 16px / 800 | #1554b7 |
| Nav | `.nav-links` | 0.95rem = 15.2px / 700 | #5a6578 |
| Button | `.button` | 16px / 800 | white or #172033 |
| Idea card title | `.claim h3` | 1.08rem = 17.28px / 700 | #172033 |
| Comparison prompt | `.sample-title h3` | 1.12rem = 17.92px / 700 | #172033 |
| Video label | `.video-label` | 0.84rem = 13.44px / 900; `small` 11.52px / 800 #5a6578 | #2e3748, ours #16723f |
| Teaser caption | `.teaser-video-card p` | 0.72rem = 11.52px / 700 / 1.18 | #172033 |
| Filter chip | `.filter-chip` | 0.88rem = 14.08px / 800 | #5a6578, active white |
| Sample tag | `.sample-tag` | 0.68rem = 10.88px / 900 | #16723f |
| BibTeX | `.bibtex pre` | 0.93rem = 14.88px monospace | #eef2f7 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow / effect |
|---|---|---|---|
| Logo tile, buttons, venue tag, filter chips | 6px | buttons 1px #172033; chips 1px #d9dee8 | buttons lift 1px on hover |
| Teaser card, method figure | 8px | 1px #d9dee8 | `0 18px 45px rgba(23, 32, 51, 0.12)` |
| Filmstrip frame | 8px 8px 0 0 | none | sprocket rows from repeating gradients |
| Teaser video cards | 7px | 1px #d9dee8 | none |
| Idea cards, video cards, sample cards, BibTeX | 8px | 1px #d9dee8 (ours rgba(22,114,63,0.55)) | ours `0 0 0 2px rgba(22, 114, 63, 0.12)` |
| Idea tab | 4px, 32×6px | none | solid color |
| Sample tag, inspector "+" box | 5px | "+" box 1px #d9dee8 | none |

## Layout Metrics

- **Column**: `.nav`, `.hero`, `.section`, `.footer`: width min(1180px, calc(100% − 32px)), margin auto → x 130–1310 at 1440; the method section widens to min(1320px, 100% − 32px) → x 60–1380.
- **Hero**: padding 52px 0 38px; vertical chain 37 (tag) + 14 + 138 (title) + 18 + 60 + 18 + 25 (authors) + 24 + 46 (buttons) + 28 + 441 (teaser) = 849px from y=115 to y=965.
- **Teaser**: filmstrip padding 34px 18px, 4 columns with 14px gap → 273px cards; caption bars min-height 44px; figure caption padding 14px 18px.
- **Sections**: padding 64px 0 (Core Idea 42px top); section heading max 760px (wide 900px), margin-bottom 28px; eyebrow margin-bottom 8px; h2 margin-bottom 12px.
- **Idea cards**: 4 columns, gap 14px (285px each), min-height 190px, padding 20px; tab 26px above the title.
- **Comparison rows**: stacked with 42px gaps; each row has a 1px #d9dee8 top rule, 22px top padding, a prompt title and a 4-column grid (gap 12px, 286px cards) with 42px label bars and square video wells.
- **Sample browser**: filter chips (gap 10px, margin-bottom 22px), then 4 columns with 14px gap; card bodies padding 10px.
- **Footer**: padding 36px 0 48px, 1px #d9dee8 top, one 16px #5a6578 line.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| base (1440) | 130px (1180px column) | 16px | 67.2px | 4-column filmstrip, ideas, comparisons and samples |
| ≤1212px | 16px | 16px | 67.2px | column fills the width minus 32px |
| ≤920px | 16px | 16px | 48px (3rem) | ideas, comparisons and samples 2 columns; filmstrip 2 columns with 10px gap and padding 30px 12px |
| ≤640px | column capped at 358px | 16px | 32.6px (2.04rem) | nav stacks with 0.8rem links; hero padding-top 34px; subtitle 16.8px; sections 44px; h2 23.4px; all grids 1 column; chips 34px tall |
| ≤480px | same | 16px | 32.6px | teaser caption 14.08px |

## Components

- **Logo tile** (`.nav-logo`): 44×44px, #172033, 6px radius, white 16px/800 initials.
- **Venue tag** (`.venue`): inline-flex, min-height 34px, padding 5px 13px, 6px radius, rgba(21,84,183,0.07) fill, 1px rgba(21,84,183,0.22) border, 16px/800 #1554b7.
- **Button** (`.button`): min-height 46px, padding 0 18px, 6px radius, 1px #172033 border, 16px/800; primary #172033 with white text, secondary white with #172033 text; hover translateY(-1px).
- **Filmstrip teaser**: a #111827 band (radius 8px 8px 0 0, padding 34px 18px) with 18px sprocket rows of 12px white rectangles every 40px (rgba(255,255,255,0.82) at 0.9 opacity), holding square video cards (white, 1px #d9dee8, 7px radius) with 44px white caption bars in 11.52px/700; the whole sits in a white 8px-radius card with a 0 18px 45px shadow and a gray caption bar.
- **Colored-tab idea card** (`.claim`): white, 1px #d9dee8, 8px radius, padding 20px, min-height 190px; a 32×6px tab (4px radius) in #1554b7, #d86419, #16723f or #b3262f, 26px above a 17.28px/700 title and 16px #5a6578 text.
- **Comparison card** (`.video-card`): white, 1px #d9dee8, 8px radius; 42px label bar (padding 8px 10px, 1px bottom rule) with a 13.44px/900 method name left and an 11.52px/800 gray role ("baseline", "base", "ours") right; square #e9edf3 video well. The EVD card: border rgba(22,114,63,0.55), ring 0 0 0 2px rgba(22,114,63,0.12), label #16723f.
- **Filter chip** (`.filter-chip`): min-height 38px, padding 0 13px, 6px radius, 1px #d9dee8, white, 14.08px/800 #5a6578; active or hover #172033 fill, white text.
- **Sample card**: white, 1px #d9dee8, 8px radius; square video; body padding 10px with a green tag (10.88px/900 #16723f on rgba(22,114,63,0.09), 5px radius, padding 3px 7px) and a 12.48px/800 single-line prompt.
- **Inspector disclosure**: 1px #d9dee8 top rule, 58px summary in 15.2px/800 #5a6578 led by a 24px white box with a 1px #d9dee8 border, 5px radius and a blue "+".
- **BibTeX**: #111827 pre, 1px #d9dee8, 8px radius, padding 22px, monospace 14.88px #eef2f7.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky header | yes | translucent paper bar with a navy logo tile |
| Venue badge | yes | blue-tinted 6px-radius tag ("ECCV 2026 Oral") |
| Title / authors | yes | centred heavy title, blue author links |
| Affiliations | absent from the source | no affiliation line in the hero |
| Link buttons | yes | navy filled and outlined 6px-radius buttons |
| Teaser | yes | filmstrip-framed 4-up video contact sheet |
| Abstract | present but non-standard | replaced by the "Core idea" heading and four tabbed idea cards |
| Baseline comparison | yes | 4-column video grids per prompt with a green-outlined ours card |
| Sample browser | yes | filter chips and a 4-column tagged sample grid |
| Results table | absent from the source | evidence is qualitative video only |
| Method figure | yes | 1320px white figure card with the teaser shadow |
| BibTeX | yes | dark #111827 block |
| Footer | yes | one gray line above a hairline |

## Adapting to Other Content

- **More authors**: keep the centred flex row (16px/700, gaps 10px 16px, links #1554b7); add affiliations as a 15.04px #5a6578 line 8px below, matching the teaser caption tone.
- **A results table**: put it in a white card (1px #d9dee8, 8px radius) in the 1180px column; header 13.44px/900 #2e3748 with a 1px #d9dee8 bottom rule, cells 16px #172033, and mark the EVD row with #16723f text and a rgba(22,114,63,0.09) fill, the same green as the ours card.
- **Long publication or news lists**: use comparison-row structure: 1px #d9dee8 top rule, 22px padding, a 17.92px/700 title and a gray 14.08px/800 meta label on the right.
- **More idea cards**: keep four per row and cycle the tab colors blue, orange, green, red.
- **Image results**: reuse the filmstrip frame for a hero contact sheet, and the square video-card grid for comparisons.

## Do's and Don'ts

- Do keep type heavy: 700 for headings, 800 for buttons and nav, 900 for labels and eyebrows.
- Do keep corners small and consistent (6px controls, 7–8px cards).
- Do mark "ours" with green #16723f only, never with the blue or orange accents.
- Do use the four tab colors once each in the idea row and nowhere as large fills.
- Don't round buttons into pills; they are 6px rectangles.
- Don't add shadows to small cards; only the teaser and the method figure carry the 0 18px 45px shadow.
- Don't track the uppercase eyebrows; they use letter-spacing 0 at weight 900.

## Surfaces

Off-white #fbfbf8 page; white #ffffff cards with #d9dee8 hairlines; a #111827 filmstrip band and a #111827 BibTeX block as the only dark surfaces; #e9edf3 video placeholders.

## Imagery

Generated short clips of everyday physical interactions (a kick into a goal, a ball hitting a wall, a door opening, a glass set on a table) shown as square videos in a filmstrip, in 4-way comparisons against Sora, Movie Gen and a DiT base, and in a tagged sample grid; one wide method diagram.

## Layout

A left-aligned 1180px column after a centred hero, with sections built from a heading block and a single grid (4 columns of 285px cards). Hairline-ruled comparison rows repeat down the page; the method figure breaks out to 1320px.

## Agent Prompt Guide

Quick colors: paper #fbfbf8, surface #ffffff, ink #172033, muted #5a6578, line #d9dee8, blue #1554b7, orange #d86419, green #16723f, red #b3262f, film #111827.

1. "Build a centred hero on #fbfbf8 in a 1180px column, padding 52px 0 38px: a tag with rgba(21,84,183,0.07) fill, 1px rgba(21,84,183,0.22) border, 6px radius, padding 5px 13px, 16px/800 #1554b7; a 67.2px/700 #172033 title (line-height 1.03); a 19.52px #30394a subtitle (max 810px); 16px/700 #1554b7 author links; 46px buttons (padding 0 18px, 6px radius, 1px #172033, 16px/800): one #172033 with white text, the others white."
2. "Make a filmstrip teaser: white card with 1px #d9dee8 border, 8px radius and box-shadow 0 18px 45px rgba(23, 32, 51, 0.12); inside a #111827 band with padding 34px 18px and a 4-column grid (14px gap) of square video cards (white, 1px #d9dee8, 7px radius, 44px caption bar in 11.52px/700). Add 18px sprocket rows 8px from top and bottom using repeating-linear-gradient(90deg, transparent 0, transparent 14px, rgba(255, 255, 255, 0.82) 14px, rgba(255, 255, 255, 0.82) 26px, transparent 26px, transparent 40px)."
3. "Create a 4-way comparison row: 1px #d9dee8 top rule, 22px padding, 17.92px/700 prompt title, then a 4-column grid with 12px gap of white cards (1px #d9dee8, 8px radius) each with a 42px label bar (13.44px/900 #2e3748 name, 11.52px/800 #5a6578 role) and a square #e9edf3 video well. The ours card uses border rgba(22,114,63,0.55), box-shadow 0 0 0 2px rgba(22,114,63,0.12) and a #16723f label."

## Similar Pages

- Video-generation project pages that present baselines as aligned 4-up grids with a highlighted ours column.
- Compact product-style research pages with heavy system-font type and 6px-radius controls.

## Quick Start

```css
:root {
  --ink: #172033;
  --muted: #5a6578;
  --paper: #fbfbf8;
  --surface: #ffffff;
  --line: #d9dee8;
  --blue: #1554b7;
  --orange: #d86419;
  --green: #16723f;
  --red: #b3262f;
  --violet: #4b3ca8;
  --film: #111827;
  --shadow: 0 18px 45px rgba(23, 32, 51, 0.12);
  --font: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --column: min(1180px, calc(100% - 32px));
  --radius-control: 6px;
  --radius-card: 8px;
}
```

## Provenance

- **URL**: https://evd-project-website.pages.dev/
- **Paper**: Event-Driven Video Generation (arXiv 2603.13402), Chika Maduabuchi, Jindong Wang.
- **Venue**: ECCV 2026 (the page labels it an Oral).
- **Selection reason**: the arXiv comment states acceptance at ECCV 2026 and links this project page.
- **Template credit**: none stated; a small hand-written page (`styles.css`, `script.js`) hosted on Cloudflare Pages.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted probes of hero, filmstrip, idea cards, comparison grid, sample browser and BibTeX, the 1440×900 shot and a full-page capture, and the page's `styles.css` and `index.html` read directly, on 2026-10-28.
