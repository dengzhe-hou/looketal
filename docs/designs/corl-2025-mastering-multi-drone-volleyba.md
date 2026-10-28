# HCSP Blue Ledger — Style Reference

> A tidy lab notebook in cobalt: a frosted project switcher, a blue pill, then blue headings ruled off by hairlines and every figure captioned in grey italics.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, loaded fonts, color share), selector probes of the badge, header video, stage cards, figures, captions and video grids, the 1440×900 and full-page screenshots, and the page's `css/index.css` (header comment: "adapted from VS-Bench template") and `index.html`. Many figure widths are set by inline `max-width` styles on each `<img>`; the rendered values are listed. The header video autoplays, so the screenshot shows one frame.

## Overview

A long, text-led project page (about 12,500px tall) in Inter on white, with #333333 body text and one cobalt accent (#1565c0). A frosted 52px bar at the top switches between three sibling projects (VolleyBots, HCSP, JuggleRL) with the current one shown as a grey tab in blue; once the reader scrolls it is replaced by a second bar with a project dropdown and section links. The header is centred: a filled cobalt "CoRL 2025" pill, a two-line 38.4px bold title, author lines, affiliation, two charcoal pill buttons and a half-width simulation video with 8px corners. The main column (1000px) holds six sections (Abstract, Task, Method, Experiments, Videos, BibTeX), each opened by a 1px #dee2e6 top rule and a 32px cobalt h2. Subsections use a 4px cobalt left bar. Figures are centred images with grey italic captions; a three-card grid with cobalt top borders explains the training stages; videos sit in 1-, 2- and 3-column grids with italic captions.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white family #ffffff / #feffff / #fffffc 74.4%; near-white #fbfbfc 7.7% (the frosted top bar); simulation blues #3b6c91 / #4a7290 / #365b79 together 14.5% and pale blue-grey #a1b4c0 3.3% (the drone court in the header video). Cobalt and charcoal cover too little area to form clusters.

Anatomy in DOM order (desktop 1440px, everything centred):

1. **Project bar** (`nav.nav-global`, fixed, 0–53px): rgba(251,251,253,0.92) with `backdrop-filter: saturate(180%) blur(20px)` and a 1px rgba(0,0,0,0.1) bottom border. Three centred tabs, 14px/500 #444444, padding 6px 14px, radius 6px, 4px apart; the active "HCSP" tab is 600 #1565c0 on rgba(0,0,0,0.08). Body padding-top 52px; header padding-top 40px.
2. **Venue pill** (`.venue-badge`, y=92, 159×47): "CoRL 2025", 21.6px/600, letter-spacing 0.02em, #ffffff on #1565c0, padding 6px 20px, radius 20px. Margin-bottom 20px, then the h1's 25.73px top margin (no collapse because the pill is inline-block).
3. **Title** (`h1`, y=184, 92px tall): 38.4px/700, line-height 1.2, #333333, centred, broken into two lines with a `<br>`. Gap 20px.
4. **Authors** (`.authors p`, y=296): 16.8px/400 #333333, two lines (forced `<br>`), † superscripts for corresponding authors. Gap 16.8px.
5. **Affiliation** (`p.affiliations`, y=371): 14.4px #666666. Gap 14.4px.
6. **Footnote** (y=408): "†Corresponding authors.", inline style 14.4px #888888. Gap 30px.
7. **Buttons** (`.links`, y=464, 46px tall): two charcoal pills, arXiv and Code, 15px apart. Gap 40px (inline `margin-top: 2.5rem` on the video).
8. **Header video** (y=549, 500×375 at x=470): inline `max-width: 50%`, radius 8px, native controls, autoplay loop. Header padding-bottom 40px and a 1px #dee2e6 bottom border end the header at y=973; `main` adds 40px, so the Abstract section starts at y=1013.

