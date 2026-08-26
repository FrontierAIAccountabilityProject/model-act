#!/usr/bin/env python3
"""
check_quotations.py — find every published quotation on the shelf, and NEVER say a
quotation is absent.

WHY THIS EXISTS
---------------
On 26 August 2026 this project deleted a correct quotation from a public page because a
search for it returned nothing. The sentence was real, verbatim, in the opinion — it just
had a page number sitting in the middle of it, because the text had been extracted from a
PDF and pagination had been inserted into the sentence it paginates. See E60.

Three false negatives happened that day from three different mechanical causes:
  - a page number and two blank lines inside a sentence  (Walton)
  - a phrase wrapping across a line break                (Philip Morris)
  - curly quotation marks against straight ones          (Philip Morris)

Each looked exactly like proof of a fabrication.

THE DESIGN RULE, AND IT IS THE WHOLE POINT
------------------------------------------
**This tool can conclude presence. It can never conclude absence.**

A match is a finding: the quotation is on the shelf, in that file, verbatim after
normalization. A miss is NOT a finding. It is one of:
  - the source is not held (most of them)
  - the quotation is from a source that will never be held (a tweet, a paywalled article)
  - the extraction is bad (an image-only PDF has no text to match)
  - the quotation is wrong

The tool cannot tell those apart and does not try. A miss is a PROMPT TO READ, and the
report says so on every run, because the day this tool starts being read as a fabrication
detector is the day it recreates E60 at scale.

USAGE
    python3 check_quotations.py              # summary + unmatched-in-a-held-source list
    python3 check_quotations.py --all        # every unmatched quotation
    python3 check_quotations.py --file X.md  # one file
    python3 check_quotations.py --find "..." # search one string against the whole shelf
    python3 check_quotations.py --negatives  # re-test every recorded negative finding
"""

import io, os, re, sys, unicodedata

LIB   = os.path.expanduser("~/mnt/faap/library/_text")
REPO  = "."
MINLEN = 60          # shorter strings match by accident; 60 chars is ~10 words

# The register and the diary quote fabricated and superseded text ON PURPOSE, as specimens.
# They are read, but their misses are reported separately and never counted as debt.
SPECIMEN_FILES = {"./ledger/errata.md", "./ledger/diary.md", "./ledger/changelog.md"}
SKIP_DIRS = {".git", "_site", "_sass", "_includes", "node_modules", "__pycache__",
             "_to_delete", "archive"}

# ---------------------------------------------------------------- normalisation
PAGE_LINE = re.compile(r"(?m)^[ \t]*\d{1,4}[ \t]*$")
HYPHEN_WRAP = re.compile(r"(\w)-[ \t]*\n[ \t]*(\w)")
FURNITURE = re.compile(r"[*_`\[\]]")

def norm(s):
    """Strip everything that a PDF extractor or a markdown author inserts INTO a sentence.

    Order matters. Page-number lines go before whitespace collapse, or they merge into
    the sentence as digits. Hyphen-wrap goes before whitespace collapse for the same
    reason. Nothing here changes a word."""
    s = unicodedata.normalize("NFKC", s)
    s = (s.replace("‘", "'").replace("’", "'")
          .replace("“", '"').replace("”", '"')
          .replace("—", "-").replace("–", "-").replace("−", "-")
          .replace(" ", " ").replace("ﬁ", "fi").replace("ﬂ", "fl"))
    s = PAGE_LINE.sub(" ", s)
    s = HYPHEN_WRAP.sub(r"\1\2", s)
    s = FURNITURE.sub("", s)
    s = re.sub(r"\s+", " ", s)
    return s.lower().strip()

# ---------------------------------------------------------------- the shelf
def load_shelf():
    corpus, unreadable, empty = {}, [], []
    if not os.path.isdir(LIB):
        print("*** SHELF NOT REACHABLE at %s — this run proves nothing ***" % LIB)
        sys.exit(2)
    for fn in sorted(os.listdir(LIB)):
        if not fn.endswith(".txt"):
            continue
        try:
            raw = io.open(os.path.join(LIB, fn), encoding="utf-8", errors="replace").read()
        except OSError as e:
            unreadable.append((fn, str(e))); continue
        if len(raw.strip()) < 200:
            empty.append(fn)           # an image-only PDF: a miss against it means nothing
        corpus[fn] = norm(raw)
    return corpus, unreadable, empty

# ---------------------------------------------------------------- the repository
BLOCK = re.compile(r"(?m)^>[ \t]?(.*)$")
INLINE = re.compile(r'"([^"\n]{%d,600})"' % MINLEN)
SMART  = re.compile(r'“([^”\n]{%d,600})”' % MINLEN)

def md_files():
    out = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in sorted(files):
            if fn.endswith(".md"):
                out.append(os.path.join(root, fn))
    return out

def quotations(path):
    """Contiguous runs of '> ' lines are one quotation. Inline quoted spans are another."""
    text = io.open(path, encoding="utf-8", errors="replace").read()
    found, run, start = [], [], None
    for i, line in enumerate(text.split("\n"), 1):
        m = BLOCK.match(line)
        if m:
            if start is None: start = i
            run.append(m.group(1))
        else:
            if run:
                q = " ".join(run).strip()
                if len(q) >= MINLEN: found.append((start, "block", q))
                run, start = [], None
    if run:
        q = " ".join(run).strip()
        if len(q) >= MINLEN: found.append((start, "block", q))
    for pat in (INLINE, SMART):
        for m in pat.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            found.append((line, "inline", m.group(1).strip()))
    return found


# ---------------------------------------------------------------- negative findings
ERRATA = "./ledger/errata.md"

