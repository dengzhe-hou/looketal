# GOATex Gallery Wall — Style Reference

> A museum catalogue of carved cabinets: a quiet white title page, then a grey gallery wall lined with lit black display cases.

**Theme:** light

Measured from the rendered page at 1440×900 in headless Chrome (`computed_style.py`, screenshot and tall capture), then checked against the Nerfies `static/css/index.css`, Bulma 0.9 and the page's inline styles. Where stylesheet and render disagree, the render is reported. Pixel values are at the 1440px viewport unless a breakpoint is named.

## Overview

A nearly unmodified Nerfies/Bulma page whose look comes from layout and media rather than styling. The hero is white and restrained: a 40px Google Sans title, an "NeurIPS 2025" line at x-large size, four Bulma-blue author links, affiliations and an equal-contribution note. There are no link buttons at all. A wide teaser image follows: textured cabin, bus and theatre meshes with dashed red interior callouts above a strip of coffin-shaped cabinets in different interior styles. Below the abstract, a full-width `#f5f5f5` band holds the results gallery: a 3×3 grid (repeated across the band) of looping videos with black backgrounds, each under a tiny 9.6px prompt caption set in a fixed 6em box so the tiles align. Further white sections show prompt-conditioning comparisons in quarter columns split by a dashed grey rule, then a grey "Main Pipeline" band, qualitative comparisons, a BibTeX `pre` and a Bulma footer. Document height is about 12,569px, the longest page in this batch.

## First Viewport

Color share of the first 1440×900 viewport: `#ffffff` 58.9% (page and hero), `#f4f5f2` 11.2% (warm off-white teaser background), `#603120` 11.0% (rust-brown textured meshes), `#e8e8ee` 9.3% (lavender-grey lower teaser strip), `#b6a9a1` 6.7% (grey untextured meshes and wood tones), `#f4efe7` 1.6%, `#fdffff` 0.8%, `#fffffd` 0.5%.

Anatomy in DOM order (centred in a 960px column):

1. Hero `section.hero`, white, `.hero-body` padding 48px 24px.
2. Title `h1.title.is-2.publication-title`, Google Sans 40px/600, `#363636`, line-height 45px, one line (y=48). Gap 24px.
3. Venue `div` (inline `font-size: x-large`), "NeurIPS 2025", Noto Sans 24px/400, `#4a4a4a`, then a `<br>` (gap about 40px).
4. Authors `.publication-authors.is-size-5`, Google Sans 20px/400, links `#209cee`, superscripts and commas `#4a4a4a` (y=184).
5. Affiliations `.publication-affiliations.is-size-6`, 16px/400 `#4a4a4a`, superscript numbers.
6. Note `div` (inline `font-size: large`), "(* denotes equal contribution.)", 18px `#4a4a4a`, then a `<br>`. Hero ends at y=337.
7. Teaser `section.hero.teaser`: an empty `h1.title` (24px margin), then `teaser.png` at 912×532px (x=264, y=361), no radius or shadow. It runs to y≈893, and the abstract heading follows below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Title Charcoal | `#363636` | Bulma `.title` | Paper title, white-section headings (`is-3`, `is-4`, `is-5`) |
| Body Grey | `#4a4a4a` | Bulma body | Venue line, affiliations, abstract, captions, BibTeX text |
| Author Blue | `#209cee` | `.publication-authors a` (`hsl(204,86%,53%)`) | Author names |
| Band Title | `rgba(0,0,0,0.7)` | Bulma `.hero.is-light .title` | "Geometry & Occlusion Aware 3D Mesh Texturing Results", "Main Pipeline" |
| Gallery Grey | `#f5f5f5` | Bulma `.hero.is-light` | Results gallery band, Main Pipeline band |
| Video Black | `#000000` | `video` letterbox | Tile backgrounds around each render; footer icons |
| Dashed Rule | `#cccccc` | inline `border-right: 2px dashed` | Divider between the outer-prompt column and the interior variants |
| Code Grey | `#f5f5f5` | Bulma `pre` | BibTeX block |
| Footer Haze | `#fafafa` | Bulma `.footer` | Footer band |
| Tab Grey | `#eeeeee` | inline `.tabs li.is-active a` | Declared active-tab fill; the tabbed section is commented out |
| Page | `#ffffff` | `body` | Hero, abstract and comparison sections |

## Tokens — Typography

- **Declared:** Nerfies stack: `body` in `'Noto Sans', sans-serif`; `.publication-title`, `.publication-authors` and `.teaser` sections in `'Google Sans', sans-serif`; Google Fonts link also requests Castoro (unused).
- **Rendered:** Google Sans 400 and Noto Sans 400 loaded; 600 weights are synthesized. Because whole `.teaser` sections are Google Sans, the prompt-conditioning headings render in Google Sans while the abstract heading renders in Noto Sans. Substitute for Google Sans: Outfit.

