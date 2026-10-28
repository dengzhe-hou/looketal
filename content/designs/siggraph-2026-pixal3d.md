# Pixal3D — Style Reference

> A midnight gallery of sculptures seen through smoked glass, with one indigo-to-violet neon sign over the door.

**Theme:** dark

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), a second probe of below-the-fold elements (section labels, video, result cards, citation box, glows), the 1440×900 and tall screenshots, and the inline `<style>` and markup of `index.html`. Sections and grids use a `.fade-in` class that starts at opacity 0 and rises 30px when scrolled into view (the results grid and citation box measured opacity 0 at load); values below are the settled state. The hero is `min-height: 100vh`, so in the tall capture it stretches to the full image height.

## Overview

A dark, product-launch style page on near-black #0a0a0f with zinc text (#e4e4e7, muted #a1a1aa) in Inter. Two fixed 600px blurred glows (indigo top-left, purple bottom-right, at 15% opacity) and a faint 60px indigo grid sit behind everything. The full-viewport hero lays the paper's teaser image (framed renders on a wall above a crowd of coloured 3D figures) across the background at 15% opacity, then centres an indigo badge ("SIGGRAPH" white, "2026" light indigo), a 72px/800 title whose "Pixal3D" line is filled with the `#6366f1 → #8b5cf6 → #a855f7` gradient, white author names, muted affiliations and six 58px buttons: one gradient "Paper" button with a glow, five dark card buttons. Below, sections live in an 80%-wide column with uppercase light-indigo labels: a 16px-radius video, a justified abstract, a three-column grid of input/3D-viewer cards, comparison rows of four cards with an indigo-tinted "Pixal3D" header, a method figure, and a citation card. The hero is long (a full 900px) before any content.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): near-black family #222129 / #111118 / #0e0e14 / #211927 / #17121c / #151821 / #0b0b10 together 93.5% (page, nav and the dimmed teaser image); muted violet-gray #5d596e 6.5% (the lighter dimmed renders and text). The gradient title and Paper button are too small to form clusters.

Anatomy in DOM order (desktop 1440px, centred):

