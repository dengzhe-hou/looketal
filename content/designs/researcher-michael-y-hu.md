# Plum Pull-Quote — Style Reference

> A clean index card in Inter with one plum ink: a pull-quote bar for the research statement and mono pills for every project.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, the page's own `style.css` and `index.html`, and the rendered boxes. The stylesheet also styles a news table and blog pages; the homepage renders neither, so those rules are listed only where they help adapt the style.

## Overview

A short single-column homepage (about 1,030px tall at 1440) on an almost-white #fcfcfd ground. Everything sits in an 820px body column. The header row has the name in Inter 32px/700, a 16px/500 subtitle and an IBM Plex Mono email line on the left, and three 23px glyph icons (GitHub, Twitter, Google Scholar) on the right. The hero pairs a 580px text column (17px Inter, plum #56018d links without underline) with a 200px rounded photo carrying a very soft two-layer shadow. The research statement is set as a pull-quote: 19px/600 with a 3px plum left bar. A "RESEARCH" label in 13px uppercase mono with a hairline underneath introduces a 2×2 grid of white cards, each with a 17px/600 topic title and IBM Plex Mono project pills tinted plum at 8%. Cards lift 2px and turn their border plum on hover.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): near-white #fcfcfd / #fdfcfd / #fafcfe / #fdfcfb / #fcfcfe 76.5%; white #ffffff 11.8% (the cards); mauve gray #a8989d 6.2% (the photo and antialiased text); pale lilac #f3f1f5 5.6% (pill fills and card borders blended). Plum #56018d appears in links, pills and the pull-quote bar but covers too little area to form a cluster.

Anatomy in DOM order (body `max-width: 820px; margin: 56px auto`, so content runs x=310–1130):

1. **Header** (`header.header`, y=56–168): flex, space-between, align flex-start, margin-bottom 48px.
2. **Name** (`.name p`, y=56, 53px tall): Inter 32px/700, line-height 1.65 (52.8px), letter-spacing -0.02em, #1f2024. Gap 4px.
3. **Subtitle** (`p.subtitle`, y=113): "MTS at Principia, PhD at NYU", 16px/500, #1f2024. Gap 4px.
4. **Email** (`p.email`, y=143): "[first]@principialabs.org", IBM Plex Mono 15px/400, #6b7280.
5. **Social icons** (right, y=71 after a 15px top margin): three 23px SVG glyphs in #1f2024, 18px apart (x=1025, 1066, 1107); hover #56018d.
6. **Hero** (`section.hero`, y=216–535): flex, gap 40px; text column 580px, photo column 200px. Margin-bottom 56px.
7. **Bio paragraph** (y=216): 17px/400, line-height 28.05px, #1f2024; links #56018d, no underline (underline with 2px offset on hover). 16px below.
8. **Pull-quote** (`p.lead`, y=322, 63px tall): 19px/600, letter-spacing -0.01em, #1f2024, 3px solid #56018d left border, 16px left padding, 22px margins.
9. **Second paragraph** (y=407–519): same as the bio.
10. **Photo** (x=930, y=216): 200×200px, 12px radius, shadow `0 1px 2px rgba(20, 20, 30, 0.04), 0 8px 24px rgba(20, 20, 30, 0.04)`.
11. **Research label** (`h2.section-label`, y=591): IBM Plex Mono 13px/500 uppercase, letter-spacing 0.12em, #6b7280, padding-bottom 12px, 1px #e7e7ea bottom border, 24px margin below.
12. **Card grid** (from y=644): 2 columns, 16px gap; first row of cards visible to the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Near White | #fcfcfd | --bg | page background |
| White | #ffffff | --surface | research cards |
| Ink | #1f2024 | --text | name, subtitle, body text, card titles, pull-quote, social icons |
| Muted | #6b7280 | --muted | email line, section label |
| Plum | #56018d | --accent | links, pill text, pull-quote bar, card hover border, pill hover border, social icon hover |
| Plum Wash | rgba(86, 1, 141, 0.08) | --accent-soft | pill fill |
| Hairline | #e7e7ea | --border | card borders, pill borders, section-label underline |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans | 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif | Inter 400, 500, 600, 700 | Inter |
| Mono | 'IBM Plex Mono', ui-monospace, monospace | IBM Plex Mono 400, 500 | IBM Plex Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `.name p` | 32px / 700 / 1.65, letter-spacing -0.02em | #1f2024 |
| Subtitle | `.name .subtitle` | 16px / 500 / 1.65 | #1f2024 |
| Email | `.name .email` | IBM Plex Mono 15px / 400 | #6b7280 |
| Body | `body` | 17px / 400 / 1.65 | #1f2024 |
| Pull-quote | `.hero-text .lead` | 19px / 600 / 1.65, letter-spacing -0.01em | #1f2024 |
| Section label | `.section-label` | IBM Plex Mono 13px / 500 / 1.25 uppercase, letter-spacing 0.12em | #6b7280 |
| Card title | `.card h3` | 17px / 600 / 1.25, letter-spacing -0.01em | #1f2024 |
| Pill | `.card .tag` | IBM Plex Mono 15px / 400 / 1.65 | #56018d |
| Link | `a` | inherits size, no underline | #56018d |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Photo | 12px | none | `0 1px 2px rgba(20, 20, 30, 0.04), 0 8px 24px rgba(20, 20, 30, 0.04)` |
| Research card | 12px | 1px #e7e7ea (hover #56018d) | none; hover the same two-layer shadow and translateY(-2px) |
| Pill | 999px | 1px #e7e7ea (hover #56018d) | none |
| Pull-quote | 0 | 3px solid #56018d left | none |
| Section label | 0 | 1px #e7e7ea bottom | none |

