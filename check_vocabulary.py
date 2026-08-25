#!/usr/bin/env python3
"""
check_vocabulary.py — what a specialist would search for, and whether it is here.

The premise. A reviewer, a defense team, an attorney general's office and a
legislative counsel each arrive with a vocabulary. They type it into the search
bar in the first minute. A term that returns nothing does not read as "not
covered"; it reads as "these people have not heard of it."

The list below is not invented. It comes from three places: an n-gram sweep of
the 37 lawyer-written documents in the library against all markdown here; the
defense-side triage lists of 25 August 2026; and the case names the sources
themselves cite. SLOT records where each term belongs, so the audit produces
work rather than a score.

Search strings are written to be unambiguous, because a bare surname is not.
"Lambert" matched three arXiv papers before anyone noticed it was Mike Lambert
in an author list rather than Lambert v. California, and a bare section number
matches anything. Where a term is a case, the string carries enough of the
caption or the citation to be sure.

Counting is presence-of-substance, not keyword density. One sentence in the
glossary plus a link is a pass. Twelve passing mentions in a sealed record is
not, which is why audit/record.md and dossier/README.md are excluded here for
the same reason the site excludes them from search.

Usage:
    python3 check_vocabulary.py                 # report
    python3 check_vocabulary.py --table         # markdown table for the library
    LIBRARY=../library python3 check_vocabulary.py   # also report library coverage
"""
import os, re, sys

TABLE = "--table" in sys.argv
LIB = os.environ.get("LIBRARY", "../library")
SKIP = {".git", "_site", "archive", "_sass", "_includes", "_mail",
        "_to_delete", "_superseded"}

# The project's own working notes are not sources. On 25 August a plan note that
# merely LISTED the missing terms registered as library coverage for every one of
# them, which would have sent the next round diving for material that is not there.
NOT_A_SOURCE = ("NOTES_", "DRAFT_", "CORRESPONDENCE_", "_LIBRARY_INDEX")
UNSEARCHABLE = {"./audit/record.md", "./dossier/README.md"}

