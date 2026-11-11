# GAMA-Bench Scoreboard — Style Reference

> A game-night scoreboard taped to a white wall, with two purple controllers flanking a bold system-font title, a strip of shields.io stickers and one blue "Overall" tab lit up.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, platform fonts per node, first-viewport color share), a full-page 1440 capture plus 375 and 768 captures, extra probes at 640, 1024 and 1280 widths, forced-hover probes, a dark-scheme probe, and the built `assets/index-BiW35zQa.css` and `assets/index-M6b2Pl5T.js` fetched with curl. The page is a Vite single-page app (Vue 3, vue-router 4.5.0) styled with UnoCSS utilities on top of the untouched Vite starter stylesheet; there is no CSS reset, so `.border` utilities without a border style draw nothing and `box-sizing` stays `content-box`. Nothing downloads as a web font; every family is a system face (Segoe UI, Arial and Consolas on the Windows render).

## Overview

A single centred column on white, 3,362px tall, with no navbar and no footer. The hero is a 48px bold black title "🎮 GAMA-Bench Leaderboard 🎮" in the system sans, ten blue semibold author links with black superscripts on two lines, a grey affiliation row, a small "* Corresponding authors" note and three shields.io `for-the-badge` images (red arXiv, near-black GitHub, grey and green "ICLR'25 POSTER"). Below sits a 748px framework diagram (game icons on a #f5f5f5 rounded panel). The rest of the page is the leaderboard itself: a justified intro paragraph, a five-column grid of white rounded game tabs with the active one filled #2563eb, a "📝 Notes" bullet list, then a white card with a soft Tailwind-style shadow holding a two-column Arial table (Model, Score) under a grey left-to-right gradient header. Rows with missing games are tinted pale red with a small red note. A grey BibTeX block with a Copy button and a "🤗 More Leaderboards" list with coloured venue chips close the page.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 69.6%; light grey #f5f5f5 14.0% (the framework diagram's rounded panel); mid grey #979594 9.4% (title, author text and diagram icons and strokes anti-aliased together); pale teal #ebf7f5 3.4% and near-whites #fafafa 2.1%, #fdffff 1.0%, #fcf9e2 0.5% (diagram icon tints). The blue author links and the badge colors are too small to form their own clusters.

Anatomy in DOM order. `body` is `display:flex; place-items:center`; `#app` has max-width 1280px, padding 32px and auto margins (48px at 1440); `main` adds `p-10` (40px), so content runs x=120–1320 (1200px) and starts at y=72.

1. **Title** (`h1.text-5xl.font-bold.mb-6.mt-4`): 48px / 700 / 48px, #000000, centred, one line 760px wide at y=88–136 (72 + 16px margin-top); a 🎮 Segoe UI Emoji glyph at each end. Gap 24px.
2. **Authors** (`div.text-xl.mb-3.font-semibold.flex.flex-wrap.justify-center.gap-x-2`): y=160–229, 20px, two centred lines 34px apart (y=167 and y=201, superscripts open the line box). Names are `a.text-blue-600` at weight 500 (the Vite `a { font-weight: 500 }` rule beats the inherited 600, so Segoe UI Semibold renders), #2563eb; superscripts 16.67px / 600 #000000; commas 600 #000000; column gap 8px between author spans. Gap 12px.
3. **Affiliations** (`div.text-base.text-gray-700.flex.justify-center.flex-wrap.gap-x-6.mb-2`): y=241, 29px tall, four items 16px / 400 #374151 with leading superscript numbers, 24px column gap, 960px total. Gap 8px.
4. **Corresponding note** (`div.text-sm.text-gray-600.mb-8`): "* Corresponding authors", 14px / 20px #4b5563, y=279. Gap 32px + 24px (badge row `mt-6`) = 56px.
5. **Badges** (`div.flex.flex-wrap.justify-center.gap-3.mt-6.mb-12`): y=355, 400px wide row at x=520, gap 12px; three shields.io images `h-7 sm:h-8` render 32px tall: arXiv 99px (#b31b1b with white arXiv logo), GitHub 109px (#121011 with white GitHub logo), "ICLR'25 | POSTER" 168px (#555555 then #44bb00, no logo because `logo=iclr` is not a known icon). Badge text is shields' own Verdana bold capitals. The row box is 38px tall (inline images sit on a 24px line). Gap 48px + 16px = 64px.
6. **Teaser** (`img.rounded-xl.max-w-6xl.w-2/3` in `div.flex.justify-center.mt-4.mb-10`): 748×432 at x=346, y=457–889, radius 12px; the PNG (1122×648 natural) carries its own #f5f5f5 rounded panel, a dashed black divider and coloured game icons. The fold falls 11px below it; the leaderboard intro starts at y=985.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #ffffff | `bg-white`, Vite `:root` | page, `main`, inactive game tabs, leaderboard card |
| Title Black | #000000 | `text-black` | h1 title, author superscripts and commas |
| Link Blue | #2563eb | `text-blue-600`, `bg-blue-600` | author names, More Leaderboards links, active game tab fill |
| Link Hover | #747bff | Vite `a:hover` (light scheme) | author and list link color on hover (overrides the blue) |
| Text Grey | #374151 | `text-gray-700` | affiliations, intro paragraph, Notes, h2 section titles, tab labels, score cells, BibTeX text, Copy label |
| Muted Grey | #4b5563 | `text-gray-600` | corresponding-author note, inactive variant chips |
| Model Ink | #1f2937 | `text-gray-800` | model-name cells |
| Tab Border | #d1d5db | `border-gray-300`, `hover:bg-gray-300` | 1px border of inactive tabs and chips; header-cell and Copy hover fill |
| Tab Hover Border | #646cff | Vite `button:hover` | border of any tab or button on hover |
| Header Start | #f3f4f6 | `from-gray-100`, `bg-gray-100` | left end of the table header gradient, tab hover fill, BibTeX block |
| Header End | #e5e7eb | `to-gray-200`, `bg-gray-200` | right end of the header gradient, Copy button |
| Row Hover | #eff6ff | `hover:bg-blue-50` | complete rows on hover |
| Missing Row | #fef2f2 | `bg-red-50` | rows of models missing some games |
| Missing Row Hover | #fee2e2 | `hover:bg-red-100` | those rows on hover |
| Missing Note | #dc2626 | `text-red-600` | "(Missing: …)" note inside the model cell |
| Variant Green | #16a34a | `bg-green-600` | active variant chip (Implicit / Explicit, Highest / Second) |
| Toast Green | #22c55e | `bg-green-500` | "✓ Copied!" toast |
| arXiv Red | #b31b1b | shields.io | arXiv badge |
| GitHub Black | #121011 | shields.io | GitHub badge |
| Badge Grey | #555555 | shields.io | left half of the ICLR'25 badge |
| Poster Green | #44bb00 | shields.io `success` | right half of the ICLR'25 badge |
| Oral Chip | #ffedd5 / #c2410c | `bg-orange-100 text-orange-700` | "ICLR'24 Oral" chip in More Leaderboards |
| Poster Chip | #dcfce7 / #15803d | `bg-green-100 text-green-700` | "NeurIPS'24 Poster", "NeurIPS'25 Poster" chips |
| Panel Grey | #f5f5f5 | (image) | framework diagram panel |
| Shadow | rgba(0,0,0,0.1) | `shadow-lg` | leaderboard card, Copied toast |

## Tokens — Typography

| Family | Declared | Rendered (platform fonts) | Substitute |
|---|---|---|---|
| Sans (everything outside the table) | `main.font-sans`: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, emoji faces | Segoe UI (Regular 400, Semibold for 500 and 600, Bold 700); emoji in Segoe UI Emoji | Noto Sans (font_fit on the title: 1.03; Hind 0.967, Lato 0.962, Open Sans 1.033, Source Sans 3 0.92) |
| Table | `table { font-family: Arial, sans-serif }` (scoped) | Arial (ArialMT; weight 500 renders Regular, 600 and 700 render Bold) | Arimo (metric clone of Arial; font_fit 1.017 at 500, Roboto 0.993) |
| Code | `pre.font-mono` stack, but `code` keeps the UA `monospace` | Consolas | Inconsolata (font_fit 0.909; Cousine, IBM Plex Mono, JetBrains Mono, Roboto Mono all 1.091) |
| Badges | shields.io SVG text | Verdana, Geneva, DejaVu Sans (inside the images) | keep the images |

`fonts_loaded` is empty: no web font is requested. With Noto Sans, map weight 500 to 600 to keep the semibold look that Segoe UI gives the author names and tab labels.

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Title | `h1.text-5xl.font-bold` | 48px / 700 / 48px, centred | #000000 |
| Section title (Notes) | `h2.text-3xl.font-bold` | 30px / 700 / 36px, centred | #374151 |
| Section title (BibTeX, More Leaderboards) | `h2.text-4xl.font-bold` | 36px / 700 / 40px, centred | #374151 |
| Author names | `.text-xl a.text-blue-600` | 20px / 500 (Semibold face) / 28px | #2563eb |
| Author superscripts, commas | `.text-xl sup`, `span` | 16.67px / 600; 20px / 600 | #000000 |
| Affiliations | `.text-base.text-gray-700` | 16px / 400 / 24px | #374151 |
| Corresponding note | `.text-sm.text-gray-600` | 14px / 400 / 20px | #4b5563 |
| Intro paragraph | `p.leading-relaxed.text-justify` | 16px / 400 / 26px, justified (its `text-md` class generates nothing) | #374151 |
| Game tab | `button.text-sm.font-medium` | 14px / 500 / 20px | #374151, white when active |
| Variant chip | `button.text-xs.font-medium` | 12px / 500 / 16px | #4b5563, white when active |
| Notes list | `ul.list-disc.list-inside.leading-relaxed.text-left` | 16px / 400 / 26px; `strong` labels 700 | #374151 |
| Table header label | `th .font-semibold` | Arial 16px / 600 (renders Bold) / 24px | #374151 |
| Sort arrow | `th .text-xs` | Arial 12px / 12px line, ▲ or ▼ | #374151 |
| Model cell | `td.font-medium.text-gray-800.text-base` | Arial 16px / 500 / 24px, nowrap | #1f2937 |
| Score cell | `td.text-center.text-gray-700` | Arial 18px / 400 / 28px, two decimals | #374151 |
| Missing note | `td span.text-red-600.text-xs` | Arial 12px / 500 / 16px | #dc2626 |
| BibTeX | `pre.text-sm > code` | Consolas 14px / 20px | #374151 |
| Copy button | `.relative > button` | 12px / 500 | #374151 |
| More Leaderboards links | `li a.text-blue-600` | 16px / 500 / 26px | #2563eb |
| Venue chip | `span.text-xs.font-semibold` | 12px / 600 / 16px | #c2410c or #15803d |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Teaser image | 12px (`rounded-xl`) | none | none |
| Game tab, variant chip | 8px (`rounded-lg`) | 1px solid #d1d5db inactive, 1px transparent active; #646cff on hover | none |
| Leaderboard card | 12px (`rounded-xl`, clips the header gradient) | none | `0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1)` |
| Table cells | 0 | none rendered (`.border` without a style) | none |
| BibTeX `pre` | 12px | none rendered (`border border-gray-300` without a style) | none |
| Copy button | 4px (`rounded`) | 1px transparent | none |
| Copied toast | 4px | none | same as the card |
| Venue chip | 4px | none rendered | none |
| Badges | shields' own square corners | none | none |

## Layout Metrics

- **Container**: `#app { max-width: 1280px; margin: 0 auto; padding: 2rem }` (content-box, so 1344px with padding, 48px side margins at 1440) → `main` 1280px with `p-10` 40px → content 1200px at x=120–1320. Below 1344px the content is viewport − 144px.
- **Hero**: no band; title starts at y=88 (32 + 40 + 16). Vertical rhythm title → authors 24px, authors → affiliations 12px, affiliations → note 8px, note → badges 56px, badges → teaser 64px, teaser → intro 96px (40 `mb-10` + 16 `mt-4` + 40 `mt-10`).
- **Children of `main`** shrink to their content because `main` is `flex-col items-center`: the affiliation row is 960px, the badge row 400px, the teaser wrapper 1122px (the PNG's natural width), so `w-2/3` makes the teaser 748px.
- **Game tabs**: `grid gap-3 max-w-6xl mx-auto mt-6 mb-4` → 1152px at x=144, five 221×38px cells, 12px gaps, two rows at y=1061 and y=1111. Tab padding 8px 16px.
- **Variant chips** (only when El Farol Bar or Sealed-Bid Auction is selected): `flex flex-wrap justify-center gap-2 mb-4`, 30px tall chips with 6px 12px padding.
- **Notes**: block at y=1174 (h2 margin 24.9px collapses with `mt-6`), ul padding-left 40px with inside discs, `mb-8` 32px.
- **Leaderboard card**: y=1388, 1200×1356px, `overflow-x-auto`; header row 80px (Model `th` padding 12px 16px, Score `th` 8px 16px; three stacked divs 16 + 24 + 16px); 29 body rows of 44px (cell padding 8px 16px); Model column 1018px, Score column 182px.
- **BibTeX**: h2 at y=2792 (48px top margin); wrapper `relative w-full max-w-4xl mx-auto` 896px at x=272; `pre` is `w-full p-4` in content-box, so it renders 928×172px (x=272–1200), overhanging the wrapper by 32px on the right; Copy button 85×30px at x=1083, y=2856 (`top-2 right-0` of the wrapper).
- **More Leaderboards**: `mt-16 mb-8`, h2 at y=3084, left-aligned intro line and list; page ends at 3,362px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1344px (incl. 1440) | (viewport − 1200)/2, 120px at 1440 | 16px | 48px | 5 tab columns; teaser 748px; badges 32px |
| 1024–1343px | 72px (32 `#app` + 40 `main`) | 16px | 48px | 5 tab columns; teaser two thirds of the content width (587px at 1024) |
| 768–1023px | 72px | 16px | 48px | 4 tab columns |
| 640–767px | 72px on a 930px floor | 16px | 48px | 3 tab columns |
| <640px | 72px on a 930px floor | 16px | 48px | 2 tab columns; badges 28px |

Below about 930px the layout stops shrinking: `body` is a flex container, the flexed `#app` keeps its 930px min-content width, and the page scrolls sideways at 768 and 375 (measured scrollWidth 930). The title never changes size.

## Components

- **Author line**: centred flex-wrap row, 8px column gap; each span is a #2563eb 20px link (Semibold face, underline and #747bff on hover), a black 600 superscript of affiliation numbers ("1,2*" marks corresponding authors), and a black comma.
- **Badge row**: three linked shields.io `for-the-badge` images, 32px tall, 12px apart, `transition-transform hover:scale-105` (scale 1.05 on hover, 0.15s).
- **Game tab**: `button`, 221×38px grid cell, white with 1px #d1d5db border, radius 8px, padding 8px 16px, 14px / 500 #374151 centred label; hover fill #f3f4f6 with a #646cff border from the Vite starter rule; active state fills #2563eb with white text and a transparent border; `transition-colors` 0.2s. Clicking a tab re-sorts by score, descending.
- **Variant chip**: smaller sibling of the tab, 12px / 500, padding 6px 12px, radius 8px; inactive white with #d1d5db border and #4b5563 label, active #16a34a with white label.
- **Leaderboard card**: white, radius 12px, `shadow-lg`, horizontal scroll; Arial table with `border-collapse`, header row `linear-gradient(to right in oklch, rgb(243 244 246) 0%, rgb(229 231 235) 100%)`, no visible cell rules. Header cells are click-to-sort: an invisible ▲ spacer, the label, and a 12px arrow at opacity 1 on the sorted column, 0 elsewhere and 0.4 on hover; hover fills the cell #d1d5db.
- **Score row**: 44px, centred cells; model name Arial 16px / 500 #1f2937 nowrap, score Arial 18px #374151 with two decimals; hover #eff6ff. Rows of models missing games are #fef2f2 (hover #fee2e2) with a `title` tooltip and a 12px #dc2626 "(Missing: …)" note 8px after the name.
- **Notes list**: centred 30px / 700 #374151 h2 with a 📝 emoji, then a left-aligned disc list, 16px / 26px, bold run-in labels.
- **BibTeX block**: #f3f4f6, radius 12px, padding 16px, Consolas 14px / 20px #374151, horizontal scroll; Copy button top right (85×30px, #e5e7eb, radius 4px, 12px / 500 #374151, hover #d1d5db, label switches to "Copied!"); a "✓ Copied!" toast appears 96px left of the wrapper's right edge for 2s (#22c55e, white 14px, padding 4px 12px, radius 4px, `shadow-lg`, `animate-bounce`).
- **Venue chip**: inline span after a link, margin-left 8px, padding 2px 8px, radius 4px, 12px / 600; orange #ffedd5 / #c2410c for an oral, green #dcfce7 / #15803d for a poster.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navbar | No (absent from the source) | |
| Title / authors / affiliations | Yes | 48px black title with emoji, blue semibold names, grey affiliation row |
| Link buttons | Present but non-standard | three shields.io badge images instead of buttons |
| Venue badge | Present but non-standard | the third shields badge, "ICLR'25 POSTER" in grey and green |
| Teaser | Yes | framework diagram at two thirds width, 12px radius |
| Abstract | No (absent from the source) | a one-paragraph leaderboard intro stands in its place |
| Method / results figures | No (absent from the source) | |
| Leaderboard | Yes | game tabs, variant chips, Notes, shadowed sortable table |
| Video | No (absent from the source) | |
| BibTeX | Yes | grey rounded block with Copy button and bouncing toast |
| Related projects | Yes | "More Leaderboards" list with venue chips |
| Footer | No (absent from the source) | |

## Adapting to Other Content

- **More authors**: keep the flex-wrap 20px line with 8px gaps; at 1440 a third line starts after about 1200px of names, 34px below the second.
- **More affiliations**: keep the 16px #374151 row with 24px gaps; it wraps inside 1200px, about 29px per line.
- **Abstract**: put it where the intro paragraph sits (y=985), 16px / 26px #374151, but cap it at the 1152px tab width or narrower; justified at 1200px the measure is too long.
- **Results with more columns**: extend the same Arial table inside the card (1200px at 1440); give each score column about 182px, header cells 80px tall with the stacked sort arrow, scores 18px with two decimals.
- **News or updates**: reuse the Notes recipe, a 30px / 700 centred h2 with an emoji and a left-aligned 16px disc list with bold run-in dates.
- **No teaser diagram**: drop the 748px image and its wrapper; the intro paragraph then starts at y=497 (badge row bottom 393 + 48 + 16 + 40), and the game tabs move up by the same 488px. Do not stretch the badges to fill the space.
- **No leaderboard data**: replace the tab grid and table card with one white card of the same recipe (1200px, radius 12px, `shadow-lg`) holding a static Arial results table; keep the Notes list above it. Without tabs the Notes block and the card begin 112px earlier (the 88px grid plus its 24px top margin).
- **No shields.io badges**: use three 32px-tall flat rectangles in the same row (12px gap, square corners) with white 11px bold uppercase Verdana-like labels on #b31b1b, #121011 and #555555 / #44bb00; keep the 400px row centred at y=355.

## Do's and Don'ts

- Do keep the page one centred column with no bands; surfaces are only the card, the BibTeX block and the tabs.
- Do reserve #2563eb for links and the single active tab, and #16a34a for the single active variant chip.
- Do keep the table in Arial and the rest in the system sans; the switch is part of the look.
- Do add a CSS reset or a border style if you want the `.border` rules on cells, `pre` and chips to show; as built they draw nothing.
- Don't let the Vite starter rules leak: they turn link hover #747bff and tab hover borders #646cff.
- Don't size the BibTeX `pre` with `w-full` plus padding in content-box; it overhangs its wrapper by 32px and sits off-centre.
- Don't let a flexed `body` set a 930px floor; let the column shrink on phones.

## Surfaces

White page and `main`; a white leaderboard card with `shadow-lg` and a #f3f4f6 → #e5e7eb header gradient; #f3f4f6 BibTeX block; white tabs with #d1d5db borders; pale red #fef2f2 rows for incomplete models; small orange and green chips. The teaser brings its own #f5f5f5 panel. The dark color scheme changes nothing visible, since `main` forces white and black.

## Imagery

One raster framework diagram: a rounded #f5f5f5 panel with a column of model logos (OpenAI, Gemini, Meta, Anthropic, a group of people) left of a dashed black divider, and three rows of flat coloured game icons (handshake, beer, dollar, auction gavel, pistol, anchor) for Cooperative, Betraying and Sequential games with small black captions. The shields.io badges and the emoji in headings (🎮, 📝, 🤗) are the only other graphics.

## Layout

Centred single column in a 1200px content box: title, authors, affiliations, badges, a 748px teaser, then the leaderboard block (intro, 5×2 tab grid at 1152px, Notes, full-width table card), BibTeX at 928px, and a left-aligned More Leaderboards list. Sections are separated only by margins (40–64px). Rendered height 3,362px.

## Agent Prompt Guide

Quick colors: page #ffffff, title #000000, text #374151, muted #4b5563, model names #1f2937, links and active tab #2563eb, borders #d1d5db, header gradient #f3f4f6 → #e5e7eb, row hover #eff6ff, missing rows #fef2f2 with #dc2626 note, active variant #16a34a, badges #b31b1b, #121011, #555555 / #44bb00.

1. "Build a centred hero in a 1200px column with no background: a 48px / 700 black system-sans title with a 🎮 emoji at each end; 24px below, a flex-wrap row of 20px author links in #2563eb at weight 500 with black 600 superscripts and black commas, 8px gaps; 12px below, a 16px #374151 affiliation row with 24px gaps; 8px below, a 14px #4b5563 corresponding-author note; 56px below, three 32px-tall shields.io for-the-badge images 12px apart that scale to 1.05 on hover."
2. "Make a game selector: a grid of buttons, 5 columns at ≥1024px, 4 at ≥768px, 3 at ≥640px, 2 below, 12px gap, max width 1152px; each button white with a 1px #d1d5db border, radius 8px, padding 8px 16px, 14px / 500 #374151 label, hover fill #f3f4f6; the active button #2563eb with white text."
3. "Make a leaderboard card: white, radius 12px, box-shadow 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1), overflow-x auto; inside, an Arial table with no cell rules, an 80px header row with background linear-gradient(to right, #f3f4f6, #e5e7eb), bold 16px #374151 labels and a 12px sort arrow, then 44px rows: model name 16px / 500 #1f2937, score 18px #374151 with two decimals, hover #eff6ff; incomplete rows #fef2f2 with a 12px #dc2626 note."

## Similar Pages

- The ARISE Lab leaderboards linked at the foot of the page (PsychoBench, EmotionBench, CodeCrash), which the list presents as siblings; their styling was not checked here.
- Vite + Vue starter builds dressed with Tailwind or UnoCSS utilities, where the starter's `style.css` (flex `body`, #646cff link and button hovers) is left in place.

## Quick Start

```css
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;600;700&family=Arimo:wght@400;700&family=Inconsolata:wght@400&display=swap");
:root {
  --bg: #ffffff;
  --title: #000000;
  --text: #374151;
  --muted: #4b5563;
  --model: #1f2937;
  --link: #2563eb;
  --border: #d1d5db;
  --header-from: #f3f4f6;
  --header-to: #e5e7eb;
  --code-bg: #f3f4f6;
  --row-hover: #eff6ff;
  --missing-bg: #fef2f2;
  --missing-text: #dc2626;
  --variant: #16a34a;
  --badge-arxiv: #b31b1b;
  --badge-github: #121011;
  --badge-venue-left: #555555;
  --badge-venue-right: #44bb00;
  --font-sans: system-ui, "Segoe UI", "Noto Sans", sans-serif; /* Segoe UI is a system face; Noto Sans is the loadable substitute */
  --font-table: Arial, "Arimo", sans-serif; /* Arimo loads where Arial is missing */
  --font-mono: Consolas, "Inconsolata", monospace; /* Inconsolata is the loadable substitute */
  --content: 1200px;
  --tabs: 1152px;
  --title-size: 48px;
  --radius-card: 12px;
  --radius-tab: 8px;
  --shadow-card: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
}
```

## Provenance

- **URL:** https://cuhk-arise.github.io/GAMABench/
- **Paper:** How Far Are We on the Decision-Making of LLMs? Evaluating LLMs' Gaming Ability in Multi-Agent Environments (arXiv 2403.11807), Jen-tse Huang, Eric John Li, Man Ho Lam, Tian Liang, Wenxuan Wang, Youliang Yuan, Wenxiang Jiao, Xing Wang, Zhaopeng Tu, Michael R. Lyu (The Chinese University of Hong Kong, Tencent AI Lab, The Chinese University of Hong Kong Shenzhen, Tsinghua University). The page's BibTeX uses the conference title "Competing large language models in multi-agent gaming environments".
- **Venue:** ICLR 2025 poster; the "ICLR'25 POSTER" badge links to OpenReview forum DI4gW8viB6 and the BibTeX booktitle is the Thirteenth International Conference on Learning Representations.
- **Selection reason:** added on the maintainer's suggestion (2026-11-11), outside the two-round design selection; the project page is a live, sortable leaderboard rather than a paper summary.
- **Template credit:** none stated on the page; built with Vite, Vue 3 and vue-router 4.5.0, UnoCSS utility classes, and the Vite starter stylesheet left in place.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share; `tools/snap.py` screenshot; full-page captures at 1440, 768 and 375; DevTools probes of computed styles, platform fonts, forced hover states, the Copy toast, the El Farol Bar variant chips, widths at 375–1440 and the dark color scheme; `tools/font_fit.py` on the title, author line, model cell and BibTeX code; the built CSS and JS bundles and the shields.io SVGs via curl; 2026-11-11.
