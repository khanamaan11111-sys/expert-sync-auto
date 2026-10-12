#!/usr/bin/env python3
"""Stage 51: dependency-free static site preflight; does not test live hosting."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
PREFIX = "/expert-sync-auto/"
errors = []
checked = 0

class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.references = []
        self.title = False
        self.viewport = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.title = True
        if tag == "meta" and attrs.get("name", "").lower() == "viewport":
            self.viewport = True
        for attr in ("href", "src"):
            if tag in ("a", "link", "script", "img", "iframe", "source") and attrs.get(attr):
                self.references.append((tag, attr, attrs[attr]))

def local_path(value):
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    path = unquote(parsed.path)
    if path.startswith(PREFIX):
        path = path[len(PREFIX):]
    elif path.startswith("/"):
        return None  # other root-level links are not this project
    parts = Path(path).parts
    if ".." in parts or "\\" in path:
        return "unsafe"
    return ROOT / path

pages = sorted(ROOT.glob("*.html"))
if not pages:
    errors.append("No HTML pages found")
for page in pages:
    parser = Links()
    try:
        parser.feed(page.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{page.name}: cannot parse HTML: {exc}")
        continue
    checked += 1
    if not parser.title:
        errors.append(f"{page.name}: missing title element")
    if not parser.viewport:
        errors.append(f"{page.name}: missing viewport meta")
    for tag, attr, url in parser.references:
        target = local_path(url)
        if target == "unsafe":
            errors.append(f"{page.name}: unsafe local {attr}: {url}")
        elif target is not None and not target.is_file() and not (target.is_dir() and (target / "index.html").is_file()):
            errors.append(f"{page.name}: missing {tag} {attr}: {url}")

try:
    tree = ET.parse(ROOT / "sitemap.xml")
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [n.text for n in tree.findall(".//s:loc", ns)]
    if not urls:
        errors.append("sitemap.xml: no URL entries")
    if len(urls) != len(set(urls)):
        errors.append("sitemap.xml: duplicate URL entries")
    for url in urls:
        parsed = urlsplit(url or "")
        if parsed.scheme != "https" or parsed.netloc != "khanamaan11111-sys.github.io" or not parsed.path.startswith(PREFIX):
            errors.append(f"sitemap.xml: unexpected site URL: {url}")
            continue
        relative = unquote(parsed.path[len(PREFIX):]) or "index.html"
        target = ROOT / relative
        if ".." in Path(relative).parts or not target.is_file():
            errors.append(f"sitemap.xml: missing page: {url}")
    # Some HTML pages are intentionally omitted from the public search sitemap.
except Exception as exc:
    errors.append(f"sitemap.xml: invalid XML or missing file: {exc}")

try:
    inventory = json.loads((ROOT / "listings.json").read_text(encoding="utf-8"))
    if not isinstance(inventory, dict) or inventory.get("schemaVersion") != 1 or not isinstance(inventory.get("listings"), list):
        errors.append("listings.json: expected schemaVersion 1 and listings array")
    else:
        for i, item in enumerate(inventory["listings"]):
            if not isinstance(item, dict):
                errors.append(f"listings.json: item {i} must be an object")
except Exception as exc:
    errors.append(f"listings.json: invalid JSON or missing file: {exc}")

print(f"Checked {checked} HTML pages, local links, sitemap and inventory JSON.")
if errors:
    print(f"FAIL: {len(errors)} issue(s):")
    for issue in errors:
        print(" - " + issue)
    sys.exit(1)
print("PASS: static repository checks. Public deployment and browser behaviour remain unverified.")
