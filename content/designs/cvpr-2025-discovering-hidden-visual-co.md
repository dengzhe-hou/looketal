# Infant Concepts Card Deck — Style Reference

> A tidy explainer deck: soft white cards, a blue question bubble, three numbered coloured tabs.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 screenshot, scrolled captures of the full 8,385px page, the page's own `static/css/style.css` (1,260 lines, hand-written with CSS custom properties) and `citations.css`, and the markup. The listed URL redirects to `kexueyi.github.io/discover-hidden-visual-concepts/`; everything below is measured there. Bulma is loaded only as a minimal grid. Color share is measured on the first 1440×900 viewport.

## Overview

A modern explainer built from cards. The white hero centres a 40px title, a bold blue "CVPR 2025", sky-blue author links with superscripts, the two affiliations and four white pill buttons with a light grey 2px outline and a small shadow. Below it a diagonal grey gradient band (#f8f9fa to #e9ecef) holds the first big white card (12px radius, 1px #e9ecef border, light shadow): a "Motivation" heading with a 120×4px blue underline bar, two grey sub-cards comparing the computational model and the biological infant joined by a blue "↔", and a "Our Research Question" callout on a pale blue gradient with a frosted inner quote box. Every later section is its own white card on white: "Key Contributions" as three cards with coloured left borders (coral, teal, sky) and matching gradient number circles, then numbered findings sections with "Key Finding" callouts, two-up figures with italic grey captions, a results table rendered as an image, and a BibTeX box with a copy button. A fixed blurred-white section nav slides in after scrolling, with the active item in a lavender pill.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 61.1%, band greys #f8f9fa 8.6%, #ecf0ef 8.0% and #f6f8f8 6.5% (the gradient band and the grey comparison sub-cards), near-white #fdfdfd 7.5%, warm grey #9f9593 7.2% (text and figure photos), traces under 1%. The blue accents (venue, authors, underline bar, "↔") are each under 1% but carry the hierarchy.

Anatomy in DOM order (hero `.container.is-fullhd` → `.glass-container` 1152px at x=144, centred):

1. **Title** — `h1.publication-title`, declared `'Google Sans', sans-serif` 40px (2.5rem) / 500 / line-height 48px; Google Sans is not loaded, so it renders in the default sans (Arial on the capture machine), #333333, two lines (y=48–144). Fades up on load (0.8s, 0.2s delay). Gap 16px.
2. **Venue** — `.publication-venue`, "CVPR 2025", system-ui 24px / 600 / 38.4px, #208eee (y=160–198). Gap 10px.
3. **Authors** — `.publication-authors`, 19.2px / 400 / 30.72px; names are links in #209cee with superscript numbers, commas #333333; hover darkens to #118fe4 and grows a 2px underline from the left (y=208–243).
4. **Affiliations** — second `.publication-authors`, "1Nanyang Technological University 2The Max Planck Institute for Psycholinguistics", 19.2px #333333 (y=243–278). Gap 16px.
5. **Buttons** — `.publication-links` flex row, gap 16px: "Paper" (fa-file-pdf), "arXiv" (Academicons), "Code" (GitHub), "Poster" (fa-images); `a.button.is-normal.is-rounded`, system-ui 16px / 500, #333333 on #ffffff, 2px solid #e9ecef, pill radius, padding 12px 20px, shadow `0 2px 4px rgba(0,0,0,0.1)`; y=294–334. Gap 60px (hero end at y=394).
6. **Gradient band and Motivation card** — `section#research-question`, `linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%)`, padding 48px 0; `.content-section` card at x=48, y=442, 1344px wide, padding 32px. Inside: `h2.section-title` "Motivation" 35.2px / 600 #333333 centred (y=475) with its blue bar, then two `.model-comparison-box` sub-cards (#f8f9fa, 12px radius, padding 24px, 500px max) from y=572, figure images with 8px radius. The fold cuts the sub-cards.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | `--background` | page, hero, content cards, buttons |
| Ink | #333333 | `--text-primary` | title, section titles, card headings, body |
| Secondary | #666666 | `--text-secondary` | contribution body text, captions, BibTeX copy icon |
| Question Ink | #474646 | `.research-question-title`, `-text` | research question heading and sentence |
| Primary Sky | #209cee | `--primary-color` (hsl(204,86%,53%)) | author links, section-title underline bar, button hover border and text |
| Sky Hover | #118fe4 | `--primary-hover` | author link hover |
| Venue Blue | #208eee | `--text-emphasis` (hsl(208,86%,53%)) | "CVPR 2025" |
| Mist | #f8f9fa | `--background-secondary` | band gradient start, comparison sub-cards, BibTeX box, contribution card gradient end |
| Hairline | #e9ecef | `--border-color` | card borders, button outlines, band gradient end |
| Question Blue | #c2dcfa | `.research-question-highlight` | gradient start of the research-question callout (to #f1f2fe) |
| Question Lilac | #f1f2fe | `.research-question-highlight` | gradient end of the callout |
| Indigo | #667eea | `.top-nav-links a.active`, `.citation`, `.vs-text` | active nav item, inline citation markers, "↔" connector, callout shadow tint |
| Coral | #ff6b6b | `.contribution-1` | first card's 4px left border and number circle (gradient to #ff5252) |
| Coral Deep | #ff5252 | `.contribution-1 .contribution-number` | number circle gradient end |
| Teal | #4ecdc4 | `.contribution-2` | second card's left border and number circle (gradient to #26a69a) |
| Teal Deep | #26a69a | `.contribution-2 .contribution-number` | number circle gradient end |
| Sky Tab | #45b7d1 | `.contribution-3` | third card's left border and number circle (gradient to #2196f3) |
| Azure | #2196f3 | `.contribution-3 .contribution-number` | number circle gradient end |
| Reference Grey | #f5f5f5 | `.references-section` | references band |
| Reference Rule | #dddddd | `.references-section`, `.reference-item` | band top border and item dividers |
| Shadow Black | #000000 | `--shadow-light`, `--shadow-medium` | `0 2px 4px rgba(0,0,0,0.1)`, `0 4px 12px rgba(0,0,0,0.15)` |

## Tokens — Typography

- **UI and body:** declared `system-ui, -apple-system, BlinkMacSystemFont, 'Inter', 'Roboto', sans-serif` on `html` and `body`. Because `system-ui` comes first it always resolves, so Inter (requested from Google Fonts) is never used; the page renders in the platform face (Segoe UI on Windows, San Francisco on macOS). Substitute: Inter.
- **Display:** declared `'Google Sans', sans-serif` on `.publication-title`, `.publication-authors`, `.section-title`; Google Sans is not loaded, so these render in the default sans (Arial on Windows, Helvetica on macOS). Substitute: Inter at weight 500–600, which is closer to the intended Google Sans than the Arial fallback.
- **Mono:** `.bibtex-container` declares `'Roboto Mono'` (loaded 400); the inner `pre` and `code` use the browser monospace at 13px.
- **Roboto 400/700:** loaded, applied only where nothing earlier in a stack resolves (effectively unused).
- **Icons:** Font Awesome 5, Academicons.

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `h1.publication-title` | 40px / 500 / 48px |
| Venue | `.publication-venue` | 24px / 600 / 38.4px |
| Authors, affiliations | `.publication-authors` | 19.2px / 400 / 30.72px |
| Section titles | `h2.section-title` | 35.2px / 600 / 56.32px, centred, 120×4px bar below |
| Card headings | `.contribution-content h4`, sub-card `h4` | 19.2px / 600 / 24.96px (sub-card h4 17.6px) |
| Research question | `h3.research-question-title`, `.research-question-text` | 20.8px / 600 and 19.2px / 450 / 28.8px, #474646 |
| Body | `p` | 16px / 400 / 25.6px, 24px side margins |
| Contribution text | `.contribution-content p` | 16px / 400 #666666 |
| Captions | `.figure-caption` | 14.4px italic / 400 / 21.6px, #666666 |
| Buttons | `.button` | 16px / 500 / 24px |
| Section nav | `.top-nav-links a` | 14px / 500 / 22.4px, rgba(0,0,0,0.8) |
| References | `.reference-item` | 14px / 400 / 22.4px |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Content card | 12px | 1px #e9ecef | `0 2px 4px rgba(0,0,0,0.1)` |
| Contribution / Key Finding card | 16px | 2px transparent, 4px coloured left | `0 4px 12px rgba(0,0,0,0.08)` |
| Number circle | 50% (40px) | none | `0 4px 12px` of its colour at 0.3 |
| Comparison sub-card | 12px | none | none |
| Research question callout | 12px | none | `0 8px 24px rgba(102,126,234,0.1)` |
| Inner quote box | 8px | 1px rgba(102,126,234,0.15) | none, fill rgba(255,255,255,0.7) |
| Buttons | pill | 2px #e9ecef | `0 2px 4px rgba(0,0,0,0.1)`, hover `0 4px 12px rgba(0,0,0,0.15)` |
| Figures | 8px | none | none |
| BibTeX box | 8px | 1px #e9ecef | none; copy button 4px radius |
| Section nav links | 6px | none | none |

## Layout Metrics

- **Hero:** `.container.is-fullhd` with a 1152px inner `.glass-container` (x=144); hero section 394px tall, content from y=48.
- **Motivation band:** padding 48px 0; the first card spans the 1344px container (x=48), padding 32px.
- **Later cards:** `.container.is-max-desktop` 1152px wide at 1440 (x=144), padding 32px; sections padded 48px 24px.
- **Inner width:** cards' content 1086px (x=177); contribution cards 1086×112px, stacked with 40px between.
- **Figures:** two-up `.column.is-6` 567px each with 12px padding; single figures 1018px; captions 495px for two-up.
- **Section nav:** fixed, 57px tall, `.top-nav-container` max 1200px, links gap 32px; hidden (opacity 0, translateY(-100%)) until scrolled.
- **References band:** full-bleed (−20px side margins), padding 32px 0 16px, items 1152px wide.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1408px | 48px (fullhd container) | 16px | 40px | two-up comparison and figures |
| 1024–1407px | Bulma container steps (960/1152px) | 16px | 40px | same |
| ≤768px | 24px card padding | 16px | 40px | `.columns` stack, comparison sub-cards and two-up figures go single column; section nav links wrap |

## Components

- **Content card:** `.content-section`, #ffffff, 12px radius, 1px #e9ecef border, padding 2rem, shadow `0 2px 4px rgba(0,0,0,0.1)`; fades up 30px when scrolled into view.
- **Section title with bar:** 35.2px / 600 #333333 centred, `::after` 120×4px #209cee bar with 2px radius, centred under the text.
- **Numbered contribution card:** gradient `135deg #ffffff → #f8f9fa`, 16px radius, 4px solid left border in the card's colour (#ff6b6b, #4ecdc4, #45b7d1), shadow `0 4px 12px rgba(0,0,0,0.08)`; a 40px circle with the matching gradient (to #ff5252, #26a69a, #2196f3), white 19.2px / 700 numeral and coloured glow; heading 19.2px / 600, text 16px #666666.
- **Research question callout:** `linear-gradient(60deg, #c2dcfa, #f1f2fe)`, 12px radius, padding 24px 32px, indigo-tinted shadow; "✨ Our Research Question" title, then a frosted inner box (rgba(255,255,255,0.7), 1px indigo-tint border, 8px radius) with grey quote marks and the question at 19.2px / 450 #474646, key phrase bold.
- **Outline pill button:** #ffffff, 2px #e9ecef, #333333 16px / 500, padding 12px 20px, icon left with 0.5rem gap, light shadow; hover lifts 2px, shadow medium, border and text #209cee.
- **Comparison pair:** two #f8f9fa sub-cards (12px radius, 24px padding) with figure, 17.6px / 600 heading and a 14.4px muted subtitle, joined by a 48px / 700 #667eea "↔".
- **Section nav:** fixed rgba(255,255,255,0.95) with `backdrop-filter: blur(10px)`, 1px rgba(0,0,0,0.1) bottom border, shadow `0 2px 20px rgba(0,0,0,0.1)`; links 14px / 500, padding 8px 16px, 6px radius; hover and active #667eea text on rgba(102,126,234,0.1–0.15) with a 20×3px indigo bar under the active item.
- **Citation marker:** `[n]` in #667eea with a faint indigo underline and a hover popover (white, 1px #333333 border, 5px radius).
- **BibTeX box:** #f8f9fa, 1px #e9ecef, 8px radius, padding 8px, 13px monospace, absolute copy button top-right (white, 1px #e9ecef, 4px radius; hover #209cee; copied state fills #209cee).

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / venue / authors / affiliations | Yes | centred, blue venue and links |
| Link buttons | Yes | four white outline pills |
| Motivation | Yes | comparison sub-cards plus research-question callout |
| Contributions | Yes | three numbered coloured cards |
| Findings sections | Yes | numbered h2 cards, each with a "Key Finding" callout, figures and captions |
| Results table | Yes (non-standard) | rendered as an image inside a card, LaTeX-style |
| Section nav | Yes | fixed blurred bar that appears on scroll |
| Teaser image or video | No (absent from the source) | the Motivation figures stand in |
| Abstract | No (absent from the source) | |
| BibTeX | Yes | grey box with copy button |
| References | Yes | numbered list on a #f5f5f5 band, backlinks to the text |
| Footer | Yes (non-standard) | a copyright line inside the references band |

## Adapting to Other Content

- **More contributions:** add `.contribution-4` and on with new colour pairs from the same soft family (for example a violet #9b8afb to #7c4dff), keeping the 4px left border and gradient circle.
- **Results table:** make it HTML inside a content card: 16px system-ui, header row on #f8f9fa, 1px #e9ecef row rules, best numbers bold #333333; keep the italic #666666 caption below.
- **Abstract:** a content card with the section-title bar and 17.6px / 1.8 #666666 justified text at 800px max, as the CSS already defines (`.abstract-content`).
- **More authors:** the centred 19.2px line wraps; keep superscripts and put affiliations on their own line.
- **News or updates:** a content card with a list of short rows, each date as a 14px #667eea pill like the active nav item.

## Do's and Don'ts

- Do put every section in a white 12px-radius card with a hairline border and a light shadow.
- Do give each contribution its own colour and use it twice (left border and number circle).
- Do frame the central question in its own gradient callout; it is the page's thesis.
- Don't rely on Google Sans without loading it; the fallback is Arial. Load the face or use Inter.
- Don't use more than one strong blue for text; links and bars are #209cee, the venue #208eee, and indigo #667eea is for nav and citations only.
- Don't stack shadows: cards use the light shadow, hover states the medium one.

## Surfaces

White hero; a 135° #f8f9fa→#e9ecef gradient band behind the first card; white cards everywhere else on white; #f8f9fa sub-cards and BibTeX; a pale blue-to-lilac callout; #f5f5f5 references band. Elevation is low and even.

## Imagery

Clean diagrams with dashed green boxes and labelled encoders, photos of infants with head cameras, a developmental-curve chart, Venn diagrams, box plots with labelled concept chips, and a LaTeX-typeset results table as an image. Figures sit on white with 8px rounded corners.

## Layout

Centred hero, then a stack of full-width cards (1344px for the first, 1152px after), each with centred section titles and mostly two-up or single figures inside. Rendered height about 8,400px.

## Agent Prompt Guide

Quick colors: text #333333 and #666666 on #ffffff, links and bars #209cee, venue #208eee, nav and citations #667eea, hairline #e9ecef, mist #f8f9fa, contribution colours #ff6b6b, #4ecdc4, #45b7d1.

1. "Create a content card: #ffffff, 12px radius, 1px solid #e9ecef, padding 2rem, shadow 0 2px 4px rgba(0,0,0,0.1); centred 35.2px weight-600 #333333 heading with a 120×4px #209cee bar centred under it."
2. "Build three contribution cards: background linear-gradient(135deg, #ffffff, #f8f9fa), 16px radius, 4px solid left border in #ff6b6b, #4ecdc4 or #45b7d1, shadow 0 4px 12px rgba(0,0,0,0.08); a 40px circle with the matching gradient (to #ff5252, #26a69a, #2196f3) holding a white 19.2px bold numeral, then a 19.2px weight-600 heading and 16px #666666 text."
3. "Make a research-question callout: linear-gradient(60deg, #c2dcfa, #f1f2fe), 12px radius, padding 24px 32px, shadow 0 8px 24px rgba(102,126,234,0.1); inside a box with rgba(255,255,255,0.7) fill, 8px radius and a 1px rgba(102,126,234,0.15) border, the question at 19.2px #474646 with the key phrase bold."

## Similar Pages

- Story-driven explainer pages that use cards and callouts instead of a paper-style column.
- Cognitive-science and developmental-AI project pages with a research-question lead.

## Quick Start

```css
:root {
  --primary-color: #209cee;
  --primary-hover: #118fe4;
  --text-emphasis: #208eee;
  --text-primary: #333333;
  --text-secondary: #666666;
  --background: #ffffff;
  --background-secondary: #f8f9fa;
  --border-color: #e9ecef;
  --indigo: #667eea;
  --c1: #ff6b6b;
  --c2: #4ecdc4;
  --c3: #45b7d1;
  --shadow-light: 0 2px 4px rgba(0, 0, 0, 0.1);
  --shadow-medium: 0 4px 12px rgba(0, 0, 0, 0.15);
  --border-radius: 8px;
  --border-radius-large: 12px;
  --font-ui: system-ui, -apple-system, 'Inter', sans-serif;
  --title-size: 40px;
  --h2-size: 35.2px;
  --body-size: 16px;
}
```

## Provenance

- **URL:** https://kexueyi.github.io/webpage-discover-hidden-visual-concepts (redirects to https://kexueyi.github.io/discover-hidden-visual-concepts/)
- **Paper:** Discovering Hidden Visual Concepts Beyond Linguistic Input in Infant Learning (arXiv 2501.05205), Xueyi Ke, Satoshi Tsutsui, Yayun Zhang, Bihan Wen.
- **Venue:** CVPR 2025 (stated in the hero).
- **Selection reason:** arXiv 2501.05205 comment states acceptance at CVPR 2025; project page linked in the abstract.
- **Template credit:** hand-written CSS; the footer says design elements are inspired by the Transformer Circuits Thread and Nerfies.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share, the 1440×900 screenshot, scrolled full-page captures, `static/css/style.css`, `static/css/citations.css`, page HTML; 2026-10-28.
