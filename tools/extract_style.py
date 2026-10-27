"""Extract measurable style facts from an academic web page (static HTML + linked CSS).

Usage: python -I -B extract_style.py URL [URL ...]  -> JSON list on stdout.
Measurements are frequency counts over declarations, not rendered computed styles.
"""
import json
import re
import sys
import urllib.request
from collections import Counter
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"
MAX_CSS = 12
SKIP_CSS = re.compile(r"font-?awesome|fontawesome|academicons|icons?\.css|all\.min\.css", re.I)


def fetch(url, limit=3_000_000):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=20) as r:
        final = r.geturl()
        raw = r.read(limit)
        ctype = r.headers.get_content_charset() or "utf-8"
    return final, raw.decode(ctype, errors="replace")


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.css_links, self.styles, self.scripts, self.fonts = [], [], [], []
        self.tags = Counter()
        self.links, self.iframes, self.classes = [], [], Counter()
        self.text, self.title, self._in = [], "", None
        self.meta = {}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags[tag] += 1
        for c in (a.get("class") or "").split():
            self.classes[c] += 1
        if tag == "link" and "stylesheet" in (a.get("rel") or "") and a.get("href"):
            self.css_links.append(a["href"])
        if tag == "link" and "fonts.googleapis" in (a.get("href") or ""):
            self.fonts.append(a["href"])
        if tag == "script" and a.get("src"):
            self.scripts.append(a["src"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "iframe" and a.get("src"):
            self.iframes.append(a["src"])
        if tag == "meta" and a.get("name") in ("generator", "description"):
            self.meta[a["name"]] = a.get("content", "")
        if tag in ("style", "title", "pre", "code"):
            self._in = tag

    def handle_endtag(self, tag):
        if tag == self._in:
            self._in = None

    def handle_data(self, data):
        if self._in == "style":
            self.styles.append(data)
        elif self._in == "title":
            self.title += data
        else:
            self.text.append(data)


COLOR = re.compile(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|hsla?\([^)]*\)")
DECL = re.compile(r"([a-z-]+)\s*:\s*([^;{}]+)")


def norm_color(c):
    c = c.lower().replace(" ", "")
    if re.fullmatch(r"#[0-9a-f]{3}", c):
        c = "#" + "".join(ch * 2 for ch in c[1:])
    return c


def analyze_css(css):
    out = {k: Counter() for k in ("color", "background", "border", "font_family", "font_size",
                                   "radius", "max_width", "shadow", "font_weight", "line_height", "accent")}
    for prop, val in DECL.findall(css):
        val = val.strip().replace("!important", "").strip()
        if prop == "color":
            for c in COLOR.findall(val):
                out["color"][norm_color(c)] += 1
        elif prop in ("background", "background-color"):
            for c in COLOR.findall(val):
                out["background"][norm_color(c)] += 1
        elif prop.startswith("border") and "radius" not in prop:
            for c in COLOR.findall(val):
                out["border"][norm_color(c)] += 1
        elif prop == "font-family":
            out["font_family"][val.split(",")[0].strip().strip("'\"")] += 1
        elif prop == "font-size":
            out["font_size"][val] += 1
        elif prop == "border-radius":
            out["radius"][val] += 1
        elif prop == "max-width" and ")" not in val:
            out["max_width"][val] += 1
        elif prop == "box-shadow" and val != "none":
            out["shadow"][val[:90]] += 1
        elif prop == "font-weight":
            out["font_weight"][val] += 1
        elif prop == "line-height":
            out["line_height"][val] += 1
        elif prop.startswith("--") and COLOR.search(val):
            out["accent"][f"{prop}:{norm_color(COLOR.search(val).group())}"] += 1
    return out


def detect(html_lower, p, scripts, css_urls):
    blob = " ".join([html_lower[:400000], " ".join(scripts).lower(), " ".join(css_urls).lower()])
    assets = " ".join(scripts + css_urls).lower() + " " + " ".join(p.classes).lower()
    gen = p.meta.get("generator", "").lower()
    tail = " ".join(p.text)[-2500:].lower()
    credit = [n for n, pat in [("nerfies", r"nerfies"), ("academic-project-page-template", r"academic project page template|eliahuhorwitz"),
                               ("jon-barron", r"jon barron|jonbarron"), ("al-folio", r"al-folio"),
                               ("academicpages", r"academicpages|academic pages"), ("hugo-blox/wowchemy", r"wowchemy|hugo blox|hugoblox"),
                               ("minimal-mistakes", r"minimal mistakes"), ("owlstown", r"owlstown")]
              if re.search(pat, tail)]
    fw = []
    for name, pat in [("bulma", r"bulma"), ("bootstrap", r"bootstrap"), ("tailwind", r"tailwind|cdn\.tailwindcss"),
                      ("jekyll", r"jekyll"), ("hugo", r"hugo"), ("wowchemy/hugo-blox", r"wowchemy|hugoblox|hugo-blox"),
                      ("al-folio", r"al-folio|al_folio"), ("academicpages", r"academicpages|minimal-mistakes"),
                      ("nerfies-template", r"nerfies|eliahuhorwitz|academic-project-page"),
                      ("jon-barron-template", r"jonbarron|jon barron"), ("next.js", r"_next/static"),
                      ("gatsby", r"gatsby"), ("react", r"react(-dom)?(\.production)?\.min\.js"),
                      ("google-sites", r"sites\.google\.com"), ("distill", r"distill\.pub/template")]:
        if re.search(pat, assets) or re.search(pat, gen):
            fw.append(name)
    links = " ".join(p.links + p.iframes).lower()
    text = " ".join(p.text).lower()
    modules = {
        "teaser_video": p.tags["video"] > 0,
        "youtube_or_vimeo": bool(re.search(r"youtube|youtu\.be|vimeo", links)),
        "bibtex": "@inproceedings" in text or "@article" in text or "@misc" in text or "bibtex" in text,
        "arxiv_link": "arxiv.org" in links,
        "code_link": "github.com" in links,
        "dataset_link": bool(re.search(r"huggingface\.co/datasets|dataset", links)),
        "hf_demo": bool(re.search(r"huggingface\.co/spaces|gradio", links + blob[:200000])),
        "interactive_3d": bool(re.search(r"three(\.min)?\.js|model-viewer|<canvas|viser|splat", blob)),
        "image_compare_slider": bool(re.search(r"twentytwenty|img-comparison|juxtapose|before-after|beforeafter", blob)),
        "carousel": bool(re.search(r"carousel|swiper|slick", blob)),
        "results_table": p.tags["table"] > 0,
        "math_rendering": bool(re.search(r"mathjax|katex", blob)),
        "dark_mode_toggle": bool(re.search(r"dark-?mode|theme-toggle|data-theme", blob)),
        "publication_list": len(re.findall(r"arxiv\.org|doi\.org|openreview\.net", links)) >= 5,
        "news_section": bool(re.search(r">\s*(news|updates)\s*<", html_lower[:400000])),
    }
    return fw, modules, gen, credit


def run(url):
    final, html = fetch(url)
    p = Page()
    p.feed(html)
    css_urls, css_text, css_errors = [], "\n".join(p.styles), []
    for href in p.css_links:
        u = urljoin(final, href)
        if SKIP_CSS.search(u) or "fonts.googleapis" in u:
            continue
        css_urls.append(u)
    for u in css_urls[:MAX_CSS]:
        try:
            css_text += "\n" + fetch(u, 1_500_000)[1]
        except Exception as e:  # report which stylesheet failed; page analysis continues on what was fetched
            css_errors.append(f"{u}: {type(e).__name__}")
    css_text += "\n" + "\n".join(re.findall(r'style="([^"]*)"', html))
    s = analyze_css(css_text)
    gfonts = sorted({f.replace("+", " ") for g in p.fonts for f in re.findall(r"family=([^:&;]+)", g)})
    fw, modules, gen, credit = detect(html.lower(), p, p.scripts, css_urls)
    top = lambda c, n=8: [[k, v] for k, v in c.most_common(n)]
    return {
        "url": url, "final_url": final, "host": urlparse(final).netloc, "title": p.title.strip()[:200],
        "generator": gen, "frameworks": fw, "footer_template_credit": credit, "google_fonts": gfonts, "modules": modules,
        "counts": {"img": p.tags["img"], "video": p.tags["video"], "iframe": p.tags["iframe"],
                   "table": p.tags["table"], "section": p.tags["section"], "h2": p.tags["h2"], "a": p.tags["a"]},
        "text_colors": top(s["color"]), "background_colors": top(s["background"]), "border_colors": top(s["border"], 5),
        "css_color_vars": top(s["accent"], 12), "font_families": top(s["font_family"]), "font_sizes": top(s["font_size"], 12),
        "font_weights": top(s["font_weight"], 5), "line_heights": top(s["line_height"], 5), "radii": top(s["radius"], 6),
        "max_widths": top(s["max_width"], 5), "shadows": top(s["shadow"], 3),
        "css_files": len(css_urls), "css_errors": css_errors,
    }


if __name__ == "__main__":
    res = []
    for u in sys.argv[1:]:
        try:
            res.append(run(u))
        except Exception as e:
            res.append({"url": u, "error": f"{type(e).__name__}: {e}"})
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False, indent=1))
