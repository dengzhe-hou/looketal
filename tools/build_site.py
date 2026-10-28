"""Build the Look et al. static site into docs/ from data/raw/*.json and content/designs/*.md.

Usage: python -I -B tools/build_site.py
Layout follows Refero / Refero Styles: home with search and taxonomy browse, a filterable
browse page, one page per style (left: specimen and tokens, right: DESIGN.md / CSS / Tailwind /
tokens panel), curated collections, and an about page with inclusion rules.
"""
import html
import json
import re
import shutil
from collections import Counter
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs"
CATALOG = ROOT / "data" / "catalog.json"  # one record per included page; DESIGN.md text lives in content/designs/
SITE = "Look et al."
ISSUES = "https://github.com/dengzhe-hou/looketal/issues/new?template=removal.yml"
REMOVAL = f'<a href="{ISSUES}" target="_blank" rel="noopener">open a removal request</a> (a short GitHub form)'
TAGLINE = "Design research for academic pages"
esc = html.escape

TEMPLATES = [
    ("Academic Project Page Template", r"academic[- ]project[- ]page"),
    ("Nerfies / Bulma", r"nerfies|bulma"),
    ("Jon Barron", r"barron"),
    ("al-folio", r"al-folio"),
    ("Hugo Blox / Wowchemy", r"hugo|wowchemy"),
    ("academicpages", r"academicpages|minimal.mistakes"),
    ("Google Sites", r"google sites"),
    ("Jekyll (other)", r"jekyll"),
]
MODULES = [
    ("Teaser video", r"video"), ("BibTeX", r"bibtex"), ("Code", r"\bcode\b|github"), ("arXiv / paper", r"arxiv|paper"),
    ("Demo", r"demo|gradio|space"), ("Interactive 3D", r"3d|webgl|viser|splat|model-viewer"),
    ("Comparison slider", r"slider|compar"), ("Results table", r"table|leaderboard"), ("Dataset", r"dataset"),
    ("Publication list", r"publication"), ("News", r"news"), ("Bio / photo", r"bio|photo|portrait"),
]
CSS_COLOR = re.compile(r"^(#[0-9a-fA-F]{3,8}|(rgba?|hsla?|oklch|oklab|lab|lch)\([^)]*\)|[a-zA-Z]+)$")


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def template_group(t):
    for name, pat in TEMPLATES:
        if re.search(pat, t, re.I):
            return name
    return "Custom"


def module_tags(mods):
    blob = " ".join(mods).lower()
    return [name for name, pat in MODULES if re.search(pat, blob)]


def split_sections(md):
    """Return (style_name, preamble, {heading: body}) keyed by '## ' headings."""
    lines = md.splitlines()
    name = lines[0].lstrip("# ").replace("— Style Reference", "").replace("· Style Reference", "").strip()
    sections, cur, buf, pre = {}, None, [], []
    for ln in lines[1:]:
        if ln.startswith("## "):
            if cur:
                sections[cur] = "\n".join(buf).strip()
            cur, buf = ln[3:].replace("·", "—").strip(), []
        elif cur:
            buf.append(ln)
        else:
            pre.append(ln)
    if cur:
        sections[cur] = "\n".join(buf).strip()
    return name, "\n".join(pre).strip(), sections


def css_block(md):
    m = re.search(r"```css\n(.*?)```", md, re.S)
    return m.group(1).strip() if m else ""


def tailwind_from_css(css):
    m = re.search(r":root[^{]*\{(.*?)\}", css, re.S)
    body = m.group(1) if m else ""
    decls = [d.strip() for d in body.replace("\n", ";").split(";") if d.strip().startswith("--")]
    return "@theme {\n" + "\n".join(f"  {d};" for d in decls) + "\n}" if decls else ""


