# Robert Hawkins — Style Reference

> A broadsheet masthead on a white page: a big Playfair name with a fine green rule beneath, then quiet Fira Sans paragraphs whose links are underlined in the same pine green.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of every text node and box, loaded fonts, first-viewport color share, plus a targeted probe of link decoration, nav, header and column boxes at 1440 and 600px), the 1440×900 and full-page screenshots (1,370px tall), and the WordPress.com Seedlet theme stylesheet (`/wp-content/themes/pub/seedlet/style.css` via the `_static` concatenator) read directly for variables and hover rules.

## Overview

A WordPress.com site on the Seedlet theme, white throughout. The masthead is centred: "Robert Hawkins" in 60px bold Playfair Display, black, with a solid 2px pine-green (#3c8067) underline drawn by a repeating background gradient (8px tiles that join into one line), and below it four lowercase Fira Sans nav links (about, publications, personal, CV). After a generous gap the content column (620px) opens with the page title "about" in 32px Playfair. A two-column block row follows: a square 182px portrait in the left column, and on the right a cluster of three black monochrome icon images (envelope, Google Scholar, GitHub) loosely arranged in nested columns. Four 18px Fira Sans paragraphs in #333333 follow, with links in black underlined 1px in #3c8067. A footer line repeats the name in bold Playfair. A small WordPress.com action bar sits at the bottom right of the window.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 89.8% (plus #fcfcfb 1.1%, #fffffe 0.3%, #fdffff 0.1%); greys from the icons and text #ccccca 2.5% and #ecefee 1.4%; portrait tones #322f1d 2.4% and #a99d96 2.4%. The pine-green rule and link underlines are too thin to form a cluster.

Anatomy in DOM order (desktop 1440px; content column x=410–1030):

1. **Header** (`header#masthead`, 0–358px): `padding: 90px 0`, centred.
2. **Site title** (`p.site-title > a`, y=89, 445×80, x=497): "Robert Hawkins", Playfair Display 60px/700 (`calc(1.25 * 48px)`), line-height 78px, #000000; underline from `background-image: linear-gradient(to right, var(--global--color-secondary) 100%, transparent 100%)`, `background-size: 8px 2px`, `background-position: 0 1.22em`, `repeat-x`. Title `margin-bottom: 15px`. Gap about 57px.
3. **Nav** (`.primary-menu-container`, y=226): "about" "publications" "personal" "CV" at x=573, 642, 759, 849; Fira Sans 16px/400, line-height 27.2px, #333333, about 25px apart, each with a transparent 1px bottom border. Header ends at y=358.
4. **Page title** (`h1.entry-title`, y=388): "about", Playfair Display 32px/400, line-height 41.6px, #000000, left-aligned at x=410 (main `padding-top: 30px`). Gap 29px.
5. **Columns row** (`.wp-block-columns`, y=459, 620px): left column x=410, 222px wide, holding a 182×184 portrait at x=430; right column x=668, 362px, holding an envelope icon (71×47 at x=813, y=463) and below it Google Scholar and GitHub icons (99px each at x=710 and x=889, y=540). Row margin-bottom 30px.
6. **Bio** (`p.wp-block-paragraph`, from y=674): Fira Sans 18px/400, line-height 30.6px (1.7), #333333, 30px between paragraphs; links #000000 underlined 1px #3c8067 with a 5.4px offset. The second paragraph ends at the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Ink | #000000 | --global--color-primary / foreground-high-contrast | site title, page title, link text |
| Body Grey | #333333 | --global--color-foreground | paragraphs, nav links, footer |
| Pine | #3c8067 | --global--color-secondary | site-title underline, link underlines, nav hover text and border, site-title hover |
| Pine Hover | #336d58 | --global--color-secondary-hover | secondary hover state (buttons) |
| Paper | #ffffff | --global--color-background | page |
| Selection | #ebf2f0 | --global--color-text-selection | selected text |
| Hairline | #efefef | --global--color-border | theme borders (none visible on the home page) |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Headings / branding | "Playfair Display", Georgia, Times, serif (fonts-api.wp.com) | Playfair Display 400, 700 | Playfair Display |
| Body / nav | "Fira Sans", Helvetica, Arial, sans-serif | Fira Sans 400 | Fira Sans |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Site title | `.site-title a` | 60px / 700 / 78px, centred | #000000 |
| Nav | `.primary-navigation a` | 16px / 400 / 27.2px | #333333 |
| Page title | `h1.entry-title` | 32px / 400 / 41.6px | #000000 |
| Body | `.entry-content p` | 18px / 400 / 1.7 = 30.6px | #333333 |
| Body link | `.entry-content p a` | 18px / 400, underline 1px #3c8067, offset 5.4px | #000000 |
| Footer name | `.site-info .site-name` | Playfair Display 16px / 700 / 27.2px, underlined | #333333 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Site-title underline | — | 8px × 2px gradient tiles at 1.22em, repeat-x | none |
| Nav links | 0 | 1px transparent bottom; #3c8067 on hover | none |
| Portrait and icons | 0 | none | none |
| WordPress action bar (platform chrome) | 4px | none | 0 1px 2px rgba(0,0,0,.12), 0 0 0 1px rgba(0,0,0,.12) |

## Layout Metrics

- **Content width**: `--responsive--aligndefault-width: min(calc(100vw - 2 * 25px), 620px)` → 620px at x=410 at 1440; wide alignment 790px.
- **Header**: `padding: 90px 0` (`--global--spacing-vertical` 30px × 3), 358px tall at 1440.
- **Main**: `padding: 30px 0`; top-level blocks `margin: 30px 0` (`--global--spacing-vertical`).
- **Columns block**: two columns (222px and 362px with a gap of about 36px); the right column nests two more columns for the icons.
- **Footer**: `padding: 30px 0`, starts at y=1283.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥ 670px | (viewport − 620) / 2 | 18px | 60px | two block columns |
| 600px (probed) | 25px (`--global--spacing-horizontal`) | 18px | 60px | block columns stack to 550px each; portrait above icons; nav still inline, x=153 |
| narrow (Seedlet mobile rules) | 25px | 18px | 60px | mobile nav font variables (`--primary-nav--font-size-mobile`) apply |

## Components

- **Masthead title**: Playfair Display 60px/700 black, centred, underlined by an 8px × 2px #3c8067 gradient tile row at 1.22em; on hover the text turns #3c8067 and the underline collapses (`background-size: 8px 0px`).
- **Nav link**: Fira Sans 16px #333333 with a 1px transparent bottom border; hover text #3c8067 and border #3c8067.
- **Body link**: black text, 1px solid underline in #3c8067, 5.4px offset; hover removes the underline and turns the text #3c8067 (`--global--color-primary-hover` resolves to the secondary).
- **Portrait**: square crop, 182×184, unframed.
- **Icon cluster**: black glyph images (envelope, Scholar "g", GitHub octocat) 71–99px wide in nested block columns; they sit at different heights, which reads as a loose arrangement.
- **Footer line**: "Robert Hawkins," in bold Playfair 16px followed by a WordPress mark.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Masthead | yes | centred 60px Playfair name with pine underline |
| Navigation | yes | four lowercase Fira Sans links |
| Page title | yes | 32px Playfair "about" |
| Portrait | yes | 182px square in a block column |
| Contact / profile links | present but non-standard | large black icon images instead of a link row |
| Bio | yes | 18px Fira Sans paragraphs with pine-underlined links |
| Publications | yes (other page) | linked from the nav |
| News | absent from the source | — |
| Footer | yes | bold Playfair name line |

## Adapting to Other Content

- **Profile links**: replace the image icons with a single row of 24px icons or text links under the portrait, spaced 20px; at 1440 a row of five fits in the 362px right column. This removes the uneven placement.
- **News**: an `h2` in Playfair 24px/400 black, then items as 18px/30.6px paragraphs with the date in Fira Sans and linked items underlined in #3c8067; 30px between items.
- **A results table**: 16px Fira Sans #333333 in the 620px column, header row 400 #000000 with a 1px #efefef rule, no fills.
- **Long publication lists**: one 18px paragraph per entry, title as a black link with the pine underline, venue italic; group years under 32px Playfair headings.
- **Wide figures**: use the 790px wide alignment; captions 16px #333333.

## Do's and Don'ts

- Do keep the masthead centred with the name at 60px/700 Playfair and the 2px pine underline.
- Do use #3c8067 only for underlines and hover states; link text stays black.
- Do hold body text to the 620px column at 18px with 1.7 line height.
- Do keep generous vertical space (90px header padding, 30px between blocks).
- Don't fill buttons or backgrounds with the green.
- Don't place large decorative icons beside the portrait at mixed heights; align them in one row.
- Don't use Playfair for body text; it is for the name and titles only.

## Surfaces

White throughout; no bands, cards or tinted panels.

## Imagery

A square headshot with foliage behind, and black monochrome icon images for email, Google Scholar and GitHub. A small seedling emoji follows the lab link.

## Layout

Centred masthead and nav, then a single 620px column: page title, a two-column block (portrait and icons), paragraphs, footer. The page is short (1,370px).

## Agent Prompt Guide

Quick colors: title and link text #000000, body #333333, accent #3c8067, accent hover #336d58, page #ffffff, selection #ebf2f0.

1. "Build a centred masthead with 90px vertical padding: name in Playfair Display 60px/700, line-height 78px, #000000, underlined by background-image linear-gradient(to right, #3c8067 100%, transparent 100%) at background-position 0 1.22em, background-size 8px 2px, repeat-x; 15px below it lowercase Fira Sans 16px #333333 nav links about 25px apart, hover #3c8067 with a 1px #3c8067 bottom border."
2. "Set the content column to 620px: page title in Playfair Display 32px/400 #000000, paragraphs in Fira Sans 18px/1.7 #333333 with 30px between blocks; links #000000 with a 1px #3c8067 underline offset 5.4px, hover text #3c8067 without underline."
3. "Add an about row: two columns in the 620px column, left a 182px square portrait, right a single row of profile icons, then the bio; footer line with the name in bold Playfair 16px #333333."

## Similar Pages

- WordPress.com Seedlet and Twenty Twenty-One personal sites with a centred serif masthead.
- Editorial-style academic homepages pairing Playfair Display with a humanist sans.

## Quick Start

```css
:root {
  --global--color-primary: #000000;
  --global--color-foreground: #333333;
  --global--color-secondary: #3c8067;
  --global--color-secondary-hover: #336d58;
  --global--color-background: #ffffff;
  --global--color-text-selection: #ebf2f0;
  --font-heading: "Playfair Display", Georgia, Times, serif;
  --font-body: "Fira Sans", Helvetica, Arial, sans-serif;
  --content: 620px;
}
body { background: var(--global--color-background); color: var(--global--color-foreground); font: 400 18px/1.7 var(--font-body); }
.site-title a { font: 700 60px/78px var(--font-heading); color: var(--global--color-primary); text-decoration: none;
  background-image: linear-gradient(to right, var(--global--color-secondary) 100%, transparent 100%);
  background-position: 0 1.22em; background-size: 8px 2px; background-repeat: repeat-x; }
.entry-content a { color: var(--global--color-primary); text-decoration: underline 1px var(--global--color-secondary); text-underline-offset: 5.4px; }
.entry-content a:hover { color: var(--global--color-secondary); text-decoration: none; }
```

## Provenance

- **URL**: https://rdhawkins.com/
- **Person**: Robert Hawkins, computational linguistics and social cognition; Assistant Professor of Linguistics at Stanford University per the page.
- **Award**: CogSci 2020 Computational Modeling Prize (Language), first author.
- **Selection reason**: Rule B(3), first author of the CogSci 2020 Computational Modeling Prize paper (Language) per https://cognitivesciencesociety.org/conference-awards/ ; listed as his website on a Stanford Psychology Podcast page, and his lab's people page points to it.
- **Template credit**: WordPress.com, Seedlet theme (`/wp-content/themes/pub/seedlet/`).
- **Evidence used**: tools/computed_style.py render at 1440×900, a per-element style census, a targeted probe at 1440 and 600px and a full-page capture from the same headless Chrome, and the Seedlet stylesheet read directly, on 2026-10-28.
