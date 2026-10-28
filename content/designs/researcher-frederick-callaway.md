# Callaway Lab — Style Reference

> One paragraph and one doodle: grey light-weight prose on white beside a hand-inked thought bubble where a blue dot walks a path to a yellow lightbulb.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of every text node and box, loaded fonts, first-viewport color share), the 1440×900 screenshot (the whole home page fits in it; document height 900px), the site's own `assets/style.css` (7.9 KB, read in full) and `index.html`, and the `assets/lab-logo.svg` source for the logo colors. The page on Frederick Callaway's personal domain is titled "Callaway Lab".

## Overview

A two-column landing page on white with almost nothing else. A small text nav (Home, Publications, People) sits at the top left in 15px, the current page underlined. Below, the left column holds three paragraphs of 19px text in #333333 with a 1.75 line height; topic words ("eye-tracking", "computational tools", "choose", "plan", "remember") are underlined links that filter the publication list. The right column holds the lab logo, a black-outlined thought bubble (with two trailing smaller bubbles) containing the bold words "Callaway Lab", a faint grey network of circles and lines, and a black arrowed path running from a blue (#018be7) node through two white nodes to a yellow (#fdf150) lightbulb. There is no footer, portrait, color accent in the UI or decoration beyond the logo.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 87.8% with near-whites #fafbfb 1.1%, #fdffff 0.5%, #fffffc 0.2%; logo network greys #dadada 2.5% and #f0f0ef 1.9%; text and outline anti-aliasing #b9b9b8 4.4% and #6d6e6f 1.6%. The blue node and yellow bulb are too small to form clusters.

Anatomy in DOM order (desktop 1440px):

1. **Header** (`header.site-header`, max-width 1200px centred at x=120, `padding: 48px 48px 0`, min-height 81px): `nav` at x=168, y=54 (48px padding plus `top: 5.5px`), links 15px/300, line-height 24.75px, #333333, 30px apart; "Home" carries `aria-current` and an underline. The header logo (`.home-brand`) is `visibility: hidden` on the home page above 1100px.
2. **Main** (`main.home`, y=81–871): grid of two equal columns with a 70px gap, `padding: 64px 48px 100px`, `min-height: min(790px, calc(100svh - 81px))` (790px), items vertically centred. A visually hidden `h1` "Callaway Lab" opens it.
3. **Introduction** (`.introduction`, x=168, max-width 517px; first paragraph y=184): 19px/300, line-height 1.75 (33.25px), #333333; paragraphs 1.3em (24.7px) apart; links inherit #333333 with a 1px underline offset .2em. Three paragraphs end at y=733.
4. **Lab logo** (`img.lab-logo` in `.research-display`, x=755, y=248, 517×420): SVG thought bubble, width 100% of the column.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Graphite | #333333 | `:root { color }` | all text, nav, underlines, focus outline |
| Black | #000000 | `a:hover` | link hover text; logo outlines, arrows and "Callaway Lab" lettering |
| Paper | #ffffff | `:root { background }` | page |
| Thought Blue | #018be7 | (SVG fill) | start node of the logo path |
| Bulb Yellow | #fdf150 | (SVG fill) | lightbulb in the logo |
| Network Grey | #d6d6d6 | (SVG stroke) | faint network lines in the logo |
| Node Grey | #c1c1c1 | (SVG stroke) | outlines of the faint network circles |
| Selection | #e8e8e8 | `::selection` background | selected text |
| Detail Grey | #666666 | `.publication-details` | publication details and notes (Publications page only) |
| Pill Line | #dedede | `.publication-filters a` border | filter pills (Publications page only) |
| Pill Fill | #f7f7f7 | `.publication-filters a` background | filter pills (Publications page only) |
| Pill Hover Line | #bbbbbb | hover border | filter pills on hover (Publications page only) |
| Pill Hover Fill | #ededed | hover background | filter pills on hover (Publications page only) |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| All text | "Helvetica Neue", Helvetica, Arial, sans-serif; `font-weight: 300`; `font-synthesis: none` | no web font; Helvetica Neue Light on macOS, Arial (regular, since no 300 face exists) on Windows | Inter 300 |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Root | `:root` | 17px / 300 / 1.65 | #333333 |
| Nav | `nav` | 15px / 300 / 24.75px | #333333 |
| Introduction | `.introduction` | 19px / 300 / 1.75 = 33.25px | #333333 |
| Page heading (other pages) | `main > h1, .page-heading h1` | 30px / 400 / 1.2, letter-spacing -.035em | #333333 |
| Person name (People page) | `.person-copy h2` | 22px / 400, letter-spacing -.025em | #333333 |
| Publication title (Publications page) | `.publication h3` | 17px / 400 / 1.55 | #333333 |
| Publication details | `.publication p` | 14px / 300 / 1.6 | #666666 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Links | — | underline 1px (`text-decoration-thickness: 1px; text-underline-offset: .2em`) | none |
| Focus ring | 0 | `outline: 1px solid #333; outline-offset: 5px` | none |
| Filter pills (Publications page) | 999px | 1px solid #dedede on #f7f7f7 | none |

