# Teal Keyword Nerfies — Style Reference

> A lab notebook in grey and white stripes, where the title marks its own key words in teal and a dashed-panel kettle explains the task before you read a line.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (`tools/computed_style.py`: computed styles of the title and its teal spans, author links, buttons, figure, section headings, list items, tables, `pre` and footer, first-viewport anatomy, loaded fonts and color share), the first-viewport screenshot, a full-height 1440×8400 headless capture for the results and code sections, and the page's own `static/css/index.css` (stock Academic Project Page Template) over Bulma 0.9. Positions are document coordinates at 1440px wide.

## Overview

InstructPart uses the Academic Project Page Template almost unchanged and gets its character from three choices. The 48px Google Sans title colors the words "Instruct", "Part" and "Instruct" (in "Instruction") teal (#008080) with inline styles, so the acronym's origin reads at a glance. The teaser is a single wide figure whose three panels have dashed grey frames drawn into the image (observation, part annotation with colored labels, answer). And the sections alternate between Bulma's light grey hero (#f5f5f5) and white, in the order Highlights (grey), Abstract (white), Dataset and Tasks (grey), Experimental Results (white), Video (grey), BibTeX (white), which gives an even rhythm. Headings on grey bands render in Bulma's translucent black (rgba(0,0,0,.7)); on white they are #363636. Figures carry left-aligned captions with a bold lead ("Figure 1. …", "Table 1. …"). The results section is long: a results table as an image, then three grids of 1.8cm thumbnails (nine methods per row, 10px labels), then a raw JSON example on #f5f5f5.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): white #ffffff 60.3%, Highlights band #f6f6f6 16.9% (Bulma #f5f5f5), light grey #cececa 10.0% (teaser photo tiles and frames), mid grey #777976 7.3% (kettle photos and text), pale blue-grey #eff2f3 3.1%, remainder under 1.5%. The teal title words and the #209cee author links are small in area but are the only flat accents.

Anatomy in DOM order (y = top of element box):

1. **Title** (`h1.title.is-1.publication-title`), y 48, 960px wide, two lines, Google Sans 48px/54px weight 600, #363636 with `<span style="color: teal">` on "Instruct", "Part", "Part" and "Instruct" (#008080), centered. Gap 24px.
2. **Authors** (`.publication-authors`, `is-size-5`), y 182, one line, Google Sans 20px/30px, eight #209cee links separated by #4a4a4a commas, no superscripts. No gap.
3. **Affiliation and venue** (second `.publication-authors`), y about 210, "Robotics Institute, Carnegie Mellon University" 20px/30px #4a4a4a, then a line break and "ACL 2025 Main" in `<b>` (weight 700, #4a4a4a). Gap about 17px.
4. **Link buttons** (`a.external-link.button.is-normal.is-rounded.is-dark`), y 287, "Paper" 105px, "arXiv" 98px, "Data" 96px, 40px tall, #363636 fill, white Noto Sans 16px/400, padding 7px 20px, Font Awesome or Academicons icon left, no shadow. Gap 5px.
5. **Teaser figure** (`figure` with a leading `<br>`), y 332; image y 356, 936×273, full column width; three photo panels with dashed grey frames inside the bitmap. Gap 0.
6. **Caption** (`figcaption.content.has-text-left`), about y 635, two lines 16px/24px #4a4a4a, left-aligned, bold lead "Figure 1. …". The hero ends at y 743.
7. **Highlights band** (`section.section.hero.is-light`), y 743, #f5f5f5, padding 48px 24px; `h2.title.is-3` "Highlights" y 791, Noto Sans 32px/36px 600, rgba(0,0,0,.7), centered; first `li` y 851, 16px/24px justified rgba(0,0,0,.7), disc bullets, 731px wide.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Heading Ink | #363636 | Bulma `.title` | Title, headings on white sections |
| Keyword Teal | #008080 | inline `color: teal` | "Instruct", "Part" words in the title |
| Body Grey | #4a4a4a | Bulma body | Affiliation, venue, captions, body text, `pre` text |
| Band Text | rgba(0,0,0,.7) | Bulma `.hero.is-light` | Headings and text on grey bands (Highlights, Dataset, Video) |
| Author Blue | #209cee | `.publication-authors a` | Author names |
| Link Blue | #3273dc | Bulma `a` | Inline links, citation numbers in tables |
| Button Dark | #363636 | `.button.is-dark` | Paper, arXiv, Data buttons (white text) |
| Button Hover | #2f2f2f | `.button.is-dark:hover` | Dark buttons on hover |
| Band Grey | #f5f5f5 | `.hero.is-light`, `.content pre` | Highlights, Dataset and Video bands; JSON and BibTeX blocks |
| Footer Wash | #fafafa | `.footer` | Footer band |
| White | #ffffff | page | Hero, Abstract, Results, BibTeX sections |

Declared but not visible: `.publication-venue` (#555, bold) and `.publication-awards` (#ff3860) exist in `index.css`; the venue is a plain `<b>` instead.

## Tokens — Typography

- **Title and authors**: declared `'Google Sans', sans-serif`. Rendered: Google Sans 400 only (`fonts_loaded`); the 600 title is synthesized. Substitute: Figtree.
- **Body and headings**: declared `'Noto Sans', sans-serif`. Rendered: Noto Sans 400 only; 600 headings synthesized.
- **Code**: generic `monospace` (Consolas on Windows), reduced to 10px for the JSON example.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title` | 48px / 54px | 600 | #363636, keywords #008080 |
| Section heading | `h2.title.is-3` | 32px / 36px | 600 | #363636 on white, rgba(0,0,0,.7) on grey |
| BibTeX heading | `h2.title` | 32px / 36px | 600 | #363636 |
| Authors, affiliation | `.publication-authors` | 20px / 30px | 400 (venue 700) | #209cee / #4a4a4a |
| Sub-heading | `.content.is-size-5 strong` | 20px | 700 | #363636 |
| Body, list | `.content p`, `li` | 16px / 24px | 400 | #4a4a4a, justified |
| Caption | `figcaption.content` | 16px / 24px | 400, lead 700 | #4a4a4a, left |
| Grid label | `td` inline `font-size: 10px` | 10px / 15px | 400 | #4a4a4a, centered |
| JSON | `pre code` | 10px / 15px | 400 | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link button | 290486px | 1px transparent | none |
| Teaser and figures | 0 | none (the dashed frames are part of the image) | none |
| Thumbnail grid | 0 | none | none |
| `pre` | 0 | none | none |
| Section bands | 0 | none | none |

The page has no shadows, cards or radii apart from the pill buttons.

## Layout Metrics

- **Container**: `.container.is-max-desktop`, 960px (x 240–1200). Hero content uses the full width (title 960px, teaser 936px). Section content sits in a four-fifths column, 768px (x 336–1104, text 763px).
- **Hero**: `.hero-body` padding 48px 24px; title margin-bottom 24px; links in a `.column` (12px padding), each button 5px vertical margin.
- **Sections**: `.section` padding 48px 24px, bands full-bleed. Heading margin-bottom 24px.
- **Figures**: full column width (768px) with captions directly below.
- **Thumbnail grids**: `table` with nine `td`s per row, each image 1.8cm (68px) square, no cell padding; the table is 612px wide and left-aligned in the 768px column.
- **JSON block**: `pre` 625px wide, padding 20px 24px, 10px text.
- **Footer**: #fafafa, padding 48px 24px 96px, template credit.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px | 960px container | 16px | 48px | as described |
| 769–1023px | fluid, 24px section padding | 16px | 48px | four-fifths column remains |
| ≤768px | fluid, 24px | 16px | 48px | columns become full width; thumbnail tables keep 68px cells and overflow |

## Components

- **Keyword title**: Google Sans 48px/54px 600 #363636, centered, with the acronym's source words wrapped in spans colored #008080; no other decoration.
- **Dark pill button**: Bulma `.button.is-dark.is-rounded`, #363636, white 16px Noto Sans, padding 7px 20px, 40px tall, icon left, no shadow; Bulma hover darkens to #2f2f2f.
- **Captioned figure**: `figure` with the image at 100% width and a left-aligned `figcaption.content` (16px #4a4a4a) whose first sentence is bold ("Figure 2. InstructPart dataset examples.").
- **Highlights list**: on a #f5f5f5 band, a disc list of three justified 16px items at rgba(0,0,0,.7).
- **Bold-lead paragraph**: `<b>Term:</b>` followed by plain 16px text, used for dataset and task definitions.
- **Thumbnail comparison grid**: an unstyled `table`, nine 68px square images per row (ground truth plus eight methods), a label row at 10px under each block, preceded by a bold one-line takeaway ("Fine-tuned PISA performs better.").
- **Code example**: `pre` on #f5f5f5, padding 20px 24px, 10px monospace, no radius.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title with highlighted keywords | yes | teal spans in a Google Sans title |
| Authors, affiliation, venue | yes | 20px centered; venue in bold under the affiliation |
| Link buttons | yes | three dark pills |
| Teaser figure | yes | wide image with dashed panels and a bold-lead caption |
| Highlights | yes | grey band, justified bullets |
| Abstract | yes | 768px justified |
| Dataset and tasks | yes | grey band, bold-lead paragraphs, dataset figure |
| Results table | present but non-standard | table rendered as an image with a caption |
| Qualitative grids | yes | 68px thumbnail tables |
| Annotation example | yes | JSON in a grey `pre` |
| Video | present but non-standard | grey band with "coming soon" text only |
| BibTeX | yes | grey `pre` |
| Navigation | absent from the source | |
| Footer | yes | Bulma #fafafa credit |

## Adapting to Other Content

- **More authors**: keep one centered 20px line that wraps; add superscripts and a separate affiliation line only if there are several institutions; keep the venue in bold below.
- **A results table**: an HTML Bulma `.table` inside the 768px column with 16px text, 600 #363636 headers, 1px #dbdbdb rules and the best score in bold; caption below in the same bold-lead style.
- **More sections**: continue the grey/white alternation; a grey band's headings must use rgba(0,0,0,.7).
- **News**: a grey band directly after the hero with a dated disc list in 16px.
- **Long publication lists**: a white section with a 768px disc list, titles bold, venues plain.
- **A highlighted term in prose**: reuse #008080 for the method name, sparingly.

## Do's and Don'ts

- Do color only the words that form the acronym; the rest of the title stays #363636.
- Do alternate #f5f5f5 and white full-bleed sections, one topic per band.
- Do caption every figure with a bold lead sentence, left-aligned.
- Do keep 48px section padding and the 768px reading column.
- Don't add cards, shadows or rounded figures; the page is flat.
- Don't leave thumbnail grids left-aligned in a wider column; center them or size them to the column.
- Don't drop JSON to 10px when the column can hold 14px.

## Surfaces

White and #f5f5f5 bands only, alternating, with #f5f5f5 also used for code blocks and #fafafa for the footer. No cards.

## Imagery

Kitchen and household photographs (kettles, knives, scissors, mugs) with colored part overlays, the teaser drawn as three dashed panels with a cartoon user, a robot icon and navy arrows; results as dense rows of square thumbnails where predicted part masks are painted solid red and ground truth green.

## Layout

A centered 960px Nerfies container with a 768px reading column, stacked as alternating full-bleed bands. Rendered height is about 8,300px at 1440px, most of it the qualitative grids and the JSON example.

## Agent Prompt Guide

Quick colors: title #363636 with keywords #008080, body #4a4a4a, band text rgba(0,0,0,.7), authors #209cee, buttons #363636, bands #f5f5f5, footer #fafafa.

1. "Build a hero in a 960px column: centered Google Sans 48px/54px weight 600 #363636 title where the words that make up the acronym are colored #008080; 24px below, 20px/30px #209cee author links on one line; under it the affiliation in 20px #4a4a4a and the venue in bold; then three #363636 pill buttons, white 16px Noto Sans, padding 7px 20px, icon left."
2. "Add a full-width figure: the image at 100% of the column, then a left-aligned 16px/24px #4a4a4a caption whose first sentence is bold, for example 'Figure 1. The task.'"
3. "Stack sections as alternating full-bleed bands, padding 48px 24px: grey #f5f5f5 bands with headings and text in rgba(0,0,0,.7), white bands with #363636 headings; headings are Noto Sans 32px/36px 600 centered, body 16px/24px justified in a 768px column."

## Similar Pages

- Academic Project Page Template and Nerfies derivatives with Bulma `hero is-light` bands.
- Segmentation and grounding project pages that show method comparisons as thumbnail grids.

## Quick Start

```css
:root {
  --heading: #363636;
  --keyword: #008080;
  --text: #4a4a4a;
  --band-text: rgba(0, 0, 0, .7);
  --author: #209cee;
  --link: #3273dc;
  --button: #363636;
  --band: #f5f5f5;
  --footer: #fafafa;
  --font-title: 'Google Sans', Figtree, sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --container: 960px;
  --column: 768px;
  --section-pad: 48px 24px;
}
```

## Provenance

- **URL**: https://zifuwan.github.io/InstructPart/
- **Paper**: InstructPart: Task-Oriented Part Segmentation with Instruction Reasoning (arXiv 2505.18291), Zifu Wan et al., Carnegie Mellon University.
- **Venue**: ACL 2025 (Main).
- **Selection reason**: existing verified entry; the arXiv 2505.18291 comment states acceptance at ACL 2025 Main and links the page. Chosen for the teal keyword highlighting in the title, the dashed-frame teaser, the alternating grey and white bands and cleanly captioned figures.
- **Template credit**: footer credits the Academic Project Page Template, adopted from Nerfies.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and fonts, the first-viewport screenshot and full-page capture, a 1440×8400 headless capture, `static/css/index.css` and the HTML. Date 2026-10-28.
