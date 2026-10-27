# David B. Lindell — Style Reference

> A lab notebook typeset by a careful editor: Source Serif prose, Source Sans labels, one clear blue, and every paper filed with its photograph.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, DOM-order anatomy, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the site's own `/assets/css/main.css` (an al-folio-derived Jekyll theme on Bootstrap 4.5.2) read directly with the page markup. Source Serif 4 (400, 400 italic, 600, 700) and Source Sans 3 (400, 600, 700) load from Google Fonts and both render; Font Awesome 5 and Academicons supply the three contact icons. The theme's dark mode script is commented out, so only the light palette is reachable.

## Overview

A 900px Bootstrap container on white. A thin header (1px #e8e8e8 bottom rule) holds "David B. Lindell" in Source Sans 3 20px/700 black on the left and six lowercase nav links on the right in Source Sans 15.2px, the current one ("about") in blue #0076df at 600. The profile block puts a 200px square portrait with 8px corners beside the name in Source Sans 28px/700, a grey 14px serif title block with two blue institutional links, and three 24px dark-grey icons (envelope, Google Scholar, Twitter). Two 16px Source Serif paragraphs follow at 1.65 line height. Three lowercase Source Sans 21.6px/600 section headings ("news", "recent press coverage", "selected publications") organise the rest: a dated news list with blue 12.8px dates in an 80px column and #f0f0f0 hairlines, a press strip of 144px 16:9 thumbnails with an uppercase blue source line, and a publication list of 160×110 thumbnails beside blue titles, grey author lines with the owner in black bold, italic venues with red award notes, and small outlined "project / pdf / code" buttons.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): #ffffff 79.0% (page), #bac2cc 7.4%, #6d6c6f 2.7% and #dde6ee 3.8% (portrait: dark backdrop and pale-blue shirt), #f7f6f6 3.0% and #fdfdfd 2.3% (news hairlines and anti-aliasing). Blue #0076df is below 1% but is the only hue in the text.

Anatomy in DOM order (desktop 1440px; container 900px at x=270, content x=285–1155):

1. **Header bar** (`header.site-header`, y=0–74): padding 24px 0 16px, border-bottom 1px #e8e8e8. Gap 32px.
2. **Site title** (`a.site-title`, x=285, y=24): Source Sans 3 20px/700, #000000, left; `margin-right: auto` pushes the nav right.
3. **Nav links** (`.nav-links a`, y=29, right-aligned to x=1155): Source Sans 3 15.2px/400 #000000, 20px gaps; active "about" 600 #0076df.
4. **Portrait** (`img.profile-img`, x=285, y=106): 200×200, object-fit cover, radius 8px. Beside it at x=509 (24px gap):
5. **Name** (`h1.profile-name`, y=106): Source Sans 3 28px/700, line-height 1.2, #000000, left. Gap 4px.
6. **Title block** (`p.profile-desc`, y=144): Source Serif 4 14px/400, line-height 23.1px, #555555; "Department of Computer Science" and "University of Toronto" as #0076df links. Gap 11px.
7. **Contact icons** (`.profile-social .contact-icon a`, y=224): 24px Font Awesome/Academicons glyphs in #424242, 8px apart; hover #0076df. Profile block ends at y=306; gap 24px.
8. **Bio** (`p`, y=330 and 399): Source Serif 4 16px/400, line-height 26.4px, #000000, margin-bottom 16px; links #0076df; one italic phrase. Gap 24px.
9. **"news" heading** (`h2`, y=634): Source Sans 3 21.6px/600, #000000, lowercase as written, margin-bottom 12px.
10. **News rows** (`.news-item`, from y=672): flex with 16px gap, padding 6.4px 0, border-bottom 1px #f0f0f0; date 12.8px/600 Source Sans #0076df in an 80px column; text Source Serif 4 14px/1.5 #000000. Rows continue past the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Theme Blue | #0076df | --global-theme-color | links, active nav item, news dates, press source line, publication titles, "Show all news", button hover text and border |
| Ink | #000000 | --global-text-color | body prose, site title, nav, headings, owner's name in author lists, press titles, button labels |
| Graphite | #555555 | (literal) | profile title block, publication authors and venue |
| Icon Grey | #424242 | --global-icon-color | envelope, Scholar and Twitter icons |
| Award Red | #cc0000 | (literal, #c00) | `.pub-note` award and highlight notes, e.g. "(Best Student Paper Award)" |
| Header Rule | #e8e8e8 | (literal) | header bottom border, footer top border |
| Row Rule | #f0f0f0 | (literal) | news, press and publication row separators |
| Button Edge | #cccccc | (literal) | outlined publication buttons |
| Thumb Fill | #f5f5f5 | (literal) | press thumbnail placeholder |
| Footer Grey | #828282 | --global-footer-text-color | footer text and link |
| Play Disc | rgba(0,0,0,0.6) | (literal) | round play badge on video press thumbnails |
| White | #ffffff | --global-bg-color | page |

Declared but not visible: `--global-hover-color` #00369f (no rule uses it; link hover keeps #0076df and adds an underline), the dark theme variables (#424242 ground, #2698ba accent), and the `.header-bar` 5rem blue heading used on other pages.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Serif (body) | "Source Serif 4", Georgia, serif | Source Serif 4 400, 400 italic, 600, 700 | Literata |
| Sans (headings, nav, labels) | "Source Sans 3", "Helvetica Neue", sans-serif | Source Sans 3 400, 600, 700 | IBM Plex Sans |
| Icons | Font Awesome 5.14 Free/Brands, Academicons 1.9 | FA 5 Free 900, FA 5 Brands 400, Academicons 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Site title | `.site-title` | 1.25rem = 20px / 700 Sans | #000000 |
| Nav link | `.nav-links a` | 0.95rem = 15.2px / 400 Sans (active 600) | #000000 (active #0076df) |
| Name | `.profile-name` | 1.75rem = 28px / 700 Sans / 1.2 | #000000 |
| Section heading | `h2` (news, press, publications) | 1.35rem = 21.6px / 600 Sans / 1.2, lowercase text | #000000 |
| Body | `body`, `p` | 1rem = 16px / 400 Serif / 1.65 | #000000 |
| Profile title | `.profile-desc` | 0.875rem = 14px / 400 Serif / 1.65 | #555555 |
| News date | `.news-date` | 0.8rem = 12.8px / 600 Sans | #0076df |
| News text | `.news-item` | 14px / 400 Serif / 1.5 | #000000 |
| Press source | `.press-source` | 12.8px / 600 Sans, uppercase, letter-spacing 0.03em | #0076df |
| Press title | `.press-title` | 14px / 400 Serif / 1.4 | #000000 |
| Publication title | `.pub-title a` | 16px / 600 Serif | #0076df |
| Authors, venue | `.pub-authors`, `.pub-venue` | 14px / 400 Serif (venue name italic) | #555555; owner #000000 700 |
| Award note | `.pub-note` | 14px / 600 Serif | #cc0000 |
| Link button | `.pub-link` | 0.8rem = 12.8px / 400 Sans | #000000 |
| Footer | `footer.sticky-bottom` | 14px / 400 Serif, centred | #828282 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Portrait | 8px | none | none |
| Publication thumbnail | 4px | none | none |
| Press thumbnail | 4px | none | none |
| Play badge | 50% (36px) | none | none |
| Link button | 3px | 1px #cccccc (hover #0076df) | none |
| Header | 0 | bottom 1px #e8e8e8 | none |
| News, press, publication rows | 0 | bottom 1px #f0f0f0 | none |
| Footer | 0 | top 1px #e8e8e8 | none |

## Layout Metrics

- **Container**: Bootstrap `.container` with `max-width: 900px` from main.css at every width, 15px side padding; content 870px from x=285 at 1440.
- **Header**: padding 24px 0 16px, margin-bottom 32px; nav is flex, baseline-aligned, gaps 8px 24px; links gap 4px 20px.
- **Profile**: flex, 24px gap, align flex-start, margin-bottom 24px; portrait 200×200.
- **Sections**: news and press margin 24px 0 32px; publications margin-top 32px; headings margin-bottom 12px (8px above publications).
- **News row**: padding 6.4px 0, 16px gap, 80px date column.
- **Press row**: flex, centred, 16px gap, padding 9.6px 0; thumbnail 144px wide at 16:9 (81px tall).
- **Publication row**: flex, centred, 20px gap, min-height 110px; li margin-bottom 12px and padding-bottom 12px; thumbnail 160×110; button row gap 5.6px, button padding 2.4px 8px.
- **Footer**: margin-top 48px, padding 32px 0. Page height 3,938px at 1440.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >900px | auto margins, 15px padding | 16px | name 28px | as described |
| 577–900px | 15px | 16px | 28px | container fills the width |
| ≤576px | 15px | 16px | 28px | profile stacks centred with a 160px portrait; publication rows stack thumbnail over text with a 140×96 thumbnail |
| ≤480px | 15px | 16px | 28px | press thumbnails shrink to 104px |

## Components

- **Header nav**: Source Sans title 20px/700 left, lowercase links 15.2px right with 20px gaps; hover and active #0076df, active 600; 1px #e8e8e8 rule below.
- **Profile block**: 200×200 portrait (radius 8px, cover) + name 28px/700 Sans + 14px #555555 serif title lines with blue links + 24px #424242 icons with 8px spacing, hover #0076df.
- **News row**: 80px #0076df 12.8px/600 date, 14px serif text with #0076df links, 1px #f0f0f0 bottom rule; older rows hidden behind a 14px #0076df "Show all news" toggle.
- **Press card row**: 144px 16:9 thumbnail (radius 4px, #f5f5f5 fill, image scales to 1.04 on hover over 0.25s); video items get a centred 36px rgba(0,0,0,0.6) disc with a white ▶; to the right an uppercase 12.8px/600 #0076df "SOURCE · DATE" line and a 14px #000000 title (hover #0076df).
- **Publication row**: 160×110 thumbnail (cover, radius 4px) linked to the project; title 16px/600 #0076df; authors 14px #555555 with the owner bold #000000; venue 14px with italic venue name and a #cc0000 600 note in parentheses; button row of outlined text buttons: 12.8px Sans #000000, padding 2.4px 8px, 1px #cccccc, radius 3px; hover text and border #0076df. Rows separated by 1px #f0f0f0.
- **Links**: #0076df, no underline at rest, underline on hover.
- **Footer**: centred "© 2026 David B. Lindell · TCIG" in 14px #828282 over a 1px #e8e8e8 top rule.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Header with nav | yes | name left, lowercase links right, hairline below |
| Profile with portrait and icons | yes | 200px portrait, Sans name, grey title, three icons |
| Bio | yes | two Source Serif paragraphs |
| News | yes | dated rows with blue Sans dates, collapsible |
| Press coverage | yes | thumbnail strip with uppercase source line |
| Selected publications | yes | thumbnail rows with outlined buttons |
| Award tags | yes | red 600 notes in parentheses after the venue |
| Abstract / BibTeX toggles | present but non-standard | `.hidden` expanders are styled but no toggle buttons appear on the home list |
| Footer | yes | centred grey credit line |

## Adapting to Other Content

- **Longer publication lists**: group by year with the theme's `h2.year` (Source Sans 20px #828282 with a 1px #e8e8e8 underline) and keep the 160×110 thumbnails; rows stay 110px minimum so the list reads as a grid.
- **Many authors**: author lines wrap freely at 14px #555555; keep the owner bold black so it is findable.
- **More press**: keep one row per item with a 144px thumbnail; text-only items should still get a #f5f5f5 thumbnail box so the column aligns.
- **Talks**: use the theme's talk entry (200×112 thumbnail, radius 4px, 600 blue title, 14px #555555 venue).
- **Students / people**: reuse the press row recipe with a square photo instead of 16:9.

## Do's and Don'ts

- Do pair Source Serif for reading text with Source Sans for anything that labels (nav, headings, dates, sources, buttons).
- Do keep headings lowercase and black; the only coloured headings are links.
- Do use #cc0000 only for award or highlight notes.
- Don't add fills to buttons; they are 1px #cccccc outlines with black labels.
- Don't round thumbnails more than 4px; only the portrait gets 8px.
- Don't add shadows; separation is by #f0f0f0 and #e8e8e8 hairlines.

## Surfaces

All white. Hairlines (#e8e8e8 for header and footer, #f0f0f0 between rows) do the structural work; the only fills are the #f5f5f5 thumbnail placeholder and the translucent play disc.

## Imagery

A studio portrait on a dark backdrop, then press thumbnails (YouTube frame, news photo) and dense publication thumbnails: night scenes, aurora, light-propagation renders, comparison grids. All cropped with object-fit cover to fixed boxes.

## Layout

Header, profile, bio, news (8 visible rows), press (2 rows), selected publications (about 14 rows), footer, all in one 870px column. About 3,938px tall at 1440.

## Agent Prompt Guide

Quick colors: text #000000, secondary #555555, accent #0076df, award #cc0000, icons #424242, rules #e8e8e8 and #f0f0f0, button edge #cccccc, footer #828282, page #ffffff.

1. "Build a header and profile: a 900px container; header padding 24px 0 16px with a 1px #e8e8e8 bottom border; site title Source Sans 3 20px/700 #000000 left, lowercase nav links Source Sans 3 15.2px #000000 right with 20px gaps, active link 600 #0076df. Below, a flex row with 24px gap: 200×200 portrait with 8px radius, then name in Source Sans 3 28px/700, a 14px Source Serif 4 #555555 title block with #0076df links, and 24px #424242 icons 8px apart."
2. "Make a news list: rows with display flex, gap 16px, padding 6.4px 0, border-bottom 1px solid #f0f0f0; date column 80px, Source Sans 3 12.8px/600 #0076df; text Source Serif 4 14px/1.5 #000000 with #0076df links."
3. "Create a publication row: flex, centred, 20px gap, min-height 110px, 1px #f0f0f0 bottom rule; 160×110 thumbnail, cover, 4px radius; title Source Serif 4 16px/600 #0076df; authors 14px #555555 with the owner bold #000000; venue 14px italic with a #cc0000 600 note; buttons Source Sans 3 12.8px #000000, padding 2.4px 8px, 1px solid #cccccc, 3px radius, hover #0076df text and border."

## Similar Pages

- al-folio-family Jekyll academic sites with a custom slimmer header.
- Computational imaging lab pages that lead with a thumbnail publication list.

## Quick Start

```css
:root {
  --text: #000000;
  --secondary: #555555;
  --accent: #0076df;
  --award: #cc0000;
  --icon: #424242;
  --rule: #e8e8e8;
  --row-rule: #f0f0f0;
  --button-edge: #cccccc;
  --footer: #828282;
  --serif: 'Source Serif 4', Georgia, serif;
  --sans: 'Source Sans 3', 'Helvetica Neue', sans-serif;
}
body { font: 400 16px/1.65 var(--serif); color: var(--text); background: #ffffff; }
.container { max-width: 900px; }
h1, h2, .site-title, .nav-links a, .news-date, .pub-link { font-family: var(--sans); }
a { color: var(--accent); }
.pub-link { font-size: 0.8rem; padding: 0.15rem 0.5rem; border: 1px solid var(--button-edge); border-radius: 3px; color: var(--text); }
```

## Provenance

- **URL**: https://davidlindell.com/
- **Person**: David B. Lindell (computational imaging, 3D vision).
- **Venue / award**: CVPR 2025 Best Student Paper, "Neural Inverse Rendering from Propagating Light".
- **Selection reason**: award rule (first/last author). https://tc.computer.org/tcpami/awards/cvpr-paper-awards/
- **Template credit**: Jekyll theme in the al-folio lineage (theme variables, `sticky-bottom` footer, `ol.bibliography`), heavily customised; Bootstrap 4.5.2.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), the 1440×900 and full-page screenshots, and `/assets/css/main.css` and the markup read directly, on 2026-10-28.
