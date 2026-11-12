# Awesome Continuous Language Models — README Reference

> A survey's reading room: a centred masthead with four small tags and a full-width tour of the paper map, then one long comparison table and eight shut drawers of papers sorted by family.

**Theme:** both

Read from `README.md` on the default branch `main` of github.com/sophtang/Awesome-Continuous-Language-Models (last commit touching the file bbe5f93 "update table", 2026-11-10; read 2026-11-12). Evidence is the raw Markdown (295 lines, 52,876 bytes), the HTML that GitHub's API returns for it, a first-screen capture at a 968×605 window and a 968×1815 tall capture (the README column is 920px wide, 856px content width), a full-length 968px capture for the tables and the page bottom, the shields.io and awesome.re SVGs for the badge URLs, and `assets/paper_map_demo.gif` fetched from the repo. y values below are in the 968px-wide frame at scale 1, where the README box starts at y≈24 with its "README.md" file bar. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; the README adds nothing to them except emoji in four headings and `<sub>`/`<sup>` sizes in the header.

## Overview

The page opens like a paper's title block. Inside one `<div align="center">` a ruled h1 "Awesome Continuous Language Models" sits above a bold one-line subtitle that names the survey in italics, a single row of four 20px flat badges (the pink-and-plum awesome.re badge, a "papers 137" count, a red alphaXiv badge and a blue Project Page badge), then the author block in three centred lines (linked names with superscript affiliation numbers, small linked email addresses, affiliations). A full-width animated GIF of the survey's interactive paper map follows with a small caption, and a `·`-separated link line acts as the table of contents. The body is plain `##` sections with no h3 at all. The heavy part is "🌟 Start here", an eight-column table of 24 representative models (23 papers) whose cells carry arXiv and alphaXiv links plus a GitHub stars badge for code. Below it the remaining 114 papers are folded into eight `<details>` drawers, each a dated four-column table, so the rendered page is short (about 7,400px) for a 52 KB source. It ends with a BibTeX block and a star-history chart that switches to a dark version through `<picture>`.

## Header Block

Everything down to the link line is wrapped in `<div align="center">` with a blank line after it, so the Markdown inside still renders.

1. **Title** (y≈140, rule at y≈168): `# Awesome Continuous Language Models`. A plain Markdown h1 (2em, 32px, weight 600), centred by the div, with GitHub's grey rule under it spanning the full 856px. No logo.
2. **Subtitle** (y≈197): `**The paper collection for our survey, *A Survey on Continuous Diffusion and Flow Language Models*.**`, bold 16px with the survey title in bold italic.
3. **Badge row** (y≈226–245): four Markdown image lines on consecutive source lines, so GitHub joins them with single spaces. Each badge is 20px tall; the SVGs are 110, 78, 106 and 86px wide and the row spans about 395px. Details in Badges.
4. **Authors** (y≈279): `<a href="https://sophtang.github.io/">Sophia Tang</a><sup>1</sup> &emsp; ...` four linked names in link blue at 16px, separated by `&emsp;`, each with a superscript affiliation number.
5. **Emails** (y≈323): `<sub><a href="mailto:...">sophtang@engineering.upenn.edu</a> &emsp; ...</sub>`, four mailto links in `<sub>` (about 12px), separated by `&emsp;`.
6. **Affiliations** (y≈359): `<sup>1</sup> University of Pennsylvania &emsp; <sup>2</sup> KAIST &emsp; <sup>3</sup> University of Amsterdam`, plain black text.
7. **Teaser GIF** (y≈388–922): `<a href="assets/paper_map_demo.mp4"><img src="assets/paper_map_demo.gif" alt="Demo of the interactive map of continuous language models" width="100%"></a>`. The GIF is 830×518, 570 frames at 80ms (47.5s, looping), so `width="100%"` upscales it to 856×534. It is preceded by an HTML comment, left in the source, saying the `.mp4` link should be replaced by a `github.com/user-attachments` URL for a video player; the link opens the file page, not an inline player.
8. **Caption** (y≈960): `<sub>A tour of our <a href="https://continuous-lm.github.io/map/">interactive paper map</a>.</sub>`.
9. **Link line** (y≈995–1019): `[News](#news) · [What are continuous language models?](#what-are-continuous-language-models) · [Start here](#-start-here) · ... · [Star History](#star-history)`, eight anchor links joined by ` · `. At 856px it wraps to two lines, breaking "Star History" across them.
10. **Close**: `</div>`, then `## News` at y≈1071.

