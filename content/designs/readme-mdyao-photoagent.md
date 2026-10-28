# PhotoAgent — README Reference

> An app-store listing for a research agent: a cartoon mascot tile, four chunky colored buttons, then a black filmstrip of before-and-after shots.

**Theme:** both

Read from `README.md` on the default branch `code` of github.com/mdyao/PhotoAgent (last commit touching the file on that branch ec09900, 2026-03-12; captured 2026-10-28). Image URLs in the README point at the `main` branch through `raw.githubusercontent.com`, and all of them resolved. Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a first-screen capture and a 2700px tall capture of the light theme with the README column 920px wide (856px content width), the shields.io SVGs for the four badge URLs, and the icon, teaser, loop diagram, dataset figure and two result images fetched for sizes and colors. The capture files are saved at 1200×750, a 0.833 scale of the 1440×900 window; every y value below is converted back to the 1440×900 frame. The tall capture ends at the "Editing Examples" heading, so sizes below that point are computed from the source. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules.

## Overview

The first screen looks like a product page. A small square mascot (an orange cartoon cat holding a brush and palette on black) sits above a centred `<h1>` "PhotoAgent" with GitHub's rule and a centred `<h3>` subtitle. Directly under the subtitle is a row of four `for-the-badge` buttons, each with a dark #555555 label and a message in a different color (blue, red, yellow, green), then a centred author line that mixes blue linked names with black unlinked ones, a five-entry affiliation line, and a full-width black-framed teaser strip of three input/output photo pairs with a one-line caption burned into the image. A bold-led blockquote gives the tagline, and a thick `---` rule closes the header. The body keeps that rhythm: every `##` section is separated by a `---` rule, the Highlights section is a three-column table led by an emoji column, the method is shown both as an ASCII box diagram and as a numbered step table, and Results are HTML image tables (input/output pairs at 180px, an iteration strip at 200px). Code is "Coming soon!" in a blockquote. About half the file's bytes are a hidden HTML comment of search keywords that GitHub does not render.

## Header Block

Rendered positions are y values in the 1440×900 frame (the README box starts at y≈25 with its "README.md" file bar). Every element is its own centred HTML block.

1. **Mascot** (y≈94–174): `<p align="center"><img src="https://raw.githubusercontent.com/mdyao/PhotoAgent/main/images/photoagent_icon.jpg" width="80" style="border-radius:16px" /></p>`. The JPG is 2669×2669 (396 KB) and renders 80×80. GitHub strips the `style` attribute, so the corners render square, not rounded.
2. **Title** (y≈226): `<h1 align="center">PhotoAgent</h1>`. GitHub h1, 2em (32px), weight 600, with the grey rule.
3. **Subtitle** (y≈293): `<h3 align="center">Agentic Photo Editing with Exploratory Visual Aesthetic Planning</h3>`. GitHub h3, 1.25em (20px), no rule.
4. **Badge row** (y≈320–348): one `<p align="center">` with four `<a><img src="https://img.shields.io/badge/...?style=for-the-badge..." /></a>` joined by `&nbsp;`. Each badge is 28px tall; the SVGs are 152.75, 145.5, 156.25 and 174.25px wide and the row spans about 655px. Details in Badges.
5. **Authors** (y≈382): `<p align="center">` with five names separated by `&nbsp;&nbsp;`; three are `<a>` links (blue) and two, King-Man Tam and Menglu Wang, are plain text (black). Each carries `<sup>1,5</sup>`-style marks.
6. **Affiliations** (y≈422): `<sup>1</sup>CUHK MMLab&nbsp;&nbsp; <sup>2</sup>Shanghai AI Lab&nbsp;&nbsp; ...` with five entries on one line.
7. **Teaser** (y≈450–659): `<p align="center"><img src=".../images/teaser.jpg" width="100%" /></p>`. The JPG is 2548×625 and renders 856×210, not linked. Its black caption strip reads "Fully autonomous editing without any manual intervention."; there is no Markdown caption.
8. **Tagline** (y≈694–719): `> **One goal, one click, autonomous enhancement.** PhotoAgent turns photos into ...`. A left-aligned blockquote, bold first sentence, grey quote text.
9. **Rule** (y≈756): `---`, GitHub's 4px #d1d9e0 bar. The first `##` section starts at y≈798.

