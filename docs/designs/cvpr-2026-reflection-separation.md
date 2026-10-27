# Reflection Split Slider — Style Reference

> A pane of night glass you can wipe clean with one drag.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 screenshot, scrolled captures of the full 4,457px page, and the page's inline `<style>` block (about 515 lines), which overrides Bulma 0.9.4 almost entirely. The root font size is 18px (`html { font-size: 18px }`), so every rem below is 18px-based. Color share is measured on the first 1440×900 viewport.

## Overview

A tight, modern page in Inter on a soft #fafafa ground. The hero centres a 45px extra-bold near-black title with a small two-square logo glyph, blue author links with superscripts, grey affiliations with an italic corresponding-author note, a white uppercase "CVPR 2026" pill and three white pill buttons with a hairline border. Without a break, a row of pill tabs (Example 1–4, active tab filled #0f1419) and a smaller Transmission / Reflection toggle sit over a large 820×547 before/after slider: the input on the left, the separated layer on the right, a white 2px divider with a round ‹ › handle and frosted dark labels in the corners. Below, everything stays on the same #fafafa: an 800-weight 36px "Abstract" over a 780px justified paragraph, a "Method" figure with pulsing red hotspots that open component details, a "Visual Comparison" slider with numbered round tabs and "Compare with" chip rows, a "Quantitative Comparison" table image with best and second-best highlights, a white BibTeX box and a hairline-topped footer.

## First Viewport

Color share (1440×900, 8-color quantize): page #fafafa 67.9% (plus #fafaf9 4.1%, #fefefd 3.3% and traces), night #060412 20.4% (the dark slider image), slate grey #69676b 3.0% (text and the image's mid tones). The blue author links, the slider's city lights and the black active tabs are each under 1%.

Anatomy in DOM order (`.sec-hero` padding 72px 36px 27px; `.hero-inner` max-width 1100px, centred):

1. **Title** — `h1.publication-title`, Inter 45px (2.5rem) / 800 / line-height 54px, letter-spacing −0.022em (−0.99px), #0f1419, two lines (y=95–203); an inline `.site-logo` image 45px square (two overlapping rounded squares, red over blue) with 15.75px right margin, tilting −8° on title hover. Gap 31.5px.
2. **Authors** — `.publication-authors` 18.9px (1.05rem) / 500, `.author-block a` #2563eb with superscripts in #444444, comma-separated with 0.3rem side margins; hover #1d4ed8 with a dashed underline (y=240–264). Gap 13px.
3. **Affiliations** — `.affiliations` 16.56px (0.92rem) / 500 #777777, superscript numbers, plus `.corresp-note` "* Corresponding author" 14.4px italic #999999 (y=277–305). Gap 22px.
4. **Venue pill** — `.venue-badge`, "CVPR 2026", 15.3px / 600 uppercase, letter-spacing 0.06em, #555555 on #ffffff, 1px #e3e3e3 border, 999px radius, padding 4.5px 16.2px (y=327–361). Gap 27px.
5. **Link buttons** — `.publication-links` flex, gap 9.9px: `a.pub-btn` "Paper" (Academicons arXiv), "Code" (GitHub), "🤗 Models"; Inter 16.2px / 600, letter-spacing 0.01em, #1a1a1a on #ffffff, 1px #d8d8d8, 999px radius, padding 9.9px 20.7px, shadow `0 1px 2px rgba(0,0,0,0.03)`; 46px tall (y=388–434). Gap 54px (hero bottom padding plus section top padding).
6. **Example tabs** — `.ex-tab` ×4, 15.3px / 600, padding 7.2px 18px, 999px radius; inactive #555555 on #ffffff with 1px #d8d8d8, active #ffffff on #0f1419 with `0 1px 3px rgba(0,0,0,0.15)` (y=488–523). Gap 19px.
7. **Layer toggle** — `.comp-tab` ×2 ("Transmission", "Reflection"), 14.4px / 600, padding 5.76px 15.3px, same pill states (y=542–573). Gap 9px.
8. **Slider** — `.comparison-frame` 820×547 (aspect 3:2) at x=310, y=582, radius 10px, #111111 behind, shadow `0 2px 8px rgba(0,0,0,0.06), 0 0 0 1px rgba(0,0,0,0.04)`; the fold cuts it at about 60% of its height.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Soft White | #fafafa | `html, body`, `.sec-hero`, `.sec-content`, `.site-footer` | page and every section background |
| Ink | #0f1419 | `.publication-title`, `.section-title`, active tabs | title, section titles, active tab fill, button hover fill |
| Body Slate | #3a3f44 | `html, body` color | default text |
| Hero Ink | #222222 | `.sec-hero` color | hero text default |
| Paragraph Grey | #4a4a4a | `.section-text` | abstract and section text |
| Author Blue | #2563eb | `.author-block a` | author links |
| Author Hover | #1d4ed8 | `.author-block a:hover` | hover color and dashed underline |
| Muted Grey | #777777 | `.affiliations`, `.cmp-row-label` | affiliations, "Compare with" label |
| Caption Grey | #888888 | `.figure-caption`, `.teaser-intro` | italic captions |
| Faint Grey | #999999 | `.corresp-note`, `.site-footer p` | corresponding-author note, footer text |
| Tab Grey | #555555 | `.ex-tab`, `.comp-tab`, `.venue-badge` | inactive tab text, venue pill text, method hint |
| Button Ink | #1a1a1a | `.pub-btn` | button labels |
| White | #ffffff | buttons, tabs, `pre`, `.venue-badge` | pill fills, BibTeX box, slider handle |
| Pill Border | #d8d8d8 | `.pub-btn`, `.ex-tab`, `.comp-tab` | 1px pill outlines |
| Hairline | #e3e3e3 | `.venue-badge`, `pre`, `.arch-algo` | venue pill and code box borders |
| Footer Rule | #dddddd | `.site-footer` border-top | footer hairline |
| Hotspot Red | #c0392b | `.arch-hotspot`, `.method-hint b` | pulsing figure hotspots (at 0.85 alpha), "red dot" hint word |
| Slider Black | #111111 | `.comparison-frame` | slider background behind images |
| Label Glass | rgba(15,20,25,0.7) | `.comp-label` | frosted "Input" / "Transmission" labels |
| Footer Link | #3274d8 | `.site-footer a` | template link |
| Selection Pink | #ffd2cc | `::selection` | text selection |
| Algo Highlight | #ffeec8 | `.arch-algo .algo-hilite` | highlighted terms in the pseudocode detail panel |
| Night | #060412 | (screenshot) | dark tone of the hero slider image |

