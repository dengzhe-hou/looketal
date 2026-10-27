# Jianyuan Wang — Style Reference

> A Jon Barron table page that got a new front door.

**Theme:** light

Measurements are normalized from the static HTML and `stylesheet.css`; roles are interpreted from the markup. Values marked (inferred) are not set by an explicit rule.

## Overview

The body is the familiar Jon Barron academic template: a 1000px centered table, Lato at 16px, blue links that turn orange on hover, `<heading>` and `<papertitle>` custom tags. What is new is the hero. Instead of the classic name-plus-photo table row, a CSS grid `header.hero` sets a large tight-tracked name (clamp 34 to 48px, letter-spacing -0.035em) with the Chinese name in STXingkai calligraphy beside it, a grey intro paragraph at line-height 1.72, slash-separated profile links, and a cropped illustrated portrait in a 203 by 196px window on the right. Below that, everything is text: a News list with bolded award counts and a Selected Publications list with bracketed link rows (Paper, Code, Project Page, Demo, Model). There are no paper thumbnails.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Barron Blue | #1772d0 | `--link` | All links, including the profile-link row |
| Hover Tangerine | #f09228 | `--link-hover` | Link hover and focus |
| Graphite Ink | #20242b | `--text` | Body text color |
| Name Black | #15191f | `--display` | Hero h1 |
| Slate Grey | #414a55 | `--text-soft` | Hero intro paragraph |
| Pewter | #65717e | `--muted` | Chinese name in the hero |
| Slash Grey | #aab0b6 | `--divider` | The `/` separators between profile links |
| Highlight Butter | #ffffd0 | `--highlight` | `span.highlight` background (template rule) |
| Page White | #ffffff | `--bg` | Body background |

## Tokens — Typography

- **Primary:** Lato 400/700 with italics from Google Fonts, fallback `Verdana, Helvetica, sans-serif`. Substitute: Source Sans 3 or Carlito.
- **Calligraphic accent:** `'STXingkai', '华文行楷', cursive` for `.chinese-name` only. Falls back to a system cursive on most non-Mac machines.
- **Weights:** 400 for text, 700 for the name, `strong`, and `papertitle`.

| Level | Element | Size | Line height | Notes |
|---|---|---|---|---|
| Display | `.hero h1` | clamp(34px, 4.1vw, 48px) | 1.08 | 700, letter-spacing -.035em |
| Display accent | `.chinese-name` | .72em of h1 | inherit | 400, #65717e |
| Section | `heading` | 22px | normal | Lato, regular weight |
| Paper title | `papertitle` | 16px | normal | 700 |
| Body | body, td, p, a | 16px | normal | |
| Hero intro | `.hero-copy > p` | 16px (15px under 420px) | 1.72 (1.66) | #414a55 |
| Profile links | `.profile-links a` | 15px | 1.9 under 420px | slash separators |
| Legacy name | `name` | 32px | | template tag, not used in the new hero |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| Radius | 0 | Everything; no rounded corners are defined |

- **Shadows:** none.
- **Layout max-width:** outer table `max-width: 1000px`; hero copy `max-width: 590px`.
- **Hero grid:** `grid-template-columns: minmax(0,1fr) 203px; gap: 42px; min-height: 330px; margin: 32px 20px 24px; padding: 20px`.
- **Rows:** section heading cells `padding: 20px 20px` or `10px 20px`; each news and paper row `padding: 10px 20px`.

## Components

- **Hero.** Role: identity and one-paragraph bio. Grid of text column and a fixed 203px portrait column, vertically centered. Collapses to a single column under 840px with the portrait centered beneath (width min(100%, 234px), height 157px).
- **Profile links.** Role: Scholar, Twitter, GitHub, CV. Flex row of #1772d0 links at 15px separated by `::after { content: '/'; margin: 0 9px; color: #aab0b6; }`.
- **Portrait stage.** Role: illustrated avatar. `overflow: hidden` 203 by 196px window; the 504px-wide image is absolutely positioned at right -5px, bottom -2px, so only a crop of a larger illustration shows.
- **Section heading.** Role: "News", "Selected Publications". Template `<heading>` tag at 22px Lato regular, no rule or color change.
- **News item.** Role: one update. `div` with `text-indent: 2em` wrapping an `li`; paper names set in `papertitle` bold, award ratios in `strong` (for example "Best Paper Award (1/13008)").
- **Publication entry.** Role: one paper. Four stacked divs: linked bold `papertitle`, author line with own name in `strong`, venue line with award in `strong`, then a row of bracketed links `[Paper] [Code] [Project Page] [🤗 Demo] [Model] [Slides]`.

