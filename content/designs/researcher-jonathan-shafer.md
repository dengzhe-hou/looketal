# Slate Statement Slides — Style Reference

> A keynote opening slide: one full-bleed slate-blue field, a ringed portrait, a 108px name and a centred paragraph you read from across the room.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, loaded fonts, color share), a DOM dump of the second slide, the 1440×900 and full-page screenshots, and `homepage.css`, `examples.css` and the fullPage.js configuration read directly. Almost every size is in `vmin`, so at 1440×900 (vmin = 9px) body text is 18px, the name 108px and the bio 36px. The text family is Calibri, a system font present on the Windows capture machine; Pacifico, Courier Prime and Noto Sans Symbols 2 load from Google Fonts. The page is a fullPage.js deck of four 100vh sections, so the document is only 900px tall and the full-page capture shows the first slide alone.

## Overview

Each section is a full-screen coloured slide: About on slate blue #6f99ac, Publications on orange #fcb052, Teaching on green #63a66d, Contact on purple #a66fac. The About slide centres a 153px round headshot with a 9px #f0f0f0 ring, "Jonathan Shafer" in 108px bold white Calibri, and two 36px white paragraphs whose names (advisors, seminar, programme) are weight 900 links; social icons fade in from below after 2.5s. A fixed top-right menu of translucent pills (About, Publications, Teaching, Contact; 18px bold white, 10px radius) slides in from the right after load and is not yet visible in the capture; a column of fullPage navigation dots sits at the right edge. The Publications slide pairs a 108px #f0f0f0 title with "& Preprints" in Pacifico script, then a numbered 27px list: black weight-900 titles, italic #333333 author lines, "»" bullets with #06547d resource links and bold venues, and awards in dark red #940606 behind a 🟓 star.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): slate blue #6f99ac 78.1% plus #6e99ac 5.1%, #6f99ae 1.8%, #6f99ab 1.5%; pale #d9e4e6 6.9% and light slate #8faebc 5.3% (anti-aliased white text and the portrait ring); #708e9a 0.8% and #8699a0 0.5% (portrait).

Anatomy in DOM order (desktop 1440px; the slide is a full-width centred table cell, no container):

1. **Menu** (`#menu`, fixed top, items float right, `margin-top: 2vw; margin-right: 2vw`): four pills, 18px / 700 white, padding 9px 18px, rgba(255,255,255,0.2) fill (active rgba(0,0,0,0.5)), 10px radius, y=29. They animate in (`animate__fadeInRight`, slow, 0.5s delay) and are absent from the static capture.
2. **Headshot** (`img.headshot`, x=635, y=72, 171×171 including the ring): 17vmin square, `border-radius: 100%`, 1vmin (9px) solid #f0f0f0 border, margin-top 8vmin. Gap 14px.
3. **Name** (`h1.my-name`, y=257, 132px line box): Calibri 108px / 700, #ffffff, centred, margin 1vh 0 2vh. Gap 18px.
4. **Bio 1** (`p.about`, y=407, 1094px wide with 12vw side margins): 36px / 400 / 39.6px (1.1em), #ffffff, centred. Gap 22px.
5. **Bio 2** (y=508): same style, six lines; linked names in weight 900 (Vinod Vaikuntanathan, ML+Cryptography Seminar, Shafi Goldwasser, Amir Shpilka, Amir Yehudayoff, Lautman Interdisciplinary Program); hover turns them blue.
6. **Social icons** (y=844, four links): 70px #f0f0f0 SVGs that start at opacity 0 and fade up to 0.6 between 2.5s and 3.4s; invisible in the capture.
7. **Section dots** (`#fp-nav`, right, x=1402, y=414–474): four small dots 20px apart, the active one larger.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Slate Blue | #6f99ac | `sectionsColor[0]` | About slide background |
| Tangerine | #fcb052 | `sectionsColor[1]` | Publications slide background |
| Sage Green | #63a66d | `sectionsColor[2]` | Teaching slide background |
| Orchid | #a66fac | `sectionsColor[3]` | Contact slide background |
| White | #ffffff | `h1.my-name`, `p.about` | name, bio text and bio links |
| Mist | #f0f0f0 | `h1:not(.my-name)`, `.headshot` | headshot ring, slide titles (Publications, Teaching), Pacifico subtitle, social icon fill |
| Charcoal | #333333 | `body` | publication authors, resource lines, subdued links |
| Black | #000000 | `a.publication-title` | publication and class titles |
| Deep Teal Link | #06547d | `a.publication-resource-link` | "Conference version", "Video", "Slides" links |
| Teaching Link | #036ea6 | `a.class-resource-link` | teaching resource links |
| Award Red | #940606 | `li.award` | award lines and their star bullet |
| Teaching Ink | #1e1e1e | `#section-teaching` | Teaching slide text |
| Contact Ink | #292724 | `#section-contact` | Contact slide text and footer links |
| Menu Pill | rgba(255,255,255,0.2) | `#menu li` | inactive menu pill fill |
| Active Pill | rgba(0,0,0,0.5) | `#menu li.active` | active and hovered menu pill fill |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans | Calibri, "Open Sans", sans-serif | Calibri (Windows system font; not a web font) | Carlito (metric-compatible with Calibri) |
| Script | Pacifico | Pacifico 400 | Pacifico (Google Fonts) |
| Mono | 'Courier Prime' | Courier Prime 400 (email address) | Courier Prime |
| Symbols | "Noto Sans Symbols 2" | Noto Sans Symbols 2 400 (award star) | Noto Sans Symbols 2 |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Base | `body` | 2vmin = 18px | #333333 |
| Name | `h1.my-name` | 6em = 108px / 700 | #ffffff |
| Slide title | `h1:not(.my-name)` | 108px / 700 (line-height 85% on Publications) | #f0f0f0 |
| Script subtitle | `h2.publications-subtitle` | 4.5vmin = 40.5px Pacifico / 400 / 85% | #f0f0f0 |
| Bio | `p.about` | 4vmin = 36px / 400 / 1.1em; links 900 | #ffffff |
| Menu | `#menu li a` | 18px / 700 | #ffffff |
| Publication list | `ol.publication-list` | 1.5em = 27px, decimal numbers | #333333 |
| Publication title | `a.publication-title` | 1.1em = 29.7px / 900 | #000000 |
| Authors | `p.publication-authors` | 27px / 400 italic | #333333 |
| Resource line | `ul.resource-list li` | 27px, "»" bullet, venue in `b` | #333333, links #06547d |
| Award | `li.award` | 29.7px / 900, 🟓 bullet | #940606 |
| Email | `.email-address` | 1.1em Courier Prime bold | #292724 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Headshot | 100% | 9px (1vmin) solid #f0f0f0 | none |
| Menu pill | 10px | none | none |
| Social icon | 0 | none | none |
| Publication list | 0 | none | none |
| Slides | 0 | none | none |

