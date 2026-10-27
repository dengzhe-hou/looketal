# StreamAvatar — Style Reference

> A night-ocean masthead in serif type, lit by a single glowing orange buoy.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, and a DOM probe of the hero and repeated components), the 1440×900 and full-page screenshots, and the page's own `style.css` read directly. The page loads Source Serif 4 (400/600/700) and JetBrains Mono 400 from Google Fonts plus Academicons; every text element renders in Source Serif 4. Most sizes are `clamp()` expressions, so the desktop values below are the clamp maxima.

## Overview

A hand-built single-file page with a "Deep Ocean" token set. A thin #0f2942 top bar carries two outlined ghost buttons (Home, More Research with a hover dropdown). Below it a 703px hero runs a 135° navy gradient (#0f2942 → #1a365d → #2c5282) with a faint orange radial glow at the top left. Everything in it is centred white serif: a 72px bold "StreamAvatar", a 24px subtitle, an orange gradient "CVPR 2026" pill with a soft orange halo, two lines of 17.6px author names (linked ones with a dashed underline), affiliations and notes at falling opacity, and two 55px buttons (solid orange arXiv, glassy outlined BibTeX). The body switches to a pale blue-grey page (#f7fafc): a 1136px teaser figure with a 12px radius and deep soft shadow, a centred grey caption, then sections with 40px semibold navy titles underlined by a 60×4px orange gradient bar. Subsections use a 4px orange left rule. Video grids of 4 or 5 black rounded tiles, white result cards, a small metrics table and two orange-topped method cards follow; the page ends on a near-black BibTeX band and a navy footer. Orange (#ed8936) is the only accent.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): navy gradient tones #274771 17.9%, #1c385d 15.7%, #20406a 13.0%, #26364c 12.0%, #293a53 11.9%, #142e4b 9.6% (together about 80%); page #f6f9fb 15.4%; anti-aliased light text #748193 4.5%. The orange pill and button are too small to register as a cluster.

Anatomy in DOM order (desktop 1440px; hero container 1200px at x=120 with 32px side padding, content 1136px at x=152):

