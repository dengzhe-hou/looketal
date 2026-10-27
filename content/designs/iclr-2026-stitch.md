# Three-Token Transcript — Style Reference

> A speech lab whiteboard with tokens color-coded in marker: orange text, red speech, blue reasoning.

**Theme:** light

*Measurements are normalized from static HTML and CSS (frequency-ranked by a script, then filtered by reading the page's own stylesheet and inline styles). Roles are interpreted, not declared by the authors.*

Built from the Academic Project Page Template (itself adapted from Nerfies), so the frame is stock Bulma: light hero, dark pill buttons, Google Sans title. What makes it distinct is a small token vocabulary. Three uppercase badges, orange for text, coral red for speech, blue for reasoning, label chunks in monospace transcripts and flow diagrams that explain how the model interleaves thinking and talking. Warm and cool tinted placeholder boxes hold example outputs. MathJax 3 is loaded, and an embedded Adobe PDF viewer shows the paper inline.

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
| Text Token Amber | `#FFB347` | `--badge-text-bg` | Text-token badge fill (label #5a3600) |
| Speech Token Coral | `#FF6B6B` | `--badge-speech-bg` | Speech-token badge fill (label #5a0000) |
| Reason Token Blue | `#6FA8FF` | `--badge-reason-bg` | Reasoning-token badge fill (label #002e66) |
| Transcript Paper | `#f7f7f7` | `--chunk-bg` | `.inline-chunks` monospace box (border #e3e3e3) |
| Warm Placeholder | `#fff6ef` | `--warm-bg` | `.placeholder.scheme-warm` (border #ffcf9e) |
| Cool Placeholder | `#eef6ff` | `--cool-bg` | `.placeholder.scheme-cool` (border #b7dcff) |
| Neutral Placeholder | `#f7f9fa` | `--placeholder-bg` | `.placeholder` default (border #d9e2e8) |

Badge label colors are dark tints of each fill (#5a3600, #5a0000, #002e66) rather than white, which keeps contrast high on light fills.

## Tokens — Typography

**Families.** Google Sans (title, authors, teaser), Noto Sans (body), system-ui stack for badges, "Courier New" monospace for transcripts. Substitutes: Inter for Google Sans; JetBrains Mono for Courier New.

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
| Token badge | 0.7-0.75rem, uppercase, letter-spacing 0.5px | 600 | system-ui |
| Transcript chunk | 0.85rem, line-height 1.4 | 400 | Courier New |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| --radius-pill | 290486px | `is-rounded` link buttons |
| --radius-sm | 4px | Bulma default controls, tags |
| --radius-md | 6px | Bulma boxes, cards |
| --radius-media | 10px | `.publication-video`, carousel items |
| --radius-badge | 0.35-0.4rem | token badges |
| --radius-box | 6px | transcript and placeholder boxes |

**Shadows.** Shadows are almost absent. The only framework shadow that appears in practice is Bulma's card/box shadow `0 .5em 1em -.125em rgba(10,10,10,.1), 0 0 0 1px rgba(10,10,10,.02)`; focus rings use `0 0 0 .125em rgba(50,115,220,.25)`.

**Layout width.** Bulma `.container` caps at 1152px (widescreen) and 1344px (fullhd); text columns usually sit in `column is-four-fifths` or `is-two-thirds` inside it, so prose runs about 750-920px wide (inferred). `.section-title` adds 2.5rem top and 1rem bottom margin.

## Components

- **Link button (Paper / arXiv / Code ...).** `a.external-link.button.is-normal.is-rounded.is-dark`: fill #363636, white label, pill radius 290486px, Font Awesome or Academicons glyph in a `span.icon` before a `span` label, 5px vertical margin from `.link-block a`. Labels: Paper, arXiv.
- **Token badge.** `.badge` inline-block, padding 0.15rem 0.45rem, radius 0.35rem, 0.75rem, weight 600, uppercase, letter-spacing 0.5px, line-height 1; three color variants above.
- **Token legend.** `.token-legend` inline-flex, gap 0.4rem, 0.85rem text, nowrap.
- **Transcript box.** `.inline-chunks`: Courier New 0.85rem, #f7f7f7, 1px #e3e3e3, radius 6px, padding 0.75rem 0.9rem, horizontal scroll.
- **Process flow.** `.process-flow` flex-wrap row with 0.75rem gaps of `.flow-box` steps.
- **Placeholder box.** monospace 0.85rem, padding 0.75rem 1rem, 6px radius, warm or cool scheme.
- **PDF embed.** Adobe Document Cloud View SDK in the "Paper PDF" section.
- **BibTeX block.** `section#BibTeX` with `h2.title` "BibTeX" above a Bulma `pre > code`; background #f5f5f5, text #4a4a4a, padding 1.25em 1.5em, no border, left-aligned monospace.
- **Footer.** Bulma `footer.footer` on #fafafa (Bulma default, inferred), centered small text with the CC BY-SA 4.0 license sentence and template credit; `.footer .icon-link` 25px black.

## Page Modules

- **Title/author block.** `title is-1 publication-title`, Google Sans authors, equal-contribution note in `.eql-cntrb` (smaller).
- **Link buttons.** Paper and arXiv dark pills.
- **Teaser.** Illustration figure/video of STITCH-R in `.hero.teaser`.
- **Abstract.** Inside `hero is-small is-light` (#f5f5f5 band), per the Academic Project Page Template.
- **Narrative method sections.** Background, Problem, Trivial Solution, Our Solution, STITCH-S, each with token-coded examples.
- **Results.** Experiments section with figures; seven audio/video demos.
- **Ethical statement.** Dedicated section.
- **Paper PDF.** Embedded viewer (iframe count 1).
- **BibTeX.** End of page.
- Not present: code button (extractor flagged a code link elsewhere), results table, slider, 3D viewer.

## Do's and Don'ts

**Do**

- Assign one fixed color per token type and reuse it in every diagram and transcript.
- Use dark tinted label text on pastel badges instead of white.
- Tell the method as a problem-to-solution story across short sections.

**Don't**

- Don't add a fourth token color without a legend entry.
- Don't render transcripts in the body font; keep Courier New.
- Don't let the PDF embed replace the abstract.

## Surfaces

White page, #f5f5f5 abstract band, pale transcript and placeholder boxes with 1px tinted borders.

## Imagery

Schematic timelines of interleaved reasoning and speech chunks, audio demo players, result plots.

## Layout

Centered single column; ten-plus narrative sections stacked, each opened by a `.section-title` with generous top margin.

## Agent Prompt Guide

**Quick color reference**

- Background #ffffff
- Text token #FFB347
- Speech token #FF6B6B
- Reason token #6FA8FF
- Transcript box #f7f7f7 / #e3e3e3

**Example component prompts**

1. Create three uppercase token badges (TEXT #FFB347 on #5a3600, SPEECH #FF6B6B on #5a0000, REASON #6FA8FF on #002e66), 0.75rem, weight 600, radius 0.35rem.
2. Create a monospace transcript box in Courier New 0.85rem on #f7f7f7 with 1px #e3e3e3 border, 6px radius, inline badges marking each chunk.
3. Create a horizontal process flow of four rounded step boxes with 0.75rem gaps that wraps on narrow screens.

## Similar Pages

- Academic Project Page Template (eliahuhorwitz), the stated base.
- Nerfies (nerfies.github.io).
- Other spoken-language-model demo pages with audio samples.

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
  --badge-text: #ffb347;
  --badge-speech: #ff6b6b;
  --badge-reason: #6fa8ff;
  --chunk-bg: #f7f7f7;
  --chunk-border: #e3e3e3;
  --container: 1152px;
}
```

## Provenance

- URL: https://d223302.github.io/STITCH/
- Paper: STITCH: Simultaneous Thinking and Talking with Chunked Reasoning for Spoken Language Models (Cheng-Han Chiang et al.), arXiv 2507.15375.
- Venue: ICLR 2026 (per the arXiv comment). Field: spoken language models.
- Selection reason: arXiv comment states acceptance at ICLR 2026 and links the project page.
- Template credit: footer says it was built with the Academic Project Page Template, adopted from Nerfies; CC BY-SA 4.0.
- Measurement: Measured from static HTML and CSS only (tools/extract_style.py plus a direct read of the page's own stylesheets and inline styles). The page was not rendered in a browser for this entry, so computed styles, actual font fallback, and video framing are not verified.