def tokens_json(e):
    colors = {slugify(p["name"]) or f"c{i}": {"$type": "color", "$value": p["hex"], "$description": p["role"]}
              for i, p in enumerate(e["palette"])}
    fonts = {slugify(f) or f"f{i}": {"$type": "fontFamily", "$value": f} for i, f in enumerate(e["fonts"])}
    return json.dumps({"color": colors, "font": fonts}, ensure_ascii=False, indent=2)


def pick_roles(palette):
    """Choose background / text / accent from interpreted roles for the synthetic specimen."""
    ok = [p for p in palette if CSS_COLOR.match(p["hex"].strip())]
    def find(*words):
        for p in ok:
            if re.search("|".join(words), p["role"], re.I):
                return p["hex"].strip()
        return None
    bg = find(r"\bbackground\b", "canvas", r"\bpage\b", "surface") or "#ffffff"
    text = find("title", "heading", "body text", r"\btext\b", "ink") or "#222222"
    accent = find("button", "link", "accent", "venue", "badge", "highlight") or text
    if accent == bg:
        accent = text
    return bg, text, accent


def load_entries():
    entries = []
    for it in json.loads(CATALOG.read_text(encoding="utf-8")):
        if not it["md_path"]:
            continue
        slug = it["slug"]
        md = (ROOT / "content" / "designs" / f"{slug}.md").read_text(encoding="utf-8")
        name, pre, sections = split_sections(md)
        venue = it.get("venue") or ""
        e = {
            "slug": slug, "kind": it["kind"], "title": it["title"], "style_name": name, "url": it["url"],
            "venue": venue, "conf": venue.split()[0] if it["kind"] == "project" and venue else "",
            "year": it.get("year"), "person": it.get("person", ""), "field": it.get("field", ""),
            "mood": it["mood"], "theme": it["theme"], "template": it["template"],
            "template_group": template_group(it["template"]),
            "fonts": [re.split(r"\s*[(|,]", f)[0].strip() for f in it["fonts"][:3]],
            "palette": [p for p in it["palette"][:8] if CSS_COLOR.match(p["hex"].strip())],
            "modules": module_tags(it["modules"]), "layout": it["layout"],
            "rendered_check": it["rendered_check"], "issues": it["issues"], "selection": it.get("selection", {}),
        }
        e["specimen"] = pick_roles(e["palette"])
        e["shot"] = (ROOT / "content" / "shots" / f"{slug}.card.webp").exists()
        e["tall"] = (ROOT / "content" / "shots" / f"{slug}.tall.webp").exists()
        entries.append((e, md, pre, sections))
    entries.sort(key=lambda x: (x[0]["kind"], x[0]["conf"], -(x[0]["year"] or 0), x[0]["slug"]))
    return entries


# ---------- shared page chrome ----------

def nav(prefix, active):
    items = [("index.html", "Home", "home"), ("browse.html?kind=project", "Project pages", "project"),
             ("browse.html?kind=researcher", "Researcher pages", "researcher"), ("browse.html", "All styles", "all"),
             ("collections.html", "Collections", "collections"), ("prompts.html", "Design prompts", "prompts"),
             ("about.html", "About", "about")]
    links = "".join(f'<a href="{prefix}{h}"{" aria-current=page" if k == active else ""}>{esc(t)}</a>'
                    for h, t, k in items)
    return f"""<aside class="side"><a class="brand" href="{prefix}index.html"><span class="mark">et<br>al.</span><span>{SITE}</span></a>
<nav>{links}</nav><button class="theme-toggle" id="theme" type="button" aria-label="Color theme">Theme: auto</button>
<div class="side-foot">Screenshots © their authors, linked to the original pages.<br>DESIGN.md text <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener">CC BY-NC 4.0</a>, code MIT.</div></aside>"""