def negatives(corpus):
    """Re-test every recorded negative finding against the shelf as it now stands.

    This is the loop E60 was missing. A finding that something is absent is never
    revisited, because the text is gone and nothing points at it. Listing them makes
    them enumerable; running them on every sweep makes the register answer for itself
    when a new source lands."""
    try:
        text = io.open(ERRATA, encoding="utf-8", errors="replace").read()
    except OSError as e:
        print("*** cannot read %s (%s) — this run proves nothing ***" % (ERRATA, e)); return 2
    m = re.search(r"(?s)```negative-findings\n(.*?)```", text)
    if not m:
        print("*** NO NEGATIVE-FINDINGS BLOCK in %s ***" % ERRATA)
        print("    Either it was deleted or the register moved. Do not treat this as 'none open'.")
        return 2
    rows = [l for l in m.group(1).split("\n") if l.strip() and not l.lstrip().startswith("#")]
    print("NEGATIVE FINDINGS — re-tested against %d shelf files" % len(corpus))
    print("  recorded: %d\n" % len(rows))
    surprises = 0
    for line in rows:
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 4: 
            print("  MALFORMED ROW: %s" % line[:70]); surprises += 1; continue
        status, quote, whose, err = parts[0], parts[1], parts[2], parts[3]
        hit = next((f for f, c in corpus.items() if norm(quote) in c), None)
        if status.upper().startswith("OPEN") and hit:
            print("  *** WAS RECORDED ABSENT AND IS ON THE SHELF ***")
            print("      %s  (%s)" % (quote[:74], err))
            print("      found in: %s" % hit[:88])
            print("      Read the document. This is how E60 was found.")
            surprises += 1
        elif status.upper().startswith("WITHDRAWN") and not hit:
            print("  *** WITHDRAWN BUT NO LONGER FINDABLE ***")
            print("      %s  (%s)" % (quote[:74], err))
            print("      The source may have left the shelf. The withdrawal still stands.")
            surprises += 1
        else:
            mark = "still absent from the shelf" if not hit else "confirmed present"
            print("  [%-9s] %-58s %s" % (status.upper()[:9], quote[:58], mark))
    print("\n  %s" % ("NOTHING CHANGED." if not surprises
                       else "*** %d ROW(S) NEED A HUMAN READ ***" % surprises))
    print("  A row still absent is NOT confirmation the finding was right. It means the")
    print("  source is not held in extractable form. Only reading the document settles it.")
    return 0

# ---------------------------------------------------------------- matching
def main():
    show_all = "--all" in sys.argv
    corpus, unreadable, empty = load_shelf()

    if "--find" in sys.argv:
        q = sys.argv[sys.argv.index("--find") + 1]
        n = norm(q)
        hits = [f for f, c in corpus.items() if n in c]
        print("SEARCHED %d shelf files for a %d-character string." % (len(corpus), len(n)))
        for h in hits: print("  MATCHED  %s" % h)
        if not hits:
            print("  NO MATCH ON THE SHELF.")
            print("  *** THIS IS NOT A FINDING. *** It means the string is not in a held,")
            print("  text-extractable source. Read the document before concluding anything.")
        return 0

    if "--negatives" in sys.argv:
        return negatives(corpus)

    only = None
    if "--file" in sys.argv:
        only = sys.argv[sys.argv.index("--file") + 1]

    matched = unmatched = specimens = 0
    misses, spec_misses = [], []
    for path in md_files():
        if only and os.path.basename(path) != os.path.basename(only):
            continue
        is_spec = path in SPECIMEN_FILES
        for line, kind, q in quotations(path):
            n = norm(q)
            if len(n) < MINLEN:
                continue
            hit = next((f for f, c in corpus.items() if n in c), None)
            if hit:
                matched += 1
            elif is_spec:
                specimens += 1; spec_misses.append((path, line, kind, q))
            else:
                unmatched += 1; misses.append((path, line, kind, q))

    total = matched + unmatched + specimens
    print("QUOTATION SWEEP")
    print("  shelf files normalised ....... %d" % len(corpus))
    print("  published quotations read .... %d   (>= %d characters)" % (total, MINLEN))
    print("  FOUND ON THE SHELF ........... %d" % matched)
    print("  not found ..................... %d" % unmatched)
    print("  not found, in a specimen file . %d   (the register quotes wrong text on purpose)"
          % specimens)

    if empty:
        print("\n  *** %d SHELF FILES HAVE NO EXTRACTABLE TEXT ***" % len(empty))
        print("      A miss against one of these means nothing at all.")
        for f in empty[:8]: print("      %s" % f[:96])
        if len(empty) > 8: print("      ... and %d more" % (len(empty) - 8))
    if unreadable:
        print("\n  *** CORPUS INCOMPLETE — %d files unreadable ***" % len(unreadable))
        for f, e in unreadable: print("      %s  (%s)" % (f, e))

    print("\n" + "=" * 78)
    print("A MISS IS NOT A FINDING. This tool can conclude that a quotation IS on the")
    print("shelf. It can never conclude that one is absent. Most misses below are simply")
    print("sources this project does not hold. Before treating any of them as an error,")
    print("open the document and read the cited location — that is what E60 cost.")
    print("=" * 78)

    if misses:
        shown = misses if show_all else misses[:30]
        print("\n  NOT FOUND ON THE SHELF — read before concluding:")
        for path, line, kind, q in shown:
            print("    %s:%d [%s] %s" % (path, line, kind, q[:86].replace("\n", " ")))
        if not show_all and len(misses) > 30:
            print("    ... and %d more (--all)" % (len(misses) - 30))
    return 0

sys.exit(main())
