# SSI-Bench — Style Reference

> Lavender morning light on frosted glass: a wireframe cube floats over a university-purple title and a leaderboard that blushes by model family.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's own `assets/styles.css` and `index.html`. Text colors are declared as translucent near-black and purple over a lavender ground; hex values with an alpha note are given as declared, and the rendered tones are described where they differ.

## Overview

A custom benchmark page in "Tsinghua purple" (#82318e, with a deeper #660874 for hero text) over a soft lavender ground (#f7f6fb) washed by three large radial glows of purple and lilac. A frosted sticky nav carries a small cube mark and "SSI-Bench" in a purple-to-lilac gradient, with three links separated by thin vertical rules. The centred hero stacks a 104px wireframe-cube logo, a 42px Inter title at weight 780, two lines of purple author names, a bold purple "Tsinghua University", the venue line with a faint underline, and four white pill links with purple text and icons. A 980px teaser figure with a 16px radius and long soft shadow closes the hero. Below, sections are frosted white panels (16px radius, purple radial tint, and a 3px purple gradient top edge on the viewer and analysis panels only) holding the overview table and pie chart, an interactive dataset viewer with dropdowns and a prompt box, the construction pipeline figure, a sortable leaderboard with family-tinted rows (pink proprietary, blue open, cream baseline) and purple best cells, and analysis cards.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): lavender whites #f8f7fb 20.3%, #f4f2f8 18.8%, #eae5ef 15.5%, #efeaf5 14.7%, #f5f4fa 10.2%; muted mauve #7f5c61 9.7% (teaser figure content and dark text); #d0ced7 8.5% (figure lines, borders, light text); #f2f2f2 2.3%.

Anatomy in DOM order (desktop 1440px, everything centred):

1. **Sticky nav** (0–51px): background rgba(244,245,247,.74) with 12px blur, 1px rgba(45,21,56,.08) bottom rule and a white inset highlight; inner container 1056px (x=192), padding 12px 0. Left: cube icon at 1.7em and "SSI-Bench" 15px/750 in linear-gradient(135deg, #82318e, #a889d6). Right: Dataset, Leaderboard, Analysis 15px/600 at 62% ink, 24px apart, divided by 1px×16px rules.
2. **Hero** (`section.hero`, 51–1035px): padding 64px 0 44px.
3. **Logo** (y=115, 104px): wireframe cube SVG, clamp(74px, 7.6vw, 104px), `filter: drop-shadow(0 12px 28px rgba(25, 18, 36, 0.12))`. Gap 18px.
4. **Title** (y=237, two lines, 92px): Inter 42px/780, line-height 1.1, letter-spacing -0.02em, max 35ch, rgba(17,14,26,.92). Gap 14px.
5. **Authors** (y=343, two balanced lines): Inter 14px/520, line-height 1.9, rgba(102,8,116,.78); corresponding authors carry a small envelope icon. Gap 18px.
6. **Affiliation** (y=415): "Tsinghua University", 17px/700, letter-spacing -0.01em, #660874. Gap 12px.
7. **Venue line** (y=456): "International Conference on Machine Learning (ICML), 2026", 14px/700, letter-spacing 0.04em, #660874, with a 1px rgba(130,49,142,.1) underline 6px below. Gap 28px.
8. **Resource pills** (y=515, 37px tall): Paper, Dataset, GitHub, arXiv; gap 10px. Gap 38px.
9. **Teaser** (y=590, 980×401px): three-panel figure (previous spatial reasoning vs structure-centric reasoning vs VLM performance) with 16px radius, 1px rgba(45,21,56,.12) border, 0 18px 50px shadow; it runs below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Lavender Ground | #f7f6fb | --bg | page background (hero band) |
| Viewer Ground | #f3f0fa | --bgViewer | page background behind the dataset viewer band |
| Leaderboard Ground | #f6f5fb | --bgLeaderboard | page background from the leaderboard down |
| Tsinghua Purple | #82318e | --brand | gradient start for brand text and panel top edges, best-cell tint, prompt emphasis, active sort |
| Lilac | #a889d6 | --brand2 | gradient end, top-right background glow |
| Deep Purple | #660874 | (literal) | affiliation, venue line, resource pill text; authors at 78% |
| Ink | rgba(17,14,26,.92) | --text | title, headings, body text (renders about #1e1b26 on lavender) |
| Muted Ink | rgba(17,14,26,.62) | --muted | nav links, section leads, card titles, captions |
| Table Header Ink | rgba(23,18,29,.82) / rgba(23,18,29,.86) | (literal) | leaderboard column headers and sort buttons (.82); Geometric/Topological group headers and inactive leaderboard tabs (.86) |
| Hairline | rgba(45,21,56,.14) | --border | panel and button borders, table separators |
| Shadow Plum | rgba(25,18,36,.12) | --shadow | panel, teaser and pill shadows (8–16% alpha) |
| Frost | rgba(255,255,255,.78) | --surface | panels, resource pills (72%), cards |
| Header Gray | rgba(244,245,247,.72) | (literal) | nav background (74%), leaderboard model header |
| Proprietary Row | rgba(255,233,238,.9) | (literal) | leaderboard rows for proprietary models |
| Open Row | rgba(233,242,255,.95) | (literal) | leaderboard rows for open models |
| Baseline Row | rgba(255,248,224,.95) | (literal) | leaderboard baseline rows |
| Geometric Header | rgba(80,120,190,.12) | (literal) | "Geometric" column group header |
| Topological Header | rgba(70,160,120,.12) | (literal) | "Topological" column group header |

Declared but not visible in the static render: --danger #e34a6f and --ok #1aa37a (used only for answer feedback in the viewer).

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (--sans) | "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI Variable Text", "Segoe UI", Roboto, Helvetica, Arial, … | Inter 400/600/700/800 (780 and 520 interpolate on the variable face) | Manrope |
| Display (--display) | "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI Variable Display", "Segoe UI", Roboto, Helvetica, Arial; used by `.hero__title`, `.section__header h2`, `.subsection__header h3` | Inter (same face as the sans stack) | Manrope |
| Mono | ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, … | Consolas on Windows | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.hero__title` | clamp(28px, 3vw, 42px) → 42px / 780 / 1.1, letter-spacing -0.02em | --text |
| Section heading | `.section__header h2` | clamp(24px, 2.4vw, 32px) → 32px / 800 / 1.15, -0.02em, centred | --text |
| Subsection heading | `.subsection__header h3` | clamp(18px, 2vw, 24px) → 24px / 800 / 1.15, centred | --text |
| Body | `body` | 15px / 400 / 1.65, letter-spacing 0.1px | --text |
| Section lead | `.section__header p` | 14px / 1.75, max 76ch | --muted |
| Authors | `.hero__subtitle--author` | 14px / 520 / 1.9, balanced | #660874 at 78% |
| Affiliation | `.hero__subtitle--affil` | 17px / 700, -0.01em | #660874 |
| Venue line | `.hero__venue` | 14px / 700, letter-spacing 0.04em | #660874 |
| Resource pill | `.heroResource` | 13px / 650 / 1 | #660874 |
| Nav brand / links | `.nav__brand`, `.nav__links` | 15px / 750; 15px / 600 | gradient; --muted |
| Table | `.leaderboardTable` | 13px; headers 650; best 800; second 750; Avg column 750 | cells --text; headers rgba(23,18,29,.82), group headers rgba(23,18,29,.86) |
| Prompt body | `.promptBox__body` | 14px / 1.55, pre-wrap; strong 750 purple | --text |
| Card text | `.analysisCard__body`, `figcaption` | 13px / 1.7 | --text / --muted |
| Viewer button | `.button` | 13.3px / 600 | --text |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Panels | 16px | 1px rgba(45,21,56,.14); 3px brand-gradient top edge on viewer and analysis panels only | 0 18px 70px rgba(25,18,36,.12); hover lift 6px, 0 26px 90px at 16% |
| Teaser and pipeline figures | 16px | 1px rgba(45,21,56,.12) | 0 18px 50px rgba(25,18,36,.12); teaser lifts 6px on hover |
| Analysis cards, viewer cards | 14px | 1px rgba(45,21,56,.12) | hover 0 18px 52px at 14% |
| Prompt box, buttons | 12px | 1px rgba(45,21,56,.12–.14) | button hover 0 10px 32px at 10% |
| Resource pills | 999px | 1px rgba(130,49,142,.22) | 0 10px 26px rgba(25,18,36,.08) |
| Inline code | 8px | 1px rgba(45,21,56,.08) | none |
| Overview table image | 0 | 1px rgba(45,21,56,.12) | 0 16px 44px at 10% |

Background (body, literal): `radial-gradient(1100px 700px at 14% 8%, rgba(130, 49, 142, 0.14), transparent 62%), radial-gradient(1000px 650px at 86% 0%, rgba(168, 137, 214, 0.16), transparent 55%), radial-gradient(900px 600px at 65% 82%, rgba(130, 49, 142, 0.07), transparent 62%)` over a banded linear gradient whose split points JavaScript aligns with the viewer and leaderboard sections.

## Layout Metrics

- **Containers**: `.container { width: min(1056px, calc(100% - 40px)); margin: 0 auto }` (x=192 at 1440); the hero container widens to min(1380px, calc(100% - 40px)).
- **Hero**: padding 64px 0 44px; title text max 35ch; authors max 72ch; teaser `width: min(980px, 100%)`, margin-top 38px.
- **Sections**: padding 52px 0 64px; section header max 80ch, margin-bottom 18px; subsections 26px apart.
- **Panels**: padding 18px; overview grid 1.25fr / 0.75fr with 16px gap (table image left, 340px pie right); viewer image grid 2 × 1fr with 14px gap; analysis cards 3 columns with 12px gap.
- **Leaderboard**: fixed table layout, model column 220px, metric columns 66px, cells padding 10px.
- **Footer**: padding 22px 0, 1px top rule, brand left and "Back to top" right.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1400px | (100% − 1056px)/2 | 15px | 42px | full layout |
| 934–1399px | 20px minimum | 15px | 3vw (28–42px) | — |
| ≤900px | 20px | 15px | 28px floor below 934px | overview, analysis cards and analysis grid → 1 column; viewer image grid → 1 column; controls min-width 160px |

## Components

- **Resource pill** (`.heroResource`): inline-flex, gap 8px, padding 8px 12px, radius 999px, 1px rgba(130,49,142,.22) border, background rgba(255,255,255,.72), shadow 0 10px 26px rgba(25,18,36,.08), 16px icon left (document, database, GitHub mark, X-style arXiv glyph), text 13px/650 #660874. Hover: translateY(-1px), white at 86%, border at 30%.
- **Frosted panel** (`.panel`): padding 18px, radius 16px, 1px --border, background `radial-gradient(800px 520px at 18% 0%, rgba(130, 49, 142, 0.1), transparent 58%), linear-gradient(180deg, var(--surfaceStrong), var(--surface))` (rgba(255,255,255,.92) → rgba(255,255,255,.78)), shadow 0 18px 70px at 12%, a 3px `::before` bar in --brandGrad at opacity 0.9 along the top, shown only on the viewer and analysis panels (`#overview`, `#pipeline` and `#leaderboard .panel::before { display: none }`). Hover lifts 6px. The leaderboard panel is unstyled: border 0, background transparent, no shadow, padding 0.
- **Viewer controls**: labelled native selects (Category, Task) and ghost buttons Prev / Next / Random (`.button--ghost`: white at 60%, 1px hairline, 12px radius, padding 10px 12px, 600 weight; hover white at 90% and lift 1px).
- **Prompt box** (`.promptBox`): 12px radius, 1px hairline, white 78% → 66% gradient, padding 12px; title 650; body 14px Inter with purple 750 emphasis; Copy button top-right; scrolls after 360px.
- **Leaderboard table**: header group cells tinted blue (Geometric) and green (Topological); sortable headers become purple when active and lift on hover; rows tinted pink, blue or cream by model family; best value cells purple at 28% with weight 800, second-best at 16% with 750; the top model in each group gets a 4px purple inset bar on its name cell.
- **Analysis card** (`.analysisCard`): radius 14px, 1px hairline, white 78% → 60% gradient, padding 12px; title 800, body 13px/1.7; hover lifts 6px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky nav | yes | frosted gray bar with gradient brand and ruled links |
| Logo mark | yes | 104px wireframe-cube SVG above the title |
| Title / authors / affiliation | yes | centred; authors and affiliation in deep purple |
| Venue | yes | full conference name as a bold purple line with faint underline |
| Link buttons | yes | four white pill links with purple icons |
| Teaser | yes | 980px figure with 16px radius and soft shadow |
| Abstract | absent from the source | sections open with one-line leads instead |
| Dataset overview | yes | table image and pie chart in a panel |
| Interactive dataset viewer | yes | dropdowns, ghost buttons, prompt box, image cards |
| Construction pipeline | yes | full-width figure in a panel |
| Leaderboard | yes | sortable family-tinted table with purple best cells |
| Analysis | yes | key-result cards and figures on a purple-tinted band |
| BibTeX | absent from the source | — |
| Footer | yes | thin rule, brand and "Back to top" |

## Adapting to Other Content

- **Fewer authors with affiliations**: keep the purple 14px author line and add numbered affiliations in the 17px/700 #660874 style, one line per institution.
- **A results table that is not a leaderboard**: reuse the leaderboard cell styles without family tints (rows white at 84%); keep purple 28% / 16% for best and second best.
- **Long publication or news lists**: use analysis cards (14px radius, hairline, white gradient) in one column with the date in --muted 13px.
- **A video**: place it inside a frosted panel with the 3px gradient top edge; give the video itself a 12px radius.
- **A BibTeX block**: use the prompt-box style (12px radius, white gradient, Copy button) with the mono stack at 13px.

## Do's and Don'ts

- Do keep text near-black and translucent (92% / 62%) on the lavender ground; use #660874 only for hero metadata and links.
- Do put content in frosted panels with long soft shadows; give the 3px purple gradient top edge only to interactive viewer and analysis panels.
- Do tint leaderboard rows by model family and reserve purple fills for best and second-best values.
- Don't use solid purple buttons in the hero; resource links are white pills with purple text.
- Don't drop the radial glows; the flat #f7f6fb alone loses the look.
- Don't use pure white page sections; even white surfaces are 60–92% translucent.

## Surfaces

Lavender page with radial purple and lilac glows; frosted white panels (78–92%) with blur-free translucency; the analysis section sits on its own band with a top hairline and a centred purple radial; the nav is translucent gray with backdrop blur.

## Imagery

Paper figures throughout: a three-panel teaser mixing photos of red steel structures, question/answer callouts and a bar chart; a taxonomy table image and a two-tone pie chart (blue Geometric, green Topological); dataset photos of real structures with highlighted members; a pipeline diagram; analysis plots. All images get 16px radii (except the table image), 1px borders and soft shadows.

## Layout

Centred hero with teaser, then three main sections (Dataset with Overview, Dataset Viewer and Construction Pipeline subsections; Leaderboard; Analysis) inside a 1056px container, and a slim footer. Page height about 6,850px at 1440 wide.

## Agent Prompt Guide

Quick colors: ground #f7f6fb, viewer band #f3f0fa, brand #82318e → #a889d6, deep purple #660874, ink rgba(17,14,26,.92), muted rgba(17,14,26,.62), border rgba(45,21,56,.14), surface rgba(255,255,255,.78).

1. "Build a centred benchmark hero on #f7f6fb with radial glows (rgba(130,49,142,.14) at 14% 8%, rgba(168,137,214,.16) at 86% 0%): a 104px line-art logo, an Inter 42px/780 title (line-height 1.1, letter-spacing -0.02em, max 35ch), authors 14px/520 in rgba(102,8,116,.78), affiliation 17px/700 #660874, venue 14px/700 #660874 with letter-spacing 0.04em."
2. "Make resource pills: inline-flex, gap 8px, padding 8px 12px, radius 999px, 1px rgba(130,49,142,.22) border, background rgba(255,255,255,.72), shadow 0 10px 26px rgba(25,18,36,.08), 16px icon left, text 13px/650 #660874; hover translateY(-1px)."
3. "Create a frosted panel: padding 18px, radius 16px, 1px rgba(45,21,56,.14) border, background radial-gradient(800px 520px at 18% 0%, rgba(130,49,142,0.10), transparent 58%), linear-gradient(180deg, rgba(255,255,255,.92), rgba(255,255,255,.78)), box-shadow 0 18px 70px rgba(25,18,36,.12), and (viewer and analysis panels only) a 3px top bar linear-gradient(135deg, rgba(130,49,142,0.98), rgba(168,137,214,0.88)) at opacity 0.9; hover translateY(-6px)."

## Similar Pages

- Benchmark pages with a hero logo mark, an interactive sample viewer and a sortable leaderboard (VLM and spatial-reasoning benchmarks).
- Glassmorphism-on-pastel research pages that tint the background with large radial glows.

## Quick Start

```css
:root {
  --bg: #f7f6fb;
  --bgViewer: #f3f0fa;
  --bgLeaderboard: #f6f5fb;
  --surface: rgba(255, 255, 255, 0.78);
  --border: rgba(45, 21, 56, 0.14);
  --text: rgba(17, 14, 26, 0.92);
  --muted: rgba(17, 14, 26, 0.62);
  --brand: #82318e;
  --brand2: #a889d6;
  --brand-deep: #660874;
  --brandGrad: linear-gradient(135deg, rgba(130, 49, 142, 0.98), rgba(168, 137, 214, 0.88));
  --shadow: 0 18px 70px rgba(25, 18, 36, 0.12);
  --radius: 16px;
  --sans: "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI Variable Text", "Segoe UI", Roboto, Helvetica, Arial;
  --display: "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI Variable Display", "Segoe UI", Roboto, Helvetica, Arial;
}
```

## Provenance

- **URL**: https://ssi-bench.github.io/
- **Paper**: Thinking in Structures: Evaluating Spatial Intelligence in Constraint-Governed Spaces (arXiv 2602.07864), Chen Yang et al., Tsinghua University.
- **Venue**: ICML 2026.
- **Selection reason**: existing verified entry kept in the pool; the arXiv comment states acceptance at ICML 2026 and links this project page.
- **Template credit**: none; a custom stylesheet whose header names its palette "Tsinghua purple + layered light grays".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, and the page's `styles.css` and `index.html` read directly, on 2026-10-28.
