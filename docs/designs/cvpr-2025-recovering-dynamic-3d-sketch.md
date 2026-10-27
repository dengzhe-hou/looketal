# Liv3Stroke Sketchbook — Style Reference

> A tidy lab notebook where the title is written in marker and the figures are pen strokes.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 screenshot, scrolled captures of the full 5,327px page, the page's own `css/styles.css` and its markup. The page sits on Bulma 1.0.1 (CSS-variable version, so body text is Bulma 1.0's #404654 and the footer #f9fafb), with the author's fonts and navy buttons layered on top; it credits the 3Doodle page as its template. Color share is measured on the first 1440×900 viewport.

## Overview

A white, centred page whose voice is handwriting. The paper title is set in Gochi Hand, a felt-tip marker face, at 48px in charcoal #2e333d. Under it sit a bold Quicksand "CVPR 2025", four author names in periwinkle #50549b spread across equal columns, the university, two lab logos with tiny superscript keys, and three navy #143163 pill buttons with white Quicksand labels. The teaser is an autoplay video whose frames are themselves drawn like a sketchbook (a black-outlined photo card with a drop shadow, a clapperboard icon and a handwritten "Input Video" label), followed by a Gochi Hand one-line TL;DR. The rest is a 960px Bulma column: navy #14274e Quicksand section heads (Abstract, Method, Results, Ablation Study, BibTeX), justified light Quicksand body, wide line-drawing figures and video rows with small bold method labels, a soft-shadowed BibTeX card and a pale grey footer with home and GitHub icons.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 68.5% and off-white #fefefe 23.4% (the teaser video's near-white background), mid grey #96979e 5.2% (text, logos, video outline and photo), then traces of near-white. The navy buttons, periwinkle names and logo blues and purples are each under 1% at this quantization.

Anatomy in DOM order (all centred; hero container `is-max-widescreen` 1152px wide at x=144):

