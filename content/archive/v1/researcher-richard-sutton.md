# Sutton Incomplete Ideas — Style Reference

> A thinker's index card, typed once and amended for thirty years.

**Theme:** light

Measurements come from the page's static HTML: one inline `<style>` block (a single Dreamweaver-style `.style1` class) and a handful of inline `style` attributes. There is no external stylesheet and no framework, so nothing needed filtering. Colors not declared anywhere are browser defaults and marked inferred. Roles are interpreted, not declared by the author. The rendered page was not viewed.

## Overview

Rich Sutton's home page at incompleteideas.net is an unstyled document in the browser's default look. The only typographic decision is the name: an `<h2 class="style1">` set in `Verdana, Helvetica, sans-serif`, which stands out against the default serif body. Under it come stacked affiliation lines (Oak Lab, University of Alberta, Canada CIFAR AI Chair, Amii, Openmind), an address block, a media contact, then a long first-person paragraph about his roles. Further down are lists of links to the RL book, the RL FAQ, talks, publications, Google Scholar and a run of short essays (The Bitter Lesson, Verification, What's Wrong with AI, the Turing speech). A 2px full-width `<hr>` separates the header from the body. A head photo and the RLAI book cover are inline images, one floated right at 200px wide.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Default Paper | `#ffffff` (inferred) | `--bg` | Browser default background; `<body>` has no attributes |
| Default Ink | `#000000` (inferred) | `--text` | Body text |
| Hyperlink Blue | `#0000ee` (inferred) | `--link` | Browser default unvisited link |
| Visited Purple | `#551a8b` (inferred) | `--link-visited` | Browser default visited link |
| Rule Grey | browser default (inferred) | `--rule` | `<hr style="width:100%; height:2px">` |

No hex color is declared anywhere on the page; the table is a description of the browser defaults the page relies on.

## Tokens — Typography

- **Name:** `Verdana, Helvetica, sans-serif` (`.style1`). Substitute: `Tahoma`, `DejaVu Sans`.
- **Body:** browser default serif (inferred Times New Roman). Substitute: `Tinos`, `Liberation Serif`.
- **Mono:** two spans with `font-family: monospace` (inline code-like labels).
- **Weights:** bold via inline `style="font-weight: bold;"` on six spans; two spans explicitly reset to `normal`.

| Role | Size | Weight | Family |
|---|---|---|---|
| Name `<h2>` | about 1.5em (inferred) | bold | Verdana |
| Affiliation lines | 16px (inferred) | bold on key titles | default serif |
| Body paragraphs | 16px (inferred) | 400 | default serif |
| Link lists | 16px (inferred) | 400 | default serif |
| Inline labels | inherit | 400 | monospace |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Everything | 0 |

- **Shadows:** none.
- **Layout width:** full browser width; no container.
- **Images:** `border: 0px solid`; the right-floated image uses `width="200"`, another is set to `width: 185px; height: 80px`.
- **Separators:** one 2px `<hr>` and plain `<hr>` elements between link groups.

## Components

- **Name heading.** Verdana `h2`, black, no decoration, followed by a `<br>`.
- **Affiliation stack.** One line per role, roles in bold spans, institutions as links.
- **Mission paragraph.** Long first-person prose, default serif, full width.
- **Essay link list.** Plain `<a>` links to `IncIdeas/*.html`, one per line or bullet.
- **Book block.** RLAI book cover image linking to `book/the-book.html`.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Bio / photo | Yes, head photo and long bio paragraph; `BriefBio.html` linked | Default document style |
| Contact | Address, media contact e-mail, web, X handle | Plain lines |
| News | No dedicated section | Current roles stated in prose |
| Publication list | Linked out (`publications.html`, Google Scholar) | |
| Talks / book / FAQ / courses | Linked | Plain links |
| Essays | Yes | Link list (Bitter Lesson etc.) |
| Video | YouTube link, not embedded | |
| Awards | No | |

## Do's and Don'ts

- Do leave the body in browser defaults; the absence of design is the design.
- Do set only the name in Verdana to give the page a single anchor.
- Do keep links in default blue with underline.
- Don't add a container, nav bar, card or color; any of them would change the character.
- Don't break the mission paragraph into bullets; it is meant to be read as prose.

## Surfaces

One surface, the browser's white. Structure comes from headings, bold spans and `<hr>` rules.

## Imagery

A small head photo and the book cover, both inline with zero border. No thumbnails or figures.

## Layout

Single full-width column in source order. Text runs edge to edge at any viewport; nothing is responsive or fixed.

## Agent Prompt Guide

**Quick colors:** none declared; use browser defaults (white, black, `#0000ee` links, `#551a8b` visited).

1. "Render a researcher page with no CSS except an h2 name in Verdana; body in default serif, default link colors."
2. "Stack five affiliation lines under the name, with the role title in bold and the institution as a plain link."
3. "Add a list of essay links separated from the header by a full-width 2px hr, no bullets styling beyond the default."

## Similar Pages

The Barto page in this batch (same era, also CSS-free) and early-web personal pages such as Donald Knuth's.

## Quick Start

```css
:root {
  --bg: #ffffff;        /* inferred browser default */
  --text: #000000;      /* inferred */
  --link: #0000ee;      /* inferred */
  --link-visited: #551a8b; /* inferred */
  --font-name: Verdana, Helvetica, sans-serif;
  --font-body: "Times New Roman", Times, serif; /* inferred */
}
.style1 { font-family: var(--font-name); }
hr.header { width: 100%; height: 2px; }
```

## Provenance

- **URL:** http://incompleteideas.net/
- **Person:** Richard S. Sutton, reinforcement learning
- **Venue / award:** ACM A.M. Turing Award 2024 (shared with Andrew Barto)
- **Selection reason:** Rule A, Turing Award 2024 laureate (https://awards.acm.org/turing, University of Alberta news release); personal domain.
- **Template credit:** none; hand-edited HTML. The `.style1` class name and `<!-- -->` wrapped style block suggest a Dreamweaver or Netscape Composer origin (inferred).
- **Measurement method:** `extract_style.py` found only Verdana, monospace and bold weights, with no colors. The rest was read from the curl'd HTML. All colors and pixel sizes are browser defaults, marked inferred. The rendered page was not viewed.