## Layout Metrics

- **Container**: `body { max-width: 820px; margin: 56px auto }` → x=310–1130 at 1440; no wrapper element.
- **Header**: margin-bottom 48px; social icons gap 18px, margin-top 15px.
- **Hero**: flex, gap 40px, align flex-start; photo column `flex: 0 0 200px`; margin-bottom 56px.
- **Paragraphs**: margin 0 0 16px; pull-quote margin 22px 0, padding-left 16px.
- **Research**: label 24px above the grid; grid `repeat(2, 1fr)` → 402px cards, gap 16px; card padding 20px 22px; title 14px above the pills; pills gap 8px, padding 4px 10px; section margin-bottom 56px.

| Breakpoint | Gutter | Body size | Name size | Grid change |
|---|---|---|---|---|
| >768px | auto margins (310px at 1440) | 17px | 32px | header row, side-by-side hero, 2-column cards |
| ≤768px | 20px | 16px | 32px | header stacks with 12px gap; hero becomes column-reverse (photo above text, 180px, centred) with 24px gap; cards one column |

## Components

- **Header block**: left stack of 32px/700 name, 16px/500 subtitle and 15px mono #6b7280 email (4px gaps); right a row of 23px icon glyphs in #1f2024 that turn #56018d on hover.
- **Pull-quote** (`.lead`): 19px/600 #1f2024, 3px #56018d left bar, 16px left padding, 22px vertical margins.
- **Research card** (`.card`): #ffffff, 1px #e7e7ea, 12px radius, padding 20px 22px; 17px/600 title 14px above a wrapping row of pills. Hover: translateY(-2px), border #56018d, shadow `0 1px 2px rgba(20, 20, 30, 0.04), 0 8px 24px rgba(20, 20, 30, 0.04)`, 0.18s ease.
- **Pill** (`.card .tag`): IBM Plex Mono 15px, #56018d on rgba(86, 1, 141, 0.08), 1px #e7e7ea border, 999px radius, padding 4px 10px; hover border #56018d.
- **Section label**: 13px mono uppercase #6b7280 with 0.12em tracking and a 1px #e7e7ea rule 12px below.
- **Link**: #56018d, no underline; hover underline offset 2px.
- **Job-market badge** (defined, not shown): inline-block, padding 9px 13px, 1px rgba(86, 1, 141, 0.18) border, 8px radius, #56018d 600 text on rgba(86, 1, 141, 0.08).

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Name, subtitle, email | yes | Inter bold name, mono email |
| Social icons | yes | three 23px glyphs at top right |
| Bio with pull-quote | yes | 17px text, 3px plum bar on the statement |
| Photo | yes | 200px, 12px radius, faint shadow |
| Research areas | yes | 2×2 cards with mono project pills |
| News | present but non-standard | the stylesheet defines a hairline news table with a 110px mono date column; the homepage does not render one |
| Publication list | absent from the source | projects are only pill links inside cards |
| Footer | absent from the source | page ends after the cards |

## Adapting to Other Content

