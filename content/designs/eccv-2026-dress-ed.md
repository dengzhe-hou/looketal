# Dress-ED — Style Reference

> An atelier lookbook on blue tissue paper: Garamond headlines with one phrase slipped into blue italic, then a single midnight-navy spread for the machinery.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, plus targeted probes of the hero, stat strip, sections, pipeline cards and citation), the 1440×900 shot and a full-page capture, and the page's single inline `<style>` block and markup. Hero elements fade up on load (0.7s, staggered 0.1–0.4s), so the 1440×900 screenshot shows the buttons and stat strip still semi-transparent; the values below are the settled state. The edit-type counters animate from 0 when scrolled into view and read 0 in the full-page capture.

## Overview

A single 860px column (7,221px tall) on pale blue-white #f5f9fe with navy ink #0d1f33. Type pairs EB Garamond for headlines, stat numbers and pull quotes with DM Sans (300–500) for everything else. The hero is centred: a hairline-bordered "ECCV 2026" tag, a 48px Garamond title whose middle phrase "Instruction-Guided Editing" is italic in cobalt #1a5fa8, a dot-separated author row (first two authors bold), small affiliations, a row of uppercase 3px-radius buttons (one filled cobalt, four outlined), and a ruled stat strip with five Garamond numbers in cobalt. Sections alternate #eaf3fb and the base #f5f9fe, each with an 11.5px tracked uppercase cobalt label and a 35.2px Garamond h2 that ends in a blue italic phrase. The Overview holds a ruled abstract callout (3px cobalt left bar on #e4f0fb). Then the page drops into a full-bleed midnight #0a1a2e section for the four-stage data pipeline: a 2×2 grid of #0e2240 cards with Roman-numeral circles and model chips in blue, gold, red and green, and a verification callout with a large "95.6%" in blue. After it, light again: colored edit-type cards with thin bars, an interactive sample browser with dropdowns, a method figure, a radar chart card and a BibTeX box, ending on a near-black #07111f footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): base #f5f9fe / #f6f9fe / #f4f9fe / #f8fbff / #f5f9fd together 82.1%; section tint #ecf4fb 15.0% (the Overview band entering at y=790); light gray-blue #c0cddb 2.9% (text and faded buttons blended). Cobalt covers too little area to form its own cluster.

Anatomy in DOM order (desktop 1440px, everything centred):

