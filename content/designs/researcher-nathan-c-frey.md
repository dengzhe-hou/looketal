# Parchment Ledger — Style Reference

> A private press colophon: one serif, espresso ink on parchment, and a column of sienna links ruled like a ledger.

**Theme:** both

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, color share), the 1440×900 and full-page screenshots, and the page's single `styles.css` and markup read directly. No web fonts are loaded (`fonts_loaded` is empty), so the Charter-first stack falls through to Georgia on the capture machine. The root font size is 17px, so every rem value below is multiplied by 17. The page also ships a dark palette (prefers-color-scheme plus a "Shade" toggle); the render is the light one.

## Overview

A single 640px column centred on a warm parchment ground #f6efe2, set entirely in one serif at 17px with a 1.6 line height. The name is a 29.75px weight-500 heading in dark espresso #2a1f17 with a taupe #786450 "New York, NY" line beneath. Three bio paragraphs follow, then four short sections whose labels (WRITING, RESEARCH, ELSEWHERE, GET IN TOUCH) are 13.26px italic uppercase with wide tracking in taupe. Writing and research entries are flex rows: a burnt-sienna #9a4520 underlined link on the left and an italic taupe date or venue on the right, separated by 1px tan #e3d5be rules. A lone italic "Shade" button sits in the top-right corner. There are no images, icons, cards or colour fills beyond the ground.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): parchment #f6efe2 81.7% plus near-identical tones #f8f2e4 3.7%, #f6efe1 2.3%, #f6efe3 1.7%; anti-aliased text greys #b8aa9d 5.9% and #eae1d3 4.1%. The text column is narrow, so ink never forms a large cluster.

Anatomy in DOM order (desktop 1440px; `body` 640px max-width centred at x=400, padding 76.5px 25.5px 102px, text box 589px at x=426):

1. **Theme toggle** (`button#theme-toggle`, absolute, y=26, right edge 1015): "Shade", 15.3px italic 400, #786450, no background or border. Gap to the name 24px.
2. **Name** (`header h1`, y=77): 29.75px / 500 / 47.6px, letter-spacing -0.30px, #2a1f17, left. Gap 3px.
3. **Location** (`p.subtitle`, y=128): 17px / 400, #786450. Gap 42.5px (header margin-bottom).
4. **Bio paragraphs** (`section.bio p`, y=198, 297, 477): 17px / 400 / 27.2px, #2a1f17, 17px apart; one inline link "write on the internet" in #9a4520. Gap 51px.
5. **WRITING label** (`h2`, y=664): 13.26px / 600 italic, uppercase, letter-spacing 1.19px, #786450. Gap 17px.
6. **Entry rows** (`ul.entries li`, first at y=702): link 17px #9a4520 left; date 14.45px italic #786450 right, tabular numerals; rows padded 9.35px top and bottom with a 1px #e3d5be rule under each. The fourth row reaches the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Parchment | #f6efe2 | `--bg` | page background (`body`) |
| Espresso Ink | #2a1f17 | `--text` | name, bio paragraphs, plain text |
| Warm Taupe | #786450 | `--muted` | location line, section labels, dates and venues, "Shade" toggle |
| Burnt Sienna | #9a4520 | `--link` | all links, selection background, focus ring, toggle hover |
| Soft Tan | #e3d5be | `--rule` | 1px rules between list entries |
| Sienna Underline | rgba(154,69,32,0.5) | `color-mix(--link 50%)` | resting link underline |
| Dark Cocoa | #1a1510 | `--bg` (dark) | background in dark mode (toggle or OS setting) |
| Cream | #ebdfc9 | `--text` (dark) | body text in dark mode |
| Grey-taupe | #a08d75 | `--muted` (dark) | labels and dates in dark mode |
| Terracotta | #d68963 | `--link` (dark) | links in dark mode |
| Dark Tan | #2f261c | `--rule` (dark) | entry rules in dark mode |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Serif (everything) | "Charter", "Iowan Old Style", "Apple Garamond", Georgia, "Times New Roman", serif | none loaded; Georgia (system) on Windows, Charter on macOS | Charis SIL (Charter metrics) |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Base | `html` 17px, `body` | 17px / 400 / 1.6 (27.2px), kern + liga | #2a1f17 |
| Name | `h1` | 1.75rem = 29.75px / 500 / 47.6px, letter-spacing -0.01em | #2a1f17 |
| Location | `.subtitle` | 17px / 400 | #786450 |
| Section label | `h2` | 0.78rem = 13.26px / 600 / italic / uppercase, letter-spacing 0.09em (1.19px) | #786450 |
| Entry link | `ul.entries a` | 17px / 400, underline 1px, offset 2px | #9a4520 |
| Date / venue | `ul.entries .date` | 0.85rem = 14.45px / 400 / italic, tabular-nums, nowrap | #786450 |
| "More on Substack →" | `p.more` | 0.95rem = 16.15px | #9a4520 |
| Toggle | `#theme-toggle` | 0.9rem = 15.3px / 400 / italic, letter-spacing 0.01em | #786450 |

