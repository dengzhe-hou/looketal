# DLLM Survey — README Reference

> A survey's companion shelf: the paper's title and a quoted citation card up top, two wide figures from the paper, then a long table of contents and thirty-three narrow two-column lists of papers, each with a way back to the top.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/LiQiiiii/DLLM-Survey (last commit touching the file 3251592 "Update README.md", 2026-08-30; read 2026-11-12). Evidence is the raw Markdown (477 lines, 42,755 bytes), the HTML that GitHub's API returns for it, a first-screen capture at a 968×605 window and a 968×1815 tall capture (the README column is 920px wide, 856px content width), a full-length 968px capture (the rendered README ends at about y≈16,850), the shields.io SVGs for the five badge URLs, and `assets/ar_vs_diff.png` and `assets/timeline.png` fetched from the repo. y values below are in the 968px-wide frame at scale 1, where the README box starts at y≈24 with its "README.md" file bar. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; the README changes nothing about them and has no emoji in any heading.

## Overview

The page opens on the survey's title, not the repository's name. Inside a `<div align="center">` the paper title is an `<h2>` in bold with GitHub's grey rule under it, and a one-line `<h4>` subtitle follows. Below them a second centred div holds the badges in two rows, a lone teal arXiv badge and then four badges (GitHub stars, forks, last commit, PRs Welcome). The paper itself is introduced by one plain sentence and a blockquote that reads like a citation card, with the linked title in bold, three linked authors with asterisk, dagger and affiliation superscripts, the journal in italics, the affiliation, an equal-contribution note and the corresponding author's email. Two full-width figures from the paper follow, a dense comparison of autoregressive and discrete diffusion models (856×753 at the column) and a model timeline (856×303), each with a bold centred caption. Then the page turns into a list. An h2 "Citation" holds the BibTeX, a blockquote between two rules asks for stars and pull requests, an intended taxonomy figure is missing, and an h3 "Quick Links" opens a nested bullet table of contents with 38 entries. The rest, about 14,000px, is 33 tables of the same two-column form (Title & Authors, Links), one per h4 topic, each preceded by a "🔝 Back to Top" link, holding 128 papers in all. It ends with two plain links under "Toolkits".

## Header Block

The header is split across two centred divs, and the paper block after them is left-aligned.

