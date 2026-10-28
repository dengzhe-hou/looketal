# BoxDreamer — Style Reference

> Rose dusk on warm paper: a coral-to-azure gradient threads through the title, the pills and every heading underline over a soft ivory page.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, scrolled viewport shots at y=2700 and 3800, a probe of rendered elements (header card, badge, rule, abstract, video container, carousel, video grid, copy button, footer), and the page's 35KB inline `<style>` plus `index.html` over Bootstrap 4.4.1. Many elements animate in on load (fade, zoom, slide) and the title gradient shifts position every 3s, so screenshot colors along the title vary with timing. Open Sans is requested at 400/600/700 only, so the declared 300 body weight and the 500 author weight both render as 400.

## Overview

A soft, animated single-column Bootstrap page (about 5,350px tall) on a warm ivory background (#fdfcf9). The header is a full-width white "glass" card (rgba(255,255,255,0.95), 20px radius, soft shadow) holding a 32px Open Sans title filled with a `linear-gradient(45deg, #ee8080, #3881e0)` that animates, a coral-to-teal "ICCV 2025" pill, a light gray rule, a bullet-separated author list in Bootstrap blue, a black affiliation paragraph and four gradient pill buttons. Below, each section opens with a centred 28px coral (#ee8080) heading with a 50×3px gradient underline, a thin #f5f5f5 rule, and content: an overview figure with rounded corners and a deep shadow, a justified abstract with azure (#3881e0) highlighted phrases, a video in a frosted white container, a strip of comparison images, a real-world demo carousel (two videos plus a scrolling column of reference images), a four-column grid of result videos, and a gradient-tinted BibTeX well with a gradient copy button. A centred gray footer credits Lior Yariv's template.

## First Viewport

Color share (quantized 1440×900 shot): white #ffffff 42.6% (the header card); ivory #fdfcf9 23.5% and #f8f8f7 21.0% (page background and figure surround); mauve gray #bdb4bd 10.9% (the method figure and title gradient blend); near-whites #fbfcfd, #fefefc, #fffefa, #fffffd under 1% each.

Anatomy in DOM order (desktop 1440px; Bootstrap `.container` 1140px at x=150, content x=165 to 1275; everything centred):

1. **Header card** (`.jumbotron.text-center`, 0–457px, full width): background rgba(255,255,255,0.95) with `backdrop-filter: blur(20px)`, 1px rgba(255,255,255,0.3) border, 20px radius, shadow `0 8px 32px rgba(0, 0, 0, 0.1)`, padding 32px, margin-bottom 32px; it fades down 30px on load.
2. **Title** (`h2`, y=33–110): Open Sans 32px/700, line-height 1.2, two lines; text clipped to `linear-gradient(45deg, var(--primary-color), var(--secondary-color))` (#ee8080 → #3881e0) with `background-size: 200% 200%` and a 3s `gradientShift` animation. Margin-bottom 8px.
3. **Venue pill** (`.conference-badge`, y=125–165, 149px wide): `linear-gradient(45deg, #ff6b6b, #4ecdc4)`, padding 6.4px 19.2px, 20px radius, shadow `0 3px 10px rgba(0, 0, 0, 0.15)`, pulsing scale 1 → 1.05 and a diagonal white shimmer; inside, "ICCV 2025" h4 22.4px/700 white with `text-shadow: 0 2px 4px rgba(0,0,0,0.3)`.
4. **Rule** (`hr`, y=205): 2px solid #f5f5f5, margin 24px 0, scales in from the centre.
5. **Authors** (`.author-list`, y=231–294): 17.6px (500 declared, 400 renders), line-height 1.8, names in Bootstrap link blue #007bff separated by " • ", superscripts black; a gradient underline grows under a name on hover.
6. **Affiliations** (`p`, y≈294–345): 16px #000000 with superscript numbers, two lines. Margin-bottom 16px.
7. **Buttons** (y=362–408): Arxiv, Code, Supplementary, Demo; each `a.btn.btn-light` in a `p.mb-3`: `linear-gradient(45deg, #ee8080, #3881e0)` fill (200% size), white 16px/600, padding 11.2px 32px, 30px radius, 8px side margins; they fade up with 0.1s staggered delays, so the last ones are still faint in the load screenshot. The card ends at y=457.
8. **Abstract section** (from y=489): h3 "Abstract" at y=521 (32px top margin), 28px/700 #ee8080, padding-bottom 8px with a 50×3px gradient bar centred under it; a 2px #f5f5f5 rule; the TL;DR `h6` (16px, #3881e0, centred); then the method figure (`img.img-fluid`, x=165, 1110×332, from y=649) crossing the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Coral | #ee8080 | --primary-color | section headings, gradient start (title, buttons, heading bars, copy button, video labels, references header), carousel arrow glyphs |
| Azure | #3881e0 | --secondary-color | gradient end, TL;DR line, `.highlight` phrases in the abstract |
| Ivory | #fdfcf9 | --bg-color | page background |
| Text Black | #000000 | --text-color | body text, affiliations, abstract |
| Rule Gray | #f5f5f5 | --light-gray | `hr` rules under headings and in the header |
| Footer Gray | #6e6e6e | --dark-gray | footer text, loading labels |
| Link Blue | #007bff | Bootstrap link | author names, footer links |
| Badge Coral | #ff6b6b | (literal, `.conference-badge`) | venue pill gradient start |
| Badge Teal | #4ecdc4 | (literal) | venue pill gradient end, FPS badge text and glow in the demo carousel |
| Glass White | rgba(255,255,255,0.95) | --glass-bg | header card, carousel arrows |
| Code Well | #f8f9fa → #e9ecef | (literal gradient) | BibTeX `pre` |
| Code Ink | #212529 | Bootstrap `pre` | BibTeX text |
| Success Green | #28a745 → #20c997 | (literal gradient) | copy button after copying |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text / headings | 'Open Sans', sans-serif (Google Fonts 400, 600, 700) | Open Sans 400, 600, 700; declared 300 and 500 render as 400 | Open Sans |
| Code | SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace | Consolas on Windows | JetBrains Mono |
| Icons | Font Awesome 5.15.3 | Font Awesome 5 Free 900, Brands 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.jumbotron h2` | 2rem = 32px / 700 / 1.2 | gradient #ee8080 → #3881e0 (text clip) |
| Venue pill text | `.conference-badge h4` (inline style) | 1.4rem = 22.4px / 700 | #ffffff |
| Section heading | `h3` | 1.75rem = 28px / 700 / 1.2, centred | #ee8080 |
| Authors | `.author-list` (inline) | 1.1rem = 17.6px / 500 declared (400 renders) / 1.8 | #007bff |
| Body / abstract | `body`, `.text-justify` | 16px / 300 declared (400 renders) / 1.6, justified | #000000 |
| Highlight phrase | `.highlight` | inherits 16px / 600 | #3881e0 |
| TL;DR | `h6` (inline color) | 16px / 500 declared (400 renders) | #3881e0 |
| Button | `.btn` | 16px / 600 | #ffffff |
| Copy button | `.copy-button` | 0.9rem = 14.4px / 600 | #ffffff |
| BibTeX | `pre` | 14px / 1.6 monospace | #212529 |
| Footer | `footer` | 16px | #6e6e6e |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Header card (`.jumbotron`) | 20px | 1px rgba(255,255,255,0.3) | `0 8px 32px rgba(0, 0, 0, 0.1)` |
| Gradient buttons | 30px | none | none; hover `0 12px 30px rgba(0, 0, 0, 0.2)` with translateY(-5px) scale(1.08) |
| Venue pill | 20px | none | `0 3px 10px rgba(0, 0, 0, 0.15)` |
| Figures (`.img-fluid`) | 12px | none | `0 8px 25px rgba(0, 0, 0, 0.15)`; hover `0 20px 45px rgba(0, 0, 0, 0.25)`, translateY(-8px) scale(1.03) |
| Video container (`.glass-video-container`) | 20px | 1px rgba(255,255,255,0.3) | `0 8px 32px rgba(0, 0, 0, 0.1)` |
| Videos | 12px | none | `0 8px 25px rgba(0, 0, 0, 0.15)` |
| Demo carousel card | 24px | 1px rgba(255,255,255,0.5) | `0 12px 40px rgba(0, 0, 0, 0.12)` |
| Video grid items | 15px | none | `0 5px 20px rgba(0, 0, 0, 0.1)` |
| BibTeX `pre` | 12px | 2px rgba(0,0,0,0.05) | `0 4px 16px rgba(0, 0, 0, 0.08)` |
| Copy button, video labels | 20px / 24px | none | `0 4px 12px rgba(0, 0, 0, 0.15)` |
| Carousel arrows | 50%, 50px | 2px rgba(255,255,255,0.5) | `0 6px 20px rgba(0, 0, 0, 0.15)` |
| Heading bar (`h3::after`) | 2px | 50×3px gradient | none |

## Layout Metrics

- **Container**: Bootstrap `.container` 1140px at ≥1200px (x=150), 15px padding → content x=165 to 1275 (1110px).
- **Header card**: full viewport width, padding 32px, margin-bottom 32px; rendered 457px tall; title margin-bottom 8px; venue pill margin 8px 0; `hr` margin 24px 0; affiliation margin-bottom 16px; buttons in `p.mb-3`.
- **Sections**: `section.section` with no padding; spacing comes from `h3` margin-top 32px and padding-bottom 8px, then an `hr` (margin-top 0).
- **Figures**: `.img-fluid` up to 1110px; overview figure renders 1110×332.
- **Video container**: margin 32px 0, padding 32px; inner video 1044px wide.
- **Demo carousel**: `.demo-carousel` max 1600px with padding 0 80px; card 950px wide at x=245, padding 32px 16px, min-height 650px; content split 65% videos / 30% references with a 40px gap; video wrappers 340px tall.
- **Video grid**: `repeat(auto-fill, minmax(224px, 1fr))`, gap 25px → four columns of 258.75px at 1440.
- **BibTeX**: `pre` padding 21px (1.5em of 14px); copy button absolute at top 16px, right 16px.
- **Footer**: padding 24px 0, centred.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1200px | 15px in 1140px | 16px | 32px | video grid 4 columns |
| 992–1199px | 960px container | 16px | 32px | video grid 3 columns |
| 769–991px | 720px container | 16px | 32px | video grid 2 columns |
| ≤768px | 540px / full width | 16px | 32px | header card padding 24px; button margin 4.8px; video grid `minmax(250px, 1fr)`; copy button becomes static under the code |

## Components

- **Gradient pill button** (`a.btn.btn-light`): `background: linear-gradient(45deg, var(--primary-color), var(--secondary-color))` with `background-size: 200% 200%`, no border, white Open Sans 16px/600, padding 11.2px 32px, 30px radius, Font Awesome icon (or 🤗 emoji for Demo) before the label. Hover: background-position right, translateY(-5px) scale(1.08), shadow `0 12px 30px rgba(0, 0, 0, 0.2)`, and a white sheen `linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent)` sweeps across.
- **Venue pill** (`.conference-badge`): `linear-gradient(45deg, #ff6b6b, #4ecdc4)`, 20px radius, padding 6.4px 19.2px; 22.4px/700 white text with a dark text-shadow; pulses and shimmers continuously.
- **Section heading** (`h3`): 28px/700 #ee8080, centred, 32px top margin, 8px bottom padding; `::after` a 50×3px `linear-gradient(45deg, var(--primary-color), var(--secondary-color))` bar with 2px radius, centred at the bottom, growing from 0 on load. A 2px #f5f5f5 `hr` follows.
- **Highlight phrase** (`.highlight`): #3881e0 600 with a 2px gradient underline that scales in when the paragraph is hovered.
- **Frosted video container** (`.glass-video-container`): rgba(255,255,255,0.85) with `backdrop-filter: blur(20px)`, 20px radius, padding 32px, shadow `0 8px 32px rgba(0, 0, 0, 0.1)`; the video inside has 12px radius.
- **Demo carousel**: frosted card (rgba(255,255,255,0.7), `blur(30px)`, 24px radius); two black 340px video wrappers (16px radius) with gradient "label" pills top-left and a dark FPS badge bottom-right (#4ecdc4 text, 2px rgba(78,205,196,0.3) border); a right column headed by a gradient `.references-header` (16px radius, 16px/700 white) over a vertically scrolling stack of square reference images with 36px round up/down arrows; 50px round side arrows with coral glyphs that fill with the gradient on hover.
- **Video grid item**: 15px radius, rgba(255,255,255,0.9) behind, shadow `0 5px 20px rgba(0, 0, 0, 0.1)`; hover lifts 10px with a 5deg X-tilt; a loader with a 4px gradient progress bar shows until the video loads.
- **BibTeX**: `pre` with `background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%)`, 12px radius, 2px rgba(0,0,0,0.05) border, soft shadow, 14px code; gradient copy button (20px radius, 14.4px/600, padding 9.6px 19.2px), green gradient once copied.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Header card | yes | full-width white glass card with 20px radius |
| Title | yes | animated coral-to-azure gradient text |
| Venue badge | yes | coral-to-teal pulsing pill |
| Authors / affiliations | yes | blue links separated by bullets, black affiliation line |
| Link buttons | yes | four gradient pills |
| TL;DR | yes | centred azure h6 under the Abstract heading |
| Abstract | yes | justified 16px text with azure highlights |
| Overview / method figure | yes | 12px radius, deep soft shadow |
| Videos | yes | frosted container, demo carousel, four-column grid (27 videos) |
| Qualitative comparison strips | yes | image strips with method labels |
| Results tables | absent from the source | — |
| BibTeX | yes | gradient gray well with gradient copy button |
| Footer | yes | centred gray template credit and © line |

## Adapting to Other Content

- **More authors**: keep the bullet-separated `.author-list` at 17.6px in the 1110px column; it wraps to as many lines as needed, with affiliations below in one 16px paragraph.
- **A results table**: place a Bootstrap `table` inside a frosted container (rgba(255,255,255,0.85), 20px radius, 32px padding); header 600 #000000 on #f5f5f5, 16px rows, best values 600 #3881e0, under a coral h3 with its gradient bar.
- **Long publication or news lists**: use rows in a frosted container, each with a 16px/600 #ee8080 date and black text, separated by 2px #f5f5f5 rules.
- **More videos**: add `.video-item`s to the grid; the auto-fill grid stays at 258.75px columns at 1440.
- **Another badge**: reuse the gradient pill button shape rather than inventing new colors; the coral-to-teal gradient is reserved for the venue.

## Do's and Don'ts

- Do run the #ee8080 → #3881e0 gradient through title, buttons, heading bars and labels; it is the page's identity.
- Do keep headings centred in coral with the 50×3px gradient bar.
- Do round everything generously (12px media, 20px containers, 30px buttons) and give media soft, deep shadows.
- Do keep the page background ivory #fdfcf9 so white cards read as raised.
- Don't add hard borders; separation comes from shadows and the faint #f5f5f5 rules.
- Don't use the coral-to-teal badge gradient for anything but the venue.
- Don't set long text in color; only short highlights are azure.

## Surfaces

Ivory page; a full-width white glass header card; frosted white containers (85% and 70% white with backdrop blur) for videos and the demo carousel; a pale gray gradient BibTeX well. Media are rounded and lifted by shadows.

## Imagery

A clean method diagram with pastel feature maps and a 3D bounding-box reconstruction; YCB-Video and LINEMOD frames with green and blue box overlays; real-world demo videos of hand-held objects with predicted boxes; square reference photos; dense comparison strips labelled by method.

## Layout

One centred 1110px column: a full-width header card, then stacked sections each introduced by a coral centred heading, with figures and videos at full column width and a wider (950px card in a 1600px frame) demo carousel.

## Agent Prompt Guide

Quick colors: coral #ee8080, azure #3881e0, ivory #fdfcf9, text #000000, rule #f5f5f5, footer #6e6e6e, link #007bff, badge #ff6b6b → #4ecdc4.

1. "Build a header card on an ivory #fdfcf9 page: full width, rgba(255,255,255,0.95) with backdrop-filter blur(20px), 20px radius, shadow 0 8px 32px rgba(0,0,0,0.1), padding 32px, centred. Title Open Sans 32px/700 clipped to linear-gradient(45deg, #ee8080, #3881e0); a venue pill linear-gradient(45deg, #ff6b6b, #4ecdc4), 20px radius, white 22.4px/700 text; a 2px #f5f5f5 rule; bullet-separated author links in #007bff at 17.6px."
2. "Make gradient pill buttons: linear-gradient(45deg, #ee8080, #3881e0), white Open Sans 16px/600, padding 11.2px 32px, radius 30px, 8px side margins, leading icon; hover translateY(-5px) scale(1.08) with shadow 0 12px 30px rgba(0,0,0,0.2)."
3. "Create a section: centred h3 28px/700 #ee8080 with an ::after 50×3px gradient bar (#ee8080 → #3881e0, 2px radius), a 2px #f5f5f5 rule, then a figure with 12px radius and shadow 0 8px 25px rgba(0,0,0,0.15), and justified 16px #000000 text with key phrases in #3881e0 600."

## Similar Pages

- Pages built on Lior Yariv's Bootstrap project template, here heavily restyled with glass cards and gradients.
- Soft-gradient research pages that reuse one two-stop gradient for text, buttons and dividers.

## Quick Start

```css
:root {
  --primary-color: #ee8080;
  --secondary-color: #3881e0;
  --bg-color: #fdfcf9;
  --text-color: #000000;
  --light-gray: #f5f5f5;
  --dark-gray: #6e6e6e;
  --glass-bg: rgba(255, 255, 255, 0.95);
  --glass-border: rgba(255, 255, 255, 0.3);
  --brand-gradient: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
  --font: 'Open Sans', sans-serif;
  --radius-media: 12px;
  --radius-card: 20px;
  --radius-pill: 30px;
}
```

## Provenance

- **URL**: https://zju3dv.github.io/boxdreamer/
- **Paper**: BoxDreamer: Dreaming Box Corners for Generalizable Object Pose Estimation (arXiv 2504.07955), Yuanhong Yu, Xingyi He, Chen Zhao, Junhao Yu, Jiaqi Yang, Ruizhen Hu, Yujun Shen, Xing Zhu, Xiaowei Zhou, Sida Peng (Zhejiang University and others).
- **Venue**: ICCV 2025.
- **Selection reason**: the arXiv comment states acceptance at ICCV 2025 and links this project page.
- **Template credit**: footer thanks Lior Yariv for the website template; Bootstrap 4.4.1 with a large custom inline stylesheet.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, two scrolled viewport shots, a rendered-element probe, and the inline style and `index.html` read directly, on 2026-10-28.
