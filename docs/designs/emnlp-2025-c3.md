# C3Benchmark — Style Reference

> A frosted-glass control panel tinted sky blue: a docked side rail, floating stat tiles and a leaderboard whose scores light up green, blue, orange and red.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and top-of-page tall screenshots, the single inline `<style>` block of `index.html` (about 630 lines, with several rules redeclared later in the cascade), inline `style` attributes on the section cards, and a browser probe at 1440px of the header, cards, tabs, category cards, example blocks and citation. Rajdhani is requested only in weights 500 and 700 (`fonts_loaded`: Rajdhani 500, 700), so text declared 400 renders with the 500 face and 600 to 900 render with the 700 face. Several values are overridden later in the stylesheet and differ from their first declaration: `.header-title` renders 35.2px / 900 (not 2rem / 700), `.card-title` 24.8px / 800 #2563eb (not 1.5rem / 700 black), and sort arrows #2563eb (not #60a5fa).

## Overview

A dashboard-like page on a pale 135deg gradient (#f8fafc → #e0e7ef). A fixed 210px side rail with the same blue-grey gradient and rounded right corners lists seven emoji-led links (Overview, Leaderboard, Categories, Examples, Responses, Submission, Citation) in bold blue, centred vertically. The main column starts 230px from the left. At the top a blue-grey gradient header card holds a small logo, "C³Benchmark" in heavy Rajdhani, an underlined-initials tagline "Challenges in Complex Conversations", a grey description, three white outlined link chips (Paper, Dataset, Code) on the right and a white announcement bar with a blue "Announcement" badge. Below sit four gradient stat cards (Models Evaluated, Languages, Categories, Best Overall), a tabbed leaderboard card (English / Chinese) with medal-gradient rank pills and colour-coded scores, a Categories card with white sub-cards, a blue-bordered scrollable Examples card with audio players and question/answer blocks, a Responses section, a submission card and a citation card. Every card lifts and scales slightly on hover.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): #f5f8fa 18.1% (page gradient, light end), #d9e3f1 16.7%, #c1d6f4 16.0%, #c6d9f4 12.4%, #d1dff2 12.3%, #ccdcf2 11.5% (all steps of the #e0e7ef → #b6d0f7 card and rail gradients), #e8edf2 7.0%, #a8b8d6 6.1% (shadows and antialiased text). Blue text and score colours are too small to form clusters.

Anatomy in DOM order (desktop 1440px):

1. **Side rail** (`nav.sidebar-nav`, fixed, x=0–210, full height): `linear-gradient(135deg, #e0e7ef 0%, #b6d0f7 100%)`, radius 0 12px 12px 0, shadow `0 4px 24px rgba(0,0,0,0.10), 0 1.5px 4px rgba(0,0,0,0.06)`. Links (`a.nav-link`) are 45px tall, padding 10px 24px, Rajdhani 17.28px / 600 #2563eb with a leading emoji, stacked every 69px from y=221 to y=635 (12px margins plus divider items). Hover: #2563eb fill, white text.
2. **Main column** (`.main-content`, margin-left 230px).
3. **Header card** (`.header#overview`, x=230 to the right edge, y=0–323): same gradient and shadow, radius 8px, padding 24px, margin-bottom 24px; inner `.container` padding 24px.
4. **Logo + title** (y=48): 40×40 logo image in a 48px box (16px right margin) at x=282; `h1.header-title` "C³Benchmark" at x=342, Rajdhani 35.2px / 900 (700 face), letter-spacing 1px, #000000, superscript 3 at 0.6em.
5. **Taglines** (y=101 and y=122): "Challenges in Complex Conversations" 17.28px #6b7280 with the three C's underlined (2px); "Spoken Dialogue Model Evaluation" 14.4px #6b7280.
6. **Link chips** (`.header-links a`, right side at y=76, 36px tall): Paper, Dataset, Code with small logo images, 15.2px #374151 on #f9fafb, 1px #d1d5db border, radius 6px, padding 6px 12px, 8px apart.
7. **Description** (y=156): 14.4px #6b7280, max 800px, two lines.
8. **Announcement bar** (`.announcement`, y=228, 46px tall): `linear-gradient(90deg, #f5f9ff 0%, #fbfdff 100%)`, 1px #bfdbfe border, radius 10px, padding 10px 12px, shadow `0 2px 8px rgba(37,99,235,0.08)`; badge "Announcement" 14.08px / 600 white on #3b82f6, radius 8px, padding 2px 8px; text 16.32px / 600 #1e3a8a.
9. **Stat cards** (`.overview-cards`, y=371, four 274×192 cards, gap 16px): title 24.8px / 800 #2563eb with 30px gap, value 16px #000000, label 15.2px #1e293b.
10. **Leaderboard card** (`.tabs`, from y=619): tab buttons at y=614–654 ("Results on English Subset" active with 2px #2563eb underline and blue bold text), table header at y=671, first rows visible to the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Page Light | #f8fafc | (body gradient start) | page background, top-left |
| Blue Grey | #e0e7ef | (gradient start, literal) | side rail, header, cards, tabs card start; model link button fill; answer block fill; example tab bar |
| Sky | #b6d0f7 | (gradient end) | side rail, header, stat cards, leaderboard card end |
| Main Blue | #2563eb | --main-blue | rail links, card titles, active tab, sort arrows, category sub-card titles, example headings, borders of the Examples card and question blocks, link button text |
| Deep Blue | #1d4ed8 | (literal) | category group titles, active sort column arrow, example tab gradient end |
| Navy Text | #1e3a8a | (literal) | announcement text |
| Badge Blue | #3b82f6 | (literal) | Announcement badge |
| Ink | #000000 | (default) | header title, stat values, table text |
| Slate Text | #1e293b | (literal) | card labels, question and answer text, response text |
| Grey | #6b7280 | (literal) | taglines, description, rank pills #4 and below, example instructions |
| Chip Text | #374151 | (literal) | header link chips, category descriptions |
| Chip Fill | #f9fafb | (literal) | header link chips |
| Chip Border | #d1d5db | (literal) | 1px border of header chips, example tab divider |
| Table Head | #f3f4f6 | (literal) | table header cells, question blocks, citation `pre` |
| Zebra | #f4f8fb | (literal) | even table rows |
| Row Hover | #e3edfa | (literal) | table row hover |
| Selected Column | #e6f0fa | (literal) | sorted column cells |
| Score Green | #16a34a | `.score-green` | high scores; Correct label |
| Score Blue | #2563eb | `.score-blue` | mid-high scores |
| Score Orange | #ea580c | `.score-orange` | mid-low scores |
| Score Red | #dc2626 | `.score-red` | low scores; Incorrect label |
| Score Muted | #9ca3af | `.score-muted` | missing scores "–" |
| Rank Grey | #e5e7eb | `.rank-default` | rank pills #4 and below |
| Rule | #eeeeee | (literal) | table row lines, tab list bottom border, header bottom border |
| Answer Border | #a5b4fc | (literal) | 1.5px answer block border |
| Label Wash | #f0f6ff | (literal) | response label background |
| Paper | #ffffff | (literal) | category sub-cards |
| Categories End | #d0e3fa | (inline gradient end) | Categories card |
| Group End | #c3dafe | (gradient end) | category group cards |
| Example Start | #f8fbff | (gradient start) | example category cards |
| Example End | #e0f2fe | (gradient end, border) | example category cards and their 1px border |
| Gold A | #ffd700 | `.rank-1` | first-place rank pill gradient start |
| Gold B | #ffb300 | `.rank-1` | first-place rank pill gradient end |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| UI / text | 'Rajdhani', 'PingFang SC', 'Microsoft YaHei', Arial, sans-serif | Rajdhani 500 and 700 only; 400 text uses 500, 600–900 use 700 | Rajdhani (load 500, 700) |
| Chinese examples | 'KaiTi', '楷体', 'STKaiti', '华文楷体', 'Microsoft YaHei' | system KaiTi where installed | LXGW WenKai |
| Tab buttons | browser default for `button` | Arial 16px | Arial |
| Code | browser monospace | system monospace | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Header title | `.header-title` (later rule) | 2.2rem = 35.2px / 900, letter-spacing 1px | #000000 |
| Tagline | `.header-desc` inline 1.08em | 17.28px / 400 | #6b7280 |
| Description | `.header-desc` | 0.9rem = 14.4px / 400 | #6b7280 |
| Rail link | `.sidebar-nav a` | 1.08em = 17.28px / 600 | #2563eb |
| Header chip | `.header-links a` | 0.95rem = 15.2px | #374151 |
| Announcement | `.announcement .text` | 1.02em = 16.32px / 600 / 1.5 | #1e3a8a |
| Card title | `.card-title` (later rule) | 1.55rem = 24.8px / 800, letter-spacing 0.5px | #2563eb |
| Section card title | inline on Categories / Responses | 1.6em = 25.6px / 1.45em = 23.2px | #2563eb |
| Stat value | `.card-value` | 16px / 400 | #000000 |
| Card label | `.card-label` | 0.95rem = 15.2px / 400 | #1e293b |
| Leaderboard tab | `.tabs-list button` | 16px; active bold | active #2563eb, other #000000 |
| Table | `th, td` | 16px; th 700; scores 600 with 0.5px tracking | per score class |
| Rank pill | `.rank-badge` | 0.95rem = 15.2px / 600 | #ffffff on medal gradients; #6b7280 on #e5e7eb |
| Category group title | `.category-group-card h3` | 1.35em = 21.6px / 800, letter-spacing 0.5px | #1d4ed8 |
| Sub-card title | `.category-card h4` | 1.08em = 17.28px / 700 | #2563eb |
| Response label | `.response-label` | 1.12em = 17.92px / 700 | #2563eb |
| Citation | `pre` inline 0.98em | 12.74px monospace | #000000 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow / background |
|---|---|---|---|
| Side rail | 0 12px 12px 0 | none | `linear-gradient(135deg, #e0e7ef 0%, #b6d0f7 100%)`; `0 4px 24px rgba(0,0,0,0.10), 0 1.5px 4px rgba(0,0,0,0.06)` |
| Header, stat cards, leaderboard card | 8px | header 1px #eee bottom (hidden by the gradient) | same gradient and shadow; hover `0 12px 36px rgba(37,99,235,0.18), 0 4px 16px rgba(37,99,235,0.13)` with `translateY(-2px) scale(1.015)` (cards) or `0 8px 32px rgba(0,0,0,0.16), 0 2px 8px rgba(0,0,0,0.10)` with `translateY(-4px) scale(1.03)` (tabs card) |
| Categories card | 8px, padding 32px 32px 24px | none | inline `linear-gradient(135deg,#e0e7ef 0%,#d0e3fa 100%)`; `0 8px 32px rgba(0,0,0,0.10), 0 2px 8px rgba(0,0,0,0.10)` |
| Category group card | 18px, padding 36px 28px 28px | none | `linear-gradient(135deg, #e0e7ef 0%, #c3dafe 100%)`; `0 4px 24px rgba(37,99,235,0.10), 0 2px 8px rgba(37,99,235,0.08)` |
| Category sub-card | 14px, padding 18px 14px 14px, max 220px | 2px solid #e0e7ef; hover 2.5px solid #2563eb | white; `0 1px 6px rgba(37,99,235,0.07)` |
| Examples card | 8px, max-height 800px, scrolls | 2px solid #2563eb (inline) | `0 8px 32px rgba(37,99,235,0.15)` |
| Example tab bar | 12px 12px 0 0 | 1.5px #d1d5db between tabs | active tab `linear-gradient(90deg, #2563eb 80%, #1d4ed8 100%)`, `0 4px 16px rgba(37,99,235,0.13)` |
| Example category card | 12px, padding 18px 18px 8px | 1px (declared 1.5px) solid #e0f2fe | `linear-gradient(135deg,#f8fbff 0%,#e0f2fe 100%)`; `0 2px 8px rgba(37,99,235,0.06)` |
| Question block | 10px, padding 16px 20px | 1px (declared 1.5px) solid #2563eb | #f3f4f6; `0 2px 12px 0 #2563eb33` |
| Answer block | 10px, padding 16px 20px | 1px (declared 1.5px) solid #a5b4fc | #e0e7ef; `0 2px 12px 0 #60a5fa33` |
| Header chips | 6px | 1px solid #d1d5db | #f9fafb; hover #f3f4f6 |
| Announcement | 10px | 1px solid #bfdbfe | `linear-gradient(90deg, #f5f9ff 0%, #fbfdff 100%)`; `0 2px 8px rgba(37, 99, 235, 0.08)` |
| Rank pills | 12px, padding 2px 8px | none | `linear-gradient(90deg, #ffd700, #ffb300)` gold, `linear-gradient(90deg, #c0c0c0, #b0b0b0)` silver, `linear-gradient(90deg, #cd7f32, #b87333)` bronze |
| Model link button | 50% | none | #e0e7ef; hover #2563eb with white icon |
| Correct / Incorrect labels | 7px, padding 2px 10px | none | #16a34a / #dc2626 |
| Response label | 0 8px 8px 0 | 4px solid #2563eb left | #f0f6ff |
| Citation `pre` | 6px, padding 12px | none | #f3f4f6 |

## Layout Metrics

- **Shell**: fixed 210px rail; `.main-content` margin-left 230px, so content spans x=230 to 1440. `.container` max 1200px, padding 24px; the header card spans the full main width (x=230 to the right edge) with its own inner container.
- **Header**: padding 24px + container 24px, so the logo sits at x=282, y=74; header ends at y=323; 24px margin below.
- **Stat cards**: `grid-template-columns: repeat(4, 1fr)`, gap 16px, margin-bottom 32px; four 274×192 cards with 20px padding.
- **Leaderboard**: card padding 20px; tab list flex with two equal buttons and 16px margin below; table full width with horizontal scroll (`white-space: nowrap`), cells padding 8px 12px.
- **Categories**: groups flex-wrap with 36px gap; Ambiguity group sub-cards in 2 columns, Context-dependency in 3, gap 18px.
- **Examples**: card scrolls internally above 800px; question and answer blocks 633px wide, centred, 18px apart.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1100px (1440 renders this) | 24px inside 1200px; 230px left offset | 16px | 35.2px | stat cards 4 across; category groups side by side |
| ≤1100px | same | 16px | 35.2px | category groups stack; sub-cards lose the 220px cap |
| ≤900px | rail hidden; container margin-left 0 | 16px | 35.2px | stat cards 2 across; category sub-cards 1 column |
| ≤700px | same | 16px | 35.2px | category group padding 20px 8px 16px; group title 17.6px |
| ≤600px | same | 16px | 35.2px | stat and category cards 1 column |

## Components

- **Gradient card**: `linear-gradient(135deg, #e0e7ef 0%, #b6d0f7 100%)`, radius 8px, padding 20px, shadow `0 4px 24px rgba(0,0,0,0.10), 0 1.5px 4px rgba(0,0,0,0.06)`, 24px bottom margin; hover lifts 2px and scales 1.015 with a blue-tinted shadow.
- **Side rail link**: block, padding 10px 24px, radius 8px 0 0 8px, Rajdhani 17.28px / 600 #2563eb with an emoji; hover or active: #2563eb fill, white text, a 4px #1d4ed8 bar on the left of the active item.
- **Stat card**: gradient card with a 24.8px / 800 #2563eb title, 30px gap, then a 16px value and a 15.2px #1e293b label; Best Overall stacks two value/label pairs.
- **Leaderboard**: two-tab header (active 2px #2563eb underline, bold blue); table with #f3f4f6 header cells, 1px #eeeeee row lines, #f4f8fb even rows, #e3edfa hover; sortable headers with #2563eb ▼; rank pills in gold, silver and bronze gradients then grey "#4" pills; model names with a round #e0e7ef link button; scores coloured by band (#16a34a, #2563eb, #ea580c, #dc2626, muted #9ca3af).
- **Category sub-card**: white, 2px #e0e7ef border, radius 14px, 17.28px / 700 #2563eb title and #374151 description; hover 2.5px #2563eb border and scale 1.035.
- **Example Q/A**: centred audio player; question block #f3f4f6 with a #2563eb border, radius 10px, italic grey instruction lines; answer block #e0e7ef with a #a5b4fc border and bold "Answer:" lead.
- **Announcement bar**: white-to-blue 90deg gradient, 1px #bfdbfe, radius 10px, blue badge plus bold navy sentence.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Side navigation | yes | fixed gradient rail with emoji links |
| Title / tagline | yes | heavy Rajdhani title with superscript, underlined initials |
| Authors / affiliations | absent from the source | no author list on the page |
| Venue | present but non-standard | announced in the announcement bar, not as a badge |
| Link buttons | yes | three outlined white chips with logo images |
| Stats | yes | four gradient stat cards |
| Leaderboard | yes | tabbed, sortable, colour-coded scores, medal pills |
| Categories | yes | gradient group cards with white sub-cards |
| Audio examples | yes | scrollable bordered card, EN/ZH tabs, audio players, Q/A blocks |
| Model responses | yes | response labels with left bars and correct/incorrect pills |
| Submission | yes | gradient card with an underlined blue link |
| Abstract | absent from the source | a two-line description replaces it |
| BibTeX | yes | grey `pre` in a gradient card |
| Footer | absent from the source | — |

## Adapting to Other Content

- **Authors**: add a 15.2px #374151 author line under the taglines inside the header card; keep affiliations at 14.4px #6b7280.
- **More results tables**: reuse the leaderboard card (tabs, #f3f4f6 head, zebra #f4f8fb) and the five score colours; do not add new hues.
- **More stats**: extend the stat grid in rows of four; below 900px it drops to two.
- **News**: stack announcement bars (white-to-blue gradient, #bfdbfe border, #3b82f6 badge) at the top of the header card, newest first.
- **An abstract**: put it in a gradient card titled with a 24.8px / 800 #2563eb card title and 16px #1e293b text.

## Do's and Don'ts

- Do keep every surface on the #e0e7ef → #b6d0f7 135deg gradient with the soft two-layer shadow.
- Do colour-code scores with the four bands and medal-gradient rank pills.
- Do navigate with the fixed side rail of emoji links.
- Do use Rajdhani (500 and 700) for everything, including numbers.
- Don't use flat white cards for top-level sections; white is reserved for sub-cards inside gradient groups.
- Don't stack more than one blue border card per section; the Examples card is the only bordered one.
- Don't drop the hover lift; it is part of the dashboard feel.

## Surfaces

Page gradient #f8fafc → #e0e7ef; side rail and cards on #e0e7ef → #b6d0f7; Categories on #e0e7ef → #d0e3fa with inner #e0e7ef → #c3dafe groups and white sub-cards; example cards on #f8fbff → #e0f2fe; grey #f3f4f6 table heads, question blocks and citation.

## Imagery

Very little imagery: a small red-and-blue logo, tiny brand logos in the link chips, emoji icons in the rail and tables, and native audio players. Data colour does the visual work.

## Layout

A fixed left rail and a 1200px main column: full-width header card, a four-up stat row, then stacked full-width cards for the leaderboard, categories, examples, responses, submission and citation. About 4,500px tall.

## Agent Prompt Guide

Quick colors: page #f8fafc → #e0e7ef, card #e0e7ef → #b6d0f7, main blue #2563eb, deep blue #1d4ed8, slate #1e293b, grey #6b7280, table head #f3f4f6, zebra #f4f8fb, scores #16a34a / #2563eb / #ea580c / #dc2626.

1. "Build a dashboard shell: body background linear-gradient(135deg, #f8fafc 0%, #e0e7ef 100%); fixed 210px left rail with linear-gradient(135deg, #e0e7ef 0%, #b6d0f7 100%), radius 0 12px 12px 0, box-shadow 0 4px 24px rgba(0,0,0,0.10), 0 1.5px 4px rgba(0,0,0,0.06); vertically centred links in Rajdhani 17.28px / 600 #2563eb with emoji, padding 10px 24px, hover #2563eb fill and white text; main content offset 230px."
2. "Make stat cards: four columns, gap 16px; each card uses the same gradient and shadow, radius 8px, padding 20px; title 24.8px / 800 #2563eb with letter-spacing 0.5px and 30px below; value 16px #000000; label 15.2px #1e293b; hover translateY(-2px) scale(1.015)."
3. "Create a leaderboard card: two equal tabs with a 2px #2563eb underline on the active one; table with #f3f4f6 header cells, 8px 12px padding, 1px #eeeeee row lines, #f4f8fb even rows, #e3edfa hover; rank pills radius 12px with gold linear-gradient(90deg, #ffd700, #ffb300), silver and bronze gradients, then #e5e7eb grey; scores 600 weight in #16a34a, #2563eb, #ea580c or #dc2626."

## Similar Pages

- Benchmark leaderboards built as single-file dashboards with a side rail and stat tiles.
- Glassy blue-gradient academic sites that colour-code scores by band.

## Quick Start

```css
:root {
  --page-a: #f8fafc;
  --page-b: #e0e7ef;
  --card-a: #e0e7ef;
  --card-b: #b6d0f7;
  --main-blue: #2563eb;
  --deep-blue: #1d4ed8;
  --slate: #1e293b;
  --grey: #6b7280;
  --table-head: #f3f4f6;
  --zebra: #f4f8fb;
  --score-green: #16a34a;
  --score-blue: #2563eb;
  --score-orange: #ea580c;
  --score-red: #dc2626;
  --shadow: 0 4px 24px rgba(0, 0, 0, 0.10), 0 1.5px 4px rgba(0, 0, 0, 0.06);
  --font: "Rajdhani", "PingFang SC", "Microsoft YaHei", Arial, sans-serif;
  --rail: 210px;
  --container: 1200px;
}
```

## Provenance

- **URL**: https://step-out.github.io/C3-web/
- **Paper**: C3: A Bilingual Benchmark for Spoken Dialogue Models Exploring Challenges in Complex Conversations (arXiv 2507.22968), Chengqian Ma, Wei Tao, Yiwen Guo.
- **Venue**: EMNLP 2025 (main conference, per the page's announcement).
- **Selection reason**: the arXiv comment states acceptance at EMNLP 2025 and links this project page.
- **Template credit**: none stated; a custom single-file build.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and tall screenshots, a browser probe at 1440px, and the inline stylesheet and markup of `index.html` read directly, on 2026-10-28.
