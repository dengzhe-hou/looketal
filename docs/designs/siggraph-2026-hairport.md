# HairPort — Style Reference

> A quiet journal masthead on warm paper: one enormous serif word, a gold dot, and everything else held to forest-green restraint.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and tall screenshots, and the page's own `assets/site.css` and `index.html`. Section blocks carry a `.reveal` class that fades them up 14px on scroll, so below-the-fold blocks are briefly transparent in load-time captures; the values below are the settled state. The 1rem base is 16px while `body` is 17px, so rem sizes and em sizes differ.

## Overview

An editorial, magazine-like project page on warm off-white #f7f7f4 with near-black ink #171817. Two families carry it: Source Serif 4 for the giant "HairPort" wordmark, the subtitle, all section headings and the abstract body, and Inter for navigation, buttons, kickers and UI text. A faint 56px grid (two 1px hairlines at 2.6% and 1.8% ink) is fixed behind the top of the page and fades out by 74% of the viewport height. Accents are deliberately low-chroma: a deep forest green (#183f3b / #23615a) for kickers, links and hover states, a single gold dot (#9a6b25) in the venue pill and gold mono indices on contribution cards. Below a sticky blurred header comes a centred hero, a framed 2200×965 teaser, then alternating white-ground and pale-green-gray toned bands of two-column sections (sticky heading left, text right), image carousels with before/after sliders, a resource-card grid, a news timeline, and a dark green-black citation band and footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): warm off-white family #f7f7f4 / #f6f7f4 / #f8f7f5 / #fafaf7 together 72.8%; warm brown-gray #665b53 17.9% (the photographs in the teaser, which starts at y=685); light gray #e0dfda 9.1% (hairlines, button borders and pale photo backgrounds). The green and gold accents cover too little area to form clusters.

Anatomy in DOM order (desktop 1440px):

