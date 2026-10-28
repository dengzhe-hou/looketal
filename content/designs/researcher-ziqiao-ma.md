# Contour Paper — Style Reference

> Two white index cards laid on a survey map, with faint contour lines and lines of verse curving through the margins.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, fonts, first-viewport color share), the 1440×900 and full-page screenshots, the page's inline `<style>` block and markup in `index.html`, the backdrop file `images/ink-landscape.svg`, and probes of rendered elements. The page follows the system color scheme (`@media (prefers-color-scheme: dark)`); the render and this file describe the light scheme, with the dark values listed separately. The page is exactly one viewport tall (document height 900px) at 1440.

## Overview

A one-screen homepage in the system UI font (Segoe UI on Windows) on white. Behind everything sits a fixed full-window backdrop: a generated SVG of smooth contour lines with text set along some of the curves (lines of a sonnet and code fragments such as `transform.rotation = Quaternion.Slerp(...)`), used as a CSS mask over a #111111 fill at 11% opacity, so it reads as pale gray line art. A second masked layer, the "gleam", darkens the drawing in a 260px radial pool around the pointer. On top: the bold name, a row of plain-text nav links that become pills on hover, and two opaque white cards side by side with 14px radii, hairline borders and a soft shadow. The left card holds About, Research Interests and Miscellaneous; the right card holds Open Weights, Recent Tutorials and Recent Research as title rows with right-aligned dates or venues, separated by hairlines. Descriptions and author lines are hidden and appear only when a row is hovered. A hairline footer closes the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white family #ffffff / #fefefe / #fafafa / #fcfcfc / #f8f8f8 / #f6f6f6 together 92.2%; light gray #ececec 3.1% (contour lines and card hairlines); mid gray #bebebe 4.7% (antialiased text). No accent color exists.

Anatomy in DOM order (`.wrap` max-width 920px, padding 56px 22px 40px, so content runs x=282–1158):

