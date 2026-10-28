# Forge — Style Reference

> A warm foundry floor: cream paper, ink-navy serif, and the letters F-O-R-G-E struck in hot brick red.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of the rendered elements and pseudo-elements, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's single inline `<style>` block (18 KB) and markup in `index.html`. Font Awesome 6 supplies the icons. The hero children fade up on load (0.6s, staggered 0.08s), so values were read after the animation had finished. There is no dark mode.

## Overview

A mid-length (4,707px) project page on warm off-white #faf9f7 with ink-navy text #1a1a2e. Headings are DM Serif Display (synthesised bold, since only the 400 face loads) and text is Source Sans 3, with JetBrains Mono for the brand, the eyebrow pill, step numbers and install chip. The identity comes from the title, where "Forge:" and the initials F, O, R, G, E of "Foundational Optimization Representations from Graph Embeddings" are filled with a 135deg brick-red gradient (#c0392b → #e74c3c) through `background-clip: text`, an acrostic that spells the name. A sticky translucent top bar carries the mono "Forge" brand and four uppercase links. The hero is a cream gradient band with a red-tinted eyebrow pill, the acrostic title, a light grey subtitle, authors, a row of seven 8px-radius buttons (one navy, six white with colored icons), an "INSTALL pip install forge-mip" chip and a pepy downloads badge. Below, sections are centred serif titles with a 40×3px red underline: a white overview card, four "STEP n" cards, a YouTube talk, resource cards with colored left strips, a navy BibTeX block and acknowledgments.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): the warm cream family #f8f4f0 19.6%, #f3f1eb 19.5%, #fbfaf8 15.1%, #f7f3ef 14.1%, #f7f2ee 10.3%, #f9f5f2 9.2%, #f6f3ee 5.7% (together 93.5%, the hero gradient and page ground); greyish #c9c2c1 6.5% (anti-aliased navy and grey text, button borders). Red and navy fill too little area to form their own clusters.

Anatomy in DOM order (desktop 1440px, everything centred):