The home page renders no boxes, borders, radii or shadows.

## Layout Metrics

- **Header**: `max-width: 1200px; margin: 0 auto; padding: var(--header-padding) var(--header-inset) 0` with both variables 48px; nav `gap: 30px`, `top: 5.5px`.
- **Main**: `max-width: 1200px; margin: 0 auto; padding: 64px 48px 100px` on the home page (content x=168–1272 at 1440); grid `1fr 1fr`, `gap: 70px`, so each column is 517px; `align-items: center`.
- **Introduction**: `max-width: 517px`; paragraph spacing `p + p { margin-top: 1.3em }`.
- **Logo**: fills its 517px column (420px tall); its column stretches (`align-self: stretch`) and centres the image.
- **Scrollbar**: `scrollbar-gutter: stable both-edges`.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1100px | 48px | intro 19px | 30px (inner pages) | two columns, logo right, header logo hidden |
| ≤1100px | 48px | 19px | 30px | one column; logo column hidden; the 148px header logo appears top right |
| ≤850px | 48px | 19px | 30px | home padding-top grows to 48px + 36px + 24px |
| ≤800px | 28px; header padding 32px | 17px | 30px | header logo 110px; content gap 32px |
| ≤600px | 24px; header padding 26px | 18px | 28px | nav gap 24px; header logo 73px; content gap 40px |
| ≤380px | 24px | 18px | 28px | extra top padding under the header logo |

## Components

- **Nav link**: 15px/300 #333333, no underline at rest; hover and current page underlined (1px, offset .2em); hover text #000000.
- **Prose link**: inherits #333333, always underlined (1px, offset .2em); hover #000000. On the home page these links are topic filters into the publication list.
- **Lab logo**: a 531×431 viewBox SVG: heavy black cloud outline (stroke 4–5), two small black-outlined trailing bubbles at lower left, "Callaway Lab" in bold black sans, a network of #c1c1c1-outlined white circles joined by #d6d6d6 lines, and a black arrowed path from a #018be7 node through two white nodes to a #fdf150 bulb with radiating black ticks.
- **Filter pill** (Publications page): 13px, `padding: 5px 12px`, 1px solid #dedede, radius 999px, background #f7f7f7; hover border #bbbbbb and background #ededed; current pill #333333 fill with white text.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top navigation | yes | three 15px text links, current one underlined |
| Lab statement | yes | 19px light paragraphs with topic links |
| Logo / illustration | yes | hand-drawn thought-bubble SVG in the right column |
| Recruitment note | yes | last paragraph with an "Email Fred" link |
| Portrait | absent from the source | (the People page uses 190px portraits) |
| Publications | yes (other page) | year groups in a 110px / 1fr grid, filter pills, search field |
| News | absent from the source | — |
| Footer | absent from the source | — |

## Adapting to Other Content

