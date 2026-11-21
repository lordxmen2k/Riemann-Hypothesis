#!/usr/bin/env python3
"""Flexible arXiv API search (all/au/ti fields, any query string).

Usage:
  axsearch.py "all:proportion of zeros critical line"
  axsearch.py --field au --max 20 "Demichel"
  axsearch.py --field all --max 10 "Riemann hypothesis function field"
"""
import argparse
import re
import sys
import time
import urllib.parse
import urllib.request

NS = "{http://www.w3.org/2005/Atom}"
UA = "RHBookVerification/1.0 (research use)"


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip()


def fetch(query: str, max_results: int = 10):
    url = (
        "https://export.arxiv.org/api/query?search_query="
        + urllib.parse.quote(query)
        + f"&max_results={max_results}"
    )
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("queries", nargs="+")
    ap.add_argument("--field", default="all", choices=["all", "ti", "au", "abs", "cat"])
    ap.add_argument("--max", type=int, default=10)
    args = ap.parse_args()

    for raw in args.queries:
        query = raw if ":" in raw.split()[0] else f'{args.field}:"{raw}"'
        try:
            xml = fetch(query, args.max)
        except Exception as e:
            print(f"### {query} -> ERROR {type(e).__name__}: {e}\n")
            continue
        entries = re.findall(r"<entry>(.*?)</entry>", xml, re.S)
        total = re.search(r"opensearch:totalResults[^>]*>(\d+)<", xml)
        print(f"### QUERY: {query}   total={total.group(1) if total else '?'}  shown={len(entries)}")
        for e in entries:
            aid = re.search(r"<id>(.*?)</id>", e, re.S)
            title = clean(re.search(r"<title>(.*?)</title>", e, re.S).group(1))
            authors = [clean(a) for a in re.findall(r"<name>(.*?)</name>", e, re.S)]
            jref = re.search(r"<arxiv:journal_ref[^>]*>(.*?)</arxiv:journal_ref>", e, re.S)
            doi = re.search(r"<arxiv:doi[^>]*>(.*?)</arxiv:doi>", e, re.S)
            pub = re.search(r"<published>(.*?)</published>", e, re.S)
            summ = clean(re.search(r"<summary>(.*?)</summary>", e, re.S).group(1))
            print(f"  ID   : {aid.group(1).split('/abs/')[-1] if aid else '?'}")
            print(f"  TITLE: {title}")
            print(f"  AUTH : {'; '.join(authors)}")
            print(f"  DATE : {pub.group(1)[:10] if pub else '?'}")
            print(f"  JREF : {clean(jref.group(1)) if jref else '(none)'}")
            print(f"  DOI  : {clean(doi.group(1)) if doi else '(none)'}")
            print(f"  ABS  : {summ[:700]}")
            print()
        time.sleep(1.5)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
