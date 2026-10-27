# WoW-Bench Field-Recording Nerfies — Style Reference

> A stock Nerfies page used as a listening booth: audio clips in a striped table, a whale beside the title.

**Theme:** light

Measurements come from the page's minified `static/css/index.css` (the unmodified Nerfies stylesheet), Bulma 0.9 defaults and inline `style=""` attributes. Bulma's full palette inflates the extractor counts; the table below lists only colors this page's markup uses. Roles are interpreted.

## Overview

The closest thing in this batch to factory Nerfies: Google Sans for title and authors, Noto Sans for body, dark rounded pill buttons, author links in Bulma info blue, and alternating `is-light` / white hero bands. What makes it its own page is the content. The title hero itself is the light `#f5f5f5` band, with a small transparent whale PNG inline after "WoW-Bench". The Example Questions section is a Bulma `table is-bordered is-striped` whose first column holds four `<audio>` players next to multiple-choice questions. Results are a five-second autoplay carousel of 600px-tall image slides, followed by stacked figures with centered subtitle captions. The venue line reads "Findings of ACL 2026" in bold.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Bulma Charcoal | `#363636` | Bulma `$dark` / strong text | Pill buttons, titles |
| Body Graphite | `#4a4a4a` | Bulma `$text` | Paragraphs |
| Info Sky | `hsl(204, 86%, 53%)` (≈ `#209cee`, inferred conversion) | `.publication-authors a` | Author links |
| Shallows | `#f5f5f5` | Bulma `hero.is-light` | Title hero, overview band |
| Stripe Grey | `#fafafa` | Bulma `table.is-striped` even rows (inferred) | Question table stripes |
| Table Rule | `#dbdbdb` | Bulma `$border` | `is-bordered` cell borders |
| Paper | `#ffffff` | Bulma body | White bands |
| Footer Ink | `#000000` | `.footer .icon-link`, carousel dots | Icons, pagination |
| Venue Grey | `#555555` | `.publication-venue` | Defined, unused (venue is a `<b>`) |
| Award Rose | `#ff3860` | `.publication-awards` | Defined, unused |

## Tokens — Typography

- **Title, authors, teaser:** `'Google Sans', sans-serif` (Google Fonts link `Google Sans|Noto Sans|Castoro`). Substitute: Product Sans, Inter.
- **Body:** `'Noto Sans', sans-serif`.
- **Mono:** Bulma `monospace` for BibTeX.
- **Weights:** Bulma title 600; venue `<b>` bold; body 400.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Title (`title is-1`) | 3rem | 600 | 1.125 | Google Sans, whale icon inline |
| Section title (`title is-3`) | 2rem | 600 | 1.125 | centered |
| Sub-heading (`title is-5`) | 1.25rem | 600 | 1.125 | max-width 80% |
| Authors / venue (`is-size-5`) | 1.25rem | 400 / bold | 1.5 | |
| Figure caption (`subtitle`) | 1.25rem | 400 | 1.25 | centered, margin 0 |
| Overview caption | 1.25rem | 400 | 1.25 | max-width 60% |
| Body | 1rem | 400 | 1.5 | justified abstract |
| Affiliation note | 0.8em | 400 | 1.5 | inline style |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons (`is-rounded`) | 290486px |
| Bulma controls, tables | 4px / 0 |
| YouTube wrapper (defined) | 10px |

- **Shadows:** none beyond Bulma focus rings.
- **Layout:** Bulma containers (1152px / 1344px); abstract in `column is-four-fifths`; carousel items `height: 600px` with an 80%-wide, 500px image box; table cells padded 15px inline.

## Components

