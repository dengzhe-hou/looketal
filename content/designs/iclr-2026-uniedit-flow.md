# UniEdit-Flow Lilac Serif — Style Reference

> A lilac-inked lab report: a serif masthead, a row of tabs, and before-and-after sliders that do the explaining.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide first-viewport and tall screenshots, the page's `assets/css/index.css` (Nerfies-derived), `tab_gallery.css`, `juxtapose.css`, and the stacked Bootstrap and Bulma files. Inline `style` attributes carry the purple. Several declared fonts never load: the title's `font-family: Lato` has no source, so it renders in Times New Roman bold; Noto Sans and Google Sans (body, authors) fall back to the default sans-serif, Arial on Windows. Only Source Sans Pro 700 (section titles) and MathJax fonts load. Color share is measured on the first viewport.

## Overview

A white Nerfies-style page whose masthead looks typeset, not templated: "UniEdit-Flow" in lilac (#8d85e5) on its own line, then "Unleashing Inversion and Editing in the Era of Flow Models" in heavy charcoal serif, both at 48px. Below come a bold "ICLR 2026" line, Arial author names with two linked names in lilac, a small affiliation line, and three charcoal pill buttons (Paper, Code, BibTex). The teaser is a 930px three-column figure (Diverse Existing Tasks, Vanilla Flow, UniEdit-Flow) of baseball, storefront, dog, goat and kitten edits with handwritten-style labels and emoji, followed by a justified paragraph whose key claim is bold italic lilac. Just under the fold, a tab row of four equal 24%-wide buttons (Home filled #8784c7, the rest outlined with lilac text) links to sibling pages. Further down: a centered Overview, a captioned two-panel method diagram, a #f5f5f5 "Feature" band of three-column Source / Uni-Edit split sliders for FLUX, Stable Diffusion 3 and SDXL, a Method section with MathJax, and BibTeX.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 70.9%, dark warm grey #44423f 7.1% (title type and dark photo areas), pale grey #c7c6c8 7.1% and stone #948e8d 6.4% (teaser photos), cool off-white #e9ebee 4.1%, warm white #faf9f9 2.9%. The lilac word and links are under 1%.

Anatomy in DOM order (Bulma `.container.is-max-desktop` 960px with Bootstrap's 15px padding, so content x=255–1185):

1. **Title line 1** — `h1.title.is-1.publication-title > span`, "UniEdit-Flow", 48px, declared Lato / 600, rendered Times New Roman bold, #8d85e5 (inline), centered (y=28–81). The `h1` has margin-top −20px.
2. **Title lines 2–3** — same `h1` after a `<br>`, "Unleashing Inversion and Editing in the Era / of Flow Models", Times New Roman bold 48px, line-height 54px, #363636 (to y=190). Margin-bottom 24px.
3. **Venue** — `p > b`, "ICLR 2026", 24px bold, Arial (declared Noto Sans), #4a4a4a (y=214–250).
4. **Authors** — `p.publication-authors`, 20px Arial (declared Google Sans), #4a4a4a; unlinked names plain, linked names in a #8d85e5 span; superscripts (y=262–292).
5. **Affiliations** — 16px Arial, #4a4a4a, one line (y=292–316). Gap 24px.
6. **Buttons** — three `a.external-link.button.is-normal.is-rounded.is-dark`, 40px tall, #363636, #ffffff 16px Arial, padding 7px 20px, pill, icon left (y=345–385).
7. **Teaser** — `img`, 930×293px at y=426: three column groups with cursive-style headings ("Diverse Existing Tasks", "Vanilla Flow", "UniEdit-Flow"), sub-labels with emoji, and a 2×N grid of photos per group.
8. **Teaser paragraph** — justified 16px Arial, #4a4a4a, bold lead "UniEdit-Flow for image inversion and editing." and a bold italic #8d85e5 claim (y=743–863).
9. **Tab row** — four `a.external-link.button.is-normal`, each `width: 24%` (217px) × 40px, Bulma 4px radius, 1px #dbdbdb border, 16px Arial; "Home" #ffffff on #8784c7, the others #8784c7 on #ffffff (y=904–944, just below the fold).

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | Bulma `$white` | page, outlined tab fill, button text |
| Charcoal | #363636 | Bulma `.title`, `is-dark` | title lines 2–3, section titles, pill buttons |
| Body Grey | #4a4a4a | Bulma body | venue, authors, affiliations, paragraphs, BibTeX text |
| Lilac Ink | #8d85e5 | inline `rgb(141,133,229)` | "UniEdit-Flow" title word, linked author names, highlighted claims |
| Tab Lilac | #8784c7 | inline | active tab fill, inactive tab text |
| Tab Rule | #dbdbdb | Bulma `.button` border | tab borders |
| Feature Band | #f5f5f5 | Bulma `.hero.is-light`, `pre` | Feature section band, BibTeX block |
| Band Title | rgba(0,0,0,0.7) | Bulma `.hero.is-light .title` | "Feature: Text-driven Image / Video Editing" |
| Code Rule | #cccccc | Bootstrap `pre` | 1px BibTeX border |
| Footer Fog | #fafafa | Bulma `.footer` | footer |
| Slider Label | rgba(0,0,0,0.7) | `.jx-label` | "Source" and "Uni-Edit" chips on sliders |
| Glyph Plum | #5555aa | inline | a math legend glyph in the Method text |
| Glyph Mauve | #caa6ca | inline | a math legend glyph in the Method text |
| Glyph Teal | #5d9eab | inline | a math legend glyph in the Method text |

## Tokens — Typography

- **Title:** declared `font-family: Lato` with no `@font-face` or font link; renders Times New Roman bold (Windows) or Times (macOS). This accidental serif is the page's most distinctive feature. Substitute that keeps the rendered look: Tinos Bold or Liberation Serif Bold. If you want what the author intended: Lato Bold.
- **Body and authors:** declared `'Noto Sans', sans-serif` and `'Google Sans', sans-serif`; neither loads, so both render in the default sans-serif (Arial on Windows, Helvetica on macOS). Substitute: Arimo.
- **Section titles:** `"Source Sans Pro", Calibri, Candara, Arial, sans-serif`; renders Source Sans Pro 700 (the only weight loaded). Substitute: Source Sans 3 Bold.
- **Teaser and diagram labels:** baked into the images (a casual handwritten-style face).
- **Math:** MathJax 2.7 CHTML fonts.

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `.title.is-1.publication-title` | 48px / bold serif (rendered) / 54px |
| Section title | `h2.title.is-3` | 32px / 700 Source Sans Pro / 36px |
| Sub-section | `h3` | 24px / 700 Source Sans Pro |
| BibTeX title | `h2.title` | 28px / 700 |
| Venue | `p > b` | 24px / bold / 36px |
| Authors | `.publication-authors` | 20px / 400 / 30px |
| Affiliations | `.publication-authors` small | 16px |
| Body | `p`, `.content` | 16px / 400 / 24px, justified in text blocks |
| Buttons and tabs | `.button` | 16px / 400 |
| Code | `pre` | 14px / 20px |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Link buttons | pill (Bulma `is-rounded`), padding 7px 20px |
| Tabs | 4px radius, 1px #dbdbdb border, padding 7px 16px, 24% width each |
| Slider labels | square chips, padding 0.25em 0.75em, white text on rgba(0,0,0,0.7) |
| Teaser, figures, sliders | square corners, no shadow |
| BibTeX `pre` | 1px #cccccc border, padding 17.5px 21px |
| Divider `hr` | 2px gradient line fading white → rgba(0,0,0,0.35) → white |

## Layout Metrics

- **Container:** Bulma `.container.is-max-desktop` capped at 960px over a Bootswatch 3.3.5 (Bootstrap 3) `.container` with 15px padding and fixed widths; content 930px (x=255–1185 at 1440).
- **Hero:** `.hero-body` padding 48px 24px 24px (custom `padding-bottom: 24px`); title pulled up 20px.
- **Sections:** `.section` padding 48px 24px; Feature band `.hero.is-light.is-small` with 24px body padding.
- **Teaser:** 930px image, full content width.
- **Tab row:** four 24% buttons in a centered flex row with small gaps (x=278–1162).
- **Feature grid:** three Bulma columns (about 290px each) of 4:3 split sliders, a prompt line centered above each row.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1024px | (viewport − 930)/2 | 16px | 48px | three slider columns; Bulma caps the container at 960px |
| 992–1023px | (viewport − 940)/2 | 16px | 48px | Bootstrap 3 fixes `.container` at 970px |
| 769–991px | (viewport − 720)/2 | 16px | 48px | Bootstrap 3 fixes `.container` at 750px; Bulma columns still side by side |
| ≤768px | 39px (24px section padding plus 15px container padding) | 16px | 48px (no mobile step) | Bulma columns stack, sliders go one per row; tabs stay 24% wide and their labels wrap |

## Components

- **Two-tone serif masthead:** a 48px bold serif title where the product name sits on its own line in #8d85e5 and the subtitle follows in #363636, centered, line-height 54px.
- **Charcoal pill button:** Bulma `.button.is-dark.is-rounded`, #363636, #ffffff 16px, padding 7px 20px, Font Awesome or academicons icon left.
- **Sub-page tab row:** four equal Bulma buttons at 24% width, 4px radius, 1px #dbdbdb border; the current page filled #8784c7 with #ffffff text, the others white with #8784c7 text; each links to a sibling page (Compare: Reconstruction, Compare: Editing, Gallery).
- **Emphasis run:** bold italic phrase in #8d85e5 inside an otherwise #4a4a4a justified paragraph.
- **Split slider card:** JuxtaposeJS slider, starting at 30%, animated; square "Source" chip at top left and "Uni-Edit" chip at top right, white text on 70% black; a centered prompt line above with struck-through old words and bold or underlined new words.
- **Model column heading:** bold label with a small flower emoji ("FLUX 🌸", "Stable Diffusion 3 🌸", "Stable Diffusion XL 🌸").
- **Method figure:** two-panel diagram (Vanilla vs UniEdit-Flow) with a bold "An overview" caption lead.
- **BibTeX:** `pre` on #f5f5f5 with a 1px #cccccc border.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / venue / authors / affiliations | Yes | two-tone serif title, Arial meta lines |
| Link buttons | Yes | three charcoal pills |
| Sub-page navigation | Present but non-standard | four 24%-wide tab buttons linking to sibling pages |
| Teaser | Yes | three-group image with labels, plus a justified caption paragraph |
| Overview / abstract | Yes | centered heading, justified text with lilac emphasis |
| Method figure | Yes | captioned two-panel diagram |
| Qualitative comparisons | Yes | three-model grid of Source / Uni-Edit split sliders on a grey band |
| Method details | Yes | Uni-Inv and Uni-Edit sub-sections with MathJax and colored glyph legends |
| Results table (HTML) | No (absent from the source) | |
| Video | Present but non-standard | the band title mentions video editing; results are image sliders |
| BibTeX | Yes | bordered grey `pre` |
| Footer | Yes | #fafafa with CC license |

## Adapting to Other Content

- **More authors:** keep one 20px line per row, linked names in #8d85e5 spans, superscripts; wrap naturally.
- **Results table:** a Bulma `.table` in the 930px column, 16px, #363636 headers in Source Sans Pro 700; mark your row's best numbers in bold #8d85e5 to reuse the emphasis color.
- **Long publication or news list:** under the tab row, a list with bold #363636 titles and the venue in italic #8d85e5.
- **More sibling pages:** add tabs but shrink the width so all fit on one row (for five, about 19% each); keep exactly one filled.
- **Video results:** use the same three-column grid with "Source" / "Ours" labels burned into the video corners in white on 70% black.

## Do's and Don'ts

- Do load the serif deliberately (or set Tinos Bold) if you want this masthead; the source gets it by accident.
- Do keep lilac for the product name, linked names and the one emphasized claim per paragraph.
- Do label every split slider with square "Source" / method chips.
- Don't mix the two purples within one component: #8d85e5 is for text, #8784c7 for the tab row.
- Don't round the sliders or figures.
- Don't rely on undeclared font files; list a fallback that matches the look you want.

## Surfaces

White page and header, one #f5f5f5 Feature band, #f5f5f5 BibTeX, #fafafa footer; a faint gradient `hr` between some blocks.

## Imagery

Photographic edit pairs (cats, birds, dogs, baseball players, storefronts) and origami edits, a two-panel flow-trajectory diagram in muted blue and purple, and a three-group teaser with cursive labels and emoji.

## Layout

Centered 930px column, tab row after the teaser, one grey band of three-column sliders. Rendered height about 6,500px.

## Agent Prompt Guide

Quick colors: title #363636, product word and emphasis #8d85e5, tabs #8784c7 with #dbdbdb borders, body #4a4a4a, band #f5f5f5, footer #fafafa, page #ffffff.

1. "Build a masthead: centered 48px bold serif (Tinos Bold or Times New Roman) with line-height 54px; first line 'ProductName' in #8d85e5, then the subtitle in #363636 over two lines; a 24px bold 'ICLR 2026' line in #4a4a4a; 20px Arial authors with linked names in #8d85e5; three #363636 pill buttons with #ffffff 16px labels and padding 7px 20px."
2. "Create a sub-page tab row: four buttons each 24% wide, 40px tall, 4px radius, 1px #dbdbdb border, 16px text; the current one #ffffff on #8784c7, the others #8784c7 on #ffffff."
3. "Make a comparison band: full-width #f5f5f5 section, 32px Source Sans Pro 700 title; three columns, each headed by a bold model name, holding 4:3 before/after sliders that start at 30% and carry square 'Source' and 'Ours' chips in white on rgba(0,0,0,0.7); a centered prompt line above each row with struck-through and bold words."

## Similar Pages

- Nerfies-template pages extended with sibling sub-pages (Compare, Gallery) and JuxtaposeJS sliders.
- Image-editing papers that present results as prompt-captioned before/after sliders.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --title: #363636;
  --text: #4a4a4a;
  --accent: #8d85e5;
  --tab: #8784c7;
  --tab-border: #dbdbdb;
  --band: #f5f5f5;
  --footer: #fafafa;
  --label-bg: rgba(0, 0, 0, 0.7);
  --font-title: 'Tinos', 'Times New Roman', serif;
  --font-body: 'Arimo', Arial, sans-serif;
  --font-section: 'Source Sans 3', 'Source Sans Pro', sans-serif;
  --title-size: 48px;
  --title-lh: 54px;
  --body-size: 16px;
  --container: 960px;
}
```

## Provenance

- **URL:** https://uniedit-flow.github.io/
- **Paper:** UniEdit-Flow: Unleashing Inversion and Editing in the Era of Flow Models (arXiv 2504.13109), Guanlong Jiao, Biqing Huang, Kuan-Chieh Wang, Renjie Liao.
- **Venue:** ICLR 2026 (stated under the title).
- **Selection reason:** existing verified entry; the arXiv comment reads "ICLR 2026" and links the page. Chosen for its purple accent system, tabbed sub-navigation, captioned overview diagram, three-model split-slider comparisons and serif headings.
- **Template credit:** none stated on the page; `index.css` is the Nerfies stylesheet with small edits.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share and loaded-font list, 1440 first-viewport and tall screenshots, `assets/css/index.css`, `tab_gallery.css`, `juxtapose.css`, inline styles in the page HTML; 2026-10-28.
