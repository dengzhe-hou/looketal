# DiWA Freiburg Banner — Style Reference

> A university lab's billboard: a navy wordmark strip, a smoky robot video behind white type, then calm white and pale-grey bands that hand each figure its own stage.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, loaded fonts, color share), selector probes of the banner, buttons, section bands, carousels and author tiles, the 1440×900 and full-page screenshots, and the page's `static/css/main.css` (TEMPLATED "Full Motion" template, heavily edited) and `index.html`. Bootstrap 5.3.2 is also loaded and contributes the 48px `my-5` spacer and a few resets. The theme base sizes are in pt and em, so many rendered sizes are fractional (body 11pt = 14.67px at 1440). The banner background is an autoplaying video, so the screenshot shows one frame.

## Overview

A long, centred project page (about 6,200px tall). The first 459px are a dark banner: a 60px navy bar (#1d154d) carrying the white "universität freiburg" wordmark, over a full-width robot-arm video dimmed by a #42424f overlay at 70% opacity. On it sit a small "DiWA" logotype filled with a blue-green-yellow gradient, a large white title, dotted-underlined white author links, a bold venue line and four translucent pill buttons with Font Awesome and Academicons glyphs. Below, full-width bands alternate between white (#ffffff) and pale grey (#ececec): a large italic one-sentence summary over the teaser figure, Abstract, Overview figure, Summary Video (YouTube embed), real-world and CALVIN video carousels, Code with download pills, Publications, round author photos, Acknowledgment, and a near-black footer (#1b1b1f). All content sits in a 1173px column; headings are Roboto 600 centred, body text Roboto 300.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white family #ffffff / #fefffd / #feffff 37.5% (the approach band and teaser figure); dimmed video greys #494950 / #53545d / #64656e together 42.8% (the banner); pale blue-grey #cfd5da 11.1% (lit parts of the video and the figure's pastel panels); dark navy #2b2648 8.7% (the wordmark bar plus dark video areas).

Anatomy in DOM order (desktop 1440px, everything centred):

1. **Wordmark bar** (`#banner .logos`, 0–60px, absolute, full width): #1d154d; the white "universität freiburg" SVG (220×49) centred at y=7, linking to the lab. No navigation links.
2. **Banner** (`section#banner`, 0–459px): padding 6em 2em 3em = 88px 29.33px 44px; video `#bgvid` covers it (`object-fit: cover`), under a `#banner:before` layer of #42424f at opacity 0.7. Content column `.inner` max-width 80em = 1173px. A Bootstrap `my-5` spacer adds 48px, so the first heading starts at y=136.
3. **Logotype** (`h2 > span.gradient-title`, y=133–174): "DiWA" in Helvetica (Arial on Windows) 36.67px/600, text filled with `linear-gradient(0deg, rgba(42, 123, 155, 1) 0%, rgba(87, 199, 133, 1) 50%, rgba(237, 221, 83, 1) 100%)` via `background-clip: text`. The h2 carries 22px bottom padding.
4. **Title** (`h2`, y=195, 59px box): "Diffusion Policy Adaptation with World Models", same face, 36.67px/600, line-height 1, #ffffff, 22px bottom padding. Gap about 1.76px.
5. **Authors** (`p`, y=255): Roboto 17.6px/300 white links with a 1px dotted white bottom border, asterisk superscripts for equal contribution, separated by ",&nbsp;". Hover turns a name #45b8ed (University of Freiburg) or #00ff46 (UTN). Margin-bottom 44px.
6. **Venue line** (`p`, y=327, 35px tall): "Conference on Robot Learning (CoRL), 2025", Roboto 22px/700 at rgba(255,255,255,0.85).
7. **Button row** (`.button-row`, y=362; buttons at y=369, 46px tall): four pills (Paper, arXiv, Code, BibTeX) 7px apart, each translucent white at opacity 0.7 so the video shows through. Banner padding-bottom 44px, so the banner ends at y=459.
8. **Summary band** (`#approach`, from y=459, #ffffff, padding 22px 0): `.short-abstract` at y=481 with padding 22px 15% 44px, 22px/300 italic #111111, two centred lines; then the teaser figure (`img.center`, 862×437 at x=289, y=617), which the fold cuts.

Arithmetic check: 88 + 48 = 136; 136 + 59 = 195; 195 + 59 + 1.76 ≈ 255; 255 + 28 + 44 = 327; 327 + 35 = 362; 362 + 7 = 369; 369 + 46 + 44 = 459.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Freiburg Navy | #1d154d | (literal, `#banner .logos`) | wordmark bar |
| Banner Smoke | #42424f | (literal, `#banner:before`, opacity 0.7) | overlay that dims the banner video |
| Paper | #ffffff | (literal) | banner title, author links, white bands (#approach, #code, #authors), button fills |
| Band Grey | #ececec | (literal) | grey bands (#abstract, #video, #publication, #acknowledgment); button hover fill |
| Ink | #111111 | (literal, `body`) | body text, section headings, captions, in-page links |
| Button Ink | #333333 | (rendered on `.fancy-button-white`) | button glyphs and labels on the button face |
| Button Rim | #222222 | (literal) | 1px button border |
| Venue White | rgba(255,255,255,0.85) | (literal, `#banner p`) | venue line and author separators |
| Gradient Teal | #2a7b9b | (gradient stop 0%) | bottom of the "DiWA" logotype |
| Gradient Green | #57c785 | (gradient stop 50%) | middle of the logotype |
| Gradient Yellow | #eddd53 | (gradient stop 100%) | top of the logotype |
| Freiburg Blue | #45b8ed | (literal, `.hover-ufr:hover`) | author name hover |
| UTN Green | #00ff46 | (literal, `.hover-utn:hover`) | hover for UTN-affiliated authors |
| Page Under | #202024 | (literal, `body`) | body background, visible only behind the banner before the video paints |
| Footer Black | #1b1b1f | (literal, `#footer`) | footer band |
| Footer Grey | #777777 | (literal, `#footer p`) | footer contact text |
| Code Wash | rgba(144,144,144,0.075) | (literal) | BibTeX `code` background (hidden until toggled), 1px rgba(144,144,144,0.25) border |
| Photo Rim | #000000 | (inline style) | 2–3px border on round author photos |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Body | "Roboto", sans-serif (Google Fonts 300, 400) | Roboto 300, Roboto 400; 600/700 are synthesized bold | Roboto |
| Section headings | "Roboto", "Helvetica", sans-serif | Roboto, synthesized 600 | Roboto Medium |
| Banner headings | Helvetica, Georgia, 'Times New Roman', Times, serif | no web font; Helvetica maps to Arial on Windows | Arial Bold |
| Code | "Courier New", monospace | system Courier New | Courier Prime |
| Icons | Font Awesome 6 Free/Brands, Academicons | Font Awesome 6 Free 900, Brands 400, Academicons 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Logotype | `#banner h2 .gradient-title` | 2.5em = 36.67px / 600 / 1.0 | gradient text |
| Paper title | `#banner h2` | 36.67px / 600 / 1.0, padding-bottom 22px | #ffffff |
| Authors | `#banner p` + `header h2+p` | 1.2em = 17.6px / 300 (p is 200, links 300) / 1.6 | links #ffffff, separators rgba(255,255,255,0.85) |
| Venue | inline `font-size:150%; font-weight:bold` | 22px / 700 / 1.6 | rgba(255,255,255,0.85) |
| Short abstract | `.short-abstract` | 1.5em = 22px / 300 italic / 1.6 | #111111 |
| Section heading | `h2` | 1.75em = 25.67px / 600 / 1.0, padding 0.6em 0 = 15.4px | #111111 |
| Video label | `h3` | 1.35em = 19.8px / 600 / 1.0, padding 11.88px 0 | #111111 |
| Carousel intro / author name | `h4` | 1.1em = 16.13px / 600 / 1.0 | #111111 |
| Body | `body` | 11pt = 14.67px / 300 / 1.6 | #111111 |
| Abstract paragraph | `.text-w` | 1.2em = 17.6px / 400 / 1.6, justified | #111111 |
| Caption | `.caption` | 9pt = 12px / 300 / 1.6, justified | #111111 |
| Button | `.fancy-button-white` | 16px / 600 / 20px | #333333 on the face; inner links #000000 |
| Footer | `#footer p` | 14.67px / 300 | #777777 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Pill buttons | 25px | 1px #222222 | none; whole button at opacity 0.7 (0.95 on hover) |
| YouTube embed | 10px (`.video`, `!important`) | none | none; `iframe.video` padding 10px |
| Carousel videos | 15px | none | none |
| Author photos | 50% (100×100) | 2–3px #000000 (inline) | none |
| Figures | 0 | none | none |
| BibTeX code | 4px | 1px rgba(144,144,144,0.25) | none |
| Section bands | 0 | none | none |

Banner overlay: `#banner:before { background-color: #42424f; opacity: 0.7; position: absolute; inset 0; z-index: 1 }`, fading in over 3s after a 1s delay.

## Layout Metrics

- **Content column**: `.inner { width: 90%; max-width: 80em; margin: 0 auto }`, which renders 1173.33px wide at x=133 at 1440 (80em × 14.67px).
- **Banner**: padding 88px 29.33px 44px, rendered 459px tall; wordmark bar 60px; video sized with `min-width: 100%; min-height: 100%` and centred by translate(50%, 50%).
- **Bands**: each `#approach`, `#abstract`, `#video`, `#code`, `#publication`, `#authors`, `#acknowledgment` has padding 1.5em 0 = 22px top and bottom; colour alternates by id (white for approach, code, authors; #ececec for abstract, video, publication, acknowledgment). Several ids repeat (two `#approach`, three `#video`), so three grey video bands run together from y=2207 to y=4904.
- **Section titles**: `.title` wrapper 86px tall (14.67px padding top and bottom around a 56px h2).
- **Figures**: teaser 862px wide (75% of the 1149px text box, centred); overview figure fills the text box; captions span 1149px, justified.
- **Embed**: 16:9 box (`padding-bottom: 56.25%`), 1173×660 at y=2315.
- **Carousels**: Slick, one slide visible, video at 80% of the slide (939×313), 30px right margin; 20px grey arrows at x=158 and the right edge; numbered dots 20×20 below.
- **Authors**: inline-block tiles 180px wide with 1em side margins; 100px round photos, name in h4, affiliation below.
- **Footer**: #1b1b1f, padding 4em 0 2em = 58.67px 0 29.33px; inner width 50% = 720px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1680px | `.inner` 90% up to 80em | 12.5pt = 16.67px | 2.5em = 41.7px | captions 15px |
| ≤1680px (1440 render) | 133px each side | 11pt = 14.67px | 36.67px | captions 9pt = 12px |
| ≤1280px | 90% width | 11pt | 36.67px | — |
| ≤980px | 90% width | 12pt = 16px | 40px | banner p 1.0em; captions 10pt; banner `br` hidden |
| ≤736px | 90% width | 12pt | 40px | `#main` padding 3em 0 1em; footer padding 3em 0 1em |
| ≤480px | 90% width, min page width 320px | 12pt | 40px | banner p 1.25em |

## Components

- **Wordmark bar**: absolute, full width, 60px, #1d154d; centred white university SVG about 220×49 inside a 50px flex row with 10px top margin. Acts as the only header.
- **Gradient logotype** (`.gradient-title`): bold display text with `background: linear-gradient(0deg, rgba(42, 123, 155, 1) 0%, rgba(87, 199, 133, 1) 50%, rgba(237, 221, 83, 1) 100%); background-clip: text; color: transparent`; teal at the baseline, yellow at the cap height.
- **Pill button** (`.fancy-button-white`): inline-block, 16px/600 Roboto, line-height 20px, padding 3px 23px 0, radius 25px, 1px #222222 border, #ffffff fill, opacity 0.7, margin 7px 7px 0; leading icon (fa-file-pdf, ai-arxiv, fa-github, fa-book). Rendered 46px tall. Hover: border #000000, fill #ececec, opacity 0.95. Inner links #000000 600 with a 1px dotted underline.
- **Author link** (`#banner .hover-ufr`): white, 300 weight, 1px dotted white bottom border; hover #45b8ed and the border disappears.
- **Short abstract**: 22px/300 italic centred block with 15% side padding (176px at 1440), 22px top and 44px bottom padding.
- **Section band**: full-width div with #ffffff or #ececec, 22px vertical padding, centred `.title` h2 25.67px/600, content in the 1173px column.
- **Video carousel** (`.video-container-single.slick-carousel`): h3 label above, one autoplaying looped video per slide at 80% width with 15px radius and native controls; Slick arrows 20px at #333333; numbered dots.
- **Author tile** (`.authors-box`): 180px wide, 100px circular photo with a black 2–3px rim, name in 16.13px/600, affiliation in 14.67px/300.
- **Footer**: #1b1b1f band, centred #777777 contact line, white links.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Institution header | yes | navy strip with a white university wordmark; no nav links |
| Video hero | yes | full-width background video under a 70% #42424f overlay |
| Title / authors / venue | yes | white Helvetica title, gradient logotype, dotted author links, bold venue line |
| Link buttons | yes | translucent white pills with icon glyphs |
| TL;DR | present but non-standard | italic one-sentence `.short-abstract` above the teaser instead of a labelled TL;DR |
| Teaser figure | yes | three-panel comparison figure on white with a 12px justified caption |
| Abstract | yes | grey band, justified 17.6px paragraph |
| Method figure | yes | full-width overview figure with caption |
| Video embed | yes | rounded 16:9 YouTube iframe |
| Video carousels | yes | Slick carousels of real-robot and CALVIN rollouts |
| Code / downloads | yes | text plus four pill buttons for checkpoints and data |
| BibTeX | present but non-standard | a citation line with "(BibTeX)" toggle; the code block is hidden by default |
| Authors | yes | round photo tiles |
| Acknowledgment / footer | yes | grey band, then a near-black footer |
| Results table | absent from the source | results appear only as videos and figures |

## Adapting to Other Content

- **More authors**: keep the single centred 17.6px/300 line with dotted white underlines; it wraps inside the 1173px column, and the `.authors-box` tiles (180px each, about six per row at 1440) carry the full list lower down.
- **A results table**: place it in a white band under a 25.67px/600 centred h2; table text 14.67px/300 #111111, header 600, 1px rgba(144,144,144,0.25) rules, no fills. Keep it within the 1149px text box.
- **More figures**: give each its own band, alternating #ffffff and #ececec, with a 12px justified caption directly under the image.
- **Long publication or news lists**: use a grey #ececec band with left-aligned 14.67px/300 rows, titles in bold #111111 and links with the 1px dotted underline; no cards.
- **More download links**: add `.fancy-button-white` pills to the button row; on white bands they render at opacity 0.7 too, so the face looks light grey.

## Do's and Don'ts

- Do keep the navy #1d154d wordmark strip as the only header and let the banner video run edge to edge under it.
- Do dim the banner with #42424f at 0.7 so white type stays readable.
- Do alternate full-width #ffffff and #ececec bands; separation comes from colour, not rules.
- Do use the gradient only on the short project name.
- Don't put the long title in the gradient; it stays white.
- Don't give figures borders, shadows or radii; only videos are rounded (10px embed, 15px carousel).
- Don't raise body weight above 300 except in the abstract paragraph (400) and headings (600).

## Surfaces

A dark, video-filled banner under a 70% slate overlay; a navy strip on top; then flat full-width bands of white and #ececec; a near-black #1b1b1f footer. Buttons are the only translucent surface.

## Imagery

Real robot footage (a Franka arm opening drawers and pushing sliders in a tabletop rig) as the banner video and carousel rollouts; CALVIN simulation videos; pastel diagram figures (light blue, cream and mint panels with salmon nodes) on white; round headshots of the authors. Logos appear only as the university wordmark.

## Layout

Centred single column, 1173px at 1440, inside full-width colour bands. Every section title is centred; text blocks are justified within the column. The page is vertical and repetitive: band, centred heading, media, caption.

## Agent Prompt Guide

Quick colors: navy bar #1d154d, overlay #42424f at 0.7, white #ffffff, band grey #ececec, ink #111111, button rim #222222, footer #1b1b1f, footer text #777777, gradient #2a7b9b → #57c785 → #eddd53.

1. "Build a 459px banner: a 60px #1d154d bar with a centred white wordmark at the top; a full-width background video under a #42424f overlay at opacity 0.7; centred content in a 1173px column with padding 88px 29px 44px. A 36.67px/600 Helvetica 'DiWA' logotype filled with linear-gradient(0deg, rgba(42,123,155,1) 0%, rgba(87,199,133,1) 50%, rgba(237,221,83,1) 100%) clipped to text, a 36.67px/600 #ffffff title, Roboto 17.6px/300 white author links with 1px dotted underlines, a 22px/700 rgba(255,255,255,0.85) venue line."
2. "Make pill buttons: Roboto 16px/600, line-height 20px, padding 3px 23px 0, height 46px, radius 25px, 1px #222222 border, #ffffff fill, text #333333, opacity 0.7, 7px margins, leading Font Awesome icon; hover border #000000, fill #ececec, opacity 0.95."
3. "Create alternating section bands: full width, padding 22px 0, background #ffffff or #ececec; inside, a 1173px column with a centred Roboto 25.67px/600 #111111 h2 (padding 15.4px 0), a full-width figure, and a 12px/300 justified #111111 caption."

## Similar Pages

- University of Freiburg robot-learning project pages built on the same edited "Full Motion" template (navy wordmark strip, video banner, alternating grey bands).
- TEMPLATED / HTML5 UP derived lab pages with a dimmed video banner and centred band sections.

## Quick Start

```css
:root {
  --navy: #1d154d;
  --overlay: #42424f;
  --paper: #ffffff;
  --band: #ececec;
  --ink: #111111;
  --button-rim: #222222;
  --button-ink: #333333;
  --footer: #1b1b1f;
  --footer-text: #777777;
  --logo-gradient: linear-gradient(0deg, rgba(42, 123, 155, 1) 0%, rgba(87, 199, 133, 1) 50%, rgba(237, 221, 83, 1) 100%);
  --font-body: "Roboto", sans-serif;
  --font-banner: Helvetica, Georgia, "Times New Roman", Times, serif;
  --column: 80em;
  --pill-radius: 25px;
}
body { font: 300 11pt/1.6 var(--font-body); color: var(--ink); }
#banner::before { content: ""; position: absolute; inset: 0; background: var(--overlay); opacity: 0.7; }
```

## Provenance

- **URL**: https://diwa.cs.uni-freiburg.de/
- **Paper**: DiWA: Diffusion Policy Adaptation with World Models (arXiv 2508.03645), Akshay L Chandra, Iman Nematollahi, Chenguang Huang, Tim Welschehold, Wolfram Burgard, Abhinav Valada (University of Freiburg, UTN).
- **Venue**: CoRL 2025.
- **Selection reason**: the arXiv comment states acceptance at CoRL 2025 and the abstract links this project page.
- **Template credit**: `main.css` header credits "Full Motion by TEMPLATED" (CC BY 3.0); the Freiburg robot-learning group's adaptation with Bootstrap 5.3.2, Slick 1.8.1, Font Awesome 6.4.2 and Academicons.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), selector probes and a band-by-band box listing at 1440, the 1440×900 and full-page screenshots, and `main.css` and `index.html` read directly, on 2026-10-28.
