# MT-RewardTree — Style Reference

> A whiteboard sketch pinned to a clean wall: a doodled pine tree, marker-drawn triangle and crayon-bordered boxes, framed by tidy charcoal buttons.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and top-of-page tall screenshots, the page's `bulma.min.css`, `index.css`, `index_mmmu.css` and `index.html`, and a browser probe of `.content p`, the hero wrappers and the footer (probed at 1024px; those values do not depend on width). The paper title and the teaser are images (`title-MT-RewardTree.png`, `MT-RewardTree_structure.png`) whose hand-lettered type is drawn into the PNGs, so no web font produces it. `index.css` sets `.container { max-width: 1200px; padding: 20px; padding-top: 10px }`; in the hero that wins over Bulma's `is-max-desktop` (960px), while in the content sections Bulma's widescreen rule (`.container:not(.is-max-desktop):not(.is-max-widescreen)`, max 1344px) wins, so the two parts render at different widths.

## Overview

A Nerfies-style Bulma page on white whose personality comes entirely from the paper's own drawings. The hero opens with a 696px-wide title image: a cartoon pine tree in mint greens with coloured baubles next to "MT-RewardTree" in a heavy hand-drawn marker face. Below sit one line of seven sky-blue author links in Google Sans 20px, one affiliation line, and three charcoal pill buttons (arXiv, Github, Hugging Face). The teaser is a large hand-drawn diagram: a black triangle labelled Reward Modeling, Reward Evaluation and Application around the tree, with arrows to three sketchy boxes outlined in red, blue and green. Text sections (Abstract, Token-level Preference Pairs Construction, Experimental Results, Practical Insights) are centred 32px headings over 19px justified Noto Sans paragraphs, broken by method and result figures. A #fafafa footer closes the page; there is no BibTeX.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 88.0%, near-black #191919 2.9% (title lettering and diagram lines), #f5f6f6 2.2%, mint #abd1cb 2.1% (tree), grey #999796 1.8% (antialiasing), dark green-grey #4c5c54 1.6% (tree outline and buttons, blended), #feffff 1.3%. The author blue is too small to form a cluster.

Anatomy in DOM order (desktop 1440px; `section.hero > .hero-body` padding 48px 24px; `.container` padding 10px 20px 20px, max 1200px, so the hero column is 1160px wide from x=140):

1. **Title image** (y=58, 696×133 at x=372): PNG with the tree mascot and hand-lettered "MT-RewardTree" in black, inline `max-width: 60%; margin-bottom: 1rem`. Gap 16px plus the first author line's leading.
2. **Authors** (`.publication-authors.is-size-5`, y≈217, text at y=226): Google Sans 20px / 400, line-height 36px, centred; names #209cee (`hsl(204, 86%, 53%) !important`), commas and superscripts #4a4a4a. One line.
3. **Affiliations** (second `.publication-authors`, next line): 20px #4a4a4a, two institutions with superscript 1 and 2.
4. **Buttons** (`.publication-links`, y=313, 40px tall): arXiv (Academicons), Github and Hugging Face (Font Awesome brands), adjacent with no gap between pills; Bulma `button is-normal is-rounded is-dark`.
5. **Teaser** (`section.hero.teaser`, from y=438): `.hero-body` padding 0 24px 48px inside the 1200px container, so the diagram renders 1112×758 at x=164, y=448; caption "MT Reward Tree Structure." `h2.subtitle` 20px Google Sans #4a4a4a centred at y=1216, below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #ffffff | (Bulma body) | page, hero, sections |
| Charcoal | #363636 | Bulma `is-dark`, `$grey-darker` | button fill, section headings (`h2.title`) |
| Text Grey | #4a4a4a | Bulma body text | paragraphs, affiliations, superscripts, teaser caption |
| Author Blue | #209cee | `.publication-authors a` hsl(204,86%,53%) | author names |
| Charcoal Hover | #2f2f2f | Bulma `.button.is-dark:hover` | button hover fill |
| Footer Grey | #fafafa | Bulma `.footer` | footer band |
| Icon Black | #000000 | `.footer .icon-link` | footer icon links |
| Ink (image) | #191919 | (in PNGs) | hand-lettered title and diagram strokes |
| Tree Mint (image) | #abd1cb | (in PNGs) | mascot fill, the only colour in the first viewport |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Body | 'Noto Sans', sans-serif (`index_mmmu.css` overrides `index.css`'s Arial) | Noto Sans 400; bold synthesised | Noto Sans |
| Authors, teaser caption | 'Google Sans', sans-serif | Google Sans 400 | Product Sans-like: Outfit |
| Title lettering | image | hand-drawn marker lettering in the PNG | Comic Neue Bold or Patrick Hand for live text |
| Icons | Font Awesome 6 (brands, solid), Academicons | Font Awesome 6 Brands 400, Free 900, Academicons 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `img` in `.hero .column` | 696×133 image (60% of the 1160px column) | black lettering |
| Authors, affiliations | `.publication-authors.is-size-5` | 20px / 400 / 36px | names #209cee, text #4a4a4a |
| Button | `.button.is-normal` | 16px / 400 / 24px | #ffffff |
| Section heading | `h2.title.is-3` | 32px / 600 / 36px, margin-bottom 24px, centred | #363636 |
| Teaser caption | `.teaser h2.subtitle` | Google Sans 20px / 400 / 25px | #4a4a4a |
| Body | `.content` (index.css) | 19px / 400 / 1.4 = 26.6px, justified, paragraph gap 19px | #4a4a4a |
| Run-in labels | `.content p b` | 19px / 700 followed by a line break | #4a4a4a |
| Base body | `body` (index.css) | 18px / line-height 1.8 | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Buttons | 290486px (`is-rounded`) | 1px solid transparent | none |
| Figures | 0 | none | none |
| Sections | 0 | none | none |

