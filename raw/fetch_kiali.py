#!/usr/bin/env python3
"""Fetch Kiali docs pages and save verbatim markdown with frontmatter.

Usage: python3 fetch_kiali.py <slug> <url>
Writes /root/wiki/raw/articles/kiali-docs-<slug>.md with frontmatter:
  source_url, ingested, sha256 (of body only).
"""
import sys, re, json, hashlib
import urllib.request
from bs4 import BeautifulSoup
import html2text

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
OUT = "/root/wiki/raw/articles"

def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")

def extract_article(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    content = soup.select_one("div.td-content")
    if content is None:
        raise RuntimeError("no div.td-content found — page structure changed?")
    # Drop chrome elements that are not article body
    for sel in ["nav", "button", "iframe", "svg", "form",
                 "div.announcement", "div.alert"]:
        for el in content.select(sel):
            el.decompose()
    # TOC / on-this-page sidebar usually outside td-content; also drop any
    # "on this page" navigation if present
    for el in content.select("a[href^='#']"):
        pass  # keep inline anchor links, they are part of text flow
    h = html2text.HTML2Text()
    h.body_width = 0
    h.ignore_images = False
    h.ignore_links = False
    h.bypass_tables = False
    md = h.handle(str(content))
    # Collapse >3 consecutive newlines to 2, strip trailing spaces
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = md.strip() + "\n"
    return md

def main():
    slug, url = sys.argv[1], sys.argv[2]
    html = fetch(url)
    title_m = re.search(r"<title>(.*?)</title>", html, re.S)
    title = title_m.group(1).strip() if title_m else url
    md = extract_article(html)
    body_sha = hashlib.sha256(md.encode("utf-8")).hexdigest()
    doc = (
        "---\n"
        f"source_url: {url}\n"
        "ingested: 2026-09-17\n"
        f"sha256: {body_sha}\n"
        "---\n\n"
        + md
    )
    path = f"{OUT}/kiali-docs-{slug}.md"
    with open(path, "w") as f:
        f.write(doc)
    print(json.dumps({"path": path, "chars": len(md), "sha256": body_sha, "title": title}))

if __name__ == "__main__":
    main()
