# CityDreamer4D — Style Reference

> A research dossier filed inside a personal blog: a white card on grey, a red-lit header with a fact sheet of venue, DOI and stars, and short red dashes marking every section.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of the rendered elements and pseudo-elements, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the site stylesheet `css/style.min.3397b01f5b3085fa2770edf8fd6971b4.css` (Bootstrap 5 plus the "Infinite Script" Hugo theme, 423 KB) read with `index.html`. The page sits in the author's blog shell and has a moon button that sets `html[data-theme=dark]`; the default render is light and the dark values are listed separately. The STARS and VIEWS numbers are fetched live (VIEWS read 14392–14396 across renders).

## Overview

A project page (4,072px) rendered as one large white post card (1296px, radius 12px) on a #f1f1f1 blog background, under a white 84px site header with a red "Infinite Script" wordmark. The card's header region is a soft wash, `radial-gradient(circle at 4% 0, rgba(231,76,60,.15), transparent 28%)` over a white-to-grey diagonal, holding a breadcrumb, a red uppercase "RESEARCH" kicker, a huge Lato title "CityDreamer4D" (62px, tight tracking), a grey subtitle, authors and affiliation, a red primary "Paper" button and an outlined "Code" button, and a 132px isometric city icon on the right. Below, a ruled metadata strip lists VENUE / RELEASED / ARXIV / DOI / STARS / VIEWS / TOPICS (topics as tinted tags), then a DATASETS row of external links. The body opens with a red-tinted TL;DR callout with a 4px red left bar, followed by sections whose h2s carry an 18×4px red pill dash: Abstract, a two-up video carousel, a dark spotlight video, Citation (paper thumbnail + BibTeX), related-project cards, and a dark two-tone footer. The only accent is #e74c3c on slate text #2f3c4e and grey #6d7683.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 23.1%, grey page #f1f1f1 22.6%, pale greys #f9f8f8 21.8% and #fcfcfb 5.2% (the header-card gradient), warm tint #f8f5f4 20.5% (the red radial wash and TL;DR fill), mid grey #d3ccce 6.4% (borders, text anti-aliasing). The red accent and the dark title are too small in area to form clusters.

Anatomy in DOM order (desktop 1440px). The Bootstrap container is 1320px with 12px padding (content x=72–1368).

