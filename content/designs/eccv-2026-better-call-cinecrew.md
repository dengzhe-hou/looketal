# Better Call CineCrew — Style Reference

> A studio screening room after hours: charcoal walls, an amber spotlight leaking from the ceiling, and every important word lit in marquee gold.

**Theme:** dark

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, plus targeted probes of the hero, cards, timeline, comparison panel and buttons), the 1440×900 shot and a full-page capture, and the page's `styles.css` plus an inline `<style>` block in `index.html` that styles the paper metadata. Buttons that do not set a font family (`.case-btn`, `.asset-thumb`) render in the browser default (Arial), not Inter.

## Overview

A product-style landing page (4,990px) on charcoal #121212 with white Inter text. A fixed full-viewport glow layer adds a warm amber radial from the top centre and a faint blue radial at upper right. The 76px sticky header shows a 42px rounded logo tile, a 15px/700 "Better Call CineCrew" title with a 12px gray subtitle, and four 14px nav links. The hero is a two-column grid: left, an amber pill eyebrow "PROJECT HOMEPAGE", a five-line 68px/700 Inter title with "Consistent Ultra-Long" in gold #f4b942, a white "ECCV 2026" pill, underlined author links, small affiliations, two 10px-radius "arXiv" and "GitHub" chips, a 19px gray summary and three 48px buttons (gold "Watch Demo", two translucent); right, a 16:9 video in a 32px-radius card. Sections repeat the amber pill eyebrow and a 48px/700 heading, then large translucent cards (32px radius, soft shadow): a script card with a 26px light-weight lead where character names are colored blue, gold and rose, reference-asset thumbnails and an asset preview; a full demo video; a horizontally scrolling shot timeline with gold "SHOT 0" labels; an abstract card beside a task-overview figure; and a comparison panel with two videos, a gold slider and three case buttons. There is no footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): charcoal family #121212 / #171717 / #121111 / #0e0e0e / #121213 / #121211 / #16110e together 84.9%; warm olive-gray #726c58 15.2% (the hero video frame, gold title words and amber glow blended).

Anatomy in DOM order (desktop 1440px, container x 80–1360):