- **News**: use the stylesheet's `.news` table (cells padding 12px 8px, 1px #e7e7ea bottom rules, 110px date column in IBM Plex Mono 14px/500 #6b7280, row hover rgba(86, 1, 141, 0.08)) under a 13px mono section label.
- **Publications**: add a section label and list rows in 17px Inter with the title as a #56018d link and venue in 15px IBM Plex Mono #6b7280; keep the 820px column.
- **More research areas**: keep the 2-column grid of 402px cards; add pills rather than paragraphs inside cards.
- **A results table**: reuse the news-table recipe; header cells in 13px mono uppercase #6b7280, best value 600 #56018d.
- **Job market or availability**: use the defined badge (rgba(86, 1, 141, 0.08) fill, 1px rgba(86, 1, 141, 0.18) border, 8px radius) above the bio.

## Do's and Don'ts

- Do keep one accent, plum #56018d, for links, pills, the quote bar and hover borders.
- Do pair Inter for prose with IBM Plex Mono for labels, emails and pills.
- Do set the single research statement as a pull-quote with the 3px plum bar.
- Do keep shadows at 4% opacity and only on the photo and hovered cards.
- Don't underline links at rest.
- Don't fill cards with color; they stay #ffffff on #fcfcfd.
- Don't widen the column past 820px.

## Surfaces

A #fcfcfd page with #ffffff cards bordered 1px #e7e7ea. The only tints are the 8% plum pill fills. Shadows are near invisible (4%).

## Imagery

One 200px square casual photo (holding an ice cream cone) with a 12px radius and soft shadow. Icons are monochrome SVG glyphs. No paper figures.

## Layout

An 820px single column: header row, a two-column hero (580px text + 200px photo, 40px gap), a labelled 2×2 card grid. The page fits roughly in one and a quarter screens.

## Agent Prompt Guide

Quick colors: page #fcfcfd, card #ffffff, ink #1f2024, muted #6b7280, accent #56018d, wash rgba(86, 1, 141, 0.08), border #e7e7ea.

1. "Set body max-width 820px, margin 56px auto, Inter 17px/1.65 #1f2024 on #fcfcfd. Header: flex space-between; left the name 32px/700 letter-spacing -0.02em, a 16px/500 subtitle, and an IBM Plex Mono 15px #6b7280 email (4px gaps); right three 23px icons 18px apart in #1f2024, hover #56018d. 48px below."
2. "Build a hero: flex with 40px gap; text column with #56018d unlined links and a pull-quote paragraph (19px/600, 3px solid #56018d left border, padding-left 16px, margin 22px 0); a 200px photo with 12px radius and box-shadow 0 1px 2px rgba(20,20,30,.04), 0 8px 24px rgba(20,20,30,.04)."
3. "Create a research grid: a label in IBM Plex Mono 13px/500 uppercase, letter-spacing .12em, #6b7280, with padding-bottom 12px and a 1px #e7e7ea bottom border, 24px above a 2-column grid (gap 16px) of #ffffff cards (1px #e7e7ea, radius 12px, padding 20px 22px). Each card: 17px/600 title, 14px gap, pills in IBM Plex Mono 15px #56018d on rgba(86,1,141,.08) with a 1px #e7e7ea border, radius 999px, padding 4px 10px. Card hover: translateY(-2px) and border #56018d."

## Similar Pages

- Minimal hand-written PhD homepages in Inter with a single saturated accent and mono labels.
- Pages that summarize research areas as small cards of project-name pills instead of a publication list.

## Quick Start

```css
:root {
  --bg: #fcfcfd;
  --surface: #ffffff;
  --text: #1f2024;
  --muted: #6b7280;
  --accent: #56018d;
  --accent-soft: rgba(86, 1, 141, 0.08);
  --border: #e7e7ea;
  --shadow: 0 1px 2px rgba(20, 20, 30, 0.04), 0 8px 24px rgba(20, 20, 30, 0.04);
  --sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, monospace;
}
body { margin: 56px auto; max-width: 820px; font: 400 17px/1.65 var(--sans); color: var(--text); background: var(--bg); }
a { color: var(--accent); text-decoration: none; }
.lead { font-size: 19px; font-weight: 600; border-left: 3px solid var(--accent); padding-left: 16px; margin: 22px 0; }
```

## Provenance

- **URL**: https://michahu.github.io/
- **Person**: Michael Y. Hu (PhD, NYU Center for Data Science; MTS at Principia); field: language model pretraining, formal languages.
- **Venue / award**: ACL 2025 Outstanding Paper, first author of "Between Circuits and Chomsky: Pre-pretraining on Formal Languages Imparts Linguistic Biases".
- **Selection reason**: Rule A; award listed at https://2025.aclweb.org/program/awards/ ; homepage from the Semantic Scholar homepage field.
- **Template credit**: none stated; hand-written `index.html` and `style.css`.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, and `style.css` and `index.html` read directly, on 2026-10-28.
