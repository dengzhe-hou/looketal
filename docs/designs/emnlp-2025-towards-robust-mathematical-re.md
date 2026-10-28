# IMO-Bench — Style Reference

> A lab report printed on a single white sheet and laid on a grey desk: brand mark top left, a gold medal pinned top right, blue-ruled notes in the margins.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and top-of-page tall screenshots, and `index.html`, which uses the Tailwind Play CDN (`cdn.tailwindcss.com`) with a config that only overrides the sans and mono font stacks. All other values are Tailwind defaults resolved from utility classes; the page has no stylesheet of its own. No web font loads (`fonts_loaded` is empty), so the system UI face renders (Segoe UI here).

## Overview

The whole page is one tall white card (1024px wide, 16px radius, Tailwind `shadow-2xl` plus a faint ring) floating on a 5% grey ground with 16px of grey above and below. Inside, a header row holds the Google DeepMind wordmark image above a 36px bold near-black title, with the gold IMO-Bench medal image on the right, closed by a 1px grey rule. Below come a 16px author paragraph with blue superscript markers, a pale-blue note box with a 4px blue left bar, and three outlined blue buttons with dark grey icons. The article continues with 36px bold section headings underlined by a hairline, 16px body text, a pale-blue italic pull quote, rounded tables with uppercase grey headers and zebra rows, centred plots with italic captions, grey paper boxes and pale-blue BibTeX panels. Blue #2563eb is the only accent.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 44.8% (card), grey ground #f3f3f4 32.0% (rgba(17,24,39,0.05) over white), #ced1d5 11.0% (card shadow and text antialiasing), pale blue #eff6ff 7.2% (note box and quote), #fafbfd 3.5%, #fffefc 0.5%, #fffffd 0.5%, #f7f4f1 0.4% (medal and logo edges).

Anatomy in DOM order (desktop 1440px; body padding 16px 0; the card sits at x=208–1232 from y=16 with padding 48px 32px, so content runs x=240–1200, 960px wide):

