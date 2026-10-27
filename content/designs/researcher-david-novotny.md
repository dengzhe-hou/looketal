# David Novotny — Style Reference

> A night-sky sidebar beside a pale grey reading room.

**Theme:** light (with a dark fixed sidebar)

Measurements are normalized from the static HTML, `assets/css/main.css` (HTML5 UP "Strata", customized) and the publication builder `assets/js/make_bib.js`; roles are interpreted. Values marked (inferred) are not directly set by a rule I read.

## Overview

This is the HTML5 UP Strata template with its signature split: a fixed left header occupying 35% of the viewport, painted dark navy (#021a2e) under a texture overlay and a full-height background photo, and a light content column on the right with a 54em cap. The sidebar is right-aligned: round avatar, bold white name, a grey "Computer Vision Researcher" line, and Font Awesome icon links for email, Twitter, Scholar and LinkedIn. The owner changed Strata's teal accent (#49bf9d, left in comments) to a warm orange, so links are #ffa64d and hovers deepen to #cc6600. The content column holds only an About section and a JavaScript-built publication list: a 4/8 grid row per paper with a thumbnail on the left and italic authors, a bold hoverable title, venue and year, an optional green award note, and small outlined buttons on the right.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Midnight Harbor | #021a2e | `--sidebar-bg` | Background color of the fixed header (under overlay and photo) |
| Frosted Glass | rgba(255,255,255,0.5) | `--sidebar-text` | Sidebar body text and h1 lines |
| Sidebar White | #ffffff | `--sidebar-strong` | Name (`strong`) and headings inside the sidebar |
| Ember Orange | #ffa64d | `--link` | Links, with a dotted 1px bottom border |
| Burnt Sienna | #cc6600 | `--link-hover` | Link hover, title hover, button hover border and text |
| Sienna Wash | rgba(204,102,0,0.1) | `--button-active` | Button active background |
| Fog Grey | #a2a2a2 | `--text` | Body text |
| Heading Ash | #787878 | `--heading` | h1 to h6 in the content column; button label |
| Button Rim | #efefef | `--button-border` | 3px button border |
| Laurel Green | #8bbe6a | `--award` | Inline award note in publication entries |
| Strata Teal (unused) | #49bf9d | none | Original template accent, kept only in comments and stock rules |
| Paper White | #ffffff | `--bg` | Content background |

## Tokens — Typography

- **Primary:** Source Sans Pro 400 and 400 italic, imported from Google Fonts in `main.css`, fallback `Helvetica, sans-serif`. Substitute: Source Sans 3.
- **Icons:** FontAwesome 4 (`fa-envelope-o`, `fa-twitter`, `fa-google`, `fa-linkedin`, plus per-button icons).
- **Weights:** 400 everywhere; headings are not bold. Bold appears only through `strong`.

| Level | Element | Size | Line height | Notes |
|---|---|---|---|---|
| Base | body | 16pt | 1.75em | #a2a2a2 |
| Sidebar h1 | `#header h1` | 1.35em (1.25em and 1.75em at breakpoints) | 1.75em | rgba white .5 |
| Section | h3 | 1.25em | 1.5em | #787878, weight 400 |
| h4 | h4 | 1.1em | | |
| Paper title | `strong.hoverable` | inherit | | color transitions to #cc6600 on hover |
| Button tiny | `.button.tiny` | 0.8em | 2.2em | min-width 5em |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| Soft corner | 0.35em | Buttons, boxes, images |
| Circle | 100% | Avatar |
| Square | 0 | Header and content blocks |

- **Shadows:** one stock `0 0.1em 0.15em 0 rgba(0,0,0,0.15)` in the template; not a visible motif here.
- **Layout:** `#header { position: fixed; width: 35%; padding: 8em 4em; text-align: right; }`, `#main { margin-left: 35%; max-width: 54em; padding: 4em; }`. The template's global container is 1200px.
- **Avatar:** 7.25em wide in the header.

## Components

- **Fixed header.** Role: identity and contact. Flex column aligned to the right edge, dark navy with overlay texture and a background photo sized `auto 100%`. Text is translucent white; the name in `strong` is solid white.
- **Icon link list.** Role: email, Twitter, Scholar, LinkedIn. FontAwesome icon class on each `a`, stacked with `<br/>`, in the orange link color.
- **Publication row.** Role: one paper. Built by `make_bib.js` as `div.row.100%.uniform` with `div.4u` holding `span.image.fit > img` thumbnail and `div.8u` holding italic authors, `strong.hoverable` title, venue and year, optional `<strong style="color:#8BBE6A">` award note, and buttons.
- **Tiny button.** Role: code, project page, talk links. `a.button.tiny`: transparent fill, 3px #efefef border, 0.35em radius, #787878 label, height calc(2.2em + 6px), padding 0 0.8em, 0.8em font size, FontAwesome icon before the label. Hover turns border and label #cc6600.
- **Link.** Role: inline links. #ffa64d with `border-bottom: dotted 1px`; on hover the dotted border goes transparent and color becomes #cc6600.

## Page Modules

- **Title/author block:** right-aligned sidebar with avatar, name, role and icon links.
- **Bio/photo:** round avatar plus a two-paragraph About section.
- **Publication list:** thumbnail-left rows, rendered client-side from `bib_data.js` (about 44 entries), with award notes in green and small outlined buttons for code, project page and talk.
- **Link buttons:** `.button.tiny` with FontAwesome icons.
- **Venue badge:** none; venue and year are plain text, with notes such as "oral presentation" appended.
- **News, awards section, BibTeX, contact form:** not present.
- **Footer:** "© David Novotny" and "Template by: HTML5 UP".

## Do's and Don'ts

- Do keep the sidebar dark and fixed at about a third of the width, with right-aligned text.
- Do use warm orange links with dotted underlines; the teal Strata accent was deliberately switched off.
- Do keep headings regular weight in mid grey; the template relies on size, not weight.
- Don't make the publication list static HTML if you want parity; the original is generated from a data file.
- Don't add colored venue badges; award notes are inline green text.
- Don't raise text contrast beyond #a2a2a2 body grey without also lifting headings; the low-contrast look is part of Strata.

## Surfaces

Two surfaces: the dark photographic sidebar and the flat white content column. Buttons are outlined, never filled.

## Imagery

A background photograph behind the sidebar (`images/fulls/08.jpg.png`) under a repeating overlay texture, a round avatar, and one thumbnail per paper (some may be GIFs per the data file's `is_gif_thumb` flag).

## Layout

Desktop: fixed header 35% wide (30% at the template's large breakpoint) and the main column offset by the same amount. On smaller screens the template makes the header static and full-width, with the background photo set to cover, and the main column fills the page.

## Agent Prompt Guide

**Quick colors:** sidebar #021a2e, sidebar text rgba(255,255,255,.5), name #ffffff, body #a2a2a2, headings #787878, link #ffa64d, hover #cc6600, award #8bbe6a.

1. "Build a fixed left sidebar 35% wide, background #021a2e with a subtle texture, padding 8em 4em, right-aligned. Round avatar 7.25em, name in bold white, a translucent-white role line, then stacked icon links in #ffa64d."
2. "Create a publication row on a white column: left third a full-width thumbnail with .35em radius, right two-thirds italic authors, a bold title that turns #cc6600 on hover, venue and year, an optional award note in #8bbe6a, and tiny outlined buttons (3px #efefef border, .35em radius, #787878 label, .8em text) with icons."
3. "Style links as #ffa64d with a dotted 1px bottom border that disappears on hover while the color shifts to #cc6600."

## Similar Pages

- [Jianyuan Wang](https://jytime.github.io/), his student, for a contrasting single-column Barron layout.
- [Idan Attias](https://www.idanattias.com/) for another dark fixed sidebar.

## Quick Start

```css
:root {
  --sidebar-bg: #021a2e;
  --sidebar-text: rgba(255,255,255,0.5);
  --sidebar-strong: #ffffff;
  --bg: #ffffff;
  --text: #a2a2a2;
  --heading: #787878;
  --link: #ffa64d;
  --link-hover: #cc6600;
  --button-border: #efefef;
  --award: #8bbe6a;
  --radius: 0.35em;
  --font: "Source Sans Pro", Helvetica, sans-serif;
}
body { background: var(--bg); color: var(--text); font: 400 16pt/1.75em var(--font); }
#header { position: fixed; left: 0; top: 0; width: 35%; height: 100%; padding: 8em 4em; text-align: right; background: var(--sidebar-bg); color: var(--sidebar-text); }
#main { margin-left: 35%; max-width: 54em; padding: 4em; }
a { color: var(--link); border-bottom: dotted 1px; text-decoration: none; }
a:hover { color: var(--link-hover); border-bottom-color: transparent; }
.button.tiny { border: 3px solid var(--button-border); border-radius: var(--radius); color: var(--heading); font-size: .8em; padding: 0 .8em; }
```

## Provenance

- **URL:** https://d-novotny.github.io/
- **Venue/award:** CVPR 2025 Best Paper (last author of VGGT), per https://cvpr.thecvf.com/Conferences/2025/News/Awards_Press
- **Selection reason:** Rule B; link taken from the vgg-t.github.io author list.
- **Template credit:** "Strata by HTML5 UP" (header comment in `main.css`; footer reads "Template by: HTML5 UP"), with the accent recolored from teal to orange.
- **Measurement method:** colors and sizes read from `main.css`, the static HTML and `make_bib.js` via `extract_style.py` and curl. The publication list is built in JavaScript, so its structure is described from the builder script, not from a rendered view; the page was not opened in a browser. The sidebar navy #021a2e comes from `main.css` and was missed by the extractor's frequency table.
