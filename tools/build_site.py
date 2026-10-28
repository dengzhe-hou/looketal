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
FEEDBACK = "https://github.com/dengzhe-hou/looketal/issues/new?title=Feedback:+"
esc = html.escape
# Cloudflare Web Analytics: cookieless visit counts; the token is the public site tag
ANALYTICS = """<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{"token": "55748c54d6a94a47bafac800c01c5e81"}'></script>"""

import sys  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parent))  # the build runs with python -I, which drops the script dir
import i18n  # noqa: E402

# the language being built; English pages sit at docs/, the others under docs/<lang>/ and share docs/assets/
LANG = "en"
SUBDIR = {"en": "", "ja": "ja/", "zh": "zh/"}


def T(key, **kw):
    return i18n.t(key, LANG, **kw)


def A(prefix):
    """Prefix for shared files (assets, designs), which live at the English root."""
    return prefix + ("../" if LANG != "en" else "")

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
    ("Badges", r"badge"), ("Install", r"install"), ("Model zoo", r"model zoo"),
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
    name = re.sub(r"\s*[—·] (Style|README) Reference\s*$", "", lines[0].lstrip("# ")).strip()
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
            "venue": venue, "conf": it.get("conf") or (venue.split()[0] if it["kind"] == "project" and venue else ""),
            "year": it.get("year"), "person": it.get("person", ""), "field": it.get("field", ""),
            "mood": it["mood"], "theme": it["theme"], "template": it["template"],
            "template_group": "README" if it["kind"] == "readme" else template_group(it["template"]),
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

HAS_README = False  # set in main(); the README nav item appears once the catalog has README entries


def lang_links(prefix, path):
    """Links to the same page in each language. prefix leads to this language's root; A(prefix) to docs/."""
    return "".join(f'<a href="{A(prefix)}{SUBDIR[l]}{path}" hreflang="{i18n.HTML_LANG[l]}" lang="{i18n.HTML_LANG[l]}"'
                   f'{" aria-current=true" if l == LANG else ""}>{i18n.LANG_NAMES[l]}</a>' for l in i18n.LANGS)


def nav(prefix, active, path):
    items = [("index.html", "nav_home", "home"), ("browse.html?kind=project", "nav_project", "project"),
             ("browse.html?kind=researcher", "nav_researcher", "researcher")]
    if HAS_README:
        items.append(("browse.html?kind=readme", "nav_readme", "readme"))
    items += [("browse.html", "nav_all", "all"), ("collections.html", "nav_collections", "collections"),
              ("prompts.html", "nav_prompts", "prompts"), ("about.html", "nav_about", "about")]
    links = "".join(f'<a href="{prefix}{h}"{" aria-current=page" if k == active else ""}>{esc(T(t))}</a>'
                    for h, t, k in items)
    return f"""<aside class="side"><a class="brand" href="{prefix}index.html"><span class="mark">et<br>al.</span><span>{SITE}</span></a>
<nav>{links}</nav><button class="theme-toggle" id="theme" type="button" aria-label="{esc(T('theme'))}">{esc(T('theme'))}: {esc(T('theme_auto'))}</button>
<div class="langs" role="group" aria-label="{esc(T('lang_label'))}">{lang_links(prefix, path)}</div>
<a class="feedback" href="{FEEDBACK}{quote(path)}" target="_blank" rel="noopener">{esc(T('feedback'))}</a>
<div class="side-foot">{T('side_foot')}</div></aside>"""


def page(title, body, prefix, active, path, desc=None, extra_head=""):
    alt = "".join(f'<link rel="alternate" hreflang="{i18n.HTML_LANG[l]}" href="{A(prefix)}{SUBDIR[l]}{path}">' for l in i18n.LANGS)
    return f"""<!doctype html>
<html lang="{i18n.HTML_LANG[LANG]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc or T('tagline'))}">{alt}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap" rel="stylesheet">
{extra_head}<link rel="stylesheet" href="{A(prefix)}assets/site.css"></head>
<body><div class="shell">{nav(prefix, active, path)}<main class="main">{body}</main></div>
<script src="{A(prefix)}assets/data.{LANG}.js"></script><script src="{A(prefix)}assets/site.js"></script>
{ANALYTICS}</body></html>"""


