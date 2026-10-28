"""Build the README candidate pool from the project-page pool: each page's own link to its code repository.

Usage: python -I -B tools/readme_pool.py POOL.json [POOL.json ...] > readme_pool.json
POOL.json is a list of project entries ({url, venue, year, title, person, field, ...}). For each page the
script fetches the HTML, takes the first github.com/<owner>/<repo> link that is not the page's own
site repo or a known page template, and keeps the repo when the GitHub API reports a README of at
least MIN_BYTES. Needs the gh CLI (authenticated) for the API calls.
"""
import json
import re
import subprocess
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

MIN_BYTES = 2500  # shorter READMEs have too little structure to judge or describe
LINK = re.compile(r'href="https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)(?:\.git)?(?:/(?:tree|blob)/[^"]*)?/?"')
SKIP_OWNERS = {"sponsors", "orgs", "features", "topics", "about", "login", "marketplace"}
TEMPLATES = {("nerfies", "nerfies.github.io"), ("eliahuhorwitz", "academic-project-page-template"),
             ("google", "nerfies"), ("jonbarron", "website"), ("alshedivat", "al-folio")}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (looketal readme pool)"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read(2_000_000).decode("utf-8", "replace")


def repo_of(entry):
    try:
        page = fetch(entry["url"])
    except Exception as ex:  # a page that no longer loads simply contributes no repo
        return None, f"page: {ex.__class__.__name__}"
    for owner, name in LINK.findall(page):
        o, n = owner.lower(), name.lower()
        if o in SKIP_OWNERS or n.endswith(".github.io") or (o, n) in TEMPLATES:
            continue
        return f"{owner}/{name}", None
    return None, "no repo link"


def readme_size(repo):
    r = subprocess.run(["gh", "api", f"repos/{repo}/readme", "--jq", ".size,.path"], capture_output=True, text=True)
    if r.returncode:
        return None, None
    size, path = r.stdout.split()
    return int(size), path


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    entries = [e for f in sys.argv[1:] for e in json.load(open(f, encoding="utf-8")) if e.get("kind", "project") == "project"]
    with ThreadPoolExecutor(8) as ex:
        repos = list(ex.map(repo_of, entries))
    out, seen, why = [], set(), {}
    for e, (repo, err) in zip(entries, repos):
        if not repo:
            why[err] = why.get(err, 0) + 1
            continue
        if repo.lower() in seen:
            continue
        seen.add(repo.lower())
        out.append({"repo": repo, "page": e})
    with ThreadPoolExecutor(8) as ex:
        sizes = list(ex.map(lambda x: readme_size(x["repo"]), out))
    kept = []
    for x, (size, path) in zip(out, sizes):
        if size is None:
            why["no readme / repo gone"] = why.get("no readme / repo gone", 0) + 1
        elif size < MIN_BYTES:
            why["readme too short"] = why.get("readme too short", 0) + 1
        else:
            kept.append({**x, "readme_bytes": size, "readme_path": path})
    print(json.dumps(kept, ensure_ascii=False, indent=1))
    print(json.dumps({"pages": len(entries), "repos": len(out), "kept": len(kept), "dropped": why}), file=sys.stderr)


if __name__ == "__main__":
    main()
