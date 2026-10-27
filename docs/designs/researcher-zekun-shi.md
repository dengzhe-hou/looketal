# Zekun Shi — Style Reference

> A terminal prompt that learned to write in Roman capitals.

**Theme:** both (light default, dark toggle)

Measurements are normalized from the static HTML and the three theme stylesheets (`terminal-0.7.4.min.css`, `animate-4.1.1.min.css`, `console.css`); roles are interpreted. The theme's own light and dark variables are taken from `console.css`, which overrides terminal.css defaults.

## Overview

A Hugo site using the hugo-theme-console theme on top of terminal.css. The header is a prompt: the site name renders as `~ /` with a blinking cursor, followed by a lowercase menu (poster, posts, software, publication) and a sun or moon emoji button that flips `data-theme`. The home page itself is very short: a waving-hand intro paragraph naming NUS, the advisor and Sea AI Lab, a second paragraph on ML and electronic structure, then "Latest posts" showing one dated entry on the Stochastic Taylor Derivative Estimator. The unusual move is the type: the body stack is `Marcellus, JetBrains Mono`, so prose is set in an inscriptional Roman display face while code and tables fall back to mono. Links are a neutral grey (#727578) that invert to a solid grey block on hover, terminal style. TikZJax is loaded so posts can render TikZ figures, and dark mode inverts them.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Snow Paper | #fefffe | `--background-color` (light) | Page background |
| Carbon Ink | #000101 | `--font-color` (light) | Body text |
| Console Grey | #727578 | `--primary-color` (light) | Links and hover block fill; also `--secondary-color` |
| Invert White | #fefffe | `--invert-font-color` (light) | Link text on hover |
| Code Mist | #e8eff2 | `--code-bg-color` (light) | Code background variable |
| Soft Coral | #ff6d7f | `--error-color` (light) | Error color |
| Gauge Graphite | #3d4143 | `--progress-bar-fill` (light) | Progress bars |
| Void | #010100 | `--background-color` (dark) | Dark background |
| Moon White | #fefffe | `--font-color` (dark) | Dark text |
| Steel Haze | #a3abba | `--primary-color` (dark) | Dark links |
| Neon Rose | #ff3c74 | `--error-color` (dark) | Dark error |
| Signal Cyan | #62c4ff | `--progress-bar-fill` (dark) | Dark progress fill |
| Muted Copy | #666666 | none | Paragraphs inside `.content-column-content` |

## Tokens — Typography

- **Primary:** `Marcellus, JetBrains Mono` (self-hosted TTFs in the theme). Marcellus is a flared Roman display face and is also on Google Fonts; the nearest substitute with lowercase is Forum.
- **Mono:** `Inconsolata, JetBrains Mono` for code; tables are forced to JetBrains Mono 14px.
- **Math/figures:** TikZJax fonts (cmb10, cmbsy10 and so on) load for TikZ diagrams.
- **Weights:** 400 text; 600 headings from terminal.css; bold for strong.

| Level | Element | Size | Line height | Notes |
|---|---|---|---|---|
| Base | body | 16px (14px under 850px) | 1.6em | `--global-font-size` |
| h1 | h1 | 1.2em !important | 1.6em | terminal h1 is table-cell, weight 600 |
| Post title | `.post h2` | terminal default (inferred 1em) | | linked |
| Date | `.posts-list .date` | inherit | | absolute 130px left gutter, hidden under 850px |
| Table | table, `table strong` | 14px | | JetBrains Mono |
| Menu | `.terminal-menu li` | inherit | | 30px right margin (20px on phones) |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| Square | 0 | Links, ghost buttons, blocks |
| Button | 5px | Theme toggle button |

- **Shadows:** none; `box-shadow` reset on masonry boxes.
- **Layout max-width:** `--page-width: 60em` (70em in the root fallback).
- **Spacing unit:** terminal.css `--global-space: 10px`; paragraphs get 20px vertical margins.
- **Posts list:** `padding-left: 130px` with the date absolutely positioned in that gutter.

## Components

- **Prompt logo.** Role: site name. `.logo.terminal-prompt` showing `~ /`; `::after` blinks a 10px cursor via the `cursor` animation; `::before` prompt glyph removed.
- **Menu.** Role: top navigation. Horizontal lowercase list; stacks under the logo below 850px.
- **Theme toggle.** Role: light or dark. A `<button>` with `content: "\1F315"` (sun) in light and `"\1F319"` (moon) in dark, 10px 15px padding, 5px radius; choice stored in `localStorage`.
- **Link.** Role: inline links. Grey text; on hover the whole link becomes a filled grey block with white text, like a selected terminal cell.
- **Post list item.** Role: latest posts. Date in the left gutter ("Jan. 13, 2025"), linked h2 title, italic one-line description.
- **Page entry animation.** Role: polish. Main container uses animate.css `zoomIn fast`.

## Page Modules

- **Title/author block:** prompt-style logo and menu only; the person's name appears in the first sentence of the intro.
- **Bio/photo:** two text paragraphs, no photo.
- **News:** "Latest posts" list (one post on the home page).
- **Publication list, software, poster:** separate pages in the menu.
- **Math rendering:** TikZJax script for TikZ figures in posts.
- **Venue badge, link buttons, BibTeX, awards, contact block:** not on the home page.

## Do's and Don'ts

- Do keep the whole UI lowercase and prompt-like (`~ /`, lowercase menu).
- Do use the invert-on-hover link treatment instead of underlines.
- Do pair a Roman display face for prose with a mono face for code and tables.
- Don't add colored accents in light mode; the palette is greyscale by design.
- Don't round corners except the toggle button.
- Don't put a photo or hero image on the home page; it is text first.

## Surfaces

One flat page surface per theme (near-white or near-black). No cards. Code blocks sit on the background color in this theme override.

## Imagery

None on the home page. Posts may include TikZ-rendered SVG figures, which are color-inverted in dark mode.

## Layout

Single centered column up to 60em. Nav is a flex row of logo and menu that stacks under 850px, where the posts' date gutter also disappears.

## Agent Prompt Guide

**Quick colors:** light bg #fefffe, text #000101, link #727578, hover text #fefffe on #727578; dark bg #010100, text #fefffe, link #a3abba.

1. "Build a terminal-style header: a logo reading `~ /` with a blinking 10px block cursor, followed by a lowercase horizontal menu with 30px gaps and an emoji theme toggle button (sun in light, moon in dark) with 5px radius."
2. "Style links like terminal selections: color #727578, no underline; on hover fill the link background with #727578 and turn the text #fefffe."
3. "Create a posts list with a 130px left gutter holding the date, a linked post title, and an italic one-line summary; hide the date column under 850px. Use Marcellus for prose and JetBrains Mono for code."

## Similar Pages

- [Kenji Kawaguchi](https://people.csail.mit.edu/kawaguch/), his advisor in this batch, for a plain HTML contrast.
- [Akbir Khan](https://akbir.dev/) for another minimal text-first page.

## Quick Start

```css
:root, [data-theme="light"] {
  --background-color: #fefffe;
  --font-color: #000101;
  --invert-font-color: #fefffe;
  --primary-color: #727578;
  --secondary-color: #727578;
  --code-bg-color: #e8eff2;
  --error-color: #ff6d7f;
  --font-stack: Marcellus, "JetBrains Mono";
  --mono-font-stack: Inconsolata, "JetBrains Mono";
  --global-font-size: 16px;
  --global-line-height: 1.6em;
  --page-width: 60em;
}
[data-theme="dark"] { --background-color: #010100; --font-color: #fefffe; --invert-font-color: #222225; --primary-color: #a3abba; --error-color: #ff3c74; }
body { font: var(--global-font-size)/var(--global-line-height) var(--font-stack); color: var(--font-color); background: var(--background-color); }
a { color: var(--primary-color); text-decoration: none; }
a:hover { background: var(--primary-color); color: var(--invert-font-color); }
```

## Provenance

- **URL:** https://zekun-shi.github.io/
- **Venue/award:** NeurIPS 2024 Best Paper (first author of "Stochastic Taylor Derivative Estimator"), per https://blog.neurips.cc/2024/12/10/announcing-the-neurips-2024-best-paper-awards/ (authors from arXiv 2412.00088)
- **Selection reason:** Rule B.
- **Template credit:** hugo-theme-console (served from `/hugo-theme-console/`) built on terminal.css 0.7.4; Hugo 0.128.0 generator tag.
- **Measurement method:** variables and rules read from `console.css`, `terminal-0.7.4.min.css` and the static HTML via `extract_style.py` and curl. Not rendered in a browser; the Marcellus look is inferred from the font-family declaration and the bundled TTF, not observed.
