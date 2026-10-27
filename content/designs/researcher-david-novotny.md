# Teal Dusk Sidebar — Style Reference

> A harbour at dusk beside a quiet reading room: a fixed teal-to-midnight panel with right-aligned contact lines, and soft grey text with tangerine links on white.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, loaded fonts, color share), selector probes of the sidebar and the JavaScript-built publication rows, the 1440×900 and full-page screenshots, and the HTML5 UP Strata `main.css` and the markup read directly. Source Sans Pro 400 and 400 italic and FontAwesome 4 load. Strata declares body text at 16pt, but its `max-width: 1800px` rule drops it to 12pt (16px), which is what renders at 1440. This v2 file replaces a v1 entry that took the 16pt value and the flat #021a2e sidebar from CSS alone; the render shows a teal gradient photograph over that colour.

## Overview

A two-part page. On the left, a fixed panel 35% wide is filled by a background image that fades from muted teal #48636e at the top to near-black navy #162630 at the bottom, under a faint repeating texture; its contents are right-aligned: a 116px round avatar, "David Novotny" in white, "Computer Vision Researcher" and four FontAwesome icon links (envelope, Twitter, Google, LinkedIn) in 21.6px translucent white, and a small "© David Novotny | Template by: HTML5 UP" line lower down. On the right, a white column (max 864px) holds "About" in a 20px #787878 regular-weight heading, two 16px #a2a2a2 paragraphs with tangerine #ffa64d links on dotted underlines, a 2px #efefef rule, and "Publications": 44 rows built by `make_bib.js`, each with a 219px thumbnail (5.6px radius) on the left and on the right italic grey authors, a #787878 title, venue and year, an optional green #8bbe6a award ("CVPR'25 Best Paper Award"), and tiny outlined buttons with icons (project page, demo, pdf, code).

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 51.4% plus #fffffe 4.9%, #feffff 1.2%; sidebar gradient #162630 10.2%, #48636e 9.2%, #2d414b 8.4%, #20323b 7.8%; warm off-white #f1eeec 6.9% (thumbnail backgrounds and the VGGT preview).

Anatomy in DOM order (desktop 1440px; header 504px fixed at x=0, padding 128px 64px; main from x=504, padding 64px, content 736px at x=568):