## Page Modules

- **Title/author block:** custom grid hero with English and Chinese names, supervisors in the intro, and profile links.
- **Bio/photo:** illustrated, cropped portrait instead of a photo.
- **News:** bulleted rows with bold paper names and award counts.
- **Publication list:** "Selected Publications", text only, no thumbnails; award noted inline after the venue.
- **Link buttons:** bracketed text links, including Hugging Face demo and model links.
- **Awards:** appear inside News and venue lines rather than as a separate section.
- **Venue badge, BibTeX, teaser media, contact form:** not present.
- **Footer:** right-aligned "Thanks to the template from Jon Barron".

## Do's and Don'ts

- Do keep Lato at 16px and the #1772d0 to #f09228 link pair; it signals the Barron lineage.
- Do give the name tight negative tracking and a large clamp size; the hero is the only modern element.
- Do use bold counts like "(1/13008)" for awards instead of colored badges.
- Don't add thumbnails or cards to publication rows; the page is text below the hero.
- Don't use the calligraphic font for anything but the Chinese name.
- Don't add borders or shadows; separation is whitespace only.

## Surfaces

A single white canvas. No panels, no tinted bands, no dividers. The portrait window is the only clipped region.

## Imagery

One illustrated portrait (`images/profile_smile.png`), cropped through a fixed window. No paper images.

## Layout

Centered 1000px column. Hero is a two-column grid (text and 203px portrait) that stacks under 840px; at 420px the name drops to 34px and the intro to 15px. Content rows below are full-width table cells with 20px side padding.

## Agent Prompt Guide

**Quick colors:** text #20242b, name #15191f, intro #414a55, link #1772d0, hover #f09228, separators #aab0b6, background #ffffff.

1. "Build a hero: CSS grid with a text column and a 203px portrait column, gap 42px, min-height 330px. Name in Lato 700 at clamp(34px, 4.1vw, 48px), line-height 1.08, letter-spacing -.035em, color #15191f; a native-script name beside it at .72em in #65717e. Intro paragraph #414a55 at 16px/1.72, then links separated by grey slashes."
2. "Create a publication row: bold Lato 16px linked title in #1772d0, author line with the owner's name in bold, a venue line like 'CVPR, 2025 (Best Paper Award)' with the award in bold, and a row of bracketed links [Paper] [Code] [Project Page] [Demo]."
3. "Make a news list: rows with 10px 20px padding, 2em text indent, bullet items that bold the paper name and an award ratio."

## Similar Pages

- [Jon Barron](https://jonbarron.info/), the template source.
- [David Novotny](https://d-novotny.github.io/), his co-advisor in this batch, for a contrasting sidebar template.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #20242b;
  --display: #15191f;
  --text-soft: #414a55;
  --muted: #65717e;
  --divider: #aab0b6;
  --link: #1772d0;
  --link-hover: #f09228;
  --highlight: #ffffd0;
  --font: 'Lato', Verdana, Helvetica, sans-serif;
  --content-max: 1000px;
}
body { margin: 0; color: var(--text); background: var(--bg); font: 16px var(--font); }
a { color: var(--link); text-decoration: none; }
a:hover, a:focus { color: var(--link-hover); }
.hero { display: grid; grid-template-columns: minmax(0,1fr) 203px; gap: 42px; align-items: center; }
.hero h1 { font-size: clamp(34px, 4.1vw, 48px); font-weight: 700; line-height: 1.08; letter-spacing: -.035em; color: var(--display); }
```

## Provenance

- **URL:** https://jytime.github.io/
- **Venue/award:** CVPR 2025 Best Paper (first author of VGGT), per https://cvpr.thecvf.com/Conferences/2025/News/Awards_Press
- **Selection reason:** Rule B; link taken from the vgg-t.github.io author list.
- **Template credit:** Jon Barron (footer: "Thanks to the template from Jon Barron"); the `<link rel="canonical" href="https://leonidk.com/">` tag is a leftover from the template fork chain.
- **Measurement method:** values read from `stylesheet.css` and the static HTML with `extract_style.py` and curl. The page was not rendered in a browser for this note, so the visual crop of the portrait is described from the CSS, not observed.
