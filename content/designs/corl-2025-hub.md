# HuB Full-Bleed Statement — Style Reference

> One word the size of a wall: a 192px "HuB" printed straight onto looping lab footage, with three tiny links in the corner and nothing else competing.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, loaded fonts, color share), selector probes of the video hero, navbar, second header, video grid, select menu and BibTeX, the 1440×900 and full-page screenshots, and the page's `static/css/index.css`, Bulma 0.9 and `index.html`. The hero is a looping video, so the screenshot shows one frame (the humanoid in a yellow suit mid-kick between two gantry frames). The full-page screenshot was taken in a tall window, where the 100vh hero stretches to fill the capture; its later sections are known from the DOM probes, not from that image.

## Overview

The first screen is the design: a full-viewport video of a Unitree G1 humanoid balancing in a grey lab, with a centred white wordmark "HuB" in Google Sans at 192px, the subtitle "Learning Extreme Humanoid Balance" at 64px and an italic "Conference on Robot Learning 2025" line, and only three links (Paper, arXiv, Video with small PDF, arXiv and YouTube logo icons) at the top right. No scrim or text shadow is applied; the light-grey wall keeps the white type readable only where the footage is busy enough. Below the fold the page turns into a standard Nerfies layout on white: a repeat title block with green author links and six dark pill buttons, then wide two-column grids of rounded task videos (Extreme Humanoid Balance, External Perturbations, Long-Horizon Execution), a comparative section with a task dropdown, the Abstract, a method figure, BibTeX and a light footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): wall and floor greys #9a9991 / #8e8e8e / #94948e / #848482 / #6b6b6a together 70.8%; dark greys #474746 13.2% and #202023 11.4% (gantry frames, the black curtain at left, the robot's gloves); pale khaki #b4b3a6 4.4% (lit wall blended with the yellow suit). White type covers too little area to form a cluster.

Anatomy in DOM order (desktop 1440px):

1. **Video layer** (`.hero-video > video`, absolute, 1600×900 at x=0): wrapper sized `height: 100%; width: 177.77777778vh; min-width: 100%; min-height: 56.25vw`, so the 16:9 clip overflows the 1440px viewport by 160px on the right. Autoplay, muted, loop. Bulma's `.hero.is-link` fill (#3273dc) sits underneath and is fully covered. An `.overlay` div exists but renders 0px tall.
2. **Navbar** (`.hero-head header.navbar`, 0–52px, transparent): `navbar-end` links inside a 1344px container (x=48–1392): "Paper", "arXiv", "Video", Noto Sans 20px/400 #ffffff, padding 8px 16px, each with a 24px logo icon (red PDF glyph, arXiv X mark, red YouTube button) 5px left of the label. Hidden on mobile (`is-hidden-mobile`).
3. **Hero body** (`.hero-body`, 52–900px, padding 48px 24px, flex-centred vertically): the three-line title block is 372px tall and starts at y=290.
4. **Wordmark** (`h1.title.is-1`, y=290, 216px box): "HuB", inline `font-size: 12rem` = 192px, Google Sans 600 (synthesized from the regular face), line-height 216px, #ffffff, centred. Margin-bottom 24px.
5. **Subtitle** (`h1.subtitle.is-1`, y=510, 80px): inline 4rem = 64px, Google Sans 400, line-height 80px, rgba(255,255,255,0.9); Bulma's −20px top margin pulls it up under the wordmark. Margin-bottom 24px.
6. **Venue** (`h1.is-2.is-italic`, y=614, 48px): inline 2rem = 32px, Noto Sans 400 italic, #ffffff at inline `opacity: 80%`.

