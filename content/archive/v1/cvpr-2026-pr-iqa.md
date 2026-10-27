# PR-IQA Amber Slate — Style Reference

> The modernized project template: slate ink, amber hover, a floating "More Works" card.

**Theme:** light

Values come from the static HTML and the page's `static/css/index.css`, which is the tokenized 2025 rewrite of the Academic Project Page Template, layered on Bulma 0.9. Bulma's palette inflates the raw counts; the table lists the custom-property tokens and literals the page uses. Measurements are normalized; roles are interpreted. The rendered page was not viewed.

## Overview

PR-IQA uses the newer Academic Project Page Template whose index.css replaces Nerfies styling with Tailwind-flavoured tokens: slate text `#1e293b`, slate grays `#64748b` / `#94a3b8`, a `#f8fafc` secondary surface, `#e2e8f0` borders, 12px and 16px radii, and Tailwind-style `shadow-sm` to `shadow-xl`. The accent is amber `#d97706`: author links, the button hover fill, the circular scroll-to-top button, the copy-BibTeX button, and focus outlines. Section titles get a centered 60px by 3px underline in an amber-to-orange gradient (`#f59e0b → #f97316`). Dark slate buttons lift 2px and turn amber on hover. A fixed "More Works from" card (top-right) opens a 400px dropdown listing two lab papers with italic venue lines and the lab logo (`airlab.png`). The title is a flex row with the PR-IQA icon at 2.4em beside the two-line name. Inter is declared as the font but no Inter stylesheet is loaded, so most visitors see Segoe UI or the system sans (inferred).

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Amber Signal | `#d97706` | `--primary-color` | Author links, button hover, scroll-to-top, copy button, focus ring |
| Amber Deep | `#b45309` | `--primary-hover` | Author link hover |
| Slate Ink | `#1e293b` | `--text-primary` | Body text, title, `is-dark` button fill |
| Slate Gray | `#64748b` | `--text-secondary` / `--secondary-color` | Venue pill text, footer text, icon links |
| Slate Mist | `#94a3b8` | `--text-light` | Dropdown venue lines and icons |
| Sky Accent | `#0ea5e9` | `--accent-color` | Declared accent (little used) |
| Paper White | `#ffffff` | `--background-primary` | Page, More Works button and dropdown |
| Slate Wash | `#f8fafc` | `--background-secondary` | `hero is-light` bands, footer |
| Slate Fog | `#f1f5f9` | `--background-accent` | BibTeX `pre`, venue pill |
| Slate Line | `#e2e8f0` | `--border-color` | Band rules, pre border, dropdown border |
| Ember Gradient | `#f59e0b → #f97316` | `--gradient-accent` | Section-title underline, author link underline on hover |
| Award Red | `#ef4444` | (literal) | `.publication-awards` (defined, unused) |

`--gradient-primary` (`#667eea → #764ba2`) and `--gradient-subtle` are declared but not seen on visible elements.

## Tokens — Typography

- **Declared:** `"Inter", "Segoe UI", -apple-system, BlinkMacSystemFont, sans-serif`, 16px, line-height 1.6, antialiased. No Inter webfont is linked (inferred fallback to system sans).
- **Mono:** `SF Mono` stack for BibTeX.

| Role | Size | Weight |
|---|---|---|
| Publication title | 2.1rem (`!important`), line-height 1.2 | 800 |
| Section title (`is-3`) | Bulma 2rem | 700, 1rem bottom padding plus 3px underline |
| Authors (`is-size-5`) | 1.25rem | 500, links 600 |
| Teaser subtitle | 0.95rem, line-height 1.6 | 400 |
| Body | 16px | 400 |
| BibTeX | 0.9rem | 400 |
| Dropdown venue | 0.8rem italic | 400 |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons, venue pill, pre, copy button | 12px (`--border-radius`) |
| More Works button and dropdown, banners, video | 16px (`--border-radius-lg`) |
| Scroll-to-top | 50% (50px circle) |

**Shadows:** `--shadow-sm 0 1px 2px 0 rgb(0 0 0 / 0.05)`; `--shadow-md 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)`; `--shadow-lg 0 10px 15px -3px …, 0 4px 6px -4px …`; `--shadow-xl 0 20px 25px -5px …, 0 8px 10px -6px …`.

**Motion:** `--transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1)`; sections `fadeInUp 0.6s`.

**Spacing:** hero body `4rem 1.5rem`; teaser `2rem / 4rem`; footer `3rem 1.5rem`; container `is-max-desktop` (960px).

## Components

