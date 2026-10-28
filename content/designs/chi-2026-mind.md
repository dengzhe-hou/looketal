# MIND — Style Reference

> A clinic's quiet waiting room rendered in shadcn gray: one heavy black wordmark with a soft drop shadow, an italic promise beneath it, and a single amber medal.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the compiled Tailwind v4 stylesheet (`index-Cq0fg1mJ.css`) and React bundle (`index-dxREf_PP.js`) read directly. The page is a Vite + React app using shadcn/ui components; colors are oklch tokens, converted to hex below. The teaser image loads after the first paint: the pool 1440×900 screenshot shows the abstract directly under the buttons, while the computed render and the full-page screenshot place a 542px teaser between them. The YouTube embed paints as a black rectangle in headless capture.

## Overview

A short, centred page (about 2,200px tall) on white in a column that is 55% of the viewport at desktop widths (774px at 1440). The header stacks a 60px extra-bold "MIND" wordmark with a CSS drop shadow, a two-line 24px italic medium subtitle, three lines of underlined gray author links with superscripts, two lines of affiliations each preceded by a small institution logo, an "*Equal contribution" note, an amber "🏅 Best Paper Honorable Mention Award" line and a row of four shadcn outline buttons (Paper, Preprint, Code, Prototypes ▾) with Lucide icons. Below: a 542px teaser screenshot of the dashboard with 8px radius, a justified 16px description paragraph that underlines the M, I, N and D initials, a "Video Teaser" section (24px semibold heading, 1px gray separator, a gray "full paper talk" link line and a 16:9 black video well with 8px radius), a "BibTeX" section with a #f5f5f5 code block and a Copy button, and a footer with "© SEA Lab 2026" on the left and the lab logo on the right.

## First Viewport

Color share (8-color quantization of the pool 1440×900 shot, taken before the teaser loaded): white #ffffff 79.5% plus near-whites #fbfbfb 2.1%, #fffffe 0.7%, #fdffff 0.7%; black #000000 5.2% (the video well and the wordmark); grays #d7d7d6 5.0%, #9e9e9e 3.8%, #f0f0f0 3.1% (antialiased text, button borders, underlines). The amber award line and the small logos are too small to form clusters.

Anatomy in DOM order (desktop 1440px; root `div.min-h-screen.flex.flex-col.items-center.px-4.py-8.space-y-8`; content wrapper `w-full sm:w-[75%] md:w-[65%] lg:w-[55%]` = 774px from x=333; everything centred):