1. **Site header** (`div#header`, 0–84px): white, 1px #d3d5d7 bottom border, `box-shadow: 0 0 5px 0 #e2e3e4`, plus a 3px multicolor strip along the top edge (`background-image: url(../images/header-top.webp)`, repeat-x, `background-size: auto 3px`). "Infinite Script" wordmark Lato 30px/700 #e74c3c at x=72; nav Home / Blog / Projects / About / Contact 15px #2f3c4e at line-height 84px, 30px apart; a 36px round theme button (#f9f9f9, 1px #d3d5d7, moon icon #e74c3c). Margin-bottom 60px.
2. **Post card** (`div.post.single-post.project-page`, x=72, y=144, 1296px wide): white, 1px #d3d5d7, radius 12px, `box-shadow: 0 0 5px 0 #e2e3e4`.
3. **Header region** (`div.project-header.paper-header`, y=145–648): padding 30px 34px 0 (content x=107–1333), background `radial-gradient(circle at 4% 0, rgba(231,76,60,.15), transparent 28%), linear-gradient(135deg, #fff, #f1f1f1)`.
4. **Breadcrumb** (y=175): "Projects › Research", Lato 12px/600 #6d7683; margin-bottom 14px.
5. **Kicker** (`.paper-hero`, padding 6px 0 24px; kicker at y=213): layer icon + "RESEARCH" 11px/700 uppercase, letter-spacing 1.1px, #e74c3c; 12px below.
6. **Title** (`h1.title`, y=242, 61px tall): Lato 62px/800 (synthesised; only Lato 400 loads), line-height 0.98, letter-spacing -2.79px (-0.045em), #2f3c4e; margin-bottom 18px.
7. **Subtitle** (y=321): 21px/400, line-height 1.45, #6d7683, max-width 640px; 20px below.
8. **Authors** (y=371): 15px; names 650 #2f3c4e separated by 600 #888888 middle dots with 6px margins; 20px below. **Affiliation** (y=416): 13px #6d7683.
9. **Buttons** (`.paper-links`, y=460, 40px tall, gap 9px): Paper (red primary, PDF icon) and Code (outlined, GitHub icon). The hero grid's right column holds the 132×132px city icon at x=1201, y=213. The hero ends at y=524 after 24px padding.
10. **Metadata strip** (`dl.paper-record`, y=524–598): 1px #ecedee top and bottom rules, padding 16px 0, flex with gaps 16px 40px; labels 10.5px/700 uppercase, letter-spacing 0.945px, #888888; values 13.5px #2f3c4e with tabular numerals; topics as tags.
11. **Datasets row** (`.paper-resources`, y=598–648): 1px #ecedee top rule, padding 15px 4px 16px; "DATASETS" 11px/700 uppercase #6d7683 with a database icon on the left; OSM / GoogleEarth / CityTopia links 12px/600 #2f3c4e with 9px #888888 external-link icons on the right.
12. **TL;DR callout** (y=689, inside `div.body` padding 40px 62px 52px → x=135–1305): see Components; 46px below it the "Abstract" h2 at y=831.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Theme Red | #e74c3c | --theme-color | wordmark, theme-button icon, kicker, primary button fill, TL;DR left bar and label, h2 dash, hover color of links and outline buttons, spotlight play hover |
| Slate | #2f3c4e | --primary-text-color | title, h2, nav links, author names, metadata values, TL;DR text, outline button text, dataset links |
| Grey Text | #6d7683 | --secondary-text-color | body and abstract text, subtitle, breadcrumb, affiliation, DATASETS label, outline button icons |
| Label Grey | #888888 | --tertiary-border-color | metadata labels, author separators, external-link icons |
| Page Grey | #f1f1f1 | --secondary-bg-color | page background, header-card gradient end, BibTeX header bar |
| Card White | #ffffff | --primary-bg-color | site header, post card, related cards, manuscript preview |
| Tertiary | #f9f9f9 | --tertiary-bg-color | theme button fill |
| Border | #d3d5d7 | --primary-border-color | site header bottom border, post card, outline button, BibTeX frame, related cards |
| Hairline | #ecedee | --secondary-border-color | metadata strip and datasets row rules |
| Shadow Grey | #e2e3e4 | --primary-shadow-color | site header and post card shadow |
| Code Grey | #f7f7f7 | (Chroma `pre` background) | BibTeX code area |
| Colophon | #252a31 | --colophon-bg-color | footer upper band, spotlight gradient start |
| Footer Black | #1b1f25 | --footer-bg-color | footer legal bar |
| Spotlight Black | #0d1014 | (literal) | spotlight gradient end |
| Footer Text | #f1f1f1 | --footer-text-color | footer text |
| Tag Slate | rgba(84,110,122,0.15) | `.post-tag-3` | "4D Generation", "City Generation" topic tags |
| Tag Blue | rgba(30,136,229,0.12) | `.post-tag-1` | "NeRF" tag |
| Tag Orange | rgba(255,87,34,0.12) | `.post-tag-0` | "AIGC" tag |
| Dark Card | #20242b | --primary-bg-color (dark) | post card in dark theme |
| Dark Page | #15191e | --secondary-bg-color (dark) | page background in dark theme |
| Dark Text | #f3f5f7 | --primary-text-color (dark) | headings in dark theme |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text / headings | "Lato", "Droid Arabic Kufi", Arial, sans-serif | Lato 400 only (self-hosted); 600–800 weights are synthesised bold | Lato (Google Fonts, with real 700/900) |
| Code | SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", Courier New, monospace | system Consolas on Windows | JetBrains Mono |
| Icons | Font Awesome 7 | Free 400/900, Brands 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `div.paper-hero h1.title` | clamp(44px, 4.4vw, 62px) → 62px / 800 / 0.98, letter-spacing -0.045em | #2f3c4e |
| Subtitle | `div.paper-hero p.project-header-subtitle` | clamp(17px, 1.5vw, 21px) → 21px / 400 / 1.45 | #6d7683 |
| Section heading | `div.post.project-page div.body > h2` | 25px / 700 / 1.3, letter-spacing -0.5px (-0.02em), margin-top 54px | #2f3c4e |
| Body / abstract | `div.post.project-page div.body > p` | 16px / 400 / 1.85, max-width 900px | #6d7683 |
| TL;DR text | `div.body > p:first-child` | 16px / 400 / 1.7 | #2f3c4e |
| TL;DR label | `div.body > p:first-child strong` | 11px / 700 uppercase, letter-spacing 0.88px | #e74c3c |
| Kicker | `span.project-header-kicker` | 11px / 700 uppercase, letter-spacing 0.1em | #e74c3c |
| Authors | `p.paper-authors` | 15px / 1.7; names 650 | #2f3c4e |
| Affiliation | `p.paper-affiliation` | 13px / 400 | #6d7683 |
| Button | `a.paper-link` | 13px / 650 | primary #ffffff, outline #2f3c4e |
| Metadata label | `dl.paper-record dt` | 10.5px / 700 uppercase, letter-spacing 0.09em | #888888 |
| Metadata value | `dl.paper-record dd` | 13.5px / 400 / 1.35, tabular-nums | #2f3c4e |
| Topic tag | `a.post-tag` | 13px / 500 | #2f3c4e |
| Breadcrumb | `nav.post-breadcrumbs a` | 12px / 600 | #6d7683 |
| Wordmark | `.site-title a` | 30px / 700 | #e74c3c |
| Nav link | `#header nav a` | 15px / 400 | #2f3c4e |
| BibTeX | `pre.chroma` | 11.5px / 1.35 | #6d7683 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Post card | 12px | 1px #d3d5d7 | 0 0 5px 0 #e2e3e4 |
| Site header | 0 | 1px #d3d5d7 bottom; 3px multicolor image strip on top | 0 0 5px 0 #e2e3e4 |
| Primary button | 8px | 1px #e74c3c | 0 9px 24px rgba(231,76,60,.22) |
| Outline button | 8px | 1px #d3d5d7 | none |
| Theme button | 50% (36px) | 1px #d3d5d7 | hover 0 5px 14px rgba(24,32,43,.12) |
| TL;DR callout | 8px | 1px rgba(231,76,60,.2), left 4px #e74c3c | none |
| h2 dash | 800px (pill), 18×4px | none | none |
| Topic tags | 4px | none | none |
| Carousel counter | 800px pill | none | none |
| Spotlight video | 12px | none | none; play button 0 14px 34px rgba(0,0,0,.34) |
| Citation frame / manuscript preview / related cards | 12px | 1px #d3d5d7 | none |
| Related thumbnail | 6px | none | none |

