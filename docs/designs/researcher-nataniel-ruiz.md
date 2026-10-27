# Blush Lowercase Bio — Style Reference

> A handwritten note on blush paper: lowercase serif, brick-red underlined links, nothing louder than a bold run-in.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share and DOM boxes from `tools/computed_style.py`), the 1440×900 and full-page screenshots, and the single inline `<style>` block in `index.html` read directly. Source Serif 4 loads from Google Fonts in 400, 600 and 700 and renders everywhere; there is no other stylesheet, script or icon font. The page is 1342px tall at 1440 wide.

## Overview

A one-screen personal page that reads like a letter. The whole body is blush paper #f4ede4 with near-black warm text #1b1714, and every word, including the name, is lowercase. A small rounded headshot (84px, 10px radius) sits left of a 34px/600 serif name with a tight -0.03em tracking; a 12px parenthetical link list "(scholar, twitter, github, linkedin, cv)" follows on the same baseline in muted brown, and a 14px/700 tagline sits under the name. Below, a 720px column of 13px/1.63 serif paragraphs: bold run-in labels ("advising.", "image generative models.") introduce short bullet lists of projects, each project name a brick-red #b54e46 underlined link. There are no headings beyond the h1, no images besides the headshot, no navigation, no footer and no colour other than the link red. The column sits left of centre (left margin 24vw), not centred.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): blush paper #f4ede4 78.0% plus near-identical paper steps #f6efe6 5.5%, #f4ede3 1.9%, #f5ede4 1.7%; anti-aliased text greys #e3dbd2 6.3% and #ada29a 6.1%. The headshot and the red links are below 1% each.

Anatomy in DOM order (desktop 1440px; `main` starts at x=345.6, y=92):

1. **Headshot** (`.hero img`, x=372, y=92): 84×84px, object-fit cover, 10px radius, no border or shadow; sits in a 96px grid column, nudged 8px + 12px right by transforms. Top-aligned with the name.
2. **Name** (`h1`, x=474, y=92, 34px tall): Source Serif 4 34px/600, line-height 1, letter-spacing -1.02px (-0.03em), #1b1714, left aligned, lowercase as typed.
3. **Link list** (`p.links`, same row, baseline-aligned, 10px after the name): 12px/400, line-height 1.4, #5f5349 parentheses and commas; five links in #b54e46, underlined with 0.1em offset.
4. **Tagline** (`p.tagline`, y=134, 8px below the name): 14px/700, line-height 1.35, #1b1714, max-width 470px. The hero block ends at y=176 (bottom of the headshot). Gap 42px.
5. **Bio column** (`section.content`, x=366, y=218, 720px wide): first paragraph 13px/400, line-height 1.63 (21.19px), #1b1714, margin-bottom 11px; then bold run-in labels and bullet lists continue past the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Blush Paper | #f4ede4 | --paper | body background, the whole page |
| Warm Ink | #1b1714 | --text | name, tagline, paragraphs, list items, bold run-ins |
| Muted Brown | #5f5349 | --muted | parentheses and commas of the link list (`.links`) |
| Brick Link | #b54e46 | --link | all links: profile links, project names in the bio |
| Brick Hover | #983d36 | --link-hover | link hover colour |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Serif (everything) | "Source Serif 4", Georgia, serif (Google Fonts) | Source Serif 4 400, 600, 700 | Literata |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `h1` | 34px / 600 / 1, letter-spacing -0.03em | #1b1714 |
| Tagline | `.tagline` | 14px / 700 / 1.35 | #1b1714 |
| Profile links | `.links` | 12px / 400 / 1.4 | #5f5349, links #b54e46 |
| Body | `.content p`, `.content li` | 13px / 400 / 1.63 | #1b1714 |
| Run-in label | `.content p strong` | 13px / 700 | #1b1714 |
| Inline emphasis | `b` inside list items | 13px / 700 | #1b1714 |
| Link | `a` | inherits size, underline offset 0.1em | #b54e46 |

All text is lowercase by authoring, not by `text-transform`.

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Headshot | 10px | none | none |
| Everything else | 0 | none | none |

There are no rules, cards, chips or boxes.

## Layout Metrics

- **Main**: `width: min(760px, calc(100vw - 48px))`, `margin-left: clamp(24px, 24vw, 500px)`, right margin auto, padding 92px 0 70px. At 1440 the column starts at x=345.6, so the page is left-weighted (345px left, 334px right).
- **Hero**: grid `96px 1fr`, column-gap 24px, align-items start, translateX(8px); headshot translateX(12px). Title row is a baseline flex row with 10px gap and wrap.
- **Bio column**: `.content` max-width 720px, margin 42px auto 0 (so 20px inset each side inside the 760px main).
- **Paragraphs**: margin 0 0 11px. Lists: margin 0 0 12px 31px, padding 0; items margin-bottom 4px, padding-left 2px, default disc bullets.
- **Figures**: none.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≤700px | 18px left, main width calc(100vw - 36px), padding 34px 0 48px | 12.5px | 27px (tagline 13px) | hero grid 72px 1fr, 14px gap, headshot 72px, transforms removed; link list wraps to its own full-width line |
| >700px | clamp(24px, 24vw, 500px) left | 13px | 34px | — |

## Components

