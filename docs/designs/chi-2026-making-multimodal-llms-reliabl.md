# ExChart — Style Reference

> A lab notebook opened to its best page: a framed video like a monitor bezel, emoji in the headline, and every figure pinned with a soft shadow.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, the page's `static/css/index.css`, inline `style` attributes on the figures, and `index.html`. The page is built on the Nerfies template (Bulma 0.9 with `bulma-carousel` and `bulma-slider` loaded but unused), so Bulma defaults govern most spacing; the values below are those probed on the rendered elements. The video poster shows a loading spinner drawn into its first frame, so the screenshot has a thin black ring over the title slide.

## Overview

A centred, single-column Nerfies-style page (about 5,000px tall) on white. The hero has a three-line 48px Google Sans title that opens with two emoji (📈 🔢), a row of seven sky-blue author links with superscripts, a gray affiliation line, a plain "CHI 2026" line in 24px, and two dark rounded Bulma buttons (Paper, Code & Data). The first section is a 960px video framed like a monitor: a 4px #2b2b2b border, 8px radius and a 0 6px 18px shadow. Then centred 32px section headings introduce short justified paragraphs and full-width figures with 5px radii and soft 0 4px 12px shadows: TL;DR, ExChart-Bench (pipeline figure, a bulleted Key Features list with bold leads, a colorful heat-map results panel), Training Framework, Mixed-Initiative Workflow, Abstract and BibTeX (gray pre block). A light gray footer credits Nerfies.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 63.0% and near-whites #fefefe 17.2%, #fcfdfd 3.2%, #fffffe 0.4%, #fefdfb 0.4%, #fdffff 0.2% (page and the video's white title slide); pale blue-gray #e6ebef 9.0% and slate #828a95 6.6% (anti-aliased text, the slide's diagrams and the dark video border). The sky-blue author links and dark buttons are too small to form clusters.

Anatomy in DOM order (desktop 1440px; `section.hero > .hero-body` padding 48px 24px; `.container.is-max-desktop` 960px from x=240; everything centred):

1. **Title** (`h1.title.is-1.publication-title`, y=48, 162px tall): "📈🔢Making Multimodal LLMs Reliable Chart Data Extractors: A Benchmark and Training Framework" in three lines, Google Sans 48px / 600 (synthetic bold; only the 400 face loads), line-height 1.125, #363636. Margin-bottom 24px.
2. **Authors** (`.publication-authors.is-size-5`, y=234, 35px tall): seven links in Google Sans 20px / 400, hsl(204, 86%, 53%) = #209cee (forced with `!important`), each followed by a #4a4a4a superscript digit; author blocks separated by spaces.
3. **Affiliations** (y=269, 35px tall): Google Sans 20px #4a4a4a, "¹Zhejiang University" and "²Guangdong University of Technology" separated by four non-breaking spaces.
4. **Venue** (`.is-size-4`, y=303, 36px tall): "CHI 2026", Google Sans 24px / 400 #4a4a4a. No badge styling.
5. **Buttons** (`.publication-links`, y=356, 40px tall; next Bulma column adds 12px padding): Paper (FA file-pdf) and Code & Data (FA GitHub), Bulma `is-dark is-rounded`: #363636 fill, white Noto Sans 16px, padding 7px 20px, 5px vertical margins. Hero ends at y=461.
6. **Video** (`#replay-video`, section padding 48px 24px, y=509, 960×544): 4px solid #2b2b2b border, radius 8px, box-shadow 0 6px 18px rgba(0,0,0,0.25); browser controls along the bottom.

The TL;DR section heading follows at y=1155.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | (Bulma `$white`) | page background, button labels |
| Heading Gray | #363636 | (Bulma `$grey-darker`) | title, section headings, button fill |
| Body Gray | #4a4a4a | (Bulma `$grey-dark`) | paragraphs, list items, affiliations, venue line, superscripts, BibTeX text |
| Sky Link | #209cee | (literal, hsl(204, 86%, 53%) !important) | author name links |
| Bulma Link | #3273dc | (Bulma `$link`) | footer links (Nerfies, license) |
| Monitor Frame | #2b2b2b | (literal, `#replay-video`) | 4px video border |
| Code Gray | #f5f5f5 | (Bulma `$white-ter`) | BibTeX pre background |
| Footer Gray | #fafafa | (Bulma `$white-bis`) | footer background |
| Button Hover | #2f2f2f | (Bulma `.button.is-dark:hover`) | dark button fill on hover |
| Bulma Rule | #dbdbdb | (Bulma `$grey-lighter`) | default table and input borders (no table on this page) |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display (hero) | 'Google Sans', sans-serif (`.publication-title`, `.publication-authors`) | Google Sans 400 only; 600 is synthesized | Product Sans or Outfit |
| Body | 'Noto Sans', sans-serif | Noto Sans 400; bold synthesized | Open Sans |
| Code | Bulma monospace | system monospace (Consolas on Windows) | Source Code Pro |
| Icons | Font Awesome (local `fontawesome.all.min.css` + JS), Academicons | SVG icons injected by the FA script | — |

