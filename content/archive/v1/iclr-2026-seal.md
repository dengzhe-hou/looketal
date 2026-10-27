# Neon Event Wordmark — Style Reference

> A night-vision demo where the method name glows in a cyan-violet-pink gradient.

**Theme:** light

*Measurements are normalized from static HTML and CSS (frequency-ranked by a script, then filtered by reading the page's own stylesheet and inline styles). Roles are interpreted, not declared by the authors.*

A stock Nerfies frame with one loud gesture: the word SEAL is set in weight 800 italic and filled with an animated gradient (#00c6ff to #7f00ff to #ff4ecd) that pulses opacity and drop-shadow every 1.1s. Three content colors tag prompt types and features inline: terracotta #df6950, indigo #5c66f0 and green #51b18d. With 42 images and six videos, the page is a dense results gallery, and its link row is the widest in this batch: Paper, arXiv, Code, Hugging Face and two social Posts.

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
| Prompt Terracotta | `#df6950` | `--tag-1` | Inline color on prompt keywords (11 uses) |
| Prompt Indigo | `#5c66f0` | `--tag-2` | Inline color on keywords (7 uses) |
| Prompt Jade | `#51b18d` | `--tag-3` | Inline color on keywords (6 uses) |
| Glow Cyan | `#00c6ff` | `--glow-1` | Wordmark gradient start |
| Glow Violet | `#7f00ff` | `--glow-2` | Wordmark gradient middle and drop-shadow tint |
| Glow Pink | `#ff4ecd` | `--glow-3` | Wordmark gradient end |

The three tag colors appear only as text color, never as fills.

## Tokens — Typography

**Families.** Google Sans (title, authors, teaser), Noto Sans (body). The `.seal` wordmark inherits the heading family at weight 800 italic. Substitutes: Inter.

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
| --radius-figure | 16px | inline style on one framework figure (width 80%) |

**Shadows.** Shadows are almost absent. The only framework shadow that appears in practice is Bulma's card/box shadow `0 .5em 1em -.125em rgba(10,10,10,.1), 0 0 0 1px rgba(10,10,10,.02)`; focus rings use `0 0 0 .125em rgba(50,115,220,.25)`. The wordmark animates `drop-shadow(0 0 10px rgba(127,0,255,0.55))` at its midpoint.

**Layout width.** Bulma `.container` caps at 1152px (widescreen) and 1344px (fullhd); text columns usually sit in `column is-four-fifths` or `is-two-thirds` inside it, so prose runs about 750-920px wide (inferred). Many sections pull up with inline `margin-top: -2rem` or `-1rem` to tighten the gallery.

## Components

- **Link button (Paper / arXiv / Code ...).** `a.external-link.button.is-normal.is-rounded.is-dark`: fill #363636, white label, pill radius 290486px, Font Awesome or Academicons glyph in a `span.icon` before a `span` label, 5px vertical margin from `.link-block a`. Labels: Paper, arXiv, Code, Hugging Face, Post, Post.
- **Gradient wordmark.** `.seal`: weight 800 italic, `linear-gradient(90deg, #00c6ff, #7f00ff, #ff4ecd)` at 200% size clipped to text, `sealGlow` 1.1s ease-in-out infinite (opacity 1 to 0.25, scale to 1.03).
- **Keyword color.** `span style="color:#df6950"` and siblings inside teaser captions.
- **Interpolation panel.** Template `.interpolation-panel` #f5f5f5, 10px radius (present in CSS).
- **Results carousel.** Items with 1px #bbb border, 10px radius.
- **BibTeX block.** `section#BibTeX` with `h2.title` "BibTeX" above a Bulma `pre > code`; background #f5f5f5, text #4a4a4a, padding 1.25em 1.5em, no border, left-aligned monospace.
- **Footer.** Bulma `footer.footer` on #fafafa (Bulma default, inferred), centered small text with the CC BY-SA 4.0 license sentence and thanks to Utkarsh Sinha and Keunhong Park (Nerfies authors); `.footer .icon-link` 25px black.

## Page Modules

- **Title/author block.** Google Sans title with the animated SEAL wordmark.
- **Link buttons.** Paper, arXiv, Code, Hugging Face (dataset/model), two social posts.
- **Teaser videos.** Four captioned teaser blocks (box prompt, point prompt, SEAL++ prompt-free, spatiotemporal).
- **Abstract and Contributions.** Text sections.
- **Proposed baselines and framework figure.** Method figures with framework image at 80% width and 16px radius.
- **Qualitative results.** Large image gallery and carousel.
- **BibTeX.** End section.
- Not present: results table, slider, 3D viewer, embedded HF Space.

## Do's and Don'ts

**Do**

- Animate only the method name; keep the rest of the page still.
- Use the three tag colors consistently for the same prompt types.
- Tighten gallery spacing with small negative margins rather than new containers.

**Don't**

- Don't use the gradient on headings other than the method name.
- Don't fill backgrounds with the tag colors.
- Don't add a fourth keyword color.

## Surfaces

White page, whitesmoke BibTeX well, gray-rimmed carousel tiles.

## Imagery

Event-camera frames with colored instance masks, framework diagram with rounded corners, short demo videos.

## Layout

Teaser-first: four teaser blocks, then abstract, contributions, baselines, framework, qualitative results, BibTeX.

## Agent Prompt Guide

**Quick color reference**

- Background #ffffff
- Wordmark gradient #00c6ff → #7f00ff → #ff4ecd
- Tags #df6950 / #5c66f0 / #51b18d
- Buttons #363636

**Example component prompts**

1. Create an animated wordmark: weight 800 italic text filled with a 90deg gradient #00c6ff, #7f00ff, #ff4ecd at 200% size, pulsing opacity and a violet drop-shadow every 1.1s.
2. Create a teaser caption sentence in 1.25rem Google Sans where 'box prompts' is #df6950 and 'open-vocabulary semantics' is #5c66f0.
3. Create a six-button link row of dark pills (Paper, arXiv, Code, Hugging Face, Post, Post) that wraps centered.

## Similar Pages

- Nerfies (nerfies.github.io), whose code the footer credits.
- Segment-anything style project pages with prompt-type color coding.

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
  --tag-1: #df6950;
  --tag-2: #5c66f0;
  --tag-3: #51b18d;
  --glow: linear-gradient(90deg, #00c6ff, #7f00ff, #ff4ecd);
  --container: 1152px;
}
```

## Provenance

- URL: https://0nandon.github.io/SEAL/
- Paper: Segment Any Events with Language (Seungjun Lee et al.), arXiv 2601.23159.
- Venue: ICLR 2026 (per the arXiv comment). Field: event-based vision.
- Selection reason: arXiv comment states acceptance at ICLR 2026 and links the project page.
- Template credit: footer says it borrows the source code of a linked website and thanks Utkarsh Sinha and Keunhong Park (Nerfies); the extractor did not flag a named template string.
- Measurement: Measured from static HTML and CSS only (tools/extract_style.py plus a direct read of the page's own stylesheets and inline styles). The page was not rendered in a browser for this entry, so computed styles, actual font fallback, and video framing are not verified.
