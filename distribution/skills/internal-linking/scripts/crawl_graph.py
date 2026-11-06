#!/usr/bin/env python3
"""Step 0 of the internal-linking skill: deterministic ingestion of a site.

Input   : a sitemap URL (or a base URL, in which case /sitemap.xml is tried).
Output  : index.json (one light line per page) + graph.json (every internal
          link with its anchor, in-body or not) + a summary on stdout.

No external dependency, standard library only. No LLM: the graph is exact.

Usage :
  python3 crawl_graph.py https://exemple.com/sitemap.xml -o ./maillage-data
  python3 crawl_graph.py https://exemple.com --limit 50 --delay 0.3
"""

import argparse
import json
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit, urlunsplit

UA = "Mozilla/5.0 (compatible; maillage-systeme/1.0; audit maillage interne)"
# Zones whose links do not count as in-body editorial links
CHROME_TAGS = {"nav", "header", "footer", "aside"}
TRACKING_PARAMS = re.compile(r"^(utm_|fbclid|gclid|ref$)")


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def sitemap_urls(sitemap_url):
    """Returns every page URL in the sitemap, handling sitemap index files."""
    xml = fetch(sitemap_url)
    root = ET.fromstring(xml.encode())
    ns = {"sm": root.tag.split("}")[0].strip("{")} if "}" in root.tag else {}
    tag = lambda name: f"sm:{name}" if ns else name
    urls = []
    if root.tag.endswith("sitemapindex"):
        for loc in root.iterfind(f".//{tag('sitemap')}/{tag('loc')}", ns):
            urls.extend(sitemap_urls(loc.text.strip()))
    else:
        for loc in root.iterfind(f".//{tag('url')}/{tag('loc')}", ns):
            urls.append(loc.text.strip())
    return urls


def normalize(url, base):
    """URL absolue, sans fragment, sans params de tracking, sans slash final."""
    absolute = urljoin(base, url)
    parts = urlsplit(absolute)
    if parts.scheme not in ("http", "https"):
        return None
    query = "&".join(
        p for p in parts.query.split("&") if p and not TRACKING_PARAMS.match(p)
    )
    path = parts.path.rstrip("/") or "/"
    host = parts.netloc.lower().removeprefix("www.")
    return urlunsplit((parts.scheme, host, path, query, ""))