1. **Title** (y≈135, rule at y≈155): `<div align="center">` then `<h2><b> Discrete Diffusion in Large Language and Multimodal Models: A Survey </b></h2>`. An HTML h2 (1.5em, 24px, weight 600, already bold so the `<b>` changes nothing) with GitHub's h2 rule spanning the full 856px. There is no h1 and no logo.
2. **Subtitle** (y≈190): `<h4> An overview of research in discrete diffusion large language and multimodal models</h4>`, a 16px bold heading, centred, then `</div>`.
3. **arXiv badge** (y≈216–235): in a second `<div align="center">`, `<a href="https://arxiv.org/pdf/2506.13759" target="_blank"><img src="https://img.shields.io/badge/arXiv-2506.13759-009688.svg" alt="arXiv"></a>`, followed by a blank line, so it stands alone on its row. 116×20, flat. It links to the PDF, not the abstract page.
4. **Badge row** (y≈259–277): four Markdown image lines on consecutive source lines, joined by single spaces into one row about 395px wide (88, 78, 122 and 92px badges). Two of them are unlinked `![](...)` images. Details in Badges. The div closes, followed by five blank lines that add nothing to the render.
5. **Lead sentence** (y≈312): `This repository is for our paper:`, plain 16px text, left-aligned.
6. **Citation card** (y≈343–482): a blockquote whose lines end in ` \` (Markdown hard breaks), so six lines sit in one quote with GitHub's grey text and left bar.
   - `> **[Discrete Diffusion in Large Language and Multimodal Models: A Survey](https://arxiv.org/pdf/2506.13759)** \` bold link-blue title.
   - `> [Runpeng Yu*](...)<sup>1</sup>, [Qi Li*](...)<sup>1</sup>, [Xinchao Wang](...)<sup>†1</sup> \` three Google Scholar links. The asterisks are inside the link text, the dagger inside the `<sup>`.
   - `> *Transactions on Machine Learning Research* \` the venue in italics, with no year.
   - `> <sup>1</sup>National University of Singapore, Singapore \`
   - `> <sup>*</sup>Equal contribution, random order. \`
   - `> <sup>†</sup>Corresponding author: xinchao@nus.edu.sg` (GitHub autolinks the address).
7. **Figure 1** (y≈507–1260, caption y≈1269): `<p align="center"><img src="assets/ar_vs_diff.png" alt="Diagram 2" style="max-width:100%;" /><br /><strong>Figure 1. Difference between autoregressive models and discrete diffusion models.</strong></p>`. The PNG is 7089×6238 (1.4 MB), so it is shrunk to 856×753 by GitHub's own `max-width: 100%` (the inline `style` is stripped by GitHub's sanitizer).
8. **Figure 2** (y≈1300–1603, caption y≈1621): the same recipe for `assets/timeline.png`, 7516×2664 (1.3 MB), rendered at 856×303, captioned `Figure 2. A timeline of existing dLLMs and dMLLMs in recent years.` Its alt text is also "Diagram 2".

The first screen (605px tall) ends about 100px into Figure 1, so it shows the title, subtitle, both badge rows, the full citation card and the top of the figure's two column headers, "Autoregressive (M)LLM" and "Discrete Diffusion (M)LLM". The venue appears twice, as the italic line in the card and as `journal={Transactions on Machine Learning Research}` in the BibTeX, but no badge names it.

## Badges

All five are 20px tall. The arXiv, last-commit and PRs badges are default `flat` shields.io badges with the label on #555555 and white (#ffffff) text. The stars and forks badges come from shields.io's `github/stars` and `github/forks` endpoints, which render in the `social` style by default, so their `?color=yellow` and `?color=lightblue` parameters have no visible effect.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| arXiv | 2506.13759 | #009688 (from the URL, `-009688.svg`) | flat, 116×20 | arxiv.org/pdf/2506.13759 (new tab) |
| Stars (GitHub mark) | 391 (live) | #fcfcfc label with #333333 text, white count box | social, 88×20 | not linked (GitHub wraps it in a link to the image itself) |
| Forks (GitHub mark) | 5 (live) | #fcfcfc label with #333333 text, white count box | social, 78×20 | not linked |
| last commit | august (live) | #67ac09 (`green`) | flat, 122×20 | not linked |
| PRs | Welcome | #007ec6 (`blue`) | flat, 92×20 | github.com/LiQiiiii/DLLM-Survey/pulls |

The stars and forks URLs still use the repository's older name, `LiQiiiii/Discrete-Diffusion-Large-Language-Models-Survey`, while the last-commit badge and the PRs link use `DLLM-Survey`. GitHub redirects the old name, so the stars badge renders the current 391 and the forks badge 5, both matching the repository. The row is plain repository status. It has no paper-page or code badge, and the venue is not a badge.

Other colors on the page are GitHub's own, not chosen by the author: link blue #0969da, the quote bar and the two `---` rules #d1d9e0, and the table rules and zebra striping (#f6f8fa). Both figures are opaque white (#ffffff) PNGs with pale peach and pale green panels and dark red-and-blue diagram accents, so they show as white panels in GitHub's dark theme.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h2 (centred by the div, ruled) | Discrete Diffusion in Large Language and Multimodal Models: A Survey | the title |
| h4 (centred) | An overview of research in discrete diffusion large language and multimodal models | the subtitle, then the badges, the citation card and Figures 1 and 2 |
| h2 | Citation | a BibTeX block with no language tag, then a `---` rule, a blockquote with two emoji lines (🌟, 🙋) and a bold "To add new papers or models" paragraph, another `---` rule and the missing taxonomy image |
| h3 | Quick Links | a nested bullet list, 9 top entries and 29 sub-entries, all anchor links |
| h3 | Mathematics | five h4 topics (Discrete Diffusion Model and Transition Matrix, Simplified Masked Diffusion Model, Continuous Time Discrete Denoising Models, Concrete Score, Reparameterized Discrete Diffusion Model) |
| h3 | Modeling Language Diffusion | one table directly under the h3 |
| h3 | Representative Model | four h4 topics (around 1B, Large Diffusion Language Models, Large Diffusion Multimodal Models, Large Unified Models) |
| h3 | Training Techniques | seven h4 topics, from Initialization Technique to Training-Testing Input Discrepancy, including Reinforcement Learning |
| h3 | Inference Techniques | eight h4 topics, from Unmasking Techniques to Response Length Control |
| h3 | Quantization | one table |
| h3 | Privacy and Safety | one table |
| h3 | Applications | six h4 topics, from Text Generation and Style Control to Biological and Drug Discovery |
| h3 | Toolkits | two bullets, `Name: URL` with bare GitHub URLs |

Absent from the source: an h1 and a logo, a news section, a code badge or project page link (there is none), install or usage instructions (the only code is `generate_item.py` for contributors), a license section or file (the repo has no license), a contact section apart from the emails in the card and the contribution note, any `<details>` folding, any date, venue or code column in the paper tables, a star-history chart.

Present but unusual: the page's top heading is an h2 and the next real section ("Citation") is also an h2, so the title and the BibTeX share a level while every list section sits one level below at h3; the subtitle is an h4 used for size; the Citation section comes before the table of contents; a hidden date note `[//]: #06/17` (month and day the row was added) trails every one of the 128 table rows as a third cell that GitHub drops because the header has two columns; the "Back to Top" link sits under each of the 30 h4 headings and the three h3 sections that have no h4 (33 in all); the Quick Links list leaves out the "Reinforcement Learning" h4.

## Components

**Citation card.** A blockquote of six lines held together by trailing ` \` hard breaks: bold linked title, linked authors with `*` inside the link and `<sup>1</sup>` or `<sup>†1</sup>` after it, the venue in `*italics*`, then `<sup>`-numbered affiliation, equal-contribution and corresponding-author lines.

**Figure with caption.** `<p align="center"><img src="assets/NAME.png" alt="..." style="max-width:100%;" /><br /><strong>Figure N. Sentence.</strong></p>`. The images are very large PNGs (about 7,000px wide) that GitHub scales to 856px, and the caption is bold 16px, centred.

**Nested link list.** `### Quick Links` then `- [Section](#section)` with two-space-indented `  - [Topic](#topic)` children, rendered as GitHub's disc and circle bullets in link blue, 28px per line. It runs about 1,050px tall (y≈2243–3300).

**Topic block.** Every topic repeats the same three parts.

```markdown
#### Topic Name
[🔝 Back to Top](#quick-links)

| Title & Authors | Links |
|:--|:---:|
|[Paper title](https://arxiv.org/abs/ID) <br> Author One, Author Two |[Paper](https://arxiv.org/abs/ID)|[//]: #MM/DD
```

The first column is left-aligned, the second centred (`:---:`). The title links to the paper and the authors follow on a second line after `<br>`, so each row is two or three lines tall (about 61px for two lines). The Links cell repeats the same URL as a single "Paper" link; no row has a code link. GitHub sizes each table to its content, so the 33 tables have different widths, from about 780px to the full 856px, and none scrolls sideways. The h4 headings are 16px bold, and the "🔝" emoji renders as GitHub's purple TOP arrow before "Back to Top".

**Contribution note.** A blockquote between two `---` rules with two emoji-led lines (`> 🌟 If you find this resource helpful...`, `> 🙋 Please let us know...`), a bold line "To add new papers or models" and a paragraph that names `generate_item.py` in inline code and gives a contact email.

**Citation block.** An unlabelled fenced block (no language tag) with `@article{yu2025discrete,` and `journal={Transactions on Machine Learning Research}`, `year={2026}`.

**Toolkits.** `* Open-dLLM: https://github.com/pengzhangzhi/Open-dLLM`, plain bullets with bare URLs that GitHub autolinks.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| ar_vs_diff.png | paper figure, a four-row grid (Model Architecture, Attention Mask, Inference, Training) comparing an autoregressive and a discrete diffusion (M)LLM | 7089×6238 PNG, opaque, 1.4 MB | `<img ... style="max-width:100%;" />` in `<p align="center">` | 856×753 | after the citation card |
| timeline.png | paper figure, a 2021–2025 timeline with four lanes (Models ≤ 1B, Language Models, MultiModal Models, Unified Models) and institution logos beside each model name | 7516×2664 PNG, opaque, 1.3 MB | the same recipe | 856×303 | after Figure 1 |
| taxonomy.png | intended taxonomy figure | missing from `assets/` | `<img src="assets/taxonomy.png" width = "95%" alt="" align=center />` in `<p align="center">` | nothing (empty alt, a gap of about 70px) | between the contribution note and Quick Links |
| 🔝 emoji | GitHub emoji image | 20px | `[🔝 Back to Top](#quick-links)` | about 20px | above every table |

Only the two paper figures render. Both are light-only images with no `<picture>` alternative. The taxonomy figure is referenced in the Markdown, but the repository's `assets/` folder holds only `ar_vs_diff.png` and `timeline.png`, so the request returns GitHub's 404 page and nothing is drawn.

## Adapting to Other Content

- **A survey paper list.** Keep the centred title and subtitle, one arXiv badge on its own row, the blockquote citation card with hard breaks, and one or two paper figures at `max-width:100%` (856px) with bold numbered captions. Put the table of contents before the lists and keep the two-column Title & Authors | Links tables with a back-to-top link per topic.
- **A long list (over 100 entries).** Fold each h3 group into `<details>` so the page is not 14,000px of open tables, or add a date or venue column so readers can sort by time.
- **A benchmark or leaderboard.** Replace the Links column with score columns, right-aligned (`| ---: |`), and keep the title-over-authors first cell.
- **No paper figure.** Move the Quick Links list directly under the citation card; the header then ends at about 500px.
- **Images.** Export figures at about 2× the 856px column (1,700px wide) rather than 7,000px, so the README does not load several megabytes of PNG.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Put the paper title in a single h1 and use h2 for sections | Use an h2 for the title and another h2 for Citation, so headings skip levels |
| Keep every image in `assets/` that the Markdown references | Leave `assets/taxonomy.png` in the README after the file is gone |
| Update badge URLs when the repository is renamed | Leave stars and forks badges on the old repository name |
| Give each figure its own alt text | Label both figures "Diagram 2" |
| List every topic heading in the table of contents | Leave "Reinforcement Learning" out of Quick Links |
| Tag the BibTeX block as `bibtex` | Leave the citation fence without a language |
| Link to the arXiv abstract page from the badge | Send the badge straight to the PDF |
| Check duplicated rows when pasting from a generator | Give two different papers the same title |

## Agent Prompt Guide

1. "Write a centred README header inside `<div align="center">`: an `<h2><b>Paper Title</b></h2>` and an `<h4>` one-line subtitle, then close the div. In a second centred div put one flat arXiv badge alone on its row (`arXiv-ID-009688` in #009688 with label #555555, linking to the paper), a blank line, and a row of four badges on consecutive lines: shields.io `github/stars` and `github/forks` (social style, #fcfcfc), `last-commit` with `color=green` (#67ac09) and `PRs-Welcome-blue` (#007ec6) linking to the pull requests."
2. "After the header write `This repository is for our paper:` and a blockquote citation card with ` \` hard breaks: the bold linked title, linked authors with `*` for equal contribution and `<sup>1</sup>` affiliations, the venue in italics, then `<sup>`-numbered affiliation, equal-contribution and corresponding-author lines. Follow it with two `<p align="center">` figures at `max-width:100%` (856px), each with a bold `Figure N.` caption."
3. "Write an h2 Citation with a BibTeX block, a contribution note in a blockquote between two `---` rules, then `### Quick Links` as a nested anchor list. For every topic write `#### Topic`, a `[🔝 Back to Top](#quick-links)` line and a two-column table `| Title & Authors | Links |` aligned `|:--|:---:|`, where each row is `[Title](url) <br> Authors` and a centred `[Paper](url)` link."

## Similar Pages

- readme-sophtang-awesome-continuous-language-models: another survey's paper list on diffusion-family language models, but it has a taxonomy table with venue and code columns and folds families into `<details>`, where this one keeps 33 open two-column tables.
- readme-kuleshov-group-bd3lms: a method README for Block Diffusion, one of the papers listed here under Modeling Language Diffusion.
- readme-eku127-satnav: also a centred academic header with superscript affiliations, but the authors sit in the centred block, where this one moves them into a left-aligned blockquote.

## Quick Start

````markdown
<div align="center">

  <h2><b> Survey Title </b></h2>
  <h4> One-line overview of the field</h4>

</div>

<div align="center">

<a href="https://arxiv.org/abs/XXXX.XXXXX" target="_blank"><img src="https://img.shields.io/badge/arXiv-XXXX.XXXXX-009688.svg" alt="arXiv"></a>

![](https://img.shields.io/github/stars/OWNER/REPO)
![](https://img.shields.io/github/forks/OWNER/REPO)
![](https://img.shields.io/github/last-commit/OWNER/REPO?color=green)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-blue)](https://github.com/OWNER/REPO/pulls)

</div>

This repository is for our paper:

> **[Survey Title](https://arxiv.org/abs/XXXX.XXXXX)** \
> [Author One*](https://example.org/)<sup>1</sup>, [Author Two*](https://example.org/)<sup>1</sup>, [Author Three](https://example.org/)<sup>†1</sup> \
> *Journal Name* \
> <sup>1</sup>University Name, Country \
> <sup>*</sup>Equal contribution. \
> <sup>†</sup>Corresponding author: name@example.edu

<p align="center">
  <img src="assets/figure1.png" alt="Comparison of model families" style="max-width:100%;" /><br />
  <strong>Figure 1. One-sentence caption.</strong>
</p>

## Citation

```bibtex
@article{key2026survey,
  title={Survey Title},
  author={One, Author and Two, Author},
  journal={Journal Name},
  year={2026}
}
```

---
> 🌟 If you find this resource helpful, please star this repository and cite our [work](#citation).
>
> **To add new papers or models**
>
> Open a pull request, or email the links to your paper and code.

---

### Quick Links

- [Section](#section)
  - [Topic](#topic)

### Section

#### Topic
[🔝 Back to Top](#quick-links)

| Title & Authors | Links |
|:--|:---:|
|[Paper title](https://arxiv.org/abs/ID) <br> Author One, Author Two |[Paper](https://arxiv.org/abs/ID)|

### Toolkits
* Tool name: https://github.com/OWNER/TOOL
````

## Provenance

- Repo: https://github.com/LiQiiiii/DLLM-Survey (`README.md`, branch `main`, last README commit 3251592 on 2026-08-30; 391 stars, no license file). The repository was earlier named Discrete-Diffusion-Large-Language-Models-Survey, which two badge URLs still use.
- Paper: "Discrete Diffusion in Large Language and Multimodal Models: A Survey", Runpeng Yu, Qi Li, Xinchao Wang (National University of Singapore), Transactions on Machine Learning Research 2026, arXiv 2506.13759. There is no separate project page.
- Selection: added on the maintainer's suggestion, outside the selection rounds and the pool rules. The README pool only took repositories linked from accepted-venue project pages, and this survey has none. It is the gallery's second paper-list README, notable for a citation card in a blockquote, two large paper figures and a long run of identical two-column topic tables.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-11-12), a 968×605 first-screen capture, a 968×1815 tall capture and a full-length 968px capture at a 920px README column, shields.io SVGs for the five badge URLs, the two figure PNGs fetched for size and opacity, and the repository's file listing for `assets/`.
- Defects seen: `assets/taxonomy.png` is missing, so the taxonomy figure renders as an empty gap; the stars and forks badges point at the old repository name (they still render correctly through GitHub's redirect); the arXiv 2402.14407 row in Vision and Multimodal repeats the title of the row above ("Underwater Diffusion Attention Network ...") with different authors; the Sohl-Dickstein et al. row links to the NeurIPS 2021 PDF of the structured denoising paper in the next row; Quick Links omits Reinforcement Learning; the author "Junbo Yin" is typed "YJunbo Yin"; the contribution note says "emal"; both figures share the alt text "Diagram 2"; the BibTeX key says 2025 while the year is 2026.
- Written 2026-11-12.
