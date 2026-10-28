# PAN-Crafter — Style Reference

> Mars red over a navy night: a planet logo sets the colors, and every result gets a tidy tile, tab or table that points back to "ours".

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's two stylesheets read directly: `static/css/family.css` (shared by the lab's GeoSET / GeoCR / MotionMaestro / PAN-Crafter pages, it sets layout and components) and `static/css/style.css` (PAN-Crafter brand tokens and page-only components). Most sizes are fluid `clamp()` values; the numbers below are what they resolve to at 1440 and were checked against rendered boxes. A fixed top nav exists but is hidden at the top of the page and slides in only after the hero is scrolled past, so the first-viewport shot does not show it.

## Overview

A carefully engineered light page (about 6,400px tall) with a design system rather than a template. A centred hero on white carries a faint Mars-red radial glow at the top, a wide two-color logo (a red planet icon plus the "PAN-Crafter" wordmark, "PAN" in Mars red #e0634b, "-Crafter" in navy #27536b), a two-line Outfit title whose middle phrase is red, red author names, a tinted venue pill, and a row of seven dark navy (#1c2738) pill buttons with line icons. A pill "Abstract" toggle sits under them. The body alternates white sections and pale bands (#f5f7fa with 1px #e2e6ec rules): a headline comparison figure, an interactive "All methods, same scenes" gallery (dataset tabs, square result tiles with "ours" outlined in red, prev/next carousel), full-resolution scenes, a paper-figure strip, quantitative tables with a red cmidrule and tinted "ours" row, method key points, BibTeX in a card, a "research line" band linking sibling papers, and a quiet footer.

## First Viewport

Color share (quantized 1440×900 shot): white #ffffff 55.3% (plus #fdfbfa 8.3%, #fffdfd 6.2%, #fdfffe 0.8%, #fffffd 0.5%, the tinted glow); dark #292023 12.6% and brown-gray #6d5c5a 9.1% come from the satellite image strip at the bottom and the navy buttons; #dcd7d7 7.2% is image highlights and borders. Mars red covers too little area to form its own cluster.

Anatomy in DOM order (desktop 1440px, centred, `.container` content box x=180 to 1260):

1. **Hero** (`header.hero`, 0–537px): padding 48px 0 14px; background `radial-gradient(1100px 420px at 50% -120px, color-mix(in srgb, var(--accent) 9%, #fff), transparent 72%), var(--bg)` (the mixed color renders as #fcf1ef).
2. **"More research" menu** (top-right, y=12, x≈1272–1408): a `details` pill, 32px tall, padding 0 10px 0 13px, 1px #e2e6ec border, 999px radius, white at 88%, 13px/600 #2b3240 text with a chevron; it opens a 272px panel (12px radius, shadow-m) listing the lab's remote-sensing papers.
3. **Logo** (`img.hero-logo` inside `h1`, y=48–144): 96px tall SVG lockup, 560px wide, centred. Gap 18px.
4. **Title** (`.hero-title`, y≈162–247): Outfit 36.8px/700, line-height 1.16, letter-spacing -0.012em, #1c2738; "Modality-Consistent Alignment" in #e0634b; breaks after the accent phrase (max-width 36ch). Gap 20px.
5. **Authors** (`.hero-authors`, y=267): 19px/500, links #b8452e, gap 4px 22px, superscripts #5a6373 600. Gap 6px.
6. **Affiliations** (`.hero-affil`, y=306): 15.6px #5a6373, two items with 18px gap. Gap 6px.
7. **Notes** (`.hero-notes`, y=338): 14px #6b7385 "† Co-corresponding authors" plus five emails in JetBrains Mono 13px. Gap 16px.
8. **Venue pill** (`.venue-pill`, y=378, 29px tall): "● ICCV 2025", 14px/600 #b8452e on #fdf2ef, 1px #f5cfc6 border, padding 5px 13px, 999px radius, a 6px dot before the text. Gap 20px.
9. **Button row** (`.btn-row`, y=427, 42px tall): Paper, Supp, arXiv, Video, Code, Gallery, BibTeX; 10px gaps. Gap 18px.
10. **Abstract toggle** (y=487, 36px tall): white pill, 1px #cad0da border, Outfit 15px/600 #1c2738 "Abstract" plus chevron. The hero ends at y=537.
11. **Headline section** (`.section--headline`, from y=537): padding-top 22px; h2 "Misaligned inputs, sharp outputs" at y=559 (Outfit 35.2px/700); lead line at y=609 (16px #5a6373, "50.11×" bold #1c2738); 20px gap; the wide comparison figure starts at y=655 (x=100, 1240px wide) and crosses the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Ink Navy | #1c2738 | --text / --ink | title, section titles, button fills, wordmark ink, table header text, bold text, topnav CTA |
| Body Slate | #2b3240 | --text-2 | body copy, table cells, "More research" button text |
| Muted Slate | #5a6373 | --muted | lead lines, affiliations, captions, footer text, author superscripts |
| Faint Slate | #6b7385 | --faint | author notes and emails, tile venue labels, table venue column, hints |
| Mars Red | #e0634b | --accent | title accent phrase, "PAN" in the logo, "ours" tile border and ring, table cmidrules, active carousel dot, selected figure thumb ring, focus outlines |
| Mars Red Text | #b8452e | --accent-text | author links, venue pill text, active tab text, filled chip tabs, "OURS" badge, link color, button hover fill |
| Mars Red Strong | #933520 | --accent-strong | link and author hover |
| Blush | #fdf2ef | --accent-soft | venue pill fill, "ours" tile and table row tint, active topnav link, current research-line item |
| Blush Line | #f5cfc6 | --accent-line | venue pill border, key-point top rules, topnav active ring |
| Brand Navy | #27536b | --brand-navy | "-Crafter" in the wordmark (logo, nav, footer) |
| Band | #f5f7fa | --bg-band | alternating section bands, BibTeX head, abstract panel, research-line band, table group rows |
| Sunken | #eceff4 | --bg-sunken | tab track, tile image well, input badges |
| Border | #e2e6ec | --border | band rules, figure, table and card borders, footer rule |
| Border Strong | #cad0da | --border-strong | abstract toggle, copy button and carousel button borders, inactive dots, input tile dashed border |
| White | #ffffff | --bg | page, hero base, cards, active tab |
| Hero Glow | #fcf1ef | (computed mix, 9% #e0634b in white) | centre of the hero radial glow |
| Success | #17804d | --ok | copy button after copying |
| Shadow Ink | rgba(16,24,40,…) | (literal, in --shadow-s / --shadow-m) | soft card, table, button-hover and nav shadows |
| Label Scrim | rgba(14,17,23,.74) | (literal, `.cmp-label`) | dark pill labels on compare-dialog images |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text | "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif | Inter 400, 500, 600, 700 | Inter (Google Fonts) |
| Display | "Outfit", "Inter", system-ui, … | Outfit variable 500–800 | Lexend |
| Mono | "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace | JetBrains Mono 400 | IBM Plex Mono |
| Icons | inline SVG sprite (stroke 1.8, round caps) | — | Lucide |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.hero-title` | clamp(1.45rem, 1.02rem + 1.55vw, 2.3rem) → 36.8px / 700 / 1.16, Outfit, -0.012em | #1c2738, accent #e0634b |
| Section title | `.section-title` | clamp(1.55rem, 1.12rem + 1.35vw, 2.2rem) → 35.2px / 700 / 1.15, Outfit, -0.012em | #1c2738 |
| Lead | `.lead` | 16px / 400 / 1.6, max 84ch | #5a6373, bold #1c2738 |
| Authors | `.hero-authors` | clamp(1rem, .95rem + .3vw, 1.1875rem) → 19px / 500 | links #b8452e |
| Affiliations | `.hero-affil` | 0.975rem = 15.6px / 400 | #5a6373 |
| Notes / emails | `.hero-notes` | 14px; emails JetBrains Mono 13px | #6b7385 |
| Body | `body` | 1.0625rem = 17px / 400 / 1.7 | #2b3240 |
| Button | `.btn` | 15px / 600 / 1 | #ffffff |
| Venue pill | `.venue-pill` | 14px / 600 / 1.2, letter-spacing 0.01em | #b8452e |
| Tab | `.tab` | 14px / 600 / 1 | #5a6373; selected #b8452e |
| Caption | `.figure figcaption` | 14.5px / 1.6, centred, max 118ch | #5a6373, lead-in bold #1c2738 |
| Tile method / venue | `.tile-m` / `.tile-v` | 13px / 600 and 11px / 500 | #1c2738 / #6b7385 |
| Table | `.results` | 14px / 1.3, tabular numbers; metric headers 12.48px / 600 | #2b3240; best 700 #1c2738; second underlined |
| Key-point number | `.kp-num` | Outfit 12px / 700, uppercase, letter-spacing 0.12em | #b8452e |
| BibTeX | `.bibtex pre` | JetBrains Mono 13.5px / 1.7 | #1c2738 |
| Footer | `.footer` | 14px | #5a6373 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Buttons, venue pill, tabs, abstract toggle, topnav links | 999px | venue 1px #f5cfc6; toggle 1px #cad0da | button hover `0 6px 16px -6px rgba(16, 24, 40, .16), 0 2px 4px -2px rgba(16, 24, 40, .06)` |
| Figures, table frames, BibTeX card | 12px | 1px #e2e6ec | tables and BibTeX `0 1px 2px rgba(16, 24, 40, .05), 0 1px 3px rgba(16, 24, 40, .07)` |
| Result tile | 11px (image well 7px) | 1px transparent; input tiles 1px dashed #cad0da; ours 1px #e0634b | ours `0 0 0 1px var(--accent)` |
| Chip picker card | 18px | 1px #e2e6ec | shadow-s as above |
| Compare dialog | 18px | none | `0 24px 60px -16px rgba(9, 13, 22, .45)`; backdrop rgba(10,12,16,.7) with `blur(3px)` |
| Carousel / icon buttons | 50%, 38px | 1px #cad0da | hover shadow-s |
| Copy button | 8px | 1px #cad0da | none |
| Research-line item | 8px | 1px #e2e6ec; current 1px #e0634b + inset ring | hover shadow-s |
| Key point | 0 | 2px #f5cfc6 top | none |

## Layout Metrics

- **Containers**: `--gutter: clamp(16px, 4vw, 32px)` → 32px. `.container` max-width 1080 + 2×32 = 1144px (content x=180 to 1260); `.container--wide` 1240 + 64 = 1304px (content x=100 to 1340) for figures, galleries and tables.
- **Hero**: padding clamp(28px, 4vw, 48px) top → 48px, clamp(8px, 1.2vw, 14px) bottom → 14px; logo height clamp(min(58px, 15.1cqw), 7vw, 96px) → 96px; logo-to-title gap 18px; authors margin-top 20px; venue margin-top 16px; button row margin-top 20px, gap 10px; abstract toggle margin-top 18px. Rendered 537px tall.
- **Sections**: `--section-pad: clamp(44px, 6vw, 76px)` → 76px top and bottom; the headline section uses 22px top, 56px bottom. Section head max 780px (headline 960px), margin-bottom 32px (headline 20px). Sub-heads inside one band start 104px below the previous block.
- **Figures**: headline comparison 1240px wide; captions 14px below.
- **Gallery tiles**: grid of `minmax(min(140px, calc(33.333% - 7px)), 1fr)` with 12px row and 10px column gaps; script balances rows (8 tiles across at 1440).
- **Tables**: in 1240px frames; cells padding 9px 11px.
- **BibTeX**: card max 880px, centred.
- **Top nav**: fixed, 56px tall when shown.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1321px | 32px | 17px | 36.8px (cap) | full layout |
| 900–1320px | 32px | 17px | 1.02rem + 1.55vw (e.g. 32.3px at 1030) | same |
| ≤899px | 32px (4vw below 800) | 17px | fluid (28.7px at 800) | "More research" menu leaves the corner and sits right-aligned above the hero |
| ≤820px | 4vw | 17px | fluid | nav height 52px; nav "Paper" CTA hidden; nav links become sunken pills |
| ≤760px | 4vw | 17px | fluid | key points 1 column; research line runs vertically with ↓ arrows |
| ≤720px | 4vw | 17px | fluid | chip rows scroll horizontally with edge fades |
| ≤600px | 4vw (24px at 600) | 17px | fluid | table text 13px, cells 8px; BibTeX wraps |
| ≤480px | 4vw, 16px floor below 400px | 17px | 23.8px at 480, 23.2px floor | buttons 40px tall, padding 0 14px 0 12px, 14px text; carousel dots hidden |
| ≤380px | 16px | 17px | 20.8px | — |

## Components

- **Hero button** (`.btn`): inline-flex, 42px tall, padding 0 18px 0 15px, gap 8px, 999px radius, #1c2738 fill, white Inter 15px/600, 18px line icon on the left. Hover: fill #b8452e, translateY(-1px), shadow-m.
- **Venue pill** (`.venue-pill`): inline-flex, padding 5px 13px, #fdf2ef fill, 1px #f5cfc6 border, 14px/600 #b8452e, a 6px round dot in currentColor before the label.
- **Abstract toggle**: `details > summary` pill, 36px tall, padding 0 12px 0 16px, white, 1px #cad0da, Outfit 15px/600 #1c2738 with a chevron that rotates 180° when open; open state #fdf2ef fill, #f5cfc6 border, #b8452e text. Panel: #f5f7fa, 1px #e2e6ec, 12px radius, 22px 26px padding, 16px/1.7 left-aligned text.
- **Segmented tabs** (`.tablist` / `.tab`): #eceff4 track, padding 4px, 999px radius; tabs padding 9px 16px, 14px/600 #5a6373 with a `small` sub-label in #6b7385 ("WV3 WorldView-3"); selected tab white with #b8452e text and shadow-s.
- **Result tile** (`.tile`): column flex, padding 5px 5px 7px, 11px radius; square image well (#eceff4, 7px radius, zoom-in cursor, a 26px dark round swap icon appears on hover); caption method 13px/600 #1c2738 and venue 11px/500 #6b7385. Input tiles: 1px dashed #cad0da border and an uppercase "INPUT" badge on #eceff4. Ours tile: #fdf2ef fill, 1px #e0634b border plus `0 0 0 1px var(--accent)` ring, method name #b8452e, white uppercase "OURS" badge on #b8452e.
- **Carousel controls**: "Scene 1 / 4" counter 14px 700 #1c2738 with muted title; dots 7px #cad0da, active stretched to 20px #e0634b; 38px round prev/next buttons with 1px #cad0da borders, hover border #e0634b and text #b8452e.
- **Compare dialog**: opens on tile click; 18px radius, white, header with an 11px/700 uppercase kicker; swipe stage with a 2px white handle and a 34px white round knob (`0 2px 8px rgba(0, 0, 0, .3)`); labels are dark translucent pills (rgba(14,17,23,.74)), ours label #b8452e.
- **Results table** (`.results` in `.table-frame`): white frame, 12px radius, 1px #e2e6ec, shadow-s; dataset group headers with a 2px #e0634b cmidrule; metric row 12.48px/600 #5a6373 over a 1.5px #1c2738 rule; rows separated by 1px #e2e6ec; "ours" row tinted #fdf2ef with a 3px inset #e0634b bar on the method cell and #b8452e 700 text; best values 700 #1c2738, second underlined 1.5px. Sticky first column.
- **Key points** (`.keypoints`): 3 columns, each with a 2px #f5cfc6 top rule, 12px top padding, Outfit 12px/700 uppercase #b8452e number, bold #1c2738 lead, 15px #2b3240 text.
- **BibTeX card**: max 880px, 12px radius, 1px #e2e6ec, shadow-s; #f5f7fa head bar with a right-aligned copy button (32px, 8px radius, 1px #cad0da, 13px/600; hover #b8452e; copied state #17804d).
- **Research-line band** (`.lineage`): #f5f7fa band above the footer, centred row of 8px-radius cards (Outfit 13.5px/650 name, 11px venue) joined by → arrows; current paper highlighted #fdf2ef with a #e0634b ring.
- **Top nav** (after scrolling): fixed, 56px, `background: rgba(255, 255, 255, .9)`, `backdrop-filter: saturate(170%) blur(12px)`, 1px #e2e6ec bottom border, shadow `0 8px 24px -18px rgba(16, 24, 40, .45)`; 28px logo icon and wordmark left; 14px/500 #5a6373 pill links right, active link #b8452e on #fdf2ef with an inset #f5cfc6 ring; navy "Paper" CTA 34px pill.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Logo / wordmark | yes | 96px two-color SVG lockup in the hero; 28px icon + wordmark in nav and footer |
| Title / authors / affiliations | yes | centred, Outfit title with red phrase, red author links, mono emails |
| Venue badge | yes | blush pill with a dot |
| Link buttons | yes | seven navy pills with line icons |
| Abstract | present but non-standard | collapsed behind a pill toggle under the buttons |
| Teaser / headline figure | yes | wide comparison figure in a 12px-radius bordered frame with centred caption |
| Interactive gallery | yes | segmented dataset tabs, square result tiles, carousel, compare dialog |
| Paper figures | yes | thumbnail strip with prev/next and a selected red ring |
| Results tables | yes | framed, cmidrule in red, tinted "ours" row |
| Method | yes | figure plus three key points on a band |
| BibTeX | yes | bordered card with a band head and copy button |
| Related work line | yes | "More research" dropdown in the hero and a research-line band before the footer |
| Video | absent from the source | the Video button links out; no embedded `<video>` |
| Footer | yes | 1px top rule, 14px muted text, wordmark and links |

## Adapting to Other Content

- **More authors**: the author row already wraps with 4px 22px gaps at 19px; beyond eight authors keep the size and let affiliations wrap at 15.6px with numbered superscripts.
- **A results table**: use the `.results` recipe as is (12px frame, 2px #e0634b group rules, tinted #fdf2ef "ours" row, best 700 #1c2738, second underlined); it renders at 14px in the 1240px wide container.
- **Long publication or news lists**: reuse the research-line items (8px radius, 1px #e2e6ec, Outfit 13.5px/650 title, 11px venue) stacked in a 1080px column on a #f5f7fa band, with the newest highlighted in #fdf2ef.
- **More qualitative results**: add a tab to the `.tablist` and tiles to the strip; mark the method's own output with the ours tile, never with a second accent color.
- **A video**: put it in a `.figure-media` frame (12px radius, 1px #e2e6ec) at 1240px width with the centred 14.5px caption.

## Do's and Don'ts

- Do take the palette from the logo: #e0634b for large accents and rules, #b8452e for small text and white-on-red fills, #27536b only in the wordmark.
- Do keep primary buttons navy #1c2738 and turn them red #b8452e only on hover.
- Do mark "ours" the same way everywhere: #fdf2ef tint, #e0634b ring, #b8452e label.
- Do alternate white sections with #f5f7fa bands framed by 1px #e2e6ec rules.
- Don't put large blocks of red; the accent stays in text, rules, rings and small fills.
- Don't use Outfit for body text; it is for titles, section heads, toggles and small labels.
- Don't show the top nav at the top of the page; it appears only after the hero.

## Surfaces

White page with a 9% Mars-red radial glow behind the hero; #f5f7fa bands for the gallery, method and research-line sections; white cards (figures, tables, BibTeX, chip pickers) with 1px #e2e6ec borders and very soft two-layer shadows; #eceff4 sunken tracks for tabs and image wells; a translucent blurred white nav bar after scrolling.

## Imagery

Satellite crops (WorldView-3, QuickBird, GaoFen-2, WorldView-2) shown as square tiles and full 512×512 scenes, paper figures with LaTeX-style labels, and a flat illustrated Mars planet icon with stars in red and navy. Images sit in rounded wells or bordered frames; the comparison figure keeps its own red zoom boxes.

## Layout

Single centred column: a 1080px measure for hero, BibTeX and footer and a 1240px measure for figures, galleries and tables. Section heads are centred (title, one lead line) and every section uses 76px vertical padding, alternating white and banded backgrounds.

## Agent Prompt Guide

Quick colors: ink #1c2738, body #2b3240, muted #5a6373, faint #6b7385, accent #e0634b, accent text #b8452e, blush #fdf2ef, blush line #f5cfc6, band #f5f7fa, sunken #eceff4, border #e2e6ec, wordmark navy #27536b.

1. "Build a centred hero: padding 48px 0 14px, background radial-gradient(1100px 420px at 50% -120px, #fcf1ef, transparent 72%) over white. 96px logo, 18px gap, Outfit 36.8px/700 title (#1c2738, line-height 1.16, letter-spacing -0.012em) with the key phrase in #e0634b; Inter 19px/500 author links in #b8452e; 15.6px #5a6373 affiliations; a venue pill (14px/600 #b8452e on #fdf2ef, 1px #f5cfc6, padding 5px 13px, 999px, 6px dot); a row of 42px navy #1c2738 pill buttons (15px/600 white, padding 0 18px 0 15px, 10px gap) that turn #b8452e on hover."
2. "Make a gallery: segmented tabs on a #eceff4 track (4px padding, 999px), tabs 14px/600 #5a6373, selected white with #b8452e text; below, square tiles (11px radius, 5px padding, image well #eceff4 7px radius) with 13px/600 method and 11px #6b7385 venue; the method's own tile gets #fdf2ef fill, a 1px #e0634b border plus a 1px #e0634b ring, and a white uppercase 'OURS' badge on #b8452e."
3. "Create a results table in a white frame (12px radius, 1px #e2e6ec, shadow 0 1px 2px rgba(16,24,40,.05), 0 1px 3px rgba(16,24,40,.07)); 14px tabular numbers, cells 9px 11px; dataset headers with a 2px #e0634b underline; metric row 12.48px/600 #5a6373 over a 1.5px #1c2738 rule; 'ours' row #fdf2ef with a 3px inset #e0634b bar and #b8452e 700 method name; best 700 #1c2738, second underlined."

## Similar Pages

- The same lab's GeoSET, GeoCR and MotionMaestro pages, which share `family.css` and differ only in brand tokens.
- Product-grade research pages built on a token system (Inter text, display face for titles, navy buttons, single brand accent).

## Quick Start

```css
:root {
  --text: #1c2738;
  --text-2: #2b3240;
  --muted: #5a6373;
  --faint: #6b7385;
  --bg: #ffffff;
  --bg-band: #f5f7fa;
  --bg-sunken: #eceff4;
  --border: #e2e6ec;
  --border-strong: #cad0da;
  --accent: #e0634b;
  --accent-text: #b8452e;
  --accent-strong: #933520;
  --accent-soft: #fdf2ef;
  --accent-line: #f5cfc6;
  --brand-navy: #27536b;
  --radius-s: 8px;
  --radius: 12px;
  --radius-l: 18px;
  --radius-pill: 999px;
  --shadow-s: 0 1px 2px rgba(16, 24, 40, .05), 0 1px 3px rgba(16, 24, 40, .07);
  --shadow-m: 0 6px 16px -6px rgba(16, 24, 40, .16), 0 2px 4px -2px rgba(16, 24, 40, .06);
  --w-content: 1080px;
  --w-wide: 1240px;
  --gutter: clamp(16px, 4vw, 32px);
  --section-pad: clamp(44px, 6vw, 76px);
  --font-sans: "Inter", system-ui, sans-serif;
  --font-display: "Outfit", "Inter", system-ui, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, monospace;
}
```

## Provenance

- **URL**: https://kaist-viclab.github.io/PAN-Crafter_site/
- **Paper**: PAN-Crafter: Learning Modality-Consistent Alignment for PAN-Sharpening (arXiv 2505.23367), Jeonghyeok Do, Sungpyo Kim, Geunhyuk Youk, Jaehyup Lee, Munchurl Kim (KAIST; Kyungpook National University).
- **Venue**: ICCV 2025.
- **Selection reason**: the arXiv comment states acceptance at ICCV 2025 and links this project page.
- **Template credit**: no outside template; the KAIST VICLab shared stylesheet `family.css` (identical across the lab's GeoSET, GeoCR and MotionMaestro pages) plus a page `style.css`; carousel and figure strip comments credit the lab's GeoSET / ReFlowSET and SOfA pages.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, and `family.css`, `style.css` and `index.html` read directly, on 2026-10-28.
