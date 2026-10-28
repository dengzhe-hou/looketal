# MotionBricks — Style Reference

> A game-engine trailer that fades into a lab report: a full-screen gameplay clip, a lime-gradient wordmark at the bottom edge, then calm warm paper.

**Theme:** both

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), a second probe of below-the-fold elements (author block, pill tabs, content text, toggle), the 1440×900 and tall screenshots, and the page's `static/css/index.css` on top of Bulma. The stylesheet contains two competing hero rule sets; where both apply, the later one wins at render time: `.publication-title` overrides the giant `.cinema-title` size (46.4px renders, not clamp(6rem, 22vw, 22rem)), and `.publication-links .button` overrides the glass `.cinema-links .button`. Theme is "both" because the first viewport is a dark video hero while every section below is light.

## Overview

The first screen is a cinematic, full-bleed autoplay video (Unreal Engine gameplay of an animated character in a courtyard) under a darkening gradient, with a translucent dark navigation bar on top. All hero text is centred and anchored to the bottom of the viewport: a lime-to-green gradient "MotionBricks" wordmark, a white subtitle, an uppercase venue line, four black pill buttons, and a glass "Switch teaser: Animation / Robotics" toggle with a lime active pill, plus a bouncing chevron. Below the fold the page switches to warm paper #fafaf7 with near-black ink #111418 in NVIDIA Sans: an author block, then Bulma sections alternating #fafaf7 and #f2f2ec, each with a centred 30.4px heading underlined by a 44×3px NVIDIA-green bar, 960px videos in 14px-radius frames with soft shadows, pill tabs for switching clips, and a dark BibTeX block and footer. NVIDIA green #76b900 is the single accent.

## First Viewport

Color share (8-color quantization of the 1440×900 shot, which is a video frame): dark olive-black family #0d0f0a / #12150d / #1e1d17 / #090b06 / #2c2b23 together 63.1%; mid olive-gray #433f32 11.7% and #716c5a 11.6% (stone courtyard in shade); light stone #9f9987 12.5% (sunlit walls). The lime wordmark and active toggle are too small to form clusters. The colours are the video's, not the page's.

Anatomy in DOM order (desktop 1440px):

