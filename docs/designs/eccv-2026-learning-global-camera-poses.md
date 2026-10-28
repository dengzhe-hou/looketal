# VGPA Technical Plate — Style Reference

> A survey engineer's field plate: warm paper, a book-serif title, monospaced vermilion section stamps, and the same red as the camera frusta in every figure.

**Theme:** both

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, plus targeted probes of the masthead, cards, stats, steps, tabs and table), the 1440×900 shot and a full-page capture, and the page's own `static/css/style.css` and `index.html`. The page renders light by default and has a fixed moon toggle; dark values (and the OS dark preference) are listed separately. Thumbnails in the interactive and gallery grids load lazily, so the full-page capture shows some of them blank.

## Overview

A calm, centred research page (5,934px) on warm paper #faf9f6 with warm near-black ink #16150f. The masthead stacks a bordered mono "● ECCV 2026" stamp, a four-line Newsreader serif title at 49px/500, a "VGPA · View-Graph Pose Averaging" line with bold initials, 20px author names, a 15px affiliation and four 44px buttons (one filled ink, three outlined, the Code button dimmed with a "SOON" tag). Below come three white teaser cards with point-cloud renders and a vermilion "Explore in 3D" button, then sections separated by 1px #dedbd2 rules, each headed by an 18px IBM Plex Mono uppercase label in rust #9e2f1c. The abstract is set in Newsreader 18.5px in a 760px column; "At a glance" uses three tinted stat cards with serif numbers; the method has a white-ground diagram and four numbered step cards; quantitative results sit in a tabbed mono table with a vermilion-washed "VGPA (OURS)" column and ▸ markers on winning values; a thumbnail gallery opens a lightbox. One accent, frustum vermilion #b8371f, is used sparingly.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): paper #faf9f6 / #faf9f5 / #fcfcfa / #fcf9f7 / #faf9f7 / #f9f9f8 together 78.1%; white #ffffff 16.1% (teaser cards); warm gray #c1b8b3 5.7% (ink, point clouds and borders blended). Vermilion covers too little area to form its own cluster.

Anatomy in DOM order (desktop 1440px, everything centred):

