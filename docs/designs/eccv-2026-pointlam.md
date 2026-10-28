# PointLAM — Style Reference

> A clean conference handout with a crimson wax seal: one deep-red wordmark, tiny red kickers, and everything else in quiet graphite on white.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, plus targeted probes of the hero, kickers, idea grid, metric band, citation and figures), the 1440×900 shot and a full-page capture, and the page's own `style.css` and `index.html`. Two lower figures load lazily and appear blank in the full-page capture.

## Overview

A short (4,762px), centred academic page on white #ffffff in the system UI font (Segoe UI on Windows) with graphite ink #24272c. The hero opens with a tiny gray line "European Conference on Computer Vision" beside an outlined crimson "ECCV 2026" chip, then a 66px/750 crimson #a52c39 wordmark "PointLAM", a two-line 38px/650 subtitle, 18px/500 authors, a two-level affiliation and three 44px pill buttons (dark filled "Paper (arXiv)", outlined "BibTeX" and "Code"). A full-width teaser figure (1000px) and a gray caption close the hero above a 1px #e7e7e9 rule. Sections are centred under 10px uppercase crimson kickers ("THE PROBLEM & THE IDEA") and 34px/650 headings: an 800px abstract, a full-width architecture figure, a three-column "Key ideas" grid numbered 01–03 in crimson with hairline tops, a pale #f7f8fa results band with three large 48px numbers separated by vertical rules, a qualitative figure, a two-column "Structure-aware features" block on the tint, and a BibTeX block with a "Copy BibTeX" button. Generous whitespace does most of the work; crimson appears only in small doses.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 83.8% plus near-whites #f0f0ef 2.6%, #fbfbfb 1.8%, #fdffff 0.4% and #fffffd 0.3%; warm gray #aea6a3 4.4% and mauve-gray #685a63 3.5% (text, crimson wordmark and figure strokes blended); pale green-gray #d7d9ce 3.2% (teaser figure fills). Crimson covers too little area to form its own cluster.

Anatomy in DOM order (desktop 1440px, everything centred in a 1000px container at x 220–1220):

1. **Hero** (`header.hero`, 0–846): padding 56px 0 0, no nav bar.
2. **Venue line** (`p.venue`, y=56): flex, 12px gap; "European Conference on Computer Vision" 12px #66707a, letter-spacing .045em; chip "ECCV 2026" 11px/750 #a52c39, letter-spacing .075em, padding 4px 9px, 1px #ead4d7 border, 4px radius. Gap 24px.
3. **Wordmark** (`span.project-name`, y=109, 69px): 66px/750, line-height 1.05, letter-spacing -0.05em, #a52c39. Gap 17px.
4. **Subtitle** (`span.project-title`, y=196, 94px, two lines): 38px/650, line-height 1.24, letter-spacing -0.033em, #24272c. h1 margin-bottom 25px.
5. **Authors** (`.authors`, y=315): 18px/500 #3b4553, gaps 8px 30px, plain text (no links). Gap 10px.
6. **Affiliation** (`p.affiliation`, y=356, 53px): "Shanghai Jiao Tong University" 16px/500 #454e58, then "MoE Key Lab of Artificial Intelligence · Institute of AI" 14px #66707a. Gap 23px.
7. **Buttons** (`nav.links`, y=432, 44px tall, 10px gaps): pills with 28px radius, padding 9px 20px, 14px/550; "Paper (arXiv)" #2b3038 fill and border with white text and a 17px document icon; "BibTeX" (with a 17px quote icon) and "Code" with a 1px #d5d9df border and #24272c text. Gap 42px.
8. **Teaser** (`figure.teaser`, y=518): width 1000px, padding 4px 0 30px, 1px #e7e7e9 bottom border; image 1000×228 (y=522); caption 14px/1.7 #66707a, max 810px, 18px below, lead phrase in 600 #454e58. Hero ends at y=846.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | (literal) | page background, plain sections, copy button fill, primary button text |
| Graphite | #24272c | --ink | subtitle, section headings, idea titles, metric numbers, outline button text |
| Slate Muted | #66707a | --muted | venue line, affiliation detail, captions, idea text, metric notes, footer |
| Crimson | #a52c39 | --accent | wordmark, venue chip text, kickers, idea numbers, links, focus outline |
| Chip Border | #ead4d7 | (literal) | venue chip border |
| Hairline | #e7e7e9 | --line | teaser bottom rule, idea-card top rules, BibTeX border, footer rule |
| Tint | #f7f8fa | --soft | results band and features band (`.tinted`), copy button hover |
| Author Ink | #3b4553 | (literal) | author names |
| Affiliation Ink | #454e58 | (literal) | university line, caption lead, copy button text, footer strong |
| Abstract Ink | #4d5660 | (literal) | abstract paragraph |
| Button Dark | #2b3038 | (literal) | primary pill fill and border; hover #414956 |
| Button Border | #d5d9df | (literal) | outline pill border; hover border #a5aab2 and fill #f2f3f5 |
| Metric Rule | #dfe2e6 | (literal) | vertical dividers between metrics |
| Code Well | #f5f6f8 | (literal) | BibTeX background; text #485361 |
| Copy Border | #d8dce1 | (literal) | Copy BibTeX button border |
| Disabled Pill | #f5f6f7 | (literal, declared) | disabled link fill (text #737984); no disabled link renders on the page |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| UI / text | -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif | no web font loaded; Segoe UI on Windows, SF Pro on macOS (weights 550/650/750 snap to the nearest face) | Inter |
| Code | ui-monospace, SFMono-Regular, Consolas, monospace | Consolas on Windows | JetBrains Mono |

