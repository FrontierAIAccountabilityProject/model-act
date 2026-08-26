#!/usr/bin/env python3
"""Hardcoded-claim audit. Every number a page states about the repository is recomputed
from the repository and compared. Run before any push. Exit 1 on mismatch.

A to-do list rots; this does not. When a count changes, this tells you which pages lie."""
import re, glob, os, sys

def read(p):
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""

WORDS = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",
         10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",20:"twenty",
         21:"twenty-one",22:"twenty-two",23:"twenty-three",24:"twenty-four",25:"twenty-five",
         26:"twenty-six",27:"twenty-seven",28:"twenty-eight",29:"twenty-nine",
         34:"thirty-four",35:"thirty-five",36:"thirty-six",
         37:"thirty-seven",38:"thirty-eight",39:"thirty-nine",40:"forty",
         41:"forty-one",42:"forty-two",43:"forty-three",44:"forty-four",
         45:"forty-five",46:"forty-six",47:"forty-seven",48:"forty-eight",
         49:"forty-nine",50:"fifty",51:"fifty-one",52:"fifty-two",
         53:"fifty-three",54:"fifty-four",55:"fifty-five",56:"fifty-six",
         57:"fifty-seven",58:"fifty-eight",59:"fifty-nine",60:"sixty",
         30:"thirty",31:"thirty-one",32:"thirty-two",33:"thirty-three"}

# The table above was written by hand and stopped at sixty. On 26 August 2026 the errata
# register reached sixty-one and the checker began reporting a page that said "sixty-one"
# as stale against a truth of 61 -- a defect in the map, read as a defect in the page.
# Generated from here on so it cannot run out again; the literals above are left as written.
_TENS = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
_UNITS = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
for _n in range(15, 200):
    if _n in WORDS:
        continue
    if _n < 20:
        WORDS[_n] = {15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}[_n]
    elif _n < 100:
        _t, _u = divmod(_n, 10)
        WORDS[_n] = _TENS[_t] + ("-" + _UNITS[_u] if _u else "")
    else:
        _h, _r = divmod(_n, 100)
        WORDS[_n] = _UNITS[_h] + " hundred" + (" " + WORDS[_r] if _r else "")

# ---- recompute the truth -------------------------------------------------
errata      = read("corrections/corrections.md")
entries     = len(re.findall(r'(?m)^## E\d+', errata))
highest_e   = max([int(n) for n in re.findall(r'(?m)^## E(\d+)', errata)] or [0])
packets     = [p for p in glob.glob("packets/*.md") if os.path.basename(p) not in ("index.md","README.md")]
# _to_delete is a holding area, not repository content -- the device shell cannot
# delete, so retired files are parked there. Counting them inflated the published
# document count by 21 the moment the consolidation ran. 26 Aug 2026.
_HOLD = ("/.git", "/_site", "/_to_delete", "/_patches", "/_internal")
docs_count  = len([f for r, d, fs in os.walk(".") for f in fs
                   if f.endswith(".md") and f != "CLAUDE.local.md"
                   and not any(h in (r + "/") for h in _HOLD)])
statute     = read("act/model-act.txt")
sections    = len(re.findall(r'(?m)^SEC\.', statute))
q35         = read("revision/proposals.md")
q34         = read("revision/proposals-adopted-v3-4.md")
cures35     = len(re.findall(r'(?m)^#{2,3} Amendment ', q35))
oq35        = len(re.findall(r'(?m)^## Decision ', q35))
cures34     = len(re.findall(r'(?m)^#{2,3} Amendment ', q34))
lanes       = len(packets)
statute     = read("act/model-act.txt")
stat_lines  = len(statute.splitlines())
reviewers   = read("revision/worklist.md")
# state-of-play rows: table lines starting with a link or bold item in that section
sop = reviewers.split("The state of play")[1] if "The state of play" in reviewers else ""
# A markdown table's separator row is one whose every cell is made only of
# hyphens, colons and space. The old test was `"---" not in line`, which throws
# away any DATA row that happens to contain three hyphens — and on 26 August 2026
# it threw away exactly one: the *Weitzenhoff* row, because the reporter prints
# an unissued U.S. Reports page as "511 U.S. at ----" and the row quotes it
# verbatim. The row was invisible to this checker: not counted, not listed, its
# three ⚠ flags absent from the standing debt. A quotation made a row stop being
# a row. See E52.
_SEP_CELL = re.compile(r"^[\s:-]+$")