Arithmetic check: hero body content area 100–852px (52 + 48, 900 − 48) is 752px; block 216 + 24 − 20 + 80 + 24 + 48 = 372px; (752 − 372) / 2 = 190; 100 + 190 = 290; 290 + 216 + 24 − 20 = 510; 510 + 80 + 24 = 614; 614 + 48 = 662.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Hero White | #ffffff | (Bulma `.hero.is-link` text) | wordmark, navbar links, venue line (at 80% opacity) |
| Subtitle White | rgba(255,255,255,0.9) | (Bulma `.subtitle`) | "Learning Extreme Humanoid Balance" |
| Link Blue | #3273dc | (Bulma `$link`) | hero background under the video (declared, covered) |
| Lab Grey | #9a9991 | (footage) | dominant wall and floor tone of the hero video |
| Paper | #ffffff | (Bulma) | page background below the hero |
| Title Ink | #363636 | (Bulma `$grey-darker`) | second h1, section h2/h3, dark button fill, select text |
| Venue Ink | #292929 | (`hsl(0, 0%, 16%)`) | "CoRL 2025" link in the second header |
| Body Ink | #4a4a4a | (Bulma `$text`) | author separators, affiliations, body text, footer |
| Author Green | #00b803 | (`hsl(121, 100%, 36%)`) | author name links |
| Select Border | #dbdbdb | (Bulma) | task dropdown border |
| Code Grey | #f5f5f5 | (Bulma `pre`) | BibTeX block |
| Footer | #fafafa | (Bulma `.footer`) | footer band |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | 'Google Sans', sans-serif (Google Fonts, regular only) | Google Sans 400; 600 is synthesized | Product Sans / Outfit |
| Body | 'Noto Sans', sans-serif | Noto Sans 400 (italic synthesized) | Noto Sans |
| UI controls | Bulma system stack | Segoe UI on Windows | Inter |
| Code | monospace | Consolas on Windows | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Wordmark | hero `h1.title.is-1` (inline 12rem) | 192px / 600 / 216px | #ffffff |
| Subtitle | hero `h1.subtitle.is-1` (inline 4rem) | 64px / 400 / 80px | rgba(255,255,255,0.9) |
| Venue | hero `h1.is-2.is-italic` (inline 2rem, opacity 80%) | 32px / 400 italic / 48px | #ffffff |
| Navbar link | `.navbar-item` in `.container.is-size-5` | 20px / 400 / 30px | #ffffff |
| Page title | second `h1.title.is-1` | 48px / 600 / 54px | #363636 |
| Venue line | `h3.title.is-4.conference-authors` | 24px / 600 | #292929 |
| Authors / affiliations | `.publication-authors.is-size-5` | 20px / 400 / 30px | names #00b803, rest #4a4a4a |
| Section heading | `h2.title.is-2` | 40px / 600 / 45px, centred | #363636 |
| Speed note | `p.is-size-5` | 20px / 400 | #4a4a4a |
| Video title | `h3.title.is-3` (inline `font-size: x-large`) | 24px / 600 / 27px, centred | #363636 |
| Abstract heading | `h2.title.is-3` | 32px / 600 | #363636 |
| Body | `.content p` | 16px / 400 / 24px, justified | #4a4a4a |
| Button | `.button.is-normal` | 16px / 400 | #ffffff |
| BibTeX | `pre` | 14px monospace / 21px | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Hero | 0, full bleed | none | none; no overlay, no text shadow |
| Link buttons | 290486px (pill) | 1px transparent | none |
| Task videos | 10px (inline) | none | none |
| Task dropdown | 4px | 1px #dbdbdb | none |
| Method figure | 0 | none | none |
| BibTeX | 0 | none | none |

## Layout Metrics