1. **Sticky header** (`header.site-header`, 0–69px): rgba(247,247,244,0.9) with `backdrop-filter: blur(18px) saturate(160%)`, 1px rgba(23,24,23,0.10) bottom border. Inner `nav.nav-wrap` is 1360px wide (x=40), min-height 68px, flex space-between.
2. **Brand** (x=40, y=18): a 32×32 white square (1px #bbc4bb border, 6px radius, shadow 0 1px 2px rgba(23,24,23,0.06)) holding an "HP" SVG monogram in #18211f with a #183f3b flow stroke, then "HairPort" 17px/800 #171817, letter-spacing 0.01em, gap 0.62rem.
3. **Nav links** (right, y=16, 36px tall): Abstract, Method, Results, Bald Converter, Code, Cite; 14.08px/650 #454b46, padding 6.72px 11.84px, 6px radius, gap 0.15rem. Hover and active (scroll-spy `.is-active`): background #e4efec, text #183f3b.
4. **Hero** (`section.hero`, from y=69): padding 92.8px 0 80px (clamp(3rem, 7vw, 5.8rem) top); `.hero-inner` max 980px, centred, text-align center, starting y=162.
5. **Venue pill** (`.paper-kicker`, y=162, ≈30px tall): "ACM SIGGRAPH 2026", 12.48px/800 uppercase, letter-spacing 0.11em, #183f3b on #ffffff, 1px #d8ddd6 border, 999px radius, padding 0.45rem 0.75rem, led by a 7.2px #9a6b25 dot with a 0.55rem gap. Margin-bottom 1.15rem.
6. **Title** (`h1.hero-title`, y=217, 120px box): "HairPort" in Source Serif 4 140px/600, line-height 0.86, letter-spacing 0, #171817. Gap 22.4px.
7. **Subtitle** (`p.hero-subtitle`, y=360): Source Serif 4 39.2px/500, line-height 1.08, #343735, max-width 900px; wraps to two lines at 1440. Gap 21.6px.
8. **Authors** (`ul.authors`, y=469): 15.68px/400 #454b46, flex-wrapped, centred, separated by 3.5px #bbc4bb dots with 1.05rem gaps; links have transparent underlines that turn #183f3b on hover. Gap 21.6px.
9. **Summary** (`p.hero-summary`, y=513): Inter 16.96px/400, line-height 1.62, #616761, max-width 760px, two lines. Gap 26.4px.
10. **Button row** (`.cta-row`, y=594, 43px tall): Code (primary, dark), Dataset, Weights, BibTeX, arXiv, Paper DOI, and a dashed "Video coming soon"; gap 0.55rem, each with a 16px line icon on the left.
11. **Teaser** (`figure.hero-figure`, y=685, 1360×647): margin-top 48px, white, 1px #bbc4bb border, 8px radius, `box-shadow: 0 2px 4px rgba(23,24,23,0.06), 0 24px 60px rgba(23,24,23,0.10)`; image at aspect 2200/965 then a centred 14.4px #616761 caption on white with a 1px #d8ddd6 top border.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Warm Paper | #f7f7f4 | --bg | page background, header (at 90%) |
| White | #ffffff | --surface | venue pill, buttons, teaser and figure frames, cards, stat tiles |
| Sage Mist | #f0f2ee | --surface-alt | toned section bands (Bald Converter Results, Code and Assets) |
| Ink | #171817 | --ink | title, h2/h3, brand, button text |
| Ink Soft | #343735 | --ink-soft | hero subtitle, abstract body, timeline text |
| Muted | #616761 | --muted | hero summary, section intros, captions, card text, unavailable button |
| Muted Strong | #454b46 | --muted-strong | nav links, authors, carousel counter |
| Hairline | #d8ddd6 | --line | venue pill border, caption top rules, toned band borders, contribution cards, timeline rules |
| Line Strong | #bbc4bb | --line-strong | button borders, figure frames, brand square, author dots |
| Forest | #23615a | --accent | link hover, button hover border, focus outline, slider accent |
| Deep Forest | #183f3b | --accent-dark | venue pill text, eyebrow kickers, links, nav active text, timeline dates, primary hover fill |
| Mint Wash | #e4efec | --accent-soft | nav hover/active fill, resource tags |
| Gold | #9a6b25 | --gold | venue pill dot, contribution indices ("01") |
| Paper Dark | #18211f | --paper-dark | primary "Code" button, result labels, slider knob, carousel arrow hover |
| Paper Dark 2 | #22312f | --paper-dark-2 | top of the citation band gradient |
| Footer Black | #101412 | (literal) | footer background |
| Hover White | #fbfcfb | (literal) | secondary button background on hover |
| Slider Black | #0d0f0e | (literal) | ground behind before/after comparison images |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display / headings / abstract | "Source Serif 4", "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif | Source Serif 4 400, 500, 600, 700 (Google Fonts, opsz axis) | Newsreader |
| UI / body | "Inter", ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif | Inter 400, 700, 800 (650/750/850 requests snap to the nearest loaded file) | IBM Plex Sans |
| Mono | "JetBrains Mono", SFMono-Regular, Menlo, Consolas, monospace | JetBrains Mono 400, 500 | IBM Plex Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Wordmark title | `h1.hero-title` | 8.75rem = 140px / 600 / 0.86 | #171817 |
| Subtitle | `.hero-subtitle` | 2.45rem = 39.2px / 500 / 1.08 | #343735 |
| Section heading | `h2` | 3.35rem = 53.6px / 600 / 1.02 | #171817 |
| Card heading | `.contribution-card h3`, `.resource-card strong` | 21.6px / 650 (h3), 22.08px / 650 (strong) | #171817 |
| Eyebrow kicker | `.eyebrow` | 0.74rem = 11.84px / 850 uppercase, letter-spacing 0.14em, 36px rule before | #183f3b |
| Venue pill | `.paper-kicker` | 0.78rem = 12.48px / 800 uppercase, letter-spacing 0.11em | #183f3b |
| Body | `body` | 17px / 400 / 1.62 | #171817 |
| Abstract body | `.abstract-body` | Source Serif 4 1.16rem = 18.56px / 400 / 1.72 | #343735 |
| Section intro | `.section-heading p` | 1.05rem = 16.8px | #616761 |
| Authors | `.authors` | 0.98rem = 15.68px / 400 | #454b46 |
| Nav link | `.nav-links a` | 0.88rem = 14.08px / 650 | #454b46 |
| Button | `.button` | 0.92rem = 14.72px / 750 / 1 | #171817 (primary #ffffff) |
| Caption | `figcaption` | 0.9rem = 14.4px / 1.48 | #616761 |
| Contribution index | `.contribution-index` | JetBrains Mono 0.78rem / 700, letter-spacing 0.08em | #9a6b25 |
| Timeline date | `.timeline time` | 0.82rem / 850 uppercase, letter-spacing 0.05em | #183f3b |
| BibTeX | `.citation-box pre` | JetBrains Mono 0.86rem = 13.76px / 1.58 | #f5f6f2 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Buttons, nav links, brand square, stat tiles, copy button | 6px | buttons 1px #bbc4bb; unavailable dashed | hover `0 1px 2px rgba(23,24,23,0.04), 0 12px 30px rgba(23,24,23,0.07)` |
| Teaser, transfer slides | 8px | 1px #bbc4bb | `0 2px 4px rgba(23,24,23,0.06), 0 24px 60px rgba(23,24,23,0.10)` |
| Figure frames, comparison cards, resource cards | 8px | 1px #bbc4bb | `0 1px 2px rgba(23,24,23,0.04), 0 12px 30px rgba(23,24,23,0.07)`; resource hover uses the larger shadow |
| Contribution cards | 8px | 1px #d8ddd6 | none |
| Venue pill, carousel counter, panel labels, resource tags | 999px | pill 1px #d8ddd6 | panel labels `0 5px 16px rgba(23,24,23,0.18)` |
| Carousel arrows | 50%, 48px | 1px rgba(255,255,255,0.75) | `0 12px 30px rgba(23,24,23,0.18)` |
| Citation box | 8px | 1px rgba(255,255,255,0.14) | none; fill rgba(0,0,0,0.26) |

Page texture: `body::before { background-image: linear-gradient(rgba(23,24,23,0.026) 1px, transparent 1px), linear-gradient(90deg, rgba(23,24,23,0.018) 1px, transparent 1px); background-size: 56px 56px; mask-image: linear-gradient(180deg, rgba(0,0,0,0.75), transparent 74%) }`, fixed.

## Layout Metrics

- **Containers**: header, hero and wide figures use `width: min(1360px, calc(100% - 2 × gutter))`, gutter `clamp(1rem, 4vw, 2rem)` = 32px at 1440, so the 1360px cap wins and the hero renders at x=40; section content uses `.section-inner` at `min(1180px, …)` (x=130). Hero text column max 980px.
- **Hero**: padding 92.8px 0 80px; teaser margin-top 48px (clamp(2rem, 4vw, 3rem)); hero ends at y=1412.
- **Sections**: padding clamp(4.25rem, 8vw, 6.75rem) = 108px top and bottom; the Method section has 0 top padding because it follows the Abstract. Section heading block max 860px, margin-bottom 48px.
- **Split sections** (Abstract): grid 0.42fr / 0.58fr, gap clamp(2rem, 5vw, 4.75rem) = 72px at 1440; the left heading is sticky at top 94px.
- **Grids**: contributions and resources 4 columns, gap 0.85rem; bald comparisons 3 columns, gap 1rem; collages 2 columns, gap 0.9rem; stat list auto-fit min 11.5rem, gap 0.75rem, max 780px.
- **Timeline rows**: 7rem date column + text, gap 1.2rem, padding 1rem 0, 1px #d8ddd6 rules.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1120px | 32px | 17px | 140px | 4-column cards, 3-column comparisons |
| ≤1120px | 32px | 17px | 140px | contribution/resource grids 2 columns; comparisons 2 columns; `.two-column` stacks |
| ≤920px | 32px | 17px | 140px | nav collapses to a 40px hamburger with a white dropdown; split and citation layouts stack; sticky aside released |
| ≤700px | 28px (4vw) | 16px | 85.6px (5.35rem) | subtitle 28px, h2 39.2px; buttons full width; all card grids 1 column; timeline stacks |
| ≤460px | 8px each side (100% − 1rem) | 16px | 65.6px (4.1rem) | subtitle 23.2px, h2 33.6px; section padding 54.4px |

## Components

- **Venue pill** (`.paper-kicker`): inline-flex, #ffffff, 1px #d8ddd6, radius 999px, padding 0.45rem 0.75rem, 12.48px/800 uppercase #183f3b, letter-spacing 0.11em; leading 0.45rem #9a6b25 dot, gap 0.55rem.
- **Button** (`.button`): inline-flex, min-height 2.7rem, padding 0.62rem 0.95rem, 1px #bbc4bb border, 6px radius, #ffffff, 14.72px/750 #171817, line-height 1, 16px stroke icon left with 0.48rem gap. Hover: translateY(-1px), border #23615a, background #fbfcfb, small shadow, text #183f3b. Primary: #18211f fill and border, white text; hover #183f3b. Unavailable: dashed border, transparent, #616761, no hover.
- **Eyebrow kicker** (`.eyebrow`): 11.84px/850 uppercase #183f3b, letter-spacing 0.14em, preceded by a 2.25rem × 1px rule in currentColor, gap 0.65rem, margin-bottom 0.85rem.
- **Contribution card** (`.contribution-card`): #ffffff, 1px #d8ddd6, 8px radius, padding 1.1rem; JetBrains Mono "01" index 12.48px/700 #9a6b25; serif h3 21.6px/650; body 14.88px #616761.
- **Result carousel**: header row with an 13.12px/850 uppercase label and a pill slide counter (1px #bbc4bb, 999px, 12.8px/800 #454b46); slides are 3:2 images in 8px frames with the large shadow; 48px round white arrows at 1rem from the edges, hover #18211f with white icon and scale 1.04; corner pill labels 10.56px/850 uppercase, "Result" label inverted to #18211f.
- **Before/after slider** (`.comparison-view`): square, #0d0f0e ground, 2px white divider, 36px #18211f knob with a 2px white ring and white centre dot, shadow `0 8px 24px rgba(23,24,23,0.28)`; native range input below in #23615a.
- **Resource card** (`.resource-card`): #ffffff, 1px #bbc4bb, 8px radius, padding 1.1rem, small shadow; #e4efec tag pill (10.88px/850 uppercase #183f3b); serif title 22.08px/650; hover lifts 2px, border #23615a, larger shadow, arrow icon nudges up-right.
- **Citation band** (`.citation-section`): `background: linear-gradient(180deg, var(--paper-dark-2), var(--paper-dark))`, white h2, text rgba(255,255,255,0.74); BibTeX box rgba(0,0,0,0.26) with a label bar and a translucent copy button.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky nav with scroll-spy | yes | blurred translucent paper bar, monogram brand, mint hover/active chips |
| Venue badge | yes | white pill with gold dot |
| Title / subtitle / authors | yes | 140px serif wordmark, 39.2px serif subtitle, dot-separated author line |
| Affiliations | absent from the source | only abbreviated author names |
| TL;DR / summary | yes | 16.96px muted paragraph under the authors |
| Link buttons | yes | 6px-radius white buttons with line icons, one dark primary, one dashed placeholder |
| Teaser | yes | full-width 8px frame with large soft shadow and caption strip |
| Abstract | yes | split layout, sticky serif heading left, serif body right, "Read full abstract" toggle |
| Method figure + contribution cards | yes | framed pipeline figure and four numbered cards |
| Results carousels / comparison sliders | yes | carousel with pill labels; 3-up before/after sliders; 2-up collages |
| Stats | yes | small white tiles with serif numbers |
| Code / resources | yes | four resource cards on the toned band |
| Video | present but non-standard | only a dashed "Video coming soon" button |
| News | yes | ruled timeline with uppercase green dates |
| BibTeX | yes | dark gradient band with mono code box and copy button |
| Footer | yes | #101412 with serif brand, venue pill and link row |

## Adapting to Other Content

- **More authors**: keep the dot-separated 15.68px #454b46 line; at more than six names let it wrap to a second centred line, and put affiliations as a 14.4px #616761 line below it, still above the 760px summary.
- **A results table**: place it in a `.figure-frame` (white, 1px #bbc4bb, 8px radius, small shadow); header row 13.12px/850 uppercase #171817 on #f0f2ee, body 16px Inter, 1px #d8ddd6 row rules, best value 700 #183f3b.
- **Long publication or news lists**: reuse `.timeline` rows (7rem date column, 0.82rem/850 #183f3b dates, 1px #d8ddd6 rules).
- **More metrics**: extend `.stat-list` tiles (serif 23.2px/650 numbers, 13.12px/800 #616761 labels); they auto-fit at min 184px.
- **Extra sections**: alternate plain #f7f7f4 and toned #f0f2ee bands at 108px vertical padding, each opening with an eyebrow kicker and a 53.6px serif h2.

## Do's and Don'ts

- Do let the 140px serif wordmark be the only large element in the hero; everything around it stays 12–17px Inter except the 39.2px subtitle.
- Do keep accents low-chroma: forest green for text and hover states, gold only for the pill dot and indices.
- Do use 6px radii on controls and 8px on figures and cards; reserve 999px for pills and labels.
- Do frame every figure with a 1px #bbc4bb border and the soft two-layer shadow.
- Don't use colored fills for buttons other than the single #18211f primary.
- Don't center section body text; section headings and copy are left-aligned within 1180px.
- Don't drop the faint fixed grid texture; it is what keeps the off-white from looking flat.

## Surfaces

Warm paper #f7f7f4 with a fixed 56px hairline grid fading out downward; white #ffffff for every card, button, frame and caption strip; toned bands in #f0f2ee bounded by 1px #d8ddd6 rules; a dark citation band using `linear-gradient(180deg, #22312f, #18211f)` and a #101412 footer close the page.

## Imagery

Photographic face and hairstyle composites: the teaser is a 2×3 grid of face/hair/result triplets with vertical serif "Face"/"Hair" labels on white, celebrity and generated portraits in natural colour. Method uses a light pipeline diagram with pastel boxes; results are 3:2 slides and square before/after sliders. All images sit inside white 8px frames; no rounding on the photos themselves beyond the frame.

## Layout

Centred hero at 980px inside a 1360px wide frame, then left-aligned 1180px sections. The Abstract is a 42/58 split with a sticky heading; Method and Results stack a heading block, a framed figure and card grids; toned bands alternate with plain ones; the page closes with news, the dark citation band and footer. About 9,750px tall at 1440.

## Agent Prompt Guide

Quick colors: page #f7f7f4, surface #ffffff, toned band #f0f2ee, ink #171817, soft ink #343735, muted #616761, lines #d8ddd6 / #bbc4bb, accent #183f3b (hover #23615a, wash #e4efec), gold #9a6b25, dark #18211f.

1. "Build a centred hero on #f7f7f4: a white pill (1px #d8ddd6, radius 999px, padding 0.45rem 0.75rem) with a 7px #9a6b25 dot and 'ACM SIGGRAPH 2026' in Inter 12.48px/800 uppercase #183f3b, letter-spacing 0.11em; below it the paper name in Source Serif 4 140px/600, line-height 0.86, #171817; subtitle Source Serif 4 39.2px/500 #343735, max-width 900px; authors 15.68px #454b46 separated by 3.5px #bbc4bb dots."
2. "Make a button row, gap 0.55rem: each button inline-flex, padding 0.62rem 0.95rem, min-height 2.7rem, 1px #bbc4bb border, radius 6px, #ffffff, Inter 14.72px/750 #171817 with a 16px line icon; hover translateY(-1px), border #23615a, text #183f3b. The first button is #18211f with white text."
3. "Create a split abstract section with 108px vertical padding: left column 0.42fr with an eyebrow (11.84px/850 uppercase #183f3b, letter-spacing 0.14em, a 36px 1px rule before) and a Source Serif 4 53.6px/600 h2; right column 0.58fr with Source Serif 4 18.56px/1.72 #343735 paragraphs and a small white 6px-radius 'Read full abstract' toggle."

## Similar Pages

- Hand-built editorial project pages that pair a large serif wordmark with an Inter UI layer and a sticky scroll-spy header.
- Pages that use a single deep-green accent and gold detailing on a warm off-white ground, closer to a journal site than a Bulma template.

## Quick Start

```css
:root {
  --bg: #f7f7f4;
  --surface: #ffffff;
  --surface-alt: #f0f2ee;
  --ink: #171817;
  --ink-soft: #343735;
  --muted: #616761;
  --muted-strong: #454b46;
  --line: #d8ddd6;
  --line-strong: #bbc4bb;
  --accent: #23615a;
  --accent-dark: #183f3b;
  --accent-soft: #e4efec;
  --gold: #9a6b25;
  --paper-dark: #18211f;
  --font-serif: "Source Serif 4", "Iowan Old Style", Georgia, serif;
  --font-sans: "Inter", ui-sans-serif, system-ui, sans-serif;
  --font-mono: "JetBrains Mono", Menlo, Consolas, monospace;
  --max: 1180px;
  --max-wide: 1360px;
  --gutter: clamp(1rem, 4vw, 2rem);
  --radius-sm: 6px;
  --radius-md: 8px;
  --shadow-sm: 0 1px 2px rgba(23, 24, 23, 0.04), 0 12px 30px rgba(23, 24, 23, 0.07);
  --shadow-md: 0 2px 4px rgba(23, 24, 23, 0.06), 0 24px 60px rgba(23, 24, 23, 0.10);
}
```

## Provenance

- **URL**: https://deepmancer.github.io/HairPort/
- **Paper**: HairPort: In-context 3D-aware Hair Import and Transfer for Images (arXiv 2606.12562), Alireza Heidari, A. Alimohammadi, A. Mahdavi-Amiri.
- **Venue**: SIGGRAPH 2026.
- **Selection reason**: the arXiv comment states acceptance at SIGGRAPH 2026 and links this project page.
- **Template credit**: none stated; a custom build (`assets/site.css` header reads "Formal academic visual system with restrained color and robust media").
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and tall screenshots, and the page's `site.css` and `index.html` read directly, on 2026-10-28.
