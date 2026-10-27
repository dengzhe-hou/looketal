# SemanticDraw Rust Outline — Style Reference

> A geometric title stamped in rust, highlighter strokes under every name, and a paintbrush that never stops moving.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 screenshot, scrolled captures of the full 7,973px page, the page's own `/css/index_project_page.css` and `/css/satoshi.css`, and the inline styles in the markup. The page is a Nerfies derivative on Bulma 0.9 inside the author's personal site (it keeps the site's "More Research" navbar). Two typefaces are system or self-hosted rather than Google Fonts; see Typography. Color share is measured on the first 1440×900 viewport.

## Overview

A white hero with a geometric, heavy title: "SemanticDraw:" in rust brown #732a14 and the rest in charcoal #363636, both in Century Gothic Bold at 40px. Author names sit on a half-height cream highlighter stripe (#fbebca), followed by the lab name, the Computer Vision Lab logo and a light "CVPR 2025". Six outlined pill buttons in rust #ab4012 run in two centred rows (Paper, Code, Poster; three Hugging Face demos). The first band below is a pale #fafbfb strip holding an 800×450 YouTube demo and a one-line caption. The main column (940px) opens with a wide film-strip teaser figure (inputs drawn with a semantic palette, outputs as an image stream), then left-aligned 32px Satoshi section heads, justified 16px Satoshi body, carefully drawn method diagrams with soft pastel blocks, light grey 1px separators, and alternating #fafbfb bands for the demo videos. It ends with a BibTeX block, a numbered reference list and a #fafbfb footer.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 51.3%, pale band #fafbfb 21.8% (the demo strip), warm grey #817777 15.5% (title, text and the dark parts of the demo frame), near-whites #fdfdfd 7.0% and #fdfbf8 3.6% (the cream highlighter and video background), traces under 1%. Rust and cream are visible accents but small by area.

Anatomy in DOM order (hero `.container.has-text-centered` 1344px max-width with 10px side padding; section padding 48px 0):

1. **Site navbar** — Bulma `.navbar`, 52px tall, white, centred `navbar-start`: a home icon (40px item) and a "More Research" dropdown, Noto Sans 16px #4a4a4a, Bulma blue chevron (y=0–52). Gap 48px.
2. **Title** — `p.title.is-2.publication-title`, Century Gothic 40px / 900 (renders the face's bold) / line-height 45px, centred, two lines (y=100–190); "SemanticDraw:" wrapped in `<font color="#732a14">`, the rest #363636. Gap 24px.
3. **Authors** — `p.title.is-4.publication-authors`, Century Gothic 24px / 600 / 27px #363636 for the commas and "and"; each name is `a.author-block`, #000000, declared weight 200 (renders regular), on `linear-gradient(to top, #fbebca 50%, transparent 50%)`; hover fills the whole name #fbebca (y=214–242). Gap 4px (−20px margin pulls the next line up).
4. **Affiliation and logo** — `p.subtitle.is-5.publication-authors`, Century Gothic 20px / 400 #4a4a4a, "Computer Vision Lab, Seoul National University", then the lab logo image, width min(200px, 80vw), margin-top 16px (y=246–339). Gap 0.
5. **Venue** — `p.subtitle.is-4`, "CVPR 2025", Satoshi 24px / 400 / 30px #4a4a4a (y=339–369). Gap 24px.
6. **Buttons** — two flex-wrap rows of `span.icon-text.mx-1 > a.button.is-rounded`: Paper (Academicons arXiv), Code (Ionicons logo-github), Poster (Font Awesome file-pdf); then Demo: Main, Demo: Canvas (SDXL), Demo: Canvas (SD3) with the Hugging Face logo image. Noto Sans 16px / 400, #ab4012 text and 1px border on #ffffff, pill radius, padding 7px 20px, 4px side margin, 5px bottom margin; rows at y=393–433 and y=438–478. Gap 53px.
7. **Demo strip** — `section.hero.is-light.is-small` with inline `background-color: #fafbfb`; `.video` max-width 800px holding a YouTube iframe 800×450 at x=320, y=555; caption below at y=1011. The fold cuts the video.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | Bulma `html` | page background, navbar, button fill |
| Title Charcoal | #363636 | Bulma `.title` | title (after the colon), author separators |
| Rust Brown | #732a14 | inline `<font color>` | "SemanticDraw:" in the title |
| Rust Orange | #ab4012 | `.icon-text a` (!important) | button text, border and icons; hover fill |
| Highlighter Cream | #fbebca | `.author-block` gradient | lower half of each author name; full fill on hover |
| Name Black | #000000 | `.author-block` color | author names |
| Body Grey | #4a4a4a | Bulma body color | venue, affiliation, section heads, body, captions, BibTeX, references |
| Band Text | rgba(0,0,0,0.7) | Bulma `.hero.is-light` | demo-strip caption |
| Pale Band | #fafbfb | inline styles | demo strip, Semantic Palette and Real-Time bands, BibTeX block, footer |
| Separator | #c0c0c0 | `.sep` border-bottom | 1px rules between sections |
| Link Blue | #3273dc | Bulma `a` | inline links (code, Hugging Face demo, references, footer) |
| Frame Grey | #817777 | (screenshot) | dominant mid-tone of the first viewport (text and the demo frame) |

## Tokens — Typography

- **Display:** declared `"Century Gothic", CenturyGothic, AppleGothic, sans-serif` on `.publication-title` and `.publication-authors` (with !important). It is not web-loaded: it renders where Century Gothic is installed (it was on the capture machine; it ships with Microsoft Office), AppleGothic on older Macs, otherwise the default sans. Weights render as regular and bold only. Substitute: URW Gothic (free, same Avant Garde-like proportions).
- **Text:** declared `'Satoshi-Regular', CenturyGothic, AppleGothic, sans-serif` on `.content` and `.subtitle`; rendered Satoshi-Regular 400, self-hosted via `/css/satoshi.css`. Substitute: General Sans or Inter.
- **UI:** `body` is `'Noto Sans', sans-serif` (Google Fonts, 400 rendered); used for the navbar, buttons, BibTeX and references.
- **Declared but not visible:** Jost, Pretendard, Google Sans, Castoro and an Adobe Typekit kit are linked but not applied to visible text.
- **Icons:** Font Awesome 5, Academicons, Ionicons (`ion-icon`), the Hugging Face logo PNG.

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `p.title.is-2.publication-title` | 40px / 900 (bold) / 45px, Century Gothic |
| Authors | `p.title.is-4.publication-authors`, `a.author-block` | 24px / 600 line, names 200 (regular) / 27px |
| Affiliation | `p.subtitle.is-5.publication-authors` | 20px / 400 / 25px, Century Gothic |
| Venue | `p.subtitle.is-4` | 24px / 400 / 30px, Satoshi |
| Section heads | `p.subtitle.is-3.mt-5.has-text-left` | 32px / 400 / 40px, Satoshi, left |
| Sub-heads | `p.subtitle.is-4.mt-5.has-text-left` | 24px / 400 / 30px, Satoshi, left |
| Body | `p.content.is-size-6.has-text-justified` | 16px / 400 / 24px, Satoshi, justified |
| Captions | `.caption` | 16px / 400 / 24px, Satoshi, centred, padding-top 10px |
| Buttons | `.button.is-normal` | 16px / 400 / 24px, Noto Sans |
| BibTeX, references | `.block.is-size-6` | 16px / 400 / 24px, Noto Sans (BibTeX `pre` 14px monospace) |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Buttons | Bulma `is-rounded` pill, 1px solid #ab4012, padding 7px 20px, margin 0 4px 5px, no shadow |
| Author highlight | bottom-half gradient stripe, no radius |
| Separator | `.sep` 1px #c0c0c0 bottom border, margin 2rem −0.1618rem |
| Demo video | square iframe, 800px max |
| Carousel slides | borderless; the template's `.carousel .item` border rule does not match the page's `.item-1`…`.item-4` slides, which carry 30px side padding |
| Figures | square, no border, full column width |
| `.block` | margin 0.618rem 0 (golden-ratio spacing) |

## Layout Metrics

- **Hero container:** `.container` max-width 1344px at 1440 with 10px padding (title line box 1324px); everything centred.
- **Main column:** `.container.is-max-desktop` 960px with 10px padding, so content is 940px (x=250–1190).
- **Sections:** `.section` padding 48px 0 (side padding forced to 0); colored bands use inline `padding-top: 5px; padding-bottom: 15px`; headings `mt-5` (24px) above and Bulma 24px below.
- **Teaser figure:** `figure_one.png` 940×620, the first thing in the main column.
- **Demo videos:** 800px max (YouTube 800×450); Real-Time demo carousel slides 920px.
- **Separators:** 945px wide, 32px above and below.
- **References:** `.block` with 2em left margin and −1.3em text-indent (hanging indent).
- **Footer:** padding 48px 24px 96px on #fafbfb, single `column is-8` line.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1024px | 960px column, 10px padding | 16px | 40px | two button rows of three |
| 769–1023px | fluid container, 10px padding | 16px | 40px | buttons wrap as space allows |
| ≤768px | 10px | 16px | 40px | navbar collapses to Bulma burger; the 450px-high iframe keeps its height while width shrinks, so it letterboxes; logo capped at 80vw |

## Components

- **Two-tone title:** one `<font color="#732a14">` span for the project name and colon, the rest #363636; Century Gothic bold 40px, centred.
- **Highlighter author:** inline-block link, #000000, `background: linear-gradient(to top, #fbebca 50%, transparent 50%)`; hover `background: #fbebca`.
- **Rust outline pill:** Bulma `.button.is-rounded` forced to #ffffff fill, #ab4012 1px border and text, icon left; hover fills #ab4012 with #ffffff text and a transparent border.
- **Pale band section:** full-width `section` with inline `background-color: #fafbfb`, 5px top and 15px bottom padding, content in the 940px column.
- **Separator rule:** `.sep`, 1px #c0c0c0, 2rem vertical margin.
- **Caption:** Satoshi 16px centred under each figure, 10px top padding.
- **Reference list:** Noto Sans 16px with bracketed numbers and a hanging indent; titles as #3273dc links.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Site navbar | Yes | home icon and "More Research" dropdown |
| Title / authors / affiliation | Yes | Century Gothic, two-tone title, highlighted names |
| Lab logo | Yes | single image under the affiliation |
| Venue | Yes | light 24px Satoshi line |
| Link buttons | Yes | six rust outline pills in two rows (incl. three demos) |
| Demo video | Yes | YouTube embed on a #fafbfb band |
| Teaser figure | Yes | film-strip figure with a time arrow at the top of the main column |
| Abstract | Yes | left head, justified body |
| Method figures | Yes | two pastel diagrams with captions |
| Demo carousels | Yes | screen-recording videos on #fafbfb bands |
| More examples | Yes | panorama carousel, tall comparison figure |
| BibTeX | Yes | #fafbfb block |
| References | Yes | numbered list (uncommon on project pages) |
| Results table | No (absent from the source) | |
| Footer | Yes | #fafbfb, Nerfies thanks |

## Adapting to Other Content

- **More authors:** the highlighter names wrap well because each is inline-block; past a line, keep the stripe and drop the font to 20px.
- **Results table:** put it in the 940px column under a 32px Satoshi left head; Satoshi 16px cells, header row on #fafbfb, 1px #c0c0c0 rules like `.sep`, the best value in #ab4012.
- **More links:** add pills to the second row; keep demos grouped separately from paper links.
- **Venue or award:** a second Satoshi 24px line; an award could take #ab4012 text without a fill.
- **News:** a short list above the teaser figure with dates in #732a14.
- **No video:** keep the #fafbfb strip and put the teaser figure there instead, so the hero still ends in a band.

## Do's and Don'ts

- Do reserve the brown pair for brand moments: #732a14 in the title, #ab4012 for every button.
- Do give each author name the half-height #fbebca stripe; it is the page's signature detail.
- Do left-align section heads while keeping the hero centred.
- Don't rely on Century Gothic being installed; self-host a geometric face (URW Gothic) for the title and authors.
- Don't add fills to the buttons at rest; they are outlines that fill on hover.
- Don't use heavy rules; separators are 1px #c0c0c0.

## Surfaces

White hero and main column, #fafbfb bands (demo strip, two demo sections, BibTeX block, footer), 1px #c0c0c0 separators. No cards and no shadows.

## Imagery

A film-strip teaser of image streams painted from coloured masks (sunset grassland with a horse, an anime girl in flowers, a coral reef), pastel method diagrams with pink, blue and peach blocks, dark-UI screen recordings of the Gradio demo, mountain panoramas, and a tall mask-to-image comparison.

## Layout

Centred hero up to 1344px, then a 940px main column with left-aligned heads and alternating white and #fafbfb full-width bands. Rendered height about 8,000px.

## Agent Prompt Guide

Quick colors: title #363636 with brand word #732a14, buttons #ab4012 on #ffffff, author highlight #fbebca on #000000 names, body #4a4a4a, bands #fafbfb, rules #c0c0c0, links #3273dc.

1. "Create a centred hero: a 40px bold Century Gothic (or URW Gothic) title in #363636 with the project name and colon in #732a14, then 24px author names in #000000 each with a background of linear-gradient(to top, #fbebca 50%, transparent 50%), hover full #fbebca; affiliation 20px #4a4a4a, then a 24px Satoshi venue line."
2. "Make link buttons: pill radius, #ffffff fill, 1px solid #ab4012 border, #ab4012 16px Noto Sans text, padding 7px 20px, icon left, 4px side margins, two centred flex-wrap rows; hover fill #ab4012, text #ffffff, transparent border."
3. "Lay out the body in a 940px column: left-aligned 32px Satoshi section heads in #4a4a4a, 16px justified Satoshi text, centred 16px captions with 10px top padding, 1px #c0c0c0 separators with 2rem margins, and full-width #fafbfb bands for demo videos."

## Similar Pages

- Nerfies-derived pages with a branded two-tone title and outlined pill buttons.
- Interactive-demo diffusion pages that lead with a screen-recorded demo.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --title: #363636;
  --brand: #732a14;
  --accent: #ab4012;
  --highlight: #fbebca;
  --text: #4a4a4a;
  --band: #fafbfb;
  --rule: #c0c0c0;
  --link: #3273dc;
  --font-display: 'Century Gothic', 'URW Gothic', sans-serif;
  --font-text: 'Satoshi', 'General Sans', sans-serif;
  --font-ui: 'Noto Sans', sans-serif;
  --title-size: 40px;
  --author-size: 24px;
  --h2-size: 32px;
  --body-size: 16px;
  --radius-pill: 9999px;
  --column: 940px;
}
```

## Provenance

- **URL:** https://jaerinlee.com/research/semantic-draw
- **Paper:** SemanticDraw: Towards Real-Time Interactive Content Creation from Image Diffusion Models (arXiv 2403.09055), Jaerin Lee, Daniel Sungho Jung, Kanggeon Lee, Kyoung Mu Lee, Seoul National University.
- **Venue:** CVPR 2025 (stated in the hero).
- **Selection reason:** arXiv 2403.09055 comment states acceptance at CVPR 2025 (camera ready); project page linked in the abstract.
- **Template credit:** footer thanks Nerfies for the template.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share, the 1440×900 screenshot, scrolled full-page captures, `/css/index_project_page.css`, `/css/satoshi.css`, inline styles in the page HTML; 2026-10-28.