def specimen(e, big=False):
    """Token specimen: type sample and buttons drawn from measured palette and fonts (no page content)."""
    bg, text, accent = e["specimen"]
    font = esc(e["fonts"][0]) if e["fonts"] else "inherit"
    labels = {"project": ("Paper", "Code", "Video"), "readme": ("Install", "Usage", "Cite")}.get(e["kind"], ("CV", "Scholar", "Email"))
    pills = "".join(f'<i style="background:{esc(accent)}">{t}</i>' for t in labels)
    return f"""<div class="spec{' big' if big else ''}" style="background:{esc(bg)};color:{esc(text)};font-family:'{font}',system-ui,sans-serif" aria-hidden="true">
<b class="aa">Aa</b><span style="color:{esc(accent)}">{esc(e['fonts'][0] if e['fonts'] else 'system font')}</span><div class="pills">{pills}</div>
<div class="strip">{''.join(f'<em style="background:{esc(p["hex"])}"></em>' for p in e["palette"][:6])}</div></div>"""


def strip(e):
    return '<div class="strip">' + "".join(f'<em style="background:{esc(p["hex"])}"></em>' for p in e["palette"][:6]) + "</div>"


def thumb(e, prefix):
    if e.get("shot"):
        # the tall capture is fetched on first hover (site.js) and scrolls inside the card
        tall = f' data-tall="{A(prefix)}assets/shots/{e["slug"]}.tall.webp"' if e.get("tall") else ""
        return (f'<div class="shot"{tall}><img src="{A(prefix)}assets/shots/{e["slug"]}.card.webp" alt="" loading="lazy" '
                f'width="640" height="400">{strip(e)}</div>')
    return specimen(e)


def card(e, prefix):
    meta = {"project": e["venue"], "readme": f'{T("readme")} · {e["venue"]}'}.get(e["kind"], f'{T("researcher")} · {e["venue"]}')
    return f"""<a class="card" href="{prefix}s/{e['slug']}.html">{thumb(e, prefix)}
<div class="cbody"><div class="meta">{esc(meta)}</div><div class="name">{esc(e['title'])}</div>
<div class="mood">{esc(e['mood'])}</div></div></a>"""


# ---------- pages ----------

def wall(es):
    """Two rows of thumbnails drifting in opposite directions; each row is doubled so the loop is seamless."""
    shots = [e for e in es if e.get("shot")]
    def row(items, cls):
        cells = "".join(f'<a href="s/{e["slug"]}.html" tabindex="-1"><img src="{A("")}assets/shots/{e["slug"]}.card.webp" alt="" width="640" height="400"></a>' for e in items)
        return f'<div class="wrow {cls}"><div class="wtrack">{cells}{cells}</div></div>'
    return f'<div class="wall" aria-hidden="true">{row(shots[0::2][:18], "r1")}{row(shots[1::2][:18], "r2")}</div>'


def mod_name(m):
    names = i18n.MODULE_NAMES.get(m)
    return names[i18n.LANGS.index(LANG) - 1] if names and LANG != "en" else m


