# PersonaVLM — Style Reference

> A field notebook taped open on a white desk: a tall soft-gray headline, a long line of sky-blue names, and a salmon-to-sand storyboard that explains the study in three panels.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, the page's `static/css/index.css`, and `index.html` (with inline styles on the teaser caption and figures) read directly. The page uses the Academic Project Page Template, itself derived from Nerfies, on Bulma 0.9; `bulma-carousel` and `bulma-slider` are loaded but no carousel is used. Every value below was probed on the rendered element.

## Overview

A white, centred Bulma page (about 4,700px tall). The hero carries a three-line 48px Google Sans title in #363636, two lines of twelve sky-blue (#209cee) author links with superscripts, a two-line gray affiliation block that ends with "CHI 2026 · Barcelona, Spain", and three dark rounded buttons (Paper, Code, arXiv). The teaser is a full-width storyboard figure in three colored columns (salmon "Step 1: Experiment", peach "Step 2: Data process and comparison", sand "Step 3: Interview"), followed by a centred Google Sans caption whose opening phrase is bold. Sections follow with centred 32px headings: Abstract (justified paragraphs with bold key terms), Video (a 1070px YouTube embed with 10px radius), How the Simulator Works (figure and centred caption with inline red `code` tokens), Video Scenarios (figure), BibTeX (gray pre) and a #fafafa footer that credits the template.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 67.0% plus near-whites #fdffff 1.3% and #fffff2 0.5%; dusty rose #af8b86 8.8% (the salmon step-1 panel and photos), dark gray #494444 7.7% (title text, buttons, photo shadows), sand #fde8bd 6.8% (step-3 panel), taupe #d3c4b8 4.9% and pale sage #e8ede3 3.0% from the figure. Sky-blue author links are too thin to form a cluster.

Anatomy in DOM order (desktop 1440px; `section.hero > .hero-body` padding 48px 24px; `.container.is-max-desktop` 960px from x=240; everything centred):

1. **Title** (`h1.title.is-1.publication-title`, y=48, 162px tall): three lines, Google Sans 48px / 600 (synthetic bold; only 400 loads), line-height 1.125, #363636. Margin-bottom 24px.
2. **Authors** (`.publication-authors.is-size-5`, y=234, 69px tall, two lines): twelve links in Google Sans 20px / 400, #209cee (hsl(204, 86%, 53%) with `!important`), each with a #4a4a4a superscript digit and a comma.
3. **Affiliations and venue** (second `.publication-authors`, y=303, 99px tall, three lines): Google Sans 20px #4a4a4a: "¹The University of Tokyo, ²UCL Interaction Centre, ³Google", "⁴Kyoto University, ⁵National Taiwan University of Arts", "CHI 2026 · Barcelona, Spain".
4. **Buttons** (`.publication-links`, y=420, 40px tall; in a second Bulma column with 12px padding): Paper (FA file-pdf), Code (FA GitHub), arXiv (academicons), Bulma `is-dark is-rounded`, 3px apart. Hero ends at y=525.
5. **Teaser** (second `section.hero`, inner `.hero-body` padding 48px 24px, so the image starts at y=573 and is 912×381): no radius, no shadow, inline width 100%.
6. **Teaser caption** (`.content`, y=984, 77px tall; inline margin-top 24px): Google Sans 16px / 1.6, #4a4a4a, centred; the paper name in bold at the start.

The Abstract section follows at y=1109, with its heading at y=1205.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | (Bulma `$white`) | page background, button labels |
| Heading Gray | #363636 | (Bulma `$grey-darker`) | title, section headings, button fill |
| Body Gray | #4a4a4a | (Bulma `$grey-dark`) | paragraphs, captions, affiliations, venue line, superscripts, BibTeX text |
| Sky Link | #209cee | (literal, hsl(204, 86%, 53%) !important) | author name links |
| Bulma Link | #3273dc | (Bulma `$link`) | footer links |
| Code Red | #da1039 | (Bulma `$code`) | inline `code` tokens (forward, stop, backward) in captions |
| Code Gray | #f5f5f5 | (Bulma `$white-ter`) | inline code background, BibTeX pre |
| Footer Gray | #fafafa | (Bulma `$white-bis`) | footer background |
| Button Hover | #2f2f2f | (Bulma `.button.is-dark:hover`) | dark button fill on hover |