## Layout Metrics

- **Slides**: fullPage.js sections, each 100vh with its own background, content vertically centred (`fp-table`); `scrollOverflow: true` lets the long Publications slide scroll inside itself.
- **About slide**: headshot margin-top 8vmin (72px); name margin 1vh 0 2vh; bio margins 0 12vw (172.8px) so the text measure is 76vw (1094px); `#section-about` padding-bottom 70px reserved for icons.
- **Social icons**: 70px (minimum 50px), margin 5vh 2vw 0.
- **Publications**: title margin-top 5vh; list margin 0 3vw 0 7vw, items 2vh apart; resource items padding-left 1em.
- **Contact**: list margin-left 7vw, font-size 2em; map max 30%; footer absolutely positioned at the bottom, 2.3vh tall, right aligned.
- **Navigation dots**: fullPage `navigation: true`, `navigationPosition: "right"`, with tooltips.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| any width | 12vw for the bio, 7vw / 3vw for lists | 2vmin (18px at 1440×900; 7.8px at 390×844) | 6em of 2vmin (108px at 1440×900; 46.8px at 390×844) | none: there are no media queries; everything scales with the shorter viewport side |

## Components

- **Statement slide**: full-bleed colour field, centred stack of ringed portrait, giant bold name and a large centred paragraph; no cards, no columns.
- **Ringed headshot**: circle at 17vmin with a 1vmin #f0f0f0 border, like a badge.
- **Bold-name links**: inline links inside the bio set in weight 900 in the same white as the text, turning blue on hover; no underline.
- **Pill menu**: fixed top-right `li` pills with a 20% white wash, 10px radius, 18px bold white labels padded 9px 18px; the active pill is 50% black; enters with an animate.css fade from the right.
- **Script subtitle**: "& Preprints" in Pacifico under the 108px "Publications" title, both #f0f0f0 on the orange slide.
- **Publication entry**: decimal-numbered item; 29.7px weight-900 black title; 27px italic authors; "»" bullet lines with #06547d links and a bold venue in parentheses; award lines in #940606 weight 900 with a 🟓 star.
- **Fade-up icons**: social SVGs animate from opacity 0 to 0.6 with a 20px rise, staggered 0.3s.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Portrait | yes | ringed circle at the top of the About slide |
| Name and bio | yes | 108px name, 36px centred paragraphs |
| Navigation | yes | fixed pill menu plus fullPage dots |
| Social links | yes | fading SVG icons |
| Publications | yes | numbered list on an orange slide |
| Awards | yes | dark red lines with a star bullet under each paper |
| Teaching | yes | numbered list on a green slide |
| Contact | yes | Courier Prime email, map, footer on a purple slide |
| News | absent from the source | none |
| Responsive layout | present but non-standard | no breakpoints; vmin scaling only |