1. **Top bar** (`nav.topnav`, 0–51px): #0f2942, 1px rgba(255,255,255,0.1) bottom rule, items centred. "Home" and "More Research ⌄" ghost buttons, 15.2px/400 rgba(255,255,255,0.9), 41px tall, 16px apart.
2. **Hero** (`header.hero`, y=51–754): gradient, padding 128px 0 80px, text centred.
3. **Title** (`h1.title`, y=179, 122px line box): 72px/700, letter-spacing -1.44px, #ffffff, text-shadow 0 2px 10px rgba(0,0,0,0.2). Gap 8px.
4. **Subtitle** (`h2.subtitle`, y=309): 24px/400, line-height 36px, rgba(255,255,255,0.9), max-width 800px. Gap 32px.
5. **Venue pill** (`.venue-tag`, y=377, 141×41): "CVPR 2026", 15.2px uppercase, letter-spacing 2.74px (0.18em), white on an #ed8936 → #f6ad55 gradient, 999px radius, 1px rgba(255,255,255,0.4) border, glow `0 0 18px rgba(0,0,0,0.35), 0 0 24px rgba(237,137,54,0.65)`. Gap 24px.
6. **Authors** (`.authors`, y=442–508, two lines): 17.6px/400, line-height 31.68px; plain names rgba(255,255,255,0.9), linked names rgba(255,255,255,0.95) with a 1px dashed rgba(255,255,255,0.4) underline; numeric and symbol superscripts at 0.7em; 6.4px side margin per name. Gap 15px.
7. **Affiliations** (y=523): 15.2px rgba(255,255,255,0.75), four spans 24px apart. Gap 8px.
8. **Author notes** (y=560): 14.4px rgba(255,255,255,0.6). Gap 32px.
9. **Buttons** (`.links`, y=619, 55px tall, 16px gap): arXiv (solid #ed8936, Academicons icon left) and BibTeX (`</>` SVG icon, translucent white).
10. **Teaser** (`section.teaser`, y=754): #f7fafc, padding 96px; the teaser image starts at y=850, 1136×328, so only its top edge shows above the fold at 900px.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Abyss Navy | #0f2942 | --primary-dark | top bar, hero gradient start, footer |
| Ocean Navy | #1a365d | --primary | hero gradient middle, section titles (`h2.section-title`), method card h4, table header bottom rule |
| Harbor Blue | #2c5282 | --primary-light | hero gradient end, body links |
| Buoy Orange | #ed8936 | --accent | arXiv button, venue pill start, section-title bar start, subsection left rule, method card top rule, link hover, selection, focus outline |
| Glow Orange | #f6ad55 | --accent-light | venue pill end, section-title bar end, author link hover |
| Ember | #c05621 | --accent-dark | arXiv button hover fill and border |
| Mist Page | #f7fafc | --bg-primary | page background, teaser section, end of section gradients |
| Fog Band | #edf2f7 | --bg-secondary | start of the abstract / alt-bg vertical gradients, table header fill, "Show more samples" chip, table row hover |
| Ink | #1a202c | --text-primary | body text, subsection titles, abstract |
| Slate | #4a5568 | --text-secondary | teaser caption, section descriptions, method card text, summary chip text |
| Hairline | #e2e8f0 | --border | table row rules, result image borders |
| Night | #0f172a | --bg-dark | BibTeX section band |
| Code Grey | #a0aec0 | --text-light | BibTeX code text, BibTeX description |
| White glass | rgba(255,255,255,0.1) | (literal) | BibTeX button and copy button fill, top bar rule |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Serif (everything) | 'Source Serif 4', Georgia, 'Times New Roman', serif | Source Serif 4 400, 600, 700 (Google Fonts, opsz 8–60) | PT Serif |
| Mono | 'JetBrains Mono', 'Fira Code', monospace | JetBrains Mono 400 | Fira Code |
| Icons | Academicons | Academicons 400 (arXiv glyph); other icons are inline SVG | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Title | `.title` | clamp(2.5rem, 8vw, 4.5rem) = 72px / 700 / 1.7, letter-spacing -0.02em | #ffffff |
| Subtitle | `.subtitle` | clamp(1rem, 3vw, 1.5rem) = 24px / 400 / 1.5 | rgba(255,255,255,0.9) |
| Venue pill | `.venue-tag` | 0.95rem = 15.2px / 400, uppercase, letter-spacing 0.18em | #ffffff |
| Authors | `.authors` | 1.1rem = 17.6px / 400 / 1.8 | rgba(255,255,255,0.9) |
| Affiliations | `.affiliations` | 15.2px / 400 | rgba(255,255,255,0.75) |
| Author notes | `.author-notes` | 0.9rem = 14.4px | rgba(255,255,255,0.6) |
| Button | `.btn` | 1rem / 500 | #ffffff |
| Section title | `.section-title` | clamp(1.75rem, 4vw, 2.5rem) = 40px / 600 / 1.7 | #1a365d |
| Subsection title | `.subsection-title` | 1.35rem = 21.6px / 600 | #1a202c |
| Body | `body` | 1.0625rem = 17px / 400 / 1.7 | #1a202c |
| Abstract | `.abstract-content` | 1.1rem = 17.6px / 400 / 1.7, justified | #1a202c |
| Captions, descriptions | `.teaser-caption`, `.section-description` | 16px and 16.8px / 400 / 1.8, centred | #4a5568 |
| Method card heading | `.method-stage h4` | 1.15rem = 18.4px / 700 | #1a365d |
| Table | `.metrics-table` | 16px; header 600; first column 500 | #1a202c |
| BibTeX | `.bibtex-wrapper pre` | 0.875rem = 14px / 400 / 1.6 JetBrains Mono | #a0aec0 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Venue pill | 999px | 1px rgba(255,255,255,0.4) | 0 0 18px rgba(0,0,0,0.35), 0 0 24px rgba(237,137,54,0.65) |
| Hero buttons | 8px | 2px #ed8936 (arXiv) / 2px rgba(255,255,255,0.3) (BibTeX) | none at rest; arXiv hover `--shadow-lg` |
| Nav ghost buttons, copy button, summary chip | 6px | 1px rgba(255,255,255,0.2) (nav, copy); none (chip) | none |
| Teaser image | 12px | none | `--shadow-xl` 0 20px 25px rgba(0,0,0,0.1), 0 10px 10px rgba(0,0,0,0.04) |
| Video tiles | 8px | none | `--shadow-md` 0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.05) |
| Result cards, pipeline/method figure | 12px | none | `--shadow-md` (pipeline wrapper `--shadow-lg` 0 10px 15px rgba(0,0,0,0.1), 0 4px 6px rgba(0,0,0,0.05)) |
| Method stage cards | 10px | 4px #ed8936 top | `--shadow-md` |
| Section-title bar | 2px | none | none; 60×4px gradient #ed8936 → #f6ad55, 12px below the title |
| Subsection title | 0 | 4px #ed8936 left, 16px padding-left | none |
| BibTeX pre | 10px | 1px rgba(255,255,255,0.1) | none |