1. **Sticky header** (`header.site-header`, 0–76px): rgba(18,18,18,0.82) with `backdrop-filter: blur(20px)`, 1px rgba(77,34,34,0.1) bottom border, inner padding 16px 0. Brand: 42px logo tile (14px radius, rgba(255,255,255,0.04)), 12px gap, title 15px/700 white over subtitle 12px #a1a1aa. Nav right: 14px #d4d4d8, 24px gaps; hover white.
2. **Glow layer** (`.page-glow`, fixed 0–900): `radial-gradient(circle at top, rgba(245, 158, 11, 0.16), transparent 34%), radial-gradient(circle at 80% 20%, rgba(59, 130, 246, 0.12), transparent 22%)`.
3. **Hero** (`section.hero`, 76–1066): padding 72px 0 56px; grid 1.06fr / 1fr, gap 40px, align-items center → copy 638px at x=80, media 602px at x=758.
4. **Eyebrow pill** (`.eyebrow`, y=148, 34px): 11px uppercase, letter-spacing 0.24em, #f7c96f on rgba(244,185,66,0.10), 1px rgba(244,185,66,0.25) border, padding 7px 12px, 999px radius. Gap 18px.
5. **Title** (`h1`, y=200, 360px, five lines): Inter 68px/700, line-height 1.06, letter-spacing -0.04em, white; "Consistent Ultra-Long" in #f4b942. Gap 20px.
6. **Venue pill** (`.paper-venue`, y=580, 35px): 13.12px/700 uppercase, letter-spacing 0.08em, white on rgba(255,255,255,0.06), 1px rgba(255,255,255,0.14) border, padding 6px 11px, 999px radius. Gap 14px.
7. **Authors** (`.paper-authors`, y=629, two rows): 16px/500 white, gaps 7px 14px, each linked name with a 1px rgba(255,255,255,0.28) bottom border; hover opacity .78. Gap 10px.
8. **Affiliations** (y=701) 13.76px/1.5 white at opacity .76, and a note (y=752) 12.8px at opacity .62. Gap 14px.
9. **Paper chips** (`.paper-link`, y=787, 41px): 14.08px/600 white, padding 8px 13px, 1px rgba(255,255,255,0.14), 10px radius, rgba(255,255,255,0.055) fill, 17px filled icon left; hover translateY(-1px). Gap 22px.
10. **Summary** (y=849, 103px): 19px/1.8 #d4d4d8, max 760px. Gap 10px.
11. **Buttons** (`.hero-actions`, y=962, 48px): 14px/600, padding 0 20px, 18px radius, 12px gaps; "Watch Demo" #f4b942 with #111111 text; "Method" and "Comparison" rgba(255,255,255,0.05) with white text and a 1px rgba(77,34,34,0.1) border.
12. **Hero media** (`.hero-media.card`, y=409, 602×339): 32px radius, overflow hidden, 16:9 video, card shadow `0 24px 60px rgba(0, 0, 0, 0.28)`.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Charcoal | #121212 | --bg | page background, header base |
| White | #ffffff | --text | title, headings, authors, card text, venue pill text |
| Zinc Muted | #a1a1aa | --muted | header subtitle, timeline intro, captions, video subtitles, switcher labels |
| Zinc Light | #d4d4d8 | (literal) | nav links, hero summary, section intros, abstract text, comparison text, case buttons |
| Gold | #f4b942 | --gold | gold title words, primary button fill, slider accent, active asset border at 65% |
| Gold Light | #f7c96f | (literal) | eyebrow text, mini labels, shot labels, comparison text labels, "ours" label |
| Gold Hover | #f7ca66 | (literal) | primary button hover |
| Gold Soft | rgba(244,185,66,0.12) | --gold-soft | gold tint (eyebrow uses 0.10 fill and 0.25 border) |
| Card | rgba(255,255,255,0.03) | --card | cards, comparison panel, switcher |
| Card Strong | rgba(255,255,255,0.05) | --card-strong | secondary buttons, icon buttons |
| Line | rgba(77,34,34,0.1) | --line | header border, card and video borders, secondary buttons (nearly invisible on charcoal) |
| Video Black | #09090b | (literal) | video and figure wells |
| Script Blue | #58a6ff | --blue | blue character names in the script lead |
| Script Gold | #f6b650 | (literal) | gold character names in the script lead |
| Script Rose | #fda4af | --rose | rose event phrases in the script lead |
| Lead White | #f5f5f5 | (literal) | script lead text |
| Label Gray | #e4e4e7 | (literal) | baseline comparison label |
| Button Ink | #111111 | (literal) | primary button text |
| Glow Amber | rgba(245,158,11,0.16) | (literal) | top-centre radial glow |
| Glow Blue | rgba(59,130,246,0.12) | (literal) | upper-right radial glow |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans | "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif | Inter 300, 400, 500, 600, 700 | Inter |
| Button default | none (form controls) | Arial on `.case-btn` and `.asset-thumb` | Arial |

| Role | Selector | Size / weight / line-height / tracking | Color |
|---|---|---|---|
| Title | `.hero-copy h1` | clamp(42px, 5.6vw, 68px) → 68px / 700 / 1.06 / -0.04em | white, `span` #f4b942 |
| Section heading | `.section-head h2` | clamp(34px, 4vw, 48px) → 48px / 700 / 1.12 / -0.03em | white |
| Section intro | `.section-head p` | 18px / 1.75, max 820px | #d4d4d8 |
| Hero summary | `.hero-copy p` | 19px / 1.8, max 760px | #d4d4d8 |
| Eyebrow | `.eyebrow` | 11px / 400 / uppercase / 0.24em | #f7c96f |
| Venue pill | `.paper-venue` | 0.82rem = 13.12px / 700 / uppercase / 0.08em | white |
| Authors | `.paper-authors` | 16px / 500 / 1.65 | white |
| Brand title | `.brand-title` | 15px / 700 | white |
| Nav | `.site-nav` | 14px | #d4d4d8 |
| Button | `.btn` | 14px / 600 | #111111 or white |
| Paper chip | `.paper-link` | 0.88rem = 14.08px / 600 | white |
| Mini label | `.mini-label` | 14px / 600 | #f7c96f |
| Script lead | `.script-lead` | clamp(18px, 2.05vw, 26px) → 26px / 300 / 1.45 / -0.03em, max 22ch | #f5f5f5, names 600 in blue/gold/rose |
| Shot label | `.timeline-shot` | 11px / uppercase / 0.20em | #f7c96f |
| Shot title | `.timeline-title` | 20px / 600 | white |
| Card body | `.abstract-card p` | 16px / 1.95 | #d4d4d8 |
| Comparison title | `.comparison-head h3` | 24px / 700 | white |
| Comparison label | `.comparison-text-label` | 12px / 700 / uppercase / 0.14em | #f7c96f |
| Caption | `.caption` | 14px / 1.75 | #a1a1aa |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow / effect |
|---|---|---|---|
| Cards, comparison panel | 32px | 1px rgba(77,34,34,0.1) | `0 24px 60px rgba(0, 0, 0, 0.28)` |
| Teaser figure | 28px | 1px rgba(77,34,34,0.1) | none |
| Timeline items | 26px | 1px rgba(77,34,34,0.1); hover rgba(244,185,66,0.4) | fill rgba(9,9,11,0.48) |
| Videos inside cards, asset preview wrap, switcher | 24px | 1px rgba(77,34,34,0.1) | none |
| Buttons, case buttons | 18px | secondary 1px rgba(77,34,34,0.1); active case rgba(244,185,66,0.58) | none |
| Asset thumbnails | 16px (image 14px) | 1px rgba(255,255,255,0.10); active rgba(244,185,66,0.65) | hover translateY(-1px) |
| Logo tile | 14px | none | rgba(255,255,255,0.04) fill |
| Paper chips | 10px | 1px rgba(255,255,255,0.14) | hover translateY(-1px) |
| Pills (eyebrow, venue), icon buttons | 999px | 1px gold 0.25 / white 0.14 | none |
| Timeline connector | 40×1px | none | `linear-gradient(90deg, rgba(244,185,66,0.7), rgba(255,255,255,0.1))` |

