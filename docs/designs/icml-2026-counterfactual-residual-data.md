# CRDA — Style Reference

> A well-kept lab notebook: serif headings, ruled pages, a raspberry tab on the cover and teal margin notes.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share) and the 1440×900 and full-page screenshots, cross-checked against the page's own `static/css/style.css` and `index.html`. The page has no framework; every value below is set by that one stylesheet, so the render and the CSS agree.

## Overview

A hand-written single-column page, centred at 920px, on pure white. Headings are Source Serif 4 at weight 600 in near-black navy (#14202b); text is Source Sans 3 at 17px in slate (#1f2933). Two accents do all the work: raspberry (#b13768) for the outlined "ICML 2026" pill, the stat numbers and best values in the comparison table, and teal (#1f6f8b) for links, superscripts, numbered step discs and the 3px left bars of equation and example callouts. The hero is centred; six charcoal pill buttons with stroke icons sit under the affiliations. Below a full-width hairline, the abstract sits in a pale grey box with a 10px radius. Each section is separated by a 1px #e6e9ec rule that spans the viewport. The bar chart in the TL;DR uses blue and magenta bars that echo the two accents.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): #ffffff 66.0%, near-whites #fbfcfc / #f9fafb / #feffff / #fafafa / #fffffd 20.7% (mostly the #fafbfc abstract box), #e2e4e5 7.8% (rules, box border, anti-aliased text), #81878d 5.5% (text and the charcoal buttons, averaged).

Anatomy in DOM order (all centred, container 920px including 24px padding, content x=284–1156):

1. **Venue pill** (`span.venue`, y=64, 28px tall): "ICML 2026", Source Sans 3 12.8px/600 uppercase, letter-spacing 0.12em, #b13768 text, 1px #b13768 border, 999px radius, padding 3px 12px. Gap 18px.
2. **Title** (`.hero h1`, y=110, two lines, 98px tall): Source Serif 4 41.6px/600, line-height 1.18, #14202b, centred. Gap 17px.
3. **Subtitle** (`p.subtitle`, y=225): Source Sans 3 16.8px/400, #5b6772. Gap 25px.
4. **Authors** (`p.authors`, y=277): 16.3px/400 #2c3a48, names as plain links in the same color, superscripts 0.72em #1f6f8b. Gap 9px.
5. **Affiliations** (`p.affiliations`, y=313): 14.7px #5b6772, numbered with #1f6f8b superscripts, items 0.6em apart. Gap 22px.
6. **Buttons** (`.actions`, y=361, 44px tall): Paper (PDF), arXiv, OpenReview, ICML Proceedings, Code (paper), pip install crda; gap 10px, centred, wrapping.
7. **Hero rule**: hero padding-bottom 40px, then a 1px #e6e9ec rule across the full viewport at y=446.
8. **Abstract box** (section padding 56px, box top y≈502): #fafbfc, 1px #e6e9ec, 10px radius, padding 24px 28px; "Abstract" h2 at 20px/600 serif, then 16px body text, which runs below the fold.

No teaser figure above the fold; the first image is the TL;DR bar chart at about y=1300.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper White | #ffffff | --bg | page background, stat cards, table body |
| Slate Ink | #1f2933 | --fg | body text, table text, button fill and border |
| Heading Navy | #14202b | (literal) | h1, h2, h3, bold text in steps and examples |
| Author Slate | #2c3a48 | (literal) | author names, button hover fill |
| Muted Gray | #5b6772 | --muted | subtitle, affiliations, figure captions, stat labels, footer |
| Teal | #1f6f8b | --accent | links, superscripts, step number discs, 3px callout and equation bars, inline code in prose |
| Raspberry | #b13768 | --accent-2 | venue pill text and border, stat card numbers, best values in comparison table |
| Hairline | #e6e9ec | --rule | section rules, box borders, table row lines, code borders |
| Box Fill | #fafbfc | (literal) | abstract box, equation blocks, example callouts, table dataset cells |
| Code Fill | #f6f8fa | --code-bg | BibTeX, code blocks, inline code, table header row |
| Header Rule | #c3cad1 | (literal) | 2px bottom border of table header |
| Peach Callout | #fdf7f0 | (literal) | pip package callout gradient top (to #fdf3ea) |
| Peach Border | #f0d7be | (literal) | pip package callout border |

The stylesheet also declares green/red result-cell colors (#d4ecd4, #fbcdcd) and a `.btn.placeholder` style (#6b7682 on transparent, #cdd4dc border); neither is used in the rendered page.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Serif (headings, stat numbers, equations) | "Source Serif 4", "Source Serif Pro", Georgia, serif | Source Serif 4 400/600 | Literata |
| Sans (body, UI) | "Source Sans 3", "Source Sans Pro", -apple-system, … Arial, sans-serif | Source Sans 3 400/500/600 | IBM Plex Sans |
| Mono (code) | "JetBrains Mono", "SF Mono", Menlo, … monospace | JetBrains Mono 400/500 | Fira Code |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.hero h1` | clamp(1.7rem, 4.2vw, 2.6rem) → 41.6px / 600 / 1.18 | #14202b |
| Section heading | `h2` | 1.75rem = 28px / 600 / 1.25, letter-spacing -0.005em | #14202b |
| Abstract heading | `.abstract h2` | 1.25rem = 20px / 600 | #14202b |
| Subsection | `h3` | 1.2rem = 19.2px / 600, margin-top 1.75em | #14202b |
| Stat number | `.highlight .num` | serif 1.7rem = 27.2px / 600 / 1 | #b13768 |
| Body | `body`, `p` | 17px / 400 / 1.6 | #1f2933 |
| Abstract text | `.abstract` | 16px / 400 / 1.6 | #1f2933 |
| Subtitle | `.hero .subtitle` | 1.05rem = 16.8px | #5b6772 |
| Authors | `.authors` | 1.02rem = 16.3px | #2c3a48 |
| Affiliations | `.affiliations` | 0.92rem = 14.7px | #5b6772 |
| Venue pill | `.hero .venue` | 0.8rem = 12.8px / 600 uppercase, letter-spacing 0.12em | #b13768 |
| Button | `.btn` | 0.93rem = 14.9px / 500 | #ffffff |
| Caption | `figcaption`, `p.caption` | 0.88rem = 14.1px / 1.5, left-aligned | #5b6772 |
| Table | `table.compare` | 0.92rem = 14.7px; header 600 | #1f2933 |
| Code block | `pre.code` | JetBrains Mono 0.88rem / 1.55 | #1f2933 |
| BibTeX | `.bibtex` | JetBrains Mono 0.85rem / 1.5, pre-wrap | #1f2933 |
| Footer | `footer` | 0.88rem, centred | #5b6772 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Venue pill, buttons | 999px | 1px (#b13768 pill, #1f2933 button) | none |
| Abstract box, stat cards | 10px | 1px #e6e9ec | none |
| pip package callout | 12px | 1px #f0d7be | none |
| Code block, BibTeX, table wrapper | 8px | 1px #e6e9ec | none |
| Example callouts | 0 8px 8px 0 | 3px #1f6f8b left only | none |
| Equation block | 0 | 3px #1f6f8b left only | none |
| Figure images | 6px | none | none |
| Inline code | 4px | 1px #e6e9ec | none |
| Step number disc | 50% (32px) | none | none |

There are no shadows anywhere on the page; separation is by hairlines and pale fills.

## Layout Metrics

- **Container**: `.container { max-width: 920px; margin: 0 auto; padding: 0 24px }`, so text spans 872px (x=284–1156 at 1440).
- **Hero**: padding 64px 0 40px, centred text, 1px #e6e9ec bottom rule across the viewport; rendered 446px tall.
- **Sections**: `section { padding: 56px 0; border-bottom: 1px solid #e6e9ec }` (last section has no rule), so 112px between section contents with a full-bleed rule in the middle.
- **Paragraph rhythm**: `p` margin 0 0 1em; h2 margin-bottom 1rem.
- **Stat cards**: `grid-template-columns: repeat(auto-fit, minmax(220px, 1fr))`, gap 14px, margin 18px 0 8px; three across at desktop.
- **Figures**: full-column images (the TL;DR chart spans the 872px column); causal diagram capped at 360px and flow diagram at 460px, both centred; two-up grids use 2 columns with 18px gap.
- **Table**: 870px inside an 8px-radius scroll wrapper with sticky header.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥990px | centred 920px container, 24px padding | 17px | 41.6px | stat cards 3 across |
| 648–990px | 24px | 17px | 4.2vw (27.2–41.6px) | stat cards 3 across down to about 740px, then 2 |
| 640px | 24px | 17px | 27.2px | `.fig-grid-2` → 1 column; stat cards 2 then 1 (auto-fit at 220px) |
| <640px | 24px | 17px | 27.2px floor | buttons wrap to several centred rows |

## Components

- **Venue pill** (`.hero .venue`): inline-block, 1px solid #b13768, radius 999px, padding 3px 12px, Source Sans 3 12.8px/600 uppercase, letter-spacing 0.12em, #b13768 on white; 18px below it the title.
- **Dark pill button** (`.btn`): inline-flex, gap 8px, padding 9px 16px, background #1f2933, 1px #1f2933 border, radius 999px, white Source Sans 3 14.9px/500; 16px stroke icon on the left (Feather-style: file, globe, list-box, table, filled GitHub mark, download). Hover: background #2c3a48, translateY(-1px), no underline, 120ms ease.
- **Abstract box** (`.abstract`): #fafbfc fill, 1px #e6e9ec border, radius 10px, padding 24px 28px, 16px text; heading 20px serif, margin 0 0 0.6em.
- **Stat card** (`.highlight`): white, 1px #e6e9ec border, radius 10px, padding 16px 18px; number Source Serif 4 27.2px/600 #b13768, line-height 1; label 0.9rem = 14.4px #5b6772, 4px below.
- **Example callout** (`ul.examples li`): padding 12px 16px 12px 18px, #fafbfc fill, 3px #1f6f8b left border, radius 0 8px 8px 0, 10px apart; lead phrase bold #14202b.
- **Equation block** (`.math-block`): #fafbfc fill, 3px #1f6f8b left border, padding 14px 18px, serif 1.05rem MathJax SVG; explanatory line in 0.85rem #5b6772.
- **Numbered steps** (`ol.steps`): rows padding 12px 0 12px 48px with #e6e9ec rules above and below; 32px #1f6f8b disc with a white serif numeral at 0.95rem.
- **Comparison table** (`table.compare`): white, 14.7px, cells padding 8px 10px right-aligned and nowrap, hairline rows; header on #f6f8fa with a 2px #c3cad1 bottom rule and sticky top; dataset cells bold on #fafbfc with a right hairline, spanning two rows; best value 600 #b13768.
- **pip callout** (`.pkg-callout`): gradient #fdf7f0 → #fdf3ea, 1px #f0d7be, radius 12px, padding 24px 26px, with a code block inside.
- **BibTeX** (`.bibtex`): #f6f8fa, 1px #e6e9ec, radius 8px, padding 16px 18px, JetBrains Mono 0.85rem, wraps.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Venue badge | yes | outlined raspberry pill above the title |
| Title / subtitle | yes | centred serif title, muted one-line subtitle |
| Authors / affiliations | yes | centred, teal numeric superscripts, linked names in author slate |
| Link buttons | yes | six charcoal pills with stroke icons, including a pip install link |
| Abstract | yes | pale grey box with serif heading |
| TL;DR + stat cards | yes | three white cards with raspberry serif numbers above a bar chart |
| Teaser image | absent from the source | first figure is the TL;DR chart |
| Intuition examples | yes | teal-bar callouts (quote-bar style) |
| Method with math | yes | MathJax in teal-bar equation blocks, small centred diagrams, numbered steps |
| Results table | yes | bordered comparison table with sticky grey header and raspberry best values |
| Code / install | yes | peach callout with a code block |
| BibTeX | yes | grey mono block |
| Video, carousel, navigation bar | absent from the source | — |
| Footer | yes | centred muted line |

## Adapting to Other Content

- **More authors**: let `p.authors` wrap; keep each `.author` nowrap and the 0.15em side margins. Move equal-contribution notes into the affiliations line in #5b6772.
- **A teaser image**: put it directly after the button row inside the hero container, full 872px, with 6px radius and a left-aligned 15px #5b6772 caption; keep the hero rule below it.
- **Larger results tables**: reuse `table.compare` inside the scroll wrapper; keep raspberry for the single best value per row and grey #f6f8fa for headers. Do not add zebra striping.
- **Long publication or news lists**: use the example-callout pattern (3px teal left bar, #fafbfc fill), with a date or venue in bold #14202b as the lead phrase.
- **Extra highlights**: the stat grid is auto-fit at 220px, so 4–6 cards wrap without new CSS; keep numbers in serif raspberry.

## Do's and Don'ts

- Do keep headings in Source Serif 4 600 and everything else in Source Sans 3.
- Do keep the split: raspberry for "result" marks (venue, stat numbers, best values), teal for structure and links (bars, discs, superscripts).
- Do separate sections with full-width #e6e9ec hairlines and 56px padding.
- Don't add shadows or gradients to cards; the only gradient is the faint peach pip callout.
- Don't colour the buttons; all six are the same charcoal pill.
- Don't underline links at rest; underline appears only on hover.

## Surfaces

White page; #fafbfc for the abstract, equation blocks, example callouts and table label cells; #f6f8fa for code, BibTeX and table header; faint peach for the package callout. All boxes use 1px #e6e9ec borders, none have shadows.

## Imagery

Matplotlib bar chart with blue (XGB) and magenta (MLP) bars and error bars, a small causal graph, and a flow diagram, all on white. Images keep their own white ground and get a 6px radius; captions are left-aligned with a bold "Figure N." lead.

## Layout

One centred 920px column. Centred hero, then left-aligned sections: Abstract, TL;DR, The intuition, Method, When does CRDA help?, comparison table, pip package, BibTeX. Page height about 7,300px at 1440 wide.

## Agent Prompt Guide

Quick colors: page #ffffff, text #1f2933, headings #14202b, muted #5b6772, teal #1f6f8b, raspberry #b13768, rule #e6e9ec, box #fafbfc, code #f6f8fa.

1. "Build a centred academic hero: 920px container with 24px padding, padding 64px 0 40px, 1px #e6e9ec bottom rule. Outlined pill 'ICML 2026' (12.8px/600 uppercase, letter-spacing 0.12em, #b13768 text and 1px border, 999px radius, padding 3px 12px), then a Source Serif 4 41.6px/600 title in #14202b, a 16.8px #5b6772 subtitle, authors 16.3px #2c3a48 with #1f6f8b superscripts."
2. "Make pill buttons: inline-flex, gap 8px, padding 9px 16px, background #1f2933, radius 999px, white Source Sans 3 14.9px/500, 16px stroke icon on the left; hover background #2c3a48 and translateY(-1px). Row centred, gap 10px, wrapping."
3. "Create stat cards: grid repeat(auto-fit, minmax(220px, 1fr)), gap 14px; each card white with 1px #e6e9ec border, radius 10px, padding 16px 18px; number in Source Serif 4 27.2px/600 #b13768, label 14.4px #5b6772 4px below."

## Similar Pages

- Hand-written academic project pages that pair a serif heading face with a humanist sans and a two-accent palette.
- Pages with boxed abstracts and full-width section rules, such as simple single-file GitHub Pages sites for tabular ML papers.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --fg: #1f2933;
  --heading: #14202b;
  --author: #2c3a48;
  --muted: #5b6772;
  --accent: #1f6f8b;
  --accent-2: #b13768;
  --rule: #e6e9ec;
  --box: #fafbfc;
  --code-bg: #f6f8fa;
  --max-width: 920px;
  --font-serif: "Source Serif 4", "Source Serif Pro", Georgia, serif;
  --font-sans: "Source Sans 3", "Source Sans Pro", -apple-system, "Segoe UI", Arial, sans-serif;
  --font-mono: "JetBrains Mono", "SF Mono", Menlo, monospace;
  --radius-box: 10px;
  --radius-pill: 999px;
}
```

## Provenance

- **URL**: https://crda-project.github.io
- **Paper**: Counterfactual Residual Data Augmentation for Regression (arXiv 2606.28460), Hossein Mohebbi, Oliver Schulte, Ke Li, Pascal Poupart.
- **Venue**: ICML 2026.
- **Selection reason**: the arXiv comment states acceptance at ICML 2026 and links this project page.
- **Template credit**: none; a single custom stylesheet (`static/css/style.css`) with Google Fonts and MathJax 3.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, and the page's `style.css` and `index.html` read directly, on 2026-10-28.
