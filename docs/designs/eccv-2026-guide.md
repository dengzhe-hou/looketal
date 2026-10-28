# GUIDE — Style Reference

> A tidy editorial page that lets one word wear a bag of macarons: five candy-colored serif capitals on warm paper, and everything else in calm ink with a blue-and-orange thread.

**Theme:** both

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, plus targeted probes of the hero, stepper, stat strip, cards, tables, tabs and BibTeX), the 1440×900 shot, and a full-page capture taken with the page's scroll-reveal forced visible, plus the page's own `static/css/style.css` and `index.html`. Sections fade up when scrolled into view (`.reveal`, 0.55s), so the 1440×900 shot shows the "GUIDE in one loop" section still faded, and the stepper card cycles through five panels, so a load-time capture shows the first panel (a task search bar) with much of the card empty. Some figures load lazily and appear blank in the full-page capture. A sun/moon toggle switches to a dark palette, listed separately.

## Overview

A long editorial page (9,538px) on warm paper #fbfaf7 with ink #1a1a1a. Headings are Fraunces (a soft serif at weight 500); body and UI are Inter; code is JetBrains Mono. The single flourish is the wordmark: the letters G, U, I, D, E each in their own color (rose #db6280, cobalt #4678d2, pistachio #50ba96, lavender #9b73c3, gold #dcb428), repeated in the 88px hero mark, the nav logo, the footer and the bold initials of the acronym expansion. Everything else follows a strict meaning code: blue #1f77b4 for Planning, orange #d67d24 for Grounding and green #2ca02c for gains. A 56×3px half-blue, half-orange "channel rule" sits above every section label. Sections alternate paper and a slightly darker band #f4f2ec at 96px padding and are built from white cards with 14–20px radii, hairline #e7e4de borders and barely-there shadows: a five-step interactive stepper with colored step chips, a four-column stat strip with Fraunces numbers, two-column problem rows with colored left bars, a method figure and three numbered step cards, Planning and Grounding channel cards with 4px top borders, results tables with a 2px ink header rule and green deltas, a Fraunces italic callout with a blue-to-orange left bar, underline tabs, resource cards and a white BibTeX block.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): paper #fbfaf7 / #faf9f5 / #fcfaf7 / #fefdfa / #fafaf7 / #fbfaf8 / #fbfaf6 together 93.2%; light gray #e4e2e0 6.8% (text, hairlines and the faded loop section blended). The wordmark colors cover too little area to form clusters.

Anatomy in DOM order (desktop 1440px, centred, `.wrap` max 1080px with 24px padding → x 204–1236):

