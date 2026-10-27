# Cayman Gradient Songbook — Style Reference

> A GitHub Pages songbook: a blue-to-green banner sings the title, a cartoon fox with a guitar explains the tasks, and every example below is a prompt, two players and a boxed lyric sheet.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (`tools/computed_style.py`: computed styles of the header, title, author paragraphs, links, teaser image, headings and `pre` blocks, first-viewport anatomy, loaded fonts and color share), the first-viewport screenshot and the full-page capture, and the site's `assets/css/style.css`, which is the Jekyll Cayman theme with a few overrides at the end (`.main-content{max-width:80rem}`, table, audio, `li` and hidden footer rules). Positions are document coordinates at 1440px wide.

## Overview

SongComposer is a Markdown page rendered by the GitHub Pages Cayman theme. A full-width header band (426px tall at 1440) runs a 120° gradient from blue #155799 to green #159957 and centers the three-line title in Open Sans 52px bold white. The empty tagline below it only adds bottom space. On white, centered author paragraphs follow with inline font sizes (authors in #1e6bb8 with superscripts, affiliations, contribution note, "ACL 2025 Main", then "arXiv | code" as 26px text links). The teaser is a full-width illustration: a cartoon fox mascot with a guitar and "SongComposer" ribbon at the center, four task prompt cards on the left and four answer cards with sheet music on the right, each tinted (blue, green, yellow, peach) and joined by curved arrows. Section headings are Cayman's green (#159957) at weight 400, left-aligned. The samples section repeats one recipe per example: a bold "Given Text Prompt :" line, "Vocal :" and "Vocal + Accompaniment :" each followed by an inline native audio player at 30% width, and the full lyrics in a pale blue-grey (#f3f6fa) code block with a 1px #dce6f0 border. The theme footer is hidden.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): white #ffffff 34.5%, gradient teal #0d8879 21.7%, gradient blue #196984 20.5%, pale grey-green #dbe6e2 15.8% (teaser card tints and antialiased text), mid green #329077 3.3%, near-white #fffffb 1.7%, deep blue #0d6274 1.3%, pale yellow #fff5db 1.1% (teaser card). The header band takes about 47% of the viewport.

Anatomy in DOM order (y = top of element box):

1. **Header band** (`header.page-header`), y 0, height 426, full width, `background-color: #159957` under `linear-gradient(120deg, #155799, #159957)`, padding 80px 96px, centered white text.
2. **Title** (`h1.project-name`), y 80, 1248px wide, three lines, Open Sans 52px/78px weight 700, #ffffff, centered. The empty `h2.project-tagline` below contributes its 32px bottom margin. Gap to the next block: 80px band padding, then 32px main padding, less the authors' -21px top margin.
3. **Authors** (`p[align=center]` at 1.22em), y 437, two lines, Open Sans 21.5px/32.2px, links #1e6bb8 with superscript marks, comma separators #606c71. No gap.
4. **Affiliations** (`p` at 1.2em), y 501, 21.1px/31.7px #606c71, superscript numbers. Gap 2px.
5. **Contribution note** (`p` at 1.1em), y 535, 19.4px/29px #606c71. No gap.
6. **Venue** (`p` at 1.2em), y 562, "ACL 2025 Main", 21.1px #606c71, plain weight. No gap.
7. **Links** (`p` at 1.5em), y 588, "arXiv | code", 26.4px/39.6px, #1e6bb8 links, #606c71 pipe, no buttons. Gap 26px.
8. **Teaser** (`p img`, width 100%), y 654, 1088×451, illustration with the mascot centered and tinted task cards. The fold cuts it at about two thirds.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Gradient Blue | #155799 | `.page-header` gradient start | Header band, left side |
| Cayman Green | #159957 | `.page-header` gradient end and fallback, `.main-content h1–h6` | Header band right side; every content heading |
| Header Text | #ffffff | `.page-header` color | Title |
| Body Slate | #606c71 | `body` | Body text, affiliations, notes, venue, link separators |
| Link Blue | #1e6bb8 | `a` | Author names, arXiv and code links, inline links (underline on hover) |
| Code Text | #567482 | `.main-content pre`, `code` | Lyrics text |
| Code Wash | #f3f6fa | `.main-content pre`, `code` | Lyrics block background |
| Code Border | #dce6f0 | `.main-content pre` | 1px lyrics block border |
| Teaser Teal | #0d8879 | gradient pixels (quantized) | Header band middle tone in the render |
| Teaser Pale | #dbe6e2 | teaser pixels (quantized) | Teaser card tints and background areas |
| White | #ffffff | page | Content background |

