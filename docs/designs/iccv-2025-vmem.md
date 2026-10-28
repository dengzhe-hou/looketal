# VMem — Style Reference

> An Oxford reading room on white: Roboto Light text, Oxford-blue links and square outlined buttons, with a playable before/after demo set like three framed prints.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, a probe of rendered elements further down the page (thumbnail strip, buttons, BibTeX, footer, paper overlay), and the page's `css/style.oxfordblue.css` (the Bootstrapious "Universal" Bootstrap 4 theme in its Oxford-blue variant), `css/custom.css`, inline `<style>` and `index.html`. Clicking a thumbnail swaps the three demo media by script; the render shows the default cloister scene.

## Overview

A plain white Bootstrap page (about 3,700px tall) from the Bootstrapious Universal template. The header is centred: a rainbow-striped "VMem" logo image set inline before a 32px bold Roboto title, underlined Oxford-blue (#002147) author links in Roboto Light 20px, "University of Oxford", and a bold "In ICCV 2025 ⭐highlight⭐" line with the word "highlight" in pure red. The first-viewport showpiece is a three-column comparison (Input image / Generated video (without VMem) in orange / (with VMem) in green), each 340×255 with 4px radius and a small shadow, two of them carrying a gamepad badge, above a pale gray thumbnail strip with a yellow-bordered active scene. A left-aligned 20px Roboto Light abstract with bold key phrases and a row of square outlined uppercase buttons (PAPER, CODE, DEMO, BIBTEX) follow. Below, left-aligned h2 sections (Quick Explanation video, Approach and Surfel-Indexed View Memory figures with light paragraphs, Paper montage with a hover overlay), an unstyled BibTeX `pre`, and a one-line right-aligned footer credit.

## First Viewport

Color share (quantized 1440×900 shot): white #ffffff 60.5% (plus #fffffd 2.7%, #feffff 1.5%); #eaebea 7.4% is the thumbnail strip and light stone in the images; the cloister photographs supply dark brown #2d261b 8.1%, ochre #543e1b 6.7%, olive gray #645c45 6.4% and stone #9e9e95 6.8%.

Anatomy in DOM order (desktop 1440px; Bootstrap `.container` 1140px at x=150, content x=165 to 1275):

1. **Section padding**: `section.bar.padding-small` padding 20px 0, so the header starts at y=20.
2. **Title** (`header.heading-light` > `h1`, y=20–111): Roboto 32px/700, line-height 1.1, #212529, centred, two lines. The logo `img` (70px tall = 2.2em, margin-top -0.46em, box y=5) sits inline before ": Consistent Interactive…". Gap 30px (`.mb-medium`).
3. **Authors** (`p.lead.text-md-center`, y=141–201): Roboto 20px/300, line-height 1.5, #212529; names are links in #002147 with underlines; "University of Oxford" on the second line. Gap 20px.
4. **Venue** (`p.lead`, y=221): "In ICCV 2025 ⭐highlight⭐" in `strong` (renders 500), the highlight span `color: red` (#ff0000). Gap 20px.
5. **Column labels** (`h5`, y=271): 16px/700 #212529, centred; "(without VMem)" in rgb(255,94,0) #ff5e00, "(with VMem)" in green #008000. Gap 16px.
6. **Media row** (y=304–559): three 340×255 items at x=180, 550 and 920 (`img/video.img-fluid.rounded.shadow-sm`: 4px radius, `0 2px 4px rgba(0, 0, 0, 0.075)`); a 64×48 gamepad badge overhangs the bottom-right of each video by 10px down and 20px right. Bottom margin 24px (`.mb-4`).
7. **Thumbnail strip** (`#thumbnailCarousel`, y=566–678, x=417, 605px wide): #f8f9fa, padding 16px, 4px radius, five 80px-tall thumbnails with 1px #dee2e6 borders and 4px radii; the active one bordered #ffc107. Gap 24px.
8. **Abstract** (`p.lead`, y=702–912): Roboto 20px/300, line-height 1.5, #212529, left-aligned in the 1080px column, key phrases in `strong` 500. It crosses the fold; the button row follows at y=957.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Body Ink | #212529 | Bootstrap body color | title, headings, lead paragraphs, labels, BibTeX |
| Oxford Blue | #002147 | theme primary (link color) | author links, outlined button text and border, button hover fill |
| Link Hover | #2f5a89 | `a:hover` | hovered links |
| Highlight Red | #ff0000 | (inline `color: red`) | "⭐highlight⭐" in the venue line |
| Without Orange | #ff5e00 | (inline rgb(255,94,0)) | "(without VMem)" label |
| With Green | #008000 | (inline `color: green`) | "(with VMem)" label |
| White | #ffffff | `.bg-white` | page, sections, footer |
| Strip Gray | #f8f9fa | Bootstrap `.bg-light` | thumbnail strip |
| Thumb Border | #dee2e6 | Bootstrap `.border` | inactive thumbnails |
| Active Yellow | #ffc107 | Bootstrap `.border-warning` | active thumbnail border |
| Footer Gray | #495057 | (custom.css `.copyrights`) | footer text |
| Footer Link | #44687d | (custom.css) | "Bootstrapious Templates" link |
| Overlay Blue | rgba(70,127,191,0.6) | `.box-image .overlay` | hover overlay on the paper montage |
| Spinner | #f3f3f3 / #007bff | (inline `.spinner`) | 40px loading ring (gray track, blue top) shown while demo videos load |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text | Roboto, Helvetica, Arial, sans-serif | Roboto 300, 400, 700 (Google Fonts) | Roboto |
| Code | SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace | Consolas on Windows | JetBrains Mono |
| Icons | Font Awesome 4 | FontAwesome | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1` (custom.css `font-size: 2rem`) | 32px / 700 / 1.1 | #212529 |
| Section title | `h2` | 1.8rem = 28.8px / 700 / 1.1, left | #212529 |
| BibTeX heading | `h3` | 24px / 700 | #212529 |
| Column label | `h5` | 16px / 700 | #212529 |
| Lead text (authors, abstract, section paragraphs) | `p.lead` | 20px / 300 / 1.5 | #212529; strong 500 |
| Body | `body` | 16px / 400 / 1.5 | #212529 |
| Button | `.btn.btn-template-outlined` | 12.8px / 700, uppercase, letter-spacing 0.1em | #002147 |
| BibTeX | `pre` | 14px / 1.5 monospace | #212529 |
| Footer | `.copyrights p` | 12.8px | #495057 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Demo images and videos (`.rounded.shadow-sm`) | 4px | none | `0 2px 4px rgba(0, 0, 0, 0.075)` |
| Thumbnail strip | 4px | none | none |
| Thumbnails | 4px | 1px #dee2e6; active 1px #ffc107 | none |
| Outlined buttons | 0 (`!important`) | 1px #002147 | none |
| Section video and figures | 0 | none | none |
| Paper montage (`.box-image`) | 0 | none | none; hover overlay rgba(70,127,191,0.6) |
| BibTeX `pre` | 0 | none | none (no background) |

## Layout Metrics

- **Container**: Bootstrap `.container` max-width 1140px at ≥1200px (x=150), 15px padding, so content runs x=165 to 1275 (1110px). The demo uses a nested `.container` inside `.col-md-12`, which brings its columns to x=180 to 1260 (three `.col-md-4` of 360px, media 340px wide).
- **Sections**: `section.bar.padding-small` padding 20px 0 (the template's `.bar` default is 60px; every section here uses the small variant); a final empty `.padding-big` filler (50px) pushes the footer down.
- **Header**: title margin-bottom 30px; `.lead` margin-bottom 20px; column labels margin-bottom 16px; media row margin-bottom 24px.
- **Section video**: Quick Explanation video spans the full 1110px (624px tall).
- **Buttons**: inline in a `p.buttons.lead`, 3px margins, padding 8px 12px, 37px tall.
- **Footer**: `.copyrights` padding 30px 0, text right-aligned in `.col-lg-8`.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1200px | 15px in a 1140px container | 16px (lead 20px) | 32px | three demo columns |
| 992–1199px | 960px container | same | 32px | same; footer columns still split |
| 768–991px | 720px container | same | 32px | demo columns still three across (`col-md-4`); footer text centred (`.text-center-md`) |
| ≤767px | 540px container / full width with 15px | same | 32px | demo columns stack; `.text-md-center` author lines turn left-aligned |

## Components

- **Outlined button** (`.btn.btn-template-outlined`): transparent, 1px #002147 border, square corners (`border-radius: 0 !important`), #002147 12.8px/700 uppercase with 0.1em tracking, padding 8px 12px, 3px margin; an inline Font Awesome or Hugging Face logo before the label. Hover: #002147 fill, white text; transition all 0.3s.
- **Comparison column**: centred h5 label with a colored parenthetical, then a 4px-radius media item with `shadow-sm`; a gamepad PNG badge absolutely positioned at bottom -10px, right -20px.
- **Thumbnail strip**: `d-flex flex-wrap justify-content-center gap-2 py-3 px-3 bg-light rounded`, centred at its own content width; 80px-tall thumbnails, active one with a #ffc107 border; a 40px spinner (#f3f3f3 ring, #007bff top) shows while videos load.
- **Section**: left-aligned h2 28.8px/700, 16px margin-bottom, then a full-width figure or video and `p.lead` paragraphs at 20px/300.
- **Paper montage**: full-width image link; on hover a rgba(70,127,191,0.6) overlay fades in with a white outlined "ARXIV PREPRINT" button (`.btn-template-outlined-white`).
- **BibTeX**: bare `pre`, no background or padding, 14px monospace.
- **Links**: underlined everywhere (custom.css), #002147, hover #2f5a89.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Logo + title | yes | rainbow "VMem" image inline before a 32px bold title |
| Authors / affiliation | yes | centred Roboto Light 20px, underlined Oxford-blue links |
| Venue line | present but non-standard | bold text with a red "⭐highlight⭐" span, no badge |
| Interactive demo | yes | input / without / with columns plus a thumbnail scene picker |
| Abstract | present but non-standard | an untitled 20px lead paragraph under the demo |
| Link buttons | yes | four square outlined uppercase buttons, placed after the abstract |
| Explanation video | yes | full-width `<video>` |
| Method figures | yes | Approach and memory diagrams with lead paragraphs |
| Paper preview | yes | montage image with hover overlay |
| BibTeX | yes | unstyled `pre` with two entries |
| Results tables | absent from the source | — |
| Footer | yes | right-aligned 12.8px template credit |

## Adapting to Other Content

- **More authors**: keep the centred `p.lead` at 20px/300 with underlined #002147 links; it wraps within 1110px, about eight names per line.
- **A results table**: use a Bootstrap `table` in the 1110px column at 16px #212529 with 1px #dee2e6 rules, header 700; best values in 700, no colored fills. Put it in its own `section.bar.padding-small` with a left-aligned h2.
- **Long publication or news lists**: `p.lead` items at 20px/300 with bold 500 dates, or a `ul` in 16px; links underlined #002147.
- **More buttons**: add more `.btn-template-outlined` buttons to the same row; keep them square and uppercase.
- **Centre or left**: the header and demo are centred, sections are left-aligned; keep that split rather than mixing within a section.

## Do's and Don'ts

- Do keep Roboto Light 20px for all reading text and 700 only for headings.
- Do use #002147 for links and outlined buttons, with square corners.
- Do label comparisons with colored parentheticals (#ff5e00 without, #008000 with) and nothing else colored.
- Do keep media corners at 4px with the faint `shadow-sm`.
- Don't add background bands; every section is white with 20px vertical padding.
- Don't round the buttons.
- Don't style the BibTeX block beyond the default `pre`.

## Surfaces

All white. The only tinted surface is the #f8f9fa thumbnail strip; the paper montage gains a blue overlay on hover.

## Imagery

Photographs of real places (an Oxford cloister, an office, a Chinese gate, the Forbidden City, a quad) as input frames and generated walk-through videos; a narrated explanation video; black-and-white line diagrams of the surfel memory with colored camera frustums; a playful rainbow logo and gamepad badges.

## Layout

A single 1110px Bootstrap column. The header and demo are centred; everything after the abstract is left-aligned and stacked with only 40px between sections (20px padding each). Content is dense and plain.

## Agent Prompt Guide

Quick colors: ink #212529, Oxford blue #002147, link hover #2f5a89, strip #f8f9fa, thumb border #dee2e6, active #ffc107, highlight #ff0000, without #ff5e00, with #008000, footer #495057.

1. "Build a centred header in a 1140px Bootstrap container, section padding 20px 0: a 70px-tall logo image inline before a Roboto 32px/700 #212529 title; 30px gap; authors in Roboto 20px/300 with underlined #002147 links; a bold venue line with a red #ff0000 '⭐highlight⭐'."
2. "Make a three-column demo: centred 16px/700 labels ('(without …)' in #ff5e00, '(with …)' in #008000), 340×255 media with 4px radius and box-shadow 0 2px 4px rgba(0,0,0,0.075); below, a centred #f8f9fa strip (16px padding, 4px radius) of 80px thumbnails with 1px #dee2e6 borders, the active one #ffc107."
3. "Create square outlined buttons: transparent, 1px #002147 border, radius 0, Roboto 12.8px/700 uppercase, letter-spacing 0.1em, #002147 text, padding 8px 12px, 3px margins; hover fills #002147 with white text."

## Similar Pages

- Oxford VGG project pages built on the Bootstrapious Universal template (Oxford-blue variant).
- Pages that lead with an interactive before/after video demo instead of a teaser figure.

## Quick Start

```css
:root {
  --ink: #212529;
  --oxford: #002147;
  --link-hover: #2f5a89;
  --strip: #f8f9fa;
  --thumb-border: #dee2e6;
  --active: #ffc107;
  --footer-text: #495057;
  --font: Roboto, Helvetica, Arial, sans-serif;
  --container: 1140px;
  --lead-size: 20px;
  --lead-weight: 300;
  --media-radius: 4px;
  --media-shadow: 0 2px 4px rgba(0, 0, 0, 0.075);
}
```

## Provenance

- **URL**: https://v-mem.github.io/
- **Paper**: VMem: Consistent Interactive Video Scene Generation with Surfel-Indexed View Memory (arXiv 2506.18903), Runjia Li, Philip Torr, Andrea Vedaldi, Tomas Jakab (University of Oxford).
- **Venue**: ICCV 2025 (Highlight, as stated on the page).
- **Selection reason**: the arXiv comment states acceptance at ICCV 2025 and links this project page.
- **Template credit**: Bootstrapious "Universal" Bootstrap 4 theme, Oxford-blue variant (footer: "Template design by Bootstrapious Templates").
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, a rendered-element probe of the lower page, and `style.oxfordblue.css`, `custom.css`, the inline style and `index.html` read directly, on 2026-10-28.
