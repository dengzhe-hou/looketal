# BlurDM Cayman Gradient — Style Reference

> A GitHub README in its Sunday best: a blue-to-green sky across the masthead, white type, and plain green headings underneath.

**Theme:** light

Measured from the rendered page at 1440×900 in headless Chrome (`computed_style.py`, screenshot and tall capture), then checked against the Jekyll Cayman theme stylesheet `assets/css/style.css` and the page's inline styles. Where stylesheet and render disagree, the render is reported. Pixel values are at the 1440px viewport unless a breakpoint is named.

## Overview

GitHub Pages' Cayman theme with a hand-edited header. A full-width banner carries Cayman's 120° gradient from blue `#155799` to green `#159957`, with white type centred on it: a 52px/700 two-line title, a 70%-opacity "NeurIPS 2025" tagline, bold author names with superscripts, a smaller affiliation line, and two shields.io "for-the-badge" image badges (PAPER | PDF in grey and blue, CODE | GITHUB in grey and black) instead of Cayman's own buttons. Below the banner, a 1024px Markdown column (832px of text after 96px side padding) holds the pipeline teaser, then sections whose `h2`s are light 26.4px headings in Cayman green `#159957`. Body text is a soft blue-grey `#606c71`. The Results section is figures only: a qualitative grid and a results table rendered as an image. A pale blue code block for the citation and a hairline-topped footer close the page. Document height is about 3,196px.

## First Viewport

Color share of the first 1440×900 viewport: `#ffffff` 33.7% (page), `#186c83` 23.1%, `#1b8171` 20.9%, `#107c74` 8.6%, `#1d567b` 2.7% (steps of the blue-to-green header gradient), `#fff8f3` 5.3% (warm white teaser background), `#7eb9a5` 4.8% (light green and blue process arrows in the teaser), `#fffffe` 0.8%.

Anatomy in DOM order (centred unless noted):

1. Header `header.page-header`, full width, 509px tall, `linear-gradient(120deg, #155799, #159957)` over `#159957`, padding 80px 96px.
2. Title `h1.project-name`, Open Sans 52px/700, `#ffffff`, line-height 78px, two lines (y=80 to 236). Gap about 17px.
3. Tagline `h2.project-tagline` "NeurIPS 2025", 20px/400, `#ffffff` at 0.7 opacity. Gap about 32px.
4. Authors `p` (inline style), 18px, names bold 700, line-height 1.45, `#ffffff`, `&nbsp;` separators, numeric superscripts (y=315). Gap 6px.
5. Affiliations `p`, 15px/400, line-height 1.35, `#ffffff` (y=347). Gap about 12px.
6. Badges `p` (margin-top 12px): two shields.io images, 28px tall, 12px apart, at y≈390. Header ends at y=509 (80px bottom padding).
7. Main column `main.main-content`, max-width 1024px, padding 32px 96px; teaser image at y=541, 832×180px.
8. `h2` "Abstract" at y=759, 26.4px/400 `#159957`, left-aligned; abstract paragraph at y=817, 17.6px `#606c71`, line-height 26.4px, running past the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Cayman Blue | `#155799` | `.page-header` gradient start | Header top-left |
| Cayman Green | `#159957` | `.page-header` gradient end and fallback; `.main-content h2` | Header bottom-right; section headings |
| Header White | `#ffffff` | `.page-header` color | Title, authors, affiliations; tagline at 0.7 opacity |
| Slate Text | `#606c71` | `body` color | Body text, footer |
| Link Blue | `#1e6bb8` | `a` | Inline links (MIMO-UNet, Stripformer, FFTformer, LoFormer), footer links; hover adds underline |
| Code Slate | `#567482` | `.main-content pre`, `code` | Citation text |
| Code Ground | `#f3f6fa` | `.main-content pre` | Citation block fill |
| Code Edge | `#dce6f0` | `.main-content pre` border | 1px citation block border |
| Footer Rule | `#eff0f1` | `.site-footer` border-top | 1px rule above the footer |
| Badge Grey | `#555555` | shields.io left segment | "PAPER" and "CODE" badge labels |
| Badge Blue | `#007ec6` | shields.io `blue` | "PDF" badge segment |
| Badge Black | `#000000` | shields.io `black` | "GITHUB" badge segment |
| Page | `#ffffff` | `body` | Main column background |

## Tokens — Typography

- **Declared:** `body { font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; line-height: 1.5 }`, Open Sans 400/700 via `@import` from Google Fonts. Code: `Consolas, "Liberation Mono", Menlo, Courier, monospace`.
- **Rendered:** Open Sans 400 and 700 loaded. Badge text is part of the shields.io SVG images (Verdana-style uppercase with letter-spacing). Substitute: Noto Sans, which shares Open Sans's proportions.

