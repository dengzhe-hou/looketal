# Sky-Blue Trajectory Reel — Style Reference

> A robotics demo reel with captions underlined in sky blue.

**Theme:** light

*Measurements are normalized from static HTML and CSS (frequency-ranked by a script, then filtered by reading the page's own stylesheet and inline styles). Roles are interpreted, not declared by the authors.*

A close Nerfies clone tuned for a video-heavy paper: eight videos, a twentytwenty before/after slider, and a Bulma carousel whose items are black boxes with 10px radius and a #bbb rim. The only accent the authors add is #4FACFA, used inline on key phrases inside section headings ("Diverse Skills"). The title block widens to 110% with a -5% margin so long titles break less, and the method name is set in small caps. The venue appears as a separate `h2` reading "ICLR 2026" under the title.

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
| Trajectory Sky | `#4FACFA` | `--accent` | Inline color on emphasized words in section headings |
| Reel Black | `#000000` | `--media-bg` | `.results-carousel .twoitem` background |

Bulma's full palette (#00d1b2, #ffdd57, #48c774 and so on) shows up in raw counts but is not used by the markup.

## Tokens — Typography

**Families.** Google Sans for title, authors and teaser (`.publication-title`, `.publication-authors`, `.teaser`); Noto Sans for body; Castoro is loaded from Google Fonts but no rule uses it (inferred unused). Substitutes: Product Sans or Inter for Google Sans. Some heading paragraphs set inline sizes of 20px and 17px with left padding.

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

**Shadows.** Shadows are almost absent. The only framework shadow that appears in practice is Bulma's card/box shadow `0 .5em 1em -.125em rgba(10,10,10,.1), 0 0 0 1px rgba(10,10,10,.02)`; focus rings use `0 0 0 .125em rgba(50,115,220,.25)`. Carousel navigation arrows add `0 0 12px rgba(0,0,0,1)`; pagination dots `0 0 4px rgba(0,0,0,1)`.

**Layout width.** Bulma `.container` caps at 1152px (widescreen) and 1344px (fullhd); text columns usually sit in `column is-four-fifths` or `is-two-thirds` inside it, so prose runs about 750-920px wide (inferred).

## Components

- **Link button (Paper / arXiv / Code ...).** `a.external-link.button.is-normal.is-rounded.is-dark`: fill #363636, white label, pill radius 290486px, Font Awesome or Academicons glyph in a `span.icon` before a `span` label, 5px vertical margin from `.link-block a`. Labels: Paper, Model, Code.
- **Accent phrase.** `span style="color:#4FACFA"` inside a centered `h2.title`, same weight as the heading.
- **Video carousel item.** `.results-carousel .twoitem`: black fill, flex column centered, height 95%, margin 5px, 1px #bbb border, 10px radius, `font-size: 0` to kill gaps.
- **Before/after slider.** jQuery twentytwenty with its default white handle (twentytwenty.css).
- **Method name.** `.methodname { font-variant: small-caps }`.
- **Loading notice.** A centered note "(Loading all videos may take some time ...)" under the venue line.
- **BibTeX block.** `section#BibTeX` with `h2.title` "BibTeX" above a Bulma `pre > code`; background #f5f5f5, text #4a4a4a, padding 1.25em 1.5em, no border, left-aligned monospace.
- **Footer.** Bulma `footer.footer` on #fafafa (Bulma default, inferred), centered small text with the CC BY-SA 4.0 license sentence and template credit; `.footer .icon-link` 25px black.

## Page Modules

- **Title/author block.** Centered title with a logo image (115px high) above it, Google Sans authors in #3298dc, venue as `h2` "ICLR 2026".
- **Link buttons.** Paper, Model (checkpoint), Code as dark pills.
- **Teaser video.** Full-width looping video in `.hero.teaser`.
- **Results videos.** Sections for diverse skills, long video generation, annotated transitions, baseline comparison (Tora, DragAnything), embodied action planning, ablation.
- **Image-comparison slider.** twentytwenty before/after widget.
- **Carousel.** bulma-carousel with black media tiles.
- **Method figure.** Placed near the end, after results.
- **BibTeX.** Standard Bulma `pre`.
- Not present: abstract heading (none in h2 list), results table, HF demo, 3D viewer.

## Do's and Don'ts

**Do**

- Use the single #4FACFA accent only on the key noun of a heading.
- Put video tiles on black so letterboxing disappears.
- Warn readers that many videos are loading.

**Don't**

- Don't color whole headings blue; only the emphasized phrase.
- Don't introduce a second accent color.
- Don't place results tiles on white without the #bbb rim.

## Surfaces

White page; black media tiles inside the carousel; whitesmoke BibTeX well.

## Imagery

Robot arm manipulation clips, trajectory overlays drawn on video frames, side-by-side baseline comparisons.

## Layout

Results-first: header, teaser, five or six results sections, then method and BibTeX. Single centered column inside Bulma container.

## Agent Prompt Guide

**Quick color reference**

- Background #ffffff
- Headings #363636
- Accent #4FACFA
- Buttons #363636
- Media tiles #000000 with #bbbbbb rim

**Example component prompts**

1. Create a centered Bulma section heading in Google Sans 2rem weight 600 where the phrase "Diverse Skills" is colored #4FACFA.
2. Create a video carousel tile: black background, 1px #bbbbbb border, 10px radius, 5px margin, video fills the tile.
3. Create three dark pill link buttons (Paper, Model, Code) with Font Awesome icons, fill #363636, white text.

## Similar Pages

- 3DTrajMaster (same author, same index.css and #4FACFA accent).
- Nerfies (nerfies.github.io).
- Tora and DragAnything project pages (compared baselines).

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

- URL: https://fuxiao0719.github.io/projects/robomaster/
- Paper: Learning Video Generation for Robotic Manipulation with Collaborative Trajectory Control (Xiao Fu et al.), arXiv 2506.01943.
- Venue: ICLR 2026 (per the arXiv comment). Field: video generation for robotics.
- Selection reason: arXiv comment states acceptance at ICLR 2026 and links the project page.
- Template credit: footer credits Nerfies, CC BY-SA 4.0.
- Measurement: Measured from static HTML and CSS only (tools/extract_style.py plus a direct read of the page's own stylesheets and inline styles). The page was not rendered in a browser for this entry, so computed styles, actual font fallback, and video framing are not verified.
