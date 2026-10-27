# SeTok Clustered Nerfies — Style Reference

> A borrowed Nerfies shell with colored triangle bullets marking each lab.

**Theme:** light

Values come from the static HTML, `static/css/index.css` and the stylesheets it links. Bulma 0.9 framework defaults dominate the raw frequency counts, so only colors that the page markup or its own CSS actually uses are listed. Measurements are normalized; roles are interpreted. The rendered page was not viewed.

## Overview

SeTok is a stock Nerfies/Bulma project page carried over from the authors' earlier NExT-GPT site (the footer says so). It is white, centered, and text-forward: Google Sans title and authors, Noto Sans body, dark pill buttons, and section titles at Bulma `is-3`. The only page-specific color is in the affiliation line, where each institution is prefixed by a ▶ glyph in its own hue (orange `#f68946`, translucent violet `#ac00d791`, green `#00d754`, blue `#008AD7`), and in one figure caption where key words are green `rgb(39,190,110)`. A Gradio theme stylesheet (`live_theme.css`, orange `--primary-500: #f97316`) and a Caveat webfont are also linked, but no visible element on the page uses them (inferred from markup).

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | (Bulma) | Page background |
| Bulma Graphite | `#363636` | (Bulma `$grey-darker`) | Titles, `is-dark` button fill |
| Body Gray | `#4a4a4a` | (Bulma) | Body copy |
| Author Sky | `hsl(204,86%,53%)` | (index.css) | Author name links (computes to about `#209CEE`) |
| Bulma Link | `#3273dc` | (Bulma) | Other inline links |
| Code Mist | `#f5f5f5` | (Bulma) | BibTeX `pre` background |
| Hairline | `#dbdbdb` | (Bulma) | Default borders |
| Lab Orange | `#f68946` | (inline) | ▶ marker, affiliation 1 |
| Lab Violet | `#ac00d791` | (inline) | ▶ marker, affiliation 2 |
| Lab Green | `#00d754` | (inline) | ▶ marker, affiliation 3 |
| Lab Blue | `#008AD7` | (inline) | ▶ marker, affiliation 4 |
| Keyword Green | `rgb(39,190,110)` | (inline) | Highlighted words in qualitative caption |
| Carousel Rule | `#bbb` | (index.css) | Results-carousel item border |

## Tokens — Typography

- **Display / authors:** Google Sans (Google Fonts). Substitute: Product Sans, Inter.
- **Body:** Noto Sans (set on `body` in index.css). Substitute: Open Sans.
- **Mono:** Bulma `monospace` stack for BibTeX.
- **Unused:** Caveat (cdnfonts) and Roboto (`@import` in index.css) are loaded but not applied to visible content (inferred).

| Role | Size | Weight |
|---|---|---|
| Publication title (`is-1`) | 3rem | 600 (Bulma title) |
| Subtitle "Understanding, Generating, Segmenting, Editing" | Bulma `is-3`/subtitle, 2rem (inferred) | 400 |
| Section title (`is-3`) | 2rem | 600 |
| Authors (`is-size-5`) | 1.25rem | 400 |
| Body | 1rem | 400 |
| Caption | 15px (inline) | 400 |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons (`is-rounded`) | 290486px (pill) |
| Carousel items, video embeds | 10px |
| Bulma controls | 4px |

**Shadows:** Bulma focus ring `0 0 0 .125em rgba(50,115,220,.25)`; card shadow `0 .5em 1em -.125em rgba(10,10,10,.1), 0 0 0 1px rgba(10,10,10,.02)` (framework, unused by visible cards).

**Layout:** `container is-max-desktop` (Bulma 960px, inferred) with `is-four-fifths` and `is-full-width` columns.

## Components

- **Hero:** white `hero`, centered title, author line with superscripts, affiliation line with colored ▶ markers, flex row of logos (inline flex, centered).
- **Link buttons:** `button is-normal is-rounded is-dark` with Font Awesome icons. Paper (arXiv), Demo (href `xxx`), Video (href `xxx`), Code (GitHub). Two of four are placeholders.
- **Section:** `section` with `title is-3` centered heading and `content has-text-justified` body.
- **BibTeX:** Bulma `pre` on `#f5f5f5`, `journal={ICLR}`.
- **Footer:** single line "The webpage is built based on NExT-GPT".

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Google Sans, colored ▶ affiliation markers |
| Venue badge | No | Venue only in BibTeX (`journal={ICLR}`) |
| Link buttons | Yes | Paper, Demo, Video, Code; dark pills; Demo and Video are `xxx` placeholders |
| Teaser figure / video | Yes | Static figure under the subtitle |
| Abstract | Yes | Justified text, `is-four-fifths` |
| Method figure | Yes | "Method", "Vision Cluster", "Training" sections with images |
| Results | Yes | "Qualitative Analysis" figures (8 images total) |
| Image comparison slider | No | |
| Interactive 3D / HF demo | No | Gradio CSS linked but no embed (`hf_demo` flag comes from CSS only) |
| BibTeX | Yes | Bulma pre |
| Acknowledgements | No | |

## Do's and Don'ts

- Do keep the page monochrome and let the four lab hues appear only as small ▶ markers.
- Do use green only to mark keywords inside captions.
- Don't ship placeholder `xxx` links as visible buttons.
- Don't load Gradio, Caveat and Roboto stylesheets that nothing uses.

## Surfaces

All white. No `hero is-light` bands; figures sit directly on the page.

## Imagery

Eight static images: logos, teaser, method diagrams and qualitative grids. No videos.

## Layout

Single centered 960px column, centered headings, justified paragraphs.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, text `#4a4a4a`, title `#363636`, author link `hsl(204,86%,53%)`, markers `#f68946` `#ac00d791` `#00d754` `#008AD7`, keyword `rgb(39,190,110)`.

1. "Write an affiliation line where each lab name is preceded by a ▶ in its own color (`#f68946`, `#00d754`, `#008AD7`), font-weight normal, separated by non-breaking spaces."
2. "Make Bulma `is-dark is-rounded` pill buttons for Paper and Code with Font Awesome icons, 5px vertical margin."
3. "Add a qualitative figure caption at 15px where key terms are colored `rgb(39,190,110)`."

## Similar Pages

NExT-GPT (the stated source), and every Nerfies-derived page in this collection (Sitcom-Crafter, LARP, AIF).

## Quick Start

```css
:root {
  --bg: #ffffff; --text: #4a4a4a; --title: #363636;
  --link: #3273dc; --author-link: hsl(204, 86%, 53%);
  --code-bg: #f5f5f5; --border: #dbdbdb;
  --lab-1: #f68946; --lab-2: #ac00d791; --lab-3: #00d754; --lab-4: #008AD7;
  --keyword: rgb(39, 190, 110);
  --font-display: "Google Sans", sans-serif; --font-body: "Noto Sans", sans-serif;
  --radius-pill: 290486px; --radius-media: 10px;
}
```

## Provenance

- **URL:** https://chocowu.github.io/SeTok-web/ (redirects to http://sqwu.top/SeTok-web/)
- **Paper:** Towards Semantic Equivalence of Tokenization in Multimodal LLM (arXiv 2406.05127), Shengqiong Wu et al.
- **Venue:** ICLR 2025 (not shown on the page itself).
- **Selection reason:** arXiv comment states acceptance at ICLR 2025 and links this page.
- **Template credit:** footer credits NExT-GPT, which is itself a Nerfies/Bulma derivative.
- **Measurement method:** `extract_style.py` on the redirected page plus manual reading of index.css, live_theme.css and inline styles. Rendered page not viewed.
