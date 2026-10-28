# Waabi Research Editorial — Style Reference

> A lab's annual report after dark: a giant soft-serif headline on charcoal, a floating white pill for navigation, figures in rounded frames, and a hot-pink sign-off.

**Theme:** dark

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, loaded fonts, color share), DOM probes of the promo bar, header pill, title block, rail buttons, figure and video frames, dividers and footer, and the 1440×900 and full-page screenshots. The page is a Next.js build with Tailwind classes and an inline stylesheet that defines tokens such as `--color-dark: #191818` and `--color-pink: #ff2c6b`; the root font size is 10px, so `1.5rem` is 15px. A cookie-consent card (bottom left) and a white promo bar (top) were captured in the screenshot; both are site chrome, described separately from the publication layout.

## Overview

A long corporate research article (about 13,500px tall) from the self-driving company Waabi. The page is charcoal (#191818) with white type. A fixed white promo strip ("Let's talk autonomous trucking · Get in touch ↗") runs across the top, and a fixed white header pill with the "waabi" wordmark, "Research" and a hamburger floats centred below it. The publication opens with a small "View All Publications" back link, a share button on the right, and a four-line title in the brand display face Zagma at 80px with tight −3.2px tracking. Venue (at 60% opacity) and authors follow in 16px, then a faint full-width hairline. Below, a narrow left rail (Waabi logo tile, "by Waabi", and outlined Video, Paper and Poster pills) sits beside an 810px reading column: the abstract set large in Neue Haas at 24px, then sections (Video, Motivation, Method…) with small 18px headings over 15% white rules, 20px body text at 80% white, and figures widened to 890px inside 12px-rounded frames. The page ends with a 600px hot-pink (#ff2c6b) company footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): charcoal family #191818 / #141212 / #191819 / #191817 / #1c1816 together 80.3%; off-white #fbfbfb 13.8% (promo bar, header pill, the title's letterforms, cookie card); mid-grey #706f6f 5.7% (anti-aliased type and the 60%-opacity venue line). Pink appears only as the cookie card's "Customize" outline and does not form a cluster.

Anatomy in DOM order (desktop 1440px):

1. **Promo bar** (fixed, 0–43px, full width): #ffffff with a 1px rgba(0,0,0,0.15) bottom border; centred "Let's talk autonomous trucking" in Neue Haas 12px/500 #191818, letter-spacing 0.24px, then an underlined "Get in touch" link with a ↗ arrow; a close × at x=1400.
2. **Header pill** (fixed `header.css-header`, y=76, 338×55 at x=551): outer layer rgba(0,0,0,0.15), 1px padding, radius 12px; inner #ffffff, radius 11px, padding 0 13px 0 28px. Contents: "waabi" wordmark SVG (75×23) at x=580, "Research" Neue Haas 15px/400 #191818 (line-height 24px), and a 36px round hamburger button at x=839.
3. **Article top** (dark container `pt-[12.2rem]`, padding-top 120px): "View All Publications" at y=120, x=103: a 24px circle with a 1px rgba(255,255,255,0.25) border holding a ← arrow (fills #ff2c6b on hover), 16px gap, label Neue Haas 12px/500 #ffffff.
4. **Share button** (y=232, x=1262): 24px circular icon plus "Share" label in white; it opens a white menu (Copy link, on X, on Linkedin).
5. **Title** (`h1.type-z-80`, y=256, 919px max width, 288px tall): Zagma 80px/400, line-height 72px, letter-spacing −3.2px, #ffffff, four lines, left-aligned at x=103.
6. **Venue** (`p.type-z-15.opacity-60`, y=568): "CoRL 2025", Zagma 16px/400, line-height 22.4px, letter-spacing −0.32px, #ffffff at opacity 0.6.
7. **Authors** (y=590): same 16px style at full opacity, names with asterisks for equal contribution.
8. **Hairline** (`hr`, y=693): 1px rgba(255,255,255,0.1), 1234px wide (x=103–1337). Gap 80px.
9. **Rail and abstract** (from y=774): Waabi logo tile (50×50, radius 10px) at x=103 and the abstract at x=315 (810px column), which the fold and the cookie card cut.

Arithmetic check: 120 + 24 (back link) + 88 = 232 (share row, 24px tall); 232 + 24 = 256 (title); 256 + 288 + 24 = 568; 568 + 22 = 590; 590 + 22 = 612; 612 + 80 + 1 = 693; 694 + 80 = 774.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Charcoal | #191818 | --color-dark | article background; promo text; header pill text |
| White | #ffffff | --color-white | title, authors, abstract, headings; promo bar and header pill fill; share menu |
| Body White | rgba(255,255,255,0.8) | (`text-white/80`) | section body paragraphs |
| Venue White | rgba(255,255,255,0.6) | (opacity-60) | venue line; footer email links |
| Rule White | rgba(255,255,255,0.15) | (`border-white/15`) | section-heading underlines, rail pill borders |
| Hairline | rgba(255,255,255,0.1) | (`bg-current/10`) | full-width divider under the title block |
| Frame Border | rgba(255,255,255,0.2) | (`border-foreground/20`) | video frame border |
| Frame Fill | rgba(0,0,0,0.2) | (`bg-black/20`) | figure and video frames behind media |
| Pill Shade | rgba(0,0,0,0.15) | (`bg-black/15`) | outer ring of the header pill; promo bar border |
| Waabi Pink | #ff2c6b | --color-pink | footer band, hover fills on rail pills and the back-arrow circle, inline links in the abstract, cookie "Customize" outline |

Declared but not visible on this page: `--color-dark-light`, `--color-light-pink`, `--color-cream` and Tailwind palette defaults are defined in the inline stylesheet but no probed element of the article uses them.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display / body | Zagma, "Zagma Fallback", sans-serif (self-hosted brand face) | Zagma 400 | Newsreader |
| UI / abstract | NeueHaas, "NeueHaas Fallback" (self-hosted Neue Haas Grotesk) | NeueHaas 400; 500 synthesized | Inter |
| Code | ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas… | Consolas on Windows | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.type-z-34.md:type-z-80` | 80px / 400 / 72px, letter-spacing −3.2px | #ffffff |
| Venue / authors | `p.type-z-15` | 16px / 400 / 22.4px, letter-spacing −0.32px | #ffffff (venue at 0.6) |
| Abstract | `h2.font-neue.md:text-[2.4rem]` | Neue Haas 24px / 400 / 28.8px | #ffffff; links #ff2c6b |
| Section heading | content `h2`, `h3` | Neue Haas 18px / 400 / 22.5px, letter-spacing −0.72px, padding-bottom 10px | #ffffff |
| Body | content `p` | Zagma 20px / 400 / 27px, letter-spacing −0.6px | rgba(255,255,255,0.8) |
| Small UI | `.type-s-12` | Neue Haas 12px / 500 / 16.8px, letter-spacing 0.24px | #ffffff on dark, #191818 on white |
| Header label | header `span.font-neue` | Neue Haas 15px / 400 / 24px, letter-spacing 0.15px | #191818 |
| Footer headline | footer `h2` | Zagma 40px / 400 / 44px, letter-spacing −1.2px | #ffffff |
| Footer links | `.type-z-20` | Zagma 20px / 400 / 24px | #ffffff |
| BibTeX | `pre` | monospace 10px base | #ffffff |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Header pill | 12px outer, 11px inner | 1px padding ring of rgba(0,0,0,0.15) | none |
| Rail pills (Video, Paper, Poster) | 50px | 1px rgba(255,255,255,0.15) | none; hover fill #ff2c6b |
| Back-arrow circle | full circle (24px) | 1px rgba(255,255,255,0.25) | none; hover fill #ff2c6b |
| Logo tile | 10px (50×50) | none | none |
| Figure frame | 12px | none | none; fill rgba(0,0,0,0.2) |
| Video frame | 12px | 1px rgba(255,255,255,0.2) | none |
| Section heading | 0 | 1px rgba(255,255,255,0.15) bottom | none |
| Footer social buttons | full circle (50px) | none | none |
| Cookie card (chrome) | 11px | 1px #ebebeb | `0 16px 32px -12px rgba(14, 18, 27, 0.1)` |

## Layout Metrics

- **Page frame**: content starts at x=103 and the divider spans 1234px (x=103–1337), so side margins are about 103px at 1440.
- **Title block**: max-width 919px, left-aligned; padding-top 120px under the fixed chrome; flex column with `gap-60 md:gap-80` (80px at 1440) between title block, divider and article.
- **Reading column**: `lg:w-810`, centred (x=315–1125). `md:w-600` from 768px; below that `w-[calc(100%-8rem)]` (80px total margin).
- **Figures**: `md:-ml-40 md:w-[calc(100%+8rem)]`, so media are 890px wide at x=275, 40px wider than the text on each side. Vertical gap between blocks `md:gap-60` (60px).
- **Rail**: `lg:absolute` at the top of the article, padding-left 103px; contents 89px wide (logo tile, "by Waabi", three 48px-tall pills 14px apart). It scrolls with the page.
- **Footer**: full-width #ff2c6b band, `lg:h-[60rem]` = 600px, headline and contact at x=103, site links column at x=813, three 50px white circle social buttons at the right.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px (lg, 1440 render) | 103px | 20px | 80px | 810px column; rail absolute at left; figures 890px |
| 768–1023px (md) | same frame | 20px | 80px | 600px column; rail moves into the flow above the article (`max-lg:px-0`); figures still extend 40px each side |
| <768px | 40px each side (`calc(100% - 8rem)`) | 18px abstract (1.8rem) | 34px (`type-z-34`) | single column, figures at text width; rail pills 36px tall |

## Components

- **Floating header pill**: fixed, centred, 338×55; a 1px rgba(0,0,0,0.15) ring around a #ffffff body with 11px radius; brand wordmark left, section label "Research" in Neue Haas 15px, round 36px hamburger right.
- **Promo strip**: fixed full-width white bar 43px tall, centred Neue Haas 12px/500 #191818 message with an underlined link and ↗; close × at the far right.
- **Back link**: 24px circle with a 1px rgba(255,255,255,0.25) border and a ← icon, 16px gap, 12px/500 white label; the circle fills #ff2c6b on hover.
- **Rail pill** (`a.hover:bg-pink`): 48px tall (36px below md), padding 0 24px, radius 50px, 1px rgba(255,255,255,0.15) border, white label; hover fill #ff2c6b.
- **Section heading**: Neue Haas 18px/400, letter-spacing −0.72px, padding-bottom 10px, 1px rgba(255,255,255,0.15) bottom border across the 810px column.
- **Media frame**: 890px wide, radius 12px, `overflow: hidden`, fill rgba(0,0,0,0.2); videos add a 1px rgba(255,255,255,0.2) border. Figures with white backgrounds read as white cards on charcoal.
- **Pink footer**: 600px #ff2c6b band; Zagma 40px/400 white headline "We're just getting started", Neue Haas 15px contact line with 60%-white underlined emails, Zagma 20px nav links, white 50px circular social buttons with black icons.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Site chrome (promo bar, header pill) | yes | fixed white bar and floating white pill over the dark page |
| Back link / share | yes | small white UI at the corners of the title block |
| Title / venue / authors | yes | 80px Zagma title, 16px meta lines, no affiliations |
| Link buttons | yes | outlined pills in the left rail |
| Abstract | yes | large 24px Neue Haas paragraph, no heading |
| Teaser figure | yes | wide framed image under the abstract |
| Video | yes | framed video with a thin white border |
| Method / results figures | yes | framed 890px images under 18px ruled headings |
| BibTeX | yes | plain monospace `pre` with no panel |
| Footer | yes | 600px hot-pink company footer |
| Cookie banner | present but non-standard | site consent card captured in the screenshot; not part of the article |
| Results table | absent from the source | results appear as figure images |

## Adapting to Other Content

- **More authors**: keep them in the 16px Zagma line under the title, comma-separated; at 919px the line holds about ten names before wrapping. Affiliations, if needed, go on the 60%-opacity line with the venue.
- **A results table**: put it in a 12px-radius frame at 890px with rgba(0,0,0,0.2) fill; Neue Haas 15px white cells, header row at 60% white, 1px rgba(255,255,255,0.15) rules, best values in #ff2c6b.
- **Long publication lists**: a list of rows in the 810px column, each a Zagma 20px title over a 12px/500 Neue Haas meta line, separated by 1px rgba(255,255,255,0.15) rules, with a pink hover.
- **News**: reuse the 18px ruled section heading and 20px body; dates in Neue Haas 12px/500 at 60% white.
- **More links**: add pills to the rail (48px tall, 14px apart); keep them outlined, with pink only on hover.

## Do's and Don'ts

- Do set the title huge and tight (80px, line-height 72px, −3.2px tracking) and left-aligned.
- Do keep reading text at 80% white on #191818 and headings small (18px) with hairline rules.
- Do let figures break out 40px beyond the text column inside 12px-rounded frames.
- Do reserve #ff2c6b for hovers, links and the footer band.
- Don't centre the hero; everything aligns to the x=103 frame or the 810px column.
- Don't use bold weights; hierarchy comes from size and opacity at weight 400.
- Don't let site chrome (promo bar, cookie card) define the article style; they are overlays.

## Surfaces

Charcoal #191818 for the whole article; white for chrome only (promo bar, header pill, share menu); translucent dark frames (rgba(0,0,0,0.2)) behind media; a full-bleed #ff2c6b footer.

## Imagery

Autonomous-driving visuals: camera frames with coloured 3D boxes, depth maps in blue and orange, LiDAR renderings in white with green boxes, flat icon rows (car, truck, cone, excavator, pedestrian with stroller, ambulance) on a common-to-rare arrow, method diagrams. Most figures have white backgrounds and so appear as white cards on the dark page. The video poster is a white title slide.

## Layout

An editorial article: a left-aligned title block across the full frame, a hairline, then a centred 810px reading column with a narrow absolute rail at the far left, and media that break slightly wider than the text. Sections stack with 60px gaps.

## Agent Prompt Guide

Quick colors: page #191818, text #ffffff, body rgba(255,255,255,0.8), meta rgba(255,255,255,0.6), rules rgba(255,255,255,0.15), divider rgba(255,255,255,0.1), accent #ff2c6b, frames rgba(0,0,0,0.2).

1. "Build a dark article header on #191818: padding-top 120px, content left-aligned at 103px. A 'View All Publications' link: 24px circle with 1px rgba(255,255,255,0.25) border and an arrow, 16px gap, 12px/500 Neue Haas white label. Title in a soft serif display face at 80px/400, line-height 72px, letter-spacing -3.2px, #ffffff, max-width 919px. Then 16px/22.4px meta lines (venue at opacity 0.6, authors at full white), an 80px gap and a 1px rgba(255,255,255,0.1) full-width rule."
2. "Create the reading column: 810px centred; the abstract in a grotesk at 24px/28.8px #ffffff; section headings 18px/400, letter-spacing -0.72px, padding-bottom 10px, 1px rgba(255,255,255,0.15) bottom border; body 20px/27px at rgba(255,255,255,0.8); figures 890px wide (40px beyond the column each side) in frames with radius 12px and background rgba(0,0,0,0.2)."
3. "Add a left rail and footer: outlined pills 48px tall, padding 0 24px, radius 50px, 1px rgba(255,255,255,0.15) border, white label, hover background #ff2c6b; finish with a 600px #ff2c6b footer band with a 40px white headline and white 50px circular social buttons."

## Similar Pages

- Corporate AI-lab research pages (Next.js and Tailwind) that render each publication as a dark editorial article with brand fonts and a coloured company footer.
- Self-driving company publication pages with a floating header pill and a fixed promo strip.

## Quick Start

```css
:root {
  --color-dark: #191818;
  --color-white: #ffffff;
  --color-pink: #ff2c6b;
  --text-body: rgba(255, 255, 255, 0.8);
  --text-meta: rgba(255, 255, 255, 0.6);
  --rule: rgba(255, 255, 255, 0.15);
  --divider: rgba(255, 255, 255, 0.1);
  --frame: rgba(0, 0, 0, 0.2);
  --font-display: "Zagma", "Newsreader", serif;
  --font-ui: "NeueHaas", "Inter", sans-serif;
  --column: 810px;
  --media: 890px;
  --frame-radius: 12px;
}
html { font-size: 10px; }
body { background: var(--color-dark); color: var(--color-white); }
h1 { font: 400 80px/72px var(--font-display); letter-spacing: -3.2px; max-width: 919px; }
```

## Provenance

- **URL**: https://waabi.ai/research/fomo3d
- **Paper**: FOMO-3D: Using Vision Foundation Models for Long-Tailed 3D Object Detection (arXiv 2603.08611), Anqi Joyce Yang, James Tu, Nikita Dvornik, Enxu Li, Raquel Urtasun (Waabi, University of Toronto).
- **Venue**: CoRL 2025.
- **Selection reason**: the arXiv comment states acceptance at CoRL 2025 (published) and the abstract links this project page.
- **Template credit**: Waabi's own research site (Next.js, Tailwind CSS, self-hosted Zagma and Neue Haas fonts, c15t consent manager); no template credit.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), DOM probes of chrome, title block, rail, frames, rules and footer at 1440, the 1440×900 and full-page screenshots, and the inline colour tokens in the served HTML, on 2026-10-28.
