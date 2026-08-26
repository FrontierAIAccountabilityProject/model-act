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
CASE = re.compile(r"([A-Z][A-Za-z.'’&\-]+(?:\s+[A-Za-z.'’&\-]+){0,7})\s+v\.\s+"
                  r"([A-Z][A-Za-z.'’&\-]+(?:\s+[A-Za-z.'’&\-]+){0,7})")

# The regex above cannot see a sentence boundary, so on 25 August 2026 it reported
# "SPENDING CLAUSE. National Pork Producers Council v. Ross" and "If xAI v. Bonta
# lands against AB" as captions with no table row. A debt list with junk in it is a
# debt list nobody works. Party names are trimmed here instead.
ABBREV = {"v.", "inc.", "corp.", "co.", "llc.", "ltd.", "ass'n", "ass’n", "dep't",
          "dep’t", "bros.", "mfg.", "st.", "no.", "u.s.", "cal.", "rel.", "ex",
          "comm'n", "comm’n", "l.p.", "n.a.", "s.a.", "plc."}
INITIAL = re.compile(r"^[A-Z]\.$")
# Lowercase words that genuinely occur inside a party name. Anything else that is
# lowercase is prose that leaked in.
INPARTY = {"of", "ex", "rel.", "and", "de", "van", "der", "the", "for", "el"}
LEADIN  = {"if", "the", "in", "and", "but", "where", "when", "that", "a", "an", "as",
           "under", "see", "per", "from", "to", "by", "on", "at", "with", "this",
           "its", "held", "so", "then", "here", "both", "while", "because"}

def _ends_sentence(tok):
    low = tok.lower()
    return tok.endswith((".", "!", "?")) and low not in ABBREV and not INITIAL.match(tok)

def trim_first_party(a):
    """Keep only the trailing run of tokens that can belong to a party name."""
    toks = a.split()
    cut = 0
    for i, tok in enumerate(toks[:-1]):          # the last token is always the party
        if _ends_sentence(tok):
            cut = i + 1
        elif tok.islower() and tok.lower() not in INPARTY:
            cut = i + 1
    toks = toks[cut:]
    while len(toks) > 1 and toks[0].lower().rstrip(".,") in LEADIN:
        toks = toks[1:]
    return " ".join(toks)

def trim_second_party(b):
    """Stop at the first token that is prose rather than part of the name."""
    toks = b.split()
    for i, tok in enumerate(toks):
        if i and tok.islower() and tok.lower() not in INPARTY:
            return " ".join(toks[:i])
        if i and _ends_sentence(tok):
            return " ".join(toks[:i + 1])
    return " ".join(toks)
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
        a, b = trim_first_party(a), trim_second_party(b)
        if not a or not b: continue
        if a.split()[0].lower().rstrip(".,") in FRAGMENT and len(a.split()) <= 2: continue
        out.add(f"{a} v. {b}".rstrip(".,;:"))
    keep = set()
    for c in sorted(out, key=len, reverse=True):
        if not any(k.endswith(c) for k in keep): keep.add(c)
    return keep

# A markdown table's separator row is one whose every cell is made only of
# hyphens, colons and space. The old test was `"---" not in line`, which throws
# away any DATA row that happens to contain three hyphens — and on 26 August 2026
# it threw away exactly one: the *Weitzenhoff* row, because the reporter prints
# an unissued U.S. Reports page as "511 U.S. at ----" and the row quotes it
# verbatim. The row was invisible to this sweep: not counted, not listed, its
# three ⚠ flags absent from the standing debt. A quotation made a row stop being
# a row. See E52.
_SEP_CELL = re.compile(r"^[\s:-]+$")

def is_separator_row(line):
    cells = [c for c in line.strip().strip("|").split("|")]
    return bool(cells) and all(_SEP_CELL.match(c) for c in cells)

def main():
    show_all = "--all" in sys.argv
    files = md_files()
    toa_text = open(TOA, encoding="utf-8").read()

    toa_rows, unread, section = [], [], None
    for line in toa_text.split("\n"):
        if line.startswith(("## ", "### ")): section = line.strip("# ").strip()
        elif line.startswith("| ") and not is_separator_row(line) and not line.startswith("| Authority"):
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
            print(f"    [NO ROW] {c[:78]:<78} in {len(where[c])} file(s)")
        if not show_all and len(missing) > 25:
            print(f"    ... and {len(missing)-25} more (--all to list)")
    return 0

sys.exit(main())