| Role | Selector | Size | Weight | Line height | Colour |
|---|---|---|---|---|---|
| Title | `h1.project-name` | 52px (3.25rem) | 700 | 78px | `#ffffff` |
| Tagline | `h2.project-tagline` | 20px | 400 | 30px | `#ffffff` at 0.7 |
| Authors | header `p` (inline) | 18px | 700 names | 26.1px | `#ffffff` |
| Affiliations | header `p` (inline) | 15px | 400 | 20.25px | `#ffffff` |
| Section heading | `.main-content h2` | 26.4px | 400 | 39.6px | `#159957`, left |
| Body | `.main-content p` | 17.6px (1.1rem) | 400 | 26.4px | `#606c71` |
| Citation | `.main-content pre` | 14.4px | 400 | 20.9px | `#567482` |
| Footer | `.site-footer` | 16px | 400 | 24px | `#606c71`, owner line bold |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Citation `pre` | 4.8px (0.3rem) |
| Header | 0 |
| Images | 0 |
| shields.io badges | 0 (for-the-badge style is square) |

- **Shadows:** none.
- **Borders:** citation block 1px `#dce6f0`; footer top 1px `#eff0f1`.
- **Motion:** none on the rendered elements; Cayman's `.btn` transitions are unused here.

## Layout Metrics

- **Container:** `.main-content` `max-width: 64rem` (1024px), `margin: 0 auto`, padding 32px 96px at ≥64em, so text and figures are 832px wide (x=304 to 1136 at 1440px).
- **Header:** full width, padding 80px 96px at ≥64em; title block is centred across 1248px.
- **Sections:** `h2` margins 32px top, 16px bottom; paragraphs 17.6px bottom margin. No section bands.
- **Figures:** all images `max-width: 100%`, so 832px wide: teaser 832×180px, qualitative grid and table image full width.
- **Footer:** inside the main column, 32px top padding and margin, 1px top rule.

| Breakpoint | Container | Header padding | Body size | Title size | Grid change |
|---|---|---|---|---|---|
| ≥1024px (64em) | 1024px, 96px side padding | 80px 96px | 17.6px | 52px, tagline 20px | none |
| 672–1023px (42–64em) | fluid, 64px side padding | 48px 64px | 17.6px | 36px, tagline 18.4px | none |
| <672px | fluid, 16px side padding | 32px 16px | 16px | 28px, tagline 16px | none; badges wrap |

## Components

- **Gradient masthead.** `header.page-header`: `background-color: #159957; background-image: linear-gradient(120deg, #155799, #159957)`, white centred type, padding 80px 96px.
- **Author lines.** Two inline-styled `p`s inside the header: 18px bold names with superscripts and `&nbsp;&nbsp;` gaps; 15px affiliations.
- **Badge links.** shields.io images with `style=for-the-badge`: 28px tall, two-segment, uppercase; PAPER (`#555555`) | PDF (`#007ec6`) and CODE (`#555555`) | GITHUB (`#000000`); wrapped in `a` with `margin: 0 6px`, no hover change.
- **Green section heading.** `.main-content h2`: 26.4px, weight 400, `#159957`, left-aligned, 32px above and 16px below.
- **Figure plus caption paragraph.** An `img` at full column width immediately followed (same `p`) by a plain 17.6px explanation; dataset links inline in `#1e6bb8`.
- **Citation block.** `pre.highlight`: `#f3f6fa` fill, 1px `#dce6f0` border, 4.8px radius, 12.8px padding, 14.4px Consolas in `#567482`.
- **Footer.** "BlurDM is maintained by Jin-Ting-He. This page was generated by GitHub Pages." in `#606c71`, 1px `#eff0f1` top rule.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / author block | Yes | Gradient masthead, white type |
| Venue badge | Yes, as tagline | "NeurIPS 2025" at 0.7 opacity |
| Link buttons | Present but non-standard | shields.io image badges (Paper PDF, Code GitHub); Cayman's "View on GitHub" button removed |
| Teaser | Yes | Pipeline figure at column width |
| Abstract | Yes | Green `h2`, plain paragraph |
| Qualitative results | Yes | Full-width image grid with caption |
| Results table | Present as an image | PSNR/SSIM/LPIPS table exported as PNG, not HTML |
| Method / overview | Yes | Teaser repeated, three-stage diagram |
| BibTeX | Yes | Cayman code block |
| Footer | Yes | GitHub Pages credit |
| Video, carousel, sliders | Absent from the source | |

