# Celadon Serif — Style Reference

> A quiet gallery wall in pale celadon: one big Georgia name, small green eyebrows, and paper thumbnails hung at even intervals.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, the page's single stylesheet `/style.css` and `index.html`, and probes of rendered elements. The stylesheet also defines a dark palette, used when the visitor's system prefers dark or the ◐ button sets `data-theme="dark"`; the render and this file describe the light theme, with dark values listed separately.

## Overview

A hand-written static homepage, about 5,580px tall at 1440. The ground is an off-white with a faint green cast (#fafaf7), text is a green-black #202b29 and the one accent is a muted jade #1a6553 used for links, the 11px uppercase eyebrows ("UPDATES", "RESEARCH") and the 2px underline of the current nav item. The name "Kai Chen" is set huge in Georgia 76px regular with tight tracking; section titles ("Latest news", "Selected publications") are Georgia 32px. Everything else is the sans stack (Inter first, but no web font is loaded, so Segoe UI renders on Windows). Layout is a 980px column: a two-column intro (bio left, a 250px square portrait right), then sections opened by a 1px #dce2dc rule, an eyebrow, a serif title and a right-aligned "All news ↗" link. Publications are rows of a 148×98px white-framed thumbnail beside a title, authors, italic venue, small uppercase outlined link tags and a BibTeX disclosure.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): off-white family #fafaf7 / #fdfcf9 / #fbfaf5 / #fbfaf7 / #f9faf8 / #fafaf8 together 88.4%; gray #939194 6.7% (the portrait's gray backdrop and suit plus antialiased text); light green-gray #e3e6e2 5.0% (header rule, section rule and the photo edges blended). The jade accent covers too little area to form a cluster.

Anatomy in DOM order (`.header-inner` and `.container` max-width 1060px with 40px side padding, so content runs x=230–1210):

1. **Header** (`header.site-header`, 0–93px): #fafaf7, 92px tall, 1px #dce2dc bottom border, static (not sticky). Wordmark "Kai Chen" 21px/650, letter-spacing -0.04em, #202b29, then "（陈恺）" at 0.85em (17.85px) weight 500 in #202b29 with 4px left margin. Right: nav About, Publications, Projects, News at 14px #606f69, 27px gap, padding 10px 0; the current item is #202b29 with `box-shadow: 0 2px #1a6553`. Then a 35px round ◐ toggle with a 1px #dce2dc border, 28px after the nav.
2. **Container** padding-top 65px.
3. **Name** (`.intro h1`, y=158, 93px tall): Georgia 76px/400, line-height 1.22, letter-spacing -0.035em (-2.66px), #202b29. Gap 12px.
4. **Position** (`p.position-title`, y=263): 15px/400, line-height 1.6, #202b29. Gap 12px.
5. **Topic line** (`p.intro-line`, y=299): "Large language models / Vision-language models / Open-source AI", 13px, line-height 1.8, #606f69. Gap 28px.
6. **Bio** (y=350–562): two paragraphs at 15px, line-height 1.85, #202b29, 18px apart; links #1a6553 with a 1px underline offset 4px. Gap 26px.
7. **Contact links** (y=588): "Email ↗", "GitHub ↗", "Google Scholar ↗", 13px/550 #1a6553, no underline, 23px apart.
8. **Portrait** (right column x=960, y=168 after a 10px top margin): 250×250px square, object-fit cover, 3px radius, no border or shadow. Column gap 65px.
9. **Intro bottom padding** 65px, then the news section at y=675: 1px #dce2dc top rule, 38px padding, eyebrow "UPDATES" (y=714, 11px/650 uppercase, letter-spacing 0.15em, #1a6553), 9px gap, "Latest news" (Georgia 32px/400, letter-spacing -0.035em) with "All news ↗" (13px/550 #1a6553) bottom-aligned on the right; 28px below, the first news row at y=809.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Celadon Paper | #fafaf7 | --bg | page and header background |
| White | #ffffff | --surface | thumbnail frames, search input on the publications page, skip link |
| Green Ink | #202b29 | --ink | name, section titles, paper titles, body text, wordmark, current nav item, link tags |
| Sage Gray | #606f69 | --muted | nav links, topic line, news dates, author lines, italic venues, BibTeX summary, footer |
| Rule | #dce2dc | --line | header bottom border, section top rules, publication separators, thumbnail and tag borders, toggle border |
| Jade | #1a6553 | --accent | links, eyebrows, contact links, "All … ↗" links, current-nav underline, tag hover border, focus outline |
| Mint Wash | #edf2ed | --soft | BibTeX code background, tag and toggle hover fill |
| Dark Ground | #141c1a | --bg (dark) | page background in dark mode |
| Dark Ink | #e8eeea | --ink (dark) | text in dark mode |
| Dark Accent | #9acbb3 | --accent (dark) | links and eyebrows in dark mode |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Serif (name, h2) | Georgia, 'Times New Roman', serif | no web font; system Georgia | Georgia (or Gelasio) |
| Sans (everything else) | Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif | no web font loaded and Inter not installed, so Segoe UI renders on Windows (SF Pro on macOS) | Inter |
| Code | ui-monospace, SFMono-Regular, monospace | system mono | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `.intro h1` | Georgia 76px / 400 / 1.22, letter-spacing -0.035em | #202b29 |
| Section title | `.section-heading h2` | Georgia 32px / 400 / 1.22, letter-spacing -0.035em | #202b29 |
| Paper title | `.paper h3` | 18px / 600 / 1.22, letter-spacing -0.015em | #202b29 |
| Eyebrow | `.eyebrow` | 11px / 650 uppercase, letter-spacing 0.15em | #1a6553 |
| Wordmark | `.wordmark` | 21px / 650, letter-spacing -0.04em | #202b29 |
| Nav | `nav a` | 14px / 400 | #606f69 (current #202b29) |
| Body | `body` | 16px / 400 / 1.7 | #202b29 |
| Bio | `.bio p` | 15px / 400 / 1.85 | #202b29 |
| Position | `.position-title` | 15px / 400 / 1.6 | #202b29 |
| Topic line | `.intro-line` | 13px / 400 / 1.8 | #606f69 |
| Text link | `.text-link`, `.contact-links a` | 13px / 550 | #1a6553 |
| News date | `.news-list time` | 12px, tabular numerals | #606f69 |
| News text | `.news-list p` | 14px / 1.7 | #202b29 |
| Authors | `.authors` | 12px / 1.8; own name 600 #202b29 | #606f69 |
| Venue | `.venue` | 12px italic | #606f69 |
| Link tag | `.paper-link` | 10px uppercase, letter-spacing 0.05em | #202b29 |
| BibTeX summary | `.paper-details details` | 11px | #606f69 |
| Footer note | `.site-footer p` | 11px | #606f69 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Portrait | 3px | none | none |
| Paper thumbnail | 3px | 1px #dce2dc on #ffffff | none |
| Link tags | 3px | 1px #dce2dc (hover #1a6553) | none |
| BibTeX block (`pre`) | 4px | none, #edf2ed fill, padding 15px | none |
| Theme toggle | 50% | 1px #dce2dc | none |
| Current nav item | 0 | none | `box-shadow: 0 2px #1a6553` |
| Sections | 0 | 1px #dce2dc top | none |

## Layout Metrics

- **Container**: `.container, .header-inner, .site-footer { max-width: 1060px; margin: auto; padding: 0 40px }` → 980px content at x=230–1210.
- **Intro**: `.intro { grid-template-columns: minmax(0,1fr) 250px; gap: 65px; padding-bottom: 65px }` → 665px + 250px; container padding-top 65px.
- **Sections**: `border-top: 1px solid #dce2dc; padding-top: 38px; margin-bottom: 54px`; section heading flex with `align-items: flex-end`, margin-bottom 28px, eyebrow 9px above the h2.
- **News**: rows grid 95px + 1fr, gap 24px, padding 13px 0, no separators.
- **Publications**: rows grid 148px + 1fr, gap 26px, padding 27px 0, 1px #dce2dc bottom border (none on the last); thumbnail 148×98px, object-fit contain, 3px top margin; title 8px above authors; venue 11px above link tags (7px gaps); BibTeX disclosure 12px below.
- **Footer**: 1060px max with 40px padding, 1px #dce2dc top border, padding 30px top 35px bottom, flex space-between.

| Breakpoint | Gutter | Body size | Name size | Grid change |
|---|---|---|---|---|
| >760px | 40px | 16px (bio 15px) | 76px | two-column intro (250px portrait), 148px thumbnails |
| ≤760px | 24px | 16px (bio 14px) | 54px | header wraps with nav on its own full-width row (13px links); intro portrait column 135px; bio spans both columns; h2 27px; thumbnails 110×80px; paper h3 16px |
| ≤520px | 24px | 16px | 53px with 90px right padding | intro becomes block with an 80×80px portrait absolutely at top right; news date column 76px; thumbnails hidden; h2 25px |

## Components

- **Eyebrow + section title** (`.section-heading`): 11px/650 uppercase #1a6553 label with 0.15em tracking, 9px above a Georgia 32px/400 title in #202b29; a 13px/550 "All … ↗" link in #1a6553 sits flush right on the title's baseline; 28px below the block.
- **Nav item**: 14px #606f69, padding 10px 0, 27px gaps; current page #202b29 with a 2px #1a6553 underline drawn by `box-shadow: 0 2px`.
- **Theme toggle**: 35px circle, 1px #dce2dc border, transparent fill, "◐" glyph 22px #202b29; hover fill #edf2ed.
- **News row**: 95px date column (12px #606f69, tabular numerals, 3px top padding) and 14px #202b29 text; links underlined in #1a6553; rows 13px top and bottom padding, no rules.
- **Publication row** (`.paper`): 148×98px thumbnail in a #ffffff frame with 1px #dce2dc border and 3px radius, contain-fitted; title 18px/600 #202b29; authors 12px #606f69 with own name 600 #202b29 and superscript †/* markers at 0.75em; an "▸ All N authors" disclosure; venue 12px italic #606f69; link tags; "▸ BibTeX" disclosure at 11px #606f69 that opens a #edf2ed 4px-radius `pre` at 11px. Row separated by a 1px #dce2dc bottom border.
- **Link tag** (`.paper-link`): 10px uppercase, letter-spacing 0.05em, #202b29, padding 3px 9px, 1px #dce2dc border, 3px radius; hover fill #edf2ed with #1a6553 border.
- **Text links**: body links #1a6553 with a 1px underline at 4px offset; contact and "All … ↗" links drop the underline and use weight 550.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Header with wordmark and Chinese name | yes | static bar, 1px rule, current-page underline |
| Name / position / topic line / bio | yes | Georgia 76px name, sans text, jade links |
| Portrait | yes | 250px square, 3px radius, no frame |
| Contact links | yes | 13px/550 jade text links with ↗ |
| News | yes | dated rows, no separators, "All news ↗" |
| Selected publications | yes | thumbnail rows with tags and BibTeX disclosure |
| Projects | present but non-standard | only in the nav; it is a separate page, not a homepage section |
| Theme toggle | yes | ◐ circle, dark palette via `data-theme` or system preference |
| Awards, teaching, students | absent from the source | none |
| Footer | yes | name, 11px tagline, 12px muted links |

## Adapting to Other Content

- **More authors**: keep the 12px #606f69 author line and the "▸ All N authors" disclosure; truncate with "…" after the third name and keep the own name bolded at 600.
- **A results table**: put it after the paper row with 1px #dce2dc horizontal rules, 12px #606f69 header in uppercase with 0.05em tracking, 14px #202b29 cells, best value 600; no fills except a #edf2ed header if needed.
- **Long publication lists**: use the source's `.year-group` pattern (75px year column in sans 20px/450 #606f69, 1px #dce2dc top rule, 30px padding-top, 40px bottom margin).
- **Projects or talks on the homepage**: add a section with an 11px eyebrow, Georgia 32px title and two-column links (18px/550 #202b29 titles, 12px #606f69 notes, 1px #dce2dc bottom borders), as the source's `.project-summary` defines.
- **No photo**: keep the 250px column empty rather than widening the bio past 665px.

## Do's and Don'ts

- Do keep Georgia for the name and section titles only, at weight 400 with -0.035em tracking.
- Do open every section with a 1px #dce2dc rule, an 11px uppercase jade eyebrow and a right-aligned "All … ↗" link.
- Do keep thumbnails at a fixed 148×98px with contain fitting on white so every row has the same rhythm.
- Do use #1a6553 for links and labels only, never as a fill.
- Don't add shadows, cards or rounded corners above 4px.
- Don't bold the serif headings; weight comes from size.
- Don't separate news rows with rules; only publications get bottom borders.

## Surfaces

One flat #fafaf7 ground for header and body, separated by 1px #dce2dc rules. White #ffffff appears only inside thumbnail frames. #edf2ed is reserved for hover fills and BibTeX blocks.

## Imagery

A 250px square studio portrait with a 3px radius. Each publication has a 148×98px figure teaser (method diagrams, bar charts, screenshots) contain-fitted on white with a hairline frame. No icons beyond the ↗ arrow and the ◐ toggle glyph.

## Layout

A centred 980px column. The intro is a 665px + 250px grid; every following section is full column width, stacked with 38px top padding after a rule and 54px bottom margin. Inside sections, a fixed left column (95px dates or 148px thumbnails) aligns content into a steady grid.

## Agent Prompt Guide

Quick colors: page #fafaf7, ink #202b29, muted #606f69, rule #dce2dc, accent #1a6553, wash #edf2ed, frame #ffffff.

1. "Build an intro inside a 1060px container with 40px padding and 65px top padding: grid minmax(0,1fr) 250px with a 65px gap. Name in Georgia 76px/400, letter-spacing -0.035em, #202b29; 12px below a 15px position line, then a 13px #606f69 topic line, then a 15px/1.85 bio with #1a6553 underlined links (1px, offset 4px), then 13px/550 #1a6553 contact links 23px apart. Right column: a 250px square portrait with 3px radius and 10px top margin."
2. "Make a section header: 1px #dce2dc top rule, 38px padding-top; 11px/650 uppercase #1a6553 eyebrow with 0.15em tracking, 9px above a Georgia 32px/400 #202b29 title; a 13px/550 #1a6553 'All publications ↗' link flush right on the title's baseline; 28px below."
3. "Create a publication row: grid 148px + 1fr, gap 26px, padding 27px 0, 1px #dce2dc bottom border. Thumbnail 148×98px, object-fit contain, #ffffff, 1px #dce2dc border, 3px radius. Title 18px/600 #202b29, authors 12px/1.8 #606f69 with own name 600 #202b29, venue 12px italic #606f69, then tags (10px uppercase, 0.05em tracking, padding 3px 9px, 1px #dce2dc border, 3px radius; hover #edf2ed fill, #1a6553 border)."

## Similar Pages

- Minimal faculty homepages that pair a Georgia display name with a system sans and a single muted green accent.
- Publication lists with fixed-size thumbnail teasers in a left column.

## Quick Start

```css
:root {
  --bg: #fafaf7;
  --surface: #ffffff;
  --ink: #202b29;
  --muted: #606f69;
  --line: #dce2dc;
  --accent: #1a6553;
  --soft: #edf2ed;
  --serif: Georgia, "Times New Roman", serif;
  --sans: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --container: 1060px;
  --gutter: 40px;
}
body { margin: 0; background: var(--bg); color: var(--ink); font: 16px/1.7 var(--sans); }
h1, h2 { font-family: var(--serif); font-weight: 400; letter-spacing: -0.035em; line-height: 1.22; }
.eyebrow { font-size: 11px; font-weight: 650; text-transform: uppercase; letter-spacing: .15em; color: var(--accent); }
:root[data-theme="dark"] { --bg: #141c1a; --ink: #e8eeea; --accent: #9acbb3; }
```

## Provenance

- **URL**: https://chenkai.site/
- **Person**: Kai Chen; field: large language models (InternLM, Shanghai AI Laboratory).
- **Venue / award**: ACL 2025 Outstanding Paper, last author of "Capability Salience Vector".
- **Selection reason**: Rule A; award listed at https://2025.aclweb.org/program/awards/ ; homepage from the GitHub hellock blog field, and the page mentions InternLM and Shanghai AI Lab.
- **Template credit**: none stated; a hand-written static site with `/style.css` and `/app.js`.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, `style.css` and `index.html` read directly, and element probes, on 2026-10-28.