1. **Title** — `h1.title.is-size-1.publication-title`, "Recovering Dynamic 3D Sketches from Videos", Gochi Hand 48px / declared weight 100 (renders the face's only weight, 400) / line-height 54px, #2e333d, one line (y=58–112). Margin 10px 0 24px. Gap 26px.
2. **Venue** — `span.conf-block`, "CVPR 2025", Quicksand 20px / 700 / 30px, #404654 (y=138–163). Gap 13px.
3. **Authors** — four `.column.is-2-tablet.publication-authors` cells, 154px wide each, inside a 960px `author-list` container; names are `a.author-blocks` in Quicksand 16px / 500 #50549b with superscript affiliation numbers; hover #9bb4c2 (y=176–202). The equal columns leave uneven visual gaps between names.
4. **Institution** — `span.author-block`, "Seoul National University", Quicksand 16px / 400 #404654 (y=210–234). Gap 22px.
5. **Lab logos** — `.logo-list` flex row: superscript "1" (12px #50549b), the Visual & Geometric Intelligence Lab wordmark (58px high), superscript "2", the 3D Vision Lab wordmark (55px high); y=256–322. Gap 20px.
6. **Buttons** — three `a.button.link-button.is-rounded`, "Paper" (Font Awesome file-pdf), "arXiv" (Academicons), "Code" (GitHub), labels in `span.botton-text` Quicksand 16px / 600 #f5f5f5 on #143163, 1px #143163 border, pill radius, padding 7px 19px, margin 0 1.6px 8px, Bulma 1.0 shadow `0 1px 2px rgba(51,51,51,0.05), 0 2px 4px rgba(51,51,51,0.05)`; y=342–382. Gap 104px (end of hero section plus the teaser hero's padding).
7. **Teaser video** — `video.teaser_video`, 864×414 at x=288, y=486; the drawn frame, clapperboard and "Input Video" label are inside the footage. Continues below the fold to y=900, then the TL;DR line at y=907.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | Bulma 1.0 scheme background | page background |
| Title Charcoal | #2e333d | Bulma 1.0 `.title` color | paper title |
| Body Slate | #404654 | Bulma 1.0 text color | venue, institution, abstract and body text, captions, method labels, footer text |
| Heading Navy | #14274e | `.publication-keywords` | section heads |
| Button Navy | #143163 | `.link-button` | button fill and border; hover text |
| Button Label | #f5f5f5 | `.link-button` color | button labels; hover fill |
| Author Periwinkle | #50549b | `.author-blocks`, `.logo-list` | author names, affiliation superscripts |
| Author Hover | #9bb4c2 | `.author-blocks:hover` | author name hover |
| Link Blue | #4258ff | Bulma 1.0 link | footer licence and template links |
| BibTeX Card | #f5f5f5 | `.bibtex-box` | BibTeX card background |
| Code Grey | #f3f4f6 | Bulma 1.0 `pre` | inner `pre` inside the BibTeX card |
| Card Shadow | #090a0c | Bulma 1.0 card shadow | `0 8px 16px -2px rgba(9,10,12,0.1), 0 0 0 1px rgba(9,10,12,0.02)` on the BibTeX card |
| Button Shadow | #333333 | Bulma 1.0 button shadow | `0 1px 2px rgba(51,51,51,0.05), 0 2px 4px rgba(51,51,51,0.05)` |
| Footer Mist | #f9fafb | Bulma 1.0 `.footer` | footer band |
| Video Grey | #96979e | (screenshot) | strongest mid-tone in the first viewport: text, logo, teaser outline |

## Tokens — Typography

- **Display (handwritten):** declared `"Gochi Hand"` on `.publication-title` and `.tldr` (Google Fonts); rendered Gochi Hand 400. Substitute: Caveat Brush (heavier) or Patrick Hand (calmer); Gochi Hand itself is free.
- **Text:** declared `'Quicksand'` on `.content`, `.publication-authors`, `.publication-keywords`, `.caption`, `.method-name`, `.botton-text`; rendered Quicksand variable 300–700. Substitute: Nunito.
- **UI fallback:** Bulma 1.0 body stack `Inter, "SF Pro", "Segoe UI", Roboto, …`; Inter is not web-loaded, so any text outside the Quicksand classes uses the visitor's system face (Segoe UI on Windows). Almost all visible text is in the classes above.
- **Mono:** `.bibtex-box` declares `"Roboto Mono"` (loaded 400); the inner `pre` uses Bulma's `Inconsolata, Hack, "SF Mono", "Roboto Mono", …` stack at 14px, which resolves to Roboto Mono where Inconsolata is absent.
- **Declared but not visible:** Indie Flower is requested from Google Fonts and never applied.
- **Icons:** Font Awesome 6 (solid, brands), Academicons.

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `h1.publication-title` | 48px / 400 / 54px, Gochi Hand |
| Venue | `.conf-block` | 20px / 700 / 30px, Quicksand |
| Authors | `.publication-authors` | 16px / 500 / 24px, Quicksand |
| TL;DR | `h2.tldr` | 20px / 400 / 30px, Gochi Hand, centred |
| Section heads | `h2.subtitle.is-size-3.publication-keywords` | 32px / 500 / 40px, Quicksand, #14274e |
| Body | `.content p` | 16px / 400 / 24px, Quicksand, justified |
| Method labels | `.method-name` | 14px / 700 / 21px, Quicksand, centred |
| Captions | `p.caption` | 16px / 400 / 24px, Quicksand, centred, margin -1rem 0 2.5rem |
| Buttons | `.botton-text` | 16px / 600 / 24px, Quicksand |
| BibTeX | `pre` | 14px / 400 / 21px mono |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Buttons | Bulma `is-rounded` (radius 9999px), padding 7px 19px, 1px #143163 border, soft two-layer shadow |
| BibTeX card | radius 12px, padding 20px, card shadow (see colors); inner `pre` square, padding 20px 24px |
| Teaser and result videos | square edges in CSS; the sketchbook frame is painted in the video |
| Figures | square, no border |
| Lab logos | 58px and 55px max-height, 10px side margin on the second |

## Layout Metrics

- **Hero:** `.container.is-max-widescreen` (1152px at 1440, x=144); authors in a 960px `.is-max-desktop` container; hero-body Bulma 1.0 padding 48px 24px.
- **Teaser:** `.container.is-max-desktop` 960px; video 864px wide (90%), centred.
- **Sections:** `section.section` padding 48px; inner container 960px (x=240–1200); body column 936px (12px column padding); h2 margin-bottom 24px.
- **Result rows:** each comparison is one wide pre-composited video per row in a Bulma 1.0 `fixed-grid has-1-cols`; the method labels below sit in a `fixed-grid has-5-cols` (five 182px cells, about 12px gutters); single result videos are capped at `max-height: 15rem` (240px).
- **Method figure:** full 936px column width.
- **BibTeX:** card 960px wide, `pre` 920px.
- **Footer:** padding 16px 24px 96px; two 40px icon links, then two centred text lines.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1216px | 960px column (1152px hero) | 16px | 48px | author columns 154px each |
| 1024–1215px | 960px column for hero and body | 16px | 48px | as above |
| 769–1023px | 48px section padding, fluid container | 16px | 48px | author cells stay `is-2-tablet`, names may wrap to two lines |
| ≤768px | 24px | 16px | 40px (`is-size-2-mobile`) | author columns stack one per line; abstract switches to left-aligned (`has-text-left-mobile`); the `fixed-grid has-5-cols` label rows stay five-up and get cramped |

## Components

- **Marker title:** Gochi Hand 48px #2e333d, centred, one line at desktop; reuse the face only for the title and the TL;DR line.
- **Navy pill button:** `.button.link-button.is-rounded`, #143163 fill and border, #f5f5f5 Quicksand 16px / 600 label, icon left, padding 7px 19px, margin 0 0.1rem 0.5rem; hover swaps to #f5f5f5 fill with #143163 text and border.
- **Author grid:** equal-width Bulma columns, periwinkle #50549b names with superscripts, hover #9bb4c2.
- **Logo strip:** affiliation superscripts beside lab wordmarks in a flex row, no boxes.
- **Labelled result row:** one composited comparison video, a five-cell grid of Quicksand 14px / 700 labels centred under its panels, then a Quicksand 16px caption.
- **BibTeX card:** #f5f5f5, radius 12px, 20px padding, Bulma card shadow, Roboto Mono.
- **Footer:** #f9fafb band, centred home and GitHub icons, licence line and "Template borrowed from 3Doodle" with #4258ff links.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / venue / authors | Yes | handwritten title, bold venue, column author grid |
| Lab logos | Yes | two wordmarks with superscript keys |
| Link buttons | Yes | three navy pills |
| Teaser video | Yes | sketchbook-styled footage plus Gochi Hand TL;DR |
| Abstract | Yes | justified Quicksand, navy head |
| Method figure | Yes | full-width line diagram plus paragraph |
| Results | Yes | labelled video rows with captions |
| Ablation | Yes | labelled video rows |
| Results table | No (absent from the source) | |
| BibTeX | Yes | shadowed grey card |
| Footer | Yes | icon links and template credit |

## Adapting to Other Content

- **More authors:** the `is-2-tablet` cells fit five per row in the 960px container; past that let the columns wrap to a second row or switch to an inline comma list in the same #50549b Quicksand 500.
- **Results table:** center it in the 960px column under a navy Quicksand head; Quicksand 16px cells, a 14px / 700 header row like the method labels, and a #f5f5f5 card with the 12px radius and the same shadow as BibTeX.
- **Long titles:** Gochi Hand runs wide; above about 50 characters let it wrap to two lines rather than shrinking below 40px.
- **News or updates:** a short Quicksand list above the Abstract, each date in #14274e bold.
- **More links:** add further navy pills; keep the hover inversion.

## Do's and Don'ts

- Do confine the handwritten face to the title and the one-line TL;DR; everything else is Quicksand.
- Do keep the palette to navy, periwinkle and slate on white; let line-drawing figures supply the texture.
- Do label every result video with a short bold Quicksand caption.
- Don't wrap figures in frames; the sketchbook framing lives inside the teaser footage.
- Don't set weight 100 on a single-weight display face and expect it to thin; Gochi Hand renders 400 regardless.
- Don't use Bulma's default blue for buttons; they are #143163.

## Surfaces

White page throughout; the only filled surfaces are the navy pills, the #f5f5f5 BibTeX card with a soft drop shadow, and the #f9fafb footer.

## Imagery

Black pen-stroke 3D sketches beside photos or renders of the source objects (LEGO excavator, dancers, a bird, toys), a hand-drawn-style method diagram with an MLP box, and a teaser that frames footage like a pasted photo card.

## Layout

A centred hero up to 1152px wide, then a single 960px column with generous 48px section padding. Rendered height about 5,300px.

## Agent Prompt Guide

Quick colors: title #2e333d, body #404654, heads #14274e, buttons #143163 with #f5f5f5 labels, authors #50549b (hover #9bb4c2), BibTeX card #f5f5f5, footer #f9fafb, links #4258ff.

1. "Create a centred hero: a 48px Gochi Hand title in #2e333d, a 20px Quicksand bold 'CVPR 2025' in #404654, four author names in equal 154px columns in Quicksand 16px weight 500 #50549b with superscripts, then pill buttons: #143163 fill and border, #f5f5f5 Quicksand 16px weight 600 labels, padding 7px 19px, icon left; hover inverts to #f5f5f5 fill and #143163 text."
2. "Add section heads in Quicksand 32px weight 500 #14274e, centred, 24px above the content, in a 960px column with 48px section padding; body Quicksand 16px / 24px #404654, justified."
3. "Build a BibTeX card: #f5f5f5 background, 12px radius, 20px padding, shadow 0 8px 16px -2px rgba(9,10,12,0.1) plus 0 0 0 1px rgba(9,10,12,0.02), Roboto Mono 14px."

## Similar Pages

- 3Doodle (the stated template source) and other sketch and stroke-rendering project pages.
- Bulma 1.0 project pages with a novelty display face for the title only.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --title: #2e333d;
  --text: #404654;
  --heading: #14274e;
  --button: #143163;
  --button-label: #f5f5f5;
  --author: #50549b;
  --author-hover: #9bb4c2;
  --link: #4258ff;
  --card: #f5f5f5;
  --footer: #f9fafb;
  --font-display: 'Gochi Hand', cursive;
  --font-text: 'Quicksand', 'Nunito', sans-serif;
  --font-mono: 'Roboto Mono', monospace;
  --title-size: 48px;
  --h2-size: 32px;
  --body-size: 16px;
  --radius-pill: 9999px;
  --radius-card: 12px;
  --column: 960px;
}
```

## Provenance

- **URL:** https://jaeah.me/liv3stroke_web
- **Paper:** Recovering Dynamic 3D Sketches from Videos (arXiv 2503.20321), Jaeah Lee, Changwoon Choi, Young Min Kim, Jaesik Park, Seoul National University.
- **Venue:** CVPR 2025 (stated under the title).
- **Selection reason:** arXiv 2503.20321 comment states acceptance at CVPR 2025; project page linked in the abstract.
- **Template credit:** footer says the template is borrowed from 3Doodle.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share, the 1440×900 screenshot, scrolled full-page captures, `css/styles.css`, page HTML, Bulma 1.0.1 computed defaults; 2026-10-28.
