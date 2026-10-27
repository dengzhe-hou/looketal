# UniPixie — Style Reference

> A product launch page for a physics engine: frosted pill nav, heavy sans headlines and a sky-to-red gradient running through every accent.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, and a DOM probe of the hero and every card type), the 1440×900 and full-page screenshots, and the page's own `static/css/index.css` read directly (Bulma 0.9 underneath). Noto Sans loads from Google Fonts in weights 400–900 and renders everywhere; the stylesheet's `'Google Sans'` declarations are overridden later in the same file by `--font-sans: 'Noto Sans'`.

## Overview

A Nerfies-derived Bulma page reworked into a polished product-style layout on pure white. A sticky frosted navbar (white at 76% with a 14px blur) holds a bold home link at the left and six section links at the right; the current section gets a white pill with a sky-blue-to-red gradient border and a short gradient underline. The hero is centred: a 48px Noto Sans 900 title over two lines in slate-ink #0f172a, Bulma-blue author links, affiliations and notes in 20px and 16px, and a row of six dark #363636 rounded pill buttons (the two "Coming Soon" ones at 58% opacity). Under the buttons a one-line claim sits in a white card with an 18px radius and a 1.5px sky → red gradient border, with "soft-to-stiff spectrum" set as gradient-clipped text and the rest of the key phrase in royal blue. A framed teaser card (22px radius, grey hairline, large soft shadow) holds the teaser figure; its caption uses inline gradient α and solver badges in blue, amber and red tints. Below, sections separated by faint khaki hairlines bring a justified abstract, three icon feature cards, four stat tiles (one with a shimmering khaki-gold numeral), a pipeline figure, method step cards, result blocks with amber-ruled insight notes, resource cards and a BibTeX block. A fixed dot navigator appears at the right edge after scrolling.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 61.6% with near-whites #fcfafa 5.4%, #fdfdfd 4.6%, #feffff 2.7%, #fffffc 0.2%; teaser figure greys and card edges #d3d7dc 10.2% and #f5f7f7 8.6%; dark pill buttons, title ink and figure shading #78777c 6.6%. The blue author links and the gradient border are too thin to form their own clusters.

Anatomy in DOM order (desktop 1440px; Bulma `.container.is-max-desktop` 960px at x=240):

