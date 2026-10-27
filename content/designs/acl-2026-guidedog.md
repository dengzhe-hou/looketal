# GuideDog Oxblood Monograph — Style Reference

> A university-press monograph on faintly grained paper, one oxblood rule before every heading.

**Theme:** light

Measurements come from the page's own `style.css` and its Google Fonts link (Crimson Pro 400/600, italic 400). The stylesheet is tokenized in `:root`, so most hex codes are declared custom properties. Roles are interpreted from markup and comments in the CSS.

## Overview

A hand-written, framework-free page that reads like a printed paper rather than a website. A single 740px text column of 19px Crimson Pro sits on an off-white `#fdfdfc` ground with a two-layer radial-dot "paper grain". The accent is oxblood `#7a1f1f`, chosen from four declared accents (`--accent-royal`, `--accent-yonsei`, `--accent-pure-royal`, `--accent-oxblood`) through `--link: var(--accent-oxblood)`. It appears only in links, a short 1px tick before each h2, the left rule of the one-sentence gist, the S1/S2/S3 labels and a 6% tint on the "ours" table row. Figures and the comparison table break out of the column to 920/860px. Old-style figures (`onum`) in prose, lining tabular figures in stats and tables.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Oxblood | `#7a1f1f` | `--accent-oxblood` → `--link` | Links, h2 tick, gist rule, standards labels, row tint |
| Press Ink | `#1a1a1a` | `--ink` | Body text, table header rule, stats numbers |
| Laid Paper | `#fdfdfc` | `--paper` | Page background |
| Margin Grey | `#555555` | `--muted` | Venue eyebrow, affiliations, notes, captions |
| Byline Grey | `#333333` | (literal) | Author line |
| Gist Ink | `#2a2a2a` | (literal) | One-sentence summary |
| Colophon Grey | `#777777` | (literal) | Footer text |
| Deckle Rule | `#e5e3de` | `--rule` | Table rows, stats strip borders, footer rule |
| Proof Sheet | `#f5f4f0` | `--code-bg` | BibTeX background |
| Grain | `rgba(26,26,26,0.018)` / `0.012` | (literal) | 3px and 7px radial-dot paper texture |
| Royal (unused) | `#1e3a8a` | `--accent-royal` | Declared alternative accent |
| Yonsei Navy (unused) | `#003876` | `--accent-yonsei` | Declared alternative accent |
| Web Royal (unused) | `#4169e1` | `--accent-pure-royal` | Declared alternative accent |

Tints are computed with `color-mix(in srgb, var(--link) N%, …)`: 30% for link underlines, 35% for box borders, 6% for the "ours" row, 4% for the standards box.

## Tokens — Typography

- **Text:** `"Crimson Pro", Georgia, "Times New Roman", serif`, 400/600 and italic 400 from Google Fonts. Substitute: Crimson Text, EB Garamond.
- **Mono:** `"SFMono-Regular", ui-monospace, Menlo, Consolas, monospace`.
- **Features:** body `"onum", "kern", "liga"`; stats and tables `"lnum", "tnum"`.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Body | 19px (17px under 640px) | 400 | 1.65 | old-style figures |
| h1 title | 1.9rem (1.5rem mobile) | 600 | 1.25 | |
| h2 section | 1.22rem | 600 | inherit | -0.01em, oxblood tick |
| Venue eyebrow | 0.78rem | 400 | inherit | uppercase, 0.12em tracking, muted |
| Authors | 1.18rem | 400 | 1.55 | `#333` |
| Affiliations | 1.05rem | 400 italic | inherit | muted |
| Links row | 1.08rem | 400 | inherit | word-spacing 0.25em, `·` separators |
| Gist | 1.15rem | 400 | 1.55 | 2px oxblood left rule |
| Stats number / label | 1.55rem / 0.86rem italic | 600 / 400 | 1.4 | tabular |
| Table | 0.95rem (header 0.92rem) | 400 / 600 | 1.45 | |
| Caption | 0.95rem italic | 400 | 1.55 | muted, left |
| BibTeX | 0.8rem mono | 400 | 1.5 | |
| Footer | 0.8rem | 400 | inherit | `#777` |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Standards box | 3px |
| BibTeX `pre` | 2px |
| Everything else | 0 |

- **Shadows:** none.
- **Layout:** `main.page` max-width 740px, padding 4rem 1.25rem 6rem; `figure.wide` 920px, `figure.medium` 780px, `.table-wrap` 860px, all centered by `margin-left: 50%; transform: translateX(-50%)`.
- **Rhythm:** h2 margin 2.6rem 0 0.7rem; figures 2rem vertical; footer 4rem above.

## Components

