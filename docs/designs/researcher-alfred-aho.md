# Aho · All-Bold Plain HTML — Style Reference

> An index card typed in bold, with every line a hyperlink or a fact.

**Theme:** light

There is no CSS on this page. Values come from HTML attributes (`<body link vlink alink bgcolor text>`, `<font face color size>`, `<hr size>`) and default browser rendering, read from the 4.5 KB source; roles are interpreted from markup and one rendered viewport.

## Overview

Alfred Aho's Columbia page is a single scrolling list. It opens with an uppercase `h1` "ALFRED V. AHO", a 9px-thick horizontal rule and a 100px-wide portrait, then everything after that sits inside one unclosed `<h3>` element, so the entire page (courses, books, students, interests, talks, patents, address) renders in bold. Content is organised with `<dl>/<dd>` indents and plain line labels ("Courses", "Recent PhD Students", "Recent Invited Talks"). Links are pure HTML blue `#0000FF`, visited links red `#FF0000`, text black, in Verdana / Helvetica. The style is accidental minimalism: zero decoration, maximum density.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Page White | `#ffffff` | `--bg` | `<body bgcolor>` |
| Text Black | `#000000` | `--text` | `<body text>` |
| Midnight Navy | `#001155` | `--text-font` | Outer `<font color>` wrapper; the inner `<font face>` sets no color, so unlinked text inherits this near-black navy (inferred from nesting) |
| Hyperlink Blue | `#0000ff` | `--link` | Links |
| Visited Red | `#ff0000` | `--link-visited` | Visited links |
| Active Rust | `#cc3300` | `--link-active` | Active (pressed) links |
| Rule Grey | browser default (inferred) | `--rule` | `<hr size="9">` |

## Tokens — Typography

- **Family:** Verdana, Arial, Helvetica, sans-serif (innermost `<font face>`); outer wrappers declare Helvetica.
- **Weight:** bold for nearly everything, because the content is nested in `<h3>`.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Name (`h1`) | 2em (≈32px, browser default) | 700 | Uppercase as typed |
| Body (inside `h3`) | 1.17em (≈18.7px, browser default, inferred) | 700 | Entire page |
| Thesis and talk titles | same | 700 italic | `<i>` |
| Address block | same | 700 italic | `<address>` lines |

`<font size="2">` and `<basefont size="0">` wrappers are present but are overridden by the `h3` sizing in modern browsers (inferred from render).

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Everything | 0 |

Spacing is browser default: `<p>` margins, `<dd>` indent of 40px, `<hr size=9>` under the name. Portrait width 100px. No max width; text runs to the window edge. No shadows.

## Components

- **Name header:** uppercase `h1`, thick rule below.
- **Portrait:** 100px-wide JPEG, no border, followed by a line break.
- **Labeled list:** a plain label line ("Courses") followed by `<dd>` items, each a link with course code and term.
- **Student list:** name, colon, italic thesis title.
- **Talk list:** italic title, venue, date, with links to PDF / PPT / YouTube.
- **Address block:** nine `<address>` lines (department, building, mail code, street, phone, fax, obfuscated email).

## Page Modules

- **Bio/photo:** portrait plus one-sentence title (Lawrence Gussman Professor Emeritus); separate "Bio" link.
- **Teaching:** three course links (2014–2017).
- **Books:** single link to a books page.
- **Students:** four recent PhD students with thesis titles.
- **Research interests:** one line.
- **Publication list:** delegated to Google Scholar link.
- **Talks:** nine invited talks with slide links (one YouTube).
- **Patents:** one US patent.
- **Contact:** postal address, phone, fax, email.
- **Awards / news:** none on the page.

## Do's and Don'ts

- Do keep each section to a label plus an indented list.
- Do use italics only for titles of works.
- Don't add color beyond the default link trio.
- Don't treat the all-bold rendering as intentional emphasis when reproducing; it comes from an unclosed `h3`. Reproduce it only if the goal is a faithful copy.

## Surfaces

One white plane.

## Imagery

One portrait photo.

## Layout

Single unconstrained column, top to bottom, no navigation.

## Agent Prompt Guide

Quick colors: bg `#ffffff`, text `#000000`, link `#0000ff`, visited `#ff0000`, active `#cc3300`.

1. "Build a plain faculty header: uppercase h1 name, a 9px `<hr>`, a 100px portrait, one bold line with title and university."
2. "Build a labeled list: a bold label line, then `<dd>`-indented items, each a blue link with italic work title and plain venue and date."
3. "Build an address block: consecutive italic `<address>` lines for department, building, street, phone, fax, email."

## Similar Pages

LeCun in this batch (another long-lived hand-written page); classic 1990s CS faculty homepages.

## Quick Start

```css
:root {
  --bg: #ffffff; --text: #000000;
  --link: #0000ff; --link-visited: #ff0000; --link-active: #cc3300;
  --font: Verdana, Arial, Helvetica, sans-serif;
}
body { background: var(--bg); color: var(--text); font: 700 1.17em var(--font); }
a { color: var(--link); } a:visited { color: var(--link-visited); }
dd { margin-left: 40px; }
```

## Provenance

- **URL:** https://www.cs.columbia.edu/~aho/
- **Person:** Alfred V. Aho, compilers and algorithms.
- **Award:** ACM A.M. Turing Award 2020.
- **Selection reason:** Rule A, Turing Award 2020 laureate (awards.acm.org/turing); self-maintained university page.
- **Template credit:** none; hand-written HTML (windows-1252 charset).
- **Measurement method:** extract_style.py found no CSS; the full source was read and attribute values transcribed, plus one rendered viewport, which confirmed the all-bold rendering. Font sizes are browser defaults (inferred).