def is_separator_row(line):
    cells = [c for c in line.strip().strip("|").split("|")]
    return bool(cells) and all(_SEP_CELL.match(c) for c in cells)

sop_rows    = len([l for l in sop.splitlines()
                   if l.startswith("| ") and not is_separator_row(l)]) - 1

CHECKS = [
 ("errata entry count", "revision/worklist.md", r'([\w-]+) entries under', entries,
  WORDS.get(entries,entries)),
 ("highest errata number", "revision/worklist.md", r'reach E(\d+)', highest_e, f"E{highest_e}"),
 ("lane count (REVIEWERS)", "revision/worklist.md", r'(\w+) lanes have', lanes, WORDS.get(lanes,lanes)),
 ("lane count (packets index)", "revision/worklist.md", r'(\w+) lanes', lanes, WORDS.get(lanes,lanes)),
 ("statute line count", "revision/worklist.md", r'(\d+) lines', stat_lines, str(stat_lines)),
 ("statute line count", "README.md", r'(\d+) lines', stat_lines, str(stat_lines)),
 ("state-of-play rows", "revision/worklist.md", r'\*([\w-]+) rows:', sop_rows, WORDS.get(sop_rows,sop_rows)),
 # The abstract states the project's scale. It is the page a stranger reads first, so its
 # numbers are recomputed here rather than trusted. Floors, not equalities, where the number
 # only grows: a floor stays true between sweeps, an equality goes stale the next commit.
 ("document count (abstract)", "enactment/summary.md", r'\*\*(\d+) documents,', docs_count, docs_count),
 ("statute sections (abstract)", "enactment/summary.md", r'\*\*611 lines, (\d+) sections\*\*', sections, sections),
 ("errata count (abstract)", "enactment/summary.md", r'errata register: (\d+) entries', entries, entries),
 ("v3.4 cures (abstract)", "enactment/summary.md", r'\*\*(\d+) cures\*\* adopted verbatim at v3\.4', cures34, cures34),
 ("v3.5 cures (abstract)", "enactment/summary.md", r'\*\*(\d+) more plus', cures35, cures35),
 ("v3.5 open questions (abstract)", "enactment/summary.md", r'plus (\d+) open questions\*\*', oq35, oq35),
]

print("RECOMPUTED FROM THE REPOSITORY")
print(f"  errata entries .......... {entries}   (highest number E{highest_e})")
print(f"  lane packets ............ {lanes}")
print(f"  statute lines ........... {stat_lines}")
print(f"  state-of-play rows ...... {sop_rows}")
print()

bad = 0
for label, path, pattern, truth, want in CHECKS:
    text = read(path)
    if not text:
        print(f"  [SKIP] {label}: {path} not found"); continue
    m = re.search(pattern, text)
    if not m:
        print(f"  [none] {label} in {path}: no claim found (pattern {pattern!r})"); continue
    said = m.group(1)
    ok = str(said).lower() == str(want).lower() or str(said) == str(truth)
    print(("  [ok]   " if ok else "  [STALE]") + f" {label} in {path}: page says {said!r}, truth is {want!r}")
    if not ok: bad += 1

print()
print("ALL CLAIMS CURRENT" if not bad else f"*** {bad} STALE CLAIM(S) — fix before pushing ***")
sys.exit(1 if bad else 0)
