# Daniel Roy — Style Reference

> A marker-scrawled name on the door of a busy statistics office.

**Theme:** light (with a dark left column)

Measurements are normalized from the static HTML, its inline `<style>` block and `styles/screen.css`; roles are interpreted. Many layout values sit in inline `style` attributes, which I read directly.

## Overview

A long-lived hand-coded page with a fixed 968px minimum width and absolutely positioned columns. The header area, 520px tall, starts 20% in from the left with the name "Dan Roy" in Permanent Marker at 60pt in a brick red (#a21919), then stacked Lato 21px lines for chairs, positions, departments and editorial boards, ending with a note about joining Google DeepMind. Under it, three columns sit side by side: a dark #333 strip on the far left (18% wide, bottom-right corner rounded 30px) holding a candid portrait and a "contact" block in light grey; a 28% justified column with research, group and teaching; and a wide 48% column with preprints, research articles and technical reports. Links and paper titles are a dark olive (#666600) that brightens to #888800 on hover. Section headers are lowercase in the source and uppercased by CSS at 28px.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Brick Marker | #a21919 | `--name` | Name in Permanent Marker; background behind award logo images |
| Olive Ink | #666600 | `--link` | All link states and `.paper` titles |
| Olive Glow | #888800 | `--link-hover` | Link hover |
| Workshop Grey | #f2f2f2 | `--bg` | Page background (inline on `body`, overriding #eee in screen.css) |
| Shadow Column | #333333 | `--rail` | Left column background (`.recede`); section header color |
| Text Ink | #222222 | `--text` | Body text |
| Position Grey | #444444 | `--pos` | Header position lines (`.pos`) |
| Silver Info | `silver` (#c0c0c0) | `--info` | `p.info` text, used for contact details on the dark column |
| Label Grey | `gray` (#808080) | `--label` | Bold labels in `.info`, announcement dates |
| Rule Grey | #999999 | `--rule` | Top border of the third grid group |
| Contact White | #eeeeee | none | "contact" header on the dark column |
| Alarm Red | `red` | none | Dates in the (commented out) news block |

## Tokens — Typography

- **Display:** Permanent Marker (Google Fonts), fallback `serif`. Substitute: Rock Salt or Caveat Brush.
- **Text:** Lato 400 and 900 (Google Fonts), fallback `sans-serif`. Open Sans is also loaded; Lato is what `body` and `.pos` use. Substitute: Carlito or Source Sans 3.
- **Mono:** `fixed` for `.bibtexhead`.
- **Weights:** body normal, bold for paper titles, labels, and key phrases.

| Level | Element | Size | Line height | Notes |
|---|---|---|---|---|
| Name | `.nameheader` | 60pt | | Permanent Marker, #a21919 |
| Position lines | `.pos` | 21px | 1.1em | Lato, #444 |
| Section | `.bigheader` | 28px (22px for contact, 18pt for probabilistic programming) | | uppercase, #333 |
| Paper title | `.paper` | 13pt | | bold, #660 |
| Body | body | 12pt | 1.4 | Lato |
| Small | inline | 10pt to 11px | | tweets, notes |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| Tab corner | 0 0 30px 0 | `.recede` dark column, bottom-right only |
| Square | 0 | everything else |

- **Shadows:** none.
- **Layout:** `body { min-width: 968px }`, wrappers `max-width: 1400px`; header block `height: 520px; margin-left: 20%`.
- **Columns:** `#box2-4` left 0 width 18%; `#box3-4` left 20% width 28%; `#box4-4` left 50% width 48%; all absolutely positioned.
- **Rhythm:** paragraphs `margin-bottom: 1.4em`; `.bigheader` `margin: 2.5em 0 15px 15px` with a -11px text indent.

## Components

- **Marker nameplate.** Role: identity. 60pt Permanent Marker in brick red, no other decoration; hidden span carries name variants for search.
- **Position stack.** Role: affiliations. Repeated `p.pos` blocks at 21px Lato, bold leads ("Professor", "Editorial Boards"), indented sub-lines with `margin-left: 2em`.
- **Dark rail.** Role: portrait and contact. #333 block pulled up 520px to align with the header, rounded 30px at the bottom-right; full-width candid photo; "contact" header in #eee and silver info text.
- **Section header.** Role: research, group members, preprints and so on. `.bigheader` 28px uppercase #333 with a hanging -11px indent.
- **Paper entry.** Role: one paper. Paragraph with a bold 13pt olive title link, line break, authors, line break, venue in italics with a bold "Spotlight" or arXiv link; 107 entries.
- **News item (inactive).** Role: dated announcements. Commented out in the current HTML; red bold dates and short paragraphs. An older award note uses a small logo image on a #a21919 padded tile.

## Page Modules

- **Title/author block:** marker-font name with a long stack of positions and boards.
- **Bio/photo:** candid portrait on the dark rail; research statement in the middle column with a talk video link.
- **Group:** "joining my group", "group members" and "group alumni" sections.
- **Publication list:** preprints, research articles, technical reports in the right column; text only, no thumbnails.
- **Link buttons:** arXiv and paper links inline; `a.bibtex` links are hidden by CSS.
- **Awards:** mentioned in prose and venue lines.
- **Contact:** on the dark rail.
- **News:** present in source but commented out.
- **Venue badges, BibTeX blocks, teaser media:** not visible.

## Do's and Don'ts

- Do set the name in a marker face, large and red; it is the page's signature.
- Do use one olive color for both links and paper titles.
- Do keep the dark rail with only its bottom-right corner rounded.
- Don't expect a phone layout; the page sets `min-width: 968px` and absolute columns. If you rebuild it, swap to CSS grid and stack below about 900px.
- Don't add colored badges; emphasis is bold text.
- Don't mix in the loaded Open Sans for body text; Lato carries the page.

## Surfaces

Light grey page, one dark rail column, no cards. A gray 1px rule tops the third grid group.

## Imagery

A candid portrait filling the rail width, an inline Vector Institute logo, and a small award logo on a red tile in older news.

## Layout

Three absolutely positioned columns under a 520px header that is offset 20% from the left. Widths are percentages of a container capped at 1400px, with a hard 968px page minimum.

## Agent Prompt Guide

**Quick colors:** bg #f2f2f2, text #222, name #a21919, link and titles #666600, hover #888800, rail #333, headers #333, info silver.

1. "Build a header offset 20% from the left: name in Permanent Marker 60pt #a21919, then stacked Lato 21px lines in #444 with line-height 1.1em for positions, with indented sub-lines at 2em."
2. "Create a dark side rail 18% wide: background #333, bottom-right radius 30px only, a full-width portrait, then a 22px uppercase 'contact' header in #eee and silver info text."
3. "Style a publication paragraph: bold 13pt title link in #666600 (hover #888800), authors on the next line, then the venue in italics with a bold 'Spotlight'. Section headers above in 28px uppercase #333."

## Similar Pages

- [Idan Attias](https://www.idanattias.com/), his co-first-author on the ICML 2024 Best Paper, for a modern sidebar layout.
- [Danica J. Sutherland](https://djsutherland.ml/) for another theory page with a long text publication list.

## Quick Start

```css
:root {
  --bg: #f2f2f2;
  --text: #222222;
  --name: #a21919;
  --link: #666600;
  --link-hover: #888800;
  --rail: #333333;
  --pos: #444444;
  --info: silver;
  --font-display: 'Permanent Marker', serif;
  --font-text: 'Lato', sans-serif;
}
body { margin: 0; background: var(--bg); color: var(--text); font: 12pt/1.4 var(--font-text); }
.nameheader { font-family: var(--font-display); font-size: 60pt; color: var(--name); margin: 0; }
.pos { font-size: 21px; line-height: 1.1em; color: var(--pos); }
.bigheader { text-transform: uppercase; font-size: 28px; color: var(--rail); text-indent: -11px; }
a:link, a:visited, .paper { color: var(--link); } a:hover { color: var(--link-hover); }
.paper { font-weight: bold; font-size: 13pt; }
.recede { background: var(--rail); border-bottom-right-radius: 30px; }
```

## Provenance

- **URL:** https://danroy.org/
- **Venue/award:** ICML 2024 Best Paper (last author of "Information Complexity of Stochastic Convex Optimization"), per https://icml.cc/virtual/2024/awards_detail
- **Selection reason:** Rule B; personal site listed by the U of Toronto Statistics directory.
- **Template credit:** none; hand-coded HTML with `screen.css`.
- **Measurement method:** values read from `screen.css`, the inline style block and inline attributes via `extract_style.py` and curl. Not rendered in a browser. The extractor flagged a dark-mode toggle, but that came from `data-theme="dark"` on a commented-out Twitter widget; the page has no theme switch.