The page has no cards, rules or shadows; all structure comes from whitespace and the drawn figures.

## Layout Metrics

- **Hero**: `.hero-body` padding 48px 24px; `.container` max 1200px, padding 10px 20px 20px, so the hero column is 1160px at x=140. Title image 60% of that = 696px. The hero section is 438px tall.
- **Teaser**: `.teaser .hero-body` padding 0 24px 48px; diagram at full container width 1112px.
- **Text sections**: `section.section` padding 0 24px 48px (index.css removes the top padding); `.container` max 1344px at x=48, padding 10px 20px 20px, margin-bottom 2vh = 18px; the `.column.is-four-fifths` gives a 1038px text column at x=201.
- **Figures**: inline `width: 100%; max-width: 1000px; margin-top: 20px` (MCTS and result figures), formula images at 40% or 70% width.
- **Footer**: Bulma `.footer` #fafafa, padding 48px 24px 96px; 25px icon links and a licence line.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1408px (1440 renders this) | text container 1344px (x=48), hero container 1200px | 19px | title image 696px | four-fifths text column 1038px |
| 1216–1407px | text container 1152px | 19px | 60% of column | — |
| 1024–1215px | text container 960px | 19px | 60% of column | — |
| 769–1023px | 24px section padding + 20px container padding | 19px | 60% of column | Bulma columns still side by side |
| ≤768px | same | 19px | 60% of column | columns stack; four-fifths column becomes full width |

## Components

- **Charcoal pill button** (`.button.is-normal.is-rounded.is-dark`): #363636 fill, #ffffff 16px / 400 Noto Sans, padding 7px 20px, 40px tall, radius 290486px, 1px transparent border; leading icon in a 24px `.icon` span (Academicons arXiv, Font Awesome GitHub and Hugging Face). Hover fill #2f2f2f. Pills sit flush against each other with 5px vertical margins.
- **Image title**: the title is a transparent PNG at 60% of the column, centred, 16px bottom margin; the mascot sits left of the lettering inside the image.
- **Sketch teaser**: a full-width PNG on white, no frame, followed by a 20px Google Sans caption.
- **Text section**: centred 32px / 600 #363636 heading, 24px gap, then justified 19px paragraphs with 19px gaps; sub-steps use a bold run-in label ("Selection:") with a `<br>` before the text.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title | present but non-standard | an image with mascot and hand-lettered name, not live text |
| Authors / affiliations | yes | centred Google Sans 20px, blue linked names |
| Link buttons | yes | three charcoal pills with brand icons |
| Venue | absent from the source | no venue line on the page |
| Teaser figure | yes | full-width hand-drawn diagram with caption |
| Abstract | yes | centred heading, two justified paragraphs |
| Method description | yes | run-in bold step labels, figure below |
| Results | yes | figures and formula images, no HTML tables |
| Practical insights | yes | text with formula images and result figures |
| BibTeX | absent from the source | the section is commented out |
| Footer | yes | #fafafa with icon links and licence |