The Google Fonts request also names Castoro, which is not applied anywhere.

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title` | Google Sans 48px / 600 / 1.125 | #363636 |
| Authors | `.publication-authors.is-size-5 a` | Google Sans 20px / 400 / 1.5 | #209cee |
| Affiliations | `.publication-authors.is-size-5` | Google Sans 20px / 400 | #4a4a4a |
| Venue | `.publication-authors.is-size-4` | Google Sans 24px / 400 | #4a4a4a |
| Section heading | `h3.title.is-3`, `h2.title.is-3` | Noto Sans 32px / 600 / 1.125, centred | #363636 |
| Subheading | `h3.title.is-4` | Noto Sans 24px / 600 / 1.125, centred | #363636 |
| BibTeX heading | `h2.title` | 28px / 600, left aligned | #363636 |
| Body | `.content p`, `.content li` | Noto Sans 16px / 400 / 1.5, justified | #4a4a4a |
| Button | `.button.is-dark` | Noto Sans 16px / 400 | white |
| BibTeX | `pre` | 14px / 1.5 monospace | #4a4a4a |
| Footer | `.footer .content p` | 16px / 1.5 | #4a4a4a, links #3273dc |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Buttons | 290486px (Bulma rounded) | 1px transparent | none; hover Bulma darkens to #2f2f2f |
| Video | 8px | 4px solid #2b2b2b | 0 6px 18px rgba(0,0,0,0.25) |
| Figures | 5px (inline style) | none | 0 4px 12px rgba(0,0,0,0.1) (inline style) |
| BibTeX pre | 0 | none | none |
| Footer | 0 | none | none |

## Layout Metrics

- **Container**: Bulma `.container.is-max-desktop`, max-width 960px at ≥1024px (x=240 to 1200 at 1440).
- **Hero**: `.hero-body` padding 48px 24px; the title, authors and venue sit in one Bulma column (12px padding), the buttons in a second column below it; hero renders 461px tall.
- **Sections**: Bulma `.section` padding 48px 24px; sections stack with no extra margin, so headings sit 96px below the previous section's last element.
- **Headings**: `.title` margin-bottom 24px; empty `h3.title.is-4` under TL;DR renders 0px tall but keeps its 24px margin.
- **Figures**: inline `max-width: 100%`, rendered 960px wide inside `.content.has-text-justified`.
- **Lists**: `.content ul` indents 32px (items at x=272), 4px between items.
- **BibTeX**: pre padding 17.5px 21px (1.25em 1.5em at 14px), full container width.
- **Footer**: `.footer` padding 48px 24px 96px, inner `.column.is-8` 888px wide (x=276).

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px | container 960px centred | 16px | 48px | hero columns stack (title column, then buttons column) |
| 769–1023px | container fluid inside 24px section padding | 16px | 48px | same |
| ≤768px | 24px section padding | 16px | 48px (Bulma does not scale `is-1`) | Bulma columns become block; buttons wrap |

## Components

- **Dark pill button** (`a.external-link.button.is-normal.is-rounded.is-dark`): #363636 fill, white Noto Sans 16px, padding 7px 20px, radius 290486px, height 40px, Font Awesome icon in a 24px `.icon` span on the left (margin 0 4px 0 -9px). Hover: Bulma darkens the fill to #2f2f2f.
- **Framed video** (`#replay-video`): native controls, 4px solid #2b2b2b border, radius 8px, shadow 0 6px 18px rgba(0,0,0,0.25), max-width 100% (960px).
- **Figure** (inline-styled `img`): full container width, radius 5px, shadow 0 4px 12px rgba(0,0,0,0.1), no caption element; any explanation sits in the paragraph above.
- **Section heading**: centred Noto Sans 32px / 600 #363636, 24px below; subheadings 24px / 600.
- **Feature list**: `.content ul` disc bullets, 16px #4a4a4a, each item led by a bold phrase and a colon.
- **BibTeX**: `h2.title` 28px left aligned, then a #f5f5f5 pre at 14px monospace with 17.5px 21px padding, no radius.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title with emoji | yes | 48px Google Sans, two emoji before the words |
| Authors / affiliations | yes | sky-blue links, gray affiliation line |
| Venue | present but non-standard | plain 24px "CHI 2026" text line, no badge |
| Link buttons | yes | two dark Bulma pills |
| Video teaser | yes | 960px video with dark 4px frame |
| TL;DR | yes | centred heading, one justified paragraph |
| Benchmark / pipeline figures | yes | shadowed full-width images |
| Key features list | yes | bullet list with bold leads |
| Results | present but non-standard | a results heat-map image, not an HTML table |
| Abstract | yes | placed near the end, after the method sections |
| BibTeX | yes | Bulma gray pre |
| Navbar | absent from the source | the Nerfies navbar is in the markup but `display: none` |
| Footer | yes | #fafafa, template credit |