1. **Sticky nav** (`nav.nav`, 0–62px): `color-mix(in srgb, #fbfaf7 78%, transparent)` with `backdrop-filter: saturate(160%) blur(11px)`, 1px #e7e4de bottom border. Logo "GUIDE" in Fraunces 21.12px/600 with per-letter colors at x=204; links right (Abstract, Method, Results, Qualitative, Resources, BibTeX) Inter 14.4px/500 #3d3d3d, padding 8px 11px, 8px radius, 4px gaps, hover #f4f2ec fill; a 32px GitHub icon button and a 34px sun toggle (1px #e7e4de, 8px radius). The active link gets a 2px blue-to-orange underline.
2. **Hero** (`header.hero`, 62–707): padding-top clamp(3rem, 7vw, 5rem) → 80px, no bottom padding; behind it a 460px wash `radial-gradient(40% 60% at 20% 0%, rgba(219,98,128,.10), transparent 70%), radial-gradient(40% 60% at 80% 0%, rgba(155,115,195,.10), transparent 70%), radial-gradient(50% 70% at 50% 0%, rgba(80,186,150,.08), transparent 70%)`.
3. **Venue pill** (`.venue-pill`, y=144, 115×27): Inter 13px/600 uppercase, letter-spacing 0.12em, #3d3d3d on #ffffff, 1px #e7e4de border, padding 6px 13px, 999px radius. Gap 22px + 4px.
4. **Hero mark** (`h1.hero-mark`, y=197, 84px box): Fraunces clamp(3rem, 9vw, 5.5rem) → 88px, line-height 0.95; letters weight 600 in #db6280, #4678d2, #50ba96, #9b73c3, #dcb428. Gap 10px.
5. **Acronym line** (`p.hero-expand`, y=291): Inter 25.6px/500 #3d3d3d, letter-spacing -0.01em; the initials G, U, I, D, E bold 700 in their wordmark colors. Gap 22px.
6. **Full title** (`p.hero-title-full`, y=345, three lines): Fraunces 21.12px/400, line-height 1.3, #1a1a1a, max 30ch (410px). Gap 26px.
7. **Authors** (`p.authors`, y=453): 16.96px, line-height 1.9, names #3d3d3d with #6b6b6b superscripts (✉ marks corresponding authors). Gap 6px.
8. **Affiliations** (`p.affil`, y=492, two lines): 15px/1.7 #6b6b6b; then "✉ Corresponding authors" 13px #6b6b6b (y=549). Gap 26px.
9. **Buttons** (`.btn-row`, y=596, 39px tall, 10px gaps): Inter 15.2px/600 pills, padding 10px 18px, 1px #1a1a1a border, 999px radius, 17px icons left; "Paper" filled #1a1a1a with #fbfaf7 text; "arXiv", "Code", "🤗 Dataset", "BibTeX" white with ink text. Gap 8px + 22px.
10. **TL;DR line** (`p.tldr-line`, y=657): 15px #3d3d3d, max 620px; the numbers "+4.47 to +7.48 pp" bold #1a1a1a. Hero ends at y=707.
11. **Loop band** (`section.loop.band`, from y=707): #f4f2ec, padding 16px 0 96px; channel rule at y=723, eyebrow "SEE IT WORK" at y=742, "GUIDE in one loop" heading at y=769.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #fbfaf7 | --paper | body, nav base, primary button text |
| Surface | #ffffff | --surface | cards, stepper stage, venue pill, outline buttons, tables, BibTeX |
| Band | #f4f2ec | --surface-2 | alternate sections, best table rows, inline code, copy button, nav hover |
| Ink | #1a1a1a | --ink | headings, full title, primary button fill and button borders, table header rule |
| Ink Soft | #3d3d3d | --ink-soft | body paragraphs, nav links, acronym line, authors, venue pill text |
| Muted | #6b6b6b | --muted | eyebrows, affiliations, section subtitles, captions, stat labels, inactive tabs |
| Hairline | #e7e4de | --hairline | nav border, card and table borders, stat dividers, pills |
| Wordmark G | #db6280 | --guide-g | letter G; step 5 chip when active |
| Wordmark U | #4678d2 | --guide-u | letter U; step 3 chip when active |
| Wordmark I | #50ba96 | --guide-i | letter I |
| Wordmark D | #9b73c3 | --guide-d | letter D |
| Wordmark E | #dcb428 | --guide-e | letter E |
| Planning Blue | #1f77b4 | --plan | links, Planning text, channel rule left half, Planning card top border, step 4 chip, active Planning tab |
| Planning Wash | #ebf3fa | --plan-bg | Planning chips and knowledge cards; border #c7ddf0 |
| Grounding Orange | #d67d24 | --ground | Grounding text, channel rule right half, Grounding card top border, active Grounding tab |
| Grounding Wash | #fdf3e7 | --ground-bg | Grounding chips and cards; border #f2d9b8 |
| Gain Green | #2ca02c | --stage-green | deltas, step 2 chip, success verdicts, check ticks |
| Fail Red | #c8322a | --fail-red | failure verdicts, the ▶ in the task search bar |
| Step Gray | #7c7c7c | (literal) | step 1 chip when active |
| Dark Paper | #16140f | --paper (dark) | page in dark theme |
| Dark Surface | #1e1b15 | --surface (dark) | cards in dark theme; band #242017 |
| Dark Ink | #f2efe8 | --ink (dark) | text in dark theme |
| Dark Channels | #5fa0de / #e59a4f | --plan / --ground (dark) | Planning and Grounding colors in dark theme |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display serif | 'Fraunces', Charter, Georgia, serif | Fraunces 400, 500, 600 | Fraunces |
| Sans | 'Inter', -apple-system, 'Segoe UI', system-ui, sans-serif | Inter 400, 500, 600, 700 | Inter |
| Mono | 'JetBrains Mono', 'SF Mono', ui-monospace, monospace | JetBrains Mono 400, 500 | JetBrains Mono |

