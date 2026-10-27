# Sky-Blue Entity Reel — Style Reference

> Twenty-six clips of choreographed entities, captioned in sky blue.

**Theme:** light

*Measurements are normalized from static HTML and CSS (frequency-ranked by a script, then filtered by reading the page's own stylesheet and inline styles). Roles are interpreted, not declared by the authors.*

The earlier sibling of RoboMaster by the same author, sharing the identical `index.css` and the #4FACFA accent. It is even more video-dense: 26 videos, a twentytwenty slider, bulma-carousel black tiles, and four link buttons including a Dataset button. The title is widened to 110% with a -5% margin and the method name is small caps. Unusually, the footer carries a numbered Related Works list (MotionCtrl, TC4D, Tora) with one-line descriptions instead of only the template credit.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | `--bg` | Page and section background |
| Whitesmoke Well | `#f5f5f5` | `--bg-well` | Bulma `pre` (BibTeX) and `hero is-light` fill |
| Graphite Heading | `#363636` | `--text-strong` | Bulma `.title` color; also the `is-dark` button fill |
| Body Slate | `#4a4a4a` | `--text` | Bulma body copy |
| Byline Gray | `#555555` | `--venue` | `.publication-venue` (bold) |
| Author Sky | `#3298dc` | `--author-link` | `.publication-authors a`, written as hsl(204, 86%, 53%) |
| Bulma Link Blue | `#3273dc` | `--link` | Default anchor color in body text |
| Hairline Gray | `#dbdbdb` | `--border` | Bulma input and table borders |
| Carousel Rim | `#bbbbbb` | `--frame` | 1px border on `.results-carousel .item` |
| Trajectory Sky | `#4FACFA` | `--accent` | Inline color on key phrases in section headings ("Diverse Entities") |
| Reel Black | `#000000` | `--media-bg` | `.results-carousel .twoitem` background |

Bulma's full palette is in the raw counts but unused by markup.

## Tokens — Typography

**Families.** Google Sans (title, authors, teaser), Noto Sans (body); Castoro loaded but unused (inferred). Substitutes: Inter.

| Role | Size | Weight | Family |
|---|---|---|---|
| Paper title (`title is-1`) | 3rem (48px) | 600 | Google Sans |
| Paper title (`title is-2`) | 2.5rem (40px) | 600 | Google Sans |
| Section heading (`title is-3`) | 2rem (32px) | 600 | Noto Sans |
| Sub-heading (`title is-4`) | 1.5rem (24px) | 600 | Noto Sans |
| Author line (`is-size-5`) | 1.25rem (20px) | 400 | Google Sans |
| Body / abstract | 1rem (16px), line-height 1.5 | 400 | Noto Sans |
| Button label | 1rem | 400 | Noto Sans |
| BibTeX | .875em | 400 | monospace |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| --radius-pill | 290486px | `is-rounded` link buttons |
| --radius-sm | 4px | Bulma default controls, tags |
| --radius-md | 6px | Bulma boxes, cards |
| --radius-media | 10px | `.publication-video`, carousel items |

**Shadows.** Shadows are almost absent. The only framework shadow that appears in practice is Bulma's card/box shadow `0 .5em 1em -.125em rgba(10,10,10,.1), 0 0 0 1px rgba(10,10,10,.02)`; focus rings use `0 0 0 .125em rgba(50,115,220,.25)`. Carousel arrows `0 0 12px rgba(0,0,0,1)`; pagination dots `0 0 4px rgba(0,0,0,1)` on white.

**Layout width.** Bulma `.container` caps at 1152px (widescreen) and 1344px (fullhd); text columns usually sit in `column is-four-fifths` or `is-two-thirds` inside it, so prose runs about 750-920px wide (inferred). A logo image 140px high sits above the title.

## Components

- **Link button (Paper / arXiv / Code ...).** `a.external-link.button.is-normal.is-rounded.is-dark`: fill #363636, white label, pill radius 290486px, Font Awesome or Academicons glyph in a `span.icon` before a `span` label, 5px vertical margin from `.link-block a`. Labels: Paper, arXiv, Dataset, Code.
- **Accent phrase.** `span style="color:#4FACFA"` inside centered `h2.title`.
- **Video carousel item.** `.twoitem` black, 1px #bbb, 10px radius, height 95%.
- **Before/after slider.** twentytwenty.
- **Method name.** `.methodname { font-variant: small-caps }`.
- **Related works footer.** Numbered list with linked names and one-line summaries.
- **BibTeX block.** `section#BibTeX` with `h2.title` "BibTeX" above a Bulma `pre > code`; background #f5f5f5, text #4a4a4a, padding 1.25em 1.5em, no border, left-aligned monospace.

## Page Modules

- **Title/author block.** Logo above a wide centered title, venue `h2` "ICLR 2025", loading notice.
- **Link buttons.** Paper, arXiv, Dataset, Code.
- **Teaser video.** In `.hero.teaser`.
- **Results videos.** Diverse entities, diverse backgrounds, complex multi-entity motion (20 trajectory cases), fine-grained control, comparisons with Tora, Direct-a-Video and TC4D.
- **Image-comparison slider and carousel.** As in RoboMaster.
- **Method.** Figure near the end.
- **BibTeX and related works.** BibTeX, then a related-works footer.
- Not present: abstract heading, results table, demo, 3D viewer.

## Do's and Don'ts

**Do**

- Reuse one accent across a series of papers by the same group.
- Put a short related-works list in the footer when comparisons drive the story.
- Warn about video loading time.

**Don't**

- Don't color full headings; only the key phrase.
- Don't place video tiles on white.

## Surfaces

White page; black carousel tiles; whitesmoke BibTeX well.

## Imagery

Multi-entity generated videos with 3D trajectories overlaid, comparison clips against baselines.

## Layout

Results-first column: header, teaser, four control sections, two comparison sections, method, BibTeX, related works.

## Agent Prompt Guide

**Quick color reference**

- Background #ffffff
- Accent #4FACFA
- Headings #363636
- Buttons #363636
- Media tiles #000000

**Example component prompts**

1. Create a centered section heading 'Control Entity Motion with Diverse Entities' where 'Diverse Entities' is #4FACFA.
2. Create four dark pill buttons (Paper, arXiv, Dataset, Code) with icons, centered, wrapping on small screens.
3. Create a footer related-works list: numbered, linked method names followed by a one-line description in body text.

## Similar Pages

- RoboMaster (same author, same stylesheet).
- Nerfies (nerfies.github.io).
- Tora, MotionCtrl, TC4D project pages (listed in the footer).

## Quick Start

```css
:root {
  --bg: #ffffff;
  --bg-well: #f5f5f5;
  --text-strong: #363636;
  --text: #4a4a4a;
  --venue: #555555;
  --author-link: #3298dc;
  --link: #3273dc;
  --border: #dbdbdb;
  --frame: #bbbbbb;
  --font-display: 'Google Sans', 'Noto Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --font-mono: monospace;
  --radius-pill: 290486px;
  --radius-sm: 4px;
  --radius-media: 10px;
  --accent: #4FACFA;
  --media-bg: #000000;
  --container: 1152px;
}
```

## Provenance

- URL: https://fuxiao0719.github.io/projects/3dtrajmaster/
- Paper: 3DTrajMaster: Mastering 3D Trajectory for Multi-Entity Motion in Video Generation (Xiao Fu et al.), arXiv 2412.07759.
- Venue: ICLR 2025 (per the arXiv comment and the page's venue line). Field: video generation.
- Selection reason: arXiv comment states acceptance at ICLR 2025 and links the project page.
- Template credit: extractor detects the Nerfies credit; the visible footer text leads with the related-works list.
- Measurement: Measured from static HTML and CSS only (tools/extract_style.py plus a direct read of the page's own stylesheets and inline styles). The page was not rendered in a browser for this entry, so computed styles, actual font fallback, and video framing are not verified.
