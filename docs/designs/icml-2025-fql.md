# FQL Berkeley Lecture Notes — Style Reference

> A clear lecture handout on flow policies, set in Source Sans at 18px.

**Theme:** light

Values come from the static HTML, the author's site-wide `stylesheet.css`, the project's `css/app.css`, and Bootstrap 3.3.5 (loaded twice, from CDN and locally). Bootstrap's contextual palette (`#3c763d`, `#a94442`, the Cosmo-like `#2780e3`/`#ff7518` swatches) appears in the frequency count but is not used by the markup. Measurements are normalized; roles are interpreted.

## Overview

FQL is a Bootstrap 3 grid page in the Michaël Gharbi / Jon Barron tradition: no hero band, no buttons, no cards. A 64px bold title, three authors with affiliation under each name in an inline list, and two light h3 text links ("Paper", "Code") lead into a looping teaser video at 8/12 width. The body is a sequence of large weight-300 h1 section heads (Overview, Challenge, Idea, Algorithm, Experiments, Citation) with 18px Source Sans 3 text, MathJax equations (with a gray `plgray` macro for secondary symbols), highlight.js code on `#f6f8fa`, and Bootstrap collapses ("Click to see the full table (73 tasks)") that hide long results. One soft blue `#598be7` serves for links.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Berkeley Link Blue | `#598be7` | `a`, `.text-blue` | Links, collapse toggles, blue text helper |
| Link Hover | `#9bb9f1` | `a:hover` | Link hover and active |
| Statement Wash | `#dee8fa` | `.block-statement` | Defined callout fill with 2px `#598be7` border (not used on this page) |
| Alert Red | `#f54254` | `.text-red` | Defined red text helper (not used on this page) |
| Bootstrap Ink | `#333333` | Bootstrap `body` | Body and heading text |
| Paper White | `#ffffff` | Bootstrap `body` | Page background |
| Code Gray | `#f6f8fa` | `.codebox-pre`, `.codebox-code` | Code block background (GitHub highlight theme) |
| Math Gray | `RGB(153,153,153)` | MathJax `plgray` macro | De-emphasized symbols in equations (≈ `#999999`) |
| Author Black | `#000000` | `.author-link` | Defined for author links on the home site (inferred unused here) |

## Tokens — Typography

- **Sans (everything):** `'Source Sans 3', 'Lato', Verdana, Helvetica, sans-serif`, loaded as a variable woff2 (300–700) in `stylesheet.css`. Substitute: Source Sans Pro.
- **Mono:** `'Source Code Pro'` (Google Fonts import) for code and `.text-tt`.
- **Math:** MathJax.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Title (`.text-title`) | 64px (44px ≤991px) | 700 | Centered |
| Section h1 | 48px (40px ≤991px) | 300 | margin 30px top / 20px bottom |
| h2 | Bootstrap 30px | 300 | margin-top 30px |
| h3 (links, toggles) | 24px | 400 | `.text-toplink` for Paper/Code |
| h4 | 20px | 400 | |
| Body, td, p, a | 18px (16px ≤991px) | 400 | Bootstrap line-height 1.42857 |
| Captions (`.text-caption`) | 20px | 400 | block, centered |
| Code block | 17px | 400 | |
| `.text-tt` method tokens | inherits | 400 | Source Code Pro |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Statement callout | 10px |
| Bootstrap code / wells | 4px |
| Video, images | 0 |

- **Shadows:** none.
- **Spacing helpers:** `.top0/5/7/10/15/17/20/30` and `.bottom0…30` utility classes in px.
- **Layout:** Bootstrap `.container` (1170px at ≥1200px); teaser at `col-md-8 col-md-offset-2`; link row at `col-md-4 col-md-offset-4`; text full `col-md-12`; task images in `col-md-2 col-xs-6` cells.

## Components