G = "glossary"
# term, cluster, slot
TERMS = [
 # --- responsible corporate officer: the core line -----------------------
 ("Dotterweich",                    "rco core",      "authorities"),
 ("Park doctrine",                           "rco core",      "authorities"),
 ("DeCoster",                       "rco core",      "authorities"),
 ("Iverson",                        "rco core",      "authorities"),
 ("Hanousek",                       "rco core",      G),
 ("Brittain",                       "rco core",      "authorities"),
 ("Ming Hong",                      "rco core",      "authorities"),
 ("1319(c)(6)",                     "rco core",      "authorities"),
 ("MacDonald & Watson",             "rco core",      "CURE 22"),
 ("Johnson & Towers",               "rco core",      "CURE 22"),
 ("responsible relationship",       "rco core",      G),
 ("responsible share",              "rco core",      G),
 ("corporate form does not shield", "rco core",      G),
 ("veil piercing",                  "rco core",      G),
 ("piercing the corporate veil",    "rco core",      G),
 # --- omission and culpability -------------------------------------------
 ("actus reus",                     "omission",      G),
 ("omission",                       "omission",      G),
 ("legal duty to act",              "omission",      G),
 ("Model Penal Code",               "omission",      G),
 ("MPC \u00a7 2.02",                           "omission",      "authorities"),
 ("MPC \u00a7 2.05",                           "omission",      "authorities"),
 ("Lambert v. California",                        "omission",      "known objections"),
 ("Morissette",                     "omission",      "authorities"),
 ("Staples v. United States",                        "omission",      "known objections"),
 ("United States v. Balint",                         "omission",      "authorities"),
 ("101 F.3d 386",                          "omission",      "known objections"),
 ("rule of lenity",                 "omission",      G),
 ("ex post facto",                  "omission",      G),
 ("void for vagueness",             "omission",      "known objections"),
 ("fair notice",                    "omission",      "known objections"),
 # --- imputation: is it vicarious? ---------------------------------------
 ("vicarious",                      "imputation",    "known objections"),
 ("respondeat superior",            "imputation",    G),
 ("collective knowledge",           "imputation",    G),
 ("Bank of New England",            "imputation",    "authorities"),
 ("New York Central",               "imputation",    "authorities"),
 ("willful blindness",              "imputation",    G),
 ("conscious avoidance",            "imputation",    G),
 ("United States v. Jewell",                         "imputation",    "authorities"),
 ("Global-Tech",                    "imputation",    "authorities"),
 ("Cincotta",                       "imputation",    "authorities"),
 # --- the council: delegation and adjudication ---------------------------
 ("private nondelegation",          "council",       "known objections"),
 ("nondelegation",                  "council",       "known objections"),
 ("Carter Coal",                    "council",       "authorities"),
 ("Association of American Railroads","council",     "authorities"),
 ("Appointments Clause",            "council",       "known objections"),
 ("Lucia v. SEC",                          "council",       "authorities"),
 ("Jarkesy",                        "council",       "known objections"),
 ("Article III",                    "council",       "known objections"),
 ("Seventh Amendment",              "council",       "known objections"),
 ("public rights",                  "council",       G),
 ("state action doctrine",          "council",       G),
 ("major questions",                "council",       "known objections"),
 ("Mathews v. Eldridge",            "council",       "authorities"),
 ("post-deprivation",               "council",       G),
 # --- preemption and extraterritoriality ---------------------------------
 ("dormant Commerce",               "preemption",    "known objections"),
 ("extraterritorial",               "preemption",    "known objections"),
 ("Pike balancing",                           "preemption",    "authorities"),
 ("Healy v. Beer Institute",        "preemption",    "authorities"),
 ("Brown-Forman",                   "preemption",    "authorities"),
 ("Edgar v. MITE",                  "preemption",    "authorities"),
 ("National Pork Producers",        "preemption",    "authorities"),
 ("conflict preemption",            "preemption",    G),
 ("obstacle preemption",            "preemption",    G),
 ("field preemption",               "preemption",    G),
 ("Arizona v. United States",       "preemption",    "authorities"),
 ("Murphy v. NCAA",                 "preemption",    "authorities"),
 ("anti-commandeering",             "preemption",    G),
 ("Morrison v. National Australia", "preemption",    "authorities"),
 ("RJR Nabisco",                    "preemption",    "authorities"),
 # --- speech --------------------------------------------------------------
 ("Moody v. NetChoice",             "speech",        "authorities"),
 ("NetChoice",                      "speech",        "authorities"),
 ("Reno v. ACLU",                   "speech",        "authorities"),
 ("Entertainment Merchants",        "speech",        "authorities"),
 ("Zauderer",                       "speech",        "known objections"),
 ("compelled speech",               "speech",        "known objections"),
 ("prior restraint",                "speech",        "known objections"),
 ("editorial discretion",           "speech",        G),
 ("content-based",                  "speech",        G),
 ("strict scrutiny",                "speech",        G),
 ("model weights as speech",        "speech",        "known objections"),
 ("Section 230",                    "speech",        G),
 # --- corporate protection ------------------------------------------------
 ("102(b)(7)",                      "corporate",     "authorities"),
 ("DGCL",                           "corporate",     G),
 ("DGCL \u00a7 145",                            "corporate",     "authorities"),
 ("advancement of fees",            "corporate",     G),
 ("D&O",                            "corporate",     G),
 ("indemnification",                "corporate",     G),
 ("demand futility",                "corporate",     G),
 ("business judgment",              "corporate",     "known objections"),
 ("bad faith",                      "corporate",     G),
 ("conscious disregard",            "corporate",     G),
 ("Caremark",                       "corporate",     "known objections"),
 ("Stone v. Ritter",                "corporate",     "authorities"),
 ("Marchand",                       "corporate",     "authorities"),
 ("Clovis Oncology",                         "corporate",     "authorities"),
 ("In re Boeing",                   "corporate",     "authorities"),
 ("In re McDonald",                       "corporate",     "authorities"),
 ("duty of oversight",              "corporate",     "known objections"),
 ("oversight liability",            "corporate",     "known objections"),
 ("mission-critical",               "corporate",     G),
 ("red flags",                      "corporate",     G),
 ("exculpation",                    "corporate",     G),
 ("joint and several",              "corporate",     G),
 # --- public benefit and nonprofit ---------------------------------------
 ("public benefit corporation",     "pbc",           G),
 ("DGCL \u00a7 365",                            "pbc",           "authorities"),
 ("charitable trust",               "pbc",           G),
 ("mission lock",                   "pbc",           G),
 ("ultra vires",                    "pbc",           G),
 ("charitable assets",              "pbc",           G),
 ("Musk v. Altman",                 "pbc",           "timeline"),
 ("OpenAI Group PBC",               "pbc",           "state record"),
 ("OpenAI Holdings",                "pbc",           "state record"),
 ("OAI Corporation",                "pbc",           "state record"),
 ("wikiHow",                        "pbc",           "state record"),
 # --- the site itself -----------------------------------------------------
 ("anti-SLAPP",                     "the site",      "known objections"),
 ("actual malice",                  "the site",      "known objections"),
 ("New York Times v. Sullivan",     "the site",      "authorities"),
 ("Gertz",                          "the site",      "authorities"),
 ("trade libel",                    "the site",      G),
 ("tortious interference",          "the site",      G),
 ("litigation hold",                "the site",      G),
 ("spoliation",                     "the site",      G),
 ("Zubulake",                       "the site",      "authorities"),
 ("Arthur Andersen",                "the site",      "authorities"),
 ("work-product",                   "the site",      G),
 ("Upjohn",                         "the site",      "authorities"),
 # --- prosecutorial policy -------------------------------------------------
 ("Yates Memo",                     "doj policy",    "known objections"),
 ("Justice Manual",                 "doj policy",    "known objections"),
 ("4-8.000",                        "doj policy",    "authorities"),
 ("Filip",                          "doj policy",    G),
 ("deferred prosecution",           "doj policy",    G),
 ("non-prosecution agreement",      "doj policy",    G),
 ("grand jury",                     "doj policy",    G),
 ("sentencing guidelines",          "doj policy",    G),
 ("Winterkorn",                     "doj policy",    "known objections"),
 # --- attorney general enforcement ----------------------------------------
 ("parens patriae",                 "ag",            G),
 ("UDAP",                           "ag",            G),
 ("consent decree",                 "ag",            G),
 ("civil investigative demand",     "ag",            G),
 ("deceptive trade",                "ag",            "state record"),
 # --- technical and definitional ------------------------------------------
 ("CBRN",                           "technical",     G),
 ("capability elicitation",         "technical",     G),
 ("jailbreak",                      "technical",     G),
 ("machine-based system",           "definitions",   G),
 ("physical or virtual environments","definitions",  G),
 ("generate outputs",               "definitions",   G),
 ("developer means",                "definitions",   G),
 ("deployer means",                 "definitions",   G),
 ("substantially modifies",         "definitions",   G),
 ("consequential decision",         "definitions",   G),
 ("reasonably foreseeable",         "definitions",   G),
]