def page(title, body, prefix, active, desc=TAGLINE, extra_head=""):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap" rel="stylesheet">
{extra_head}<link rel="stylesheet" href="{prefix}assets/site.css"></head>
<body><div class="shell">{nav(prefix, active)}<main class="main">{body}</main></div>
<script src="{prefix}assets/data.js"></script><script src="{prefix}assets/site.js"></script></body></html>"""


def specimen(e, big=False):
    """Token specimen: type sample and buttons drawn from measured palette and fonts (no page content)."""
    bg, text, accent = e["specimen"]
    font = esc(e["fonts"][0]) if e["fonts"] else "inherit"
    labels = ("Paper", "Code", "Video") if e["kind"] == "project" else ("CV", "Scholar", "Email")
    pills = "".join(f'<i style="background:{esc(accent)}">{t}</i>' for t in labels)
    return f"""<div class="spec{' big' if big else ''}" style="background:{esc(bg)};color:{esc(text)};font-family:'{font}',system-ui,sans-serif" aria-hidden="true">
<b class="aa">Aa</b><span style="color:{esc(accent)}">{esc(e['fonts'][0] if e['fonts'] else 'system font')}</span><div class="pills">{pills}</div>
<div class="strip">{''.join(f'<em style="background:{esc(p["hex"])}"></em>' for p in e["palette"][:6])}</div></div>"""


def strip(e):
    return '<div class="strip">' + "".join(f'<em style="background:{esc(p["hex"])}"></em>' for p in e["palette"][:6]) + "</div>"


def thumb(e, prefix):
    if e.get("shot"):
        # the tall capture is fetched on first hover (site.js) and scrolls inside the card
        tall = f' data-tall="{prefix}assets/shots/{e["slug"]}.tall.webp"' if e.get("tall") else ""
        return (f'<div class="shot"{tall}><img src="{prefix}assets/shots/{e["slug"]}.card.webp" alt="" loading="lazy" '
                f'width="640" height="400">{strip(e)}</div>')
    return specimen(e)


def card(e, prefix):
    meta = e["venue"] if e["kind"] == "project" else f'Researcher · {e["venue"]}'
    return f"""<a class="card" href="{prefix}s/{e['slug']}.html">{thumb(e, prefix)}
<div class="cbody"><div class="meta">{esc(meta)}</div><div class="name">{esc(e['title'])}</div>
<div class="mood">{esc(e['mood'])}</div></div></a>"""


# ---------- pages ----------

def wall(es):
    """Two rows of thumbnails drifting in opposite directions; each row is doubled so the loop is seamless."""
    shots = [e for e in es if e.get("shot")]
    def row(items, cls):
        cells = "".join(f'<a href="s/{e["slug"]}.html" tabindex="-1"><img src="assets/shots/{e["slug"]}.card.webp" alt="" width="640" height="400"></a>' for e in items)
        return f'<div class="wrow {cls}"><div class="wtrack">{cells}{cells}</div></div>'
    return f'<div class="wall" aria-hidden="true">{row(shots[0::2][:18], "r1")}{row(shots[1::2][:18], "r2")}</div>'


def build_home(entries):
    es = [e for e, *_ in entries]
    def facet(label, key, values):
        chips = "".join(f'<a class="chip" href="browse.html?{key}={quote(str(v))}">{esc(str(v))} <span>{n}</span></a>' for v, n in values)
        return f'<section class="facet"><h3>{label}</h3><div class="chips">{chips}</div></section>'
    confs = Counter(e["conf"] for e in es if e["conf"])
    years = Counter(e["year"] for e in es if e["kind"] == "project")
    tpls = Counter(e["template_group"] for e in es)
    mods = Counter(m for e in es for m in e["modules"])
    fields = Counter(e["field"].split("/")[0].split(",")[0].strip() for e in es if e["field"]).most_common(14)
    recent = [e for e in es if e["kind"] == "project" and e["year"] == 2026][:8]
    body = f"""<header class="hero"><h1>{SITE}</h1><p class="lede">{TAGLINE}. Real paper project pages and researcher homepages,
