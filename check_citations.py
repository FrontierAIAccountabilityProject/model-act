#!/usr/bin/env python3
"""
check_citations.py — every authority the prose relies on, and whether anyone read it.

Why this exists. On 25 August 2026 eleven authorities were added to the table in one
afternoon, from footnotes in a research service report and two law reviews, and from
one adversary's brief. Two of the quotations turned out not to appear in the opinions
they were attributed to (E46). The ⚠ markers are what made that recoverable.

So the marker is load-carrying, and a marker nobody applied is worse than no system.
This checker exists to find the authority that is cited in the prose and has no row in
the table at all — which is where an unmarked, unread citation hides.

What it reports:
  CITED, NO ROW    an authority appears in the prose and not in the table of authorities
  ROW, NEVER CITED a row exists for something no page relies on (fine for section VI)
  UNREAD           rows carrying ⚠, with the count that is the standing debt figure

It cannot tell you whether a quotation is accurate. Only reading can, and E22 says so.

Usage:  python3 check_citations.py [--all]
"""
import os, re, sys, collections

SKIP = {".git", "_site", "archive", "_sass", "_includes"}
TOA  = "standards/table_of_authorities.md"
# Sections VI and V list candidates and scholarship; a row there need not be cited.
NOT_REQUIRED_CITED = ("VI. Candidate authorities", "V. Scholarship")

def md_files():
    out = []
    for r, d, fs in os.walk("."):
        d[:] = [x for x in d if x not in SKIP]
        for f in fs:
            if f.endswith(".md"): out.append(os.path.join(r, f))
    return out

# A case name is the durable part of a citation; reporter volumes wrap across lines
# and get italicised, so match the caption and normalise whitespace first.
CASE = re.compile(r"([A-Z][A-Za-z.'’&\-]+(?:\s+[A-Za-z.'’&\-]+){0,5})\s+v\.\s+"
                  r"([A-Z][A-Za-z.'’&\-]+(?:\s+[A-Za-z.'’&\-]+){0,5})")
NOISE = {"see", "compare", "accord", "cf", "but", "e.g", "id", "supra", "infra"}
# The same caption caught at different boundaries produces fragments — "AI LLC v.
# Weiser" beside "X.AI LLC v. Weiser". Drop a caption whose first party is a bare
# fragment, and collapse any caption that is a suffix of a longer one already seen.
FRAGMENT = {"ai", "inc", "llc", "co", "corp", "states", "united", "america",
            "school", "hospital", "group", "the", "and", "of"}

def captions(text):
    flat = " ".join(re.sub(r"[*_`]", "", text).split())
    out = set()
    for m in CASE.finditer(flat):
        a, b = m.group(1).strip(), m.group(2).strip()
        if a.split()[0].lower().rstrip(".,") in NOISE: a = " ".join(a.split()[1:])
        if not a or not b: continue
        if a.split()[0].lower().rstrip(".,") in FRAGMENT and len(a.split()) <= 2: continue
        out.add(f"{a} v. {b}".rstrip(".,;:"))
    keep = set()
    for c in sorted(out, key=len, reverse=True):
        if not any(k.endswith(c) for k in keep): keep.add(c)
    return keep

def main():
    show_all = "--all" in sys.argv
    files = md_files()
    toa_text = open(TOA, encoding="utf-8").read()

    toa_rows, unread, section = [], [], None
    for line in toa_text.split("\n"):
        if line.startswith(("## ", "### ")): section = line.strip("# ").strip()
        elif line.startswith("| ") and "---" not in line and not line.startswith("| Authority"):
            toa_rows.append((section, line))
            if "⚠" in line: unread.append((section, line))
    toa_caps = captions(toa_text)

    prose_caps = collections.Counter()
    where = collections.defaultdict(set)
    for f in files:
        if os.path.normpath(f) in {os.path.normpath(TOA), "./ledger/errata.md"}: continue
        t = open(f, encoding="utf-8", errors="replace").read()
        for c in captions(t):
            prose_caps[c] += 1; where[c].add(f)

    def known(c):
        parts = c.split(" v. ")
        return any(p[-16:] in toa_text or p[:16] in toa_text for p in parts if len(p) > 4)

    missing = sorted((c for c in prose_caps if not known(c)), key=lambda c: -len(where[c]))

    print("CITATION SWEEP")
    print(f"  markdown files ............... {len(files)}")
    print(f"  rows in the table ............ {len(toa_rows)}")
    print(f"  rows flagged unread (⚠) ...... {len(unread)}   <-- the standing debt")
    print(f"  case captions seen in prose .. {len(prose_caps)}")
    print(f"  captions with no table row ... {len(missing)}")
    if unread:
        print("\n  THE DEBT, row by row:")
        for sec, line in unread:
            auth = line.split("|")[1].strip()[:78]
            print(f"    [UNREAD] {auth}")
    if missing:
        print("\n  CITED WITH NO ROW IN THE TABLE:")
        for c in (missing if show_all else missing[:25]):
            print(f"    [NO ROW] {c[:60]:<60} in {len(where[c])} file(s)")
        if not show_all and len(missing) > 25:
            print(f"    ... and {len(missing)-25} more (--all to list)")
    return 0

sys.exit(main())
