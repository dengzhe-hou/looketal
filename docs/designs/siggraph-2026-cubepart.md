# CubePart — Style Reference

> A design-studio catalogue on cream stock: a violet-to-jade serif wordmark, black pill buttons, and toy-like 3D parts that come apart under a slider.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and tall screenshots, and the page's `static/css/style.css` and `index.html`. In the render the hero video showed only its black player with native controls (no poster frame loaded), and the gallery's 3D viewer was still showing "Loading model…" with a black behavior-video tile beside it; those blank states are capture artefacts, not the design. Interactive values (explode slider, tooltips) come from the stylesheet.

## Overview

A polished, left-aligned editorial page on warm cream #fbfaf7 with ink #1a1d24. Newsreader, a display serif, sets the title and section headings; Inter sets everything else, and JetBrains Mono the code. The identity is a gradient wordmark: "CubePart" fills with violet → indigo → jade (`#6f5cd6 → #4f3fbf → #2aa48a`) beside a 36px serif subtitle on the same line. A white venue pill with a glowing violet dot sits above it, and two faint radial washes (violet top-left, jade top-right) tint the hero. Authors wrap in one left-aligned flow with violet superscripts, and five black pill buttons with line icons close the hero. Below, a tinted band holds the video, the full-width teaser figure sits in a 12px-radius white frame, and sections follow with 40px serif titles underlined by a 36×3px violet-to-jade bar. The gallery is a carousel of white cards, each pairing an interactive 3D viewer (cream gradient stage, glass control bar with a gradient explode slider and black "Reset" pill) with a behavior video. Tables sit in 14px cards with tinted headers; BibTeX is a dark #14171f block.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): cream family #fbfaf7 / #f5f3f0 / #f9f9f6 / #fefefc / #fbfaf6 / #fafaf8 / #fbfafc together 90.4% (page, the tinted video band and the header); slate gray #6a6b71 9.6% (the black video player and pill buttons blended with author text). The violet-to-jade wordmark is too small to form a cluster.

Anatomy in DOM order (desktop 1440px; content column x=158 to 1282):