1. **Navbar** (`nav.project-navbar`, 0–66px, sticky): rgba(255,255,255,0.76), backdrop blur 14px, 1px rgba(226,232,240,0.8) bottom rule, shadow 0 8px 28px rgba(15,23,42,0.055), padding 5.6px 20px. Left: home icon + "UniPixie" 16px/900 #0f172a, letter-spacing -0.24px. Right (x=824–1419): Abstract, Overview, Method, Results, Resources, BibTeX at 16px/750 #334155, each a 39px pill with padding 7.68px 13.6px.
2. **Title** (`h1.publication-title`, y=126, 104px for two lines): Noto Sans 48px/900, line-height 1.08, letter-spacing -1.2px, #0f172a, centred. Gap 24px.
3. **Authors** (y=253–323, two lines): 20px/400 line-height 30px; names #209cee, separators and superscripts #1f2937. Gap 8px.
4. **Affiliations** (y=331): 20px/400 #1f2937 with superscript numbers. Gap 7px.
5. **Notes** (y=373): "* Equal contribution", "† Work done during an internship at UPenn", 16px #1f2937.
6. **Buttons** (y=421, 40px tall, 4px apart): Paper, arXiv, Video, Twitter, Code Coming Soon, Data Coming Soon; #363636 pills, white 16px, icon left. Gap 38px.
7. **Claim card** (`.project-tldr-card`, y=499–600, 960px): white, 18px radius, 1.5px gradient border (rgba(56,189,248,0.55) → rgba(239,68,68,0.55)), shadow 0 12px 32px rgba(15,23,42,0.08), padding 18.4px 25.6px. Text 21.6px/650 #0f172a, line-height 1.45, centred; "UniPixie" 800, "soft-to-stiff spectrum" 800 gradient text (#0ea5e9 → #38bdf8 → #ef4444), "simulation-ready 3D physical parameters" 800 #1d4ed8. Gap 57px.
8. **Teaser card** (`.teaser-card`, y=657–1027, 912px at x=264): white, 1px #e5e7eb border, 22px radius, padding 11.2px, shadow 0 18px 45px rgba(15,23,42,0.10); image inside with 16px radius. Its top half shows above the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Slate Ink | #0f172a | (literal) | title, section titles, card titles, claim text, stat numbers, nav home link, step-index circles |
| Body Ink | #1f2937 | (literal) | body text, author separators, affiliations, notes |
| Slate Copy | #334155 | (literal) | nav links, abstract and section lead copy, teaser caption, insight text, alpha labels |
| Muted Slate | #475569 | (literal) | card paragraphs, figure captions |
| Label Grey | #64748b | (literal) | stat labels (uppercase), resource card text |
| Author Blue | #209cee | hsl(204,86%,53%) | author name links, body links |
| Pill Charcoal | #363636 | Bulma `.is-dark` | link buttons |
| Sky | #38bdf8 | (literal) | gradient start: claim-card border, nav current pill border and underline, α badge, soft-icon |
| Signal Red | #ef4444 | (literal) | gradient end of the same accents, spectrum text end |
| Deep Sky | #0ea5e9 | (literal) | spectrum text start, home link hover |
| Royal Blue | #1d4ed8 | (literal) | highlighted phrase in the claim card |
| Hairline | #e5e7eb | (literal) | card borders, teaser card border, pre border, video frames |
| Insight Amber | #f59e0b | (literal) | 4px left rule of result insight notes |
| Insight Cream | #fffaf0 | (literal) | result insight fill |
| Code Mist | #f8fafc | (literal) | BibTeX pre fill, video frame fill |
| Footer Grey | #fafafa | Bulma footer | footer band |
| Dot Pink | #f472b6 | (literal) | active dot in the side navigator and video switcher |
| Dot Grey | #cbd5e1 | (literal) | idle video-switcher dots, α gradient bar border |
| Khaki Gold | #c7ad61 | (literal) | shimmering gradient numeral "3" in the stat row (#8a6f2d → #fff0b8 → #fff7d6) |

Solver badges use paired tints: MPM #0369a1 on #e0f2fe (border #bae6fd), LBS #92400e on #fef3c7 (border #fde68a), Spring-Mass #991b1b on #fee2e2 (border #fecaca). Feature icons are 135° gradients: #38bdf8 → #ef4444, #2563eb → #14b8a6, #7c3aed → #2563eb.