- **Hero**: `.hero.is-fullheight` = 100vh (900px at 1440×900); navbar 52px; body padding 48px 24px, content flex-centred.
- **Second header**: `.hero` with a `.container.is-max-desktop` (960px at x=240); title at y=948, buttons at y=1222 (40px tall, 4–5px apart).
- **Video sections**: Bulma `.section` padding 48px 24px; plain `.container` 1344px at x=48 (widescreen); two `.column`s of 660px with a 24px gutter; inline `margin-bottom: 50px` between rows; h3 10px above each video.
- **Abstract and method**: `.container.is-max-desktop` 960px; abstract in `.column.is-four-fifths` (768px), method figure 960×542.
- **Footer**: #fafafa, padding 48px 24px 96px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1408px (1440 render) | 48px outside a 1344px container | 16px | 192px wordmark, 64px subtitle | two video columns of 660px |
| 1216–1407px | container 1152px | 16px | 192px | same |
| 1024–1215px | container 960px | 16px | 192px | same |
| 769–1023px | fluid | 16px | 192px | same |
| ≤768px | 24px | 16px | `is-size-1-mobile` 3rem = 48px wordmark (Bulma `!important` beats the inline 12rem); subtitle and venue `is-size-4-mobile` 24px | navbar hidden; empty mobile link column shown; video columns stack |

## Components