There is no venue line, no date and no link row outside the badges; ICML 2026 Oral (the gallery's venue for this entry) is not stated anywhere in the visible README.

## Badges

All four use `style=for-the-badge` with the default #555555 label, uppercase letter-spaced text and white (#ffffff) message text, as the returned SVGs show. Three carry a white Simple Icons logo on the label; the Hugging Face badge puts the 🤗 emoji in the label instead of a word.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| PROJECT (googlechrome logo, white) | PAGE | #007ec6 (`blue`; label #555555) | for-the-badge | mdyao.github.io/PhotoAgent/ |
| ARXIV (arxiv logo, white) | PAPER | #b31b1b (label #555555) | for-the-badge | arxiv.org/abs/2602.22809 |
| 🤗 | HUGGINGFACE | #d8b800 (`yellow`; label #555555) | for-the-badge | `#` (placeholder) |
| DATASET (databricks logo, white) | COMING | #67ac09 (`green`; label #555555) | for-the-badge | `#` (placeholder) |

The named colors `yellow` and `green` were read from the SVGs shields.io returns today (#d8b800 and #67ac09), which differ from the older shields.io values (#dfb317 and #97ca00); the README itself only says `yellow` and `green`. Two of the four buttons are placeholders that link to `#`, and one message is literally "Coming".

Other colors visible on the page come from images: the teaser and mascot frames are near-black #010101, the loop diagram is a dark navy and violet illustration (dominant pixels around #201040), and the dataset figure is a white panel. GitHub's `---` rule is #d1d9e0.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | PhotoAgent | title; badges, authors, affiliations, teaser, tagline and rule follow without a heading |
| h3 (centred) | Agentic Photo Editing with Exploratory Visual Aesthetic Planning | subtitle |
| h2 | Paradigm: From Human-in-the-loop to Agent-in-the-loop | one paragraph with two bold terms, then the loop illustration at `width="100%"` |
| h2 | Highlights | a three-column table: emoji, bold feature name, one-sentence description; six rows |
| h2 | How PhotoAgent Works | one paragraph, an unlabelled code fence with a box-drawing diagram, and a Step / Component / What it does table |
| h2 | Results | a centred bold claim sentence |
| h3 | Editing Examples | an HTML `<table>` of input/output pairs and a centred italic link line |
| h3 | Iterative Editing Process | one sentence and a one-row HTML table of four images with arrows |
| h2 | UGC-Edit Dataset & Benchmark | the dataset figure at `width="100%"` and a Component / Details table |
| h2 | Code | a blockquote "**Coming soon!** ..." |
| h2 | Citation | a `bibtex` block |
| h2 | License | one sentence linking LICENSE |

Every `##` from Paradigm to Code is preceded by a `---` rule; Citation and License are not.

Absent from the source: venue line, news, installation and usage commands, model zoo, numeric results table, demo or video, `<details>`, table of contents, acknowledgements, contact section.

Present but unusual: two badges link to `#`; the mascot's `style="border-radius:16px"` has no effect on GitHub; the ASCII diagram's inner boxes are wider than its outer frame, so the right edge of the frame breaks in the rendering; the README ends with a roughly 10.7 KB HTML comment of search phrases, multilingual keywords and venue lists (it mentions "ICML 2025"), invisible on GitHub but part of the file; the BibTeX is `@article` with no journal field and year 2025.

## Components

**Mascot tile.** A square illustration at `width="80"` above the title, black background, no border.

**Multicolor button row.** `for-the-badge` shields, one per destination, label #555555 and a destination color: project #007ec6, arXiv #b31b1b, Hugging Face #d8b800, dataset #67ac09, joined by `&nbsp;`.

**Tagline blockquote.** One `>` line with a bold first sentence and a plain second sentence, placed after the teaser.

**Section rules.** A `---` line before each `##` heading, giving a 4px grey bar plus the heading's own 1px rule a few lines below.

**Icon table.** `|  | Feature | Description |` with `|:---:|:---|:---|`: an empty first header over a centred emoji column (🔄 🌳 🧠 🎯 🛠 📐), a bold feature name, and a one-sentence description.

**Step table.** `| Step | Component | What it does |` with `|:---:|:---|:---|`; step numbers and component names are both bold (`**1**`, `**Perceiver**`), with *K* in italics in one cell.

**ASCII diagram.** An unlabelled ```` ``` ```` fence of box-drawing characters (┌ ─ ▶ ▲) showing Perceiver → Planner → Executor → Evaluator with a "memory + feedback" return arrow.

**Image pair table.** An HTML `<table>` whose first row is `<td align="center"><b>Input</b></td>` / `<b>Output</b>` twice, then three rows of four `<img ... width="180" />` cells.

**Iteration strip.** One HTML table row of four `<img ... width="200" /><br/><sub>Iter 1: Color & tone</sub>` cells with `→` cells between them.

**Centred notes.** `<p align="center"><b>...</b></p>` for the Results claim and `<p align="center"><i>More results ... <a>project page</a>.</i></p>` under the examples.

**Citation and license.** `@article{yao2025photoagent, ...}` with ` = ` aligned fields; one-line license sentence.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| photoagent_icon.jpg | JPG mascot on black | 2669×2669 | `<img ... width="80">` in `<p align="center">` | 80×80 | first element |
| teaser.jpg | JPG strip of three input/output pairs, black frame, caption inside the image | 2548×625 | `<img ... width="100%">` in `<p align="center">` | 856×210 | header, after affiliations |
| photoagent_loop.png | PNG illustration, dark navy, two panels (Human-in-the-loop vs Agent-in-the-loop cycle) | 2816×1536 | `<img ... width="100%">` | 856×467 | Paradigm section |
| results/img*-i/o.jpg | JPG photos, portrait | img1-i is 1062×1416 | `<img ... width="180" />` in HTML table cells | 180×240 for img1 | Editing Examples, 3 rows × 4 |
| intermediate/fig1-*.png | PNG iteration frames | fig1-1 is 497×663 | `<img ... width="200" />` with `<sub>` captions | 200×267 each; with three arrow cells the row is wider than 856px, so it likely scrolls horizontally (inferred, below the tall capture) | Iterative Editing Process |
| dataset.png | PNG figure on white | 5136×1680 | `<img ... width="100%">` | 856×280 | UGC-Edit section |

All images load from absolute `raw.githubusercontent.com/.../main/images/` URLs. There is no `<picture>` switch; the dark-framed teaser, mascot and loop illustration read on both themes, while the dataset figure stays a white panel.

## Adapting to Other Content

- **A library.** Keep the 80px mascot, h1 and h3, and a `for-the-badge` row (Docs, PyPI, License) with one color per destination; replace the teaser strip with a code example and drop the author lines.
- **A dataset.** Lead with the dataset figure at `width="100%"` (856px) in place of the teaser, keep the Component / Details table, and add a Download badge that links somewhere real.
- **A benchmark with scores.** Add a numeric table under Results with right-aligned columns (`| ---: |`) and bold best values; PhotoAgent states its claim in one centred bold sentence and shows images only, so this is an extension.
- **A repo without a mascot.** Start at the `<h1>`; the badge row directly under the subtitle still gives the product-page look.
- **A released codebase.** Replace the Code blockquote with install and run blocks, and keep the `---` rules between sections.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Keep the mascot small (`width="80"`) and square | Rely on `style="border-radius:..."`, which GitHub strips |
| Give each `for-the-badge` button its destination's color over a #555555 label | Link a badge to `#` as a placeholder |
| Show input/output pairs as a black-framed strip at `width="100%"` | Scatter single before/after images through the text |
| Start each highlight row with one emoji in its own centred column | Put emoji inside the bold feature name |
| Pair an ASCII or image diagram with a numbered Step table | Leave the diagram unexplained |
| Check that box-drawing diagrams align inside their frame | Ship a diagram whose outer frame breaks |
| Keep the README to visible content | Hide kilobytes of keyword text in an HTML comment |

## Agent Prompt Guide

1. "Write a centred README header: a square mascot `<img ... width="80">` in `<p align="center">`, `<h1 align="center">Name</h1>`, `<h3 align="center">Subtitle</h3>`, then one `<p align="center">` with four `for-the-badge` shields joined by `&nbsp;`: Project Page in `blue` (#007ec6) with the googlechrome logo, arXiv Paper in #b31b1b with the arxiv logo, 🤗 HuggingFace in `yellow` (#d8b800), Dataset in `green` (#67ac09) with the databricks logo; then a centred author line with `<sup>` marks and `&nbsp;&nbsp;`, a centred affiliation line, a full-width teaser strip, a bold-led `>` tagline and a `---` rule."
2. "Write body sections separated by `---`: Paradigm (paragraph plus a full-width illustration), Highlights (a `|  | Feature | Description |` table with `|:---:|:---|:---|`, one emoji per row and bold feature names), How it works (an ASCII box diagram in a code fence and a Step / Component / What it does table with bold step numbers), Results, Dataset & Benchmark, Code, then Citation and License without rules."
3. "Under Results, put a centred bold one-line claim, then an HTML `<table>` with a header row of `<td align="center"><b>Input</b></td>` / `<b>Output</b>` twice and rows of four `<img width="180" />`, then a centred italic link to the project page; add an iteration row of `<img width="200" /><br/><sub>Iter n: ...</sub>` cells separated by `→` cells."

## Similar Pages

- readme-seohongpark-ogbench: also a small logo over a centred title and a `for-the-badge` row, but in one color with a pale label and no author block.
- readme-damon-demon-spanuq: also puts badges right under the title and uses tables to make the method scannable, with 20px flat badges and a numeric results table.
- readme-gradientspaces-world-from-motion: the restrained counterpart, with text links instead of badges and a single teaser.

## Quick Start

````markdown
<p align="center">
  <img src="images/icon.jpg" width="80" />
</p>

<h1 align="center">ProjectName</h1>
<h3 align="center">Full Subtitle of the Paper</h3>

<p align="center">
  <a href="https://example.github.io/project/"><img src="https://img.shields.io/badge/Project-Page-blue?style=for-the-badge&logo=googlechrome&logoColor=white" /></a>&nbsp;
  <a href="https://arxiv.org/abs/XXXX.XXXXX"><img src="https://img.shields.io/badge/arXiv-Paper-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white" /></a>&nbsp;
  <a href="https://huggingface.co/org/name"><img src="https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow?style=for-the-badge" /></a>&nbsp;
  <a href="https://huggingface.co/datasets/org/name"><img src="https://img.shields.io/badge/Dataset-Download-green?style=for-the-badge&logo=databricks&logoColor=white" /></a>
</p>

<p align="center">
  <a href="https://example.org/">Author One</a><sup>1,2</sup>&nbsp;&nbsp;
  Author Two<sup>1</sup>&nbsp;&nbsp;
  <a href="https://example.org/">Author Three</a><sup>1,2</sup>
</p>

<p align="center">
  <sup>1</sup>Institution A&nbsp;&nbsp;
  <sup>2</sup>Institution B
</p>

<p align="center">
  <img src="images/teaser.jpg" width="100%" />
</p>

> **One-line promise in bold.** One plain sentence on how it works.

---

## Paradigm: From Old Way to New Way

Paragraph with the two **key terms** in bold.

<p align="center">
  <img src="images/loop.png" width="100%" />
</p>

---

## Highlights

|  | Feature | Description |
|:---:|:---|:---|
| 🔄 | **Feature** | One sentence. |

---

## How It Works

| Step | Component | What it does |
|:---:|:---|:---|
| **1** | **Component** | One sentence. |

---

## Results

<p align="center">
  <b>One-line claim.</b>
</p>

<table>
  <tr>
    <td align="center"><b>Input</b></td>
    <td align="center"><b>Output</b></td>
  </tr>
  <tr>
    <td><img src="images/results/1-i.jpg" width="180" /></td>
    <td><img src="images/results/1-o.jpg" width="180" /></td>
  </tr>
</table>

---

## Code

## Citation

```bibtex
@article{key,
  title   = {...},
  year    = {2026}
}
```

## License
````

## Provenance

- Repo: https://github.com/mdyao/PhotoAgent (`README.md`, default branch `code`, last README commit ec09900 on 2026-03-12; images served from branch `main`).
- Paper: listed for the gallery as "PhotoAgent: Exploratory Visual Aesthetic Planning with Large Vision Models", ICML 2026 Oral; first author Mingde Yao. The README's subtitle and BibTeX title it "PhotoAgent: Agentic Photo Editing with Exploratory Visual Aesthetic Planning" (arXiv 2602.22809) and give no venue. Project page https://mdyao.github.io/PhotoAgent/.
- Selection: a small mascot logo, matching `for-the-badge` buttons and an input/output teaser strip give it a polished product feel, and the icon-led Highlights table and step table make the method easy to scan.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), first-screen and 2700px captures at a 920px README column, shields.io SVGs for all four badge URLs, the icon, teaser, loop, dataset, one result image and one iteration frame fetched from the repo for sizes and colors.
- Written 2026-10-28.
