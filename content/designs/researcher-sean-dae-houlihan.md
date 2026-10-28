# Sean Dae Houlihan — Style Reference

> A grey slate marquee with a red-and-black wordmark, then a stack of rounded index cards, each stamped with a typewriter date and a small-caps ribbon.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of every text node and box, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots (3,070px tall), and the site's own SvelteKit stylesheets (`/_app/immutable/assets/0.BARNes1L.css`, `3.DzsZ5r3p.css`) read directly. Theme colors are declared in oklch; their sRGB hex conversions are given in the tables. The portrait, the "seandaehoulihan" wordmark and the subtitle are one raster image (`splash.jpg`), not live text.

## Overview

A short, single-column academic homepage in the system UI font (Segoe UI on Windows). An 80px light grey (#dddddd) bar carries a small head-silhouette logo, the name in 20px, and four lowercase nav links, the active one in brick red (#993333) with a 4px red underline. Below it a full-width 300px slate-grey (#596069) banner image shows a circular portrait at left and a heavy black "sean dae houlihan" wordmark with "dae" in bright red, over the subtitle "Computational Cognitive Science of Emotion". A row of four icon links (Bluesky, GitHub, Scholar, Email) is framed by tall thin brackets and divided by thin grey rules. A justified 20px bio follows, with names linked in #993333. The News section is the signature: each item is a white card with a 2px grey border and 24px radius, a 120px square thumbnail on the left, a monospace date top right, the text, and a small-caps red title "~ Like This ~" in a tab cut into the bottom edge. A grey footer with circular social icons closes the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 46.0% (plus near-whites #f4f3f3 2.5%, #fffffd 0.8%, #fdffff 0.6%); banner slate #59606a 26.9%; header grey #dcdbdb 13.4%; portrait and wordmark mid-tones #9e9899 6.0% and #483639 3.8%.

Anatomy in DOM order (desktop 1440px):

1. **Header** (`header.header`, 0–80px): background #dddddd. Head-silhouette SVG (30.7px, fill #515151) at x≈261 with 16px right margin; name "Sean Dae Houlihan" at x=308, 20px/400, line-height 30px, #1a1416. Nav right (x=885–1179): "about" "news" "publications" "cv", 20px/400, gap about 24px; active "about" #993333 with a 4px #993333 bar under it. No gap to the banner.
2. **Banner** (`div.daetest__header--container`, 80–380px): #596069 fill, `max-height: 300px`, holding `img.daetest__header--cover` (splash.jpg, 1440×300, `object-fit: contain`): circular portrait with a white ring at x≈120–380, wordmark and subtitle to its right. Gap 17px.
3. **Link row** (`div.social-links-row`, y=397–454, centred): "[" bracket, four icon links, "]" bracket. Brackets 62px/100 #1a1416 and dividers 62px/100 #a1a1a1, both `transform: scaleX(.7) translateY(-15%)`. Each link is a column: Font Awesome / Academicons icon 1.8rem (28.8px), label 16px/400 #993333. Gap 22px.
4. **Bio** (`p.academic-prose-home`, from y=476, x=293, 854px wide): 20px/400, line-height 35px, `text-align: justify`, #1a1416; paragraphs 16px apart, every paragraph after the first indented 1em. Names and institutions are links in #993333, no underline. Four paragraphs end at y=1119.
5. **News label** (`span#newssection`, y=1136): "News" 20px/700 #1a1416. Gap 26px.
6. **First news card** (y=1189, 854×336): begins inside the viewport and runs past the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Brick | #993333 | --color-primary | active nav link and its 4px bar, link-row labels, bio links, news title links, footer link hover |
| Oxblood | #861118 | --color-secondary (oklch(40% .15 25)) | hover color of `.academic-link` |
| Ink | #1a1416 | --color-base-content (oklch(20% .01 0)) | name, nav links, bio, news text, brackets |
| Stone | #776f71 | --color-neutral (oklch(55% .01 0)) | 2px news-card borders, monospace dates, the "~" around news titles |
| Rule Grey | #a1a1a1 | neutral-400 (oklch(70.8% 0 none)) | thin dividers between the link-row icons |
| Fog | #dddddd | --color-body-bg | header bar, footer, 1px tab border on news titles |
| Slate | #596069 | (literal, `.daetest__header--container`) | banner band behind the splash image |
| Paper | #ffffff | --color-base-100 | page background, news cards |
| Footer Ink | #333333 | (literal, `.footer`) | footer text and icons |
| Logo Grey | #515151 | (literal, `.st0`) | head-silhouette logo fill |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| UI / text | -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif | no web text font loads; Segoe UI on Windows, SF Pro on macOS | Inter |
| Dates / code | Menlo, Monaco, Consolas, "Andale Mono", "lucida console", "Courier New", monospace | system Consolas on Windows | JetBrains Mono |
| Icons | Font Awesome 7 (Brands 400, Free 900), Academicons 400 | all three load | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Site name | `.header__brand a` | 20px / 400 / 30px | #1a1416 |
| Nav link | `.navigation__item a` | 20px / 400 / 30px | #1a1416; active #993333 |
| Bio | `.bio-text p.academic-prose-home` | 1.25rem = 20px / 400 / 1.75 = 35px, justified | #1a1416 |
| Section label | `#newssection` | 20px / 700 / 30px | #1a1416 |
| Link-row label | `.social-links-row a span` | 16px / 400 / 24px | #993333 |
| Brackets / dividers | `.social-bracket`, `.social-divider` | 62px / 100 / 93px, scaleX(.7) | #1a1416 / #a1a1a1 |
| News text | `.news-container div` | 16px / 400 / 24px | #1a1416 |
| News date | `span.text-neutral.font-mono` | 16px / 400 / 24px, right-aligned | #776f71 |
| News title | `a.news-title-link` | 16px / 700 / 24px, `font-variant: small-caps`, centred | #993333 |
| Footer note | `.site-info div` | 11.2px / 400 / 15.68px, centred | #333333 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| News card | 24px (`--radius-3xl: 1.5rem`) | 2px solid #776f71 | none |
| News title tab | 24px 0 0 0 (top-left only) | 1px solid #dddddd on top and left | none |
| Footer icon buttons | 50% (37×37px) | none | none |
| Nav active bar | 0 | 4px #993333 block under the item (`:after`) | none |
| Banner portrait | circle with white ring, inside the image | — | — |

No box shadows render anywhere on the page.

## Layout Metrics

- **Containers**: header `.main` max-width 950px with `padding: 0 16px`, centred (x=245–1195 at 1440); page content column x=293, 854px wide (950px minus 3rem side padding); footer `.main` max-width 950px, `padding: 0 3rem`.
- **Header**: height `--navbar-height: 5rem` (80px); brand and nav vertically centred.
- **Banner**: full width, 300px tall at 1440 (image width 100%, height follows the image's aspect, capped at 300px).
- **Bio**: paragraph margins 16px 0; 1em indent from the second paragraph.
- **News cards**: 854px wide, `padding: 8px`, flex row of thumbnail column `flex: 0 0 180px` (120px square image centred, min-height 120px), 10px spacer column, and a text column (644px at x=493); cards 24px apart. Title tab: `margin-top: .5rem; padding: .5rem`.
- **Footer**: #dddddd, `padding: 1rem 0`, 92px tall, centred icon row above the © line.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1024px | 3rem inside 950px | bio 20px / 35px | site name 20px | as described |
| ≤1024px | footer padding 1.5rem | 20px | 20px | — |
| ≤800px | same | 20px | 20px | news thumbnail and spacer columns hidden; title tab loses border, radius and padding |
| <768px | same | bio 18px / 1.6 | 20px | link-row icons 1.5rem, labels .9rem, gap .75rem; nav gap 1rem |
| <600px | same | bio 16px / 1.5 | 16px | site name hidden (`.header__title` display none); nav 16px, gap .75rem; icons 1.3rem |
| <500px | footer padding 1rem | bio 14.4px / 1.4 | — | short name replaces full name; footer icons 2rem |
| <480px | same | 14.4px | — | link-row icons 1.1rem, labels .75rem, gap .35rem |

## Components

- **Nav item** (`.navigation__item`): 20px/400 link in #1a1416 with `transition: all .2s ease-in-out`; hover #993333. Each item has a 4px `:after` bar that is transparent, and #993333 on the active item.
- **Bracketed link row** (`.social-links-row`): inline-flex, gap 1rem; a 62px/100 "[" and "]" in #1a1416 and "|" dividers in #a1a1a1, all squeezed with `transform: scaleX(.7) translateY(-15%)`; each link stacks a 28.8px icon over a 16px #993333 label, no underline, icon turns #993333 on hover.
- **Inline link** (`.academic-link`): #993333, no underline, `transition: color .2s`; hover #861118 with underline.
- **News card** (`.news-container`): white, 2px solid #776f71, radius 24px, padding 8px, flex row. Left: 120×120 thumbnail centred in 180px. Right column: monospace date right-aligned in #776f71; body text 16px/24px with bold names and italic venues; at the bottom a title tab (`.news-title-container`) with a 1px #dddddd top and left border, 24px top-left radius, 8px padding, holding a centred 16px/700 small-caps #993333 link wrapped in "~ " and " ~" in #776f71.
- **Banner**: #596069 band 300px tall with a single splash image (portrait plus wordmark plus subtitle) set `object-fit: contain`.
- **Footer**: #dddddd band; centred row of 37px circular icon buttons in #333333 (Bluesky, GitHub, Scholar, LinkedIn, Email); © line 11.2px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top navigation | yes | 80px #dddddd bar, lowercase 20px links, red active bar |
| Banner / hero | yes | slate band with one raster image containing portrait, wordmark and subtitle |
| Name heading | present but non-standard | the visible name is in the image; the real `h1` is a 1.6px transparent `.mask` for SEO |
| Link buttons | yes | bracketed icon row with grey dividers |
| Bio | yes | 20px justified paragraphs, indented after the first |
| News | yes | rounded bordered cards with thumbnail, mono date and small-caps title tab |
| Publications, CV | yes (other pages) | linked from the nav, not on the home page |
| Results tables, figures | absent from the source | — |
| Footer | yes | grey band with circular icons |

## Adapting to Other Content

- **More news**: repeat the card unchanged; at 1440 a two-line item renders about 166px tall and cards stay 24px apart. Use a square logo or event graphic for the 120px thumbnail, never a wide image.
- **A publication list**: reuse the card with the paper figure as the thumbnail, the year as the mono date, authors and venue as body text (venue italic), and the paper title as the small-caps #993333 tab.
- **A results table**: put it inside the card's 644px text column at 16px/24px, header row 700 #1a1416, cell rules 1px #dddddd; no fills.
- **More links**: extend the bracketed row; at 1440 each icon-plus-label unit is 38–53px wide with a divider between, so eight links still fit in 854px.
- **Without a designed wordmark image**: keep the 300px #596069 band and place a circular portrait plus live text in it rather than leaving it empty; the page has no live hero text to fall back on.

## Do's and Don'ts

- Do use #993333 for every link and active state; there is no second accent.
- Do keep bio text justified at 20px/35px with a 1em indent from the second paragraph.
- Do frame the link row with the thin scaled brackets and grey dividers.
- Do give news titles small caps, 700 weight and the "~" ornaments in #776f71.
- Don't add shadows or fills to the cards; the 2px #776f71 outline and 24px radius are the whole treatment.
- Don't underline links at rest; underline appears only on hover.
- Don't use the red of the wordmark (inside the image) as a UI color; the UI red is #993333.

## Surfaces

White page and white cards; #dddddd header and footer bands; one #596069 slate banner. Cards are separated from the page only by their 2px outline.

## Imagery

A single splash image (circular portrait in a white ring, black heavy wordmark with "dae" in red, black subtitle) on slate; square 120px news thumbnails (event logos, award marks, a calendar icon, paper figures) without frames. Icons from Font Awesome and Academicons.

## Layout

Fixed 80px top bar, full-width banner, then one 854px column: centred link row, justified bio, a bold "News" label and a vertical stack of cards, then the footer band. Generous line height, compact vertical gaps (16–26px).

## Agent Prompt Guide

Quick colors: link and accent #993333, hover #861118, text #1a1416, borders and dates #776f71, dividers #a1a1a1, header/footer #dddddd, banner #596069, page #ffffff.

1. "Build a header: 80px #dddddd bar, content max-width 950px with 16px side padding; left a 30.7px #515151 logo and the name in 20px/400 #1a1416; right lowercase links 20px/400 #1a1416, hover #993333, active link #993333 with a 4px #993333 bar beneath. Under it a full-width #596069 band 300px tall holding the splash image."
2. "Create a news card: white, 2px solid #776f71, border-radius 24px, padding 8px, flex row; a 180px column with a 120px square image, a 10px spacer, then a column with a right-aligned monospace date in #776f71, 16px/24px text in #1a1416, and a bottom tab with 1px #dddddd top and left borders, 24px top-left radius, 8px padding, containing a centred 16px/700 small-caps #993333 link wrapped in '~ ' and ' ~' in #776f71. Stack cards 24px apart."
3. "Make a bracketed link row: inline-flex, gap 1rem, centred; '[' and ']' at 62px weight 100 in #1a1416 and '|' dividers in #a1a1a1, each transformed scaleX(.7) translateY(-15%); links stack a 28.8px icon over a 16px #993333 label, no underline, icon #993333 on hover."

## Similar Pages

- SvelteKit and Jekyll academic homepages that put a designed banner image above a single text column.
- Personal sites that render news as bordered cards with thumbnails rather than a dated list.

## Quick Start

```css
:root {
  --color-primary: #993333;
  --color-secondary: #861118;
  --color-base-content: #1a1416;
  --color-neutral: #776f71;
  --color-divider: #a1a1a1;
  --color-body-bg: #dddddd;
  --banner: #596069;
  --paper: #ffffff;
  --radius-3xl: 1.5rem;
  --navbar-height: 5rem;
  --font-ui: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  --font-mono: Menlo, Monaco, Consolas, "Andale Mono", "lucida console", "Courier New", monospace;
}
body { background: var(--paper); color: var(--color-base-content); font: 400 16px/24px var(--font-ui); }
.bio p { font-size: 1.25rem; line-height: 1.75; text-align: justify; margin: 1rem 0; }
.bio p + p { text-indent: 1em; }
.news-card { border: 2px solid var(--color-neutral); border-radius: var(--radius-3xl); padding: 8px; display: flex; }
.news-title { color: var(--color-primary); font-weight: 700; font-variant: small-caps; text-align: center; }
```

## Provenance

- **URL**: https://daeh.info/
- **Person**: Sean Dae Houlihan, computational cognitive science of emotion; postdoctoral scholar at Stanford per the page.
- **Award**: Glushko Dissertation Prize 2024.
- **Selection reason**: Rule B(2), Glushko Dissertation Prize 2024 winner per https://cognitivesciencesociety.org/glushko-dissertation-prize/ ; homepage linked from his own Bluesky bio (dae.bsky.social).
- **Template credit**: none stated; a SvelteKit build with Tailwind/daisyUI-style tokens, Font Awesome 7.3.1 and Academicons 1.9.6.
- **Evidence used**: tools/computed_style.py render at 1440×900, a per-element style census and full-page capture from the same headless Chrome, and the site's two SvelteKit CSS bundles read directly, on 2026-10-28.
