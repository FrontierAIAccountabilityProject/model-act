#!/usr/bin/env python3
"""
build_section_index.py — compute the join that is already written.

WHY THIS EXISTS
---------------
This repository is filed by document type: cures in one place, authorities in another,
errata in a third, objections in a fourth. Every one of them is about some SEC. of the Act,
and nothing has ever joined them.

The join does not need to be authored. It is already in the prose: roughly three thousand
references of the form "SEC. 6" or "SEC. 6(b)(1)", across two thirds of the markdown files,
down to sub-clause granularity. This script reads them.

WHAT IT EMITS
    standards/section_index.md   human-readable, grouped by section
    standards/section_index.json sidecar with every reference, for the page generator

WHAT IT IS FOR
    1. "What has to change in SEC. 6 before v3.5" becomes a lookup instead of an act of memory.
    2. The citing/cited rails on a generated section page come from here.
    3. Before consolidating files, you can see what each one is actually referenced by.

USAGE
    python3 build_section_index.py            # write both outputs
    python3 build_section_index.py --dry      # report only, write nothing
    python3 build_section_index.py --files    # per-FILE view, for planning consolidation
    python3 build_section_index.py --sec 6    # everything about one section
"""

import io, json, os, re, sys
from collections import defaultdict, Counter

REPO   = "."
STATUTE = "model_act_v3_4.txt"
OUT_MD  = "standards/section_index.md"
OUT_JS  = "standards/section_index.json"

SKIP_DIRS = {".git", "_site", "_sass", "_includes", "node_modules",
             "__pycache__", "_to_delete", "_patches"}

# A reference is SEC. n, optionally with (a), (a)(1), (a)(1)(A).
# The trailing groups are optional and captured separately so a page can offer both
# "everything about SEC. 6" and "everything about SEC. 6(b)(1)".
SECREF = re.compile(r"\bSEC\.\s*(\d+)((?:\([a-zA-Z0-9]{1,3}\)){0,3})")

# Classification is by path, because that is what the repository actually encodes.
# It is deliberately coarse: the point is to group, not to be clever.
def kind_of(path):
    p = path.replace("\\", "/").lstrip("./")
    if p == STATUTE or p.startswith("model_act"):        return "statute"
    if p.startswith("archive/"):                          return "archive"
    if p.startswith("packets/"):                          return "packet (generated)"
    if "cure_language" in p:                              return "cure"
    if "lane_sweep" in p or "pre_review_pass" in p:       return "finding"
    if p.startswith("audit/"):                            return "drafting record"
    if "table_of_authorities" in p:                       return "authority"
    if "errata" in p:                                     return "erratum"
    if "known_objections" in p:                           return "objection"
    if p.startswith("ledger/"):                           return "ledger"
    if p.startswith("standards/"):                        return "standard"
    if p.startswith("research/"):                         return "research"
    if p.startswith("docs/"):                             return "explainer"
    if p.startswith("dossier/") or p.startswith("filings/"): return "sealed"
    return "root"

# Order matters in the output: what a drafter needs first comes first.
KIND_ORDER = ["statute", "cure", "finding", "authority", "objection", "erratum",
              "standard", "explainer", "drafting record", "ledger", "research",
              "packet (generated)", "sealed", "root", "archive"]


def md_files():
    out = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in sorted(files):
            if fn.endswith(".md") or fn == STATUTE:
                out.append(os.path.join(root, fn).replace("\\", "/"))
    return sorted(out)


def scan():
    """Every reference, with file and line. No deduplication here — the caller decides."""
    refs, unreadable = [], []
    for path in md_files():
        try:
            text = io.open(path, encoding="utf-8", errors="replace").read()
        except OSError as e:
            unreadable.append((path, str(e)))
            continue
        for i, line in enumerate(text.split("\n"), 1):
            for m in SECREF.finditer(line):
                sec = int(m.group(1))
                sub = m.group(2) or ""
                refs.append({
                    "sec": sec, "sub": sub, "cite": "SEC. %d%s" % (sec, sub),
                    "file": path.lstrip("./"), "line": i,
                    "kind": kind_of(path),
                    "text": line.strip()[:200],
                })
    return refs, unreadable


def statute_sections():
    """The sections that actually exist, read from the statute itself.

    A section referenced everywhere but absent from the statute is a defect; a section in
    the statute referenced nowhere is a blind spot. Both are worth seeing, and neither is
    visible without this list."""
    try:
        text = io.open(STATUTE, encoding="utf-8", errors="replace").read()
    except OSError:
        return {}, False
    out = {}
    for m in re.finditer(r"(?m)^SEC\.\s*(\d+)\.\s*([^\n]*)", text):
        n = int(m.group(1))
        if n not in out:                       # first occurrence is the heading
            # The statute puts the section title and subsection (a) on the SAME LINE --
            # "SEC. 6. INDIVIDUAL LIABILITY. (a) Offense. A controlling person who..." --
            # so take only the leading capitalised title and stop at its period.
            raw = m.group(2).strip()
            mt = re.match(r"([A-Z0-9 ,'&()/\-]+?)\.(?:\s|$)", raw)
            out[n] = (mt.group(1) if mt else raw[:60]).strip().rstrip(".")
    return out, True


