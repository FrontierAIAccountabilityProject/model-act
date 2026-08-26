# The remap — what is wrong, and the structure that fixes it

*Written 26 August 2026 from a full pass over the repository. Numbers are computed, not
estimated; the commands are in the session log. Nothing here has been done yet.*

---

## Part I — What a reader actually meets

**The artifact is 1.5% of its own repository.** 109 markdown files, 39,194 lines, around a
611-line statute. Roughly 1,300 pages of apparatus wrapped around a 15-page bill.

**The navigation is switched off.** The site runs Just the Docs, whose sidebar hierarchy is built
entirely from per-page front matter. **85 of the 86 published pages have none.** The result is one
flat alphabetical list — `abstract`, `already_a_crime_for_you`, `banked_threads`,
`bracketed_matter` — with no grouping and no order.

**So three hand-written indexes grew to replace it.** README (76 links), MAP.md (150),
REVIEWERS.md (150). Across the repository there are **2,149 internal links over 86 pages, 25 per
page.** The single heaviest linker, `standards/section_index.md`, emits **472 links and is linked
to by nothing** — the biggest connector in the repository is unreachable.

**The reviewer path costs 13,012 lines.** REVIEWERS.md prescribes eight steps for a task it bills
at six to eight hours:

| Step | File | Lines |
|---|---|---|
| 0 | README.md | 821 |
| 1 | model_act_v3_4.txt | 611 |
| 2 | audit/v3_5_lane_sweep.md | 467 |
| 3 | ledger/errata.md | 3,317 |
| 4 | verification record · press corpus · authorities | 1,701 |
| 5 | v3.4 + v3.5 cure language | 2,667 |
| 6 | model_act_v3_4_companion.md | 893 |
| 7 | audit/record.md | 2,535 |
| | **Total** | **13,012** |

About 430 pages. The statute under review is 4.7% of it. Step 3 is the corrections register, read
in full, "so no reviewer spends an hour rediscovering a published mistake" — an hour spent to save
an hour.