1. **Backdrop** (`.backdrop`, fixed, inset 0, z-index -1): `background: #111111; opacity: .11; mask: url("images/ink-landscape.svg") center / cover no-repeat`. The SVG has a 1600×1000 viewBox with `preserveAspectRatio="xMidYMid slice"`. Contour bands curve in from the left edge around x=0–330, cross the top right (x≈640–1440, y=0–200) and form concentric rings centred near (700, 680) below the cards.
2. **Gleam** (`.gleam`, fixed): `background: radial-gradient(260px circle at var(--px, 50%) var(--py, 50%), #111111, transparent 70%)` under the same mask, opacity 0 until the pointer moves, then 0.24 with a 0.45s fade.
3. **Name** (`h1.name`, y=56, 32px tall): 28px/700, line-height 1.15, letter-spacing -0.02em (-0.56px), #111111. Gap 10px margin + 18px flex row gap.
4. **Nav** (`nav.nav`, y=116, 40px tall): Email, GitHub, Scholar, Twitter, Bsky, Blogs, Personal, World; 16px #666666, padding 6px 10px, 1px transparent border, 999px radius, 14px gaps. Hover: #111111 text, 1px rgba(0,0,0,.10) border, rgba(0,0,0,.06) fill. Email opens a small popover with an arrow. Gap 22px.
5. **Card grid** (`main.grid`, y=178–745): `grid-template-columns: 0.95fr 1.05fr` → 409px and 453px, gap 14px.
6. **Left card** (x=282, 409×567px): #ffffff, 1px rgba(0,0,0,.10) border, 14px radius, padding 18px, shadow `0 10px 30px rgba(0,0,0,.06)`. Inside: "ABOUT" label (y=197, 14px/650 uppercase, letter-spacing 0.08em, #666666), 10px gap, paragraph 16px/1.6 #666666 with underlined #111111 links; an 18px-margin 1px rgba(0,0,0,.10) divider; "RESEARCH INTERESTS"; divider; "MISCELLANEOUS".
7. **Right card** (x=705, 453×567px): same recipe. "OPEN WEIGHTS" then rows (title 16px/600 #111111 left, date 16px #666666 right, 10px vertical padding, hairline between rows), divider, "RECENT TUTORIALS", divider, "RECENT RESEARCH" with five title-only rows.
8. **Footer** (y=771): 26px margin, 1px rgba(0,0,0,.10) top border, 16px padding-top, "© 2026 Martin Ziqiao Ma" 14px #666666.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | --bg | page background, card fill, popover fill |
| Ink | #111111 | --fg / --link | name, row titles, inline links, backdrop and gleam fill (seen at 11% and 24%) |
| Muted | #666666 | --muted | nav links, section labels, paragraphs, dates and venues, footer |
| Hairline | rgba(0,0,0,0.10) | --border | card borders, dividers, row separators, footer rule, nav pill hover border |
| Chip | rgba(0,0,0,0.06) | --chip | nav pill hover fill, chips |
| Link Hover | rgba(0,0,0,0.65) | --link-hover | link hover color |
| Dark Ground | #0b0c0f | --bg (dark) | page and cards in dark scheme |
| Dark Ink | #f2f3f5 | --fg (dark) | text and contour fill in dark scheme (backdrop opacity .17) |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| UI | system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji", "Segoe UI Emoji" | no web font loaded; Segoe UI on Windows, SF Pro on macOS | Inter |
| Backdrop text | drawn inside the SVG (serif italic verse and monospace code along paths) | part of the mask image, not live text | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `h1.name` | 28px / 700 / 1.15, letter-spacing -0.02em | #111111 |
| Section label | `h2` | 14px / 650 uppercase, letter-spacing 0.08em | #666666 |
| Body | `body` | 16px / 400 / 1.6, letter-spacing 0.01em | #111111 |
| Card paragraph | `.card p` (inline style) | 16px / 400 / 1.6, max-width 72ch | #666666 |
| Row title | `.item-title` | 16px / 600 | #111111 |
| Row meta | `.item-meta` | 16px / 400, nowrap | #666666 |
| Row authors (hover) | `.item-authors` | 16px italic | #666666 |
| Nav link | `.nav a` | 16px / 400 | #666666 |
| Footer | `.footer` | 14px | #666666 |
| Popover / chip | `.email-pop`, `.chip` | 13px | #666666 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Card | 14px | 1px rgba(0,0,0,0.10) | `0 10px 30px rgba(0,0,0,.06)` |
| Nav pill (hover) | 999px | 1px rgba(0,0,0,0.10) | none |
| Email popover | 10px | 1px rgba(0,0,0,0.10), 10px rotated-square arrow | `0 10px 30px rgba(0,0,0,.06)` |
| Divider | 0 | 1px rgba(0,0,0,0.10) fill, 18px margin above and below | none |
| List rows | 0 | 1px rgba(0,0,0,0.10) top (none on the first) | none |

## Layout Metrics

- **Container**: `.wrap { max-width: 920px; margin: 0 auto; padding: 56px 22px 40px }` → 876px content at x=282–1158.
- **Header**: flex, `align-items: baseline; justify-content: space-between; gap: 18px; flex-wrap: wrap`; the nav wraps under the name at 1440 because the brand has min-width 260px and the nav does not fit beside it; margin-bottom 22px.
- **Grid**: one column by default; `@media (min-width: 860px)` gives `0.95fr 1.05fr`, gap 14px.
- **Cards**: padding 18px; section label margin-bottom 10px; dividers 18px top and bottom.
- **List rows**: flex space-between, gap 12px, padding 10px 0 (first row no top padding, last row no bottom padding).
- **Footer**: margin-top 26px, padding-top 16px.

| Breakpoint | Gutter | Body size | Name size | Grid change |
|---|---|---|---|---|
| ≥860px | 22px | 16px | 28px | two cards, 0.95fr / 1.05fr |
| <860px | 22px | 16px | 28px | cards stack in one column |

## Components

- **Card** (`.card`): #ffffff fill (opaque over the backdrop), 1px rgba(0,0,0,.10) border, 14px radius, 18px padding, `box-shadow: 0 10px 30px rgba(0,0,0,.06)`.
- **Section label**: 14px/650 uppercase, 0.08em tracking, #666666, 10px below; groups inside a card are split by a 1px rgba(0,0,0,.10) divider with 18px margins.
- **Item row** (`.list li`): title 16px/600 #111111 left, meta 16px #666666 right (nowrap), 12px gap, 10px vertical padding, hairline top border. On row hover, hidden italic authors (#666666) and a description with bracketed links "[Blog] [Model Card] [HuggingFace]" unfold below the title.
- **Nav pill**: plain 16px #666666 text with padding 6px 10px and a transparent 1px border; hover shows #111111 text in a 999px pill with a rgba(0,0,0,.10) border and rgba(0,0,0,.06) fill.
- **Inline link** (`a.inline`): #111111 with a default text underline; hover rgba(0,0,0,.65). Non-inline links have no underline.
- **Email popover**: 13px #666666 text on #ffffff, padding 6px 10px, 10px radius, hairline border and the card shadow, centred 8px under the link with a rotated-square arrow.
- **Contour backdrop**: fixed masked layer described in First Viewport; a pointer-following radial gleam inks the lines darker within 260px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Name and link row | yes | bold system-font name, text links that turn into pills on hover |
| About / interests / miscellany | yes | left card with uppercase labels and dividers |
| Open weights, tutorials, recent research | yes | right card of title rows with right-aligned meta |
| Generative backdrop | yes | masked contour SVG with text on paths, cursor gleam |
| Photo | absent from the source | none |
| Full publication list | absent from the source | only "Recent Research" titles; details on hover |
| News | absent from the source | none |
| Footer | yes | hairline and 14px muted copyright |

## Adapting to Other Content

- **A publication list**: add a card section with the item-row recipe (16px/600 #111111 title, 16px #666666 venue right-aligned, hairline rows) and keep authors folded into the hover reveal as italic #666666.
- **News**: use the same rows with the date as the right-aligned meta; keep at most five rows per card section.
- **A results table**: put it inside a card with hairline rows (1px rgba(0,0,0,.10)), 14px/650 uppercase #666666 headers, 16px #111111 cells, no fills.
- **A photo**: place it at the top of the left card, full card width (373px at 1440) with a 10px radius, above the "ABOUT" label; keep the card white.
- **Longer pages**: keep the backdrop fixed so cards scroll over it; add more card pairs in the same 0.95fr / 1.05fr grid with 14px gaps.

## Do's and Don'ts

- Do keep the cards opaque white with the 14px radius and the 0 10px 30px rgba(0,0,0,.06) shadow, so they sit on the map like paper.
- Do keep the backdrop as a mask over the text color at low opacity (11%) so it follows the theme.
- Do use uppercase 14px/650 labels and hairline dividers to structure each card.
- Do hide secondary detail (authors, descriptions) until hover to keep rows to one line.
- Don't add a color accent; the page is monochrome #111111 / #666666.
- Don't place text directly on the backdrop except the name, nav and footer.
- Don't load a web font; the system UI face is part of the look.

## Surfaces

The page ground is #ffffff carrying the fixed contour drawing at 11% ink. Two white cards float above it with hairline borders and a wide, faint shadow. The dark scheme swaps to #0b0c0f with #f2f3f5 lines at 17%.

## Imagery

No photos. The only image is the generated contour landscape (smooth isolines, some carrying verse and code set along the path), used as a mask so it renders in the theme's ink color.

## Layout

A centred 876px column holding a left-aligned header and a two-card grid; the whole page fits in one 900px viewport at 1440. The cards align at top and stretch to equal height (567px).

## Agent Prompt Guide

Quick colors: page and cards #ffffff, ink #111111, muted #666666, hairline rgba(0,0,0,0.10), hover fill rgba(0,0,0,0.06); backdrop #111111 at opacity .11.

1. "Create a fixed full-window backdrop div at z-index -1 with background #111111, opacity .11 and mask: url(contours.svg) center / cover no-repeat, where the SVG is a 1600×1000 drawing of smooth contour lines with some text on paths. Add a second masked layer with radial-gradient(260px circle at var(--px) var(--py), #111111, transparent 70%) that fades to opacity .24 when the pointer moves."
2. "Build a 920px wrap with padding 56px 22px 40px: name 28px/700, letter-spacing -0.02em, #111111; below it 16px #666666 nav links with padding 6px 10px and 14px gaps that on hover become pills (radius 999px, 1px rgba(0,0,0,.10) border, rgba(0,0,0,.06) fill, #111111 text). Then a grid of two cards (0.95fr 1.05fr, gap 14px)."
3. "Style each card: #ffffff, 1px rgba(0,0,0,.10) border, radius 14px, padding 18px, box-shadow 0 10px 30px rgba(0,0,0,.06). Sections start with a 14px/650 uppercase #666666 label (letter-spacing .08em) and are split by 1px rgba(0,0,0,.10) dividers with 18px margins. List rows: flex space-between, 16px/600 #111111 title, 16px #666666 meta, 10px vertical padding, hairline top border; authors and links appear on row hover."

## Similar Pages

- Minimal "two-card" researcher pages that sit opaque panels over a generative or topographic background.
- Pages built around plain system type with hover-revealed paper details.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --fg: #111111;
  --muted: #666666;
  --border: rgba(0, 0, 0, .10);
  --chip: rgba(0, 0, 0, .06);
  --max: 920px;
  --radius: 14px;
  --shadow: 0 10px 30px rgba(0, 0, 0, .06);
  --backdrop: .11;
}
@media (prefers-color-scheme: dark) {
  :root { --bg: #0b0c0f; --fg: #f2f3f5; --backdrop: .17; }
}
body { margin: 0; color: var(--fg); font: 16px/1.6 system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; letter-spacing: .01em; }
html { background: var(--bg); }
.card { background: var(--bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 18px; box-shadow: var(--shadow); }
```

## Provenance

- **URL**: https://mars-tin.github.io/
- **Person**: Martin Ziqiao Ma (Member of Technical Staff, Thinking Machines Lab; PhD, University of Michigan); field: grounded language acquisition, vision-language models.
- **Venue / award**: ACL 2023 Outstanding Paper, first author of "World-to-Words: Grounded Open Vocabulary Acquisition through Fast Mapping in Vision-Language Models".
- **Selection reason**: Rule A; award listed at https://2023.aclweb.org/program/best_papers/ ; the Semantic Scholar/GitHub homepage ziqiaoma.com redirects here (HEAD on ziqiaoma.com returns 405, so the github.io target is recorded).
- **Template credit**: hand-written single HTML file with inline CSS; the stylesheet comment says the contours were generated by the author's `tools/ink/generate.py`.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, `index.html` (inline style and scripts) and `images/ink-landscape.svg` read directly, and element probes, on 2026-10-28.
