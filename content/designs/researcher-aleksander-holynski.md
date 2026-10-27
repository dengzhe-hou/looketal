# Centered Gallery Column — Style Reference

> A museum wall label beside every work: one narrow white column, small centred serif captions on the left and silent square videos that wake when you hover.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, loaded fonts, color share), selector probes of the filters, rows and media, the 1440×900 and full-page screenshots, and the hand-written `application.css` and table markup read directly (Bootstrap 4.0 is also linked but only sets the body colour #212529, which the page's own #222222 text overrides). PT Serif, PT Sans and PT Sans Narrow load from Google Fonts in weight 400 only, so every bold on the page is synthesized. Sizes are percentages of a 120px base on `.mainPage`, which is why they come out as 16.8px, 21.6px and 26.4px.

## Overview

An 800px white column centred on a white page, built from HTML tables. The header row puts "ALEKSANDER HOŁYŃSKI" in 26.4px PT Sans Narrow bold uppercase, centred in the left half, with "Email / Google Scholar / Bio / CV" as underlined 16.8px PT Serif links beneath, and a 216px black-and-white circular portrait cut-out (a looping video) on the right. "ABOUT ME" in 21.6px PT Sans bold uppercase heads a single 16.8px PT Serif paragraph whose links are #222222 with plain underlines. A row of small pill filter chips follows: white with #d8d8d8 borders, the active "Representative" chip filled #222222 with white bold text, and a cream "Students" chip set apart. Then the publication gallery: each row is a table with a 67% text cell (centred underlined title, 12.6px authors with the owner in heavy bold, venue and year, and underlined "PDF / arXiv / Webpage / Code") and a 33% cell holding a 197px square video that plays on hover. Oral presentations and awards appear in pure red #ff0000.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 83.9% plus #f8f8f8 1.4%, #e6e5e5 2.4%; cool greys #c0c9cc 3.9% and #97a0a5 3.8% (the chrome whale render); dark #413c46 3.8% (portrait, text and the Genie city still). The red Genie robot and the teal street are too small to form clusters.

Anatomy in DOM order (desktop 1440px; `.mainPage` 800px at x=320; header table cells 395px and the portrait cell):

1. **Name** (`h1` in `.sample#camus`, y=74, centred in the left 395px cell): PT Sans Narrow 26.4px / 700 (synthesized) / 26.4px, uppercase, #222222, padding 15.8px 0 7.9px. Gap 6px.
2. **Links** (y=130): "Email / Google Scholar / Bio / CV", PT Serif 16.8px / 400, #222222, underlined, slashes unlinked. 
3. **Portrait** (right cell, x=811, y=16, 216×216): looping black-and-white video of a head-and-shoulders cut-out inside a circle on white. Gap to the next heading about 4px.
4. **About heading** (`h1`, y=236): PT Sans 21.6px / 700 (synthesized), uppercase, #222222, left aligned, padding 32px 0 16px.
5. **Bio** (`p`, y=306): PT Serif 16.8px / 21.5px, #222222, left aligned across 800px, links underlined. Gap 31px.
6. **Filter chips** (`a.filt`, y=402, 22px tall): PT Sans 12px, padding 2.4px 7.4px, radius 24px; "All Projects", the active "Representative", "Generative 3D", "Video & World Models", "Reconstruction", "Image Generation", "Products", and the cream "Students" after a 10.8px extra gap. Gap 22px.
7. **First gallery rows** (from y=446): centred 16.8px title links ("Gemini Omni", "Genie 3: A New Frontier for World Models"), 12.6px credits, year, then 13.4px link row; 197px square videos at x=889, stacked edge to edge (1px apart).

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | `body`, `.mainPage` | page and column background, inactive chips |
| Ink | #222222 | `h1`, `.sample#camus p, center` | name, headings, bio, titles, authors, links, active chip fill |
| Oral Red | #ff0000 | inline `color: red` | "Oral Presentation", "Best Paper Honorable Mention" |
| Chip Border | #d8d8d8 | `a.filt` | inactive chip border |
| Chip Hover | #f1f1f1 | `a.filt:hover` | chip hover fill, border #9a9a9a |
| Chip Hover Border | #9a9a9a | `a.filt:hover` | chip hover border |
| Cream Chip | #fdfaed | `a.filt.people` | "Students" chip fill |
| Cream Chip Border | #e7dcb6 | `a.filt.people` | "Students" chip border; hover fill #f8f0d4, border #cdbd82 |
| Cream Hover | #f8f0d4 | `a.filt.people:hover` | "Students" hover fill |
| Cream Hover Border | #cdbd82 | `a.filt.people:hover` | "Students" hover border |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display narrow | "pt sans narrow" | PT Sans Narrow 400 (700 synthesized) | Archivo Narrow |
| Label sans | "pt sans" | PT Sans 400 (700 synthesized) | Source Sans 3 |
| Text serif | "pt serif" | PT Serif 400 (bold synthesized) | Source Serif 4 |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `.sample#camus h1` | 22% of 120px = 26.4px / 700 / 100%, uppercase, centred | #222222 |
| Section heading | `h1` | 18% = 21.6px / 700 / 100%, uppercase, left | #222222 |
| Bio and links | `.sample#camus p` | 14% = 16.8px / 400 / 128.5% (21.5px) | #222222 |
| Paper title | row `a` (`font-size: 100%` or 99%) | 16.8px / 400, centred, underlined | #222222 |
| Credits / venue | row `div` (`font-size: 75%`) | 12.6px / 400 / 21.5px, centred | #222222 |
| Own name | `strong` (inline `font-weight: 1000; text-shadow: 0.1px 0.1px`) | 12.6px / heavy synthesized bold | #222222 |
| Paper links | row `a` (`font-size: 80%`) | 13.44px / 400, underlined | #222222 |
| Highlight | inline red | 12.6px / 400 | #ff0000 |
| Filter chip | `a.filt` | 12px / 400 / 1.3; active 700; Students 600 | #222222 / #ffffff |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Filter chip | 2em (24px) | 1px solid #d8d8d8 | none |
| Active chip | 24px | 1px solid #222222 | none |
| Students chip | 24px | 1px solid #e7dcb6 | none |
| Portrait | circle inside the video frame | none | none |
| Project videos | 0 | none | none |
| Tables | 0 | none (`border-collapse: separate`) | none |

## Layout Metrics

- **Column**: `.mainPage { width: 800px; margin: 0 auto; font-size: 120px; line-height: 100px }` from 800px up; below that `width: 100%; font-size: 100px`. The outer `section` has a 10px margin.
- **Header table**: two cells, text cell 395px with centred name and links, portrait cell holding a 216×216 video.
- **About**: `h1` padding 4% 0 2% (32px 0 16px at 800px); one paragraph.
- **Filters**: chips margin 0 3.4px 3.6px 0 (Students has 10.8px extra left margin); block padding 32px 0 17.6px.
- **Gallery rows**: `<tr>` per project, `td` 67% (text, vertical-align middle, centred) and 33% (media); videos `width="75%"` = 197px square, rows about 198px tall so images stack edge to edge.
- **Hover**: `onmouseover` plays the row's video, `onmouseout` pauses it; some rows swap between two stacked images with `.fadeImage` opacity transitions of 0.2s.
- **Page height**: 5,022px at 1440.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥800px | (100% − 800px)/2 | 16.8px | 26.4px name, 21.6px headings | 800px column, 67/33 rows |
| <800px | 10px (section margin) | 14px (14% of 100px) | 22px name, 18px headings | column fills the width; rows keep the 67/33 table split |

## Components

- **Wall-label row**: a table row with a centred caption block (underlined 16.8px PT Serif title; 12.6px authors with line breaks placed by hand; owner name heavy bold with a 0.1px text shadow; venue and year; a blank line; underlined 13.4px links separated by " / ") beside a 197px square silent video.
- **Hover-to-play media**: videos load from `data-src`, are muted, inline and looping, and only play while the pointer is over their row.
- **Filter chips**: inline-block pills, 12px PT Sans, 1px #d8d8d8 border, 24px radius, padding 0.2em 0.62em; hover #f1f1f1 with a #9a9a9a border; active #222222 with white bold text; the "Students" chip is cream #fdfaed with a #e7dcb6 border, set apart by extra margin.
- **Red highlight**: "(Oral Presentation)" and "Best Paper Honorable Mention" set in #ff0000 inside the venue line, no weight change.
- **Slash link row**: underlined links separated by plain " / " text, used in the header and under every paper.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Name and links | yes | narrow uppercase name, slash-separated links |
| Portrait | yes | black-and-white circular cut-out as a looping video |
| Bio | yes | one 16.8px serif paragraph under ABOUT ME |
| Topic filters | yes | pill chips that show and hide rows by `data-group` |
| Publications | yes | centred wall-label rows with square hover videos |
| Awards | present but non-standard | red text inside venue lines |
| Students | yes | a filter chip that switches the gallery to student rows |
| News | absent from the source | none |
| Navigation bar | absent from the source | links in the header only |
| Footer | absent from the source | page ends after the last row |

## Adapting to Other Content

- **Long publication lists**: keep the wall-label rows; the filter chips already handle length. For older work without media, keep the 33% cell with a still image at the same 197px square so the right edge stays a continuous strip.
- **News**: a left-aligned list under a 21.6px uppercase PT Sans heading, each line 16.8px PT Serif with the date in heavy bold.
- **More authors**: break author lines by hand at about 60 characters, as the page does, so the centred block stays balanced.
- **Awards**: keep them as red #ff0000 words in the venue line rather than badges.
- **Results tables**: plain 12.6px PT Serif tables, centred, no borders, bold for best values.

## Do's and Don'ts

- Do keep everything inside one 800px centred column with a white ground.
- Do centre captions and underline every link in the same #222222 as the text.
- Do make media square, borderless and flush so the right edge reads as a filmstrip.
- Don't add colour except pure red for orals and awards and the cream Students chip.
- Don't round or shadow images.
- Don't autoplay all videos; play on hover only.

## Surfaces

White everywhere. The only fills are the chips (white, #222222 active, #fdfaed Students) and the media themselves.

## Imagery

A black-and-white cut-out portrait in a circle; square project videos and stills (a chrome whale, a red robot in a teal neon street, a 3D-reconstructed pavilion, fire dancers, an apple tree, a teddy bear in a city, a chef mouse) that make the right edge a colourful strip against the monochrome text.

## Layout

Header table (name, links | portrait); ABOUT ME; filter chips; gallery table of about 50 rows. About 5,022px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: background #ffffff, text and links #222222, highlight #ff0000, chip border #d8d8d8, chip hover #f1f1f1, Students chip #fdfaed with #e7dcb6 border.

1. "Build an 800px centred white column. Header: two cells; left a centred PT Sans Narrow 26.4px bold uppercase name in #222222 with 'Email / Google Scholar / Bio / CV' below in 16.8px PT Serif underlined #222222 links; right a 216px black-and-white circular portrait."
2. "Make filter chips: inline-block PT Sans 12px pills, padding 0.2em 0.62em, 1px #d8d8d8 border, 24px radius, white; hover #f1f1f1 with a #9a9a9a border; active #222222 fill with white bold text; one extra 'Students' chip in #fdfaed with a #e7dcb6 border."
3. "Make a publication row as a table: 67% cell centred and vertically middled with an underlined 16.8px PT Serif #222222 title, 12.6px authors (own name heavy bold), venue and year, a red #ff0000 '(Oral Presentation)' when relevant, a blank line, then 13.4px underlined 'PDF / arXiv / Code'; 33% cell with a 197px square muted looping video that plays on row hover. No borders, no radius."

## Similar Pages

- Jon Barron-style table homepages with hover-animated thumbnails.
- Graphics researcher pages that pair centred captions with square media.

## Quick Start

```css
:root {
  --ink: #222222;
  --bg: #ffffff;
  --highlight: #ff0000;
  --chip-border: #d8d8d8;
  --chip-hover: #f1f1f1;
  --people-bg: #fdfaed;
  --people-border: #e7dcb6;
}
body { background: var(--bg); margin: 0; }
.mainPage { width: 800px; margin: 0 auto; font-size: 120px; line-height: 100px; }
.mainPage p, .mainPage center { color: var(--ink); font: 400 14%/128.5% "PT Serif", serif; }
.mainPage h1 { color: var(--ink); font: 700 18%/100% "PT Sans", sans-serif; text-transform: uppercase; padding: 4% 0 2%; }
a:link { color: inherit; text-decoration: underline; }
a.filt { font: 12px/1.3 "PT Sans", sans-serif; border: 1px solid var(--chip-border); border-radius: 2em; padding: .2em .62em; background: #ffffff; text-decoration: none; }
a.filt.active { background: var(--ink); border-color: var(--ink); color: #ffffff; font-weight: 700; }
.oral { color: var(--highlight); }
```

## Provenance

- **URL**: https://holynski.org/
- **Person**: Aleksander Holynski, computer vision, generative video and 3D.
- **Award**: CVPR 2024 Best Paper, "Generative Image Dynamics" (last author). https://cvpr.thecvf.com/Conferences/2024/News/Awards
- **Selection reason**: award rule (first or last author); chosen for the centred, gallery-like publication column paired with square imagery and filter chips.
- **Template credit**: none stated; hand-written tables with `application.css` and a `hidebib.js` script.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), selector probes, the 1440×900 and full-page screenshots, and `application.css` and the markup read directly, on 2026-10-28.
