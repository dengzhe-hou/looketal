# Raghunathan Palatino Tabs — Style Reference

> A light-weight Palatino reading room with colored venue tabs on the shelf.

**Theme:** light

Measurements come from the static HTML and its one stylesheet `style.css`, plus `nav.js` (tab switching) and `publications.js` (renders papers from `publications.json`). Google Fonts requests for Roboto and Inter are present, but no rule in `style.css` uses them, so they are treated as unused. All colors below appear in `style.css`. Roles are interpreted, not declared. The rendered page was not viewed.

## Overview

Aditi Raghunathan's CMU page is a two-pane, tabbed single page from the jQuery era, lightly refreshed. A fixed 300px left sidebar holds the 275px photo, the name at 30px weight 400 and a light subtitle (Assistant Professor, Computer Science Department, CMU). To the right, a topbar of 22px weight-300 tab labels (about, publications, honors, group, teaching, contact) in cobalt switches the visible `.maintext` panel; the selected tab gets a 1px raspberry underline `#ab425f`. The main text column is 650px of Palatino at weight 300. A newer `.highlight-card` (pale blue `#f0f4ff`, 4px `#0072c6` left border, 8px radius, soft shadow) announces the group website. Publications are generated client-side into a table-like list with a small colored tag cell per entry: conference cobalt `#0233d1`, journal red `#e6233d`, book chapter orange `#ff8c00`, thesis gold `#ffd700`, working paper slate `#606b70`. Award notes are raspberry `#D81159` bold.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Plain White | `#ffffff` (inferred) | `--bg` | Browser default background |
| Ink | `#000000` | `--text` | `.research-label` and body (default) |
| Cobalt Link | `rgb(0,71,171)` / `#0047ab` | `--link` | Links and tab labels |
| Sky Hover | `rgb(0,150,255)` / `#0096ff` | `--link-hover` | Link and tab hover |
| Raspberry Rule | `#ab425f` | `--tab-selected` | Selected tab underline |
| Award Raspberry | `#D81159` | `--award` | `.paper-award` text |
| Venue Cobalt | `#0233d1` | `--tag-conference` | Conference tag fill |
| Venue Red | `#e6233d` | `--tag-journal` | Journal tag fill |
| Venue Orange | `#ff8c00` | `--tag-chapter` | Book chapter tag fill |
| Venue Gold | `#ffd700` | `--tag-thesis` | Thesis tag fill |
| Venue Slate | `#606b70` | `--tag-working` | Working paper tag fill |
| Year Teal | `#41ab8d` | `--year` | Education / group list year chips |
| Card Ice | `#f0f4ff` | `--card` | Highlight card background |
| Card Edge | `#0072c6` | `--card-edge` | Highlight card 4px left border |

## Tokens — Typography

- **Family:** `'Palatino Linotype', Palatino, Arial, serif`. Substitute: `TeX Gyre Pagella`, `URW Palladio`, or `EB Garamond`.
- **Loaded, unused:** Roboto (300 to 500), Inter (300 to 800).
- **Weights:** 300 is the reading weight (`.maintext`, subtitle, tabs, content); 400 for name, h2/h3 and bold text; 500 for paper titles in lists; 700 for award notes and `.paper-title`.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Name `.name` | 30px | 400 | Sidebar |
| Section h1 in main | 28px | 300 | "Publications", "PhD advisees" |
| Tab label | 22px | 300 | Cobalt, 50px apart |
| Paper title `.paper-title` | 1.1rem | 700 | |
| Venue tag | 14px | 400 | White on color, 65px wide, 18px line-height |
| Body `.maintext` | browser default 16px (inferred) | 300 | 650px column |
| Highlight card text | inherit | 300 | line-height 1.5 |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Highlight card | 8px |
| Venue tags, year chips, photo | 0 |

- **Shadows:** highlight card only, `0 4px 14px rgba(0,0,0,0.06)`.
- **Layout:** sidebar 300px float with padding `15px 15px 0 30px`; topbar 90px tall offset 300px; main text `margin-left: 300px; padding-left: 50px; width: 650px`; research list items max 800px.
- **List spacing:** publication items 20px apart, list block 30px bottom margin; tables use `border-spacing: 6px`.

## Components