1. **Sticky nav** (`nav`, 0–48px): rgba(245,249,254,0.95) with `backdrop-filter: blur(10px)`, 1px #d0e2f4 bottom border, padding 10px 5vw (72px at 1440). Left "Dress-ED" in EB Garamond 16px/500 #1a5fa8; right six links in DM Sans 13.12px/400 #3a5570, letter-spacing .02em, 24px gaps; hover #1a5fa8.
2. **Hero** (`.hero`, max 860px, padding 72px 24px 56px → content x 314–1126).
3. **Venue tag** (`.venue-badge`, y=120, 108×30): 12px/500 uppercase, letter-spacing .12em, #1a5fa8, padding 4px 14px, 1px rgba(26,95,168,0.35) border, 2px radius. Gap 28px.
4. **Title** (`h1`, y=179, 115px, two lines): EB Garamond 48px/400, line-height 1.2, letter-spacing -0.01em, #0d1f33; "Instruction-Guided Editing" italic #1a5fa8. Gap 32px.
5. **Authors** (`.authors`, y=326): DM Sans 15.2px #0d1f33, flex-wrap with gaps 8px 4px, "·" separators in #d0e2f4; first two names in `strong` (700); superscripts .6em #1a5fa8. Gap 10px.
6. **Affiliations** (`.affiliations`, y=362, two lines): 12.48px #3a5570, line-height 1.8, superscripts in #1a5fa8; second line "* Equal contribution". Gap 36px.
7. **Buttons** (`.cta-row`, y=443, 42px tall, 12px gaps): "ARXIV PAPER" filled #1a5fa8 with white text; "GITHUB", "🤗 DATASET", "DATASET STATS", "RESULTS" outlined with 1px #d0e2f4 and #0d1f33 text; all DM Sans 13.12px/500 uppercase, letter-spacing .06em, padding 9px 20px, 3px radius, 14px SVG icon left on arXiv and GitHub. Gap 56px.
8. **Stat strip** (`.stat-strip`, y=541, 812×193): 1px #d0e2f4 top and bottom rules; items padding 20px 36px with 1px #d0e2f4 right rules; EB Garamond 32px/400 #1a5fa8 numbers (146k, 49k, 7, 3) and 11.52px uppercase .08em #3a5570 labels; the fifth item (95.6%, "Filter accuracy") wraps to a second centred row. Hero ends at y=790.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Ice | #f5f9fe | --bg | body, hero, plain sections, cards and chart card fill, dropdown fill |
| Section Tint | #eaf3fb | --section-bg | alternate sections (`.section-alt`), citation box, outline button hover |
| Accent Wash | #e4f0fb | --accent-light | abstract callout fill |
| Navy Ink | #0d1f33 | --text | title, h2, authors, body text, outline button text |
| Slate | #3a5570 | --text-light | nav links, affiliations, stat labels, captions, BibTeX text |
| Cobalt | #1a5fa8 | --accent | italic title phrase and h2 phrases, venue tag, nav logo, filled button, stat numbers, section labels, abstract bar, superscripts |
| Cobalt Hover | #154d8a | (literal) | filled button hover |
| Hairline Blue | #d0e2f4 | --border | nav rule, stat strip rules, outline buttons, cards, author separators |
| Teal | #1a7a8a | --teal | feature and contribution accents (second item) |
| Steel Blue | #2a6aaa | --gold | feature and contribution accents (third item) |
| Midnight | #0a1a2e | (literal, `.section-dark`) | pipeline section background |
| Deep Navy | #0e2240 | (literal) | pipeline step cards |
| Footer Night | #07111f | (literal) | footer background |
| Sky Label | #6ab0e8 | (literal) | section label and callout heading inside the dark section |
| Signal Blue | #4a90e8 | (literal) | step I circle and chip, verification callout bar, 95.6% figure |
| Stage Gold | #c9a800 | (literal) | step II circle; chip text #b89600 |
| Stage Red | #d94040 | (literal) | step III circle and chip |
| Stage Green | #2eaa60 | (literal) | step IV circle and chip |
| Dark Text | rgba(220,235,250,0.95) | (literal) | dark-section headings; body at 0.55 alpha |
| Mist | rgba(180,210,240,0.55) | (literal) | pipeline card text; at 0.08 the grid gaps and figure rules; at 0.42 the footer text |
| Signal Wash | rgba(30,110,200,0.1) | (literal) | verification callout fill; at 0.18 the step I circle |
| Edit-type dots | #c8522a / #e8834d / #2d6e6e / #b8930a / #7a5aaa / #5e8a3a / #3a7a8a | (inline styles) | dots and bars of the seven edit-type cards |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Serif | 'EB Garamond', Georgia, serif | EB Garamond 400, 400 italic, 500, 600 | Cormorant Garamond |
| Sans | 'DM Sans', system-ui, sans-serif | DM Sans 300, 400, 500 (700 for `strong` is synthesized) | DM Sans |
| Mono | 'Courier New', monospace | system Courier New | Courier Prime |