The salmon, peach and sand panels belong to the teaser image, not the CSS.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display (hero, captions) | 'Google Sans', sans-serif; captions inline 'Google Sans', 'Noto Sans', sans-serif | Google Sans 400 only; 600 synthesized | Outfit |
| Body | 'Noto Sans', sans-serif | Noto Sans 400; bold synthesized | Open Sans |
| Code | Bulma monospace | system monospace (Consolas on Windows) | Source Code Pro |
| Icons | Font Awesome (local CSS and JS), Academicons | FA icons as injected SVG; Academicons 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title` | Google Sans 48px / 600 / 1.125 | #363636 |
| Authors | `.publication-authors a` | Google Sans 20px / 400 / 1.5 | #209cee |
| Affiliations, venue | `.publication-authors` | Google Sans 20px / 400 / 1.5 | #4a4a4a |
| Button | `.button.is-dark` | Noto Sans 16px / 400 | white |
| Section heading | `h2.title.is-3.has-text-centered` | Noto Sans 32px / 600 / 1.125 | #363636 |
| Figure caption | inline-styled `.content p.has-text-centered` | Google Sans 16px / 1.6, bold lead | #4a4a4a |
| Body | `.content.has-text-justified p` | Noto Sans 16px / 1.5, justified, margin-bottom 16px | #4a4a4a |
| Inline code | `.content code` | 14px monospace, padding 3.5px 7px | #da1039 on #f5f5f5 |
| BibTeX | `pre` | 14px / 1.5 | #4a4a4a |
| Footer | `.footer p` | 16px / 1.5 | #4a4a4a, links #3273dc |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Buttons | 290486px | 1px transparent | none |
| Teaser and figures | 0 | none | none |
| Video embed | 10px (`.publication-video`, !important), overflow hidden | none | none |
| BibTeX pre | 4px | none | none |
| Inline code | Bulma default 0 | none | none |
| Footer | 0 | none | none |

## Layout Metrics

- **Container**: `.container.is-max-desktop` max-width 960px at ≥1024px (x=240 at 1440). Sections that wrap `.hero-body` inside the container (teaser, Abstract, Simulator, Scenarios, BibTeX) indent content by 24px each side, so figures and paragraphs render 912px wide from x=264.
- **Hero**: `.hero-body` padding 48px 24px; renders 525px tall.
- **Teaser section**: `.hero-body` 48px 24px inside the container; caption margin-top 24px; section ends at y=1109.
- **Content sections**: `section.section.hero` adds Bulma section padding 48px 24px plus the inner `.hero-body` 48px 24px, so headings sit 96px below the section top (Abstract at 1109 + 96 = 1205).
- **Video**: `section.hero.is-small` (hero-body padding 24px 24px) with a plain `.container` (1344px) and a `.column.is-four-fifths`, giving a 1070×602 16:9 embed from x=185.
- **Footer**: padding 48px 24px 96px, inner `.column.is-8` 888px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px | 960px container, 24px inner padding | 16px | 48px | buttons in their own centred column below the title column |
| 769–1023px | fluid container, 24px padding | 16px | 48px | same |
| ≤768px | 24px | 16px | 48px | Bulma columns stack; the four-fifths video column becomes full width |

## Components

- **Dark pill button** (`a.external-link.button.is-normal.is-rounded.is-dark`): #363636 fill, white Noto Sans 16px, padding 7px 20px, 40px tall, radius 290486px, 24px `.icon` on the left with margin 0 4px 0 -9px. Hover #2f2f2f.
- **Author line**: author spans inline-block, Google Sans 20px #209cee links, superscript digits in #4a4a4a, comma after each, hover underline.
- **Teaser with bold-lead caption**: full-width image without frame; caption 24px below in centred Google Sans 16px / 1.6 #4a4a4a, beginning with the paper title in bold.
- **Section heading**: Noto Sans 32px / 600 #363636, centred, 24px margin-bottom.
- **Video embed** (`.publication-video`): 16:9 wrapper, radius 10px, overflow hidden, iframe absolutely filling it.
- **Inline code token**: Bulma `.content code`, #da1039 on #f5f5f5, 14px, padding 3.5px 7px; used for the simulator's action words.
- **BibTeX**: section heading "BibTeX", then a #f5f5f5 pre, radius 4px, padding 16px, 14px monospace.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / authors / affiliations | yes | Google Sans hero, sky-blue author links |
| Venue | present but non-standard | plain third line of the affiliation block, "CHI 2026 · Barcelona, Spain" |
| Link buttons | yes | three dark Bulma pills |
| Teaser + caption | yes | three-step storyboard figure, centred bold-lead caption |
| Abstract | yes | justified Noto Sans paragraphs with bold terms |
| Video | yes | YouTube embed, 10px radius, wider than the text column |
| Method figure | yes | simulator diagram with centred caption and inline code tokens |
| Results tables | absent from the source | results are figures |
| BibTeX | yes | gray pre |
| Footer | yes | #fafafa with template credit |

## Adapting to Other Content

- **More authors**: keep the Google Sans 20px line of #209cee links and let it wrap at 960px (seven names per line here); affiliations go on following #4a4a4a lines with `<br>` breaks, ending with the venue and city.
- **A results table**: Bulma `.table` in the 912px content width, Noto Sans 16px #4a4a4a, header 600 #363636, 1px rule rows; caption below in centred Google Sans 16px / 1.6 with a bold lead.
- **Long publication or news lists**: a `.content ul` in the 912px column, 16px Noto Sans, dates bold #363636.
- **An award**: the template's `.publication-awards` rule (bold #ff3860) is declared but unused; add it as its own line under the venue if needed.
- **More figures**: one `section.section.hero` each, centred 32px heading, unframed full-width figure, bold-lead caption.

## Do's and Don'ts

- Do keep the hero in Google Sans and the body in Noto Sans.
- Do start every figure caption with a bold phrase and centre it.
- Do keep author links #209cee and buttons #363636.
- Do let the teaser carry the color; the page chrome stays white and gray.
- Don't frame or shadow figures; they sit flush.
- Don't put the venue in a badge; it is a plain line under the affiliations.
- Don't narrow the video to the 912px column; it spans 1070px.

## Surfaces

White throughout, with #f5f5f5 for code and #fafafa for the footer. No shadows on any element; the only rounding is the 10px video and the 4px BibTeX block.

## Imagery

A three-column storyboard teaser in salmon, peach and sand with field photos of a street crossing, pictogram people and robots, a terminal-style action log and thumbs icons; a simulator diagram with five position frames on a pale green strip and pink action tags; a scenario grid of autonomous-vehicle eHMI conditions; and a YouTube video with title cards.

## Layout

A centred 960px column: hero, unframed teaser with caption, then alternating heading-and-figure sections at 912px, with the video breaking out to 1070px. Large vertical gaps (96px above each heading) give the page an airy rhythm.

## Agent Prompt Guide

Quick colors: background #ffffff, headings and buttons #363636, body #4a4a4a, author links #209cee, inline code #da1039 on #f5f5f5, footer #fafafa.

1. "Build a centred hero in a 960px column with 48px 24px padding: title Google Sans 48px / 600, line-height 1.125, #363636, three lines; authors Google Sans 20px links #209cee with #4a4a4a superscripts and commas, wrapping; affiliations and the venue as plain 20px #4a4a4a lines; three buttons with #363636 fill, white 16px text, padding 7px 20px, fully rounded, icons on the left."
2. "Add a teaser: full-width unframed image, then 24px below a centred Google Sans 16px / 1.6 #4a4a4a caption that starts with the paper title in bold."
3. "Make a section: centred Noto Sans 32px / 600 #363636 heading 24px above justified 16px / 1.5 #4a4a4a paragraphs (bold key terms), inside 96px of combined top padding; a 16:9 video embed with radius 10px and overflow hidden; inline code as #da1039 on #f5f5f5, 14px, padding 3.5px 7px."

## Similar Pages

- Academic Project Page Template sites (Nerfies-derived) with Google Sans heroes and dark pill buttons.
- HCI study pages that lead with a multi-panel storyboard teaser.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --heading: #363636;
  --text: #4a4a4a;
  --author-link: #209cee;
  --link: #3273dc;
  --code-fg: #da1039;
  --code-bg: #f5f5f5;
  --footer-bg: #fafafa;
  --font-display: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --container: 960px;
  --hero-pad: 48px 24px;
  --video-radius: 10px;
}
```

## Provenance

- **URL**: https://apisxia.github.io/PersonaVLM/
- **Paper**: Peeking Ahead of the Field Study: Exploring VLM Personas as Support Tools for Embodied Studies in HCI (arXiv 2602.16157), Xinyue Gui, Ding Xia, Mark Colley, Yuan Li, Vishal Chauhan, Anubhav Anubhav, Zhongyi Zhou, Ehsan Javanmardi, Stela Hanbyeol Seo, Chia-Ming Chang, Manabu Tsukada, Takeo Igarashi.
- **Venue**: CHI 2026, Barcelona.
- **Selection reason**: the arXiv comment states acceptance at CHI 2026; the project page is the GitHub Pages site of the paper's code repository (ApisXia/PersonaVLM) linked in the paper body.
- **Template credit**: footer reads "This page was built using the Academic Project Page Template", which is adapted from Nerfies; Bulma 0.9 base.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted computed-style probes of authors, captions, abstract, video and BibTeX, the 1440×900 and full-page screenshots, and `static/css/index.css` and `index.html` read directly, on 2026-10-28.
