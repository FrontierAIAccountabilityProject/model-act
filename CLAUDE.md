# CLAUDE.md — read this before touching anything

*This file is loaded automatically at the start of every Claude Code and Cowork session in this
repository. It holds what stays true. It deliberately holds no counts, no dates and no "current
state" — those go stale, and a stale instruction is worse than none.*

**It is published deliberately.** This project's drafting is AI-assisted and says so on every page.
These are the actual instructions the assistance operates under, including every rule written because
something went wrong. Publishing the output and withholding the method would be the wrong half.

---

## What this repository is

A **public-domain model state statute** (CC0) extending the responsible corporate officer doctrine —
*United States v. Dotterweich* (1943), *United States v. Park* (1975) — to frontier AI. Duties attach
to whoever holds final authority to prevent or halt, not to whoever wrote the code.

The drafting record is part of the product: the audits, the worklist, the corrections register and the drafting history
are published beside the statute. **That is the whole argument for trusting an AI-assisted draft**, so
the apparatus is not overhead — it is the thing.

---

## The rules that are not negotiable

**1. Never run a git command that writes.** Not `commit`, `push`, `add`, `checkout`, `stash` or
`reset`. Reads only, with `git --no-optional-locks`. **The push is always the maintainer's**, and the
command is handed over unasked — see the hand-off format below.

**2. Before asserting a fact a file already owns, read that file.** A grep finds the owning file; it
never substitutes for reading it. This is the most-violated rule in this repository's history.

**2a. Never move, rename, merge or retire a file you have not opened.** A filename is a claim, and
several in this repository are wrong. On 26 August 2026 seven eleven-line redirect stubs were
renamed as though they were research, one was described in a published index as "every publicly
reported incident, dated", and a 2,698-line dossier was destroyed by three `mv` commands whose
targets collided on `README.md`. **Read the file. Check the destination is empty. Then move it.**

**2b. Open items live in one register and nowhere else.** Anything owed — a defect, a decision, an
unpinned fact, an unanswered objection, a citation that cannot be confirmed — belongs in
`revision/worklist.md`. A second list of open items in a second file is how this repository lost track of twelve
unpinned facts inside a sealed dossier. **If you find work recorded somewhere else, move it to the
worklist and leave a pointer, never a copy.** Proposed amendments are numbered there as
"Amendment *n*"; the drop-in language for each lives in `revision/proposals.md`.

**3. American spelling** throughout, enforced by `check_spelling.py`. Em dashes are fine in repository
prose and **banned in outgoing email**, enforced by `library/check_emails.py`.

**And American legal English, which is more than spelling.** This is a United States state statute.
Use US legal register and US conventions: `offense` not `offence`, `defense` not `defence`,
`judgment` without the medial e, `plaintiff`, `attorney general`, `district court`. (Backticked here
because these are specimens rather than uses, and the spelling sweep cannot tell mention from use —
that is [E50](./corrections/corrections.md).) Citations follow US practice
— reporter volume, abbreviation, first page, pincite; `Id.` and `supra` as the Bluebook uses them, not
as MHRA does. **Where the statute's own text uses a form that is not American** — SEC. 6(b)(1) says
"wilfully" — that is a defect the worklist owns (Amendment 22), not a license to write British English around it.

**4. No superlatives.** Do not write "the strongest", "the most important", "the sharpest". State what
a thing is and what depends on it, and let the reader rank. A repository whose credibility rests on
saying only what it can show should not be grading its own findings.

**5. Quotation discipline.** Nothing is published as a quotation unless it was read in the document. A
retrieval reply, a secondary summary, a law-firm alert and a model's answer about a page are the same
category: leads, not quotations.

---

## The checkers

**Run from the repository root. Run all of them before any hand-off.**

*All seven live in `tools/`. Invoke them from the repository root as `python3 tools/check_links.py`.*

