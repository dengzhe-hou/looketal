# Omegance — README Reference

> A one-knob instrument panel: a centred title card, four small tags, then a single annotated contact sheet that shows the knob turning before the install line appears.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/itsmag11/Omegance (last commit touching the file ca0aca1, 2026-10-02; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors come from the SVGs that shields.io returns for the badge URLs; teaser accent colors are medians of saturated pixels in `media/teaser.jpg` fetched from the repo. Rendered positions are y values in the 1440×900 frame. GitHub sets the type (its system stack), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The README is short and built for use. A `<div align="center">` wraps a Markdown `#` title (the full paper title, wrapping to two lines with GitHub's h1 rule under it), a comma-separated line of four linked authors, a plain affiliation line, a bold venue line, and one row of four badges: three flat static badges (ICCV 2025, Paper arXiv, Project Page) and a GitHub social stars badge. The body uses six `##` headings that each start with an emoji. "🎯 Project Overview" holds a three-line paragraph with the key rule in bold (**omega < 0 gives more details, omega > 0 gives fewer details**) and then the teaser, a tall annotated figure (856×891 rendered) that shows global, mask-based spatial and schedule-based temporal effects and links to the project page. "🚀 Quick Start" follows with a one-line `pip` install and a ten-line `python` example, so the library is usable straight after the figure. Usage, Local Demo, Citation and License complete it. There is no table of contents, no news list and no results table.

## Header Block

All header items are Markdown inside one `<div align="center">` with blank lines after `<div>` and before `</div>`.

1. **Title** (y≈139 and 180, two lines): `# Omegance: A Single Parameter for Various Granularities in Diffusion-Based Synthesis`. GitHub h1, 2em (32px), weight 600, centred by the div; it wraps after "in" at the 856px width, and the 1px grey rule sits under the second line at about y≈208.
2. **Authors** (y≈236): `[Xinyu Hou](https://itsmag11.github.io/), [Zongsheng Yue](...), [Xiaoming Li](...), [Chen Change Loy](...)` on one source line. Link blue, comma-separated, no affiliation marks.
3. **Affiliation** (y≈277): `S-Lab, Nanyang Technological University`. Plain text.
4. **Venue** (y≈317): `**ICCV 2025**`. Bold body text, no link.
5. **Badge row** (y≈354): four `[![alt](https://img.shields.io/...)](url)` lines in one paragraph, 20px tall, about 334px wide in total (74 + 80 + 86 + 82 plus three spaces). Details in Badges.
6. **End of header**: `</div>` closes the block; the first `##` heading ("🎯 Project Overview", y≈412) and its paragraph (y≈461–509) are still above the teaser.
7. **Teaser** (from y≈546, runs past the fold to about y≈1437): `[![Teaser Image](./media/teaser.jpg)](https://itsmag11.github.io/Omegance/)` as its own paragraph inside Project Overview. No width attribute; GitHub's `max-width: 100%` scales the 8604×8954 JPEG to 856×891, and the image links to the project page. The first screen shows its top row (the global-effect strip) and the top of the spatial-effect row.

## Badges

The three static badges use the path form `https://img.shields.io/badge/<label>-<message>-<hex>` with no `style=` or `logo=`, so they render in shields.io's default `flat` style: 20px tall, 3px corner radius, faint vertical gloss, Verdana 11px, white text, label on #555555. The fourth is a dynamic GitHub stars badge in `style=social`.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| ICCV | 2025 | #4b44ce (label #555555) | flat (default) | iccv2025.thecvf.com |
| Paper | arXiv | #b31b1b (label #555555) | flat (default) | arxiv.org/abs/2411.17769 |
| Project | Page | #4c9a2a (label #555555) | flat (default) | itsmag11.github.io/Omegance/ |
| Stars (GitHub logo) | 52 at capture time | #fcfcfc label and #fafafa count box, text #333333 | `style=social` | github.com/itsmag11/Omegance |

The label/message pairs are split phrases ("Paper | arXiv", "Project | Page") rather than category and destination, and each message color is distinct: indigo for the venue, arXiv red, green for the project page. The social badge breaks the flat look with a light rounded button and a separate count bubble.

Colors on the page that are not badges come from the teaser: orange #e0973d and green #6ba435 highlight boxes around crops in the spatial and temporal rows (pixel medians; the orange bin also picks up warm image content), and red and blue mask thumbnails explained in the figure's own caption "(Red for Detail Enhancement, Blue for Detail Suppression)".

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | Omegance: A Single Parameter for Various Granularities in Diffusion-Based Synthesis | title; authors, affiliation, venue and badges follow in the same div |
| h2 | 🎯 Project Overview | one paragraph with **Omegance** and the omega sign rule in bold and a 🤗 emoji before "Diffusers", then the linked teaser |
| h2 | 🚀 Quick Start | a one-line `bash` install from GitHub, a `python` block (load SDXL, `apply_omegance(pipe, omega=-5)`, generate), one paragraph of tested pipelines and schedulers |
| h2 | 🎛️ Usage | one `python` block with four commented groups: Global, Temporal, Spatial, Turn off |
| h2 | 🎮 Local Demo | one sentence, three bullets with bold tab names, a four-line `bash` block, one sentence with the local URL and download size, a two-column option table, one sentence of hardware advice |
| h2 | 📖 Citation | one sentence and a `bibtex` block |
| h2 | 📜 License | one paragraph (S-Lab License 1.0, base models under their own licenses) |

Absent from the source: news or changelog, table of contents, results or benchmark table, model zoo, dataset section, GIF or embedded video, teaser caption outside the image, acknowledgements, `<details>` blocks.

Present but unusual: the teaser sits inside the first `##` section rather than in the header; it is a single 8604×8954 JPEG of about 6.6 MB that renders taller than the first screen; it links to the project page, not to itself; the venue appears both as a bold line and as the first badge; the install command is `pip install git+https://...` rather than a clone; every heading carries an emoji, including the variation-selector form 🎛️.

## Components

**Centred Markdown header.** One `<div align="center">` with Markdown inside (a `#` heading, link lines, a bold line, badge lines), separated by blank lines so GitHub parses them. No `<p>` or `<h1>` tags.

**Badge row.** Four `[![alt](...)](url)` lines on consecutive source lines; flat badges on label grey #555555 with messages #4b44ce, #b31b1b, #4c9a2a, then the social stars badge. Alt text repeats the content ("ICCV 2025", "Paper", "Project Page", "GitHub Stars").

**Emoji headings.** Every `##` starts with one emoji and a space: 🎯, 🚀, 🎛️, 🎮, 📖, 📜. Sentence-case words, no numbering, no `###` anywhere.

**Bold rule in the lead paragraph.** The paragraph under Project Overview puts the one usage rule in bold so it survives skimming: `**omega < 0 gives more details, omega > 0 gives fewer details**`.

**Code blocks.** `bash` for install and demo commands, `python` for the API, `bibtex` for the citation. The Usage block uses `#` comments as sub-headings ("# Global: useful range is about [-10, 10]") instead of `###` headings, and inline comments for parameter notes.

**Option table.** Two columns (Option, Description) with `|--------|-------------|` delimiters and no alignment colons; flags in inline code, examples inline in the description.

**Demo bullets.** `- **Global**: ...` style, bold tab name then a colon and one clause.

**Citation.** "If you find our work useful for your research, please consider citing:" then `@inproceedings{hou2025omegance, ...}` with aligned `=` signs and a full ICCV `booktitle`.

**License line.** One paragraph with an inline link to LICENSE; no badge.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| media/teaser.jpg | JPEG, white background, annotated result grid with in-image captions | 8604×8954, about 6.6 MB | `[![Teaser Image](./media/teaser.jpg)](https://itsmag11.github.io/Omegance/)`, no width | 856×891 | first image of the page, after the Project Overview paragraph |

The figure has three labelled bands. "(a) Global Effect" is a row of five landscape crops under dashed arrows reading "More Detail", "SDXL" and "Less Detail". "(b) Mask-Based Spatial Effect" shows three wizard images (ControlNet + SDXL in the middle) with small red and blue mask thumbnails, orange and green boxes, and enlarged crops under each. "(c) Schedule-Based Temporal Effect" shows three street scenes with dashed and solid crop boxes. All captions are inside the image, so the Markdown has no caption line. No `<picture>`, no dark variant, no GIF and no video.

## Adapting to Other Content

- **A library.** This is already the model: keep the centred title, one badge row, a figure that shows the parameter's effect, and put a `pip` line and a ten-line example as the first section after it.
- **A paper repo with training code.** Keep the header and the figure, then add Installation and Training sections after Quick Start, each with its own emoji heading in the same style.
- **A dataset.** Replace the effect grid with a sample grid at the same full width (856px) and replace the Python example with a two-line loader snippet.
- **A repo without a teaser.** Move Quick Start directly under the badge row; the bold rule sentence then becomes the only summary, so keep it.
- **A shorter first screen.** Give the teaser `width="70%"` (about 599px) to bring Quick Start closer to the fold; the source figure is nearly square, so full width uses about 891px of height.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Keep the header to title, authors, affiliation, venue and one badge row | Add a second badge row for every link |
| State the one usage rule in bold in the first paragraph | Bury the parameter's sign convention in the API section |
| Show the effect in one annotated figure with in-image labels | Spread the same comparisons across many small images |
| Follow the figure with a one-line install and a short runnable example | Make the reader clone and build before trying the method |
| Use `#` comments to group variants inside one code block | Split four short variants into four headings |
| Give every `##` one emoji, consistently | Mix emoji and plain headings |
| Compress a large teaser before committing | Commit a 6.6 MB, 8604px-wide JPEG for an 856px slot |

## Agent Prompt Guide

1. "Write a README header in GitHub Markdown inside `<div align="center">`: a `#` heading with the full paper title, one comma-separated line of linked author names, a plain affiliation line, a bold venue line, and one row of four badges: flat shields.io badges ICCV 2025 (message #4b44ce), Paper arXiv (message #b31b1b), Project Page (message #4c9a2a) on label grey #555555, plus a GitHub stars badge with `style=social`. Close the div."
2. "After the header, write `## 🎯 Project Overview` with one paragraph that names the method in bold and states the usage rule in bold, then a linked teaser image `[![Teaser Image](./media/teaser.jpg)](project-page-url)` with no width. Then `## 🚀 Quick Start` with a one-line `pip install git+https://...` block and a ten-line `python` example."
3. "Continue with `## 🎛️ Usage` as one `python` block grouped by `#` comments, `## 🎮 Local Demo` with three bold-lead bullets, a `bash` block and a two-column Option | Description table, `## 📖 Citation` with one sentence and a `bibtex` block, and `## 📜 License` as one paragraph."

## Similar Pages

- readme-zjx0101-objectclear: also from S-Lab, Nanyang Technological University, with a centred author, affiliation and venue stack above the badges.
- readme-huggingface-peft: a library README with a centred title and a short code example placed early; it shares the 🤗 Diffusers ecosystem.
- readme-sisyphm-studiorecon: the same `<div align="center">` wrapper around Markdown headings, author line, bold venue and flat static badges, with a full-width teaser.

## Quick Start

````markdown
<div align="center">

# ProjectName: Full Paper Title

[Author One](https://example.org/), [Author Two](https://example.org/), [Author Three](https://example.org/)

Lab, University

**Venue Year**

[![Venue Year](https://img.shields.io/badge/ICCV-2025-4b44ce)](https://venue.example.org/)
[![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b)](https://arxiv.org/abs/XXXX.XXXXX)
[![Project Page](https://img.shields.io/badge/Project-Page-4c9a2a)](https://example.github.io/name/)
[![GitHub Stars](https://img.shields.io/github/stars/org/name?style=social)](https://github.com/org/name)

</div>

## 🎯 Project Overview

**ProjectName** does X with one parameter. One line of code adds it to existing pipelines:
**rule in bold**, and the default leaves the output unchanged.

[![Teaser Image](./media/teaser.jpg)](https://example.github.io/name/)

## 🚀 Quick Start

```bash
pip install git+https://github.com/org/name
```

```python
from name import apply_name

apply_name(pipe, param=-5)
```

Tested with ... Other setups may also work, but are untested.

## 🎛️ Usage

```python
# Variant one
...

# Variant two
...
```

## 🎮 Local Demo

- **Tab one**: what it does.
- **Tab two**: what it does.

```bash
git clone https://github.com/org/name.git
cd name
pip install -e ".[demo]"
python app.py
```

| Option | Description |
|--------|-------------|
| `--flag` | What it does |

## 📖 Citation

If you find our work useful for your research, please consider citing:

```bibtex
@inproceedings{key,
  title = {...},
}
```

## 📜 License
````

## Provenance

- Repo: https://github.com/itsmag11/Omegance (`README.md`, branch `main`, last README commit ca0aca1 on 2026-10-02).
- Paper: "Omegance: A Single Parameter for Various Granularities in Diffusion-Based Synthesis", ICCV 2025, arXiv 2411.17769; first author Xinyu Hou. Project page https://itsmag11.github.io/Omegance/.
- Selection: one annotated figure shows the global, spatial and temporal effects, and a copy-paste quick start appears right below it, a good model for a library-style repo that should be usable within the first screen.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the four badge URLs, `media/teaser.jpg` fetched from the repo for pixel size, file size and accent colors.
- Written 2026-10-28.