1. **Fixed nav** (`nav`, 0–65px): rgba(10,10,15,0.8) with `backdrop-filter: blur(20px)`, 1px #27272a bottom border. `.nav-inner` max-width 80% (1152px) with 24px padding, height 64px. Logo "Pixal3D" Inter 24px/800, letter-spacing -0.02em, filled with the accent gradient (x=168). Links Video, Abstract, Results, Comparisons, Method, Citation at 14.4px/500 #a1a1aa, gap 32px, hover #e4e4e7.
2. **Hero** (`section.hero`, 0–900px): min-height 100vh, flex centred, padding 120px 24px 80px; `.hero::before` paints `url('assets/teaser.png') center top / cover no-repeat` at opacity 0.15. `.hero-content` max 1100px spans y=206–735.
3. **Badge** (`a.badge`, y=206, 201×50): inline-flex, gap 8px, padding 10px 24px, radius 100px, rgba(99,102,241,0.1) fill, 1px rgba(99,102,241,0.3) border, Inter 17.6px/700, letter-spacing 0.02em; "SIGGRAPH" 800 #ffffff, "2026" #818cf8. Gap 32px.
4. **Title** (`h1`, y=288, 238px, three lines): Inter 72px (clamp(2.5rem, 6vw, 4.5rem)) / 800 / 1.1, letter-spacing -0.03em, #e4e4e7; first line `span.gradient-text` "Pixal3D" filled with `linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7)`. Gap 24px.
5. **Authors** (`p.hero-authors`, y=549): 16.8px/400, line-height 1.8, links #e4e4e7 (hover #818cf8), superscripts 11.2px #818cf8. Gap 8px.
6. **Affiliations** (`p.hero-affiliations`, y=588): 14.4px #a1a1aa with #818cf8 superscripts. Gap 8px.
7. **Footnote** (`p.hero-footnote`, y=619): 13.6px italic #a1a1aa. Gap 36px.
8. **Buttons** (`.hero-buttons`, y=676, 58px tall, gap 16px): Paper (primary) then arXiv, 🤗 Demo, Model, Video, Code (secondary); Inter 15.2px/600, padding 14px 28px, radius 12px, 18px icons left with 8px gap. Primary: accent gradient fill, white text, `box-shadow: 0 4px 20px rgba(99, 102, 241, 0.3)`. Secondary: #13131a fill, 1px #27272a border, #e4e4e7 text.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Night | #0a0a0f | --bg | page, nav (80%) |
| Card | #13131a | --bg-card | secondary buttons, result cards, 3D viewer ground, citation box |
| Card Hover | #1a1a24 | --bg-card-hover | secondary button and feature-card hover |
| Well | #0d0d14 | (literal) | video ground, input-image wells, code block |
| Text | #e4e4e7 | --text | title, authors, headings, button labels |
| Muted | #a1a1aa | --text-muted | nav links, affiliations, footnote, abstract, captions, card labels, BibTeX |
| Border | #27272a | --border | nav and footer rules, button and card borders, figure borders |
| Indigo | #6366f1 | --primary | gradient start, glow 1, secondary button hover border, toggle on-state |
| Light Indigo | #818cf8 | --primary-light | badge year, section labels, superscripts, "Pixal3D" result label, links in footer |
| Violet | #8b5cf6 | (gradient stop) | accent gradient middle |
| Purple | #a855f7 | (gradient stop) | accent gradient end, glow 2 |
| Accent Gradient | linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7) | --accent-gradient | logo, title first line, Paper button, slider handles |
| Indigo Wash | rgba(99, 102, 241, 0.1) | (literal) | badge fill, feature icon tiles; 0.08 on the "Pixal3D" result label |
| White | #ffffff | (literal) | "SIGGRAPH" in the badge, primary button text |
| Close Red | rgba(239, 68, 68, 0.8) | (literal) | viewer close buttons |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| All text | 'Inter', -apple-system, BlinkMacSystemFont, sans-serif | Inter 400, 500, 600, 700, 800 | Geist |
| Code | 'JetBrains Mono', monospace | not loaded; system monospace | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1` | clamp(2.5rem, 6vw, 4.5rem) → 72px / 800 / 1.1, letter-spacing -0.03em | #e4e4e7, first line gradient |
| Logo | `.logo` | 1.5rem = 24px / 800, letter-spacing -0.02em | gradient |
| Badge | `.badge` | 1.1rem = 17.6px / 700 (SIGGRAPH 800), letter-spacing 0.02em | #ffffff / #818cf8 |
| Section label | `.section-label` | 1.05rem = 16.8px / 600 uppercase, letter-spacing 0.1em | #818cf8 |
| Section title | `.section-title` | clamp(1.3rem, 2.5vw, 1.8rem) → 28.8px / 700, letter-spacing -0.02em | #e4e4e7 |
| Body | `body` | 16px / 400 / 1.6 | #e4e4e7 |
| Abstract | `.abstract-text` | 1.05rem = 16.8px / 1.8, justified | #a1a1aa |
| Section description | `.section-desc` | 1.1rem = 17.6px / 1.7 | #a1a1aa |
| Authors | `.hero-authors` | 1.05rem = 16.8px / 1.8 | #e4e4e7 |
| Affiliations | `.hero-affiliations` | 0.9rem = 14.4px | #a1a1aa |
| Nav link | `.nav-links a` | 0.9rem = 14.4px / 500 | #a1a1aa |
| Button | `.btn` | 0.95rem = 15.2px / 600 | #ffffff / #e4e4e7 |
| Result label | `.result-label` | 0.85rem = 13.6px / 600 | #a1a1aa (ours #818cf8) |
| Caption | `.video-caption`, `.pipeline-caption` | 0.85rem italic | #a1a1aa |
| BibTeX | `.citation-box pre` | JetBrains Mono stack 0.85rem / 1.7 | #a1a1aa |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Badge | 100px | 1px rgba(99,102,241,0.3) | none; hover fill 0.2, border 0.5 |
| Buttons | 12px | secondary 1px #27272a | primary `0 4px 20px rgba(99, 102, 241, 0.3)`, hover `0 6px 30px rgba(99, 102, 241, 0.4)` and translateY(-2px) |
| Video, citation box, code block, comparison viewer, feature cards | 16px | 1px #27272a | none |
| Result and gallery cards | 14px | 1px #27272a | none |
| Method figure | 12px | 1px #27272a | none |
| Viewer chips (Load 3D, normal toggle, reset, expand) | 6px | 1px rgba(99,102,241,0.5) or #27272a | none |
| Split-slider handle | 50%, 26px (40px in comparisons) | none | `0 2px 8px rgba(99, 102, 241, 0.4)`; line `0 0 6px rgba(99, 102, 241, 0.4)` |

Background layers: `.bg-grid { background-image: linear-gradient(rgba(99, 102, 241, 0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(99, 102, 241, 0.03) 1px, transparent 1px); background-size: 60px 60px }` fixed; `.bg-glow` 600px circles with `filter: blur(120px)` at opacity 0.15, #6366f1 at top -200px left -100px and #a855f7 at bottom -200px right -100px.

## Layout Metrics

- **Container**: `section { max-width: 80%; margin: 0 auto; padding: 100px 24px }`, so sections are 1152px wide at x=144 with content x=168 to 1272 (1104px). The nav inner uses the same 80%.
- **Hero**: 900px tall (100vh), padding 120px 24px 80px, content vertically centred (y=206–735); badge→title 32px, title→authors 24px, footnote→buttons 36px.
- **Sections**: 100px top and bottom padding; label margin-bottom 12px; title margin-bottom 20px; description margin-bottom 60px.
- **Media**: video 100% (1104×622, max 1200px); method figure 1104px; citation box margin-top 40px, padding 32px.
- **Grids**: results gallery 3 columns of 355px, gap 20px, each card split into a square input well and a square 3D viewer; comparison rows 4 columns of 264px, gap 16px, rows 20px apart.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1200px | 24px inside 80% | 16px | 72px (6vw caps from 1200px) | 3-column results, 4-column comparisons |
| ≤1200px | 24px | 16px | 6vw ≈ 72px at 1200 | results 2 columns; comparisons 2 columns |
| ≤768px | 20px | 16px | 6vw, floor 40px from 667px | nav links hidden; hero padding 100px 20px 60px; sections 60px 20px; pipeline steps stack |
| ≤600px | 20px | 16px | 40px | results 1 column |
| ≤500px | 20px | 16px | 40px | comparisons 1 column |

## Components

- **Badge** (`.badge`): pill, padding 10px 24px, rgba(99,102,241,0.1), 1px rgba(99,102,241,0.3), Inter 17.6px/700; "SIGGRAPH" 800 white, "2026" #818cf8; margin-bottom 32px.
- **Gradient title**: 72px/800 Inter with the first line clipped to `linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7)` and the rest #e4e4e7.
- **Primary button** (`.btn-primary`): accent gradient fill, white 15.2px/600, padding 14px 28px, radius 12px, shadow `0 4px 20px rgba(99, 102, 241, 0.3)`; hover lifts 2px with `0 6px 30px rgba(99, 102, 241, 0.4)`.
- **Secondary button** (`.btn-secondary`): #13131a, 1px #27272a, #e4e4e7, same size; hover #1a1a24 with #6366f1 border.
- **Section header**: uppercase label 16.8px/600 #818cf8, letter-spacing 0.1em, then an optional 28.8px/700 title.
- **Result card** (`.results-gallery-item`): #13131a, 1px #27272a, radius 14px, two square cells: input image on #0d0d14 with a 1px right border, and a `<model-viewer>` with a wireframe/textured split slider (2px white line, 26px gradient handle), a "Load 3D" chip (rgba(99,102,241,0.8), 10.4px/600 white, radius 6px) top-right and a "Normal" switch chip top-left.
- **Comparison card** (`.result-item`): #13131a, 14px radius, 1px #27272a; 13.6px/600 #a1a1aa label strip with a 1px bottom rule; the "Pixal3D" strip uses #818cf8 on rgba(99,102,241,0.08).
- **Citation box** (`.citation-box`): #13131a, 1px #27272a, radius 16px, padding 32px, monospace 13.6px/1.7 #a1a1aa, pre-wrap.
- **Footer**: centred, padding 60px 24px, 1px #27272a top border, 13.6px #a1a1aa with #818cf8 links.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Fixed nav | yes | blurred near-black bar with gradient logo |
| Hero with background image | yes | full-viewport, teaser image at 15% opacity behind centred text |
| Venue badge | yes | indigo-tinted pill with two-tone text |
| Title / authors / affiliations | yes | 72px/800 with gradient first line; white authors; muted affiliations |
| Link buttons | yes | one gradient glow button + five dark card buttons |
| Video | yes | 16px-radius 1104px video on #0d0d14 |
| Abstract | yes | justified muted text under an uppercase label |
| Interactive 3D results | yes | 3-column input/viewer cards with load buttons and split sliders |
| Comparisons | yes | 4-column rows with an indigo "Pixal3D" header |
| Method | yes | framed figure with italic caption |
| Results tables | absent from the source | comparisons are visual |
| BibTeX | yes | dark 16px card |
| Footer | yes | centred muted line with top rule |

## Adapting to Other Content

- **More authors**: keep the single centred 16.8px line and let it wrap; at two lines or more, keep affiliations at 14.4px #a1a1aa and the 36px gap before the buttons.
- **A results table**: put it in a #13131a card with 1px #27272a and 14px radius; header 13.6px/600 uppercase #a1a1aa, cells 15.2px #e4e4e7, 1px #27272a row rules, our row on rgba(99,102,241,0.08) with #818cf8 text.
- **Long publication or news lists**: use #13131a cards (16px radius, padding 32px as in the citation box) with an uppercase 16.8px/600 #818cf8 date label and #a1a1aa body text, stacked 20px apart.
- **Shorter hero**: if the teaser image is busy, keep its opacity at 0.15 but reduce `min-height` rather than adding a scrim; the text already sits on near-black.

## Do's and Don'ts

- Do keep one gradient (`#6366f1 → #8b5cf6 → #a855f7`) and use it on the logo, the title's first line, the Paper button and slider handles.
- Do use #13131a cards with 1px #27272a borders and 12–16px radii for every container.
- Do keep body copy muted (#a1a1aa) and reserve #e4e4e7 for titles, names and button labels.
- Do keep the background layers subtle: 3% grid lines, 15% glows, 15% teaser image.
- Don't use pure white for body text or large surfaces.
- Don't add a second accent hue; status colours appear only on viewer chips (red close, green loaded).
- Don't add shadows to cards; only the primary button and slider handles glow.

## Surfaces

Near-black #0a0a0f page with a fixed 60px indigo grid and two blurred indigo/purple glows; the hero adds the teaser image at 15% opacity; #13131a cards and #0d0d14 media wells, all bordered with 1px #27272a; a translucent blurred nav.

## Imagery

Image-to-3D results: framed concept images on a wall and dense crowds of coloured 3D sculptures (characters, creatures, vehicles, buildings) in the hero; square input images beside interactive 3D models with wireframe/textured split views; side-by-side method comparisons. All media sit in dark cards with 12–16px radii.

## Layout

A 900px centred hero, then an 80%-wide (1152px) single column: Video, Abstract, Results (3-column grid), Comparisons (4-column rows), Method and Citation, each 100px padded, with a centred footer. About 8,150px tall.

## Agent Prompt Guide

Quick colors: page #0a0a0f, card #13131a, well #0d0d14, text #e4e4e7, muted #a1a1aa, border #27272a, indigo #6366f1, light indigo #818cf8, gradient linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7).

1. "Build a full-viewport centred hero on #0a0a0f with the teaser image as a ::before background at opacity 0.15. Badge: pill, padding 10px 24px, rgba(99,102,241,0.1), 1px rgba(99,102,241,0.3), Inter 17.6px/700, 'SIGGRAPH' white 800 and '2026' #818cf8. Title Inter 72px/800, line-height 1.1, letter-spacing -0.03em, #e4e4e7, with the method name on its own line filled by linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7) clipped to text."
2. "Make a button row, gap 16px: primary with the same gradient, white Inter 15.2px/600, padding 14px 28px, radius 12px, shadow 0 4px 20px rgba(99,102,241,0.3); secondary #13131a with 1px #27272a and #e4e4e7 text, hover #1a1a24 with a #6366f1 border."
3. "Create a results grid: 3 columns, gap 20px; each card #13131a, 1px #27272a, radius 14px, split into a square #0d0d14 input well and a square 3D viewer with a 'Load 3D' chip (rgba(99,102,241,0.8), white 10.4px/600, radius 6px). Above it an uppercase label 16.8px/600 #818cf8, letter-spacing 0.1em."

## Similar Pages

- Dark AI-product-style project pages with a gradient wordmark, glow buttons and a faint grid background.
- 3D generation pages that show results in interactive `<model-viewer>` cards with wireframe/texture sliders.

## Quick Start

```css
:root {
  --primary: #6366f1;
  --primary-light: #818cf8;
  --bg: #0a0a0f;
  --bg-card: #13131a;
  --bg-card-hover: #1a1a24;
  --well: #0d0d14;
  --text: #e4e4e7;
  --text-muted: #a1a1aa;
  --border: #27272a;
  --accent-gradient: linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7);
  --font: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --radius-btn: 12px;
  --radius-card: 16px;
  --section-max: 80%;
}
```

## Provenance

- **URL**: https://ldyang694.github.io/projects/pixal3d/
- **Paper**: Pixal3D: Pixel-Aligned 3D Generation from Images (arXiv 2605.10922), Dong-Yang Li, Wang Zhao, Yuxin Chen, Wenbo Hu, Meng-Hao Guo, Fang-Lue Zhang, Ying Shan, Shi-Min Hu (Tsinghua University, Tencent ARC Lab, Victoria University of Wellington).
- **Venue**: SIGGRAPH 2026 (as listed in the arXiv comment).
- **Selection reason**: the arXiv comment lists the venue as SIGGRAPH 2026 without an explicit acceptance word and links this project page.
- **Template credit**: none stated; a single-file custom build with `<model-viewer>`; footer reads "© 2026 Pixal3D."
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), an additional computed-style probe below the fold, the 1440×900 and tall screenshots, and the inline CSS and markup of `index.html` read directly, on 2026-10-28.
