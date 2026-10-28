# PEFT — README Reference

> A well-kept workshop manual: a hugging-face nameplate, one plain sentence of purpose, a green-ruled tip card, and then the code is already on the bench.

**Theme:** both

Read from `README.md` on the default branch `main` of github.com/huggingface/peft (last commit touching the file 667d0c3, 2026-07-20; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). The captures are styled with `github-markdown-css` 5.8.1 (light), which supplies the alert, link and syntax colors quoted below. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them. The README has no images and no badges.

## Overview

This is a library README, and it looks like one. The first screen is almost all text: a centred h1 "🤗 PEFT" with GitHub's grey rule, a centred bold h3 tagline "State-of-the-art Parameter-Efficient Fine-Tuning (PEFT) methods", two left-aligned prose paragraphs on what PEFT does and what it integrates with, a GitHub `[!TIP]` alert with its green left bar and lightbulb title, one paragraph of doc links, and then `## Quickstart` with a one-line `pip install peft` block. Below the fold come two syntax-highlighted Python examples (train with LoRA, load for inference), a "Why you should use PEFT" section that backs the claim with a memory table and an accuracy table, more tip alerts, an integrations tour (Diffusers, Transformers, Accelerate, TRL) with short Python snippets, and a citation. There are no badges, no logo image, no teaser, no news and no authors; the only color on the first screen is the alert green, the link blue and the 🤗 emoji.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **License comment**: the file opens with a 15-line `<!--- Copyright 2023 The HuggingFace Team ... -->` Apache-2.0 notice. It renders nothing.
2. **Title** (y≈115): `<h1 align="center"> <p>🤗 PEFT</p></h1>`. GitHub h1, 2em (32px), weight 600, centred, with the 1px grey rule under it at about y≈160. The emoji is a text character drawn by the system emoji font, not an image.
3. **Tagline** (y≈199): `<h3 align="center"><p>State-of-the-art Parameter-Efficient Fine-Tuning (PEFT) methods</p></h3>`. GitHub h3, 1.25em (20px), weight 600, centred, no rule. It is a real heading and appears in GitHub's outline.
4. **Intro paragraphs** (y≈238 to 400): two plain Markdown paragraphs, left-aligned, no bold, no links.
5. **Tip alert** (y≈430 to 545): `> [!TIP]` followed by `> Visit the [PEFT](https://huggingface.co/PEFT) organization ...`. GitHub renders a callout with a 4px left bar and a "Tip" title with a lightbulb octicon, both in #1a7f37; the body text stays default.
6. **Doc-links paragraph** (y≈574 to 598): one sentence linking three conceptual guides (Adapters, Soft prompts, IA3).
7. **Quickstart** (y≈650): `## Quickstart` with its rule, "Install PEFT from pip:" and a `bash` block `pip install peft` (y≈730 to 780). The first Python block starts just above the 900px fold.

## Badges

The README contains no badges and no link rows that act as buttons; the only header links are inline text links in the tip and the doc-links paragraph. Colors that appear on the page come from GitHub's own rendering, not from the author:

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| (alert) | Tip | #1a7f37 (left bar and title) | GitHub `[!TIP]` alert | not a link |
| (inline links) | PEFT, Adapters, Soft prompts, IA3, blog post | #0969da | plain text links | huggingface.co/PEFT, huggingface.co/docs/peft/... |

Code blocks use GitHub's light syntax palette: keywords #cf222e (`import`, `from`, `if`), strings #0a3069, function and class names #6639ba (`from_pretrained`, `get_peft_model`), constants #0550ae (`True`, `CAUSAL_LM`) and comments #59636e, on the light grey code background.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | 🤗 PEFT | name only |
| h3 (centred) | State-of-the-art Parameter-Efficient Fine-Tuning (PEFT) methods | tagline; two intro paragraphs, a tip alert and a doc-links paragraph follow without a heading |
| h2 | Quickstart | `pip install peft` in a `bash` block, a LoRA training example and an inference example in `python` blocks, each with an expected-output comment |
| h2 | Why you should use PEFT | one-sentence lead |
| h3 | High performance on consumer hardware | a four-column memory table (Model, Full Finetuning, PEFT-LoRA PyTorch, PEFT-LoRA DeepSpeed with CPU Offloading), one paragraph, a two-column Submission Name / Accuracy table, a tip alert |
| h3 | Quantization | one paragraph and two `*` bullets of blog and notebook links |
| h3 | Save compute and storage | one paragraph |
| h2 | PEFT integrations | one-sentence lead |
| h3 | Diffusers | one paragraph, a one-row memory table, a tip alert |
| h3 | Transformers | three short `python` blocks (`add_adapter`, `load_adapter`, `set_adapter`) with a lead sentence each |
| h3 | Accelerate | one paragraph |
| h3 | TRL | three `*` bullets of guides |
| h2 | Model support | one paragraph of links |
| h2 | Contribute | one sentence |
| h2 | Citing 🤗 PEFT | one sentence and a `bibtex` block |

