# REPA Forest Initials — Style Reference

> A light Titillium page where the acronym grows out of the title in forest green.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide screenshots, and the page's single inline `<style>` block (a Jon Barron / Ben Mildenhall-lineage template). No CSS framework is loaded. Color share is measured on the first 1440×900 viewport.

## Overview

A 980px body centred on white, set entirely in Titillium Web at a light 300 weight on black. The two-line 40px title colours the letters that make the acronym ("**Rep**resentation **A**lignment") in forest green #0e710e using `<font>` tags, and the same green carries every link: author names, the icon links "Paper" and "Code", and inline references. Under a bold 23px "ICLR 2025", the teaser is a tight 6×2 grid of generated ImageNet samples (one PNG, 948px). Sections are plain: a 29.75px regular h2, a 1px #dddddd rule under "News", justified 17px body, figure grids side by side (diagram beside FID chart, then three-up result plots), and one grey rounded callout box for the key claim. A grey #eeeeee BibTeX block ends the page.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 70.4%, then the sample grid: olive-brown #716855 8.6%, dark umber #3b2c24 6.8%, sage #9daa95 5.1%, tan #dec9a8 4.2%, off-white #f4f5f1 3.1%. Text and green links are under 1% each.

Anatomy in DOM order (body x=230–1210, content x=246–1194):