Hover lift is a shared motif: video tiles, result cards, method cards and figures rise 4px (`translateY(-4px)`) and take `--shadow-xl`; buttons rise 2px. Transitions are 150ms / 250ms ease.

## Layout Metrics

- **Container**: `.container { max-width: 1200px; margin: 0 auto; padding: 0 clamp(1rem, 4vw, 2rem) }`, content 1136px at x=152 on a 1440 viewport.
- **Top bar**: 50px tall plus a 1px rule, items centred, 16px gap.
- **Hero**: padding clamp(4rem, 12vw, 8rem) top (128px) and clamp(3rem, 8vw, 5rem) bottom (80px); total height 703px at 1440.
- **Sections**: `section { padding: clamp(3rem, 8vw, 6rem) 0 }` = 96px top and bottom; subsections 48px apart.
- **Measures**: subtitle 800px, authors 900px, teaser caption 900px, abstract 850px (justified), section description 800px, BibTeX 700px.
- **Figures and video**: teaser full 1136px; YouTube demo in `.main-video` at max-width 900px, 16:9; comparison videos 1000px; result cards stacked in a 900px column with 32px gaps.
- **Grids**: `.video-grid` gap 16px; `.grid-4` tiles 272px wide at 1440; `.grid-5` and `.grid-3` used for other sample sets; method details two columns with 32px gap.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1200px | (100% − 1136px)/2 | 17px | 72px (section 40px) | grid-5 / grid-4 / grid-3 as authored; method 2 columns |
| ≤1024px | 32px (4vw floors at 2rem until 800px) | 17px | 72px until 900px, then 8vw | grid-5 → 3 columns, grid-4 → 2 |
| ≤900px | 4vw | 17px | 8vw | results-grid → 1 column |
| ≤768px | 4vw (about 30px) | 17px | 8vw (61px at 768) | grid-5/4/3 → 2 columns, grid-2 → 1; method details → 1 column |
| ≤480px | 16px | 17px | 40px floor (section 28px) | all video grids → 1 column |

## Components

