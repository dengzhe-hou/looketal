# RenderFormer — Style Reference

> A product launch for a renderer: an 80px cobalt wordmark, a block of black buttons, and a 3×3 wall of Cornell boxes doing the talking.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's own Next.js stylesheet (`_next/static/css/bb47472caea334b1.css`) and `index.html`. The stylesheet declares `--font-sans: "Manrope", sans-serif`, but no `@font-face` or font link loads Manrope, so `document.fonts` reports nothing loaded and every line renders in the browser's default sans-serif (Arial on Windows). The sizes and weights below are what that fallback renders.

## Overview

A white, commercial-feeling project page built as a static Next.js export. A fixed 71px white bar holds a square logo mark on the left and five bold anchor links on the right. The hero is a two-column grid: on the left an 80px/800 cobalt (#2f6dd1) "RenderFormer" wordmark, a 28.8px/600 black subtitle on two lines, a flat cobalt "SIGGRAPH 2025" block badge, bold author names with superscripts, gray affiliations and two rows of square-cornered black buttons with 18px icons; on the right a 640×640 3×3 grid of rendered scenes with a 1px #e0e0e0 border. Below, sections sit in a 1000px column with 48px/800 cobalt section titles, 28.8px/700 black subsection titles, an animated scene illustration, an architecture diagram, a three-column gallery of bordered cards with light-gray caption bars, the same grid for 16 videos, and a BibTeX block with a cobalt copy button. Corners are square everywhere except the BibTeX box and copy button (4px).

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 57.0% (plus #fdffff and #fffffc 1.9%); near-black #000101 12.8% (the six button blocks and black render backgrounds); render-grid tones #37282a 9.9%, #616f73 7.8%, #adb1aa 7.7%, #dee1e1 2.9%. The cobalt wordmark and badge cover too little area to form their own cluster.

Anatomy in DOM order (desktop 1440px):

1. **Fixed top bar** (`nav.top-nav`, 0–71px): rgba(255,255,255,0.95), 1px solid #e0e0e0 bottom border; inner `.nav-content` max-width 1400px, padding 15px 30px. Logo image 40×40 at x=50, y=15. Links "Introduction · Gallery · Videos · BibTeX · More Research" 16px/600 #000000, 30px apart, right-aligned (first at x=902, last ends at x=1390). "More Research" is a hover dropdown.
2. **Hero** (`header.main-header`, 0–840px): padding 120px 30px 80px, max-width 1400px (x=20–1420). Inside, `.header-grid` two equal columns, 60px gap, vertically centred; the left text column is capped at 600px.
3. **Wordmark** (`h1.main-title`, y=153, 80px tall): 80px/800, line-height 1, letter-spacing -1.6px, #2f6dd1 (from `span.title-highlight`). Gap 20px.
4. **Subtitle** (`h2.subtitle`, y=253, 75px, two lines): 28.8px/600, line-height 1.3, letter-spacing -0.288px, #000000. Gap 30px.
5. **Venue badge** (`.conference-badge`, y=357, 168×42): "SIGGRAPH 2025" 16px/600 white on #2f6dd1, line-height 42px, padding 0 16px, letter-spacing 0.8px, square corners. Gap 30px.
6. **Authors** (`.authors-list`, y=429, 29px): 16px/600 #000000 names with superscript numbers, flex-wrapped 15px apart; hover underline. Gap 20px.
7. **Affiliations** (y=478, 512, 546): three lines 16px/400 #666666, 5px apart. Gap 30px.
8. **Buttons** (`.cta-button`, y=605 and y=674, 54px tall): row one arXiv, Paper, Code, Model; row two Talk, Poster, Slides; 15px gaps in both directions. Black #000000 fill, 2px solid #000000 border, white 16px/600 text, padding 12px 24px, square corners, 18px react-icons SVG on the left with 10px gap.
9. **Teaser grid** (`img.header-image`, x=750, y=120, 640×640): a single 3×3 composite image of nine renders, 1px solid #e0e0e0 border.

The Introduction section begins at y=840; its title sits at y=920.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper White | #ffffff | --background-color | page background, footer, button text, badge text, copy-button text |
| Ink Black | #000000 | --primary-color | body text, subtitle, subsection titles, author names, nav links, button fills and borders |
| Render Cobalt | #2f6dd1 | --accent-color | wordmark, venue badge, section titles, link hover color, nav-link hover underline, gallery source links, copy button |
| Cobalt Pressed | #2160c4 | (literal) | copy button hover |
| Slate Gray | #666666 | --dark-gray | affiliations, gallery and video source lines |
| Hairline | #e0e0e0 | --medium-gray | top-bar bottom border, teaser-image border, gallery and video card borders, footer top border |
| Caption Gray | #f4f4f4 | --light-gray | gallery and video caption bars, dropdown item hover |
| BibTeX Well | #f8f9fa | (literal) | BibTeX container |
| BibTeX Border | #e2e8f0 | (literal) | BibTeX container border |
| Code Ink | #24292e | (literal) | BibTeX text |
| Nav Glass | rgba(255,255,255,0.95) | (literal) | fixed top bar |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans | "Manrope", sans-serif (`--font-sans`) | nothing loaded; browser default sans-serif renders (Arial on Windows, Helvetica on macOS) | Arial |
| Mono | "IBM Plex Mono", monospace (`--font-mono`) | not loaded; default monospace (Consolas/Courier New) | IBM Plex Mono |

Arial is the right substitute because it is what visitors without Manrope installed actually see; loading Manrope would change the look to a rounder, narrower geometric face.

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Wordmark | `.main-title .title-highlight` | 80px (5rem) / 800 / 1, letter-spacing -0.02em | #2f6dd1 |
| Subtitle | `.subtitle` | 28.8px (1.8rem) / 600 / 1.3, letter-spacing -0.01em | #000000 |
| Section title | `.section-title` | 48px (3rem) / 800 / 1.6, letter-spacing -0.02em | #2f6dd1 |
| Subsection title | `.subsection-title` | 28.8px / 700 / 1.6, letter-spacing -0.01em | #000000 |
| Lead paragraph | `.abstract-content` | 17.6px (1.1rem) / 400 / 1.6 | #000000 |
| Body | `body`, `p` | 16px / 400 / 1.6 | #000000 |
| Venue badge | `.conference-badge` | 16px / 600 / 42px, letter-spacing 0.05em | #ffffff |
| Author | `.author` | 16px / 600 | #000000 |
| Affiliation | `.affiliation` | 16px / 400 | #666666 |
| Nav link | `.nav-links a` | 16px / 600 | #000000 |
| Button | `.cta-button` | 16px / 600 | #ffffff |
| Card caption | `.gallery-caption`, `.video-caption` | 16px / 500, centred | #000000 |
| Card source | `.gallery-source` | 13.6px (0.85rem) italic | #666666, links #2f6dd1 |
| BibTeX | `.bibtex-code` | 15px / 400 / 1.6 monospace | #24292e |
| Copy button | `.copy-button` | 14px / 500 | #ffffff |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Buttons, badge, logo, cards, teaser image | 0px (`--border-radius: 0px`) | buttons 2px solid #000000; cards and teaser 1px solid #e0e0e0 | none |
| BibTeX container | 4px | 1px solid #e2e8f0; focus border #2f6dd1 | focus 0 0 0 2px rgba(47,109,209,.2) |
| Copy button | 4px | none | none |
| Dropdown menu | 0px | none | 0 5px 15px rgba(0,0,0,.1) |
| Top bar | 0px | bottom 1px solid #e0e0e0 | none |

Nav links get a 2px underline bar 5px below the text on hover (`.nav-links a:after`, background #2f6dd1).

## Layout Metrics

- **Header container**: `.main-header { max-width: 1400px; margin: 0 auto; padding: 120px 30px 80px }` → content x=50–1390 at 1440.
- **Hero grid**: `.header-grid { grid-template-columns: 1fr 1fr; gap: 60px; align-items: center }` → two 640px columns; text column `.title-area` max-width 600px; teaser image 640×640 at x=750.
- **Hero vertical sum**: 120 padding → grid top 120; image 640 tall → grid bottom 760; 80 padding → header bottom 840. The text column (y=153–659) is centred against the image.
- **Sections**: `.section { padding: 80px 30px; max-width: 1400px }` wrapping `.section-container { max-width: 1000px; margin: 0 auto }` → text column x=220–1220. Consecutive sections are 160px apart (80 + 80). Section title margin-bottom 40px; subsection title margin-bottom 30px; lead paragraph margin-bottom 40px.
- **Card grids**: `.gallery-grid` and `.videos-grid` repeat(3, 1fr) with 30px gap → 313px cards; gallery grid margin-top 40px; video subsections 60px apart.
- **Description text**: `.gallery-description`, `.videos-description` max-width 800px, 17.6px.
- **BibTeX**: container padding 25px 30px, copy button absolute at top 10px / right 10px, padding 8px 12px.
- **Footer**: padding 40px 30px, 1px #e0e0e0 top border, centred links 30px apart.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1024px | header 30px inside 1400px; sections 30px | 16px | 80px | hero two columns; card grids 3 columns |
| ≤1024px | same | 16px | 64px (4rem) | hero one column, 40px gap; text column full width; card grids 2 columns |
| ≤768px | nav 15px 20px; header 100px 20px 60px; sections 60px 20px | 16px | 48px; subtitle 24px; section title 40px | card grids 1 column; nav links 20px apart |
| ≤480px | same | 16px | 40px; subtitle 19.2px; section title 32px | authors stack 10px apart; footer links stack |

## Components

- **Wordmark**: the acronym alone as h1, 80px/800, line-height 1, letter-spacing -0.02em, #2f6dd1; the full paper title follows as a separate 28.8px/600 black h2.
- **Venue badge** (`.conference-badge`): inline-block, height 42px, line-height 42px, padding 0 16px, #2f6dd1 fill, white 16px/600 text, letter-spacing 0.05em, square corners, margin-bottom 30px.
- **Black button** (`.cta-button`): inline-flex, gap 10px, padding 12px 24px, #000000 fill, 2px solid #000000 border, white 16px/600 text, square corners, 18px filled SVG icon on the left (react-icons: X logo for arXiv, file, GitHub, model, YouTube, poster, presentation). Hover: background transparent, text #000000, so the button becomes an outline.
- **Nav link**: 16px/600 #000000; hover text #2f6dd1 plus a 2px #2f6dd1 bar 5px under the text.
- **Gallery / video card** (`.gallery-item`): 1px solid #e0e0e0, square corners, image full width on top, then a #f4f4f4 caption bar holding a 16px/500 centred caption (padding 15px) and a 13.6px italic #666666 source line with #2f6dd1 links.
- **BibTeX block**: #f8f9fa well, 1px solid #e2e8f0, 4px radius, padding 25px 30px, 15px monospace #24292e; copy button top-right #2f6dd1 fill, white 14px/500, 4px radius, padding 8px 12px, hover #2160c4.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Fixed top nav | yes | translucent white bar, logo left, bold links right, "More Research" dropdown |
| Title / subtitle | yes | cobalt 80px wordmark plus black 28.8px subtitle |
| Venue badge | yes | flat cobalt block |
| Authors / affiliations | yes | bold black names, gray affiliation lines, left-aligned |
| Link buttons | yes | seven square black buttons with icons in two rows |
| Teaser | yes | 640px 3×3 render grid, right column of the hero |
| Abstract | present but non-standard | headed "Introduction"; one 17.6px lead paragraph |
| Method figures | yes | animated scene illustration and architecture diagram, full 1000px width |
| Image gallery | yes | three-column bordered cards with gray caption bars |
| Video grid | yes | same card recipe for 16 videos under subsection titles |
| Results tables | absent from the source | results are shown as renders and videos only |
| BibTeX | yes | gray well with cobalt copy button |
| Footer | yes | Microsoft legal links, centred, 1px top rule |

## Adapting to Other Content

- **More authors**: keep the flex-wrap row at 16px/600 with 15px gaps; at about eight names it wraps to a second line inside the 600px column. Keep affiliations one per line at 16px #666666.
- **A results table**: place it in the 1000px section column under a 28.8px/700 subsection title; header row #f4f4f4 with 16px/600 #000000 text, 1px solid #e0e0e0 cell borders, square corners, best value in #2f6dd1 600.
- **Long publication or news lists**: use the card recipe in the 3-column grid (313px wide at 1440) with the date as the caption bar's 13.6px italic #666666 line, or a plain list at 16px with 1px #e0e0e0 separators.
- **More links**: add more black buttons; the row wraps with 15px gaps, so keep at most four per row inside the 600px text column.
- **No teaser image**: keep the two-column grid and put a 640px square video or figure on the right; the layout depends on that square.

## Do's and Don'ts

- Do keep every corner square except the BibTeX block and copy button.
- Do reserve #2f6dd1 for the wordmark, the badge, section titles and hover states; body text stays #000000.
- Do keep buttons solid black with white text and invert to outline on hover.
- Do let the hero teaser be one square image with a 1px #e0e0e0 border, not a carousel.
- Don't add shadows to cards or buttons; separation comes from 1px #e0e0e0 lines and #f4f4f4 caption bars.
- Don't centre the hero text; it is left-aligned against the right-hand image.
- Don't set section titles in black; the cobalt 48px/800 titles are the page's rhythm.

## Surfaces

Pure white page and footer; a 95%-opaque white fixed bar; #f4f4f4 only in card caption bars; #f8f9fa only in the BibTeX well. Solid black appears as button blocks and inside the renders themselves.

## Imagery

Physically based renders of Cornell boxes, glossy objects, crystals and low-poly scenes on black or gray grounds, shown as a 3×3 composite in the hero and as square-cornered cards in three-column grids. Method figures are a line-drawn animated scene and a pastel boxed architecture diagram on white.

## Layout

A full-width hero split 50/50 between a left-aligned title block and a square teaser, followed by four 1000px-wide sections (Introduction, Rendering Gallery, Videos, BibTeX) separated by 160px of padding, and a centred footer.

## Agent Prompt Guide

Quick colors: background #ffffff, text #000000, accent #2f6dd1, muted #666666, hairline #e0e0e0, caption bar #f4f4f4, BibTeX well #f8f9fa.

1. "Build a two-column hero (max-width 1400px, padding 120px 30px 80px, grid 1fr 1fr, gap 60px, items centred). Left column max 600px: h1 80px/800 line-height 1 letter-spacing -0.02em #2f6dd1; h2 subtitle 28.8px/600 #000000; a 42px-tall #2f6dd1 badge with white 16px/600 text, padding 0 16px, square corners; bold author names 16px/600; affiliations 16px #666666. Right column: a 640px square image with 1px solid #e0e0e0 border."
2. "Make black buttons: inline-flex, gap 10px, padding 12px 24px, background #000000, 2px solid #000000 border, white 16px/600 text, 0 radius, 18px icon on the left; hover background transparent and text #000000. Rows wrap with 15px gaps."
3. "Create a three-column card grid (gap 30px, inside a 1000px column): each card 1px solid #e0e0e0, square corners, image on top, then a #f4f4f4 caption bar with a centred 16px/500 #000000 caption (padding 15px) and a 13.6px italic #666666 source line with #2f6dd1 links. Section titles above it 48px/800 #2f6dd1."

## Similar Pages

- Corporate-lab project pages built as one-off React or Next.js sites with a fixed nav and a split hero.
- Graphics papers whose hero shows a grid of renders beside a large coloured wordmark.

## Quick Start

```css
:root {
  --primary-color: #000000;
  --accent-color: #2f6dd1;
  --background-color: #ffffff;
  --light-gray: #f4f4f4;
  --medium-gray: #e0e0e0;
  --dark-gray: #666666;
  --font-sans: Arial, Helvetica, sans-serif;
  --font-mono: "IBM Plex Mono", monospace;
  --border-radius: 0px;
  --header-max: 1400px;
  --section-max: 1000px;
}
```

## Provenance

- **URL**: https://microsoft.github.io/renderformer/
- **Paper**: RenderFormer: Transformer-based Neural Rendering of Triangle Meshes with Global Illumination (arXiv 2505.21925), Chong Zeng, Yue Dong, Pieter Peers, Hongzhi Wu, Xin Tong.
- **Venue**: SIGGRAPH 2025 (Conference Papers).
- **Selection reason**: the arXiv comment states "Accepted to SIGGRAPH 2025" and links this project page; chosen for its large bold blue wordmark, split first screen with a 3×3 render grid, black icon buttons and sticky nav.
- **Template credit**: none stated; a custom Next.js static export with react-icons; footer carries Microsoft legal links.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), extra computed-style probes of the badge, affiliations, gallery cards and BibTeX block, the 1440×900 and full-page screenshots, and the page's stylesheet and `index.html` read directly, on 2026-10-28.