Absent from the source: badges, logo or banner image, teaser, GIF or video, news or changelog, authors and affiliations, venue line, installation matrix, model zoo table, license section (the license appears only as a hidden HTML comment), acknowledgements, table of contents.

Present but unusual: both header headings wrap their text in a `<p>` inside the heading tag; the tagline is an `<h3>` rather than bold text; three `[!TIP]` alerts carry the side notes; the second Python example ends with a `# prints something like:` comment so the reader sees output without running it; the citation entry is `@Misc` with `\url` in `howpublished`.

## Components

**Centred heading pair.** `<h1 align="center">` for the name and `<h3 align="center">` for the tagline, nothing between them. The h1 takes GitHub's rule, the h3 does not, so the tagline floats under the rule.

**Tip alert.** `> [!TIP]` on its own line, then `> ` lines of body text with inline links. Rendered with a #1a7f37 left bar and "Tip" title. Used three times: under the intro, after the accuracy table and after the Diffusers table, always for a pointer to further material.

**Install block.** One-line `bash` fence: `pip install peft`. No conda, no version pins.

**Runnable examples.** `python` fences that import, configure, run and save in one block, with the expected output as a trailing comment (`# prints: trainable params: 3,686,400 || all params: 3,089,625,088 || trainable%: 0.1193`). Each block is introduced by one sentence that states the outcome ("To load a PEFT model for inference:").

**Value tables.** Pipe tables with `| --------- | ---- |` delimiters and no alignment colons; GitHub centres header cells, left-aligns body cells and stripes alternate rows. Cells combine two numbers with a slash ("47.14GB GPU / 2.96GB CPU") and use "OOM GPU" where a setting fails. No bold best values. Each table is followed by a paragraph that states the conclusion in words.

**Link bullets.** `*` bullets that start with "Learn how to …" or a linked guide title, mixing blog, Hugging Face and Colab links.

**Citation.** "To use 🤗 PEFT in your publication, please cite it by using the following BibTeX entry." then a `bibtex` block with column-aligned `=` signs.

## Imagery

The README has no images. Nothing uses `<img>`, Markdown image syntax, `<picture>` or a video link; the 🤗 in the title and the last heading is a Unicode emoji. Visual weight comes from three sources only: the h1/h2 rules, the green tip alerts and the grey code blocks, which take up most of the tall capture. Because every visible element is GitHub-rendered text, the page follows GitHub's light and dark themes without any extra work, which is why the theme is `both`.

## Adapting to Other Content

- **A paper repo.** Keep the centred h1 name and h3 tagline, add one `<p align="center">` line of authors and a venue line between them and the intro, and keep the tip alert for "see the project page" pointers. Put the paper's main table where "Why you should use PEFT" sits, followed by one paragraph that states the result in words.
- **A dataset.** Replace Quickstart's two Python blocks with a `load_dataset(...)` block and a printed sample row as a trailing comment; keep the value table for split sizes.
- **A benchmark with scores.** Keep the two-column Submission Name / Accuracy table shape, right-align the score (`| ---: |`) and bold the best value; PEFT leaves both at GitHub defaults.
- **A repo that needs a teaser.** Insert one image at `width="100%"` (856px) between the tagline and the intro, but keep the first `##` as Quickstart; the code-first order is the point of this style.
- **A smaller library.** Drop the integrations tour; keep h1, h3, intro, one tip alert, Quickstart, one value table and the citation, which fits in about two screens.

## Do's and Don'ts