- **Full-bleed video hero**: section 100vh, `overflow: hidden`, a 16:9 video wrapper sized from the viewport height (177.78vh wide, min 100% wide and min 56.25vw tall), absolutely positioned at the top left; centred white type with no scrim. Works only with footage whose centre is mid-grey and calm.
- **Corner link bar**: transparent 52px navbar; right-aligned items 20px/400 #ffffff, padding 8px 16px, each led by a 24px full-colour brand icon (PDF, arXiv, YouTube) with 5px gap.
- **Wordmark stack**: 192px/600 acronym, a 64px/400 subtitle pulled up 20px, a 32px italic venue at 80% opacity, all centred.
- **Dark pill button** (Bulma `.button.is-dark.is-rounded`): #363636, #ffffff 16px text, 40px tall, padding 7px 20px, icon left (Font Awesome, Academicons or an inline Bilibili SVG).
- **Task video card**: centred 24px/600 #363636 title, 10px gap, a 660px video with 10px radius and native controls, looping.
- **Task selector**: "Evaluated on task" in bold, then a Bulma `select.is-small` (12px, 1px #dbdbdb border, radius 4px) that swaps the HuB vs OmniH2O comparison videos.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Full-screen video hero | yes | lab footage with a giant white wordmark |
| Navbar links | yes | three white icon links, top right |
| Title / authors / affiliations | yes | repeated below the fold in a Nerfies block, green author links |
| Link buttons | yes | six dark pills (Paper, arXiv, Video, Bilibili, Datasets, Summary) |
| Video results | yes | two-column grids of rounded looping videos with centred titles |
| Comparison | yes | dropdown-driven side-by-side HuB vs baseline videos |
| Abstract | yes | four-fifths column, justified, appears after the videos |
| Method figure | yes | full-width image with a bold-led paragraph |
| BibTeX | yes | grey `pre` block |
| Footer | yes | credit line for NeRFies and UMI on Legs |
| Results table | absent from the source | — |

## Adapting to Other Content

- **More authors**: keep them below the fold in the 20px Google Sans line with green #00b803 links and superscript affiliation numbers; never add them to the video hero, which carries only the wordmark, subtitle and venue.
- **A results table**: place it in a `.container.is-max-desktop` (960px) section after the videos; Bulma `.table` with 16px #4a4a4a cells, 600-weight #363636 headers, best values bold. Keep the hero untouched.
- **More demo videos**: add rows to the two-column grid (660px videos at 1440, 24px gutter, 50px between rows), each with a 24px/600 centred title.
- **Long publication or news lists**: a 960px section with 16px #4a4a4a items and #363636 bold dates; no cards.
- **A longer project name**: keep the wordmark to one short word; if it is longer than about six characters, reduce from 192px so it stays on one line within 1344px.

## Do's and Don'ts

- Do give the first screen to footage and one oversized white word.
- Do keep the navbar to a few icon links in the top right corner.
- Do pick a hero clip with a light-to-mid grey centre; there is no scrim to help.
- Do move all detail (authors, buttons, abstract) below the fold.
- Don't put author lists, logos or buttons over the video.
- Don't add a coloured overlay; the hero's #3273dc fill is meant to stay hidden behind the clip.
- Don't round or frame the hero; it bleeds to every edge.

## Surfaces

A full-bleed video hero; then plain white for everything else, with #f5f5f5 for BibTeX and #fafafa for the footer. Task videos are the only rounded surfaces (10px).

## Imagery

Real-world footage of a Unitree G1 humanoid in a bright yellow suit performing balance poses (swallow balance, Bruce Lee's kick, single-leg stand) in a grey lab between safety gantries; perturbation clips with a soccer ball strike; a method diagram. All footage is unedited colour, played at original speed.

## Layout

Two acts. Act one is a 100vh video with centred type. Act two is a conventional centred Nerfies page: a 960px header block, wide 1344px video grids, then narrower 960px text sections.

## Agent Prompt Guide

Quick colors: hero text #ffffff, subtitle rgba(255,255,255,0.9), title ink #363636, body #4a4a4a, authors #00b803, venue #292929, code #f5f5f5, footer #fafafa.

1. "Build a 100vh hero with a looping 16:9 background video (wrapper width 177.78vh, min-width 100%, min-height 56.25vw, overflow hidden), no overlay. Centre three lines: Google Sans 192px/600 #ffffff wordmark (line-height 216px), a 64px/400 rgba(255,255,255,0.9) subtitle with margin-top -20px, and a Noto Sans 32px italic #ffffff venue at opacity 0.8."
2. "Add a transparent 52px navbar with right-aligned links in Noto Sans 20px #ffffff, padding 8px 16px, each preceded by a 24px colour brand icon with a 5px gap. Hide it below 769px."
3. "Below the hero, create a video grid: 1344px container, two 660px columns with a 24px gutter, 50px between rows; each item has a 24px/600 #363636 centred title, 10px gap, and a looping video with 10px radius."

## Similar Pages

- Humanoid and locomotion project pages that open with a full-screen looping robot video and a one-word wordmark.
- Nerfies-derived pages that add a `.hero.is-fullheight.video` cover before the standard title block (e.g. the UMI on Legs template credited in the footer).

## Quick Start

```css
:root {
  --hero-text: #ffffff;
  --title-ink: #363636;
  --text: #4a4a4a;
  --author: #00b803;
  --venue: #292929;
  --code-bg: #f5f5f5;
  --footer-bg: #fafafa;
  --font-display: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --wordmark: 12rem;
  --subtitle: 4rem;
  --video-radius: 10px;
}
.hero.video { height: 100vh; overflow: hidden; position: relative; }
.hero-video { position: absolute; height: 100%; width: 177.77777778vh; min-width: 100%; min-height: 56.25vw; }
```

## Provenance

- **URL**: https://hub-robot.github.io/
- **Paper**: HuB: Learning Extreme Humanoid Balance (arXiv 2505.07294), Tong Zhang, Boyuan Zheng, Ruiqian Nai, Yingdong Hu, Yen-Jen Wang, Geng Chen, Fanqi Lin, Jiongye Li, Chuye Hong, Koushil Sreenath, Yang Gao (Tsinghua University, Shanghai Qi Zhi Institute, UC Berkeley, UC San Diego).
- **Venue**: CoRL 2025, Oral Presentation.
- **Selection reason**: the arXiv comment states acceptance at CoRL 2025 (Oral) and links this project page.
- **Template credit**: footer reads "Website template borrowed from NeRFies and UMI on Legs" (Bulma 0.9, bulma-carousel, Font Awesome 6.5, Academicons).
- **Evidence used**: computed-style render at 1440×900 (the stock tool timed out on the slow load event, so the same script was rerun with a tolerant load wait), selector probes at 1440, the 1440×900 and full-page screenshots, and `static/css/index.css` and `index.html` read directly, on 2026-10-28.
