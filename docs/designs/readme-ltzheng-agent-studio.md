# AgentStudio — README Reference

> A spec sheet before the story: one centred name, a strip of six tooling tags, then a pastel chart that maps what agents need onto what the toolkit ships, and a tick-and-cross table that says where everyone else falls short.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/ltzheng/agent-studio (last commit touching the file 64b839d, 2025-06-16; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors come from the SVGs that shields.io returns for each badge URL; image sizes come from the PNG and JPEG headers fetched from the repo, and figure colors from pixel counts on those files. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The README is a toolkit page dressed as a paper summary. It has no author line, no affiliation and no venue: a centred `<h1>` "AgentStudio" with GitHub's grey rule sits over one centred row of six flat shields.io badges that mix paper links (arXiv, project page) with engineering signals (Python 3.11, black, AGPL v3, pre-commit). Directly under the badges a full-width pastel diagram does the summarising: a column of three colored desiderata (general grounding in green, digital world knowledge in blue, open-ended learning in orange) mapped onto three outlined columns for environments, tools and benchmarks. A left-aligned intro paragraph with a four-item numbered list in bold lead phrases follows, then the line "Comparisons with existing work:" and a second full-width image, a paper-style feature table with green ticks and red crosses against ten prior environments, AgentStudio last and bold. Only after these two images does the first `##` heading (News) appear. The body is eight plain `##` sections without emoji, each one paragraph or a short list, with one more wide figure (observation and action spaces) and only two code blocks (`bash`, `bibtex`).

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Title** (y≈116): `<h1 align="center">` with `AgentStudio` on its own source line. GitHub h1, 2em (32px), weight 600, with the 1px grey rule under it across the 856px content width.
2. **Badge row** (y≈160–180): one `<p align="center">` holding six `<a><img src="https://img.shields.io/badge/..."></a>` lines and one HTML comment (a disabled mypy badge, `<!-- <a href="https://mypy-lang.org/">... -->`) that GitHub drops. Each badge is 20px tall; the source newlines render as single spaces and the row spans about 665px. Details in Badges.
3. **Summary diagram** (y≈210–459): `![](docs/assets/overview.png)` with an empty alt and no width. The 1680×488 PNG scales to 856×249 under GitHub's `max-width: 100%`; it is centred only because it fills the column. No caption.
4. **Intro paragraph** (y≈485): plain Markdown, left-aligned, "AgentStudio is **a trinity of environments, tools, and benchmarks** for ..." followed directly by a numbered list (`1.` to `4.`) whose items open with bold phrases (**A lightweight, interactive environment**, **Online benchmark tasks**, **Three benchmark datasets**).
5. **Comparison lead-in** (y≈745): the plain line `Comparisons with existing work:`.
6. **Comparison table image** (y≈778 to about 1035, below the fold): `![](docs/assets/comparison.png)`, 1924×578, rendered 856×257. This ends the header block; `## News` follows.

## Badges

All six use the static path form `https://img.shields.io/badge/<label>-<message>-<color>` (four with a `.svg` suffix) and no `style=`, so they render in shields.io's default `flat` style: 20px tall, 3px corner radius, a faint vertical gloss, Verdana 11px, label on the default #555555 grey, white (#ffffff) text. Only the last badge carries a logo.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| arXiv | 2403.17918 | #b31b1b (label #555555) | flat (default) | arxiv.org/abs/2403.17918 |
| Project | Page | named `Green`, rendered #44bb00 (label #555555) | flat (default) | ltzheng.github.io/agent-studio |
| python | 3.11 | named `blue`, #007ec6 (label #555555) | flat (default) | python.org release page for 3.11.7 |
| code style | black | #000000 (label #555555) | flat (default) | github.com/psf/black |
| License | AGPL v3 | named `blue`, #007ec6 (label #555555) | flat (default) | gnu.org/licenses/agpl-3.0 |
| pre-commit | enabled | named `brightgreen`, rendered #44bb00 (label #555555) | flat, `logo=pre-commit&logoColor=white` | pre-commit.com |

The two green badges were requested with different names (`Green`, `brightgreen`) but the SVGs shields.io returns today fill both messages with #44bb00 (written `#4b0` in the SVG), so they look identical in the capture. Message is a value (an arXiv number, a version, a tool name), not a destination, so the row reads as label/value pairs. Rendered widths are 116, 86, 84, 104, 108 and 145px.

Other colored marks on the page come from the two header images. The summary diagram fills its three desiderata cells with green #dae7d5, blue #dde8fc and orange #f5e5cb, and outlines the matching boxes in the other columns in paler tints of the same hues; text is black. The comparison table image uses green ticks #40651a and red crosses #bb271a on a white table with alternate grey bands #f2f2f2, in a serif paper font.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | AgentStudio | title; badges, summary diagram, intro with numbered list, comparison line and comparison image follow without a heading |
| h2 | News | three bullets, each a bold date ("**Oct 3, 2024**:") and one sentence, newest first; one inline HTML `<a>` link |
| h2 | Installation | "Install requirements:", one five-line `bash` block, then a paragraph on the API key file with two inline-code paths |
| h2 | AgentStudio Overall Benchmark Tasks | the observation/action space figure, then one paragraph (205 tasks) with a link to the task README and the project page |
| h2 | AgentStudio Datasets Decompose Agent Abilities | one paragraph naming GroundUI, IDMBench and CriticBench with links |
| h2 | AgentStudio Tools | a lead sentence, a three-item bullet list, a paragraph of three doc links |
| h2 | Contributing | one sentence linking CONTRIBUTING.md |
| h2 | Acknowledgement | one sentence listing seven linked projects |
| h2 | Citation | one sentence and a `bibtex` block |

Absent from the source: author, affiliation and venue lines (the venue appears only as the `booktitle` in BibTeX), a teaser GIF or video, a results table in Markdown, a model zoo, a quick-start run command, a license section (the license is only a badge), a table of contents, emoji in headings.

Present but unusual: the first screen holds two images before any heading, and the second is a feature-comparison table delivered as a PNG rather than a Markdown table; both images use `![]()` with empty alt text; a disabled badge stays in the source as an HTML comment; three section headings repeat the project name ("AgentStudio Overall Benchmark Tasks", "AgentStudio Datasets ...", "AgentStudio Tools").

## Components

**Centred title and badge paragraph.** Only two header elements are centred: `<h1 align="center">` and the badge `<p align="center">`. Everything after them is ordinary left-aligned Markdown, and the two images look centred only because they span the 856px column.

**Badge row.** Six flat static badges, label grey #555555, messages #b31b1b, #44bb00, #007ec6, #000000, #007ec6, #44bb00. Paper links come first, tooling badges after. Quotes are mixed in the source (single quotes on the first two `href`/`src`, double on the rest); `alt` is set on four of six.

**Desiderata-to-component diagram.** A four-column grid image: a filled left column of three colored desiderata (#dae7d5, #dde8fc, #f5e5cb) and three outlined columns (Environments, Tools, Benchmarks) whose rows inherit the color of the desideratum they serve; a merged "Online benchmark tasks" cell spans three rows. Column titles are bold black two-line headings inside the image.

**Bold-lead numbered list.** Four `1.` items under the intro, each opening with a bold phrase and adding bold key terms mid-sentence (**generic observation and action spaces**, **auto-evaluation**).

**Comparison table as image.** Columns Environment, Domain, Obs. Space, Action Space, then five yes/no feature columns (Interactive, Data & Task Tools, Language Feedback, Lightweight, Decompose Abilities) marked with ticks #40651a and crosses #bb271a. Rows are grouped by rules (web, mobile, desktop) and the project's own row is last, in bold, with ticks in every feature column.

**News list.** `- **Mon D, YYYY**: Sentence.` with the month abbreviated and no emoji; three entries, newest first.

**Code blocks.** Two fenced blocks: `bash` for install (with a trailing `# If using Ubuntu 22.04` comment on one line) and `bibtex` for the citation. Paths and file names elsewhere are inline code.

**Citation.** "If you find AgentStudio useful, please cite our paper:" then `@inproceedings{zheng2024agentstudio, ...}` with `Agent{S}tudio` brace-protected and the ICLR proceedings written out in `booktitle`.

**Acknowledgement and contributing.** One-sentence prose sections with inline links, no logos and no badges.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| overview.png | PNG, pastel grid diagram on white | 1680×488 | `![](docs/assets/overview.png)` | 856×249 | header, directly under the badge row |
| comparison.png | PNG, paper-style table with ticks and crosses | 1924×578 | `![](docs/assets/comparison.png)` | 856×257 | header, after "Comparisons with existing work:" |
| agent_space.jpg | JPEG, two-panel icon diagram (web browser vs AgentStudio environments) split by a dashed line | 6236×2120 | `![](docs/assets/agent_space.jpg)` | 856×291 | first line of "AgentStudio Overall Benchmark Tasks" |

All three are wide and short (aspect ratios 3.4 to 2.9), white-backed and free of captions; none uses `<picture>`, a width attribute or a link wrapper written by the author (GitHub adds its own link to the full image). There is no GIF and no video.

## Adapting to Other Content

- **A library or toolkit.** This is the native fit: keep the centred h1 and one flat badge row of label/value pairs (paper, docs, Python version, code style, license), and replace the desiderata diagram with a single wide feature-map image about 1700px wide (856px rendered, roughly 250px tall).
- **A benchmark.** Keep the comparison image but consider a Markdown table instead, with the same columns (domain, observation space, action space, then yes/no features) and the benchmark's own row last in bold; a Markdown table stays searchable and readable in dark mode.
- **A paper repo with authors.** Insert a centred author line and a bold venue line between the h1 and the badge row; AgentStudio leaves both out, so this is an extension.
- **A repo without a figure.** Let the badge row close the header and move the bold-lead numbered list directly under it as the summary.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Put one wide summary diagram directly under the badges | Open with a long paragraph before any picture |
| Key the diagram's rows by color so the reader can trace a need to a component | Use colors in the diagram that mean nothing |
| Show positioning against prior work as a tick/cross table with your row last and bold | Claim superiority in prose without a comparison |
| Keep badges in one flat family on the default #555555 label | Leave dead badges commented out in the header source |
| Give every image alt text | Ship `![]()` images with empty alt as AgentStudio does |
| Keep sections short and link out to sub-READMEs | Duplicate the sub-READMEs' instructions in the main page |

## Agent Prompt Guide

1. "Write a README header in GitHub Markdown: `<h1 align="center">ProjectName</h1>`, then one `<p align="center">` with six flat shields.io static badges on the default #555555 label: arXiv number #b31b1b, Project Page #44bb00, python 3.11 #007ec6, code style black #000000, License #007ec6, pre-commit enabled #44bb00 with `logo=pre-commit&logoColor=white`. No author or venue lines."
2. "Under the badges put a full-width summary diagram (`![alt](docs/assets/overview.png)`, about 1680×488 source, 856×249 rendered): a left column of three desiderata filled #dae7d5, #dde8fc and #f5e5cb, and three outlined columns for environments, tools and benchmarks colored to match. Follow with one intro sentence with a bold core phrase and a four-item numbered list whose items open in bold."
3. "Add 'Comparisons with existing work:' and a wide comparison table (about 1924×578) listing prior environments by domain, observation space and action space, with five feature columns marked by ticks #40651a and crosses #bb271a and your row last in bold. Then plain `##` sections: News (bold `Mon D, YYYY` dates), Installation (`bash`), one section per component, Contributing, Acknowledgement, Citation (`bibtex`)."

## Similar Pages

- readme-nepfaff-scenesmith: also a centred h1 over one centred row of flat static badges (arXiv #b31b1b first) before any figure, though SceneSmith adds an icon in the title and an author block.
- readme-drexubery-viewcrafter: uses the same two badge URLs in the same form (`arXiv-<id>-b31b1b.svg`, `Project-Page-Green`), so its first two tags look the same as AgentStudio's.
- readme-seohongpark-ogbench: another agent benchmark README with a centred title and a uniform badge row; it uses `for-the-badge` badges in one brand color rather than the flat mixed palette here.
- readme-eku127-satnav: a benchmark README that explains itself with one wide diagram, but it adds a paper-style author header and a runnable Quick Start that AgentStudio lacks.

AgentStudio's distinguishing choices are the absence of any author block, a color-keyed desiderata map as the header figure and a positioning table delivered as an image before the first heading.

## Quick Start

````markdown
<h1 align="center">
ProjectName
</h1>

<p align="center">
<a href="https://arxiv.org/abs/XXXX.XXXXX"><img src="https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg" alt="arXiv"></a>
<a href="https://example.github.io/project"><img src="https://img.shields.io/badge/Project-Page-44bb00" alt="Project page"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.11-007ec6.svg" alt="Python 3.11"></a>
<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL%20v3-007ec6.svg" alt="License"></a>
<a href="https://pre-commit.com/"><img src="https://img.shields.io/badge/pre--commit-enabled-44bb00?logo=pre-commit&logoColor=white" alt="pre-commit"></a>
</p>

![Desiderata mapped to components](docs/assets/overview.png)

ProjectName is **a one-phrase summary of what it is** for some audience. It provides:
1. **First component** with **a key property**
2. **Second component** for a task
3. **Third component** that evaluates something
4. **Datasets**: A, B and C, for three abilities

Comparisons with existing work:

![Feature comparison with prior environments](docs/assets/comparison.png)

## News

- **Mon D, YYYY**: Released the full version.
- **Mon D, YYYY**: Released the beta version.

## Installation

Install requirements:

```bash
git clone https://github.com/org/name.git
conda create --name name python=3.11 -y
conda activate name
pip install -e .
```

## Component One

![Component figure](docs/assets/component.jpg)

One paragraph with a link to the component README.

## Component Two

## Contributing

## Acknowledgement

## Citation

If you find ProjectName useful, please cite our paper:

```bibtex
@inproceedings{key,
  title={...},
}
```
````

## Provenance

- Repo: https://github.com/ltzheng/agent-studio (`README.md`, branch `main`, last README commit 64b839d on 2025-06-16).
- Paper: "AgentStudio: A Toolkit for Building General Virtual Agents", ICLR 2025, arXiv 2403.17918; first author Longtao Zheng. Project page https://ltzheng.github.io/agent-studio.
- Selection: a colored desiderata-to-component diagram serves as the header summary, and a feature-comparison table against prior environments adds a positioning style the other picks lack.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for all six badge URLs, PNG/JPEG headers and pixel color counts for `overview.png`, `comparison.png` and `agent_space.jpg`.
- Written 2026-10-28.