## Tokens — Typography

- **Sans:** declared `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif` with `font-feature-settings: 'kern', 'liga', 'cv11'`; rendered Inter 400, 500, 600, 700, 800 from Google Fonts. Substitute: Inter is free; if replacing, Geist.
- **Mono:** `'JetBrains Mono', 'SFMono-Regular', Menlo, …`; rendered JetBrains Mono 400 for BibTeX and the pseudocode panel. Substitute: IBM Plex Mono.
- **Icons:** Font Awesome 6.5 (brands), Academicons.

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `.publication-title` | 45px (2.5rem) / 800 / 54px, −0.022em |
| Authors | `.publication-authors` | 18.9px / 500 / 28.35px |
| Affiliations | `.affiliations` | 16.56px / 500 |
| Venue pill | `.venue-badge` | 15.3px / 600 uppercase, +0.06em |
| Buttons | `.pub-btn` | 16.2px / 600, +0.01em |
| Example tabs | `.ex-tab` | 15.3px / 600 |
| Layer tabs | `.comp-tab` | 14.4px / 600 |
| Section titles | `.section-title` | 36px (2rem) / 800 / 54px, −0.018em, centred |
| Abstract | `.abstract-text` | 17.1px (0.95rem) / 400 / 1.75, justified, max 780px |
| Captions | `.figure-caption`, `.teaser-intro` | 15.84px (0.88rem) italic / 400, #888888 |
| Slider labels | `.comp-label` | 14.04px / 600 |
| BibTeX | `.sec-content pre` | 14.76px (0.82rem) / 1.6 JetBrains Mono |
| Footer | `.site-footer p` | 15.3px / 400 |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Buttons, tabs, venue pill, slider labels | radius 999px |
| Buttons | 1px #d8d8d8, padding 9.9px 20.7px, shadow `0 1px 2px rgba(0,0,0,0.03)`; hover `0 4px 10px rgba(0,0,0,0.12)` and `translateY(-1px)` |
| Active tab | shadow `0 1px 3px rgba(0,0,0,0.15)` |
| Slider frame | radius 10px, `0 2px 8px rgba(0,0,0,0.06), 0 0 0 1px rgba(0,0,0,0.04)`, aspect-ratio 3/2 |
| Slider handle | 2px rgba(255,255,255,0.9) line with `0 0 6px rgba(0,0,0,0.4)`; 34px white circle with `0 2px 6px rgba(0,0,0,0.35)` and "‹ ›" glyphs |
| Figures, table image | radius 12px |
| Code boxes | radius 10px, 1px #e3e3e3, padding 22.5px, shadow `0 1px 3px rgba(0,0,0,0.03)` |
| Hotspots | 12px circles, 1.5px white border, pulsing 7px ring |
| Footer | 1px #dddddd top rule |