| Role | Selector | Size / weight / line-height / tracking | Color |
|---|---|---|---|
| Title | `.hero h1` | clamp(2rem, 5vw, 3rem) → 48px / 400 / 1.2 / -0.01em | #0d1f33, `em` italic #1a5fa8 |
| Section title | `.section-title` | clamp(1.5rem, 3.5vw, 2.2rem) → 35.2px / 400 / 1.25 | #0d1f33, `em` italic #1a5fa8 |
| Section label | `.section-label` | .72rem = 11.52px / 500 / uppercase / .16em | #1a5fa8 (#6ab0e8 on dark) |
| Body | `body` | 16px / 400 / 1.7 | #0d1f33 |
| Section body | `.section-body` | .92rem = 14.72px / 300 / 1.85, max 680px | #3a5570 |
| Abstract | `.abstract-box p` | .93rem = 14.88px / 300 / 1.8 | #0d1f33 |
| Venue tag | `.venue-badge` | .75rem = 12px / 500 / uppercase / .12em | #1a5fa8 |
| Authors | `.authors` | .95rem = 15.2px / 400 (bold first authors 700) | #0d1f33 |
| Affiliations | `.affiliations` | .78rem = 12.48px / 1.8 | #3a5570 |
| Button | `.btn` | .82rem = 13.12px / 500 / uppercase / .06em | white or #0d1f33 |
| Stat number | `.stat-n` | EB Garamond 2rem = 32px / 400 / 1 | #1a5fa8 |
| Stat label | `.stat-l` | .72rem / 400 / uppercase / .08em | #3a5570 |
| Card heading | `.pipeline-step h4`, `.chart-card h4` | EB Garamond 1.05rem / 1rem / 400 | rgba(220,235,250,0.9) / #0d1f33 |
| Pull quote | `.results-instruction em` | EB Garamond 1.15rem = 18.4px italic | #3a5570 |
| Big figure | `.big-pct` | EB Garamond 1.9rem / 400 | #4a90e8 |
| BibTeX | `.citation-box pre` | Courier New .78rem = 12.48px / 1.7 | #3a5570 |
| Footer | `footer` | .8rem = 12.8px / 300 / 1.9 | rgba(180,210,240,0.42) |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow / effect |
|---|---|---|---|
| Venue tag | 2px | 1px rgba(26,95,168,0.35) | none |
| Buttons | 3px | 1px #1a5fa8 or #d0e2f4 | color/background transition only |
| Abstract and verification callouts | 0 4px 4px 0 | 3px left bar #1a5fa8 / #4a90e8 | none |
| Edit-type cards, chart card, citation box | 4px | 1px #d0e2f4 | none |
| Figures and sample images | 6px | sample images 1px #d0e2f4 | overview figure `mix-blend-mode: multiply` |
| Step circles | 50%, 36px | 1px stage color at ~40% | fill at 18% |
| Model chips, copy button | 2px | copy 1px #d0e2f4 | none |
| Dropdowns | 4px | 1.5px #d0e2f4 | hover/focus border #1a5fa8 and `0 0 0 3px rgba(26,95,168,0.1)` |
| Edit-type bars | 1px | none | 2px track #d0e2f4 |

## Layout Metrics

- **Container**: `.hero` and `.section-inner` max-width 860px; sections padding 72px 24px → content x 290–1150 at 1440 (hero content 314–1126 because the hero adds 24px padding inside its 860px box).
- **Hero**: padding 72px 24px 56px; vertical chain 30 (tag) + 28 + 115 (title) + 32 + 26 (authors) + 10 + 45 (affiliations) + 36 + 42 (buttons) + 56 + 193 (stat strip) = 613px between y=120 and y=734.
- **Sections**: padding 72px 24px; label margin-bottom 12px; title margin-bottom 20px; abstract callout margin-top 32px, padding 24px 28px.
- **Pipeline grid**: 2 columns with 1px gaps on rgba(180,210,240,0.08), margin-top 40px; each card padding 32px 28px 0, a text block and a 4:3 figure slot aligned by subgrid.
- **Edit-type cards**: auto-fit minmax(160px, 1fr), gap 12px, padding 18px 16px → five per row at 860px.
- **Sample browser**: dropdowns min 180px, then four 3:4 images in a row (16px gap) with uppercase labels above.
- **Charts**: chart card padding 24px; chart heights 220px / 300px.
- **Footer**: padding 40px 5vw, centred.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| base (1440) | nav 72px (5vw); sections 24px inside 860px | 16px | 48px | 2-column pipeline, 4-up samples |
| ≤960px (5vw < 3rem) | same | 16px | 5vw, e.g. 38.4px at 768 | none |
| ≤640px | same | 16px | 32px (2rem floor) | pipeline, charts, method and results grids 1 column; funnel 1 column; stat items lose right rules and gain bottom rules; result images 1 column |

## Components