| Role | Selector | Size / weight / line-height / tracking | Color |
|---|---|---|---|
| Wordmark | `.project-name` | clamp(48px, 7vw, 66px) → 66px / 750 / 1.05 / -0.05em | #a52c39 |
| Subtitle | `.project-title` | clamp(25px, 3.6vw, 38px) → 38px / 650 / 1.24 / -0.033em | #24272c |
| Section heading | `h2` | clamp(26px, 3vw, 34px) → 34px / 650 / 1.25 / -0.035em | #24272c |
| Kicker | `.eyebrow` | 10px / 700 / uppercase / .12em | #a52c39 |
| Idea title | `h3` | 19px / 650 / 1.4 / -0.02em | #24272c |
| Idea number | `.idea-number` | 12px / 650 tabular | #a52c39 |
| Body | `body` | 17px / 400 / 1.75 | #24272c |
| Abstract | `.abstract-section p` | 16px / 1.9 | #4d5660 |
| Authors | `.authors` | 18px / 500 | #3b4553 |
| Affiliation | `.affiliation` | 14px / 1.75; university 16px / 500 | #66707a / #454e58 |
| Button | `.links a` | 14px / 550 | white or #24272c |
| Metric number | `.metric-grid strong` | 48px / 600 / 1.2 / -0.04em tabular | #24272c |
| Metric label / note | `.metric-grid span` / `p` | 14px / 650 and 12px | #24272c / #66707a |
| Caption | `figcaption` | 14px / 1.7, max 810px | #66707a |
| BibTeX | `pre` | 12px / 1.8 | #485361 |
| Footer | `footer` | 12px | #66707a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow / effect |
|---|---|---|---|
| Link pills | 28px | 1px #2b3038 (primary) or #d5d9df | none; hover fill changes |
| Venue chip | 4px | 1px #ead4d7 | none |
| Copy BibTeX button | 5px | 1px #d8dce1 | hover #f7f8fa |
| BibTeX block | 6px | 1px #e7e7e9 | none |
| Idea cards | 0 | 1px #e7e7e9 top only | none |
| Figures | 0 | none | zoom-in cursor on figure links |
| Focus ring | n/a | 3px #a52c39 outline, offset 5px | none |

## Layout Metrics