Declared but not visible: the theme's `.btn` styles (translucent white buttons) are unused because the header has no buttons, and `.site-footer` is hidden by `footer{display:none !important}`.

## Tokens — Typography

- **Family**: declared `"Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif`, imported from Google Fonts at 400 and 700. Rendered: Open Sans 400 and 700 (`fonts_loaded`). Substitute: Noto Sans (same humanist proportions).
- **Code**: declared `Consolas, "Liberation Mono", Menlo, Courier, monospace`; renders in Consolas on Windows.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Title | `.page-header h1.project-name` | 52px (3.25rem) / 78px | 700 | #ffffff |
| Section heading | `.main-content h1` | 35.2px (2em of 17.6px) / 52.8px | 400 | #159957, left |
| Example heading | `.main-content h2` | 26.4px / 39.6px | 400 | #159957, left |
| Links line | `p` inline `font-size: 1.5em` | 26.4px / 39.6px | 400 | #1e6bb8 |
| Authors | `p` inline `1.22em` | 21.5px / 32.2px | 400 | #1e6bb8 |
| Affiliation, venue | `p` inline `1.2em` | 21.1px / 31.7px | 400 | #606c71 |
| Note | `p` inline `1.1em` | 19.4px / 29px | 400 | #606c71 |
| Body | `.main-content` | 17.6px (1.1rem) / 26.4px | 400 | #606c71 |
| Field label | `p strong` | 17.6px | 700 | #606c71 |
| Lyrics | `.main-content pre` | 14.4px (0.9rem) / 20.9px | 400 | #567482 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Header band | 0 | none | none |
| Lyrics `pre` | 4.8px (0.3rem) | 1px solid #dce6f0 | none; padding 12.8px |
| Inline `code` | 4.8px | none | none; padding 2px 4px |
| Teaser | 0 | none (card borders are inside the image) | none |
| Audio player | Chrome native pill | none | none |

## Layout Metrics