| Do | Don't |
|---|---|
| State what the library does in one centred h3 line under the name | Stack a logo, a banner and a badge wall above the first sentence |
| Make the first `##` a Quickstart with a one-line install | Put a long environment setup before the first runnable example |
| Show expected output as a trailing comment in the example | Leave the reader to guess what the example prints |
| Use `[!TIP]` alerts for pointers to further material | Use alerts for core instructions that must not be skipped |
| Follow every table with a sentence that states the conclusion | Leave a table of numbers without a takeaway |
| Keep the page image-free so it reads in both GitHub themes | Add a light-only screenshot without a `<picture>` dark variant |

## Agent Prompt Guide

1. "Write a library README header in GitHub Markdown: `<h1 align="center"><p>🤗 Name</p></h1>`, then `<h3 align="center"><p>one-line purpose</p></h3>`, two left-aligned prose paragraphs (what it does, what it integrates with), a `> [!TIP]` alert (rendered with the #1a7f37 bar) pointing to the docs, and one sentence of doc links. No badges, no images."
2. "Make the first section `## Quickstart`: 'Install X from pip:' and a one-line `bash` block, then a `python` block that trains and saves with the expected output as a trailing `# prints:` comment, then a second `python` block for inference introduced by 'To load … for inference:'."
3. "Add `## Why you should use X` with `###` subsections; in each, give a pipe table with `| --- |` delimiters (cells like '47.14GB GPU / 2.96GB CPU'), one paragraph that states the conclusion, and a `[!TIP]` alert for further reading. End with `## Citing X`, one sentence and a `bibtex` block."

## Similar Pages

- readme-deepseek-ai-deepseek-v3: another large organisation README that relies on GitHub alerts and many tables (six alert markers and many pipe tables in its raw Markdown), but it adds a logo, a hr and two rows of badges where PEFT has none.
- readme-seohongpark-ogbench: also a library-style README with GitHub alerts and a pip-installable package, but it opens with an SVG logo and a row of `for-the-badge` badges.
- readme-donaldssh-k-merge: a paper repo on the same topic (LoRA adapters, built on `peft`), showing the academic counterpart: centred credits, flat badges and a teaser diagram before any code.

## Quick Start

````markdown
<h1 align="center"> <p>🤗 Name</p></h1>
<h3 align="center">
    <p>One-line statement of what the library does</p>
</h3>

First paragraph: the problem and what the library does about it.

Second paragraph: what it integrates with.

> [!TIP]
> Visit the [organization](https://huggingface.co/org) to read about ... and see notebooks.

Read the [Guide A](https://example.org/a), [Guide B](https://example.org/b) and [Guide C](https://example.org/c) conceptual guides to learn more.

## Quickstart

Install Name from pip:

```bash
pip install name
```

Prepare a model for training by wrapping it with `make_model`:

```python
from name import Config, make_model

model = make_model(base_model, Config(r=16))
model.print_trainable_parameters()
# prints: trainable params: ... || all params: ... || trainable%: ...
```

To load a trained model for inference:

```python
model = Model.from_pretrained(base_model, "output-dir")
# prints something like: ...
```

## Why you should use Name

### High performance on consumer hardware

| Model | Baseline | Name |
| --------- | ---- | ---- |
| model-a (3B params) | 47.14GB GPU / 2.96GB CPU | 14.4GB GPU / 2.96GB CPU |

One paragraph stating the conclusion.

> [!TIP]
> Pointer to a blog post or further tuning advice.

## Integrations

### Library A

## Model support

## Contribute

## Citing 🤗 Name

To use Name in your publication, please cite it by using the following BibTeX entry.

```bibtex
@Misc{name,
  title =        {...},
  howpublished = {\url{https://github.com/org/name}},
  year =         {2022}
}
```
````

## Provenance

- Repo: https://github.com/huggingface/peft (`README.md`, branch `main`, last README commit 667d0c3 on 2026-07-20).
- Paper: "Orthogonal Finetuning Made Scalable", EMNLP 2025; first author Zeju Qiu. The method is implemented in PEFT, but the README does not mention this paper; its own citation entry is the PEFT library (Mangrulkar et al., 2022). The style described here is the library README, not a paper README.
- Selection: as a library README it leads with a one-line purpose, a Tip callout and runnable quickstart code, then backs the value claim with memory and accuracy tables, a code-first style worth studying.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, and `github-markdown-css` 5.8.1 for the alert, link and syntax colors, with the alert green checked against capture pixels.
- Written 2026-10-28.
