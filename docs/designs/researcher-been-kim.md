# Been Kim — Style Reference

> A typewritten lab notebook: grey PT Mono on white, a hand-lettered name, cobalt links that grow a 2px underline, and every paper pinned beside a periwinkle-matted figure.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of every text node and box, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots (10,951px tall), and the site's own `css/style.css` (a freehtml5.co template, 26.9 KB) plus inline `style` attributes in `index.html`, read directly. The name "Been Kim" is a raster image (`images/logo.png`), not live text.

## Overview

A long one-page profile set entirely in PT Mono at weight 300 (rendering the 400 face) in grey #7b7b7b with 0.05em letter-spacing. A left-aligned text nav (About, Publications, Talks, Media) has a 2px cobalt (#1d2dfd) underline under the active item; two small grey square icons (Twitter, Scholar) sit at the right. The intro pairs a landscape portrait photo with the hand-drawn outline lettering "Been Kim" and three grey mono lines (title, employer, obfuscated email). Below run 12px mono paragraphs with cobalt inline links, an indented "Stuff I help with" list and tutorials. Then come 30px black mono section titles: "Blogs", "Publications" (with a red #ff0000 notice that the list is out of date), "Talks" (with orange #f87431 notes) and media. Each blog and publication item floats a 350px figure thumbnail framed by a 4px periwinkle (#a4b8ee) mat to the left of a 15px bold title, an optional bold TL;DR, 12px authors and a cobalt venue link. A grey "+ Show more..." button expands the list; a small "Designed by: freehtml5.co" credit ends the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 83.4% (plus #fafafb 1.9%, #feffff 0.5%, #fffffe 0.3%); portrait photo tones #9d8a74 4.0% and #4d4334 4.0%; light greys from the photo, icons and text #d4cfd0 3.5% and #eaebed 2.5%.

Anatomy in DOM order (desktop 1440px; Bootstrap container 1170px at x=225, content x=240):

1. **Nav** (`#fh5co-main-nav`, y=102): links PT Mono 16px/300, line-height 24px, letter-spacing 0.8px, #7c7c7c, `padding: 5px 0`, `margin: 0 10px`, each with a transparent 2px bottom border; active "About" has `border-bottom: 2px solid #1d2dfd`. "Talks" renders #1d2dfd because its anchor sits outside an `li`. Two 30px grey square PNG icons (Twitter, Google Scholar) at x=1130, y=104. Gap about 83px.
2. **Portrait** (img, x=240, y=215, 276px tall in a 470px column): landscape outdoor photo, square corners, no frame.
3. **Name** (`images/logo.png`, x=710, y=215, 190×88): hand-drawn outline lettering in black.
4. **Title lines** (`p`, from y=303): "Director (principal scientist)", "at Google DeepMind", "beenkim at csail dot mit dot edu", PT Mono 16px/300, line-height 26px, #7b7b7b, `margin-bottom: 20px`.
5. **Lead sentence** (`div.p12 > b`, y=517): 12px/700 #7b7b7b.
6. **Intro text** (`div.p12`, from y=511, 960px wide): 12px/300, line-height 26px, letter-spacing 0.8px, #7b7b7b; inline links #1d2dfd ("agentic interpretability", "neologism", "PNAS", "Quanta magazine"). Continues below the fold with the keynote line, an indented service list and tutorials.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Typewriter Grey | #7b7b7b | `body { color }` | body text, title lines, paper titles, authors, TL;DR, link hover text, footer |
| Nav Grey | #7c7c7c | `#fh5co-main-nav ul > li > a` | nav links |
| Cobalt | #1d2dfd | `a { color }` | inline links, venue links, active nav underline, 2px hover underline |
| Ink | #000000 | `h1–h6 { color }` | section titles (Blogs, Publications, Talks) and the drawn name |
| Periwinkle Mat | #a4b8ee | `img.fh5co-align-left { background-color }` | 4px frame around blog and publication thumbnails |
| Notice Red | #ff0000 | inline `style="color:red;"` | "I don't keep this list up-to-date anymore…" line |
| Note Orange | #f87431 | inline `style="color:#F87431"` | notes in the Talks list ("This list is seriously out of date", "keynote") |
| Button Grey | #f0f0f0 | `#thebutton` background (browser default) | "+ Show more..." button |
| Paper | #ffffff | `body` background | page |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| All text | "PT Mono", sans-serif (Google Fonts) at weight 300 | PT Mono 400 (only face; bold is synthesized) | PT Mono |
| Name | raster image (`logo.png`) | — | a hand-drawn outline font such as "Rubik Doodle Shadow" only if no drawing is available |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Nav link | `#fh5co-main-nav ul > li > a` | 16px / 300 / 24px, letter-spacing 0.8px | #7c7c7c |
| Body / title lines | `body` | 16px / 300 / 26px, letter-spacing .05em = 0.8px | #7b7b7b |
| Section title | `h4` | 30px / 400 / 42px, margin-bottom 20px | #000000 |
| Intro text | `div.p12` | 12px / 300 / 26px | #7b7b7b |
| Talks list | `div.p13` | 13px / 300 / 26px | #7b7b7b |
| Paper title | `div.paper-title` | 15px / 700 / 26px | #7b7b7b |
| TL;DR | `div.tldr` | 14px / 700 / 26px | #7b7b7b |
| Authors / venue | `div.paper-contents` | 12px / 300 / 26px | #7b7b7b; venue link #1d2dfd |
| Footer credit | `.fh5co-copyright small` | 12.75px / 300 | #7b7b7b |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Thumbnails | 0 | none; 4px #a4b8ee padding acts as a mat | none |
| Links | 0 | 2px solid transparent bottom; #1d2dfd on hover | none |
| Show-more button | 0 | none | none |
| Portrait | 0 | none | none |