## Layout Metrics

- **Hero:** `.sec-hero` padding 72px 36px 27px (4rem 2rem 1.5rem at 18px root); inner max-width 1100px; title margin 22.5px 0 31.5px.
- **Sections:** `.sec-content` padding 27px; `.section-inner` max-width 960px (x=240–1200); section titles margin-bottom 27px.
- **Sliders:** `.teaser-stack` max-width 820px (x=310–1130); frames 820×547.
- **Abstract:** 780px max, centred (x=330).
- **Method figure:** 960px wide with hotspots; in detail mode it shrinks to 360–560px beside a 320px+ text column with a 2rem gap.
- **Quantitative table:** image at the full 960px, 12px radius, with its own Transmission / Reflection toggle.
- **Footer:** margin-top 54px, padding 27px 18px 36px.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| >768px | 36px (hero), 27px (sections) | 18px root | 45px | as described |
| 641–768px | 22.5px | 18px root | 28.8px (1.6rem) | hero padding 2.5rem 1.25rem; section titles 27px |
| ≤640px | 21.25px | 17px root | 27.2px (1.6rem at 17px) | everything rem-based shrinks by 1/18; method detail mode stacks below 720px |

## Components

- **Pill link button:** inline-flex, #ffffff, 1px #d8d8d8, 999px radius, padding 0.55rem 1.15rem, Inter 16.2px / 600 #1a1a1a, icon left with 0.5rem gap, faint shadow; hover inverts to #0f1419 fill and #ffffff text, lifts 1px, shadow `0 4px 10px rgba(0,0,0,0.12)`.
- **Venue pill:** #ffffff, 1px #e3e3e3, 999px radius, padding 0.25rem 0.9rem, uppercase 15.3px / 600 #555555 with 0.06em tracking.
- **Segmented pill tabs:** a centred flex row of 999px pills; inactive #ffffff / #555555 / 1px #d8d8d8 (hover border and text #0f1419), active #0f1419 / #ffffff with a small shadow. Example tabs 15.3px; layer tabs 14.4px; numbered comparison tabs are the same pills with single digits.
- **Before/after slider:** 3:2 frame, 10px radius, #111111 base; the overlay image clipped with `clip-path: inset(0 calc(100% - var(--pos)) 0 0)`; 2px white divider and 34px white round handle with "‹ ›"; `cursor: ew-resize`; frosted labels rgba(15,20,25,0.7) with 8px backdrop blur, 999px radius, 14.04px / 600 white, 10px from the bottom corners.
- **Hotspot figure:** pulsing 12px #c0392b dots (0.85 alpha) over the method figure; clicking swaps to a side-by-side detail view with a dark "← back" pill and a component title, or a white JetBrains Mono pseudocode panel with #ffeec8 highlights.
- **Code box:** #ffffff, 1px #e3e3e3, 10px radius, padding 1.25rem, JetBrains Mono 14.76px / 1.6.
- **Footer:** #fafafa with a 1px #dddddd top rule, centred 15.3px #999999 credit with a #3274d8 link.
- **Reveal:** sections fade up 24px over 0.7s as they enter the viewport.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title with logo glyph | Yes | 45px Inter 800, inline 1em logo |
| Authors / affiliations | Yes | blue links, grey affiliations, italic note |
| Venue | Yes | white uppercase pill |
| Link buttons | Yes | three white pills (Paper, Code, Models) |
| Teaser | Yes | four-example before/after slider with layer toggle |
| Abstract | Yes | 780px justified block |
| Method figure | Yes | interactive hotspots with detail panels |
| Visual comparison | Yes | ten-example slider with baseline chips |
| Results table | Yes (non-standard) | LaTeX table as an image with best/second-best fills and a layer toggle |
| BibTeX | Yes | white code box |
| Video | No (absent from the source) | |
| Footer | Yes | hairline footer with Academic Project Page Template credit |

## Adapting to Other Content

