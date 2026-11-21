#!/usr/bin/env python3
"""Crossref bibliographic lookup, one query per argv entry.

Usage: crq.py "query one" "query two" ...
"""
import json
import sys
import time
import urllib.parse
import urllib.request

UA = "RHBookVerification/1.0 (mailto:research@example.org)"


def q(query, rows=4):
    u = "https://api.crossref.org/works?" + urllib.parse.urlencode(
        {
            "query.bibliographic": query,
            "rows": rows,
            "mailto": "research@example.org",
            "select": "DOI,title,container-title,volume,page,issued,author,type,abstract",
        }
    )
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
        f"{a.get('family','')}, {a.get('given','')}".strip(", ") for a in au[:8]
    )
    if len(au) > 8:
        names += f" (+{len(au)-8} more)"
    yr = it.get("issued", {}).get("date-parts", [[None]])[0][0]
    t = (it.get("title") or ["?"])[0]
    c = (it.get("container-title") or ["-"])[0]
    return (
        f"  {t}\n"
        f"    {c} | v{it.get('volume','?')} | p{it.get('page', it.get('article-number','?'))} | {yr} | {it.get('type','')}\n"
        f"    DOI: {it.get('DOI')}\n"
        f"    AUTHORS: {names}"
    )


for query in sys.argv[1:]:
    print(f"=== {query}")
    for it in q(query):
        print(fmt(it))
    print()
    time.sleep(1.2)