| Role | Selector | Size / weight / line-height / tracking | Color |
|---|---|---|---|
| Hero mark | `.hero-mark` | clamp(3rem, 9vw, 5.5rem) → 88px / 600 letters / 0.95 / -0.01em | per-letter colors |
| Acronym line | `.hero-expand` | clamp(1.35rem, 2.6vw, 1.6rem) → 25.6px / 500 / -0.01em | #3d3d3d, initials 700 |
| Full title | `.hero-title-full` | clamp(1.05rem, 2.2vw, 1.32rem) → 21.12px / 400 / 1.3 | #1a1a1a |
| Section heading | `.section-head h2` | clamp(1.9rem, 4vw, 2.7rem) → 43.2px / 500 / 1.12 / -0.02em | #1a1a1a |
| Card heading | `.pstep h3`, `.res-card h3` | Fraunces 1.08rem = 17.28px / 1.15rem = 18.4px, 500 | #1a1a1a |
| Channel heading | `.channel h3` | Fraunces 1.45rem = 23.2px / 500 | #1f77b4 or #d67d24 |
| Eyebrow | `.eyebrow` | Inter 13px / 600 / 1 / uppercase / 0.14em | #6b6b6b |
| Body | `body` | 1.0625rem = 17px / 400 / 1.65 | #1a1a1a; paragraphs #3d3d3d |
| Small | `--fs-small` | 15px | #6b6b6b or #3d3d3d |
| Button | `.btn` | Inter 15.2px / 600 | #fbfaf7 or #1a1a1a |
| Step chip | `.dot` | Inter 13.76px / 600 | #6b6b6b; white when active |
| Stat number | `.stat .num` | Fraunces clamp(1.9rem, 4.5vw, 2.9rem) → 46.4px / 500 / 1, tabular | #1a1a1a |
| Table head | `.results thead th` | Inter 13.76px / 600 | #1a1a1a |
| Table cell | `.results tbody td` | 15px tabular | #3d3d3d; agent 600 #1a1a1a; type 12.9px #6b6b6b |
| Callout | `.callout` | Fraunces 19.2px italic / 1.5 | #1a1a1a |
| Code chip | `.chip` | JetBrains Mono 12.48px / 500 | #1f77b4 or #d67d24 |
| BibTeX | `pre.bibtex` | JetBrains Mono 13.76px / 1.7 | #3d3d3d, keys #1f77b4 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow / effect |
|---|---|---|---|
| Buttons, venue pill, step chips, RAG pills | 999px | 1px #1a1a1a (buttons) or #e7e4de | button hover translateY(-2px) and inverted colors |
| Stepper stage, channel cards, figure frames | 20px | 1px #e7e4de (channel cards 4px colored top) | stage `0 2px 8px rgba(26,26,26,.05), 0 1px 2px rgba(26,26,26,.04)`; figure `0 8px 28px rgba(26,26,26,.07)` |
| Pipeline steps, table cards, resource cards, problem rows, BibTeX, details | 14px | 1px #e7e4de (problem rows 4px colored left) | `0 1px 2px rgba(26,26,26,.04)` |
| Nav links, toggles, code chips, copy button | 8px | toggles 1px #e7e4de; chips 1px #c7ddf0 / #f2d9b8 | none |
| Channel rule | 2px, 56×3px | none | `linear-gradient(90deg, #1f77b4 0 50%, #d67d24 50% 100%)` |
| Callout | 0 | 3px left, `border-image: linear-gradient(#1f77b4, #d67d24) 1` | white fill |
| Pipeline number | 50%, 30px | 1.5px #1a1a1a | none |
| Lightbox image | 14px | none | `0 20px 60px rgba(0,0,0,.6)` on rgba(22,20,15,.86) |

## Layout Metrics