- **Container**: `.container { width: min(1000px, calc(100% - 48px)); margin-inline: auto }` → x 220–1220 at 1440; `.narrow` 800px (abstract, BibTeX) → x 320–1120.
- **Hero**: padding 56px 0 0; vertical chain 29 (venue) + 24 + 69 (wordmark) + 17 + 94 (subtitle) + 25 + 32 (authors) + 10 + 53 + 23 + 44 (buttons) + 42 + 4 + 228 (teaser) + 18 + 48 (caption) + 30 = 790px from y=56 to y=846.
- **Sections**: padding 68px 0; kicker margin-bottom 10px; h2 margin-bottom 28px; the section after the abstract is 20px 0 8px; the ideas section 30px 0 65px.
- **Idea grid**: 3 columns, gap 36px → 309px columns; 1px top rule, 18px top padding; number 10px above the title.
- **Metric band**: `.tinted` #f7f8fa, 3 columns, margin 36px 0 30px, items padding 0 22px with 1px #dfe2e6 left rules; result note max 800px, 14px.
- **Two-column block**: grid 1fr / 1.1fr, gap 60px, centred vertically; text left-aligned.
- **Footer**: padding 26px 0, 1px #e7e7e9 top, brand left and university floated right.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| base (1440) | 220px (container 1000px) | 17px | wordmark 66px, subtitle 38px | 3-column ideas and metrics |
| ≤1056px | 24px from 1048px down | 17px | subtitle 3.6vw, e.g. 34.6px at 960 | none |
| ≤943px | 24px | 17px | wordmark 7vw, e.g. 56px at 800 | none |
| ≤700px | 18px | 17px | wordmark 48px floor; subtitle 29px | hero padding-top 35px; venue stacks; buttons 13px with 14px side padding; sections 46px; ideas 1 column with numbers in a 38px left gutter; metrics stack at 42px with top rules; two-column stacks; BibTeX 11px |

## Components

