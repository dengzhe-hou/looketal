# LingoQ — Style Reference

> A friendly product one-pager in a light weight: a fat black wordmark, airy Nunito prose, sky-blue section labels and candy-colored pill buttons.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, a second 1440×900 screenshot taken after a 4s wait, and the compiled Tailwind stylesheet (`index.ac3f4b59.css`) and React bundle (`index.01536059.js`) read directly. The page is a Parcel-built React app with no semantic headings (every heading is a styled `div`). The teaser image (`lingoq_teaser.png`, 904×563) loads late: the pool screenshots were captured before it arrived and show the Abstract directly under the subtitle, while the computed render and the later screenshot show the teaser between subtitle and Abstract. The render is used below. The YouTube embed in the Demonstration Video frame does not paint in headless capture, so the frame looks empty in screenshots.

## Overview

A narrow, left-aligned page (about 3,400px tall) on white in a 1000px Tailwind container with 48px side padding. It opens like a product page: a small bold sky-blue kicker "CHI 2026 Paper", a 60px bold black "LingoQ" wordmark, and a 30px light (300) subtitle with "EFL Learning" and "Work" set one step bolder. Below sits a wide illustrated teaser (a chat assistant panel, two line-drawn people, an orange "Language queries → Work-related quiz" arrow and a phone quiz UI). Sections are introduced by 30px sky-blue (#4592ec) labels in regular weight: Abstract (18px light body text) followed by three pill buttons in teal, coral and slate with white 600 labels and soft shadows; Demonstration Video in a 4px translucent slate frame with 12px radius; Contributors as a two-column grid of 120px round photos with name, role and affiliation, plus purple italic notes; a row of institution logos; Citing This Work with a purple-ruled citation and a purple-bordered BibTeX block; Acknowledgments; and a thin purple-topped footer.

## First Viewport

Color share (8-color quantization). Pool screenshot (teaser not yet loaded): white #ffffff 82.0%, light grays #cdd0d2 5.8%, #e8eaeb 3.7%, #f6f6f5 2.9%, #9ca0a3 2.5%, #fcfcfc 2.2% (text antialiasing and the empty video frame edge), #fffffe 0.4%, #feffff 0.4%. Later screenshot with the teaser: white #ffffff 74.1%, sage gray #cad0c5 7.1%, warm gray #8c837d 5.2% (teaser line art and UI), pale mint #e6eee8 4.9%, cream #f5f1ee 3.8%, #fafafb 2.8%, #efffff 1.5%, #fffffc 0.5%. The sky-blue kicker and the orange teaser arrow are too small to form clusters.

Anatomy in DOM order (desktop 1440px; `main.container.mx-auto.px-4.sm:px-12.pt-6`: max-width 1000px, padding 24px 48px 0, so content runs x=268 to 1172; everything left aligned):

1. **Kicker** (`div.font-bold.text-lg.text-[#4592ec].mb-3`, y=24, 28px tall): "CHI 2026 Paper", Nunito Sans 18px / 700, line-height 28px, #4592ec. Margin-bottom 12px.
2. **Wordmark** (`div.font-bold.text-6xl.mb-3`, y=64, 60px tall): "LingoQ", 60px / 700, line-height 1, #000000. Margin-bottom 12px.
3. **Subtitle** (`div.font-light.text-3xl.sm:leading-[2.5rem]`, y=136, 80px tall, two lines): 30px / 300, line-height 40px, black; "EFL Learning" and "Work" in `<b>` render at 400 (bolder than 300).
4. **Teaser** (`div.mt-10.rounded-xl.overflow-hidden`, y=256, 904×563): margin-top 40px, radius 12px, no visible border or shadow (the `border-orange-600/10` class has no width).
5. **Abstract label** (`div.section-title.text-3xl`, y=867): the section wrapper adds 48px top padding (`md:pt-12`) after the teaser; 30px / 400 #4592ec, margin-bottom 16px.
6. **Abstract text** (`p`, y=919, 336px tall): 18px / 300, line-height 28px, black, left aligned, max 904px.

The three buttons follow at y=1271 and the video frame at y=1447.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | (Tailwind `bg-white` via `body{background:#fff}`) | page background, button labels |
| Black | #000000 | (`--foreground-rgb: 0,0,0`) | wordmark, subtitle, body text, names, citation |
| Sky Blue | #4592ec | (`text-[#4592ec]`) | "CHI 2026 Paper" kicker, all section labels |
| Teal | #14b8a6 | (Tailwind `bg-teal-500`) | Paper button |
| Coral | #f87171 | (Tailwind `bg-red-400`) | arXiv button |
| Slate | #64748b | (Tailwind slate-500, `.icon-label-button` default) | Source code button; video frame border at 20% |
| Icon Gray | #6b7280 | (Tailwind `text-gray-500`) | home icon after contributor names |
| Purple | #a855f7 | (Tailwind `text-purple-500`) | contributor notes; citation rules and BibTeX border at 30% |
| Deep Purple | #9333ea | (Tailwind purple-600) | footer top rule at 30% |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text | Nunito Sans, ui-sans-serif, system-ui, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji | Nunito Sans 300, 400, 600, 700 (Google Fonts, opsz axis) | Mulish |
| Code | ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace | Consolas on Windows | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Kicker | `.font-bold.text-lg.text-[#4592ec]` | 18px / 700 / 28px | #4592ec |
| Wordmark | `.font-bold.text-6xl` | 60px / 700 / 1 | #000000 |
| Subtitle | `.font-light.text-3xl.sm:leading-[2.5rem]` | 30px / 300 / 40px; bold words 400 | #000000 |
| Section label | `.section-title.text-3xl.text-[#4592ec]` | 30px / 400 / 36px | #4592ec |
| Body | `p` | 18px / 300 / 28px | #000000 |
| Button label | `.icon-label-button > span` | 16px / 600 | white |
| Contributor name | `.text-xl.font-semibold` | 20px / 600 / 28px | #000000 |
| Contributor role, affiliation | `.font-light` | 16px / 300 / 24px | #000000 |
| Contributor note | `.font-light.italic.text-sm.text-purple-500` | 14px / 300 italic / 20px | #a855f7 |
| Citation | `.border-y-2` block | 16px; title line 700 | #000000 |
| BibTeX | `p.font-mono.text-xs.sm:text-sm` | 14px / 300 / 20px (12px below 640px) | #000000 |
| Footer | `.text-sm.text-center` | 14px | #000000 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Teaser | 12px (`rounded-xl`), overflow hidden | none visible | none |
| Pill buttons | 9999px | none | `0 4px 6px -1px #0000001a, 0 2px 4px -2px #0000001a`; hover `0 20px 25px -5px #0000001a, 0 8px 10px -6px #0000001a` with scale(1.1) |
| Video frame | 12px, overflow hidden | 4px rgba(100,116,139,0.2) | none |
| Contributor photo | 9999px (120px circle) | none | none |
| Citation block | 0 | 2px rgba(168,85,247,0.3) top and bottom | none |
| BibTeX block | 8px (`rounded-lg`) | 2px rgba(168,85,247,0.3) | none |
| Footer | 0 | 2px rgba(147,51,234,0.3) top | none |

## Layout Metrics

- **Container**: Tailwind `.container` with custom steps: max-width 480px (≥480), 600px (≥600), 728px (≥728), 1000px (≥1000); `px-4` (16px) below 640px, `sm:px-12` (48px) above; `pt-6` (24px). At 1440 the text column is 904px from x=268.
- **Header stack**: kicker and wordmark each margin-bottom 12px; teaser margin-top 40px.
- **Sections**: each section wrapper has `pt-0 md:pt-12` (48px top padding at ≥768px); labels margin-bottom 16px.
- **Buttons**: `flex flex-wrap gap-4 mt-4` (16px gaps, 16px above), 44px tall; padding 8px 16px 8px 8px (Paper and arXiv override left padding to 16px).
- **Video**: frame 904px wide with a 4px border; iframe `aspect-video` 896×504.
- **Contributors**: `grid grid-cols-1 sm:grid-cols-2 gap-6` (two 440px columns, 24px gap); each card a flex row of a 120px photo and a text block with 16px left margin.
- **Logos**: `mt-8 flex flex-wrap gap-6 gap-y-8`, logos at fixed widths 120–200px.
- **Citation**: `border-y-2 py-3`; BibTeX label 16px / 700 then the mono block with `p-3`.
- **Acknowledgments**: wrapper padding 48px 0 32px; footer `p-4`, full width.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| <640px | 16px | 18px | wordmark 60px; subtitle 24px / 32px | contributors 1 column; BibTeX 12px |
| ≥640px | 48px | 18px | subtitle 30px / 40px | contributors 2 columns; BibTeX 14px |
| ≥768px | 48px | 18px | same | sections gain 48px top padding |
| ≥1000px | 48px inside 1000px | 18px | same | container capped at 1000px |

## Components

- **Pill button** (`.icon-label-button`): flex, height 44px, padding 8px 16px 8px 8px, radius 9999px, background #64748b (Source code), #14b8a6 (Paper, `pl-4`) or #f87171 (arXiv, `pl-4`); a 24px white icon (document glyph, arXiv logo, GitHub mark) then a white 16px / 600 label 8px to its right; shadow `0 4px 6px -1px #0000001a, 0 2px 4px -2px #0000001a`. Hover: scale(1.1) over 150ms and the larger shadow.
- **Section label** (`.section-title`): 30px / 400 Nunito Sans #4592ec, left aligned, 16px below, no rule.
- **Video frame**: `overflow-hidden rounded-xl border-4 border-slate-500/20` around a 16:9 iframe.
- **Contributor card**: 120px circular photo (or a blank 120px slot when there is none), then name 20px / 600 black with a 20px #6b7280 home icon linking to the homepage, role and affiliation 16px / 300 on separate lines, optional purple italic 14px note.
- **Citation block**: 2px rgba(168,85,247,0.3) rules above and below, 12px vertical padding; author line, bold title line, venue line and DOI line at 16px.
- **BibTeX block**: monospace 14px / 300, padding 12px, 2px rgba(168,85,247,0.3) border, radius 8px.
- **Footer**: full-width strip with a 2px rgba(147,51,234,0.3) top rule, 16px padding, centred 14px copyright.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Venue kicker | yes | bold sky-blue "CHI 2026 Paper" above the title |
| Title / subtitle | yes | 60px bold wordmark, 30px light subtitle, left aligned |
| Teaser | yes | wide illustration with 12px radius (loads late) |
| Authors in header | absent from the source | authors appear only in the Contributors grid and citation |
| Abstract | yes | 18px light paragraph under a sky-blue label |
| Link buttons | present but non-standard | placed after the abstract, three colors |
| Video | yes | slate-framed 16:9 YouTube embed |
| Contributors | yes | 2-column grid with round photos and roles |
| Institution logos | yes | row of logos (DGIST, Virginia Tech, Yonsei, NAVER AI Lab) |
| Citation + BibTeX | yes | purple-ruled citation and purple-bordered mono block |
| Acknowledgments | yes | label and paragraph |
| Results tables | absent from the source | none |
| Footer | yes | purple top rule, centred copyright |

## Adapting to Other Content

- **More authors**: add contributor cards to the 2-column grid (440px each at 1440, 24px gaps); keep the 120px circle, 20px / 600 name and 16px / 300 role lines; use a blank 120px slot rather than a placeholder icon when a photo is missing.
- **A results table**: put it under a 30px #4592ec label, full 904px width, 16px Nunito Sans; header 600 black, 1px rgba(100,116,139,0.2) row rules, no fills; numbers at 400, best values 700.
- **Long publication or news lists**: a `list-disc list-outside ml-4` list at 18px / 300, dates in 600; or reuse the purple-ruled citation block per entry.
- **More links**: extra pills follow the same recipe; choose another Tailwind 400–500 hue only if the three existing colors are used up.
- **A header author line**: if authors must appear at the top, place them under the subtitle at 18px / 300 black, 12px below, before the teaser.

## Do's and Don'ts

- Do keep the page left aligned in a 904px column.
- Do use #4592ec for the kicker and every section label, at regular weight.
- Do set body text light (300) at 18px with 28px line-height.
- Do keep buttons as colored pills with white 600 labels and soft shadows.
- Don't add rules under section labels; separation is 48px of space.
- Don't centre the header or the contributors.
- Don't use the purple for anything other than citation, BibTeX, notes and the footer rule.

## Surfaces

All white. Frames are drawn with translucent borders (slate at 20% for the video, purple at 30% for citation and BibTeX) rather than fills or shadows; only the pill buttons cast shadows.

## Imagery

One line-drawn and screenshot teaser in muted grays with a cream chat panel, a green-highlighted answer, a coral quiz highlight and an orange gradient arrow; a narrated demo video; round head-shot photos; color institution logos.

## Layout

A single 904px left-aligned column: kicker, wordmark, subtitle, teaser, then sections at 48px intervals. The only grid is the 2-column contributor block.

## Agent Prompt Guide

Quick colors: background #ffffff, text #000000, section labels #4592ec, buttons #14b8a6 / #f87171 / #64748b, notes #a855f7, icon gray #6b7280.

1. "Build a left-aligned header in a 1000px container with 48px side padding and 24px top padding: kicker Nunito Sans 18px / 700 #4592ec, 12px below it the 60px / 700 black wordmark (line-height 1), 12px below that a 30px / 300 subtitle with 40px line-height and key words at 400; then a full-width teaser with 12px radius 40px below."
2. "Make sections 48px apart: label Nunito Sans 30px / 400 #4592ec with 16px below, body 18px / 300 / 28px black. After the abstract, a row of pill buttons with 16px gaps: height 44px, padding 8px 16px, radius 9999px, fills #14b8a6, #f87171 and #64748b, white 16px / 600 labels with a 24px icon, shadow 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1), hover scale(1.1)."
3. "Create a contributors grid of two 440px columns with 24px gaps: 120px round photo, then name 20px / 600 black with a 20px #6b7280 home icon, role and affiliation 16px / 300, optional 14px italic #a855f7 note. Follow with a citation block ruled 2px rgba(168,85,247,0.3) top and bottom and a monospace BibTeX box with the same 2px border, radius 8px, padding 12px."

## Similar Pages

- Lab-built React or Tailwind project pages from industry research labs with product-style headers.
- HCI pages that end with a photo grid of contributors and their roles.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #000000;
  --accent: #4592ec;
  --btn-paper: #14b8a6;
  --btn-arxiv: #f87171;
  --btn-code: #64748b;
  --note: #a855f7;
  --icon: #6b7280;
  --rule-purple: rgba(168, 85, 247, 0.3);
  --frame-slate: rgba(100, 116, 139, 0.2);
  --font: "Nunito Sans", ui-sans-serif, system-ui, sans-serif;
  --container: 1000px;
  --gutter: 48px;
  --section-gap: 48px;
}
```

## Provenance

- **URL**: https://naver-ai.github.io/lingo-q/
- **Paper**: LingoQ: Bridging the Gap between EFL Learning and Work through AI-Generated Work-Related Quizzes (arXiv 2509.17477), Yeonsun Yang, Sang Won Lee, Jean Y. Song, Sangdoo Yun, Young-Ho Kim.
- **Venue**: CHI 2026.
- **Selection reason**: the arXiv comment states acceptance at CHI 2026 (conditionally accepted); the project page is linked in the paper body (arXiv HTML).
- **Template credit**: none stated; a React app bundled with Parcel and styled with Tailwind; footer reads "Copyright © 2025-2026 NAVER AI Lab".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted computed-style probes of the header stack, buttons, video frame, contributor cards and citation, the pool 1440×900 and full-page screenshots plus a second 1440×900 screenshot after a 4s wait (teaser loaded), and the compiled CSS and JS read directly, on 2026-10-28.