1. **Title** — `h1` in `.paper-title`, 40px / 500 declared (renders with the 400 face) / 46px, #000000, centred, two lines (y=36–128); "Rep" and "A" wrapped in `<font color="#0E710E">`. Margin 26.8px.
2. **Authors** — `.author-row-new a`, inline-block, 20px / 300, #0e710e, padding 4px, comma separated, superscripts 12px #313436; one line (y=156–195).
3. **Affiliations** — two `div.affiliations` lines, 17px / 300, #000000, superscript keys and `&nbsp;` spacing; second line "*Equal Advising." (about y=200–245).
4. **Venue** — `.venue`, 23px / 700 (renders with the 600 face), #000000, centred, margin-top 18px (`.affil-row`), about y=285.
5. **Links** — `.paper-btn-parent`, flex, centred, gap 25px, margin 16px 0: "Paper" (FA file icon) and "Code" (FA GitHub), 20px / 300, #0e710e (y=323–354).
6. **Teaser** — `.figure img`, 948×312, y=370; 12 square samples in two rows with thin white gaps inside the PNG. Gap 32px.
7. **News** — `section` (32px margin), h2 29.75px / 400 at y=714, 1px #dddddd `hr`, two lines each led by a 24px Material Icons "event" glyph.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | (browser default) | page |
| Ink | #000000 | (browser default) | title, headings, body, venue, affiliations |
| Forest | #0e710e | `a:link`, `.green`, `<font color>` | acronym letters in title, author links, Paper/Code, inline links |
| Teal Hover | #208799 | `a:hover` | inline link hover |
| Coral Hover | #ff8563 | `.paper-btn:hover`, `.github-btn:hover` | Paper/Code hover (with 2px lift) |
| Superscript Slate | #313436 | `.author-row-new sup` | author affiliation numbers |
| Rule Grey | #dddddd | `hr` | 1px rule under section titles |
| Callout Grey | rgba(40,40,40,0.2) | `blockquote` | key-claim box fill (renders about #d4d4d4) |
| Code Grey | #eeeeee | `#bibtex pre` | BibTeX block |
| Caption Grey | #666666 | `.caption` | figure captions where used |
| Ember | #d35400 | `.orange` | bold orange emphasis class (declared, sparingly used) |

## Tokens — Typography

- **Sans:** declared `"Titillium Web", "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif`; Google Fonts request 300, 400, 600 with italics. Rendered: Titillium Web 300, 300i, 400, 600. Weights 500 and 700 fall back to the 400 and 600 faces. Substitute: Exo 2 (light weights) or Rajdhani for a closer squared look.
- **Mono:** browser `monospace` for BibTeX (14px).
- **Icons:** Font Awesome 6 beta (file, GitHub), Material Icons (event).

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `h1` | 40px / 500 (400 face) / 1.15em |
| Venue | `.venue` + `<b>` | 23px / 700 (600 face) |
| Authors | `.author-row-new a` | 20px / 300 |
| Links | `.paper-btn-parent` | 20px / 300 |
| Section title | `h2` | 29.75px (1.75em) / 400, margin 16px 0 4px |
| Subsection | `h3` | 19.89px / 600, margin 16px 0 4px |
| Body | `body`, `section` | 17px / 300, justified; `p` line-height 1.25em (21.25px) |
| Caption | `.caption` | 16px, #666666 |
| BibTeX | `#bibtex pre` | 14px monospace |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Callout box | `blockquote`, radius 10px, padding 1px 5px, margin 2px 0, fill rgba(40,40,40,0.2), no border |
| BibTeX block | radius 3px, padding 16px, #eeeeee |
| Rules | `hr` 1px #dddddd, margin 0 |
| Figures and teaser | square corners, no border or shadow |
| Link hover | `transform: translateY(-2px)` on Paper/Code |
| Shadows | none |

## Layout Metrics

- **Container:** `body { width: 980px; margin: auto }` at ≥980px; `.container` adds 16px side padding, so content is 948px. Below 980px the body is fluid with 8px default margins plus 16px padding.
- **Hero:** title margins 26.8px; venue 18px top; links block margin 16px 0; teaser directly below at full 948px.
- **Sections:** `section` margin 32px 0, `clear: both`; h2 then 4px gap then `hr`; `.row` margin 16px 0.
- **Figure grids:** `.image-grid` two columns `1fr 1.25fr`, gap 10px (diagram beside chart); `.image-grid-three` three equal columns, gap 10px, width 90% centred; `.image-grid-tab` `1fr 1.22fr` at 90%.
- **Legacy floats:** `.column` 16.666% and `.column3` 33.333% with 5px padding.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥980px | (viewport − 980)/2 + 16px | 17px | 40px | all grids side by side |
| 621–979px | 8px + 16px | 17px | 40px | body goes fluid; grids scale |
| ≤620px | 24px | 17px | 40px | `.download-thumb` hidden; `.paper-stuff` full width |
| ≤500px | 24px | 17px | 40px | `.column` and `.column3` stack to 100%; CSS grids still keep their columns |

## Components

- **Acronym title:** centred 40px Titillium; the letters forming the acronym are coloured #0e710e, the rest #000000, so the name reads inside the full title.
- **Icon text links:** `a.paper-btn` / `a.github-btn` in a centred flex row (gap 25px), 20px / 300 #0e710e with a Font Awesome icon left; hover turns #ff8563 and lifts 2px. No background or border.
- **News row:** each item a 24px Material Icons "event" glyph (vertical-align -6px), then "[Mon YYYY]" and the text, 17px.
- **Section head:** 29.75px / 400 h2 left aligned, a 1px #dddddd rule directly beneath in the News section.
- **Key-claim callout:** `blockquote` with rgba(40,40,40,0.2) fill, 10px radius, tight 1px 5px padding, 17px text with bold phrases.
- **Side-by-side figure:** `.image-grid` 1fr / 1.25fr, 10px gap: method diagram left, FID-vs-iterations chart right.
- **BibTeX:** `#bibtex pre`, #eeeeee, 16px padding, 3px radius, 14px mono.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title with coloured acronym | Yes | green initials in a black title |
| Authors / affiliations / equal-advising note | Yes | green links, black 17px affiliation lines |
| Venue line | Yes | bold 23px "ICLR 2025" |
| Link buttons | Present but non-standard | two green icon text links |
| Teaser | Yes | 6×2 sample grid PNG |
| News | Yes | Material "event" icons with bracketed dates |
| Overview with callout | Yes | justified text, grey rounded blockquote |
| Method + headline chart | Yes | 2-column image grid |
| Observations / results charts | Yes | three-up plot grids |
| Results table | Present but non-standard | tables are images in `.image-grid-tab` |
| BibTeX | Yes | #eeeeee pre |
| Footer / template credit | No (absent from the source) | |

## Adapting to Other Content

- **Acronym without obvious initials:** colour the syllables that spell it (as "Rep" here); if none fit, colour the whole acronym prefix before the colon.
- **More authors:** keep inline-block 20px links with 4px padding; they wrap centred; keep equal-contribution notes on their own line.
- **HTML results table:** 17px Titillium 300, header 600, 1px #dddddd rules top and bottom, best numbers bold #0e710e, inside the 90% grid width.
- **Longer news list:** keep the icon + bracketed date pattern; past five items, show the latest five and collapse the rest.
- **More links:** add icon text links to the same flex row (Models, Demo), 25px gap, same hover.

## Do's and Don'ts

- Do let the acronym's green letters be the only colour in the title.
- Do keep body at weight 300 and headings at 400 so the page stays light.
- Do place a diagram and its headline chart side by side at the top of the overview.
- Don't turn the text links into filled buttons; the page has no buttons.
- Don't use the coral hover colour anywhere except the hero links.
- Don't request weights that are not loaded; 500 and 700 here silently become 400 and 600.

## Surfaces

White page; one grey translucent callout, one #eeeeee BibTeX block, 1px #dddddd rules. No bands, cards or shadows.

## Imagery

A grid of photorealistic ImageNet samples as hero (animals, food, objects), a light block diagram with green DiT/SiT blocks and a grey encoder, line charts in red, blue and green on white, and table images.

## Layout

Single 948px column, centred hero, left-aligned sections with justified text and 2- or 3-up figure grids. Rendered height about 4,750px.

## Agent Prompt Guide

Quick colors: text #000000 on #ffffff, accent #0e710e, link hover #208799, hero-link hover #ff8563, rule #dddddd, callout rgba(40,40,40,0.2), code #eeeeee.

1. "Create a title: centred Titillium Web 40px, line-height 1.15em, two lines in #000000, with the letters that spell the acronym coloured #0e710e; below, inline-block author links at 20px / 300 in #0e710e with 4px padding and 12px #313436 superscripts, then a bold 23px venue line."
2. "Add hero links: a centred flex row with 25px gap of icon-plus-text links ('Paper', 'Code') at 20px / 300 #0e710e, no background; on hover turn #ff8563 and translate up 2px."
3. "Write a key-claim callout: a blockquote with background rgba(40,40,40,0.2), 10px radius, padding 1px 5px, 17px Titillium 300 text with two bold phrases, placed between justified paragraphs."

## Similar Pages

- Sihyun Yu's other project pages and KAIST ALIN Lab pages using the same Titillium template.
- Pages in the Jon Barron / Ben Mildenhall lineage with a 980px body and plain section rules.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #000000;
  --accent: #0e710e;
  --link-hover: #208799;
  --hero-link-hover: #ff8563;
  --sup: #313436;
  --rule: #dddddd;
  --callout: rgba(40, 40, 40, 0.2);
  --code-bg: #eeeeee;
  --caption: #666666;
  --font-sans: "Titillium Web", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --title-size: 40px;
  --h2-size: 1.75em;
  --body-size: 17px;
  --body-weight: 300;
  --page-width: 980px;
}
```

## Provenance

- **URL:** https://sihyun.me/REPA/
- **Paper:** Representation Alignment for Generation: Training Diffusion Transformers Is Easier Than You Think (arXiv 2410.06940), Sihyun Yu et al.
- **Venue:** ICLR 2025 (stated on the page).
- **Selection reason:** arXiv comment states acceptance at ICLR 2025; project page linked in the comment.
- **Template credit:** none stated on the page.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share, 1440 screenshots (first viewport and tall), the inline style block and page HTML; 2026-10-28.