The first screen (605px tall) ends about 217px into the GIF, so the visible part is the map's title, "A Map of *Continuous Language Models*", in the site's serif and violet italics. There is no venue line; the survey is an alphaXiv preprint and the venue appears only as `publisher = {alphaXiv}` in the BibTeX.

## Badges

The four header badges are default `flat` (no `style=` parameter), 20px, with rounded corners and the shields.io gradient. Three are shields.io static badges with the label on #555555 and white (#ffffff) text; the first is awesome.re's own SVG. The per-paper code badges in the tables use `style=social`.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| (sunglasses icon on #cca6c4) | awesome (wordmark on #494368) | #cca6c4 / #494368 | awesome.re SVG, 110×20 | awesome.re |
| papers | 137 | #007ec6 (`blue`, label #555555) | flat, 78×20 | not linked |
| alphaXiv | Survey | #b31b1b | flat, 106×20 | alphaxiv.org/abs/2611.continuous-diffusion-flow-language-models |
| Project | Page | #007ec6 (`blue`) | flat, 86×20 | continuous-lm.github.io |
| Code (GitHub mark) | live star count, e.g. 181 for david3684/flm | #fcfcfc label with #333333 text, white count box | social, 88×20 natural | each paper's repository (76 badges in the file, 17 in Start here) |

The row mixes awesome-list convention (the awesome.re badge) with paper-page badges (alphaXiv red, project-page blue). The paper count is hard-coded in the URL (`papers-137-blue`), so it has to be edited by hand. In the tables the social badges sit in a Links column that is about 59px wide inside its padding, so GitHub's `max-width: 100%` shrinks each 88×20 badge to roughly 59×13 (measured on the capture), and it wraps onto its own line after a dangling ` · `.

Other colors on the page are GitHub's own, not chosen by the author: link blue #0969da, the quote bar #d1d9e0 and the table rules and zebra striping (#f6f8fa). The teaser GIF is an opaque white (#ffffff) page with the survey site's navy and violet (#4f4bd6, from the survey project page entry) and pastel family colors.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred by the div, ruled) | Awesome Continuous Language Models | the header block above |
| h2 | News | two bullets, each led by a bold date (`**Nov 9, 2026**:`) |
| h2 | What are continuous language models? | a one-sentence blockquote definition, one paragraph, a link to the survey and four blog links with author and date |
| h2 | 🌟 Start here | one intro sentence, then an eight-column table of 24 rows: Paper, Links, Venue, Representation, Formulation, Main loss, Few-step, Key feature |
| h2 | 🆕 Recently added | a sentence on the literature cutoff (November 2, 2026) and a four-column table with one placeholder row, "No papers yet." |
| h2 | 📚 More papers | one sentence, then eight `<details>` drawers, one per model family, each a Date, Paper, Links, Venue table |
| h2 | Contributing | one sentence with an "open an issue" link |
| h2 | BibTeX | one lead sentence and a `bibtex` block (`@article{tang2026survey`) |
| h2 | Star History | a `<picture>` star-history.com chart with a dark source |

Absent from the source: a logo, a venue line, a license section or file (the repo has no license), a table of contents as a list (the `·` link line stands in), install or usage instructions (there is no code), contribution guidelines beyond one line, a contact section, any h3.

Present but unusual: the author block (names, emails, affiliations) of a paper title page inside an awesome list; the main table repeats the survey's model taxonomy columns (representation, formulation, loss, few-step) rather than only listing links; two rows (FLM and FMLM) point to the same arXiv paper 2602.16813, so the table has 24 rows for 23 papers; inline math `$v$-MSE` and `$d\ll V$` in cells, which GitHub renders through `<math-renderer>` (the local capture shows the raw dollars because it does not load GitHub's math script); the dates in the drawer tables use non-breaking hyphens (U+2011, `2026‑10‑27`) so they never wrap; an HTML comment in the header that is a note to the author.