Georgia's old-style numerals give the dates ("Dec 2025") their book-like look in the render.

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Entry rows | 0 | 1px solid #e3d5be bottom (none on last) | none |
| Links | 0 | underline 1px rgba(154,69,32,0.5), 2px on hover in #9a4520 | none |
| Focus ring | 2px | 2px solid #9a4520, offset 3px | none |
| Toggle | 0 | none | none |

There are no boxes, cards, images or radii anywhere apart from the focus ring.

## Layout Metrics

- **Column**: `body { max-width: 640px; margin: 0 auto; padding: 4.5rem 1.5rem 6rem }` = 76.5px 25.5px 102px; text measure 589px.
- **Header**: name and location stacked, margin-bottom 2.5rem (42.5px).
- **Paragraphs**: margin 0 0 1rem (17px).
- **Section rhythm**: `h2` margin 3rem 0 1rem (51px above, 17px below); first section's label has no top margin.
- **Entry rows**: flex, `justify-content: space-between`, `align-items: baseline`, gap 1.25rem (21.25px), padding 0.55rem (9.35px) 0.
- **Elsewhere links**: flex wrap, column gap 1.5rem (25.5px).
- **Page height**: 1,816px at 1440 wide; the lower half of the full-page capture is empty parchment.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >520px | 25.5px inside a 640px column | 17px | 29.75px | entry rows are title-left, date-right |
| ≤520px | 20px (1.25rem at 16px root) | 16px | 28px | entry rows stack; date 12.48px under the title; body padding 48px 20px 64px |

## Components

- **Entry row**: `<li>` flex row; left a #9a4520 17px link with a half-opacity 1px underline 2px below the baseline; right an italic 14.45px #786450 date or "Venue · Year" (for example "ICLR 2024 · Outstanding Paper"); 9.35px vertical padding and a 1px #e3d5be bottom rule; hover thickens the underline to 2px and makes it solid #9a4520.
- **Section label**: italic uppercase 13.26px weight 600 in #786450 with 0.09em tracking, 51px above and 17px below.
- **Theme toggle**: text-only italic "Shade" (reads "Light" in dark mode), 15.3px #786450, absolute 24px from the top and right of the column; hover turns it #9a4520 over 120ms.
- **Inline link**: same sienna underline treatment inside paragraphs.
- **Elsewhere row**: five links (Substack, Twitter, GitHub, LinkedIn, ORCID) in a wrapping flex row, 25.5px apart.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Name and location | yes | 29.75px serif name, taupe location line |
| Portrait | absent from the source | no image anywhere |
| Bio | yes | three 17px paragraphs |
| Navigation bar | absent from the source | only the theme toggle |
| Writing list | yes | ruled entry rows with italic dates and a "More on Substack →" link |
| Publications | present but non-standard | five selected papers as entry rows, venue in the date slot, no authors or thumbnails |
| Awards | present but non-standard | written into the venue slot ("ICLR 2024 · Outstanding Paper") |
| Social links | yes | plain text link row under ELSEWHERE |
| Contact | yes | mailto link in a sentence |
| Footer | absent from the source | page ends after GET IN TOUCH |
| Dark mode | yes | full alternate palette via `[data-theme]` and media query |

## Adapting to Other Content

