# POET-X — Style Reference

> A planetarium lobby: an ink-violet night sky across the top, a lavender-to-sky glow on the name, then plain white lecture halls below.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, a second live render used to read computed styles of lower-page elements (math block, h4, list items, BibTeX, captions, divider pill, references), and the page's inline `<style>` block plus Bulma 0.9.1 (`static/css/bulma.min.css`). The page is a Nerfies-family Bulma page restyled by a long inline stylesheet; where Bulma and the inline rules disagree, the `!important` inline rules win in the render. The full-page screenshot covers the top ~2,700px; the divider bands, method math blocks, BibTeX and footer are described from the live render's computed styles and the CSS.

## Overview

A light, centred Bulma page (about 13,000px tall) framed by deep indigo. A fixed 56px translucent navy bar sits over a 422px hero painted with a 135deg gradient from #0f0c29 through #1a1459 and #24243e to #0d1b3e, with two soft radial glows (violet top-left, blue bottom-right). In the hero the short name "POET-X" is the only coloured text, filled with a 90deg #a78bfa → #60a5fa gradient; the long subtitle, authors and affiliations are white at decreasing opacity. Two gradient pill buttons (#6d28d9 → #2563eb) close the hero. Below, the content alternates white and #f8f9fc full-width bands, each with a centred indigo (#1a1459) section title underlined by a 48×3px violet-to-blue bar and justified 16px body text in Google Sans. Three full-width dark "divider" bands (Performance Comparison, In-depth Efficiency Study, the method title) repeat the hero gradient with a faint plus-sign pattern, an uppercase lavender pill and a 32px white heading. Figures are wide PNG plots with 10px radius and a soft shadow; equations sit in pale #f3f4f8 blocks with a 3px violet left bar. A gradient footer closes the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white family #ffffff / #fdffff / #fffffe 40.3% (the abstract band below y=478); hero indigo family #24214c 15.3%, #1c1551 13.9%, #1a254a 12.9%, #211e51 9.7% (together 51.8%, the gradient hero and the navy bar); #acacbd 7.8% (anti-aliased white-on-indigo text and the gray body text mix). The lavender and violet accents are too small to form their own clusters.

Anatomy in DOM order (desktop 1440px, hero centred in a 960px container at x=240):

