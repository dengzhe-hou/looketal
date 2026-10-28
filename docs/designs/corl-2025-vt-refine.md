# VT-Refine Two-Tone Nerfies — Style Reference

> A crowded but orderly lab poster: sky-blue "Visuo" and violet "Tactile" in the title, three institution logos, a red award line and six dark pills over a wide real-versus-sim video.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, loaded fonts, color share), selector probes of the title spans, affiliation block, award line, buttons, teaser video, paper-thumbnail strip, section headings and footer, the 1440×900 and full-page screenshots, and the page's `static/css/index.css`, Bulma 0.9 and `index.html`. Several sizes and colours come from inline styles in the markup (title keyword spans, the affiliation h3, logo widths, the grey caption line, the award `<font color="firebrick">`); each was checked on the rendered element. The teaser autoplays, so the screenshot shows one frame.

## Overview

A long Nerfies-template page (about 11,300px tall) on white. The header is dense and centred: a slim white navbar with a home icon and a "More Related Research" dropdown; a two-line Google Sans title in which "V" and "Visuo" are sky blue (#46b1f0) and "T" and "Tactile" are violet (#9b59b6) (two flat colours, not a gradient); eleven sky-blue author links with superscripts; a small affiliation and footnote block; a row of three institution logos (Columbia, NVIDIA, UC San Diego); the venue line "Conference on Robot Learning (CoRL) 2025"; a "Best Paper Award" line in firebrick; and six dark pill buttons. Directly below, a 32px headline claim, a light-grey "Left: … Right: …" caption and a near-full-width side-by-side video of the real robot and its tactile heatmaps against the simulated twin. Further down: a justified Abstract, a bordered strip of paper-page thumbnails linking to the PDF, a YouTube summary video, paired hardware and simulation videos, capability experiment grids, BibTeX, a related-research list with thumbnails and a light footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white family #ffffff / #fdffff / #fffffd 66.8%; pale grey-blue #dee6ea 7.2% (simulation floor and lab background in the teaser); warm grey #97948e 6.9% (tabletop); brown #6c5550 6.7% (orange gripper parts in shade); dark violet #2f213b 6.3% and plum #48044c 6.1% (the purple tactile heatmap panels and dark grippers). Text accents are too thin to form clusters.

Anatomy in DOM order (desktop 1440px, everything centred):

1. **Navbar** (`nav.navbar`, 0–52px, #ffffff): centred `navbar-start` with a Font Awesome home icon (40px item) and "More Related Research" (16px #4a4a4a, Bulma dropdown arrow in #3273dc) that opens links to two sibling projects. Hero-body padding-top 48px.
2. **Title** (`h1.title.is-2.publication-title`, y=100, 90px tall): Google Sans 40px/600 (synthesized from the 400 face), line-height 45px, #363636, two lines split by `<br>`; inline spans colour "V" and "Visuo" #46b1f0 and "T" and "Tactile" #9b59b6. Margin-bottom 24px.
3. **Authors** (`.publication-authors.is-size-5`, y=214, two lines): Google Sans 20px/400, links #209cee, numeric superscripts, † for equal advising.
4. **Affiliations and notes** (inline-styled `h3`, y=283, 55px): Google Sans 16px (80%) #2d2e2e, two lines: "¹ Columbia University ² NVIDIA ³ University of California, San Diego" and "* Work partially done at internship † Equal advising".
5. **Logo row** (y=338–391): three inline images at 30%, 25% and 20% of the 960px column (288, 240, 192px wide), separated by non-breaking spaces; a `<br>` follows.
6. **Venue** (`h1.title.is-4`, y=421): "Conference on Robot Learning (CoRL) 2025", Google Sans 24px/600 #363636. Gap 24px.
7. **Award** (`h1.title.is-5`, y=472): "Best Paper Award" in bold firebrick (#b22222) then " at IROS 2025 AHFHR Workshop", 20px/600 #363636, ending in a "[Link]" in #3273dc.
8. **Buttons** (y=512, 40px tall): arXiv, Open Review, Poster, Video, Twitter, Code; Bulma dark pills about 4px apart.
9. **Teaser claim** (`h2.title.is-3`, y=593): "Our Visuo-Tactile Diffusion Policy can be Fine-Tuned in Simulation Using RL!", Noto Sans 32px/600 #363636. Gap 24px.
10. **Teaser caption** (`h2.title.is-5`, y=653): "Left: Fine-Tuned Policy Rollout in Real-World … Right: Fine-Tuned Policy Rollout in Simulation", 20px/600 in #bdbdbd (inline), spaced with eight non-breaking spaces. Gap 24px.
11. **Teaser video** (y=699, 1307×447 at x=67): `width=99%`, radius 10px, autoplay, loop, controls; the fold cuts it.

Arithmetic check: 52 + 48 = 100; 100 + 90 + 24 = 214; authors 214–274 (two 30px lines) plus 9px of line box = 283; 283 + 55 = 338; 338 + 53 = 391, then a `<br>` (24px) and a 6px line gap = 421; 421 + 27 + 24 = 472; 472 + 23 + 24 − 12 (columns margin) + 5 (button margin) = 512; 512 + 40 + 5 − 12 + 48 (hero padding) = 593; 593 + 36 + 24 = 653; 653 + 23 + 24 ≈ 699.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #ffffff | (Bulma) | page, navbar |
| Title Ink | #363636 | (Bulma `$grey-darker`) | title, venue, award line text, section headings, dark button fill |
| Body Ink | #4a4a4a | (Bulma `$text`) | body text, navbar link, footer |
| Visuo Blue | #46b1f0 | (inline span) | "V" and "Visuo" in the title |
| Tactile Violet | #9b59b6 | (inline span) | "T" and "Tactile" in the title |
| Author Blue | #209cee | (`hsl(204, 86%, 53%)`) | author links |
| Affiliation Ink | #2d2e2e | (inline) | affiliation and footnote block |
| Award Red | #b22222 | (`<font color="firebrick">`) | "Best Paper Award" |
| Link Blue | #3273dc | (Bulma `$link`) | "[Link]", navbar dropdown arrow, in-text links |
| Caption Grey | #bdbdbd | (inline) | teaser "Left / Right" caption |
| Strip Border | #888888 | (inline) | 1px border around the paper-thumbnail strip |
| Code Grey | #f5f5f5 | (Bulma `pre`) | BibTeX block |
| Footer | #fafafa | (Bulma `.footer`) | footer band |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Title / authors | 'Google Sans', sans-serif (Google Fonts link, regular only) | Google Sans 400; 600 is synthesized | Product Sans / Outfit |
| Body / headings | 'Noto Sans', sans-serif | Noto Sans 400; 600 is synthesized | Noto Sans |
| Code | monospace | Consolas on Windows | JetBrains Mono |
| Icons | Font Awesome, Academicons | Academicons 400 (Font Awesome via its own CSS) | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.title.is-2.publication-title` | 40px / 600 / 45px | #363636; keywords #46b1f0, #9b59b6 |
| Authors | `.publication-authors.is-size-5` | 20px / 400 / 30px | links #209cee |
| Affiliations | inline `h3` (font-size 80%) | 16px / 400 / 24px | #2d2e2e |
| Venue | `h1.title.is-4.publication-title` | 24px / 600 / 27px | #363636 |
| Award | `h1.title.is-5.publication-title` | 20px / 600 / 22.5px | #b22222 lead, #363636 rest |
| Section heading | `h2.title.is-3` | Noto Sans 32px / 600 / 36px, centred | #363636 |
| Sub-heading | `h2.title.is-4`, `h2.title.is-5` | 24px / 600 and 20px / 600 | #363636 |
| Teaser caption | `h2.title.is-5` (inline colour) | 20px / 600 | #bdbdbd |
| Body | `.content p` | 16px / 400 / 24px, justified | #4a4a4a |
| Button | `.button.is-normal` | 16px / 400 | #ffffff |
| BibTeX | `pre` | 14px / 21px monospace | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link buttons | 290486px (pill) | 1px transparent | none |
| Teaser and grid videos | 10px (inline) | none | none |
| YouTube embed | 10px (`.publication-video`) | none | none |
| Paper-thumbnail strip | 0 | 1px #888888 | none |
| Institution logos | 0 | none | none |
| BibTeX | 0 | none | none |

## Layout Metrics

- **Header column**: `.container.is-max-desktop` 960px at x=240; hero-body padding 48px 24px.
- **Teaser and sections**: plain `.container` 1344px at x=48 (widescreen); the teaser sits in a bare `.columns` wrapper (−12px margins) with 12px column padding, so the heading spans 1320px at x=60 and the video 1307px.
- **Sections**: Bulma `.section` padding 48px 24px; the Abstract paragraph runs the full 1344px, justified.
- **Thumbnail strip**: 1342×193 image at y=1477 inside a 1px #888888 frame, linking to the camera-ready PDF.
- **Paired media**: two `.column`s of 660px with a 24px gutter (Hardware Resources / Penetration-based Tactile Model); experiment grids repeat this pattern with 20px/600 "Trial N" titles.
- **Related research**: rows with a thumbnail on the left and text at x=390 (1002px wide).
- **Footer**: #fafafa, padding 48px 24px 96px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1408px (1440 render) | 48px outside a 1344px container | 16px | 40px | paired media in two 660px columns |
| 1216–1407px | container 1152px | 16px | 40px | same |
| 1024–1215px | container 960px | 16px | 40px | same |
| ≤1023px | Bulma navbar collapses to a burger | 16px | 40px | same columns until 769px |
| ≤768px | 24px section padding | 16px | 40px (Bulma `is-2`) | columns stack; logos stay inline at their percentage widths |

## Components

- **Two-colour keyword title**: Google Sans 40px/600 #363636 on two manual lines; the acronym letters and the matching words are coloured per concept (#46b1f0 for vision, #9b59b6 for touch).
- **Logo row**: three institution logos inline, sized 30% / 25% / 20% of the 960px column, separated by three non-breaking spaces each, sitting between the affiliation block and the venue line.
- **Award line**: Bulma `title is-5`, a bold #b22222 "Best Paper Award" followed by plain #363636 text and a #3273dc "[Link]".
- **Dark pill button** (Bulma `.button.is-dark.is-rounded`): #363636, #ffffff 16px text, 40px tall, padding 7px 20px, icon left (Academicons arXiv, Font Awesome PDF, YouTube, Twitter, GitHub).
- **Claim-over-teaser block**: 32px/600 headline, a 20px/600 #bdbdbd Left/Right caption, then a 99%-width video with 10px radius.
- **Paper strip**: a single wide image of the paper's pages in a 1px #888888 frame, clickable to the PDF.
- **Related research row**: small thumbnail left, bold paper title and authors right, 16px #4a4a4a.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navbar | yes | white bar with home icon and a related-research dropdown |
| Title / authors / affiliations | yes | two-colour keyword title, sky-blue authors, small dark affiliation block |
| Institution logos | yes | three inline logos |
| Venue / award | yes | 24px venue, firebrick award lead |
| Link buttons | yes | six dark pills |
| Teaser | yes | headline claim, grey caption, wide real-vs-sim video |
| Abstract | yes | full-width justified paragraph |
| Paper thumbnails | yes | bordered strip of page previews |
| Summary video | yes | rounded YouTube embed |
| Paired media sections | yes | two-column videos with 20px titles |
| BibTeX | yes | grey `pre` |
| Related research | yes | thumbnail rows |
| Footer | yes | #fafafa credit line |
| Results table | absent from the source | results shown as videos and figures |

## Adapting to Other Content

- **More authors**: keep the 20px #209cee links with superscripts inside the 960px column; eleven names take two lines, so a list of twenty takes about four. Keep affiliations in the 16px #2d2e2e block below.
- **A results table**: place it in a 1344px `.section` under a 32px/600 heading; Bulma `.table` at 16px #4a4a4a with #363636 600 headers; mark the method's best numbers in bold #363636, not in the title colours.
- **More awards**: add lines in the award style (20px/600, bold #b22222 lead); keep them above the button row.
- **More experiment videos**: repeat the two-column pattern (660px videos, 10px radius, "Trial N" 20px/600 titles).
- **Long publication lists**: use the related-research rows (thumbnail plus 16px text) rather than cards.

## Do's and Don'ts

- Do colour only the acronym letters and the matching keywords, with exactly two hues.
- Do stack the header in this order: title, authors, affiliations, logos, venue, award, buttons.
- Do give the teaser a short claim and a muted Left/Right caption.
- Do round every video at 10px and leave images square-cornered.
- Don't introduce a gradient; the two title colours are flat fills.
- Don't put the award in a badge; it is a coloured text line.
- Don't use the title colours for links or buttons.

## Surfaces

White page and navbar; dark #363636 pills; videos with 10px radius on white; a 1px grey frame around the paper strip; #f5f5f5 BibTeX; #fafafa footer.

## Imagery

Real and simulated bimanual robot arms with orange 3D-printed grippers assembling nuts, bolts and plugs; purple-and-yellow tactile heatmap panels shown beside the robot; institution logos in their brand colours (Columbia blue, NVIDIA green and black, UC San Diego navy); page previews of the paper.

## Layout

A centred 960px header stack, then wide 1344px sections for media and text, with paired media in two columns. Everything is centred except justified paragraphs.

## Agent Prompt Guide

Quick colors: page #ffffff, title #363636, body #4a4a4a, visuo #46b1f0, tactile #9b59b6, authors #209cee, affiliations #2d2e2e, award #b22222, link #3273dc, caption #bdbdbd.

1. "Build a centred 960px header: Google Sans 40px/600 #363636 two-line title with the acronym letters and two keywords coloured #46b1f0 and #9b59b6; 20px #209cee author links with superscripts; a 16px #2d2e2e affiliation block; a row of three institution logos at 30%, 25% and 20% width; a 24px/600 #363636 venue line; a 20px/600 award line with a bold #b22222 lead."
2. "Make six dark pill buttons in a centred row: #363636 fill, #ffffff 16px Noto Sans text, 40px tall, padding 7px 20px, full pill radius, icons on the left, about 4px apart."
3. "Create a teaser block in a 1344px container: a Noto Sans 32px/600 #363636 claim, a 20px/600 #bdbdbd 'Left: … Right: …' caption 24px below, then a 99%-width autoplaying video with 10px radius."

## Similar Pages

- Nerfies-template robotics pages that add an institution logo row and an award line to the header.
- Tactile and manipulation project pages that pair real-robot footage with tactile heatmaps side by side.

## Quick Start

```css
:root {
  --paper: #ffffff;
  --title: #363636;
  --text: #4a4a4a;
  --visuo: #46b1f0;
  --tactile: #9b59b6;
  --author: #209cee;
  --affiliation: #2d2e2e;
  --award: #b22222;
  --link: #3273dc;
  --caption: #bdbdbd;
  --font-title: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --video-radius: 10px;
  --header-column: 960px;
}
.publication-title { font-family: var(--font-title); }
.publication-authors a { color: var(--author) !important; }
```

## Provenance

- **URL**: https://binghao-huang.github.io/vt_refine/
- **Paper**: VT-Refine: Learning Bimanual Assembly with Visuo-Tactile Feedback via Simulation Fine-Tuning (arXiv 2510.14930), Binghao Huang, Jie Xu, Iretiayo Akinola, Wei Yang, Balakumar Sundaralingam, Rowland O'Flaherty, Dieter Fox, Xiaolong Wang, Arsalan Mousavian, Yu-Wei Chao, Yunzhu Li (Columbia University, NVIDIA, UC San Diego).
- **Venue**: CoRL 2025; Best Paper Award at the IROS 2025 AHFHR Workshop.
- **Selection reason**: the arXiv comment states acceptance at CoRL 2025 and links this project page.
- **Template credit**: footer reads "This website template is borrowed from Here" (the Nerfies template: Bulma 0.9, Font Awesome, Academicons).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), selector probes at 1440, the 1440×900 and full-page screenshots, and `static/css/index.css` and `index.html` read directly, on 2026-10-28.