1. **Sticky header** (`header.site-header`, 0–57px): rgba(251,250,247,0.78) with `backdrop-filter: saturate(180%) blur(10px)`, 1px rgba(0,0,0,0.05) bottom border; `.header-inner` height 56px inside the 1180px container (padding 0 28px). Brand: 20px cube icon in #1a1d24 (violet on hover) and "CubePart" Inter 17px/700, letter-spacing -0.01em, gap 9px. Nav: Gallery, Abstract, Method, Dataset, Results, BibTeX at 14px/500 #303542, gap 18px; hover #6f5cd6.
2. **Hero** (`section.hero`, 57–534px): padding 64px 0 28px; `.hero::before` 360px tall from -100px with `radial-gradient(60% 90% at 12% 18%, rgba(111, 92, 214, 0.08), transparent 70%), radial-gradient(60% 90% at 88% 14%, rgba(42, 164, 138, 0.07), transparent 70%)`.
3. **Venue pill** (`.venue-badge`, y≈121, ≈37px tall): "SIGGRAPH ’2026 · Los Angeles", 13px/500 #303542, letter-spacing 0.01em, #ffffff, 1px #e3dfd5, radius 999px, padding 7px 14px, small shadow; 8px #6f5cd6 dot with `box-shadow: 0 0 0 4px rgba(111, 92, 214, 0.15)`, gap 10px. Gap 18px.
4. **Title** (`h1.title`, y=176, one line, left-aligned): Newsreader 64px (clamp(34px, 5.4vw, 64px)) / 600 / 1.05, letter-spacing -0.02em. `span.title-mark` "CubePart" with `background: linear-gradient(120deg, var(--accent) 0%, #4f3fbf 50%, var(--accent-2) 100%)` clipped to text; colon `.title-sep` in #303542 with 6px right margin; `span.subtitle` Newsreader 36px (clamp(22px, 3.2vw, 36px)) / 500 #1a1d24, inline. Gap 6px + 28px.
5. **Authors** (`ul.authors`, y=275 and 306, two lines): flex-wrap, gap 4px 16px; names Inter 16px/500 #1a1d24, superscripts 11.2px/600 #6f5cd6; hover violet with a dotted violet underline.
6. **Affiliations** (`ul.affiliations`, y≈339): 15px #6b7180, gap 6px 22px, violet 600 superscripts.
7. **Notes** (`.contrib-note`, y=375): two lines at 13px #6b7180 ("The first four authors…", "Project leads."). Gap 28px.
8. **Buttons** (`.action-row`, y=450, 44px tall, gap 10px): arXiv, Code, Video, Demo, BibTeX; #1a1d24 fill, #fbfaf7 text Inter 14.5px/500, letter-spacing 0.005em, radius 999px, padding 10px 18px, 18px line icon left with 9px gap, `box-shadow: 0 1px 2px rgba(20, 20, 30, 0.05), 0 4px 14px -8px rgba(20, 20, 30, 0.12)`.
9. **Video band** (`section.section.section-tinted`, 534–814px): padding 64px 0, `background: linear-gradient(180deg, var(--bg) 0%, var(--bg-tint) 18%, var(--bg-tint) 82%, var(--bg) 100%)`; inside the 820px narrow container a `.video-card` (1px #e3dfd5, 14px radius, #0c0e14) holding the video, captured at 762×150 with only its controls showing.
10. **Teaser** (`section.teaser-wrap`, from 814px): padding 12px 0 8px; figure at y=838, image 1124px wide with 12px radius, 1px #e3dfd5 border, white ground and the small shadow; caption 14.5px #303542 with a bold lead.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Cream | #fbfaf7 | --bg | page, header (78%), button text |
| Cream Tint | #f3f0ea | --bg-tint | tinted bands, table headers, legend chips, footer |
| White | #ffffff | --bg-soft | venue pill, figure grounds, gallery cards, stat cards, tables |
| Ink | #1a1d24 | --ink / --pill-bg | title, headings, author names, pill buttons, Reset pill |
| Ink 2 | #303542 | --ink-2 | nav links, colon, captions, table text, section intros |
| Muted | #6b7180 | --muted | affiliations, notes, loading text, footer |
| Line | #e3dfd5 | --line | pill, figure, card, table and video borders |
| Line Strong | #c9c2b3 | --line-strong | card hover borders, inactive carousel dots |
| Violet | #6f5cd6 | --accent | wordmark start, venue dot, superscripts, links, title underline start, slider, active dot, best values, stat numbers |
| Indigo | #4f3fbf | (literal) | wordmark gradient midpoint |
| Jade | #2aa48a | --accent-2 | wordmark end, title underline end, slider end, "Copied" state |
| Button Hover | #2c3140 | (literal) | pill and Reset hover fill |
| Code Ink | #14171f / #e8ecf5 | --code-bg / --code-fg | BibTeX block fill / text |
| Inline Code | #3d2f9c on rgba(111, 92, 214, 0.08) | (literal) | prompt-template code in the Method text |
| Video Black | #0c0e14 | (literal) | video card and player ground |
| Behavior Video | #15171f | (literal) | gallery behavior-video tile ground |
| Disabled Pill | #444956 | (literal) | disabled action button fill |
| Viewer Stage | #f1eee6 → #e1dcce | (literal) | 3D viewer gradient stops |

Declared but not visible: `--accent-3: #d56c8f` (rose) is defined in `:root` but no rendered element uses it.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | 'Newsreader', 'Inter', serif | Newsreader 500, 600 | Source Serif 4 |
| UI / body | 'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif | Inter 400, 500, 600, 700 | IBM Plex Sans |
| Code | 'JetBrains Mono', ui-monospace, SFMono-Regular, 'SF Mono', Menlo, monospace | JetBrains Mono 400 | IBM Plex Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Wordmark + title | `.title` | clamp(34px, 5.4vw, 64px) → 64px / 600 / 1.05, letter-spacing -0.02em | gradient mark, #1a1d24 |
| Inline subtitle | `.subtitle` | clamp(22px, 3.2vw, 36px) → 36px / 500 | #1a1d24 |
| Section title | `.section-title` | clamp(28px, 3.6vw, 40px) → 40px / 600, letter-spacing -0.015em | #1a1d24 |
| Subsection | `.subsection-title` | Inter 22px / 600, letter-spacing -0.01em | #1a1d24 |
| Gallery card title | `.pv-title` | Inter 20px / 600, letter-spacing -0.01em | #1a1d24 |
| Body | `body` | 17px / 400 / 1.65 | #1a1d24 |
| Section intro / lead | `.section-intro`, `.lead` | 17px (lead 1.06em) | #303542 |
| Authors | `.authors li` | 16px; names 500 | #1a1d24 |
| Affiliations | `.affiliations` | 15px | #6b7180 |
| Venue pill | `.venue-badge` | 13px / 500, letter-spacing 0.01em | #303542 |
| Button | `.action-btn` | 14.5px / 500 | #fbfaf7 |
| Caption, prompt | `.figure figcaption`, `.pv-prompt` | 14.5px / 1.55 | #303542 |
| Stat number | `.tldr-num` | Newsreader 30px / 600 / 1.1 | #6f5cd6 |
| Control label | `.pv-label`, `.pv-reset` | 12px / 600 uppercase, letter-spacing 0.04em | #303542 / #fbfaf7 |
| Table | `.data-table` | 14.5px; th 600 | #303542 |
| BibTeX | `.bibtex-card pre` | JetBrains Mono 13.5px / 1.6 | #e8ecf5 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Venue pill, action buttons, chips, Reset, viewer control bar | 999px | pill 1px #e3dfd5; chips 1px #e3dfd5; control bar 1px rgba(0,0,0,0.06) | `0 1px 2px rgba(20, 20, 30, 0.05), 0 4px 14px -8px rgba(20, 20, 30, 0.12)`; control bar `0 6px 16px rgba(20,23,31,0.06)` |
| Gallery cards, stat cards, tables, video card, BibTeX | 14px | 1px #e3dfd5 (BibTeX none) | small shadow; gallery hover and BibTeX `0 2px 6px rgba(20, 20, 30, 0.06), 0 18px 40px -20px rgba(20, 20, 30, 0.25)` |
| Figure images, 3D viewer, behavior video | 12px | 1px #e3dfd5 | small shadow on figures |
| Carousel arrows | 50%, 44px | 1px #e3dfd5 | `0 6px 18px rgba(20,23,31,0.15)` |
| Carousel dots | 50%, 9px | none | none; active #6f5cd6 scaled 1.25 |
| Inline code | 4px | none | none |
| Section-title underline | 2px | — | 36×3px `linear-gradient(90deg, var(--accent), var(--accent-2))`, 8px below |

3D viewer stage: `background: radial-gradient(60% 80% at 50% 28%, rgba(255,255,255,0.85), transparent 70%), linear-gradient(180deg, #f1eee6 0%, #e1dcce 100%)`, aspect 4/3. Part tooltip: `rgba(255, 255, 255, 0.62)` with `backdrop-filter: blur(14px) saturate(180%)` and `box-shadow: 0 1px 1px rgba(255, 255, 255, 0.6) inset, 0 6px 18px rgba(20, 23, 31, 0.14), 0 1px 3px rgba(20, 23, 31, 0.08)`.

## Layout Metrics

- **Containers**: `.container` max 1180px with 28px side padding (content x=158 to 1282 at 1440); `.container.narrow` max 820px (764px content, x=338) for the video, Abstract and BibTeX.
- **Hero**: padding 64px 0 28px under the 57px header; pill→title 18px, title→authors 6px + 28px, notes→buttons 28px, buttons margin-bottom 12px.
- **Sections**: padding 64px 0; tinted sections use the four-stop cream gradient; section title margin-bottom 14px plus the underline, section intro margin 18px 0 28px.
- **Figures**: margin 22px 0 28px; `figure-medium` 80%, `figure-narrow` 60%, `figure-xnarrow` 50% of the column above 720px.
- **Gallery**: carousel track grid-auto-columns 100%, gap 24px; card padding 22px; stage 2 columns gap 16px (viewer + video, each 4:3); arrows at -10px outside the card; dots 8px gap, 14px below.
- **Grids**: stat cards 4 columns in the 820px narrow container (171px each), gap 14px; two-column explainer 1.05fr / 1fr, gap 28px; results grid 2 columns, gap 22px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >880px | 28px | 17px | 64px (5.4vw caps from 1185px) | 4 stat cards, 2-column stage and explainer |
| ≤880px | 28px | 17px | 5.4vw ≈ 47.5px at 880 | stat cards 2 columns; explainer and viewer stage 1 column; arrows move inside to 4px |
| ≤720px | 28px | 17px | 5.4vw, floor 34px from 630px | nav hidden; results grid 1 column; figure width limits removed |

## Components

- **Venue pill** (`.venue-badge`): inline-flex, gap 10px, padding 7px 14px, #ffffff, 1px #e3dfd5, radius 999px, 13px/500 #303542, small shadow; leading 8px #6f5cd6 dot with a 4px rgba(111,92,214,0.15) halo.
- **Gradient wordmark**: Newsreader 64px/600, `linear-gradient(120deg, #6f5cd6 0%, #4f3fbf 50%, #2aa48a 100%)` clipped to text, followed by a #303542 colon and a 36px/500 Newsreader subtitle on the same baseline.
- **Pill button** (`.action-btn`): #1a1d24, #fbfaf7 Inter 14.5px/500, radius 999px, padding 10px 18px, 18px icon left, small shadow. Hover: #2c3140, translateY(-1px). Disabled: #444956 at 55% opacity.
- **Section title** (`.section-title`): Newsreader 40px/600, inline-block, with a 36×3px violet-to-jade bar 8px below its left edge.
- **Gallery card** (`.pv-card`): white, 1px #e3dfd5, radius 14px, padding 22px, small shadow (medium on hover); 20px/600 Inter title, italic 14.5px prompt, a 2-up stage of a 4:3 3D viewer (12px radius, cream gradient stage) and a 4:3 behavior video (#15171f).
- **Explode control** (`.pv-overlay`): glass bar 12px from the viewer edges, rgba(255,255,255,0.84) with blur 8px, radius 999px, padding 8px 12px; "Explode" 12px/600 uppercase label, a 4px `linear-gradient(90deg, var(--accent), var(--accent-2))` range track with a 16px white thumb ringed 2px #6f5cd6, and a black 12px/600 uppercase "Reset" pill (padding 6px 14px).
- **Carousel controls**: 44px round arrows (rgba(255,255,255,0.92), 1px #e3dfd5, 22px glyphs, scale 1.05 on hover); 9px dots in #c9c2b3, active #6f5cd6.
- **Stat card** (`.tldr-card`): white, 1px #e3dfd5, radius 14px, padding 18px 18px 16px, Newsreader 30px/600 #6f5cd6 number, 13.5px #303542 label; hover lifts 2px.
- **Data table** (`.table-wrap`): white 14px card; header #f3f0ea 600 #303542, padding 12px 14px; cells 11px 14px with 1px #e3dfd5 rules; best row rgba(111,92,214,0.05) with violet bold values; ablation rows italic #6b7180.
- **BibTeX** (`.bibtex-card pre`): #14171f, #e8ecf5 JetBrains Mono 13.5px/1.6, radius 14px, padding 22px, medium shadow; translucent copy pill top-right that turns rgba(42,164,138,0.85) when copied.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky header | yes | blurred cream bar, cube icon brand, 14px nav |
| Venue badge | yes | white pill with glowing violet dot |
| Title / subtitle | yes | gradient serif wordmark with inline serif subtitle, left-aligned |
| Authors / affiliations / notes | yes | left-aligned flow, violet superscripts, muted notes |
| Link buttons | yes | five black pills with line icons |
| Video | yes | 820px dark video card in a tinted band (blank in the capture) |
| Teaser | yes | full-width 12px-radius figure with caption |
| Interactive 3D gallery | yes | carousel cards with 3D viewer, explode slider and behavior video (viewer still loading in the capture) |
| Abstract | yes | 820px narrow column |
| Method / dataset | yes | figures, two-column explainer, inline code, tinted dataset band |
| Results tables | yes | 14px table cards with tinted headers |
| Stats | yes | four stat cards with violet serif numbers |
| BibTeX | yes | dark block with copy pill |
| Footer | yes | #f3f0ea with 1px top rule, 13.5px muted text |

## Adapting to Other Content

- **More authors**: keep the left-aligned flex flow (gap 4px 16px) at 16px/500 with violet superscripts; it wraps naturally across the 1124px column.
- **A results table**: use `.table-wrap` (white, 1px #e3dfd5, 14px radius, small shadow) with the #f3f0ea header row; mark our row with rgba(111,92,214,0.05) and violet bold values.
- **Long publication or news lists**: render each item as a white 14px-radius card (1px #e3dfd5, padding 18px) with a Newsreader 20px/600 date or title in #6f5cd6 and 14.5px #303542 text, in the 820px narrow container.
- **Static results instead of 3D**: keep the gallery card frame and 4:3 12px-radius tiles on the cream viewer gradient so the carousel rhythm survives without WebGL.

## Do's and Don'ts

- Do keep the hero left-aligned with the wordmark and subtitle on one line.
- Do use the violet-to-jade gradient only on the wordmark, section underlines and the explode track.
- Do use black #1a1d24 pills for every primary action, never violet fills.
- Do keep surfaces cream and white with 1px #e3dfd5 lines; tinted bands fade in and out through the four-stop gradient.
- Don't use a sans for headings; titles are Newsreader 600.
- Don't round figures beyond 12px or cards beyond 14px.
- Don't ship the hero video without a poster frame; the capture shows how bare the empty player looks.

## Surfaces

Cream #fbfaf7 page with faint violet and jade radial washes behind the hero; #f3f0ea tinted bands that fade from and back to cream; white cards, tables and figure grounds; a cream-to-sand gradient inside 3D viewers; dark #0c0e14 video wells and a #14171f BibTeX block.

## Imagery

Clay-like, softly lit 3D assets in pastel part colours (lilac, mint, salmon, sky blue): a sea turtle with a castle shell, race cars, robots, treasure chests, shown exploded into parts with serif callout labels. Teaser and method figures are wide white-ground diagrams; the gallery adds interactive WebGL models and behavior videos.

## Layout

A left-aligned hero in a 1180px container, a narrow 820px video band, a full-width teaser figure, then Gallery, Abstract, Method, Dataset (tinted) and Results sections at 64px padding, ending with BibTeX and a tinted footer. About 11,100px tall.

## Agent Prompt Guide

Quick colors: page #fbfaf7, tint #f3f0ea, surface #ffffff, ink #1a1d24, ink-2 #303542, muted #6b7180, line #e3dfd5, violet #6f5cd6, indigo #4f3fbf, jade #2aa48a.

1. "Build a left-aligned hero on #fbfaf7 with radial-gradient(60% 90% at 12% 18%, rgba(111,92,214,0.08), transparent 70%) and radial-gradient(60% 90% at 88% 14%, rgba(42,164,138,0.07), transparent 70%). A white pill (1px #e3dfd5, radius 999px, padding 7px 14px, Inter 13px/500 #303542) with an 8px #6f5cd6 dot and a 4px rgba(111,92,214,0.15) halo. Title in Newsreader 64px/600, letter-spacing -0.02em: the name filled with linear-gradient(120deg, #6f5cd6 0%, #4f3fbf 50%, #2aa48a 100%) clipped to text, a #303542 colon, then a 36px/500 subtitle inline."
2. "Make black pill buttons: #1a1d24 fill, #fbfaf7 Inter 14.5px/500, radius 999px, padding 10px 18px, 18px line icon left with a 9px gap, shadow 0 1px 2px rgba(20,20,30,0.05), 0 4px 14px -8px rgba(20,20,30,0.12); hover #2c3140 and translateY(-1px)."
3. "Create a gallery card: white, 1px #e3dfd5, radius 14px, padding 22px; Inter 20px/600 title and italic 14.5px #303542 prompt; two 4:3 tiles with 12px radius, the left on linear-gradient(180deg, #f1eee6 0%, #e1dcce 100%) with a glass control bar (rgba(255,255,255,0.84), blur 8px, radius 999px) holding a 4px violet-to-jade slider and a black uppercase 12px/600 'Reset' pill."

## Similar Pages

- Product-grade 3D generation project pages with a gradient wordmark, interactive model viewers and an explode control.
- Cream-ground pages that pair a Newsreader or Source Serif display with Inter UI and black pill buttons.

## Quick Start

```css
:root {
  --bg: #fbfaf7;
  --bg-tint: #f3f0ea;
  --bg-soft: #ffffff;
  --ink: #1a1d24;
  --ink-2: #303542;
  --muted: #6b7180;
  --line: #e3dfd5;
  --line-strong: #c9c2b3;
  --accent: #6f5cd6;
  --accent-2: #2aa48a;
  --pill-bg: #1a1d24;
  --pill-fg: #fbfaf7;
  --code-bg: #14171f;
  --code-fg: #e8ecf5;
  --max-w: 1180px;
  --max-w-narrow: 820px;
  --radius: 14px;
  --shadow-sm: 0 1px 2px rgba(20, 20, 30, 0.05), 0 4px 14px -8px rgba(20, 20, 30, 0.12);
  --shadow-md: 0 2px 6px rgba(20, 20, 30, 0.06), 0 18px 40px -20px rgba(20, 20, 30, 0.25);
  --font-display: 'Newsreader', 'Inter', serif;
  --font-ui: 'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif;
}
```

## Provenance

- **URL**: https://cubepart.github.io/
- **Paper**: CubePart: An Open-Vocabulary Part-Controllable 3D Generator (arXiv 2605.28763), Yiheng Zhu, Kangle Deng, Jean-Philippe Fauconnier, Inaki Navarro, et al. (Roblox, Carnegie Mellon University, Stanford University).
- **Venue**: SIGGRAPH 2026 (Los Angeles), as listed in the arXiv comment.
- **Selection reason**: the arXiv comment lists the venue as SIGGRAPH 2026 without an explicit acceptance word and links this project page.
- **Template credit**: none stated; a custom build; footer reads "© 2026 The Authors" under a Creative Commons licence.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and tall screenshots, and `style.css` and `index.html` read directly, on 2026-10-28. The hero video and 3D viewer were blank or loading at capture time.
