# Barto Emeritus Plainpage — Style Reference

> A department noticeboard with red headings in marker.

**Theme:** light

Measurements come from the static HTML only. The page has no stylesheet and no inline `style` attributes; every value is an HTML 3.2 attribute (`bgColor`, `link`, `vLink`, `<FONT color>`, table `width` and `cellPadding`). Font family and sizes are browser defaults and marked inferred. Roles are interpreted, not declared by the author. The rendered page was not viewed.

## Overview

Andrew Barto's UMass page is plain uppercase-tag HTML on white. A name and title block (Professor Emeritus, Retired Co-Director of the Autonomous Learning Laboratory) leads into a short bio line and a link to a fuller biography. Sections are separated by doubled `<HR><HR>` rules and introduced by `<H3>` headings wrapped in `<FONT color=#ff0000>`, so every section title is pure red. Content sits in borderless tables with 20px cell padding: a list of 26 Ph.D. students beside a 189x240 photo of the Science paper authors, three book covers (130x163 and 125x163) linking to the RL book, the handbook and the second edition, and a two-column "Research Interests / Areas of interest" block. Links are a muted crimson, visited links a deep teal-navy.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Plain White | `white` | `--bg` | `<BODY bgColor=white>` |
| Plain Black | `black` | `--text` | `<BODY text=black>` |
| Notice Red | `#ff0000` | `--heading` | Every `<H3>` section title and two emphasis lines |
| Crimson Link | `#b8334b` | `--link` | `<BODY link>` |
| Ink Teal | `#0d4977` | `--link-visited` | `<BODY vLink>` |
| Rule Grey | browser default (inferred) | `--rule` | Doubled `<HR>` separators |

## Tokens — Typography

- **Family:** browser default serif (no `face` attribute anywhere), typically Times New Roman (inferred). Substitute: `Times New Roman`, `Tinos`, or `Liberation Serif`.
- **Weights:** headings at the browser's bold `<H3>`; body regular.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Name | browser `<H2>`/`<H1>` default (inferred) | bold | Black |
| Section heading `<H3>` | about 1.17em (inferred) | bold | `#ff0000`; two use `size=+1` for a larger red title |
| Body / list items | 16px (inferred) | 400 | Black serif |
| Links | inherit | 400 | `#b8334b`, underlined (browser default) |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Everything | 0 |

- **Shadows:** none.
- **Layout width:** fixed tables at `width=773` and `width=815`, inner cells at 262, 308, 423 and 427px; `cellPadding=20`, `border=0`.
- **Separators:** two stacked `<HR>` elements between sections.
- **Images:** float via `align=left` on the student-list photo (`width=262 height=389` cell).

## Components

- **Section heading.** `<H3><FONT color=#ff0000>Title</FONT></H3>`, sometimes with `size=+1`.
- **Retirement notice.** Red `size=+1` heading "Note to Potential Grad-Student, Internship, and Post-Doc Applicants" followed by a plain paragraph.
- **Book row.** Three linked cover JPEGs side by side with `&nbsp;` spacing, under a red "Books: click on a book for more information" line.
- **Student list.** `<UL>` of linked names with graduation year, newest first, beside a left-aligned photo.
- **Two-column interests.** A table with "Research Interests" prose on the right and an "Areas of interest" bullet list on the left.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Bio / photo | Short bio plus linked biography page; group photo, no headshot | Plain serif |
| Contact | Obfuscated e-mail `barto [at] cs [dot] umass [dot] edu` | Plain text |
| News | No | |
| Publication list | Linked out ("Publications up through 2020") | Red link label |
| Books | Yes | Three cover thumbnails |
| Students | Yes | 26-name bullet list |
| Awards | No | |
| Results table | Layout tables only | |

## Do's and Don'ts

- Do keep everything in default serif on white with no CSS.
- Do color only section headings red and keep body black.
- Do separate sections with a doubled horizontal rule.
- Don't add a nav bar, web fonts or any rounded or shadowed element.
- Don't recolor links away from the crimson / teal pair; they are the only other color.

## Surfaces

One surface, white. Separation is purely by `<HR>` rules and table cell padding.

## Imagery

Book cover JPEGs at about 130x163 and one group photo at 189x240, all inline with no border.

## Layout

Single scrolling column built from fixed-width tables (773 to 815px). Two sections use two-column tables. No responsive behaviour.

## Agent Prompt Guide

**Quick colors:** bg `white`, text `black`, headings `#ff0000`, link `#b8334b`, visited `#0d4977`.

1. "Write a section heading as a bold h3 in pure red `#ff0000` on white, browser-default serif, preceded by two thin hr rules."
2. "Lay out three book cover thumbnails (130x163) inline under a red caption line, each linking to its book page."
3. "Make a two-column 20px-padded borderless table: prose interests on one side, a bullet list of areas on the other."

## Similar Pages

The Dongarra and Sutton pages in this batch (same CSS-free era). Barto's is the most minimal of the three: no frame, no nav, no font declaration.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #000000;
  --heading: #ff0000;
  --link: #b8334b;
  --link-visited: #0d4977;
  --font: "Times New Roman", Times, serif; /* inferred browser default */
  --cell-pad: 20px;
  --sheet: 815px;
}
h3 { color: var(--heading); }
a:link { color: var(--link); }
a:visited { color: var(--link-visited); }
```

## Provenance

- **URL:** https://people.cs.umass.edu/~barto/
- **Person:** Andrew G. Barto, reinforcement learning
- **Venue / award:** ACM A.M. Turing Award 2024 (shared with Richard Sutton)
- **Selection reason:** Rule A, Turing Award 2024 laureate (https://awards.acm.org/turing); self-maintained university page.
- **Template credit:** none; hand-written HTML 3.2 with uppercase tags.
- **Measurement method:** `extract_style.py` returned no colors, fonts or sizes because the page has no CSS. All values above were read from `BODY`, `FONT` and `TABLE` attributes in the curl'd HTML. Font family and pixel sizes are browser defaults and marked inferred. The rendered page was not viewed.