- **Title block.** Venue eyebrow "ACL 2026 Main" in small caps-like uppercase, h1, authors with symbol superscripts (♣ ♢ ♡ ♠), italic affiliations, note line, then a text link row "PDF · arXiv · Code · Data · BibTeX".
- **Link.** Oxblood text, 1px underline at 30% oxblood via `border-bottom`, full oxblood on hover. Author links have no underline until hover.
- **Gist.** One-paragraph summary with a 2px oxblood left border and 1rem left padding.
- **Stats strip.** Four-column grid (two on mobile) between top and bottom `#e5e3de` rules; big tabular number over an italic muted label (22,084 pairs, 2,106 gold, 818 QA, 46/183 countries/locations).
- **Comparison table.** Booktabs-like: ink 1px rule under the header, `#e5e3de` row rules, "ours" row tinted 6% oxblood; on mobile it scrolls horizontally with a sticky first column and a right-edge fade mask.
- **Standards box.** Echoes the paper's tcolorbox: 1px border at 35% oxblood, 4% tint fill, 3px radius, S1/S2/S3 labels in oxblood 600.
- **Takeaway.** Italic 1.05rem line under a top rule.
- **BibTeX.** `#f5f4f0` block, 2px radius, mono 0.8rem.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Left-aligned, serif |
| Venue badge | Text eyebrow | Uppercase 0.78rem muted "ACL 2026 Main" |
| Link buttons | PDF, arXiv, Code, Data (HF dataset), BibTeX anchor | Inline text links with `·`, not buttons |
| Teaser figure | Yes | Wide figure with italic caption |
| Abstract | As a "gist" section | Plain paragraph plus teaser |
| Stats | Yes | Four-number strip |
| Results table | Dataset comparison table | Booktabs style with highlighted row |
| Method / findings | Standards box, QA figure, numbered findings | Callout boxes |
| Video / sliders / 3D / HF demo | No | |
| BibTeX | Yes | Proof-sheet `pre` |
| Acknowledgements | No | Footer links to the GitHub source |

## Do's and Don'ts

- Do keep one accent and derive every tint from it with `color-mix`.
- Do use old-style figures in prose and lining tabular figures in numbers.
- Do let figures and tables break out of the 740px column instead of widening the column.
- Don't use buttons or pills; links are text separated by middots.
- Don't add shadows or rounded cards; the page is flat print.

## Surfaces

One surface: grained `#fdfdfc` paper. Tinted boxes and the `#f5f4f0` code block are the only fills.

## Imagery

A teaser figure and a QA-task figure, both static PNG/JPG with italic captions. No video.

## Layout

Single left-aligned reading column with breakout figures. Breakpoints at 920, 860, 780 and 640px collapse breakouts and shrink type.

## Agent Prompt Guide

**Quick colors:** paper `#fdfdfc`, ink `#1a1a1a`, muted `#555555`, rule `#e5e3de`, code `#f5f4f0`, accent `#7a1f1f`.

1. "Write an h2 in Crimson Pro 600 at 1.22rem with a 0.7em-wide, 1px `#7a1f1f` tick before it, vertically aligned at 0.32em and 0.55em to its right."
2. "Make a four-cell stats strip between 1px `#e5e3de` rules: 1.55rem/600 tabular numbers in `#1a1a1a` over 0.86rem italic `#555555` labels; two columns under 640px."
3. "Build a comparison table with an ink header rule, `#e5e3de` row rules and the 'ours' row filled with `color-mix(in srgb, #7a1f1f 6%, transparent)`."

## Similar Pages

LaMI (ACL 2026) in this batch is the other serif-led, framework-free page, though with button links and a blue accent.

## Quick Start

```css
:root {
  --ink: #1a1a1a; --paper: #fdfdfc; --muted: #555555;
  --rule: #e5e3de; --code-bg: #f5f4f0;
  --accent-oxblood: #7a1f1f; --link: var(--accent-oxblood);
  --font: "Crimson Pro", Georgia, "Times New Roman", serif;
  --mono: "SFMono-Regular", ui-monospace, Menlo, Consolas, monospace;
  --measure: 740px; --wide: 920px;
}
body { font: 19px/1.65 var(--font); color: var(--ink); background: var(--paper);
  font-feature-settings: "onum", "kern", "liga"; }
```

## Provenance

- **URL:** https://jun297.github.io/GuideDog/
- **Paper:** GuideDog: A Real-World Egocentric Multimodal Dataset for Blind and Low-Vision Accessibility-Aware Guidance (arXiv 2503.12844), Junhyeok Kim, Jaewoo Park et al. (Yonsei University, LG AI Research, Euler Robotics, Seoul National University).
- **Venue:** ACL 2026 (page eyebrow reads "ACL 2026 Main").
- **Selection reason:** the arXiv comment states ACL 2026 acceptance and links this page.
- **Template credit:** none named; footer says "Project page source on GitHub. Template free to fork." Custom build.
- **Measurement method:** `extract_style.py` plus a full read of `style.css`. The rendered page was not viewed, so the paper-grain texture and breakout widths are read from CSS, not seen.
