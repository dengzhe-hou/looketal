# GeoV2V — README Reference

> A film-festival one-sheet set in GitHub type: a tagline under the title, one dark poster still, and the credits rolling beneath it.

**Theme:** both

Read from `README.md` on the default branch `main` of github.com/Xiyuche/GeoV2V (last commit touching the file 9513e82, 2026-10-02; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). The teaser size and its accent colors come from `assets/images/social-preview.jpg` fetched from the repo and pixel-sampled. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The whole header is one `<div align="center">` written mostly in plain Markdown, so it uses GitHub's own heading and paragraph styles rather than HTML tags. It reads like a film poster: the short name "GeoV2V" as a centred h1 with its rule, the tagline "Change the view. Keep the dynamics." as an h3, a bold full title over a venue line with volume and pages, a row of five text links joined by middle dots (the first two bold), and then a dark 1200×630 social-preview image (856×449 rendered) that repeats the tagline in large white and lavender type over a side-by-side "recorded video / new view" pair. The authors, affiliations and a `<sub>` footnote come after the image, like credits. There are no badges at all. The body is left-aligned prose with five plain `##` sections and no emoji: a motion section that describes the project page and film in words, a three-row evidence table with right-aligned numbers and bold GeoV2V values, a local-preview section, a materials table, and a citation that ends with license and contact lines.

## Header Block

Everything down to the footnote sits inside `<div align="center">`, opened and closed with blank lines so the Markdown inside renders. Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Title** (y≈139): `# GeoV2V`. GitHub h1, 2em (32px), weight 600, centred by the div, with the 1px grey rule under it across the 856px content width.
2. **Tagline** (y≈206): `### Change the view. Keep the dynamics.` GitHub h3, 1.25em (20px), weight 600, no rule. It is a real heading, so it shows in GitHub's outline menu.
3. **Title and venue** (y≈246 and 270): `**Geometry-Grounded Video Diffusion Model for Driving Scene Generation**<br>` then `ECCV 2026 · LNCS 17012 · pp. 656–673`. One paragraph, bold title over a plain line; volume and page range are given with the venue.
4. **Link row** (y≈310): `[**Explore the project**](...) · [**Watch the film**](...) · [Paper](...) · [Author manuscript](...) · [Supplement](...)`. Five Markdown links in GitHub link blue joined by " · "; the first two are bold to mark the primary actions (project page and film), the last three plain (DOI, PDF in repo, supplement PDF in repo).
5. **Teaser** (y≈338 to 787): `<a href="https://xiyuche.github.io/GeoV2V/"><img src="assets/images/social-preview.jpg" alt="Change the view. Keep the dynamics. A matched source video and GeoV2V novel view." width="100%"></a>`. 1200×630 JPEG, 856×449 at the 920px column, linked to the project page. No caption; the `alt` carries the description.
6. **Authors** (y≈821): `Yuchen Xi* · Yuhan Guo* · ... · Ruigang Yang†<br>`. Seven unlinked names joined by " · ", with `*` and `†` typed as plain characters, not `<sup>`.
7. **Affiliations** (y≈845): `Shanghai Jiao Tong University · Shanghai Pudong Development Bank<br>`, same paragraph, no affiliation numbers.
8. **Footnote** (y≈874): `<sub>* Equal contribution · † Corresponding author</sub>`, about 12px, the last line of the div.
9. **Intro** (below the fold): left-aligned paragraph whose middle sentence is bold, then three bullets each opening with a bold phrase ending in a period ("**A complete clip as context.**"). This ends the header block.

## Badges

There are no shields.io badges, logos or image buttons anywhere in the README. The link row plays that role.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| (link row) | **Explore the project** · **Watch the film** | GitHub link blue | bold Markdown links | xiyuche.github.io/GeoV2V/, xiyuche.github.io/GeoV2V/film/ |
| (link row) | Paper · Author manuscript · Supplement | GitHub link blue | plain Markdown links | doi.org/10.1007/978-3-032-37044-0_36, assets/papers/geov2v-author-manuscript.pdf, assets/papers/supplementary.pdf |

Colors visible on the page come from the teaser image, pixel-sampled from `social-preview.jpg`: a near-black ground #0a0b10, the lavender second line "Keep the dynamics." #bba8ff, the small cyan panel labels ("ECCV 2026 / RESEARCH FILM + PROJECT", "RECORDED VIDEO / 0 m") #8ad3da, and white #ffffff for "Change the view." and the GeoV2V wordmark.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | GeoV2V | short name |
| h3 (centred) | Change the view. Keep the dynamics. | tagline; title, venue, link row, teaser, authors and footnote follow in the same div; intro paragraph and three bullets follow outside it |
| h2 | See it in motion | three paragraphs describing the project page, the 89-second film and the supplementary video, with key numbers in bold (**1, 2 and 4 m**, **1.5×**) and inline links |
| h2 | Reported evidence | a bold one-sentence claim, a three-column results table, a caveat paragraph and one closing sentence |
| h2 | Local preview | a bold filename (**preview.command**), a `sh` block, a bold local URL, a second `sh` block for the release check, a link to publishing notes |
| h2 | Materials and provenance | a two-column Material / Location table with inline-code paths, then two paragraphs on what the repo excludes and how the scene was matched |
| h2 | Citation | a `bibtex` block, a license paragraph and a `Contact:` line with a `mailto:` link |