1. **Sticky nav** (`nav`, 0–57px): 56px bar plus 1px #e2ddd5 bottom border, background rgba(250,249,247,0.85) with `backdrop-filter: blur(16px)`; inner max-width 1080px with 32px padding (content x=212–1228). Left "Forge" in JetBrains Mono 13.6px/500, letter-spacing 0.408px, #c0392b; right OVERVIEW / VIDEO / RESOURCES / CITATION in Source Sans 3 13.12px/500 uppercase, letter-spacing 0.26px, #6b7280, 28px apart.
2. **Hero band** (`header.hero`, y=57–834): padding 80px 32px 64px, background `linear-gradient(175deg, var(--paper) 0%, var(--warm) 100%)` (#faf9f7 → #f5f0ea) with a `::before` overlay `radial-gradient(ellipse 80% 60% at 50% 0%, rgba(192,57,43,0.04), transparent), radial-gradient(ellipse 60% 50% at 80% 100%, rgba(22,160,133,0.04), transparent)`; `.hero-inner` max-width 820px (x=310–1130).
3. **Eyebrow pill** (`.hero-label`, y=137, 31px tall): "REPRESENTATION LEARNING FOR COMBINATORIAL OPTIMIZATION", JetBrains Mono 11.52px/500 uppercase, letter-spacing 1.38px (0.12em), #c0392b on rgba(192,57,43,0.07), padding 5.6px 16px, radius 100px; margin-bottom 24px.
4. **Title** (`h1`, y=192, 188px tall): DM Serif Display 54.4px/700 (synthesised), line-height 1.15, letter-spacing -0.544px, #1a1a2e, three lines; acrostic spans filled with `linear-gradient(135deg, var(--accent) 0%, var(--accent-soft) 100%)`; margin-bottom 12px.
5. **Subtitle** (`p.subtitle`, y=391): Source Sans 3 18.4px/300, line-height 1.7, #6b7280, max-width 640px, four lines; margin-bottom 24px.
6. **Authors** (y=541): 16.8px, names 500 #1a1a2e with a 1px dashed #e2ddd5 bottom border (hover #c0392b); superscripts; margin-bottom 4.8px.
7. **Affiliations** (y=577): 14.08px #6b7280, three inline-block spans with 8px side margins; margin-bottom 32px.
8. **Button row** (`.hero-buttons`, y=636, 45px tall): TMLR'26 (navy primary, file icon), Code (GitHub icon), Slides (red PowerPoint icon), 🤗 Models, Dataset (blue database icon), Demo (teal rocket icon), BibTeX (chevron, toggles an inline code block); 12px gaps.
9. **Install chip** (`.install-command`, y=697, 16px below): white, 1px #e2ddd5, radius 8px, padding 7.2px 10.4px; red mono "INSTALL" label then `pip install forge-mip` in JetBrains Mono 13.44px #1a1a2e.
10. **Downloads badge** (y=748, 9.6px below): pepy.tech image 22px tall, grey "Downloads" and orange "1k", radius 4px. The hero ends 64px later at y=834.

"Overview" starts at y=898, just inside the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #faf9f7 | --paper | page background, nav (85% alpha), hero gradient start, resource link chips |
| Warm | #f5f0ea | --warm | hero gradient end, models panel inside resource card |
| Ink | #1a1a2e | --ink | body text, h1, h2, h3, author names, primary button fill, BibTeX block background, tooltip |
| Ink Hover | #2c2c4a | (literal) | primary button hover fill |
| Brick Red | #c0392b | --accent | "Forge" brand, eyebrow pill text, acrostic gradient start, h2 underline bar, STEP labels, INSTALL label, MODELS tag, Slides icon |
| Coral Red | #e74c3c | --accent-soft | acrostic gradient end |
| Red Tint | rgba(192,57,43,0.07) | (literal) | eyebrow pill and red card-tag fill (INSTALL label uses 0.08) |
| Teal | #16a085 | --teal | Demo rocket icon, TRANSFER LEARNING tag and card strip, model-chip hover border |
| Blue | #2471a3 | --blue | Dataset database icon, blue card strip variant |
| Gold | #d4a017 | --gold | gold card strip variant (declared for a third card type) |
| Muted | #6b7280 | --muted | nav links, subtitle, affiliations, section sub-lines, step descriptions, card descriptions and author lines, footer |
| Body Grey | #374151 | (literal) | overview card text |
| Border | #e2ddd5 | --border | nav bottom border, outline buttons, install chip, cards, dividers, author dashed underline, footer top border |
| Card White | #ffffff | --card-bg | outline buttons, install chip, overview card, step cards, resource cards, model chips |
| Code Text | #e2e8f0 | (literal) | BibTeX text and copy button text |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display / headings | 'DM Serif Display', Georgia, serif | DM Serif Display 400 only; h1–h3 render at 700 as synthesised bold | Abril Text |
| Text | 'Source Sans 3', 'Segoe UI', sans-serif | Source Sans 3 300, 400, 400 italic, 500, 600, 700 | Source Sans Pro |
| Mono | 'JetBrains Mono', 'Fira Code', monospace | JetBrains Mono 400, 500 (BibTeX `pre` falls back to plain `monospace`) | Fira Code |
| Icons | Font Awesome 6 | Font Awesome 6 Free 900, Brands 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.hero h1` | clamp(2.2rem, 5vw, 3.4rem) → 54.4px / 700 / 1.15, letter-spacing -0.01em | #1a1a2e; acrostic spans red gradient |
| Section title | `.section-header h2` | 32px / 700 / 54.4px, centred, inline-block | #1a1a2e |
| Card title | `.card-header-row h3` | 24.8px / 700 / 1.3 | #1a1a2e |
| Step title | `.pipe-step h3` | 17.6px / 700 / 29.92px | #1a1a2e |
| Body | `body` | 17px / 400 / 1.7 | #1a1a2e |
| Hero subtitle | `.hero .subtitle` | 18.4px / 300 / 1.7 | #6b7280 |
| Section sub-line | `.section-header p` | 16px / 400 / 1.7, max 600px | #6b7280 |
| Overview card | `.abstract-box` | 15.68px / 400 / 1.85; `strong` 700 | #374151 |
| Authors | `.hero .authors` | 16.8px; names 500 | #1a1a2e |
| Affiliations | `.hero .affiliation` | 14.08px / 400 | #6b7280 |
| Button | `.btn` | 14.08px / 600 / 1.7 | primary #ffffff, outline #1a1a2e |
| Nav brand | `.nav-brand` | JetBrains Mono 13.6px / 500, letter-spacing 0.03em | #c0392b |
| Nav link | `.nav-links a` | 13.12px / 500 uppercase, letter-spacing 0.02em | #6b7280 |
| Eyebrow pill | `.hero-label` | JetBrains Mono 11.52px / 500 uppercase, letter-spacing 0.12em | #c0392b |
| Step label | `.pipe-step .step-num` | JetBrains Mono 11.2px / 500 uppercase, letter-spacing 0.08em | #c0392b |
| Step text | `.pipe-step p` | 13.6px / 400 / 1.55 | #6b7280 |
| Card tag | `.card-tag` | JetBrains Mono 10.88px / 500 uppercase, letter-spacing 0.08em | per color |
| Card author line | `.card-venue` | 13.12px italic | #6b7280 |
| BibTeX | `.bibtex-block` | monospace 12.48px / 1.8 | #e2e8f0 |
| Footer | `footer` | 13.12px / 400 | #6b7280 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Hero buttons | 8px | primary 1px transparent (declared 1.5px, renders 1px); outline 1px #e2ddd5 | primary hover 0 4px 16px rgba(0,0,0,0.08); outline hover 0 1px 3px rgba(0,0,0,0.06) |
| Eyebrow pill | 100px | none | none |
| Install chip | 8px | 1px #e2ddd5 | none |
| Install / card tags | 4px | none | none |
| Overview card, step cards, resource cards | 10px | 1px #e2ddd5 | step hover 0 4px 16px rgba(0,0,0,0.08); resource card hover 0 12px 40px rgba(0,0,0,0.10) |
| Models panel | 10px | none | none |
| Model chip | 8px | 1px #e2ddd5 (hover #16a085) | hover 0 1px 3px rgba(0,0,0,0.06) |
| Card link chips | 6px | 1px #e2ddd5 (hover #1a1a2e) | none |
| Video embed | 10px | none | 0 4px 16px rgba(0,0,0,0.08) |
| BibTeX block | 10px | none; copy button 1px rgba(255,255,255,0.15), radius 5px | none |
| h2 underline bar | 2px | none | none |

## Layout Metrics

- **Containers**: nav inner and `section` both `max-width: 1080px; margin: 0 auto; padding: 0 32px` (sections `padding: 64px 32px`) → content x=212–1228 (1016px). Hero inner 820px (x=310); overview card, video and BibTeX 780px (x=330).
- **Hero**: 777px tall at 1440 (y=57–834); padding 80px 32px 64px; gaps eyebrow→title 24px, title→subtitle 12px, subtitle→authors 24px, authors→affiliations 4.8px, affiliations→buttons 32px, buttons→install 16px, install→badge 9.6px.
- **Section rhythm**: each section 64px top and bottom padding, separated by `.section-divider hr` (1px #e2ddd5 across 1016px); section header margin-bottom 48px; h2 underline 40×3px placed 9.6px below the text.
- **Steps**: `.pipeline-visual { grid-template-columns: repeat(4, 1fr); gap: 24px; margin-top: 32px }` → four 236px cards, padding 28px 20px.
- **Resource cards**: full 1016px; inner grid `5px 1fr` (colored strip + body), body padding 32px 36px; models panel padding 36px with chips in `repeat(auto-fill, minmax(240px, 1fr))`, gap 12px.
- **Video**: 780px wide, height from `padding-bottom: 43.9%` of the 1016px section → 446px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >768px (incl. 1440) | 32px | 17px | 54.4px (cap) | 4 step cards; nav links shown |
| ≤768px | 32px | 17px | 5vw (38.4px at 768) | steps 2 columns; nav links hidden; card body padding 24px; model chips 1 column |
| ≤704px | 32px | 17px | 35.2px floor (2.2rem) | — |
| ≤480px | 20px (sections 40px 20px; hero 48px 20px 40px) | 17px | 35.2px | steps 1 column |

## Components

- **Primary button** (`.btn-primary`): inline-flex, gap 8px, padding 9.6px 20.8px, radius 8px, #1a1a2e fill, white Source Sans 3 14.08px/600, leading Font Awesome icon in white; 45px tall. Hover: #2c2c4a, translateY(-1px), shadow 0 4px 16px rgba(0,0,0,0.08).
- **Outline button** (`.btn-outline`): same metrics, #ffffff fill, 1px #e2ddd5 border, #1a1a2e text; icons keep their own colors (Slides #c0392b, Dataset #2471a3, Demo #16a085, GitHub #1a1a2e, Models a 🤗 emoji). Hover: border #1a1a2e, translateY(-1px), shadow 0 1px 3px rgba(0,0,0,0.06).
- **Acrostic title**: wrap the brand word and each initial in `<span>` with `background: linear-gradient(135deg, #c0392b 0%, #e74c3c 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent`.
- **Eyebrow pill** (`.hero-label`): mono 11.52px/500 uppercase, 0.12em tracking, #c0392b on rgba(192,57,43,0.07), padding 5.6px 16px, radius 100px.
- **Install chip** (`.install-command`): white, 1px #e2ddd5, radius 8px, padding 7.2px 10.4px, gap 8.8px; label "INSTALL" mono 10.88px/500 uppercase #c0392b on rgba(192,57,43,0.08), radius 4px, padding 3.2px 7.2px; command mono 13.44px #1a1a2e.
- **Section header**: centred DM Serif Display 32px h2 with `::after` bar 40×3px #c0392b, radius 2px, 9.6px below; optional 16px #6b7280 sub-line 12px below; 48px to content.
- **Overview card** (`.abstract-box`): white, 1px #e2ddd5, radius 10px, padding 40px, max-width 780px, 15.68px/1.85 #374151 with bold leads and a bulleted list.
- **Step card** (`.pipe-step`): white, 1px #e2ddd5, radius 10px, padding 28px 20px, centred; "STEP n" mono red label, 28.8px emoji icon (📐 🧠 🎯 📊), 17.6px serif title, 13.6px #6b7280 text. Hover lifts 4px with 0 4px 16px rgba(0,0,0,0.08).
- **Resource card** (`.project-card`): white, 1px #e2ddd5, radius 10px, overflow hidden, 5px colored strip on the left (#c0392b, #16a085, #2471a3 or #d4a017); body has a tinted mono tag, a 24.8px serif title with a hover-revealed anchor link, a 15.2px #6b7280 description, an italic 13.12px author line and #faf9f7 link chips (radius 6px, 12.8px/600, padding 6.4px 13.6px). Hover lifts 3px with 0 12px 40px rgba(0,0,0,0.10).
- **BibTeX block** (`.bibtex-block`): #1a1a2e, radius 10px, padding 28px 32px, max 780px, monospace 12.48px/1.8 #e2e8f0; "Copy" button top-right at 12px, rgba(255,255,255,0.1) fill, 1px rgba(255,255,255,0.15) border, radius 5px, 11.52px.
- **Footer**: centred, padding 48px 32px, 13.12px #6b7280, 1px #e2ddd5 top border, underlined muted links.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky top nav | yes | translucent cream bar with blur, mono red brand, uppercase grey links |
| Eyebrow / topic pill | yes | red-tinted mono pill above the title |
| Title / authors / affiliations | yes | acrostic red-gradient initials, dashed-underlined names |
| Link buttons | yes | one navy primary and six white outline buttons with colored icons |
| Install snippet | yes | white chip with red INSTALL label |
| Downloads badge | yes | pepy.tech image under the install chip |
| TL;DR / subtitle | yes | 18.4px light grey subtitle in the hero |
| Abstract | present but non-standard | an "Overview" card with bullets instead of the paper abstract |
| How it works | yes | four numbered step cards with emoji icons |
| Teaser image / figures | absent from the source | no static figures; the talk video carries the visuals |
| Video | yes | 780px YouTube embed with 10px radius and soft shadow |
| Resource cards | yes | cards with colored left strips, tags, link chips and a models panel |
| Results tables | absent from the source | — |
| BibTeX | yes | dark navy block with translucent copy button; also an inline toggle in the hero |
| Acknowledgments | yes | centred section |
| Footer | yes | Apache license line and template credit |

## Adapting to Other Content

- **More authors**: keep one centred 16.8px line with dashed underlines and wrap it within the 820px hero inner; move extra affiliations into more inline-block spans at 14.08px #6b7280.
- **A results table**: put it in a white card like `.abstract-box` (1px #e2ddd5, radius 10px, padding 40px, max 780px); header cells JetBrains Mono 11.2px/500 uppercase #6b7280, body 15.68px #374151, best values 700 #1a1a2e with a rgba(192,57,43,0.07) cell fill; rows divided by 1px #e2ddd5.
- **Figures**: centre them at 780px inside a 10px-radius frame with the video's 0 4px 16px rgba(0,0,0,0.08) shadow; caption 13.6px #6b7280 below.
- **News or a publication list**: reuse the resource card at reduced scale: 5px colored strip by type, mono tag for the date (10.88px uppercase), 17.6px serif title, link chips.
- **A different acronym**: only colour letters that actually spell the name; everything else in the title stays #1a1a2e.

## Do's and Don'ts

- Do keep the page ground warm (#faf9f7) and the cards pure white with 1px #e2ddd5 borders.
- Do reserve the red gradient text for the acrostic and the brand word in the title.
- Do use JetBrains Mono for small labels (brand, eyebrow, STEP n, tags, INSTALL) and uppercase them.
- Do give every section title the 40×3px #c0392b bar.
- Don't fill outline buttons with color; only the first (venue) button is navy.
- Don't use teal, blue or gold for text; they appear only in icons, tags and card strips.
- Don't add heavy shadows at rest; shadows appear on hover and on the video.

## Surfaces

Cream page #faf9f7; a 175deg cream-to-warm hero band (#faf9f7 → #f5f0ea) with faint red and teal radial glows; white cards with hairline borders; a #f5f0ea models panel nested in a white card; one dark navy surface (#1a1a2e) for BibTeX.

## Imagery

Almost none. Emoji serve as step icons, Font Awesome glyphs as button icons, and a YouTube talk thumbnail (dark slide with neon green highlights) is the only large image. A pepy.tech shield sits under the install chip.

## Layout

Centred single column. A 1080px container with 32px padding holds a 777px hero, then sections separated by full-width hairlines: Overview (780px card), How it Works (4-up cards), Video (780px), Resources (full-width cards), Citation (780px dark block), Acknowledgments, footer.

## Agent Prompt Guide

Quick colors: paper #faf9f7, warm #f5f0ea, ink #1a1a2e, accent #c0392b → #e74c3c, muted #6b7280, border #e2ddd5, card #ffffff, teal #16a085, blue #2471a3.

1. "Build a centred hero band with background linear-gradient(175deg, #faf9f7 0%, #f5f0ea 100%), padding 80px 32px 64px, inner max-width 820px. Eyebrow pill: JetBrains Mono 11.52px/500 uppercase, letter-spacing 0.12em, #c0392b on rgba(192,57,43,0.07), padding 5.6px 16px, radius 100px. Title: DM Serif Display 54.4px bold, line-height 1.15, #1a1a2e, with the name's initials in spans filled by linear-gradient(135deg, #c0392b 0%, #e74c3c 100%) via background-clip: text. Subtitle 18.4px/300 #6b7280, max 640px."
2. "Create a button row (gap 12px, centred): buttons are 8px-radius, padding 9.6px 20.8px, Source Sans 3 14.08px/600 with a leading Font Awesome icon. First button #1a1a2e fill with white text; the rest #ffffff with a 1px #e2ddd5 border and #1a1a2e text, icons tinted #c0392b, #2471a3 or #16a085. Hover lifts 1px; outline hover border #1a1a2e."
3. "Make a 'How it works' row: four equal white cards (gap 24px), 1px #e2ddd5, radius 10px, padding 28px 20px, centred; a JetBrains Mono 11.2px uppercase #c0392b 'STEP n' label, a 28.8px emoji, a DM Serif Display 17.6px title and 13.6px #6b7280 text. Above, a centred 32px serif h2 with a 40×3px #c0392b bar 9.6px below."

## Similar Pages

- Hand-built single-file project pages with a warm paper palette, serif display titles and card sections, credited to the Academic Project Page Template but restyled.
- Library or toolkit landing pages that put a pip-install chip and download badge in the hero.

## Quick Start

```css
:root {
  --ink: #1a1a2e;
  --paper: #faf9f7;
  --warm: #f5f0ea;
  --accent: #c0392b;
  --accent-soft: #e74c3c;
  --teal: #16a085;
  --blue: #2471a3;
  --gold: #d4a017;
  --muted: #6b7280;
  --border: #e2ddd5;
  --card-bg: #ffffff;
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.06);
  --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 12px 40px rgba(0, 0, 0, 0.10);
  --radius: 10px;
  --serif: "DM Serif Display", Georgia, serif;
  --sans: "Source Sans 3", "Segoe UI", sans-serif;
  --mono: "JetBrains Mono", "Fira Code", monospace;
  --container: 1080px;
}
```

## Provenance

- **URL**: https://skadio.github.io/forge/
- **Paper**: Forge: Foundational Optimization Representations from Graph Embeddings, Serdar Kadıoğlu and Zohair Shafi (Brown University; Fidelity Investments AI Center of Excellence; Northeastern University).
- **Venue**: TMLR 2026 (OpenReview 7Uo1yRWUpo, June 2026).
- **Selection reason**: linked from the jmlr.org/tmlr/papers accepted list; curl returned 200 text/html.
- **Template credit**: footer reads "Built with the Academic Project Page Template" (eliahuhorwitz/Academic-project-page-template), but the styling is a fully custom inline sheet; Font Awesome 6 icons.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), additional computed-style probes of the hero pseudo-element, acrostic spans, buttons, install chip, section bars, cards, video, BibTeX and footer, the 1440×900 and full-page screenshots, and the inline stylesheet and markup of `index.html`, on 2026-10-28.