Arithmetic check: 52 + 40 = 92; 92 + 47 + 20 + 25.73 ≈ 184; 184 + 92 + 20 = 296; 296 + 57 + 16.8 ≈ 371; 371 + 23 + 14.4 ≈ 408; 408 + 26 + 30 = 464; 464 + 46 + 40 ≈ 549 (the inline video adds a few pixels of line box); 973 + 40 = 1013.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #ffffff | --bg-color | page, header, button text |
| Ink | #333333 | --text-color | body text, title, authors; charcoal button fill |
| Cobalt | #1565c0 | --primary-color | venue pill fill, h2 headings, h3 left bars, stage-card top borders and titles, active tab text, button hover fill |
| Link Blue | #3273dc | (literal) | in-text links (VolleyBots, references) |
| Subhead Grey | #444444 | (literal) | h3 text, nav tab text |
| Caption Grey | #555555 | (literal, `.caption`) | figure captions, stage-card body, copy button |
| Muted | #666666 | (literal) | affiliation, video captions, footer text |
| Footnote | #888888 | (inline) | "Corresponding authors" line |
| Hairline | #dee2e6 | --border-color | section top rules, header bottom rule, stage-card and pre borders, footer top rule |
| Light Gray | #f8f9fa | --light-gray | stage cards, BibTeX block, footer band |
| Frost | rgba(251,251,253,0.92) | (literal) | both fixed navigation bars |
| Tab Fill | rgba(0,0,0,0.08) | (literal) | active nav tab, copy button |
| Play Red | rgba(255,0,0,0.85) | (literal, `.yt-play-btn`) | YouTube thumbnail play disc (declared for thumbnail links) |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text | 'Inter', sans-serif (Google Fonts 300, 400, 600, 700) | Inter 400, 600, 700 | Roboto |
| Code | 'Courier New', Courier, monospace | system Courier New | Courier Prime |
| Icons | Font Awesome 6.0.0, Academicons | Font Awesome 6 Free 900, Brands 400, Academicons 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1` | 2.4rem = 38.4px / 700 / 1.2 | #333333 |
| Venue pill | `.venue-badge` | 1.35rem = 21.6px / 600, letter-spacing 0.02em | #ffffff |
| Section heading | `h2` | 2rem = 32px / 700 / 1.6, margin 10px 0 16px | #1565c0 |
| Subsection | `h3` | 1.3rem = 20.8px / 700, 4px #1565c0 left border, padding-left 10px, margin 28px 0 15px | #444444 |
| Card title | `.stage-card h4` | 16px / 700 | #1565c0 |
| Body | `body`, `main p` (justified) | 16px / 400 / 1.6 | #333333 |
| Authors | `.authors` | 1.05rem = 16.8px / 400 | #333333 |
| Affiliation | `.affiliations` | 0.9rem = 14.4px | #666666 |
| Figure caption | `.caption` | 0.9rem = 14.4px / 400 italic / 1.5, centred | #555555 |
| Video caption | `.video-caption` | 0.9rem / 400 italic, centred, padding-top 4px | #666666 |
| Nav tab | `.nav-global-links a` | 0.875rem = 14px / 500; active 600 | #444444; active #1565c0 |
| Button | `.btn` | 16px / 600 | #ffffff |
| BibTeX | `pre` | 0.9rem = 14.4px Courier New | #333333 |
| Footer | `footer` | 0.9rem = 14.4px | #666666 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Venue pill | 20px | none | none |
| Buttons | 30px | none | none |
| Nav tabs | 6px | none | none |
| Header and grid videos | 8px | none | none |
| Stage cards | 8px | 1px #dee2e6, 4px #1565c0 top | none |
| BibTeX block | 5px | 1px #dee2e6 | none |
| Copy button | 5px | none | none |
| YouTube thumbnail | 8px | none | hover `0 8px 24px rgba(0,0,0,0.2)` |
| Scroll-to-top | 50% (48px) | none | `0 4px 12px rgba(0,0,0,0.15)` |
| Project dropdown | 10px | 1px rgba(0,0,0,0.1) | `0 8px 32px rgba(0,0,0,0.12)` |

Bars: `background: rgba(251,251,253,0.92); backdrop-filter: saturate(180%) blur(20px); border-bottom: 1px solid rgba(0,0,0,0.1)`.

## Layout Metrics

- **Container**: `.container { max-width: 1000px; margin: 0 auto; padding: 0 20px }` with content-box sizing, so text runs 1000px wide at x=220–1220 at 1440. Nav content is also 1000px max with 24px padding.
- **Header**: padding 40px 0, 1px #dee2e6 bottom border; rendered 52–973px.
- **Main**: padding 40px 0. Each `section` has padding-top 20px, margin-bottom 40px and a 1px #dee2e6 top border (the first section has none); `scroll-margin-top: 52px`.
- **Figures**: `.figure-container` margin 20px 0, centred; images use inline max-widths of 40–100% (700px for Figure 1, 1000px for Figure 2, 900px for Table 1).
- **Stage grid**: 3 columns, gap 16px, margin 20px 0 30px; cards 323px wide, padding 16px.
- **Video grids**: gap 20px; `.video-grid-1` max 640px centred, `.video-grid-2` two 490px columns, `.video-grid-3` three 320px columns.
- **BibTeX**: full 1000px, padding 20px; copy button absolute at 10px from the top right.
- **Footer**: full width, #f8f9fa, padding 20px 0, margin-top 40px, 1px #dee2e6 top rule.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >768px | 20px inside a 1000px column | 16px | 38.4px | stage grid 3 columns; video grids 1/2/3 columns |
| ≤768px | 20px | 16px | 1.8rem = 28.8px | `.figures-row` stacks; 2- and 3-column video grids and the stage grid become 1 column; sticky-bar section links collapse into a menu opened by a bars icon |

## Components

- **Venue pill** (`.venue-badge`): inline-block, #1565c0 fill, #ffffff 21.6px/600 text, letter-spacing 0.02em, padding 6px 20px, radius 20px, 20px bottom margin.
- **Charcoal button** (`.btn`): inline-flex, #333333 fill, #ffffff 16px/600 Inter, padding 10px 20px, radius 30px, 46px tall, leading icon with 8px right margin (Academicons arXiv, Font Awesome GitHub). Hover fill #1565c0, transition 0.3s.
- **Project switcher bar** (`.nav-global`): fixed 52px frosted bar, centred tabs 14px/500 #444444, padding 6px 14px, radius 6px; hover rgba(0,0,0,0.06); active 600 #1565c0 on rgba(0,0,0,0.08). Hides on scroll and gives way to `.nav-sticky-bar`: same frost, a bold 16px project name with a chevron dropdown (340px card list, radius 10px, shadow `0 8px 32px rgba(0,0,0,0.12)`) on the left and section links on the right.
- **Section heading**: 1px #dee2e6 rule, 20px padding, then a 32px/700 #1565c0 h2.
- **Subsection heading** (`h3`): 20.8px/700 #444444 with a 4px #1565c0 left border and 10px left padding.
- **Stage card** (`.stage-card`): #f8f9fa, 1px #dee2e6 border with a 4px #1565c0 top border, radius 8px, padding 16px; title 16px/700 #1565c0, body 14.4px #555555, left-aligned.
- **Figure** (`.figure-container`): centred image with an inline max-width, then a 14.4px italic #555555 caption beginning "Figure N." or "Table N.".
- **Video item**: 8px-radius video with native controls, then an italic 14.4px #666666 caption.
- **BibTeX block**: #f8f9fa `pre`, 1px #dee2e6 border, radius 5px, padding 20px, Courier New 14.4px; "Copy" button rgba(0,0,0,0.08), radius 5px, padding 5px 8px, 13.6px #555555 with a copy icon.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Project switcher / sticky section nav | yes | frosted 52px bars, grey tabs with a blue active state |
| Venue badge | yes | filled cobalt pill above the title |
| Title / authors / affiliation | yes | centred, forced line breaks, muted affiliation and footnote |
| Link buttons | yes | two charcoal pills |
| Teaser | yes | half-width simulation video |
| Abstract | yes | three justified paragraphs with bold key phrases |
| Method figures | yes | centred images with italic captions |
| Stage cards | yes | three light-grey cards with cobalt top borders |
| Results | present but non-standard | win-rate plots and tables are embedded as images (Table 1, Table 2 are PNGs) |
| Video gallery | yes | spotlight video, then 2- and 3-column captioned grids |
| BibTeX | yes | light grey code block with copy button |
| Footer | yes | light grey band with a licence line |
| HTML results table | absent from the source | — |

## Adapting to Other Content

- **More authors**: keep the centred 16.8px line and break it by hand into lines of about six names, as the source does; affiliations stay in one 14.4px #666666 line.
- **A results table**: render a real table at the 1000px measure: header row 14.4px/600 #333333 on #f8f9fa, 1px #dee2e6 rules, cells 14.4px, best values bold; caption above or below in 14.4px italic #555555 starting "Table N.".
- **More method stages**: extend the stage grid in rows of three 323px cards (16px gap); each keeps the 4px #1565c0 top border.
- **Long publication or news lists**: a list under a cobalt h2 with dates in 600 #333333 and titles as #3273dc links; separate groups with h3 subsections (4px cobalt bar), not cards.
- **More videos**: use `.video-grid-3` (three 320px columns, 20px gap) with italic captions; reserve `.video-grid-1` (640px) for a single spotlight.

## Do's and Don'ts

- Do keep #1565c0 for structure only: the pill, h2, h3 bars, card tops, the active tab and button hover.
- Do open every section with a 1px #dee2e6 rule and a 32px blue h2.
- Do caption every figure and video in grey italics, centred.
- Do size figures individually with max-width so diagrams are not blown up to the full column.
- Don't use the cobalt for body links; links use the lighter #3273dc.
- Don't add shadows to figures or cards; separation comes from rules and light grey fills.
- Don't let paragraphs run ragged; main text is justified.

## Surfaces

White page and header; frosted near-white bars (rgba(251,251,253,0.92) with blur) at the top; light grey #f8f9fa for stage cards, the BibTeX block and the footer; charcoal #333333 only for buttons and the scroll-to-top disc.

## Imagery

Blue simulation renders of a drone-volleyball court (grid floor, white net with yellow posts, red and black quadrotors), clean vector method diagrams on white with pastel panels, plot and table images, and real-world indoor drone clips in the video grids.

## Layout

Centred header, then a single 1000px column of ruled sections. Text paragraphs run the full measure (justified); figures are centred at their own widths; stage cards and video grids are the only multi-column elements.

## Agent Prompt Guide

Quick colors: page #ffffff, text #333333, accent #1565c0, link #3273dc, h3 #444444, caption #555555, muted #666666, hairline #dee2e6, light fill #f8f9fa.

1. "Build a centred header with padding 40px 0 and a 1px #dee2e6 bottom border under a fixed 52px bar (rgba(251,251,253,0.92), backdrop-filter saturate(180%) blur(20px)). Venue pill: #1565c0, #ffffff Inter 21.6px/600, padding 6px 20px, radius 20px. Title Inter 38.4px/700 #333333, line-height 1.2. Authors 16.8px #333333, affiliation 14.4px #666666. Buttons: #333333 fill, #ffffff 16px/600, padding 10px 20px, radius 30px, 15px gap, hover #1565c0."
2. "Create section headings: each section has a 1px #dee2e6 top border, padding-top 20px, margin-bottom 40px; h2 Inter 32px/700 #1565c0; h3 20.8px/700 #444444 with a 4px #1565c0 left border and 10px padding-left. Body 16px/1.6 #333333, justified; links #3273dc."
3. "Make a three-card stage grid: 3 columns, 16px gap; each card #f8f9fa, 1px #dee2e6 border, 4px #1565c0 top border, radius 8px, padding 16px; title 16px/700 #1565c0, text 14.4px #555555. Follow with a centred figure and a 14.4px italic #555555 caption."

## Similar Pages

- Pages built from the VS-Bench project template (Inter, cobalt h2s with hairline section rules, charcoal pill buttons).
- Multi-project research series sites that share a frosted project-switcher bar across sibling papers.

## Quick Start

```css
:root {
  --primary-color: #1565c0;
  --bg-color: #ffffff;
  --text-color: #333333;
  --light-gray: #f8f9fa;
  --border-color: #dee2e6;
  --link: #3273dc;
  --caption: #555555;
  --muted: #666666;
  --font: 'Inter', sans-serif;
  --column: 1000px;
}
body { font-family: var(--font); line-height: 1.6; color: var(--text-color); background: var(--bg-color); padding-top: 52px; }
h2 { font-size: 2rem; color: var(--primary-color); margin: 10px 0 16px; }
section { padding-top: 20px; margin-bottom: 40px; border-top: 1px solid var(--border-color); }
```

## Provenance

- **URL**: https://hi-co-self-play.github.io/
- **Paper**: Mastering Multi-Drone Volleyball through Hierarchical Co-Self-Play Reinforcement Learning (arXiv 2505.04317), Ruize Zhang, Sirui Xiang, Zelai Xu, Feng Gao, Shilong Ji, Wenhao Tang, Wenbo Ding, Chao Yu, Yu Wang (Tsinghua University).
- **Venue**: CoRL 2025.
- **Selection reason**: the arXiv comment states acceptance at CoRL 2025 and the abstract links this project page.
- **Template credit**: `css/index.css` states "HCSP Paper Website — adapted from VS-Bench template"; footer licence CC BY-SA 4.0.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), selector probes at 1440, the 1440×900 and full-page screenshots, and `css/index.css` and `index.html` read directly, on 2026-10-28.
