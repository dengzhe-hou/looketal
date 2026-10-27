# EgoGazeVQA Teal Dusk — Style Reference

> A lagoon at dusk: deep teal water sinking into black, a white title surfacing above a pale stone landing page.

**Theme:** light

Measured from the rendered page at 1440×900 in headless Chrome (`computed_style.py`, screenshot and tall capture), then checked against the page's own `assets/css/style.css`, the Prism "tomorrow" theme and `index.html`. Where stylesheet and render disagree, the render is reported. Pixel values are at the 1440px viewport unless a breakpoint is named. The hero buttons animate in with a 0.7s-delayed fade, and the capture caught them partly transparent; values below are the settled computed styles.

## Overview

A hand-built single page in Inter with no framework. A fixed white navbar (brand left, four anchor links right) sits over a full-width hero that fades from teal `#00a19b` (solid for the top 40%) to black, with a faint white wave silhouette near its bottom. The hero is all white type: a 64px/800 title with a near-white gradient fill, a 24px subtitle, author links, affiliations, a translucent pill badge "NeurIPS D&B 2025", and three buttons (one solid white, two glassy outlines). Below, the page turns light: alternating `#f9fafb` and `#f3f4f6` sections, each opened by a centred 40px/700 heading with a short 60×4px grey bar. Figures are rounded 12px cards with soft shadows; key contributions are white list cards with teal check icons; the main results table sits in a white card with grey header cells. A dark Prism code block with a grey Copy button and a `#1f2937` footer close the page. Document height is about 6,656px.

## First Viewport

Color share of the first 1440×900 viewport: `#20aaa5` 25.3% (teal hero top, lifted by the wave overlay), `#f9fafb` 24.4% (abstract section), `#09312f` 21.8% (dark lower hero), `#0d7f7b` 17.7% (mid hero gradient), `#ffffff` 7.8% (navbar), `#fcf6f7` 1.8%, `#f9fafa` 0.7%, `#fbfafb` 0.5%.

Anatomy in DOM order (centred unless noted):

