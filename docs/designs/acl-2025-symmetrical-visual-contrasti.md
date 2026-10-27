# Blue-Orange Contrast Bands — Style Reference

> A two-color argument: cyan means the matching image, orange the mismatched one, and that code runs unbroken from the prose highlights into every figure across alternating grey and white bands.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (`tools/computed_style.py`: computed styles of the title, authors, venue heading, buttons, band sections, paragraphs, highlight spans, sub-headings, `pre` and footer, first-viewport anatomy, loaded fonts and color share), the first-viewport screenshot and the full-page capture, and the page's own `static/css/index.css` (stock template plus `.mycolumn` and `.myrow`), an inline `<style>` for logo sizes, and inline `color` styles in the HTML, over Bulma 0.9 from the Nerfies-style template. Positions are document coordinates at 1440px wide.

## Overview

S-VCO is a Nerfies-template page with no section titles in its body: after a white hero, it runs as full-bleed bands alternating Bulma `hero is-light` grey (#f5f5f5) and `hero is-white`, each holding one justified paragraph block and one figure. The hero centers a three-line Google Sans 40px title, four bold #209cee author names separated by em spaces, a Stanford logo (30px seal plus 200px wordmark image), an "ACL 2025 Main" line in Stanford cardinal (#be1e2d) at 24px bold, and three dark pill buttons (Arxiv, Code & Data, Twitter). The visual system is semantic: inline spans color "the matching image" cyan (#05b0f0), "the mismatched image" and "the contradictory image" orange (#f49443), and "no image" grey (#7f7f7f), and the figures use the same cyan and orange frames and labels, so the prose and the perplexity, method and qualitative figures read as one diagram. Text on grey bands renders at rgba(0,0,0,.7) and on white bands at #0a0a0a. The qualitative grid near the bottom is dense and is set wider than the column. A Citation `pre` and a #fafafa footer close the page.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): white #ffffff 47.0%, light band #f5f5f5 32.9%, mid grey #b4b8bc 11.4% (text, buttons and photo pixels), pale figure mint #f6fbfa 3.3%, pale figure blue #f0f7f8 3.0%, remainder under 1.5%. Cyan and orange appear as text spans and figure frames, cardinal red in the logo and venue line.

Anatomy in DOM order (y = top of element box):

1. **Title** (`h1.title.is-2.publication-title`), y 48, 960px, three lines (a forced `<br>` after the colon), Google Sans 40px/45px weight 600, #363636, centered. Gap 26px.
2. **Authors** (`.publication-authors a b`), y 209, Google Sans 20px/30px bold, #209cee, separated by em spaces, no superscripts. Gap 22px.
3. **Affiliation logo** (`img.small-image-30` and `img.small-image`), y 261, a 30×45 Stanford seal and a 200×36 "Stanford University" wordmark side by side, centered. Gap 32px.
4. **Venue** (`h1.title.is-4 > font[color=#BE1E2D] > b`), y 339, "ACL 2025 Main", Google Sans 24px/27px, bold, #be1e2d, centered. Gap 24px.
5. **Link buttons** (`a.external-link.button.is-normal.is-rounded.is-dark`), y 390, Arxiv 99px, Code & Data 155px, Twitter 113px, 40px tall, #363636, white Noto Sans 16px/400, padding 7px 20px, Academicons and Font Awesome icons left. The hero ends at y 483.
6. **Light band** (`section.section.hero.is-light`), y 483, #f5f5f5, padding 48px 24px; no heading. Paragraph at y 531, 960px, 16px/24px justified, rgba(0,0,0,.7), with bold phrases and colored spans (#05b0f0, #f49443). Gap about 25px (a `<br>`).
7. **Perplexity figure** (`img`, width 70%), y 654, 672×262, centered; cyan-framed "image_match", orange-framed "image_mismatch" and a grey "no image" placeholder. The fold cuts it at its formula line.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Heading Ink | #363636 | Bulma `.title` | Paper title, "Citation" heading |
| White-band Text | #0a0a0a | Bulma `.hero.is-white` | Paragraphs and h3 sub-headings on white bands |
| Grey-band Text | rgba(0,0,0,.7) | Bulma `.hero.is-light` | Paragraphs on grey bands |
| Body Grey | #4a4a4a | Bulma body | Citation section and `pre` text |
| Author Blue | #209cee | `.publication-authors a`, inline `hsl(204,86%,53%)` | Author names; reference superscripts (DPO, mDPO, MFPO, benchmark names) |
| Venue Cardinal | #be1e2d | `<font color>` | "ACL 2025 Main"; matches the Stanford logo |
| Match Cyan | #05b0f0 | inline `color` | "the matching image", "the response about the dog"; cyan figure frames |
| Mismatch Orange | #f49443 | inline `color` | "the mismatched image", "the contradictory image"; orange figure frames |
| No-image Grey | #7f7f7f | inline `color` | "no image input" phrases |
| Base Grey | #767171 | inline `color` | "base-VLMs" label in the qualitative text |
| Light Band | #f5f5f5 | `.hero.is-light`, `.content pre` | Grey bands, citation block |
| Footer Wash | #fafafa | `.footer` | Footer band |
| Button Dark | #363636 | `.button.is-dark` | Arxiv, Code & Data, Twitter |
| White | #ffffff | `.hero.is-white`, page | Hero and white bands |

Declared but not visible as text color: inline #ff9300, #f8a09c ("the negative image"), #7030a0 and #0070c0 appear once each on single phrases in the Symmetry and results paragraphs; they echo figure legend colors and are not part of the main pair.

## Tokens — Typography

- **Title, authors, venue**: declared `'Google Sans', sans-serif`. Rendered: Google Sans 400 only (`fonts_loaded`); bold and 600 are synthesized. Substitute: Figtree.
- **Body**: declared `'Noto Sans', sans-serif`. Rendered: Noto Sans 400 only; bold phrases synthesized.
- **Code**: generic `monospace`.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Paper title | `h1.title.is-2.publication-title` | 40px / 45px | 600 | #363636 |
| Venue | `h1.title.is-4 b` | 24px / 27px | 700 | #be1e2d |
| Authors | `.publication-authors a b` | 20px / 30px | 700 | #209cee |
| Sub-heading | `h3.title.is-5.has-text-left` | 20px / 22.5px | 600 | #0a0a0a |
| Citation heading | `h2.title.is-3` | 32px / 36px | 600 | #363636 |
| Body | `.column.has-text-justified p` | 16px / 24px | 400, key phrases 700 | rgba(0,0,0,.7) or #0a0a0a by band |
| Reference superscript | `sup a` | 13.3px / 20px | 400 | #209cee |
| Code | `pre code` | 14px / 21px | 400 | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link button | 290486px | 1px transparent | none |
| Figures | 0 | none (frames are drawn inside the images) | none |
| Bands | 0 | none | none |
| `pre` | 0 | none | none |

## Layout Metrics

- **Container**: `.container.is-max-desktop`, 960px (x 240–1200); paragraphs span the full 960px.
- **Hero**: `.hero-body` padding 48px 24px; title margin-bottom 24px; logo, venue and buttons stack centered.
- **Bands**: `section.section.hero` padding 48px 24px, full-bleed, alternating light (#f5f5f5) and white: intro (light, y 483–963), method (white, 964–1905), qualitative (light, 1905–3494), data (white, 3494–4250), results (light, 4250–5093), citation (plain white).
- **Figures**: inline widths per figure: the perplexity figure 70% (672px), the method and results figures 100%, the qualitative grid `width: 130%; max-width: none`, which pushes its right side past the 960px column.
- **Lists**: bullets are typed as `&emsp;•` with `<br><br>` between items, not `ul` elements.
- **Footer**: #fafafa, padding 48px 24px 96px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px | 960px container | 16px | 40px | as described |
| 769–1023px | fluid, 24px band padding | 16px | 40px | the 130% qualitative grid overflows more |
| ≤768px | fluid, 24px | 16px | 40px | columns full width; logo and buttons wrap |

## Components

- **Semantic highlight span**: inline `<span style="color: …">` in body text, usually with `<b>`: #05b0f0 for the matching image, #f49443 for the mismatched or contradictory image, #7f7f7f for no image. The same colors frame images and label subscripts inside the figures.
- **Logo affiliation**: two small images side by side (`max-width: 30px` seal, `max-width: 200px` wordmark) in place of a text affiliation line.
- **Colored venue line**: an `h1.title.is-4` holding a bold #be1e2d "ACL 2025 Main", tying the venue to the institution's color.
- **Headless band**: a full-bleed Bulma hero band (padding 48px 24px) with a justified paragraph, a `<br>` and a centered figure, without a section title; sub-topics inside a band get a left-aligned `h3.title.is-5`.
- **Reference superscripts**: method and benchmark names as superscript links in #209cee directly after a term ("finetuning<sup>DPO, mDPO, MFPO</sup>").
- **Dark pill button**: Bulma `.button.is-dark.is-rounded`, #363636, white 16px, padding 7px 20px, icon left.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title, authors | yes | Google Sans, bold blue authors |
| Affiliation | present but non-standard | logo images instead of text |
| Venue | yes | cardinal bold line |
| Link buttons | yes | three dark pills |
| Teaser | yes | perplexity figure in the first grey band |
| Abstract | present but non-standard | the intro paragraph replaces a titled abstract |
| Method | yes | white band, full-width figure, two `h3` sub-topics |
| Qualitative grid | yes | dense image-and-text grid wider than the column |
| Dataset | yes | white band with a figure and typed bullets |
| Results table | present but non-standard | table as an image plus typed bullets |
| Section titles | absent from the source | only "Citation" has one |
| BibTeX | yes | #f5f5f5 `pre` under "Citation" |
| Footer | yes | #fafafa credit |

## Adapting to Other Content

- **More authors**: keep bold #209cee names separated by em spaces; add superscripts only if affiliations differ, and keep logos as the affiliation row.
- **A results table**: an HTML Bulma table in the 960px column on a grey band; color the column or row headers of the two compared conditions with #05b0f0 and #f49443 text so the table keeps the semantic pair; best values in bold.
- **More sections**: continue alternating light and white bands; add a left-aligned `h3.title.is-5` when a band holds more than one idea.
- **News**: a short line of bold text in the first grey band above the intro paragraph; no extra color.
- **Long publication lists**: a white band with a real `ul`, 16px, titles bold, venues #7f7f7f.
- **A third condition**: reserve #7f7f7f for "absent" and pick one more hue only if a figure already uses it.

## Do's and Don'ts

- Do assign each experimental condition one color and use it in prose, frames, labels and legends alike.
- Do let full-bleed band alternation separate topics when there are no section titles.
- Do keep body text justified in the 960px column.
- Do echo the institution's color in the venue line if a logo is shown.
- Don't set wide figures beyond the column with `max-width: none`; crop or scale the grid instead.
- Don't add further one-off text colors; the extra purple, blue and pink spans dilute the pair.
- Don't type bullets as `&emsp;•` with line breaks in new pages; use a list with the same spacing.

## Surfaces

White hero, then alternating #f5f5f5 and white full-bleed bands, a #f5f5f5 citation block and a #fafafa footer. Figures bring their own very pale mint and blue panels (#f6fbfa, #f0f7f8). No cards or shadows.

## Imagery

Clean vector-style figures with cyan and orange image frames, speech-bubble queries, small icon rows (image, chat) and arrows, built around photographs (a dog and a cat in snow, a kitchen, a clock tower, food), plus a qualitative grid of benchmark photos with color-coded model answers (orange DPO, blue mDPO, purple S-VCO).

## Layout

A centered 960px Nerfies column inside alternating full-bleed bands, each band a paragraph followed by a figure. Rendered height is about 5,680px at 1440px.

## Agent Prompt Guide

Quick colors: title #363636, authors #209cee, venue #be1e2d, match #05b0f0, mismatch #f49443, absent #7f7f7f, grey band #f5f5f5 with rgba(0,0,0,.7) text, white band text #0a0a0a, buttons #363636.

1. "Build a hero in a 960px column: centered Google Sans 40px/45px weight 600 #363636 title on three lines; bold 20px #209cee author names separated by em spaces; a row with a 30px seal and a 200px wordmark logo; 'ACL 2025 Main' in 24px bold #be1e2d; three #363636 pill buttons with white 16px text, padding 7px 20px, icon left."
2. "Create a headless grey band: full-bleed #f5f5f5, padding 48px 24px, a 960px justified 16px/24px paragraph in rgba(0,0,0,.7) where 'the matching image' is bold #05b0f0 and 'the mismatched image' is bold #f49443, then a centered figure at 70% width whose frames use the same two colors."
3. "Follow with a white band (#ffffff, padding 48px 24px): a full-width method figure, then a left-aligned 20px/600 #0a0a0a sub-heading and a justified 16px #0a0a0a paragraph; references appear as #209cee superscript links after the terms."

## Similar Pages

- Nerfies-template pages that drop section titles and rely on Bulma hero band alternation.
- VLM alignment and hallucination papers whose figures color-code matched versus mismatched images.

## Quick Start

```css
:root {
  --heading: #363636;
  --text-white-band: #0a0a0a;
  --text-grey-band: rgba(0, 0, 0, .7);
  --author: #209cee;
  --venue: #be1e2d;
  --match: #05b0f0;
  --mismatch: #f49443;
  --absent: #7f7f7f;
  --band: #f5f5f5;
  --footer: #fafafa;
  --button: #363636;
  --font-title: 'Google Sans', Figtree, sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --container: 960px;
  --band-pad: 48px 24px;
}
```

## Provenance

- **URL**: https://s-vco.github.io/
- **Paper**: Symmetrical Visual Contrastive Optimization: Aligning Vision-Language Models with Minimal Contrastive Images (arXiv 2502.13928), Shengguang Wu, Fan-Yun Sun, Kaiyue Wen, Nick Haber (Stanford University).
- **Venue**: ACL 2025 (Main).
- **Selection reason**: the arXiv 2502.13928 comment states acceptance at ACL 2025 Main and links the page. Chosen because the banded sections are matched to a two-color (blue/orange) semantic palette that runs from text highlights into the figures; the qualitative grid gets dense at the bottom.
- **Template credit**: footer says the page was built using a template inspired by Nerfies.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and fonts, the first-viewport screenshot and full-page capture, `static/css/index.css`, the inline styles and the HTML. Date 2026-10-28.