each with an AI-readable DESIGN.md: colors, type, spacing, components and page modules.</p>
<form class="search" action="browse.html"><input name="q" type="search" placeholder="Search a paper, person, template or mood…" aria-label="Search">
<button>Search</button></form>
<div class="quick"><a href="browse.html?kind=project">Project pages <span>{sum(e['kind']=='project' for e in es)}</span></a>
<a href="browse.html?kind=researcher">Researcher pages <span>{sum(e['kind']=='researcher' for e in es)}</span></a>
<a href="collections.html">Collections</a><a href="prompts.html">Design prompts</a></div></header>
{wall(es)}
<div class="facets">
{facet("Venues", "conf", sorted(confs.items()))}
{facet("Years", "year", sorted(years.items(), reverse=True))}
{facet("Templates", "tpl", tpls.most_common())}
{facet("Page modules", "module", mods.most_common())}
{facet("Fields", "q", fields)}
</div>
<section><div class="sechead"><h2>New from 2026</h2><a href="browse.html?year=2026">See all</a></div>
<div class="grid">{''.join(card(e, '') for e in recent)}</div></section>"""
    return page(f"{SITE} · {TAGLINE}", body, "", "home")


def build_browse():
    body = """<header class="phead"><h1 id="btitle">All styles</h1><p class="lede" id="bcount"></p></header>
<div class="filters" id="filters">
<input type="search" id="q" placeholder="Search…" aria-label="Search">
<div class="seg" id="kind" role="group" aria-label="Kind"><button data-v="">All</button><button data-v="project">Project pages</button><button data-v="researcher">Researchers</button></div>
<select id="conf" aria-label="Venue"><option value="">All venues</option></select>
<select id="year" aria-label="Year"><option value="">All years</option></select>
<select id="tpl" aria-label="Template"><option value="">All templates</option></select>
<select id="theme" aria-label="Theme"><option value="">Any theme</option><option value="light">Light</option><option value="dark">Dark</option><option value="both">Light + dark</option></select>
</div><div class="chips mods" id="mods"></div>
<div class="grid" id="grid"></div>"""
    return page(f"Browse · {SITE}", body, "", "all")


def section_md(sections, *names):
    for n in names:
        for k, v in sections.items():
            if k.lower().startswith(n.lower()):
                return v
    return ""


def build_style(e, md, pre, sections, entries):
    css = css_block(md)
    tw = tailwind_from_css(css)
    compact_keys = [k for k in sections if re.match(r"(Tokens|Agent Prompt)", k)]
    compact = f"# {e['style_name']} — Style Reference\n\n" + pre + "\n\n" + "\n\n".join(f"## {k}\n\n{sections[k]}" for k in compact_keys)
    sim = [x for x, *_ in entries if x["slug"] != e["slug"] and x["kind"] == e["kind"] and x["template_group"] == e["template_group"]]
    sim += [x for x, *_ in entries if x["slug"] != e["slug"] and x["kind"] == e["kind"] and x not in sim and x["conf"] == e["conf"]]
    swatches = "".join(f"""<button class="sw" data-copy="{esc(p['hex'])}"><span style="background:{esc(p['hex'])}"></span>
<b>{esc(p['name'])}</b><code>{esc(p['hex'])}</code><small>{esc(p['role'])}</small></button>""" for p in e["palette"])
    fonts_q = "&".join("family=" + f.replace(" ", "+") for f in e["fonts"][:2] if re.fullmatch(r"[A-Za-z0-9 ]+", f))
    extra = f'<link href="https://fonts.googleapis.com/css2?{fonts_q}&display=swap" rel="stylesheet">\n' if fonts_q else ""
    sample = e["title"] if e["kind"] == "project" else f"{e['title']}, {e['field']}"
    type_rows = "".join(f"""<div class="trow"><div class="tlabel">{esc(f)}</div>