- **Top-bar ghost button** (`.nav-link`, `.dropdown-toggle`): transparent, 1px rgba(255,255,255,0.2) border, 6px radius, padding 8px 16px, 15.2px serif rgba(255,255,255,0.9); hover fill rgba(255,255,255,0.1) and border 0.3. The dropdown opens on hover as a white 180px menu, 8px radius, `--shadow-xl`, rows 12px 16px with #edf2f7 hairlines; its chevron rotates 180°.
- **Venue pill** (`.venue-tag`): inline-block, padding 6.4px 19.2px, 999px radius, #ed8936 → #f6ad55 horizontal gradient, 1px rgba(255,255,255,0.4) border, white 15.2px uppercase with 0.18em tracking, orange halo shadow; hover lifts 4px and the halo grows to 0 0 32px rgba(237,137,54,0.8).
- **Primary button** (`.btn-primary`): inline-flex, gap 8px, padding 12px 24px, 8px radius, 2px #ed8936 border and fill, white 16px/500, Academicons arXiv icon left; hover #c05621 fill and border, lift 2px, `--shadow-lg`.
- **Glass button** (`.btn-secondary`): rgba(255,255,255,0.1) fill, 2px rgba(255,255,255,0.3) border, backdrop-filter blur(10px), white text, SVG icon left; hover fill 0.2, border 0.5, lift 2px.
- **Section title** (`.section-title`): centred 40px/600 #1a365d with a 60×4px #ed8936 → #f6ad55 bar, 2px radius, 12px below; 16px margin to the next item.
- **Subsection title** (`.subsection-title`): left-aligned 21.6px/600 #1a202c, 4px #ed8936 left rule, 16px padding-left, 12px margin below.
- **Video tile** (`.video-item`): black, 8px radius, `--shadow-md`, video fills it; hover lifts 4px with `--shadow-xl` and fades in a bottom 30% black gradient.
- **More-samples disclosure** (`details.more-samples summary`): #edf2f7 chip, 6px radius, padding 8px 16px, 15.2px #4a5568 with a "▶" that rotates 90° when open; hover #e2e8f0 and #1a202c.
- **Result card** (`.result-card`): white, 12px radius, padding 24px, `--shadow-md`, centred 21.6px title without the left rule, 15.2px #4a5568 description, image with 8px radius and 1px #e2e8f0 border.
- **Metrics table** (`.metrics-table`): max-width 400px, centred, cells 12px 24px, 1px #e2e8f0 row rules; header #edf2f7 fill, 600 weight, 2px #1a365d bottom rule; row hover #edf2f7.
- **Method stage card** (`.method-stage`): white, 10px radius, padding 24px, 4px #ed8936 top border, `--shadow-md`; h4 18.4px #1a365d; text 15.2px #4a5568.
- **BibTeX block**: #0f172a section with a white section title; `pre` at 700px, rgba(255,255,255,0.05) fill, 1px rgba(255,255,255,0.1) border, 10px radius, 24px padding, 14px JetBrains Mono #a0aec0; copy button absolutely placed 12px from the top right.
- **Footer**: #0f2942, padding 32px 0, centred 15.2px rgba(255,255,255,0.7).

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top navigation | yes | dark bar with two outlined ghost buttons and a hover dropdown to other projects |
| Title / subtitle | yes | 72px white serif name over a 24px descriptive subtitle |
| Venue badge | yes | glowing orange gradient pill |
| Authors / affiliations | yes | two centred lines, dashed-underline links, numeric and symbol superscripts, notes line |
| Link buttons | yes | two only: solid orange arXiv and glass BibTeX; no code or data button |
| Teaser | yes | wide figure with 12px radius and deep shadow, centred grey caption |
| Abstract | yes | 850px justified text on a #edf2f7 → #f7fafc gradient band |
| Demo video | yes | YouTube iframe at 900px |
| Qualitative results | yes | 4- and 5-column black video tile grids under orange-ruled subsections, with "Show more samples" disclosures |
| Comparisons | yes | wide comparison videos at 1000px |
| Results tables | present but non-standard | results are mostly figure images in white cards; one small HTML table for inference speed |
| Method | yes | pipeline figure card plus two orange-topped stage cards |
| BibTeX | yes | dark band with a copy button |
| Footer | yes | navy, centred |

## Adapting to Other Content

- **More authors**: keep the centred 17.6px line-height 1.8 block; it wraps to as many lines as needed inside the 900px measure. Add the affiliation and notes lines below at the same falling opacities (0.75, 0.6).
- **More buttons** (Code, Data, Demo): reuse `.btn-secondary` for all but the single most important link, which stays solid #ed8936; keep the 16px flex gap and let the row wrap.
- **A larger results table**: widen `.metrics-table` to the 900px result column, keep the #edf2f7 header with the 2px #1a365d rule and 1px #e2e8f0 row rules, and wrap it in a `.result-card`. Mark best values in 600 weight rather than colour.
- **Long publication or news lists**: put them in a white `.result-card` column at 900px, each item a 17px line with a 15.2px #4a5568 date, separated by 1px #e2e8f0 rules; use a subsection title with the orange left rule as the group header.
- **Light sections in alternation**: alternate plain #f7fafc sections with `.alt-bg` gradient bands; do not introduce a second accent.

## Do's and Don'ts

- Do set every line in Source Serif 4; weight (400/600/700) and the clamp scale carry the hierarchy.
- Do keep the hero navy gradient and white type; orange appears only on the pill, the primary button, title bars and rules.
- Do use the 4px hover lift with `--shadow-xl` on every card and video tile.
- Don't add a second accent hue; hovers move orange to #c05621 or #f6ad55.
- Don't left-align section titles; they are centred with the 60px orange bar.
- Don't put text directly on black video tiles; labels go in the subsection title above.

## Surfaces