def build_home(entries):
    es = [e for e, *_ in entries]
    def facet(label, key, values):
        label_of = (lambda v: mod_name(v)) if key == "module" else str
        chips = "".join(f'<a class="chip" href="browse.html?{key}={quote(str(v))}">{esc(label_of(v))} <span>{n}</span></a>' for v, n in values)
        return f'<section class="facet"><h3>{label}</h3><div class="chips">{chips}</div></section>'
    confs = Counter(e["conf"] for e in es if e["conf"])
    years = Counter(e["year"] for e in es if e["kind"] == "project")
    tpls = Counter(e["template_group"] for e in es)
    mods = Counter(m for e in es for m in e["modules"])
    fields = Counter(e["field"].split("/")[0].split(",")[0].strip() for e in es if e["field"]).most_common(14)
    recent = [e for e in es if e["kind"] == "project" and e["year"] == 2026][:8]
    n_readme = sum(e['kind'] == 'readme' for e in es)
    readme_link = f'<a href="browse.html?kind=readme">{T("nav_readme")} <span>{n_readme}</span></a>' if n_readme else ""
    body = f"""<header class="hero"><h1>{SITE}</h1><p class="lede">{T("hero_lede", tagline=T("tagline"))}</p>
<form class="search" action="browse.html"><input name="q" type="search" placeholder="{esc(T('search_ph'))}" aria-label="{esc(T('search_btn'))}">
<button>{T('search_btn')}</button></form>
<div class="quick"><a href="browse.html?kind=project">{T('nav_project')} <span>{sum(e['kind']=='project' for e in es)}</span></a>
<a href="browse.html?kind=researcher">{T('nav_researcher')} <span>{sum(e['kind']=='researcher' for e in es)}</span></a>{readme_link}
<a href="collections.html">{T('nav_collections')}</a><a href="prompts.html">{T('nav_prompts')}</a></div></header>
{wall(es)}
<div class="facets">
{facet(T("facet_venues"), "conf", sorted(confs.items()))}
{facet(T("facet_years"), "year", sorted(years.items(), reverse=True))}
{facet(T("facet_templates"), "tpl", tpls.most_common())}
{facet(T("facet_modules"), "module", mods.most_common())}
{facet(T("facet_fields"), "q", fields)}
</div>
<section><div class="sechead"><h2>{T('new_2026')}</h2><a href="browse.html?year=2026">{T('see_all')}</a></div>
<div class="grid">{''.join(card(e, '') for e in recent)}</div></section>"""
    return page(f"{SITE} · {T('tagline')}", body, "", "home", "index.html")


def build_browse():
    readme_btn = f'<button data-v="readme">{T("nav_readme")}</button>' if HAS_README else ""
    body = f"""<header class="phead"><h1 id="btitle">{T('nav_all')}</h1><p class="lede" id="bcount"></p></header>
<div class="filters" id="filters">
<input type="search" id="q" placeholder="{esc(T('search_short'))}" aria-label="{esc(T('search_btn'))}">
<div class="seg" id="kind" role="group"><button data-v="">{T('kind_all')}</button><button data-v="project">{T('nav_project')}</button><button data-v="researcher">{T('kind_researchers')}</button>{readme_btn}</div>
<select id="conf" aria-label="{esc(T('m_venue'))}"><option value="">{T('all_venues')}</option></select>
<select id="year" aria-label="{esc(T('m_year'))}"><option value="">{T('all_years')}</option></select>
<select id="tpl" aria-label="{esc(T('m_template'))}"><option value="">{T('all_templates')}</option></select>
<select id="theme" aria-label="{esc(T('m_theme'))}"><option value="">{T('any_theme')}</option><option value="light">{T('light')}</option><option value="dark">{T('dark')}</option><option value="both">{T('both')}</option></select>
</div><div class="chips mods" id="mods"></div>
<div class="grid" id="grid"></div>"""
    return page(f"{T('browse')} · {SITE}", body, "", "all", "browse.html")


def section_md(sections, *names):
    for n in names:
        for k, v in sections.items():
            if k.lower().startswith(n.lower()):
                return v
    return ""


KIND_NAV = {"project": "nav_project", "researcher": "nav_researcher", "readme": "nav_readme"}


def bigshot(e):
    """Screenshot in a browser frame; the tall capture scrolls inside it."""
    if not e["shot"]:
        return ""
    src = f'{A("../")}assets/shots/{e["slug"]}.{"tall.webp" if e["tall"] else "webp"}'
    w, h = (720, 1350) if e["tall"] else (1200, 750)
    host = esc(re.sub(r"^https?://", "", e["url"]).rstrip("/"))
    link = f'<a href="{esc(e["url"])}" target="_blank" rel="noopener">{esc(e["url"])}</a>'
    return (f'<figure class="bigshot"><a class="frame{" scroll" if e["tall"] else ""}" href="{esc(e["url"])}" target="_blank" rel="noopener">'
            f'<span class="bar"><i></i><i></i><i></i><b>{host}</b></span><span class="view"><img src="{src}" alt="{esc(e["title"])}" width="{w}" height="{h}"></span></a>'
            f'<figcaption>{T("shot_caption", link=link)} <a href="{ISSUES}&amp;title=Removal:+{e["slug"]}" target="_blank" rel="noopener">{T("request_removal")}</a></figcaption></figure>')


