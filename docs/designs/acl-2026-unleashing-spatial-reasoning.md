# Newsreader Paper Plate — Style Reference

> A cream editorial broadsheet with a drafting-grid hero, pill controls and figures mounted on white plates.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the sticky header, hero, buttons, figure plate, section heads, results table, YAML pane and footer, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the page's own `styles.css` and `script.js`. Positions are document coordinates at 1440px wide. Sections below the hero use a scroll-reveal (`.js .reveal`, opacity 0 until intersected), so the full-page capture shows them faded; values below come from the CSS and computed styles, not from the faded pixels.

## Overview

TRACE is a hand-built, art-directed page on a warm cream paper (#f7f4ee). A translucent sticky header carries a serif wordmark, pill-shaped text navigation and a black "Paper ↗" pill. The hero is centered: a white pill venue badge with a pink dot and a pink "ORAL", a 61.6px Newsreader title at weight 500 with tight tracking, an italic serif expansion of the acronym with bold capitals, sans authors, affiliation logos, and a row of 44px pill buttons (one black primary, four white). Behind it a faint 96px/24px drafting grid fades out radially. The teaser is a 1240px white plate with a 22px radius and a soft long shadow. Sections open with a mono-numbered uppercase kicker ("01 ABSTRACT") and a 50.4px serif heading; the abstract splits into a large serif TL;DR (with a yellow "TL;DR" tag) beside a justified serif abstract, and a four-column stat row sets 52.8px serif numerals. Later sections add a deeper paper band, white cards, an interactive results table with chips, and one near-black section with blue and pink glows.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): paper #f7f4ee 54.8%, paper #f6f3ed 20.4% (paper under the hero grid lines), warm grey #9e9a95 9.8% (title and text anti-aliasing, grid), off-white #fbf9f4 9.7% (header glass and badge), pale yellow #fbf4e5 2.3% (the teaser's yellow panel), remainder under 2%. Ink (#1b1916) appears as type and the two black pills.

Anatomy in DOM order (y = top of element box):

1. **Sticky header** (`header.site-header`), y 0, 1440×61, background rgba(247,244,238,0.86) with `backdrop-filter: saturate(1.5) blur(14px)`; bottom border transparent until scrolled, then rgba(27,25,22,0.1).
2. **Wordmark** (`a.brand`), x 130, y 15: a 26px square black logo mark and "TRACE" in Newsreader 17.92px/600, letter-spacing 0.16em, #1b1916.
3. **Nav** (`nav.site-nav`), right-aligned, six links Inter 14.4px/500 #6a635a, padding 6.72px 12px, pill radius; then **header CTA** `a.header-cta` "Paper ↗", 13.76px/500 #f7f4ee on #1b1916, padding 7.2px 12.8px 7.2px 15.2px, radius 999px. Gap to hero content 88px (hero top padding).
4. **Venue badge** (`a.venue`), y 149, 330×30, centered: "● ACL 2026 · MAIN CONFERENCE · ORAL", Inter 11.52px/600 uppercase, letter-spacing 0.13em, #3a3530, "ORAL" and the 7px dot in #d65a6a (dot ringed by a 3px #fbe8ea halo), background rgba(255,255,255,0.72), 1px rgba(27,25,22,0.17) border, radius 999px. Gap 24px.
5. **Title** (`h1.title`), y 203, max-width 1080px, four lines, Newsreader 61.6px/500, line-height 65.3px (1.06), letter-spacing -1.36px (-0.022em), #1b1916, centered, `text-wrap: balance`. Gap 18px.
6. **Acronym line** (`p.acronym`), y 482, Newsreader italic 20.48px/400, #6a635a, with the initial capitals upright bold (650) #1b1916. Gap about 30px.
7. **Authors** (`ul.authors`), y 546, flex-wrap centered, gap 4.8px 21.6px, Inter 16.64px/500 #1b1916, superscripts 0.66em #6a635a; hover draws a 1px underline left to right. Gap about 20px.
8. **Affiliations** (`ul.affiliations`), y 589, logos 19–30px tall beside Inter 14.4px #3a3530 names, items 30.4px apart. Gap 11px.
9. **Corresponding note** (`p.corresponding`), y 630, Inter 12.8px #6a635a. Gap 30px.
10. **Buttons** (`nav.actions`), y 681, five 44px pills 9.6px apart: "Paper" primary (#1b1916 fill, #f7f4ee text), then "arXiv", "PDF", "Prompt", "BibTeX" white with 1px rgba(27,25,22,0.17) border; 18px line icons on the left. Gap 60px.
11. **Teaser plate** (`figure.plate.plate-hero`), y 785, x 100, 1240×737, white, 1px rgba(27,25,22,0.1) border, radius 22px, padding 21.6px, shadow `0 1px 2px rgba(45,34,20,.05), 0 18px 40px -18px rgba(45,34,20,.22)`; image inside with 10px radius. The fold cuts it.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #f7f4ee | `--paper` | Page background, header glass base, text on black pills |
| Paper Deep | #f0ebe2 | `--paper-deep` | `.section-band` background (Analysis section) |
| White | #ffffff | `--white` | Figure plates, secondary buttons, cards, table wrapper, BibTeX card, YAML pane |
| Sheet | #fbfaf7 | `.rt thead th`, `.code-bar-light` | Results table header row, code tab bar |
| Ink | #1b1916 | `--ink` | Title, headings, authors, primary pill fill, header CTA, wordmark, active layer tab |
| Ink 2 | #3a3530 | `--ink-2` | Venue badge text, affiliations, abstract body, lead paragraphs, table body text |
| Muted | #6a635a | `--muted` | Nav links, acronym line, kickers, captions, stat labels, footer |
| Faint | #8e867b | `--faint` | "/5" suffix in stat numerals |
| Line | rgba(27,25,22,0.1) | `--line` | Plate and card borders, table rules, stat dividers, footer top rule |
| Line Strong | rgba(27,25,22,0.17) | `--line-strong` | Button and badge borders, kicker number box, stat-row top rule |
| Meta Pink | #d65a6a | `--meta` | Venue dot and "ORAL", meta-context color in diagrams and YAML |
| Meta Soft | #fbe8ea | `--meta-soft` | Halo around the venue dot |
| Trajectory Blue | #3a78d4 | `--traj` | Trajectory color in diagrams, focus outline, glow in the dark section |
| Entity Green | #1f9373 | `--ent` | Entity color in diagrams and YAML |
| Highlight | #fdf5e0 | `--hl` | "Ours" rows in results tables |
| Highlight Strong | #f7e3b0 | `--hl-strong` | TL;DR tag background, delta chips in tables |
| Highlight Ink | #765012 | `--hl-ink` | TL;DR tag text, delta chip text, "ours" note |
| Ink Section | #171512 | `.section-ink` | "Use TRACE" section background (with 16% blue and 13% pink radial glows) |
| Ink Section Text | #e9e3d8 | `.section-ink` | Body text in the dark section; heading there #fbf8f2, lead #cbc3b6 |
| Ink Section Kicker | #a59c8f | `.section-ink .kicker` | Kicker text in the dark section |

## Tokens — Typography

- **Display and reading serif**: declared `"Newsreader", "Iowan Old Style", "Palatino Linotype", Georgia, serif`, self-hosted variable woff2 (200–800, roman and italic) with optical sizing set per role (`opsz` 72 for the title, 60 for h2, 48 for the TL;DR, 16 for the abstract). Rendered: Newsreader 200–800 and italic (`fonts_loaded`). Substitute: Source Serif 4 (also an optical-size variable serif with similar x-height).
- **UI sans**: declared `"Inter", ui-sans-serif, -apple-system, …, Arial, sans-serif`, self-hosted variable (100–900). Rendered: Inter. Used for body, nav, buttons, authors, kickers, tables.
- **Mono**: `"JetBrains Mono"` (400–800 loaded) for kicker numbers, YAML panes and BibTeX.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Paper title | `h1.title` | 61.6px / 1.06, -0.022em | 500 | #1b1916 |
| Stat numeral | `.stat-value` | 52.8px / 1, -0.025em, lining tabular | 500 serif | #1b1916 |
| Section heading | `h2` | 50.4px / 1.07, -0.02em | 500 serif | #1b1916 |
| TL;DR | `.tldr` | 28.8px / 1.3 | 400 serif | #1b1916 |
| Card heading | `.card h3` | 25.6px / 1.18 | 500 serif | #1b1916 |
| Sub-heading | `h3` (`.explorer-title`, `.anatomy-title`) | 23.2px | 500 serif | #1b1916 |
| Acronym | `.acronym` | 20.48px / 1.45 | 400 italic serif | #6a635a |
| Abstract body | `.abstract-body p` | 19.2px / 1.72, justified | 400 serif | #3a3530 |
| Lead | `.lead` | 18.24px / 1.68 | 400 | #3a3530 |
| Wordmark | `.brand` | 17.92px, 0.16em | 600 serif | #1b1916 |
| Authors | `.authors` | 16.64px | 500 | #1b1916 |
| Body | `body` | 16px / 1.65 | 400 | #1b1916 |
| Button | `.btn` | 15.04px | 500 | #1b1916 or #f7f4ee |
| Nav, table body | `.site-nav a`, `.rt` | 14.4px | 500 / 400 | #6a635a / #3a3530 |
| Caption, stat label | `.plate figcaption`, `.stat-label` | 14.4px / 1.6 | 400 | #6a635a |
| Footer | `.site-footer` | 13.76px | 400 | #6a635a |
| Kicker | `.kicker` | 11.84px, uppercase, 0.14em | 600 | #6a635a |
| Venue badge, TL;DR tag | `.venue`, `.tldr-label` | 11.52px, uppercase | 600 / 700 | #3a3530 / #765012 |
| Table header | `.rt thead th` | 11.52px, 0.03em (group rows uppercase 0.1em) | 600 | #6a635a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Venue badge, buttons, nav links, header CTA, layer tabs, chips | 999px | 1px rgba(27,25,22,0.17) (primary: #1b1916) | `--shadow-sm`: 0 1px 2px rgba(45,34,20,0.05), 0 3px 10px -4px rgba(45,34,20,0.08) |
| Figure plate, anatomy panel, BibTeX card, cards, gains chart | 22px (`--radius-lg`) | 1px rgba(27,25,22,0.1) | plates and BibTeX: `--shadow` 0 1px 2px rgba(45,34,20,0.05), 0 18px 40px -18px rgba(45,34,20,0.22); cards: `--shadow-sm` |
| Results table wrapper, pipeline nodes | 16px (`--radius`) | 1px rgba(27,25,22,0.1) / 0.17 | `--shadow-sm` |
| Image inside a plate | 10px (`--radius-sm`) | none | none |
| Kicker number box, TL;DR tag | 6px | 1px rgba(27,25,22,0.17) / none | none |

Hover on buttons, badge and CTA: `translateY(-1px)` and the larger `--shadow`; button border darkens to rgba(27,25,22,0.3). Plates show a "Click to enlarge" dark pill on hover and open a lightbox.

## Layout Metrics

- **Container**: `.container` width `min(1180px, 100% - 2 × gutter)` with gutter `clamp(1.1rem, 4vw, 2.5rem)` (40px at 1440), so content spans x 130–1310. `.container-wide` is 1240px (x 100–1340) for the hero plate.
- **Header**: 60px tall (`--header-h`), flex row, gap 20px; `scroll-padding-top` 76px for anchors.
- **Hero**: padding `clamp(3rem, 7vw, 5.5rem)` top (88px) and `clamp(3rem, 6vw, 4.5rem)` bottom (72px), centered column; title max-width 1080px; plate margin-top 60px.
- **Sections**: padding `clamp(4rem, 8vw, 7rem)` (112px) top and bottom; `.section-head` max-width 780px with 48px bottom margin; kicker 17.6px above the h2.
- **Abstract grid**: 5fr / 7fr columns, gap 80px (`clamp(2rem, 5vw, 5rem)`); stat row 4 equal columns, 64px above, 1px top rule, cells padded 24px with 1px left dividers.
- **Analysis**: cards on a 12-column grid, `span 6` each (two per row) or full width.
- **Results table**: horizontally scrollable wrapper, table min-width 860px (1180px for the second benchmark), sticky first column.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1081px | 40px | 16px | 61.6px | layout as described |
| 961–1080px | 40px | 16px | about 52–58px (fluid clamp) | pipeline columns rebalance |
| ≤1023px | 40px | 16px | fluid | abstract grid becomes one column |
| ≤960px | 38px at 960 | 16px | fluid | stats 2×2; prompt, citation, results split and cards to one column; pipeline vertical (max 520px) |
| ≤760px | 4vw (about 17.6–30px) | 16px | down to 34.4px minimum | header 56px, CTA hidden, wordmark text hidden, nav scrolls sideways with a fade mask; affiliations stack; buttons 42px |
| ≤420px | 17.6px | 16px | 34.4px | stats one column |

## Components

- **Venue pill badge**: inline-flex, gap 9.6px, padding 8px 15.2px 8px 12.8px, Inter 11.52px/600 uppercase 0.13em #3a3530, background rgba(255,255,255,0.72), 1px rgba(27,25,22,0.17) border, radius 999px, `--shadow-sm`; leading 7px #d65a6a dot with a 3px #fbe8ea ring; 3px dot separators at 35% opacity; highlight word in #d65a6a.
- **Pill button**: 44px tall, padding 0 18.4px 0 16px, gap 8px, Inter 15.04px/500, radius 999px, 18px stroked line icon (1.7px stroke) on the left. Secondary: #ffffff fill, #1b1916 text, 1px rgba(27,25,22,0.17) border. Primary: #1b1916 fill and border, #f7f4ee text. Hover lifts 1px and deepens the shadow.
- **Header CTA**: #1b1916 pill, 13.76px/500 #f7f4ee, 15px arrow icon on the right.
- **Nav link**: 14.4px/500 #6a635a, padding 6.72px 12px, pill; hover #1b1916 on rgba(27,25,22,0.05); active section rgba(27,25,22,0.075).
- **Figure plate**: white, 1px rgba(27,25,22,0.1) border, 22px radius, padding 21.6px, long soft shadow; image 10px radius; caption 14.4px #6a635a left-aligned with a bold #1b1916 "Figure 1" run-in.
- **Section kicker**: inline-flex row, Inter 11.84px/600 uppercase 0.14em #6a635a, with the section number in a JetBrains Mono box (padding 4.8px 7.2px, 1px rgba(27,25,22,0.17) border, 6px radius, #1b1916, no tracking).
- **TL;DR block**: a #f7e3b0 tag (Inter 11.52px/700, 0.08em, #765012, padding 4.5px 8px, 6px radius) above a 28.8px Newsreader paragraph with an italic phrase.
- **Stat row**: 4 columns under a 1px rgba(27,25,22,0.17) rule; each cell a 52.8px serif numeral (suffix "/5" at 0.55em in #8e867b) over a 14.4px #6a635a label; cells divided by 1px rgba(27,25,22,0.1).
- **Results table**: in a white 16px-radius scroll wrapper; header row #fbfaf7 with 11.52px/600 #6a635a labels; body 14.4px tabular #3a3530, center-aligned; 1px rgba(27,25,22,0.1) row rules; best values 700 #1b1916, second best underlined; "ours" row #fdf5e0 with a #f7e3b0 delta chip in #765012; segmented controls and chips above switch backbones.
- **Dark section**: #171512 with a blue glow top right and a pink glow bottom left; heading #fbf8f2, body #e9e3d8, kicker #a59c8f; code panes inside.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky header and nav | yes | translucent cream glass, pill links, black CTA |
| Venue badge | yes | white pill with pink dot and "ORAL" |
| Title, acronym, authors | yes | centered serif title, italic acronym, sans authors |
| Affiliation logos | yes | small logos inline with names |
| Link buttons | yes | five pill buttons, one black |
| Teaser figure | yes | white plate, 22px radius, lightbox |
| TL;DR and abstract | yes | 5/7 split, serif TL;DR, justified serif abstract |
| Stat row | yes | four large serif numerals with rules |
| Method pipeline | yes | five-step node row with arrows and one black key node |
| Interactive anatomy | yes | tabbed map and YAML pane, color-coded layers |
| Results chart and table | yes | dumbbell gain chart plus a filterable table |
| Analysis cards | yes | deeper paper band, white cards two per row |
| Prompt / code section | yes | near-black section with glows |
| BibTeX | yes | white card with tabbed light code bar |
| Footer | yes | 13.76px muted row above a hairline |
| Videos | absent from the source | none |

## Adapting to Other Content

- **More authors**: keep the centered flex-wrap list with 21.6px gaps; at more than about ten names, drop the logos into a separate centered row and keep superscript numbers.
- **A results table**: reuse `.rt` inside the white 16px-radius wrapper; highlight the proposed row with #fdf5e0, bold best values, underline seconds, and add #f7e3b0 delta chips.
- **Videos**: mount them in the same white plate (22px radius, 21.6px padding) with a 10px inner radius and a caption.
- **Long publication lists or news**: a white card list on paper, each item with an uppercase 11.84px #6a635a date kicker and a 25.6px serif title.
- **Fewer stats**: the stat row tolerates 2 or 3 columns; keep the top rule and the left dividers.
- **No dark section content**: omit `.section-ink` rather than inventing one; the band alternation (paper, deep paper) carries the rhythm.

## Do's and Don'ts

- Do pair Newsreader at weight 500 for display with Inter 500 for UI; keep display tracking negative.
- Do put every figure on a white plate with a 22px radius and the long soft shadow.
- Do keep controls as pills with thin warm-grey borders; reserve black fill for one primary action per row.
- Do use the three diagram colors (#d65a6a, #3a78d4, #1f9373) only to encode meta context, trajectory and entities.
- Don't use pure white as the page; the ground is #f7f4ee.
- Don't add hard shadows or dark borders; borders stay at 10–17% ink.
- Don't left-align the hero; only section content is left-aligned.

## Surfaces

Cream paper #f7f4ee is the base; the Analysis band drops to #f0ebe2; white #ffffff plates, cards and tables float on both with soft warm shadows; one near-black #171512 section with colored glows; table headers and code bars use #fbfaf7.

## Imagery

Paper figures with hand-styled panels (pink, lavender and yellow rounded boxes around egocentric video frames, a room map, YAML-like text), mounted as zoomable plates. Inline SVG diagrams draw a room map with a drafting grid, a camera trajectory and entity pins in the three code colors. Small university logos sit beside affiliations.

## Layout

A 1180px centered container with a centered hero and left-aligned sections. Sections alternate paper, deep-paper band and one dark band, each with a kicker, a large serif heading and a content grid (5/7 splits, 12-column cards, four-column stats). Rendered height is about 12,430px at 1440px.

## Agent Prompt Guide

Quick colors: paper #f7f4ee, deep paper #f0ebe2, white plates #ffffff, ink #1b1916, ink-2 #3a3530, muted #6a635a, accent pink #d65a6a, highlight #fdf5e0 / #f7e3b0 / #765012.

1. "Build a centered hero on #f7f4ee: a pill badge (Inter 11.52px/600 uppercase, 0.13em tracking, #3a3530, background rgba(255,255,255,0.72), 1px rgba(27,25,22,0.17) border, radius 999px) with a 7px #d65a6a dot and the word 'ORAL' in #d65a6a; 24px below, a Newsreader 61.6px weight-500 title with line-height 1.06 and -0.022em tracking in #1b1916; an italic 20.48px #6a635a acronym line; Inter 16.64px/500 authors."
2. "Add a row of 44px pill buttons 9.6px apart: the first #1b1916 with #f7f4ee text, the rest #ffffff with #1b1916 text and a 1px rgba(27,25,22,0.17) border; Inter 15.04px/500, an 18px line icon on the left, shadow 0 1px 2px rgba(45,34,20,0.05), 0 3px 10px -4px rgba(45,34,20,0.08); on hover lift 1px."
3. "Mount a figure on a white plate: 1px rgba(27,25,22,0.1) border, 22px radius, 21.6px padding, shadow 0 1px 2px rgba(45,34,20,0.05), 0 18px 40px -18px rgba(45,34,20,0.22); image with 10px radius; caption Inter 14.4px #6a635a with a bold #1b1916 'Figure 1' run-in."

## Similar Pages

- Editorial "magazine" project pages with a serif display face on warm paper and pill controls (for example hand-built pages in the style of Distill or Anthropic research posts).
- Pages that replace the Nerfies template with a custom design system and section kickers.

## Quick Start

```css
:root {
  --paper: #f7f4ee;
  --paper-deep: #f0ebe2;
  --white: #ffffff;
  --ink: #1b1916;
  --ink-2: #3a3530;
  --muted: #6a635a;
  --line: rgba(27, 25, 22, 0.1);
  --line-strong: rgba(27, 25, 22, 0.17);
  --meta: #d65a6a;
  --traj: #3a78d4;
  --ent: #1f9373;
  --hl: #fdf5e0;
  --hl-strong: #f7e3b0;
  --hl-ink: #765012;
  --serif: "Newsreader", "Iowan Old Style", Georgia, serif;
  --sans: "Inter", -apple-system, "Segoe UI", Arial, sans-serif;
  --mono: "JetBrains Mono", ui-monospace, Menlo, monospace;
  --radius: 16px;
  --radius-lg: 22px;
  --shadow-sm: 0 1px 2px rgba(45, 34, 20, 0.05), 0 3px 10px -4px rgba(45, 34, 20, 0.08);
  --shadow: 0 1px 2px rgba(45, 34, 20, 0.05), 0 18px 40px -18px rgba(45, 34, 20, 0.22);
  --container: 1180px;
}
```

## Provenance

- **URL**: https://trace-reasoning.github.io/
- **Paper**: Unleashing Spatial Reasoning in Multimodal Large Language Models via Textual Representation Guided Reasoning (TRACE; arXiv 2603.23404), Jiacheng Hua et al. (Tsinghua University, Shanghai AI Laboratory, The University of Tokyo).
- **Venue**: ACL 2026 Main Conference, oral (per the page's badge).
- **Selection reason**: arXiv 2603.23404 comment states acceptance at ACL 2026; project page linked in the comment. Chosen for its polished centered serif hero, pill venue badge, affiliation logos, refined buttons, large teaser plate, TL;DR and abstract split and big stat numerals.
- **Template credit**: none stated; custom stylesheet.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and first-viewport anatomy, first-viewport screenshot and scaled full-page capture (lower sections caught mid scroll-reveal), `styles.css`, `script.js` and `index.html`. Date 2026-10-28.
