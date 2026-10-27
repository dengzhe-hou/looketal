# Navy Keycap Ledger — Style Reference

> A tidy navy research ledger signed in brush script, with two cats peeking over the tab bar and gold stamps on every milestone.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share and DOM boxes from `tools/computed_style.py`, plus a selector probe of the nav, news timeline, publication cards, year headers, awards and footer), the 1440×900 and full-page screenshots, two screenshots scrolled to y=1050 and y=8450 (sticky nav, publication cards, awards), and the single inline `<style>` block of `index.html` read directly. Only Kaushan Script 400 and Ma Shan Zheng 400 load as web fonts; the body stack starts with "Avenir Next", which is not loaded, so the capture renders in Segoe UI (on macOS it would be Avenir Next). Publication cards start at opacity 0 and fade in as they scroll into view. The page is 16,639px tall at 1440 wide. v2 rewrite: v1 was written without viewing the render and said inline links were NVIDIA green; they render #2b6cb0, and green is only the "NVIDIA" word.

## Overview

A hand-built single-file page in a 1100px column on white. The header is a grid: a 160px square photo with 8px radius and a soft double shadow on the left; to its right the name "Liwei Jiang" in Kaushan Script brush lettering at 35.2px with "姜力炜" in Ma Shan Zheng beside it, both navy #1a365d, followed on the same line by "Research Scientist at NVIDIA" in 18.4px/500 slate with "NVIDIA" in green #76b900; under it a row of frost-blue keycap pills (email, five icon buttons, Bio, CV) with a hard 3px #ccdcec bottom edge. Two cut-out cat photos sit at the right edge of the header and overlap the top of the nav. The nav is a white tab bar with a 2px #2b6cb0 border on the left, right and bottom, 12px bottom corners and a navy-tinted shadow; it is sticky and highlights the current section with a #e6f1fb pill. Below: a justified bio, a "Topics" list with yellow-highlighter heading and blue-highlighter phrases and ring bullets, keycap interest tags, then sections with 28px/600 navy h2s underlined by a 36px navy-to-sky gradient bar. News is a vertical timeline with gold dots and gold dates and corner-cut UPCOMING and AWARD badges; publications are white cards grouped under gold year headers with a gold side tab; awards use small gold trophy icons and a left date column.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 71.1% plus #feffff 2.9% and #fffffb 0.8%; blue-grey #bbc7d2 6.4% (nav border and shadow, keycap edges, photo); frost #f9fbfd 6.2% (keycaps and highlighter bands); photo and cat neutrals #eceeec 4.8%, #9a958e 4.0%, #d7d7d0 3.9%. Navy text, blue links and gold dates are each under 1%.

Anatomy in DOM order (desktop 1440px; `.container` x=170, 1100px, padding 12px 32px 32px, so content starts at x=202):