**And the good version already exists.** `packets/criminal_law.md` is 1,185 lines and does the job
properly: an ask, an arithmetic ("six questions, six drafted repairs — any three items are a
complete disposition"), the four sections to read named, the lane's corrections already extracted,
and where to file. **Forty pages, bounded, professional.** REVIEWERS.md offers it in italics above
a 430-page alternative, so a reader cannot tell it supersedes the eight steps.

---

## Part II — The language

**About 4,000 uses of roughly 25 coined terms.** Several collide with established American legal
meanings, which is worse than being unfamiliar: the reader arrives at a wrong meaning confidently.

| Term | Uses | Problem | Plain replacement |
|---|---|---|---|
| cure | 1,170 | You are amending statutory text | **amendment** |
| lane | 586 | Corporate jargon | **topic** |
| errata | 521 | Fine in publishing, oversold as a system | **corrections** |
| sweep | 486 | A sweep is what police do | **internal review** |
| packet | 414 | Nearly fine | **reading pack** |
| seat | 369 | A seat is on a bench or a board | **role** |
| **disposition** | **170** | **Means how a case was resolved. One letter from *deposition*.** | **review** |
| shelf | 149 | Coined | **source library** |
| READ FIRST | 110 | Coined | **open issues** |
| open question | 97 | Coined | **decision needed** |
| standing watch | 50 | Nautical | **recheck** |
| read-status | 36 | Coined | **checked / not checked** |
| debt | 30 | Means money | **unverified citations** |
| checksum, sha256 | 59 | Means nothing to a law reader | **version fingerprint**, or drop |
| jacket | 26 | A jacket is a court file cover | **clean copy** |
| **companion** | — | **A publishing word — a companion *volume*. The genre has its own term.** | **section-by-section notes** |
| tombstone, banked thread, canon check, crown entry | — | Coined | drop |

MAP.md adds six more of its own — *tagged, sealed, live, queue, append-only, signpost*.

**On *companion*.** The file is notes n.1–n.43 keyed to sections — which is exactly what US
legislative drafting calls a **section-by-section analysis**, and what model-act publishers (the
Uniform Law Commission, the American Law Institute) call **Comments**. Both are terms of art the
audience already knows. Using neither, and inventing "companion", loses the one piece of free
recognition the genre offers.

**"Disposition" is the one to fix first.** It is the word the project uses for the thing it most
wants from a reader, it is addressed to criminal lawyers, and to them it means something else.

---

## Part III — Where things hide

**"Objections" is the test case.** 51 of 86 files mention them. Objection content lives in **five
systems with three numbering schemes**:

1. `docs/known_objections.md` — "Known objections"
2. `docs/questions.md` — "Part two: the objections we hear most"
3. `audit/record.md` chunk 7 — "the hostile brief"
4. an "objection bank" with numbered entries and a "crown entry"
5. a section in each of the nine reading packs

A reader asking "has anyone raised X?" cannot answer it.

**Same title, different documents.** README § "The record, dated" (83 lines) and
`docs/timeline.md` "The record, dated" (228 lines) share a title and **zero sentences**. Repository
wide: *"Who this is about"* appears as a heading in 11 files, *"The ask"* in 9, *"Read first — the
statute itself"* in 7.

**The front page does five other files' jobs.** 821 lines, 21 sections. Its table of contents sits
at line 150, after four major sections. It carries two overlapping introductions ("In one
paragraph" at 291, "Overview" at 477) on top of the unheaded summary at line 17. Everything from
line 477 — Overview, Project disclosure, Status, Repository structure, For sponsors, For the review
council, Provenance, Citation, Contact, File status, License — is 344 lines of back matter, 42% of
the page.

**The counts are a standing liability.** `check_claims.py` tracks 13 count-claims and its own
documentation admits it does not know them all. Its number-word table silently ran out at sixty on
26 August. Every count is a number that goes stale and buys the reader nothing: *"an append-only
register of every correction, each with the rule it produced"* says what *"fifty entries, numbers
reaching E64"* says, and never needs touching again.

---

## Part IV — The proposed structure

Six plain-named places. Nothing invented; every folder says what is in it.

```
/
  index.md              the front page — about 100 lines
  the_act.txt           the statute, tagged and unchanged
  section_by_section.md the notes on each section      [model_act_v3_4_companion.md]
  start_here.md         what this is, one page         [docs/abstract.md]

  work/                 WHAT IS OPEN — the worklist
    index.md              one table: decisions, amendments, citations to check
    proposed_amendments.md                             [audit/v3_5_cure_language.md]
    internal_review.md                                 [audit/v3_5_lane_sweep.md]
    history.md                                         [audit/record.md]

  reference/            LOOK THINGS UP
    glossary.md                                        [standards/what_these_words_mean.md]
    sources.md                                         [standards/table_of_authorities.md]
    objections.md         ← ONE file, merged from five
    choices_for_your_state.md                          [standards/bracketed_matter.md]
    adopted_standards.md                               [standards/interim_standards.md]
    …the remaining standards/ and docs/ pages

  record/               WHAT CHANGED, WHAT WE GOT WRONG
    corrections.md                                     [ledger/errata.md]
    changes.md                                         [ledger/changelog.md]
    work_log.md                                        [ledger/diary.md]

  by_topic/             the nine reading packs         [packets/]
  evidence/             supporting material            [research/ dossier/ filings/]
```

**Deleted:** `MAP.md` (its rule — *one owner per fact* — moves into `CLAUDE.md`; the sidebar does
the rest), `LEDGER.md` (a pointer file), `standards/section_index.md` (472 links, reachable from
nowhere).

**Merged:** the five objection systems into `reference/objections.md`. The dated one-off audit
files into `work/history.md`.

**Every moved page keeps its old URL** via `redirect_from` — supported on GitHub Pages. The Zenodo
deposit is a frozen snapshot and is unaffected.

---

## Part V — The centrepiece: `work/index.md`

The reviewer-recruitment apparatus is replaced by a worklist. **63 letters produced 4 replies and
every reading pack has had zero visits**; an invitation is not the mechanism. A list someone can
start on in ninety seconds might be.

**The content already exists** and is 57 rows:

- **4 decisions needed** — currently "OPEN QUESTION 1–4"
- **23 proposed amendments** — currently "CURE 1–26", each already tied to a section
- **30 citations wanting a reporter check** — currently "the standing debt"

One table. Columns: *what it is · which section · what it needs · how hard.* Anyone picks a row —
the maintainer, a professor who wandered in, or a future session.

---

## Part VI — Order of work

1. **`work/index.md`** — build the worklist. Additive, nothing broken, and it shows the new
   language working on one page before 4,000 substitutions.
2. **Front matter on all 86 pages** — the sidebar starts working. Mechanical, reversible.
3. **Vocabulary** — the table in Part II, `disposition` first.
4. **Folders and filenames** — Part IV, with `redirect_from` on every moved page.
5. **The front page** — cut to about 100 lines.
6. **Merge the objections** into one file.
7. **Strip the counts** and retire the `check_claims.py` rows that no longer have a target.

Steps 1 and 2 carry most of the reader gain and neither destroys anything.
