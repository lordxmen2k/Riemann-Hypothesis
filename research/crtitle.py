#!/usr/bin/env python3
"""Crossref title-specific search with a year filter window.

Usage: crtitle.py "title phrase" ["title phrase" ...]
Env: CRROWS (default 5), CRYEAR (default 0 = no filter)
"""
import json
import os
import sys
import time
import urllib.parse
import urllib.request

UA = "RHBookVerification/1.0 (mailto:research@example.org)"
ROWS = int(os.environ.get("CRROWS", "5"))
YEAR = int(os.environ.get("CRYEAR", "0"))


def q(title, rows=ROWS):
    params = {
        "query.title": title,
        "rows": rows,
        "mailto": "research@example.org",
        "select": "DOI,title,container-title,volume,page,issued,author,type",
    }
    if YEAR:
        params["filter"] = f"from-pub-date:{YEAR}-01-01,until-pub-date:{YEAR}-12-31"
    u = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            r = urllib.request.urlopen(
                urllib.request.Request(u, headers={"User-Agent": UA}), timeout=30
            )
            return json.load(r)["message"]["items"]
        except Exception as e:
            if attempt == 3:
                return [{"ERR": f"{type(e).__name__}: {e}"}]
            time.sleep(3 * (attempt + 1))


def fmt(it):
    if "ERR" in it:
        return "  !! " + it["ERR"]
    au = it.get("author", [])
    names = "; ".join(
        f"{a.get('family','')}, {a.get('given','')}".strip(", ") for a in au[:10]
    )
    if len(au) > 10:
        names += f" (+{len(au)-10} more)"
    yr = it.get("issued", {}).get("date-parts", [[None]])[0][0]
    t = (it.get("title") or ["?"])[0]
    c = (it.get("container-title") or ["-"])[0]
    return (
        f"  {t}\n"
        f"    {c} | v{it.get('volume','?')} | p{it.get('page', it.get('article-number','?'))} | {yr} | {it.get('type','')}\n"
        f"    DOI: {it.get('DOI')}\n"
        f"    AUTHORS: {names or '(none listed)'}"
    )


for title in sys.argv[1:]:
    print(f"=== {title}")
    for it in q(title):
        print(fmt(it))
    print()
    time.sleep(1.0)