1. **Avatar** (`a.image.avatar`, x=324, y=128, 116×136 box): image with `border-radius: 100%`, right-aligned. Gap 24px.
2. **Name** (`#header h1 strong`, y=293): 21.6px / 400 / 37.8px, #ffffff, right aligned.
3. **Role and links** (`#header h1`, y=325–510): 21.6px / 400 / 37.8px, rgba(255,255,255,0.5), right aligned; "Computer Vision Researcher", then email, Twitter handle, "Scholar", "LinkedIn" each with a FontAwesome glyph on the left, one per line.
4. **Copyright** (`#footer`, y=752): 12.8px rgba(255,255,255,0.4), "© David Novotny | Template by: HTML5 UP", the link underlined.
5. **About heading** (`h3`, x=568, y=64): 20px / 400 / 30px, #787878. Gap 30px.
6. **About paragraphs** (y=124 and 252): 16px / 400 / 28px, #a2a2a2; links #ffa64d with 1px dotted bottom borders. Gap 48px to the rule.
7. **Section rule and Publications heading** (rule y=356, 2px #efefef; heading y=406): same 20px #787878 style. Gap 30px.
8. **First publication rows** (y=466 and 656): thumbnail 219×107 at x=568; text column at x=827: italic #a2a2a2 authors, #787878 title, "CVPR 2025, CVPR'25 Best Paper Award" with the award in #8bbe6a, buttons 34px tall at y=582.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Dusk Teal | #48636e | sidebar image (top) | upper part of the sidebar gradient photo |
| Midnight Slate | #162630 | sidebar image (bottom) | lower part of the sidebar gradient photo |
| Midnight Harbor | #021a2e | `#header` background-color | colour under the sidebar overlay and photo (shows only if the image fails) |
| Sidebar White | #ffffff | `#header strong` | name in the sidebar |
| Frosted Text | rgba(255,255,255,0.5) | `#header` color | role line, contact links and icons |
| Copyright Text | rgba(255,255,255,0.4) | `#footer .copyright` | sidebar copyright line |
| Paper White | #ffffff | `body` | content background |
| Body Grey | #a2a2a2 | `body` color | paragraphs, author lists, venue lines |
| Heading Ash | #787878 | `h3`, `strong.hoverable`, `.button` | section headings, paper titles, button labels |
| Tangerine | #ffa64d | `a` | inline links and their dotted underline |
| Burnt Orange | #cc6600 | `a:hover`, `strong.hoverable:hover`, `.button:hover` | hover colour for links, titles and button borders |
| Rule Grey | #efefef | `#main > section`, `.button` | 2px section rule, 3px button borders |
| Laurel Green | #8bbe6a | inline `strong style` | award notes ("CVPR'25 Best Paper Award", "IMC'24 winner") |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans | "Source Sans Pro", Helvetica, sans-serif | Source Sans Pro 400, 400 italic | Source Sans 3 |
| Icons | FontAwesome | FontAwesome 4 | Font Awesome 4.7 |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Base | `body` (12pt under 1800px) | 16px / 400 / 1.75em (28px) | #a2a2a2 |
| Sidebar name | `#header h1 strong` | 1.35em = 21.6px / 400 / 37.8px | #ffffff |
| Sidebar lines | `#header h1` | 21.6px / 400 / 37.8px | rgba(255,255,255,0.5) |
| Section heading | `h3` | 1.25em = 20px / 400 / 30px | #787878 |
| Authors | `#publist em` | 16px / 400 italic / 28px | #a2a2a2 |
| Paper title | `strong.hoverable` | 16px / 400 / 28px (no bold) | #787878; hover #cc6600 over 0.4s |
| Award | inline `strong` | 16px / 400 | #8bbe6a |
| Tiny button | `.button.tiny` | 0.8em = 12.8px / 400 / 2.2em | #787878 |
| Copyright | `#footer .copyright` | 0.8em = 12.8px | rgba(255,255,255,0.4) |

There is no bold anywhere: `strong` renders at 400 because only the 400 weights load and Strata sets headings to 400.

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Avatar | 100% | none | none |
| Thumbnails | 0.35em (5.6px) | none | none |
| Tiny button | 0.35em (4.48px at 12.8px) | 3px solid #efefef; hover #cc6600 | none |
| Section rule | 0 | 2px solid #efefef top | none |
| Inline link | 0 | 1px dotted #ffa64d bottom; transparent on hover | none |
| Sidebar | 0 | none | none |

## Layout Metrics

- **Sidebar**: `#header { position: fixed; width: 35%; height: 100%; padding: 8em 4em; text-align: right; display: flex; flex-direction: column; align-items: flex-end }`; background `url(overlay.png), url(images/fulls/08.jpg.png)` over #021a2e.
- **Main**: `margin-left: 35%; max-width: 54em (864px); padding: 4em`, so at 1440 the text column is 736px.
- **Sections**: `#main > section { border-top: 2px solid #efefef; margin-top: 2em; padding-top: 3em }`, first section without the rule; `h3` margin-bottom 30px.
- **About paragraphs**: Skel `.row` gutter gives them 40px left padding inside a -40px row margin, so text aligns with the heading.
- **Publication row**: `div.row` with `4u` (thumbnail, 219px) and `8u` (text, 477px) columns, 40px gutter; rows about 190px apart.
- **Buttons**: `calc(2.2em + 6px)` tall (34px), padding 0 0.8em, min-width 5em, margin-top 0.3em, 3–4px apart.
- **Page height**: 9,603px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1800px | 64px (4em) | 21.3px (16pt) | 28.8px sidebar name | sidebar 35% |
| 1281–1800px | 64px | 16px (12pt) | 21.6px | sidebar 35%, main max 864px |
| 981–1280px | 48px (3em) | 16px | 20px; sidebar line breaks removed | sidebar 30%, padding 6em 3em 3em; main fills the rest |
| 737–980px | 64px | 16px | 28px | sidebar becomes a static full-width centred banner (image `cover`); main below |
| ≤736px | 24px (1.5em) | 16px | 21.6px | header padding 2.25em 1.5em; sections 2.25em apart; Skel rows stack |

## Components

- **Gradient sidebar**: fixed, full height, a teal-to-midnight photograph under a repeating texture; right-aligned avatar, white name and translucent-white contact lines with FontAwesome icons on the left of each label.
- **Dotted link**: #ffa64d text with a 1px dotted bottom border; on hover the border turns transparent and the text goes #cc6600.
- **Publication row**: 4/8 Skel grid; left a full-width thumbnail with 5.6px corners; right italic grey authors ("Wang, J. and Chen, M. and …"), the title in #787878 at regular weight, venue and year, an optional #8bbe6a award, then tiny buttons.
- **Tiny outline button**: transparent, 3px #efefef border, 4.48px radius, 12.8px #787878 label with a FontAwesome icon before it (lightbulb for project page, desktop for demo, file for pdf, code brackets for code); hover border and label #cc6600.
- **Section rule**: 2px #efefef line above each section after the first.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sidebar identity | yes | avatar, name, role, icon links |
| Bio | yes | two About paragraphs with orange links |
| Publications | yes | 44 thumbnail rows built from `bib_data.js` |
| Awards | present but non-standard | inline green text in the venue line |
| Link buttons | yes | tiny outlined buttons with icons |
| News | absent from the source | none |
| Navigation | absent from the source | sidebar links only |
| Footer | present but non-standard | copyright sits inside the sidebar |

## Adapting to Other Content

- **News**: a section after About, separated by the 2px #efefef rule; each item a 16px #a2a2a2 line with the date in #787878 and links in #ffa64d.
- **Long publication lists**: the rows already scale; add year sub-headings as 20px #787878 `h3`s with the same rule.
- **Papers without thumbnails**: keep the 4u column with a #efefef placeholder so titles align.
- **Awards**: keep the #8bbe6a inline note; do not add badges.
- **Teaching or service**: plain paragraphs or lists in #a2a2a2 with #787878 headings.

## Do's and Don'ts

- Do keep the left panel fixed and photographic, with all its text right-aligned.
- Do use tangerine #ffa64d dotted links and burnt orange #cc6600 for every hover.
- Do keep headings and titles regular weight in #787878.
- Don't fill buttons; they are 3px #efefef outlines.
- Don't add colour to the content column beyond links and the green award note.
- Don't replace the gradient photo with flat #021a2e; the render shows teal fading to navy.

## Surfaces

Two surfaces: the photographic teal-to-midnight sidebar and the flat white content column. Thumbnails sit directly on white.

## Imagery

A round outdoor portrait; a gradient photograph behind the sidebar; per-paper thumbnails (3D reconstructions, grids of object renders, point clouds, animated GIFs for some entries).

## Layout

Fixed sidebar (35%) | content column: About, Publications. About 9,603px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: sidebar gradient #48636e → #162630 (base #021a2e), sidebar name #ffffff, sidebar text rgba(255,255,255,0.5), body #a2a2a2, headings and titles #787878, links #ffa64d, hover #cc6600, rules and button borders #efefef, award #8bbe6a.

1. "Build a fixed left sidebar 35% wide, full height, padding 128px 64px, right-aligned flex column, background a vertical gradient from #48636e to #162630 over #021a2e. Inside: a 116px round avatar, the name in Source Sans Pro 21.6px weight 400 #ffffff, then role and four icon links at 21.6px/37.8px in rgba(255,255,255,0.5)."
2. "Make the content column: margin-left 35%, max-width 864px, padding 64px, white. Section headings 20px weight 400 #787878 with 30px below; 16px/28px #a2a2a2 text; links #ffa64d with a 1px dotted bottom border that becomes transparent on hover while the text turns #cc6600; sections after the first get a 2px #efefef top rule, margin-top 32px, padding-top 48px."
3. "Make a publication row: a 4/8 grid with a 40px gutter; left a thumbnail with 5.6px radius; right italic #a2a2a2 authors, a 16px weight-400 #787878 title that turns #cc6600 on hover, venue and year, an optional #8bbe6a award, and tiny buttons 34px tall with a 3px #efefef border, 4.48px radius, 12.8px #787878 label and a leading icon."

## Similar Pages

- [Jianyuan Wang](https://jytime.github.io/), his student, for a contrasting single-column layout.
- [Idan Attias](https://www.idanattias.com/) for another dark fixed sidebar.

## Quick Start

```css
:root {
  --sidebar-top: #48636e;
  --sidebar-bottom: #162630;
  --sidebar-base: #021a2e;
  --sidebar-text: rgba(255,255,255,0.5);
  --text: #a2a2a2;
  --heading: #787878;
  --link: #ffa64d;
  --link-hover: #cc6600;
  --rule: #efefef;
  --award: #8bbe6a;
}
body { background: #ffffff; color: var(--text); font: 400 16px/1.75em "Source Sans Pro", Helvetica, sans-serif; }
#header { position: fixed; top: 0; left: 0; width: 35%; height: 100%; padding: 8em 4em; text-align: right;
  background: linear-gradient(var(--sidebar-top), var(--sidebar-bottom)) var(--sidebar-base); color: var(--sidebar-text); }
#header strong { color: #ffffff; font-weight: 400; }
#main { margin-left: 35%; max-width: 54em; padding: 4em; }
a { color: var(--link); text-decoration: none; border-bottom: 1px dotted; }
a:hover { color: var(--link-hover); border-bottom-color: transparent; }
.button.tiny { border: 3px solid var(--rule); border-radius: .35em; color: var(--heading); font-size: .8em; height: calc(2.2em + 6px); padding: 0 .8em; }
```

## Provenance

- **URL**: https://d-novotny.github.io/
- **Person**: David Novotny, 3D computer vision.
- **Award**: CVPR 2025 Best Paper, VGGT (last author). https://tc.computer.org/tcpami/awards/cvpr-paper-awards/
- **Selection reason**: existing verified entry, kept; qualifies as last author of VGGT. Chosen for the gradient teal sidebar with the identity block and the publication list with figure thumbnails.
- **Template credit**: "Strata by HTML5 UP" (`main.css` header; sidebar line "Template by: HTML5 UP"), with the accent recoloured from teal #49bf9d to orange.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), selector probes of the sidebar and publication rows, the 1440×900 and full-page screenshots, and `main.css`, the HTML and the `make_bib.js` output as rendered, on 2026-10-28.