## Layout Metrics

- **Page**: Bootstrap container 1320px with 12px padding at ≥1400px → post card 1296px at x=72; site header 84px tall with 60px margin below.
- **Header region**: padding 30px 34px 0 → content x=107–1333 (1226px). Hero grid `minmax(0,1fr) auto`, gap clamp(24px, 3vw, 44px) → 43.2px at 1440; columns 1051px copy + 132px icon; padding 6px 0 24px.
- **Header spacing**: breadcrumb→kicker 14px + 6px, kicker→title 12px, title→subtitle 18px, subtitle→authors 20px, authors→affiliation 20px, affiliation→buttons 24px.
- **Body**: `div.body` padding 40px 62px 52px → text column x=135–1305 (1170px); paragraphs cap at 900px. h2 margin 54px 0 16px; TL;DR margin-bottom 46px.
- **Carousel**: inner 1180px (bleeds 5px each side), two 590px items per view with 5px side padding, 326px tall; 68px-wide full-height prev/next zones; counter pill bottom-left.
- **Spotlight video**: 1170 × 658px (16:9), margin 24px 0.
- **Citation**: grid `190px 964px`, gap 16px: manuscript preview card left, BibTeX frame right.
- **Related**: two 579px cards, gap 12px, padding 10px 14px 10px 10px, 76×52px thumbnails.
- **Footer**: upper band #252a31, padding 52px 0 44px, margin-top 60px, three-column grid 620/237/310px with 64px gap; legal bar #1b1f25, 11px, padding 17px 0.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1400px (incl. 1440) | container 1320px, header padding 34px, body 62px | 16px | 62px | hero copy + 132px icon |
| 1200–1399px | container 1140px | 16px | 4.4vw ≈ 53–62px | — |
| 992–1199px | container 960px | 16px | 44px floor (4.4vw reaches 44px at 1000px) | — |
| 768–991px | container 720px | 16px | 44px | — |
| ≤767px | header 25px 24px 27px; body 28px 22px 40px | 15px | 34px (`div.project-header h1.title`) | datasets row stacks; citation grid 150px + 1fr; TL;DR 15px with 14px 16px padding |
| ≤575px | — | 15px | 34px | hero single column, icon hidden; metadata gaps 14px 26px |
| ≤420px | — | 15px | 34px | buttons flex 1 1 112px, centred; citation single column, manuscript preview hidden |