- **Long publication lists**: keep entry rows; add authors as a second line in 14.45px #786450 roman under the link, and keep the venue on the right. Group by year with another italic uppercase label rather than headings in a new style.
- **News**: an entry row with the item text on the left (plain #2a1f17, links inline) and the italic date on the right.
- **Portrait**: if one is needed, a small square (about 96px) to the left of the name with no radius and no shadow; do not widen the column.
- **Awards**: keep them in the right-hand italic slot or as a section with the same rows; no badges or colour.
- **Talks or teaching**: same rows, venue or term on the right.

## Do's and Don'ts

- Do keep one serif family at a 17px root and the 640px column.
- Do keep links sienna #9a4520 with the half-opacity underline; they are the only colour.
- Do right-align dates in italic taupe with tabular numerals.
- Don't add cards, shadows, icons or images; rules and type do all the structure.
- Don't bold body text; weight 500 appears only on the name and 600 on labels.
- Don't use pure white or black; the palette is parchment and espresso.

## Surfaces

One surface: parchment #f6efe2 edge to edge (dark mode swaps it for #1a1510). Separation comes only from 1px #e3d5be rules and whitespace.

## Imagery

None. The page is pure typography; no portrait, logos or figures.

## Layout

Top-right theme toggle; name and location; bio (three paragraphs); Writing (five rows plus a Substack link); Research (one sentence plus five rows); Elsewhere (link row); Get in touch (email sentence). About 1,816px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: background #f6efe2, text #2a1f17, muted #786450, links #9a4520, rules #e3d5be. Dark mode: #1a1510 / #ebdfc9 / #a08d75 / #d68963 / #2f261c.

1. "Set a single 640px centred column on #f6efe2 with padding 76.5px 25.5px 102px; root font 17px Charter, Georgia fallback, line-height 1.6, color #2a1f17. Name h1 29.75px weight 500, letter-spacing -0.01em; under it a 17px #786450 location line; 42.5px gap before the bio."
2. "Make section labels: italic uppercase 13.26px weight 600, letter-spacing 0.09em, color #786450, 51px above and 17px below. Under each, a list of flex rows (space-between, baseline aligned, 21.25px gap, 9.35px vertical padding, 1px #e3d5be bottom rule except the last): left a 17px #9a4520 link with a 1px half-transparent underline offset 2px; right a 14.45px italic #786450 date with tabular numerals."
3. "Add a text-only theme toggle reading 'Shade' at the top-right of the column, 15.3px italic #786450, no border or background, turning #9a4520 on hover; dark mode swaps the variables to #1a1510 background, #ebdfc9 text, #a08d75 muted, #d68963 links, #2f261c rules."

## Similar Pages

- Gwern-style or Tufte-inspired single-column serif homepages with ruled lists.
- Plain academic pages that put venue and year in a right-aligned italic column.

## Quick Start

```css
:root {
  --text: #2a1f17;
  --muted: #786450;
  --bg: #f6efe2;
  --link: #9a4520;
  --rule: #e3d5be;
}
:root[data-theme="dark"] {
  --text: #ebdfc9; --muted: #a08d75; --bg: #1a1510; --link: #d68963; --rule: #2f261c;
}
html { font-size: 17px; }
body { max-width: 640px; margin: 0 auto; padding: 4.5rem 1.5rem 6rem; color: var(--text); background: var(--bg);
  font-family: "Charter", "Iowan Old Style", Georgia, serif; line-height: 1.6; }
h1 { font-size: 1.75rem; font-weight: 500; letter-spacing: -0.01em; margin: 0 0 0.25rem; }
h2 { font-size: 0.78rem; font-weight: 600; font-style: italic; text-transform: uppercase; letter-spacing: 0.09em; color: var(--muted); margin: 3rem 0 1rem; }
a { color: var(--link); text-decoration-thickness: 1px; text-underline-offset: 2px;
  text-decoration-color: color-mix(in srgb, var(--link) 50%, transparent); }
ul.entries li { display: flex; justify-content: space-between; align-items: baseline; gap: 1.25rem; padding: 0.55rem 0; border-bottom: 1px solid var(--rule); }
.date { color: var(--muted); font-size: 0.85rem; font-style: italic; font-variant-numeric: tabular-nums; white-space: nowrap; }
```

## Provenance

- **URL**: https://ncfrey.com/
- **Person**: Nathan C. Frey, generative models for protein design.
- **Award**: ICLR 2024 Outstanding Paper, "Protein Discovery with Discrete Walk-Jump Sampling" (first author). https://blog.iclr.cc/2024/05/06/iclr-2024-outstanding-paper-awards/
- **Selection reason**: award rule (first or last author); chosen as a restrained typographic page on a cream ground with italic uppercase labels and right-aligned dates.
- **Template credit**: none stated; hand-written HTML with one `styles.css`.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, empty fonts_loaded, color share), the 1440×900 and full-page screenshots, and `styles.css` and the HTML read directly, on 2026-10-28.