1. **Fixed nav** (`nav.site-nav`, 0–64px): rgba(14,16,20,0.55) with `backdrop-filter: saturate(140%) blur(14px)`, 1px rgba(255,255,255,0.08) bottom border. Inner max 1200px, padding 0 1.5rem (brand at x=144). Brand: a 30×30 "MB" tile with `background: linear-gradient(120deg, #76b900 0%, #2b9348 100%)`, 7px radius, 12.8px/700 white, shadow `0 2px 8px rgba(118, 185, 0, 0.35)`, then "MotionBricks" 15.68px/600 white, letter-spacing -0.01em. Links (Overview … BibTeX) 14.08px/500 rgba(255,255,255,0.82), padding 6.4px 12px, radius 7px, gap 0.25rem; hover white on rgba(255,255,255,0.1). After scrolling (`.is-scrolled`) the bar becomes rgba(255,255,255,0.82) with a #e4e6eb border, `box-shadow: 0 2px 14px rgba(17, 20, 24, 0.06)`, and #2b2f36 links.
2. **Hero** (`section.hero-cinema`, 0–900px): min-height 100vh, #050608, flex column aligned to the bottom, padding 96px 24px 72px. Video `object-fit: cover` fills it; overlay `background: linear-gradient(180deg, rgba(4, 6, 8, 0.3) 0%, rgba(4, 6, 8, 0.15) 38%, rgba(4, 6, 8, 0.85) 100%), radial-gradient(1400px 700px at 50% 85%, rgba(118, 185, 0, 0.2), transparent 70%)`. Content column max 1100px.
3. **Wordmark** (`h1.publication-title.cinema-title`, y=532, 41px box): NVIDIA 46.4px (clamp(1.8rem, 3.4vw, 2.9rem)), line-height 0.88; inner `span.motionbricks-logo` 700, letter-spacing -0.03em, filled with `linear-gradient(100deg, #aef250 0%, #76b900 45%, #2b9348 100%)` clipped to text, `text-shadow: 0 2px 22px rgba(118, 185, 0, 0.25)`. Gap 12px.
4. **Subtitle** (`h2.cinema-subtitle`, y=585, two lines, max 880px): 22.4px/400, line-height 1.35, letter-spacing -0.005em, rgba(255,255,255,0.92), `text-shadow: 0 1px 12px rgba(0, 0, 0, 0.45)`. Gap 20px.
5. **Venue** (`h3.cinema-venue`, y=665): "ACM Transactions on Graphics · SIGGRAPH 2026", 15.2px/500 uppercase, letter-spacing 0.04em, rgba(255,255,255,0.78). Gap 28px.
6. **Buttons** (`.publication-links`, y=716, 44px tall, gap 0.6rem): Paper, arXiv, Code, BibTeX; #111418 fill and border, white 15.2px/500, radius 999px, padding 9.6px 18.4px, shadow `0 1px 2px rgba(17, 20, 24, 0.08)`, icon left. Gap 22.4px.
7. **Teaser toggle** (`.hero-bg-toggle`, y=782, 350×46): rgba(10,12,16,0.55) glass capsule, `backdrop-filter: saturate(140%) blur(12px)`, 1px rgba(255,255,255,0.16), radius 999px, padding 5.6px 7.2px 5.6px 16px, shadow `0 6px 18px rgba(0, 0, 0, 0.25)`; label "Switch teaser:" 13.12px/500 uppercase rgba(255,255,255,0.7); active "Animation" pill #76b900 with #0c1006 text 14.72px/500, padding 7.2px 16px, shadow `0 4px 14px rgba(118, 185, 0, 0.4)`; inactive "Robotics" rgba(255,255,255,0.85).
8. **Scroll chevron** (y=846, 36×36): 16px rotated border chevron in rgba(255,255,255,0.75), bouncing 8px every 2s, 1.6rem from the bottom.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Hero Black | #050608 | (literal) | hero ground behind the video |
| Nav Glass | rgba(14, 16, 20, 0.55) | (literal) | fixed nav over the hero |
| Paper | #fafaf7 | --paper | page background, author section, odd sections |
| Paper 2 | #f2f2ec | --paper-2 | even sections, BibTeX section |
| Card | #ffffff | --card | pill tabs, method figure and video cards, scrolled nav (82%) |
| Ink | #111418 | --ink | headings, body, link buttons, footer background |
| Ink Soft | #2b2f36 | --ink-soft | content paragraphs, author links, overview caption, scrolled nav links |
| Muted | #5a6170 | --muted | affiliations, notes, section captions, inactive pill tabs |
| Hairline | #e4e6eb | --hairline | section top borders, pill tab borders, figure borders |
| NVIDIA Green | #76b900 | --accent | heading underline bar, active toggle and pill tab, brand tile, footer links |
| Green Dark | #5b8f00 | --accent-dark | superscripts, emphasis, button hover fill, link hover |
| Green Wash | rgba(118, 185, 0, 0.12) | --accent-soft | pill tab hover fill, scrolled-nav link hover |
| Lime | #aef250 | (literal) | wordmark gradient start, superscripts on the dark hero |
| Forest | #2b9348 | (literal) | wordmark gradient end, brand tile gradient end |
| Active Text | #0c1006 | (literal) | text on green active pills |
| Code Black | #0f1115 / #e5e9ef / #1a1d23 | (literal) | BibTeX pre fill / text / border |
| Footer Text | #d2d6de / #aeb4bf | (literal) | footer text / paragraphs |
| Footer Link Hover | #9fdc2d | (literal) | footer link hover |
| Video Well | #0a0c10 | (literal) | background behind section videos |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| All text | 'NVIDIA', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif (NVIDIA Sans woff2 from images.nvidia.com) | NVIDIA 400, 500, 700 (600 requests snap to 700) | Inter |
| Code | 'JetBrains Mono', 'Menlo', 'SF Mono', 'Consolas', monospace | no web font loaded; Consolas on Windows | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Wordmark | `.cinema-title .motionbricks-logo` | 46.4px / 700 / 0.88, letter-spacing -0.03em | lime gradient |
| Hero subtitle | `.cinema-subtitle` | clamp(1rem, 1.8vw, 1.4rem) → 22.4px / 400 / 1.35 | rgba(255,255,255,0.92) |
| Venue line | `.cinema-venue` | 0.95rem = 15.2px / 500 uppercase, letter-spacing 0.04em | rgba(255,255,255,0.78) |
| Section heading | `.section .title.is-3` | 1.9rem = 30.4px / 600, letter-spacing -0.015em | #111418 |
| Subheading | `.section .title.is-5` | Bulma 20px / 600 | #2b2f36 |
| Authors | `.authors-list` | 1.08rem → 16.8px / 400 / 2 | #111418, links #2b2f36 |
| Affiliations | `.authors-affiliations` | 0.92rem = 14.72px, letter-spacing 0.01em | #5a6170 |
| Notes | `.authors-notes` | 0.82rem = 13.12px, letter-spacing 0.02em | #5a6170 |
| Body content | `.section .content` | 1.02rem = 16.32px / 1.75 | #2b2f36 |
| Section caption | `.section-caption` | 1rem / 1.65, max 780px | #5a6170 |
| Nav link | `.site-nav-links a` | 0.88rem = 14.08px / 500 | rgba(255,255,255,0.82) |
| Button | `.publication-links .button` | 0.95rem = 15.2px / 500 | #ffffff |
| Pill tab | `.pill-tab` | 0.88rem = 14.08px / 500 / 1.3 | #5a6170 (active #0c1006) |
| BibTeX | `#bibtex pre` | 0.88rem = 14.08px / 1.55 | #e5e9ef |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link buttons, toggle, pill tabs | 999px | buttons 1px #111418; tabs 1px #e4e6eb; toggle 1px rgba(255,255,255,0.16) | buttons `0 1px 2px rgba(17, 20, 24, 0.08)`, hover `0 6px 16px rgba(91, 143, 0, 0.25)`; active tab `0 4px 12px rgba(118, 185, 0, 0.28)` |
| Section videos, figures, pill video frame | 14px | 1px rgba(17,20,24,0.06) or #e4e6eb | `0 2px 6px rgba(17, 20, 24, 0.05), 0 12px 32px rgba(17, 20, 24, 0.08)`; hover lifts 2px |
| Method figure card | 14px, padding 1.25rem | 1px #e4e6eb | `0 1px 2px rgba(17, 20, 24, 0.04), 0 2px 8px rgba(17, 20, 24, 0.04)` |
| BibTeX pre | 10px | 1px #1a1d23 | the 14px-frame shadow |
| Nav links, brand tile | 7px | none | brand `0 2px 8px rgba(118, 185, 0, 0.35)` |
| Heading underline | 2px | — | 44×3px #76b900 bar, 0.65rem below the heading |
| Related-project callout | 0 6px 6px 0 | 3px #76b900 left | none; fill rgba(118,185,0,0.04) |