1. **Brand logo** (`img.h-8.sm:h-10`, y=64): Google DeepMind wordmark image 298×40, margin-bottom 24px.
2. **Title** (`h1.text-3xl.md:text-4xl.font-bold`, y=128): 36px / 700 / 40px, #111827, left aligned, one line.
3. **Medal** (`img.h-24`, right of the header row at x=1104, y=64): 96×96 gold IMO-Bench medal, 4px radius; the header row is `flex items-start justify-between`.
4. **Header rule**: the header block has padding-bottom 16px and margin-bottom 16px inside a wrapper with a 1px #e5e7eb bottom border at y≈200, then margin-bottom 24px.
5. **Authors** (`p.mb-2.text-base`, y=225): 16px / 400 / 24px, #1f2937, three lines, left aligned; markers (◊, *, †) are `sup` in #2563eb 600; "(lead)" italic.
6. **Note box** (y≈322 to 400): #eff6ff, 4px #3b82f6 left border, 8px radius, padding 16px, 16px #4b5563 text (`md:text-base`), two lines with corresponding-author emails as #2563eb links. Margin-bottom 32px.
7. **Buttons** (y=433, 42px tall): Paper, Dataset, Leaderboard, 16px apart.
8. **First section heading** (`h2`, y=523 after margin-top 48px): "Introduction", 36px / 700 with 12px bottom padding and a 1px #e5e7eb underline; paragraphs from y=600 at 16px / 26px #1f2937; the blue pull quote starts at y≈866 at the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Desk Grey | rgba(17,24,39,0.05) | `bg-gray-900/5` | body ground around the card (renders #f3f3f4) |
| Card White | rgba(255,255,255,0.95) | `bg-white/95` | the page card |
| Ink | #111827 | `text-gray-900` | title, headings, table cells, BibTeX |
| Body Ink | #1f2937 | `text-gray-800` | author paragraph, body paragraphs |
| Muted | #4b5563 | `text-gray-600` | note box text, table header labels, citation intros, button icon fills |
| Caption Grey | #374151 | `text-gray-700` | italic figure captions, paper-box author lines |
| Accent Blue | #2563eb | `text-blue-600`, `border-blue-600` | links (500 weight), author markers, button text and border, best leaderboard values |
| Link Hover | #1e40af | `hover:text-blue-800`, `text-blue-800` | link hover, pull-quote text |
| Bar Blue | #3b82f6 | `border-blue-500` | 4px left bars of note box and pull quote, 1px BibTeX panel border |
| Pale Blue | #eff6ff | `bg-blue-50` | note box, pull quote, BibTeX panels, button hover |
| Hairline | #e5e7eb | `border-gray-200` | header rule, h2 underlines, table borders and row dividers, paper-box border |
| Zebra | #f9fafb | `bg-gray-50` | table header row, even rows, LEAP paper box |
| Shadow Ring | rgba(0,0,0,0.05) | `ring-black/5` | 1px ring around the card |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans | -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif (Tailwind config) | no web font; Segoe UI in this render | Inter |
| Mono | SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace | Consolas on Windows | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.text-3xl.md:text-4xl.font-bold` | 36px / 700 / 40px | #111827 |
| Section heading | `h2.text-3xl.md:text-4xl.font-bold.pb-3.border-b` | 36px / 700 / 40px, margin 48px 0 24px | #111827 |
| Subsection | `h3.text-2xl.md:text-3xl.font-bold` | 30px / 700 / 36px, margin 32px 0 16px | #111827 |
| Centred table title | `h3.text-xl.md:text-2xl.text-center` | 24px / 700 | #111827 |
| Paper-box title | `h4.text-xl.font-bold` | 20px / 700 | #111827 |
| Body | `.prose.leading-relaxed` paragraphs | 16px / 400 / 26px (`prose-lg` has no effect without the typography plugin) | #1f2937 |
| Authors | `p.text-base` | 16px / 400 / 24px | #1f2937 |
| Pull quote | `blockquote p.italic.text-xl` | 20px / 400 italic / 28px | #1e40af |
| Link | `a.text-blue-600.font-medium` | inherits size / 500 | #2563eb, hover #1e40af underline |
| Button | `a.text-sm.sm:text-base.font-medium` | 16px / 500 / 24px | #2563eb |
| Table header | `th.text-xs.font-semibold.uppercase.tracking-wider` | 12px / 600 / 16px, letter-spacing 0.6px | #4b5563 |
| Table cell | `td.text-base` | 16px / 400 / 24px | #111827 |
| Caption | `blockquote.italic` in figures | 16px italic, centred | #374151 |
| BibTeX | `pre.font-mono.text-sm.md:text-base` | 16px / 26px | #111827 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Page card | 16px (`rounded-2xl`) | ring 1px rgba(0,0,0,0.05) | `0 25px 50px -12px rgba(0,0,0,0.25)` (`shadow-2xl`) |
| Buttons | 8px (`rounded-lg`) | 1px solid #2563eb | `0 1px 2px 0 rgba(0,0,0,0.05)` (`shadow-sm`); focus ring 2px #3b82f6 with 2px offset |
| Note box | 8px | 4px solid #3b82f6 on the left | none |
| Pull quote | 0 8px 8px 0 (`rounded-r-lg`) | 4px solid #3b82f6 on the left | none |
| Tables | 12px (`rounded-xl`, overflow hidden) | 1px solid #e5e7eb; 1px row dividers; column rules `border-r` on leaderboards | `0 1px 3px 0 rgba(0,0,0,0.1), 0 1px 2px -1px rgba(0,0,0,0.1)` (`shadow`) |
| Figure frame | 12px, padding 16px, white | none | none; image inside `rounded-lg` 8px |
| Paper box (LEAP) | 12px, padding 24px | 1px solid #e5e7eb | none |
| BibTeX panel | 12px, padding 24px | 1px solid #3b82f6 | none |
| Medal image | 4px | none | none |

## Layout Metrics

- **Card**: `max-w-5xl` = 1024px, centred (x=208 at 1440), padding `lg:px-8 lg:py-12` = 48px 32px; content width 960px. Body padding `py-4` = 16px top and bottom.
- **Header**: logo 40px tall + 24px; title 40px; header padding-bottom 16px + margin-bottom 16px to the rule; 24px to the authors.
- **Sections**: `section.mb-12` (48px) plus each h2's `mt-12` (48px), so sections are about 96px apart; h2 `mb-6` 24px; paragraphs spaced by `space-y-4` 16px.
- **Tables**: wrapped in `my-8 flex justify-center` (32px above and below), full 960px width; cells padding 12px 20px.
- **Figures**: `my-8` wrapper; inner white frame `p-4` at `md:w-[75%]` = 720px for the main plot; captions `mt-4`.
- **Pull quote**: padding 16px 0 16px 24px, margin 24px 0.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px (`lg`, 1440 renders this) | card padding 32px; card padding-y 48px | 16px | 36px | — |
| 768–1023px (`md`) | 24px; card padding-y 32px | 16px | 36px | figures at 75% |
| 640–767px (`sm`) | 24px | 16px | 30px; h3 24px | buttons flex-wrap, 16px text |
| <640px | 16px | 16px | 30px | buttons in a 2-column grid at 14px; logo 32px tall; figures full width |

## Components

- **Outlined button**: flex, gap 8px, padding 8px 16px, radius 8px, #ffffff fill, 1px #2563eb border, 16px / 500 #2563eb text, `shadow-sm`; leading 24px icon (inline SVG document icon filled #4b5563, GitHub octicon, trophy) on the left. Hover fill #eff6ff, 150ms colour transition.
- **Note box**: #eff6ff, 4px #3b82f6 left bar, 8px radius, padding 16px, 16px #4b5563 text, items spaced 8px, blue superscript markers.
- **Pull quote**: `blockquote` with 4px #3b82f6 left bar, padding-left 24px, padding-y 16px, #eff6ff, right corners 8px; quote 20px italic #1e40af, attribution 16px #1e40af with an italic credential.
- **Section heading**: 36px / 700 #111827, padding-bottom 12px, 1px #e5e7eb bottom border, margin 48px 0 24px.
- **Data table**: 12px radius, 1px #e5e7eb border, Tailwind `shadow`, header #f9fafb with 12px / 600 uppercase #4b5563 labels tracked 0.05em, cells 16px #111827 at padding 12px 20px, rows alternate #ffffff / #f9fafb with 1px #e5e7eb dividers; leaderboards add vertical `border-r` rules and mark top values in #2563eb 700.
- **Figure**: white frame with 16px padding and 12px radius around a `rounded-lg` image, centred caption in 16px italic #374151 below.
- **Paper box**: #f9fafb, 1px #e5e7eb border, 12px radius, padding 24px; 20px / 700 title, 16px / 500 #374151 author line, then outlined buttons at 14px.
- **BibTeX panel**: #eff6ff, 1px #3b82f6 border, 12px radius, padding 24px, mono 16px / 26px #111827, wrapping (`whitespace-pre-wrap`).

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Brand header (logo + medal) | yes | DeepMind wordmark image left, gold medal image right, hairline below |
| Title / authors | yes | 36px bold title; 16px author paragraph with blue markers |
| Affiliation / contact note | present but non-standard | no affiliation list; a pale-blue note box carries contact emails and marker meanings |
| Link buttons | yes | three outlined blue buttons with icons |
| Venue badge | absent from the source | venue appears only as an inline link in the introduction |
| Introduction | yes | 16px article prose, no separate abstract |
| Pull quote | yes | pale-blue italic testimonial with a blue bar |
| Summary table | yes | rounded zebra table |
| Plots | yes | framed images with italic captions |
| Leaderboards | yes | multi-column tables with column rules and blue best values |
| Related paper box | yes | grey bordered box with its own buttons |
| BibTeX | yes | two pale-blue mono panels |
| Footer | absent from the source | the card ends after the citations |

## Adapting to Other Content

- **More authors**: keep one 16px paragraph wrapping at 960px with #2563eb superscript markers; put affiliations and contact lines in the pale-blue note box (16px #4b5563) rather than under the names.
- **A results table**: copy the data table recipe (12px radius, #f9fafb header with 12px uppercase labels, 16px cells, zebra rows) and mark the best value with #2563eb 700 only.
- **Teaser figure in the header**: place it as a figure after the buttons, inside the white 16px-padded frame at 720px width, caption italic #374151.
- **News or updates**: use the note-box recipe (pale blue, 4px #3b82f6 left bar) for each dated item, the date in 600 #111827.
- **More stats**: a summary table is the native form; avoid stat cards, which the page never uses.

## Do's and Don'ts

- Do put the whole article on one white card with a 16px radius and `shadow-2xl`, floating on the 5% grey ground.
- Do underline every h2 with a 1px #e5e7eb rule.
- Do use the 4px #3b82f6 left bar plus #eff6ff fill for any aside (notes, quotes).
- Do keep buttons outlined (white fill, blue border); there is no filled button on the page.
- Don't load a web font; the system UI stack is intended.
- Don't use colour other than the blue family, apart from the brand images.
- Don't add a hero background or full-bleed bands; everything stays inside the card.

## Surfaces

Grey ground rgba(17,24,39,0.05) behind a single white card. Inside, three tints only: #eff6ff for notes, the quote and BibTeX; #f9fafb for table headers, zebra rows and the paper box; white frames for figures.

## Imagery

Brand images (the multicolour Google DeepMind wordmark, a gold medal with ribbon) in the header, then matplotlib scatter and bar plots from the paper on white, each centred with an italic caption. Icons are inline SVG in grey.

## Layout

A single centred 1024px card with a document flow: header row, authors, note, buttons, then seven sections of prose, tables and figures, separated by 48px margins and h2 rules. No columns except within tables. About 11,800px tall.

## Agent Prompt Guide

Quick colors: ground rgba(17,24,39,0.05), card white, ink #111827, body #1f2937, muted #4b5563, caption #374151, accent #2563eb, hover #1e40af, bar #3b82f6, pale #eff6ff, hairline #e5e7eb, zebra #f9fafb.

1. "Wrap the page in one card: max-width 1024px, margin 16px auto, padding 48px 32px, background rgba(255,255,255,0.95), radius 16px, box-shadow 0 25px 50px -12px rgba(0,0,0,0.25) plus a 1px rgba(0,0,0,0.05) ring, on a body coloured rgba(17,24,39,0.05). Header row: logo image 40px tall, then a 36px / 700 #111827 title; a 96px emblem on the right; 1px #e5e7eb rule below."
2. "Make an outlined button: padding 8px 16px, radius 8px, #ffffff fill, 1px #2563eb border, 16px / 500 #2563eb, 24px grey icon on the left with an 8px gap, shadow 0 1px 2px 0 rgba(0,0,0,0.05), hover background #eff6ff."
3. "Build an aside: background #eff6ff, 4px solid #3b82f6 left border, radius 8px (quotes: right corners only), padding 16px (quotes: 16px 0 16px 24px); note text 16px #4b5563, quote text 20px italic #1e40af."

## Similar Pages

- Tailwind CDN research pages built as a single card on a tinted ground.
- Corporate-lab benchmark pages that lead with the lab wordmark rather than a title banner.

## Quick Start

```css
:root {
  --ground: rgba(17, 24, 39, 0.05);
  --card: rgba(255, 255, 255, 0.95);
  --ink: #111827;
  --body: #1f2937;
  --muted: #4b5563;
  --caption: #374151;
  --accent: #2563eb;
  --accent-hover: #1e40af;
  --bar: #3b82f6;
  --pale: #eff6ff;
  --hairline: #e5e7eb;
  --zebra: #f9fafb;
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  --font-mono: SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
  --radius-card: 16px;
  --radius-panel: 12px;
  --radius-btn: 8px;
  --card-max: 1024px;
}
```

## Provenance

- **URL**: https://imobench.github.io/
- **Paper**: Towards Robust Mathematical Reasoning (arXiv 2511.01846), Thang Luong (lead), Dawsen Hwang, Hoang Nguyen and colleagues, Google DeepMind.
- **Venue**: EMNLP 2025.
- **Selection reason**: the arXiv abstract links this project page and the comment states acceptance at EMNLP 2025.
- **Template credit**: none stated; Tailwind Play CDN with utility classes and Phosphor icons script.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and tall screenshots, and `index.html` markup and Tailwind config read directly, on 2026-10-28.