1. **Header grid** (`header`, y=12, 1036×181px): `grid-template-columns: auto 1fr`, gap 40px, items centred, `overflow: hidden`.
2. **Photo** (`img.profile-img`, x=202, y=12): 160×160px, 8px radius, shadow 0 4px 16px rgba(0,0,0,0.15), 0 2px 6px rgba(0,0,0,0.10), brightness(1.15).
3. **Name line** (`.header-content h2`, x=402, y=39, margin-top -24px): Kaushan Script 35.2px/400 #1a365d "Liwei Jiang", then Ma Shan Zheng 35.2px "姜力炜", then `.title` 18.4px/500 #4a5568 with 16px left margin, "NVIDIA" 600 #76b900. Gap 7px.
4. **Keycap row** (`.social-btn-row`, y=104): email pill 224×33px and five 41×33px icon pills, then Bio and CV pills; 14.08px/500 #1a365d, 20px radius, frost gradient, gaps 7–8px.
5. **Cats** (`.loafy-wrap` x=998, 140×200px; `.loopy-wrap` x=1118, 120×172px): cut-out photos, bottoms clipped by the header and resting on the nav.
6. **Sticky nav** (`nav`, x=186, y=193, 1068×55px, margins -16px to overhang the column): white, border 2px #2b6cb0 except top, radius 0 0 12px 12px, shadow 0 4px 16px rgba(26,54,93,0.10), 0 2px 6px rgba(26,54,93,0.08), padding 13.6px 32px; ten centred links 16px/500 #2b6cb0, padding 6.4px 11.2px, 6px radius, gap 2.4px. Gap 32px.
7. **Bio** (`p.about-text`, y=280): 15.68px/400, line-height 1.5, justified, #2d3748, links #2b6cb0, bold phrases. Gap 8px between paragraphs.
8. **Topics** (`.topics-heading`, y=414): 16px/600 #1a365d on a yellow #ffe98a highlighter band (lower 40%); list items 14.72px with 10px ring bullets (2px #2b6cb0) and `.topic-hl` phrases on a #e4eefb band.
9. **Interest tags** (`.interest-tag`, y=672): keycap pills, same recipe as the social row.
10. **News heading** (`h2`, y=714): 28px/600 #1a365d with a 36×3px gradient bar below; timeline starts at y=790.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Harbor Navy | #1a365d | --primary-color | name, h2 headings, publication titles, award names, keycap text, news text |
| Seaboard Blue | #2b6cb0 | --secondary-color | nav border, nav links, inline links, venue text, award dates, ring bullets, h3 sub-headings |
| Signal Blue | #3182ce | --accent-color | publication link buttons (PDF, Project Page) text and outline |
| Sky Blue | #4299e1 | (literal) | end of the h2 underline gradient and the tag hover gradient |
| Slate Ink | #2d3748 | --text-color | body text, bio |
| Slate Grey | #4a5568 | --dark-gray | title line, author lists, footer |
| NVIDIA Green | #76b900 | (literal) | the word "NVIDIA" in the title line |
| Trophy Gold | #ffcc00 | --yellow-color | news dates and dots, year headers, quote marks, trophy and badge gradients |
| Badge Umber | #5b4500 | (literal) | text on gold UPCOMING badges |
| Award Red | #ff2600 | --red-color | AWARD badge gradient, `.paper-award` text such as "(Oral, Top 0.4%)" |
| Card Edge | #eef1f5 | (literal) | publication card border |
| Hairline | #e2e8f0 | --border-color | footer top border, card hover border, end of the news rail gradient |
| Nav Active | #e6f1fb | (literal) | nav link hover and active pill |
| Keycap Frost | #f5faff | (literal) | keycap gradient start (to #eef5fd) |
| Keycap Edge | #ccdcec | (literal) | hard 3px bottom shadow of keycaps |
| Gold Light | #ffe066 | (literal) | top of the UPCOMING badge and year-tab gradients |
| Gold Deep | #f2b400 | (literal) | bottom of the UPCOMING badge and year-tab gradients |
| Red Light | #ff5a3c | (literal) | start of the AWARD badge gradient |
| Red Deep | #db1f00 | (literal) | end of the AWARD badge gradient |
| Yellow Highlighter | #ffe98a | (literal) | topics heading band |
| Blue Highlighter | #e4eefb | (literal) | `.topic-hl` phrase band |
| Photo Mist | #f7fafc | --light-gray | photo placeholder background |