<div class="tsample" style="font-family:'{esc(f)}',system-ui,sans-serif"><span class="t1">{esc(sample[:70])}</span>
<span class="t2">Abstract · Method · Results · BibTeX — 0123456789</span></div></div>""" for f in e["fonts"])
    status = "Checked against the rendered page." if e["rendered_check"] else "Written from static HTML/CSS; the rendered page was not viewed."
    meta_rows = [("Venue" if e["kind"] == "project" else "Award", e["venue"]), ("Year", e["year"]),
                 ("First author" if e["kind"] == "project" else "Person", e["person"]), ("Field", e["field"]),
                 ("Template", e["template"]), ("Theme", e["theme"])]
    meta = "".join(f"<dt>{esc(k)}</dt><dd>{esc(str(v))}</dd>" for k, v in meta_rows if v)
    blocks = {k: section_md(sections, k) for k in ("Overview", "Tokens — Spacing", "Page Modules", "Do's", "Layout", "Components")}
    if not blocks["Overview"]:
        # some files keep the overview in the preamble, after the theme line and the measurement note (Refero's own layout)
        paras = [p for p in re.split(r"\n\s*\n", pre) if p.strip() and not p.lstrip().startswith((">", "**Theme"))]
        blocks["Overview"] = "\n\n".join(paras[1:] if len(paras) > 1 else paras)
    payload = json.dumps({"md": md, "compact": compact, "css": css, "tw": tw, "tokens": tokens_json(e), "blocks": blocks},
                         ensure_ascii=False).replace("</", "<\\/")
    crumbs = f'<a href="../index.html">{SITE}</a> / <a href="../browse.html?kind={e["kind"]}">{"Project pages" if e["kind"] == "project" else "Researcher pages"}</a>'
    body = f"""<div class="style">