- **Sidebar.** Photo (`width="275px"`, 30px top padding), name, light subtitle lines.
- **Tab bar.** Floating `li` items, 22px/300 cobalt; hover sky blue; selected item gets `border-bottom: 1px solid #ab425f`.
- **Highlight card.** Display block, padding `18px 20px`, `#f0f4ff`, 4px `#0072c6` left border, 8px radius, 18px vertical margin; links at weight 500.
- **Venue tag cell.** 50px-wide cell holding a 65x18px white label on the venue color, 5px padding, centered.
- **Paper entry.** Title weight 500 (or `.paper-title` 700 at 1.1rem), authors and venue at weight 300, optional raspberry award line.
- **Year chip.** `#41ab8d` block, white 400 text, 40px wide, 10px padding.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Bio / photo | Yes | Left sidebar, photo plus name |
| Research focus | Yes | Prose with a bold `.research-label` lead-in |
| Announcement | Yes | Highlight card linking the group site |
| Publication list | Yes, rendered from JSON (preprints and publications) | Colored venue tags, no thumbnails |
| Group / advisees / alumni | Yes | Plain lists under h1 headings |
| Honors | Yes ("Selected honors") | List |
| Teaching | Yes | Semester-bold list |
| Contact | Yes | E-mail and office |
| News | No | |

## Do's and Don'ts

- Do read in Palatino at weight 300 and keep headings at 300 to 400.
- Do switch content with tabs instead of a long scroll.
- Do color-code venue type with small square tags, one hue per type.
- Don't round the venue tags; only the announcement card is rounded.
- Don't introduce Inter or Roboto into the body just because they are loaded.

## Surfaces

White page; the only tinted surface is the ice-blue highlight card. Venue tags and year chips are small saturated blocks.

## Imagery

One portrait in the sidebar. No paper thumbnails or figures.

## Layout

Fixed two-pane desktop layout: 300px floated sidebar, tab bar and a 650px main column offset by 350px. No responsive rules in `style.css`, so small screens scroll horizontally (inferred).

## Agent Prompt Guide

**Quick colors:** text `#000000`, link `#0047ab`, hover `#0096ff`, tab rule `#ab425f`, award `#D81159`, conference `#0233d1`, journal `#e6233d`, card `#f0f4ff` with edge `#0072c6`.

1. "Make a tab bar of 22px Palatino weight-300 labels in `#0047ab`, 50px apart, hover `#0096ff`, the selected tab underlined with 1px `#ab425f`."
2. "Render a publication row: a 65x18px square tag (white 14px text on `#0233d1` for conference, `#e6233d` for journal), then a weight-500 title and weight-300 authors."
3. "Add an announcement card: `#f0f4ff`, 4px solid `#0072c6` left border, 8px radius, padding 18px 20px, shadow `0 4px 14px rgba(0,0,0,.06)`."

## Similar Pages

The jQuery tabbed faculty template seen on several Stanford-lineage ML pages (sidebar photo plus topbar tabs). The Jake Snell page in this batch uses the same venue-color tag idea in Bulma.

## Quick Start

```css
:root {
  --text: #000;
  --link: rgb(0,71,171);
  --link-hover: rgb(0,150,255);
  --tab-selected: #ab425f;
  --award: #D81159;
  --tag-conference: #0233d1;
  --tag-journal: #e6233d;
  --tag-chapter: #ff8c00;
  --tag-thesis: #ffd700;
  --tag-working: #606b70;
  --year: #41ab8d;
  --card: #f0f4ff;
  --card-edge: #0072c6;
  --font: 'Palatino Linotype', Palatino, serif;
  --sidebar: 300px;
  --main: 650px;
}
```

## Provenance

- **URL:** https://www.cs.cmu.edu/~aditirag/
- **Person:** Aditi Raghunathan, ML robustness and reliability
- **Venue / award:** ICML 2025 Outstanding Paper (Roll the dice & look before you leap, last author)
- **Selection reason:** Rule B, last author of an ICML 2025 Outstanding Paper (https://icml.cc/virtual/2025/awards_detail).
- **Template credit:** none credited; hand-written HTML with `style.css`, `nav.js` and `publications.js`, jQuery 3.1.0.
- **Measurement method:** `extract_style.py` on HTML plus `style.css`; the stylesheet was then read in full. Publications are injected by JavaScript from `publications.json`, so their rendered markup was inferred from `publications.js` and the CSS classes. The rendered page was not viewed.