## Adapting to Other Content

- **More authors:** keep them in the header `p` at 18px bold with `&nbsp;&nbsp;` separators; they wrap centred within the 1248px header width. Move to two lines before shrinking type.
- **More links:** add more shields.io badges with matching two-tone segments, or use Cayman's own `.btn` (`rgba(255,255,255,0.08)` fill, 1px `rgba(255,255,255,0.2)` border, 0.3rem radius, `rgba(255,255,255,0.7)` text) for a quieter look.
- **A results table:** use a real Markdown table; Cayman styles `th, td` with 8px 16px padding and 1px `#e9ebec` borders, bold headers, and lets the table scroll horizontally inside the 832px column.
- **Long publication or news lists:** plain Markdown lists in `#606c71`, dates in bold, under a green `h2`.

## Do's and Don'ts

- Do keep the masthead the only coloured block and the rest of the page white.
- Do carry the green through every `h2` and nowhere else.
- Do keep figures at full column width with the explanation directly beneath.
- Don't render results tables as images if they need to be read or copied; Cayman already styles HTML tables.
- Don't mix badge styles; use one shields.io style for every link.

## Surfaces

A full-width blue-to-green gradient header, then a white page. The only other fill is the `#f3f6fa` citation block.

## Imagery

A warm-white pipeline figure of a face progressively blurred and noised with orange forward and blue reverse arrows; a qualitative grid of street and sign crops comparing baselines and BlurDM; a results table image; a three-stage architecture diagram with blue, orange and green blocks.

## Layout

One centred 1024px Markdown column (832px of content) under a full-bleed header. No grids or columns; everything stacks.

## Agent Prompt Guide

Quick colors: header `#155799` → `#159957`, header text `#ffffff`, headings `#159957`, body `#606c71`, link `#1e6bb8`, code `#f3f6fa` with `#dce6f0` border and `#567482` text, footer rule `#eff0f1`.

1. "Build a masthead: full width, `background: #159957 linear-gradient(120deg, #155799, #159957)`, padding 80px 96px, centred white Open Sans 52px/700 title, a 20px tagline at 0.7 opacity, 18px bold author names with superscripts and a 15px affiliation line."
2. "Style the content column: max-width 1024px, padding 32px 96px, body Open Sans 17.6px in `#606c71` with 1.5 line-height, `h2` at 26.4px weight 400 in `#159957`, links `#1e6bb8` with underline on hover."
3. "Make a citation block: `#f3f6fa` fill, 1px `#dce6f0` border, 0.3rem radius, 0.8rem padding, 14.4px Consolas in `#567482`."

## Similar Pages

Any GitHub Pages site on the Cayman theme. In this NeurIPS 2025 batch, EgoGazeVQA also opens on a saturated gradient hero with white type, and 4DGT and ZPressor use a full-width (pale) hero band.

## Quick Start

```css
:root {
  --header-from: #155799;
  --header-to: #159957;
  --heading: #159957;
  --text: #606c71;
  --link: #1e6bb8;
  --code-bg: #f3f6fa;
  --code-border: #dce6f0;
  --code-text: #567482;
  --rule: #eff0f1;
  --font: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.page-header { color: #fff; text-align: center; background: var(--header-to) linear-gradient(120deg, var(--header-from), var(--header-to)); padding: 5rem 6rem; }
.main-content { max-width: 64rem; margin: 0 auto; padding: 2rem 6rem; font-size: 1.1rem; color: var(--text); }
.main-content h2 { font-weight: normal; color: var(--heading); margin: 2rem 0 1rem; }
```

## Provenance

- **URL:** https://jin-ting-he.github.io/BlurDM/
- **Paper:** BlurDM: A Blur Diffusion Model for Image Deblurring (arXiv 2512.03979), Jin-Ting He, Fu-Jen Tsai, Yan-Tsung Peng, Min-Hung Chen, Chia-Wen Lin, Yen-Yu Lin (National Yang Ming Chiao Tung University, National Tsing Hua University, National Chengchi University, NVIDIA).
- **Venue:** NeurIPS 2025 (page tagline).
- **Selection reason:** the arXiv comment states acceptance at NeurIPS 2025 and links the project page.
- **Template credit:** footer says the page was generated by GitHub Pages; the stylesheet is the Jekyll Cayman theme.
- **Evidence used:** `computed_style.py` render at 1440×900 with first-viewport color share, the 1440 screenshot and tall capture, the Cayman `assets/css/style.css` and the page markup. Captured 2026-10-28.
