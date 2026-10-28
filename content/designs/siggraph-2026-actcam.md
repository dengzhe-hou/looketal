# ActCam — Style Reference

> A Distill-style reading room under a dark navy lintel: an italic serif name, narrow measured columns, and numbered cards that whisper their numbers.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), a second probe of rendered elements (title emphasis, byline, teaser row, rules, cards, badges, table rows, bars), the 1440×900 and tall screenshots, and the inline `<style>` and markup of `index.html`. Two script-driven states matter: blocks with `.reveal` start at opacity 0 and fade up 14px when scrolled into view (the contribution cards measured opacity 0 at load), and user-study bars start at width 0 and grow to their percentage on scroll. No web font is loaded, so the "Hoefler Text, Cochin" stack falls back to Georgia on Windows.

## Overview

A restrained, classic academic page in the Distill tradition: white ground, text in black at 80% opacity, Georgia serif body at 17px, and system sans for UI labels, buttons, tables and badges. A fixed 50px dark navy bar (#0f2e3d, `hsl(200, 60%, 15%)`) carries a small serif logo and spaced uppercase sans links, with a thin sky-blue scroll-progress line under it. The header is centred: "ActCam" in a 52px italic serif, a 22px gray serif subtitle, a sans byline, affiliations and three outlined navy buttons with 4px radii. A wide teaser row (input figure, chevron, output video grid) sits in a 3px-radius frame with a soft shadow. Content then narrows to measured columns: 600px for the abstract, 768px for contributions and method, with 1px hairline rules between sections. Contributions are three white cards with large faint navy numerals; the method is a numbered vertical list on a fading line; results use clean sans tables with a navy-tinted "Ours" row, horizontal preference bars, and paired video cards with warm headers and camera badges. The footer repeats the navy bar.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white family #ffffff / #fcfcfc / #f2f3f2 / #fefffe / #fffffe together 79.0%; dark slate #21292c 7.7% (the navy bar plus dark pixels of the teaser photos); desert orange #b1743d 6.8% and sand #dabd98 6.5% (the generated desert-crash video frames). The navy accent covers too little area outside the bar to form its own cluster.

Anatomy in DOM order (desktop 1440px, centred):

1. **Fixed nav** (`nav`, 0–50px): #0f2e3d, padding 0 24px, flex space-between. Logo "ActCam" Georgia (Hoefler stack) 18px/400, letter-spacing 0.02em, rgba(255,255,255,0.95) at x=24. Links ABSTRACT, METHOD, RESULTS, CONDITIONING, VIDEOS, CITE: system sans 12px/500 uppercase, letter-spacing 0.05em, rgba(255,255,255,0.65), gap 24px, hover rgba(255,255,255,0.95). A 2px `hsl(200, 70%, 50%)` progress bar is fixed at top 50px and grows with scroll.
2. **Header** (`header.header-area`, 0–393px): padding 100px 24px 40px, text-align center.
3. **Title** (`h1`, y=100, 65px box): "ActCam" inside `<em>`, Georgia italic 52px (clamp(36px, 5vw, 52px)) / 400, line-height 1.25, letter-spacing -0.02em, rgba(0,0,0,0.8). Gap 8px.
4. **Subtitle** (`.header-subtitle`, y=173): Georgia 22px (clamp(17px, 2.2vw, 22px)) / 400, line-height 1.45, rgba(0,0,0,0.55). Gap 28px.
5. **Byline** (`.byline`, y=233): system sans 14px, line-height 1.8, nine names as links 500 rgba(0,0,0,0.8), superscripts 10px rgba(0,0,0,0.35), commas rgba(0,0,0,0.55). Gap 6px.
6. **Affiliations** (`.affiliations`, y=265): system sans 15px rgba(0,0,0,0.55), entries separated by " · ". Gap 24px.
7. **Buttons** (`.links-row`, y=316, 37px tall, gap 12px): Paper, Code (soon), arXiv; white, 1px rgba(0,66,118,0.2), 4px radius, padding 7px 18px, system sans 13px/500 #004276, 14px stroke icons left. Gap 40px header padding + 36px figure margin.
8. **Teaser row** (`.teaser-row`, y=429, 936×283, x=252): flex, white, 3px radius, `box-shadow: 0 2px 12px rgba(0,0,0,0.08)`, overflow hidden; left 42% a static figure (acting video, first frame, camera shots), a gray chevron in rgba(0,0,0,0.35), right a 2×2 output video.
9. **Rule** (`hr.section-rule`, y=759, 600px): 1px rgba(0,0,0,0.1); then "Abstract" h2 at y=808.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | --bg | page, buttons, cards, tables, teaser frame |
| Warm White | #fcfaf7 | --bg-warm | table headers, video-pair headers, condition captions, BibTeX block, second phase panel |
| Text | rgba(0, 0, 0, 0.8) | --text | body, title, headings, author names, table model names |
| Text Secondary | rgba(0, 0, 0, 0.55) | --text-secondary | subtitle, byline separators, affiliations, captions, table values, card text, BibTeX |
| Text Muted | rgba(0, 0, 0, 0.35) | --text-muted | superscripts, table header labels, teaser chevron, copy button, chart legend |
| Navy | #004276 | --accent | links, button text, contribution numerals (at 12% opacity), method step numbers, "Ours" row, best values, user-study bars |
| Navy Wash | rgba(0, 66, 118, 0.07) | --accent-light | button hover fill, "Ours" table row, featured condition caption |
| Navy Border | rgba(0, 66, 118, 0.2) | --accent-border | button borders, method step circles, featured condition card |
| Deep Teal | #0f2e3d | --teal (hsl(200, 60%, 15%)) | nav bar, footer |
| Progress Blue | #269dd9 | (hsl(200, 70%, 50%)) | 2px scroll-progress bar |
| Hairline | rgba(0, 0, 0, 0.1) | --border | section rules, card and table borders, row rules |
| Border Strong | rgba(0, 0, 0, 0.18) | --border-strong | table header bottom rule, card hover border |
| Badge Blue | #1a5276 / #eaf2f8 | --camera-badge / --camera-badge-bg | camera-motion badge text / fill |
| Orange | #b45309 | --orange | "Phase 2" tag, intrinsic-camera badge |
| Baseline Bar | #7aa3b8 | (hsl(200, 30%, 60%)) | baseline segment of user-study bars |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display (h1, h2, logo, numerals) | 'Hoefler Text', Cochin, Georgia, serif | no web font; Georgia on Windows, Hoefler Text on macOS | Libre Caslon Text |
| Body | Georgia, 'Times New Roman', serif | system Georgia | Gelasio |
| UI (nav, byline, buttons, tables, badges) | -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif | system UI (Segoe UI on Windows) | Inter |
| Code | Menlo, Consolas, 'Courier New', monospace | Consolas on Windows | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.header-area h1 em` | clamp(36px, 5vw, 52px) → 52px / 400 italic / 1.25, letter-spacing -0.02em | rgba(0,0,0,0.8) |
| Subtitle | `.header-subtitle` | clamp(17px, 2.2vw, 22px) → 22px / 400 / 1.45 | rgba(0,0,0,0.55) |
| Section heading | `h2` | 26px / 400 / 1.25 | rgba(0,0,0,0.8) |
| Subsection | `h3` | 20px / 400 italic | rgba(0,0,0,0.8) |
| Card title | `.contrib-card h3`, `.method-step h4` | Georgia 16px / 600 | rgba(0,0,0,0.8) |
| Label heading | `h4` | Georgia 14px / 600 uppercase, letter-spacing 0.06em | rgba(0,0,0,0.55) |
| Body | `html` | 17px / 400 / 1.6 | rgba(0,0,0,0.8) |
| Abstract | `.abstract-text` | 17px / 1.7 | rgba(0,0,0,0.8) |
| Byline | `.byline` | sans 14px / 1.8; names 500 | rgba(0,0,0,0.8) |
| Nav link | `nav .nav-links a` | sans 12px / 500 uppercase, letter-spacing 0.05em | rgba(255,255,255,0.65) |
| Button | `.link-btn` | sans 13px / 500 | #004276 |
| Table header | `thead th` | sans 11px / 600 uppercase, letter-spacing 0.04em | rgba(0,0,0,0.35) |
| Table cell | `tbody td` | sans 13px, tabular numbers | rgba(0,0,0,0.55); first column 500 rgba(0,0,0,0.8) |
| Contribution numeral | `.contrib-num` | 44px / 400 / 1 | #004276 at opacity 0.12 |
| Caption | `.figure-caption` | 13px / 1.55 | rgba(0,0,0,0.55) |
| BibTeX | `.bibtex-block pre` | Menlo stack 12px / 1.6 | rgba(0,0,0,0.55) |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Teaser row, figure images | 3px | none | `0 2px 12px rgba(0,0,0,0.08)` |
| Link buttons | 4px | 1px rgba(0,66,118,0.2) | none; hover fill rgba(0,66,118,0.07), border #004276 |
| Contribution cards | 5px, padding 22px 18px | 1px rgba(0,0,0,0.1) | hover `0 2px 12px rgba(0,0,0,0.08)` and border rgba(0,0,0,0.18) |
| Video pairs, condition cards, two-phase panel | 5px | 1px rgba(0,0,0,0.1) | hover `0 2px 12px rgba(0,0,0,0.08)` |
| Table wrapper, BibTeX block | 4px | 1px rgba(0,0,0,0.1) | none |
| Camera badges, copy button, bars | 3px | badge 1px rgba(26,82,118,0.2) | none |
| Video labels | 2px | none | none |
| Method step circles | 50%, 30px | 1.5px rgba(0,66,118,0.2) | none |

The method list's spine is `background: linear-gradient(to bottom, var(--accent-border), var(--border), transparent)`, 1px wide at left 15px.

## Layout Metrics

- **Column system** (Distill-like, each with 24px side padding): `.l-body` max 648px (600px text, x=420), `.l-middle` 816px (768px, x=336), `.l-page` 984px (936px, x=252), `.l-screen` 1200px (1152px, x=144).
- **Header**: padding 100px 24px 40px (the fixed nav covers 0–50px); title→subtitle 8px, subtitle→byline 28px, byline→affiliations 6px, affiliations→buttons 24px.
- **Teaser**: `.figure-block` margin 36px 0 inside `.l-page`; left panel 42% width, chevron padding 0 6px, right video flex 1.
- **Sections**: margin 48px 0; each preceded by a 1px rule; h2 margin 48px 0 20px; paragraphs margin-bottom 20px.
- **Grids**: contributions 3 columns, gap 16px; condition gallery 2 columns, gap 20px (featured card spans both); video triples 3 equal columns with 1px dividers; video pairs margin-bottom 28px.
- **Footer**: margin-top 60px, padding 32px 24px, centred affiliations (sans 13px rgba(255,255,255,0.7), gap 28px) and a 12px rgba(255,255,255,0.4) line.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1040px | 24px | 17px | 52px | 3-column contributions, side-by-side teaser |
| ≤1040px | 24px | 17px | 5vw (36px floor at 720px) | none |
| ≤768px | 24px | 17px | 36px | contributions, condition gallery and video pairs 1 column; two-phase panel stacks; teaser stacks with the chevron rotated 90°; nav links 10px with 12px gaps; sections margin 32px |
| ≤500px | 24px | 16px | 36px | nav links hidden; buttons stack vertically |

## Components

- **Navy bar** (`nav`): fixed, 50px, #0f2e3d, serif logo left, uppercase spaced sans links right; 2px #269dd9 progress line under it.
- **Outlined button** (`.link-btn`): inline-flex, gap 6px, padding 7px 18px, white, 1px rgba(0,66,118,0.2), radius 4px, sans 13px/500 #004276, 14px stroke icon (stroke-width 2). Hover: rgba(0,66,118,0.07) fill and #004276 border.
- **Contribution card** (`.contrib-card`): white, 1px rgba(0,0,0,0.1), 5px radius, padding 22px 18px; Georgia 16px/600 title, 14px/1.55 rgba(0,0,0,0.55) text; a 44px serif numeral in #004276 at 12% opacity pinned top 8px right 14px.
- **Method steps** (`.method-steps`): padding-left 44px, 24px gaps, a 1px fading navy-to-transparent spine; each step has a 30px white circle with a 1.5px rgba(0,66,118,0.2) ring and an 11px/600 #004276 number, a Georgia 16px/600 title and 15px secondary text.
- **Two-phase panel**: two flex halves in a 5px bordered box; Phase 1 on rgba(0,66,118,0.03) with a navy 10px/600 uppercase tag (letter-spacing 0.1em), Phase 2 on #fcfaf7 with an #b45309 tag.
- **Results table**: in a 4px bordered wrapper; header #fcfaf7, 11px/600 uppercase rgba(0,0,0,0.35), 2px rgba(0,0,0,0.18) bottom rule; rows 1px rules, 13px centred numbers; "Ours" row on rgba(0,66,118,0.07) with #004276 600 text; best values #004276 700.
- **User-study bars**: 32px tall rows, 3px radius, track rgba(0,0,0,0.04); "Ours" segment #004276 with 11px/700 white percentage; baseline #7aa3b8; tie rgba(0,0,0,0.08); widths animate over 1s `cubic-bezier(0.23, 1, 0.32, 1)` on scroll.
- **Video pair card** (`.video-pair`): 1px rgba(0,0,0,0.1), 5px radius; header #fcfaf7 with 1px bottom rule, padding 10px 16px, title 14px/600 and camera badges (11px/700 uppercase #1a5276 on #eaf2f8, 1px rgba(26,82,118,0.2), radius 3px, padding 3px 10px); videos below with corner labels (10px/700 uppercase, "Acting" on rgba(0,0,0,0.6), "Output" on rgba(0,66,118,0.85)).
- **BibTeX**: #fcfaf7, 1px hairline, 4px radius, padding 16px 20px, Consolas 12px gray, white copy button (11px, 3px radius) top-right turning navy on hover.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Fixed nav | yes | 50px deep-teal bar with uppercase sans links and progress line |
| Title / subtitle / authors / affiliations | yes | centred italic serif title, gray serif subtitle, sans byline |
| Venue badge | absent from the source | venue only appears in the BibTeX |
| Link buttons | yes | three outlined navy buttons, 4px radius |
| Teaser | yes | figure + chevron + output video in a 3px framed row |
| Abstract | yes | 600px Georgia column, bold key phrases |
| Contributions | yes | three numbered cards with faint numerals |
| Method | yes | framed pipeline figure and a numbered vertical step list, two-phase panel |
| Results tables | yes | two sans tables with warm headers and a navy "Ours" row |
| User study | yes | horizontal stacked preference bars |
| Conditioning / video galleries | yes | condition cards (2 columns) and paired video cards with camera badges |
| BibTeX | yes | warm-white block with copy button |
| Footer | yes | deep-teal bar with affiliations |

## Adapting to Other Content

- **More authors**: keep the single centred sans byline at 14px/1.8; it wraps within the 1392px header width; put affiliations on the next line at 15px rgba(0,0,0,0.55) with " · " separators.
- **Another results table**: reuse the table recipe inside `.l-middle` (768px): warm 11px/600 uppercase header, 13px tabular cells, the "Ours" row on rgba(0,66,118,0.07) with #004276 text.
- **Long publication or news lists**: use the method-step pattern (30px ringed number or date, Georgia 16px/600 title, 15px secondary line) inside `.l-body` (600px), 24px apart on the fading spine.
- **Wide figures**: promote them to `.l-page` (936px) or `.l-screen` (1152px) and keep 3px radii with the `0 2px 12px rgba(0,0,0,0.08)` shadow; text never leaves the 600–768px columns.

## Do's and Don'ts

- Do keep the reading measure narrow: 600px for prose, 768px for cards, 936–1152px only for media.
- Do set the title as an italic serif and everything functional (nav, buttons, tables, badges) in the system sans.
- Do use navy #004276 sparingly: links, button text, numbers, the "Ours" row.
- Do separate sections with 1px rgba(0,0,0,0.1) rules, not background bands.
- Don't fill buttons; they are white with a 20%-navy outline.
- Don't use pure black text; all text is black at 80%, 55% or 35% opacity.
- Don't round anything beyond 5px.

## Surfaces

White page throughout, with warm-white #fcfaf7 reserved for table headers, video-card headers, captions and the BibTeX block; navy-tinted rgba(0,66,118,0.07) only for the "Ours" row and featured captions; deep-teal #0f2e3d for the nav and footer bars.

## Imagery

Generated video of characters in cinematic scenes (a man beside a crashed plane in a desert, dancers, action poses) shown as autoplay loops, paired with the acting input video; method figures are dense, colourful pipeline diagrams with depth maps and pose skeletons. Media sit in 3px or 5px frames on white with soft shadows or hairlines.

## Layout

Fixed navy bar; a centred header; a 936px teaser; then a single centred column that widens and narrows by content type (600px abstract, 768px contributions, method and results, 1152px video galleries), with sections 48px apart and divided by hairline rules; a navy footer. About 8,500px tall.

## Agent Prompt Guide

Quick colors: page #ffffff, warm #fcfaf7, text rgba(0,0,0,0.8) / rgba(0,0,0,0.55) / rgba(0,0,0,0.35), accent #004276, nav #0f2e3d, hairline rgba(0,0,0,0.1), badge #1a5276 on #eaf2f8.

1. "Build a centred header below a fixed 50px #0f2e3d nav (serif logo 18px rgba(255,255,255,0.95); uppercase sans links 12px/500, letter-spacing 0.05em, rgba(255,255,255,0.65), gap 24px). Header padding 100px 24px 40px: italic Georgia 52px/400 title, letter-spacing -0.02em, rgba(0,0,0,0.8); Georgia 22px subtitle rgba(0,0,0,0.55); sans 14px byline; then outlined buttons (white, 1px rgba(0,66,118,0.2), radius 4px, padding 7px 18px, sans 13px/500 #004276)."
2. "Make three contribution cards in a 768px column, gap 16px: white, 1px rgba(0,0,0,0.1), radius 5px, padding 22px 18px; title Georgia 16px/600; text 14px/1.55 rgba(0,0,0,0.55); a 44px serif numeral in #004276 at opacity 0.12 at top 8px right 14px; hover shadow 0 2px 12px rgba(0,0,0,0.08)."
3. "Create a results table in a 4px-radius wrapper with 1px rgba(0,0,0,0.1): header #fcfaf7, sans 11px/600 uppercase rgba(0,0,0,0.35), 2px rgba(0,0,0,0.18) bottom rule; cells 13px centred rgba(0,0,0,0.55) with 1px row rules; highlight our row with rgba(0,66,118,0.07) and #004276 600 text."

## Similar Pages

- Distill-template research articles with `l-body` / `l-page` / `l-screen` column widths and Georgia body text.
- Classic serif project pages that use a single dark navy bar and outlined buttons instead of filled pills.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --bg-warm: #fcfaf7;
  --text: rgba(0, 0, 0, 0.8);
  --text-secondary: rgba(0, 0, 0, 0.55);
  --text-muted: rgba(0, 0, 0, 0.35);
  --accent: #004276;
  --accent-light: rgba(0, 66, 118, 0.07);
  --accent-border: rgba(0, 66, 118, 0.2);
  --teal: hsl(200, 60%, 15%);
  --border: rgba(0, 0, 0, 0.1);
  --border-strong: rgba(0, 0, 0, 0.18);
  --shadow-md: 0 2px 12px rgba(0, 0, 0, 0.08);
  --font-display: 'Hoefler Text', Cochin, Georgia, serif;
  --font-body: Georgia, 'Times New Roman', serif;
  --font-ui: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif;
  --l-body: 648px;
  --l-middle: 816px;
  --l-page: 984px;
  --l-screen: 1200px;
}
```

## Provenance

- **URL**: https://elkhomar.github.io/actcam/
- **Paper**: ActCam: Zero-Shot Joint Camera and 3D Motion Control for Video Generation (arXiv 2605.06667), Omar El Khalifi, Thomas Rossi, Oscar Fossey, Thibault Fouque, Ulysse Mizrahi, Philip Torr, Ivan Laptev, Fabio Pizzati, Baptiste Bellot-Gurlet (Kinetix, MBZUAI, University of Oxford).
- **Venue**: SIGGRAPH 2026 (as listed in the arXiv comment).
- **Selection reason**: the arXiv comment lists the venue as SIGGRAPH 2026 without an explicit acceptance word; the project page is linked in the abstract.
- **Template credit**: none stated; a single-file custom build whose `.l-body` / `.l-middle` / `.l-page` / `.l-screen` widths follow the Distill layout system.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), an additional computed-style probe, the 1440×900 and tall screenshots, and the inline CSS and markup of `index.html` read directly, on 2026-10-28.
