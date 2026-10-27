# SceneSmith — Style Reference

> A film still before the credits: a robot in a rendered kitchen fills the screen and the title rises out of the dark at the bottom.

**Theme:** both

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 screenshot, a scrolled capture of the first body sections, and the page's own `static/css/index.css` on top of Bulma (`bulma.min.css`). "Both" means a dark navy hero, nav and footer around a light body; there is no theme switch. The hero is a playing video, so the color share depends on the frame captured.

## Overview

A Nerfies-lineage Bulma page reworked into a cinematic layout. The first screen is a full-bleed, 100vh autoplay video of a robot working in a generated kitchen, darkened by a navy overlay that deepens toward the bottom. Institutional logos (MIT CSAIL, Toyota Research Institute) sit on frosted white plaques in the top corners. Everything else is anchored to the bottom centre: a small triangle symbol, "SceneSmith:" in a cyan-to-amber gradient, a white 44.8px title, a glassy amber-outlined "ICML 2026 Spotlight" capsule with a "Top 2.2%" chip, white-on-dark author names and seven translucent pill links. Below the fold the page turns light: white and pale blue-gray (#f0f4f8) bands, centred 32px Noto Sans section titles in #363636 with a 60×3px cyan-to-orange underline, 12px-radius video frames with soft shadows, a cyan left-bar intro card and five pipeline cards whose top borders run cyan, blue, violet, orange and red. A fixed navy nav bar slides in after the hero, and the footer returns to navy.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): video grays #797a7e 19.3%, #5e5f64 13.1%, #45454a 12.5%, #6f6c6e 11.2%, #9c9ea0 8.0%; slate #323944 15.1%; warm wood #564e4b 11.3%; overlay navy #151a23 9.5% (bottom band). The share follows the video frame; the navy share grows toward the bottom because of the overlay.

Anatomy in DOM order (1440×900, hero is exactly the viewport):

1. **Fixed nav** (`nav.site-nav`): hidden above the viewport (translateY(-100%)) on load; slides in once the hero scrolls away. 56px tall, #0a1628 at 92% with 16px blur, 1px cyan-at-12% bottom rule.
2. **Background video** (0–900px): `object-fit: cover`, full width and height; overlay gradient #0a1628 at 35% → 20% (40%) → 50% (70%) → 85% (bottom).
3. **Logos** (top 24px, 32px side inset): left MIT CSAIL (logo 55px tall), right Toyota Research Institute (40px); each on rgba(255,255,255,.78) with 12px blur, 8px radius, padding 6px 10px.
4. **Title** (`h1.publication-title`, y=500, 155px, three lines): Google Sans 44.8px/800, line-height 1.15, letter-spacing -0.02em, white, text-shadow 0 2px 20px black at 30%, centred in a 960px container. Line 1: 1em triangle symbol + "SceneSmith:" in linear-gradient(135deg, #00d4ff, #fcbf49); lines 2–3 "Agentic Generation of Simulation-Ready Indoor Scenes". Gap 15px.
5. **Venue capsule** (y=670, 42px): "ICML 2026 Spotlight" Google Sans 16.8px/800, letter-spacing 0.03em, white; 1px #fcbf49 at 65% border, 999px radius, fill linear-gradient(135deg, orange at 22%, cyan at 12%) over #0a1628 at 46%, inset white hairline and 0 10px 32px orange glow; inner chip "Top 2.2%" 11.5px/900 #0a1628 on #fcbf49 at 90%. Gap 15px.
6. **Authors** (y=728): Google Sans 17.6px, names white at 90% (hover #fcbf49), commas white at 70%. Gap 24px.
7. **Link pills** (y=795, 40px tall): arXiv, Video, Code, Scene Dataset, X Post, MIT News, Fox News; Noto Sans 16px, white at 75% on white at 8%, 1px white-at-15% border, fully rounded, padding 7px 20px, icon left (Academicons arXiv, Font Awesome brands and solids). Wrapper bottom padding 48px.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Deep Navy | #0a1628 | --surface-dark | hero ground and overlay, fixed nav, footer gradient top, BibTeX block, capsule chip text |
| Midnight | #060d18 | (literal) | footer gradient bottom |
| Harbor Navy | #0f2b46 | --primary | carousel arrow glyphs, active carousel dot, tooltip box |
| Cyan | #00b4d8 | --accent | section-title underline start, intro and callout left bars, first pipeline card border and numeral, carousel dots, hint text |
| Glow Cyan | #00d4ff | --accent-glow | "SceneSmith:" gradient start |
| Orange | #f77f00 | --accent-warm | section-title underline end, fourth pipeline card, capsule glow |
| Amber | #fcbf49 | --accent-warm-light | "SceneSmith:" gradient end, capsule border, "Top 2.2%" chip, author hover |
| Ink | #1a1a2e | --text-primary | body text, pipeline stage titles |
| Title Charcoal | #363636 | (Bulma `.title`) | section titles (h2) |
| Slate Text | #4a5568 | --text-secondary | stage descriptions, secondary copy |
| Mist Band | #f0f4f8 | --surface-mid | alternate section bands (Scene Construction, Open-Vocabulary, Simulation-Ready) |
| White | #ffffff | (Bulma) | body sections, intro card, pipeline cards, hero title |
| Blue | #3b82f6 | (literal) | second pipeline card border and numeral |
| Violet | #8b5cf6 | (literal) | third pipeline card border and numeral |
| Red | #ef4444 | (literal) | fifth pipeline card border and numeral |

Declared but not visible: a stats bar, dark sections, agent-role chips and wave dividers exist in `index.css` but have no markup on the page.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | 'Google Sans', sans-serif | Google Sans 400 only; the 800 title weight is synthesized bold | Product Sans is not public; use Outfit |
| Text | 'Noto Sans', sans-serif | Noto Sans 400 | Open Sans |
| Icons | Font Awesome 6, Academicons | loaded | — |

The Google Fonts link also requests Castoro, which does not appear in the render.

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.hero-section .publication-title` | 2.8rem = 44.8px / 800 / 1.15, letter-spacing -0.02em | #ffffff, "SceneSmith:" gradient |
| Venue capsule | `.hero-venue-badge` | 1.05rem = 16.8px / 800, letter-spacing 0.03em | #ffffff |
| Capsule chip | `.hero-venue-badge span` | 0.72rem = 11.5px / 900, letter-spacing 0.04em | #0a1628 |
| Hero authors | `.publication-authors` | 1.1rem = 17.6px / 400 | white at 70–90% |
| Section title | `h2.title.is-3` | Noto Sans (Bulma `.title` inherits the body face) 2rem = 32px / 600 / 36px, padding-bottom 0.75rem, margin-bottom 1.5rem | #363636 (Bulma title color) |
| Body | `body`, `.content p` | Noto Sans 16px / 1.5 | #1a1a2e |
| Pipeline numeral | `.stage-num` | 1.4rem / 800 | stage color |
| Pipeline title | `.stage-title` | 0.85rem / 700 | #1a1a2e |
| Pipeline description | `.stage-desc` | 0.75rem | #4a5568 |
| Nav brand / links | `.nav-brand`, `.nav-links a` | Google Sans 1rem / 700; links 0.8rem / 500 | #ffffff; links white at 65% |
| Video label | `.video-view-label` | 12px / 600 | #ffffff on navy at 75% |
| BibTeX | `pre` | monospace 13.6px / 1.5 | white at 80% |
| Footer | `.footer-tagline`, `.footer-links a` | 0.85rem | white at 40–50% |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Hero link pills | 290486px (Bulma rounded) | 1px white at 15% | hover 0 4px 12px black at 20% |
| Venue capsule | 999px | 1px #fcbf49 at 65% | inset 0 0 0 1px white at 8%, 0 10px 32px orange at 20% |
| Logo plaques | 8px | none | none; 12px backdrop blur |
| Video frames | 12px (carousel items 8px) | none | --shadow-lg 0 10px 25px black at 8%, 0 4px 10px black at 4% |
| Intro card, info callouts | 12px | 4px #00b4d8 left | --shadow-sm |
| Pipeline cards | 12px | 3px top border in stage color | --shadow-sm |
| Section-title underline | 2px | 60×3px bar, #00b4d8 → #f77f00 | none |
| BibTeX block | 12px | none | none |
| Video view labels | 6px | none | none |

Shadow scale from the stylesheet: sm 0 1px 3px black at 6%; md 0 4px 6px at 5%; lg 0 10px 25px at 8%; xl 0 20px 40px at 10%.

## Layout Metrics

- **Hero**: `height: 100vh; min-height: 600px`; content wrapper absolutely positioned at the bottom with padding 0 24px 48px; text in Bulma `container is-max-desktop` (960px).
- **Body containers**: Bulma `container is-max-widescreen` (1152px; x=144–1296 at 1440); the intro card in the first section is about 900px wide; the same card style spans the full 1152px in the teaser section.
- **Sections**: Bulma `.section` padding 48px 24px; the intro section uses 56px top and 40px bottom. Section bands alternate white and #f0f4f8.
- **Title rhythm**: h2 padding-bottom 12px (the underline sits there), margin-bottom 24px; a short italic prompt line sits under carousel titles.
- **Media**: carousel videos about 1040px wide with slick arrows outside them; pipeline row 5 equal columns of 218px with about 16px gaps.
- **Footer**: padding 48px 24px 32px on a navy gradient with a cyan-at-10% top rule.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1216px | 24px; content 1152px | 16px | 44.8px | full layout, video hero |
| 769–1215px | 24px (Bulma containers shrink to 960px) | 16px | 44.8px | — |
| ≤768px | 24px | 16px | 28.8px | video hidden; hero becomes a 62vh navy gradient with blurred cyan/orange/violet orbs and a drifting 60px grid; content centred vertically; logos hidden; capsule 0.76rem; authors 0.9rem; nav links hidden; pipeline cards 2 columns with the last spanning both |
| ≤480px | 24px | 16px | 28.8px | — |

## Components

- **Cinematic hero**: section 100vh on #0a1628; `<video>` cover-fit at z 1; overlay linear-gradient(180deg, rgba(10,22,40,.35) 0%, rgba(10,22,40,.2) 40%, rgba(10,22,40,.5) 70%, rgba(10,22,40,.85) 100%) at z 2; text block bottom-anchored at z 3 with 48px bottom padding.
- **Gradient name** (`.accent-text`): linear-gradient(135deg, #00d4ff, #fcbf49) clipped to text, preceded by a 1em logo glyph.
- **Venue capsule**: inline-flex, gap 0.65rem, padding 9.3px 15.2px 9.3px 17.6px, radius 999px, 1px #fcbf49 at 65%, gradient fill over translucent navy, 10px blur, white 16.8px/800 label, inner amber chip with 900-weight navy text.
- **Glass link pill** (`.publication-links .button`): Bulma rounded button, padding 7px 20px, background white at 8%, 1px white-at-15% border, text white at 75%, 4px blur, icon left. Hover: background white at 15%, border white at 30%, text white, translateY(-1px), 0 4px 12px shadow.
- **Section title** (`h2.title.is-3.has-text-centered`): Noto Sans 32px/600 #363636, centred, 12px padding-bottom with a 60×3px #00b4d8 → #f77f00 bar (2px radius) centred at the bottom.
- **Intro card** (`.teaser-section .content.has-text-justified`): white, padding 1.5rem 2rem, radius 12px, --shadow-sm, 4px #00b4d8 left border, justified 16px text with a bold lead word.
- **Pipeline stage card**: white, radius 12px, padding 1rem, centred, --shadow-sm, 3px top border; numeral 1.4rem/800 and border in #00b4d8, #3b82f6, #8b5cf6, #f77f00, #ef4444 for stages 1–5; title 0.85rem/700, description 0.75rem #4a5568.
- **Video carousel**: slick carousel, round gray arrow glyphs at the sides, dots in #00b4d8 with the active dot #0f2b46; view labels ("Third Person", "Head View") top-left on navy at 75%, 6px radius.
- **Footer**: navy gradient #0a1628 → #060d18, brand 1.2rem/700 white with symbol, tagline 0.85rem white at 40%, links white at 50% hovering to #00b4d8, a white-at-6% divider and 0.75rem fine print.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Full-bleed hero video | yes | 100vh autoplay with navy bottom gradient |
| Institutional logos | yes | frosted white plaques in the top corners |
| Title with logo glyph | yes | bottom-anchored white title, gradient project name |
| Venue / award badge | yes | amber-outlined glass capsule with "Top 2.2%" chip |
| Authors | yes | white names, no affiliations line in the hero |
| Link buttons | yes | seven glass pills including press links (MIT News, Fox News) |
| Abstract | present but non-standard | the Abstract section is commented out; a short intro card replaces it |
| Method / pipeline | yes | five color-coded stage cards, method overview video, system overview figure |
| Video carousels | yes | many slick carousels of generated scenes and robot rollouts |
| Interactive 3D viewer | yes | room- and house-scale scene viewers (`viewer.css`) |
| Results tables | absent from the source | results are shown in videos and figures |
| Authors section | yes | separate "Authors" section near the end |
| BibTeX | yes | navy block, 12px radius, white-at-80% mono text |
| Acknowledgements, footer | yes | light section, then navy footer with brand and links |
| Sticky nav | yes | appears after the hero |

## Adapting to Other Content

- **No video**: use a still render with the same overlay gradient, or the mobile fallback (navy gradient with blurred cyan and orange orbs); keep the text anchored at the bottom.
- **More authors and affiliations**: keep the hero to names only and move affiliations to the "Authors" section; if names exceed two lines, drop the size to 0.95rem rather than shrinking the title.
- **A results table**: place it on a white card (12px radius, --shadow-md) inside a #f0f4f8 band; header row #0f2b46 text 700, best values #00b4d8 700; no colored cell fills.
- **Long publication or news lists**: use the info-callout pattern (white, 12px radius, 4px #00b4d8 left bar, --shadow-sm) with dates in #4a5568; press items can reuse the glass link pills in the dark footer.
- **Extra pipeline stages**: extend the color sequence only from the declared accents (cyan, blue, violet, orange, red); keep 3px top borders.

## Do's and Don'ts

- Do let the hero media fill 100vh and keep all text in the bottom third over the darkest part of the overlay.
- Do mark every centred section title with the 60×3px cyan-to-orange bar.
- Do alternate white and #f0f4f8 bands in the body and keep cards white with soft shadows.
- Don't put opaque buttons over the video; pills stay at 8% white with a 15% border.
- Don't use the amber color in the light body except as the underline's end; it belongs to the hero capsule and gradient name.
- Don't show the fixed nav over the hero.

## Surfaces

Dark navy for the hero, nav, BibTeX and footer; white and #f0f4f8 bands for the body; white cards with sm–lg shadows; frosted white plaques for logos; translucent white glass for hero pills.

## Imagery

Photoreal renders and screen recordings of generated indoor scenes (kitchens, dining rooms, bathrooms) with robots, shown as autoplay videos in carousels and side-by-side third-person and head views; an interactive 3D scene viewer; a system overview diagram. Media get 8–12px radii and soft shadows.

## Layout

One full-viewport hero, then about a dozen centred sections in a 1152px Bulma container: intro card, Scene Construction with pipeline cards, Robot Teleoperation, Zero-Shot Policy, Open-Vocabulary generation, Simulation-Ready scenes, room- and house-scale viewers, policy evaluation, method video, system overview, Authors, Citation, Acknowledgements. Page height about 12,600px at 1440 wide.

## Agent Prompt Guide

Quick colors: title #363636, navy #0a1628, harbor #0f2b46, cyan #00b4d8, glow cyan #00d4ff, orange #f77f00, amber #fcbf49, ink #1a1a2e, slate #4a5568, band #f0f4f8, white #ffffff.

1. "Build a cinematic hero: section 100vh on #0a1628 with a cover-fit background video and an overlay linear-gradient(180deg, rgba(10,22,40,.35), rgba(10,22,40,.2) 40%, rgba(10,22,40,.5) 70%, rgba(10,22,40,.85)). Bottom-anchored centred block (padding 0 24px 48px): Google Sans 44.8px/800 white title, line-height 1.15, letter-spacing -0.02em, with the project name in linear-gradient(135deg, #00d4ff, #fcbf49) clipped to text."
2. "Make a venue capsule: inline-flex, padding 9px 15px 9px 18px, radius 999px, 1px rgba(252,191,73,.65) border, background linear-gradient(135deg, rgba(247,127,0,.22), rgba(0,180,216,.12)) over rgba(10,22,40,.46), white 16.8px/800 text, inner chip 11.5px/900 #0a1628 on rgba(252,191,73,.9), box-shadow 0 10px 32px rgba(247,127,0,.2)."
3. "Create a light section: Bulma section padding 48px 24px on #f0f4f8, centred Noto Sans 32px/600 #363636 title with a 60×3px bar linear-gradient(90deg, #00b4d8, #f77f00) under it, then five white cards (12px radius, padding 16px, 3px top borders #00b4d8, #3b82f6, #8b5cf6, #f77f00, #ef4444, numerals 22.4px/800 in the same colors)."

## Similar Pages

- Nerfies / Bulma project pages upgraded with a full-bleed video hero (robotics and 3D generation papers).
- Pages that switch from a dark cinematic opening to a light, card-based body.

## Quick Start

```css
:root {
  --primary: #0f2b46;
  --accent: #00b4d8;
  --accent-glow: #00d4ff;
  --accent-warm: #f77f00;
  --accent-warm-light: #fcbf49;
  --surface-dark: #0a1628;
  --surface-mid: #f0f4f8;
  --text-primary: #1a1a2e;
  --text-secondary: #4a5568;
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
  --shadow-lg: 0 10px 25px rgba(0,0,0,0.08), 0 4px 10px rgba(0,0,0,0.04);
  --radius: 12px;
  --radius-lg: 20px;
  --font-display: 'Google Sans', sans-serif;
  --font-text: 'Noto Sans', sans-serif;
}
```

## Provenance

- **URL**: https://scenesmith.github.io/
- **Paper**: SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes (arXiv 2602.09153), Nicholas Pfaff, Thomas Cohn, Sergey Zakharov, Rick Cory, Russ Tedrake.
- **Venue**: ICML 2026 Spotlight (the page badge adds "Top 2.2%").
- **Selection reason**: the arXiv comment states acceptance at ICML 2026 as a Spotlight and links this project page.
- **Template credit**: built on the Nerfies Bulma template (Bulma, slick carousel, Google Sans / Noto Sans / Castoro stack, `publication-title` classes), heavily restyled by `index.css` ("SceneSmith - Visual Design System").
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 screenshot, a scrolled capture of the first body sections, and the page's `index.css` and `index.html` read directly, on 2026-10-28.
