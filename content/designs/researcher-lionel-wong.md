# Lio Wong — Style Reference

> A Swiss-grotesk index card pinned to the left edge: a squat black wordmark, a grainy black-and-white portrait hung in the margin, and research questions boxed in thin black frames.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of every text node and box, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots (1,640px tall), and the page's own `academic_stylesheet.css` (5.0 KB, read in full) and `academic.html` (inline `style` attributes). The page has no media queries; every size below holds at any width.

## Overview

A left-aligned, 600px-wide single column on white, set 50px from the top and left of the window, with the rest of the 1440px viewport left empty. The name "lio wong" is a lowercase 32px wordmark in ABC Gravity, a heavy, compressed grotesk. A 200px black-and-white grainy portrait with 5px rounded corners hangs to the right of the column in its margin (`margin-right: -250px`). The bio is 14px ABC Diatype in black with bold sentences for the key questions and blue (#1772d0) links that carry a "↗" arrow; links turn orange (#f09228) on hover. A centred contact row separates links with slashes. "Research Areas" (21px bold) introduces the signature component: each research question is a box with a 1px black border and 5px radius, a bold 14px question heading, and a bulleted list of sub-questions, each ending with bracketed citation links like "[CogSci, 2023]". Five such boxes stack down the page; there is no footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 79.6% (plus #fffffd 0.4%, #fdffff 0.4%); portrait and text greys #afb2b5 5.5%, #7d7d7d 4.4%, #d1d6da 4.1%, #e9ebed 3.3%, #f8f8f8 2.1%. The blue links are too thin to form a cluster.

Anatomy in DOM order (desktop 1440px; `.content` x=58–658 after the 50px margin plus the 8px body margin):

1. **Wordmark** (`<name>` element, y=50, x=58, 140×41): "lio wong", ABC Gravity 32px/400, #000000, lowercase as typed.
2. **Portrait** (`img.margin`, x=708, y=50, 200×205): `float: right; width: 200px; margin-right: -250px; border-radius: 5px`; grainy black-and-white photo, no border or shadow.
3. **Intro paragraph** (`p.description`, y=105, 600px): ABC Diatype 14px/400, line-height normal (about 18px), #000000, `margin: 14px 0`; recruiting sentence in 700; links #1772d0 with a trailing "↗" in the link text. Gap 14px between paragraphs.
4. **Research paragraphs** (y=191 and y≈311): same 14px style with bold question phrases ("How do we learn and use language so efficiently?").
5. **Contact row** (`p` with `text-align:center`, y=471): "liowong@stanford.edu / Google Scholar / Github / writing and clocks / signal hill", links #1772d0, slashes #000000. Gap 49px.
6. **Section heading** (`h2`, y=538): "Research Areas", ABC Diatype 21px/700, `margin: 17.43px 0`.
7. **First research box** (`div.highlight`, x=44, y=585, 628×219): 1px solid #000000, radius 5px, `padding: 1.5em` (21px), `margin: 1.5em -1em` (21px / -14px); inside a 14px/700 question (`h4`) and a disc list at x=80 with `margin-bottom: 3px` per item. The second box starts at y≈825, at the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Ink | #000000 | (default text, `.highlight` border) | wordmark, all text, box borders, slashes |
| Link Blue | #1772d0 | `a { color }` | every link, including "↗" arrows and bracketed citations |
| Hover Orange | #f09228 | `a:hover, a:focus` | link text on hover and focus |
| Paper | #ffffff | (default) | page |
| Note Yellow | #ffffd0 | `span.highlight` | declared highlighter span; not used on this page |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Wordmark | 'ABCGravity', "Bauhaus93", 'ABCDiatype', Verdana, Helvetica, sans-serif (self-hosted `fonts/ABCGravity-Normal.woff`) | ABCGravity normal | Anton (lowercase) or Archivo Black condensed |
| Text | 'ABCDiatype', Verdana, Helvetica, sans-serif (self-hosted `.otf`, regular and bold) | ABCDiatype normal, bold | Inter Tight |
| Lato | `@font-face` blocks for Lato 400/700 and italics | not used by any rule | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Wordmark | `name` | 32px / 400 / normal | #000000 |
| Body | `body, p, a, td` | 14px / 400 / normal (≈18px) | #000000 |
| Emphasis | `b` | 14px / 700 | #000000 |
| Section heading | `h2` | 21px / 700 / normal (1.5em default) | #000000 |
| Box question | `.highlight h4` | 14px / 700 / normal | #000000 |
| List item | `.highlight li` | 14px / 400, sub-terms italic, thesis title bold italic | #000000 |
| Link | `a` | 14px / 400 | #1772d0; hover #f09228 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Research box (`.highlight`) | 5px | 1px solid #000000 | none |
| Portrait (`.margin`) | 5px | none | none |
| Links | 0 | none, no underline | none |

## Layout Metrics

- **Column**: `.content { max-width: 600px; margin: 50px }` plus the 8px default body margin, so text runs x=58–658 and starts at y=50. The column is left-aligned; at 1440 about 530px of the viewport to the right of the portrait stays empty.
- **Portrait**: floated right inside the column but pushed out with `margin-right: -250px`, so it sits at x=708–908 (50px gap from the column).
- **Paragraphs**: browser-default `margin: 1em 0` (14px).
- **Research boxes**: `margin: 1.5em -1em` (21px vertical, -14px sides, so boxes are 628px wide and overhang the column by 14px each side), `padding: 1.5em` (21px); lists indented to x=80; consecutive boxes about 21px apart.
- **Headings**: `h2` default margins 0.83em (17.43px).

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| all widths | 50px + 8px | 14px | 32px | no media queries; below about 910px the portrait's negative margin pushes it past the right edge |

## Components

- **Wordmark**: lowercase name in ABC Gravity 32px, black; no logo or tagline.
- **Margin portrait**: 200px grainy black-and-white photo, 5px radius, floated into the right margin at the top of the page.
- **Arrow link**: #1772d0, no underline, with "↗" typed into the link text for external links; hover and focus #f09228.
- **Slash link row**: one centred line of links separated by " / " in black.
- **Research question box** (`.highlight`): 1px solid #000000, radius 5px, padding 21px; bold 14px question; disc bullets of sub-questions at 14px with key phrases in italic, each ending with bracketed blue citation links "[CogSci, 2023]" or "[Thesis, 2024][SPP, 2023]"; 3px between items.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Name / wordmark | yes | heavy grotesk, lowercase |
| Portrait | yes | grainy B/W photo in the right margin |
| Bio | yes | 14px black paragraphs with bold questions |
| Contact links | yes | centred slash-separated row |
| Research areas | yes | bordered question boxes with bulleted sub-questions |
| Publications | present but non-standard | no list; papers appear as bracketed citations inside the research boxes |
| Navigation | absent from the source | — |
| News | absent from the source | — |
| Footer | absent from the source | — |

## Adapting to Other Content

- **A full publication list**: add an `h2` (21px/700) and list each paper as one 14px line with the title in 700 (`papertitle` is declared at 14px/700) and blue bracketed links; no boxes, so the research boxes stay the only framed element.
- **News**: an `h2` "News" and a plain list, each item starting with the date in 700; at 1440 one line holds about 90 characters in the 600px column.
- **A results table**: 14px ABC Diatype, header in 700, 1px #000000 rules under the header only, inside the 600px column.
- **More research areas**: repeat the box; each extra box adds its content height plus 21px. Keep each to one bold question and at most eight bullets.
- **Centring on wide screens**: the source does not centre; if you must, set `margin: 50px auto` on `.content` and keep the portrait's -250px overhang, which needs the viewport to extend at least 250px past the column's right edge.

## Do's and Don'ts

- Do set the name in a heavy lowercase grotesk and everything else in one 14px sans.
- Do use #1772d0 for links and #f09228 only for hover.
- Do frame research questions in 1px black boxes with 5px corners and 21px padding.
- Do keep the portrait black and white with grain, 200px, outside the text column.
- Don't underline links or add colored backgrounds.
- Don't add shadows or a second box style.
- Don't enlarge body text; the 14px measure is part of the compact look.

## Surfaces

White only. The research boxes are outlined, not filled.

## Imagery

One grainy black-and-white portrait (a laughing pose in a striped shirt, framed pictures behind), 200px with 5px corners. No other images.

## Layout

Top-left anchored 600px column (50px margins), portrait hanging in the right margin, then bio, contact row, a heading and a stack of bordered question boxes. Left-aligned on every screen size.

## Agent Prompt Guide

Quick colors: text and borders #000000, links #1772d0, hover #f09228, page #ffffff.

1. "Build a top-left column: .content max-width 600px, margin 50px; name in a heavy lowercase grotesk (ABC Gravity, fallback Anton) at 32px #000000; body in ABC Diatype 14px #000000; links #1772d0 with no underline and a '↗' after external links, hover #f09228."
2. "Hang a 200px black-and-white portrait in the right margin: float right, width 200px, margin-right -250px, border-radius 5px, no border or shadow."
3. "Create research question boxes: border 1px solid #000000, border-radius 5px, padding 1.5em, margin 1.5em -1em; a bold 14px question, then a disc list of 14px sub-questions with key phrases in italic, each ending with bracketed #1772d0 citation links like '[CogSci, 2023]', 3px between items."

## Similar Pages

- Jon Barron-style single-column academic pages adapted with custom grotesk fonts.
- Research statements organized as question cards instead of a publication list.

## Quick Start

```css
:root {
  --ink: #000000;
  --link: #1772d0;
  --hover: #f09228;
  --paper: #ffffff;
  --font-name: "ABCGravity", "Bauhaus93", "ABCDiatype", Verdana, Helvetica, sans-serif;
  --font-text: "ABCDiatype", Verdana, Helvetica, sans-serif;
}
body { background: var(--paper); color: var(--ink); font: 400 14px var(--font-text); }
.content { max-width: 600px; margin: 50px; }
name { font: 400 32px var(--font-name); }
a { color: var(--link); text-decoration: none; }
a:hover, a:focus { color: var(--hover); }
.margin { float: right; width: 200px; margin-right: -250px; border-radius: 5px; }
.highlight { margin: 1.5em -1em; padding: 1.5em; border: 1px solid var(--ink); border-radius: 5px; }
```

## Provenance

- **URL**: https://web.mit.edu/zyzzyva/www/academic.html
- **Person**: Lionel (Lio) Wong, computational cognitive science of language and thought; the page says incoming assistant professor at Brown University (CoPsy) and postdoc at Stanford.
- **Award**: Glushko Dissertation Prize 2025 (thesis "From Words to World").
- **Selection reason**: Rule B(2), Glushko Dissertation Prize 2025 winner per https://cognitivesciencesociety.org/glushko-dissertation-prize/ ; personal MIT web page titled "Lio Wong | Stanford", found through a third-party post and confirmed to be his from its content.
- **Template credit**: none stated; the stylesheet's `name`, `heading`, `papertitle`, `.one/.two` and `#1772d0 / #f09228` link colors come from Jon Barron's widely copied academic page template.
- **Evidence used**: tools/computed_style.py render at 1440×900, a per-element style census and full-page capture from the same headless Chrome, and `academic_stylesheet.css` plus `academic.html` read directly, on 2026-10-28.