| Role | Selector | Size | Weight | Line height | Colour |
|---|---|---|---|---|---|
| Paper title | `h1.title.is-2.publication-title` | 40px | 600 | 45px | `#363636` |
| Venue | inline `x-large` | 24px | 400 | 1.5 | `#4a4a4a` |
| Band heading | `h1.title.has-text-centered` | 32px | 600 | 36px | `rgba(0,0,0,0.7)` |
| Section heading | `h2.title.is-3` | 32px | 600 | 36px | `#363636` |
| Sub-heading | `h2.title.is-4` | 24px | 600 | 27px | `#363636` |
| Column label | `p.title.is-5` | 20px | 600 | 25px | `#363636` ("Outer Prompt:") |
| Authors | `.publication-authors` | 20px | 400 | 30px | links `#209cee` |
| Body | `.content.has-text-justified` | 16px | 400 | 24px | `#4a4a4a`, justified |
| Gallery caption | `.video-caption` (inline 0.6rem) | 9.6px | 400 | 1.5 | `#4a4a4a`, centred in a 6em box |
| Comparison caption | `.video-caption` (inline 0.7rem) | 11.2px | 400 | 1.5 | `#4a4a4a`, 5em box |
| BibTeX | `pre` | 14px | 400 | 21px | `#4a4a4a` |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Everything rendered (images, videos, bands) | 0 |
| BibTeX `pre` | Bulma default 4px |
| Active tab (declared, unused) | 4px |

- **Shadows:** none.
- **Borders:** only the 2px dashed `#cccccc` column divider in the prompt-conditioning rows.
- **Motion:** none; videos autoplay, loop and show native controls.

## Layout Metrics

- **Container:** `.container.is-max-desktop`, 960px at ≥1024px; content inside `.hero-body` is 912px (24px side padding). The abstract sits in `column is-four-fifths` (about 763px).
- **Hero:** `.hero-body` padding 48px 24px; `<br>`s after the venue and note lines add the vertical air.
- **Gallery band:** `section.hero.is-light.is-small` (`.hero-body` padding 24px), `columns is-multiline` of `column is-one-third` tiles; each tile is a flex column: 6em (57.6px) caption box, then a `width="100%"` video. Tiles are about 296px wide with 24px gutters.
- **Comparison rows:** `columns is-vcentered`: a `column is-one-quarter` "Outer Prompt" column with a dashed right border, then three interior-variant columns; spacer `div`s with 48px and 32px margins separate rows.
- **Figures:** teaser, pipeline and qualitative images at 100% of the 912px body.

| Breakpoint | Container | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|---|
| ≥1024px | 960px | 24px | 16px | 40px | gallery three per row; comparison rows four columns |
| 769–1023px | fluid | 24px | 16px | 40px | same |
| ≤768px | fluid | 24px | 16px | 40px | Bulma columns stack: gallery and comparison tiles become one per row |

## Components

- **Plain title block.** Centred 40px/600 Google Sans title, an x-large venue line, 20px author links in `#209cee`, 16px affiliations and an 18px equal-contribution note, separated by `<br>`s. No buttons.
- **Full-width teaser figure.** A single PNG at column width, no frame; the figure's own warm-white and lavender panels act as the frame.
- **Grey gallery band.** `section.hero.is-light.is-small` on `#f5f5f5` with a centred 32px/600 heading in `rgba(0,0,0,0.7)` and a one-line centred lead.
- **Captioned video tile.** A flex column inside `column is-one-third`: a 6em-tall centred caption at 9.6px (the full text prompt, e.g. "A post-apocalyptic bus interior with rusted chairs bolted to the floor."), then an autoplaying muted looping `video` with controls; renders sit on black, so each tile reads as a black display case on grey.
- **Prompt comparison row.** "Outer Prompt:" label (20px/600) over a 5em caption and video, separated by a 2px dashed `#cccccc` right border from three interior-variant videos with their own captions.
- **BibTeX block.** Bulma `pre` on `#f5f5f5`, padding 17.5px 21px, 14px monospace.
- **Footer.** Bulma `.footer` on `#fafafa` with icon links and the Nerfies Creative Commons credit.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / author block | Yes | Plain white hero |
| Venue badge | Yes, as text | x-large "NeurIPS 2025" line |
| Link buttons | Absent from the source | No paper, code or arXiv buttons on the page |
| Teaser | Yes | Full-width figure |
| Abstract | Yes | Centred heading, justified text |
| Results gallery | Yes | Grey band, 3-column grid of captioned black video tiles |
| Prompt-conditioning comparisons | Yes, non-standard | Quarter columns with dashed divider |
| Method | Yes | "Main Pipeline" figure and numbered paragraphs in a grey band |
| Qualitative comparisons | Yes | Full-width figure |
| Tabbed video viewer | Commented out in the source (its tab CSS remains) | |
| Results table | Absent from the source | |
| BibTeX | Yes | Bulma `pre` |
| Footer | Yes | Nerfies credit |

