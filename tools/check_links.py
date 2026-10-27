"""Check that every catalogued page still loads. Writes data/link_status.json; exits 1 if any page is broken.

Usage: python -I -B tools/check_links.py
"""
import json
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (compatible; looketal-linkcheck; +https://github.com/dengzhe-hou/looketal)"


def check(item):
    req = urllib.request.Request(item["url"], headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return {"slug": item["slug"], "url": item["url"], "status": r.status, "final_url": r.geturl()}
    except urllib.error.HTTPError as e:
        return {"slug": item["slug"], "url": item["url"], "status": e.code}
    except Exception as e:  # DNS failure, timeout, TLS error: the page is unreachable either way
        return {"slug": item["slug"], "url": item["url"], "status": None, "error": f"{type(e).__name__}: {e}"}


def main():
    items = json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(check, items))
    # 403/429 usually mean a bot wall, not a dead page; report them separately
    broken = [r for r in res if r["status"] is None or (r["status"] >= 400 and r["status"] not in (403, 429))]
    blocked = [r for r in res if r["status"] in (403, 429)]
    out = {"checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "total": len(res),
           "broken": broken, "blocked": blocked, "results": res}
    (ROOT / "data" / "link_status.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(res)} checked, {len(broken)} broken, {len(blocked)} blocked")
    for r in broken:
        print(f"BROKEN {r['slug']} {r['url']} {r.get('status') or r.get('error')}")
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
