# CANOR Midnight Launch — Style Reference

> A product reveal in a darkened hall: one neon-candy headline, a slow video behind it, and slides that snap into place.

**Theme:** dark

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide first-viewport and tall screenshots, the page's `style.css`, inline styles in the HTML, and the shared Bulma, bulma-carousel and `index.css` files it borrows from chen-geng.com/rose4d. The page is a stack of full-screen `scroll-snap` sections inside a 100vh scroll container (`html` and `body` have `overflow: hidden`), so the document is exactly 900px tall and the full-page capture shows only the hero; sections below the first are described from the markup and stylesheet. Google Sans loads at 400 only, so the 600 title is a synthesized bold; the body stack `'Linux Biolium', sans-serif` names a font that is never loaded (and is misspelled), so non-Google-Sans text renders in the default sans-serif (Arial on Windows). Color share is measured on the first viewport.

## Overview

The first screen is pure black with a dim, slowly looping video texture behind it. Centered on it, a giant two-line title at 7vw (100.8px at 1440): a grey outline icon of a dog's face, then "Category-Agnostic" in a pink-to-violet gradient (#ff6ec4 to #7873f5), and below it "Neural Object Rigging" in white. Far beneath, "CVPR 2025" in light Google Sans, the four author names at 36px, affiliations and an equal-contribution note, all white. A minimal link bar sits at the top right (Paper, arXiv, Code, Video, each with a Tabler outline icon), a column of six small dots on the right edge marks the sections (the current one in aqua #36e9e6), and a full-width row of five text tabs along the bottom names them: Introduction, Interactive Demo, "Clay-Monster", Approach, Miscellaneous. Each following section is another black, 100vh, centered slide: a 43px white title, a figure at 80% width dimmed to 90% brightness, short white text, and in the demo slide, dark rounded panels with 3D model viewers, a selection list and glowing vertical sliders.

## First Viewport

Color share (1440×900, 8-color quantize): black #000000 88.4%, lilac #9e81ac 3.1% and plum #654f6c 2.6% (the gradient title and its anti-aliasing), near-black #1a181b 2.3% (video texture), white #ffffff 1.8% (text), grey #cdcece 0.9% (icon and dots).

Anatomy in DOM order (full-width hero, content centered on x=720):

1. **Section dots** — `.section-nav`, fixed at the right edge (0.8vh in, vertically centered), six 1.3vh (≈12px) circles with 1vh gaps, #cccccc; active and hover #36e9e6 (x=1421, y=392–508).
2. **Background video** — `.hero-video video`, 1600×900 (cover, x=−80), autoplay, muted, loop, over #000000.
3. **Link bar** — `header.navbar.is-hidden-touch`, top right (x=1016–1440, 52px tall), four `a.navbar-item` with 16px side padding, 20.16px, #ffffff, Tabler icons left (ti-file, ti-link, ti-code, ti-video), rendered in Arial.
4. **Title** — `h1.title.is-1.publication-title`, inline `font-size: 7vw` (100.8px), Google Sans 600 (synthesized bold), line-height 1.1, centered (y=182–415). Line 1: a grey dog-face icon (`#changing-icon`, cycles between animal icons) and "Category‑Agnostic" with `linear-gradient(90deg, #ff6ec4, #7873f5)` text fill and 0.1em bottom padding; line 2: "Neural Object Rigging" in #ffffff.
5. **Venue** — `h1.subtitle.is-1.publication-title.myfont`, "CVPR 2025", inline `font-size: 2.5vw` (36px), padding-top 10vh (90px), Google Sans 400, rgba(255,255,255,0.9) (text at about y=508–545).
6. **Authors** — `h1.is-2` inline 2.5vw (36px), links in Google Sans #ffffff with superscripts, line-height 54px (y=577–637).
7. **Affiliations** — `h1.is-5.myfont` inline 2vw (28.8px), Google Sans #ffffff (y=637–686).
8. **Note** — `h1.is-5.myfont` inline 1.5vw (21.6px), "(* Equal Contribution)" (y=686–718).
9. **Section tabs** — `nav.tabs.is-boxed.is-fullwidth.is-size-5` in the hero foot, five equal tabs, Google Sans 20px #ffffff, padding 10px 20px, transparent, Bulma boxed corners 4px 4px 0 0 (y=849–900).

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Hall Black | #000000 | `.section`, `.hero-video` | every section background, video backing |
| White | #ffffff | `.myfont`, `.text-white`, `.section` | title line 2, venue (90%), authors, affiliations, section titles, body text, link bar, tabs |
| Candy Pink | #ff6ec4 | inline gradient start | "Category-Agnostic" title fill |
| Candy Violet | #7873f5 | inline gradient end | "Category-Agnostic" title fill |
| Aqua Dot | #36e9e6 | `.section-nav .dot.active` | active and hovered section dot |
| Dot Grey | #cccccc | `.section-nav .dot` | inactive section dots |
| Panel Ink | #202020 | `.selection-card` | demo selection cards |
| Mint Select | #3cdabd | `.selected`, `.slider .thumb` | selected card text, slider thumbs |
| Thumb Glow | #207263 | `.slider .thumb` box-shadow | glow around slider thumbs |
| Code Grey | #e0e0e0 | `code` (rendered) | BibTeX text |
| Slider Green | #16de91 | `.slider-one` | first slider gradient top (from transparent #01c9b5) |
| Slider Sky | #14a8e8 | `.slider-two` | second slider gradient top |
| Slider Blue | #1169dc | `.slider-three` | third slider gradient top |
| Panel Veil | rgba(0,0,0,0.53) | `.selection-wrapper`, `.slider-wrapper` | demo side panels |
| Viewer Veil | rgba(0,0,0,0.41) | `.model-viewer-wrapper` | 3D viewer panels |

