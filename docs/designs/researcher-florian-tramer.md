# Florian Tramèr — Style Reference

> A lab notice board framed under glass in a Zürich corridor.

**Theme:** light

Measurements are normalized from the static HTML, `stylesheets/ftramer.css`, `navbar.css` and Bootstrap 5.3.3; roles are interpreted. Bootstrap's full palette appears in the extractor's frequency table, but only the colors traced to visible markup or the custom stylesheet are listed. Values marked (inferred) are Bootstrap defaults that I did not see overridden.

## Overview

A Bootstrap 5 site with one strong idea: the content sits in a single white card (max 1050px, radius 10px, soft 16px shadow) under a light grey navbar. The navbar carries the name as brand and small-caps links (Home, Open Positions, Publications, Talks, Teaching, CV, Blog); the current page is marked with a #E7E7E7 fill. The home card floats a 300px portrait right, runs a short bio, a contact block with outline-primary buttons for Twitter, Scholar and LinkedIn (each with a 16px icon), and then hr-separated blocks for Current group, Alumni, News and "Some of my recorded talks", the last a three-column grid of embedded YouTube iframes and a native video at 16:9. Links are Bootstrap blue without underline; bold-wrapped links are forced red and underlined as a deliberate call-out.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Bootstrap Blue | #0d6efd (inferred default) | `--bs-link-color` | Links; outline-primary button border and text |
| Pressed Blue | #b6d4fe / #86b7fe (inferred) | Bootstrap | Button and focus tints |
| Focus Navy | #0056b3 | none | 2px focus outline on links, buttons, nav links |
| Charcoal Text | #212529 (inferred default) | `--bs-body-color` | Body text |
| Navbar Haze | #f8f9fa (inferred, `bg-light`) | Bootstrap | Header and navbar background |
| Active Tab Grey | #e7e7e7 | none | Background of the current nav item |
| Active Tab Text | #555555 | none | Text of the current nav item |
| Card White | #ffffff | none | Main content card |
| Call-out Red | `red` | none | `b a` links, underlined |
| Award Maroon | #8b0000 on `yellow` | none | `.award` highlight on publication listings |
| Author Bronze | #7e5109 | none | `.author_order` notes |
| Abstract Ice | #ebf4fa | none | Abstract boxes (publications page) |
| BibTeX Fog | #f5f5f5 | none | BibTeX boxes (publications page) |
| Box Border | #cccccc | none | 1px border of abstract and BibTeX boxes |
| Quote Rule | #eeeeee | none | 5px blockquote left border |

## Tokens — Typography

- **Primary:** Bootstrap 5 system stack (`system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", "Noto Sans", "Liberation Sans", Arial, sans-serif`, inferred from Bootstrap defaults). No web fonts.
- **Mono:** `Monaco, "Courier New", Courier, monospace` for BibTeX.
- **Weights:** 400 body; bold for contact labels, talk titles and highlighted news.
- **Variant:** nav links use `font-variant: small-caps`.

| Level | Element | Size | Line height | Notes |
|---|---|---|---|---|
| Brand | `.navbar-brand` | 1.25rem (inferred) | | name |
| Block title | h4 | calc(1.275rem + .3vw), 1.5rem from 1200px (inferred) | 1.2 | Current group, News, talks |
| Body | body | 16px (18px under 767px) | 1.5 | weight 400 |
| Talk button | `.talk_links .btn` | 14px | | compact padding |
| Table header | `.main_table h3` | 1em | | uppercase, right-aligned 140px column (publications page) |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| Card | 10px | `.inner` content card |
| Box | 4px | Abstract and BibTeX boxes |
| Button | Bootstrap `--bs-border-radius` .375rem (inferred) | Outline buttons |

- **Shadows:** card `0 0 16px rgba(0,0,0,0.1)`; Bootstrap focus rings.
- **Layout max-width:** navbar and `.inner` both 1050px, centered; `.outer` 1em side padding (0.625rem on phones).
- **Portrait:** `.imagebox { max-width: 300px; float: right; padding: 0 0 20px 20px; }`, min-height 400px from 1000px.
- **Video grid:** Bootstrap `.col-md-4` with 2px side padding and 20px bottom padding; media `aspect-ratio: 640/360`.

## Components