## Adapting to Other Content

- **A venue line**: add a centred line under the affiliations in 20px / 700 #363636; keep it as text, not a badge, so the drawn title remains the only graphic in the hero.
- **A results table**: use Bulma `.table.is-striped` inside the 1038px column at 16px, header #363636 / 600, no colour fills; the page's drawn figures already carry the colour.
- **More authors**: let the 20px author line wrap within the 1160px hero column; insert `<br>` after each group of seven names.
- **BibTeX**: restore the template's `section#BibTeX` with a Bulma `pre` (#f5f5f5) under a centred 32px heading.
- **No mascot**: keep the title as live text at 48px / 600 #363636 in Google Sans rather than imitating hand lettering with a web font.

## Do's and Don'ts

- Do let the hand-drawn title and diagram carry the identity; keep the HTML around them plain.
- Do keep buttons charcoal pills with brand icons.
- Do centre section headings and justify body text at 19px.
- Don't add colour to the HTML; colour lives in the drawings (mint tree, red/blue/green boxes).
- Don't frame or shadow the figures; they sit directly on white.
- Don't mix more fonts in; Noto Sans and Google Sans already cover text and authors.

## Surfaces

White everywhere except the #fafafa footer. No bands, cards or gradients.

## Imagery

Hand-drawn, marker-style diagrams: a cartoon pine tree with baubles as the mascot, a black-outlined triangle with rotated hand-lettered labels, and boxes outlined in red, blue and green with rough strokes. Later figures are standard paper diagrams (MCTS steps, bar and line charts) and formula images.

## Layout

Centred hero (image title, authors, buttons), a full-width sketch teaser, then four text sections in a 1038px centred column with full-width figures. About 6,000px tall.

## Agent Prompt Guide

Quick colors: page #ffffff, charcoal #363636, text #4a4a4a, author blue #209cee, footer #fafafa, drawn ink #191919, mint #abd1cb.

1. "Build a centred hero (padding 48px 24px, column 1160px): a transparent PNG title at 60% width with a cartoon mascot and hand-lettered name, 16px below it a 20px Google Sans author line with #209cee names and #4a4a4a superscripts, an affiliation line, then charcoal pill buttons (#363636 fill, #ffffff 16px Noto Sans, padding 7px 20px, 40px tall, fully rounded, brand icon on the left, hover #2f2f2f)."
2. "Make a text section: no top padding, 48px bottom padding, a 1038px centred column; heading 32px / 600 #363636 centred with a 24px gap; paragraphs 19px Noto Sans, line-height 1.4, #4a4a4a, justified, 19px apart; step labels as bold run-ins followed by a line break."
3. "Place a teaser: full container width (1112px) hand-drawn diagram on white with no frame, caption 20px Google Sans #4a4a4a centred below, 48px bottom padding."

## Similar Pages

- Nerfies-template pages whose identity comes from a custom title image or mascot.
- Project pages with hand-drawn (Excalidraw-style) teaser diagrams.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --charcoal: #363636;
  --charcoal-hover: #2f2f2f;
  --text: #4a4a4a;
  --author: #209cee;
  --footer: #fafafa;
  --font-body: "Noto Sans", sans-serif;
  --font-authors: "Google Sans", sans-serif;
  --body-size: 19px;
  --body-leading: 1.4;
  --hero-container: 1200px;
  --text-column: 1038px;
}
```

## Provenance

- **URL**: https://sabijun.github.io/MT_RewardTreePage/
- **Paper**: MT-RewardTree: A Comprehensive Framework for Advancing LLM-Based Machine Translation via Reward Modeling (arXiv 2503.12123), Zhaopeng Feng, Jiahan Ren, Jiayuan Su, Jiamei Zheng, Zhihang Tang, Hongwei Wang, Zuozhu Liu.
- **Venue**: EMNLP 2025 Findings.
- **Selection reason**: the arXiv comment states acceptance at EMNLP 2025 Findings and links this project page.
- **Template credit**: Nerfies/MMMU Bulma template (`index_mmmu.css`); footer carries the CC BY-SA 4.0 licence line.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and tall screenshots, a browser probe of body text and wrappers, and `bulma.min.css`, `index.css`, `index_mmmu.css` and `index.html` read directly, on 2026-10-28.