1. **Wordmark** (`h1.text-6xl.font-extrabold.mb-2.text-center.drop-shadow-lg`, y=32, 60px tall): "MIND", 60px / 800, line-height 1, #0a0a0a, `filter: drop-shadow(rgba(0, 0, 0, 0.15) 0px 4px 4px)`. Margin-bottom 8px.
2. **Subtitle** (`h2.text-2xl.font-medium.mb-2.text-center.italic`, y=100, 64px tall): two lines, 24px / 500 italic, line-height 32px, #0a0a0a. Margin-bottom 8px.
3. **Authors** (y=172 to 244, three lines): links 16px / 400, line-height 24px, #4a5565 (`text-gray-600`) with underline; superscripts 12px #737373 ("1*" marks equal contribution); comma separated.
4. **Affiliations** (y=248 to 296, two lines): 14px #737373, each institution led by a 24×24 logo image (Columbia, UW, Hamilton-Madison House, Weill Cornell, Oregon, Cornell, Northeastern) and a superscript number.
5. **Equal-contribution note** (`div.text-sm.text-muted-foreground.mb-2`, y≈304): "*Equal contribution", 14px #737373.
6. **Award** (`div.mb-2.text-amber-600`, y=332, 19px tall): "🏅 Best Paper Honorable Mention Award", 16px / 400, #e17100. Margin-bottom 8px.
7. **Buttons** (`div.flex.flex-row.flex-wrap.gap-4.mb-4.max-w-xl.mx-auto`, y=359, 36px tall): four outline buttons 16px apart within a 576px row. Margin-bottom 16px.
8. **Teaser** (`section.w-full.mb-6` → `div.lg:w-[70%].mt-8.mb-4.rounded-lg.overflow-hidden`, image at y=443, 542×372): margin-top 32px, radius 8px, no border or shadow; the image itself shows the dashboard UI with a blue frame.
9. **Description** (`p.leading-[1.5].text-justify`, y=831, 216px tall): 16px / 400, line-height 24px, justified, #0a0a0a; the M, I, N, D initials of the acronym are underlined and "narrative" is italic.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | --background, oklch(1 0 0) | page background, button fills, Copy button |
| Ink | #0a0a0a | --foreground, oklch(0.145 0 0) | wordmark, subtitle, headings, body text, button labels |
| Author Gray | #4a5565 | Tailwind `text-gray-600`, oklch(0.446 0.03 256.802) | author links, "full paper talk" line |
| Muted | #737373 | --muted-foreground, oklch(0.556 0 0) | affiliations, superscripts, equal-contribution note, footer text |
| Border | #e5e5e5 | --border, oklch(0.922 0 0) | button borders, section separators |
| Muted Fill | #f5f5f5 | --muted, oklch(0.97 0 0) | BibTeX block, button hover (`--accent`) |
| Amber | #e17100 | Tailwind `text-amber-600`, oklch(0.666 0.179 58.318) | award line |
| Video Black | #000000 | `bg-black` | video well behind the YouTube iframe |
| Hover Ink | #101828 | Tailwind `hover:text-gray-900` | "full paper talk" link hover |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text | Inter, system-ui, Avenir, Helvetica, Arial, sans-serif | no web font loaded (fonts_loaded is empty); Inter only if installed, otherwise system-ui (Segoe UI on Windows, SF Pro on macOS) | Inter |
| Code | ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace | Consolas on Windows | JetBrains Mono |
| Icons | Lucide (inline SVG) | — | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Wordmark | `h1.text-6xl.font-extrabold` | 60px / 800 / 1, drop shadow | #0a0a0a |
| Subtitle | `h2.text-2xl.font-medium.italic` | 24px / 500 italic / 32px | #0a0a0a |
| Authors | `a.text-gray-600.underline` | 16px / 400 / 24px, underlined | #4a5565 |
| Superscript | `sup` | 12px | #737373 |
| Affiliations | `.text-sm.text-muted-foreground` | 14px / 400 / 20px | #737373 |
| Award | `.text-amber-600` | 16px / 400 | #e17100 |
| Button | shadcn `Button variant="outline"` | 14px / 500 / 20px | #0a0a0a |
| Section heading | `h2.text-2xl.font-semibold.mb-2` | 24px / 600 / 32px | #0a0a0a |
| Body | `p.leading-[1.5].text-justify` | 16px / 400 / 24px | #0a0a0a |
| Video note | `p.text-gray-600` | 16px / 400 | #4a5565 |
| BibTeX | `pre.text-sm.font-mono` | 14px / 22.75px | #0a0a0a |
| Copy button | `button.text-xs` | 12px / 500 monospace | #0a0a0a |
| Footer | `footer span` | 14px / 20px | #737373 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Wordmark | — | none | `filter: drop-shadow(rgba(0, 0, 0, 0.15) 0px 4px 4px)` |
| Outline buttons | 8px | 1px #e5e5e5 | `0 1px 2px rgba(0,0,0,0.05)` (shadow-xs); hover fill #f5f5f5 |
| Teaser | 8px, overflow hidden | none | none |
| Video well | 8px, overflow hidden | none | none |
| Section separator | 0 | 1px #e5e5e5 line (shadcn `Separator`), 16px below | none |
| BibTeX block | 8px | none | none |
| Copy button | 8px | 1px #e5e5e5 | shadow-xs |
| Footer | 0 | none | none |

## Layout Metrics