## Layout Metrics

- **Containers**: nav inner max 1200px; hero content max 1100px; Bulma `.container` max 1344px; text and media columns 960px (`--media-max`, x=240 at 1440); captions max 780px; author list max 920px; BibTeX max 900px.
- **Hero**: min-height 100vh = 900px at this viewport, padding 96px 24px 72px, content bottom-aligned so the wordmark lands at y≈530; title→subtitle 12px, subtitle→venue 20px, venue→buttons 28px, buttons→toggle 22.4px.
- **Author section**: padding 48px 24px 20px on #fafaf7, so the author lines start at y=948.
- **Sections**: padding 3.5rem 1.5rem = 56px 24px; every section after the first gets a 1px #e4e6eb top border; even sections #f2f2ec; heading margin-bottom 1.25rem plus the 0.65rem bar.
- **Media**: section videos 100% of 960px with 1rem vertical margin; video grids 3 columns (or 2 for `--halves`, max 1040px), gap 1.25rem, max 1140px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >900px | 24px | 16px | 46.4px (3.4vw caps at 2.9rem from 1365px) | full nav, 3-column video grids |
| ≤900px | 16px (hero) | 16px | `.publication-title` 3.4vw, floor 28.8px | nav collapses to a hamburger with a dark drop panel; hero min-height 92vh, padding 5rem 1rem 3.5rem; subtitle 16px; video grids 2 columns |
| ≤768px | 16px | 16px | 1.7rem = 27.2px | sections 40px 16px; h2 24px; buttons 13.6px with 8px 14.4px padding |
| ≤640px | 16px | 16px | 27.2px | related-project callout stacks |
| ≤600px | 16px | 16px | 27.2px | video grids 1 column; teaser toggle 11.52px label, 13.12px buttons |

## Components