1. **Theme toggle** (`button.theme-toggle`, fixed at x=1388, y=16): 36px circle, #faf9f6 fill, 1px #c6c2b6 border, 17px moon icon in #4f4d44.
2. **Masthead** (`header.masthead`, 0–623): padding 60px 0 44px, inside `.wrap` (max 1080px, padding 0 24px → content x 204–1236).
3. **Venue stamp** (`span.venue`, y=60, 145×42): IBM Plex Mono 16px/600 uppercase, letter-spacing .06em, #4f4d44 on #faf9f6, padding 7px 16px, 1px #c6c2b6 border, 3px radius, a 7px #b8371f dot 9px before the text. Gap 22px.
4. **Title** (`h1`, y=124, 587×245): Newsreader 49px/500, line-height 1.25, letter-spacing -0.02em, #16150f, max 20ch, four lines. Gap 16px.
5. **Method name** (`p.method-name`, y=385): 16px #4f4d44 with the V, G, P, A initials and "VGPA" in 600 #16150f. Gap 26px.
6. **Authors** (`.authors`, y≈437): 20px/400 #16150f links without underline, gaps 4px 20px; hover #b8371f with underline. Gap 10px.
7. **Affiliation** (`p.affil`, y=481): 15px #4f4d44. Gap 30px.
8. **Buttons** (`nav.links`, y=536, 44px tall, 10px gaps): "Paper" filled #16150f with #faf9f6 text; "arXiv", "Code", "BibTeX" outlined (#faf9f6 fill, 1px #c6c2b6 border, #16150f text); all 14.5px/500, padding 9px 16px, 4px radius, 16px filled icons left. "Code" at opacity .55 with a 10px/600 uppercase "SOON" tag. Masthead ends at y=623.
9. **Teaser** (`section.teaser`, padding-top 8px; cards from y=631): three 333×373 white cards (gap 16px), 1px #dedbd2 border, 4px radius; 300px-tall contained render; "Explore in 3D" button 14px from the stage bottom; caption strip below. The caption paragraph (14px #4f4d44, max 76ch) sits under the cards at y=1020.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #faf9f6 | --surface-0 | page background, venue stamp fill, outline buttons, table header cells, selected tab, button text on ink |
| Card Tint | #f2f1ec | --surface-1 | stat cards, step cards, figure caption strips, tab track, BibTeX block |
| Well | #e8e6df | --surface-2 | wells and chart tracks |
| Border | #dedbd2 | --border | section rules, card and figure borders, table row rules, footer rule |
| Border Strong | #c6c2b6 | --border-strong | venue stamp, outline buttons, theme toggle, copy button, table column separators |
| Ink | #16150f | --text-primary | title, authors, abstract, stat numbers, filled button fill, scene names, winning values |
| Ink Secondary | #4f4d44 | --text-secondary | venue text, method line, affiliation, captions, section intros, table numbers, tabs |
| Ink Muted | #7a776c | --text-muted | footer, table notes |
| Frustum Vermilion | #b8371f | --accent | venue dot, "Explore in 3D" buttons, step number rings, ▸ win markers, tile hover border, focus outline, author hover |
| Rust Ink | #9e2f1c | --accent-ink | section labels (h2), "VGPA (OURS)" group header, links, step numbers, Explore button hover |
| Accent Soft | #f6e9e4 | --accent-soft | soft accent wash |
| Ours Column | color-mix(in srgb, #b8371f 6%, transparent) | (literal) | VGPA columns in tables (9% on even rows) |
| Figure White | #ffffff | --figure-bg | teaser cards, interactive stages, gallery tiles |
| Series Other | #8a8a83 | --series-other | non-ours methods in charts |
| Dark Paper | #141412 | --surface-0 (dark) | page background in dark mode |
| Dark Card | #1c1c1a | --surface-1 (dark) | cards in dark mode |
| Dark Ink | #f3f1ea | --text-primary (dark) | text in dark mode |
| Dark Accent | #dd6d56 | --accent (dark) | accent in dark mode; links #e89179 |
| Diagram Plate | #f4f3ee | (literal, dark mode only) | light plate behind the transparent method diagram in dark mode |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display serif | "Newsreader", "Iowan Old Style", Charter, Georgia, serif | Newsreader 400, 500 | Source Serif 4 |
| Sans | "IBM Plex Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif | IBM Plex Sans 400, 500, 600 | IBM Plex Sans |
| Mono | "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace | IBM Plex Mono 400, 500 (600 is synthesized for labels) | IBM Plex Mono |

| Role | Selector | Size / weight / line-height / tracking | Color |
|---|---|---|---|
| Title | `.masthead h1` | clamp(31px, 4.7vw, 49px) → 49px / 500 / 1.25 / -0.02em, max 20ch | #16150f |
| Section label | `.section-head h2` | Plex Mono 18px / 600 / 1.25 / .1em uppercase | #9e2f1c |
| Section intro | `.section-head p` | 15px / 1.65, max 68ch | #4f4d44 |
| Abstract | `.abstract p` | Newsreader 18.5px / 400 / 1.7 | #16150f |
| Body | `body` | 16px / 400 / 1.65 | #16150f |
| Venue stamp | `.venue` | Plex Mono 16px / 600 / .06em uppercase | #4f4d44 |
| Authors | `.authors` | 20px / 400 | #16150f |
| Affiliation | `.affil` | 15px | #4f4d44 |
| Button | `.btn` | 14.5px / 500 | #faf9f6 or #16150f |
| Stat number | `.stat .num` | Newsreader 34px / 500 / 1.1 / -0.03em (word variant 27px) | #16150f |
| Stat label | `.stat .lbl` | 13.5px | #4f4d44 |
| Step title | `.step h3` | 15px / 600 | #16150f |
| Step text | `.step p` | 14px | #4f4d44 |
| Tab | `.tab` | 13.5px / 500 | #4f4d44, selected #16150f |
| Table | `table` | Plex Mono 12.5px tabular; scene column Plex Sans 500 | #4f4d44, scene #16150f |
| Group header | `thead th.grp` | 11px / 600 / .04em uppercase | #4f4d44, ours #9e2f1c |
| Caption | `.fig figcaption`, `.caption` | 13px / 14px | #4f4d44 |
| BibTeX | `.code-block pre` | Plex Mono 13px / 1.6 | #4f4d44 |
| Footer | `footer` | 13.5px | #7a776c |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow / effect |
|---|---|---|---|
| Buttons | 4px | 1px transparent (filled) or #c6c2b6 | hover translateY(-1px), opacity .88 |
| Venue stamp, tabs, Explore button, tiles, copy button | 3px | stamp/copy 1px #c6c2b6; tiles 1px #dedbd2 | tile hover: border #b8371f, translateY(-2px) |
| Figures, stat and step cards, table wrapper, BibTeX | 4px | 1px #dedbd2 | none |
| Selected tab | 3px | none | `0 1px 3px rgba(0,0,0,.1)` |
| Theme toggle, step number rings | 50% | 1px #c6c2b6 / 1px #b8371f | none |
| Lightbox | 4px figure on a scrim | close button 1px rgba(255,255,255,.3) | scrim rgba(8,8,8,.86) with `backdrop-filter: blur(3px)` |

## Layout Metrics

- **Container**: `.wrap { max-width: 1080px; margin: 0 auto; padding: 0 24px }` → content x 204–1236 (1032px) at 1440; `.wrap--narrow` 760px (abstract and BibTeX, content 712px at x=364).
- **Masthead**: padding 60px 0 44px; vertical chain 42 (stamp) + 22 + 245 (title) + 16 + 26 + 26 + ~33 (authors) + 10 + 25 + 30 + 44 = 563px of content between y=60 and y=580.
- **Sections**: padding 56px 0 with a 1px #dedbd2 top rule (none on the first); section head margin-bottom 28px; intro 8px below the label.
- **Teaser**: padding-top 8px; grid repeat(auto-fit, minmax(320px, 1fr)), gap 16px → three 333px cards; stage height 300px; caption strip padding 10px 14px.
- **Interactive grid**: auto-fit minmax(320px, 1fr), gap 22px, stages aspect 560/380.
- **Highlights**: auto-fit minmax(200px, 1fr), gap 14px; cards padding 20px. Steps: auto-fit minmax(220px, 1fr), gap 14px, padding 18px, margin-top 24px.
- **Table**: wrapper 1px #dedbd2, 4px radius, horizontal scroll; th padding 9px 12px, td 8px 12px; even rows a 4% ink wash; mean row (tfoot) 600 on a 6% ink wash with a 1px #c6c2b6 top rule.
- **Gallery**: auto-fill minmax(190px, 1fr), gap 12px, image height 150px.
- **Footer**: padding 40px 0 60px, 1px #dedbd2 top.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| base (1440) | 24px inside 1080px | 16px | 49px | 3 teaser cards, 3 stats, 4 steps, 5 gallery columns |
| ≤1042px (4.7vw < 49px) | 24px | 16px | 4.7vw, e.g. 45px at 960 | auto-fit grids drop columns as widths fall below their minimums |
| ≤700px | 24px | 16px | 32.9px at 700 | teaser stage and level images 220px tall |
| ≤640px | 24px | 16px | 31px floor (reached at 660px) | sections padding 40px; masthead 40px 0 32px; gallery minmax(150px), tile images 118px |

## Components

- **Venue stamp** (`.venue`): inline-flex, gap 9px, padding 7px 16px, 1px #c6c2b6 border, 3px radius, #faf9f6 fill, IBM Plex Mono 16px/600 uppercase .06em #4f4d44, 7px #b8371f dot first.
- **Filled button** (`.btn`): padding 9px 16px, 4px radius, #16150f fill, #faf9f6 14.5px/500 text, 16px filled icon left with 8px gap; hover translateY(-1px), opacity .88.
- **Outline button** (`.btn--ghost`): #faf9f6 fill, 1px #c6c2b6 border, #16150f text; hover border #7a776c. Placeholder state: opacity .55, not-allowed cursor, a 10px/600 uppercase "soon" tag with padding 1px 5px, 4px radius, `color-mix(in srgb, currentColor 18%, transparent)` fill.
- **Explore card** (`.fig.fig--level.recon`): white, 1px #dedbd2, 4px radius; 300px contained point-cloud poster; "Explore in 3D" button centred 14px from the stage bottom: 13.5px/500 #faf9f6 on #b8371f, padding 9px 18px, 3px radius, hover #9e2f1c; caption strip #f2f1ec with a 1px #dedbd2 top border, padding 10px 14px, 13.5px #4f4d44 with bold scene id and camera count. Once live, small outlined control buttons (12.5px, padding 6px 11px, 3px radius) sit along the stage bottom.
- **Section label** (`.section-head h2`): IBM Plex Mono 18px/600 uppercase, .1em tracking, #9e2f1c; optional 15px #4f4d44 intro 8px below, max 68ch.
- **Stat card** (`.stat`): #f2f1ec, 1px #dedbd2, 4px radius, padding 20px; Newsreader 34px/500 number (unit in 16px), 13.5px #4f4d44 label 6px below.
- **Step card** (`.step`): #f2f1ec, 1px #dedbd2, 4px radius, padding 18px; a 22px circle with 1px #b8371f border holding an 11.5px/500 mono counter in #9e2f1c, 10px above a 15px/600 title and 14px #4f4d44 text.
- **Segmented tabs** (`.tabs`): fit-content track #f2f1ec, 1px #dedbd2, 4px radius, padding 4px, 6px gaps; tabs 13.5px/500 #4f4d44, padding 6px 14px, 3px radius; selected #faf9f6 fill, #16150f text, shadow `0 1px 3px rgba(0,0,0,.1)`.
- **Results table**: IBM Plex Mono 12.5px tabular, right-aligned; sticky #faf9f6 header cells 600 #4f4d44 with 1px #dedbd2 bottom; group headers 11px uppercase (ours in #9e2f1c); method groups split by 1px #c6c2b6 left rules (a 3px double rule between learned and classical); ours columns washed 6% vermilion; winning cells 600 #16150f with a 10px #b8371f "▸" after.
- **BibTeX** (`.code-block`): #f2f1ec pre, 1px #dedbd2, 4px radius, padding 18px 20px, mono 13px/1.6 #4f4d44; "Copy" button top-right 12px/500, padding 5px 11px, 1px #c6c2b6, 3px radius, #faf9f6 fill.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Theme toggle | yes | fixed 36px circle top-right |
| Venue badge | yes | bordered mono stamp with vermilion dot |
| Title / authors / affiliation | yes | centred serif title, 20px names, one institution |
| Link buttons | yes | one filled, three outlined, placeholder "SOON" state |
| Interactive 3D teaser | yes | three white cards with vermilion Explore buttons |
| Abstract | yes | Newsreader 18.5px in a 760px column |
| Stats | yes | three tinted cards with serif numbers |
| Method figure and steps | yes | transparent line-art diagram plus four numbered cards |
| Results table | yes | tabbed mono tables with ours-column wash and ▸ markers |
| Gallery with lightbox | yes | white thumbnail tiles, zoom-in cursor, dark scrim lightbox |
| Video | absent from the source | interaction comes from WebGL point-cloud viewers instead |
| BibTeX | yes | tinted mono block with copy button |
| Footer | yes | acknowledgement paragraph in muted 13.5px |

## Adapting to Other Content

- **More authors**: keep the centred flex-wrap at 20px with gaps 4px 20px; add a second affiliation line in 15px #4f4d44 rather than superscript-heavy markup.
- **A results table**: reuse the mono table: 12.5px tabular, 8px 12px cells, even-row 4% ink wash, the ours column at 6% vermilion, winning values 600 #16150f with a #b8371f "▸"; wrap it in the 1px #dedbd2, 4px-radius scroll container at full 1032px width.
- **Long publication or news lists**: use step-card styling (#f2f1ec, 1px #dedbd2, 4px radius, 18px padding) or plain rows with 1px #dedbd2 rules; dates in IBM Plex Mono 12.5px #4f4d44.
- **More sections**: open each with an 18px mono uppercase #9e2f1c label and a 15px intro; separate sections with the 1px #dedbd2 top rule and 56px padding.
- **Video**: put it in a white `.fig` card (1px #dedbd2, 4px radius) with a #f2f1ec caption strip, matching the teaser cards.

## Do's and Don'ts

- Do keep vermilion #b8371f for things that mean "ours" or "act here": camera frusta, Explore buttons, win markers, step rings.
- Do set display text in Newsreader (title, abstract, stat numbers) and labels in IBM Plex Mono.
- Do keep radii small (3–4px) and borders warm (#dedbd2, #c6c2b6).
- Do keep figures on white cards against the warm paper ground.
- Don't introduce a second accent; other methods use neutral #8a8a83.
- Don't use shadows except the 1px-3px selected-tab lift.
- Don't left-align the masthead; it is fully centred, while sections below are left-aligned in the 1032px column.

## Surfaces

Warm paper #faf9f6 page; tinted #f2f1ec cards, caption strips, tab tracks and code; pure white #ffffff only for figure grounds; table even rows at a 4% ink wash and the mean row at 6%. Dark mode swaps to #141412 / #1c1c1a with #f3f1ea text and a lighter #dd6d56 accent, and gives the transparent method diagram a #f4f3ee plate.

## Imagery

Sparse gray point clouds with red camera frusta on white, rendered interactively on demand; a colorful method diagram (photos, graph nodes in orange, a salmon GNN block and a blue BA block); a grid of reconstruction thumbnails that open in a lightbox.

## Layout

Centred masthead, then a left-aligned 1032px column (760px for the abstract and BibTeX) with sections separated by full-width hairlines and 56px padding. Grids are auto-fit, so module column counts come from minimum widths (320px, 220px, 200px, 190px) rather than breakpoints.

## Agent Prompt Guide

Quick colors: paper #faf9f6, card #f2f1ec, border #dedbd2, strong border #c6c2b6, ink #16150f, secondary #4f4d44, muted #7a776c, vermilion #b8371f, rust #9e2f1c, figure white #ffffff.

1. "Build a centred masthead on #faf9f6, padding 60px 0 44px: a mono stamp (IBM Plex Mono 16px/600 uppercase, .06em, #4f4d44, padding 7px 16px, 1px #c6c2b6 border, 3px radius, 7px #b8371f dot), then a Newsreader 49px/500 title (line-height 1.25, -0.02em, #16150f, max 20ch) 22px below, a 16px #4f4d44 method line, 20px authors, a 15px affiliation, and 44px buttons (padding 9px 16px, 4px radius, 14.5px/500): one #16150f with #faf9f6 text, the rest #faf9f6 with a 1px #c6c2b6 border."
2. "Make section labels and stat cards: label IBM Plex Mono 18px/600 uppercase, letter-spacing .1em, #9e2f1c, with a 15px #4f4d44 intro 8px below; sections padding 56px 0 with a 1px #dedbd2 top rule. Stat cards: #f2f1ec, 1px #dedbd2, 4px radius, padding 20px, Newsreader 34px/500 number, 13.5px #4f4d44 label."
3. "Create a results table: IBM Plex Mono 12.5px tabular, right-aligned; header cells #faf9f6, 600 #4f4d44, 9px 12px padding, 1px #dedbd2 bottom; body cells 8px 12px; even rows a 4% #16150f wash; ours columns color-mix(in srgb, #b8371f 6%, transparent); winners 600 #16150f followed by a 10px #b8371f '▸'."

## Similar Pages

- Warm-paper academic pages pairing a book serif with IBM Plex for technical labels.
- Structure-from-motion and 3D reconstruction pages with on-demand WebGL viewers in figure cards.

## Quick Start

```css
:root {
  --surface-0: #faf9f6;
  --surface-1: #f2f1ec;
  --surface-2: #e8e6df;
  --border: #dedbd2;
  --border-strong: #c6c2b6;
  --text-primary: #16150f;
  --text-secondary: #4f4d44;
  --text-muted: #7a776c;
  --accent: #b8371f;
  --accent-ink: #9e2f1c;
  --accent-soft: #f6e9e4;
  --series-other: #8a8a83;
  --figure-bg: #ffffff;
  --radius: 4px;
  --radius-sm: 3px;
  --maxw: 1080px;
  --font-display: "Newsreader", "Iowan Old Style", Charter, Georgia, serif;
  --font-sans: "IBM Plex Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;
}
:root[data-theme="dark"] {
  --surface-0: #141412;
  --surface-1: #1c1c1a;
  --text-primary: #f3f1ea;
  --accent: #dd6d56;
  --accent-ink: #e89179;
}
```

## Provenance

- **URL**: https://vgpa-sfm.github.io/
- **Paper**: Learning Global Camera Poses from Noisy View-Graphs for Structure from Motion (arXiv 2609.09491), Fadi Khatib, Meirav Galun, Ronen Basri (Weizmann Institute of Science).
- **Venue**: ECCV 2026.
- **Selection reason**: the arXiv comment states acceptance at ECCV 2026 and links this project page.
- **Template credit**: none stated; a custom build whose stylesheet calls its palette a "technical plate".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted probes of masthead, cards, stats, steps, tabs and table, the 1440×900 shot and a full-page capture, and the page's `style.css` and `index.html` read directly, on 2026-10-28.