## Components

**Masthead badge row.** Four default-style badges on consecutive lines: the awesome.re badge first, a hard-coded count (`papers-137-blue`), an alphaXiv badge in #b31b1b and a project-page badge in #007ec6.

**Paper author block.** Three centred lines inside the header div: linked names with `<sup>` affiliation numbers joined by `&emsp;`, the email addresses wrapped in `<sub>` as mailto links, and an affiliations line with `<sup>` numbers.

**Dot-separated link line.** `[Section](#anchor) · [Section](#anchor) · ...`, centred, after the caption, with the emoji headings linked as `#-start-here` (GitHub drops the emoji and keeps a leading hyphen).

**Comparison table.** `|:--|:--|...|` left-aligned on every column. The Paper cell is `<b>Short name</b>: Full title`; the Links cell is `<a href="https://arxiv.org/abs/ID">arXiv</a> · <a href="https://www.alphaxiv.org/abs/ID">alphaXiv</a> · <a href="REPO"><img src="https://img.shields.io/github/stars/OWNER/REPO?style=social&label=Code" alt="Code"></a>`, the badge only when code exists; short abbreviated values (`Learned vocab. emb.`, `Gaussian diff.`, `MSE + CE`, `Distill.`) and an en dash `–` for an empty Few-step cell. At a 920px column the eight columns need more than 856px, so the table scrolls sideways and the Key feature column is cut off at the right edge in the capture.

**Family drawers.** `<details>` then `<summary><b>🌊 Vocabulary embeddings</b> (12 papers)</summary>` then `<br>` and a blank line before the table, closed by `</details>`. Every summary leads with an emoji and a bold family name and ends with the paper count in plain text. The tables inside are `| Date | Paper | Links | Venue |`, newest first, with `YYYY‑MM‑DD` dates in non-breaking hyphens and the same Links cell recipe.

**Placeholder table.** "🆕 Recently added" keeps an empty table with one row `|  | No papers yet. |  |  |` so the column layout is ready for new entries.