- **Title:** flex row, icon image 2.4em tall, two-line title.
- **Author block:** Dongguk University | NAVER WEBTOON AI, then "CVPR 2026" as plain text; `*` equal contribution and `†` corresponding notes in `small`.
- **Link buttons:** `button is-dark is-rounded` restyled to 12px radius, `#1e293b` fill, `shadow-md`; hover lifts 2px, `shadow-lg`, fill `#d97706`. Buttons: Paper (arXiv PDF), Supplementary (PDF), Code, arXiv.
- **More Works:** fixed at `top: 2rem; right: 2rem`, white card with 2px `#e2e8f0` border, 16px radius; dropdown 400px with `shadow-xl`.
- **Section title:** 700 weight with centered 60×3px gradient bar.
- **BibTeX:** `#f1f5f9` pre with 1px border, 12px radius, 1.5rem padding, amber copy button in a header row.
- **Scroll-to-top:** 50px amber circle fixed bottom-right.
- **Footer:** `#f8fafc`, top border, slate text, APPT and Nerfies credit plus CC BY-SA.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Icon plus title flex row |
| Venue badge | Yes (text) | "CVPR 2026" under affiliations; `.publication-venue` pill style exists but is not used |
| Link buttons | Yes | Paper, Supplementary, Code, arXiv |
| Teaser figure | Yes | `F1_Main.png` with overview caption |
| Abstract | Yes | Justified |
| Method figure | Yes | `F2_Overview.png` |
| Results | Yes | Two "Results" sections with qualitative figures (`F3`, `F4`) |
| Image comparison slider / 3D / demo | No | 3D flag came from the word "Splatting" |
| Related works dropdown | Yes | Fixed "More Works" card |
| BibTeX | Yes | With copy button |
| Acknowledgements | Yes | MSIT / ITRC funding note |

## Do's and Don'ts

- Do keep amber for interaction states and one decorative underline per heading.
- Do use the slate scale for all neutral text, never pure black.
- Do load the Inter webfont if you rely on it; this page does not.
- Don't use the purple `--gradient-primary`; it clashes with the amber accent and is unused here.

## Surfaces

White page, `#f8fafc` light bands with `#e2e8f0` rules, white floating More Works card, `#f1f5f9` code panel.

## Imagery

Seven static images: two lab logos, the method icon and four paper figures. No video.

## Layout

960px centered column; fixed overlays (More Works, scroll-to-top) at 2rem from the viewport edges.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, band `#f8fafc`, code `#f1f5f9`, border `#e2e8f0`, ink `#1e293b`, gray `#64748b`, light `#94a3b8`, accent `#d97706`, accent hover `#b45309`.

1. "Restyle Bulma `is-dark` buttons: 12px radius, `#1e293b` fill, shadow `0 4px 6px -1px rgb(0 0 0 / 0.1)`; on hover translateY(-2px), larger shadow, fill `#d97706`."
2. "Give each section title a centered 60px by 3px underline using `linear-gradient(135deg, #f59e0b, #f97316)` with 1rem padding below the text."
3. "Add a fixed top-right 'More Works' button (white, 2px `#e2e8f0` border, 16px radius) that opens a 400px dropdown card with `shadow-xl`, each item showing a title and an italic 0.8rem `#94a3b8` venue."

## Similar Pages

Other pages on the 2025 APPT rewrite; Reflection Separation in this collection is a comparable token-driven restyle with ink instead of amber.

## Quick Start

```css
:root {
  --primary-color: #d97706; --primary-hover: #b45309; --accent-color: #0ea5e9;
  --text-primary: #1e293b; --text-secondary: #64748b; --text-light: #94a3b8;
  --background-primary: #ffffff; --background-secondary: #f8fafc; --background-accent: #f1f5f9;
  --border-color: #e2e8f0;
  --gradient-accent: linear-gradient(135deg, #f59e0b 0%, #f97316 100%);
  --border-radius: 12px; --border-radius-lg: 16px;
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  --font: "Inter", "Segoe UI", -apple-system, BlinkMacSystemFont, sans-serif;
}
```

## Provenance

- **URL:** https://kakaomacao.github.io/pr-iqa-project-page/
- **Paper:** PR-IQA: Partial-Reference Image Quality Assessment for Diffusion-Based Novel View Synthesis (arXiv 2604.04576), Inseong Choi et al.
- **Venue:** CVPR 2026 (text in author block).
- **Selection reason:** arXiv comment states acceptance at CVPR 2026 and links this page.
- **Template credit:** Academic Project Page Template adopted from Nerfies (footer), in its tokenized 2025 version.
- **Measurement method:** `extract_style.py` plus manual reading of index.css tokens and component rules. Rendered page not viewed, so the actual fallback font is not confirmed.