| Script | What it actually checks |
|---|---|
| `tools/check_links.py` | Internal file links and anchors. ⚠ **Skips every `http`/`https` target** — external URLs are unchecked and unarchived |
| `tools/check_claims.py` | Recomputes counts from the repository and compares them to what pages claim. Prints `ALL CLAIMS CURRENT` when clean |
| `tools/check_spelling.py` | British→American, with quotation masking. `--apply` writes; default is a dry run |
| `tools/check_vocabulary.py` | Terms the argument uses against terms the library holds |
| `tools/check_citations.py` | Table-of-authorities rows, debt flags, duplicate rows, captions cited in prose with no row |
| `tools/check_quotations.py` | Every published quotation against the shelf. **Concludes presence, never absence** — see below |
| `tools/build_section_index.py` | Joins all 3,000-odd `SEC. n` references to the sections they are about; rebuilds the front page's status table |

**Read the comments in these scripts before changing them.** Several carry a defect and its
post-mortem, because the defect was subtle and the comment is the only thing standing between the next
person and repeating it.

---

## Traps that have each cost a day

**A generator can outlive the thing it generated.** The eight review-lane packets and their three
extraction builders were retired in the reorganization of 26 August 2026. `tools/build_section_index.py`
survived it and still computes correctly, but it writes to `standards/`, a directory that no longer
exists, and classifies files by directory prefixes that were all renamed. **A tool that runs without
erroring is not a tool that is doing its job.** Before trusting a generator's output, confirm the file
it claims to write is the file the repository actually reads. The older form of this trap, worth keeping
in mind for any generator built next: an extractor that pulls **named sections** cannot see new material
appended at the end of a source file, so the section gets written, the build comes back clean, and the
new text reaches nobody.

**A silent skip and a clean pass look identical in output.** Every checker here has, at some point,
printed a clean result while not reading part of the corpus — an unterminated seal marker running to
end of file, an `except OSError: pass`, a structural test that was really a substring test, a holding
area counted as content. **When a number improves, ask what stopped being counted.**

**A search that returns nothing is evidence about the search.** Extracted text has furniture inserted
into it: page numbers land inside sentences, words hyphenate across line breaks, quotation marks curl.
Three false negatives from three different causes in one day. Use `check_quotations.py --find "…"`,
which normalizes both sides.

**Read the sentence after the one you are quoting.** A proposition a court states in order to reject
it reads exactly like one it holds.

**A case number is not a document.** One matter can produce several opinions, and "not in the opinion"
means nothing until you know which one and how many there are.

**A filename is a claim.** Files on the shelf carry their limits in their own names —
`NO-star-pagination`, `WRONG-IVERSON-NOT-OUR-CASE`, `DOCKET-METADATA-STUB`, `SECOND-COPY-THINNER`.
Those labels are written by the same process that writes the claims they warn about, and **nothing
checks them**. One was wrong for a day and the whole repository believed it.

**Surnames and citations collide.** Two Erin Murphys, two Jensens, two Iversons, and a citation
(`162 F.3d 1015`) shared by two unrelated cases. Confirm it is the case you meant before filing it.

---

## Read-status marks

Used in `authorities/table-of-authorities.md` and throughout. **They are read-statuses and nothing
else — never emphasis, never a way to point at something.** Using ⚠ decoratively inflates a published
figure.

| Mark | Promise |
|---|---|
| ✅ | Read in the document by a person. A pincite is confirmed only where the row says the copy carried real pagination |
| ⚠ | Outstanding debt: not held, held and unread, or read with a pincite the copy cannot settle |
| ◐ | Model-mediated — reached by a tool that had a model read the page. Fixes metadata; **never supplies a quotation.** Always carries a ⚠ too |

**There is no "good law" flag and there will not be one.** That is a staffed proprietary editorial
judgment and this project cannot compute it.

---

## Where things live

*Reorganized 26 August 2026. Every path below is current; if a path in an older instruction does
not exist, it moved here.*

