# DPLM-2.1 Coral Spotlight — Style Reference

> A Nerfies page that reads like a structured technical report with a table of contents.

**Theme:** light

Values come from the static HTML, its inline `<style>` and inline attributes, the stock Nerfies `index.css`, and a custom `animation_style.css`, all over Bulma 0.9. Bulma's unused palette is excluded. Measurements are normalized; roles are interpreted.

## Overview

The DPLM-2.1 page keeps the stock Nerfies hero (Google Sans title, sky-blue author links, dark rounded buttons) and adds two strong signals. The venue line "ICML 2025 (Spotlight)" is a semibold `subtitle is-3` in coral `#F05365`, and the hero ends in a 1px `#dbdbdb` rule. The body then behaves like a report: an in-page Table of Contents with nested lists, eight h2 sections and six h3 subsections, four Bulma `table is-bordered is-striped is-narrow is-hoverable is-fullwidth` results tables, gray left-ruled italic callouts for key findings, and a warm cream `rgb(252,247,237)` highlighter on one phrase. A custom CSS animation shows protein sequences in Courier boxes next to structure thumbnails.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Spotlight Coral | `#F05365` | (inline) | Venue and award line "ICML 2025 (Spotlight)" |
| Bulma Charcoal | `#363636` | Bulma `.title`, `button is-dark` | Title, h2, link buttons |
| Body Gray | `#4a4a4a` | Bulma `$text` | Body text (inferred Bulma default) |
| Author Sky | `hsl(204, 86%, 53%)` | Nerfies `.publication-authors a` | Author links (≈ `#209cee`) |
| Link Blue | `#3273dc` | Bulma `$link` | TOC and body links |
| Hero Rule | `#dbdbdb` | (inline) | 1px border under the hero |
| Callout Paper | `#f9f9f9` | (inline) | Finding callout background |
| Callout Rule | `#cccccc` | (inline) | 4px left border on callouts |
| Cream Highlight | `rgb(252,247,237)` | (inline) | Background mark on "highlight these results" |
| Sequence Box | `#e9ecef` | `.sequence-text-box` | Courier sequence chip, 1px `#adb5bd` border, text `#212529` |
| Label Gray | `#555555` | `.data-label` | Animation labels |
| Table Stripe | `#fafafa` | Bulma `.table.is-striped` | Even rows (Bulma default, inferred) |
| Table Border | `#dbdbdb` | Bulma `.table.is-bordered` | Cell borders |
| Carousel Rule | `#bbbbbb` | Nerfies | Carousel item border |

## Tokens — Typography

- **Display / authors:** `Google Sans` (Google Fonts link also loads Noto Sans and Castoro). Substitute: Product Sans, Inter.
- **Body:** `Noto Sans` (Nerfies). Castoro is loaded but unused (inferred).
- **Sequences:** `'Courier New', Courier, monospace` at 0.9em.
- **Small caps:** `.small-caps` / `.dnerf` for model names.
- **Math:** MathJax is loaded.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Title (`title is-1`) | 3rem | 600 | Two lines, Google Sans |
| Venue line (`subtitle is-3`) | 2rem | 600 (`has-text-weight-semibold`) | Coral; "Spotlight" bold |
| Authors | `is-size-6` 1rem | 400 | Superscripts for affiliations, equal contribution, corresponding |
| Section h2 (`title is-3`) | 2rem | 600 | |
| Subsection h3 | 1.5rem (Bulma `is-4`, inferred) | 600 | |
| Inline subheads | `1.9ch` | 500 | Custom inline size |
| Table text | 0.8em / 0.75em (inline) | 400 | Narrow tables |
| Sequence chip | 0.9em mono | 400 | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px (Bulma rounded) |
| Carousel items, video wrapper | 10px (Nerfies) |
| Sequence chip, structure image | 4px |
| Callouts, tables | 0 |

- **Shadows:** none beyond Bulma defaults.
- **Layout:** Bulma `container is-max-desktop` (960px); hero padding-bottom reduced to 1.2rem; figures inline at 80% (one at 120%); video grids at 80% (3 columns, 4px gap) and 60% (2 columns, 10px gap).

## Components