- **Root**: `min-h-screen w-full flex flex-col items-center px-4 py-8 space-y-8` (16px side padding, 32px top and bottom).
- **Content column**: `w-full sm:w-[75%] md:w-[65%] lg:w-[55%]` of the padded width; 774px at 1440 (x=333 to 1107).
- **Header gaps**: wordmark, subtitle, award and equal-contribution note each `mb-2` (8px); button row `max-w-xl` (576px) with `gap-4` and `mb-4`.
- **Media**: teaser wrapper and video well are `w-full sm:w-[90%] md:w-[80%] lg:w-[70%]` of the column (542px at 1440), centred; teaser `mt-8 mb-4`, video `aspect-video mb-4` (542×305).
- **Sections**: `section.w-full.mb-6` (24px apart); heading `mb-2`, separator `mb-4`.
- **BibTeX**: `pre` padding 16px, `whitespace-pre-wrap`; Copy button absolute at top 8px, right 8px.
- **Footer**: `w-full mt-5 flex justify-between items-center py-6`; logo 125×64 on the right.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| <640px | 16px | 16px | 60px | column 100%; media 100%; Prototypes dropdown hidden (`hidden sm:block`) |
| ≥640px | 16px | 16px | 60px | column 75%; media 90% of column; dropdown shown |
| ≥768px | 16px | 16px | 60px | column 65%; media 80% |
| ≥1024px | 16px | 16px | 60px | column 55% (774px at 1440); media 70% (542px) |

## Components

- **Outline button** (shadcn `Button variant="outline"`): inline-flex, height 36px, padding 8px 16px (12px sides when it has an icon), radius 8px, white fill, 1px #e5e5e5 border, shadow 0 1px 2px rgba(0,0,0,0.05), 14px / 500 #0a0a0a label after a 16px Lucide icon (file-text, file-pen, GitHub, a person-pointer glyph) with 8px gap. Hover fill #f5f5f5. "Prototypes" opens a dropdown menu with "MIND" and "FACT (Baseline)" and has a 12px chevron.
- **Wordmark**: 60px / 800 #0a0a0a with drop-shadow(rgba(0, 0, 0, 0.15) 0px 4px 4px), centred.
- **Affiliation chip**: superscript number, 24×24 logo (object-fit contain), then the name, 14px #737373, laid out inline and wrapping.
- **Section heading with separator**: 24px / 600 #0a0a0a left aligned, 8px gap, full-width 1px #e5e5e5 line, 16px gap.
- **Video well**: 16:9, 8px radius, black background, YouTube iframe filling it; a 16px #4a5565 line above with a video icon and an underlined "full paper talk" link.
- **BibTeX block**: #f5f5f5, radius 8px, padding 16px, 14px monospace with 22.75px line-height, wrapping; outline "Copy" button (12px, copy icon) pinned top right.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Wordmark / subtitle | yes | 60px extra-bold with drop shadow, 24px italic subtitle |
| Authors / affiliations | yes | underlined gray links, logo-led affiliations |
| Award | yes | amber text line with medal emoji |
| Link buttons | yes | four shadcn outline buttons, one dropdown |
| Teaser | yes | 542px dashboard screenshot, 8px radius (loads late) |
| Description | present but non-standard | a justified paragraph with no "Abstract" heading |
| Video | yes | black 16:9 well with 8px radius |
| BibTeX | yes | muted gray block with Copy button |
| Results tables | absent from the source | none |
| Footer | yes | copyright left, lab logo right |

## Adapting to Other Content

- **More authors**: keep 16px underlined #4a5565 links on centred lines within the 774px column; mark equal contribution with "*" in the superscript and keep the 14px note line.
- **A results table**: shadcn-style table in the 774px column: 14px #0a0a0a cells, header 500 #737373, 1px #e5e5e5 row borders, no fills; place it under a 24px / 600 heading with the 1px separator.
- **Long publication or news lists**: a plain list under a separator heading, 16px / 24px, dates in 14px #737373 to the left.
- **More sections**: repeat `section.mb-6` with heading, separator and content; media stays at 70% of the column (542px at 1440).
- **More awards**: one amber #e17100 line each, 8px apart, above the buttons.

## Do's and Don'ts

