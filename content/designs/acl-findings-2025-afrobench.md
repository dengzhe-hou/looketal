# Tailwind Benchmark Launch — Style Reference

> A product launch page for a benchmark: black-weight question headline, a pulsing yellow announcement, and three white stat cards on a cool off-white floor.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (`tools/computed_style.py`: computed styles of the nav, both `h1`s, stat cards, buttons, sections, `pre` and footer, first-viewport anatomy and color share), the first-viewport screenshot and the full-page capture, and the page's single HTML file, which styles everything with Tailwind CSS v3 utility classes from `cdn.tailwindcss.com` (no custom stylesheet). Utility classes resolve to Tailwind's default palette and scale, so the hex values below are what the classes compute to and match the render. Positions are document coordinates at 1440px wide.

## Overview

AfroBench is a single hand-written Tailwind page. A white top bar (85px tall, 1px #e5e7eb bottom border, medium shadow) carries the "AfroBench" wordmark at 30px/800 on the left and four 16px/500 text links on the right. The bar is not sticky; it scrolls away with the page. Below it, on a #f9fafb floor, a centered 48px weight-900 question ("How Good are Large Language Models on African Languages?") in #111827 is followed by an 18px #374151 subtitle and an 18px summary paragraph. Then a loud yellow (#facc15) rounded announcement box with 30px/800 brown text pulses (`animate-pulse`), three pill buttons follow (two #eab308 yellow, one #3b82f6 blue), and a row of three white stat cards with 8px radius, a 1px #e5e7eb border and a large soft shadow. The overview map figure sits below at 60% width with an 8px radius and shadow. Further down, a centered gray justified abstract, a two-column text-plus-scatter-plot section, a second two-column LITE section, a bulleted Key Insights list, and a white citation card with a #f3f4f6 BibTeX block. All type is the system sans stack (Segoe UI on Windows); no web font loads.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): floor #f9fafb 55.5%, white #ffffff 19.6% (nav bar and stat cards), a mixed khaki bucket #c5bd9d 12.4% (the quantizer's merge of the yellow banner, the yellow pills and dark headline pixels), near-floor #f9fafa 9.4%, remainder under 2.5%. The yellow is the only saturated color above the fold apart from the blue Codebase pill.

Anatomy in DOM order (y = top of element box):

1. **Nav bar** (`nav.flex.justify-between.p-6.bg-white.shadow-md.border-b`), y 0, height 85, full width, white, padding 24px, 1px #e5e7eb bottom border. Gap to headline 64px.
2. **Wordmark** (`h1.text-3xl.font-extrabold.text-gray-800`), x 24, y 24, "AfroBench", 30px/36px, weight 800, #1f2937, left.
3. **Nav links** (`a.font-medium`, four in `ul.flex.space-x-6`), y 31, 16px/24px weight 500 #111827, 24px apart, right edge at x 1416; hover #ca8a04.
4. **Headline** (`header h1.text-4xl.sm:text-5xl.font-black`), y 149, 896px wide (max-w-4xl), two lines, 48px/48px weight 900, #111827, centered. Gap 16px.
5. **Subtitle** (`p.mt-4.text-gray-700.text-lg`), y 261, 18px/28px, #374151, centered. Gap 48px.
6. **Summary** (`section.mt-12.max-w-4xl p.text-lg.text-gray-700`), y 337, 896px, two lines 18px/28px #374151, centered. Gap 48px.
7. **Announcement banner** (`div.inline-block.bg-yellow-400.py-4.px-6.rounded-xl.font-extrabold.text-3xl.shadow-lg.animate-pulse`), y 441, about 793×68, #facc15 fill, 12px radius, text 30px/36px weight 800 #713f12 with an underlined "Hugging Face Spaces" link and a rocket emoji. Gap 38px.
8. **Buttons**, y 547, height 48: "ArXiv" (95px) and "View Leaderboard" (201px) in #eab308, then "Codebase" (129px, 16px left margin) in #3b82f6; all 18px/28px weight 700, #111827 text, padding 12px 24px, full radius. Gap 38px.
9. **Stat cards** (`section.grid.md:grid-cols-3.gap-6.max-w-5xl`), y 633, three cards 317px wide (1024px row, 24px gaps), 162px tall; heading 24px/32px 700 #1f2937, text 16px/24px #374151, centered. Gap 48px.
10. **Overview figure** (`img.max-w-[60%].shadow-lg.rounded-lg`), y 843, 864×487, centered, 8px radius; caption 14px #9ca3af 16px below. The fold cuts the figure at its top.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Ink | #111827 | `text-gray-900` (body) | Headline, nav links, button labels, section headings, body default |
| Charcoal | #1f2937 | `text-gray-800` | Wordmark, stat card headings, BibTeX text |
| Slate | #374151 | `text-gray-700` | Subtitle, summary, card text, evaluation paragraphs, figure captions in sections |
| Abstract Grey | #6b7280 | `text-gray-500` | Abstract paragraph, footer |
| Caption Grey | #9ca3af | `text-gray-400` | Overview figure caption |
| List Grey | #4b5563 | `text-gray-600` | Key Insights bullets |
| Floor | #f9fafb | `bg-gray-50` | Page background, abstract section |
| White | #ffffff | `bg-white` | Nav bar, stat cards, citation card |
| Hairline | #e5e7eb | `border-gray-200` | Nav bottom border, card borders |
| Code Wash | #f3f4f6 | `bg-gray-100` | BibTeX `pre` fill |
| Code Border | #d1d5db | `border-gray-300` | BibTeX `pre` border |
| Banner Yellow | #facc15 | `bg-yellow-400` | Announcement banner; yellow pill hover |
| Button Yellow | #eab308 | `bg-yellow-500` | ArXiv and View Leaderboard pills |
| Banner Brown | #713f12 | `text-yellow-900` | Banner text and link |
| Banner Link Hover | #854d0e | `hover:text-yellow-800` | "Hugging Face Spaces" link in the banner on hover |
| Hover Amber | #ca8a04 | `hover:text-yellow-600` | Nav link hover |
| Button Blue | #3b82f6 | `bg-blue-500`, `text-blue-500` | Codebase pill, "tasks taxonomy" link |
| Blue Hover | #60a5fa | `hover:bg-blue-400` | Codebase pill hover |

## Tokens — Typography

- **Family**: declared Tailwind `font-sans`, `ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"`. `fonts_loaded` is empty: no web font is fetched, so it renders in the OS UI face (Segoe UI on Windows, San Francisco on macOS). Substitute: Inter, which keeps the same compact proportions across platforms.
- **Mono**: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas…` for the BibTeX block (Consolas on Windows).

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Headline | `header h1.sm:text-5xl.font-black` | 48px / 48px | 900 | #111827 |
| Wordmark | `nav h1.text-3xl.font-extrabold` | 30px / 36px | 800 | #1f2937 |
| Banner text | `.text-3xl.font-extrabold` | 30px / 36px | 800 | #713f12 |
| Section heading | `h2.text-3xl.font-bold` | 30px / 36px | 700 | #111827 |
| Card heading | `h2.text-2xl.font-bold` | 24px / 32px | 700 | #1f2937 |
| Abstract | `.text-xl.leading-relaxed` | 20px / 32.5px | 400 | #6b7280, justified |
| Subtitle, summary, button | `.text-lg` | 18px / 28px | 400 (buttons 700) | #374151 (buttons #111827) |
| Body, card text, nav | `p`, `a.font-medium` | 16px / 24px | 400 (nav 500) | #374151 (nav #111827) |
| Caption, footer, BibTeX | `.text-sm` | 14px / 20px | 400 | #9ca3af / #6b7280 / #1f2937 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Nav bar | 0 | 1px solid #e5e7eb bottom | `shadow-md`: 0 4px 6px -1px rgba(0,0,0,.1), 0 2px 4px -2px rgba(0,0,0,.1) |
| Announcement banner | 12px (`rounded-xl`) | none | `shadow-lg`: 0 10px 15px -3px rgba(0,0,0,.1), 0 4px 6px -4px rgba(0,0,0,.1) |
| Pill buttons | 9999px | none | `shadow-md` |
| Stat cards, citation card | 8px (`rounded-lg`) | 1px solid #e5e7eb | `shadow-lg` |
| Figures | 8px | none | `shadow-lg` |
| BibTeX `pre` | 8px | 1px solid #d1d5db | none |

Spacing follows Tailwind's 4px scale: 48px (`mt-12`) between every hero block and section, 24px card and column gaps, 24px card padding, 16px `pre` padding.

## Layout Metrics

- **No global container.** Each section sets its own width: headline and summary `max-w-4xl` (896px), stat cards and later sections `max-w-5xl` (1024px, x 208–1232), abstract wrapper `max-w-7xl` (1280px) with `lg:px-8` and the text itself `max-w-3xl` (768px).
- **Hero**: nav 85px, then 64px (`mt-16`) to the headline; 48px (`mt-12`) between summary, banner, buttons, cards and figure.
- **Stat cards**: 3 columns of 317px, 24px gap (`gap-6`), padding 24px.
- **Overview figure**: `max-w-[60%]` at ≥768px (864px at 1440), `max-w-[75%]` below.
- **Abstract**: section `py-16` (64px top and bottom) on the same #f9fafb, so it reads as plain spacing, not a band.
- **Two-column sections**: `grid md:grid-cols-2 gap-6` inside 1024px, so two 500px columns; the first section centers its columns vertically (`items-center`), the LITE section top-aligns and pushes the right image down 80px (`mt-20`). Full-width images follow at 1024px.
- **Footer**: 48px top margin, 24px vertical padding, centered 14px text.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px (`lg`) | sections centered by max-width; abstract padding 32px | 16px | 48px | 3 stat cards, 2-column sections, figure 60% |
| 768–1023px (`md`) | sections full width when narrower than 1024px | 16px | 48px | same grids; abstract padding 24px |
| 640–767px (`sm`) | no side padding on most sections | 16px | 48px | cards stack to 1 column, two-column sections stack, figure 75% |
| <640px | none on most sections; abstract 16px | 16px | 36px (`text-4xl`, 40px line) | single column; nav row does not collapse |

## Components

- **Top bar**: white `nav`, flex space-between, padding 24px, 1px #e5e7eb bottom border, `shadow-md`; wordmark 30px/800 #1f2937 left; links 16px/500 #111827 with 24px spacing, hover #ca8a04, no underline, no icons. Static, not sticky.
- **Announcement banner**: inline-block box, #facc15 fill, 12px radius, padding 16px 24px, 30px/36px weight 800 #713f12 text, underlined link inside (hover #854d0e), leading emoji, `shadow-lg`, and Tailwind `animate-pulse` (opacity 1 → 0.5 → 1 every 2s).
- **Pill button**: anchor, padding 12px 24px, full radius, 18px/28px weight 700, #111827 text, `shadow-md`; yellow variant #eab308 with hover #facc15, blue variant #3b82f6 with hover #60a5fa. No icons, no border.
- **Stat card**: white, 1px #e5e7eb border, 8px radius, `shadow-lg`, padding 24px, centered; 24px/32px 700 #1f2937 heading ("64 Languages"), 8px gap, 16px/24px #374151 one-line description.
- **Framed figure**: `img` with 8px radius and `shadow-lg`, no border; caption 14px, #9ca3af under the overview figure and #374151 under section figures, 12–16px below.
- **Citation card**: white card (same recipe as the stat card), `h2` 30px/700, then `pre` with #f3f4f6 fill, 1px #d1d5db border, 8px radius, 16px padding, 14px mono #1f2937; a follow-up line with a bold #3b82f6 link.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top navigation | yes | white static bar with wordmark and four text links |
| Title | yes | the question headline; the paper title "AfroBench" appears only as the wordmark |
| Authors and affiliations | absent from the source | names appear only inside the BibTeX |
| Announcement | yes | pulsing yellow banner |
| Link buttons | yes | three pill buttons, yellow and blue, no icons |
| Stat highlights | yes | three white cards |
| Teaser figure | yes | overview map at 60% width, rounded and shadowed |
| Abstract | yes | centered heading, 20px grey justified text, 768px |
| Results | present but non-standard | scatter plots and tables as shadowed images, no HTML tables |
| Two-column text plus figure | yes | 500px columns, 24px gap |
| Key findings | yes | 16px #4b5563 disc list, bullets inside |
| BibTeX | yes | grey `pre` inside a white card |
| Footer | yes | one centered 14px #6b7280 line |
| Video, carousel | absent from the source | |

## Adapting to Other Content

- **Authors**: add a centered line under the headline in 18px/28px #374151, names comma-separated, with superscript affiliation numbers and a 14px #6b7280 affiliation line below; keep the 48px rhythm to the summary.
- **A results table**: put a real HTML table in a white card (1px #e5e7eb border, 8px radius, `shadow-lg`, padding 24px) at 1024px; header row 14px weight 700 #1f2937 on #f3f4f6, body 14px #374151 with 1px #e5e7eb row rules, best scores in weight 700.
- **More stat cards**: keep the 3-column grid and add rows; the card copy should stay one or two lines.
- **News**: reuse the banner shape without the pulse and at 18px/700, or a white card with a dated 16px list; one yellow banner per page at most.
- **Long publication lists**: a 16px #374151 list inside the 1024px column with titles in weight 700 and #3b82f6 links.
- **More links**: add pills to the same row; keep yellow for paper/results and blue for code.

## Do's and Don'ts

- Do keep the floor #f9fafb and put content on white cards with a 1px #e5e7eb border and a soft large shadow.
- Do use weight 900 only for the headline and 800 for the wordmark and banner.
- Do space hero blocks evenly at 48px.
- Do use the same 8px radius for cards and figures and full radius for buttons.
- Don't stack more than one saturated yellow element above the fold; the pulsing banner already dominates.
- Don't mix more accent hues; yellow and one blue are the whole palette.
- Don't rely on the system font for brand consistency if exact metrics matter; load Inter.

## Surfaces

Two surfaces: the #f9fafb floor and white (#ffffff) for the nav bar and cards. Cards lift with `shadow-lg` and a hairline #e5e7eb border. The BibTeX block is #f3f4f6. Yellow #facc15 is used as a fill only on the banner.

## Imagery

Paper figures exported as PNG: a colored Africa map with category boxes (pinks, greens, blues), matplotlib scatter plots of score versus model size, a dense LaTeX results table and a language-performance chart. All are shown with an 8px radius and a soft shadow, without borders.

## Layout

A centered single column whose width changes by section (896px hero text, 1024px cards and results, 768px abstract), with two-column text-plus-figure rows in the results sections. Rendered height is about 4,960px at 1440px.

## Agent Prompt Guide

Quick colors: floor #f9fafb, cards #ffffff with #e5e7eb border, ink #111827, body #374151, muted #6b7280, banner #facc15 with #713f12 text, yellow button #eab308, blue button #3b82f6.

1. "Build a top bar: white, padding 24px, 1px solid #e5e7eb bottom border, shadow 0 4px 6px -1px rgba(0,0,0,.1); wordmark left in system sans 30px/800 #1f2937; four 16px/500 #111827 text links right, 24px apart, hover #ca8a04. Below it on #f9fafb, 64px down, a centered 48px/48px weight-900 #111827 two-line question headline, max-width 896px, then an 18px/28px #374151 subtitle 16px below."
2. "Add a row of three stat cards: grid with 24px gap, max-width 1024px, centered; each card white, 1px solid #e5e7eb border, 8px radius, shadow 0 10px 15px -3px rgba(0,0,0,.1), padding 24px, centered text; heading 24px/32px 700 #1f2937, description 16px/24px #374151 8px below."
3. "Add pill buttons: padding 12px 24px, border-radius 9999px, 18px/28px weight 700 #111827 text; yellow #eab308 (hover #facc15) for ArXiv and Leaderboard, blue #3b82f6 (hover #60a5fa) for Codebase, shadow 0 4px 6px -1px rgba(0,0,0,.1)."

## Similar Pages

- Tailwind-CDN benchmark landing pages that put a leaderboard link in the nav and stat cards under the hero.
- Product-style dataset sites (for example Hugging Face Spaces landing pages) with a static white bar and card rows.

## Quick Start

```css
:root {
  --floor: #f9fafb;
  --surface: #ffffff;
  --ink: #111827;
  --heading: #1f2937;
  --body: #374151;
  --muted: #6b7280;
  --hairline: #e5e7eb;
  --code-bg: #f3f4f6;
  --banner: #facc15;
  --banner-text: #713f12;
  --btn-yellow: #eab308;
  --btn-blue: #3b82f6;
  --font: ui-sans-serif, system-ui, "Segoe UI", Inter, sans-serif;
  --headline: 900 48px/48px var(--font);
  --radius-card: 8px;
  --shadow-card: 0 10px 15px -3px rgba(0,0,0,.1), 0 4px 6px -4px rgba(0,0,0,.1);
  --section-gap: 48px;
}
```

## Provenance

- **URL**: https://mcgill-nlp.github.io/AfroBench/
- **Paper**: AfroBench: How Good are Large Language Models on African Languages? (arXiv 2311.07978), Jessica Ojo et al.
- **Venue**: ACL 2025 Findings.
- **Selection reason**: arXiv 2311.07978 comment states acceptance at ACL 2025 (Findings); project page linked in the abstract. Chosen because it reads like a product site: top bar, bold question headline, stat cards and a framed overview map, then two-column text-plus-scatter sections. The yellow announcement is loud. The selection note called the nav sticky; the render shows a static bar.
- **Template credit**: none; a hand-written page using the Tailwind CSS CDN.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share, the first-viewport screenshot and full-page capture, the page HTML (Tailwind utility classes resolved against the Tailwind v3 default theme). Date 2026-10-28.