<div class="sleft">
<div class="crumbs">{crumbs}</div>
<h1 class="sname">{esc(e['title'])}</h1>
<p class="smood">{esc(e['mood'])}</p>
{f'<figure class="bigshot"><a class="frame{' scroll' if e['tall'] else ''}" href="{esc(e["url"])}" target="_blank" rel="noopener"><span class="bar"><i></i><i></i><i></i><b>{esc(re.sub(r"^https?://", "", e["url"]).rstrip("/"))}</b></span><span class="view"><img src="../assets/shots/{e["slug"]}.{'tall.webp' if e['tall'] else 'webp'}" alt="Screenshot of {esc(e["title"])}" width="{720 if e['tall'] else 1200}" height="{1350 if e['tall'] else 750}"></span></a><figcaption>Screenshot of <a href="{esc(e["url"])}" target="_blank" rel="noopener">{esc(e["url"])}</a>, © the authors. Shown for reference. <a href="{ISSUES}&amp;title=Removal:+{e["slug"]}" target="_blank" rel="noopener">Request removal</a></figcaption></figure>' if e["shot"] else ""}
{specimen(e, big=True)}
<div class="sactions"><a class="btn primary" href="{esc(e['url'])}" target="_blank" rel="noopener">Visit page ↗</a>
<a class="btn" href="../designs/{e['slug']}.md" download>Download DESIGN.md</a></div>
<dl class="smeta">{meta}</dl><p class="status">{esc(status)} {esc(e['issues'])}</p>
{f'<section><h2>Why it is here</h2><p>{esc(e["selection"]["why"])}</p></section>' if e.get("selection", {}).get("why") else ""}
<section><h2>Overview</h2><div class="mdx" data-block="Overview"></div></section>
<section><h2>Color Palette</h2><div class="swatches">{swatches}</div></section>
<section><h2>Typography</h2>{type_rows}</section>
<section><h2>Spacing &amp; Shape</h2><div class="mdx" data-block="Tokens — Spacing"></div></section>
<section><h2>Page Modules</h2><div class="mdx" data-block="Page Modules"></div></section>
<section><h2>Guidelines</h2><div class="mdx" data-block="Do's"></div></section>
<section><h2>More like this</h2><div class="grid small">{''.join(card(x, '../') for x in sim[:6])}</div></section>
</div>
<aside class="sright"><div class="panel">
<div class="ptabs" role="tablist"><button data-tab="md" aria-selected="true">DESIGN.md</button><button data-tab="tw">Tailwind v4</button><button data-tab="css">CSS Variables</button><button data-tab="tokens">Design Tokens</button></div>
<div class="ptools"><div class="seg sm" id="mode"><button data-v="compact">Compact</button><button data-v="extended" aria-pressed="true">Extended</button></div>
<button class="btn sm" id="pcopy">Copy</button><a class="btn sm" href="../designs/{e['slug']}.md" download>.md</a></div>
<pre class="pbody" id="pbody"></pre></div></aside>
</div>
<script id="style-data" type="application/json">{payload}</script>"""
    return page(f"{e['title']} design system · {SITE}", body, "../", e["kind"], desc=e["mood"],
                extra_head=extra + '<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>\n')


COLLECTIONS = [
    ("nerfies-family", "The Nerfies family",
     "Pages built on the Nerfies template or its descendant, the Academic Project Page Template.",
     lambda e: e["kind"] == "project" and e["template_group"] in ("Nerfies / Bulma", "Academic Project Page Template"),
     "Most of these share Bulma's grid, Google Sans titles and dark pill link buttons. Compare where authors departed from the defaults: a venue color, a custom teaser band, a results table style. Those small edits are what a DESIGN.md should record."),
    ("built-from-scratch", "Built from scratch",
     "Project pages that do not use a known academic template.",
     lambda e: e["kind"] == "project" and e["template_group"] == "Custom",
     "Custom pages show the wider range: editorial serif layouts, dark product-style launches, single-file HTML. Read the Layout and Components sections to see which choices carry the identity."),
    ("show-dont-tell", "Show, don't tell",
     "Pages whose main evidence is interactive or comparative: sliders, 3D viewers, live demos.",
     lambda e: any(m in e["modules"] for m in ("Comparison slider", "Interactive 3D", "Demo")),
     "When results are visual, the page layout is built around a comparison widget. Check how each page frames the widget and what it puts next to it."),
    ("researcher-homepages", "Researcher homepages",
     "Turing laureates and recent best-paper authors, chosen by a fixed rule (see About).",
     lambda e: e["kind"] == "researcher",
     "Homepages range from 1990s hand-written HTML to al-folio and Hugo themes. The Page Modules table shows how each orders bio, news and publications."),
    ("dark-and-dual", "Dark and dual-theme pages",
     "Pages that ship a dark theme or a light/dark switch.",
     lambda e: e["theme"] in ("dark", "both"),
     "Dark academic pages are rare. Look at how surfaces step up in lightness and how figures with white backgrounds are handled."),
]


def build_collections(entries):
    es = [e for e, *_ in entries]
    parts = []
    for cid, title, desc, pred, closer in COLLECTIONS:
        items = [e for e in es if pred(e)]
        parts.append(f"""<section class="coll" id="{cid}"><div class="sechead"><h2>{esc(title)} <span class="count">{len(items)}</span></h2>
<a href="browse.html?collection={cid}">See all</a></div><p class="lede">{esc(desc)}</p>
<div class="grid">{''.join(card(e, '') for e in items[:6])}</div>
<div class="closer"><span>Look closer</span><p>{esc(closer)}</p></div></section>""")
    body = f'<header class="phead"><div class="eyebrow">Collections</div><h1>Collections</h1><p class="lede">Groups of pages that share a template, a feature or a theme.</p></header>{"".join(parts)}'
    return page(f"Collections · {SITE}", body, "", "collections")


def build_prompts(entries):
    es = [e for e, *_ in entries]
    ex = next(e for e in es if e["kind"] == "project" and e["template_group"] == "Custom")
    ex2 = next(e for e in es if e["kind"] == "researcher")
    body = f"""<header class="phead"><div class="eyebrow">Collections</div><h1>Design prompts from real academic pages</h1>