## Adapting to Other Content

- **Link buttons:** the page has none; if adding them, use Nerfies dark pills (`button is-normal is-rounded is-dark`, `#363636`) in a row under the note line so the hero stays monochrome.
- **More authors:** keep `span.author-block`s in one centred `is-size-5` run; they wrap naturally in the 960px column.
- **Larger galleries:** extend the `columns is-multiline` grid in the grey band; keep every caption box the same fixed height (6em) so videos align across a row.
- **A results table:** place it in a white section between gallery and pipeline, centred at 912px, Bulma `table is-striped` with 600-weight headers in `#363636`; keep it unboxed like the figures.
- **News:** a short list in the hero below the note line, 16px `#4a4a4a`, dates in bold.

## Do's and Don'ts

- Do let the media supply colour: white and `#f5f5f5` are the only page surfaces.
- Do give every gallery tile the full text prompt as its caption and a fixed caption height.
- Do group many results into a grey band so the grid reads as one wall.
- Don't omit paper and code links in a real deployment; this page has no buttons at all.
- Don't add frames or shadows to videos; the black letterbox already frames them.

## Surfaces

White hero and content sections; two `#f5f5f5` bands (results gallery and Main Pipeline); black video letterboxes; a `#fafafa` footer.

## Imagery

Textured 3D meshes rendered as turntable videos: cabins, buses, theatres, tents, chests, mugs, lamps and baroque wardrobes, each showing exterior and interior textures. The teaser and qualitative comparisons are PNG composites with handwritten-style prompt text and red dashed callouts.

## Layout

A 960px centred column throughout, with full-width colour bands behind the gallery and pipeline. Grids are Bulma columns: thirds for the gallery, a quarter plus three for comparisons.

## Agent Prompt Guide

Quick colors: title `#363636`, body `#4a4a4a`, authors `#209cee`, band `#f5f5f5`, band title `rgba(0,0,0,0.7)`, tile `#000000`, divider `#cccccc`, footer `#fafafa`.

1. "Build a quiet hero: white, padding 48px 24px, centred Google Sans 40px/600 title in `#363636`, a 24px venue line in `#4a4a4a`, 20px author links in `#209cee`, 16px affiliations and an 18px equal-contribution note; no buttons."
2. "Create a results gallery band: full-width `#f5f5f5`, centred 32px/600 heading in `rgba(0,0,0,0.7)`, then a three-column grid with 24px gutters where each tile is a 6em-tall centred 9.6px `#4a4a4a` caption above an autoplaying looping video on `#000000`."
3. "Make a comparison row: a quarter-width column labelled 'Outer Prompt:' at 20px/600 with a 2px dashed `#cccccc` right border, followed by three equal columns each with an 11.2px caption in a 5em box above a video."

## Similar Pages

Other Nerfies-template pages share the skeleton. In this NeurIPS 2025 batch, Seeing the Wind also uses bands to separate result carousels, and FastGDA is the other page with no buttons, using bracketed text links instead.

## Quick Start

```css
:root {
  --title: #363636;
  --text: #4a4a4a;
  --author: #209cee;
  --band: #f5f5f5;
  --band-title: rgba(0, 0, 0, 0.7);
  --tile: #000000;
  --divider: #cccccc;
  --footer: #fafafa;
  --font-display: 'Google Sans', 'Outfit', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
}
.gallery { background: var(--band); }
.video-caption { height: 6em; display: flex; align-items: center; justify-content: center; font-size: 0.6rem; color: var(--text); }
.gallery video { width: 100%; background: var(--tile); }
```

## Provenance

- **URL:** https://goatex3d.github.io/
- **Paper:** GOATex: Geometry & Occlusion-Aware Texturing (arXiv 2511.23051), Hyunjin Kim, Kunho Kim, Adam Lee, Wonkwang Lee (KRAFTON, NC AI, UC Berkeley, Seoul National University).
- **Venue:** NeurIPS 2025 (shown under the title).
- **Selection reason:** existing entry; the arXiv comment states acceptance at NeurIPS 2025 and links the project page.
- **Template credit:** footer credits the Nerfies source code.
- **Evidence used:** `computed_style.py` render at 1440×900 with first-viewport color share, the 1440 screenshot and tall capture, the Nerfies `index.css`, Bulma defaults and inline styles. Captured 2026-10-28.