```
act/            the statute and its apparatus
  model-act.txt      the Act at v3.4 — the only source of truth
  clean-copy.txt     the same text, jacket-clean: findings and SEC. 1-13 and nothing else.
                     This is the file to send someone who asked for the statute
  comments.md        the numbered notes
  rules.md           the draft regulations
  bracketed-matter.md  every adopting-state choice, gathered
index.md  README.md  the front page
authorities/    table-of-authorities.md, adopted-standards.md, glossary.md, house-style.md
commentary/     the public explainers, including objections.md
revision/       worklist.md (the single register of open items), proposals.md (drop-in
                amendment language), the review passes and what reviewers sent back
corrections/    corrections.md (the register), changes.md, drafting-history.md, work-log.md
enactment/      legislator-facing: summary, plain English, fiscal note, paths to enactment
appendix/       the evidence record: dossier, bill census, incidents, verification record,
                state enforcement, press corpus, what laboratories publish
filed-comments/ regulatory comments filed, and how to file one
tools/          the six checkers and the section-index generator
archive/        frozen prior versions; do not sweep
_internal/      working material that is not published. Underscore-prefixed so Jekyll
                never builds it and the checkers skip it
_to_delete/     the holding area, created when it is needed. The device shell cannot
                delete, so removing something means moving it here and saying so
_patches/ _includes/ _sass/ assets/   build and styling
```

The private library is **outside this repository**, at `../library/`, and holds copyrighted and
evidentiary files that can never enter a public repo. **`library/_text/` mirrors every source as
plain text — grep does not read PDFs.** Its own `_LIBRARY_INDEX.md` explains the naming scheme.

**The device shell cannot delete.** `rm` fails on the mount. To remove something, `mv` it into
`_to_delete/` and say so.

---

## The errata register, and why it is the most important file here

`corrections/corrections.md` records every published claim this project got wrong, with the fix
attached and a **numbered rule** extracted from it. The numbers are identifiers, not an ordering.

**Read it before opening a question.** More than once a "finding" has been announced that the register
had already made days earlier. The rules that recur:

- **E22** — a quotation held in a working summary is not a quotation
- **E32** — no characterization of a source until it has been read, and the *ordering of a court's
  reasons* is a characterization
- **E44** — the tool built to protect quotations falsified them. A checker is a claim too
- **E47** — text and page are separate claims. A source without star pagination can confirm a
  quotation and never a pincite
- **E48** — an elision is an edit. What a quotation leaves out is published too
- **E49** — the register is part of the text. Read the index of what is already open first
- **E53** — a table of authorities is an index of read-statuses. Grep before adding a row
- **E57** — a model-mediated fetch is a lead, not a reading
- **E58** — a citation appearing only in a URL, a page title or a filename is a label, not a citation
- **E60** — a finding that a quotation is absent must name the document. Absence is provable against a
  text, never against a case
- **E64** — read the sentence after the one you are quoting

**Adding an erratum is normal and good.** It is not an admission of failure; it is the product. But
`corrections/corrections.md` and `corrections/drafting-history.md` are excluded from the spelling
sweep **because their content is evidence** — they quote words as specimens rather than using them, and no normalizer can tell
mention from use. Correct them by hand.

**Negative findings** — a claim that something is *absent* — live in the register's Part I(b) and are
re-tested on every run by `check_quotations.py --negatives`. A false positive is caught by the next
reader; **a false negative is caught by nothing**, because the text has been deleted and nobody
re-checks a sentence that is no longer there.

---

## Working conventions

**Record after each read, not at the end.** A verification that lives only in a session's context is a
verification that did not happen.

**Commit messages: one substantive line.** Not a bullet list, not a summary paragraph.

**Every hand-off carries a push status block**, generated fresh — run `git --no-optional-locks status`
first, because the maintainer often pushes while work is in progress:

> - Uncommitted: *the files, named*
> - Unpushed commits: *how many, or none*
> - Checkers: *the one-line results*
> - Then the single-line `cd … && git add -A && git commit -m "…" && git push`

**When counts change, update every place that claims them.** `check_claims.py` catches the ones it
knows about; it does not know about all of them.

**Web fetching goes through the provided fetch tools only.** Do not reach for `curl`, `wget` or a
Python HTTP client to get around a block. And "blocked" is a property of a request, not of a site — a
route that defeats a script sometimes works through a different tool. Record which route worked.

---

## Fuller documents this compresses

`revision/worklist.md` for every open item, which is the one place they live ·
`corrections/corrections.md` for the rules above at full strength ·
`appendix/verification-record.md` for what is held and in what state ·
`authorities/table-of-authorities.md` for every authority the statute rests on ·
`commentary/objections.md` for what has been said against the Act and what has not been answered.

**If a proposal document is referenced in conversation and you cannot find it on disk, ask for a
current copy rather than reconstructing it.**