## Layout Metrics

- **Container**: `.container { width: min(1280px, calc(100% - 48px)); margin: 0 auto }` → x 80–1360 at 1440.
- **Hero**: padding 72px 0 56px; grid 1.06fr / 1fr, gap 40px, align-items center (638px copy, 602px media); vertical chain 34 (eyebrow) + 18 + 360 (title) + 20 + 35 (venue) + 14 + ~62 (authors) + 10 + 44 + 7 + 20 (note) + 14 + 41 (chips) + 22 + 103 (summary) + 10 + 48 (buttons) = 862px from y=148 to y=1010.
- **Sections**: padding 72px 0; section head max 820px, margin-bottom 32px, h2 margin-bottom 12px; eyebrow margin-bottom 18px.
- **Demo grid**: 0.78fr / 1.22fr, gap 28px (488px script card, 764px video card); cards padding 20px. The timeline card spans the full 1280px below.
- **Timeline**: items 260px wide, padding 20px, 16px gap with a 40px gradient connector 72px from the top; the row scrolls horizontally.
- **Method grid**: 1fr / 1.1fr, gap 32px.
- **Comparison panel**: padding 24px; two video columns with 20px gap; switcher margin-top 18px, padding 16px; case buttons 3 columns, 10px gap, padding 14px 16px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| base (1440) | 80px (container 1280px) | 16px | 68px | hero 2 columns, demo 0.78/1.22, method 1/1.1, comparison 2 columns |
| ≤1328px | 24px | 16px | 68px until 1214px, then 5.6vw | none |
| ≤1100px | 24px | 16px | 5.6vw, e.g. 61.6px at 1100 | hero, demo, method and comparison grids become 1 column |
| ≤860px | 14px (min(100% − 28px, 1280px)) | 16px | 48.2px at 860 | nav hidden; sections 56px; hero padding-top 44px; script lead 24px; asset thumbs 72px; case buttons 1 column; comparison head stacks |
| ≤750px | 14px | 16px | 42px floor | none |
| ≤640px | 14px | 16px | 42px | authors 15.04px with gaps 5px 10px; affiliations 13.12px |

## Components

