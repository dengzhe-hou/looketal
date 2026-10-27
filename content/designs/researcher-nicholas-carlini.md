# Nicholas Carlini — Style Reference

> A hand-set essay in Lora: small-caps masthead, oxblood links, and talk videos that alternate sides like plates in a monograph.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, DOM-order anatomy, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's single inline `<style>` block read directly (there is no external stylesheet). Only Lora 400 loads (self-hosted `/lora.woff2`, `font-display: optional`); bold award text and the masthead's small caps are synthesized by the browser from that one face. Body copy renders at 14pt (18.67px), not the 16px the body declares, because `div.inner` sets `font-size: 14pt`.

## Overview

A writer's homepage built by hand. A white masthead bar, 60px tall with a 1px #d0d0d0 bottom border and a soft 12px shadow, carries "Nicholas Carlini" in 24px small caps with 0.15em tracking on the left and five small-caps links (Main, Papers, Talks, Code, Writing) in oxblood #a02020 on the right. Below it, on a #fefefe page, sits one white 960px column with 5px corners and a barely visible 12px shadow. Inside, Lora 18.67px prose at line-height 27.2px runs in #222222 around a grey contact card floated right: a 300px greyscale portrait with 5% rounding, then name, role, obfuscated email and two links, centred. The bio uses superscript award footnotes and oxblood press links. A 28px "Selected Recent Work" label opens a long sequence of 480×270 videos floated alternately left and right with a paragraph wrapped beside each. There are no headings in the HTML sense, no icons and no color beyond the link red.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): #ffffff 35.2% (column and masthead), #fefefe 33.7% (page ground), #7e7872 13.3% (greyscale portrait and the top of the first video), #eae9e9 11.9% (contact card #f8f8f8 and anti-aliased text), #fcfeff 5.3%. Oxblood link text is under 1% of pixels but is the only hue.

Anatomy in DOM order (desktop 1440px; column x=240–1200, text from x=256):

1. **Masthead bar** (`div.topouter`, y=0–60): #ffffff, padding 16px 0, border-bottom 1px #d0d0d0, box-shadow 0 0 12px rgba(0,0,0,0.1). Gap 24px.
2. **Nav** (`div.links nav`, right, x=809): five links, Lora 19.2px/400 small caps, #a02020, 15.36px right margins, padding-right 2em on the group; DOM-first but floated right.
3. **Name** (`div.title`, left, x≈248): Lora 24px/400 small caps, letter-spacing 3.6px, #000000, margin-left 0.5em. Gap to column 24px.
4. **Contact card** (`div.rightelement`, floated right, x=858, y=110): #f8f8f8, 10px padding, 300×300 portrait (radius 5%), then four centred lines at 18.67px #222222 ending in GitHub | Google Scholar links; card ends at y≈545.
5. **Bio paragraphs** (`div.inner > p`, x=256, y=110, 286, 447): Lora 18.67px/400, line-height 27.2px, #222222, margin-bottom 13px; superscript footnote links at 15.56px #a02020.
6. **Publications line** (y=625): one sentence with three oxblood links. Gap 38px (a `<br>`).
7. **Section label** (`span.header`, y=690): Lora 28px/400, line-height 28px, #222222. Gap 41px.
8. **First video** (`div.video video`, y=763, x=275): 480×270, floated left, paragraph wraps on the right; it crosses the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Oxblood | #a02020 | (literal) | every link: nav, press links, footnote numbers, contact links |
| Ember | #c03030 | (literal) | link hover color |
| Underline Coral | #cc4444 | (literal) | 2px hover underline that scales in under nav and contact links (`div.fancy a::before`) |
| Ink | #222222 | (literal) | body prose, section label, contact card text |
| Masthead Black | #000000 | (inherited) | masthead name |
| Page | #fefefe | (literal) | body background around the column |
| Column White | #ffffff | (literal) | masthead bar, boxed column, footnote popover |
| Card Grey | #f8f8f8 | (literal) | contact card fill |
| Hairline | #d0d0d0 | (literal) | masthead bottom border, contact card right and bottom borders |
| Popover Rule | #aaaaaa | (literal) | footnote popover border |
| Dropdown Edge | rgba(30,30,30,0.5) | (literal) | border of the mobile nav dropdown (≤640px only) |