1. Navbar `nav.navbar`, fixed, full width, 70px tall, `#ffffff`, shadow `0 1px 3px rgba(0,0,0,0.12)`; inner `.nav-container` max 1200px, padding 16px 20px. Brand "EgoGazeVQA" left, Inter 24px/700 `#000000`; links right, 16px/500 `#000000`, 32px apart.
2. Hero `section.hero`, full width, padding 120px 0 80px, `linear-gradient(180deg, #00a19b 40%, #000000 100%)`, height 654px.
3. Title `h1.hero-title`, 64px/800, line-height 102px, text filled with `linear-gradient(45deg, #faf9f9, #e5e7eb)`; top at y=120. Gap 16px.
4. Subtitle `h2.hero-subtitle`, 24px/400, `#ffffff`. Gap 32px.
5. Authors `.authors a`, 17.6px/400, `#ffffff`, 10px side margins, comma-separated, numeric and dagger superscripts. Gap 16px.
6. Affiliations `.affiliations`, 15.2px, white at 0.9 opacity, two lines. Gap 32px.
7. Badge `span.conference-badge` "NeurIPS D&B 2025", 16px/600, `rgba(255,255,255,0.2)` fill, 2px `rgba(255,255,255,0.3)` border, 25px radius, padding 8px 20px; 188×46px at y=443. Gap 32px.
8. Buttons `.hero-buttons`, flex, 16px gap, at y=520: Paper (solid white, label `#788084`, 121×54px), Code and 🤗 Dataset (glass outline). Hero ends at y=654.
9. Abstract section `section.section` on `#f9fafb`, padding 80px 0: heading "Abstract" 40px/700 `#000000` at y=734 with a 60×4px `#788084` bar 16px below; paragraph at y=866 in 17.6px `#6b7280`, justified, max-width 1000px. The abstract continues past the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Lagoon Teal | `#00a19b` | `.hero` gradient start; `.feature-list i` | Hero top 40%; check-circle icons in Key Contributions |
| Night | `#000000` | `.hero` gradient end; `--text-primary` | Hero bottom; navbar text, section headings, table text |
| Title Pearl | `#faf9f9` → `#e5e7eb` | `.gradient-text` | Hero title fill |
| Pebble | `#788084` | `--primary-color` | Section heading bars, Paper button label, Copy button, nav-link hover and underline |
| Stone Text | `#6b7280` | `--text-secondary` | Abstract, figure captions, list text |
| Mist Page | `#f9fafb` | `--light-bg` | Body background, Abstract and Results sections |
| Mist Band | `#f3f4f6` | `--gray-bg` | Method and Citation sections, table header cells, table row hover |
| Hairline | `#e5e7eb` | `--border-color` | Table row rules |
| Slate Footer | `#1f2937` | `--dark-bg` | Footer band |
| Copy Hover | `#4b5563` | `.copy-btn:hover` | Copy button hover; the highlighted table row uses `rgba(75,85,99,0.1)` |
| Code Night | `#2d2d2d` | Prism tomorrow `pre[class*=language-]` | BibTeX block (overrides the page's `#1f2937`) |
| Code Text | `#cccccc` | Prism tomorrow | BibTeX text |
| Glass Fill | `rgba(255,255,255,0.1)` | `.btn-secondary` | Code and Dataset buttons; badge uses 0.2 |
| Glass Edge | `rgba(255,255,255,0.3)` | `.btn-secondary`, `.conference-badge` border | 2px outlines of glass buttons and badge |
| Card White | `#ffffff` | `.result-card`, `.feature-list li`, `.citation-box`, `.navbar` | Cards and navbar |

## Tokens — Typography

- **Declared:** `--font-main: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif`, Google Fonts weights 300–700; `--font-mono: 'JetBrains Mono', 'Courier New', monospace`.
- **Rendered:** Inter 400, 500, 600, 700 loaded; the 800 title weight is synthesized from 700. The BibTeX block renders in Prism's stack (`Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace`) because the Prism theme overrides the page's JetBrains Mono, which is never loaded. The Copy button falls back to the browser's Arial 13.33px. Substitute for Inter: Roboto Flex or SF Pro Text at the same weights.

| Role | Selector | Size | Weight | Line height | Colour |
|---|---|---|---|---|---|
| Hero title | `h1.hero-title` | 64px | 800 | 102.4px | gradient `#faf9f9` → `#e5e7eb` |
| Hero subtitle | `h2.hero-subtitle` | 24px | 400 | 38.4px | `#ffffff` |
| Section heading | `h2.section-title` | 40px | 700 | 64px | `#000000`, centred |
| Sub-heading | `.method-details h3`, `.visualization-section h3` | 24px | 700 | 38.4px | `#000000` |
| Card heading | `.result-card h3` | 18.72px | 700 | 30px | `#000000` |
| Nav brand | `.nav-brand a` | 24px | 700 | 38.4px | `#000000` |
| Nav link | `.nav-menu a` | 16px | 500 | 25.6px | `#000000` |
| Authors | `.authors a` | 17.6px | 400 | 28.2px | `#ffffff` |
| Abstract | `.abstract-content` | 17.6px | 400 | 31.7px | `#6b7280`, justified |
| Body, captions, table | `body`, `.image-caption`, `td` | 16px | 400 | 25.6px | `#6b7280` / `#000000` in tables |
| Table header | `.results-table th` | 16px | 600 | 25.6px | `#000000` |
| Button, badge | `.btn`, `.conference-badge` | 16px | 600 | 25.6px | see Components |
| BibTeX | `pre.language-bibtex` | 16px | 400 | 24px | `#cccccc` |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Conference badge | 25px |
| Method figures `.method-image`, result card, stat cards | 12px |
| Buttons `.btn`, feature list cards, vis items, citation box | 8px |
| BibTeX `pre`, Copy button | 6px |
| Section heading bar | 2px |

- **Shadows:** `--shadow-sm` `0 1px 3px rgba(0,0,0,0.12)` (navbar, feature cards); `--shadow-md` `0 4px 6px rgba(0,0,0,0.1)` (Paper button, result card, citation box, vis items); `--shadow-lg` `0 10px 15px rgba(0,0,0,0.1)` (method figures, Paper hover); `--shadow-xl` `0 20px 25px rgba(0,0,0,0.1)` (vis item hover).
- **Borders:** buttons and badge 2px; table rows 1px `#e5e7eb`.
- **Motion:** hero items `fadeInUp` (30px rise, 0.8s, staggered 0.2–0.7s); buttons and vis items lift 2px or 5px on hover; feature cards slide 5px right; nav links grow a 2px `#788084` underline from 0 to 100% width.

## Layout Metrics

- **Container:** `.container` max-width 1200px, padding 0 20px, so content is 1160px wide (x=140 to 1300 at 1440px). Text blocks narrow to 1000px (`.abstract-content`, `.image-caption`, `.feature-list`); method figures max 900px; `.method-details` adds 80px side padding.
- **Hero:** padding 120px 0 80px (the first 70px sit under the fixed navbar); height 654px at 1440px.
- **Sections:** `.section` padding 80px 0; heading margin-bottom 48px plus the bar's 16px margins.
- **Cards and grids:** `.results-grid` `repeat(auto-fit, minmax(500px, 1fr))` with 32px gap (one card here, so full width, 2rem padding); `.vis-grid` `minmax(250px, 1fr)` with 24px gap, items at 90% width.
- **Table:** full card width (1096px), cells padding 12px.

| Breakpoint | Container | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|---|
| >768px | 1200px max | 20px | 16px | 64px (section 40px) | nav links inline; grids auto-fit |
| 481–768px | fluid | 20px | 16px | 40px, subtitle 19.2px | nav collapses to a hamburger with a slide-in white menu; results and demo grids one column; stat grid two columns |
| ≤480px | fluid | 20px | 16px | 32px, section titles 28.8px | vis grid one column |

## Components

- **Fixed navbar.** White, `0 1px 3px rgba(0,0,0,0.12)` shadow, 70px tall; brand 24px/700 left; links 16px/500 with 32px gaps, hover colour `#788084` and a 2px underline that grows from the left over 0.3s.
- **Teal-to-black hero.** `linear-gradient(180deg, #00a19b 40%, #000000 100%)`, centred white type, a `::before` SVG wave in white at 10% fill and 0.3 opacity anchored to the bottom.
- **Solid hero button.** `.btn.btn-primary`: `#ffffff` fill, `#788084` 16px/600 label, Font Awesome icon left with 8px gap, padding 12px 24px, 8px radius, 2px transparent border, shadow `0 4px 6px rgba(0,0,0,0.1)`; hover lifts 2px with `0 10px 15px rgba(0,0,0,0.1)`.
- **Glass hero button.** `.btn.btn-secondary`: `rgba(255,255,255,0.1)` fill, white label, 2px `rgba(255,255,255,0.3)` border, same size and radius; hover fill `rgba(255,255,255,0.2)` and 2px lift.
- **Venue pill.** `.conference-badge`: `rgba(255,255,255,0.2)` fill, 2px `rgba(255,255,255,0.3)` border, 25px radius, padding 8px 20px, 16px/600 white.
- **Section heading.** `h2.section-title`, 40px/700 centred, with `::after` 60×4px `#788084` bar, 2px radius, 16px auto margins.
- **Figure card.** `img.method-image`, max 900px, 12px radius, `0 10px 15px rgba(0,0,0,0.1)`, followed by a justified 16px `#6b7280` caption with bold lead-in.
- **Contribution card.** `.feature-list li`: white, 8px radius, 16px padding, `0 1px 3px rgba(0,0,0,0.12)`, `fa-check-circle` icon in `#00a19b` at 19.2px on the left; hover slides 5px right.
- **Results card and table.** `.result-card` white, 32px padding, 12px radius, `0 4px 6px rgba(0,0,0,0.1)`; `.results-table` collapsed borders, 12px cells, header cells `#f3f4f6` 600, 1px `#e5e7eb` row rules, row hover `#f3f4f6`, highlighted rows `rgba(75,85,99,0.1)`.
- **Citation box.** White card (32px padding, 8px radius, md shadow) holding a Prism `pre` (`#2d2d2d`, `#cccccc` text, 6px radius, 16px padding) and an absolutely placed Copy button (`#788084`, white label, padding 8px 16px, 6px radius; hover `#4b5563`).
- **Footer.** `#1f2937` band, white centred text, padding 48px 0, icon links at 19.2px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navbar | Yes | Fixed white bar with anchor links |
| Title / author block | Yes | Teal-to-black gradient hero, white type |
| Venue badge | Yes | Glass pill "NeurIPS D&B 2025" |
| Link buttons | Paper, Code, Dataset | One solid white, two glass outlines |
| Abstract | Yes | Centred heading with bar, 1000px justified grey text, teaser figure card |
| Method | Yes | Gray band, figure cards with captions, Key Contributions card list |
| Results table | Yes | White card, grey header, hairline rows |
| Qualitative results | Yes | Vis grid item with caption |
| BibTeX | Yes | Prism dark block with Copy button |
| Footer | Yes | Dark slate band |
| Video, carousel, sliders | Absent from the source | |
| Dataset stats, demo panel | Declared in CSS, absent from the page | |

## Adapting to Other Content

- **More authors:** authors are inline links with 10px margins and wrap in the centred hero; keep them white and drop affiliations to two lines at 0.9 opacity.
- **More buttons:** add `.btn-secondary` glass buttons; reserve the single solid white `.btn-primary` for the paper.
- **More results:** add `.result-card`s; the `minmax(500px, 1fr)` grid puts two side by side at desktop widths. Use `tr.highlight` (`rgba(75,85,99,0.1)`) for the proposed method row.
- **Dataset statistics:** the stylesheet already defines `.stat-card` (white, 12px radius, 32px padding, 48px `#788084` icon, 32px number); use a `repeat(auto-fit, minmax(200px, 1fr))` grid on a `#f3f4f6` band.
- **News:** a `.feature-list` of white cards with teal icons and dates in 600 `#000000`, placed in its own section between hero and abstract.

## Do's and Don'ts

- Do keep the hero the only saturated area: teal fading to black, everything else greys and white.
- Do alternate `#f9fafb` and `#f3f4f6` section backgrounds, each with a centred 40px heading and 60×4px bar.
- Do put every figure and table on a white rounded card with a soft shadow.
- Do use teal `#00a19b` again only as small icon accents.
- Don't animate the hero buttons with a long delayed fade if the page may be screenshotted; they read as disabled while fading.
- Don't load a code theme that silently overrides your declared code colours unless that is intended.

## Surfaces

A fixed white navbar; a teal-to-black gradient hero; light sections alternating `#f9fafb` and `#f3f4f6`; white cards with 8–12px radius and soft shadows; a `#2d2d2d` code block; a `#1f2937` footer.

## Imagery

Egocentric video frames annotated with gaze points and QA overlays (orange gaze labels, coloured answer options), a construction-pipeline diagram, radar charts comparing MLLMs across scenarios, and qualitative examples. All are static PNG figures inside rounded shadowed cards.

## Layout

A 1200px centred container under a fixed navbar. Text narrows to 1000px; figures centre at up to 900px; the results card spans the container. Sections are full-width colour bands.

## Agent Prompt Guide

Quick colors: hero `#00a19b` → `#000000`, title fill `#faf9f9` → `#e5e7eb`, accent `#788084`, text `#000000` and `#6b7280`, page `#f9fafb`, band `#f3f4f6`, rule `#e5e7eb`, footer `#1f2937`, code `#2d2d2d` with `#cccccc`.

1. "Build a hero: full-width `linear-gradient(180deg, #00a19b 40%, #000000 100%)`, padding 120px 0 80px, centred Inter 64px/800 title filled with `linear-gradient(45deg, #faf9f9, #e5e7eb)` via background-clip text, a 24px white subtitle, 17.6px white author links, and a glass pill badge (`rgba(255,255,255,0.2)` fill, 2px `rgba(255,255,255,0.3)` border, 25px radius, padding 8px 20px, 16px/600)."
2. "Make two button styles at padding 12px 24px, 8px radius, 16px/600 Inter: solid `#ffffff` with `#788084` label and `0 4px 6px rgba(0,0,0,0.1)` shadow, and glass `rgba(255,255,255,0.1)` with white label and 2px `rgba(255,255,255,0.3)` border; both lift 2px on hover."
3. "Create a section on `#f3f4f6` with 80px vertical padding: centred 40px/700 `#000000` heading with a 60×4px `#788084` bar below, then a white results card (32px padding, 12px radius, `0 4px 6px rgba(0,0,0,0.1)`) holding a table with 12px cells, `#f3f4f6` 600-weight header, and 1px `#e5e7eb` row rules."

## Similar Pages

BlurDM in this NeurIPS 2025 batch also opens with a saturated gradient hero and white type, but in blue-green and without a navbar. Time-IMM shares the modern sans-serif card idiom on a light page.

## Quick Start

```css
:root {
  --hero: linear-gradient(180deg, #00a19b 40%, #000000 100%);
  --title-fill: linear-gradient(45deg, #faf9f9, #e5e7eb);
  --primary: #788084;
  --teal: #00a19b;
  --text: #000000;
  --text-secondary: #6b7280;
  --page: #f9fafb;
  --band: #f3f4f6;
  --border: #e5e7eb;
  --footer: #1f2937;
  --code-bg: #2d2d2d;
  --code-text: #cccccc;
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.12);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
  --font: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --radius-card: 12px;
  --radius-btn: 8px;
  --radius-pill: 25px;
}
.section-title::after { content: ''; display: block; width: 60px; height: 4px; background: var(--primary); margin: 1rem auto; border-radius: 2px; }
```

## Provenance

- **URL:** https://taiyi98.github.io/projects/EgoGazeVQA (redirects to the trailing-slash path)
- **Paper:** In the Eye of MLLM: Benchmarking Egocentric Video Intent Understanding with Gaze-Guided Prompting (arXiv 2509.07447), Taiying Peng, Jiacheng Hua, Miao Liu, Feng Lu (Beihang University, Tsinghua University).
- **Venue:** NeurIPS 2025; the page badge reads "NeurIPS D&B 2025".
- **Selection reason:** the arXiv comment states acceptance at NeurIPS 2025; the project page is linked in the abstract.
- **Template credit:** none stated; the page is a custom stylesheet.
- **Evidence used:** `computed_style.py` render at 1440×900 with first-viewport color share, the 1440 screenshot and tall capture, `assets/css/style.css`, the Prism tomorrow theme and the page markup. Captured 2026-10-28.