Absent from the source: badges, news, installation, model zoo or checkpoints (the repo states model code and checkpoints are not included), table of contents, separate license section, acknowledgements, `<details>` blocks, emoji, embedded GIF or video, `---` rules.

Present but unusual: the tagline is an `###` heading rather than italic text; the authors come after the teaser; the venue line gives the LNCS volume and page range; the video and film are described in prose and linked as pages or `.mp4` files rather than embedded; the results caveats (no ground truth for shifted views, where other methods win on FID or SSIM) are stated right under the table; the citation section also carries the license terms and the contact address.

## Components

**Markdown-in-div header.** `<div align="center">` followed by a blank line, plain Markdown headings, bold text, links and one `<img>`, then a blank line and `</div>`. GitHub centres everything inside, including the h1 and h3, without per-element `align` attributes.

**Dot-joined lines.** " · " (space, middle dot, space) is the one separator used throughout: the venue line, the link row, the author list, the affiliations, the footnote and the results-table cells ("212.56 · StreetGS").

**Primary and secondary links.** In the link row, primary actions are bold links (`[**Explore the project**](...)`) and secondary ones plain; both stay GitHub link blue.

**Bold lead bullets.** Three `-` bullets, each opening with a bold full sentence fragment ending in a period, then one or two plain sentences.

**Results table.** `| Lateral shift | GeoV2V FVD ↓ | Best other method in the table |` with delimiter `| --- | ---: | ---: |`, so both number columns are right-aligned. GeoV2V values are bold (`**159.00**`); the comparison cell joins the value and method name with " · ". The ↓ arrow in the header gives the metric direction. A bold claim sentence sits above the table and a caveat paragraph below.

**Materials table.** `| Material | Location |` with `| --- | --- |`; the right column is inline code paths, sometimes several joined by commas.

**Code blocks.** Two `sh` blocks of one command each (`python3 tools/preview.py`, `python3 tools/check_release.py --archive ...`) and one `bibtex` block with aligned `=` signs and a `doi` field. No `bash` tag.

**Citation close.** The `bibtex` block, one paragraph on publication license and material terms, and `Contact: [address](mailto:...)` as the last line of the README.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| assets/images/social-preview.jpg | JPEG, dark poster | 1200×630 | `<a href="project page"><img ... width="100%"></a>` inside the centred div | 856×449 | header, after the link row and before the authors |

The teaser is the repo's social-preview card reused as the README image, which is why it has the 1.91:1 Open Graph shape. On a near-black ground (#0a0b10) it sets "Change the view." in white and "Keep the dynamics." in lavender (#bba8ff) at a size that dominates the first screen, a grey subline, small cyan (#8ad3da) uppercase labels, and two rounded frames of the same street scene (recorded view and generated new view) side by side. Because the poster carries its own dark ground and the README has no transparent images or badges, it reads the same on GitHub's light and dark themes; only the light theme was captured. It is the only image; videos are linked, not embedded, and there is no `<picture>` pair.

## Adapting to Other Content

- **A library.** Keep the div header with `# Name` and an `###` tagline, replace the title-and-venue paragraph with a one-line description, keep the dot-joined link row (Docs · Install · Examples) and drop the poster if there is no strong visual.
- **A dataset.** Keep the full header and replace "Reported evidence" with a statistics table in the same shape: right-aligned number columns, a bold claim sentence above and a caveat paragraph below.
- **A method repo with code.** Add "Installation" and "Usage" sections after the intro, each with one short `sh` block, and keep the evidence table after them.
- **A repo without a poster.** Let the authors and footnote follow the link row directly; do not substitute a badge row.
- **A repo with video.** Keep describing the video in a "See it in motion" section and link it; if a GIF is used, place it where the poster is at `width="100%"` (856px).

## Do's and Don'ts

| Do | Don't |
|---|---|
| Use one separator (" · ") for every inline list in the page | Mix pipes, bullets and dots across rows |
| Mark the primary links in bold and leave secondary links plain | Turn every link into a badge |
| Put a poster with its own dark ground at `width="100%"` and link it to the project page | Use a transparent figure with dark labels if the poster must work on both themes |
| State the claim in bold above a results table and the caveats directly below it | Leave the comparison without metric direction or caveats |
| Right-align number columns with `---:` and bold only your own values | Bold every best value without saying what is compared |
| Say in prose what the repo does not contain | Imply that model code or data are included when they are not |

