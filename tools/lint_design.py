"""Deterministic checks for a v2 DESIGN.md (see content/METHOD.md).

Usage: python -I -B tools/lint_design.py FILE.md [FILE.md ...]
Fails (exit 1) when a required section is missing or out of order, or when a hex color used in the
prompt guide / quick start / components is not listed in the color table. Reports the 'inferred' count.
"""
import re
import sys
from pathlib import Path

REQUIRED = ["Overview", "First Viewport", "Tokens — Colors", "Tokens — Typography", "Tokens — Spacing & Shapes",
            "Layout Metrics", "Components", "Page Modules", "Adapting to Other Content", "Do's and Don'ts",
            "Surfaces", "Imagery", "Layout", "Agent Prompt Guide", "Similar Pages", "Quick Start", "Provenance"]
REQUIRED_README = ["Overview", "Header Block", "Badges", "Section Outline", "Components", "Imagery",
                   "Adapting to Other Content", "Do's and Don'ts", "Agent Prompt Guide", "Similar Pages", "Quick Start", "Provenance"]
HEX = re.compile(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b")
RGB = re.compile(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)")


def norm(h):
    h = h.lower()
    return "#" + "".join(c * 2 for c in h[1:]) if len(h) == 4 else h


def colors_in(text):
    out = {norm(h) for h in HEX.findall(text)}
    out |= {"#%02x%02x%02x" % tuple(int(v) for v in m) for m in RGB.findall(text)}
    return out


def lint(path):
    md = Path(path).read_text(encoding="utf-8")
    problems = []
    readme = bool(re.match(r"# .+ — README Reference\n", md))  # README references: content/METHOD_README.md
    if not readme and not re.match(r"# .+ — Style Reference\n", md):
        problems.append("first line must be '# <Name> — Style Reference' or '# <Name> — README Reference'")
    if not re.search(r"^> .+", md, re.M):
        problems.append("missing mood line ('> ...')")
    if not re.search(r"^\*\*Theme:\*\* (light|dark|both)", md, re.M):
        problems.append("missing '**Theme:** light|dark|both'")
    heads = re.findall(r"^## (.+?)\s*$", md, re.M)
    pos = -1
    for h in (REQUIRED_README if readme else REQUIRED):
        if h not in heads:
            problems.append(f"missing section: {h}")
            continue
        i = heads.index(h)
        if i < pos:
            problems.append(f"section out of order: {h}")
        pos = max(pos, i)
    sections = dict(re.findall(r"^## (.+?)\s*\n(.*?)(?=^## |\Z)", md, re.M | re.S))
    table = colors_in(sections.get("Tokens — Colors", "")) | colors_in(sections.get("First Viewport", "")) | colors_in(sections.get("Badges", ""))
    used = set()
    for k in ("Agent Prompt Guide", "Quick Start", "Components", "Layout Metrics", "Surfaces"):
        used |= colors_in(sections.get(k, ""))
    stray = sorted(used - table - {"#ffffff", "#000000"})
    if stray:
        problems.append(f"colors used but not in the color table: {', '.join(stray)}")
    if not readme and "share" not in sections.get("First Viewport", "").lower() and "%" not in sections.get("First Viewport", ""):
        problems.append("First Viewport has no color share")
    inferred = len(re.findall(r"inferred", md, re.I))
    return problems, inferred


def main():
    bad = 0
    for f in sys.argv[1:]:
        problems, inferred = lint(f)
        status = "OK" if not problems else "FAIL"
        print(f"{status} {f} (inferred: {inferred})")
        for p in problems:
            print(f"  - {p}")
        bad += bool(problems)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
