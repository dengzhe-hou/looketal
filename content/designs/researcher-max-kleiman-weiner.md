# Max Kleiman-Weiner — Style Reference

> A tidy faculty card on a lab bench: round portrait and light Montserrat on the left, dense Roboto prose on the right, and a pale grey band where the best papers sit.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of every text node and box, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots (3,838px tall), and the site's own `wowchemy.3accaee08a2055435a0c14df040db522.css` read directly. The site is Wowchemy 5.7.0 for Hugo with the root font size set to 14px (`@media screen and (min-width:58em){html{font-size:14px}}`), so every rem value renders at 14px per rem at 1440.

## Overview

A compact Hugo Academic homepage on white. A 70px sticky white navbar with a soft shadow holds the name in 16.8px bold Roboto at left and three tiny 10.78px links (Bio, Publications, CV) plus a Twitter icon at right. The About section is a two-column Bootstrap row: a centred profile column with a 270px circular portrait, the name in 24.5px light Montserrat, two light grey affiliation lines and a row of blue icons (email, Twitter, Google Scholar, CV); and a wide bio column in 14px Roboto at 80% black with blue (#1565c0) inline links and a bold-led bullet list of research themes. Two publication sections follow, each with the section title in 31.5px Montserrat on the left third and citations on the right two-thirds: "Selected Publications" on a #f7f7f7 band, then the full "Publications" list on white. Each citation shows authors (own name bold), year, title, italic venue and two tiny outlined blue "PDF" and "Cite" buttons. There is no footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 56.9% (plus near-whites #feffff 1.4%, #fffffb 1.2%); the #f7f7f7 publications band, quantized #f8f8f8 16.7% and #f3f4f3 4.5%; portrait greys and text anti-aliasing #d7d9da 11.1% and #959496 7.7%; #f5f8fa 0.5%.

Anatomy in DOM order (desktop 1440px; container x=75–1365 with 15px padding, so content spans x=90–1350):

1. **Navbar** (`nav#navbar-main`, 0–70px, sticky): #ffffff, `box-shadow: 0 .125rem .25rem rgba(0,0,0,.11)` (renders 0 1.75px 3.5px), side padding 14px. Brand "Max Kleiman-Weiner" at x=90, y=20: Roboto 16.8px/700, #2b2b2b. Links "Bio" "Publications" "CV" at x≈1201–1300, y=28: Roboto 10.78px/400, #34495e; then a Twitter icon.
2. **About section** (`section#about`, 70–727px): white, `padding: 50px 0 20px`. Content begins at y=120.
3. **Portrait** (left column, `img.avatar.avatar-circle`, x=155, y=150, 270×270): `border-radius: 50%`, `object-fit: cover`, centred in the 400px column (the `#profile` block has `padding: 30px 10px`). Gap 20px.
4. **Name** (`.portrait-title h2`, y=440): Montserrat 24.5px/300 (1.75em; Montserrat 400 is the lightest face loaded, so it renders at 400), #000000, centred. Gap 10px.
5. **Affiliation** (`.portrait-title h3`, y=481 and 507): "Computational Minds and Machines" / "University of Washington", Montserrat 14px/300, line-height 17.5px, rgba(0,0,0,.54), centred. Gap 10px.
6. **Icon row** (`ul.network-icon`, y≈540): envelope, Twitter, Google Scholar, "cv" icons at `.big-icon` 2rem = 28px, #1565c0, 10px apart; each scales 1.2 on hover.
7. **Bio** (right column, `div.article-style`, x=520, 830px wide, from y=120): paragraphs Roboto 14px/400, line-height 23.1px, rgba(0,0,0,.8), margin-bottom 14px; links #1565c0. A bullet list (x=560) leads each item with a bold label ("Social Learning:", "Cooperation:", "Morality:"). Bio ends near y=700.
8. **Selected Publications band** (`section#featured`, from y=727): #f7f7f7, `padding: 20px 0`; heading "Selected Publications" at x=90, y=747 in Montserrat 31.5px/400, #313131; first citation starts at the same y in the right column.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Ink 80 | rgba(0, 0, 0, 0.8) | (literal, body text) | bio paragraphs, citations, author lists (#333333 on white) |
| Ink Black | #000000 | `.portrait-title h2` | profile name |
| Ink 54 | rgba(0, 0, 0, 0.54) | `.portrait-title h3` | affiliation lines |
| Heading Grey | #313131 | `.section-heading h1` | "Selected Publications", "Publications" |
| Brand Ink | #2b2b2b | `.navbar-light .navbar-brand` | navbar name |
| Nav Slate | #34495e | nav link color | Bio / Publications / CV links |
| Academic Blue | #1565c0 | primary | inline links, profile icons, PDF / Cite button text and border, button hover fill |
| Brand Hover Blue | #2962ff | `.navbar-brand:hover` | navbar name on hover |
| Band Grey | #f7f7f7 | `.home-section` (featured) | Selected Publications band |
| Paper | #ffffff | `.home-section` | navbar, About section, Publications section |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Body | Roboto, sans-serif (Google Fonts, 400 and 700) | Roboto 400, 700 | Inter |
| Headings | Montserrat, sans-serif (Google Fonts, 400 and 700) | Montserrat 400 (weight 300 requests fall back to 400) | Montserrat |
| Icons | Font Awesome 5/6, Academicons 1.9.2 | all load | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Navbar brand | `.navbar-brand` | 1.2rem = 16.8px / 700 / 21px | #2b2b2b |
| Nav links | `.navbar-nav .nav-link` | 10.78px / 400 / 13.475px | #34495e |
| Profile name | `.portrait-title h2` | 1.75em = 24.5px / 300 (renders 400) / 30.625px | #000000 |
| Affiliation | `.portrait-title h3` | 1rem = 14px / 300 (renders 400) / 17.5px | rgba(0,0,0,.54) |
| Section title | `.section-heading h1` | 2.25rem = 31.5px / 400 / 39.375px | #313131 |
| Body / bio | `.article-style p` | 14px / 400 / 23.1px | rgba(0,0,0,.8) |
| Citation authors | `.article-metadata` | 14px / 400 / 23.1px, letter-spacing .03em = 0.42px; own name 700 | rgba(0,0,0,.8) |
| Venue | `.pub-list-item em` | 14px / 400 italic | rgba(0,0,0,.8) |
| PDF / Cite | `a.btn.btn-outline-primary.btn-page-header` | 10px / 400 / 9px | #1565c0 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Navbar | 0 | none | 0 .125rem .25rem rgba(0,0,0,.11) |
| Portrait | 50% (270×270) | none | none |
| PDF / Cite buttons | .2rem = 2.8px | 1px solid #1565c0 | none (focus ring 0 0 0 .2rem rgba(21,101,192,.5)) |
| Sections | 0 | none | none |

## Layout Metrics

- **Container**: `.container-xl` max-width 1290px at ≥1200px, `padding: 0 15px`, centred: x=75–1365 at 1440, content x=90–1350.
- **Columns**: Bootstrap row with `col-12 col-lg-4` (profile, section titles) and `col-12 col-lg-8` (bio, citations); left column x=90–490, right column x=520–1350 (830px) with a 30px gutter.
- **About section**: `padding: 50px 0 20px`; profile block `padding: 30px 10px`, portrait 270px.
- **Publication sections**: `padding: 20px 0`; each `.pub-list-item` has `margin-bottom: 14px`, author line `margin-bottom: 15px`; buttons `padding: 3px 4px`, `margin: 8px 8px 8px 0`.
- **Navbar**: 70px tall at ≥992px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1200px | 15px inside 1290px | 14px | 31.5px | 4 / 8 columns |
| 992–1199px | 15px, container narrower | 14px | 31.5px | 4 / 8 columns |
| <992px | 15px | 14px | 31.5px | columns stack (`col-12`); navbar 50px tall and collapses to a toggler |
| <928px (58em) | 15px | 16px (root font no longer 14px) | 36px | rem values scale up by 16/14 |
| <768px | 15px | 16px | 36px | avatar 200×200 (the theme's 60px section padding rule is overridden by a later `.home-section{padding:20px 0}`) |

## Components

- **Navbar** (`nav.navbar.navbar-expand-lg.navbar-light`): 70px, white, `box-shadow: 0 .125rem .25rem rgba(0,0,0,.11)`, sticky top; brand 16.8px/700 #2b2b2b (hover #2962ff); right-aligned 10.78px links in #34495e and a Twitter icon.
- **Profile card** (`#profile`): centred text, `padding: 30px 10px`; 270px circular portrait; name Montserrat 24.5px #000000 with `margin: 20px 0 10px`; two affiliation lines Montserrat 14px rgba(0,0,0,.54); icon row of 28px #1565c0 icons, 10px apart, `transform: scale(1.2)` on hover.
- **Inline link**: #1565c0, no underline; hover keeps #1565c0 and adds an underline.
- **Research-theme list**: disc bullets indented to x=560, each item starting with a bold "Label:" in 700.
- **Citation** (`.pub-list-item.view-citation`): one paragraph at 14px/23.1px; authors with letter-spacing 0.42px and the owner in 700, starred co-first authors, "(2021)." year, title, italic venue, then two outline buttons.
- **Outline button** (`.btn-outline-primary.btn-page-header`): 10px Roboto #1565c0, 1px solid #1565c0, radius 2.8px, padding 3px 4px, 28×17px; hover fills #1565c0 with white text.
- **Section band**: full-width background (#f7f7f7 or #ffffff) with the title in the left 4 columns and the list in the right 8.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top navigation | yes | sticky 70px white bar with shadow, tiny links |
| Profile / portrait | yes | centred card in the left column |
| Bio | yes | 14px Roboto prose with blue links |
| Research themes | yes | bold-led bullets inside the bio |
| Selected publications | yes | #f7f7f7 band, title left, citations right |
| Full publication list | yes | same pattern on white, reverse chronological |
| PDF / Cite buttons | yes | tiny outline blue buttons |
| News | absent from the source | — |
| Footer | absent from the source | the page ends after the last citation |

## Adapting to Other Content

- **News**: add another full-width section with the title "News" in the left column at 31.5px Montserrat and dated items on the right at 14px/23.1px, the date in 700; alternate the band colour (#f7f7f7 / #ffffff) with its neighbours.
- **More links**: extend the profile icon row; at 1440 each 28px icon with a 10px gap fits about ten across the 380px column.
- **A results table**: in the 830px right column, 14px Roboto rgba(0,0,0,.8), header row 700, 1px rules; never fill cells with blue.
- **Long publication lists**: keep the single list (the page runs to about 3,800px with one list); add year subheads in Montserrat 31.5px only if the list must be split.
- **Projects with images**: place a figure in the 830px column above the citation; keep it unframed.

## Do's and Don'ts

- Do keep a single blue (#1565c0) for links, icons and buttons.
- Do put section titles in the left third and content in the right two-thirds.
- Do alternate white and #f7f7f7 full-width bands to separate sections.
- Do bold the owner's name in every author list.
- Don't enlarge the 10px PDF / Cite buttons; their small size keeps citations quiet.
- Don't add borders or cards around citations; spacing alone separates them.
- Don't use heavy Montserrat; the headings depend on the light 400 face.

## Surfaces

White navbar with a faint drop shadow, white About and Publications sections, and one #f7f7f7 band for Selected Publications. No cards, borders or tinted panels.

## Imagery

One 270px circular portrait (a suited head-and-shoulders photo on a blurred blue background). No other images; icons come from Font Awesome and Academicons.

## Layout

Sticky navbar; a 1290px container; Bootstrap 4/8 split used throughout (profile vs bio, titles vs lists); full-width section bands; dense 14px text with 14px gaps between citations.

## Agent Prompt Guide

Quick colors: text rgba(0,0,0,.8), muted rgba(0,0,0,.54), headings #313131, brand #2b2b2b, nav #34495e, accent #1565c0, band #f7f7f7, page #ffffff.

1. "Build a sticky 70px white navbar with box-shadow 0 .125rem .25rem rgba(0,0,0,.11): the name in Roboto 16.8px/700 #2b2b2b at left (hover #2962ff), tiny links in Roboto 10.78px #34495e at right, inside a 1290px container with 15px padding."
2. "Create a two-column About row (4 / 8 columns, 30px gutter): left a centred profile with a 270px circular photo, name Montserrat 24.5px #000000 (margin 20px 0 10px), affiliations Montserrat 14px rgba(0,0,0,.54), and 28px #1565c0 icons 10px apart that scale 1.2 on hover; right a bio in Roboto 14px/23.1px rgba(0,0,0,.8) with #1565c0 links."
3. "Make a publications band: full-width #f7f7f7, padding 20px 0; title 'Selected Publications' in Montserrat 31.5px/400 #313131 in the left 4 columns; citations on the right at 14px/23.1px with authors letter-spaced 0.42px, the owner in 700, italic venue, then 'PDF' and 'Cite' outline buttons: 10px, #1565c0 text and 1px border, radius 2.8px, padding 3px 4px, hover fill #1565c0 with white text."

## Similar Pages

- Hugo Academic / Wowchemy "about + publications" homepages used across cognitive science and ML.
- Bootstrap faculty pages that put a circular avatar card beside a bio.

## Quick Start

```css
:root {
  --ink: rgba(0, 0, 0, 0.8);
  --ink-muted: rgba(0, 0, 0, 0.54);
  --heading: #313131;
  --brand: #2b2b2b;
  --nav: #34495e;
  --primary: #1565c0;
  --band: #f7f7f7;
  --paper: #ffffff;
  --font-body: "Roboto", sans-serif;
  --font-heading: "Montserrat", sans-serif;
  --container: 1290px;
}
html { font-size: 14px; }
body { background: var(--paper); color: var(--ink); font: 400 1rem/1.65 var(--font-body); }
.section-heading h1 { font: 400 2.25rem/1.25 var(--font-heading); color: var(--heading); }
.btn-pub { font-size: 10px; padding: 3px 4px; border: 1px solid var(--primary); border-radius: .2rem; color: var(--primary); }
.btn-pub:hover { background: var(--primary); color: #fff; }
```

## Provenance

- **URL**: https://faculty.washington.edu/maxkw/
- **Person**: Max Kleiman-Weiner, computational social cognition; Assistant Professor at the University of Washington per the page.
- **Award**: Glushko Dissertation Prize 2019.
- **Selection reason**: Rule B(2), Glushko Dissertation Prize 2019 winner per https://cognitivesciencesociety.org/glushko-dissertation-prize/ ; homepage linked from his own Bluesky profile (maxkw.bsky.social).
- **Template credit**: Wowchemy 5.7.0 for Hugo (generator meta tag), with Bootstrap 4 grid.
- **Evidence used**: tools/computed_style.py render at 1440×900, a per-element style census and full-page capture from the same headless Chrome, and the site's `wowchemy.*.css` read directly, on 2026-10-28.