- **More authors:** the inline-block author list wraps; keep the 18.9px / 500 size and move affiliations to their own line, as here.
- **Results table in HTML:** in the 960px column, Inter 16.2px tabular numbers, header row 600 on #ffffff, 1px #e3e3e3 rules inside a 12px-radius white box; mark best with #ffd2cc and second-best with #ffeec8 fills, matching the page's selection and highlight tints.
- **Video teaser:** place it inside the same 820px 3:2 frame with the 10px radius and frame shadow; keep the example pills above it.
- **Award:** add a second venue-style pill next to "CVPR 2026"; keep it white with #555555 text.
- **News:** a short list in a white code-box-style card (1px #e3e3e3, 10px radius) under the buttons.

## Do's and Don'ts

- Do make every control a 999px pill, with #0f1419 as the single active fill.
- Do let the interactive slider be the first thing after the buttons; there is no static teaser.
- Do keep the page on one #fafafa surface; separate sections by space and bold 36px titles only.
- Don't add colour to buttons; they are white with a #d8d8d8 hairline and invert to #0f1419 on hover.
- Don't use more than one blue; #2563eb is for author links only (the footer's #3274d8 is a template leftover).
- Don't drop the slider's frosted corner labels; they tell the reader which side is which.

## Surfaces

One continuous #fafafa surface with white pills, a white BibTeX box, a dark #111111 slider frame and a hairline-topped footer. Shadows are faint and only on controls and frames.

## Imagery

Night cityscapes and street scenes photographed through glass, separated into transmission and reflection layers; a colourful method diagram with red and blue U-Nets and red hotspots; a LaTeX results table with pink and peach best-value fills.

## Layout

A centred hero, then 960px sections on the same background, with sliders capped at 820px and the abstract at 780px. Rendered height about 4,460px.

## Agent Prompt Guide

Quick colors: page #fafafa, title and active #0f1419, text #4a4a4a, authors #2563eb (hover #1d4ed8), muted #777777, captions #888888, pill border #d8d8d8, hairline #e3e3e3, hotspot #c0392b.

1. "Create a hero on #fafafa: a 45px Inter weight-800 title in #0f1419 with −0.022em tracking and an inline 1em logo, 18.9px weight-500 author links in #2563eb, 16.56px #777777 affiliations, a white uppercase 'CVPR 2026' pill (1px #e3e3e3, 999px radius, 15.3px weight 600, #555555), then white pill buttons: 1px #d8d8d8, padding 0.55rem 1.15rem, Inter 16.2px weight 600 #1a1a1a, hover fill #0f1419 with #ffffff text and a 1px lift."
2. "Build pill tabs over a before/after slider: tabs 15.3px weight 600, inactive #ffffff with #555555 text and 1px #d8d8d8, active #0f1419 with #ffffff text; the slider an 820px 3:2 frame, 10px radius, #111111 base, a 2px white divider with a 34px white circular handle, and frosted labels rgba(15,20,25,0.7) with 8px blur in the bottom corners."
3. "Lay out sections on #fafafa in a 960px column: centred 36px Inter weight-800 titles in #0f1419, a 780px justified abstract at 17.1px with 1.75 line height in #4a4a4a, figures with 12px radius and 15.84px italic #888888 captions, and a white JetBrains Mono BibTeX box with 1px #e3e3e3 and 10px radius."

## Similar Pages

- Academic Project Page Template derivatives restyled with Inter and pill controls.
- Image-restoration pages built around an interactive before/after slider (dehazing, deraining, reflection removal).

## Quick Start

```css
:root {
  --bg: #fafafa;
  --ink: #0f1419;
  --text: #3a3f44;
  --paragraph: #4a4a4a;
  --author: #2563eb;
  --author-hover: #1d4ed8;
  --muted: #777777;
  --caption: #888888;
  --tab-text: #555555;
  --pill-border: #d8d8d8;
  --hairline: #e3e3e3;
  --hotspot: #c0392b;
  --slider-bg: #111111;
  --font-sans: 'Inter', -apple-system, 'Segoe UI', sans-serif;
  --font-mono: 'JetBrains Mono', Menlo, monospace;
  --root-size: 18px;
  --title-size: 45px;
  --h2-size: 36px;
  --radius-pill: 999px;
  --radius-frame: 10px;
  --radius-figure: 12px;
  --column: 960px;
  --slider: 820px;
}
```

## Provenance

- **URL:** https://brian90709.github.io/diff-reflection-separation/
- **Paper:** Reflection Separation from a Single Image via Joint Latent Diffusion (arXiv 2606.04107), Zheng-Hui Huang, Zhixiang Wang, Yu-Lun Liu, Yung-Yu Chuang.
- **Venue:** CVPR 2026 (venue pill on the page).
- **Selection reason:** existing verified entry; arXiv 2606.04107 comment reads "CVPR 2026. Project page: ..."; project page linked in the comment.
- **Template credit:** footer says the page was built using the Academic Project Page Template, heavily restyled.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share, the 1440×900 screenshot, scrolled full-page captures, the inline `<style>` block and page HTML; 2026-10-28.
