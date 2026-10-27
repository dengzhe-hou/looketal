# MirrorVerse Rose Band — Style Reference

> A dusty-rose title card with a photograph glowing on the facing page.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 screenshot, scrolled captures of the full 5,004px page, a 390px render, the page's `assets/stylesheets/main_free.css` (Shikun Liu's Clarity template) and the inline styles in the HTML. One finding drives the whole look: the template's Poppins @font-face points at a jsDelivr path that now returns 404, so every "Poppins" rule falls back. Headings render in Times New Roman, chips and tables in Arial, and only the body paragraphs get a real web font (Charter). The values below describe that rendered page.

## Overview

A two-part page. The first 860px is a full-width dusty-rose band (#ddcecd, set inline on `#first-content`) holding a two-column hero: at left a 30px regular serif title, a bold 26px "CVPR 2025", italic underlined author names with superscripts, an italic affiliation block, a TL;DR paragraph in 18px Charter with bold dataset names and two bullet features, then four small uppercase chips on a 25% white wash. At right sits a portrait photo of a cat-shaped mirror and toy figures, lifted by a blurred copy of itself placed behind (a soft coloured glow, not a box-shadow). Below the band the page switches to a white reading column 749px wide: bold 26px serif section heads (Introduction, Dataset, Qualitative Results), 18px Charter body in #353535 with underlined links, figure grids with tiny serif captions, one #f6f6f6 band for the dataset pipeline figure, a centred comparison table with grey zebra rows, and an italic Charter footer credit on #fafafa.

## First Viewport

Color share (1440×900, 8-color quantize): rose #ddcecd 61.1% plus near-identical rose tones #ddcecc 5.3% and #ddcece 4.5%, so the band is about 71%; mauve shadow #6d4c4f 12.0% (dark text and photo shadows), grey rose #c5bbbc 10.7% (photo and glow), chip wash #f0e9e8 5.2% (chips and the white strip at the bottom), sage #cfd4c7 1.0%.

Anatomy in DOM order (band padding 54px 216px 0; grid `1.2fr 1fr`, column gap 57.6px; left column 518px from x=216, right column 389px from x=835; the intro column has 45px vertical padding):

1. **Title** — `h1.title`, "MirrorVerse: Pushing Diffusion Models to Realistically Reflect the World", declared `Poppins, serif` 30px / 400 / line-height 36px, renders Times New Roman, #353535, left aligned, two lines (y=99–180). Gap 0 (padding-bottom 9px is inside the box).
2. **Venue** — second `h1`, "CVPR 2025", 26px / 600 / 31.2px, Times New Roman bold, #353535 (y=180–229, 9px padding top and bottom). Gap 0.
3. **Authors** — `p.author`, 15.3px (85%) italic / 400 / 18.36px, #353535; names are underlined links in the same color with superscript affiliation marks; padding 4px 0 10px (y=229–266).
4. **Affiliations** — second `p.author`, three italic lines with superscripts ("* Equal Contribution", "1 Vision and AI Lab, IISc Bangalore", "2 Samsung R & D Institute India - Bangalore"), y=266–331. Gap about 36px of empty `p.abstract` padding.
5. **TL;DR** — `p` in Charter 18px / 300 (renders Charter regular) / 27px, #353535, "TL;DR:" and dataset names in `b` (600, Charter bold); 13.5px vertical padding (y=367–529).
6. **Key features** — second Charter paragraph with "•" bullets and bold lead words (y=529–664).
7. **Link chips** — `.info a.button.icon`, "PAPER", "SOURCE CODE", "DATASET", "REFLECTING-REALITY", 11.7px / 500 Arial uppercase, letter-spacing 0.8775px, #353535 on rgba(255,255,255,0.25), radius 10px, padding 8.775px 11.7px, Font Awesome 6 solid icon on the right; separated by `&nbsp;&nbsp;`; the fourth chip wraps to a second row (y=732–802).
8. **Cover photo** — `.blog-cover img.foreground` 389×495px at x=835, y=210, square corners, with `img.background` (same image, `filter: blur(24px)`, absolute, z-index 1) behind it, which reads as a coloured halo.
9. **Band end** — the rose band stops at y=860; the white column's first heading starts at y=878.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Dusty Rose | #ddcecd | inline `background-color` on `#first-content` | hero band |
| Graphite | #353535 | `h1…li` color (template) | title, venue, authors, body text, headings, chip labels, captions, table cells |
| Chip Wash | rgba(255,255,255,0.25) | inline style on each `.button` | link chips on the rose band |
| Paper | #ffffff | `body` | reading column background |
| Band Grey | #f6f6f6 | `.container.blog.gray` | dataset pipeline figure band |
| Zebra | #ececec | template table rows | odd table rows |
| Header Grey | #666667 | template `th` | table header text |
| Code Grey | #c6c6c6 | template `code` border | 1px border of inline code chips ("MirrorFusion") |
| Code Wash | rgba(230,235,237,0.25) | template `code` background | inline code chips |
| Footer Haze | #fafafa | `footer` | footer band |
| Rose Shadow | #6d4c4f | (screenshot) | darkest mauve in the first viewport, from text and photo shadows |

Declared but not visible: Poppins (404, see Typography); `.highlight-row` adds a 2px #d78f8f border and #f9f9f9 fill to the "SynMirrorV2 (Ours)" row, but with the template's separated borders and zebra fill the row renders like the others (#ececec, no visible red edge); the slide-menu active dot #e2a3a3 is unused because the page has no carousel.

## Tokens — Typography

- **Serif display (rendered):** declared `"Poppins", serif`; the Poppins files 404, so it renders Times New Roman (system). Applies to the title, venue, section h1s and captions. Substitute: Tinos or Liberation Serif for the same metrics; if you want the intended look, load real Poppins.
- **Body serif:** declared `"Charter", sans-serif` on `p.text` and `footer p`; rendered Charter regular, italic and bold (self-hosted woff2). Weight 300 renders as Charter regular. Substitute: Charis SIL or Bitstream Charter.
- **Sans (rendered):** declared `"Poppins", sans-serif` on `.button` and `table`; renders Arial. Substitute: Arimo.
- **Mono:** Fira Code 400 for inline `code`.
- **Icons:** Font Awesome 6.6 Free (solid).

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `#first-content h1.title` | 30px / 400 / 36px, Times New Roman |
| Venue line | `#first-content h1` | 26px / 600 / 31.2px, Times New Roman bold |
| Authors, affiliations | `.blog-intro p.author` | 15.3px italic / 400 / 18.36px |
| TL;DR, body | `p.text`, intro `p` | 18px / 300 (renders 400) / 27px, Charter |
| Section heads | `.container.blog.main h1` | 26px / 600 / 31.2px, Times New Roman bold |
| Figure captions | `p.caption` | 12.6px (70%) / 400 / 15.12px, bold "Prompt:" or "Comparison with" lead |
| Link chips | `.button.icon` | 11.7px (0.65em) / 500, uppercase, letter-spacing 0.8775px, Arial |
| Table header / cells | `table th`, `table td` | 15.3px / 500 #666667 and 15.3px / 400 #353535, centred, Arial |
| Inline code | `code` | 9.45px / 300 Fira Code |
| Footer | `footer p` | 18px italic / 300 / 27px, Charter |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Link chips | radius 10px, padding 0.75em 1em (8.775px 11.7px), no border, no shadow |
| Inline code chip | radius 10px, 1px solid #c6c6c6, padding 2.36px 6.14px |
| Cover photo | square corners; halo from a 24px-blurred duplicate behind it |
| Figures | square corners, `padding-bottom: 1vh` |
| Table | full column width, zebra fill, no visible rules |
| Shadows | none as `box-shadow`; the only depth is the blurred image halo |

## Layout Metrics

- **Hero band:** full width, padding-top 6vh (54px), side padding 15vw (216px); inner grid `1.2fr 1fr` with 4vw column gap (57.6px) at 1440; intro and cover columns have 5vh (45px) vertical padding; cover column is 90% wide, right aligned.
- **Reading column:** `.container.blog.main` padding 2vh 24vw at 1440 (text column 749px from x=346).
- **Grey figure band:** `.container.blog.main.gray.large`, padding 2vh 16vw (979px figure width at 1440), #f6f6f6.
- **Section rhythm:** each block is a separate full-width container; h1 has 9px (1vh) vertical padding; paragraphs 13.5px (1.5vh) vertical padding; caption blocks 9px.
- **Figures:** two-up figure pairs at 360px each with a 28px gap; qualitative grids fill the 749px column.
- **Footer:** 4vh (36px) vertical padding, text from x=216.

| Breakpoint | Gutter (hero / column) | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1200px | 15vw / 24vw | 18px | 30px | hero `1.2fr 1fr`, 4vw gap |
| 992–1199px | 12vw / 20vw | 17px | 26px | hero two columns, 3vw gap |
| 769–991px | 8.5vw / 15vw | 16px | 26px | hero two columns, 5vw gap |
| ≤768px | 6vw (23.4px at 390) for both | 15px | 26px | hero stacks to one column (photo below the chips); chips shrink to 9px text |

## Components

- **Rose title band:** full-bleed block with a single inline background color; left column text stack, right column photo; ends flush against the white page with no divider.
- **Glow photo:** two copies of the same `img` in `.blog-cover`; the back one absolute with `filter: blur(24px)`, the front one relative at z-index 2. The halo takes the photo's own colours.
- **Wash link chip:** `a.button.icon`, inline-flex, rgba(255,255,255,0.25) on the rose band, #353535 uppercase 11.7px / 500 Arial, letter-spacing 0.075em, radius 10px, padding 0.75em 1em, icon after the label at 1.2em with 0.5em left padding; hover opacity 0.8, active 0.5. Off the band the template default fill is #ececec.
- **Caption:** `p.caption`, 12.6px serif, line-height 1.2, bold lead word, sits directly under each figure.
- **Zebra table:** Arial 15.3px centred cells, odd rows #ececec, header #666667 / 500 with no fill, dataset names underlined links.
- **Inline code chip:** Fira Code 9.45px #666667 on rgba(230,235,237,0.25), 1px #c6c6c6 border, radius 10px.
- **Footer:** #fafafa band, italic Charter line crediting the Clarity Template.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / venue / authors | Yes | left column of the rose band, serif title, bold venue h1 |
| TL;DR | Yes | Charter paragraph plus two bullet features in the hero |
| Link chips | Yes | four uppercase wash chips |
| Teaser image | Yes | portrait photo with blurred halo |
| Introduction | Yes | white column, two-up failure figures with captions |
| Method / dataset figure | Yes | pipeline figure on the #f6f6f6 band |
| Dataset comparison table | Yes | zebra table, the "Ours" row last |
| Qualitative results | Yes | image grids with italic column labels and green/red circled regions |
| Abstract | No (absent from the source) | the TL;DR stands in |
| BibTeX | No (absent from the source) | |
| Video | No (absent from the source) | |
| Footer | Yes | #fafafa, Clarity credit |

## Adapting to Other Content

- **More authors:** the italic author line wraps inside the 518px column; past about eight names move affiliations to a single line of superscript keys to keep the TL;DR above the fold.
- **Results table:** reuse the zebra table; to mark the best row, use bold text rather than the declared red border, which does not show with separated borders.
- **Abstract:** add it as the first white-column section with a 26px bold serif head and 18px Charter text; keep the TL;DR in the band.
- **BibTeX:** a `pre` in Fira Code on #fafafa with the same 10px radius as the chips.
- **Long publication or news lists:** plain Charter list items in the 749px column; no cards, no bands.
- **Video teaser:** place a looping video in the cover slot and keep the blurred-duplicate halo by layering a second blurred `video` behind it.

## Do's and Don'ts

- Do set the band color inline once and let everything on it be #353535.
- Do keep the hero to a two-column text-plus-photo grid; the photo always sits right.
- Do pair a serif display face with a bookish body serif; this page reads as editorial because both are serif.
- Don't rely on the template's remote Poppins; host fonts yourself or declare the serif you want, since the fallback is what visitors see.
- Don't use box-shadows for the photo; the blurred duplicate is the effect.
- Don't add colored links; links stay #353535 and underlined.

## Surfaces

Dusty-rose hero band, white reading column, one #f6f6f6 band for the pipeline figure, #ececec zebra rows, #fafafa footer. Chips are 25% white washes, so they take on the band color.

## Imagery

Real photographs of mirrors and toys, synthetic Blender renders of furniture in front of mirrors, image grids comparing methods with red and green circles, and a pastel pipeline diagram. Images are square-cornered and fill their column.

## Layout

A full-width two-column title band, then a narrow single reading column (24vw gutters at 1440) with one wider grey band. Rendered height about 5,000px.

## Agent Prompt Guide

Quick colors: band #ddcecd, text and links #353535, chip rgba(255,255,255,0.25), page #ffffff, figure band #f6f6f6, table zebra #ececec with header text #666667, footer #fafafa.

1. "Create a hero band: full width, background #ddcecd, padding 54px 15vw 0; a grid with columns 1.2fr 1fr and a 4vw gap. Left: a 30px regular serif title in #353535, a 26px bold serif venue line, 15.3px italic underlined author names, a TL;DR paragraph in Charter 18px / 27px, then uppercase chips. Right: a portrait photo with a 24px-blurred copy of itself absolutely positioned behind it."
2. "Make link chips: inline-flex, background rgba(255,255,255,0.25), #353535 11.7px weight 500 uppercase sans with 0.075em letter-spacing, radius 10px, padding 0.75em 1em, icon after the label; hover opacity 0.8."
3. "Below the band, set a white reading column with 24vw side padding: 26px bold serif section heads, Charter 18px / 27px #353535 body, underlined #353535 links, 12.6px captions under figures, and a centred sans table with #ececec odd rows and #666667 headers."

## Similar Pages

- Clarity-template pages by Shikun Liu that set a colored `#first-content` band.
- Editorial blog-style project pages that put a single hero photo opposite the title.

## Quick Start

```css
:root {
  --band: #ddcecd;
  --text: #353535;
  --chip-bg: rgba(255, 255, 255, 0.25);
  --bg: #ffffff;
  --figure-band: #f6f6f6;
  --zebra: #ececec;
  --th: #666667;
  --footer: #fafafa;
  --font-display: 'Times New Roman', Tinos, serif;
  --font-body: 'Charter', 'Charis SIL', serif;
  --font-ui: Arial, Arimo, sans-serif;
  --font-mono: 'Fira Code', monospace;
  --title-size: 30px;
  --h1-size: 26px;
  --body-size: 18px;
  --chip-size: 11.7px;
  --radius-chip: 10px;
  --halo-blur: 24px;
}
```

## Provenance

- **URL:** https://mirror-verse.github.io/
- **Paper:** MirrorVerse: Pushing Diffusion Models to Realistically Reflect the World (arXiv 2504.15397), Ankit Dhiman, Manan Shah, R Venkatesh Babu.
- **Venue:** CVPR 2025 (stated in the hero).
- **Selection reason:** arXiv 2504.15397 comment states acceptance at CVPR 2025; project page linked in the comment.
- **Template credit:** footer credits the Clarity Template designed by Shikun Liu.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share, the 1440×900 screenshot, scrolled full-page captures, a 390px render, `assets/stylesheets/main_free.css`, inline styles in the page HTML, an HTTP check showing the Poppins woff2 returns 404; 2026-10-28.