## Agent Prompt Guide

1. "Write a GitHub README header inside `<div align="center">` (blank line after the opening and before the closing tag) in plain Markdown: `# Name`, `### Short tagline.`, a bold full title with `<br>`, a venue line 'Venue Year · LNCS Vol · pp. a–b', a link row of five links joined by ' · ' with the first two bold, a `width="100%"` dark poster image (1200×630, ground #0a0b10, accent #bba8ff, labels #8ad3da) linked to the project page, then authors joined by ' · ' with plain `*` and `†`, affiliations, and a `<sub>` footnote. No badges."
2. "After the header, write a left-aligned intro with one bold sentence and three bullets that each open with a bold phrase ending in a period. Then five plain `##` sections with no emoji and no `---` rules: See it in motion, Reported evidence, Local preview, Materials and provenance, Citation."
3. "In Reported evidence, write a bold one-sentence claim, then a table with `| --- | ---: | ---: |`, a ↓ arrow on the metric header, your values in bold and comparison cells as 'value · Method', then a caveat paragraph. Use `sh` blocks for single commands, a two-column Material / Location table with inline-code paths, and end with a `bibtex` block, a license paragraph and a `Contact:` mailto line."

## Similar Pages

- **readme-chuan-10-agile**: the same `<div align="center">` with `# Name` and an `###` subtitle in plain Markdown, followed by `for-the-badge` badges where GeoV2V uses a dot-joined text link row.
- **readme-drexubery-viewcrafter**: another video-diffusion novel-view repo, with a badge row and logo where GeoV2V has only text links and a poster.
- **readme-eku127-satnav**: also opens with a centred name, a full-width teaser and a two-column resource table, but with a uniform shields.io badge row and authors before the teaser.

## Quick Start

````markdown
<div align="center">

# Name

### Short tagline. Second short clause.

**Full Paper Title on One Line**<br>
Venue Year · LNCS Volume · pp. 000–000

[**Explore the project**](https://example.github.io/project/) · [**Watch the film**](https://example.github.io/project/film/) · [Paper](https://doi.org/xx) · [Author manuscript](assets/papers/manuscript.pdf) · [Supplement](assets/papers/supplementary.pdf)

<a href="https://example.github.io/project/"><img src="assets/images/social-preview.jpg" alt="Describe the poster." width="100%"></a>

Author One* · Author Two* · Author Three · Author Four†<br>
Institution A · Institution B<br>
<sub>* Equal contribution · † Corresponding author</sub>

</div>

Context sentence. **The one-sentence claim of the method.** One sentence on how it works.

- **First idea.** One or two sentences.
- **Second idea.** One or two sentences.
- **Third idea.** One or two sentences.

## See it in motion

Paragraph describing the [project page](https://example.github.io/project/) and the [film](https://example.github.io/project/film/), with key numbers in **bold**.

## Reported evidence

**One-sentence claim the table supports.**

| Setting | Name Metric ↓ | Best other method in the table |
| --- | ---: | ---: |
| Setting A | **0.00** | 0.00 · Method |
| Setting B | **0.00** | 0.00 · Method |

Caveat paragraph: what the metric does and does not show, and where other methods do better.

## Local preview

Run:

```sh
python3 tools/preview.py
```

Open **http://127.0.0.1:8765/**.

## Materials and provenance

| Material | Location |
| --- | --- |
| Interactive page | `index.html` |
| Paper figures | `assets/images/` |

One paragraph on what this repository does not include.

## Citation

```bibtex
@InProceedings{key2026,
  title     = {...},
  year      = {2026},
}
```

License paragraph.

Contact: [name@example.org](mailto:name@example.org).
````

## Provenance

- Repo: https://github.com/Xiyuche/GeoV2V (`README.md`, branch `main`, last README commit 9513e82 on 2026-10-02). The README states this is the project-page repository; model code, checkpoints and the full Para4D dataset are not included.
- Paper: "GeoV2V: Geometry-Grounded Video Diffusion Model for Driving Scene Generation", ECCV 2026 (LNCS 17012, pp. 656–673, DOI 10.1007/978-3-032-37044-0_36); first author Yuchen Xi. Project page https://xiyuche.github.io/GeoV2V/.
- Selection: plain text in the README itself carries an editorial header (name, tagline, citation line, link row) and a film-poster teaser, and a compact evidence table and materials table show restraint without any badges.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, and `assets/images/social-preview.jpg` fetched from the repo for its size and sampled colors.
- Written 2026-10-28.
