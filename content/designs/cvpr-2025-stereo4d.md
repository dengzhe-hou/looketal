# Stereo4D Nerfies Plus — Style Reference

> A Nerfies page that learned to curate: a tight masthead, a gallery that peeks past the margins, and a pale-blue reading room.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide first-viewport and tall screenshots, the page's `static/css/index.css` and `app.css`, inline styles in the HTML, Bulma and bulma-carousel, and the carousel options in `static/js/index.js`. Because `index.css` is linked before `bulma.min.css`, Bulma's body font stack wins over the declared Noto Sans, so plain text renders in the system UI face (Segoe UI on Windows, San Francisco on macOS); Google Sans 400/600 renders where `.publication-title` and `.publication-authors` ask for it. The TL;DR and "How is it made?" fills were sampled from the screenshots. Color share is measured on the first viewport.

## Overview

The header is compact and centered: "Stereo4D" in Google Sans 48px, a 32px subtitle "Learning How Things Move in 3D from Internet Stereo Videos", one line of blue author links, one line of grey affiliations ending with "(*: equal contribution)", a bold "CVPR 2025 (Oral)", and three charcoal pill buttons, the last carrying a small red "NEW" tag. A pale-blue TL;DR box (#c8e1f1) sits under them. Then a full-bleed #f5f5f5 band titled "Dataset gallery" runs an autoplaying carousel of 936px video slides with 10px corners: the center slide shows a real stereo clip inset over a grey 3D grid with rainbow motion trails, and neighbors peek in at both screen edges, with white round arrows on the center slide. Below, the method story is told inside one long pale-blue notification column (#eef6fc) with blue text (#1d72aa): paragraphs alternate with camera-rig icons, a fisheye video grid, pipeline frames and a 3D trajectory video. A white "Using this data to learn how things move" section adds an interactive input/reconstruction table with thumbnail pills, then Acknowledgements, BibTeX and the Nerfies footer.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 42.0%, warm grey #81797c 16.4% and sage grey #818c8c 11.6% (the 3D grid renders), band grey #f6f6f6 14.9% (`.hero.is-light`), charcoal #4d4d51 7.1%, blue-grey #bdc5c9 6.9%. The TL;DR blue, author blue and buttons are each under 3%.

Anatomy in DOM order (centered on x=720; `.container.is-max-desktop` 960px; hero body padding 48px 24px):

1. **Title** — `h1.title.is-1.publication-title`, "Stereo4D", Google Sans 48px / 600, line-height 54px, #363636 (y=48–102). Margin-bottom 0 (inline).
2. **Subtitle** — `h3.title.is-3.publication-title`, Google Sans 32px / 600, #363636 (y=102–138). Margin-bottom 24px.
3. **Authors** — `.is-size-6.publication-authors`, Google Sans 16px, links #209cee, superscripts, one line (y=167–187).
4. **Affiliations** — second `.is-size-6.publication-authors`, 16px, #4a4a4a, one line with "(*: equal contribution)" at the end (about y=190–210).
5. **Venue** — `h1` with inline `font-size: 24px; font-weight: bold`, "CVPR 2025 (Oral)", system UI bold, #4a4a4a (y=217–253).
6. **Buttons** — three `a.external-link.button.is-normal.is-rounded.is-dark`, 40px, #363636, #ffffff Noto Sans 16px, padding 7px 20px, pill, icons left (arXiv, database, GitHub); "DynaDUSt3R" carries a `.tag.is-danger.is-small` "NEW" in #f14668 (y=270–310).
7. **TL;DR** — `.notification.is-info` in a four-fifths column (about 764px, x=338–1102), fill #c8e1f1, 4px radius, padding 5px top and bottom; `h6` 16px #000000 centered, "TL;DR" bold, key phrases italic (about y=351–409).
8. **Gallery band** — `section.hero.is-light.is-small` from y=457, #f5f5f5; `h2` "Dataset gallery" 32px / 600, rgba(0,0,0,0.7), margin-bottom 5px; a 16px two-line description; then the carousel row at y=582: slides 936×527px with 10px corners, center slide x=252–1188, neighbors cut by the viewport edges, white circular arrows inside the center slide.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | Bulma `$white` | page, header, lower sections, button text, carousel arrows |
| Charcoal | #363636 | Bulma `.title` | title, subtitle, section titles in white sections, button fill |
| Body Grey | #4a4a4a | Bulma body | affiliations, venue line, body text, BibTeX text |
| Author Blue | #209cee | `.publication-authors a` | author links |
| TL;DR Blue | #c8e1f1 | `.notification.is-info` (rendered) | TL;DR box fill |
| Gallery Band | #f5f5f5 | Bulma `.hero.is-light` | Dataset gallery band, BibTeX `pre` |
| Band Title | rgba(0,0,0,0.7) | Bulma `.hero.is-light` | gallery title and description |
| Reading Room | #eef6fc | `.notification.is-info.is-light` | "How is it made?" column fill |
| Reading Ink | #1d72aa | `.notification.is-info.is-light` | text and title in that column |
| New Red | #f14668 | `.tag.is-danger` | "NEW" tag on the DynaDUSt3R button |
| Pill Active | #1772d0 | `.scene-pill.active` | selected thumbnail pill |
| Pill Rule | #dddddd | `.pill` | 1px border of thumbnail pills |
| Footer Fog | #fafafa | Bulma `.footer` | footer |

## Tokens — Typography

- **Title, subtitle, authors:** `'Google Sans', sans-serif`; renders Google Sans 400 and 600 (loaded). Substitute: Product Sans or Outfit.
- **Body:** declared `'Noto Sans', sans-serif` in `index.css`, overridden by Bulma's `BlinkMacSystemFont, -apple-system, "Segoe UI", …` stack loaded afterwards; renders Segoe UI on Windows, SF Pro on macOS. Noto Sans 400 does load and renders on the link buttons. Substitute for the body: Inter.
- **Code:** browser monospace (Consolas on Windows).

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Title | `.title.is-1.publication-title` | 48px / 600 / 54px |
| Subtitle | `h3.title.is-3.publication-title` | 32px / 600 / 36px |
| Section title | `h2.title.is-3` | 32px / 600 / 36px |
| Venue | `h1` inline style | 24px / 700 / 36px |
| Authors, affiliations | `.is-size-6.publication-authors` | 16px / 400 / 24px |
| TL;DR | `h6` in `.notification` | 16px / 400, bold lead, centered |
| Body | `p`, `.content` | 16px / 400 / 24px, justified in the method column |
| Buttons | `.button` | 16px / 400 |
| Tag | `.tag.is-small` | 12px |
| Table header | `th` | 16px / 700, #363636 |
| Code | `pre` | 14px / 21px |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Buttons | pill, padding 7px 20px |
| Gallery slides | 10px radius, no border, 1px margin |
| Notifications | Bulma 4px radius |
| Carousel arrows | white circles, Bulma carousel default with dark chevrons |
| Thumbnail pills | 5px radius, 1px #dddddd border, 2px padding and margin, 80px wide; hover scales 1.1; active fill #1772d0 |
| Figures and videos in the method column | square corners, no shadow |

## Layout Metrics

- **Container:** Bulma `.container.is-max-desktop`, 960px (x=240–1200 at 1440); text columns `is-four-fifths` (768px).
- **Header:** `.hero-body` padding 48px 24px; title block ends at y≈310; TL;DR column four-fifths wide.
- **Gallery:** full-bleed band; the carousel container is set to `max-width: 100%`, so slides of 936px sit edge to edge with neighbors partially visible; `slidesToShow: 1`, loop, autoplay, no pagination.
- **Method column:** `.notification.is-info.is-light` in a four-fifths column (747px, x=346–1093), Bulma notification padding 20px 40px 20px 24px.
- **Interactive table:** 747px wide; input column 30%, reconstruction 70%; pills row centered below.
- **Sections:** `.section` padding 48px 24px for Acknowledgements and BibTeX.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1024px | (viewport − 960)/2 | 16px | 48px | gallery slides 936px with peeking neighbors |
| 769–1023px | 24px | 16px | 48px | four-fifths columns stay |
| ≤768px | 24px | 16px | 48px (no mobile step) | columns stack, TL;DR and method column go full width; gallery slides shrink to the viewport |

## Components

- **Charcoal pill button with tag:** Bulma `.button.is-dark.is-rounded`, #363636, #ffffff 16px, padding 7px 20px, icon left; an optional `.tag.is-danger.is-small` "NEW" (#f14668, #ffffff, 5px left margin) inside the label.
- **TL;DR box:** `.notification.is-info` rendered #c8e1f1, 4px radius, 5px vertical padding, centered 16px #000000 text with bold "TL;DR" and italic key phrases, in a four-fifths column.
- **Peeking gallery:** full-bleed #f5f5f5 band, centered 32px title with 5px gap to a 16px description, then a looping autoplay carousel of 16:9 videos with 10px corners; neighbors show at the edges; white round arrows sit inside the active slide near its vertical middle.
- **Reading-room column:** one tall `.notification.is-info.is-light` (#eef6fc fill, #1d72aa text, 4px radius) holding the "How is it made?" narrative: justified paragraphs alternating with centered figures (camera icons beside a fisheye video grid, a pipeline strip of poses / depth / 2D tracks, an RGB clip beside a 3D trajectory plot).
- **Interactive reconstruction table:** borderless two-column table (Input image pair / Reconstruction), 16:9 videos, and a row of 80px thumbnail pills; hover scales a pill to 1.1, active pill gets a #1772d0 fill.
- **BibTeX:** Bulma `pre` on #f5f5f5.
- **Footer:** #fafafa, "This website is borrowed from Nerfies and CAT3D".

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / subtitle / authors / affiliations | Yes | compact Google Sans masthead |
| Venue line | Yes | bold 24px "CVPR 2025 (Oral)" |
| Link buttons | Yes | three charcoal pills, one with a NEW tag |
| TL;DR | Yes | pale-blue notification box |
| Teaser / gallery | Yes | full-bleed peeking video carousel on a grey band |
| Method narrative | Yes | pale-blue notification column interleaving text and figures |
| Interactive demo | Yes | input/reconstruction table with thumbnail pills |
| Image comparison | Yes | slider in the method column |
| Results table (HTML) | No (absent from the source) | |
| Abstract | Present but non-standard | replaced by the TL;DR and the narrative column |
| Acknowledgements | Yes | white section |
| BibTeX | Yes | grey `pre` |
| Footer | Yes | Nerfies and CAT3D credit |

## Adapting to Other Content

- **More authors:** move authors to `is-size-5` (20px) and let them wrap; keep affiliations on their own 16px line and the equal-contribution note at its end.
- **Results table:** put it in a four-fifths `.notification.is-light` box like the method column, with a white Bulma `.table` inside, #363636 headers, best values bold.
- **Long publication or news list:** a four-fifths column of #eef6fc notification cards, one per item, #1d72aa text.
- **Image gallery instead of video:** keep the full-bleed band and the 10px-corner slides; use `slidesToShow: 1` so neighbors keep peeking.
- **Abstract:** if one is required, place it in a white four-fifths column above the gallery, justified 16px, and keep the TL;DR box.

## Do's and Don'ts

- Do keep the masthead tight: title and subtitle with no gap, one line each of authors and affiliations.
- Do let the gallery bleed to the screen edges; the peeking neighbors are the point.
- Do group the method story in one tinted column so it reads as one narrative.
- Don't add more tinted colors; two blues (TL;DR and reading room) and one band grey are the whole palette.
- Don't put the TL;DR inside the gallery band.
- Don't link `index.css` before Bulma if you actually want Noto Sans in the body.

## Surfaces

White header and lower sections; full-bleed #f5f5f5 gallery band; #c8e1f1 TL;DR box; #eef6fc reading-room column; #f5f5f5 code; #fafafa footer.

## Imagery

Stereo video frames inset over grey 3D grid renders with rainbow motion trails, camera-rig product photos, a grid of fisheye stereo frames, depth maps and 2D track overlays, 3D trajectory plots and reconstruction videos.

## Layout

A centered 960px column interrupted by one full-bleed gallery band; the method lives in a single tinted 747px column. Rendered height about 4,750px.

## Agent Prompt Guide

Quick colors: title #363636, body #4a4a4a, author links #209cee, TL;DR #c8e1f1, band #f5f5f5, reading room #eef6fc with #1d72aa text, NEW tag #f14668, active pill #1772d0, footer #fafafa.

1. "Build a compact masthead: Google Sans 48px/600 title in #363636 with no bottom margin, directly followed by a 32px/600 subtitle; one 16px line of #209cee author links; one 16px #4a4a4a affiliation line; a bold 24px venue line; three #363636 pill buttons (padding 7px 20px, #ffffff 16px) with a small #f14668 'NEW' tag inside the last; then a centered 16px TL;DR box filled #c8e1f1 with 4px radius in a 768px column."
2. "Create a peeking gallery: full-bleed #f5f5f5 band, centered 32px title in rgba(0,0,0,0.7) with a 5px gap to a 16px description; below, a looping autoplay carousel showing one 936px 16:9 video slide at a time with 10px corners, the previous and next slides visible at the viewport edges, white circular arrows inside the active slide."
3. "Make a reading-room column: a 747px box filled #eef6fc with #1d72aa text and 4px radius, padding 20px 40px 20px 24px; a centered 32px title, then justified 16px paragraphs alternating with centered figures and videos at full column width, square corners."

## Similar Pages

- Nerfies and CAT3D project pages (credited in the footer).
- Google Research dataset pages that lead with a full-bleed autoplay gallery.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --title: #363636;
  --text: #4a4a4a;
  --author-link: #209cee;
  --tldr-bg: #c8e1f1;
  --band: #f5f5f5;
  --reading-bg: #eef6fc;
  --reading-text: #1d72aa;
  --tag-new: #f14668;
  --pill-active: #1772d0;
  --footer: #fafafa;
  --font-title: 'Google Sans', 'Outfit', sans-serif;
  --font-body: BlinkMacSystemFont, -apple-system, 'Segoe UI', 'Inter', sans-serif;
  --title-size: 48px;
  --subtitle-size: 32px;
  --body-size: 16px;
  --container: 960px;
  --slide-radius: 10px;
}
```

## Provenance

- **URL:** https://stereo4d.github.io
- **Paper:** Stereo4D: Learning How Things Move in 3D from Internet Stereo Videos (arXiv 2412.09621), Linyi Jin, Richard Tucker, Zhengqi Li, David Fouhey, Noah Snavely, Aleksander Hołyński.
- **Venue:** CVPR 2025, Oral (stated on the page).
- **Selection reason:** the arXiv comment states CVPR 2025 (camera ready) and the abstract links the page; chosen as the most complete composition: tight header with pill buttons and tinted TL;DR, a full-bleed gallery that peeks at neighboring slides, then a tinted narrative column interleaving figures and prose.
- **Template credit:** footer reads "This website is borrowed from Nerfies and CAT3D".
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share and loaded-font list, 1440 first-viewport and tall screenshots (TL;DR and column fills sampled from them), `static/css/index.css`, `app.css`, `static/js/index.js`, page HTML; 2026-10-28.