- **Venue chip**: inline next to a 12px #66707a conference name; 11px/750 #a52c39, letter-spacing .075em, padding 4px 9px, 1px #ead4d7 border, 4px radius, no fill.
- **Crimson wordmark**: the project name alone in 66px/750 #a52c39 with -0.05em tracking, set above the graphite descriptive title.
- **Primary pill** (`.primary-link`): min-height 44px, padding 9px 20px, radius 28px, #2b3038 fill and border, white 14px/550, 8px gap to a 17px stroked icon (1.65px stroke); hover #414956.
- **Outline pill** (`.links a`): same box, transparent, 1px #d5d9df border, #24272c text; hover #f2f3f5 fill and #a5aab2 border. A disabled variant uses #f5f6f7 fill, #737984 text and an 11px "coming soon" note.
- **Kicker + heading**: centred 10px/700 uppercase .12em #a52c39 kicker, 10px gap, 34px/650 heading with -0.035em tracking.
- **Idea card** (`.idea-grid article`): 1px #e7e7e9 top rule, 18px top padding; 12px/650 crimson number "01", 19px/650 title, 14px/1.8 #66707a text.
- **Metric column** (`.metric-grid article`): centred, padding 0 22px, 1px #dfe2e6 left rule between items; 48px/600 #24272c number, 12px gap, 14px/650 label, 12px #66707a note 8px below.
- **BibTeX**: heading row with left-aligned kicker and h2 ("Cite PointLAM") and a right "Copy BibTeX" button (12px #454e58, padding 8px 13px, 1px #d8dce1, 5px radius, white); pre on #f5f6f8, 1px #e7e7e9, 6px radius, padding 22px 24px, 12px/1.8 #485361.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navigation bar | absent from the source | the page starts directly with the venue line |
| Venue badge | yes | conference name plus outlined crimson chip |
| Title / authors / affiliations | yes | crimson wordmark, graphite subtitle, plain authors, two-line affiliation |
| Link buttons | yes | dark filled pill plus outlined pills with stroked icons |
| Teaser figure | yes | full 1000px figure with centred gray caption and a bottom rule |
| Abstract | yes | 800px column at 16px/1.9 under a crimson kicker |
| Method figure | yes | full-width architecture diagram with caption |
| Key ideas | yes | three numbered columns with hairline tops |
| Results | present but non-standard | three headline metrics on a tinted band instead of a table |
| Qualitative figure | yes | full-width figure with caption |
| Feature visualization | yes | two-column text and square figure on the tint |
| BibTeX | yes | gray code block with copy button |
| Footer | yes | one 12px line with a hairline above |

## Adapting to Other Content

- **More authors**: keep the centred flex-wrap at 18px/500 #3b4553 with gaps 8px 30px; add superscript markers in 12px #66707a and list affiliations as extra 14px lines.
- **A results table**: put it in the 1000px container on the #f7f8fa band below the metric columns; header 12px/650 uppercase .12em #66707a, cells 14px #24272c tabular with 1px #e7e7e9 rules, best values 650 #a52c39. No fills or radius.
- **Long publication or news lists**: use idea-card rows: 1px #e7e7e9 top rule, 18px padding, a 12px/650 crimson date or index, a 19px/650 title and 14px #66707a detail.
- **More metrics**: keep three per row; add a second metric row rather than shrinking the 48px numbers.
- **A video**: treat it like a figure: full container width, no border, a centred 14px #66707a caption 18px below.

## Do's and Don'ts

- Do keep crimson #a52c39 to the wordmark, chip text, kickers and numbers.
- Do centre the hero and section headings, and left-align body text inside narrow columns.
- Do separate ideas and metrics with hairline rules (#e7e7e9, #dfe2e6) rather than cards.
- Do alternate white and #f7f8fa bands for results-type sections.
- Don't load a web font; the system UI face is part of the look.
- Don't add shadows or card fills; the only filled shapes are the dark pill and the code well.
- Don't use crimson for buttons; the primary pill is dark graphite #2b3038.

## Surfaces

White page and plain sections; #f7f8fa bands for the metrics and the feature visualization; #f5f6f8 code well with a #e7e7e9 border. No shadows, gradients or textures.

## Imagery

Black-line academic diagrams with soft green, yellow, red and blue fills (a sets/voxels/points comparison and a speed-accuracy bubble plot in the teaser; the architecture diagram), LiDAR detection visualizations and a square point-retention heat map.

## Layout

A centred single column: 1000px for figures and grids, 800px for prose and code. The hero is fully centred; sections stack with 68px padding, and only the feature block uses a two-column layout. Whitespace and two tinted bands provide rhythm.

## Agent Prompt Guide

Quick colors: white #ffffff, ink #24272c, muted #66707a, crimson #a52c39, chip border #ead4d7, hairline #e7e7e9, tint #f7f8fa, dark button #2b3038, button border #d5d9df.

1. "Build a centred hero on white with padding 56px 0 0: a 12px #66707a conference line with an outlined chip (11px/750 #a52c39, padding 4px 9px, 1px #ead4d7 border, 4px radius), a 66px/750 #a52c39 wordmark with letter-spacing -0.05em, a 38px/650 #24272c subtitle with -0.033em tracking, 18px/500 #3b4553 authors with 30px gaps, and 44px pills (padding 9px 20px, radius 28px, 14px/550): one #2b3038 with white text, others with a 1px #d5d9df border."
2. "Make a key-ideas row: 3 columns, 36px gap, each with a 1px #e7e7e9 top border and 18px top padding, a 12px/650 #a52c39 number, a 19px/650 #24272c title and 14px/1.8 #66707a text. Above it a centred 10px/700 uppercase kicker in #a52c39 (.12em) and a 34px/650 heading."
3. "Create a results band: background #f7f8fa, padding 68px 0; three centred columns separated by 1px #dfe2e6 left rules, each with a 48px/600 tabular #24272c number, a 14px/650 label and a 12px #66707a note."

## Similar Pages

- Minimal centred project pages that use one deep accent color for the project name.
- 3D detection and point-cloud papers presented with a teaser figure, key-idea columns and headline metrics.

## Quick Start

```css
:root {
  --ink: #24272c;
  --muted: #66707a;
  --accent: #a52c39;
  --line: #e7e7e9;
  --soft: #f7f8fa;
  --button-dark: #2b3038;
  --button-border: #d5d9df;
  --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  --container: min(1000px, calc(100% - 48px));
  --narrow: 800px;
}
body { background: #ffffff; color: var(--ink); font: 17px/1.75 var(--font); }
```

## Provenance

- **URL**: https://pointlam.github.io/
- **Paper**: PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection (arXiv 2609.21780), Xuanming Shang, Weijia Zhang, Chao Ma (Shanghai Jiao Tong University).
- **Venue**: ECCV 2026.
- **Selection reason**: the arXiv abstract links this project page and the comment states acceptance at ECCV 2026.
- **Template credit**: none stated; a small hand-written page (`style.css`, `script.js`).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted probes of hero, kickers, idea grid, metric band, figures and citation, the 1440×900 shot and a full-page capture, and the page's `style.css` and `index.html` read directly, on 2026-10-28.
