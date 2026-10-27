# Pastel SaaS Launch — Style Reference

> A product launch page for a cognitive-science benchmark, all frosted glass and sherbet gradients.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the nav, hero, buttons, author block, news card, timeline badges, criteria cards, finding cards, table and code block, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the page's two inline `<style>` blocks and Tailwind Play CDN configuration. Tailwind utility classes were resolved to their rendered values. Positions are document coordinates at 1440px wide.

## Overview

CoreCognition looks like a SaaS landing page rather than a paper page. A frosted white nav (85% white, 20px blur) holds a trophy emoji and a gradient wordmark on the left and four text links on the right. The hero is a soft diagonal wash from #fdfcfb to #e2d1c3 with slowly floating radial glows in lavender, pink and sky. On it sit a centered 36px Inter bold title in slate (#1e293b), three justified 20px paragraphs of TL;DR text and a row of five 12px-radius buttons: one white and four with bright left-to-right gradients (yellow→orange, purple→pink, indigo→purple, cyan→blue). The authors follow on white, then a news timeline inside a white rounded card. After that come alternating sections on very pale Tailwind 50-tint gradients, holding white rounded cards with gradient icon tiles, three tinted criteria cards, figures framed in slate-100 panels, and four large finding cards with pastel gradient fills and dark translucent number badges. The type is Inter throughout, and the code block is a dark slate gradient.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): blush beige #ecd4d2 25.3%, near-white #fefefe 13.9%, lavender grey #d2cbd5 13.7%, pale lilac #e0dbe3 13.2%, pale pink #f1e4e5 12.0%, dusty violet #a099ae 9.8% (text and glow), beige #dfd4d4 6.3%, #e9dfdf 5.8%. The hero wash fills y 64–858 (88% of the viewport); the white nav and the top of the white author band take the rest.

Anatomy in DOM order (y = top of element box):