- **Author row.** `ul.list-inline` centered; each `li` holds a linked name, `<br>`, and the affiliation.
- **Text link row.** Two h3 `.text-toplink` headings wrapped in links, weight 400, no icons, no button chrome.
- **Section head.** Weight-300 48px h1, the page's main rhythm marker.
- **Collapse toggle.** An h3 link with `data-toggle="collapse"` ("Click to see the full algorithm", "…full table (73 tasks)") that reveals an image or code block.
- **Code box.** highlight.js GitHub theme in `pre.codebox-pre` on `#f6f8fa`, Source Code Pro 17px, no border.
- **Equation block.** Centered `.text-equation` at 110%, with separate desktop and mobile versions toggled by `.desktop-only` / `.mobile-only` at 992px.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | 64px bold title, inline author list |
| Venue badge | No | Venue appears only in the BibTeX `booktitle` |
| Link buttons | Paper, Code | Plain h3 text links |
| Teaser video | Yes, autoplay loop | 8/12-width, no frame |
| Abstract | Bulleted "Overview" instead | Bold lead-ins |
| Method | Challenge, Idea, Algorithm (with collapsible full algorithm) | Prose plus MathJax |
| Results | Tasks gallery (7 videos), offline RL and offline-to-online tables as collapsible images, speed and hyperparameter Q&A | |
| Tables / sliders / 3D / HF | No HTML tables | |
| BibTeX | "Citation" section | Code box |
| Acknowledgements | Template credit line only | |

## Do's and Don'ts

- Do write section heads as light 48px h1s and let whitespace carry the structure.
- Do hide long tables behind a collapse toggle phrased as "Click to see…".
- Do gray out secondary math symbols with a MathJax color macro.
- Don't add buttons, badges or cards; links are plain text.
- Don't mix in Bootstrap's contextual colors; only `#598be7` is used.

## Surfaces

White page, gray `#f6f8fa` code blocks. Nothing else.

## Imagery

Looping videos of locomotion and manipulation tasks (OGBench-style environments), algorithm and table screenshots as images.

## Layout

Bootstrap 12-column grid, mostly full-width rows; centered title, link row and teaser; left-aligned prose.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, text `#333333`, link `#598be7`, hover `#9bb9f1`, code `#f6f8fa`, math gray `#999999`.

1. "Set the page in Source Sans 3 at 18px with `#333` text; section heads are 48px weight-300 h1s with 30px top and 20px bottom margin."
2. "Create the header: a centered 64px/700 title, an inline list of authors each with the affiliation on a second line, and a centered row of two 24px h3 text links 'Paper' and 'Code' in `#598be7`."
3. "Make a collapsible results block: an h3 link 'Click to see the full table (73 tasks)' that toggles a hidden image using Bootstrap's collapse."

## Similar Pages

Seohong Park's other project pages (shared `../../stylesheet.css`), and pages derived from Jon Barron's and Michaël Gharbi's minimal templates.

## Quick Start

```css
:root {
  --text: #333333; --bg: #ffffff;
  --link: #598be7; --link-hover: #9bb9f1;
  --code-bg: #f6f8fa; --math-gray: #999999;
  --font-sans: "Source Sans 3", "Lato", Verdana, Helvetica, sans-serif;
  --font-mono: "Source Code Pro", Menlo, monospace;
  --fs-body: 18px; --fs-h1: 48px; --fs-title: 64px;
}
body { font-family: var(--font-sans); font-size: var(--fs-body); color: var(--text); }
h1 { font-weight: 300; font-size: var(--fs-h1); margin: 30px 0 20px; }
```

## Provenance

- **URL:** https://seohong.me/projects/fql/
- **Paper:** Flow Q-Learning (arXiv 2502.02538), Seohong Park, Qiyang Li, Sergey Levine.
- **Venue:** ICML 2025 (BibTeX `booktitle={International Conference on Machine Learning (ICML)}`).
- **Selection reason:** arXiv comment states acceptance at ICML 2025; project page linked in the arXiv abstract.
- **Template credit:** footer says the template "was partly borrowed from Michaël Gharbi and Jon Barron".
- **Measurement method:** `extract_style.py` plus manual reading of `stylesheet.css` and `app.css`; Bootstrap defaults (such as `#333` body text and the 1170px container) are taken from Bootstrap 3.3.5 conventions. Rendered page not viewed.