- **Navbar.** Role: site navigation. `navbar-expand-lg navbar-light bg-light`, 1050px max, small-caps links, current page filled #e7e7e7 with #555 text; collapses to a toggler under lg.
- **Content card.** Role: page body. `.inner` white, 10px radius, 1em padding, soft 16px shadow.
- **Profile buttons.** Role: Twitter, Google Scholar, LinkedIn. `btn btn-outline-primary` with a 16px background-image icon span; hover keeps no underline.
- **News list.** Role: updates. `ul.news` square bullets, 1.25rem indent, 5px between items; bold sentences for calls to action.
- **Talk tile.** Role: recorded talk. Centered `.col-md-4` with an embedded YouTube iframe or `<video controls>` at 16:9, then a title with an italic venue in parentheses.
- **Call-out link.** Role: emphasized link. Any `b a` turns red and underlined.
- **Publication table (publications page).** Role: list papers. Fixed table with a 140px right-aligned uppercase year column, entries as `dl` with bold title links, toggled abstract (#ebf4fa) and BibTeX (#f5f5f5, Monaco) boxes, `.award` in maroon on yellow.

## Page Modules

- **Title/author block:** navbar brand plus floated portrait in the card.
- **Bio/photo:** short bio with press mentions, 300px portrait.
- **Contact:** email (injected by script), office address with a room link, and outline buttons.
- **Group:** current group and alumni lists with destinations ("PhD Student -> Anthropic").
- **News:** square-bulleted list.
- **Teaser media:** "Some of my recorded talks" grid with YouTube iframes and one self-hosted MP4.
- **Publication list, talks, teaching, CV:** separate pages; the publications page has abstract and BibTeX toggles and award highlights.
- **Venue badges:** none on the home page.

## Do's and Don'ts

- Do put the whole page in one white card with a 10px radius and a faint 16px shadow.
- Do use small caps for the nav and a flat grey fill for the active item.
- Do embed talks as a three-up 16:9 grid with captions.
- Don't underline normal links; reserve underline and red for bold call-outs.
- Don't widen past 1050px.
- Don't color award text with the brand blue; the site uses maroon on yellow.

## Surfaces

Light grey navbar strip, white raised card, and on the publications page tinted abstract and BibTeX boxes with 1px #ccc borders.

## Imagery

A 300px portrait (`images/florian2020.png`), 16px brand icons inside buttons, and embedded talk videos with poster frames.

## Layout

Centered 1050px column. Portrait floats right inside the card and becomes centered and unfloated under 600px. Talk tiles use Bootstrap's 12-column grid at three per row from md. Body text grows to 18px on phones.

## Agent Prompt Guide

**Quick colors:** text #212529, link #0d6efd, navbar #f8f9fa, active nav #e7e7e7/#555, card #ffffff, focus #0056b3, award #8b0000 on yellow.

1. "Build a page shell: a light-grey Bootstrap navbar (max 1050px) with the person's name as brand and small-caps links, the active one filled #e7e7e7 with #555 text; below it a single white card, max 1050px, 10px radius, 1em padding, box-shadow 0 0 16px rgba(0,0,0,.1)."
2. "Create a recorded-talks row: three centered columns, each an iframe or video at aspect-ratio 640/360 with no border, followed by a talk title and an italic venue in parentheses."
3. "Make contact buttons: Bootstrap btn-outline-primary with a 16px icon image before the label (Twitter, Google Scholar, LinkedIn), 3px vertical margin, no underline on hover."

## Similar Pages

- [Nicholas Carlini](https://nicholas.carlini.com/), his co-author on the ICML 2024 Best Paper, for a similar card-on-grey layout with a talks section.
- [Angelina Wang](https://angelina-wang.infosci.cornell.edu/) for another Bootstrap 5 faculty page.

## Quick Start

```css
:root {
  --text: #212529;
  --link: #0d6efd;
  --focus: #0056b3;
  --nav-bg: #f8f9fa;
  --nav-active-bg: #e7e7e7;
  --nav-active-fg: #555555;
  --card: #ffffff;
  --award-fg: #8b0000; --award-bg: yellow;
  --radius-card: 10px;
  --content-max: 1050px;
}
body { font-size: 16px; font-weight: 400; line-height: 1.5; color: var(--text); }
a { color: var(--link); text-decoration: none; } a:hover { text-decoration: underline; }
a:focus, .btn:focus { outline: 2px solid var(--focus); outline-offset: 2px; }
.navbar { max-width: var(--content-max); margin: 0 auto 20px; padding: 0 1em; }
.nav-link { font-variant: small-caps; }
.inner { max-width: var(--content-max); margin: 0 auto; padding: 1em; background: var(--card); border-radius: var(--radius-card); box-shadow: 0 0 16px rgba(0,0,0,.1); }
b a { color: red; text-decoration: underline; }
```

## Provenance

- **URL:** https://www.floriantramer.com/
- **Venue/award:** ICML 2024 Best Paper (first author of "Position: Considerations for Differentially Private Learning with Large-Scale Public Pretraining"), per https://icml.cc/virtual/2024/awards_detail
- **Selection reason:** Rule B; homepage taken from his GitHub profile link.
- **Template credit:** none stated; Bootstrap 5.3.3 with a custom `ftramer.css`.
- **Measurement method:** custom rules read from `ftramer.css` and `navbar.css`, structure from the static HTML, via `extract_style.py` and curl. Bootstrap defaults are marked (inferred). Publication-page styles (abstract, BibTeX, award) are described from the shared stylesheet; that page itself was not fetched. Not rendered in a browser.