## Adapting to Other Content

- **More authors**: keep them in the 20px Google Sans line with #209cee links and wrap within 960px; add affiliation digits as superscripts and list institutions on one #4a4a4a line.
- **A results table**: use Bulma `.table` in the 960px column: 16px Noto Sans #4a4a4a, header 600 #363636, 1px #dbdbdb row rules (Bulma default), best values bold. Keep it inside `.content` so it inherits the justified column.
- **Long publication or news lists**: a `.content ul` with bold leads, exactly like Key Features, 16px with 4px item spacing.
- **An award**: the template's `.publication-awards` rule (bold #ff3860) is declared but unused here; if added, place it under the venue line at 24px.
- **More figures**: keep each full-width with radius 5px and shadow 0 4px 12px rgba(0,0,0,0.1); introduce it with a 24px subheading.

## Do's and Don'ts

- Do keep the hero centred in Google Sans and the body in Noto Sans.
- Do frame the main video with the 4px #2b2b2b border and 8px radius.
- Do give every figure the same soft 5px-radius shadow.
- Do keep author links sky blue #209cee and buttons dark #363636.
- Don't add a colored hero band; the page is white from top to bottom.
- Don't caption figures under the image; text goes in the paragraph before.
- Don't mix more emoji into headings; they appear only at the start of the title.

## Surfaces

White page throughout; #f5f5f5 for the BibTeX block and #fafafa for the footer. Depth comes only from the video shadow (0 6px 18px at 25%) and the lighter figure shadows (0 4px 12px at 10%).

## Imagery

A narrated slide video (white title slide with institution logos and a CHI'26 mark), a pastel pipeline diagram in blue, green and violet panels, a results figure combining bar charts and red-to-green heat-map tables, and a training-framework diagram. Figures are wide, light and dense with small labels.

## Layout

A 960px centred column from top to bottom: hero, video, then sections each with a centred heading, a justified paragraph and a full-width figure. The Abstract comes after the method sections rather than at the top.

## Agent Prompt Guide

Quick colors: background #ffffff, headings and buttons #363636, body #4a4a4a, author links #209cee, video frame #2b2b2b, code #f5f5f5, footer #fafafa.

1. "Build a centred hero in a 960px column with 48px 24px padding: title Google Sans 48px / 600, line-height 1.125, #363636, may start with two emoji; authors Google Sans 20px links in #209cee with #4a4a4a superscripts; affiliations 20px #4a4a4a; venue as a plain 24px line; two buttons with #363636 fill, white 16px text, padding 7px 20px, fully rounded, Font Awesome icons on the left."
2. "Add a framed video under the hero: 960px wide, border 4px solid #2b2b2b, radius 8px, box-shadow 0 6px 18px rgba(0,0,0,0.25), section padding 48px 24px."
3. "Make a content section: centred Noto Sans 32px / 600 #363636 heading with 24px below, a 16px / 1.5 justified #4a4a4a paragraph, then a full-width figure with radius 5px and box-shadow 0 4px 12px rgba(0,0,0,0.1); subheadings 24px / 600; bullet lists with bold leads."

## Similar Pages

- Nerfies-template project pages with Google Sans titles and dark rounded buttons.
- Benchmark papers whose project page leads with a framed narrated video.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --heading: #363636;
  --text: #4a4a4a;
  --author-link: #209cee;
  --link: #3273dc;
  --video-frame: #2b2b2b;
  --code-bg: #f5f5f5;
  --footer-bg: #fafafa;
  --font-display: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --container: 960px;
  --section-pad: 48px 24px;
  --figure-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  --video-shadow: 0 6px 18px rgba(0, 0, 0, 0.25);
}
```

## Provenance

- **URL**: https://ExChart.github.io/
- **Paper**: Making Multimodal LLMs Reliable Chart Data Extractors: A Benchmark and Training Framework (arXiv 2606.29808), Yuchen He, Peizhi Ying, Liqi Cheng, Kuilin Peng, Yuan Tian, Dazhen Deng, Yingcai Wu.
- **Venue**: CHI 2026.
- **Selection reason**: the arXiv comment states acceptance at CHI 2026; the project page is linked in the paper body (arXiv HTML).
- **Template credit**: footer reads "The style of this website is adapted from Nerfies under a CC BY-SA 4.0 License"; Bulma 0.9 base.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted computed-style probes of hero lines, content paragraphs, figures and footer, the 1440×900 and full-page screenshots, and `static/css/index.css` and `index.html` read directly, on 2026-10-28.