Declared but not visible on the first screen: `.animated-gradient-text` (a four-stop #ff6ec4 / #7873f5 / #6ee7b7 / #facc15 shifting gradient) and the `gradient-text-*` instruction styles (#4e54c8, #8f94fb, #7960ca, #c672c5, #0086d4) used for "left click / right click / scroll / slide" hints in the demo.

## Tokens — Typography

- **Display:** `'Google Sans', sans-serif` on `.publication-title`, `.myfont` and the tabs; renders Google Sans 400 (only weight loaded), synthesized bold for the 600 title and `.title` headings. Substitute: Outfit 600 for the title, Outfit 400 elsewhere (close geometric forms with real weights).
- **Body:** `'Linux Biolium', sans-serif` on `html, body` (a misspelling of Linux Biolinum, not loaded); renders the default sans-serif (Arial on Windows, Helvetica on macOS). Substitute: Arimo, or load Linux Biolinum if the humanist look was the intent.
- **Icons:** Tabler Icons outline font (`ti-*`).
- **Sizes are viewport-relative** (inline `vw` and `vh`), so every value below scales with the window.

| Role | Selector | Size at 1440 / weight / line-height |
|---|---|---|
| Title | `h1.publication-title` | 7vw = 100.8px / 600 synthesized / 1.1 |
| Venue | `h1.subtitle.publication-title` | 2.5vw = 36px / 400 / 1.25 |
| Authors | `h1.is-2` | 2.5vw = 36px / 400 / 54px |
| Affiliations | `h1.is-5.myfont` | 2vw = 28.8px / 400 / 43.2px |
| Note | `h1.is-5.myfont` | 1.5vw = 21.6px / 400 |
| Section title | `h1.title.text-white` | 3vw = 43.2px / 600 synthesized |
| BibTeX / Acknowledgements title | `h1.title` | 3vh = 27px |
| Tabs | `nav.tabs.is-size-5` | 20px / 400 |
| Link bar | `a.navbar-item` | 20.16px / 400 |
| Body | `.content` | 16px / 400 / 24px |
| Code | `pre` | 14px / 21px |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Section dots | circles 1.3vh, gap 1vh, right offset 0.8vh, 0.3s color transition |
| Demo panels | 20px radius, translucent black veils, 20px top margin, 80% width |
| Selection cards | 1.5vh radius, #202020, padding 1.3vh, 80% width, first and last with 2vh outer margin |
| Vertical sliders | 0.7vw × 4vh track, 0.35vw radius, gradient from transparent to a saturated green, sky or blue; 1.4vw round #3cdabd thumb with `0 0 0.8vw 0.5vw` #207263 glow |
| Figures | no radius, `filter: brightness(90%)`, 80–100% width |
| BibTeX `pre` | transparent background, 12px radius |
| Tabs | Bulma boxed, 4px top corners, transparent |

## Layout Metrics

- **Container:** none for the hero (full width, text centered over 1344px of `.hero-body`); later sections use Bulma `.container` (max 1344px at ≥1408) inside centered flex columns; the footer block measured 971px wide (x=234–1205).
- **Sections:** each `.section` is `height: 100vh`, `display: flex`, column, centered both ways, `scroll-snap-align: start`; the scroll container snaps `y mandatory`.
- **Hero vertical rhythm:** title block starts about 182px down; 10vh (90px) padding above the venue; authors, affiliations and note stack without gaps; tabs pinned to the bottom of the hero.
- **Figures:** `max-width: 80%` (Introduction, Approach) or 90–100% (Clay-Monster pair).
- **Demo grid:** `.grid-container` three columns by two rows at 80% width, 1vh gap.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1408px | centered, text spans the viewport | 16px | 7vw (98.6px at 1408) | link bar and tabs visible |
| 1024–1407px | 24px (`.hero-body` padding) | 16px | 7vw (72–98px) | none |
| 769–1023px | 24px | 16px | 7vw (54–72px) | link bar hidden (`is-hidden-touch`); `hero-cover-touch` swaps in a mobile cover image |
| ≤768px | 24px | 16px | 48px (`is-size-1-mobile`, !important) | tabs hidden (`is-hidden-mobile`); venue and authors 24px, affiliations 20px; Bulma columns stack |

## Components

- **Gradient headline:** two lines at 7vw, Google Sans bold, line-height 1.1; first line a 1em icon (cycling animal outlines in grey) plus the gradient phrase (`linear-gradient(90deg, #ff6ec4, #7873f5)`, `background-clip: text`), second line plain white.
- **Corner link bar:** right-aligned row of four text links with outline icons, 20px, white, no buttons or borders; hidden on touch devices.
- **Section dot rail:** fixed right-edge column of small grey dots, the active section's dot in aqua #36e9e6; click to jump.
- **Bottom tab rail:** full-width Bulma boxed tabs, five equal cells, white 20px labels, transparent, sitting on the hero's bottom edge as a table of contents.
- **Slide section:** black 100vh panel, centered 3vw white title, an image at 80% width with 90% brightness, then short centered white paragraphs.
- **Demo panel:** translucent black rounded panels (20px) holding a selection list of #202020 cards (selected text #3cdabd), four 3D `model-viewer` canvases (mesh, predicted blobs, edited blobs, edited mesh) and three glowing vertical sliders.
- **BibTeX slide:** transparent `pre` with 12px radius and light grey code on black.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / authors / affiliations | Yes | giant gradient headline over a video, white meta lines |
| Venue line | Yes | "CVPR 2025" in 36px light white |
| Link buttons | Present but non-standard | top-right text links with icons, no buttons |
| Section navigation | Yes | right-edge dot rail plus bottom tab rail |
| Teaser | Present but non-standard | a background video behind the title instead of a figure |
| Introduction | Yes | full-screen slide with teaser image |
| Interactive demo | Yes | model viewers, selection list and sliders |
| Showcase ("Clay-Monster") | Yes | capture photo and animated result |
| Method | Yes | "Approach" slide with diagram |
| Results table (HTML) | No (absent from the source) | |
| Abstract | No (absent from the source) | the Introduction slide carries a short summary |
| BibTeX | Yes | transparent `pre` on black |
| Footer | Present but non-standard | the `footer` element is unset; credits sit in the last slide |

## Adapting to Other Content

- **More authors:** keep one 2.5vw line and let it wrap; above six names, drop to 2vw so the hero still fits in 100vh.
- **Results table:** give it its own 100vh slide; a white-on-black table at 16px with 1px rgba(255,255,255,0.1) rules, the header in Google Sans, best values in the pink-to-violet gradient text.
- **Long publication or news list:** a slide with a scrollable rgba(0,0,0,0.53) panel (20px radius) of #202020 cards, one per item, dates in #3cdabd.
- **Abstract:** a slide with a centered 3vw "Abstract" title and up to 70ch of 20px white text; anything longer breaks the one-screen rule.
- **No video:** use a still render darkened to 30–40% as the hero background so the white and gradient type keep their contrast.

## Do's and Don'ts

- Do keep every section black and exactly one screen tall; the snap is the format.
- Do reserve the pink-to-violet gradient for the headline phrase (and at most one other highlight).
- Do keep navigation as text: corner links, dots and tabs, no filled buttons.
- Don't use fixed pixel sizes for display type here; the source scales everything with vw.
- Don't depend on the misspelled body font; name the face you want.
- Don't place long prose in one slide; split it into more slides instead.

## Surfaces

Black everywhere; a dim looping video behind the hero; translucent black panels with 20px corners and #202020 cards in the demo; images dimmed to 90%.

## Imagery

A dark textured looping video behind the title, a teaser figure of animals and rigs, 3D meshes and colored Gaussian blob rigs in model viewers, photos of a clay figure and its animated digital twin, an approach diagram.

## Layout

Full-screen snap slides, each centered vertically and horizontally, with a fixed dot rail on the right. The scroll container makes the document itself one viewport tall; content height is about 5,300px across the slides.

## Agent Prompt Guide

Quick colors: background #000000, text #ffffff, title gradient #ff6ec4 → #7873f5, active dot #36e9e6, dots #cccccc, cards #202020, selection #3cdabd, panel veil rgba(0,0,0,0.53).

1. "Build a launch hero: black full-screen section with a muted looping background video; centered two-line title at 7vw in Google Sans bold with line-height 1.1, first line an outline icon plus a phrase filled with linear-gradient(90deg, #ff6ec4, #7873f5) via background-clip text, second line #ffffff; 10vh below, a 2.5vw rgba(255,255,255,0.9) venue line, 2.5vw white author names, 2vw affiliations and a 1.5vw note."
2. "Add navigation: a top-right row of four 20px #ffffff text links with outline icons; a fixed right-edge column of six 1.3vh circles with 1vh gaps in #cccccc, the active one #36e9e6; and a full-width row of five equal transparent tabs with 20px #ffffff labels pinned to the hero's bottom edge."
3. "Make a demo slide: black 100vh flex column, centered 3vw #ffffff title; a panel with rgba(0,0,0,0.53) fill and 20px radius holding #202020 cards (1.5vh radius, padding 1.3vh) whose selected label turns #3cdabd; vertical sliders 0.7vw wide and 4vh tall with a gradient to #16de91 and a 1.4vw #3cdabd round thumb glowing with 0 0 0.8vw 0.5vw #207263."

## Similar Pages

- "Birth and Death of a Rose" (rose4d) and CUT3R project pages, credited as template sources.
- Product-style research pages built as full-screen scroll-snap slide decks.

## Quick Start

```css
:root {
  --bg: #000000;
  --text: #ffffff;
  --title-gradient: linear-gradient(90deg, #ff6ec4, #7873f5);
  --dot: #cccccc;
  --dot-active: #36e9e6;
  --card: #202020;
  --select: #3cdabd;
  --panel-veil: rgba(0, 0, 0, 0.53);
  --viewer-veil: rgba(0, 0, 0, 0.41);
  --font-display: 'Google Sans', 'Outfit', sans-serif;
  --font-body: 'Arimo', Arial, sans-serif;
  --title-size: 7vw;
  --venue-size: 2.5vw;
  --section-title-size: 3vw;
  --panel-radius: 20px;
}
html, body { height: 100%; overflow: hidden; background: var(--bg); }
.scroll-container { height: 100vh; overflow-y: scroll; scroll-snap-type: y mandatory; }
.section { height: 100vh; scroll-snap-align: start; display: flex; flex-direction: column; justify-content: center; align-items: center; }
```

## Provenance

- **URL:** https://guangzhaohe.com/canor (redirects to https://www.guangzhaohe.com/canor/)
- **Paper:** Category-Agnostic Neural Object Rigging (arXiv 2505.20283), Guangzhao He, Chen Geng, Shangzhe Wu, Jiajun Wu.
- **Venue:** CVPR 2025 (stated on the page).
- **Selection reason:** the arXiv comment states CVPR 2025 acceptance and links the page; chosen for its immersive dark identity: gradient-accent title with an icon, minimal top-right link bar, side dot navigation and a bottom section rail.
- **Template credit:** the last slide says the website template was modified from Birth and Death of a Rose and CUT3R; it also loads that project's CSS and JS directly from chen-geng.com/rose4d.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share and loaded-font list, 1440 first-viewport and tall screenshots (hero only, because the page scrolls inside a container), `style.css`, inline styles and section markup in the page HTML; 2026-10-28.