- **Gold pill eyebrow** (`.eyebrow`): inline-flex, padding 7px 12px, 999px radius, rgba(244,185,66,0.10) fill, 1px rgba(244,185,66,0.25) border, 11px uppercase #f7c96f with 0.24em tracking; 18px above every section heading.
- **Primary button** (`.btn-primary`): min-height 48px, padding 0 20px, 18px radius, #f4b942 fill, #111111 14px/600; hover #f7ca66.
- **Secondary button** (`.btn-secondary`): same box, rgba(255,255,255,0.05) fill, white text, 1px rgba(77,34,34,0.1) border; hover rgba(255,255,255,0.10).
- **Paper chip** (`.paper-link`): min-height 38px, padding 8px 13px, 10px radius, rgba(255,255,255,0.055) fill, 1px rgba(255,255,255,0.14), 14.08px/600, 17px filled icon (arXiv mark, GitHub mark); hover lift 1px and fill rgba(255,255,255,0.09).
- **Glass card** (`.card`): 32px radius, rgba(255,255,255,0.03) fill, 1px rgba(77,34,34,0.1) border, shadow `0 24px 60px rgba(0, 0, 0, 0.28)`, padding 20px; opens with a 14px/600 #f7c96f mini label and an optional 14px #a1a1aa subtitle.
- **Script lead**: 26px/300 #f5f5f5 with -0.03em tracking, max 22ch; key phrases in 600 #58a6ff, #f6b650 or #fda4af.
- **Asset picker**: 64px thumbnails (16px radius, 3px padding) in a scrolling row with 10px gaps, the active one ringed in rgba(244,185,66,0.65); a preview well below (24px radius, rgba(0,0,0,0.24), padding 12px) with a 14px/600 title, 12px gray subtitle and a 20px-radius image at aspect 16/8.6.
- **Timeline item**: 260px, 26px radius, rgba(9,9,11,0.48), padding 20px; 11px uppercase #f7c96f "SHOT n", 20px/600 title, 14px/1.7 #a1a1aa text; items joined by 40px gold-to-white gradient lines.
- **Comparison panel**: 32px-radius card with 24px padding; a 24px/700 movie title, 12px uppercase gold "PLOT" and "OUR ADVANTAGE" labels over 16px/1.8 #d4d4d8 text, 40px round prev/next buttons; two 24px-radius videos labeled "LTX-Studio" (#e4e4e7) and "Better Call CineCrew" (#f7c96f); a case navigator with a gold-accent range slider and three 18px-radius case buttons (active: rgba(244,185,66,0.10) fill, rgba(244,185,66,0.58) border).

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky header | yes | blurred charcoal bar with logo tile, title and subtitle |
| Eyebrow / venue badge | yes | gold "PROJECT HOMEPAGE" pill and a white "ECCV 2026" pill |
| Title / authors / affiliations | yes | left column, gold title phrase, underlined author links |
| Link buttons | yes | small arXiv/GitHub chips plus three large section buttons |
| Hero video | yes | 16:9 in a 32px-radius card |
| Script-to-asset demo | yes | script card with colored names, asset thumbnails and preview |
| Full demo video | yes | card with 24px-radius video |
| Shot timeline | yes | horizontally scrolling 260px shot cards |
| Abstract | yes | glass card beside a task-overview figure |
| Baseline comparison | yes | side-by-side videos with case navigator |
| Results table | absent from the source | comparison is qualitative video only |
| BibTeX | absent from the source | no citation block |
| Footer | absent from the source | the page ends after the comparison panel |

## Adapting to Other Content

- **More authors**: keep the flex-wrapped 16px/500 row with 7px 14px gaps and underlined links; a third row adds about 35px above the venue chips.
- **A results table**: place it in a glass card (32px radius, 20px padding) with a 14px/600 #f7c96f mini label; header 12px/700 uppercase 0.14em #f7c96f, cells 14px #d4d4d8 with rgba(255,255,255,0.06) row rules; the ours row in white 600 on rgba(244,185,66,0.10).
- **BibTeX**: use a glass card with a mini label "Citation" and a #09090b well (24px radius, 16px padding) in a monospace 13px #d4d4d8.
- **Long publication or news lists**: use timeline items (260px, 26px radius, gold uppercase date label, 20px/600 title, 14px gray text) in a scrolling row, or stack them full-width inside one card.
- **A footer**: one 14px #a1a1aa line in the 1280px container with a 1px rgba(255,255,255,0.06) top rule and 40px padding.

## Do's and Don'ts

- Do keep one warm accent: gold #f4b942 for fills and #f7c96f for text labels.
- Do use generous radii (18px buttons, 24–32px cards and media) consistently.
- Do keep the fixed amber and blue radial glows behind content.
- Do color only key nouns in narrative text (blue, gold, rose) and keep the rest light gray.
- Don't use pure black backgrounds; the base is #121212 and video wells are #09090b.
- Don't rely on the card border for separation; it is nearly invisible, so the shadow and the 3% white fill do the work.
- Don't set button text in Arial by accident; give form controls `font: inherit` if you want them in Inter.