<p class="lede">A DESIGN.md gives your coding agent visual rules. Your paper supplies the content. Fill in the brackets and attach the DESIGN.md you picked.</p></header>
<section><h2>Build a project page</h2><pre class="prompt">Build a project page for our paper "[title]" ([venue]). Use the attached DESIGN.md for colors, type, spacing and component styling only.
Content comes from our paper: authors and affiliations, [teaser figure or video], abstract, [method figure], [results: tables / videos / comparison slider], BibTeX.
Link buttons: [Paper] [arXiv] [Code] [Data] [Demo].
Keep it a static page that works on GitHub Pages. List which visual decisions came from the reference and which you changed.</pre>
<p>Example reference: <a href="s/{ex['slug']}.html">{esc(ex['title'])}</a></p></section>
<section><h2>Build a researcher homepage</h2><pre class="prompt">Build my academic homepage. Use the attached DESIGN.md for visual rules only.
Content: name, [position, affiliation], photo, short bio, [news], selected publications with [thumbnails / venue badges], [awards], contact links.
Generate the publication list from [publications.bib]. Keep it static and accessible; support dark mode only if the reference does.</pre>
<p>Example reference: <a href="s/{ex2['slug']}.html">{esc(ex2['title'])}</a></p></section>
<section><h2>Restyle an existing page</h2><pre class="prompt">Restyle our existing project page (attached HTML) using the attached DESIGN.md. Keep every piece of content and every link.
Change only colors, fonts, spacing, button and card styling, and section rhythm. Report the before/after tokens you changed.</pre></section>"""
    return page(f"Design prompts · {SITE}", body, "", "prompts")


def build_about(entries):
    es = [e for e, *_ in entries]
    n_proj = sum(e["kind"] == "project" for e in es)
    n_res = len(es) - n_proj
    n_rend = sum(e["rendered_check"] for e in es)
    body = f"""<header class="phead"><div class="eyebrow">About</div><h1>About {SITE}</h1>