- **Container**: `.main-content`, `max-width: 80rem` (1280px, overriding Cayman's 64rem), centered, padding 32px 96px, so content spans x 176–1264 (1088px).
- **Header**: full width, padding 80px 96px at ≥1024px; title box 1248px.
- **Hero block**: centered `p`s pulled up with `margin-top: -1em` each, so lines sit almost flush; 26px from the link line to the teaser.
- **Teaser**: 100% of the content width (1088px).
- **Sections**: headings with 32px top and 16px bottom margins; paragraphs 1em bottom margin.
- **Examples**: label paragraphs with an inline `<audio style="width:30%">` (about 326px), then the lyrics `pre` at full width; lists use an 18px item gap.
- **Footer**: hidden.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px (64em) | header 80px 96px; content padding 96px | 17.6px | 52px | as described |
| 672–1023px (42–64em) | header 48px 64px; content padding 64px | 17.6px | 36px | content fluid |
| <672px (42em) | header 32px 16px; content padding 16px | 16px | 28px | single column; theme `.btn` would stack |

## Components

- **Gradient title band**: full-width `header`, `linear-gradient(120deg, #155799, #159957)` over #159957, centered white Open Sans 52px/78px bold title, padding 80px 96px, no nav and no buttons.
- **Text link row**: centered paragraph at 1.5em with #1e6bb8 links separated by a plain " | "; links underline on hover, no icons.
- **Illustrated teaser**: one full-width PNG with a central mascot and pastel task cards connected by arrows; no frame, no caption.
- **Example block**: `h2` in #159957 26.4px/400, then `p > strong` labels ("Given Text Prompt :", "Vocal :", "Vocal + Accompaniment :", "Lyrics :") in 700 with inline content; native audio controls at 30% width sit on the label's baseline.
- **Lyrics box**: `pre` with #f3f6fa background, 1px #dce6f0 border, 4.8px radius, padding 12.8px, Consolas 14.4px/1.45 #567482, section tags like `<verse>` and `<chorus>` shown literally.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Header band and title | yes | blue-to-green gradient, white bold title |
| Authors, affiliations, venue | yes | centered paragraphs with inline sizes |
| Link buttons | present but non-standard | two text links separated by a pipe |
| Teaser | yes | illustrated mascot and task cards |
| Abstract | yes | left-aligned 17.6px paragraph with bold phrases |
| Audio samples | yes | labeled native players, English and Chinese sections |
| Lyrics | yes | bordered pale code boxes |
| Results table, method figure | absent from the source | |
| BibTeX | absent from the source | |
| Navigation, footer | absent from the source | theme footer hidden |

## Adapting to Other Content

- **More authors**: add lines to the centered author paragraph with `<br>`; keep 1.22em size and #1e6bb8 links with superscripts.
- **A results table**: Cayman tables are `display: block` with 1px #e9ebec cell borders and 8px 16px padding; on this page `table, td` are centered and transparent and `th` is weight 100, so set header weight back to 700 and add a 2px #dce6f0 rule under the header.
- **More links**: extend the pipe-separated row rather than adding buttons; for many links, the theme's `.btn` (translucent white on the gradient) can go inside the header.
- **News**: a short `ul` under the link row; items already get 18px bottom margins.
- **Long publication lists**: plain Markdown list in the 1088px column, titles bold, links #1e6bb8.
- **Long text samples**: keep using the bordered `pre`; for prose rather than lyrics, a `blockquote` (0.3rem #dce6f0 left border, #819198 text) is the theme's quieter option.

## Do's and Don'ts

- Do keep the 120° #155799 → #159957 band as the only strong color field.
- Do set every content heading in #159957 at weight 400, left-aligned.
- Do keep sample blocks uniform: bold label, inline player, boxed text.
- Do let the illustrated teaser span the full content width.
- Don't add buttons to the hero; the page uses text links.
- Don't center long body text; only the author block is centered.
- Don't add borders or shadows to images; the teaser draws its own cards.

## Surfaces

The gradient header band, then white throughout, with #f3f6fa lyric boxes edged in #dce6f0. No cards, no section bands, no footer.

## Imagery

A colorful cartoon fox mascot wearing headphones and holding a guitar on a blue "SongComposer" ribbon, surrounded by eight pastel prompt and answer cards (blue, green, yellow, peach) with music staves and lyric snippets, joined by soft curved arrows. Everything else is text and audio.

## Layout

A full-width header band above a single centered 1088px column with a centered author block and left-aligned sections. Rendered height is about 8,560px at 1440px, mostly lyrics boxes.

## Agent Prompt Guide

Quick colors: band #155799 → #159957, headings #159957, body #606c71, links #1e6bb8, code #f3f6fa with #dce6f0 border and #567482 text.

1. "Build a header band: full width, background-color #159957 with linear-gradient(120deg, #155799, #159957), padding 80px 96px, centered Open Sans 52px/78px bold #ffffff title, no buttons. Below it, in a 1088px centered column, author links in #1e6bb8 at about 21.5px with superscripts, affiliation and venue lines at 21px #606c71, and an 'arXiv | code' row at 26.4px."
2. "Create a sample block: an h2 'Example 1' in Open Sans 26.4px weight 400 #159957 left-aligned; then paragraphs with bold labels ('Given Text Prompt :', 'Vocal :') in 17.6px #606c71, each audio label followed by an inline native audio control at 30% width."
3. "Add a lyrics box: pre with background #f3f6fa, 1px solid #dce6f0 border, 4.8px radius, padding 12.8px, Consolas 14.4px with line-height 1.45 in #567482, full column width."

## Similar Pages

- GitHub Pages sites on the Cayman theme (jasonlong/cayman-theme) used as project pages.
- Music and speech generation demo pages that pair prompts with audio and lyric text.

## Quick Start

```css
:root {
  --band: linear-gradient(120deg, #155799, #159957);
  --band-fallback: #159957;
  --heading: #159957;
  --text: #606c71;
  --link: #1e6bb8;
  --code-bg: #f3f6fa;
  --code-border: #dce6f0;
  --code-text: #567482;
  --font: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-mono: Consolas, "Liberation Mono", Menlo, Courier, monospace;
  --title-size: 52px;
  --body-size: 17.6px;
  --container: 1280px;
  --content-pad: 32px 96px;
}
```

## Provenance

- **URL**: https://pjlab-songcomposer.github.io/
- **Paper**: SongComposer: A Large Language Model for Lyric and Melody Generation in Song Composition (arXiv 2402.17645), Shuangrui Ding et al.
- **Venue**: ACL 2025 (Main).
- **Selection reason**: the arXiv 2402.17645 comment states ACL 2025 main and links the page. Chosen for the blue-to-green gradient title band and green headings that give a coherent color identity, and the charming illustrated mascot teaser with task cards; the lyrics blocks run long but are neatly boxed.
- **Template credit**: Jekyll Cayman theme for GitHub Pages (its footer credit is hidden on this page).
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and fonts, the first-viewport screenshot and full-page capture, `assets/css/style.css` and the HTML. Date 2026-10-28.