## Adapting to Other Content

- **News**: give it its own slide colour (keep the saturated mid-tone family, for example another muted hue at the same lightness) and a numbered 27px list with bold dates.
- **Long publication lists**: they already scroll inside the slide; group by year with a 40.5px Pacifico year label in #f0f0f0.
- **Phones**: add a floor to the vmin sizes (for example `font-size: max(2vmin, 15px)`) since the source shrinks body text below 8px.
- **More authors**: keep authors italic on one line; let them wrap.
- **Awards**: keep the #940606 star line under the paper rather than a badge.

## Do's and Don'ts

- Do give each section one flat full-bleed colour and centre the content.
- Do keep the About slide to portrait, name and one or two large paragraphs.
- Do use weight 900 for linked names and titles instead of colour.
- Don't add borders, shadows or cards; contrast comes from scale and the colour fields.
- Don't mix more than one script line per slide; Pacifico is a single accent.
- Don't rely on the vmin sizes on phones without a minimum.

## Surfaces

Four flat slide colours (#6f99ac, #fcb052, #63a66d, #a66fac); translucent white or black menu pills; nothing else.

## Imagery

A single warm-toned headshot inside a light ring; a Google Map on the Contact slide; social glyphs.

## Layout

Four stacked 100vh slides navigated by scroll, menu or dots: About; Publications & Preprints; Teaching; Contact. The document is 900px tall because fullPage.js moves the slides with transforms.

## Agent Prompt Guide

Quick colors: About #6f99ac, Publications #fcb052, Teaching #63a66d, Contact #a66fac, white text #ffffff, ring and titles #f0f0f0, body #333333, titles #000000, links #06547d, awards #940606.

1. "Build a full-viewport section on #6f99ac with everything centred: a 17vmin round headshot with a 1vmin #f0f0f0 border and 8vmin top margin, then 'Name' in Calibri bold at 6em of a 2vmin base (108px at 1440×900) in #ffffff, then a paragraph at 4vmin with line-height 1.1em, white, side margins 12vw, linked names in weight 900 with no underline."
2. "Add a fixed top-right menu of pills: each li has rgba(255,255,255,0.2) fill and a 10px radius, links 18px bold #ffffff padded 9px 18px, the active pill rgba(0,0,0,0.5); animate them in from the right after load."
3. "Make a publications slide on #fcb052: centred 108px bold #f0f0f0 'Publications' with line-height 85%, under it '& Preprints' in Pacifico 4.5vmin #f0f0f0; then a left-aligned decimal list at 27px with 7vw left margin: titles 1.1em weight 900 #000000, italic #333333 authors, '»' bullet lines with #06547d links, and award lines in #940606 weight 900."

## Similar Pages

- fullPage.js personal sites built as one colour per section.
- Single-statement hero homepages with a ringed avatar.

## Quick Start

```css
:root {
  --about: #6f99ac;
  --pubs: #fcb052;
  --teaching: #63a66d;
  --contact: #a66fac;
  --mist: #f0f0f0;
  --text: #333333;
  --link: #06547d;
  --award: #940606;
}
body { font-family: Calibri, Carlito, "Open Sans", sans-serif; font-size: 2vmin; color: var(--text); }
.section { min-height: 100vh; display: grid; place-content: center; text-align: center; }
#about { background: var(--about); }
img.headshot { width: 17vmin; height: 17vmin; border-radius: 100%; border: 1vmin solid var(--mist); margin-top: 8vmin; }
h1.my-name { font-size: 6em; font-weight: bold; color: #ffffff; margin: 1vh 0 2vh; }
p.about { font-size: 4vmin; line-height: 1.1em; color: #ffffff; margin: 0 12vw; }
p.about > a { color: #ffffff; font-weight: 900; text-decoration: none; }
li.award { color: var(--award); font-weight: 900; }
```

## Provenance

- **URL**: http://shaferjo.com/ (redirects to https://shaferjo.com/)
- **Person**: Jonathan Shafer, learning theory.
- **Award**: NeurIPS 2025 Best Paper Runner-up, "Optimal Mistake Bounds for Transductive Online Learning" (last author). https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/
- **Selection reason**: rule B (last author); chosen for the bold single-statement hero with large type on a slate-blue full-bleed field.
- **Template credit**: built on fullPage.js (its `examples.css` is loaded) with animate.css.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), a DOM dump of the Publications slide, the 1440×900 and full-page screenshots, and `homepage.css`, `examples.css` and the inline fullPage.js configuration read directly, on 2026-10-28.