Declared but not visible: `--orange-color` #ff5c00 (only on the unused `.nav-cv-btn` hover), the commented alternative name fonts (Parisienne, Dancing Script, Great Vibes, Playfair Display), and the `.nav-monogram` and `.nav-divider` rules, which have no element in the nav.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (everything) | 'Avenir Next', -webkit-system-fallback, 'Segoe UI', Roboto, sans-serif | not a web font; Segoe UI in the Windows capture, Avenir Next on macOS | Nunito Sans |
| Name (English) | 'Kaushan Script', cursive (Google Fonts) | Kaushan Script 400 | Kaushan Script |
| Name (Chinese) | 'Ma Shan Zheng', cursive (Google Fonts) | Ma Shan Zheng 400 | Ma Shan Zheng |
| Quote mark | Georgia, serif | system Georgia | Georgia |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `.header-content h2 .name-en` | 35.2px / 400 / 1.6 | #1a365d |
| Title line | `.title` | 18.4px / 500 | #4a5568 (NVIDIA 600 #76b900) |
| Nav link | `nav a` | 16px / 500 | #2b6cb0; active #1a365d on #e6f1fb |
| Section h2 | `section > h2` | 28px / 600 / 1.6 | #1a365d |
| Sub-heading h3 | `h3` (Education, Experience) | 20.8px / 700 | #2b6cb0 |
| Bio | `.about-text` | 15.68px / 400 / 1.5, justified | #2d3748 |
| Topics heading | `.topics-heading` | 16px / 600 | #1a365d |
| Topic item | `.topic-list li` | 14.72px / 400 / 1.5 | #2d3748 |
| Keycap | `.interest-tag`, `.social-btn-row a` | 14.08px / 500 | #1a365d |
| News text | `.news-item` | 14.4px / 400 | #1a365d |
| News date | `.news-date` | 14.4px / 700 | #ffcc00 |
| News badge | `.news-badge` | 9.92px / 700 / 1.4, uppercase, letter-spacing 0.04em | #5b4500 on gold, #ffffff on red |
| Year header | `.year-header` | 19.2px / 700 | #ffcc00 |
| Publication title | `.publication-title` | 16px / 600 / 1.3 | #1a365d |
| Authors | `.publication-authors` | 14.4px / 400; own name bold | #4a5568 |
| Venue | `.publication-venue` | 14.4px / 500 (workshop lines italic) | #2b6cb0 |
| Link button | `.publication-links a` | 12.8px / 400 | #3182ce |
| Award name | `.award-name` | 15.68px / 700 | #1a365d |
| Award date | `.award-year` | 12.8px / 700 | #2b6cb0 |
| Footer | `footer` | 14.4px / 400, centred | #4a5568 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Photo | 8px | none | 0 4px 16px rgba(0,0,0,0.15), 0 2px 6px rgba(0,0,0,0.10) |
| Nav | 0 0 12px 12px | 2px #2b6cb0 left, right, bottom | 0 4px 16px rgba(26,54,93,0.10), 0 2px 6px rgba(26,54,93,0.08) |
| Nav link | 6px | none | none |
| Keycap pill | 20px | none | 0 3px 0 #ccdcec, 0 4px 8px rgba(0,0,0,0.06); hover 0 3px 0 #1a365d, 0 4px 8px rgba(0,0,0,0.15) |
| Publication card | 8px | 1px #eef1f5 (hover #e2e8f0) | 0 1px 4px rgba(26,54,93,0.05); hover 0 4px 12px rgba(26,54,93,0.08), translateY(-2px) |
| Link button | 3px | 1px #3182ce | none |
| News badge | corner cut (clip-path 7px top-left) | none | none |
| Year tab | 3px | none (10px gold gradient bar) | none |
| h2 underline | 2px | 36×3px gradient #1a365d → #4299e1 | none |
| Ring bullet | 50% | 2px #2b6cb0 | none |
| Footer | 0 | 1px #e2e8f0 top | none |

## Layout Metrics

- **Container**: max-width 1100px, centred, padding 12px 32px 32px (1036px content, x=202 at 1440).
- **Header**: grid `auto 1fr`, gap 40px, padding-bottom 4.8px, overflow hidden; name line margin-top -24px; cats absolutely positioned at right 100px / bottom -110px and right 0 / bottom -25px.
- **Nav**: sticky top 0, z-index 100, margin 0 -16px 32px (overhangs the column by 16px each side), padding 13.6px 32px; links centred with 2.4px gaps.
- **Sections**: margin-bottom 32px, padding 3.2px, `scroll-margin-top: 70px`; h2 margin-bottom 24px.
- **News timeline**: margin-left 6px, padding-left 22.4px, a vertical rail gradient #2b6cb0 → #e2e8f0; items margin-bottom 14.4px with 2px gold-ringed gold dots.
- **Publications**: year headers margin-bottom 9.6px with a 10px gold tab; cards padding 13.6px 16px, margin-bottom 11.2px; meta row is flex with authors left and venue right; link buttons gap 6.4px, padding 2.4px 8px.
- **Awards**: rows padding 0 0 14.4px 92px with the date absolutely placed in the 92px gutter; trophy icons 24px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≤420px | 16px | 16px | name 23.2px (1.45rem) | photo 132px; keycaps 13.1px; nav links 13.6px |
| ≤620px | 16px | 16px | 27.2px | mentoring list rows stack into one column |
| ≤768px | 16px (container padding 1rem) | 16px | name 27.2px (1.7rem), title 16px on its own line | header single column and centred; cats hidden; email pill icon-only; nav one swipeable row (padding 8.8px 16px, links 14.4px); publication meta stacks |
| >768px | 32px | 16px | 35.2px | two-column header, wrapped centred nav |

## Components

