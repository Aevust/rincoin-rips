#!/usr/bin/env python3
"""
compare-captures.py -- compare Wayback captures at the level of extracted
document text, for pages whose raw response bytes are not stable.

Usage:
    ./compare-captures.py cap-*.html

For each input it reports the raw byte count, the SHA-256 of the raw bytes,
and the SHA-256 of the extracted visible text; it then compares every pair.
Extracted text is written alongside each input as <name>.txt so that the
differing pairs can be inspected with diff(1).

Script, style, noscript and template contents are excluded. Whitespace is
collapsed to single spaces, so formatting churn does not register as a
difference; a difference in the output therefore means the visible document
text changed.
"""

import hashlib
import html.parser
import itertools
import pathlib
import re
import sys

SKIP = {"script", "style", "noscript", "template"}


class Extract(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.depth += 1

    def handle_endtag(self, tag):
        if tag in SKIP and self.depth:
            self.depth -= 1

    def handle_data(self, data):
        if not self.depth:
            self.out.append(data)


def text_of(raw):
    p = Extract()
    p.feed(raw.decode("utf-8", "replace"))
    return re.sub(r"\s+", " ", "".join(p.out)).strip()


def main():
    paths = [pathlib.Path(a) for a in sys.argv[1:]]
    if len(paths) < 2:
        print("usage: compare-captures.py cap1.html cap2.html [...]")
        return 2

    text = {}
    for p in paths:
        raw = p.read_bytes()
        t = text_of(raw)
        text[p] = t
        out = p.with_suffix(".txt")
        out.write_text(t, encoding="utf-8", newline="\n")
        print(p.name)
        print(f"  raw bytes    {len(raw)}")
        print(f"  sha256 raw   {hashlib.sha256(raw).hexdigest()}")
        print(f"  text chars   {len(t)}")
        print(f"  sha256 text  {hashlib.sha256(t.encode()).hexdigest()}")
        print(f"  written      {out.name}")

    print()
    differing = 0
    for a, b in itertools.combinations(paths, 2):
        same = text[a] == text[b]
        if not same:
            differing += 1
        print(f"  {'SAME' if same else 'DIFF'}  {a.name}  vs  {b.name}")

    print(f"\n{len(paths)} inputs, "
          f"{len(list(itertools.combinations(paths, 2)))} pairs, "
          f"{differing} differing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