Declared but not visible on this page: `a.button` maroon (#663333, hover #884444), `span.award` butter (#ffffbb), the `div.header` 2px #dddddd rule, and the mobile publication separators. They belong to the shared stylesheet used by the Papers page.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Serif (everything) | "lora", sans (self-hosted @font-face 'Lora' 400) | Lora 400 only | Source Serif 4 |
| Mono (inline) | monospace (inline style) | system monospace | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Masthead name | `div.title` | 150% = 24px / 400, small caps, letter-spacing 0.15em | #000000 |
| Nav link | `div.links nav a` | 120% = 19.2px / 400, small caps / 27.2px | #a02020 |
| Body prose | `div.inner p` | 14pt = 18.67px / 400 / 27.2px (170% of 16px) | #222222 |
| Section label | `span.header` | 1.5em = 28px / 400 / 28px | #222222 |
| Footnote number | `sup a` | 15.56px / 400, superscript | #a02020 |
| Contact card | `div.rightelement div` | 18.67px / 400, centred | #222222 |
| Popover footnote | `.footnote_content` | inherits 18.67px | #222222 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Masthead bar | 0 | bottom 1px #d0d0d0 | 0 0 12px rgba(0,0,0,0.1) |
| Boxed column | 5px | none | 0 0 12px rgba(0,0,0,0.05) |
| Contact card | 4px | right and bottom 1px #d0d0d0 | 0 0 6px rgba(0,0,0,0.1) |
| Portrait | 5% | none | none |
| Videos | 0 | none | none |
| Footnote popover | 2px | 1px #aaaaaa | 0 2px 10px 2px rgba(0,0,0,0.25) |

## Layout Metrics

- **Column**: `div.outer` max-width 60em = 960px, centred (x=240 at 1440); `div.container` padding 24px 16px 0; `div.boxed` padding 16px; `div.inner` padding-top 8px. Text runs 928px wide from x=256.
- **Masthead**: `div.top` shares the 960px width; the bar is full-bleed.
- **Contact card**: `div.rightouter` 18em (336px) floated right with 10px left padding; card width 16em (≈299px) plus 10px padding.
- **Paragraphs**: margin 0 0 0.7em (13px).
- **Videos**: 480×270 inside `div.video` with 1em (18.67px) side padding; floats alternate left/right; each pair ends with a clearing div and two `<br>`s (about 54px).
- **Page height**: 4,061px at 1440.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >80em (1280px) | auto margins around 960px | 18.67px | 24px small caps | contact card floats right |
| 640–1280px | 16px container + 16px box padding | 18.67px | 24px | unchanged (the left section nav used on other pages slides off-screen) |
| ≤40em (640px) | 16px + 8px box padding | 18.67px | 24px | contact card hidden, a centred `div.contact` with a 10em photo shows above the bio; nav collapses to a 28×3px three-bar hamburger opening a white dropdown with a 1px rgba(30,30,30,0.5) border; videos go full width at 60% padding-top aspect |

## Components

- **Small-caps masthead**: white bar, padding 16px 0, 1px #d0d0d0 bottom border, 0 0 12px rgba(0,0,0,0.1) shadow; name 24px small caps tracked 0.15em in #000000 left; links 19.2px small caps #a02020 right with 15.36px spacing.
- **Draw-in underline** (`div.fancy a`): on hover a 2px #cc4444 bar at the link's baseline scales from scaleX(0) to 0.99 over 0.3s ease; text turns #c03030. Used on nav and contact-card links only; body links just change color.
- **Contact card**: #f8f8f8, padding 10px, radius 4px, right and bottom 1px #d0d0d0, shadow 0 0 6px rgba(0,0,0,0.1); 300×300 portrait with 5% radius; four centred lines of 18.67px text; links separated by a plain "|".
- **Award footnotes**: superscript numbers in #a02020 at 0.7em inside parentheses after each venue name.
- **Hover footnote** (`span.footnote`): bracketed "[a]" link; on hover a fixed popover with #ffffff at 0.95 opacity, 1px #aaaaaa border, 2px radius, 0 2px 10px 2px rgba(0,0,0,0.25) shadow appears; it lingers 1s after mouse-out.
- **Talk row**: `div.video` floated left or right with a 480×270 `<video controls>` (poster frame, preload none); the description paragraph wraps beside it; optional "[View on YouTube]" link below the video.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Masthead with nav | yes | white bar, small caps, oxblood links |
| Bio | yes | four Lora paragraphs with superscript award links |
| Contact card with portrait | yes | grey floated card, greyscale photo |
| Press mentions | yes | inline oxblood links in the bio, no logos |
| Selected work / talks | yes | alternating floated 480×270 videos with prose |
| Publication list | absent from the source | linked to /papers |
| News | absent from the source | — |
| Section headings | present but non-standard | a 28px `span.header` inside a `<p>`, no h-tags |
| Footer | present but non-standard | an empty `div.footer` with only a comment |

## Adapting to Other Content

- **Publication list**: use one `div.publication` per paper at 18.67px, title line with `margin-right: 10em` and right-floated links; bold your own name (`span.me`), and highlight awards with the butter `span.award` (#ffffbb, 3px radius, bold) the stylesheet already defines for the Papers page.
- **News**: a plain list in the same column, date in the same Lora at 400; no badges or color other than #a02020 links.
- **More sections**: repeat the 28px `span.header` label preceded and followed by a `<br>`; do not add rules or colored headings.
- **Images instead of videos**: keep the 480×270 frame (`div.video img` has the same size) and the left/right alternation.
- **Long bios**: stay within the 928px measure; the floated card keeps the first ~440px of text narrower automatically.

## Do's and Don'ts

- Do set everything in one Lora 400 face; hierarchy comes from size (18.67 / 24 / 28px) and small caps only.
- Do keep #a02020 as the only hue; hover is #c03030.
- Do alternate floats for media rows and clear after each.
- Don't add headings with weight or rules; the section label is regular weight.
- Don't add icons or buttons to the masthead or card; links are words separated by "|".
- Don't widen past 960px or tighten the 170% leading.

## Surfaces

A #fefefe page, a full-bleed white masthead with a shadow, one white boxed column with a 5% black shadow, and a #f8f8f8 contact card. Nothing else is filled.

## Imagery

A greyscale portrait and talk-video poster frames (dark stage photos and black title cards with white text). Videos are native HTML5 players with browser controls.

## Layout

Masthead, then a single 960px boxed column: bio wrapped around the floated card, a "Selected Recent Work" label, then eight or so video-and-paragraph rows with alternating sides. About 4,061px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: text #222222, links #a02020 (hover #c03030, underline bar #cc4444), page #fefefe, column #ffffff, card #f8f8f8, hairline #d0d0d0.

1. "Build a masthead: full-width #ffffff bar, padding 16px 0, border-bottom 1px solid #d0d0d0, box-shadow 0 0 12px rgba(0,0,0,0.1); inside a 960px centred row, the name left in Lora 24px/400 small caps, letter-spacing 0.15em, #000000; nav right in Lora 19.2px small caps #a02020 with 15.36px gaps and a 2px #cc4444 underline that scales in from the left on hover."
2. "Make a contact card floated right: #f8f8f8, padding 10px, radius 4px, border-right and border-bottom 1px solid #d0d0d0, box-shadow 0 0 6px rgba(0,0,0,0.1); 300×300 photo with 5% radius; centred Lora 18.67px #222222 lines for name, role, email and 'GitHub | Google Scholar' links in #a02020."
3. "Create a talk row: a 480×270 HTML5 video floated left inside 18.67px side padding, with a Lora 18.67px/27.2px #222222 paragraph wrapping beside it; clear the float and add 54px before the next row, which floats right."

## Similar Pages

- Hand-written single-file academic homepages with an inline stylesheet and one serif face.
- Essay-style personal sites that put talks and side projects ahead of a publication list.

## Quick Start

```css
:root {
  --ink: #222222;
  --link: #a02020;
  --link-hover: #c03030;
  --underline: #cc4444;
  --page: #fefefe;
  --column: #ffffff;
  --card: #f8f8f8;
  --hairline: #d0d0d0;
  --font: 'Lora', serif;
}
body { background: var(--page); font-family: var(--font); line-height: 170%; margin: 0; }
.outer { max-width: 60em; margin: 0 auto; }
.boxed { background: var(--column); border-radius: 5px; padding: 1em; box-shadow: 0 0 12px rgba(0,0,0,0.05); }
.inner { font-size: 14pt; color: var(--ink); }
.title { font-size: 150%; font-variant: small-caps; letter-spacing: .15em; }
a { color: var(--link); text-decoration: none; }
a:hover { color: var(--link-hover); }
```

## Provenance

- **URL**: https://nicholas.carlini.com/
- **Person**: Nicholas Carlini (ML security).
- **Venue / award**: ICML 2024 Best Paper.
- **Selection reason**: Rule B (first author, Stealing Part of a Production Language Model); announcement https://icml.cc/virtual/2024/awards_detail.
- **Template credit**: none; hand-written HTML with an inline stylesheet.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), the 1440×900 and full-page screenshots, and the inline `<style>` and markup read directly, on 2026-10-28. v2 rewrite: v1 listed button and award colors that are declared but not visible on this page.