def build_style(e, md, pre, sections, entries):
    css = css_block(md)
    tw = tailwind_from_css(css)
    is_readme = e["kind"] == "readme"
    compact_keys = [k for k in sections if re.match(r"(Header Block|Badges|Agent Prompt|Quick Start)" if is_readme else r"(Tokens|Agent Prompt)", k)]
    compact = f"# {e['style_name']} — {'README' if is_readme else 'Style'} Reference\n\n" + pre + "\n\n" + "\n\n".join(f"## {k}\n\n{sections[k]}" for k in compact_keys)
    sim = [x for x, *_ in entries if x["slug"] != e["slug"] and x["kind"] == e["kind"] and x["template_group"] == e["template_group"]]
    sim += [x for x, *_ in entries if x["slug"] != e["slug"] and x["kind"] == e["kind"] and x not in sim and x["conf"] == e["conf"]]
    swatches = "".join(f"""<button class="sw" data-copy="{esc(p['hex'])}"><span style="background:{esc(p['hex'])}"></span>
<b>{esc(p['name'])}</b><code>{esc(p['hex'])}</code><small>{esc(p['role'])}</small></button>""" for p in e["palette"])
    fonts_q = "&".join("family=" + f.replace(" ", "+") for f in e["fonts"][:2] if re.fullmatch(r"[A-Za-z0-9 ]+", f))
    extra = f'<link href="https://fonts.googleapis.com/css2?{fonts_q}&display=swap" rel="stylesheet">\n' if fonts_q else ""
    sample = f"{e['title']}, {e['field']}" if e["kind"] == "researcher" else e["title"]
    type_rows = "".join(f"""<div class="trow"><div class="tlabel">{esc(f)}</div>
<div class="tsample" style="font-family:'{esc(f)}',system-ui,sans-serif"><span class="t1">{esc(sample[:70])}</span>
<span class="t2">Abstract · Method · Results · BibTeX — 0123456789</span></div></div>""" for f in e["fonts"])
    status = T("status_rendered") if e["rendered_check"] else T("status_static")
    is_res = e["kind"] == "researcher"
    meta_rows = [(T("m_award") if is_res else T("m_venue"), e["venue"]), (T("m_year"), e["year"]),
                 (T("m_person") if is_res else T("m_first_author"), e["person"]), (T("m_field"), e["field"]),
                 (T("m_template"), e["template"]), (T("m_theme"), T(e["theme"]))]
    meta = "".join(f"<dt>{esc(k)}</dt><dd>{esc(str(v))}</dd>" for k, v in meta_rows if v)
    blocks = {k: section_md(sections, k) for k in ("Overview", "Tokens — Spacing", "Page Modules", "Do's", "Layout", "Components",
                                                   "Header Block", "Section Outline")}
    if not blocks["Overview"]:
        # some files keep the overview in the preamble, after the theme line and the measurement note (Refero's own layout)
        paras = [p for p in re.split(r"\n\s*\n", pre) if p.strip() and not p.lstrip().startswith((">", "**Theme"))]
        blocks["Overview"] = "\n\n".join(paras[1:] if len(paras) > 1 else paras)
    payload = json.dumps({"md": md, "compact": compact, "css": css, "tw": tw, "tokens": tokens_json(e), "blocks": blocks},
                         ensure_ascii=False).replace("</", "<\\/")
    page_mid = f"""<section><h2>{T('palette')}</h2><div class="swatches" lang="en">{swatches}</div></section>
<section><h2>{T('typography')}</h2>{type_rows}</section>
<section lang="en"><h2>{T('spacing')}</h2><div class="mdx" data-block="Tokens — Spacing"></div></section>
<section lang="en"><h2>{T('page_modules')}</h2><div class="mdx" data-block="Page Modules"></div></section>"""
    # a README has no page CSS of its own: show its header recipe, badge colors and section outline instead
    readme_mid = f"""<section lang="en"><h2>{T('header_block')}</h2><div class="mdx" data-block="Header Block"></div></section>
<section><h2>{T('badge_colors')}</h2><div class="swatches" lang="en">{swatches}</div></section>
<section lang="en"><h2>{T('section_outline')}</h2><div class="mdx" data-block="Section Outline"></div></section>"""
    crumbs = f'<a href="../index.html">{SITE}</a> / <a href="../browse.html?kind={e["kind"]}">{T(KIND_NAV[e["kind"]])}</a>'
    body = f"""<div class="style">
<div class="sleft">
<div class="crumbs">{crumbs}</div>
<h1 class="sname">{esc(e['title'])}</h1>
<p class="smood">{esc(e['mood'])}</p>
{bigshot(e)}
{"" if is_readme else specimen(e, big=True)}
<div class="sactions"><a class="btn primary" href="{esc(e['url'])}" target="_blank" rel="noopener">{T('visit_repo') if e['kind'] == 'readme' else T('visit')}</a>
<a class="btn" href="{A('../')}designs/{e['slug']}.md" download>{T('download_md')}</a></div>
<dl class="smeta">{meta}</dl><p class="status">{esc(status)}{' ' + esc(e['issues']) if LANG == 'en' and e['issues'] else ''}</p>
{f'<section><h2>{T("why_here")}</h2><p>{esc(e["selection"]["why"])}</p></section>' if e.get("selection", {}).get("why") else ""}
{f'<p class="langnote">{T("md_in_english")}</p>' if LANG != "en" else ""}
<section lang="en"><h2>{T('overview')}</h2><div class="mdx" data-block="Overview"></div></section>
{readme_mid if is_readme else page_mid}
<section lang="en"><h2>{T('guidelines')}</h2><div class="mdx" data-block="Do's"></div></section>
<section><h2>{T('more_like')}</h2><div class="grid small">{''.join(card(x, '../') for x in sim[:6])}</div></section>
</div>
<aside class="sright"><div class="panel">
<div class="ptabs" role="tablist"><button data-tab="md" aria-selected="true">DESIGN.md</button><button data-tab="tw">Tailwind v4</button><button data-tab="css">CSS Variables</button><button data-tab="tokens">Design Tokens</button></div>
<div class="ptools"><div class="seg sm" id="mode"><button data-v="compact">{T('compact')}</button><button data-v="extended" aria-pressed="true">{T('extended')}</button></div>
<button class="btn sm" id="pcopy">{T('copy')}</button><a class="btn sm" href="{A('../')}designs/{e['slug']}.md" download>.md</a></div>
<pre class="pbody" id="pbody"></pre></div></aside>
</div>
<script id="style-data" type="application/json">{payload}</script>"""
    return page(f"{T('design_system', title=e['title'])} · {SITE}", body, "../", e["kind"], f"s/{e['slug']}.html", desc=e["mood"],
                extra_head=extra + '<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>\n')