1. **Nav bar** (`nav.nav-glass.fixed`), y 0, height 65px, `rgba(255,255,255,0.85)` with `backdrop-filter: blur(20px) saturate(180%)`. Left at x 80: 🏆 at 24px with 8px gap, then "Core Cognition" in Inter 20px/700 as gradient text (#111827 → #1e3a8a). Right: Code, Paper, Dataset, LeaderBoard in 16px/500 #374151, 32px apart. Gap to title 63px (hero padding 64px).
2. **Title** (`h1.text-3xl.md:text-4xl.font-bold.text-slate-800`), y 128, two centered lines in an 896px box, Inter 36px/700, line-height 40px, #1e293b. Gap 32px.
3. **TL;DR paragraphs** (`div.text-lg.md:text-xl.text-justify`), y 240, three paragraphs of 20px/28px Inter 400, #334155, justified, 16px apart; bold (`strong`) product names. Gap 48px.
4. **Button row** (`div.flex.flex-wrap.justify-center.gap-4`), y 712, five 50px-tall buttons with 16px gaps: Paper (white), Dataset (yellow→orange), Poster (purple→pink), Code (indigo→purple), Website (cyan→blue); 20px stroke icons on the left. Hero ends at y 858.
5. **Author band** starts at y 858 on white; the fold shows only its top edge.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Hero Ivory | #fdfcfb | `.gradient-bg` 0% | Hero wash top-left |
| Hero Sand | #e2d1c3 | `.gradient-bg` 100% | Hero wash bottom-right |
| Glow Lavender | rgba(120,119,198,0.3) | `.gradient-bg::before` | Radial glow at 20% 80% of the hero |
| Glow Pink | rgba(255,119,198,0.15) | `.gradient-bg::before` | Radial glow at 80% 20% of the hero |
| Glow Sky | rgba(120,200,255,0.1) | `.gradient-bg::before` | Radial glow at 40% 40% of the hero |
| Slate 800 | #1e293b | `text-slate-800` | Hero title; code-block gradient start |
| Slate 700 | #334155 | `text-slate-700` | Hero paragraphs, Paper button label |
| Gray 900 | #111827 | `text-gray-900` | Section titles (h2, h3, h4), wordmark gradient start |
| Navy 900 | #1e3a8a | `to-blue-900` | Wordmark gradient end |
| Gray 800 | #1f2937 | `text-gray-800` | Finding-card titles |
| Gray 700 | #374151 | `text-gray-700` | Nav links, author names, card body text, news text |
| Gray 600 | #4b5563 | `text-gray-600` | Section intro paragraphs, affiliations |
| Gray 500 | #6b7280 | `text-gray-500` | Equal-contribution note |
| Blue 600 | #2563eb | `hover:text-blue-600`, `to-blue-600` | Nav link hover; Website button end |
| Yellow 400 | #facc15 | `from-yellow-400` | Dataset button start |
| Orange 500 | #f97316 | `to-orange-500` | Dataset button end, news-header icon tile end |
| Amber 400 | #fbbf24 | `from-amber-400` | News-header icon tile start, newest-dataset timeline dot |
| Purple 500 | #a855f7 | `from-purple-500` | Poster button start |
| Pink 600 | #db2777 | `to-pink-600` | Poster button end |
| Indigo 500 | #6366f1 | `from-indigo-500` | Code button start, timeline dots, Dataset Curation icon tile |
| Purple 600 | #9333ea | `to-purple-600` | Code button end, timeline dots |
| Cyan 500 | #06b6d4 | `from-cyan-500` | Website button start |
| Indigo 700 | #4338ca | `text-indigo-700` | News date badge text |
| Indigo 50 | #eef2ff | `bg-indigo-50` | News date badge fill |
| Indigo 600 | #4f46e5 | `text-indigo-600` | News inline links (bold, underlined) |
| Red 600 | #dc2626 | `text-red-600` | Bold key word inside the first criteria card |
| Slate 50 | #f8fafc | `hover:bg-slate-50`, `from-slate-50` | Paper button hover fill; News section gradient start |
| Card Border | #f3f4f6 | `border-gray-100` | White card 1px border, news header divider |
| Timeline Rule | #e5e7eb | `border-gray-200` | News timeline left rule, table row rules |
| Figure Panel | #f1f5f9 | `.paper-figure-container` | Figure frame fill |
| Figure Border | #e2e8f0 | `.paper-figure-container`, `border-slate-200` | Figure frame border, Paper button border |
| Table Head Rule | #d1d5db | `border-gray-300` | Table header 2px bottom rule |
| Criterion Blue | #eff6ff | `from-blue-50` | First criteria card fill (to #eef2ff), border #dbeafe |
| Criterion Blue Edge | #dbeafe | `border-blue-100` | First criteria card border |
| Criterion Mint | #ecfdf5 | `from-emerald-50` | Second criteria card fill (to #f0fdfa) |
| Criterion Mint Edge | #d1fae5 | `border-emerald-100` | Second criteria card border |
| Finding Periwinkle | #a5b4ff | inline gradient | Finding card 1 start (to #c084fc) |
| Finding Orchid | #c084fc | inline gradient | Finding card 1 end |
| Finding Coral | #ff9a9e | inline gradient | Finding card 2 start (to #fecfef) |
| Finding Blush | #fecfef | inline gradient | Finding card 2 end |
| Finding Aqua | #a8edea | inline gradient | Finding card 3 start (to #fed6e3) |
| Finding Rose | #fed6e3 | inline gradient | Finding card 3 end |
| Finding Peach | #ffecd2 | inline gradient | Finding card 4 start (to #fcb69f) |
| Finding Apricot | #fcb69f | inline gradient | Finding card 4 end |
| Code Night | #0f172a | `pre[class*="language-"]` | Code block gradient end (from #1e293b) |
| Code Text | #cccccc | Prism Tomorrow | BibTeX text |
| Page Grey | #f9fafb | `body.bg-gray-50` | Body background behind sections |
| White | #ffffff | `bg-white` | Author band, white sections, cards, Paper button |

## Tokens — Typography

- **Text and headings**: Tailwind config sets `sans: ['Inter', 'system-ui', 'sans-serif']`. Rendered: Inter 400, 500, 600 and 700 (`fonts_loaded`). Substitute: Geist (same neutral grotesque proportions).
- **Mono**: `mono: ['JetBrains Mono', 'Monaco', 'monospace']`, JetBrains Mono 400 loaded; the Prism block itself declares `Consolas, Monaco, "Andale Mono"`.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Wordmark | `nav a.group span` | 20px / 28px | 700 | gradient #111827 → #1e3a8a |
| Nav link | `nav a.text-gray-700` | 16px / 24px | 500 | #374151 |
| Hero title | `h1.text-3xl.md:text-4xl` | 36px / 40px | 700 | #1e293b |
| Hero paragraph | `.text-lg.md:text-xl` | 20px / 28px | 400 | #334155, justified |
| Button label | hero `a.inline-flex` | 16px / 24px | 600 | white, Paper #334155 |
| Author name | author `a` | 18px / 28px | 400 | #374151 |
| Affiliation line | `.text-gray-600 .font-bold` | 18px / 28px | 700 | #4b5563 |
| Section title | `h2.text-3xl.md:text-4xl` | 36px / 40px | 700 | #111827 |
| News title | `h2.text-2xl.md:text-3xl.tracking-tight` | 30px / 36px, -0.75px | 700 | #111827 |
| Section intro | `p.text-xl.text-gray-600` | 20px / 28px | 400 | #4b5563 |
| Card title | `h3.text-2xl` | 24px / 32px | 700 | #111827 (#1f2937 on finding cards) |
| Criterion title | `h4.text-lg` | 18px / 28px | 700 | #111827 |
| Card body | `p.text-base`, `p.text-lg` | 16px / 26px, 18px / 29px | 400 | #374151 |
| Date badge | `time` | 14px / 20px | 600 | #4338ca on #eef2ff |
| Table header | `th` | 18px / 28px | 600 | #111827 |
| Code | `pre.language-latex` | 16px / 24px | 400 | #cccccc |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Hero button | 12px (`rounded-xl`) | Paper only: 1px #e2e8f0 | `shadow-lg` (0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1)); hover `shadow-xl` and scale 1.05 |
| White content card | 16px (`rounded-2xl`) | 1px #f3f4f6 | `shadow-xl` (0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1)); hover `shadow-2xl`, translateY(-4px) |
| Icon tile | 12px (`rounded-xl`), small tiles 8px | none | `shadow-lg` |
| Criteria card | 12px | 1px tint-100 (#dbeafe, #d1fae5) | none; hover `shadow-lg`, translateY(-4px) |
| Figure frame | 16px | 1px #e2e8f0 | `0 4px 6px -1px rgba(0,0,0,0.1)`; inner image 8px radius, white, 16px padding, `0 2px 4px rgba(0,0,0,0.1)` |
| Finding card | 16px | none | `shadow-lg`; hover `shadow-xl`, translateY(-8px), scale 1.05 |
| Date badge | 6px | none | none |
| Timeline dot | 9999px, 24px | 4px white ring | none |
| Code block | 16px | 1px rgba(148,163,184,0.1) | `0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04)` |

## Layout Metrics

- **Container**: Tailwind `max-w-7xl mx-auto` (1280px), x 80–1360 at 1440px. The `container-spacing` and `section-spacing` helpers use `@apply` inside a plain `<style>`, which the Play CDN does not process, so they add no padding; sections that use `px-4 sm:px-6 lg:px-8` directly get 32px at ≥1024px (content 1216px).
- **Hero**: `py-16` (64px top and bottom) under the 65px fixed nav; title and paragraphs capped at `max-w-4xl` (896px); 48px between paragraphs and buttons.
- **Sections**: `py-16` (64px) for content sections, `py-12` (48px) for the author band. Section headers centered with 48px bottom margin (`mb-12`).
- **News**: `max-w-5xl` (1024px) wrapper with 32px padding, so the card is 960px; card padding 32px; timeline indent 12px plus 24px per item, 32px between items.
- **Cards**: white cards span the full 1216px with 32px padding; criteria in a 3-column grid with 24px gaps (367px each); findings in a 2-column grid with 32px gaps; finding cards 32px padding.
- **Figures**: framed in `max-w-3xl` (768px) or `max-w-5xl` (1024px) slate panels with 32px padding.
- **Table**: `max-w-2xl` (672px) centered, cells padding 16px 24px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1280px | centered 1280px container | 16px | 36px | 3-column criteria, 2-column findings |
| 1024–1279px | 32px (`lg:px-8`) | 16px | 36px | same grids |
| 768–1023px | 24px (`sm:px-6`) | 16px | 36px | same grids; nav links visible |
| 640–767px | 24px | 16px | 30px (`text-3xl`) | nav links hidden behind a hamburger (`md:hidden` button); hero text 18px; grids collapse to one column; news card padding 24px |
| <640px | 16px (`px-4`) | 16px | 30px | single column; buttons wrap centered |

## Components

- **Glass nav**: fixed, full width, height 65px, `rgba(255,255,255,0.85)`, `backdrop-filter: blur(20px) saturate(180%)`, 1px rgba(255,255,255,0.2) bottom border; gains `shadow-lg` after 100px of scroll. Links 16px/500 #374151, hover #2563eb with scale 1.05. Mobile: a 24px hamburger opens a white/95 blurred panel with 12px-by-8px padded links and blue-50 hover.
- **Gradient CTA button**: `inline-flex items-center px-6 py-3 rounded-xl font-semibold text-white shadow-lg`, 50px tall, `bg-gradient-to-r` with a two-stop Tailwind ramp (#facc15→#f97316, #a855f7→#db2777, #6366f1→#9333ea, #06b6d4→#2563eb), 20px outline icon left with 8px gap; hover darkens both stops one step, scale 1.05, `shadow-xl`. The neutral variant is white with 1px #e2e8f0 border and #334155 text, hover #f8fafc.
- **News timeline card**: white, 16px radius, 1px #f3f4f6 border, `shadow-xl`, padding 32px. Header: a 12px-radius gradient icon tile (#fbbf24→#f97316, 28px bell icon) beside a 30px/700 "News" title, then a 1px #f3f4f6 divider and 32px space. Items hang off a 1px #e5e7eb left rule: a 24px round gradient dot with a 4px white ring, a date badge (14px/600 #4338ca on #eef2ff, 6px radius, padding 2px 10px), and 16px #374151 text with bold underlined #4f46e5 links.
- **Feature card with icon tile**: white, 16px radius, padding 32px, `shadow-xl`; header row of a 64px gradient icon tile (padding 16px, 12px radius, white 32px stroke icon) and a 24px/700 #111827 title.
- **Criteria card**: `bg-gradient-to-br from-{c}-50 to-{c2}-50`, 1px `{c}-100` border, 12px radius, padding 24px; 36px solid icon tile (`bg-{c}-500`, 8px radius) beside an 18px/700 title; 14px justified body with a colored bold key word (#dc2626 for "discriminative").
- **Finding card**: 135deg pastel gradient fill (#a5b4ff→#c084fc and three others), 16px radius, padding 32px, `shadow-lg`; a rgba(0,0,0,0.2) 12px-radius badge with a white 30px/700 numeral, then a 24px/700 #1f2937 title and 16px/26px #374151 justified text; hover lifts 8px and scales 1.05.
- **Figure frame**: #f1f5f9 panel, 1px #e2e8f0 border, 16px radius, padding 32px, the image inside on white with 16px padding, 8px radius and a 2px shadow; hover lifts 4px.
- **Code block**: Prism Tomorrow on `linear-gradient(135deg, #1e293b, #0f172a)`, 16px radius, padding 16px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky navigation | yes | frosted white bar with gradient wordmark |
| Title and TL;DR | yes | centered title, three justified paragraphs on the warm wash |
| Link buttons | yes | five 12px-radius buttons, four with color gradients |
| Authors and affiliations | yes | separate white band, bold grey affiliation lines |
| Venue line | absent from the source | ICML 2025 is not stated in the hero |
| News | yes | timeline card with gradient dots and date badges |
| Benchmark overview | yes | framed illustration plus white feature cards |
| Dataset criteria | yes | three tinted icon cards |
| Concept glossary | yes | twelve small cards for the core concepts |
| Key findings | yes | four pastel gradient cards with number badges |
| Results figures | yes | slate-framed figures |
| Results table | yes | small 672px table with ✓ marks, 2px #d1d5db header rule |
| Usage / deployment tabs | yes | selectable cards that switch code tabs |
| BibTeX | yes | dark slate gradient Prism block |
| Footer | absent from the source | the page ends after the citation |

## Adapting to Other Content

- **Venue badge**: add a pill above the title (14px/600 #4338ca on #eef2ff, 6px radius, padding 2px 10px), reusing the news date-badge recipe.
- **More authors**: the author band already wraps flex rows with 24px column gaps; keep 18px #374151 names and bold #4b5563 affiliation rows.
- **A large results table**: put it in a white feature card (16px radius, `shadow-xl`), 16px Inter cells with padding 16px 24px, a 2px #d1d5db header rule and 1px #e5e7eb row rules, best numbers in 600 weight; no zebra fills.
- **Long publication or related-work lists**: reuse the timeline pattern without dates, or a 3-column grid of criteria cards using one neutral tint.
- **Fewer links**: keep the white neutral button first and give each remaining link its own two-stop gradient; do not reuse a gradient on two buttons.
- **Video teasers**: frame them like figures in the #f1f5f9 panel with 32px padding.

## Do's and Don'ts

- Do keep the hero wash warm (#fdfcfb → #e2d1c3) and let the colored glows stay faint.
- Do pair every card header with a gradient icon tile and a 24px bold title.
- Do use Tailwind 50 tints for section backgrounds and 100 tints for card borders.
- Do give each CTA its own two-stop gradient and a white outline icon.
- Don't use `@apply` in plain `<style>` blocks with the Play CDN; those rules do nothing here.
- Don't put dark backgrounds anywhere except the code block.
- Don't center long body text; only the hero paragraphs are justified in a centered 896px block.

## Surfaces

Four layers. A #f9fafb page under alternating white and pastel-gradient sections (slate-50→blue-50, purple-50→red-50, red-50→pink-50, pink-50→orange-50). On top, white rounded cards with large soft shadows. Inside them sit tinted criteria cards, slate-100 figure frames and gradient icon tiles. A frosted nav floats above everything.

## Imagery

Paper figures (a radial chart of the twelve concepts, stage diagrams, scatter plots and heatmaps) placed on white inside slate panels, plus small stroke icons (Heroicons-style SVG) in white on gradient tiles. Emoji appear in the wordmark (🏆) and the news items.

## Layout

A 1280px Tailwind container with centered section headers and full-width cards, grids of three and two columns, and a narrower 896px hero text block. Rendered height about 15,000px at 1440px.

## Agent Prompt Guide

Quick colors: hero #fdfcfb → #e2d1c3, title #1e293b, hero text #334155, headings #111827, body #374151, intro #4b5563, CTA gradients #facc15→#f97316, #a855f7→#db2777, #6366f1→#9333ea, #06b6d4→#2563eb, neutral button white with #e2e8f0 border, badge #4338ca on #eef2ff, figure panel #f1f5f9.

1. "Build a hero: section with `background: linear-gradient(135deg, #fdfcfb 0%, #e2d1c3 100%)` and a `::before` overlay of radial gradients (rgba(120,119,198,0.3) at 20% 80%, rgba(255,119,198,0.15) at 80% 20%, rgba(120,200,255,0.1) at 40% 40%), padding 64px 0. Centered Inter 36px/700 #1e293b title max 896px, then justified 20px/28px #334155 paragraphs 16px apart, then a centered row of 12px-radius buttons with 16px gaps."
2. "Create gradient CTA buttons: inline-flex, padding 12px 24px, 12px radius, Inter 16px/600 white, 20px outline icon left, `linear-gradient(to right, #6366f1, #9333ea)` (and #facc15→#f97316, #a855f7→#db2777, #06b6d4→#2563eb for siblings), `shadow-lg`; hover scale 1.05 and `shadow-xl`. First button white with 1px #e2e8f0 border and #334155 text."
3. "Make a news timeline card: white, 16px radius, 1px #f3f4f6 border, padding 32px, `0 20px 25px -5px rgba(0,0,0,0.1)`. Header with a 12px-radius #fbbf24→#f97316 icon tile and 30px/700 #111827 'News'. List with a 1px #e5e7eb left rule; each item a 24px round #6366f1→#9333ea dot with a 4px white ring, a date badge 14px/600 #4338ca on #eef2ff (6px radius), and 16px #374151 text."

## Similar Pages

- Tailwind Play CDN research landing pages built to look like product sites (glass nav, gradient CTAs, feature cards).
- Benchmark pages with a separate leaderboard route linked from the nav.

## Quick Start

```css
:root {
  --hero-from: #fdfcfb;
  --hero-to: #e2d1c3;
  --title: #1e293b;
  --hero-text: #334155;
  --heading: #111827;
  --body: #374151;
  --muted: #4b5563;
  --nav-bg: rgba(255, 255, 255, 0.85);
  --nav-hover: #2563eb;
  --cta-1: linear-gradient(to right, #facc15, #f97316);
  --cta-2: linear-gradient(to right, #a855f7, #db2777);
  --cta-3: linear-gradient(to right, #6366f1, #9333ea);
  --cta-4: linear-gradient(to right, #06b6d4, #2563eb);
  --neutral-border: #e2e8f0;
  --card-border: #f3f4f6;
  --rule: #e5e7eb;
  --badge-text: #4338ca;
  --badge-bg: #eef2ff;
  --figure-panel: #f1f5f9;
  --page: #f9fafb;
  --code-from: #1e293b;
  --code-to: #0f172a;
  --font: 'Inter', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', Monaco, monospace;
  --radius-button: 12px;
  --radius-card: 16px;
  --container: 1280px;
}
```

## Provenance

- **URL**: https://grow-ai-like-a-child.github.io/core-knowledge/
- **Paper**: Core Knowledge Deficits in Multi-Modal Language Models (arXiv 2410.10855), Yijiang Li, Qingying Gao, Tianwei Zhao et al. (UC San Diego, Johns Hopkins, Emory and others).
- **Venue**: ICML 2025.
- **Selection reason**: the arXiv 2410.10855 comment states acceptance at ICML 2025 and links the page. Chosen for the product-site look: sticky nav, pastel gradient hero, gradient link buttons, news timeline card and icon-headed criteria cards.
- **Template credit**: none stated; built directly on the Tailwind Play CDN with custom inline CSS.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share, targeted computed-style probes of the author band, news card, badges, criteria and finding cards, figure frames and table, the first-viewport screenshot and scaled full-page capture, the inline `<style>` blocks, Tailwind config and the HTML. Date 2026-10-28.