## Layout Metrics

- **Container**: Bootstrap 3 `.container` 1170px at ≥1200px with 15px padding (x=225–1215 at 1440, content x=240–1200, 960px).
- **Intro row**: portrait column 470px at x=240 and the name/title column from x=710.
- **Thumbnails**: `img.fh5co-align-left { float: left; width: 350px; padding: 4px; margin: 0 1em .5em 0 }`, so text starts at about x=606 (240 + 350 + 16).
- **Section titles**: `h4` 42px line box plus 20px margin-bottom; sections start about 90px after the previous block.
- **Button**: `#thebutton { padding: 15px 32px; border: none }`, centred, 198×56px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1200px | 15px inside 1170px | 16px (lists 12–13px) | 30px | thumbnails float left at 350px |
| 992–1199px | 15px inside 970px | 16px | 30px | same |
| ≤992px | 15px inside 750px | 16px | 30px | nav list left-aligned, full width |
| ≤768px | 15px, fluid | 16px | 20px / 32px | nav items stack (`display: block`), nav toggle shown |
| ≤480px | 15px | 16px | 20px | thumbnails become 100% wide, no float |

## Components

- **Nav link**: PT Mono 16px #7c7c7c, `padding: 5px 0; margin: 0 10px`, 2px transparent bottom border; hover and active show `border-bottom: 2px solid #1d2dfd`; `transition: all 0.5s ease`.
- **Inline link**: #1d2dfd, no underline at rest; hover text turns #7b7b7b and a 2px #1d2dfd bottom border appears (0.5s ease).
- **Paper item**: floated 350px thumbnail with a 4px #a4b8ee mat; to its right a 15px/700 grey title, optional 14px/700 "TL;DR:" paragraph, 12px author line, and a bracketed cobalt venue link "[ICML 2024]"; items separated by about 30px.
- **Blog item**: same as the paper item with the title line "ICLR 2022 keynote" followed by bold cobalt "talk video" and "blog post" links and a grey parenthetical.
- **Show-more button**: centred, #f0f0f0 fill, no border, `padding: 15px 32px`, PT Mono 16px #7b7b7b "+ Show more...".
- **Service list**: plain text lines indented with spaces under "Stuff I help with:", 12px, cobalt links where relevant.
- **Social icons**: two 30px grey square PNGs at the right end of the nav row.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top navigation | yes | left-aligned mono links with a cobalt underline on the active item |
| Portrait | yes | landscape photo, unframed |
| Name | present but non-standard | hand-drawn lettering as an image |
| Bio | yes | 12px mono paragraphs with cobalt links |
| Service / tutorials | yes | indented plain-text lists |
| Blogs | yes | thumbnail item with periwinkle mat |
| Publications | yes | thumbnail items with TL;DR, collapsed behind "+ Show more..." |
| Talks / media | yes | dense 13px lists with orange notes |
| News | absent from the source | — |
| Footer | yes | small right-aligned template credit |

## Adapting to Other Content