Declared but not visible: each `.section-band` has a warm tint such as rgba(255,253,247,0.1); at 10% alpha on white they render as white. Only their 1px rgba(148,136,96,0.14) top hairline shows.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (everything) | 'Noto Sans', sans-serif (via `--font-sans`, overriding earlier 'Google Sans') | Noto Sans 400, 600, 700, 800, 900 | Inter |
| Mono | Bulma `monospace` | browser monospace (Consolas) | JetBrains Mono |
| Icons | Font Awesome 5.15 (SVG mode), Academicons | Font Awesome 5 Free/Brands, Academicons 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Title | `.publication-title` (`h1.title.is-1`) | 48px / 900 / 1.08, letter-spacing -0.025em | #0f172a |
| Section title | `.section-band h2.title` (`is-3`) | 32px / 850 / 36px, letter-spacing -0.018em | #0f172a |
| Results subsection | `.result-block h3.title.is-4` | 24px / 800, letter-spacing -0.01em | #0f172a |
| Card title | `.info-card h3.title.is-5` etc. | 20px / 800 / 22.5px, letter-spacing -0.01em | #0f172a |
| Claim | `.project-tldr` | 1.35rem = 21.6px / 650 / 1.45; spans 800 | #0f172a |
| Section copy | `.section-copy` | 1.2rem = 19.2px / 400 / 1.72; bold 850 | #334155 |
| Authors / affiliations | `.publication-authors` (`is-size-5`) | 20px / 400 / 30px | #209cee links, #1f2937 text |
| Teaser caption | `.teaser-caption` | 1.08rem = 17.28px / 400 / 1.55 | #334155 |
| Nav link | `.navbar-end > .navbar-item` | 16px / 750, letter-spacing -0.01em | #334155 (current and hover #0f172a) |
| Body | `body` | 16px / 400 / 24px | #1f2937 |
| Card text | `.info-card p` | 16px / 400 / 1.5 | #475569 |
| Stat number | `.stat-number` | 1.85rem = 29.6px / 800 / 1.1 | #0f172a |
| Stat label | `.stat-label` | 0.72rem = 11.52px / 300, uppercase, letter-spacing 0.13em, opacity 0.82 | #64748b |
| Solver badge | `.solver-badge` | 0.92rem = 14.72px / 750 | per badge |
| BibTeX | `pre` | 0.9rem = 14.4px / 1.5 monospace | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Nav pills, home link | 999px | current: 1px gradient (#38bdf8 → #ef4444 at 0.75) | current: 0 8px 20px rgba(15,23,42,0.08) |
| Link buttons | 290486px (Bulma rounded) | 1px transparent | none |
| Claim card | 18px | 1.5px gradient rgba(56,189,248,0.55) → rgba(239,68,68,0.55) | 0 12px 32px rgba(15,23,42,0.08) |
| Teaser card | 22px (image 16px) | 1px #e5e7eb | 0 18px 45px rgba(15,23,42,0.10) |
| Info, method-step, resource cards | 16px | 1px #e5e7eb | 0 10px 24px rgba(15,23,42,0.06) |
| Stat tiles | 16px | 1px #e5e7eb | none |
| Result block | 18px | 1px rgba(226,232,240,0.95) | 0 12px 28px rgba(15,23,42,0.055) |
| Insight note | 10px | 4px #f59e0b left | none |
| Feature icon | 50% (54px circle) | none | none |
| Step index | 50% (30px circle, #0f172a) | none | none |
| Solver and α badges | 999px | 1px tint border (solver) | none |
| BibTeX pre | 12px | 1px #e5e7eb | none |
| Side dot navigator | 999px | dots 1px rgba(15,23,42,0.08) | 0 8px 28px rgba(15,23,42,0.08) |

Cards are white at 86–88% with a 2px backdrop blur, which reads as solid white on this page.

## Layout Metrics

- **Container**: Bulma `.container.is-max-desktop`, max-width 960px, centred (x=240 at 1440); section side padding 24px.
- **Navbar**: min-height 4.1rem (66px rendered), padding 5.6px 20px, sticky at top 0.
- **Hero**: `.hero-body` padding-top 3.75rem (60px), bottom 1.25rem; title starts 60px under the navbar.
- **Claim card**: max-width 980px (renders at the 960px container), margin 33.6px auto 36px.
- **Teaser**: card max-width 980px, rendered 912px; caption max-width 920px, 20px below.
- **Sections**: `.section-band` padding 3.2rem (51.2px) top and bottom; the abstract uses `.section-compact-top` with 2rem (32px) top; 1px khaki hairline on top of each.
- **Section copy**: `width: min(920px, calc(100vw - 2rem))`, centred by translateX(-50%), so it can run wider than its column.
- **Grids**: Bulma columns with 24px gutters: three 304px feature, method and resource cards; four 222px stat tiles; result blocks full 960px, 48px apart.
- **Footer**: #fafafa, padding 48px 24px 96px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1216px | (100% − 960px)/2 | 16px | 48px | columns as authored; dot navigator visible after scroll |
| 1024–1215px | (100% − 960px)/2 | 16px | 48px | — |
| ≤1023/1024px | 24px (fluid container) | 16px | 48px | navbar collapses to a burger menu in a white 18px-radius sheet; side dot navigator hidden |
| ≤768px | 24px | 16px | 32px (`!important`) | Bulma columns stack to one; claim 16.8px with padding 16px 17.6px; section copy 17.28px full width; section padding 2.4rem; teaser card padding 7.2px, radius 16px |

## Components

- **Frosted nav pill** (`.navbar-end > .navbar-item`): padding 7.68px 13.6px, 999px radius, 16px/750 #334155. Hover: #0f172a, lift 1px, and a `::before` pill (white fill, 1px sky → red gradient border, 0 8px 20px rgba(15,23,42,0.08)) fades in to 55% opacity. Current section: the same pill at full opacity plus an 18×3px #38bdf8 → #ef4444 underline 4.5px from the bottom.
- **Dark link pill** (Bulma `.button.is-dark.is-rounded`): #363636, white 16px/400, height 40px, padding 7px 20px, Font Awesome or Academicons icon left; unreleased links get `.coming-soon` (opacity 0.58, pointer-events none).
- **Gradient-border claim card**: white padding-box over a 90° gradient border-box (1.5px, sky 0.55 → red 0.55), 18px radius, shadow 0 12px 32px rgba(15,23,42,0.08); one centred sentence at 21.6px/650 with 800-weight spans in #0f172a, gradient-clipped text and #1d4ed8.
- **Framed teaser card**: white, 1px #e5e7eb, 22px radius, 11.2px padding, 0 18px 45px rgba(15,23,42,0.10); caption below with an inline α badge (gradient pill, white 800) and solver tint badges.
- **Icon feature card** (`.info-card`): white 86%, 1px #e5e7eb, 16px radius, padding 24px, centred; 54px gradient circle icon (Font Awesome, white 20px), 20px/800 title, 16px #475569 text.
- **Stat tile** (`.stat-card`): same card without shadow, padding 18.4px 12px; 29.6px/800 number over an 11.52px/300 uppercase #64748b label tracked 0.13em. One number uses an animated khaki-gold gradient text with a drop shadow.
- **Method step** (`.method-step`): card with padding 22.4px 20px 20px and a 30px #0f172a numbered circle.
- **Result block** (`.result-block`): 960px card, 18px radius, padding 22.4px 24px 24.8px; table shown as an image inside a 12px-radius white frame; followed by an insight note: #fffaf0, 4px #f59e0b left rule, 10px radius, padding 13.6px 16px, #334155 text.
- **Video switcher**: rounded viewport (20px) with 46px white circular arrows (shadow 0 10px 24px rgba(15,23,42,0.10)) and 10px dots, #cbd5e1 idle, #f472b6 active with a 5px pink halo.
- **Side dot navigator**: fixed 26px from the right edge, frosted 999px capsule, 13px dots; active #f472b6, hover reveals a pill label to the left.
- **BibTeX**: `pre` #f8fafc, 1px #e5e7eb, 12px radius, 14.4px monospace.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky navigation | yes | frosted bar with gradient-bordered current-section pill |
| Title / authors / affiliations | yes | centred heavy sans title, blue author links, notes line |
| Venue | absent from the source | no CVPR badge or line on the page |
| Link buttons | yes | six dark rounded pills, two dimmed as "Coming Soon" |
| One-line claim (TL;DR) | yes | gradient-bordered card with gradient text |
| Teaser | yes | framed figure card with badge-studded caption |
| Abstract | yes | justified 19.2px copy, 920px |
| Feature cards | yes | three icon cards |
| Dataset stats | yes | four stat tiles |
| Method | yes | pipeline figure plus three numbered step cards |
| Results tables | present but non-standard | tables are images inside framed result blocks, with insight notes |
| Video results | yes | video switcher with arrows and dots |
| Resources | yes | three icon cards (Code, Dataset, Models) |
| BibTeX | yes | light rounded pre |
| Footer | yes | Bulma footer with Nerfies credit |
| Scroll navigator | yes | fixed dot rail on the right |

## Adapting to Other Content

- **More authors**: keep the 20px centred author block and let it wrap; keep links #209cee and superscripts in body ink. Put a venue line, if needed, as a 16px/700 #334155 line between notes and buttons rather than a badge.
- **A real HTML results table**: place it inside a `.result-block` card; header row 16px/800 #0f172a with a 1px #e5e7eb rule, body 16px #334155, best values 800 weight; follow with an amber insight note.
- **More stats or features**: extend the stat row in fours and the card grid in threes; keep shadows off the stat tiles.
- **Long publication or news lists**: use stacked white cards (16px radius, 1px #e5e7eb, padding 24px) with a 20px/800 title, an 11.52px uppercase #64748b date label and 16px #475569 summary.
- **Extra highlights**: use the solver-badge pattern (999px pill, tint fill, matching border, 750 weight) rather than new solid colours.

## Do's and Don'ts

- Do keep the sky → red gradient (#38bdf8 → #ef4444) for the few accent moments: claim border, current nav pill, α badge, spectrum text.
- Do use heavy Noto Sans weights (850–900 for titles, 800 for card titles) against light 300 uppercase labels.
- Do frame large media in white cards with 1px #e5e7eb borders, generous radii (16–22px) and soft slate shadows.
- Don't use flat blue for buttons; link buttons stay dark #363636 pills.
- Don't add section background colours; sections are white with a faint top hairline.
- Don't square off corners; every surface from badges to cards is rounded.

## Surfaces

White page and white cards; dark pills; frosted white nav and dot rail; #fffaf0 insight notes; #f8fafc code and video frames; #fafafa footer.

## Imagery

A three-panel teaser (property range renders, α-controlled bouncing objects on pink and blue grounds, multi-solver output tiles), a coloured pipeline diagram with numbered stages, results tables as images, simulation videos. Clean renders on light backgrounds, matching the page.

## Layout

Centred 960px single column: sticky nav, hero, claim card, teaser card, abstract, overview (feature cards, stat row, pipeline), method, results, resources, BibTeX, footer. About 6,760px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: ink #0f172a, copy #334155, body #1f2937, card text #475569, authors #209cee, pills #363636, gradient #38bdf8 → #ef4444, highlight #1d4ed8, hairline #e5e7eb, insight #fffaf0 with #f59e0b, footer #fafafa.

1. "Build a sticky frosted navbar: background rgba(255,255,255,0.76), backdrop-filter blur(14px), 1px rgba(226,232,240,0.8) bottom border, shadow 0 8px 28px rgba(15,23,42,0.055), min-height 66px. Left: home icon and 'Name' in Noto Sans 16px/900 #0f172a. Right: links 16px/750 #334155 in 999px pills with padding 7.68px 13.6px; the current one gets a white fill with a 1px linear-gradient(90deg, #38bdf8, #ef4444) border and an 18×3px gradient underline."
2. "Create a claim card: max-width 960px, centred, padding 18.4px 25.6px, radius 18px, border 1.5px solid transparent, background linear-gradient(#ffffff,#ffffff) padding-box, linear-gradient(90deg, rgba(56,189,248,0.55), rgba(239,68,68,0.55)) border-box, shadow 0 12px 32px rgba(15,23,42,0.08); one sentence Noto Sans 21.6px/650 #0f172a centred, key phrase 800 #1d4ed8."
3. "Make a stat row: four tiles in a row with 24px gaps, each white with 1px #e5e7eb border, 16px radius, padding 18.4px 12px, no shadow; number Noto Sans 29.6px/800 #0f172a; label 11.52px/300 uppercase, letter-spacing 0.13em, #64748b."

## Similar Pages

- Nerfies/Bulma academic pages restyled as product landing pages with card grids and stat tiles.
- Physics and simulation project pages with gradient accent systems and sticky section nav.

## Quick Start

```css
:root {
  --ink: #0f172a;
  --body: #1f2937;
  --copy: #334155;
  --muted: #475569;
  --label: #64748b;
  --author: #209cee;
  --pill: #363636;
  --grad-a: #38bdf8;
  --grad-b: #ef4444;
  --highlight: #1d4ed8;
  --hairline: #e5e7eb;
  --insight-bg: #fffaf0;
  --insight-rule: #f59e0b;
  --code-bg: #f8fafc;
  --card-shadow: 0 10px 24px rgba(15, 23, 42, 0.06);
  --font-sans: 'Noto Sans', sans-serif;
}
body { font: 16px/1.5 var(--font-sans); color: var(--body); background: #ffffff; }
.container { max-width: 960px; margin: 0 auto; }
```

## Provenance

- **URL**: https://unipixie.github.io/
- **Paper**: UniPixie: Unified and Probabilistic 3D Physics Learning via Flow Matching (arXiv 2606.05399), Qilin Huang et al.
- **Venue**: CVPR 2026, Highlight.
- **Selection reason**: the arXiv comment states publication at CVPR 2026 as a Highlight and links this page.
- **Template credit**: footer credits the Nerfies template; heavily customized in `static/css/index.css`.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), a DOM probe of hero and card components, the 1440×900 and full-page screenshots, and `index.css` and `index.html` read directly, on 2026-10-28.