## Surfaces

Charcoal #121212 under a fixed amber/blue glow; glass cards at 3% white with a 0 24px 60px shadow; inner wells (timeline items at rgba(9,9,11,0.48), video and figure backgrounds #09090b, asset preview at rgba(0,0,0,0.24)); a blurred 82% charcoal header.

## Imagery

Cinematic generated film stills and videos (the Monkey King above clouds, a wizard school, a Superman barn scene, Better Call Saul episodes), character reference portraits as square thumbnails, and a beige-and-brown task-overview diagram of the multi-agent studio with a filmstrip of generated frames.

## Layout

A 1280px container with a two-column hero, then full-width sections that each hold one or two big rounded cards. Rhythm comes from the repeated gold pill eyebrow, 48px headings and 72px section padding; the shot timeline breaks the grid with horizontal scrolling.

## Agent Prompt Guide

Quick colors: bg #121212, text #ffffff, muted #a1a1aa, light gray #d4d4d8, gold #f4b942, gold label #f7c96f, video well #09090b, script blue #58a6ff, rose #fda4af.

1. "Build a dark hero on #121212 with a fixed glow (radial-gradient(circle at top, rgba(245, 158, 11, 0.16), transparent 34%) plus radial-gradient(circle at 80% 20%, rgba(59, 130, 246, 0.12), transparent 22%)). 1280px container, grid 1.06fr / 1fr with 40px gap. Left: a pill eyebrow (11px uppercase, 0.24em, #f7c96f on rgba(244,185,66,0.10), 1px rgba(244,185,66,0.25), padding 7px 12px), a 68px/700 Inter title with -0.04em tracking and one phrase in #f4b942, 16px/500 underlined authors, and 48px buttons with 18px radius: #f4b942 with #111111 text, and rgba(255,255,255,0.05) secondary. Right: a 16:9 video in a 32px-radius card."
2. "Make a glass card: border-radius 32px, background rgba(255,255,255,0.03), border 1px rgba(77,34,34,0.1), box-shadow 0 24px 60px rgba(0, 0, 0, 0.28), padding 20px; a 14px/600 #f7c96f label, then a 26px/300 #f5f5f5 lead (max 22ch, -0.03em) with key names in 600 #58a6ff, #f6b650 and #fda4af."
3. "Create a shot timeline: horizontally scrolling row of 260px cards (26px radius, rgba(9,9,11,0.48), padding 20px), each with an 11px uppercase 0.20em #f7c96f 'SHOT n', a 20px/600 white title and 14px/1.7 #a1a1aa text; between cards a 40×1px linear-gradient(90deg, rgba(244,185,66,0.7), rgba(255,255,255,0.1)) connector 72px from the top."

## Similar Pages

- Product-launch style generative-video pages with glass cards and a single gold accent.
- Multi-agent and storytelling demos that present a script, assets and a shot timeline as an app-like panel.

## Quick Start

```css
:root {
  --bg: #121212;
  --card: rgba(255, 255, 255, 0.03);
  --card-strong: rgba(255, 255, 255, 0.05);
  --line: rgba(77, 34, 34, 0.1);
  --text: #ffffff;
  --muted: #a1a1aa;
  --light: #d4d4d8;
  --gold: #f4b942;
  --gold-label: #f7c96f;
  --gold-soft: rgba(244, 185, 66, 0.12);
  --blue: #58a6ff;
  --rose: #fda4af;
  --well: #09090b;
  --radius-xl: 32px;
  --radius-lg: 26px;
  --shadow: 0 24px 60px rgba(0, 0, 0, 0.28);
  --font: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
```

## Provenance

- **URL**: https://jiabenchen.github.io/cinecrew/
- **Paper**: Better Call CineCrew: Consistent Ultra-Long Narrative-to-Film Generation (arXiv 2609.07720), Jiaben Chen, Sixun Dong, Qinhong Zhou, Raine Ma, Zhiyang Dou, Wojciech Matusik, Chuang Gan (UMass Amherst, MIT).
- **Venue**: ECCV 2026.
- **Selection reason**: the arXiv comment states acceptance at ECCV 2026 and links this project page.
- **Template credit**: none stated; a custom page (`styles.css`, `script.js`, an inline metadata stylesheet).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted probes of hero, cards, timeline, comparison panel and buttons, the 1440×900 shot and a full-page capture, and `styles.css` and `index.html` read directly, on 2026-10-28.