Navy hero and top bar (#0f2942 → #2c5282), pale page #f7fafc, alternating #edf2f7 → #f7fafc vertical gradient bands, white raised cards, a near-black #0f172a BibTeX band and a navy footer.

## Imagery

A wide schematic teaser (non-causal model → two-stage adaptation → causal model, with photo frames of a singer), many short talking and listening avatar video clips in black tiles, comparison videos, result figure images, and a pipeline diagram. Photographic people on dark studio backgrounds dominate below the fold.

## Layout

Full-width bands with a 1200px container: top bar, navy hero, teaser, abstract band, demo video, three results sections, method band, BibTeX band, footer. About 13,900px tall at 1440 wide, with 46 videos.

## Agent Prompt Guide

Quick colors: hero #0f2942 → #1a365d → #2c5282, accent #ed8936 (hover #c05621, light #f6ad55), page #f7fafc, band #edf2f7, ink #1a202c, secondary #4a5568, hairline #e2e8f0, BibTeX band #0f172a.

1. "Build a navy hero: background linear-gradient(135deg, #0f2942 0%, #1a365d 50%, #2c5282 100%), padding 128px 0 80px, centred. Title Source Serif 4 72px/700, letter-spacing -0.02em, #ffffff, text-shadow 0 2px 10px rgba(0,0,0,0.2); subtitle 24px/400 rgba(255,255,255,0.9), max-width 800px, 32px below; then a venue pill: padding 6.4px 19.2px, 999px radius, linear-gradient(90deg, #ed8936, #f6ad55), 1px rgba(255,255,255,0.4) border, 15.2px uppercase white, letter-spacing 0.18em, box-shadow 0 0 18px rgba(0,0,0,0.35), 0 0 24px rgba(237,137,54,0.65)."
2. "Make two hero buttons 16px apart: padding 12px 24px, 8px radius, Source Serif 4 16px/500, icon left with 8px gap. Primary: #ed8936 fill and 2px border, white text; hover #c05621, translateY(-2px). Secondary: rgba(255,255,255,0.1) fill, 2px rgba(255,255,255,0.3) border, backdrop-filter blur(10px), white text."
3. "Create a section title: centred Source Serif 4 40px/600 #1a365d, followed by a 60×4px bar with linear-gradient(90deg, #ed8936, #f6ad55), 2px radius, 12px above it; subsections below use 21.6px/600 #1a202c with a 4px #ed8936 left border and 16px padding-left."

## Similar Pages

- Hand-built project pages with a saturated gradient hero and a light body, rather than Bulma/Nerfies templates.
- Avatar and talking-head project pages that lead with dense grids of short video clips.

## Quick Start

```css
:root {
  --primary: #1a365d;
  --primary-light: #2c5282;
  --primary-dark: #0f2942;
  --accent: #ed8936;
  --accent-light: #f6ad55;
  --accent-dark: #c05621;
  --bg-primary: #f7fafc;
  --bg-secondary: #edf2f7;
  --bg-dark: #0f172a;
  --text-primary: #1a202c;
  --text-secondary: #4a5568;
  --text-light: #a0aec0;
  --border: #e2e8f0;
  --shadow-md: 0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.05);
  --shadow-xl: 0 20px 25px rgba(0,0,0,0.1), 0 10px 10px rgba(0,0,0,0.04);
  --section-padding: clamp(3rem, 8vw, 6rem);
  --container-max: 1200px;
  --font-serif: 'Source Serif 4', Georgia, 'Times New Roman', serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
}
body { font: 1.0625rem/1.7 var(--font-serif); color: var(--text-primary); background: var(--bg-primary); }
.container { max-width: var(--container-max); margin: 0 auto; padding: 0 clamp(1rem, 4vw, 2rem); }
```

## Provenance

- **URL**: https://streamavatar.github.io/
- **Paper**: StreamAvatar: Streaming Diffusion Models for Real-Time Interactive Human Avatars (arXiv 2512.22065), Zhiyao Sun et al.
- **Venue**: CVPR 2026.
- **Selection reason**: the arXiv comment states acceptance at CVPR 2026 and links this page.
- **Template credit**: none credited; a single custom `style.css` ("StreamAvatar - Academic Project Website", Deep Ocean palette).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), a DOM probe of the hero and repeated components, the 1440×900 and full-page screenshots, and `style.css` and `index.html` read directly, on 2026-10-28.