- **News**: a 30px black `h4` "News" followed by 13px mono lines, the date first in 700 #7b7b7b, links cobalt; keep it to plain lines rather than cards.
- **A results table**: 12px PT Mono #7b7b7b with 26px rows, header row 700, a 2px #1d2dfd rule under the header only; no fills.
- **Long publication lists**: keep the 350px matted thumbnail per item and the show-more button after the first ten; at 1440 text beside a thumbnail gets about 594px.
- **Items without a figure**: drop the thumbnail and let the text start at x=240; do not use an empty mat.
- **Notices**: use #f87431 for soft notes; reserve #ff0000 for a single warning line, or leave it out (it reads as a blemish).

## Do's and Don'ts

- Do set everything in PT Mono with 0.05em letter-spacing and grey #7b7b7b text.
- Do frame every paper figure with the 4px #a4b8ee mat and float it left at 350px.
- Do use one blue, #1d2dfd, for links and the 2px hover underline.
- Do keep section titles black 30px mono with no rules or backgrounds.
- Don't add rounded corners, shadows or cards.
- Don't introduce a sans or serif face; the monospace is the identity.
- Don't spread red text around; one warning line is already loud on this page.

## Surfaces

A single white surface. Only the periwinkle thumbnail mats and the pale grey show-more button add tone.

## Imagery

A landscape portrait photo, a hand-drawn outline name, and many paper figures (diagrams, chess boards, plots, screenshots) shown as 350px thumbnails on a periwinkle mat. Social icons are small grey square PNGs.

## Layout

A 1170px Bootstrap container; intro as photo-left, name-right; then one long column of sections, each a 30px title over floated-thumbnail items or dense mono lists.

## Agent Prompt Guide

Quick colors: text #7b7b7b, nav #7c7c7c, link #1d2dfd, titles #000000, thumbnail mat #a4b8ee, note #f87431, button #f0f0f0, page #ffffff.

1. "Style the page in PT Mono: body 16px, weight 300, line-height 26px, letter-spacing .05em, color #7b7b7b on #ffffff; links #1d2dfd with a 2px transparent bottom border that turns #1d2dfd on hover while the text turns #7b7b7b, transition all 0.5s ease."
2. "Create a publication item: a 350px thumbnail floated left with padding 4px and background #a4b8ee, margin 0 1em .5em 0; beside it a 15px/700 #7b7b7b title, a 14px/700 'TL;DR:' sentence, a 12px author line and a bracketed #1d2dfd venue link."
3. "Make a nav row: left-aligned PT Mono 16px #7c7c7c links, padding 5px 0, margin 0 10px, the active one with border-bottom 2px solid #1d2dfd; section titles as h4 30px/42px #000000 with 20px margin-bottom; a centred '+ Show more...' button with #f0f0f0 fill and padding 15px 32px."

## Similar Pages

- Monospace academic homepages built on freehtml5.co and similar one-page templates.
- Profiles that list papers with figure thumbnails instead of plain citations.

## Quick Start

```css
:root {
  --text: #7b7b7b;
  --nav: #7c7c7c;
  --link: #1d2dfd;
  --title: #000000;
  --mat: #a4b8ee;
  --note: #f87431;
  --button: #f0f0f0;
  --paper: #ffffff;
  --font: "PT Mono", monospace;
}
body { background: var(--paper); color: var(--text); font: 300 16px/26px var(--font); letter-spacing: .05em; }
a { color: var(--link); border-bottom: 2px solid transparent; text-decoration: none; transition: all .5s ease; }
a:hover { color: var(--text); border-bottom-color: var(--link); }
h4 { font: 400 30px/42px var(--font); color: var(--title); margin: 0 0 20px; }
.thumb { float: left; width: 350px; padding: 4px; background: var(--mat); margin: 0 1em .5em 0; }
```

## Provenance

- **URL**: https://beenkim.github.io/
- **Person**: Been Kim, machine learning interpretability; Director (principal scientist) at Google DeepMind per the page.
- **Award / event**: CCN 2024 keynote speaker.
- **Selection reason**: Rule B(4), CCN 2024 keynote speaker per https://2024.ccneuro.org/keynote-been-kim/ ; blog URL listed on her own GitHub profile (BeenKim).
- **Template credit**: footer "Designed by: freehtml5.co"; Bootstrap 3 grid.
- **Evidence used**: tools/computed_style.py render at 1440×900, a per-element style census and full-page capture from the same headless Chrome, and `css/style.css` plus `index.html` read directly, on 2026-10-28.