- **Cinematic hero**: full-viewport `<video>` with the two-layer overlay quoted above; centred text block pinned to the bottom; white text with soft dark text-shadows.
- **Gradient wordmark**: NVIDIA 700, letter-spacing -0.03em, `linear-gradient(100deg, #aef250 0%, #76b900 45%, #2b9348 100%)` clipped to text with a faint green glow.
- **Pill button** (`.publication-links .button`): #111418 fill and border, white NVIDIA 15.2px/500, radius 999px, padding 0.6rem 1.15rem, 44px tall, icon left with 0.35rem gap. Hover: #5b8f00 fill and border, translateY(-1px), shadow `0 6px 16px rgba(91, 143, 0, 0.25)`.
- **Glass teaser toggle**: dark translucent capsule with blur, uppercase label, two segment buttons; active segment #76b900 with #0c1006 text and lift; inactive hover rgba(255,255,255,0.1).
- **Section heading**: centred inline-block 30.4px/600 #111418, with a 44×3px #76b900 bar (2px radius) centred 0.65rem below.
- **Pill tabs** (`.pill-tab`): white, 1px #e4e6eb, radius 999px, padding 6.4px 15.2px, 14.08px/500 #5a6170; hover #5b8f00 text, #76b900 border, green-wash fill; active #76b900 fill with #0c1006 text and green shadow. They switch the clip in a 16:9 #0a0c10 frame with 14px radius.
- **Video card** (`.video-card`): white, 1px #e4e6eb, 14px radius, small shadow; 16:9 media on #0a0c10; caption 14.72px/500 #111418 with a 1px top rule; lowercase green tag pill (#5b8f00 on the green wash).
- **BibTeX**: #0f1115 block, 1px #1a1d23, 10px radius, padding 1.4rem 1.5rem, JetBrains Mono stack 14.08px #e5e9ef, the 14px-frame shadow, on a #f2f2ec section.
- **Footer**: #111418, padding 2.5rem 1.5rem 2rem, 14.4px #aeb4bf text, #76b900 links with 1px green underline, hover #9fdc2d.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Fixed nav | yes | dark glass over the hero, white glass after scroll, green brand tile |
| Cinematic video hero | yes | full-viewport autoplay clip with gradient overlay, bottom-anchored text |
| Venue badge | present but non-standard | an uppercase text line, not a pill |
| Title / subtitle | yes | lime gradient wordmark + white subtitle |
| Teaser switch | yes | glass segmented toggle (Animation / Robotics) |
| Link buttons | yes | four black pills, green on hover |
| Authors / affiliations | yes | separate light section below the hero with green superscripts |
| Overview / method figures | yes | 960px media in 14px frames with soft shadows |
| Video demos | yes | uncut demo, pill-tab switched clips, side-by-side comparisons |
| Stats strip | present but non-standard | `.stat-strip` styles exist in the CSS but no strip renders |
| Results tables | absent from the source | comparisons are videos |
| BibTeX | yes | dark code block on paper-2 |
| Footer | yes | ink footer with green links; credits Nerfies via GEAR-SONIC |

## Adapting to Other Content

