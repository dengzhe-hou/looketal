# Kushin Mukherjee — Style Reference

> Cream notepaper with a teal pen: light Roboto prose, a rounded portrait over a typewritten address, and a dated news ledger ruled in turquoise.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of every text node and box, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots (1,482px tall), and the site's own `/assets/css/main.css` (6.2 KB, read in full) on top of Bootstrap 4.6.1. The name and email line declare Raleway, which no stylesheet loads, so they render in the browser's generic sans-serif (Arial on Windows).

## Overview

A compact, al-folio-like personal page on a cream background (#fffef7). A fixed 63px navbar of the same cream, at 95% opacity, has a 1px teal (#009db5) bottom rule; it carries five black social icons at the left (email, Google Scholar, GitHub, Twitter, Bluesky) and four lowercase links at the right (home in teal as the active page, publications, cv, personal). The body sits in an 800px container: the name in 40px, an obfuscated email line, then light 16px Roboto (weight 300) paragraphs with many teal links and one bold keyword. A 231px portrait with 16px rounded corners and a soft two-layer shadow floats right, with the postal address below it in grey Roboto Mono under a teal hairline. A "news" heading leads to a borderless table of dated items, dates in bold on the left. An italic "Last updated" line closes the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): cream #fffef7 71.7% with its neighbours #fffff9 6.6%, #f6f6ef 4.6%, #fefef8 1.3%, #fffef5 1.0%, #fffff7 0.4%; portrait tones #d7e7e4 8.0% and text and photo greys #969591 6.5%. Teal covers too little area to form its own cluster.

Anatomy in DOM order (desktop 1440px; container x=320–1120 with 15px padding, content x=335–1105):

1. **Navbar** (`nav#navbar.navbar.fixed-top`, 0–63px): background #fffef7 at `opacity: 0.95`, `padding: 8px 16px`, `border-bottom: 1px solid #009db5`, no shadow. Left `.navbar-brand.social`: five Font Awesome / Academicons icons, 1.5rem (24px), #000000, hover #009db5. Right links (x=839–1105): Roboto 16px/300, `padding: 8px`, #000000; active "home" #009db5; hover #009db5. Body `padding-top: 56px`. Gap 41px.
2. **Name** (`h1.post-title`, y=104): "Kushin Mukherjee", 40px/500, line-height 48px, #000000 (Raleway declared, generic sans renders), `margin-bottom: 8px`.
3. **Email line** (`p.desc`, y=160): "kushinm at stanford dot edu", 16px/300, #000000, `margin-bottom: 16px`.
4. **Portrait** (`.profile.float-right > img.rounded-rect.z-depth-1`, x=874, y=200, 231×231): `border-radius: 1rem` (16px), `box-shadow: 0 2px 5px 0 rgba(0,0,0,.16), 0 2px 10px 0 rgba(0,0,0,.12)`; the profile column is 30% of the container with `margin-left: 1rem`.
5. **Address** (`.address`, y=443): Roboto Mono 12.8px (0.8rem)/1.5, #828282, `margin-top: 0.75rem`, `padding-top: 0.6rem`, `border-top: 1px solid #009db5`; four lines.
6. **Bio** (`p`, from y=200, x=335, 470px wide beside the float): Roboto 16px/300, line-height 24px, #000000, paragraphs 16px apart; links #009db5, no underline; "visualizations" in 400 bold. The second paragraph runs to y=816.
7. **News heading** (`h2 > a`, y=832): "news", 32px/500, #000000; the table begins at y=878, just below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Cream | #fffef7 | --global-bg-color | page and navbar background |
| Ink | #000000 | --global-text-color | name, bio, nav links, social icons, news text, footer line |
| Teal | #009db5 | --global-theme-color / hover / divider | inline links, active nav link, nav and icon hover, navbar bottom rule, address rule |
| Address Grey | #828282 | --global-text-color-light | postal address under the portrait |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Body / nav / headings | "Roboto", sans-serif (Google Fonts 300–700, italics) | Roboto 300, 300 italic, 400, 500, 700 | Roboto |
| Name and email line | Raleway, sans-serif | not loaded; generic sans-serif (Arial on Windows) | Raleway 500 |
| Address | "Roboto Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace | Roboto Mono 400 | Roboto Mono |
| Icons | Font Awesome 6.7.2, Academicons 1.9.1 | all load | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `h1.post-title` | 40px / 500 / 48px | #000000 |
| Email line | `p.desc` | 16px / 300 / 24px | #000000 |
| Nav link | `.navbar .nav-link` | 16px / 300 / 24px | #000000; active #009db5 |
| Social icons | `.navbar-brand.social` | 1.5rem = 24px | #000000 |
| Body | `body`, `p` | 16px / 300 / 24px | #000000 |
| Emphasis | `strong` | 16px / 400 | #000000 |
| Section heading | `h2` | 32px / 500 / 38.4px | #000000 |
| News date | `.news table th` | 16px / 700 / 24px, nowrap | #000000 |
| News text | `.news table td` | 1rem = 16px / 300 / 24px | #000000 |
| Address | `.profile .address` | 0.8rem = 12.8px / 300 / 1.5 | #828282 |
| Footer | `footer` | 0.8rem = 12.8px / 300 italic, centred | #000000 (a `div` color rule overrides the declared #828282) |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Portrait | 1rem = 16px | none | 0 2px 5px 0 rgba(0,0,0,.16), 0 2px 10px 0 rgba(0,0,0,.12) (`.z-depth-1`) |
| Navbar | 0 | bottom 1px solid #009db5 | none |
| Address block | 0 | top 1px solid #009db5 | none |
| News table | 0 | none (`.news table td, th { border: none }`) | none |

## Layout Metrics

- **Container**: Bootstrap `.container` overridden to `max-width: 800px`, `padding: 0 15px`, centred: x=320–1120 at 1440, content 770px from x=335.
- **Top offset**: `body { padding-top: 56px }` under the fixed 63px navbar; content starts at y=104 (the `.container.mt-5` adds 3rem).
- **Profile float**: `.profile { width: 30% }` at ≥576px (231px), `float: right; margin-left: 1rem`; bio text wraps beside it at 470px.
- **News table**: `table-sm` cells `padding: 4.8px`; date column `padding-right: 1.5rem` (24px), 126px wide; text column 644px.
- **Footer**: `margin-top: 4rem; padding: 1.5rem 0 3rem`, centred.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥800px + gutters | 15px inside 800px | 16px | 40px | portrait floats right at 30% |
| 576–829px | 15px, container narrows to the viewport | 16px | 40px | same float, narrower text |
| <576px | 15px | 16px | 40px | profile becomes 100% wide (portrait full width); navbar collapses to the three-bar toggler (`navbar-expand-sm`) |

## Components

- **Navbar**: fixed, cream at 95% opacity, 1px #009db5 bottom rule; left a row of 24px black icons (hover #009db5); right lowercase 16px/300 links with 8px padding, active #009db5, hover #009db5.
- **Inline link**: #009db5, no underline; hover keeps #009db5 and adds an underline.
- **Rounded portrait**: 231px square, 16px radius, `.z-depth-1` two-layer shadow; under it a Roboto Mono 12.8px #828282 address block with a 1px #009db5 top rule, 9.6px padding-top and 12px margin-top.
- **News ledger**: borderless Bootstrap `table-sm`; left column dates in 700 ("Jul 27, 2026"), nowrap, 24px right padding; right column a sentence or two at 16px/300 with teal links and the odd emoji.
- **Footer note**: centred italic 12.8px "Last updated: …", 4rem above.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top navigation | yes | fixed cream bar with teal rule, social icons left, lowercase links right |
| Name / contact line | yes | 40px name, 16px obfuscated email |
| Portrait | yes | rounded 231px photo with soft shadow, floated right |
| Address | yes | grey Roboto Mono under a teal hairline |
| Bio | yes | light 16px Roboto with dense teal links |
| News | yes | dated borderless table |
| Publications, CV, personal | yes (other pages) | in the nav |
| Footer | yes | italic last-updated line |

## Adapting to Other Content

- **Selected publications on the home page**: add an `h2` (32px/500) and reuse the news-table pattern with the year in the left column (700) and the citation on the right; teal for titles that link.
- **A results table**: Bootstrap `table-sm` without borders, header row 700, body 16px/300; separate the header with a 1px #009db5 rule, matching the navbar and address rules.
- **Long news lists**: keep the table but cap the home page at about five rows; at 1440 a two-line row is about 72px tall.
- **More social links**: add 24px icons to the navbar brand row; at 1440 there is room for about ten before the links.
- **Without a portrait**: drop the float; the bio then runs the full 770px, which is too wide at 16px, so cap paragraphs at 620px.

## Do's and Don'ts

- Do keep the cream #fffef7 background and pure black text.
- Do use #009db5 for every link, rule and hover, and nowhere as a fill.
- Do set body text in Roboto 300 at 16px/24px.
- Do round only the portrait (16px) and give it the soft z-depth shadow.
- Don't add borders to the news table; whitespace and bold dates carry it.
- Don't mix the teal with another accent color.
- Don't rely on Raleway rendering; load it or set the name in Roboto 500.

## Surfaces

One cream surface (#fffef7) for page and navbar; separation from teal hairlines (navbar bottom, address top) and the portrait shadow.

## Imagery

One square headshot with rounded corners and a shadow. Icons from Font Awesome and Academicons in black. Occasional emoji in news items.

## Layout

Fixed navbar; 800px container; name block; bio text wrapping beside a right-floated 30% portrait column; news table full width; centred footer note.

## Agent Prompt Guide

Quick colors: page #fffef7, text #000000, accent #009db5, muted #828282.

1. "Build a fixed navbar: background #fffef7 at opacity .95, padding 8px 16px, border-bottom 1px solid #009db5, no shadow; left a row of 24px black social icons (hover #009db5); right lowercase Roboto 16px/300 links with 8px padding, the active one #009db5. Content in an 800px container with 15px padding."
2. "Create a profile float: right-floated column 30% wide with margin-left 1rem; image with border-radius 1rem and box-shadow 0 2px 5px 0 rgba(0,0,0,.16), 0 2px 10px 0 rgba(0,0,0,.12); below it an address in Roboto Mono 0.8rem/1.5 #828282 with margin-top .75rem, padding-top .6rem and border-top 1px solid #009db5."
3. "Make a news ledger: borderless small table; left cells the date in Roboto 16px/700, nowrap, padding-right 1.5rem; right cells Roboto 16px/300 #000000 with #009db5 links that underline on hover; heading 'news' in 32px/500."

## Similar Pages

- al-folio Jekyll academic sites with a floated profile picture and a dated news table.
- Personal pages that swap the default white for a warm cream background.

## Quick Start

```css
:root {
  --global-bg-color: #fffef7;
  --global-text-color: #000000;
  --global-text-color-light: #828282;
  --global-theme-color: #009db5;
  --font-body: "Roboto", sans-serif;
  --font-mono: "Roboto Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}
body { padding-top: 56px; background: var(--global-bg-color); color: var(--global-text-color); font: 300 16px/24px var(--font-body); }
.container { max-width: 800px; }
a { color: var(--global-theme-color); }
a:hover { text-decoration: underline; }
.navbar { background: var(--global-bg-color); opacity: .95; border-bottom: 1px solid var(--global-theme-color); }
.profile img { border-radius: 1rem; box-shadow: 0 2px 5px 0 rgba(0,0,0,.16), 0 2px 10px 0 rgba(0,0,0,.12); }
.profile .address { margin-top: .75rem; padding-top: .6rem; border-top: 1px solid var(--global-theme-color); font: .8rem/1.5 var(--font-mono); color: var(--global-text-color-light); }
```

## Provenance

- **URL**: https://kushinm.com/
- **Person**: Kushin Mukherjee, cognitive science and visual communication; postdoctoral scholar in the Cognitive Tools Lab at Stanford per the page.
- **Award**: CogSci 2025 Computational Modeling Prize (Applied Cognition), co-first author.
- **Selection reason**: Rule B(3), co-first author of the CogSci 2025 Computational Modeling Prize paper (Applied Cognition) per https://cognitivesciencesociety.org/conference-awards/ ; personal domain whose content says he is a Stanford Cognitive Tools Lab postdoc, matching his Bluesky profile.
- **Template credit**: none stated; the structure and variable names (`--global-theme-color`, `.z-depth-1`, `.profile .address`) follow the al-folio Jekyll theme, on Bootstrap 4.6.1.
- **Evidence used**: tools/computed_style.py render at 1440×900, a per-element style census and full-page capture from the same headless Chrome, and `/assets/css/main.css` read in full, on 2026-10-28.
