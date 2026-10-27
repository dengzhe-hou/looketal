# RePHO Optima Jumbotron — Style Reference

> A humanist-serif title on a cool grey jumbotron, dusty blue and sand in the words.

**Theme:** light

Values come from the static HTML, `css/theme.css` (HSMR-style project theme) and `css/bootstrap-4.4.1.css`. Bootstrap's palette inflates the raw counts, so only colors the page markup or theme.css uses are listed. Measurements are normalized; roles are interpreted. The rendered page was not viewed.

## Overview

RePHO follows the Bootstrap 4 project-page lineage (footer: "adapted from the HSMR project page template"). The header is a Bootstrap `jumbotron` with a vertical gradient `#f7f8fb → #eef2f5`. The two-line bold title is set in Philosopher and colors two noun phrases: "Physically Plausible" in dusty blue `#9bb7c9` and "Human-Object Interactions" in sand `#c2ab97`. A gray `h4` "CVPR 2026 (Highlight)" and an `hr` precede plain author links. Below, five `btn btn-light btn-large` buttons (Arxiv, SupMat, Code, Video, Citation) carry Font Awesome and Academicons icons. Body copy uses `'optima', 'Philosopher'` at `font-size: medium`, paragraphs in Google-Slides gray `#595959`. Results are Bootstrap video carousels inside dark `#111` frames with a soft `0 8px 24px` shadow, circular translucent arrows and pill-shaped indicator dots. The BibTeX block is a `#e9eeef` panel with 15px radius and `user-select: all`.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | (Bootstrap body) | Page background |
| Frost Top | `#f7f8fb` | (theme.css) | Jumbotron gradient start |
| Frost Bottom | `#eef2f5` | (theme.css) | Jumbotron gradient end |
| Dusty Blue | `#9bb7c9` | (inline) | Title phrase "Physically Plausible" |
| Sand | `#c2ab97` | (inline) | Title phrase "Human-Object Interactions" |
| Venue Slate | `#5a6268` | (inline) | "CVPR 2026 (Highlight)" |
| Slide Gray | `#595959` | (theme.css `p`) | Paragraph text |
| Bootstrap Ink | `#212529` | (Bootstrap) | Headings and default text |
| Link Blue | `#007bff` | (Bootstrap) | Author and inline links |
| Video Black | `#111` | (theme.css) | Video frame and video background |
| Arrow Smoke | `rgba(0,0,0,0.5)` | (theme.css) | Carousel arrows and indicator dots |
| Citation Mist | `#e9eeef` | (inline) | BibTeX panel |

## Tokens — Typography

- **Title (h1):** Philosopher (Google Fonts, 400/700 with italics). Substitute: Optima, Candara.
- **Body:** `'optima', 'Philosopher'` at `font-size: medium`. Optima renders on macOS; on other systems Philosopher is used (inferred).
- **Code:** Bootstrap mono stack, `white-space: pre-wrap`.

| Role | Size | Weight |
|---|---|---|
| Title | Bootstrap h1 2.5rem (2rem, line-height 1.2 under 768px) | bold |
| Venue (`h4`) | 1.5rem | 500 (Bootstrap h4) |
| Section heading (`h3`) | 1.75rem | 500 |
| Body | `medium` (16px) | 400 |
| Buttons (`btn-large`) | Bootstrap default 1rem | 400 |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| BibTeX panel | 15px |
| Indicator dots | 10px (active pill 7px, 25×15px) |
| Video frames, videos, comparison canvases | 5px |
| Carousel arrows | 50% (50px circles, 40px on mobile) |
| Buttons | Bootstrap `.25rem` |

**Shadows:** video frame `0 8px 24px rgba(0,0,0,0.14)`.

**Widths:** figures `min(82vw, 1020px)` (tall variant `min(76vw, 920px)`); carousel frame max 1040px; video frame 98% wide.

## Components

