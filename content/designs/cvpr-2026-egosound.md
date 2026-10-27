# EgoSound — Style Reference

> A wall of first-person CCTV feeds with the headline projected straight onto the glass.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, and a DOM probe of the hero and every section), the 1440×900 and full-page screenshots, and the page's single inline `<style>` block read directly. Inter loads in 400, 600 and 700 only, so the 900-weight `<strong>` in the hero renders at Inter 700. The hero background is an animated GIF mosaic (`assets/grid.gif`), so its colours change frame to frame; the color share below is from one frame.

## Overview

A small hand-written page in Inter that leads with its data. A sticky white header (85% white, 8px blur, saturate 180%) shows "EgoSound" as a 32px bold wordmark on the left and seven 16px/600 text links on the right. The hero fills exactly one viewport height (100vh) with an animated mosaic of egocentric video tiles (kitchens, cars, pool tables, living rooms) set to `object-fit: cover`, under a 10% teal wash. The title block floats over the centre with no visible panel: white 64px/700 "EgoSound" with a lighter 38.4px "[CVPR2026 HighLight]" tag on the same line, two lines of 18px author names, a 16px affiliation line, a 22px/600 one-sentence pitch with a 16px stats line, and a single white-outlined 12px-radius button. Below the hero the page turns plain and quiet: white sections with 28px bold left-aligned headings, grey 16px lead paragraphs (with key sentences tinted light blue #60a5fa), a 2×2 grid of rounded video cards with Q/A text, full-width rounded figures for the construction pipeline and results, a mauve Hugging Face button, dashed pale-blue resource tiles, a dark navy BibTeX block and a hairline footer. Mauve #8f5975 is the link and button colour.

## First Viewport

Color share (8-color quantization of one 1440×900 frame): video-mosaic tones #5a6056 15.6%, #96b6ad 13.8%, #8b9081 12.4%, #213233 11.1%, #657e78 11.0%, #4a4035 10.9%; near-black shadows #0b1414 13.9%; light grey #e5ebe9 11.3% (white header and bright tiles). Essentially the whole viewport below the 67px header is footage.

Anatomy in DOM order (desktop 1440px; `.container` 1120px with 20px padding, content 1080px at x=180):

1. **Header** (0–67px, sticky): rgba(255,255,255,0.85), backdrop-filter saturate(180%) blur(8px), 1px #e9ecf5 bottom rule. Left: "EgoSound" Inter 32px/700, letter-spacing 0.2px, #0b1220, at x=180. Right: About, Samples, DatasetConstruction, Experiments, Download, Resources, Citation in 16px/600 #1a2440, 18px apart, ending at x=1260.
2. **Hero** (`section.hero`, y=67–967, height 100vh): animated GIF mosaic covering the full width; overlay rgba(16,123,128,0.1). Content is flex-centred.
3. **Title panel** (`.hero-content`, x=300–1140, y=271–763): max-width 840px, padding 28px 32px, 16px radius, radial teal fill at 15–16% alpha (barely visible over the footage). All text white, centred.
4. **Title** (y=302, 69px line): Inter 64px/700, line-height 1.08, #ffffff; the inline `[CVPR2026 HighLight]` tag is 0.6em = 38.4px/400 at 90% opacity, 8px left margin. Gap 42px.
5. **Authors** (y=413 and 443): 18px/400 white, each name inline-block with a 21.6px right margin; numeric and symbol superscripts. Gap 25px.
6. **Affiliations** (y=494, wraps to two lines): 16px/400 white at 90% opacity, superscript numbers. Gap 34px.
7. **Pitch** (y=571): 22px/600 white, "sound understanding" in bold; then a 16px/400 line with bold counts ("7315", "900"). Gap 24px.
8. **Hero button** (`.btn-hero`, y=687, 366×48): transparent, 2px #ffffff border, 12px radius, padding 12px 16px, Inter 16px/700 white. The mosaic continues below to y=967.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Ink | #0b1220 | --ink | wordmark, section headings, card titles, body text |
| Nav Ink | #1a2440 | (literal) | header links |
| Muted | #5b6474 | --muted | lead paragraphs, card Q/A text, download note |
| Mauve | #8f5975 | --brand | inline links, Download button fill and border, hero button hover fill, unmuted sound button |
| Sky Note | #60a5fa | (inline style) | highlighted sentences inside the About paragraphs |
| Hairline | #e9ecf5 | (literal) | header bottom rule, card borders, footer top rule |
| Teal Wash | rgba(16,123,128,0.1) | --hero-overlay-color | overlay over the hero mosaic; the title panel uses the same teal at 0.15–0.16 |
| Resource Tint | #f7faff | (literal) | resource tiles |
| Resource Dash | #cfe0ff | (literal) | 1px dashed border of resource tiles |
| Media Placeholder | #e9efff | (literal) | video card media background before load |
| BibTeX Night | #020617 | (inline style) | citation block fill |
| BibTeX Text | #e5e7eb | (inline style) | citation text |
| Footer Grey | #6b7385 | (literal) | footer text |

Declared but not visible: `.tag`, `.badge`, `.team-member` and `.logos` styles (and `--bg-alt` #f6f8ff) exist in the stylesheet but no element uses them.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (everything) | Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, emoji fonts | Inter 400, 600, 700 | Roboto |
| Mono | browser monospace | Consolas | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Hero title | `.hero h1` | 64px / 700 / 1.08 | #ffffff |
| Title tag | `.hero-title-tag` | 0.6em = 38.4px / 400, opacity 0.9 | #ffffff |
| Hero authors | hero `p` (inline style) | 18px / 400 | #ffffff |
| Hero pitch | inline span | 22px / 600; strong 900 declared, renders 700 | #ffffff |
| Hero body | `.hero p` | 16px / 400, opacity 0.9 | #ffffff |
| Wordmark | `.brand .title` | 32px / 700, letter-spacing 0.2px | #0b1220 |
| Nav | `nav a` | 16px / 600 | #1a2440 |
| Section heading | `section h2` | 28px / 700, left-aligned | #0b1220 |
| Card title | `.card h3` | 18px / 700 | #0b1220 |
| Lead / card text | `section p.lead`, `.muted` | 16px / 400 / normal | #5b6474 |
| Buttons | `.btn`, `.btn-hero` | 16px / 700 | #ffffff |
| BibTeX | `pre` (inline) | 13px monospace | #e5e7eb |
| Footer | `footer` | 14px | #6b7385 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Hero title panel | 16px | none | none |
| Hero button, Download button | 12px | 2px #ffffff (hero) / 2px #8f5975 (download) | none (hero) / 0 10px 30px rgba(0,0,0,0.06) (download) |
| Video cards | 18px | 1px #e9ecf5 | 0 10px 30px rgba(0,0,0,0.06) |
| Section figures | 18px | none | none |
| Resource tiles | 14px | 1px dashed #cfe0ff | none |
| Sound toggle | 50% (40px circle) | 2px rgba(255,255,255,0.9) | none |
| BibTeX block | 12px | none | none |
| Header, footer | 0 | 1px #e9ecf5 bottom / top | none |

## Layout Metrics

- **Container**: `.container { max-width: 1120px; margin: 0 auto; padding: 0 20px }`, content 1080px at x=180.
- **Header**: 66px flex row, space-between, plus a 1px rule.
- **Hero**: `height: 100vh` (900px at 1440×900), flex-centred; title panel max-width 840px with padding 28px 32px.
- **Sections**: `section { padding: 64px 0 }`; h2 margin 0 0 14px; lead paragraphs 18px apart.
- **Card grid**: 12-column grid, gap 18px; each `.card` spans 6 columns (531px at 1440); media 16:9; card body padding 14px 16px.
- **Figures**: `.section-figure` full 1080px, margin 12px 0 20px, 18px radius with `overflow: hidden`.
- **Resource grid**: 12 columns, gap 14px, tiles span 6.
- **Footer**: padding 28px 0, two items space-between.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1120px | (100% − 1080px)/2 | 16px | 64px | 2 cards per row, 2 resource tiles per row |
| 881–1120px | 20px | 16px | 64px | — |
| ≤880px | 20px | 16px | 64px (no override) | cards and resource tiles span all 12 columns (one per row) |

The stylesheet has no small-screen rule for the header or the 64px title; on phones the seven nav links and the title would overflow, so an adaptation must add one.

## Components

- **Frosted header**: sticky, rgba(255,255,255,0.85), `backdrop-filter: saturate(180%) blur(8px)`, 1px #e9ecf5 bottom border; 32px/700 wordmark and plain 16px/600 #1a2440 links (no pills, no underline until hover).
- **Mosaic hero**: full-viewport `<img>` of an animated tile GIF, `object-fit: cover`, under a teal 10% overlay; title text white, centred, with no shadow.
- **Outline hero button** (`.btn-hero`): transparent, 2px white border, 12px radius, padding 12px 16px, 16px/700 white; hover fills #8f5975 with a #8f5975 border and lifts 1px.
- **Solid button** (`.btn`): #8f5975 fill and 2px border, white 16px/700, 12px radius, padding 12px 16px, shadow 0 10px 30px rgba(0,0,0,0.06), emoji at the end; hover lifts 1px.
- **Video sample card** (`.card`): white, 1px #e9ecf5, 18px radius, shadow 0 10px 30px rgba(0,0,0,0.06); 16:9 autoplay muted video on #e9efff; a 40px round sound toggle at the top right (rgba(0,0,0,0.5), 2px white border, speaker emoji; turns #8f5975 when unmuted); body 14px 16px with an 18px/700 task name and 16px #5b6474 "Question:" / "Answer:" lines with bold labels.
- **Rounded figure** (`.section-figure`): white wrapper, 18px radius, line-height 0, image full width.
- **Resource tile** (`.res`): #f7faff, 1px dashed #cfe0ff, 14px radius, padding 16px, bold label over a mauve link.
- **Dark BibTeX block**: #020617, 13px #e5e7eb monospace, padding 16px, 12px radius.
- **Footer**: 1px #e9ecf5 top rule, padding 28px 0, 14px #6b7385, copyright left and "Back to top ↑" link right.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky navigation | yes | frosted header with wordmark and seven text links |
| Hero with data mosaic | yes | full-viewport animated GIF of egocentric clips |
| Title / venue | present but non-standard | the venue and award are an inline bracket tag after the title |
| Authors / affiliations | yes | white text over footage, no links |
| Link buttons | present but non-standard | one in-page anchor button in the hero; paper and code live in a Resources section further down |
| TL;DR | yes | 22px/600 pitch sentence plus a counts line in the hero |
| Teaser figure | absent from the source | the mosaic replaces it |
| Abstract | present but non-standard | "About the Dataset" lead paragraphs with light-blue emphasis sentences |
| Data samples | yes | 2×2 grid of video cards with Q/A text and sound toggles |
| Method / pipeline | yes | one rounded figure with three bold-led paragraphs |
| Results | present but non-standard | one results figure image; no HTML table |
| Download | yes | mauve Hugging Face button with a note |
| Resources | yes | two dashed tiles (Paper, GitHub) |
| BibTeX | yes | dark navy block |
| Footer | yes | hairline, copyright and back-to-top |

## Adapting to Other Content

- **A different dataset or model**: build the mosaic from 12–20 short clips or stills of your own data at equal tile size; keep the 10% overlay and white text. If the footage is bright, raise the overlay alpha (for example rgba(16,123,128,0.35)) rather than adding a text shadow.
- **More authors**: keep 18px inline-block names; wrap to a third line inside the 840px panel, and drop the pitch line to the first section if the panel would exceed about 600px tall.
- **Paper / code / data buttons**: add them next to the hero button as more `.btn-hero` outlines, 12px gap; keep the solid mauve `.btn` for below-the-fold downloads.
- **A results table**: put it in a white card with the 18px radius and 1px #e9ecf5 border; header row 14px/700 #0b1220, body 14px #5b6474, 1px #e9ecf5 row rules; best values bold.
- **News or a long list**: a single-column list of `.res`-style tiles (dashed #cfe0ff on #f7faff) with a bold date label and a mauve link.

## Do's and Don'ts

- Do lead with the data itself; the hero has no figure, only footage.
- Do keep the title white and unboxed; the 16px panel is near-transparent.
- Do keep the body plain: left-aligned 28px headings, grey 16px leads, white cards.
- Don't add a second accent beyond mauve #8f5975 and the light-blue emphasis #60a5fa.
- Don't centre section headings; only the hero is centred.
- Don't forget a mobile rule for the header and title; the source lacks one.

## Surfaces

Animated footage hero under a faint teal wash; white page and white cards; pale-blue dashed resource tiles; one dark navy code block; frosted white header.

## Imagery

Egocentric video: hands at kitchen counters, car dashboards, a pool hall, living rooms with smart glasses, desks with laptops. In the body, four autoplaying sample clips, a pipeline diagram and a results chart.

## Layout

Sticky header; one full-viewport mosaic hero; then a 1080px left-aligned column: About, Data Samples (2×2), Dataset Construction, Performance, Download, Resources, Citation; footer. About 4,860px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: ink #0b1220, nav #1a2440, muted #5b6474, brand mauve #8f5975, emphasis #60a5fa, hairline #e9ecf5, resource #f7faff with #cfe0ff dashes, code #020617 with #e5e7eb text.

1. "Build a full-viewport data-mosaic hero: section height 100vh, an animated grid image covering it with object-fit cover, an overlay rgba(16,123,128,0.1), and a centred block max-width 840px: title Inter 64px/700 #ffffff with an inline 0.6em/400 bracket tag at 90% opacity; authors 18px white; a 22px/600 one-line pitch; then a button with transparent fill, 2px solid #ffffff border, 12px radius, padding 12px 16px, 16px/700 white, hover background #8f5975."
2. "Create a sample card: white, 1px solid #e9ecf5, 18px radius, box-shadow 0 10px 30px rgba(0,0,0,0.06), overflow hidden; a 16:9 autoplay muted video with a 40px circular mute toggle at top 12px right 12px (rgba(0,0,0,0.5), 2px rgba(255,255,255,0.9) border); body padding 14px 16px with an Inter 18px/700 #0b1220 title and 16px #5b6474 'Question:' / 'Answer:' lines."
3. "Make a frosted sticky header: background rgba(255,255,255,0.85), backdrop-filter saturate(180%) blur(8px), 1px solid #e9ecf5 bottom border, height 66px, max-width 1120px container; wordmark Inter 32px/700 #0b1220; links 16px/600 #1a2440, 18px gap."

## Similar Pages

- Dataset and benchmark pages whose hero is a collage or mosaic of the data.
- Lightweight single-file pages with an Inter body and one brand colour.

## Quick Start

```css
:root {
  --brand: #8f5975;
  --ink: #0b1220;
  --muted: #5b6474;
  --nav: #1a2440;
  --hairline: #e9ecf5;
  --emphasis: #60a5fa;
  --res-bg: #f7faff;
  --res-border: #cfe0ff;
  --code-bg: #020617;
  --code-fg: #e5e7eb;
  --shadow: 0 10px 30px rgba(0, 0, 0, 0.06);
  --radius: 18px;
  --hero-overlay-color: rgba(16, 123, 128, 0.1);
  --font: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
body { margin: 0; font-family: var(--font); color: var(--ink); background: #ffffff; }
.container { max-width: 1120px; margin: 0 auto; padding: 0 20px; }
section { padding: 64px 0; }
```

## Provenance

- **URL**: https://groolegend.github.io/EgoSound/
- **Paper**: EgoSound: Benchmarking Sound Understanding in Egocentric Videos (arXiv 2602.14122), Bingwen Zhu et al.
- **Venue**: CVPR 2026 (the page title tag says "CVPR2026 HighLight").
- **Selection reason**: the arXiv comment states acceptance at CVPR 2026 and the abstract links this page.
- **Template credit**: none credited; a single hand-written HTML file with an inline stylesheet (its Download text still says "EgoCross", suggesting it was adapted from that sibling page).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), a DOM probe of hero and sections, the 1440×900 and full-page screenshots, and the inline stylesheet and markup read directly, on 2026-10-28.