- **Venue tag**: inline-block, 12px/500 uppercase .12em #1a5fa8, padding 4px 14px, 1px rgba(26,95,168,0.35) border, 2px radius.
- **Italic accent headline**: EB Garamond 400 in #0d1f33 with one phrase in `em` italic #1a5fa8; often broken with a `<br>` before the accent phrase.
- **Filled button** (`.btn-primary`): 13.12px/500 uppercase .06em white on #1a5fa8, 1px #1a5fa8 border, padding 9px 20px, 3px radius, 8px gap to a left icon (document icon); hover #154d8a.
- **Outline button** (`.btn-outline`): transparent, #0d1f33 text, 1px #d0e2f4; hover #eaf3fb fill. GitHub uses its mark, Dataset uses the 🤗 emoji.
- **Stat strip**: centred flex-wrap between 1px #d0e2f4 top and bottom rules; items padding 20px 36px with 1px right rules; 32px Garamond #1a5fa8 number, 4px gap, 11.52px uppercase label.
- **Abstract callout** (`.abstract-box`): #e4f0fb fill, 3px #1a5fa8 left bar, radius 0 4px 4px 0, padding 24px 28px; "ABSTRACT" 11.2px/600 uppercase .14em #1a5fa8; text 14.88px/300 #0d1f33, line-height 1.8.
- **Pipeline card** (`.pipeline-step`): #0e2240, padding 32px 28px 0; 36px circle with a Roman numeral (Garamond 14.4px) in the stage color, background at 18% and border at ~40%; Garamond 16.8px heading in rgba(220,235,250,0.9); 13.12px/300 text at rgba(180,210,240,0.55); model chip 10.88px/500, padding 3px 10px, 2px radius, stage color on a 15% tint; figure slot below a 1px rgba(180,210,240,0.08) rule.
- **Verification callout** (`.accuracy-callout`): rgba(30,110,200,0.1) fill, 3px #4a90e8 left bar, radius 0 4px 4px 0, padding 24px 28px; heading Garamond #6ab0e8; big "95.6% human-model agreement" in Garamond 30.4px #4a90e8.
- **Edit-type card** (`.et-card`): #f5f9fe, 1px #d0e2f4, 4px radius, padding 18px 16px; 8px colored dot + 12.8px/500 name; Garamond 25.6px count; 11.2px/300 percent; 2px bar on a #d0e2f4 track that grows over 1.2s.
- **Dropdown** (`.dd-btn`): 13.12px, padding 8px 36px 8px 16px, 1.5px #d0e2f4 border, 4px radius, #f5f9fe fill, a 12px chevron in #3a5570 at right 12px; focus border #1a5fa8 with a 3px 10% cobalt ring.
- **Citation box**: #eaf3fb, 1px #d0e2f4, 4px radius, padding 24px; Courier New 12.48px #3a5570; "COPY" button top-right 11.2px/500 uppercase, padding 4px 12px, 1px #d0e2f4, 2px radius, hover #d0e2f4 fill.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky nav | yes | translucent ice bar with Garamond logo |
| Venue badge | yes | hairline-bordered uppercase tag |
| Title / authors / affiliations | yes | centred Garamond title with blue italic phrase, dot-separated authors |
| Link buttons | yes | one filled cobalt, four outlined, uppercase |
| Stat strip | yes | five ruled Garamond numbers in cobalt |
| Abstract | yes | ruled callout inside the Overview section |
| Teaser figure | present but non-standard | the overview figure sits below the abstract instead of in the hero |
| Pipeline | yes | full-bleed midnight section with a 2×2 card grid |
| Dataset statistics | yes | seven colored edit-type cards with bars |
| Interactive sample browser | yes | two dropdowns and four 3:4 images with an italic instruction quote |
| Results table | absent from the source | results are a Chart.js radar chart in a card |
| BibTeX | yes | tinted box with copy button |
| Footer | yes | near-black, centred, muted light-blue text |

## Adapting to Other Content

