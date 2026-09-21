#!/usr/bin/env python3
"""
normalize-rip-ascii.py -- convert typographic characters in RIP markdown
to pure ASCII.

Usage:
    ./normalize-rip-ascii.py --check  rip-0004/rip-0004.md [...]
    ./normalize-rip-ascii.py --write  rip-0004/rip-0004.md [...]

--check reports what would change and exits 1 if any file is not ASCII.
--write rewrites the files in place with LF line endings.

Rules are applied in the order listed. Ordered rules matter: the
section-range rule must run before the generic section-sign rule.
Exits non-zero if any non-ASCII byte survives, so an unlisted
character can never pass through silently.
"""

import argparse
import pathlib
import sys
import unicodedata

# (pattern, replacement, note) -- applied in order, literal replacement.
RULES = [
    # Section ranges must be handled before the bare section sign.
    ("\u00a7\u0034.2\u2013\u00a74.4", "Sections 4.2 through 4.4",
     "section range with en dash"),
    ("\u00a7\"", "Section \"",
     "section sign before a quoted heading name"),
    ("\u00a7", "Section ",
     "section sign before a number"),
    (" \u2014 ", " - ",
     "spaced em dash used as a parenthetical break"),
    ("\u2014", "-",
     "any remaining em dash"),
    ("\u2013", "-",
     "en dash in numeric ranges"),
    ("\u2192", "->",
     "rightwards arrow"),
    ("\u00d7", "x",
     "multiplication sign"),
    ("\u2212", "-",
     "minus sign"),
    ("\u2248", "approximately",
     "almost-equal sign"),
    ("\u2260", "!=",
     "not-equal sign"),
]


def normalize(text):
    """Apply RULES in order. Returns (new_text, [(note, count), ...])."""
    applied = []
    for pattern, replacement, note in RULES:
        count = text.count(pattern)
        if count:
            text = text.replace(pattern, replacement)
            applied.append((note, count))
    return text, applied


def survivors(text):
    """Non-ASCII characters remaining, as (codepoint, char, name, count)."""
    out = {}
    for ch in text:
        if ord(ch) > 127:
            out[ch] = out.get(ch, 0) + 1
    return [
        (f"U+{ord(c):04X}", c, unicodedata.name(c, "<unnamed>"), n)
        for c, n in sorted(out.items())
    ]


def main():
    ap = argparse.ArgumentParser()
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    ap.add_argument("paths", nargs="+", type=pathlib.Path)
    args = ap.parse_args()

    failed = False
    for path in args.paths:
        raw = path.read_bytes()
        if b"\r" in raw:
            print(f"{path}: CR bytes present; normalize line endings first")
            failed = True
            continue

        text = raw.decode("utf-8")
        new_text, applied = normalize(text)
        left = survivors(new_text)

        print(f"{path}")
        if not applied and not left:
            print("  already pure ASCII; no change")
            continue
        for note, count in applied:
            print(f"  {count:>4}  {note}")
        if left:
            print("  UNHANDLED non-ASCII remains:")
            for cp, ch, name, n in left:
                print(f"    {cp} {ch!r} x{n}  {name}")
            print("  add a rule for each before writing")
            failed = True
            continue

        before = sum(1 for b in raw if b > 127)
        after = sum(1 for b in new_text.encode("utf-8") if b > 127)
        print(f"  non-ASCII bytes {before} -> {after}")

        if args.write:
            path.write_text(new_text, encoding="ascii", newline="\n")
            check = path.read_bytes()
            assert not any(b > 127 for b in check), "post-write check failed"
            assert b"\r" not in check, "post-write CR check failed"
            print("  written and re-verified")
        else:
            failed = failed or before != after

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
