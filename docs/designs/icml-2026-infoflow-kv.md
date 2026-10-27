# InfoFlow KV — Style Reference

> A mission-control console at night: cyan signal lines converge on one glowing node while amber sparks drift through the dark.

**Theme:** dark

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share) and the 1440×900 screenshot, cross-checked against the page's own `styles.css`. The stylesheet declares every color in OKLCH; hex values below are exact conversions of those declarations, and the rendered pixels agree with them. The hero stat numbers count up on load, so a screenshot taken mid-animation shows smaller numbers (1.02×, 0.75×) than the final 3.49× and 2.57× written in the markup.

## Overview

A hand-built single-page site with a dark navy ground (#080c16), not a Bulma or Nerfies template. The hero fills the viewport with an animated canvas: dim dots and amber sparks, plus thin curves that flow from the left edge into one glowing node at about 80% width. Over it sits a left-aligned stack: a cyan pill eyebrow, a 138px Space Grotesk title on two lines (white "InfoFlow", cyan-to-violet gradient "KV"), a light Sora subtitle, three glassy stat tiles, authors, mono affiliations and three buttons, one of them a cyan-violet gradient. Below the hero, ten numbered sections ("01 — The setting") run in a 920px column with mono kickers, 46px headlines whose emphasized words carry the same gradient, glass panels with 16–18px radii, interactive diagrams and dark results tables with cyan best-cell highlights. Amber (#ffaf43) is reserved for "recomputed" tokens and equal-contribution stars.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): navy family #080c16 / #0c121f / #070c16 / #070b15 / #0c0e19 / #080e18 / #090c16 together 93.6%; #364a59 (blended text, lines and glow) 6.4%. The cyan and amber accents occupy too little area to register as their own clusters.

Anatomy in DOM order (desktop 1440px; hero content block starts at x=180, left-aligned):

1. **Fixed nav bar** (0–49px): padding 16px 28px, gradient from navy at 85% opacity to transparent, backdrop blur 10px. Left: 8px cyan dot with 12px cyan glow, then "InfoFlow" in JetBrains Mono 13px/500 #f0f4f9 and "KV" in #00c6fb. Right: links Setting, Method, Results, Cite, Code ↗ in JetBrains Mono 12px/400 #959fac, letter-spacing 0.03em, 22px apart; "arXiv ↗" in #00c6fb.
2. **Hero** (`header.hero`, 0–939px): min-height 100svh, padding 120px 28px 80px, content vertically centred. Canvas particle field fills it at 0.9 opacity; a radial navy mask darkens the text side.
3. **Eyebrow pill** (y≈120): "● ICML 2026 · ARXIV:2603.05353", JetBrains Mono 12px uppercase, letter-spacing 0.16em, #00c6fb, padding 7px 14px, 999px radius, 1px border cyan at 35%, fill cyan at 7%, inset cyan glow. Gap to title 26px.
4. **Title** (`h1.title`, y=178, 254px tall): Space Grotesk 138px/700, line-height 0.92, letter-spacing -0.04em (-5.52px). Line 1 "InfoFlow" #f0f4f9; line 2 "KV" gradient 100deg #00c6fb → #a476ff 55% → #ffaf43 110%, clipped to text, with a cyan drop-shadow glow. Gap 22px.
5. **Subtitle** (`p.hero-sub`, y=454): Sora 22px/300, line-height 1.5, #bfc8d3, max-width 620px; bold phrases Sora 600 #f0f4f9. Gap 30px.
6. **Stat tiles** (`.metrics`, y≈616): three tiles in a row, gap 14px. Value Space Grotesk 30px/700 with the number in #00c6fb; label JetBrains Mono 11px uppercase #959fac, letter-spacing 0.06em. Gap 34px.
7. **Authors** (`.byline`, y≈730): Sora 15px, line-height 1.7, #bfc8d3; superscripts 10px/600 #00c6fb; equal-contribution stars #ffaf43.
8. **Affiliations** (`.affil`, 4px below): JetBrains Mono 12px #959fac, items 16px apart; "* equal contribution" in #ffaf43. Gap 30px.
9. **Buttons** (`.btns`, y=816, 43px tall): Paper (gradient primary), Code, BibTeX; gap 12px.
10. **Scroll cue**: "SCROLL" JetBrains Mono 10.5px, letter-spacing 0.22em, #778190, centred 26px above the hero bottom, over a 38px cyan-to-transparent pulsing line.

No teaser image or video appears in the first viewport; the canvas animation is the hero visual.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Deep Navy | #080c16 | --bg | body background, nav gradient base, hero mask, equation boxes |
| Navy 2 | #0d131e | --bg-2 | results table wrapper, BibTeX block, step rows, figure wrap top |
| Navy 3 | #151c2a | --bg-3 | inline chips, model-group rows in tables, idle tokens, step hover |
| Glass Panel | #111723 at 55% | --panel | stat tiles, secondary buttons, TL;DR box, pillars, cards, tabs |
| Ice White | #f0f4f9 | --ink | title line 1, h2/h3, nav brand, button text, bold text |
| Mist | #bfc8d3 | --ink-2 | subtitle, body paragraphs, authors, table cells, BibTeX text |
| Slate | #959fac | --ink-3 | nav links, stat labels, affiliations, captions, card body |
| Dim Slate | #778190 | --ink-4 | table headers, scroll cue, footer text, card kickers |
| Line | #2e3544 | --line | secondary button border, column dividers |
| Line 2 | #202633 | --line-2 | tile, card, table-row and footer borders |
| Signal Cyan | #00c6fb | --accent | eyebrow, "KV" gradient start, stat numbers, kickers, superscripts, links, best table cell |
| Violet | #a476ff | --accent-2 | gradient end on primary button, "KV", h2 emphasis, step numbers |
| Amber | #ffaf43 | --hot | equal-contribution stars, selected tokens, BibTeX string values, "click" cue |
| Ember | #ff6f4a | --hot-2 | numbered badges in the setting panels, score-bar gradient end |
| Button Ink | #090d16 | (literal oklch 0.16) | text on the gradient primary button and active toggles |

Four chunk colors (#00c6fb family) appear only inside the interactive token demo and are not part of the page chrome.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | "Space Grotesk", system-ui, sans-serif | Space Grotesk 400/500/600/700 | Manrope |
| Text | "Sora", system-ui, sans-serif | Sora 300/400/500/600 | Lexend |
| Mono | "JetBrains Mono", ui-monospace, Menlo, monospace | JetBrains Mono 400/500/600 | IBM Plex Mono |

| Role | Selector | Size / weight / line-height | Tracking | Color |
|---|---|---|---|---|
| Paper title | `h1.title` | clamp(52px, 11vw, 138px) / 700 / 0.92; 138px at 1440 | -0.04em | #f0f4f9, line 2 gradient |
| Section heading | `h2.h2` | clamp(30px, 4.4vw, 46px) / 600 / 1.04; 46px at 1440 | -0.025em | #f0f4f9, `em` gradient #00c6fb→#a476ff |
| Kicker | `.kicker` | JetBrains Mono 12px / 400 uppercase | 0.18em | #00c6fb, 28px cyan rule before |
| Insight heading | `.insight h3` | 25px / 600 / 1.2 | -0.02em | #f0f4f9 |
| Step heading | `.step h3` | 21px / 600 / 1.2 | -0.01em | #f0f4f9 |
| Card heading | `.mcard h3`, `.tldr .hd h3` | 18px / 600 | -0.01em | #f0f4f9 |
| Hero subtitle | `p.hero-sub` | clamp(17px, 2.1vw, 22px) / 300 / 1.5 | 0 | #bfc8d3 |
| Lede | `p.lede` | clamp(17px, 2vw, 21px) / 300 / 1.55 | 0 | #bfc8d3 |
| Body | `p.body` | 16.5px / 300 / 1.7, max-width 740px | 0 | #bfc8d3, `em` 500 #f0f4f9 |
| Stat value | `.metric .v` | 30px / 700 / 1 | -0.02em | #f0f4f9, number #00c6fb |
| Big card number | `.spcard .big` | 52px / 700 / 1 | -0.03em | gradient #00c6fb→#ffaf43 |
| Authors | `.byline` | 15px / 400 / 1.7 | 0 | #bfc8d3 |
| Button / tab | `.btn`, `.tab` | JetBrains Mono 13px / 500 (primary 600) | 0.02em | #f0f4f9 |
| Table body | `table.results td` | Sora 13.5px tabular-nums | 0 | #bfc8d3 |
| Table header | `table.results th` | JetBrains Mono 10.5px / 500 uppercase | 0.05em | #778190 |
| Caption | `.figcap` | 14px / 300 / 1.55 | 0 | #959fac, lead tag mono 11px #00c6fb |
| BibTeX | `pre.bib` | JetBrains Mono 12.5px / 1.65 | 0 | #bfc8d3, keys #00c6fb, strings #ffaf43 |
| Footer | `footer` | JetBrains Mono 12px | 0 | #778190 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Eyebrow pill | 999px | 1px cyan at 35% | inset 0 0 30px cyan at 12% |
| Hero buttons | 12px | 1px #2e3544 (primary transparent) | hover 0 10px 40px cyan at 18% + 1px inset cyan ring |
| Stat tiles | 14px | 1px #202633 | none; backdrop blur 8px |
| Cards (pillar, mcard, svis, rostep, spcard) | 16px | 1px #202633 | pillar hover 0 24px 60px cyan at 18% |
| TL;DR, figure wrap, token demo, step stack | 18px | 1px #202633 | none |
| Results table wrapper, BibTeX | 16px | 1px #202633 | none |
| Equation box | 12px | 1px #202633, 3px cyan-to-violet left bar | none |
| Inline chip | 6px | 1px #202633 | none |
| Diagram stage buttons | 10px | 2px rotating conic gradient (idle) | active 0 6px 24px cyan at 30% |
| Selected token | 6px | 1px #ffaf43 | 0 0 0 3px amber at 22%, 0 0 22px amber at 50% |

Background texture: a fixed 46px grid of #2e3544 lines at 35% (layer opacity 0.4), masked to fade out below the top, plus three soft radial glows (cyan top-right, violet top-left, amber bottom).

## Layout Metrics

- **Containers**: hero content `max-width: 1080px; margin: 0 auto` inside 28px hero padding (x=180 at 1440). Sections `.section { max-width: 920px; margin: 0 auto }`; `.block` then sets padding to 96px 0, so sections have no side gutter of their own (x=260 at 1440). Body paragraphs cap at 740px.
- **Hero**: min-height 100svh; padding 120px 28px 80px; rendered 939px tall at 1440×900 because the content block (739px) plus padding exceeds the viewport.
- **Section rhythm**: 96px top and bottom padding per section (192px between section contents); kicker → h2 16px; h2 → lede 18px; lede → first panel 24–30px.
- **Grids**: pillars and speed cards 3 columns gap 18px; setting and method cards 2 columns gap 18–20px; insight rows 200px label + 1fr, gap 30px, label sticky at top 90px.
- **Figures**: diagrams and tables fill the 920px column; wide results table has min-width 920px and scrolls horizontally inside its wrapper.
- **Footer**: max-width 1080px, 60px top margin, padding 34px 28px 60px, top hairline.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1255px | hero 28px + centring; sections centred at 920px | 16.5px | 138px | all multi-column grids active |
| <920px | hero keeps 28px; sections lose all side gutter (`.block` padding is 96px 0), so text runs to the viewport edge | 16.5px | 11vw ≈ 100px | — |
| 860px | as above | 16.5px | ≈ 95px | reorder steps → 1 column |
| 820px | as above | 16.5px | ≈ 90px | three-cell rows → 1 column; RoPE rows 96px + 1fr |
| 760px | as above | 16.5px | ≈ 84px | pillars, speed cards, mask cards → 1 column |
| 700px | as above | 16.5px | ≈ 77px | insight rows stack, gap 14px |
| 680px | as above | 16.5px | ≈ 75px | nav hides all links except Code ↗ and arXiv ↗; setting and method cards → 1 column |
| ≤473px | as above | 16.5px | 52px floor | — |

## Components

- **Gradient primary button** (`.btn.primary`): inline-flex, gap 9px, 15px stroke icon on the left (external-link arrow), JetBrains Mono 13px/600, letter-spacing 0.02em, padding 12px 18px, radius 12px, background linear-gradient(120deg, #00c6fb, #a476ff), text #090d16, transparent border. Hover lifts 2px and adds 0 12px 44px cyan at 45%.
- **Glass button** (`.btn`): same shape; background #111723 at 55% with backdrop blur 8px, 1px #2e3544 border, text #f0f4f9, weight 500, GitHub or book icon left. Hover: translateY(-2px), border #00c6fb, glow 0 10px 40px cyan at 18%.
- **Stat tile** (`.metric`): padding 14px 20px, min-width 150px, radius 14px, 1px #202633 border, #111723 at 55% fill with blur. Value Space Grotesk 30px/700 (number in #00c6fb, counts up on scroll-in); label JetBrains Mono 11px uppercase #959fac, 7px below.
- **Section kicker** (`.kicker`): "01 — The setting", JetBrains Mono 12px uppercase, letter-spacing 0.18em, #00c6fb, preceded by a 28×1px cyan line with 10px glow, 16px below it the h2.
- **TL;DR panel** (`.tldr`): radius 18px glass box; header row padding 18px 24px with a cyan-at-8% to transparent wash and a hairline under it; list rows padding 16px 24px separated by #202633 hairlines, mono cyan index 13px/600 on the left.
- **Step stack** (`.steps`): rows on #0d131e separated by 1px gaps showing #202633, radius 18px outer; each row grid 54px + 1fr, padding 26px 28px; big gradient numeral 34px/700; hover #151c2a.
- **Equation strip** (`.eq`): JetBrains Mono 14px #f0f4f9 on #080c16, 1px #202633 border, radius 12px, padding 16px 20px, 3px cyan-to-violet bar on the left edge.
- **Tabs** (`.tab`): JetBrains Mono 12.5px, padding 11px 16px, radius 11px, 1px #202633 border, glass fill, #959fac text; active: #00c6fb border, cyan at 8% fill, inset cyan ring, #f0f4f9 text.
- **Results table** (`table.results`): inside a #0d131e wrapper with 1px #202633 border and 16px radius; cells padding 11px 12px, right-aligned except the first column (18px left padding); headers mono 10.5px uppercase #778190; model-group rows Space Grotesk 15px/600 on #151c2a; best cell 700 #00c6fb on cyan at 20%; second-best 600 #f0f4f9 on cyan at 9%; "ours" row cyan-to-violet wash with a 3px cyan inset on the first cell; baseline rows italic #778190; row hover cyan at 6%.
- **BibTeX block** (`pre.bib`): mono 12.5px on #0d131e, radius 16px, padding 22px; keys cyan, string values amber; copy button top-right, mono 11px, radius 9px, glass fill, hover border cyan.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky nav | yes | fixed transparent-to-navy gradient bar, mono links, blur |
| Venue badge | yes | cyan pill eyebrow with pulsing dot, includes arXiv id |
| Title block | yes | 138px two-line wordmark, second line gradient |
| Stat strip | yes | three glass tiles in the hero |
| Authors / affiliations | yes | Sora byline, mono affiliation row, amber equal-contribution stars |
| Link buttons | yes | Paper (gradient), Code, BibTeX; mono labels with stroke icons |
| Teaser image or video | absent from the source | canvas particle animation stands in for it |
| Abstract | present but non-standard | no "Abstract" heading; the hero subtitle and a TL;DR list carry it |
| Method figures | yes | interactive SVG diagrams in glass figure wraps with stage buttons |
| Interactive demo | yes | token-selection demo with mode switch and amber selected tokens |
| Results tables | yes | dark tables with tabs, cyan best and second-best cells |
| Speed-up cards | yes | 3 cards with 52px gradient numbers and bar rows |
| BibTeX | yes | dark mono block with copy button |
| Footer | yes | mono line with venue and contact, hairline on top |
| Video, carousel | absent from the source | — |

## Adapting to Other Content

- **More authors**: keep the byline as one wrapping Sora 15px paragraph at max-width 760px; each name stays `white-space: nowrap`. Beyond two lines, add a second mono affiliation row rather than shrinking type.
- **A teaser figure**: place it below the buttons inside a 16px-radius glass frame (#111723 at 55%, 1px #202633), or move it to section 01; do not put a bright photo in the hero, because the canvas and white title depend on a dark ground.
- **Results tables**: reuse `table.results` exactly; mark the proposed row with the cyan-to-violet wash and use cyan only for best values, never amber.
- **Long publication or news lists**: use the TL;DR list pattern: mono cyan index or date column at 26px min-width, 15.5px #bfc8d3 text, hairline rows inside an 18px-radius glass box.
- **Light content (photos, white-background plots)**: inset them on #0d131e with 22–28px padding so the white edges do not touch the navy page.

## Do's and Don'ts

- Do keep every surface navy; layers differ by 2–4 OKLCH lightness steps (#080c16, #0d131e, #151c2a), never by gray.
- Do confine the cyan-to-violet gradient to one element per block: the title's second line, an h2 `em`, a numeral or the primary button.
- Do keep amber (#ffaf43) for the "recomputed / selected" meaning and equal-contribution marks.
- Do set all labels, metadata and buttons in JetBrains Mono and all prose in Sora 300.
- Don't use pure white text; #f0f4f9 is the brightest ink.
- Don't add drop shadows to cards at rest; depth comes from hairline borders, blur and hover glows.
- Don't centre the hero; it is a left-aligned stack.

## Surfaces

Navy page (#080c16) with a fixed grid texture and three radial glows; glass panels (#111723 at 55% plus blur) for tiles, cards, tabs and buttons; solid #0d131e for tables, step rows and code; #151c2a for chips and group rows. Every panel has a 1px #202633 border.

## Imagery

No photographs. All visuals are generated: the hero canvas (dots, amber sparks, flow curves converging on a glowing node), inline SVG diagrams of chunk positions and attention, token-chip grids in four chunk colors, bar rows and score bars. Diagrams sit on the same navy and reuse the accent palette.

## Layout

Full-viewport left-aligned hero over a 1080px container, then a single 920px reading column of ten numbered sections separated by 96px padding. Inside sections, content alternates between prose, two- or three-column card grids, and full-width interactive panels. Page height about 9,600px at 1440 wide.

## Agent Prompt Guide

Quick colors: page #080c16, panel #111723 at 55%, raised #0d131e, chip #151c2a, ink #f0f4f9 / #bfc8d3 / #959fac / #778190, border #202633, accent #00c6fb → #a476ff, highlight #ffaf43.

1. "Build a dark hero: background #080c16, padding 120px 28px 80px, min-height 100svh, content left-aligned in a 1080px container. Cyan pill eyebrow (JetBrains Mono 12px uppercase, letter-spacing 0.16em, #00c6fb, 999px radius, padding 7px 14px). Title in Space Grotesk 138px/700, line-height 0.92, letter-spacing -0.04em: line 1 #f0f4f9, line 2 gradient 100deg #00c6fb → #a476ff → #ffaf43 clipped to text. Subtitle Sora 22px/300 #bfc8d3, max-width 620px."
2. "Make stat tiles: flex row gap 14px; each tile padding 14px 20px, radius 14px, 1px #202633 border, background #111723 at 55% with 8px backdrop blur. Value Space Grotesk 30px/700 with the number in #00c6fb; label JetBrains Mono 11px uppercase #959fac, letter-spacing 0.06em, 7px below."
3. "Create link buttons: JetBrains Mono 13px/500, padding 12px 18px, radius 12px, icon left at 15px. Primary: linear-gradient(120deg, #00c6fb, #a476ff), text #090d16, weight 600. Secondary: #111723 at 55% fill, 1px #2e3544 border, text #f0f4f9; hover translateY(-2px) and border #00c6fb."

## Similar Pages

- Hand-built dark "product launch" research pages with canvas hero animations and numbered sections.
- Pages that pair a grotesk display face with a mono metadata layer (eyebrow pills, uppercase kickers, mono table headers).

## Quick Start

```css
:root {
  --bg: #080c16;
  --bg-2: #0d131e;
  --bg-3: #151c2a;
  --panel: rgba(17, 23, 35, 0.55);
  --ink: #f0f4f9;
  --ink-2: #bfc8d3;
  --ink-3: #959fac;
  --ink-4: #778190;
  --line: #2e3544;
  --line-2: #202633;
  --accent: #00c6fb;
  --accent-2: #a476ff;
  --hot: #ffaf43;
  --hot-2: #ff6f4a;
  --on-accent: #090d16;
  --font-display: "Space Grotesk", system-ui, sans-serif;
  --font-sans: "Sora", system-ui, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, Menlo, monospace;
  --maxw: 1080px;
  --section-w: 920px;
  --radius-card: 16px;
  --radius-btn: 12px;
}
```

## Provenance

- **URL**: https://infoflow-kv.github.io
- **Paper**: InfoFlow KV: Information-Flow-Aware KV Recomputation for Long Context (arXiv 2603.05353), Xin Teng et al.
- **Venue**: ICML 2026.
- **Selection reason**: the arXiv comment states acceptance at ICML 2026 and links this project page.
- **Template credit**: none; a custom single-page build (`styles.css`, `app.js`) with no template attribution in the footer.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 screenshot, and the page's `styles.css` and `index.html` read directly, on 2026-10-28.