- **Dark pill link button.** Bulma `external-link button is-normal is-rounded is-dark` with icon or emoji: Paper, Video, Code, "🤗 Model Checkpoints (Incoming)", "📚 Citation".
- **Coral venue line.** Semibold 2rem coral subtitle between title block and buttons; the award word in `<b>`.
- **Table of Contents.** h2 followed by nested `<ul>` anchor links in Bulma blue.
- **Finding callout.** Inline-styled block: 4px `#ccc` left border, 1em padding, `#f9f9f9` fill, italic and bold text.
- **Results table.** Bulma `table is-bordered is-striped is-narrow is-hoverable is-fullwidth`, small 0.75–0.8em type, wrapped in a figure with 1rem vertical margins.
- **Sequence animation.** Absolutely positioned flex row with a Courier chip (`#e9ecef`, 1px `#adb5bd`, 4px radius) beside an 85px structure image, fading in over 0.5s.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Nerfies centered hero with bottom hairline |
| Venue badge | "ICML 2025 (Spotlight)" | Coral semibold text, no chip |
| Link buttons | Paper, Video, Code, Model Checkpoints, Citation | Dark rounded with emoji icons |
| Teaser / video | "Video" section | Nerfies video wrapper |
| Abstract | Yes | Justified content |
| Table of Contents | Yes | Nested list |
| Method / design space | Overview figure, findings, six subsections | Figures and callouts |
| Results tables | 4 Bulma tables | Bordered, striped, narrow |
| Carousel | Bulma carousel script loaded | |
| Conclusion | Yes | |
| BibTeX | Yes | Nerfies pre |
| Acknowledgements | Yes | |

## Do's and Don'ts

- Do give the venue and award line a single warm accent, distinct from the blue links.
- Do add a TOC when the page has more than six sections.
- Do use Bulma's striped, narrow tables at reduced size for dense numbers.
- Don't use the coral anywhere else; it marks the venue only.
- Don't restore the commented-out "ICCV 2023 (Oral, Best Student Paper)" line left over from the template's source page.

## Surfaces

White throughout, with a hairline under the hero and light gray `#f9f9f9` callouts.

## Imagery

Protein structure renders, design-space diagrams, and short videos in 2- and 3-column grids.

## Layout

Single 960px Bulma column; tables full-width within it; some figures intentionally overflow to 120%.

## Agent Prompt Guide

**Quick colors:** text `#4a4a4a`, title `#363636`, venue `#F05365`, link `#3273dc`, callout `#f9f9f9` with `#ccc` rule, highlight `rgb(252,247,237)`.

1. "Under a Google Sans 3rem title, add a 2rem semibold venue subtitle in `#F05365` reading 'ICML 2025 (Spotlight)' with 'Spotlight' in bold."
2. "Create a key-finding callout: 4px `#ccc` left border, 1em padding, `#f9f9f9` fill, bold italic text."
3. "Render results as a Bulma table with `is-bordered is-striped is-narrow is-hoverable is-fullwidth` at 0.8em text inside a figure with 1rem top and bottom margins."

## Similar Pages

Other Nerfies pages with report-style structure; CoMemo and EQ-VAE in this collection also add many h2/h3 sections on the Nerfies base.

## Quick Start

```css
:root {
  --text: #4a4a4a; --title: #363636; --link: #3273dc;
  --author: hsl(204, 86%, 53%); --venue: #F05365;
  --rule: #dbdbdb; --callout-bg: #f9f9f9; --callout-rule: #cccccc;
  --mark: rgb(252,247,237);
  --chip-bg: #e9ecef; --chip-line: #adb5bd; --chip-ink: #212529;
  --font-display: "Google Sans", "Inter", sans-serif;
  --font-body: "Noto Sans", sans-serif;
  --font-seq: "Courier New", Courier, monospace;
  --container: 960px;
}
```

## Provenance

- **URL:** https://bytedance.github.io/dplm/dplm-2.1/
- **Paper:** Elucidating the Design Space of Multimodal Protein Language Models (arXiv 2504.11454), Cheng-Yen (Wesley) Hsieh et al.
- **Venue:** ICML 2025 Spotlight (shown on the page as "ICML 2025 (Spotlight)").
- **Selection reason:** arXiv comment states acceptance at ICML 2025 and links this project page.
- **Template credit:** footer says the site "is borrowed from Nerfies" (CC BY-SA 4.0).
- **Measurement method:** `extract_style.py` plus manual reading of inline styles, `index.css` and `animation_style.css` (`style.css` returned empty). Commented-out markup excluded. Rendered page not viewed.