<p class="lede">A reference library of academic web pages, in the spirit of Refero Styles, for researchers and their coding agents.</p></header>
<section class="prose"><h2>What is included</h2>
<p><b>{n_proj} paper project pages</b> from papers accepted at NeurIPS, ICML, ICLR, CVPR and ACL in 2025 and 2026, ten per venue and year. Candidates come from arXiv comments that state the acceptance and link a project page; a page had to load, and workshop papers were left out. That gave a pool of 505 pages, at least 40 per venue and year.</p>
<p><b>{n_res} researcher homepages</b> from a pool of 138: ACM Turing Award laureates (2018–2025) and first or last authors of Best Paper, Outstanding Paper and Test of Time awards at the same five venues (2023–2025) who keep a personal page. ACL Outstanding Papers are not yet in the pool. Institutional directory pages, Google Scholar and LinkedIn profiles do not count.</p>
<h2>How pages were chosen</h2>
<p>By visual design only, in two rounds. Every candidate was screenshotted at 1440×900. In the first round a model reviewer looked at every first screen in a pool and kept 20 (60 for researchers); in the second it looked at a 2700px-tall capture of each and kept 10 (30 for researchers). The criteria were typography, a look of its own beyond template defaults, layout and rhythm, how the work is presented, and polish. Research content, venue and fame were ignored, and near-ties went to the page that added a style not yet picked. Pages that showed a loader, a blank screen or a bot wall could not be judged and were dropped. The reason for each pick is on its style page.</p>
<h2>How a DESIGN.md is made</h2>
<p>From the rendered page first. A headless browser reports the computed styles of the title, headings, body, buttons and containers, the fonts that actually loaded, the first-viewport anatomy in DOM order, and the color share of the first screen. The page's stylesheet and markup then supply selectors, hover and responsive rules. When the CSS and the render disagree, the render wins. Each file follows a fixed section order (Overview, First Viewport, color, type and spacing tokens, Layout Metrics, Components, Page Modules, guidance for other content, an agent prompt guide and a Quick Start) and passes an automatic check that every color used in the prompts appears in the token table. {n_rend} of {len(es)} entries were checked against the rendered page.</p>
<p>The method was revised after a reconstruction test. Builders given only a DESIGN.md and different content rebuilt five pages, a blind judge tried to match each rebuild to its original, and an analyst scored similarity from 1 to 5 against the live page. With the first version, written from CSS alone, the judge matched all five, but overall similarity averaged 3.0 (2 to 4), mostly because of values the CSS declared and the page never showed. With the current version, the same test on the same five pages again matched all five and averaged 4.0 (all five scored 4). A separate audit of ten other files found 4 wrong values in about 129 checked claims; those were corrected.</p>
<h2>Screenshots</h2>
<p>Each entry shows an above-the-fold screenshot of the original page, reduced to 1200×750, credited to the authors and linked back to the live page. Screenshots are shown for reference and comparison, the same way design reference libraries such as Refero do. DESIGN.md files describe visual style; they are not official guides of the authors.</p>
<h2>License and citation</h2>
<p>The DESIGN.md files, the selection and the site text are under <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener">CC BY-NC 4.0</a>. You can reuse them for non-commercial work with credit to Look et al. (Dengzhe Hou). For commercial use, ask first. The code is MIT. Screenshots belong to the pages' authors and are not covered by either license. To cite the library, use Hou, D. (2026), <i>Look et al.: A Design Library of Academic Web Pages for Humans and AI Agents</i>, Zenodo, <a href="https://doi.org/10.5281/zenodo.23718470" target="_blank" rel="noopener">doi:10.5281/zenodo.23718470</a>.</p>
<h2>Removal</h2>
<p>If you are an author and want your page or screenshot removed or corrected, {REMOVAL} and it will be taken down. Requests are handled by hand, usually within a few days.</p></section>"""
    return page(f"About · {SITE}", body, "", "about")


def main():
    entries = load_entries()
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "s").mkdir(parents=True)
    (OUT / "designs").mkdir()
    (OUT / "assets").mkdir()
    for f in ("site.css", "site.js"):
        shutil.copy(ROOT / "tools" / "assets" / f, OUT / "assets" / f)
    (OUT / "assets" / "shots").mkdir()
    for e, *_ in entries:
        if e["shot"]:
            for suf in (".webp", ".card.webp") + ((".tall.webp",) if e["tall"] else ()):
                shutil.copy(ROOT / "content" / "shots" / f"{e['slug']}{suf}", OUT / "assets" / "shots" / f"{e['slug']}{suf}")
    # full-text index for search, loaded lazily by the browse page
    idx = {e["slug"]: re.sub(r"```.*?```", " ", md, flags=re.S).lower() for e, md, *_ in entries}
    (OUT / "assets" / "search.js").write_text("window.LOOKETAL_TEXT=" + json.dumps(idx, ensure_ascii=False) + ";", encoding="utf-8")
    es = [e for e, *_ in entries]
    coll = {cid: [e["slug"] for e in es if pred(e)] for cid, _, _, pred, _ in COLLECTIONS}
    coll_titles = {cid: t for cid, t, *_ in COLLECTIONS}
    (OUT / "assets" / "data.js").write_text(
        "window.LOOKETAL=" + json.dumps({"entries": es, "collections": coll, "collectionTitles": coll_titles},
                                        ensure_ascii=False) + ";", encoding="utf-8")
    (ROOT / "data" / "entries.json").write_text(json.dumps(es, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "index.html").write_text(build_home(entries), encoding="utf-8")
    (OUT / "browse.html").write_text(build_browse(), encoding="utf-8")
    (OUT / "collections.html").write_text(build_collections(entries), encoding="utf-8")
    (OUT / "prompts.html").write_text(build_prompts(entries), encoding="utf-8")
    (OUT / "about.html").write_text(build_about(entries), encoding="utf-8")
    for e, md, pre, sections in entries:
        (OUT / "s" / f"{e['slug']}.html").write_text(build_style(e, md, pre, sections, entries), encoding="utf-8")
        (OUT / "designs" / f"{e['slug']}.md").write_text(md, encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"{len(entries)} styles -> {OUT}")


if __name__ == "__main__":
    main()