COLLECTIONS = [
    ("nerfies-family", lambda e: e["kind"] == "project" and e["template_group"] in ("Nerfies / Bulma", "Academic Project Page Template")),
    ("built-from-scratch", lambda e: e["kind"] == "project" and e["template_group"] == "Custom"),
    ("show-dont-tell", lambda e: e["kind"] == "project" and any(m in e["modules"] for m in ("Comparison slider", "Interactive 3D", "Demo"))),
    ("researcher-homepages", lambda e: e["kind"] == "researcher"),
    ("readme-gallery", lambda e: e["kind"] == "readme"),
    ("dark-and-dual", lambda e: e["kind"] != "readme" and e["theme"] in ("dark", "both")),
]


def coll_text(cid):
    i = i18n.LANGS.index(LANG)
    return tuple(x[i] for x in i18n.COLLECTIONS[cid])


def build_collections(entries):
    es = [e for e, *_ in entries]
    parts = []
    for cid, pred in COLLECTIONS:
        items = [e for e in es if pred(e)]
        if not items:
            continue
        title, desc, closer = coll_text(cid)
        parts.append(f"""<section class="coll" id="{cid}"><div class="sechead"><h2>{esc(title)} <span class="count">{len(items)}</span></h2>
<a href="browse.html?collection={cid}">{T('see_all')}</a></div><p class="lede">{esc(desc)}</p>
<div class="grid">{''.join(card(e, '') for e in items[:6])}</div>
<div class="closer"><span>{T('look_closer')}</span><p>{esc(closer)}</p></div></section>""")
    body = f'<header class="phead"><div class="eyebrow">{T("nav_collections")}</div><h1>{T("nav_collections")}</h1><p class="lede">{T("collections_lede")}</p></header>{"".join(parts)}'
    return page(f"{T('nav_collections')} · {SITE}", body, "", "collections", "collections.html")