- **News**: add it below the introduction as short 19px paragraphs with the date in 400; keep the 517px measure and 24.7px paragraph spacing rather than a list or cards.
- **A results table or figure**: give it the full 1104px content width below the two-column hero, 14px/1.6 text, 1px #dedede rules, no fills.
- **Long publication lists**: follow the Publications page pattern: year label in a 110px column (15px) beside a 1fr list, 28px between entries, title 17px, details 14px #666666.
- **More people**: a 190px portrait beside the copy, 45px gap, names 22px with -.025em tracking.
- **A different logo**: keep a single black line illustration on white at the column's 517px width; one or two small accents (blue, yellow) at most.

## Do's and Don'ts

- Do let one illustration carry the identity; the UI itself stays monochrome #333333.
- Do keep the introduction at 19px with 1.75 line height and a 517px measure.
- Do underline in-text links with a thin 1px line offset .2em.
- Don't add color to links or buttons; hover only darkens text to #000000.
- Don't add boxes, shadows or dividers on the home page.
- Don't bold body text; the face is set at weight 300 with synthesis turned off.

## Surfaces

A single white surface. No panels, bands or cards.

## Imagery

One hand-drawn-style SVG: a thought bubble with a network graph and an arrowed path to a lightbulb, black outlines with a single blue and a single yellow accent. Portraits appear only on the People page.

## Layout

A 1200px frame with 48px insets: small nav top left, then a vertically centred two-column grid (text left, illustration right, 70px apart). Everything fits in one 1440×900 screen.

## Agent Prompt Guide

Quick colors: text #333333, hover #000000, page #ffffff, logo accents #018be7 and #fdf150, logo greys #d6d6d6 and #c1c1c1.

1. "Build a lab landing page: :root font 'Helvetica Neue', Helvetica, Arial, sans-serif at 17px weight 300, color #333333 on #ffffff; header max-width 1200px with 48px padding; nav of three 15px links 30px apart, current page underlined 1px with .2em offset, hover #000000."
2. "Create the hero: main max-width 1200px, padding 64px 48px 100px, a two-column grid 1fr 1fr with a 70px gap, items centred, min-height 790px; left an introduction at 19px/1.75, max-width 517px, paragraphs 1.3em apart with underlined inline links; right a single SVG illustration at 100% column width."
3. "Draw a logo in the house style: a heavy black thought-bubble outline with two small trailing bubbles, bold black wordmark inside, a faint network of white circles outlined #c1c1c1 joined by #d6d6d6 lines, and a black arrowed path from a #018be7 dot to a #fdf150 lightbulb."

## Similar Pages

- Minimal lab landing pages that pair one statement paragraph with a single illustrated logo.
- Hand-coded static sites with one CSS file and no framework.

## Quick Start

```css
:root {
  --text: #333333;
  --hover: #000000;
  --paper: #ffffff;
  --accent-blue: #018be7;
  --accent-yellow: #fdf150;
  --header-padding: 48px;
  --header-inset: 48px;
  --content-gap: 48px;
  font: 300 17px/1.65 "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-synthesis: none;
  color: var(--text);
  background: var(--paper);
}
a { color: inherit; text-decoration-thickness: 1px; text-underline-offset: .2em; }
a:hover { color: var(--hover); }
nav { display: flex; gap: 30px; font-size: 15px; }
.home { display: grid; grid-template-columns: 1fr 1fr; gap: 70px; align-items: center; max-width: 1200px; margin: 0 auto; padding: 64px 48px 100px; }
.introduction { max-width: 517px; font-size: 19px; line-height: 1.75; }
```

## Provenance

- **URL**: https://fredcallaway.com/
- **Person**: Frederick Callaway, computational cognitive science and resource-rational decision making; the page presents the Callaway Lab in the Cognitive Science program at Dartmouth College.
- **Award**: Glushko Dissertation Prize 2023.
- **Selection reason**: Rule B(2), Glushko Dissertation Prize 2023 winner per https://cognitivesciencesociety.org/glushko-dissertation-prize/ ; linked from his own Bluesky profile (fredcallaway.bsky.social). The page on his personal domain is titled "Callaway Lab".
- **Template credit**: none; a hand-written static site (one `style.css`, one `site.js`).
- **Evidence used**: tools/computed_style.py render at 1440×900, a per-element style census from the same headless Chrome, the screenshot, and `style.css`, `index.html` and `lab-logo.svg` read directly, on 2026-10-28.