- **Hero identity row**: 84px square photo with 10px radius, then name 34px/600 #1b1714 tracked -0.03em with a 12px parenthetical link list on its baseline, then a 14px/700 tagline 8px below.
- **Parenthetical link list**: "(" + comma-separated lowercase links + ")" at 12px/400 #5f5349; links #b54e46 with underline offset 0.1em; hover #983d36. No icons.
- **Run-in section label**: a paragraph whose first words are `<strong>` 13px/700 ending in a period ("background."), followed by plain text or a bullet list. This replaces headings.
- **Project bullet**: `ul` indented 31px, disc bullets, 13px/1.63 sentences in first person with the project name as a brick-red underlined link and an occasional bold product name.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Name / tagline | yes | lowercase serif h1 and bold 14px tagline beside the photo |
| Portrait | yes | 84px rounded square, top left |
| Profile links | yes | inline parenthetical list in 12px |
| Bio / research areas | yes | run-in bold labels with bullet lists |
| Background / values | yes | two run-in paragraphs at the end |
| Navigation | absent from the source | none |
| Publication list | absent from the source | papers appear only as links inside bullets |
| News | absent from the source | none |
| Footer | absent from the source | page ends after the last paragraph |
| Section headings | present but non-standard | bold run-in labels instead of h2 |

## Adapting to Other Content

- **A publication list**: keep it as a `ul` under a run-in label ("papers."), one item per paper, 13px/1.63, title as the brick-red link, venue and year in plain text after a comma; no thumbnails.
- **More authors on an entry**: write them inline in the sentence, own name in 700; do not add a second colour.
- **News**: a run-in label "news." followed by a bullet list starting with a lowercase date ("oct 2026:"), same 13px type.
- **A results table**: this style has no table; if one is unavoidable use 13px text, no fills, a 1px #5f5349 rule under the header only.
- **Long pages**: keep the single column and the run-in labels; do not add a sticky nav.

## Do's and Don'ts

- Do keep everything lowercase, including the name and section labels.
- Do keep the whole page on #f4ede4 with #1b1714 text and #b54e46 links only.
- Do keep body text small (13px) with generous 1.63 leading.
- Do keep the column left-weighted with a 24vw left margin.
- Don't add headings, cards, borders, icons or a navbar.
- Don't centre the column or the name.

## Surfaces

One surface: blush paper #f4ede4 edge to edge. The only image is the rounded headshot.

## Imagery

A single colour portrait, cropped square and rounded to 10px. No project thumbnails, teasers or logos.

## Layout

Single column, 760px main block left-offset by 24vw: identity row, then a 720px bio of run-in paragraphs and bullet lists. About 1342px tall at 1440 wide, so most of it fits in two screens.

## Agent Prompt Guide

Quick colors: paper #f4ede4, text #1b1714, muted #5f5349, link #b54e46, link hover #983d36.

1. "Build the identity row: a grid of 96px and 1fr with 24px gap; a 84×84px photo with 10px radius; the name in Source Serif 4 34px/600, line-height 1, letter-spacing -0.03em, #1b1714, lowercase; on the same baseline 10px after it a 12px/1.4 #5f5349 parenthetical list of #b54e46 underlined links; below, 8px down, a 14px/700 tagline."
2. "Write the bio as Source Serif 4 13px/1.63 #1b1714 paragraphs with 11px bottom margin on #f4ede4; start each section with a bold 700 run-in label ending in a period, then a disc list indented 31px with 4px item gaps; project names are #b54e46 links underlined at 0.1em offset, hover #983d36."
3. "Place everything in a main block of min(760px, 100vw - 48px) with margin-left clamp(24px, 24vw, 500px) and padding 92px 0 70px; below 700px use an 18px left gutter, a 72px photo, a 27px name and 12.5px body."

## Similar Pages

- Minimal lowercase researcher pages with a single bio column and inline link lists.
- Text-only "about" pages on a tinted paper background.

## Quick Start

```css
:root {
  --text: #1b1714;
  --muted: #5f5349;
  --link: #b54e46;
  --link-hover: #983d36;
  --paper: #f4ede4;
  --font-serif: "Source Serif 4", Georgia, serif;
}
body { margin: 0; background: var(--paper); color: var(--text); font-family: var(--font-serif); }
main { width: min(760px, calc(100vw - 48px)); margin-left: clamp(24px, 24vw, 500px); padding: 92px 0 70px; }
h1 { font-size: 34px; line-height: 1; font-weight: 600; letter-spacing: -0.03em; margin: 0; }
.content { max-width: 720px; margin: 42px auto 0; }
.content p, .content li { font-size: 13px; line-height: 1.63; }
a { color: var(--link); text-underline-offset: 0.1em; }
a:hover { color: var(--link-hover); }
```

## Provenance

- **URL**: https://natanielruiz.github.io/
- **Person**: Nataniel Ruiz (generative models, personalization).
- **Venue / award**: CVPR 2023 Best Student Paper Honorable Mention, "DreamBooth" (first author). https://cvpr.thecvf.com/Conferences/2023/BestPaperAwards
- **Selection reason**: award rule (first/last author); chosen for its warm blush background, lowercase voice and compact single-column bio.
- **Template credit**: hand-written single HTML file with an inline stylesheet; no template credited.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share, DOM boxes), the 1440×900 and full-page screenshots, and the inline `<style>` of `index.html` read directly, on 2026-10-28.