- **More authors**: keep them in the light author section after the hero, 16.8px with line-height 2 inside 920px, green #5b8f00 superscripts; never put authors over the video.
- **A results table**: centre it in the 960px column inside a white card (1px #e4e6eb, 14px radius, small shadow); header 14.08px/600 #111418, cells 16.32px #2b2f36, best values 600 #5b8f00.
- **Long publication or news lists**: use the related-project callout pattern (3px #76b900 left bar, rgba(118,185,0,0.04) fill, radius 0 6px 6px 0, padding 1rem 1.25rem) for each item, stacked with 1.4rem gaps.
- **No video available**: keep the hero structure but use a still frame as the `::before` cover image with the same overlay; the bottom-anchored text needs a dark image to stay legible.

## Do's and Don'ts

- Do keep the hero full-viewport with text anchored to the bottom over the darkening gradient.
- Do use NVIDIA green only for the wordmark, active states, the 44×3px heading bars and superscripts.
- Do switch to warm paper #fafaf7 immediately below the hero; the contrast between dark trailer and light report is the identity.
- Do frame every video at 960px with 14px radii and the soft two-layer shadow.
- Don't use the giant `clamp(6rem, 22vw, 22rem)` cinema title size; the rendered wordmark is 46.4px.
- Don't place pill buttons in green by default; they are black and turn #5b8f00 on hover.
- Don't add body copy to the hero beyond subtitle and venue.

## Surfaces

A #050608 full-viewport video hero with a dark-to-darker gradient and a faint green radial glow at 50% 85%; then #fafaf7 and #f2f2ec alternating sections separated by 1px #e4e6eb rules; white cards for tabs and figure frames; a #0f1115 BibTeX block and #111418 footer.

## Imagery

Game-engine footage: realistic third-person characters walking, fighting and interacting with props in Unreal Engine scenes, plus humanoid robot clips behind the "Robotics" toggle. Section media are 16:9 videos on near-black wells with 14px radii; the method figure is a light diagram in a white card.

## Layout

A 900px video hero, a short author band, then a single centred 960px column through Overview, Uncut Animation Demo, Smart Locomotion, Smart Objects, Smart Primitive Setup, In-betweening Comparisons and BibTeX, each section 56px padded and alternating paper tones. About 10,100px tall.

## Agent Prompt Guide

Quick colors: hero #050608, paper #fafaf7 / #f2f2ec, ink #111418, soft ink #2b2f36, muted #5a6170, hairline #e4e6eb, accent #76b900 (dark #5b8f00), wordmark gradient #aef250 → #76b900 → #2b9348.

1. "Build a full-viewport video hero: background #050608, `<video>` with object-fit cover, overlay linear-gradient(180deg, rgba(4,6,8,0.3) 0%, rgba(4,6,8,0.15) 38%, rgba(4,6,8,0.85) 100%), radial-gradient(1400px 700px at 50% 85%, rgba(118,185,0,0.2), transparent 70%). Bottom-aligned centred content, padding 96px 24px 72px: wordmark 46.4px/700 with linear-gradient(100deg, #aef250 0%, #76b900 45%, #2b9348 100%) clipped to text, subtitle 22.4px rgba(255,255,255,0.92), uppercase venue 15.2px/500 rgba(255,255,255,0.78), letter-spacing 0.04em."
2. "Make pill link buttons: #111418 fill and 1px border, white 15.2px/500, radius 999px, padding 0.6rem 1.15rem, icon left; hover #5b8f00 fill, translateY(-1px), shadow 0 6px 16px rgba(91,143,0,0.25). Below them a glass toggle: rgba(10,12,16,0.55) with backdrop blur 12px, 1px rgba(255,255,255,0.16), radius 999px; active segment #76b900 with #0c1006 text."
3. "Create a light section: padding 56px 24px, background #fafaf7 (alternate #f2f2ec), 1px #e4e6eb top border; centred heading 30.4px/600 #111418 with a 44×3px #76b900 bar 0.65rem below; 960px video with radius 14px, 1px rgba(17,20,24,0.06) border and shadow 0 2px 6px rgba(17,20,24,0.05), 0 12px 32px rgba(17,20,24,0.08)."

## Similar Pages

- Industry-lab project pages that open with a full-screen product-trailer video and brand-coloured wordmark before a conventional paper layout.
- Nerfies-template pages restyled with a corporate typeface and a single brand accent.

## Quick Start

```css
:root {
  --accent: #76b900;
  --accent-dark: #5b8f00;
  --accent-soft: rgba(118, 185, 0, 0.12);
  --ink: #111418;
  --ink-soft: #2b2f36;
  --muted: #5a6170;
  --hairline: #e4e6eb;
  --paper: #fafaf7;
  --paper-2: #f2f2ec;
  --card: #ffffff;
  --hero-bg: #050608;
  --font: 'NVIDIA', 'Inter', -apple-system, 'Segoe UI', Arial, sans-serif;
  --shadow-sm: 0 1px 2px rgba(17, 20, 24, 0.04), 0 2px 8px rgba(17, 20, 24, 0.04);
  --shadow-md: 0 2px 6px rgba(17, 20, 24, 0.05), 0 12px 32px rgba(17, 20, 24, 0.08);
  --radius: 10px;
  --radius-lg: 14px;
  --media-max: 960px;
}
```

## Provenance

- **URL**: https://nvlabs.github.io/motionbricks/
- **Paper**: MotionBricks: Scalable Real-Time Motions with Modular Latent Generative Model and Smart Primitives (arXiv 2604.24833), Tingwu Wang, Olivier Dionne, Michael De Ruyter, et al. (NVIDIA, ETH Zürich, Simon Fraser University).
- **Venue**: ACM TOG; SIGGRAPH 2026.
- **Selection reason**: the arXiv comment lists the venue as ACM TOG; SIGGRAPH 2026 without an explicit acceptance word and links this project page.
- **Template credit**: the footer states the template is adapted from Nerfies, via GEAR-SONIC; Bulma, bulma-carousel, bulma-slider and Font Awesome are loaded.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), an additional computed-style probe below the fold, the 1440×900 and tall screenshots, and `index.css` and `index.html` read directly, on 2026-10-28.
