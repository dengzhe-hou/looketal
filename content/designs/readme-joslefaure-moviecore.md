# MovieCORE — README Reference

> A festival programme in miniature: a film-reel brain logo, a centred title over a bold tagline, three small tags, and a staggered strip of movie frames with pastel callouts that ask what the scene means.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/joslefaure/moviecore (last commit touching the file 316f1ff, 2025-09-02; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors and sizes come from the SVGs that shields.io returns for the badge URLs; image sizes and colors come from `assets/moviecore_icon.png` and `assets/poster_teaser.png` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The header is one `<div align="center">` written in indented Markdown: a 150px logo (a film reel fused with a brain, in blues, above the word "MovieCORE"), a `#` title with GitHub's grey rule, a bold one-line tagline, three default flat shields.io badges and a full-width teaser. The teaser is three staggered film strips from one movie, each paired with a pastel callout box (blue, orange, green) and a color legend underneath. The body uses an emoji on every `##` heading (📖 🗂️ 🚀 🎯 📊 💻 📚 🤝 📄) and some `###` headings, with short prose, two bullet lists of dataset links, a five-row evaluation-dimension table whose first column is bold and emoji-led, a `bash` evaluation command, a long `json` input example and BibTeX. A Markdown `---` and a second centred div close the page with an emoji tagline and a bold link bar. There is no author list, no news and no results table.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Wrapper**: `<div align="center">` with every inner line indented two spaces and separated by blank lines; GitHub still parses the indented lines as Markdown, so the `#` heading, bold text and image links work inside the div.
2. **Logo** (y≈116–222): `<img src="assets/moviecore_icon.png" alt="MovieCORE Icon" width="150"/>`. The 1024×1024 PNG with a transparent background renders at 150×150.
3. **Title** (y≈295): `# MovieCORE: COgnitive REasoning in Movies`. GitHub h1, 2em (32px), weight 600, one line, centred, with the 1px grey rule across the 856px content width. The capitals in "COgnitive REasoning" spell the acronym.
4. **Tagline** (y≈353): `**A Video Question Answering Dataset for Probing Deeper Cognitive Understanding of Movie Content**`. A bold body-size paragraph, upright, not a heading.
5. **Badge row** (y≈390): three Markdown image links on consecutive lines, joined into one paragraph; 20px tall, the row spans about 355px.
6. **Teaser** (y≈450–816): `![MovieCore Dataset](assets/poster_teaser.png)` with no width. GitHub's `max-width: 100%` scales the 2936×1416 PNG to 856×413; the drawing has white side margins (non-white pixels from x=138 to x=2800), so the visible strips span about 776px.
7. **Overview heading** (y≈882): "📖 Overview" sits at the fold, so the first screen is logo, title, tagline, badges and teaser only.

## Badges

All three use the static path form with a `.svg` suffix and no `style=`, `logo=` or `labelColor=` parameter, so they render in shields.io's default `flat` style: 20px tall, 3px corner radius, a faint vertical gloss, Verdana 11px, label on #555555.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| arXiv | 2508.19026 | #b31b1b (label #555555) | flat (default) | arxiv.org/abs/2508.19026 |
| 🤗 Dataset | HuggingFace | #d8b800 (`yellow` as shields.io now renders it; label #555555) | flat (default) | huggingface.co/datasets/MovieCORE/MovieCORE |
| License | MIT | #67ac09 (`green` as shields.io now renders it; label #555555) | flat (default) | LICENSE |
| (footer link row) | 📖 Paper \| 🤗 Dataset \| 💻 Code | GitHub link blue | bold links, ` \| ` separators, centred | arxiv.org/abs/2508.19026v1, the dataset, github.com/joslefaure/MovieCORE |

The hugging-face emoji is typed into the label text (`🤗%20Dataset`), not a shields.io logo. The bold link row appears only at the very bottom of the page, in a closing `<div align="center">`, not in the header.

Image colors used below, read from the PNGs: logo blues #387eb2 and navy #113c67; teaser callout and legend fills pale blue #dde7fb (Emotional/Psychological States), pale green #dae7d4 (Character Contrasts) and pale orange #f8e5cc (Cause-Effect Relationships); highlighted words in the callouts in lavender #9b7fb5; film-strip frames black #000000.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | MovieCORE: COgnitive REasoning in Movies | title; logo above, tagline, badges and teaser below, all in one div |
| h2 | 📖 Overview | one paragraph |
| h2 | 🗂️ Data Preparation | one sentence, then `###` Video Data (two bold-led bullet links), `###` Annotations (one bullet link), and a closing sentence |
| h2 | 🚀 Quick Start | `###` Installation with a two-line `bash` block (clone and `cd`) |
| h2 | 🎯 Baselines | one bullet linking HERMES (ICCV'25) |
| h2 | 📊 Evaluation Dimensions | one sentence, a Dimension / Description table of five rows, one closing sentence |
| h2 | 💻 Usage | `###` Evaluation Script (`bash`: export key, run script), `###` 📝 Input Format (a `json` example), `###` 📈 Output (three bullets) |
| h2 | 📚 Citation | one sentence and a `bibtex` `@misc` block |
| h2 | 🤝 Contributing | one sentence and four bullets |
| h2 | 📄 License | one sentence |

After License: `---`, then `<div align="center">` with `<p>🎬 <strong>Advancing Video Understanding Through Cognitive Evaluation</strong> 🎬</p>` and the bold link row.

Absent from the source: author and affiliation block, venue line (EMNLP appears nowhere in the README), news, results or leaderboard table, model zoo, GIF or video, table of contents, acknowledgements, contact.

Present but unusual: the header div is written in indented Markdown rather than HTML; the Quick Start only clones the repo; two `###` headings carry emoji and two do not; the page ends with a centred tagline and link bar; the `json` example's first question is long enough to scroll sideways in its code block.

## Components

**Indented Markdown div.** `<div align="center">`, then blank-line-separated lines indented two spaces (`  <img ... width="150"/>`, `  # Title`, `  **Tagline**`, badge lines, `  ![alt](teaser.png)`), then `</div>`.

**Flat badge row.** Three `[![alt](https://img.shields.io/badge/Label-Message-color.svg)](target)` lines; label #555555; messages #b31b1b, #d8b800, #67ac09.

**Emoji headings.** Every `##` starts with one emoji and a space (`## 📊 Evaluation Dimensions`); `###` headings inside Usage add emoji only for Input Format and Output.

**Bold-led link bullets.** `- **Training Data**: [MovieChat-1K Train](...)`, one artifact per bullet.

**Dimension table.** Two columns with `|-----------|-------------|` and no alignment colons; first cells are bold with a leading emoji (`**🎯 Accuracy**`, `**🧠 Depth**`), second cells one sentence each. GitHub centres the header cells and stripes alternate rows.

**Code blocks.** `bash` for clone and evaluation (with `export OPENAI_API_KEY='...'`), `json` for the prediction format, `bibtex` for the citation; GitHub renders them on its light grey code background with a copy button.

**Closing footer.** `---`, then a centred div with an emoji-flanked bold tagline and `**[📖 Paper](...) | [🤗 Dataset](...) | [💻 Code](...)**`.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| moviecore_icon.png | PNG logo, transparent background, blue film reel and brain over the wordmark | 1024×1024 | `<img ... width="150"/>` | 150×150 | first element of the header div |
| poster_teaser.png | PNG, three film strips with pastel callouts and a legend, on white | 2936×1416 | `![MovieCore Dataset](assets/poster_teaser.png)` | 856×413 (strips about 776px) | last element of the header div; no caption |

The teaser stages three rows of three to five movie frames inside black film-strip borders, offset left, right, left; each row points with an outline arrow to a rounded callout that names an emotional reading in black and lavender text with a small "(Q: ...)" example question beneath. A boxed legend maps the three fill colors to the three question types. Neither image uses `<picture>`; the logo's transparency would let it sit on dark backgrounds, but the teaser is white-backed.

## Adapting to Other Content

- **A model or method repo.** Keep the logo, title, bold tagline and three-badge row; replace the teaser with a method figure at full width (856px) and add an author line under the tagline.
- **A benchmark with scores.** Keep the dimension table as the metric definition and add a results table after it with right-aligned numbers (`| ---: |`); MovieCORE has none, so this is an extension.
- **A repo without a logo.** Drop the 150px image; the title then starts the page and the teaser rises by about 190px.
- **A repo without a teaser.** Let the badge row close the header and move the dimension-style table up under Overview.
- **A runnable tool.** Give Quick Start an install line and one example command; MovieCORE's two-line clone-only block is too thin to copy.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Size the logo explicitly (`width="150"`) | Let a 1024px logo render at full column width |
| Put the tagline in bold under the title | Repeat the title as a second heading |
| Keep one emoji per `##` heading, consistently | Add emoji to some `##` headings and not others |
| Lead table rows with a bold, emoji-tagged term | Use emoji in body sentences as decoration |
| Pair a color-coded teaser with a legend inside the image | Rely on callout colors without saying what they mean |
| Close with a centred link bar that repeats the badges | Make the footer the only place a link appears |
| State the venue somewhere in the header | Leave the venue out, as MovieCORE does |

## Agent Prompt Guide

1. "Write a README header inside `<div align="center">` using indented Markdown: a 150px logo `<img width="150"/>`, a `#` title whose capitals spell the acronym, a bold one-line tagline, then three default flat shields.io badges on consecutive lines (arXiv number #b31b1b, 🤗 Dataset HuggingFace #d8b800, License MIT #67ac09, labels #555555), then a teaser as `![alt](assets/teaser.png)` with no width so it fills 856px."
2. "Write the body with one emoji on every `##` heading: 📖 Overview, 🗂️ Data Preparation (`###` subsections with bold-led link bullets), 🚀 Quick Start, 🎯 Baselines, 📊 Evaluation Dimensions (a two-column table whose first cells are bold and start with an emoji), 💻 Usage (`bash` then `json`), 📚 Citation, 🤝 Contributing, 📄 License."
3. "End with `---` and a centred div holding a bold tagline flanked by 🎬 and a bold link row `[📖 Paper] | [🤗 Dataset] | [💻 Code]`. If the teaser uses colored callouts, keep them to three pastel fills (#dde7fb, #dae7d4, #f8e5cc) with a legend."

## Similar Pages

- readme-snuhcc-dice-bench: an NLP dataset README with emoji `##` headings (📖 Overview, 📜 Citation, 🤝 Contact) and a small centred badge row; it opens with a full-width banner where MovieCORE opens with a 150px logo.
- readme-mdyao-photoagent: a small centred icon over a centred title and subtitle, then badges; PhotoAgent uses `for-the-badge` and plain headings, MovieCORE flat badges and emoji headings.
- readme-eth-medical-ai-lab-med-prm: an EMNLP 2025 README with a centred logo above the title and emoji on some headings; it lists results in a scoreboard section, which MovieCORE lacks.

## Quick Start

````markdown
<div align="center">
  <img src="assets/icon.png" alt="Project Icon" width="150"/>

  # ProjectNAME: Acronym-Spelling Title

  **One-Line Tagline Describing the Dataset**

  [![arXiv](https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg)](https://arxiv.org/abs/XXXX.XXXXX)
  [![Dataset](https://img.shields.io/badge/🤗%20Dataset-HuggingFace-yellow.svg)](https://huggingface.co/datasets/org/name)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

  ![Teaser](assets/teaser.png)
</div>

## 📖 Overview

One paragraph.

## 🗂️ Data Preparation

### Video Data
- **Training Data**: [Name](https://example.org/)

### Annotations
- **Annotations**: [🤗 HuggingFace Dataset](https://huggingface.co/datasets/org/name)

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/org/name.git
cd name
```

## 🎯 Baselines
- One bullet.

## 📊 Evaluation Dimensions

| Dimension | Description |
|-----------|-------------|
| **🎯 Accuracy** | One sentence |

## 💻 Usage

### Evaluation Script

```bash
python evaluate.py --pred_path path/to/predictions.json
```

### 📝 Input Format

```json
{
    "video_1.mp4": [{"question": "...", "answer": "...", "pred": "..."}]
}
```

## 📚 Citation

```bibtex
@misc{key2025,
      title={...},
}
```

## 🤝 Contributing

## 📄 License

---

<div align="center">
  <p>🎬 <strong>Closing Tagline</strong> 🎬</p>

  **[📖 Paper](https://arxiv.org/abs/XXXX.XXXXX) | [🤗 Dataset](https://huggingface.co/datasets/org/name) | [💻 Code](https://github.com/org/name)**
</div>
````

## Provenance

- Repo: https://github.com/joslefaure/moviecore (`README.md`, branch `main`, last README commit 316f1ff on 2025-09-02).
- Paper: "MovieCORE: COgnitive REasoning in Movies", EMNLP 2025, arXiv 2508.19026; first author Gueter Josmy Faure.
- Selection: a small logo, title and subtitle over three badges and a film-strip teaser give a clean centred header, and the emoji headings stay consistent down to a neat evaluation-dimension table. The selection note calls the subtitle italic; the source and the capture show it bold (`**...**`).
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the three badge URLs, the logo and teaser PNGs fetched for pixel sizes and colors.
- Written 2026-10-28.