- **Container**: `.wrap { max-width: 1080px; margin: 0 auto; padding: 0 24px }` → content x 204–1236 (1032px); `.prose` 720px; stepper 940px; BibTeX 820px; callout 760px.
- **Hero**: padding-top 80px, no bottom padding; vertical chain 27 (pill) + 26 + 84 (mark) + 10 + 32 + 22 + 82 (title) + 26 + 33 (authors) + 6 + 53 + 4 + 21 + 26 + 39 (buttons) + 30 + 50 (TL;DR) = 591px from y=144 to y=707 (the 22px pill margin plus the mark's 4px top margin make the 26px gap).
- **Sections**: padding clamp(3.5rem, 8vw, 6rem) → 96px top and bottom; the loop band 16px top; the stat strip 0 top, 96px bottom. Section head margin-bottom 2.6rem (41.6px); subtitle max 640px, 11.2px below the heading; channel rule 16px above the eyebrow, eyebrow 14px above the heading.
- **Stepper**: chips rail with 8px gaps, 22px above a 940×360 white stage (20px radius).
- **Stat strip**: 4 equal columns over 1032px, padding 14px 18px, 1px #e7e4de left dividers.
- **Grids**: problem section two columns, gap 44px; pipeline 1fr auto 1fr auto 1fr with arrows; channels 2 columns, gap 22px; resource cards 3 columns, gap 18px; tab panel 1.2fr / 1fr, gap 28px, max 920px.
- **Tables**: in a white 14px card; th padding 13px 15px with a 2px #1a1a1a bottom rule; td padding 12px 15px with 1px #e7e4de rules; best rows #f4f2ec.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| base (1440) | 24px inside 1080px | 17px | hero mark 88px, h2 43.2px | 4 stats, 3 resource cards, 2 channel cards |
| ≤1200px | 24px | 17px | h2 43.2px until 1080, then 4vw | section padding 8vw (e.g. 86px at 1080) down to a 56px floor at 700px |
| ≤978px | 24px | 17px | hero mark 9vw, e.g. 69px at 768 | none |
| ≤880px | 24px | 17px | mark 79.2px, h2 35.2px | two-col, pipeline, channels, tab panels and resource cards become 1 column; pipeline arrows rotate 90° |
| ≤768px | 24px | 17px | mark 69.1px, h2 30.7px | nav links collapse into a burger menu; stats 2×2; knowledge and act cards 1 column |
| ≤420px | 24px | 17px | mark 48px (3rem floor, reached at 533px) | stats 1 column |

## Components

- **Macaron wordmark** (`.guide-mark`): Fraunces 600, letter-spacing -0.01em; each letter a `span` in #db6280, #4678d2, #50ba96, #9b73c3, #dcb428. Use it only on the literal letters G-U-I-D-E.
- **Channel rule + eyebrow**: 56×3px bar, 2px radius, half #1f77b4 and half #d67d24, 16px above a 13px/600 uppercase 0.14em #6b6b6b eyebrow; centred in section heads, left-aligned in two-column sections.
- **Pill button** (`.btn`): padding 10px 18px, 1px #1a1a1a, 999px radius, Inter 15.2px/600, 17px icon left with 8px gap; outline is white with ink text and inverts on hover (ink fill, paper text, lift 2px); primary is ink with paper text and turns transparent on hover.
- **Step chip** (`.dot`): padding 7px 15px, 999px radius, 1px #e7e4de, white, Inter 13.76px/600 #6b6b6b with a dimmed "01" number; active chips fill with the step color (#7c7c7c, #2ca02c, #4678d2, #1f77b4, #db6280) and white text.
- **Stepper stage** (`.loop-stage`): white, 1px #e7e4de, 20px radius, small shadow, min-height 360px; panels fade and rise 8px over 0.45s. The first panel is a pill search bar (padding 16px 20px, 1px #e7e4de, 999px radius) with a red ▶ and a typing caret.
- **Stat column** (`.stat`): centred, padding 14px 18px, Fraunces 46.4px/500 number (units at 0.5em in #6b6b6b), 15px #6b6b6b label 10px below; columns split by 1px #e7e4de.
- **Problem row** (`.bias-row`): white, 1px #e7e4de with a 4px left bar in #1f77b4 or #d67d24, 14px radius, padding 16px, a 150px screenshot left; 10.88px/700 uppercase tag in the channel color.
- **Pipeline step** (`.pstep`): white 14px card, padding 22px 20px, a 30px circle number with a 1.5px ink border, Fraunces title, 15px text and a dashed-top mono footnote (12.48px #6b6b6b); JetBrains Mono chips `{video_planning}` (#1f77b4 on #ebf3fa, 1px #c7ddf0) and `{video_grounding}` (#d67d24 on #fdf3e7, 1px #f2d9b8), 8px radius.
- **Channel card** (`.channel`): white, 1px #e7e4de with a 4px top border in the channel color, 20px radius, padding 26px; Fraunces 23.2px heading in the channel color with a 13px dot; list rows with 1px #e7e4de top rules and 7px colored bullets.
- **Results table** (`.tbl-card table.results`): caption 15px #6b6b6b; head 13.76px/600 ink with a 2px #1a1a1a rule; cells right-aligned tabular; best value 700 #1a1a1a; best row #f4f2ec; gains in 700 #2ca02c ("+7.48").
- **Callout** (`.callout`): max 760px, padding 18px 26px, white, 3px left bar from `linear-gradient(#1f77b4, #d67d24)`, Fraunces 19.2px italic.
- **Underline tabs** (`.tab`): Inter 15.2px/600 #6b6b6b, padding 10px 18px, 2px bottom border; active Planning #1f77b4, active Grounding #d67d24.
- **BibTeX** (`pre.bibtex`): white, 1px #e7e4de, 14px radius, padding 22px, JetBrains Mono 13.76px; copy button top-right (#f4f2ec, 1px #e7e4de, 8px radius, padding 7px 13px, 13.12px/600; turns green when copied).

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky nav with theme toggle | yes | translucent paper bar, wordmark logo, pill-hover links, GitHub and sun icons |
| Venue badge | yes | white outlined uppercase pill |
| Title / authors / affiliations | yes | macaron mark, acronym line, Fraunces full title, centred authors |
| Link buttons | yes | ink-outlined pills, one filled |
| TL;DR | yes | one 15px line with bold numbers |
| Interactive demo | yes | five-step stepper with colored chips over a white stage |
| Stat strip | yes | four Fraunces numbers with hairline dividers |
| Abstract | yes | prose in a band section |
| Method figure and steps | yes | shadowed figure frame, three numbered cards, RAG stage pills |
| Knowledge channels | yes | blue and orange top-bordered cards |
| Results tables | yes | white table cards with green deltas and a pull-quote callout |
| Qualitative | yes | figure plus underline tabs switching Planning/Grounding panels |
| Resources | yes | three white cards with emoji icons and pill buttons |
| BibTeX | yes | white mono block with copy button |
| Footer | yes | centred wordmark, links and fine print |

## Adapting to Other Content

- **More authors**: keep the centred 16.96px line at line-height 1.9 with #6b6b6b superscripts; it wraps within 760px, so a second line adds about 32px.
- **A results table**: use the table card recipe at full 1032px width: 2px #1a1a1a header rule, 1px #e7e4de row rules, best row #f4f2ec, best value 700 #1a1a1a, gains in 700 #2ca02c and losses in #c8322a.
- **Long publication or news lists**: use channel-list rows (padding 8px 0 8px 26px, 1px #e7e4de top rules, 7px dot bullets) inside a white 20px-radius card; put dates in JetBrains Mono 12.48px #6b6b6b.
- **A project with no two-channel story**: keep the channel rule as a single #1f77b4 bar and drop orange, but keep the macaron colors confined to the wordmark.
- **More stats**: keep four per row; a fifth starts a new row (the grid is fixed at 4 columns above 768px).

## Do's and Don'ts

- Do use the five macaron colors only on the letters of the wordmark and its acronym initials.
- Do encode meaning with color: blue for planning, orange for grounding, green for gains, red for failures.
- Do put the 56×3px blue-orange channel rule above every section eyebrow.
- Do keep cards white on paper with #e7e4de hairlines and very light shadows.
- Don't use bold Fraunces; headings are weight 500, the wordmark letters 600.
- Don't add new accent colors for decoration; neutral ink and grays carry the layout.
- Don't square the corners: pills are 999px, cards 14px, large frames 20px.

## Surfaces

Warm paper #fbfaf7 alternating with #f4f2ec bands; white #ffffff cards, stage, tables and code; tinted washes only inside Planning (#ebf3fa) and Grounding (#fdf3e7) elements; a soft three-color radial wash behind the hero. Dark theme: #16140f page, #1e1b15 cards, #242017 bands, #f2efe8 text, lighter blue #5fa0de and orange #e59a4f.

## Imagery

Software screenshots (GIMP, LibreOffice, VLC) with annotated menus and sliders, YouTube tutorial keyframes, a wide method overview figure in a shadowed frame, a before/after action comparison with red and green verdict tags, and emoji used as small icons on resource cards.

## Layout

Centred hero and section heads in a 1032px column; content alternates between full-width cards, two-column comparisons and three-column card rows. Bands alternate every section with 96px padding; every module sits on white cards rather than directly on the paper.

## Agent Prompt Guide

Quick colors: paper #fbfaf7, band #f4f2ec, surface #ffffff, ink #1a1a1a, ink soft #3d3d3d, muted #6b6b6b, hairline #e7e4de, plan #1f77b4, ground #d67d24, gain #2ca02c, wordmark #db6280 #4678d2 #50ba96 #9b73c3 #dcb428.

1. "Build a centred hero on #fbfaf7 with padding-top 80px: a white uppercase pill (Inter 13px/600, 0.12em, #3d3d3d, 1px #e7e4de, padding 6px 13px), an 88px Fraunces wordmark whose letters are #db6280, #4678d2, #50ba96, #9b73c3 and #dcb428 at weight 600, a 25.6px/500 Inter acronym line in #3d3d3d with colored bold initials, a 21.12px Fraunces full title (max 30ch), and pill buttons (padding 10px 18px, 1px #1a1a1a, radius 999px, 15.2px/600): one #1a1a1a with #fbfaf7 text, the rest white."
2. "Make a section head: a 56×3px bar with background linear-gradient(90deg, #1f77b4 0 50%, #d67d24 50% 100%) and 2px radius, 16px above a 13px/600 uppercase 0.14em #6b6b6b eyebrow, 14px above a 43.2px/500 Fraunces heading; subtitle 17px #6b6b6b, max 640px. Sections alternate #fbfaf7 and #f4f2ec with 96px padding."
3. "Create a results table card: white, 1px #e7e4de, 14px radius, box-shadow 0 1px 2px rgba(26,26,26,.04); header cells Inter 13.76px/600 #1a1a1a, padding 13px 15px, 2px #1a1a1a bottom rule; body cells 15px tabular #3d3d3d, padding 12px 15px, 1px #e7e4de rules; best value 700 #1a1a1a; gains as 700 #2ca02c."

## Similar Pages

- Editorial academic pages pairing Fraunces headings with Inter body text on warm paper.
- Agent and RAG papers that explain a pipeline with an interactive multi-step demo.

## Quick Start

```css
:root {
  --guide-g: #db6280;
  --guide-u: #4678d2;
  --guide-i: #50ba96;
  --guide-d: #9b73c3;
  --guide-e: #dcb428;
  --plan: #1f77b4;
  --plan-bg: #ebf3fa;
  --ground: #d67d24;
  --ground-bg: #fdf3e7;
  --stage-green: #2ca02c;
  --fail-red: #c8322a;
  --ink: #1a1a1a;
  --ink-soft: #3d3d3d;
  --muted: #6b6b6b;
  --hairline: #e7e4de;
  --paper: #fbfaf7;
  --surface: #ffffff;
  --surface-2: #f4f2ec;
  --r-sm: 8px;
  --r-md: 14px;
  --r-lg: 20px;
  --r-pill: 999px;
  --maxw: 1080px;
}
[data-theme="dark"] {
  --ink: #f2efe8;
  --paper: #16140f;
  --surface: #1e1b15;
}
```

## Provenance

- **URL**: https://sharryxr.github.io/GUIDE/
- **Paper**: GUIDE: Resolving Domain Bias in GUI Agents through Real-Time Web Video Retrieval and Plug-and-Play Annotation (arXiv 2603.26266), Rui Xie, Zhi Gao, Chenrui Shi, Zirui Shang, Lu Chen, Qing Li.
- **Venue**: ECCV 2026.
- **Selection reason**: the arXiv comment states acceptance at ECCV 2026 and links this project page.
- **Template credit**: none stated; a custom page whose stylesheet header describes a "Clean Editorial / Top-tier Academic" direction.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted probes of hero, stepper, stats, cards, tables, tabs and BibTeX, the 1440×900 shot and a full-page capture with scroll-reveal forced visible, and the page's `style.css` and `index.html` read directly, on 2026-10-28.
