# Vladimir Chituc — Style Reference

> A letterpress calling card on warm rice paper: lowercase Georgia set wide, grey Source Sans prose, and small blush-grey tabs tucked under each paper.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of every text node and box, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots (1,567px tall), and the site's compiled Quarto/Bootstrap stylesheet (`site_libs/bootstrap/bootstrap-5713f3742d085f0d9696c1c3753e0a1f.min.css`, which carries the custom SCSS) read directly. The root font size renders at 17px, so `0.92rem` body text renders 15.64px; sizes below are the rendered values.

## Overview

A short, quiet Quarto site on a warm off-white (#f8f4f4) with every element in one 580px centred column. The header is text only: "vlad chituc" in lowercase Georgia with 3px letter-spacing, and under it a row of lowercase Georgia nav links in grey (#888888), the current one in near-black (#222222) with a 2px underline offset 6px; a 1px #dddddd rule closes the header. The bio is three short paragraphs of grey (#5c5c5c) Source Sans 3 at 15.64px with italic outlet names. A centred row of plain-text links (email, cv, bsky, scholar, o-id), each led by a small north-east arrow icon, sits between generous margins. "select publications" follows as a lowercase Georgia heading with a full-width hairline under it; each entry shows the bold short author name, the title in a darker #333333, an italic venue, and a centred row of tiny blush-grey (#ede8e8) tabs ("preprint", "web", "data"), with a 200px centred hairline between entries. A "see all publications →" link and a slim footer (email left, "Built with Quarto" right) end the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): warm off-white #f8f4f4 84.9% with its neighbours #faf6f6 2.3%, #f9f4f4 1.9%, #f8f4f3 1.8%; text anti-aliasing #c7c4c4 5.0%; link-tab and rule tints #efebeb 3.7%.

Anatomy in DOM order (desktop 1440px; column x=430–1010):

1. **Navbar** (`nav.navbar`, 0–128px, `fixed-top` with headroom hide-on-scroll): background #f8f4f4, `padding-top: 2rem` (34px), no shadow. Inner `.navbar-container` max-width 580px, `padding-bottom: 20.4px`, `border-bottom: 1px solid #dddddd`.
2. **Site title** (`span.navbar-title`, y=43): "vlad chituc", Georgia 22.1px/400 (1.3rem), letter-spacing 3px, lowercase, #222222. Gap 19px.
3. **Nav links** (`.navbar .nav-link`, y=87): "home research writing consulting psychophysical measures", Georgia 14.45px/400 (.85rem), letter-spacing 1px, lowercase, #888888, `padding-right: 1.2rem`; active "home" #222222 with `text-decoration: underline; text-underline-offset: 6px; text-decoration-thickness: 2px`. Rule at y=128. Gap 47px.
4. **Bio** (`main.content p`, y=175, 579px wide): Source Sans 3 15.64px/400, line-height 23.46px, #5c5c5c, margin-bottom 17px; links in #5c5c5c without underline; outlet names italic. Three paragraphs end at y=465.
5. **Link row** (`.social-links`, y=509): centred, 15.3px (.9rem), `word-spacing: .3rem`, `margin: 2.5rem 0 3rem`; links #5c5c5c, each with a leading ↗ arrow SVG and `gap: .15rem`, `margin: 0 .2rem`. Gap 53px.
6. **Section heading** (`h2`, y=585): "select publications", Georgia 17.85px/400, letter-spacing 1.5px, lowercase, #222222, `padding-bottom: 20.4px`, `border-bottom: 1px solid #dddddd`, `margin-bottom: 20.4px`.
7. **First publication** (`.pub-entry`, y=648): authors 16.15px with "Chituc, V." in 700 #5c5c5c, title #333333, venue italic #5c5c5c, line-height 1.6; link tabs at y=731 (27px tall), then a 200px #dddddd hairline. The second entry starts near y=800, so the fold cuts the list.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Rice Paper | #f8f4f4 | --bs-body-bg | page, navbar, footer backgrounds |
| Ink | #222222 | --bs-link-hover-color, headings | site title, active nav link, h2 headings, link hover |
| Pencil Grey | #5c5c5c | --bs-body-color / --bs-link-color | bio text, links, authors, venues, link-row items, tab labels |
| Title Grey | #333333 | `.pub-title` | publication titles |
| Nav Grey | #888888 | `.navbar .nav-link` | inactive nav links |
| Footer Grey | #999999 | footer text | footer email and "Built with Quarto" |
| Blush Tab | #ede8e8 | `.pub-links a` background | preprint / web / data tabs |
| Hairline | #dddddd | (literal) | header rule, h2 rule, 200px separators, footer top border, tab hover background |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text | "Source Sans 3", "Source Sans Pro", -apple-system, sans-serif (Google Fonts 300/400/600/700/400i) | Source Sans 3 400, 400 italic, 700 | Source Sans 3 |
| Display / nav | Georgia, "Times New Roman", serif | system Georgia (no web font) | Gelasio |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Site title | `.navbar-brand` | 1.3rem = 22.1px / 400 / 33.15px, letter-spacing 3px, lowercase | #222222 |
| Nav link | `.navbar .nav-link` | .85rem = 14.45px / 400 / 21.675px, letter-spacing 1px, lowercase | #888888; active #222222 |
| Section heading | `section#publications h2` | 17.85px / 400 / 21.42px, letter-spacing 1.5px, lowercase | #222222 |
| Body | `body` | .92rem = 15.64px / 400 / 23.46px | #5c5c5c |
| Publication text | `.pub-entry p` | 15.64px / 400 / 1.6 = 25.02px | #5c5c5c |
| Own name | `.pub-authors strong` | .95rem of parent = 16.15px / 700 | #5c5c5c |
| Publication title | `.pub-title` | 15.64px / 400 | #333333 |
| Venue | `.pub-venue` | 15.64px / 400 italic | #5c5c5c |
| Link row | `.social-links` | .9rem = 15.3px / 400 | #5c5c5c |
| Link tab | `.pub-links a` | .8rem = 13.6px / 400 / 21.76px | #5c5c5c |
| Footer | `.nav-footer p` | 11.92px / 400 / 17.88px | #999999 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link tabs | 3px | none | none |
| Header block | 0 | bottom 1px solid #dddddd | none (`box-shadow: none !important`) |
| Section heading | 0 | bottom 1px solid #dddddd | none |
| Entry separator | 0 | a 200×1px #dddddd block (`.pub-entry::after`), centred | none |
| Footer | 0 | top 1px solid #dddddd | none |

## Layout Metrics

- **Column**: Quarto `page-columns` grid with the body column `minmax(500px, calc(580px - 3em))`; renders 580px wide at x=430–1010 at 1440, centred by the `5fr` side tracks. The navbar container also caps at 580px.
- **Header**: `padding-top: 2rem` (34px), container `padding-bottom: 1.2rem` (20.4px), title `margin-bottom: .4rem`, total height 128px.
- **Bio**: starts 47px below the header rule; paragraph spacing 17px.
- **Link row**: `margin-top: 2.5rem; margin-bottom: 3rem` (42.5px / 51px).
- **Publications**: `.pub-entry { margin-bottom: 1rem; padding-bottom: .8rem; line-height: 1.6 }`; tabs `margin-top: .2rem`, `padding: .15rem .5rem`, `margin-right: .4rem`; separator `margin-top: .8rem`.
- **Footer**: full width, `padding: 8.5px 14.45px`, two 470px halves (left / right aligned) at x=14 and x=955.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥992px | 5fr side tracks, column 580px | 15.64px | 22.1px | as described |
| <992px | 1.5rem side tracks | 15.64px | 22.1px | navbar collapses to a toggler; first h2 margin-top 1rem |
| ≤767px | 1.5rem | 15.64px | 30.6px (1.8rem), letter-spacing 2px | — |

## Components

- **Wordmark**: lowercase Georgia 22.1px, letter-spacing 3px, #222222, no logo or portrait.
- **Nav link**: lowercase Georgia 14.45px, letter-spacing 1px, #888888, `transition: color .2s ease`, 1.2rem right padding; hover #222222 (`.navbar .nav-link:hover{color:#222 !important}`); active link #222222 underlined 2px with a 6px offset.
- **Arrow link row**: centred plain-text links in #5c5c5c, each prefixed by a small ↗ SVG, `word-spacing: .3rem`; hover #222222, no underline.
- **Section heading**: lowercase Georgia 17.85px, letter-spacing 1.5px, #222222, full-column 1px #dddddd underline with 20.4px padding and margin.
- **Publication entry** (`.pub-entry`): one paragraph at 15.64px/1.6; bold short name, other authors and year in #5c5c5c, title in #333333, venue italic; a centred row of link tabs; a centred 200px hairline after every entry but the last.
- **Link tab** (`.pub-links a`): inline-block, 13.6px #5c5c5c on #ede8e8, `padding: .15rem .5rem`, radius 3px, no underline; hover background #dddddd and text #222222.
- **Footer**: #f8f4f4 with a 1px #dddddd top border; email at left and "Built with Quarto" at right, 11.92px #999999.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top navigation | yes | text-only Georgia wordmark and lowercase links over a hairline |
| Portrait | absent from the source | — |
| Bio | yes | three grey Source Sans paragraphs |
| Link row | yes | centred arrow-prefixed text links |
| Selected publications | yes | entries with centred tab links and 200px separators |
| Full publication list | yes (other page) | "see all publications →" link |
| Consulting / writing pages | yes (other pages) | in the nav |
| News | absent from the source | — |
| Footer | yes | slim two-sided Quarto footer |

## Adapting to Other Content

- **A portrait**: place it above the bio at no more than 160px wide inside the 580px column, square corners, no frame; the page has none, so keep it small enough that the wordmark stays the identity.
- **News**: a lowercase Georgia h2 ("news") with the same hairline, then items as 15.64px #5c5c5c paragraphs with the date in 700, separated by the 200px centred hairline.
- **A results table**: 15.64px Source Sans, header row in #222222 700, 1px #dddddd rules, no fills; keep it within 580px.
- **Long publication lists**: keep the entry pattern; group by year with lowercase Georgia h2 headings. The page itself moves the full list to a separate page.
- **More links**: extend the arrow row; at 1440 each item is 40–70px wide, so eight fit on one centred line.

## Do's and Don'ts

- Do keep everything inside one 580px centred column on #f8f4f4.
- Do set titles and navigation in lowercase Georgia with letter-spacing (3px title, 1–1.5px elsewhere).
- Do keep body text grey (#5c5c5c) and reserve #222222 for headings, the active link and hover.
- Do use the #ede8e8 tab for paper links and the 200px hairline between entries.
- Don't underline inline links or color them; they stay #5c5c5c until hover.
- Don't add pure white surfaces, cards or shadows.
- Don't capitalize headings; lowercase is part of the voice.

## Surfaces

One warm off-white surface (#f8f4f4) for page, header and footer; separation only by #dddddd hairlines and the #ede8e8 link tabs.

## Imagery

None. The only graphics are small arrow SVGs in the link row.

## Layout

Single 580px column, centred; text-only header with a rule; bio; centred link row with wide margins; a heading with rule; publication entries with centred tabs and short centred separators; a slim full-width footer.

## Agent Prompt Guide

Quick colors: page #f8f4f4, text #5c5c5c, headings and active #222222, titles #333333, nav #888888, footer #999999, tabs #ede8e8, rules #dddddd.

1. "Build a text-only header inside a 580px centred column on #f8f4f4: padding-top 34px; wordmark 'first last' in Georgia 22.1px, letter-spacing 3px, lowercase, #222222; below it lowercase Georgia 14.45px links with letter-spacing 1px in #888888, 1.2rem apart, the active one #222222 underlined 2px with a 6px offset; close with a 1px #dddddd rule 20.4px below."
2. "Create a publication entry: Source Sans 3 15.64px, line-height 1.6, #5c5c5c; own name 700, title #333333, venue italic; then a centred row of tabs: 13.6px #5c5c5c on #ede8e8, padding .15rem .5rem, radius 3px, 0.4rem apart, hover background #dddddd and text #222222; after the entry a centred 200×1px #dddddd line."
3. "Make a centred link row: 15.3px #5c5c5c text links each led by a small north-east arrow icon, word-spacing .3rem, margin 2.5rem 0 3rem, hover #222222, no underline."

## Similar Pages

- Quarto and Hugo personal sites with a text-only wordmark and a single narrow column.
- Literary-styled academic pages that pair a serif display face with a humanist sans body.

## Quick Start

```css
:root {
  --bg: #f8f4f4;
  --ink: #222222;
  --text: #5c5c5c;
  --title: #333333;
  --nav: #888888;
  --footer: #999999;
  --tab: #ede8e8;
  --rule: #dddddd;
  --font-text: "Source Sans 3", "Source Sans Pro", -apple-system, sans-serif;
  --font-display: Georgia, "Times New Roman", serif;
  --column: 580px;
}
html { font-size: 17px; }
body { background: var(--bg); color: var(--text); font: 400 .92rem/1.5 var(--font-text); }
.brand { font: 400 1.3rem var(--font-display); letter-spacing: 3px; text-transform: lowercase; color: var(--ink); }
h2 { font-family: var(--font-display); font-weight: 400; letter-spacing: 1.5px; text-transform: lowercase; color: var(--ink); border-bottom: 1px solid var(--rule); padding-bottom: 1.2rem; }
.pub-links a { font-size: .8rem; background: var(--tab); color: var(--text); padding: .15rem .5rem; border-radius: 3px; text-decoration: none; }
.pub-links a:hover { background: var(--rule); color: var(--ink); }
```

## Provenance

- **URL**: https://vladchituc.com/
- **Person**: Vladimir Chituc, moral psychology and psychophysics; postdoctoral researcher at Stanford per the page.
- **Award**: Glushko Dissertation Prize 2025.
- **Selection reason**: Rule B(2), Glushko Dissertation Prize 2025 winner per https://cognitivesciencesociety.org/glushko-dissertation-prize/ ; homepage linked from his own Bluesky profile (vladchituc.bsky.social).
- **Template credit**: built with Quarto (footer "Built with Quarto"); custom SCSS compiled into the Bootstrap bundle.
- **Evidence used**: tools/computed_style.py render at 1440×900, a per-element style census and full-page capture from the same headless Chrome, and the compiled Bootstrap/Quarto CSS read directly, on 2026-10-28.