- **Keycap pill**: inline-flex, padding 5.12px 12.8px, 20px radius, background linear-gradient(135deg, #f5faff, #eef5fd), 14.08px/500 #1a365d, shadow 0 3px 0 #ccdcec, 0 4px 8px rgba(0,0,0,0.06); hover fills with linear-gradient(135deg, #1a365d, #2b6cb0 60%, #4299e1), white text and a 3px #1a365d edge. Icons (Material-style SVG) sit left of the label.
- **Tab-bar nav**: white, 2px #2b6cb0 border without top, 12px bottom corners, navy-tinted double shadow, sticky; links 16px/500 #2b6cb0 with 6px radius; active or hovered link #1a365d on #e6f1fb.
- **Section heading**: 28px/600 #1a365d, then a 36×3px bar with linear-gradient(90deg, #1a365d, #4299e1), 2px radius.
- **Highlighter phrases**: background linear-gradient(transparent 60%, #ffe98a 60%) for the topics heading and (transparent 60%, #e4eefb 60%) for key phrases.
- **News timeline item**: gold dot on a blue-to-grey rail, 14.4px/700 #ffcc00 date, optional corner-cut badge (UPCOMING gold gradient #ffe066 → #ffcc00 → #f2b400 with #5b4500 text; AWARD red gradient #ff5a3c → #ff2600 → #db1f00 with white text), then 14.4px #1a365d text with #2b6cb0 links.
- **Publication card**: white, 1px #eef1f5, 8px radius, padding 13.6px 16px; title 16px/600 #1a365d; authors 14.4px #4a5568 with own name bold, venue 14.4px/500 #2b6cb0 right-aligned; optional red "(Oral, …)" and a 24px gold trophy; outlined link buttons 12.8px #3182ce, 1px border, 3px radius; lifts 2px on hover.
- **Year header**: 19.2px/700 #ffcc00 text with 16px left padding and a 10px gold gradient tab (3px radius) on the left.
- **Award row**: 12.8px/700 #2b6cb0 date in a 92px left gutter, 24px gold-gradient trophy for paper awards, 15.68px/700 #1a365d award name, " — venue" in #2b6cb0, optional 14px description line.
- **Personal quote**: paragraph with 35.2px left padding and a #ffcc00 Georgia 38.4px opening quote mark.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Name / title / contact | yes | brush-script name, keycap social row |
| Portrait | yes | 160px rounded square with soft shadow |
| Mascot art | yes | two cut-out cat photos over the nav |
| Navigation | yes | sticky tab bar with section highlighting |
| Bio and research topics | yes | justified text, highlighter heading, ring bullets |
| Interest tags | yes | keycap pills |
| News | yes | gold-dot timeline with corner-cut badges |
| Publications | yes | year-grouped white cards (about 53) |
| Awards / grants | yes | dated rows with gold trophies |
| Education, experience, talks, teaching, people | yes | h3 institutions, dated lists |
| Personal | yes | quote paragraphs with gold quote marks |
| Footer | yes | centred 14.4px with a hairline above |

## Adapting to Other Content

- **More authors**: authors wrap inside the card's left meta column; for very long lists use the page's existing collapsible "+ 55 more authors" link (#2b6cb0) after the first few names.
- **A results table**: put it in a white card with the publication-card border and radius; header 14.4px/600 #1a365d, cells 14.4px #2d3748, 1px #eef1f5 row rules.
- **Long publication lists**: keep year headers with the gold tab; the page already makes the "Old Preprints" header a collapsible `<summary>`, and older years can follow the same pattern.
- **News**: one timeline item per event; reserve the gold UPCOMING badge for future dates and the red AWARD badge for honours.
- **Fewer accents**: if the page must be calmer, drop the cats and the highlighter bands first; keep navy, #2b6cb0 and gold.

## Do's and Don'ts

- Do keep the navy / blue ramp (#1a365d, #2b6cb0, #3182ce, #4299e1) for structure and gold #ffcc00 for dates, years and trophies.
- Do give pills a hard 3px #ccdcec edge rather than a blurred shadow.
- Do keep publication cards light: 1px #eef1f5 border, near-invisible shadow, lift on hover.
- Don't use the brush script anywhere but the name.
- Don't spread NVIDIA green beyond the employer word.
- Don't put a top border on the nav; it hangs from the header like a tab.

## Surfaces

White page, white cards with #eef1f5 borders, frost-blue keycaps, a white sticky nav with a blue three-sided frame, and gold only as small accent fills (dots, tabs, badges, trophies).

## Imagery

One bright square portrait, two cut-out cat photos as mascots, small SVG icons inside pills, gold trophy masks; no publication thumbnails.

## Layout

A 1100px column: header grid with photo, name and pills; sticky nav; bio and topics; then stacked full-width sections (News, Publications, Awards, Grants, Education & Experience, Talks, Teaching, People, Personal); footer. About 16,600px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: navy #1a365d, blue #2b6cb0, link button #3182ce, sky #4299e1, text #2d3748, muted #4a5568, gold #ffcc00, badge text #5b4500, red #ff2600, card border #eef1f5, hairline #e2e8f0, keycap #f5faff with edge #ccdcec, nav active #e6f1fb.

1. "Make a sticky tab-bar nav: white, border 2px solid #2b6cb0 with no top border, radius 0 0 12px 12px, shadow 0 4px 16px rgba(26,54,93,0.10), 0 2px 6px rgba(26,54,93,0.08), padding 13.6px 32px, margins -16px to overhang the column; centred links 16px/500 #2b6cb0 with 6px radius and padding 6.4px 11.2px; active link #1a365d on #e6f1fb."
2. "Build a publication card: white, 1px solid #eef1f5, 8px radius, shadow 0 1px 4px rgba(26,54,93,0.05), padding 13.6px 16px; title 16px/600 #1a365d; authors 14.4px #4a5568 with your name bold and the venue 14.4px/500 #2b6cb0 right-aligned; outlined link buttons 12.8px #3182ce, 1px #3182ce border, 3px radius, padding 2.4px 8px; on hover translateY(-2px) and shadow 0 4px 12px rgba(26,54,93,0.08)."
3. "Make keycap pills: padding 5.12px 12.8px, 20px radius, background linear-gradient(135deg, #f5faff, #eef5fd), 14.08px/500 #1a365d, box-shadow 0 3px 0 #ccdcec, 0 4px 8px rgba(0,0,0,0.06); on hover background linear-gradient(135deg, #1a365d, #2b6cb0 60%, #4299e1), white text."

## Similar Pages

- Hand-written single-file academic sites with a Chakra-like navy palette and card-based publication lists.
- Personal pages that add mascot art and playful badges to an otherwise conventional CV layout.

## Quick Start

```css
:root {
  --primary-color: #1a365d;
  --secondary-color: #2b6cb0;
  --accent-color: #3182ce;
  --sky: #4299e1;
  --text-color: #2d3748;
  --dark-gray: #4a5568;
  --yellow-color: #ffcc00;
  --red-color: #ff2600;
  --card-edge: #eef1f5;
  --border-color: #e2e8f0;
  --font-body: 'Avenir Next', 'Segoe UI', Roboto, sans-serif;
  --font-name: 'Kaushan Script', cursive;
}
body { font-family: var(--font-body); line-height: 1.6; color: var(--text-color); background: #ffffff; }
.container { max-width: 1100px; margin: 0 auto; padding: 12px 32px 32px; }
nav { position: sticky; top: 0; background: #ffffff; border: 2px solid var(--secondary-color); border-top: none; border-radius: 0 0 12px 12px; padding: 13.6px 32px; margin: 0 -16px 32px; }
h2 { font-size: 28px; font-weight: 600; color: var(--primary-color); margin-bottom: 24px; }
h2::after { content: ""; display: block; width: 36px; height: 3px; border-radius: 2px; background: linear-gradient(90deg, #1a365d, #4299e1); }
.publication { background: #ffffff; border: 1px solid var(--card-edge); border-radius: 8px; padding: 13.6px 16px; box-shadow: 0 1px 4px rgba(26,54,93,0.05); }
```

## Provenance

- **URL**: https://liweijiang.github.io/
- **Person**: Liwei Jiang (NLP, LLM pluralism and safety).
- **Venue / award**: NeurIPS 2025 Best Paper, "Artificial Hivemind" (first author). https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/
- **Selection reason**: Rule B (first author); existing entry, unchanged. Chosen for the customised header with a signature-style name and mascot art, a timeline news list and colour-tagged publications.
- **Template credit**: none found; hand-written single HTML file with an inline stylesheet and Google Fonts.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share, DOM boxes), a selector probe of nav, news, publications, awards and footer, the 1440×900 and full-page screenshots plus two scrolled captures, and the inline `<style>` read directly, on 2026-10-28.