- **More authors**: keep the dot-separated flex-wrap row at 15.2px with gaps 8px 4px; let it wrap to a second centred line, and keep affiliations at 12.48px on their own lines.
- **A results table**: put it in a chart-card style container (#f5f9fe, 1px #d0e2f4, 4px radius, 24px padding) in the 860px column; header 10.88px/500 uppercase .1em #3a5570, cells 13.28px #0d1f33 with 1px #d0e2f4 row rules; mark the ours row with a 3px #1a5fa8 left bar and #e4f0fb fill, the same way the abstract callout is marked.
- **Long publication or news lists**: use edit-type card styling (1px #d0e2f4, 4px radius, 18px 16px padding) in an auto-fit minmax(160px, 1fr) grid, or a ruled list with the 11.52px uppercase cobalt label as the date.
- **A second dark section**: reuse #0a1a2e with #0e2240 cards and #6ab0e8 labels, but keep it to one per page so the transition stays an event.
- **More stats**: add stat-strip items; they wrap at 812px, so a sixth item joins the second row next to the fifth.

## Do's and Don'ts

- Do put one phrase of every headline in EB Garamond italic #1a5fa8.
- Do keep all type light: Garamond at 400, DM Sans body copy at 300 in sections.
- Do use hairline #d0e2f4 rules and 2–4px radii; nothing is heavily rounded.
- Do reserve the multi-color stage palette (blue, gold, red, green) for the pipeline and the edit-type palette for the dataset cards.
- Don't use shadows on cards; only the dropdown focus ring glows.
- Don't set headlines in bold; weight contrast comes from italic and color.
- Don't widen the column beyond 860px; figures and grids stay inside it.

## Surfaces

Ice #f5f9fe base alternating with #eaf3fb section bands; callouts on #e4f0fb with a cobalt bar; one full-bleed midnight #0a1a2e section with #0e2240 cards and translucent light-blue text; a #07111f footer. The nav is 95% ice with a 10px blur.

## Imagery

Fashion product photography on white: garments and full-body model shots in 3:4 frames, an overview collage with a pie chart and before/after edit pairs, colorful pastel pipeline block diagrams inside the dark cards, a method architecture diagram, and a Chart.js radar chart.

## Layout

Everything sits in a centred 860px column with left-aligned sections after the centred hero. Vertical rhythm is regular (72px section padding), and color bands, not rules, separate sections. The midnight pipeline band is the page's one dramatic shift.

## Agent Prompt Guide

Quick colors: base #f5f9fe, tint #eaf3fb, callout #e4f0fb, ink #0d1f33, slate #3a5570, cobalt #1a5fa8, hairline #d0e2f4, midnight #0a1a2e, card navy #0e2240, sky label #6ab0e8, signal blue #4a90e8.

1. "Build a centred hero in an 860px column on #f5f9fe, padding 72px 24px 56px: an uppercase 12px/500 tag (.12em, #1a5fa8, padding 4px 14px, 1px rgba(26,95,168,0.35) border, 2px radius), a 48px EB Garamond 400 title in #0d1f33 with one phrase italic #1a5fa8, 15.2px DM Sans authors separated by #d0e2f4 dots, 12.48px #3a5570 affiliations, then uppercase buttons (13.12px/500, padding 9px 20px, 3px radius): one #1a5fa8 filled, the others outlined 1px #d0e2f4."
2. "Make a ruled stat strip and abstract callout: strip with 1px #d0e2f4 top and bottom rules, items padding 20px 36px separated by 1px #d0e2f4 rules, EB Garamond 32px #1a5fa8 numbers and 11.52px uppercase .08em #3a5570 labels. Callout: #e4f0fb fill, 3px #1a5fa8 left bar, radius 0 4px 4px 0, padding 24px 28px, 14.88px/300 text."
3. "Create a dark pipeline section: full-bleed #0a1a2e, padding 72px 24px; label 11.52px uppercase #6ab0e8; Garamond 35.2px title in rgba(220,235,250,0.95) with an italic word; a 2-column grid with 1px gaps of #0e2240 cards (padding 32px 28px 0), each with a 36px circle numeral in a stage color (#4a90e8, #c9a800, #d94040, #2eaa60) at 18% fill and a small 2px-radius model chip."

## Similar Pages

- Fashion and virtual try-on project pages that pair a Garamond-style serif with a geometric sans.
- Single-column dataset pages that switch to one dark section for the data pipeline.

## Quick Start

```css
:root {
  --bg: #f5f9fe;
  --text: #0d1f33;
  --text-light: #3a5570;
  --accent: #1a5fa8;
  --accent-light: #e4f0fb;
  --teal: #1a7a8a;
  --gold: #2a6aaa;
  --border: #d0e2f4;
  --section-bg: #eaf3fb;
  --dark: #0a1a2e;
  --dark-card: #0e2240;
  --dark-label: #6ab0e8;
  --footer: #07111f;
  --serif: 'EB Garamond', Georgia, serif;
  --sans: 'DM Sans', system-ui, sans-serif;
  --max: 860px;
}
```

## Provenance

- **URL**: https://aimagelab.github.io/Dress-ED/
- **Paper**: Dress-ED: Instruction-Guided Editing for Virtual Try-On and Try-Off (arXiv 2603.22607), Davide Lobba, Fulvio Sanguigni, Bin Ren, Marcella Cornia, Rita Cucchiara, Nicu Sebe.
- **Venue**: ECCV 2026.
- **Selection reason**: the arXiv comment states acceptance at ECCV 2026 and links this project page.
- **Template credit**: none stated; a single hand-written HTML file with an inline stylesheet and Chart.js 4.4.1.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted probes of hero, stat strip, section bands, pipeline cards, edit-type cards and citation, the 1440×900 shot and a full-page capture, and the inline stylesheet and markup read directly, on 2026-10-28.