class PageParser(HTMLParser):
    """Extrait titre, meta description, h1 et liens (avec zone in-body ou non)."""

    def __init__(self, base_url):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.title = ""
        self.description = ""
        self.h1 = ""
        self.links = []  # (href, anchor_text, in_body)
        self._chrome_depth = 0
        self._in_title = False
        self._in_h1 = False
        self._current_link = None  # [href, [text_parts], in_body]

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in CHROME_TAGS:
            self._chrome_depth += 1
        elif tag == "title":
            self._in_title = True
        elif tag == "h1":
            self._in_h1 = True
        elif tag == "meta" and attrs.get("name", "").lower() == "description":
            self.description = (attrs.get("content") or "").strip()
        elif tag == "a" and attrs.get("href"):
            self._current_link = [attrs["href"], [], self._chrome_depth == 0]

    def handle_endtag(self, tag):
        if tag in CHROME_TAGS and self._chrome_depth > 0:
            self._chrome_depth -= 1
        elif tag == "title":
            self._in_title = False
        elif tag == "h1":
            self._in_h1 = False
        elif tag == "a" and self._current_link:
            href, parts, in_body = self._current_link
            anchor = re.sub(r"\s+", " ", "".join(parts)).strip()
            self.links.append((href, anchor, in_body))
            self._current_link = None

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_h1 and not self.h1.strip():
            self.h1 += data
        if self._current_link:
            self._current_link[1].append(data)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("sitemap", help="URL du sitemap.xml ou URL de base du site")
    ap.add_argument("-o", "--out", default=".", help="dossier de sortie")
    ap.add_argument("--limit", type=int, default=0, help="max de pages (0 = tout)")
    ap.add_argument("--delay", type=float, default=0.2, help="pause between requests, in seconds")
    args = ap.parse_args()

    sitemap = args.sitemap
    if not sitemap.endswith(".xml"):
        sitemap = sitemap.rstrip("/") + "/sitemap.xml"

    pages = sitemap_urls(sitemap)
    if args.limit:
        pages = pages[: args.limit]
    site_host = urlsplit(pages[0]).netloc.lower().removeprefix("www.")
    known = {normalize(u, u) for u in pages}

    index, edges, errors = {}, [], []
    for i, url in enumerate(pages, 1):
        page_key = normalize(url, url)
        try:
            html = fetch(url)
        except Exception as e:
            errors.append({"url": url, "error": str(e)})
            print(f"[{i}/{len(pages)}] ERREUR {url} : {e}", file=sys.stderr)
            continue
        parser = PageParser(url)
        try:
            parser.feed(html)
        except Exception as e:
            errors.append({"url": url, "error": f"parse: {e}"})
            continue
        for href, anchor, in_body in parser.links:
            target = normalize(href, url)
            if not target or urlsplit(target).netloc != site_host:
                continue
            if target == page_key:
                continue
            edges.append(
                {
                    "source": page_key,
                    "target": target,
                    "anchor": anchor,
                    "in_body": in_body,
                    "target_in_sitemap": target in known,
                }
            )
        index[page_key] = {
            "url": page_key,
            "title": re.sub(r"\s+", " ", parser.title).strip(),
            "h1": re.sub(r"\s+", " ", parser.h1).strip(),
            "description": parser.description,
            "inbound_in_body": 0,
            "outbound_in_body": 0,
        }
        print(f"[{i}/{len(pages)}] {page_key}", file=sys.stderr)
        if args.delay:
            time.sleep(args.delay)

    # The same (target, anchor) pair present on nearly every page is a
    # template link (a non-semantic menu or footer), not an editorial one
    from collections import defaultdict

    pair_sources = defaultdict(set)
    for e in edges:
        if e["in_body"]:
            pair_sources[(e["target"], e["anchor"])].add(e["source"])
    sitewide_threshold = max(3, int(len(index) * 0.8))
    for e in edges:
        e["sitewide"] = (
            e["in_body"]
            and len(pair_sources[(e["target"], e["anchor"])]) >= sitewide_threshold
        )

    # Compteurs sur les liens in-body non sitewide uniquement (nav/footer et
    # template links do not count as editorial linking in this method)
    for e in edges:
        if not e["in_body"] or e["sitewide"]:
            continue
        if e["source"] in index:
            index[e["source"]]["outbound_in_body"] += 1
        if e["target"] in index:
            index[e["target"]]["inbound_in_body"] += 1

    orphans = [u for u, p in index.items() if p["inbound_in_body"] == 0]
    dead_ends = [u for u, p in index.items() if p["outbound_in_body"] == 0]

    import os

    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, "index.json"), "w") as f:
        json.dump(
            {
                "site": site_host,
                "crawled": len(index),
                "errors": errors,
                "orphans": orphans,
                "dead_ends": dead_ends,
                "pages": list(index.values()),
            },
            f,
            ensure_ascii=False,
            indent=2,
        )
    with open(os.path.join(args.out, "graph.json"), "w") as f:
        json.dump(edges, f, ensure_ascii=False, indent=2)

    in_body_edges = sum(1 for e in edges if e["in_body"] and not e["sitewide"])
    sitewide_edges = sum(1 for e in edges if e["sitewide"])
    print(
        f"\n{len(index)} pages crawled, {len(edges)} internal links "
        f"({in_body_edges} editorial, {sitewide_edges} template), "
        f"{len(orphans)} orphans, "
        f"{len(dead_ends)} dead ends, {len(errors)} errors.\n"
        f"Sorties : {args.out}/index.json et {args.out}/graph.json"
    )


if __name__ == "__main__":
    main()
