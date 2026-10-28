# DiTree Sites Maze — Style Reference

> A maze seen from above, teal floor and brown walls, with white type laid straight on the render and a pair of sandy buttons that borrow the wall colour.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, loaded fonts, color share), extra probes of the hero, buttons, sections, images, embeds and citation block at 1440 and 700px, and the 1440×900 and full-page screenshots. The page is a Google Sites build, so the markup uses generated class names (`.yaqOZd`, `.FKF6mc`, `.C9DxTc`) and theme CSS served from gstatic; selectors below are those rendered classes. The two embedded Drive videos had not started at capture time; the first shows as a near-black player box.

## Overview

A short Google Sites page (about 3,500px tall) with a 430px image hero: a top-down render of the Ant robot in a teal maze with brown walls, red and pink sample dots and trajectory curves, under a 56px header that shows a square tree icon and the site name "DiTree" in white. The two-line title, authors, "Technion" and "Accepted to CoRL 2025" sit centred in white directly on the render; there is no overlay layer. Below, on white, two sandy orange buttons (#e8a563) echo the figure palette, then a Drive video embed, a centred italic abstract under a Lato "Abstract" heading, four alternating feature rows (figure left and text right, then text left and figures right), a real-car video embed, and a citation block whose lines sit on a 6% grey wash. The teal-and-orange of the figures (maze tiles, environment thumbnails, path plots) carries through the whole page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 35.8% (lower half of the page); teal #135255 21.4% plus #50756d 2.3% (maze floor); near-black #141516 15.1% plus #0e0e0f 0.5% (the unloaded video player); brown #6c553c 13.5% (wall tops); dark brown #2e211b 10.3% plus #312c24 1.2% (wall sides and shadows). The sandy buttons are too small to form a cluster.

Anatomy in DOM order (desktop 1440px, everything centred):

1. **Header** (`header`, 0–56px, overlaid on the hero): bar background #1c1c1c at opacity 0 at the top of the page (Google Sites fades it in on scroll). Left: 56×56 logo image at x=16 (padding 8px 4px 8px 12px, a dark tree icon) and "DiTree" Roboto 20px/400 #f9f9f9. No navigation links (single-page site).
2. **Hero** (`section.yaqOZd` with `div.IFuOkc`, 0–430px): `background-size: cover; background-position: 50% 50%` render image; section padding 56px 0; content block from y=56 to y=374.
3. **Title** (`h2`, y=115, 72px tall): Lato 24px/700, line-height 36px, #f9f9f9, centred, two lines ("Train-Once Plan-Anywhere" / "Kinodynamic Motion Planning via Diffusion Trees"). Gap 28px.
4. **Authors + affiliation** (`p`, y=215, 48px): Roboto 16px/400, line-height 24px, #f9f9f9, names on one line and "Technion" below. Gap 28px.
5. **Venue line** (`p`, y=291): "Accepted to CoRL 2025", Roboto 16px/400 #f9f9f9. The hero ends at y=430.
6. **Buttons** (`section`, 430–514px, padding 24px 0): two 168×36 buttons at x=537 and x=735 (30px apart), y=454: #e8a563 fill and 1px #e8a563 border, radius 4px, Roboto 16px/400 #1c1c1c labels "Paper" and "Code".
7. **Video embed** (`section`, from y=514, padding 24px 0): Drive player iframe 562×390 at x=439, y=538, black until it loads, with a pop-out icon top right.
8. **Info button** (fixed, bottom left at about x=24, y=860): the Google Sites "Page updated" circle-i control in #dadada.

Arithmetic check: the hero's content block spans y=56–374 (318px) and is vertically centred, so the title starts 59px into it (56 + 59 = 115); 115 + 72 + 28 = 215; 215 + 48 + 28 = 291; the venue line ends at 315, the block's bottom padding brings it to 374, and the 56px section padding ends the hero at 430; 430 + 24 = 454; 454 + 36 + 24 = 514; 514 + 24 = 538.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #ffffff | (theme) | page background below the hero |
| Ink | #1c1c1c | (theme) | headings and body text on white, button labels; header bar when it appears |
| Hero White | #f9f9f9 | (theme) | site name, title, authors and venue on the hero image |
| Sand | #e8a563 | (button colour, theme accent) | Paper and Code button fill and border |
| Maze Teal | #135255 | (image) | hero render floor; dominant hue of figures |
| Wall Brown | #6c553c | (image) | hero wall tops; echoed by the sand buttons |
| Player Black | #141516 | (embed) | unloaded Drive video player |
| Code Wash | rgba(0,0,0,0.06) | (theme) | background of each BibTeX line |
| Caption Chip | #f2f2f2 | (theme) | file-name strip on Drive video embeds |
| Info Grey | #dadada | (theme) | "Page updated" info control |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Headings | Lato (Google Sites theme) | Lato 700 | Lato |
| Body | Roboto | Roboto 400, Roboto 400 italic, Roboto 500 | Roboto |
| Code | "Source Code Pro", Arial | Source Code Pro 400 | Source Code Pro |
| Site UI | "Google Sans", Roboto, Arial, sans-serif | Google Sans 500 (skip links only) | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Site name | `a.GAuSPc` | Roboto 20px / 400 | #f9f9f9 |
| Paper title | hero `h2.JYVBee` | Lato 24px / 700 / 36px, centred | #f9f9f9 |
| Section heading | `h2.JYVBee` ("Abstract") | Lato 24px / 700 / 36px, centred | #1c1c1c |
| Feature heading | `h3.OmQG5e` | Lato 18.67px / 700 / 28px, left | #1c1c1c |
| Body | `p.zfr3Q` | Roboto 16px / 400 / 24px | #1c1c1c (hero #f9f9f9) |
| Abstract | `p.zfr3Q > span` | Roboto 16px / 400 italic / 24px, centred | #1c1c1c |
| Button label | `a.FKF6mc` | Roboto 16px / 400 | #1c1c1c |
| Citation | `span.C9DxTc` in code lines | Source Code Pro 16px / 400 / 24px | #1c1c1c |
| Image caption | `p` under figures | Roboto 16px / 400, centred | #1c1c1c |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Buttons | 4px | 1px #e8a563 | none; pressed ripple `radial-gradient(circle farthest-side, rgba(0, 0, 0, 0.12), rgba(0, 0, 0, 0.12) 80%, rgba(0, 0, 0, 0) 100%)` |
| Figures | 0 | none (borders are drawn inside the images) | none |
| Video embeds | 0 | none | none |
| Citation lines | 0 | none | none; each line has rgba(0,0,0,0.06) with 5.33px side padding |
| Hero | 0 | none | none; no overlay or text shadow |

## Layout Metrics

- **Content width**: Google Sites section content box 1154px at x=143 with 8px tile padding, so text runs 1138px from x=151 at 1440.
- **Hero**: 430px tall, padding 56px 0 (the header height), cover image centred at 50% 50%.
- **Sections**: each `section.yaqOZd` has padding 24px 0; sections butt against each other without rules or colour changes.
- **Button row**: two 168×36 buttons centred, 30px apart.
- **Video**: first embed 562×390 centred; car video 760×345 centred.
- **Abstract**: centred column 744px wide at x=348.
- **Feature rows**: a 760px figure plus a 349px text column (x=940) separated by about 37px; the second row reverses with text (546px) left and two 266px figures right, each with a centred caption below.
- **Citation**: full 1138px width, lines 25px tall.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| 1440 (desktop) | 143px + 8px tile padding | 16px | 24px | two-column feature rows |
| 700 (probed) | 22px; text at x=30 | 16px | 22.67px / 34px | feature rows stack (figure 656px wide, heading below); buttons 194px wide |

## Components

- **Image hero with title**: a full-width cover render, 430px tall, under a transparent 56px header; centred Lato 24px/700 title and Roboto 16px lines in #f9f9f9 laid directly on the image. Choose an image with a mid-dark, low-detail centre so white text stays legible without an overlay.
- **Sand button**: 168×36, #e8a563 fill with a matching 1px border, radius 4px, Roboto 16px/400 #1c1c1c label centred; Google Sites ripple on press.
- **Header**: 56px, logo tile (square app-style icon) plus Roboto 20px site name in #f9f9f9; the #1c1c1c bar fades in once the page scrolls.
- **Feature row**: Lato 18.67px/700 h3 and a short 16px paragraph beside a teal-and-orange figure; rows alternate image-left and image-right.
- **Citation block**: an intro line, then each BibTeX line as its own paragraph in Source Code Pro 16px on rgba(0,0,0,0.06), giving a striped grey slab.
- **Drive video embed**: black player with a pop-out icon and a #f2f2f2 file-name strip.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Header / brand | yes | logo tile and site name on a transparent bar |
| Image hero with title | yes | full-width render, white centred text, no overlay |
| Authors / affiliation / venue | yes | plain white lines in the hero |
| Link buttons | yes | two sand buttons with 4px corners |
| Video overview | yes | Drive embed |
| Abstract | yes | centred italic paragraph under a Lato heading |
| Feature rows | yes | four alternating figure/text rows |
| Real-world video | yes | Drive embed under a section heading |
| BibTeX | present but non-standard | lines on a grey wash rather than a code block; no copy button |
| Results table | absent from the source | results appear as figures |
| Footer | absent from the source | only the Google Sites info control |

## Adapting to Other Content

- **More authors**: keep them on centred #f9f9f9 16px lines in the hero; at 1138px a line holds about twelve names, and affiliations go on the next line as "Technion" does.
- **A results table**: insert a Google Sites table in a 1138px section; Roboto 16px #1c1c1c, header row in Lato 700, thin #1c1c1c rules; highlight the method's row by tinting cells with #e8a563 at low opacity rather than colouring text.
- **More features**: add rows at the same proportions (760px figure, 349px text, about 37px gap) and keep alternating sides.
- **Long publication or news lists**: left-aligned 16px Roboto paragraphs under an 18.67px Lato h3, dates in 700; no cards.
- **A different hero image**: keep it top-down or wide-angle with a dark, even centre; the title has no shadow or overlay to rescue it.

## Do's and Don'ts

- Do pick the button colour from the figures (here the maze wall sand #e8a563) so UI and imagery match.
- Do keep headings in Lato 700 and everything else in Roboto 400.
- Do alternate figure and text sides in feature rows.
- Don't put a scrim over the hero; the design relies on the render's own dark midtones.
- Don't add borders or radii to figures; their teal-orange frames are part of the images.
- Don't add extra button colours; both links use the same sand fill.

## Surfaces

A full-bleed render hero, then plain white sections without bands, rules or cards. The only grey surfaces are the citation wash (rgba(0,0,0,0.06)) and the Drive embeds' #f2f2f2 strips.

## Imagery

Top-down renders of an Ant robot in a teal maze with brown walls; a grid of maze environment thumbnails labelled Train/Test in teal and orange; path-tracking plots on orange tiles; a method diagram in teal and black; real car race-track video. The overview embed's poster is a title slide whose text is cropped at both sides of the 562px frame. The palette of teal, sand-orange, brown and red is consistent across all images.

## Layout

Hero band, a centred button row, a centred video, a centred italic abstract, then alternating two-column feature rows and a full-width citation. Everything sits within Google Sites' 1154px content box; vertical rhythm is the 24px section padding.

## Agent Prompt Guide

Quick colors: page #ffffff, ink #1c1c1c, hero text #f9f9f9, button #e8a563, teal #135255, brown #6c553c, citation wash rgba(0,0,0,0.06).

1. "Build a 430px hero: full-width cover image centred at 50% 50%, a transparent 56px header with a square logo and Roboto 20px #f9f9f9 site name at x=16; centred Lato 24px/700 #f9f9f9 two-line title (line-height 36px), then Roboto 16px #f9f9f9 authors, affiliation and venue lines, 28px apart. No overlay."
2. "Make a centred button row: two 168×36 buttons 30px apart, background #e8a563, 1px #e8a563 border, radius 4px, Roboto 16px/400 #1c1c1c labels, 24px section padding above and below."
3. "Create alternating feature rows: a 760px figure and a 349px text column about 37px apart; the text has a Lato 18.67px/700 #1c1c1c heading and Roboto 16px/24px #1c1c1c body; the next row swaps sides. Finish with a citation where each BibTeX line is a Source Code Pro 16px paragraph on rgba(0,0,0,0.06)."

## Similar Pages

- Google Sites research pages using an "image with title" header banner and the Lato/Roboto theme fonts.
- Robotics planning pages whose UI accent is sampled from the simulation palette.

## Quick Start

```css
:root {
  --paper: #ffffff;
  --ink: #1c1c1c;
  --hero-text: #f9f9f9;
  --sand: #e8a563;
  --teal: #135255;
  --wall: #6c553c;
  --code-wash: rgba(0, 0, 0, 0.06);
  --font-head: "Lato", sans-serif;
  --font-body: "Roboto", sans-serif;
  --font-code: "Source Code Pro", Arial, monospace;
  --content: 1154px;
  --section-pad: 24px;
}
.button { background: var(--sand); border: 1px solid var(--sand); border-radius: 4px; color: var(--ink); width: 168px; height: 36px; font: 400 16px var(--font-body); }
```

## Provenance

- **URL**: https://sites.google.com/view/ditree
- **Paper**: Train-Once Plan-Anywhere Kinodynamic Motion Planning via Diffusion Trees (arXiv 2508.21001), Yaniv Hassidof, Tom Jurgenson, Kiril Solovey (Technion).
- **Venue**: CoRL 2025 (the citation names the 9th Annual Conference on Robot Learning).
- **Selection reason**: the arXiv comment states acceptance at CoRL 2025 and links this project page.
- **Template credit**: Google Sites (new Sites) with an image-title header; no template credit on the page.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), DOM probes of the hero, buttons, sections, embeds and citation at 1440 and 700px, and the 1440×900 and full-page screenshots, on 2026-10-28. The Google Sites theme CSS was not read; values come from the render.