- **Jumbotron header:** centered, gradient background, bold two-tone title, venue `h4`, `hr`, author links with superscripts and affiliations.
- **Buttons:** `btn btn-light btn-large`, `margin: 0.2rem 0.35rem`, icons `fa-file-alt`, `fa-code`, `fa-video`, `ai-google-scholar`.
- **TL;DR:** `h3` heading with four numbered sentences.
- **Video carousel:** `.video-carousel-frame` (max 1040px) holding `.video-aspect-frame` on `#111`, 5px radius, `0 8px 24px` shadow; arrows are 50px dark translucent circles at 25px from the edges; Bootstrap indicators replaced by 15px dots.
- **Figure shell:** `.paper-figure-shell` centered, `object-fit: contain`.
- **Citation:** `pre.selectable` on `#e9eeef`, `1.5em` padding, 15px radius.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Jumbotron, two-tone Philosopher title |
| Venue badge | Yes | Gray `h4` "CVPR 2026 (Highlight)" |
| Link buttons | Yes | Arxiv, SupMat (PDF), Code, Video (YouTube), Citation (anchor) |
| Teaser | Yes | TL;DR list plus results carousel near the top |
| Abstract | Yes | `h3` section |
| Method figure | Yes | `paper-figure` |
| Results videos | Yes | Carousels for BEHAVE, InterCap, in-the-wild, generated videos, InterMimic comparison, forward/backward visualization |
| Image comparison slider / 3D / demo | No | `.comparison-canvas` rule exists but no canvas in markup |
| BibTeX | Yes | Mist panel, select-all |
| Acknowledgements | No | |

## Do's and Don'ts

- Do color the two key noun phrases of the title in two muted, low-saturation hues.
- Do frame every video in a near-black mat with a soft drop shadow.
- Do make the citation block select-all so one click copies it.
- Don't use saturated accents anywhere; the palette is grey, dusty blue and sand.

## Surfaces

Gradient grey jumbotron, white body, dark video mats, pale mist citation panel.

## Imagery

Mostly video in six `.video-carousel-frame` blocks, populated by script (inferred: the static HTML has 2 `<img>`, 0 `<video>` and no `.mp4` references), plus method and result figures.

## Layout

Bootstrap `container` / `row` / `col-12`; media up to 1020 to 1040px; text centered in the header and left-aligned in sections.

## Agent Prompt Guide

**Quick colors:** jumbotron `#f7f8fb`→`#eef2f5`, title accents `#9bb7c9` and `#c2ab97`, venue `#5a6268`, text `#595959`, mat `#111`, citation `#e9eeef`.

1. "Build a Bootstrap jumbotron header with a `#f7f8fb` to `#eef2f5` vertical gradient, a bold Philosopher h1 where one phrase is `#9bb7c9` and another `#c2ab97`, and a `#5a6268` h4 venue line."
2. "Make a video carousel frame: max 1040px, inner 98% frame on `#111`, 5px radius, shadow `0 8px 24px rgba(0,0,0,0.14)`, 50px round arrows in `rgba(0,0,0,0.5)`."
3. "Add a citation `pre` with `#e9eeef` background, 1.5em padding, 15px radius and `user-select: all`."

## Similar Pages

HSMR and other Bootstrap-4 project themes with jumbotron headers; in this collection, the only other Bootstrap page is VisCoIN.

## Quick Start

```css
:root {
  --jumbo-top: #f7f8fb; --jumbo-bottom: #eef2f5;
  --accent-blue: #9bb7c9; --accent-sand: #c2ab97;
  --venue: #5a6268; --text: #595959; --ink: #212529; --link: #007bff;
  --mat: #111; --citation: #e9eeef;
  --font-title: "Philosopher", Optima, serif; --font-body: optima, "Philosopher", sans-serif;
  --radius-media: 5px; --radius-citation: 15px;
  --shadow-media: 0 8px 24px rgba(0, 0, 0, 0.14);
}
.jumbotron { background: linear-gradient(180deg, var(--jumbo-top), var(--jumbo-bottom)); }
```

## Provenance

- **URL:** https://dingbang777.github.io/RePHO/
- **Paper:** Recovering Physically Plausible Human-Object Interactions from Monocular Videos (arXiv 2606.05359), Dingbang Huang et al.
- **Venue:** CVPR 2026; the page labels it Highlight.
- **Selection reason:** arXiv comment states acceptance at CVPR 2026 and links this page.
- **Template credit:** "adapted from the HSMR project page template and related academic project-page layouts" (footer).
- **Measurement method:** `extract_style.py` plus manual reading of theme.css and inline styles. Rendered page not viewed, so video content and carousel count are inferred from markup.