- Do keep the palette neutral (#0a0a0a, #737373, #e5e5e5, #f5f5f5) with amber only for the award.
- Do use shadcn outline buttons with Lucide icons, not filled pills.
- Do keep the drop shadow on the wordmark and nowhere else on text.
- Do centre the header and left-align section headings.
- Don't widen media past 70% of the column at desktop.
- Don't add a colored hero or background; the page is white.
- Don't replace the separator line under headings with a heavier rule.

## Surfaces

White page; #f5f5f5 for the BibTeX block and button hover; a black 16:9 video well. Buttons carry a 5% hairline shadow; nothing else is raised.

## Imagery

A dense dashboard screenshot (patient data panels, insight cards, quote bubbles from clinicians) as the teaser; small full-color university and hospital logos in the affiliations; a lab logo in the footer; the video is the paper talk on YouTube.

## Layout

A centred 774px column (55% of the viewport at desktop) with a stacked header, then three short sections spaced 24px apart and a two-ended footer. Media is narrower than text (542px) and centred.

## Agent Prompt Guide

Quick colors: background #ffffff, text #0a0a0a, authors #4a5565, muted #737373, borders #e5e5e5, muted fill #f5f5f5, award #e17100.

1. "Build a centred header in a column 55% of the viewport wide (min 16px gutters): wordmark 60px / 800 #0a0a0a with filter drop-shadow(rgba(0,0,0,0.15) 0px 4px 4px); subtitle 24px / 500 italic, 32px line-height; authors 16px underlined #4a5565 with 12px #737373 superscripts; affiliations 14px #737373 each led by a 24px logo; an award line 16px #e17100 with a medal emoji; elements 8px apart."
2. "Make a row of outline buttons 16px apart in a 576px row: height 36px, padding 8px 16px, radius 8px, white fill, 1px #e5e5e5 border, shadow 0 1px 2px rgba(0,0,0,0.05), 14px / 500 #0a0a0a label after a 16px Lucide icon; hover fill #f5f5f5."
3. "Create a section: 24px / 600 #0a0a0a heading, 8px below a 1px #e5e5e5 full-width separator, 16px below that the content; media centred at 70% of the column with radius 8px; a BibTeX block on #f5f5f5, radius 8px, padding 16px, 14px monospace, with an outline Copy button at top 8px right 8px."

## Similar Pages

- React + shadcn/ui project pages with outline buttons and oklch neutral tokens.
- Visualization and health-informatics pages that lead with a wordmark-style acronym title.

## Quick Start

```css
:root {
  --background: #ffffff;
  --foreground: #0a0a0a;
  --muted: #f5f5f5;
  --muted-foreground: #737373;
  --border: #e5e5e5;
  --author: #4a5565;
  --award: #e17100;
  --radius-md: 8px;
  --font: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  --column: calc((100vw - 32px) * 0.55);
  --media: 70%;
}
```

## Provenance

- **URL**: https://sea-lab.space/MIND/
- **Paper**: MIND: Empowering Mental Health Clinicians with Multimodal Data Insights through a Narrative Dashboard (arXiv 2601.14641), Ruishi Zou, Shiyu Xu, Margaret E. Morris, Jihan Ryu, Timothy Becker, Nicholas Allen, Anne Marie Albano, Randy Auerbach, Dan Adler, Varun Mishra, Lace Padilla, Dakuo Wang, Ryan Sultan, Xuhai "Orson" Xu.
- **Venue**: CHI 2026, Best Paper Honorable Mention Award (as shown on the page).
- **Selection reason**: the arXiv comment states acceptance at CHI 2026 (conditionally accepted); the project page is the homepage of the paper's code repository (sea-lab-space/MIND) linked in the paper body.
- **Template credit**: none stated; a Vite + React app with Tailwind v4 and shadcn/ui; footer reads "© SEA Lab 2026".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted computed-style probes of the header, buttons, separators, video and BibTeX, the pool 1440×900 and full-page screenshots, and the compiled CSS and JS bundle read directly, on 2026-10-28.