**Definition quote.** The field is defined once in a `>` blockquote (grey text with GitHub's left bar), followed by plain prose and a bullet list of blog posts in the form `[Title](url) by Author (date)`.

**Citation and stars.** `bibtex` block with `publisher = {alphaXiv}` and `url`, then `<picture><source media="(prefers-color-scheme: dark)" srcset="...&theme=dark"><img alt="..." src="..."></picture>` for the star-history chart.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| paper_map_demo.gif | animated GIF screen recording of the survey's interactive map (zoom, pan, filter chips, a CFM detail panel), 570 frames, 47.5s, looping | 830×518 (8.86 MB) | `<img ... width="100%">` inside a link to `assets/paper_map_demo.mp4` | 856×534 | after the affiliations, before the caption |
| star-history chart | external SVG from api.star-history.com, hand-drawn style, with a dark-theme `<source>` | chart about 800px wide at render | `<picture>` with `prefers-color-scheme: dark` | about 760px wide, centred | last element |
| Code badges | shields.io `style=social` | 88×20 typical | inline `<img>` in table cells | about 59×13 | Links column of every table |

The GIF is the only content image. It is a light page from the survey site, so it shows as a white panel in GitHub's dark theme; the star chart is the only element that switches with the theme. The first frame of the GIF reads "136 papers · 8 families" in the map header while the badge says 137.

## Adapting to Other Content

- **A survey paper list.** Keep the centred title, subtitle, author block and badge row; put a short recording or a static figure of the taxonomy at `width="100%"` (856px); keep a "Start here" table of the representative works with taxonomy columns, and fold the rest into one `<details>` drawer per family with the count in the summary.
- **A shorter list (under 40 entries).** Drop the drawers and keep one dated table per family under `###` headings, since the drawers only pay off when a section would run several screens.
- **A benchmark or leaderboard.** Replace the taxonomy columns with metric columns, right-aligned (`| ---: |`), and keep the Links cell recipe so each row links paper and code.
- **No teaser recording.** Move the `·` link line directly under the affiliations; the header then fits in about 360px.
- **Wide tables.** Keep the main table to six columns or fewer at 856px, or move long text columns (Key feature) into the drawer tables.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Fold long family lists into `<details>` with the paper count in the summary | Print 114 rows open on the page |
| Use one Links cell recipe (`arXiv · alphaXiv · Code badge`) in every table | Mix link formats between tables |
| Write dates as `YYYY‑MM‑DD` with non-breaking hyphens in a fixed Date column | Let dates wrap inside narrow cells |
| Keep a "Recently added" table with a placeholder row after the survey cutoff | Silently append new papers to the main table |
| Give a dark `<source>` for external charts through `<picture>` | Embed a light-only chart without a fallback |
| Keep the badge count in sync with the list | Leave a hard-coded `papers-137` badge and a map recording that says 136 |
| Keep the main table narrow enough for 856px | Add an eighth column that forces sideways scrolling |
| Link a video through `github.com/user-attachments` if it should play | Link a raw `.mp4` from the repo and expect an inline player |

## Agent Prompt Guide

1. "Write a centred README header inside `<div align="center">` with a blank line after the tag: a plain `#` title, a bold one-line subtitle naming the survey in italics, one row of four default flat badges on consecutive lines (awesome.re badge, `papers-N-blue` in #007ec6 with label #555555, `alphaXiv-Survey-b31b1b` in #b31b1b, `Project-Page-blue`), then three centred lines: linked author names with `<sup>` affiliation numbers joined by `&emsp;`, the emails as mailto links inside `<sub>`, and the affiliations with `<sup>` numbers. Add a full-width `width="100%"` GIF of the paper map with a `<sub>` caption and a ` · `-separated anchor link line, then close the div."
2. "Use only `##` sections in this order: News (bullets led by a bold date), What are continuous language models? (a one-sentence `>` definition, a paragraph and a list of blog links), 🌟 Start here, 🆕 Recently added, 📚 More papers, Contributing, BibTeX, Star History."
3. "In 🌟 Start here, write a left-aligned table with columns Paper, Links, Venue, Representation, Formulation, Main loss, Few-step, Key feature. Paper cells are `<b>Short</b>: Full title`; Links cells are `arXiv · alphaXiv · ` plus a shields.io `github/stars/OWNER/REPO?style=social&label=Code` badge when code exists; use `–` for empty cells. In 📚 More papers, wrap each family in `<details><summary><b>EMOJI Family</b> (N papers)</summary><br>` with a Date, Paper, Links, Venue table, newest first, dates in non-breaking hyphens."

## Similar Pages

- readme-kuleshov-group-bd3lms: also a diffusion language model README, but a method repo with a comparison graphic and code map, where this one is a paper list with a taxonomy table.
- readme-eku127-satnav: a similar centred title-page header with linked authors, superscript affiliations, a flat badge row and a full-width teaser; SatNav puts a venue line first and the badges after the authors, where this one puts the badges first, adds an email line and uses a screen recording as the teaser.
- readme-seohongpark-ogbench: also leads with a centred block and a full-width image, but packs the paper links into a heading-size line and uses one badge color, where this row mixes four.

## Quick Start

````markdown
<div align="center">

# Awesome Topic Models

**The paper collection for our survey, *Survey Title*.**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Papers](https://img.shields.io/badge/papers-N-blue)
[![alphaXiv](https://img.shields.io/badge/alphaXiv-Survey-b31b1b)](https://www.alphaxiv.org/abs/XXXX)
[![Project Page](https://img.shields.io/badge/Project-Page-blue)](https://example.github.io/)

<a href="https://author1.example/">Author One</a><sup>1</sup> &emsp; <a href="https://author2.example/">Author Two</a><sup>2</sup>

<sub><a href="mailto:one@example.edu">one@example.edu</a> &emsp; <a href="mailto:two@example.edu">two@example.edu</a></sub>

<sup>1</sup> University A &emsp; <sup>2</sup> University B

<a href="https://example.github.io/map/"><img src="assets/map_demo.gif" alt="Demo of the paper map" width="100%"></a>

<sub>A tour of our <a href="https://example.github.io/map/">interactive paper map</a>.</sub>

[News](#news) · [What is X?](#what-is-x) · [Start here](#-start-here) · [Recently added](#-recently-added) · [More papers](#-more-papers) · [Contributing](#contributing) · [BibTeX](#bibtex) · [Star History](#star-history)

</div>

## News

- **Mon D, YYYY**: The survey is live on [alphaXiv](https://www.alphaxiv.org/abs/XXXX).

## What is X?

> One-sentence definition of the field.

One paragraph of context. For more, read our [survey paper](https://www.alphaxiv.org/abs/XXXX).
- [Blog title](https://example.org/) by Author (Mon YYYY)

## 🌟 Start here

| Paper | Links | Venue | Representation | Formulation | Main loss | Few-step | Key feature |
|:--|:--|:--|:--|:--|:--|:--|:--|
| <b>Short</b>: Full Title | <a href="https://arxiv.org/abs/ID">arXiv</a> · <a href="https://www.alphaxiv.org/abs/ID">alphaXiv</a> · <a href="https://github.com/OWNER/REPO"><img src="https://img.shields.io/github/stars/OWNER/REPO?style=social&label=Code" alt="Code"></a> | Venue YYYY | value | value | value | – | value |

## 🆕 Recently added

Papers added after the survey's literature cutoff will appear here, newest first.

| Added | Paper | Links | Family |
|:--|:--|:--|:--|
|  | No papers yet. |  |  |

## 📚 More papers

<details>
<summary><b>🌊 Family name</b> (N papers)</summary>
<br>

| Date | Paper | Links | Venue |
|:--|:--|:--|:--|
| YYYY‑MM‑DD | <b>Short</b>: Full Title | <a href="https://arxiv.org/abs/ID">arXiv</a> · <a href="https://www.alphaxiv.org/abs/ID">alphaXiv</a> | Venue YYYY |

</details>

## Contributing

To suggest a change, [open an issue](https://github.com/OWNER/REPO/issues).

## BibTeX

```bibtex
@article{key2026survey,
  title = {Survey Title},
  publisher = {alphaXiv},
  year = {2026}
}
```

## Star History

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=OWNER%2FREPO&type=date&theme=dark">
  <img alt="Star history of OWNER/REPO" src="https://api.star-history.com/svg?repos=OWNER%2FREPO&type=date">
</picture>
````

## Provenance

- Repo: https://github.com/sophtang/Awesome-Continuous-Language-Models (`README.md`, branch `main`, last README commit bbe5f93 on 2026-11-10; 28 stars, no license file).
- Paper: "A Survey on Continuous Diffusion and Flow Language Models", alphaXiv preprint 2026-11-09, no venue; Sophia Tang, Chanhyuk Lee, Floor Eijkelboom, Jinwoo Kim. Project page https://continuous-lm.github.io/, recorded in this gallery as alphaxiv-2026-continuous-lm-survey.
- Selection: added on the maintainer's suggestion together with the survey's project page, outside the selection rounds and the pool rules (the README pool only took repositories linked from accepted-venue project pages). It is the gallery's first awesome-list README, notable for a paper-style author block, a taxonomy table and family drawers.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-11-12), a 968×605 first-screen capture, a 968×1815 tall capture and a full-length 968px capture at a 920px README column, shields.io and awesome.re SVGs for the four header badge URLs and one social code badge, `assets/paper_map_demo.gif` fetched for size, frame count and its first frame.
- Defects seen: the Start here table overflows 856px and scrolls sideways; the GIF's map reads 136 papers while the badge says 137; the blog list spells Sander Dieleman as "Dielman"; the `.mp4` link and its HTML comment are an unfinished video embed; the link line wraps "Star History" across two lines.
- Written 2026-11-12.
