# Cross-Modal Readout — Style Reference

> A reading-group handout typed in DM Sans, with one sticky note in Georgia.

**Theme:** light

*Measurements are normalized from static HTML and CSS (frequency-ranked by a script, then filtered by reading the page's own stylesheet and inline styles). Roles are interpreted, not declared by the authors.*

A Nerfies-derived page that has been quietly rebuilt around DM Sans (self-hosted) and a 12pt root size. Bootstrap 4 is loaded alongside Bulma only for its carousel and select-row behavior, so the visible chrome stays Bulma: dark pill buttons, centered title block, white sections separated by a thin #ededed rule that spans 90vw. Body text is forced to pure black. The one signature element is the `.finding-box`, a cream note card with a 2px black border and Georgia type that states each key finding like a margin annotation. Interactive figures use underlined `<select>` controls set inline in a sentence, so the reader changes the task by editing the prose.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | `--bg` | Page background |
| Ink Black | `#000000` | `--text` | `body { color: black }` in custom.css |
| Graphite Heading | `#363636` | `--text-strong` | Bulma titles and `is-dark` button fill |
| Byline Gray | `#555555` | `--venue` | `.publication-venue` |
| Author Sky | `#3298dc` | `--author-link` | `.publication-authors a` (hsl(204, 86%, 53%)) |
| Finding Cream | `#fff2d9` | `--note-bg` | `.finding-box` background (written #fff2d9ff) |
| Rule Mist | `#ededed` | `--rule` | `hr` background, 90vw wide |
| Icon Fog | `#C7C7C7` | `--icon-muted` | Inline `color` on small header icons (padding-top 5px) |
| Award Coral | `#ff3860` | `--award` | `.publication-awards` (template rule, not visibly used, inferred) |

Bootstrap 4 contributes its palette variables (#007bff, #6c757d, #212529) to the raw frequency counts, but the page's own markup does not use Bootstrap color utilities; treat them as unused framework residue.

## Tokens — Typography

**Families.** DM Sans 400 for everything (`body { font-family: 'DM Sans', sans-serif !important }`, woff2 self-hosted in `static/fonts`), DM Mono 400 for code, Georgia serif for `.finding-box` and `.method-setting`. Substitutes: Inter or IBM Plex Sans for DM Sans, IBM Plex Mono for DM Mono. Root size is `html { font-size: 12pt }` (16px), so Bulma rem sizes render as usual.

| Role | Size | Weight | Family |
|---|---|---|---|
| Paper title (`title is-2`) | 2.5rem | 600 | DM Sans |
| Section heading (`title is-3`) | 2rem | 600 | DM Sans |
| Author line | 1.25rem | 400 | DM Sans |
| Body / abstract | 1rem, line-height 1.5 | 400 | DM Sans |
| Finding note | 1.1em, line-height 1.4 | 400 | Georgia |
| Code / task labels | .875rem | 400 | DM Mono |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| --radius-pill | 290486px | `is-rounded` link buttons |
| --radius-sm | 4px | Bulma default controls, tags |
| --radius-md | 6px | Bulma boxes, cards |
| --radius-media | 10px | `.publication-video`, carousel items |
| --radius-note | 12px | `.finding-box` |

**Shadows.** Shadows are almost absent. The only framework shadow that appears in practice is Bulma's card/box shadow `0 .5em 1em -.125em rgba(10,10,10,.1), 0 0 0 1px rgba(10,10,10,.02)`; focus rings use `0 0 0 .125em rgba(50,115,220,.25)`.

**Layout width.** Main content is wrapped in `.max-width-content { max-width: 70vw }`; result figures use `.max-width-results { max-width: min(600px, 80vw) }`; one inline block sets `max-width: 720px`. The hero uses an inline padding of `3rem 1.5rem 0.5rem 1.5rem`.

## Components

- **Link button (Paper / arXiv / Code ...).** `a.external-link.button.is-normal.is-rounded.is-dark`: fill #363636, white label, pill radius 290486px, Font Awesome or Academicons glyph in a `span.icon` before a `span` label, 5px vertical margin from `.link-block a`. Only two are present: arXiv and Code.
- **Finding box.** `.finding-box`: background #fff2d9, `2px solid black`, radius 12px, padding 10px 14px, Georgia 1.1em, line-height 1.4, max-width 600px, `display: inline-block`, left-aligned text.
- **Inline select.** Native `<select>` stripped of borders and arrows, underlined, transparent background, cursor pointer; sits inside a sentence (`.select-row span { padding: 5px }`).
- **Teaser toggle.** `button.is-white.btn-teaser`: zero padding, left-justified, underline on hover with transparent background.
- **Task carousel.** Bootstrap carousel with cards capped at 550px and arrows pushed 50px outside the card, arrow icons inverted to black via `filter: invert(1) grayscale(100%) brightness(200%)`.
- **Rule.** `hr` 90vw wide, #ededed, centered.
- **BibTeX block.** `section#BibTeX` with `h2.title` "BibTeX" above a Bulma `pre > code`; background #f5f5f5, text #4a4a4a, padding 1.25em 1.5em, no border, left-aligned monospace.

## Page Modules

- **Title/author block.** Centered `title is-2 publication-title`, author blocks with 5px side margins, affiliation line, venue line in bold #555.
- **Link buttons.** arXiv and Code only, dark pills.
- **Teaser video.** Three `<video>` elements, clickable (`video { cursor: pointer }`), some layered absolutely over a figure (`.layered-video`).
- **Abstract.** Standard centered `h2` and justified paragraph.
- **Method figures.** Cross-Modal Patching diagrams set at 30-35% inline widths beside text.
- **Interactive task explorer.** Scrollable `.task-examples` table (max-height 75vh) with 50px thumbnails and select-driven rows.
- **Results table.** One table in the task explorer; no dedicated benchmark table styling.
- **Relevant Readings.** A short reference list section before Acknowledgements (counted as a publication list by the extractor).
- **Acknowledgements and BibTeX.** Plain sections at the end.
- Not present: HF demo, image-comparison slider, 3D viewer, dataset button.

## Do's and Don'ts

**Do**

- Keep body text pure black and the type single-family (DM Sans) so the Georgia notes stand out.
- State each finding in a `.finding-box` directly under the figure it summarizes.
- Let readers switch conditions with inline underlined selects instead of tab bars.

**Don't**

- Don't add colored section bands; the page relies on white space and the #ededed rule.
- Don't use Bootstrap's blue buttons; links stay Bulma dark pills.
- Don't widen prose beyond 70vw.

## Surfaces

Two surfaces only: white page and the cream finding card. No elevated cards, no tinted hero.

## Imagery

Diagrams of patching between text and image tokens, small 50px task thumbnails, and looping videos. Figures sit on white with no frame.

## Layout

Single centered column, 70vw cap, figures sometimes split 30/70 with text. Sections stack: header, teaser, abstract, five method/result sections, readings, acknowledgements, BibTeX.

## Agent Prompt Guide

**Quick color reference**

- Background #ffffff
- Text #000000
- Buttons #363636 with white label
- Author links #3298dc
- Finding note #fff2d9 with 2px #000 border

**Example component prompts**

1. Create a finding callout: inline-block card, background #fff2d9, 2px solid black border, 12px radius, 10px 14px padding, Georgia 1.1em, max-width 600px.
2. Create an inline task selector: a sentence in DM Sans 16px where the task name is a borderless underlined native select with transparent background.
3. Create a Nerfies header in DM Sans: centered 40px title weight 600, author names in #3298dc, two dark pill buttons (arXiv, Code) with icons.

## Similar Pages

- Nerfies (nerfies.github.io), the stated base template.
- Readout Guidance project page, the second credited source.
- Other interpretability pages built on Nerfies with a single custom font.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #000000;
  --text-strong: #363636;
  --venue: #555555;
  --author-link: #3298dc;
  --note-bg: #fff2d9;
  --rule: #ededed;
  --font-body: 'DM Sans', sans-serif;
  --font-mono: 'DM Mono', monospace;
  --font-note: Georgia, serif;
  --radius-pill: 290486px;
  --radius-note: 12px;
  --content-max: 70vw;
}
html { font-size: 12pt; }
body { font-family: var(--font-body); color: var(--text); }
.finding-box { background: var(--note-bg); border: 2px solid #000; border-radius: var(--radius-note);
  padding: 10px 14px; font-family: var(--font-note); font-size: 1.1em; line-height: 1.4; max-width: 600px; }
```

## Provenance

- URL: https://vlm-cross-modal-reps.github.io/
- Paper: Vision-Language Models Create Cross-Modal Task Representations (Grace Luo et al.), arXiv 2410.22330.
- Venue: ICML 2025 (per the arXiv comment). Field: VLM interpretability.
- Selection reason: arXiv comment states acceptance at ICML 2025; project page linked in the arXiv abstract.
- Template credit: footer says the template is based on the Nerfies and Readout Guidance project pages.
- Measurement: Measured from static HTML and CSS only (tools/extract_style.py plus a direct read of the page's own stylesheets and inline styles). The page was not rendered in a browser for this entry, so computed styles, actual font fallback, and video framing are not verified.