def build_prompts(entries):
    es = [e for e, *_ in entries]
    ex = next(e for e in es if e["kind"] == "project" and e["template_group"] == "Custom")
    ex2 = next(e for e in es if e["kind"] == "researcher")
    ex3 = next((e for e in es if e["kind"] == "readme"), None)
    ref = lambda x: f'<p>{T("example_ref")}: <a href="s/{x["slug"]}.html">{esc(x["title"])}</a></p>'
    readme = f'<section><h2>{T("p_readme")}</h2><pre class="prompt">{esc(T("prompt_readme"))}</pre>{ref(ex3)}</section>' if ex3 else ""
    body = f"""<header class="phead"><div class="eyebrow">{T('nav_collections')}</div><h1>{T('prompts_h1')}</h1>
<p class="lede">{T('prompts_lede')}</p></header>
<section><h2>{T('p_project')}</h2><pre class="prompt">{esc(T('prompt_project'))}</pre>{ref(ex)}</section>
<section><h2>{T('p_researcher')}</h2><pre class="prompt">{esc(T('prompt_researcher'))}</pre>{ref(ex2)}</section>
{readme}
<section><h2>{T('p_restyle')}</h2><pre class="prompt">{esc(T('prompt_restyle'))}</pre></section>"""
    return page(f"{T('nav_prompts')} · {SITE}", body, "", "prompts", "prompts.html")


def build_about(entries):
    es = [e for e, *_ in entries]
    kinds = Counter(e["kind"] for e in es)
    removal = (f'<a href="{ISSUES}" target="_blank" rel="noopener">' + {"en": "open a removal request</a> (a short GitHub form)",
               "ja": "削除依頼フォーム</a>(GitHub の短いフォーム)", "zh": "删除申请表</a>(GitHub 上的简短表单)"}[LANG])
    body = i18n.about(LANG, n_proj=kinds["project"], n_res=kinds["researcher"], n_readme=kinds["readme"],
                      n_rend=sum(e["rendered_check"] for e in es), n_all=len(es), removal=removal, site=SITE)
    return page(f"{T('nav_about')} · {SITE}", body, "", "about", "about.html")


def localize(entries, lang):
    """Per-language copy of the entries: mood and selection reason from data/i18n/<lang>.json when present."""
    if lang == "en":
        return entries, 0
    tr = json.loads((ROOT / "data" / "i18n" / f"{lang}.json").read_text(encoding="utf-8"))
    out, missing = [], 0
    for e, md, pre, sections in entries:
        x = tr.get(e["slug"])
        if not x:
            missing += 1
            out.append((e, md, pre, sections))
            continue
        sel = dict(e["selection"], why=x.get("why") or e["selection"].get("why", ""))
        out.append(({**e, "mood": x["mood"], "selection": sel}, md, pre, sections))
    return out, missing