1. **Fixed nav bar** (`nav.sticky-nav`, 0–56px): rgba(18,20,40,.92) with backdrop blur 12px, 1px rgba(255,255,255,.08) bottom border, shadow 0 2px 20px rgba(0,0,0,.3), padding 0 32px. Left brand "POET-X" 16.8px/700 white, letter-spacing 0.03em (x=32, y=15). Right five links (Abstract, Results, Efficiency, Method, References) 14.08px/500 rgba(255,255,255,.75), padding 5.6px 13.6px, 20px radius, 4px gaps, ending at x=1408.
2. **Hero band** (`section.hero-gradient`, 56–478px): padding 96px 24px 72px; gradient as above; `::before` radial rgba(100,60,220,.18) at top-left, `::after` radial rgba(30,120,220,.15) at bottom-right.
3. **Title** (`h1.publication-title`, y=152–202): 41.6px/700, line-height 1.2, letter-spacing -0.01em, centred; the word is a `span.accent` with the #a78bfa → #60a5fa text gradient. Gap 12px.
4. **Subtitle** (`h2.publication-subtitle`, y=214–246): 21.6px/400, line-height 1.5, rgba(255,255,255,.85), centred, one line. Gap 28px.
5. **Authors** (y≈280, one line): 16.8px/400 rgba(255,255,255,.9), comma-separated `span.author-block` with 0.15rem side margins; superscript numbers coloured per affiliation (#a78bfa for 1, #60a5fa for 2, #94a3b8 for 3). Gap ≈10px.
6. **Affiliations** (y≈316, one line): 15.2px rgba(255,255,255,.65), separated by " · ", same coloured superscripts. Gap 24px.
7. **Link buttons** (`.publication-links`, y=363–406): "Paper" (Font Awesome `fa-file-pdf`) and "Code" (`fa-github`), each 104×43px, 12px apart, icon left. Hero ends 72px below.
8. **Abstract band** (`section#abstract.content-section`, from y=478): white, padding 64px 24px; section title at y=542 (28.8px/700 #1a1459, two lines, with the 48×3px gradient bar 8px below), then justified body text at y=642 in a 763px column (x=338).

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Deep Night | #0f0c29 | (literal) | hero gradient 0% stop, divider bands 0%, footer gradient start |
| Royal Indigo | #1a1459 | (literal) | hero gradient 35% stop, divider bands 40%, footer gradient end, section titles (`.section-title`) |
| Slate Indigo | #24243e | (literal) | hero gradient 65% stop |
| Navy | #0d1b3e | (literal) | hero gradient 100% stop |
| Divider Blue | #1e3a8a | (literal) | divider band gradient 100% stop |
| Nav Glass | rgba(18,20,40,0.92) | (literal) | fixed nav bar background |
| Violet Glow | rgba(100,60,220,0.18) | (literal) | hero `::before` radial glow |
| Blue Glow | rgba(30,120,220,0.15) | (literal) | hero `::after` radial glow |
| Lavender | #a78bfa | (literal) | title gradient start, superscript 1, author hover, footer links, divider pill fill (25%) and border (40%) |
| Sky | #60a5fa | (literal) | title gradient end, superscript 2 |
| Steel | #94a3b8 | (literal) | superscript 3 |
| Pale Lavender | #c4b5fd | (literal) | divider pill text, footer link hover |
| Violet | #6d28d9 | (literal) | button gradient start, section-title bar start, math-block left bar, back-to-top gradient, button hover shadow (45%) |
| Blue | #2563eb | (literal) | button gradient end, section-title bar end, back-to-top gradient end |
| Ink | #2d2d2d | body color | body text, list items, math blocks |
| Bulma Heading | #363636 | (Bulma) | `.content h4` subheads, bold inline text, BibTeX h2 |
| Caption Gray | #666666 | (literal) | `.figure-caption` |
| Reference Gray | #444444 | (literal) | `#references ol li` |
| Pre Gray | #4a4a4a | (Bulma) | BibTeX code text |
| Code Red | #da1039 | (Bulma) | inline `code` text (e.g. POET-X<sub>fast</sub>) |
| Code Well | #f5f5f5 | (Bulma) | inline `code` and `pre` background |
| Mist | #f8f9fc | body bg | page background, even `.content-section` bands, BibTeX and References bands |
| Math Gray | #f3f4f8 | (literal) | `.math-block` background |
| Band Line | #eef0f6 | (literal) | 1px bottom border of every `.content-section` |
| White | #ffffff | (literal) | odd `.content-section` bands, title, nav brand, button labels, divider h2 |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| UI / text | 'Google Sans', 'Noto Sans', sans-serif (Google Fonts link also requests Castoro) | Google Sans 400, 500, 700; Noto Sans and Castoro never load | Figtree |
| Code | Bulma `monospace` | system monospace (Consolas on Windows) | JetBrains Mono |
| Math | MathJax 3 CHTML | MJXTEX, MJXTEX-I, MJXTEX-B, MJXTEX-A, MJXTEX-C, MJXTEX-S1, MJXTEX-S4 | — |
| Icons | Font Awesome (SVG replacement) | inline SVG icons | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.publication-title` | 2.6rem = 41.6px / 700 / 1.2, letter-spacing -0.01em | #a78bfa → #60a5fa text gradient |
| Subtitle | `.publication-subtitle` | 1.35rem = 21.6px / 400 / 1.5 | rgba(255,255,255,.85) |
| Authors | `.author-block` | 1.05rem = 16.8px / 400 | rgba(255,255,255,.9) |
| Affiliations | `.affil-block` | 0.95rem = 15.2px / 400 | rgba(255,255,255,.65) |
| Nav brand | `.sticky-nav .nav-brand` | 1.05rem = 16.8px / 700, letter-spacing 0.03em | #ffffff |
| Nav link | `.sticky-nav .nav-links a` | 0.88rem = 14.08px / 500 | rgba(255,255,255,.75) |
| Button | `.external-link` | 0.9rem = 14.4px / 600 | #ffffff |
| Section title | `.section-title` | 1.8rem = 28.8px / 700 / 32.4px | #1a1459 |
| Divider heading | `.section-divider h2` | 2rem = 32px / 700 / 1.5, letter-spacing 0.01em | #ffffff |
| Divider subtitle | `.divider-subtitle` | 0.95rem = 15.2px | rgba(255,255,255,.7) |
| Divider pill | `.divider-pill` | 0.78rem = 12.48px / 600 uppercase, letter-spacing 0.08em | #c4b5fd |
| Subhead | `.content h4` | 1.25em = 20px / 600 / 1.125 | #363636 |
| Body | `body`, `.content p` | 16px / 400 / 24px, justified | #2d2d2d |
| Caption | `.figure-caption` | 0.9rem = 14.4px / 400 / 1.5, centred, max 720px | #666666 |
| References | `#references ol li` | 0.93rem = 14.88px / 1.6 | #444444 |
| BibTeX heading | `#BibTeX h2.title.is-3` | 32px / 600 | #363636 |
| BibTeX code | `.content pre` | 0.875em = 14px / 21px | #4a4a4a |
| Footer | `.site-footer` | 0.88rem = 14.08px / 1.7; license line 0.8rem | rgba(255,255,255,.7); license rgba(255,255,255,.4) |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link buttons | 50px | 2px transparent | none at rest; hover 0 8px 24px rgba(109,40,217,.45) |
| Nav links | 20px | none | none; hover fill rgba(255,255,255,.12) |
| Nav bar | 0 | bottom 1px rgba(255,255,255,.08) | 0 2px 20px rgba(0,0,0,.3) |
| Figures (`.figure-img`) | 10px | none | 0 4px 24px rgba(0,0,0,.1), 0 1px 4px rgba(0,0,0,.06); hover 0 8px 36px rgba(0,0,0,.14), 0 2px 8px rgba(0,0,0,.08) |
| Math block | 0 8px 8px 0 | left 3px #6d28d9 | none |
| Section-title bar | 2px | none (48×3px gradient block) | none |
| Divider pill | 50px | 1px rgba(167,139,250,.4) | none |
| Inline code / pre | 0 (Bulma default) | none | none |
| Back-to-top | 50%, 44px | none | 0 4px 16px rgba(109,40,217,.4); hover 0 8px 24px rgba(109,40,217,.5) |
| Content bands | 0 | bottom 1px #eef0f6 | none |

## Layout Metrics

- **Containers**: Bulma `.container.is-max-desktop` = 960px max at ≥1024px (x=240 at 1440). Text sections nest `.columns.is-centered > .column.is-four-fifths`, giving a 763px reading column at x=338. The teaser figures are capped inline at `max-width: 70%`, result plots at 80%, and wide tables/plots at 100% of the 960px container; paired plots use `.two-col-figures` (flex, 16px gap, each `max-width: 48%`).
- **Nav**: fixed, 56px tall, padding 0 32px; the hero carries `margin-top: 56px` so nothing is covered.
- **Hero**: padding 96px 24px 72px, rendered 422px tall (56–478).
- **Section rhythm**: `.content-section` padding 64px 24px, so text blocks sit 128px apart across a band edge; section title margin-bottom 24px; `.content h4` margin-bottom 16px; figures 20px vertical margin, caption pulled up 8px with 24px below. Divider bands padding 40px 24px. BibTeX uses Bulma `.section` padding 48px 24px. Footer padding 40px 24px.
- **Band order** (`:nth-child(even)` gives #f8f9fc): Abstract white, teaser figures #f8f9fc, single-layer benchmark white, divider, multi-node white, divider, memory white, divider, method white, BibTeX #f8f9fc (body shows through), References #f8f9fc.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px | 24px band padding, 960px container | 16px | 41.6px | four-fifths column (763px) |
| 769–1023px | 24px band padding, container fluid | 16px | 41.6px | four-fifths column of the fluid width |
| ≤768px | hero padding 80px 16px 56px | 16px | 28.8px | nav links hidden (brand only); Bulma columns stack to full width; paired plots go 100% wide; divider h2 24px |

## Components

- **Nav bar** (`.sticky-nav`): fixed, 56px, rgba(18,20,40,.92) with 12px backdrop blur, 1px rgba(255,255,255,.08) bottom border, shadow 0 2px 20px rgba(0,0,0,.3). Brand left 16.8px/700 white; links right 14.08px/500 rgba(255,255,255,.75), padding 5.6px 13.6px, radius 20px; hover white text on rgba(255,255,255,.12), 0.2s.
- **Gradient title** (`.publication-title .accent`): 41.6px/700, letter-spacing -0.01em, `background: linear-gradient(90deg, #a78bfa, #60a5fa)` clipped to text.
- **Primary button** (`.external-link.btn-primary`): inline-flex, gap 7.2px, padding 8.8px 20.8px, radius 50px, 2px transparent border, `linear-gradient(135deg, #6d28d9, #2563eb)`, 14.4px/600 white, Font Awesome icon left. Hover: translateY(-2px) and shadow 0 8px 24px rgba(109,40,217,.45), 0.22s. An outline variant (`.btn-outline`: rgba(255,255,255,.08) fill, rgba(255,255,255,.25) border) is declared but not used.
- **Section title** (`.section-title`): 28.8px/700 #1a1459 centred, margin-bottom 24px; `::after` is a 48×3px block, `linear-gradient(90deg, #6d28d9, #2563eb)`, radius 2px, 8px below the text, centred.
- **Divider band** (`.section-divider`): full width, `linear-gradient(135deg, #0f0c29 0%, #1a1459 40%, #1e3a8a 100%)`, padding 40px 24px, centred; overlay of a 60px plus-sign SVG tile in white at 3% opacity. Contents: uppercase pill (12.48px/600, letter-spacing 0.08em, #c4b5fd on rgba(167,139,250,.25), 1px rgba(167,139,250,.4) border, padding 3.2px 14.4px, radius 50px), then h2 32px/700 white, then a 15.2px rgba(255,255,255,.7) subtitle such as "Multi-node pretraining · Quantized training · Wall-clock efficiency".
- **Figure** (`.figure-img`): centred block PNG, radius 10px, soft two-layer shadow that deepens on hover; caption below in 14.4px #666666, centred, max 720px.
- **Math block** (`.math-block`): #f3f4f8, 3px #6d28d9 left border, radius 0 8px 8px 0, padding 16px 20px, 20px vertical margin, horizontal scroll for long MathJax lines; most are centred inline.
- **Subhead list** (`.content h4` + `ul`): 20px/600 #363636 subhead, then Bulma disc list (2em left margin, 4px between items) of 16px #2d2d2d text with bold numbers.
- **BibTeX**: Bulma `pre` on #f5f5f5, padding 17.5px 21px, 14px monospace #4a4a4a, no radius, under a 32px/600 #363636 centred heading; no copy button.
- **Footer** (`.site-footer`): `linear-gradient(135deg, #0f0c29, #1a1459)`, padding 40px 24px, centred 14.08px rgba(255,255,255,.7); links #a78bfa, hover #c4b5fd underlined; license line 12.8px rgba(255,255,255,.4).
- **Back-to-top** (`#back-to-top`): fixed 32px from bottom-right, 44px circle with the violet-to-blue gradient and a white chevron, shadow 0 4px 16px rgba(109,40,217,.4); fades in after scrolling.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Fixed nav with section links | yes | translucent navy glass bar, rounded hover chips |
| Title / subtitle / authors / affiliations | yes | centred white-on-indigo, gradient short name, colour-coded superscripts |
| Venue badge | absent from the source | ICML 2026 Oral is not mentioned anywhere on the page |
| Link buttons | yes | two violet-to-blue gradient pills with Font Awesome icons |
| Teaser | present but non-standard | no hero image; two wide latency and memory bar charts in a #f8f9fc band directly after the abstract |
| Abstract | present but non-standard | headed by a descriptive title ("POET-X: A Scalable and Memory-efficient Method…") rather than "Abstract" |
| Section dividers | yes | three dark gradient bands with uppercase pill and 32px white heading |
| Results tables | present but non-standard | results tables are PNG images (`throughput_comparison.png`), no HTML `<table>` |
| Method / equations | yes | MathJax in pale gray blocks with a violet left bar |
| BibTeX | yes | plain Bulma `pre`, no copy button |
| References | yes | numbered `ol` in 14.88px #444444 on #f8f9fc |
| Video | absent from the source | none |
| Footer | yes | indigo gradient with template credit and CC BY-SA line |

## Adapting to Other Content

- **More authors**: keep the one-line `author-block` row at 16.8px and let it wrap inside 960px; extend the superscript colour code (#a78bfa, #60a5fa, #94a3b8) by reusing the three colours in order rather than adding new ones.
- **A venue or award**: use the divider-pill recipe (uppercase 12.48px/600 #c4b5fd on rgba(167,139,250,.25), 1px rgba(167,139,250,.4) border) above the title inside the hero.
- **A results table**: put an HTML table in the four-fifths column; header 14.4px/600 #1a1459 with a 1px #eef0f6 rule, body 16px #2d2d2d, best value bold #6d28d9. Wrap it in the `.figure-img` radius and shadow on a white band.
- **Long publication or news lists**: use the references style (14.88px #444444, 12px between items) inside a #f8f9fc band, with dates in #1a1459 600.
- **More sections**: alternate white and #f8f9fc bands and insert a dark divider band before each major part (Results, Analysis, Method).

## Do's and Don'ts

- Do keep the dark indigo gradient for chrome only: nav, hero, divider bands and footer. Content bands stay white or #f8f9fc.
- Do reserve the lavender-to-sky gradient for the short name in the hero.
- Do mark every section title with the 48×3px violet-to-blue bar.
- Do justify body paragraphs inside the 763px column, as the page does.
- Don't put text in a third hue; accents are violet/blue gradients and the lavender family only.
- Don't round the BibTeX or code blocks; Bulma's square #f5f5f5 wells are part of the look.
- Don't add a hero image; the hero is type and gradient only.

## Surfaces

Three surface families. Chrome surfaces are dark gradients: the nav glass rgba(18,20,40,.92), the hero (#0f0c29 → #1a1459 → #24243e → #0d1b3e with two radial glows), the divider bands (#0f0c29 → #1a1459 → #1e3a8a with a 3% plus pattern) and the footer (#0f0c29 → #1a1459). Content surfaces alternate #ffffff and #f8f9fc full-bleed bands separated by 1px #eef0f6. Inset surfaces are #f3f4f8 math blocks with a #6d28d9 bar and #f5f5f5 code wells.

## Imagery

Matplotlib-style bar charts, line plots and table screenshots as PNGs on white, each with a 10px radius and soft shadow; hatched bars in salmon, blue and green come from the figures themselves, not the page palette. No photos, no video, no logos in the hero.

## Layout

Single centred column. Dark nav and hero, then a sequence of full-width bands, each holding a centred 28.8px indigo title and a 763px justified text column with wide figures between paragraphs. Three dark divider bands split the page into Results, Efficiency and Method parts. Separation comes from band colour changes and 64px padding, not from cards.

## Agent Prompt Guide

Quick colors: hero #0f0c29 → #1a1459 → #24243e → #0d1b3e, accent text #a78bfa → #60a5fa, buttons #6d28d9 → #2563eb, section title #1a1459, body #2d2d2d, page #f8f9fc and #ffffff, math block #f3f4f8, band line #eef0f6.

1. "Build a centred hero below a fixed 56px nav (rgba(18,20,40,.92), backdrop blur 12px, 1px rgba(255,255,255,.08) bottom border). Hero background linear-gradient(135deg, #0f0c29 0%, #1a1459 35%, #24243e 65%, #0d1b3e 100%), padding 96px 24px 72px. Title 41.6px/700 Google Sans with the name filled by linear-gradient(90deg, #a78bfa, #60a5fa) clipped to text; subtitle 21.6px rgba(255,255,255,.85); authors 16.8px rgba(255,255,255,.9) with #a78bfa / #60a5fa / #94a3b8 superscripts; affiliations 15.2px rgba(255,255,255,.65)."
2. "Make link buttons: inline-flex, padding 8.8px 20.8px, radius 50px, background linear-gradient(135deg, #6d28d9, #2563eb), 14.4px/600 white text with a Font Awesome icon on the left, 12px apart. Hover: translateY(-2px), box-shadow 0 8px 24px rgba(109,40,217,.45)."
3. "Create a content band: full width, background #ffffff (alternate with #f8f9fc), padding 64px 24px, 1px #eef0f6 bottom border. Centred title 28.8px/700 #1a1459 with a 48×3px linear-gradient(90deg, #6d28d9, #2563eb) bar 8px below; 763px column of justified 16px/24px #2d2d2d text; equations in #f3f4f8 blocks with a 3px #6d28d9 left border and radius 0 8px 8px 0."

## Similar Pages

- Nerfies-derived Bulma project pages restyled with a dark gradient hero, such as the MathVista and SGP-Bench pages credited in the footer.
- LLM-systems pages that pair a navy chrome with violet-blue gradient buttons and plot-heavy white content bands.

## Quick Start

```css
:root {
  --hero: linear-gradient(135deg, #0f0c29 0%, #1a1459 35%, #24243e 65%, #0d1b3e 100%);
  --divider: linear-gradient(135deg, #0f0c29 0%, #1a1459 40%, #1e3a8a 100%);
  --nav: rgba(18, 20, 40, 0.92);
  --accent-text: linear-gradient(90deg, #a78bfa, #60a5fa);
  --accent-fill: linear-gradient(135deg, #6d28d9, #2563eb);
  --violet: #6d28d9;
  --heading: #1a1459;
  --ink: #2d2d2d;
  --muted: #666666;
  --page: #f8f9fc;
  --band: #ffffff;
  --math: #f3f4f8;
  --line: #eef0f6;
  --font: "Google Sans", "Noto Sans", sans-serif;
  --container: 960px;
  --radius-pill: 50px;
  --radius-figure: 10px;
}
```

## Provenance

- **URL**: https://spherelab.ai/poetx/
- **Paper**: POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation (arXiv 2603.05500), Zeju Qiu, Lixin Liu, Adrian Weller, Han Shi, Weiyang Liu.
- **Venue**: ICML 2026 Oral.
- **Selection reason**: the arXiv 2603.05500 comment states acceptance at ICML 2026 Oral and links this project page.
- **Template credit**: footer reads "This website is adapted from Nerfies, MathVista, and SGP-Bench"; Bulma 0.9.1, Font Awesome, MathJax 3.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, a live render read for lower-page computed styles, and the page's inline stylesheet, markup and Bulma 0.9.1 read directly, on 2026-10-28.
