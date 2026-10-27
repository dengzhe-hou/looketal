# Brain-OF Modality Docs — Style Reference

> A well-labelled atlas: a navy sidebar index, three signal colors that never mix, and big numbers stacked in tidy cards.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share) and the 1440 screenshots, checked against the page's stylesheet styles.css (minified, with several later override blocks; where an early rule is overridden, the rendered value is used). Sizes are given at 1440 with their clamps.

## Overview

Brain-OF is laid out like product documentation. A fixed 72px frosted white top bar holds the logo and "Brain-OF" wordmark (the "OF" in violet), centered section links, a "Paper & resources ↗" outline button and a "Contents" toggle. A fixed 256px left sidebar (#fcfdff) lists numbered sections, the active one tinted blue with a 2px left bar. The content column is centered in the remaining width at 1020px. The hero is centered: a 115px Manrope ExtraBold "Brain-OF" with violet "OF", a 32px subtitle in which "fMRI", "EEG" and "MEG" are each in their own color (blue #4263d4, ochre #b67215, teal #178477), authors with superscripts, four institution logos, and three navy resource buttons. A gradient-framed schematic shows three modality cards (colored top borders) feeding a navy "Brain-OF" block, then a four-up big-number strip. Sections below carry blue uppercase labels ("02 / PRETRAINING CORPUS"), 47px ExtraBold two-sentence headings, gray justified intros, modality profile cards with 3px colored top borders, tables, interactive charts and collapsible panels.

## First Viewport

Color share of the 1440×900 viewport: #ffffff 65% (content), #fcfdff 14% (sidebar), #eff2f6 6% (hairlines and pale fills), #768098 6% (gray text mass), #fafcfe 6% (diagram gradient), #feffff and #fcfdfd 4%. The fold is white and gray; color comes only from the title accents, the navy buttons and the three modality borders.

Anatomy in DOM order:

1. **Top bar** `header.topbar`: fixed, 72px, background rgba(255,255,255,.93) with 16px backdrop blur, 1px #dfe5ed bottom border, padding 0 32px. Brand at x 32: 36px circular brain logo + "Brain-OF" Manrope 21px/800, letter-spacing -.6px, "OF" in #7751b8. Center nav Data, Method, Results, Models, DM Sans 14px/600 #19243b. Right: "Paper & resources ↗" (14px/600, 1px #dfe5ed border, radius 6px, padding 8px 14px) and "Contents" toggle (14px/600 #4263d4 on #edf1fc, 1px #d7dff5 border, radius 6px, padding 7px 10px, panel icon left).
2. **Sidebar** `aside.sidebar`: fixed below the bar, 256px wide, #fcfdff, 1px #dfe5ed right border, padding 32px 16px 24px. Heading "EXPLORE THE RESEARCH" 12px/700, letter-spacing 1.7px, #627086. Links 14px/400 #607087 with 12px numerals at 65% opacity, padding 10px, radius 5px; active link 700 #4263d4 on #edf1fc with a 2px #4263d4 left border. At the bottom, a short rule, a 13px #627086 two-line message and a modality legend (colored dots: fMRI, EEG, MEG).
3. **Title** `h1` (centered in the 1020px column, x 338–1358): "Brain-OF", Manrope 115px/800 (clamp 70px, 8vw, 118px), letter-spacing -7px, line-height 1.1, #19243b, with "OF" in #7751b8. Top at 153px (hero padding 62px + 19px margin). Gap 14px.
4. **Subtitle** `p.paper-title`: two lines, Manrope 32px/650 (clamp 21px, 2.5vw, 32px), line-height 1.4, letter-spacing -.7px, #19243b; the "O" and "F" of OmniFunctional in violet, "fMRI" #4263d4, "EEG" #b67215, "MEG" #178477. Gap 22px.
5. **Venue** `p.venue-line`: "NeurIPS 2026", Manrope 18px/700, letter-spacing .3px, #15264c. Gap 20px.
6. **Authors** `.authors`: two centered lines, DM Sans 14px, line-height 2.1, #19243b, superscript affiliation numbers, 13px between names; max-width 740px.
7. **Affiliation logos**: four logos (Jülich, RWTH, HHU, JARA), max 150px wide, each with a small number above-left. Gap 24px.
8. **Resource buttons**: arXiv, Code ↗, Checkpoints; 57px tall, navy #15264c, white DM Sans 15px/700, radius 9px, icons left; 10px gaps.
9. **Hero schematic** (from y ≈ 700): bordered panel (1px #dce3ef, radius 16px, padding 26px 38px 22px, gradient #f8faff → #ffffff → #f1faf8), caption "HETEROGENEOUS SIGNALS · JOINT PRETRAINING" 12px uppercase, three white input cards with 3px colored top borders and 23px modality names in their colors.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | --paper | content background, input cards, figure frames |
| Ink | #19243b | --ink | title, headings, body, nav links |
| Navy | #15264c | --navy | resource buttons, shared-model block in the schematic, venue line, selected segmented buttons, emphasized TL;DR text |
| Navy Border | #243c68 | (literal) | resource button border |
| Muted | #627086 | --muted | section intros, captions, stat labels, eyebrows, footer |
| Sidebar Link | #607087 | (literal) | inactive sidebar links |
| Table Head | #566782 | (literal) | table header text |
| Table Text | #506077 | (literal) | table cells |
| Code Text | #344766 | (literal) | BibTeX |
| Line | #dfe5ed | --line | top-bar and sidebar borders, section rules, table rows, stat dividers, figure frames |
| Panel Border | #dce3ef | (literal) | hero schematic border |
| Sidebar | #fcfdff | (literal) | sidebar background |
| Soft | #f6f8fc | --soft | segmented hover, soft panels |
| Table Header Fill | #f5f7fb | (literal) | table header cells |
| Code Wash | #f3f6fb | (literal) | BibTeX block |
| Active Tint | #edf1fc | (literal) | active sidebar link, Contents toggle fill |
| Toggle Border | #d7dff5 | (literal) | Contents toggle border |
| Ours Row | #f1f5ff | (literal) | Brain-OF rows in tables |
| fMRI Blue | #4263d4 | --fmri | "fMRI" text, fMRI card borders, section labels, active sidebar link, links |
| EEG Ochre | #b67215 | --eeg | "EEG" text and card borders |
| MEG Teal | #178477 | --meg | "MEG" text and card borders |
| OF Violet | #7751b8 | (literal) | "OF" in the wordmark and title, O/F initials in the subtitle |
| Input Border | #d9e0ed | (literal) | modality input card borders |
| Connector | #a8b6cc | (literal) | connector lines in the schematic |
| Model Subline | #ccd7ed | (literal) | subline text inside the navy shared-model block |
| Hover Wash | #f0f3f8 | (literal) | sidebar link hover |
| Frame Hover | #a9b9d6 | (literal) | figure frame border on hover |
| Copy Border | #bdc9dd | (literal) | BibTeX copy button border |
| Button Shadow | #14254b | (literal) | resource button shadow color, used at 8% alpha |
| Diagram Mint | #f1faf8 | (literal) | end stop of the schematic gradient |
| Diagram Blue | #f8faff | (literal) | start stop of the schematic gradient |

## Tokens — Typography

- **Display**: declared `'Manrope', Arial, sans-serif`; renders Manrope 700 and 800 (the 650 weight of the subtitle is synthesized from the loaded faces). Substitute: Plus Jakarta Sans ExtraBold.
- **Body/UI**: declared `'DM Sans', Arial, sans-serif`; renders DM Sans 400, 500, 600, 700. Substitute: Inter.
- **Mono**: `monospace` (system) for BibTeX.

| Role | Selector | Size at 1440 (clamp) | Weight | Line-height | Tracking |
|---|---|---|---|---|---|
| Title | `h1` | 115px (70px, 8vw, 118px); 85px ≤900px; 73px ≤600px | 800 | 1.1 | -7px |
| Model card name | `.model-grid h3` | 48px | 700 | 1.17 | -2px |
| Section heading | `h2` | 47px (32px, 3.4vw, 47px) | 800 | 1.2 | -1.8px |
| Shared model name | `.shared-model strong` | 34px | 800 | 1.4 | -1px |
| Hero stat | `.hero-stats strong` | 33px | 800 | 1.17 | -1px |
| Profile total | `.profile-total` | 34px (23px, 2.7vw, 34px) | 800 | 1.2 | -1px |
| Subtitle | `.paper-title` | 32px (21px, 2.5vw, 32px) | 650 | 1.4 | -.7px |
| Modality card heading | `h3` in profile and input cards | 23–25px | 700 | 1.17 | -.5px |
| Brand | `.brand` | 21px | 800 | 1.65 | -.6px |
| TL;DR lead, intros | `.tldr p`, `.section-intro` | 18px | 400 (lead 700) | 1.8 | 0 |
| Venue | `.venue-line` | 18px | 700 | 1.65 | .3px |
| Body | `body` | 16px | 400 | 1.65 | 0 |
| Buttons | `.resource-button` | 15px | 700 | 1.65 | 0 |
| Nav, sidebar, tables, authors | `.topbar nav a`, `.sidebar nav a`, `table`, `.authors` | 14px | 600 / 400 / 400 / 400 | 1.5–2.1 | 0 |
| Labels and eyebrows | `.section-label`, `.side-heading`, `.eyebrow` | 12px uppercase | 700 | 1.5 | 1.7px |
| Captions, stat labels | `figcaption`, `.hero-stats span` | 12–13px | 400 | 1.65 | 0 |

## Tokens — Spacing & Shapes

- **Radius**: 16px for the hero schematic; 10px for the shared-model block; 9px for resource buttons and figure frames; 8px for input cards, corpus profile cards and BibTeX; 6px for top-bar buttons; 5px for sidebar links and segmented buttons.
- **Shadows**: resource buttons 0 3px 7px rgba(20,37,75,.08); selected segmented button 0 2px 3px rgba(21,38,76,.08); mobile sidebar drawer 15px 0 40px rgba(16,32,64,.13). Cards are otherwise flat.
- **Borders**: 1px #dfe5ed on almost everything; 3px colored top borders (#4263d4, #b67215, #178477) on modality cards; 2px #4263d4 left bar on the active sidebar item.

## Layout Metrics

- **Frame**: fixed top bar 72px; fixed sidebar 256px; `main` margin-left 256px, padding-top 72px, side padding clamp(28px, 5vw, 86px) = 72px, max-width 1580px.
- **Content column**: `.hero, .section` max-width 1020px, centered in main (x 338–1358 at 1440).
- **Hero**: padding-top 62px, centered; authors max-width 740px; resource buttons margin 24px 0 33px.
- **Schematic**: margin-top 35px, padding 26px 38px 22px; three input cards in a row; navy block max-width 430px below, linked by 1px #a8b6cc connector lines.
- **Hero stats**: 4 columns, padding 29px 0, 1px dividers and a bottom rule.
- **Sections**: padding 48px 0 (34px ≤600px), no bottom border in the override; label 22px above h2; intro margin 24px 0 35px.
- **Corpus profiles**: 3 columns of bordered cards, padding 25px 22px.
- **Tables**: full column width, cells 11px 14px.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1700px | auto | 16px | 118px | main centered with margin-left max(256px, (100vw − 1360px)/2) |
| 1151–1699px | 72px (5vw) | 16px | 8vw | sidebar 256px fixed |
| ≤1150px | 35px | 16px | 8vw | sidebar narrows; tighter top-bar gaps; bar charts compress |
| ≤900px | 35px | 16px | 85px | sidebar becomes a slide-in drawer opened by Contents; top bar grows to two rows with a scrolling nav; h2 39px; subtitle 28px |
| ≤600px | 22px | 16px | 73px | hero stats 2×2; profile cards and fusion panels 1 column; buttons 14px; h2 33px; BibTeX 13px |

## Components

- **Resource button** `.resource-button`: min-height 53px (57px rendered), padding 13px 20px, #15264c fill, 1px #243c68 border, radius 9px, #ffffff DM Sans 15px/700, brand icon left (arXiv, GitHub, Hugging Face) with 10px gap, "↗" on external links, shadow 0 3px 7px rgba(20,37,75,.08).
- **Outline top button** `.top-paper`: 14px/600 #19243b, 1px #dfe5ed border, radius 6px, padding 8px 14px.
- **Sidebar item**: padding 10px, radius 5px, 14px #607087, 12px tabular numeral at 65% opacity; hover #f0f3f8; active #4263d4, 700, #edf1fc fill, 2px #4263d4 left border.
- **Section label** `.section-label`: 12px/700 uppercase, 1.7px tracking, #4263d4, "NN / NAME".
- **Modality input card** `.input`: #ffffff, 1px #d9e0ed border, 3px colored top border, radius 8px, padding 15px 6px; name Manrope 23px in the modality color; 12px #627086 description.
- **Shared-model block**: #15264c, radius 10px, padding 17px 25px, max-width 430px; overline 12px, name Manrope 34px/800 white, subline 12px #ccd7ed.
- **Big-number stat**: Manrope 33px/800, -1px, #19243b over a 12px #627086 label; columns divided by 1px #dfe5ed.
- **Corpus profile card**: 1px #dfe5ed border, 3px modality-colored top border, radius 8px, padding 25px 22px; heading 25px in the modality color, 34px/800 total, then a definition list split by hairlines.
- **Table**: 14px, header 600 #566782 on #f5f7fb, cells 11px 14px with 1px #dfe5ed bottom borders, text #506077; Brain-OF rows #f1f5ff fill, #15264c 600.
- **Segmented control**: 14px buttons, padding 7px 15px, radius 5px; selected #15264c with white text and a small shadow; hover #f6f8fc.
- **Figure frame** `.figure-zoom`: #ffffff, padding 15px, 1px #dfe5ed border, radius 9px; a "zoom" chip bottom-right (12px on rgba(245,247,251,.93), radius 4px); hover border #a9b9d6.
- **BibTeX**: #f3f6fb panel, radius 8px, 14px/1.8 mono #344766, copy button top-right (white, 1px #bdc9dd, radius 5px, 13px #15264c).

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top nav | yes | fixed frosted bar with brand, centered links and two buttons |
| Sidebar TOC | yes, non-standard | fixed numbered contents with an active state |
| Title block | yes | centered giant wordmark with violet accent, color-coded subtitle |
| Authors / affiliations | yes | centered superscripted names and a row of institution logos |
| Link buttons | yes | navy filled buttons with brand icons |
| Teaser | yes, non-standard | HTML schematic of modalities feeding the model, not an image |
| Stat strip | yes | four big-number columns |
| TL;DR | yes | two-column "WHY JOINT PRETRAINING?" eyebrow plus 18px lead |
| Data cards | yes | modality profile cards with big totals |
| Figures | yes | framed, zoomable paper figures |
| Results | yes | interactive bar charts with a dataset selector, tables with tinted rows |
| Collapsible panels | yes | "Explore the pretraining datasets" style rows with "+" |
| Model family | yes | cards with 48px model names |
| BibTeX | yes | tinted block with copy button |
| Footer | yes | 1px rule, brand and 12px muted text |

## Adapting to Other Content

- **More authors**: keep centered 14px lines at line-height 2.1 with superscripts; max-width 740px wraps cleanly to three or four lines; add more logos to the affiliation row (max 150px each).
- **Results table**: use the table recipe as is, highlight the proposed rows with #f1f5ff and #15264c 600, and color any per-modality column headers with the three modality colors.
- **Long publication list**: one sidebar entry for "Publications"; in the column, rows separated by 1px #dfe5ed with a 12px uppercase #4263d4 year label and 16px titles.
- **News**: a section labelled "NN / NEWS" with dated rows; dates in 12px/700 uppercase #627086, text 16px #19243b.
- **More than three categories**: give each category one fixed color and reuse it on text, card top borders and chart bars; never mix two category colors in one element.

## Do's and Don'ts

- Do keep one color per modality and repeat it everywhere that modality appears.
- Do use Manrope ExtraBold for display text and numbers, DM Sans for everything else.
- Do number sections in both the sidebar and the section label.
- Do frame cards with 1px #dfe5ed and a 3px colored top border for categories.
- Don't use the modality colors for UI chrome; buttons are navy, links blue.
- Don't center body sections; only the hero is centered.
- Don't add drop shadows to cards; only buttons get a light one.

## Surfaces

White content, #fcfdff sidebar, frosted white top bar, a pale blue-to-mint gradient panel around the schematic, #f5f7fb table heads, #f3f6fb code, navy blocks for buttons and the shared model.

## Imagery

An HTML/CSS schematic in the hero, paper figures (architecture, reconstructions, spectra) in white frames, interactive bar charts and dataset bars colored by modality, and institution logos.

## Layout

Fixed top bar and fixed left sidebar with a 1020px content column; hero centered, sections left-aligned with 3-column card grids, 4-column stat strips and full-width tables. About 10,300px tall.

## Agent Prompt Guide

Quick colors: ink #19243b, navy #15264c, muted #627086, line #dfe5ed, sidebar #fcfdff, active tint #edf1fc, fMRI #4263d4, EEG #b67215, MEG #178477, violet #7751b8, ours row #f1f5ff.

1. "Build a docs sidebar: fixed, 256px wide, background #fcfdff, 1px solid #dfe5ed right border, padding 32px 16px 24px; heading 12px/700 uppercase, letter-spacing 1.7px, #627086; links DM Sans 14px #607087 with 12px numerals at 65% opacity, padding 10px, radius 5px; the active link #4263d4, weight 700, background #edf1fc, 2px solid #4263d4 left border."
2. "Build a resource button: min-height 53px, padding 13px 20px, background #15264c, 1px solid #243c68, radius 9px, DM Sans 15px/700 #ffffff, brand icon on the left with 10px gap, shadow 0 3px 7px rgba(20,37,75,.08)."
3. "Build category cards: 3-column grid; each card 1px solid #dfe5ed with a 3px top border in its category color (#4263d4, #b67215 or #178477), radius 8px, padding 25px 22px; heading Manrope 25px/700 in the category color; a 34px/800 #19243b total; a 12px #627086 label."

## Similar Pages

- Documentation-style project sites with a fixed sidebar table of contents.
- Multimodal papers that assign a fixed color to each data type across text, diagrams and charts.

## Quick Start

```css
:root {
  --navy: #15264c;
  --ink: #19243b;
  --muted: #627086;
  --line: #dfe5ed;
  --paper: #ffffff;
  --soft: #f6f8fc;
  --sidebar-bg: #fcfdff;
  --active-bg: #edf1fc;
  --ours-bg: #f1f5ff;
  --fmri: #4263d4;
  --eeg: #b67215;
  --meg: #178477;
  --violet: #7751b8;
  --side: 256px;
  --top: 72px;
  --sans: 'DM Sans', Arial, sans-serif;
  --display: 'Manrope', Arial, sans-serif;
}
```

## Provenance

- **URL**: https://hanningguo.github.io/BrainOF
- **Paper**: Brain-OF: An Omnifunctional Foundation Model for fMRI, EEG and MEG (arXiv 2602.23410), Hanning Guo et al.
- **Venue**: NeurIPS 2026.
- **Selection reason**: the arXiv comment states acceptance at NeurIPS 2026 and links this page.
- **Template credit**: custom page; no template credit shown.
- **Evidence used**: computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440 screenshot and tall capture, and styles.css read directly (later override blocks taken as the rendered values). Captured 2026-10-28.