def ui_strings():
    keys = ["copied", "copy_failed", "theme", "theme_auto", "theme_light", "theme_dark", "count", "searching", "loading_index",
            "no_match", "not_available", "researcher", "readme", "nav_project", "nav_researcher", "nav_readme", "nav_all"]
    ui = {k: T(k) for k in keys}
    ui["mods"] = {m: mod_name(m) for m in i18n.MODULE_NAMES}
    return ui


def main():
    global LANG, HAS_README
    base = load_entries()
    HAS_README = any(e["kind"] == "readme" for e, *_ in base)
    base_es = [e for e, *_ in base]
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "designs").mkdir(parents=True)
    (OUT / "assets" / "shots").mkdir(parents=True)
    for f in ("site.css", "site.js"):
        shutil.copy(ROOT / "tools" / "assets" / f, OUT / "assets" / f)
    for e, md, *_ in base:
        if e["shot"]:
            for suf in (".webp", ".card.webp") + ((".tall.webp",) if e["tall"] else ()):
                shutil.copy(ROOT / "content" / "shots" / f"{e['slug']}{suf}", OUT / "assets" / "shots" / f"{e['slug']}{suf}")
        (OUT / "designs" / f"{e['slug']}.md").write_text(md, encoding="utf-8")
    # full-text index for search over the English DESIGN.md text, loaded lazily by the browse page
    idx = {e["slug"]: re.sub(r"```.*?```", " ", md, flags=re.S).lower() for e, md, *_ in base}
    (OUT / "assets" / "search.js").write_text("window.LOOKETAL_TEXT=" + json.dumps(idx, ensure_ascii=False) + ";", encoding="utf-8")
    (ROOT / "data" / "entries.json").write_text(json.dumps([e for e, *_ in base], ensure_ascii=False, indent=1), encoding="utf-8")
    for lang in i18n.LANGS:
        LANG = lang
        entries, missing = localize(base, lang)
        root = OUT / SUBDIR[lang]
        (root / "s").mkdir(parents=True, exist_ok=True)
        es = [e for e, *_ in entries]
        coll = {cid: [e["slug"] for e in es if pred(e)] for cid, pred in COLLECTIONS}
        coll_titles = {cid: coll_text(cid)[0] for cid, _ in COLLECTIONS}
        (OUT / "assets" / f"data.{lang}.js").write_text(
            "window.LOOKETAL=" + json.dumps({"entries": es, "collections": coll, "collectionTitles": coll_titles,
                                            "ui": ui_strings(), "assets": A("")}, ensure_ascii=False) + ";", encoding="utf-8")
        (root / "index.html").write_text(build_home(entries), encoding="utf-8")
        (root / "browse.html").write_text(build_browse(), encoding="utf-8")
        (root / "collections.html").write_text(build_collections(entries), encoding="utf-8")
        (root / "prompts.html").write_text(build_prompts(entries), encoding="utf-8")
        (root / "about.html").write_text(build_about(entries), encoding="utf-8")
        for e, md, pre, sections in entries:
            (root / "s" / f"{e['slug']}.html").write_text(build_style(e, md, pre, sections, entries), encoding="utf-8")
        print(f"{lang}: {len(entries)} styles" + (f", {missing} without a translated mood/reason (English shown)" if missing else ""))
    LANG = "en"
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    (OUT / "CNAME").write_text("looketal.com\n", encoding="utf-8")  # GitHub Pages custom domain
    # sitemap with every page in each language, linked as alternates, for search engines
    paths = ["index.html", "browse.html", "collections.html", "prompts.html", "about.html"] + [f"s/{e['slug']}.html" for e in base_es]
    def url(l, p):
        return f"https://looketal.com/{SUBDIR[l]}{'' if p == 'index.html' else p}"
    rows = "".join("<url><loc>" + url(l, p) + "</loc>" + "".join(
        f'<xhtml:link rel="alternate" hreflang="{i18n.HTML_LANG[a]}" href="{url(a, p)}"/>' for a in i18n.LANGS) + "</url>\n"
        for p in paths for l in i18n.LANGS)
    (OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                                     'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + rows + "</urlset>\n", encoding="utf-8")
    (OUT / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: https://looketal.com/sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    main()