def main():
    dry   = "--dry" in sys.argv
    refs, unreadable = scan()
    heads, have_statute = statute_sections()

    if unreadable:
        print("*** CORPUS INCOMPLETE — %d file(s) unreadable ***" % len(unreadable))
        for p, e in unreadable:
            print("    %s  (%s)" % (p, e))
        print("    The index below is missing whatever they contain.")
    if not have_statute:
        print("*** %s NOT READ — section headings and blind spots unavailable ***" % STATUTE)

    by_sec = defaultdict(list)
    for r in refs:
        by_sec[r["sec"]].append(r)

    # ---- per-FILE view, for planning consolidation
    if "--files" in sys.argv:
        per_file = defaultdict(Counter)
        for r in refs:
            per_file[r["file"]]["SEC. %d" % r["sec"]] += 1
        print("PER-FILE SECTION FOOTPRINT — what each file is actually about\n")
        for f in sorted(per_file, key=lambda k: -sum(per_file[k].values())):
            tot = sum(per_file[f].values())
            top = ", ".join("%s×%d" % (s, n) for s, n in per_file[f].most_common(6))
            print("  %-52s %4d refs  %s" % (f[:52], tot, top))
        return 0

    # ---- single section
    if "--sec" in sys.argv:
        n = int(sys.argv[sys.argv.index("--sec") + 1])
        rows = by_sec.get(n, [])
        print("SEC. %d — %s" % (n, heads.get(n, "(not found in the statute)")))
        print("  %d references across %d files\n" % (rows, len({r["file"] for r in rows}))
              if isinstance(rows, int) else
              "  %d references across %d files\n" % (len(rows), len({r["file"] for r in rows})))
        byk = defaultdict(list)
        for r in rows:
            byk[r["kind"]].append(r)
        for k in KIND_ORDER:
            if k not in byk:
                continue
            print("  [%s]" % k)
            for r in sorted(byk[k], key=lambda x: (x["file"], x["line"])):
                print("    %s:%d  %s" % (r["file"], r["line"], r["text"][:96]))
            print()
        return 0

    # ---- the index
    lines = []
    A = lines.append
    A("# Section index — every file in this repository, joined to the section it is about")
    A("")
    A("*Generated by `build_section_index.py`. **Do not edit.** This file is a computation, not a")
    A("document: it reads the `SEC. n` references already written in the prose and groups them. If a")
    A("row here is wrong, the prose is wrong.*")
    A("")
    A("**Why it exists.** The repository is filed by document type — cures in one place, authorities")
    A("in another, errata in a third. Every one of them is about some section of the Act, and until")
    A("this file nothing joined them. \"What has to change in SEC. 6 before v3.5\" was an act of memory.")
    A("")
    A("| | |")
    A("|---|---|")
    A("| References read | **%d** |" % len(refs))
    A("| Files carrying at least one | **%d** |" % len({r["file"] for r in refs}))
    A("| Sections in the statute | **%d** |" % len(heads))
    A("")

    # blind spots first — a section nobody discusses is the finding
    blind = [n for n in sorted(heads) if not by_sec.get(n)]
    thin  = [n for n in sorted(heads) if 0 < len(by_sec.get(n, [])) <= 15]
    if blind:
        A("⚠ **Sections with no reference anywhere outside the statute:** " +
          ", ".join("SEC. %d" % n for n in blind) + ". **Nothing in this repository discusses them.**")
        A("")
    if thin:
        A("⚠ **Thinly covered** (15 references or fewer): " +
          ", ".join("SEC. %d (%d)" % (n, len(by_sec[n])) for n in thin) + ".")
        A("")
    A("---")
    A("")

    for n in sorted(set(list(heads) + list(by_sec))):
        rows = by_sec.get(n, [])
        A("## SEC. %d — %s" % (n, heads.get(n, "⚠ *referenced but not a section of the statute*")))
        A("")
        A("**%d references across %d files.** Anchor: `#sec-%d`" %
          (len(rows), len({r["file"] for r in rows}), n))
        A("")
        subs = Counter(r["cite"] for r in rows if r["sub"])
        if subs:
            A("**Sub-clauses referenced:** " +
              " · ".join("`%s` ×%d" % (c, k) for c, k in subs.most_common(10)))
            A("")
        byk = defaultdict(Counter)
        for r in rows:
            byk[r["kind"]][r["file"]] += 1
        A("| Kind | Where | Refs |")
        A("|---|---|---|")
        for k in KIND_ORDER:
            if k not in byk:
                continue
            for f, c in byk[k].most_common():
                A("| %s | [`%s`](../%s) | %d |" % (k, f, f, c))
        A("")

    out = "\n".join(lines) + "\n"
    payload = {"references": refs, "headings": {str(k): v for k, v in heads.items()}}

    if dry:
        print("DRY RUN — nothing written.")
    else:
        os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)
        io.open(OUT_MD, "w", encoding="utf-8").write(out)
        io.open(OUT_JS, "w", encoding="utf-8").write(json.dumps(payload, indent=1))

    print("SECTION INDEX")
    print("  references read .............. %d" % len(refs))
    print("  files carrying at least one .. %d" % len({r["file"] for r in refs}))
    print("  sections in the statute ...... %d" % len(heads))
    print("  sections with no reference ... %d %s" %
          (len(blind), ("— " + ", ".join("SEC. %d" % n for n in blind)) if blind else ""))
    if not dry:
        print("  wrote %s (%d lines) and %s" % (OUT_MD, len(lines), OUT_JS))
    return 0


sys.exit(main())