## Components

- **Primary button** (`a.paper-link.paper-link-primary`): inline-flex, gap 8px, min-height 40px, padding 8px 15px, radius 8px, #e74c3c fill and border, white Lato 13px/650 with a white file-PDF icon, `box-shadow: 0 9px 24px rgba(231,76,60,.22)`. Hover: `filter: brightness(1.08)`, translateY(-2px).
- **Outline button** (`a.paper-link`): same metrics, background rgba(255,255,255,.035), 1px #d3d5d7, #2f3c4e text, #6d7683 icon. Hover: background rgba(231,76,60,.11), border rgba(231,76,60,.48), text #e74c3c, translateY(-2px).
- **Kicker**: Font Awesome layer icon (5px right margin) + uppercase 11px/700 #e74c3c, letter-spacing 0.1em.
- **Metadata strip** (`dl.paper-record`): flex-wrap row of label/value pairs between 1px #ecedee rules; labels 10.5px/700 uppercase #888888, 3px above 13.5px #2f3c4e values; links in values turn #e74c3c and underline on hover.
- **Topic tag** (`a.post-tag`): 13px/500 #2f3c4e, padding 2px 10px, radius 4px, translucent fill by category (rgba(84,110,122,.15), rgba(30,136,229,.12), rgba(255,87,34,.12)); 5px gaps.
- **TL;DR callout** (`div.body > p:first-child`): padding 16px 20px, radius 8px, 1px rgba(231,76,60,.2) border with a 4px #e74c3c left border, background `linear-gradient(90deg, rgba(231,76,60,.1), rgba(231,76,60,.024))`; label "TL;DR:" 11px/700 uppercase #e74c3c with 7px right margin, then 16px #2f3c4e text.
- **Section heading**: 25px/700 #2f3c4e h2 preceded by an inline 18×4px #e74c3c pill (`::before`, margin 0 11px 6px 0).
- **Video carousel**: two 16:9 clips per view with rounded corners, translucent round arrow buttons over the outer edges, a "1 / 4" counter pill (rgba(0,0,0,.46), white 11px/600, radius 800px) at bottom-left.
- **Spotlight video** (`div.spotlight`): radius 12px, background `radial-gradient(120% 120% at 18% 8%, rgba(231,76,60,.26), transparent 58%), linear-gradient(135deg, #252a31, #0d1014)`; poster image covers it; centred 72px round play button rgba(0,0,0,.46) with 1px rgba(255,255,255,.38) border and `backdrop-filter: blur(10px)`; hover turns it #e74c3c and scales 1.08 while the poster dims (`brightness(.82)`) and scales 1.04; a "YOUTUBE" source pill bottom-left.
- **Citation block**: 190px manuscript thumbnail card (radius 12px, 1px #d3d5d7) beside a BibTeX frame (radius 12px, 1px #d3d5d7) whose header bar is #f1f1f1 with a quote icon, "BibTeX" label and a small "Copy" button; code on #f7f7f7 at 11.5px.
- **Related card** (`a.paper-related-card`): flex, gap 12px, 1px #d3d5d7, radius 12px, 76×52px thumbnail radius 6px, 14px/700 title over a grey line, trailing chevron #888888 that turns red and shifts 3px on hover.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Site header / blog shell | yes | white 84px bar, red wordmark, slate nav, round theme button, 3px multicolor strip |
| Breadcrumb | yes | 12px grey "Projects › Research" |
| Kicker / category | yes | red uppercase "RESEARCH" with icon |
| Title / subtitle / authors / affiliation | yes | 62px Lato title with tight tracking, grey subtitle, dotted author list |
| Project icon | yes | 132px isometric city image right of the title |
| Link buttons | yes | red primary Paper, outlined Code |
| Metadata strip | yes | ruled row: venue, release, arXiv, DOI, stars, views, topics |
| Datasets links | yes | ruled row with external-link icons |
| TL;DR | yes | red-tinted callout with 4px red left bar |
| Abstract | yes | grey 16px text, line-height 1.85, max 900px |
| Video carousel | yes | two-up clips with arrows and counter pill |
| Spotlight video | yes | dark red-lit 16:9 panel with glass play button |
| Results tables | absent from the source | results are shown in videos only |
| BibTeX | yes | framed code block with manuscript thumbnail |
| Related projects | yes | two thumbnail cards |
| Footer | yes | dark two-band footer with kicker, site intro, nav and contact |
| Dark mode | yes | moon button switches to `html[data-theme=dark]` |

## Adapting to Other Content

- **More authors**: keep the single `p.paper-authors` line at 15px with 650-weight names and #888888 middle dots; it wraps inside the 1051px hero copy column. Put multiple affiliations on one 13px #6d7683 line separated by middle dots.
- **More links**: add outlined `a.paper-link` buttons after the red primary (gap 9px); only one button is red.
- **A results table**: place it in the 1170px body under a dashed h2; header row on #f1f1f1 with 10.5px/700 uppercase #888888 labels, body 13.5px #2f3c4e tabular numerals, rows divided by 1px #ecedee, best values 700 #e74c3c; wrap in the same 12px-radius 1px #d3d5d7 frame as the BibTeX block.
- **Figures**: full 1170px body width with 12px radius; caption 13px #6d7683 below.
- **News or a long publication list**: reuse the related-card pattern (76×52px thumbnail, 14px/700 title, grey meta line, trailing chevron) in a two-column grid at 579px per card.
- **More metadata**: add `dt`/`dd` pairs to the ruled strip; it wraps with 16px row and 40px column gaps.

## Do's and Don'ts

- Do keep everything inside one white 12px-radius card on the #f1f1f1 page.
- Do use #e74c3c only for the kicker, primary button, TL;DR bar and label, h2 dashes and hover states.
- Do mark each section h2 with the 18×4px red pill.
- Do present venue, DOI and counts as the ruled label/value strip, not as badges.
- Don't set body text in slate; paragraphs are grey #6d7683 and only headings and data values are #2f3c4e.
- Don't add a second accent; topic tags use pale translucent tints only.
- Don't center the header; the title block is left-aligned with the icon on the right.

## Surfaces

Grey page #f1f1f1; white header bar and white post card with a 5px soft grey shadow; the card's header region is a white-to-grey diagonal with a red radial glow at its top-left; a pink-tinted gradient TL;DR box; a dark red-lit spotlight panel; a #f1f1f1 BibTeX header bar over #f7f7f7 code; a two-tone charcoal footer (#252a31, #1b1f25).

## Imagery

A small isometric neon city icon in the header, aerial video clips of generated city blocks (grey and brick buildings, roads, cars) in a two-up carousel, a dark title-card video poster with gradient lettering and NTU / S-Lab logos, a paper first-page thumbnail, and two related-project thumbnails. All media have 6–12px rounded corners.

## Layout

Blog shell with a fixed-width 1296px content card. Inside: a left-aligned header block with a right-hand icon, two ruled data rows, then a 1170px body column holding the TL;DR, abstract (900px measure), carousel, spotlight video, citation grid and related cards, each section introduced by a dashed h2 54px below the previous content.

## Agent Prompt Guide

Quick colors: page #f1f1f1, card #ffffff, accent #e74c3c, headings #2f3c4e, body text #6d7683, labels #888888, borders #d3d5d7, hairlines #ecedee, footer #252a31.

1. "Build a project header inside a white card (radius 12px, 1px #d3d5d7, shadow 0 0 5px 0 #e2e3e4) on a #f1f1f1 page. Header region padding 30px 34px 0 with background radial-gradient(circle at 4% 0, rgba(231,76,60,.15), transparent 28%), linear-gradient(135deg, #ffffff, #f1f1f1). Stack: 12px/600 #6d7683 breadcrumb; 11px/700 uppercase #e74c3c kicker; Lato 62px/800 title, line-height 0.98, letter-spacing -0.045em, #2f3c4e; 21px #6d7683 subtitle; 15px authors with 650 names; buttons 40px tall, radius 8px, padding 8px 15px, primary #e74c3c with shadow 0 9px 24px rgba(231,76,60,.22), secondary outlined 1px #d3d5d7."
2. "Add a metadata strip: a flex-wrap row with 16px/40px gaps between 1px #ecedee top and bottom rules, padding 16px 0. Each item is an uppercase 10.5px/700 #888888 label (letter-spacing 0.09em) over a 13.5px #2f3c4e tabular value; topics are 13px/500 tags with radius 4px, padding 2px 10px and translucent fills rgba(84,110,122,.15) or rgba(30,136,229,.12)."
3. "Create a TL;DR callout and section heads: callout padding 16px 20px, radius 8px, 1px rgba(231,76,60,.2) border with a 4px #e74c3c left border, background linear-gradient(90deg, rgba(231,76,60,.1), rgba(231,76,60,.024)), an 11px/700 uppercase #e74c3c 'TL;DR:' label and 16px #2f3c4e text. Section h2s are 25px/700 #2f3c4e with an inline 18×4px #e74c3c pill 11px before the text, 54px above."

## Similar Pages

- Project pages generated inside a personal Hugo blog theme, where each paper reuses the blog's post card and adds a paper header, metadata strip and spotlight video.
- Research portfolio pages that present venue, DOI and GitHub stars as a dashboard-like fact row.

## Quick Start

```css
:root {
  --theme-color: #e74c3c;
  --primary-bg-color: #ffffff;
  --secondary-bg-color: #f1f1f1;
  --tertiary-bg-color: #f9f9f9;
  --primary-text-color: #2f3c4e;
  --secondary-text-color: #6d7683;
  --label-color: #888888;
  --primary-border-color: #d3d5d7;
  --secondary-border-color: #ecedee;
  --primary-shadow-color: #e2e3e4;
  --colophon-bg-color: #252a31;
  --footer-bg-color: #1b1f25;
  --font: "Lato", "Droid Arabic Kufi", Arial, sans-serif;
  --radius-md: 8px;
  --radius-lg: 12px;
}
html[data-theme="dark"] {
  --primary-bg-color: #20242b;
  --secondary-bg-color: #15191e;
  --primary-text-color: #f3f5f7;
}
```

## Provenance

- **URL**: https://www.infinitescript.com/project/city-dreamer-4d/
- **Paper**: CityDreamer4D: Compositional Generative Model of Unbounded 4D Cities, Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu (S-Lab, Nanyang Technological University); arXiv 2501.08983, DOI 10.1109/TPAMI.2025.3603078.
- **Venue**: IEEE TPAMI 2026.
- **Selection reason**: found in an arXiv cs.CV listing scan; the arXiv comment reads "Accepted by TPAMI. Project Page: ...", and the repository hzxie/CityDreamer4D states TPAMI 2026; curl returned 200 text/html.
- **Template credit**: the author's own "Infinite Script" Hugo blog theme on Bootstrap 5 with Font Awesome 7; footer reads "© 2026 Infinite Script. All rights reserved".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), additional computed-style probes of the header region, kicker, buttons, metadata strip, TL;DR, h2 `::before` dash, carousel, spotlight, citation and footer, the 1440×900 and full-page screenshots, and the site stylesheet and `index.html` read directly, on 2026-10-28.