- **Light title hero.** `hero is-light` holds the title, five linked authors with numeric superscripts, affiliation line, a 0.8em note and the bold venue line.
- **Pill button.** `external-link button is-normal is-rounded is-dark`, `#363636`, white label with icon. Three buttons: Paper (ACL Anthology), Code (GitHub), Dataset (Hugging Face).
- **Audio question table.** `table is-bordered is-striped`, width 100%; left column an `<audio controls>` player (inline 120px height wrappers), right column question text, type label and options A–D, padded 15px and left-aligned.
- **Results carousel.** `bulma-carousel` with `autoplaySpeed="5000"`; each slide is a flex column 600px tall, image centered in a 500px box, caption under it.
- **Stacked figures.** Distribution, human-evaluation and qualitative PNGs, each followed by a centered `subtitle` caption with margin 0.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Google Sans on light band, whale icon |
| Venue badge | Text | Bold "Findings of ACL 2026" |
| Link buttons | Paper, Code, Dataset | Dark pills |
| Teaser | No video; overview figure in second band | |
| Abstract | Yes | White `section hero` |
| Method / overview figure | Yes | Light band, 60%-wide caption |
| Example table with audio | Yes | Striped bordered table with four players |
| Results | Carousel plus three captioned figures | |
| Sliders / 3D / HF Space | No | |
| BibTeX | Yes | ACL Anthology `@inproceedings` with DOI and pages |
| Acknowledgements | Yes | Credits the Watkins Marine Mammal Sound Database |

## Do's and Don'ts

- Do keep the stock Nerfies fonts if you want the familiar look; this page changes nothing in the CSS.
- Do put audio inside the table cell next to its question so the clip and options read together.
- Do give carousel slides a fixed height so images of different aspect ratios do not jump.
- Don't add colour accents; the page uses only Bulma neutrals and the author-link blue.
- Don't leave `alt="MY ALT TEXT"` placeholders as this page does on several figures.

## Surfaces

Alternating `#f5f5f5` and white full-width bands, starting with a light title band. Bulma default footer.

## Imagery

Static PNG figures (overview, main results, distribution, human evaluation, qualitative), a whale icon, and four audio clips. No video.

## Layout

Centered single column inside Bulma containers; figures centered with inline flex wrappers.

## Agent Prompt Guide

**Quick colors:** band `#f5f5f5`, page `#ffffff`, text `#4a4a4a`, title/buttons `#363636`, author links `hsl(204,86%,53%)`, table rules `#dbdbdb`.

1. "Create a light Bulma title hero (`#f5f5f5`) with a Google Sans 3rem title followed by an inline transparent animal icon, author links in `hsl(204,86%,53%)`, and a bold 1.25rem venue line."
2. "Build a `table is-bordered is-striped` where each row has an `<audio controls>` player in the left cell and a question, type tag and A–D options left-aligned with 15px padding in the right cell."
3. "Make a results carousel with five-second autoplay; each slide is a 600px-tall flex column with the image centered in an 80%-wide, 500px-tall box."

## Similar Pages

SALAD (CVPR 2025) and CoSyn (ACL 2025) in this collection use the same Nerfies skeleton with a different font; BadScientist and VC-Inspector use the newer Inter-based revision of the same template.

## Quick Start

```css
:root {
  --dark: #363636; --text: #4a4a4a; --band: #f5f5f5; --page: #ffffff;
  --rule: #dbdbdb; --author-link: hsl(204, 86%, 53%);
  --font-title: 'Google Sans', sans-serif; --font-body: 'Noto Sans', sans-serif;
  --radius-pill: 290486px;
}
body { font-family: var(--font-body); }
.publication-title, .publication-authors { font-family: var(--font-title); }
```

## Provenance

- **URL:** https://jaeyeonkim99.github.io/wow_bench/
- **Paper:** WoW-Bench: Evaluating Fine-Grained Acoustic Perception in Audio-Language Models via Marine Mammal Vocalizations (arXiv 2508.20976), Jaeyeon Kim, Heeseung Yun, Tony Woo, Chao-Han Huck Yang, Gunhee Kim (CMU, Seoul National University, NVIDIA).
- **Venue:** ACL 2026 Findings (page: "Findings of ACL 2026"; BibTeX gives `2026.findings-acl.1562`, pages 31208–31229).
- **Selection reason:** the arXiv comment states acceptance at ACL 2026 Findings and links this page.
- **Template credit:** footer credits the Academic Project Page Template, adopted from Nerfies.
- **Measurement method:** `extract_style.py` plus manual reading of `index.css`, the HTML and inline styles. No arXiv link button is present (the Paper button points to the ACL Anthology). The rendered page was not viewed; the striped-row colour is Bulma's documented default, not measured.