def load(root, exts=(".md",), skip_files=frozenset()):
    out = {}
    for r, d, fs in os.walk(root):
        d[:] = [x for x in d if x not in SKIP]
        for f in fs:
            if not f.endswith(exts): continue
            if f.startswith(NOT_A_SOURCE): continue
            p = os.path.join(r, f)
            if os.path.normpath(p) in {os.path.normpath(s) for s in skip_files}: continue
            try: out[p] = open(p, encoding="utf-8", errors="replace").read().lower()
            except OSError: pass
    return out

repo = load(".", (".md",), UNSEARCHABLE)
lib  = load(LIB, (".md", ".txt")) if os.path.isdir(LIB) else {}

rows = []
for term, cluster, slot in TERMS:
    t = term.lower()
    n  = sum(b.count(t) for b in repo.values())
    fl = sum(1 for b in repo.values() if t in b)
    lb = sum(1 for b in lib.values() if t in b)
    state = "ABSENT" if n == 0 else ("thin" if n <= 2 else "held")
    rows.append((cluster, state, n, fl, lb, term, slot))

order = {"ABSENT": 0, "thin": 1, "held": 2}
rows.sort(key=lambda r: (r[0], order[r[1]], -r[4], r[5]))

if TABLE:
    print("| cluster | term | repo | files | library | state | slot |")
    print("|---|---|---:|---:|---:|---|---|")
    for c, s, n, fl, lb, t, sl in rows:
        src = "**library**" if lb else "online"
        print(f"| {c} | {t} | {n} | {fl} | {lb} | {'**' + s + '**' if s == 'ABSENT' else s} | {sl} · {src} |")
else:
    absent = [r for r in rows if r[1] == "ABSENT"]
    thin   = [r for r in rows if r[1] == "thin"]
    print(f"VOCABULARY SWEEP — {len(TERMS)} terms, {len(repo)} searchable files"
          + (f", {len(lib)} library files" if lib else " (no library on this path)"))
    print(f"  absent .................. {len(absent)}")
    print(f"  thin (1-2 hits) ......... {len(thin)}")
    print(f"  held .................... {len(rows) - len(absent) - len(thin)}")
    cur = None
    for c, s, n, fl, lb, t, sl in rows:
        if s == "held": continue
        if c != cur: print(f"\n### {c}"); cur = c
        src = f"library:{lb}" if lb else "RETRIEVE"
        print(f"  {s:<7} {n:>3}  {t:<34} -> {sl:<16} {src}")
