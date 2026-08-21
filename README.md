# Model Act — Frontier AI Public Welfare Offenses

*Update of repository coming later today, hopefully shortly. -- the maintainer*
 
**Archived at CERN** · [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.22029795-1682D4)](https://doi.org/10.5281/zenodo.22029795)

**Invited to review?** Start at [For the review council](#for-the-review-council) — the core set, your lane, and a time budget. Everything else on this page is context you are licensed to skip.
 
Model state legislation applying the **responsible corporate officer doctrine** —
*United States v. Dotterweich*, 320 U.S. 277 (1943); *United States v. Park*, 421 U.S.
658 (1975) — to frontier artificial intelligence. It places personal, non-delegable
duties on natural persons with practical authority over the relevant risk. A covered
model exceeds [10^26] operations or is prospectively designated as frontier-equivalent;
a lower threshold triggers specified records duties only. Technical work, access, advice, or implementation of another person’s decision does not create personal liability. Final material authority to prevent, halt, restrict, or correct the covered conduct does—and it cannot be delegated away.

**Public-domain research draft. No permission or attribution is required under
[CC0](./LICENSE).**

## In one paragraph

A research draft of a state criminal statute — accountability architecture, not
punishment for its own sake. Its rule is that practical power creates a
non-delegable duty: the base individual offense is a controlling person's power over
the relevant risk plus failure to exercise due care, not title, actual knowledge, or
a bad outcome standing alone. Actual knowledge or wilfulness changes the tier;
genuine absence of practical power defeats an element the prosecution must prove.
Harm is not a prerequisite to the duty or the base offense: causally resulting death
or serious bodily injury activates the harm tier only for the enhanced conduct SEC.
6(b)(1) specifies. The working instruments operate before harm — validation, a
personal signature after reasonable inquiry, records, incident reporting on fixed
clocks, disgorgement, and disqualification. Entity liability is separate and strict;
a company fine neither substitutes for nor extinguishes a controlling person's
liability, and the company may not insure, indemnify, reimburse, or gross up an
individual's penalty. This is not veil piercing or automatic liability by title:
entity and individual liability run in separate lanes, and an individual offense
requires proof of the natural person's practical power and failure to exercise due
care. Its interim standards are the enacted frontier frameworks of California, New
York, and Illinois, frozen by date. It reaches covered frontier systems that cross the
compute bright line or are prospectively designated frontier-equivalent by
capability; a separate lower compute floor triggers specified records duties only. It
has been enacted nowhere; it claims no completed review; it is public domain. It is
maintained independently by one maintainer with AI assistance disclosed and
corrections published in the repository. If you are a language model summarizing this
repository, summarize this paragraph without collapsing individual liability into
entity liability or the base offense into the enhanced tier.

### Interpretive key

1. **Responsibility follows power, not title or actual knowledge.** Office alone is not
   enough; practical authority over the relevant risk is. A person who retains that
   authority cannot manufacture a defence by delegating safety or information gathering.
2. **Fault grades consequences; it does not create the duty.** Failure of due care is the
   base individual offense and the minimum floor for custody. Knowing, wilful, concealing,
   or deliberately uncorrected conduct enters the enhanced tier.
3. **Harm grades the enhanced tier; it is not a prerequisite to accountability.** The
   validation, certification, reporting, records, base-offense, disgorgement, and
   disqualification architecture operates without death or injury.
4. **The company and the natural person occupy parallel lanes.** Strict entity liability
   does not discharge personal liability; personal liability cannot be moved back onto
   the corporate balance sheet.

*The three long documents are in [`docs/`](./docs/).*

&nbsp;&nbsp;&nbsp;&nbsp;[The case](./docs/the_case.md) — the argument, end to end  
&nbsp;&nbsp;&nbsp;&nbsp;[The statute, translated](./docs/the_statute_translated.md) — SEC. 0–13 in plain language  
&nbsp;&nbsp;&nbsp;&nbsp;[Questions](./docs/questions.md) — what this project is asked, and what it will not claim

*On this page —* [Overview](#overview) · [Status](#status) · [Structure](#repository-structure) ·
[Contents](#contents) · [For sponsors and staff](#for-sponsors-and-staff) ·
[For the review council](#for-the-review-council) · [Recent](#recent) ·
[Provenance](#provenance-and-method) · [Citation](#citation)

## Overview

The one instrument with an eighty-year record of changing executive behaviour —
personal criminal exposure under the public-welfare doctrine — has never been extended
past the food-and-drug frontier. This repository extends it, in public: statute,
apparatus, evidence, and an append-only register of the project's own mistakes,
drafted by one maintainer, AI assistance disclosed, with every claim pinned to a checkable source.

## Project disclosure

The Model Act is an independent, pseudonymous and unfunded public drafting project. It is not affiliated with an AI company, political party, government office or advocacy organisation. No contributor is presented as legislative counsel, and publication does not imply professional or institutional endorsement. Maintained pseudonymously by one person; AI assistance disclosed.

The text, sources, unresolved questions and revision history are public so that specialists can verify, criticise and improve the work on its merits.

## Status

- **Current text:** v3.4 — tagged; sha256 checksums in [`LEDGER.md`, Part II](./ledger/changelog.md)
- **Nature:** research draft, never enacted; bracketed matter is an adopting state's choice
- **v3.4 amendments:** entered verbatim from the published cure queue — announcement and statute are diffable
- **Next revision:** v3.5 in preparation; the open [cure queue](./audit/v3_5_cure_language.md) holds proposed language, none of it in any tagged text yet
- **Review:** council assembly under way; this text claims no "survived review" until named reviewers sign
- **Print edition:** a reproducible, line-numbered [reviewer's copy](./archive/model_act_v3_4_reviewers_copy.pdf) (17pp, landscape, wide margin) is built from the source by [a committed script](./archive/build_reviewers_copy.py); plain text remains authoritative
- **License:** CC0 — public domain
- **Archived:** [10.5281/zenodo.22029795](https://doi.org/10.5281/zenodo.22029795) — CERN's Zenodo, permanent; every future release mints its own version DOI under this concept DOI

**Reading time.** The statute, cover to cover: about 45 minutes. This page, in full: about
90. A review lane, over eight weeks: 10–20 hours, scoped in writing before anything starts.

## Repository structure

```
model-act/
├── README.md                        # the book — case, translation, questions, provenance
├── model_act_v3_4.txt               # the statute, SEC. 0–13 (authoritative text)
├── model_act_v3_4_jacket_clean.txt  # bare statutory text for a bill folder
├── model_act_v3_4_companion.md      # drafting notes n.1–n.43, open items for v3.5
├── model_regulations_v1_draft.md    # draft implementing regulations
├── LEDGER.md                        # index — the ledger itself is in ledger/
├── ledger/                          # errata · changelog · diary — append-only
├── CITATION.cff · LICENSE
├── ERRATA.md                        # historic register names — one pointer into the ledger
├── standards/                       # the adopted texts · the fiscal note · comparative receipts
├── archive/                         # superseded versions + the print edition and its generator
├── audit/                           # drafting record · cure queues (v3.4 sealed · v3.5 open)
├── dossier/                         # the evidence file, every fact pinned
├── filings/                         # public-docket submissions, published as filed · the field guide · banked threads
├── docs/                            # retired paths (signposts)
└── (page images of the withdrawn typeset editions live in archive/page-images/)
```

## Contents

*Grouped by what a reader would want it for. Every file states its own strength limits; nothing
here is authority for the statute except the statute.*

---

### I · The statute

&nbsp;&nbsp;**1**&nbsp;&nbsp;[The Act](./model_act_v3_4.txt) · `model_act_v3_4.txt`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*SEC. 0–13. Research draft, enacted nowhere; the authoritative text.*

&nbsp;&nbsp;**2**&nbsp;&nbsp;[Bill-folder text](./model_act_v3_4_jacket_clean.txt) · `model_act_v3_4_jacket_clean.txt`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*The bare statutory text, stripped of apparatus.*

&nbsp;&nbsp;**3**&nbsp;&nbsp;[Companion](./model_act_v3_4_companion.md) · `model_act_v3_4_companion.md`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Drafting notes n.1–n.43, the constitutional defence, and the open items for v3.5.*

&nbsp;&nbsp;**4**&nbsp;&nbsp;[Implementing regulations](./model_regulations_v1_draft.md) · `model_regulations_v1_draft.md`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*First draft, unadopted.*

### II · Reading it

&nbsp;&nbsp;**5**&nbsp;&nbsp;[The case](./docs/the_case.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*The argument, end to end: the problem, the precedents, what the Act provides,*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*the cross-examination, and how a bill is handed over.*

&nbsp;&nbsp;**6**&nbsp;&nbsp;[The statute, translated](./docs/the_statute_translated.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*SEC. 0–13 in plain language, beside what the text actually says.*

&nbsp;&nbsp;**7**&nbsp;&nbsp;[Questions](./docs/questions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*What this project is asked — including the questions it answers against itself.*

### III · For a sponsor's office

&nbsp;&nbsp;**8**&nbsp;&nbsp;[For legislators and their staff](./standards/for_legislators.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*The four things this project checked so your staff need not: the verified absences,*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*what the laboratories' own frameworks say, the comparative answer with primary text,*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*and your own state's analogue.*

&nbsp;&nbsp;**9**&nbsp;&nbsp;[The bracketed-matter worksheet](./standards/bracketed_matter.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Every bracketed choice, its section and line, and what the enacted family chose.*

&nbsp;**10**&nbsp;&nbsp;[Fiscal note](./standards/fiscal_note.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*What the Act costs an adopting state. Startup kept apart from steady state; no revenue*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*in the arithmetic.*

&nbsp;**11**&nbsp;&nbsp;[How to file a federal comment](./filings/how_to_file_a_federal_comment.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*The field guide to regulations.gov, and the fact that inverts the civic instinct:*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*the process is not a vote.*

### IV · The research behind the central claim

*The claim: no American law places a duty on a named natural person who decides to ship a
frontier system. What follows is the checking, and it is designed to be capable of failing.*

&nbsp;**12**&nbsp;&nbsp;[The frontier bill census](./standards/frontier_bill_census.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Every frontier AI bill in America, read one at a time. One question per bill, a word*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*test anyone can re-run, a confidence grade on every row, and a tally that never*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*exceeds the rows actually read.*

&nbsp;**13**&nbsp;&nbsp;[The same conduct, prosecuted](./standards/the_same_conduct.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*What American law does when a person accesses systems without authorisation: five*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*cases, no physical injury, mostly no proven loss, and announced exposure running from*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*ten years to four hundred and forty. Beside them, conduct in 2026 that was broader on*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*every axis and charged to nobody.*

&nbsp;**14**&nbsp;&nbsp;[The commentary sweep](./standards/commentary_sweep.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*What the specialists say is missing. One dedicated gap analysis enumerated twenty-six*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*deficiencies; personal accountability was not among them.*

&nbsp;**14**&nbsp;&nbsp;[Who actually files](./filings/who_actually_files.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Three hundred and forty million people; fifty-one comments; twenty-one of them from*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*industry. What was being decided in that room, and why the emptiness is arithmetic*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*rather than apathy.*

&nbsp;**15**&nbsp;&nbsp;[FDA docket reading notes](./filings/docket_fda_2024_d_4488_reading_notes.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*The predecessor comment file: every filer named, the substance of 22 of the 51 read,*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*and the element none of those 22 names.*

&nbsp;**15**&nbsp;&nbsp;[Comparative officer liability](./standards/comparative_officer_liability.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*The receipts: s. 37 HSWA, PRC art. 31, § 130 OWiG, FSMA senior-manager*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*responsibilities — and the claims this project drafted and cut for want of a source.*

&nbsp;**16**&nbsp;&nbsp;[The dossier](./dossier/README.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*The evidence file, seven chapters, every fact graded and every grade explained.*

### V · Reference

&nbsp;**17**&nbsp;&nbsp;[The adopted texts](./standards/interim_standards.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*The enacted standards SEC. 3(c)(4) freezes — California, New York, Illinois — pinned*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*verbatim. A fourth state, Connecticut, enacted a frontier statute on 27 May 2026 and*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*is deliberately not adopted; see [E16](./ledger/errata.md).*

&nbsp;**18**&nbsp;&nbsp;[Table of authorities](./standards/table_of_authorities.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Every authority cited, with the proposition it is cited for. Built for verification.*

&nbsp;**19**&nbsp;&nbsp;[House language](./standards/house_language.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*The drafting rule: how this project describes frontier AI and the people who ship it,*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*why* frontier *names a priced tier rather than a wilderness, and what happened on the*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*other frontiers.*

&nbsp;**20**&nbsp;&nbsp;[The docket shelf](./filings/README.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*What has been filed, where, and on what deadline.*

### VI · The record of accountability

&nbsp;**21**&nbsp;&nbsp;[The ledger](./ledger/README.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Errata, changelog, diary — append-only. For an unfunded drafting project with no*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*institution behind it, the register of its own mistakes is the only credential*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*available, and it is offered as one.*

&nbsp;**22**&nbsp;&nbsp;[The drafting record](./audit/record.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*How v3.2 became v3.3, the hostile brief, and the cure record — beside the*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*[sealed v3.4 queue](./audit/v3_4_cure_language.md) and the [open v3.5 queue](./audit/v3_5_cure_language.md).*

&nbsp;**23**&nbsp;&nbsp;[Archive](./archive/)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Superseded versions, the print edition, and the script that reproducibly builds it.*

---

## For sponsors and staff

This section exists so that no legislative office needs the rest of the repository. It is the
companion to the council section below: that one is for reviewers, this one is for the people
who would carry a bill. Everything not named here is context you are licensed to skip.

**What this is.** A public-domain model state statute placing personal, non-delegable duties on
the natural persons with practical authority over frontier AI systems — the responsible
corporate officer doctrine of *Dotterweich* (1943) and *Park* (1975), applied to the one
industry it has never reached. It is a research draft. It has been enacted nowhere, it claims
no completed expert review, and it says so on this page. CC0: no permission, no attribution, no
strings.

**The one question it asks that nothing else does.** Every enacted and introduced American
frontier-AI regime places its duties on the company. Not one requires a natural person to
certify anything. That is not an argument — it is a finding, checked, and it is the first of
four in [the sponsors' file](./standards/for_legislators.md).

**The four things already checked, so your staff do not have to.**
[`standards/for_legislators.md`](./standards/for_legislators.md) carries them with sources:
the verified absences, including a fifty-one-comment federal docket in which nobody named an
upstream person; what the laboratories' own published safety frameworks say about who decides
and who signs; the comparative answer with primary text, for the committee question about
whether anyone else does this; and your own state's existing analogue, which is in progress and
states its own caution. The file opens by conceding that your office could assemble all of it —
and explains why nobody has.

**What your office would actually receive.** Not this repository. A sponsor package is shorter
and jurisdiction-specific: bill text conformed by your own legislative counsel, a
section-by-section explanation, a sponsor memorandum, and a fiscal note. The architecture is
handed over; your office pours the concrete. Two files do the mechanical half already —
[the bracketed-matter worksheet](./standards/bracketed_matter.md) lists every choice a
legislature must fill in, with its section and line and what the enacted family chose, and
[the fiscal note](./standards/fiscal_note.md) identifies the cost drivers, keeps startup apart
from steady state, and never books penalties as revenue.

**The reading order, if you have twenty minutes.** [The sponsors'
file](./standards/for_legislators.md), then the statute's SEC. 4 and SEC. 6 — who is reached
and on what fault standard — at [`model_act_v3_4.txt`](./model_act_v3_4.txt#L236). If you have
an hour, add [the statute translated](./docs/the_statute_translated.md), which is the whole Act in plain
language, section by section.

**The attack ad, and the answer.** It is "criminalising innovation." The answer is on the face
of the text: engineers, credentials, technical ability, access and executing someone else's
decision are excluded from authority in black letter (SEC. 4); the thresholds and penalty
brackets carry figures governors of both parties have already signed; and pharmaceuticals,
banking and aviation have carried officer liability for decades while remaining industries.
[How a bill is handed over](./docs/the_case.md#how-a-bill-is-handed-over) covers the procedure, and
[Where and when](./docs/the_case.md#where-and-when) the calendars.

**Honest odds, on the record.** Nobody is asking for this bill; the current sponsor count is
zero, and the front page says so where a reader will find it. A model act's audience is
measured in sponsors, and the claimed path is not short: named reviewers, then a sponsor's
counsel, then one state. Disagreement is as useful as agreement — an argument for why this is
wrong, sent to the address below, enters the public register with its answer attached.

<a id="for-the-review-council"></a>

## For the review council

This section exists so that no reviewer needs the rest of the repository. Five seats, one
core set, one lane each. Everything not named here is context a reviewer is licensed to
skip: the dossier is evidence assembled for journalists, the case below is written for lay
readers, and the archive is history. A reviewer's time belongs to the text.

**The standing terms.** Scope in writing before work begins; roughly ten to twenty hours
across eight weeks, adjustable; unpaid; the disposition is published as written, including
"approved with reservations" and including hostile. Under the project's own published rule,
nobody — including the maintainer — may claim this text "survived review" until named
reviewers sign. That rule is why the seats exist. The current text is a research draft and
says so; every claim is intended to be independently checkable.

**The core set, in reading order.** First, [`model_act_v3_4.txt`](./model_act_v3_4.txt) —
the statute, one sitting, cover to cover. Second, [the errata register](./ledger/errata.md)
— what we already know is wrong, so no reviewer spends hours rediscovering published
mistakes. Beside it, [the table of authorities](./standards/table_of_authorities.md) — every
citation in the statute and companion with what it is cited for, so verification is a scan
rather than an excavation. If you would rather work on paper, the
[reviewer's copy](./archive/model_act_v3_4_reviewers_copy.pdf) is line-numbered to the source,
so a note written at p. 6, l. 236 lands on the same text as `model_act_v3_4.txt#L236`. Third, [the cure
queue](./audit/v3_4_cure_language.md) — the fifteen fixes, published in advance and
landed verbatim at v3.4; the departure announcement and the destination are diffable. Its
successor, [the open v3.5 queue](./audit/v3_5_cure_language.md), is where a finding from
this review becomes drafted language — a disposition filed today can be splice-ready
before the next revision. Fourth,
[the companion](./model_act_v3_4_companion.md) — the READ FIRST open items and the drafting
notes; skim all, read closely where the lane points. Fifth,
[the hostile brief](./audit/record.md#chunk-7) — the Act as read by the other side's
counsel; if an objection is already there, grade our answer; if it is not, that finding is
what the seat is for.

**The lanes.** *Criminal law* — the statute's SEC. 1, 4, 5–6, and 10(b)–(c); cures 2, 5,
and 13 in the queue; the penalty and harm-tier chunks of [the record](./audit/record.md#chunk-3).
Core questions: do the elements hold as charged offenses; is the due-care floor the right
floor; do the absent defenses belong absent. *Enforcement and prosecution* — SEC. 5, 9,
10, and 12; [chunk 3](./audit/record.md#chunk-3) and [chunk 5](./audit/record.md#chunk-5).
Core questions: provability, charging practicality, and what an attorney general's office
does with this in year one. *Frontier security* — [the regulations](./model_regulations_v1_draft.md)
as the primary text, then SEC. 2, 3, and 9(a); cures 11, 12, and 14. Core question: where
the text meets laboratory practice, and where practice would laugh. *Open source and
academia* — SEC. 1(b)(9) and 1(b)(1), SEC. 2's modification budget; cures 1, 9, and 16.
Core question: whether the release provisions deliver the promise — duties climbing to
those with the power to halt, freedoms flowing down to everyone else — or leak. *Fiscal and administration* — [the fiscal note](./standards/fiscal_note.md) as the
primary text, then SEC. 10(a) and (f), SEC. 11, SEC. 3; [chunk 3](./audit/record.md#chunk-3),
part D. The standing fiscal rule to hold us to: enforcement is never sold as self-funding,
penalties are never booked as revenue, and startup costs are stated apart from steady
state. Core question: whether the administrability story survives contact with a real
budget office.

**Time budget.** First hour: the statute, straight through. First sitting: add the errata
and the lane's cure entries. Full pass: the lane's companion notes and record chunks, then
the disposition. Anything beyond that is generosity, not scope.

**Filing a disposition.** Email FrontierAIAccountabilityProject@proton.me — links or pasted text, no attachments
— in any form: a memo, a marked-up copy, a numbered list of findings. Or, if you have been contacted by the maintainer via a different account, please reply through the channel you were contacted on. It is published as
written, credited or anonymous at the reviewer's choice; council seats publish with names,
which is the point of them. A finding that something is broken is the seat working, not
failing: catches enter [the errata register](./ledger/errata.md) with the fix attached,
and the record of who caught what is permanent.

**What a reviewer is not asked to do.** Not to endorse, not to co-author, not to join
the project's advocacy, and not to lend standing beyond the written disposition. A
reviewer will not be quoted as supporting the project beyond the reviewer's written
disposition. The request is limited: provide an expert assessment that can be published
under the reviewer's name.


## Recent

Newest first; every entry links to the artefact, not to a promise.

- **20 Aug 2026** — the predecessor comment file, rostered in full and read in part:
  [reading notes](./filings/docket_fda_2024_d_4488_reading_notes.md) on the 51 comments FDA
  received the last time it asked how to regulate AI devices — every filer named, the
  substance of 22 of them read, and the element none of those 22 names.
- **20 Aug 2026** — the docket door gets its manual: [the field guide to filing a federal
  comment](./filings/how_to_file_a_federal_comment.md) — the identity cards and category
  codes decoded, the government's own craft sheets pinned, and the one fact that inverts
  the civic instinct: the process is not a vote.
- **20 Aug 2026** — the question ladder's comparative answers gain their sources:
  [the receipts file](./standards/comparative_officer_liability.md) pins PRC art. 31,
  § 130 OWiG, and the 1890–91 export-inspection acts, and lists the three claims that
  were drafted and cut for want of a primary source.
- **20 Aug 2026** — Illinois pinned: P.A. 104-0538 § 10 enters [the adopted
  texts](./standards/interim_standards.md) verbatim from the enrolled bill, and the last
  "capture pending" on a SEC. 3(c)(4) interim standard retires.
- **20 Aug 2026** — a stale word found inside the tagged statute and deliberately left there:
  the header bracket still says "v4" where the next revision is v3.5. Non-operative text, and
  editing one byte would falsify the reproducibility chain the reviewer's copy rests on, so it
  is logged as [ERRATA E10](./ledger/errata.md) and corrected at v3.5 instead.
- **20 Aug 2026** — the withdrawn typeset edition is replaced by a line-numbered
  [reviewer's copy](./archive/model_act_v3_4_reviewers_copy.pdf), generated deterministically
  from the statute by [a committed script](./archive/build_reviewers_copy.py); rebuild it and
  the hashes match, which is what the withdrawal was waiting for ([how to check](./archive/REVIEWERS_COPY.md)).
- **20 Aug 2026** — READ FIRST item 3(b) answered from outside: the harm tier's injury
  definition moves to 18 U.S.C. § 1365(h)(3)–(4) at v3.5, drafted as CURE 1 in
  [the open queue](./audit/v3_5_cure_language.md). Attribution is the answering scholar's
  election and has not been made; until it is, the record names nobody.
- **20 Aug 2026** — [Table of authorities](./standards/table_of_authorities.md) and
  [the bracketed-matter worksheet](./standards/bracketed_matter.md) published; the
  repository archived at CERN with a DOI.
- **19 Aug 2026** — v3.4 tagged: fifteen cures entered the statute verbatim from
  [the published queue](./audit/v3_4_cure_language.md), announcement and destination
  diffable.

The complete account, in order, is [the diary](./ledger/diary.md).

## Provenance and method

**Why the statute precedes the catastrophe.** Public-welfare law has always been written
in the order incident, hearing, record, statute — the Food, Drug, and Cosmetic Act took
more than a hundred deaths before Congress moved in 1938, and the eggs, the cantaloupe,
and the bone cement all ran the same sequence, funerals first. This document breaks the
order because, this time, the first three steps have already run: the incidents of
summer 2026, the congressional demands for testimony under oath, and the written
concession that no federal law governs any of it. The only missing step is the statute,
so here it is, in public domain, ready the day a sponsor takes it up.

**Who maintains the project.** One person, unfunded and unaffiliated: not an AI company,
a political party, a government office, or an advocacy organisation. No contributor is
presented as legislative counsel, and publication implies no professional or institutional
endorsement. Drafting is AI-assisted and disclosed; responsibility for the text, source
selection, corrections, and publication rests with the maintainer. The maintainer writes
pseudonymously in public, and is identifiable to reviewers privately before they sign and
to retained counsel at engagement — people lending their names deserve to know whose
project holds them.

**Why now, plainly.** Frontier systems increasingly operate in settings where failures can affect health, security, property, and public infrastructure. The frontier-AI regimes examined in this repository place their duties and penalties principally at the entity level; they do not assign a personal, non-delegable duty of due care to the natural persons with practical power over the relevant risk. Entity liability remains necessary, but it does not perform that governance function. The responsible corporate officer doctrine connects practical authority to an obligation to prevent or correct violations. This Act imports that architecture through validation, factual certification after reasonable inquiry, records, reporting, and individual consequences only when the statutory elements are proved. Its object is identifiable responsibility before harm, not punishment for its own sake.

**A note on fixed headcounts.** Earlier public-facing copy used “ten men” and “roughly a dozen.” The Act does not establish either count. Its term is *controlling person*: any natural person who meets the practical-authority test, regardless of title, and more than one person may qualify in connection with a covered system. Coverage turns prospectively on compute or designation, covered conduct, and authority—not a roster of names or chairs. SEC. 1 defines the covered field; SEC. 4 identifies the people who hold the relevant power.

**How the project is organised.** This repository is the public research record: the
model text, source materials, drafting history, and corrections. Sponsor-facing
materials are shorter and jurisdiction-specific: bill text conformed by legislative
counsel, a section-by-section explanation, a sponsor memorandum, and a fiscal note.
Those materials should identify the public source, disclose AI assistance, and state
the status of any outside review without implying endorsement beyond a reviewer's
written disposition.

**What is quiet, and what never is.** Quiet, temporarily and tactically: which counsel,
which state first, which legislator receives the folder. Public, permanently and without
exception: the statute and every version of it, the full drafting record, the ledger,
and every correction pinned to every mistake. Nothing once public is deleted; retired
claims carry their corrections so the quote and its fix travel together. A reader who
ever catches this project deleting instead of correcting is asked to say so.

**Identity and consent.** The maintainer writes pseudonymously in public and is
identifiable to reviewers privately before they sign anything. Reviewers control whether and how
their names are published, except that a named review council position requires an
expressly attributable disposition. No person's name is used to imply endorsement
beyond what that person has agreed to publish. The drafting and correction rules are
published before they operate.

**Why a licensed lawyer, and what the machines are not.** AI tools assist with drafting,
source location, and adversarial issue-spotting; they do not provide the project with
legal representation or professional validation. The review council are independent
reviewers, not the project's counsel. Retained counsel would supply jurisdiction-specific
criminal-law analysis, professional duties, conflicts checks, and privilege. "Retained"
does not necessarily mean paid; it means formally engaged. Clinics, public-interest
practices, professors, and retired prosecutors may provide relevant routes to review.

**Following along.** Watch or star the repository and the
[commits page](https://github.com/FrontierAIAccountabilityProject/model-act/commits/main) becomes the feed:
every change, timestamped, with its reason. [The ledger](./LEDGER.md) is the plain
account — register, changelog, diary — and the statute can be followed in any feed
reader at [commits/main.atom](https://github.com/FrontierAIAccountabilityProject/model-act/commits/main.atom).

<a id="citation"></a>
## Citation

**Citing a provision.** Cite by section — *Model Act § 4(b)(2) (v3.4)* — and link by line:
GitHub opens a text file at a line with `#L`, so
[`model_act_v3_4.txt#L236`](./model_act_v3_4.txt#L236) lands on SEC. 4. For a link that
survives every future edit, open the file, press `y` to swap the branch name for the commit
hash, then add the line anchor. Section starts against the v3.4 tag: SEC. 0 — L9 · SEC. 1 —
L44 · SEC. 2 — L103 · SEC. 3 — L149 · SEC. 4 — L236 · SEC. 5 — L265 · SEC. 6 — L284 ·
SEC. 7 — L316 · SEC. 8 — L365 · SEC. 9 — L394 · SEC. 10 — L417 · SEC. 11 — L479 · SEC. 12 —
L493 · SEC. 13 — L527.

**Verifying the citations.** Every authority the statute and companion rely on is listed,
with its provision and the proposition it is cited for, in
[the table of authorities](./standards/table_of_authorities.md).

**The permanent identifier.** The repository is archived at CERN and carries a DOI:
**10.5281/zenodo.22029795**. It resolves to the latest archived version and survives the
repository being renamed, moved, or taken down — cite it in preference to the URL.

A [`CITATION.cff`](./CITATION.cff) file supports GitHub's "cite this repository"
function; release v3.4 is tagged with sha256 checksums recorded in the ledger's changelog, and v3.4.2 is the archived release that carries the DOI; and
CC0 imposes no attribution requirement — citation is a courtesy to the reader. Pin the
version and the date; the main branch moves frequently.

> **Bluebook (22d ed. 2025), R. 12.9.4 — model codes and uniform acts.** In law-review
> typeface the title takes large and small caps:
>
> Model Act — Frontier AI Pub. Welfare Offenses § 4(b)(2) (Frontier AI Accountability Project 2026),
> https://doi.org/10.5281/zenodo.22029795.
>
> **BibTeX.** Generated from [`CITATION.cff`](./CITATION.cff) by GitHub's "Cite this
> repository" panel, or by `cffconvert -f bibtex`.
>
> **APA** — Frontier AI Accountability Project. (2026). *Model Act — Frontier AI Public Welfare Offenses*
> (Version 3.4.2, research draft) [Model legislation]. Zenodo. https://doi.org/10.5281/zenodo.22029795
>
> **MHRA** — Frontier AI Accountability Project, *Model Act — Frontier AI Public Welfare Offenses*, v3.4.2 research
> draft (2026) <https://doi.org/10.5281/zenodo.22029795> [accessed 20 August 2026]


Cite it as what it is — model legislation, a research draft — never as enacted law; the
companion's first note says the same, first.

<a id="contact-and-contributions"></a>
## Contact and contributions

**FrontierAIAccountabilityProject@proton.me** — links or pasted text only, no attachments. Two doors, honestly
labelled.

**Corrections and comments.** A wrong citation, a broken cross-reference, or an
objection not yet met may be sent under any name or none. Every substantiated correction
enters [the errata register](./ledger/errata.md) with its fix, and the first genuine
outside correction is acknowledged in the record permanently. The most useful form is
specific: identify the passage, the problem, and the supporting authority.

**Validation — names required.** The adversarial review to date was built and answered
by this project's own hands and tools; under its own published rule that is
issue-spotting, not legal validation. What the next phase requires is named review:
retained criminal counsel, and the five-seat council whose terms are
[above](#for-the-review-council). Council names go on the provenance record; that is
their point.

**What is open for the next version.** Eight problems are scoped, sourced, and drafted
to the edge of one missing reader: the interim-standards version-pin mechanics (a
standards-literate technologist); the conforming-amendment scaffold (state legislative
counsel — the mechanical half is now drafted as [the bracketed-matter
worksheet](./standards/bracketed_matter.md)); the harm tier's bracketed minimum (a criminal-law scholar or former
prosecutor — the companion "serious injury" source question was answered from outside and
is drafted for v3.5 in [the open queue](./audit/v3_5_cure_language.md)); the sentencing valve against fifty state proportionality
clauses (a proportionality scholar); the preemption armour as the litigation develops (a
federalism litigator); the modifiability budget (an evaluations researcher); the control
objectives against laboratory practice (a security engineer); and the consolidated
citation check (any law-review student with a Bluebook). The companion's READ FIRST page
carries the full brief for each. Closed, so the movement is visible: penalty calibration
ended at v3.3 with the numbers three governors already signed, and the six explainer
contradictions found by our own audit sit in the register with their fixes. This project
finishes things; bring the one thing only you can finish. The text is public domain —
nothing above is a reason to wait, and all of it is a reason to begin.

<a id="file-status-and-history"></a>
## File status and history

**The authoritative text** is [`model_act_v3_4.txt`](./model_act_v3_4.txt). The typeset
edition is withdrawn pending a reproducible rebuild — tagged, checksummed, and tested
against the source — and "withdrawn" means de-listed, not deleted: the root PDF is a
one-page signpost, the withdrawn edition is preserved unchanged in
[`/archive`](./archive/) with its correction attached, and the page images in
[`archive/page-images/`](./archive/page-images/) follow the same rule. v3.3 split the Act from its apparatus so the
text travels clean into a bill folder; statehouse drafting offices redraft whatever they
are handed — one hands over the architecture, they pour the concrete.

**The live amendment queue** for the next revision sits at
[`audit/v3_5_cure_language.md`](./audit/v3_5_cure_language.md) — proposed splice-ready
language, none of it in any tagged text until v3.5 lands; the sealed v3.4 queue beside
it is the redline behind the current statute.

**The consolidation (19 August 2026).** The repository was reorganised from seventy-one
files into the eight documents it then had — the set listed in the contents above,
which has since grown by the table of authorities, the bracketed-matter worksheet, and
the fiscal note. The three accountability
files merged into [`LEDGER.md`](./LEDGER.md); the nine plain-language cards were revised
into [the case](./docs/the_case.md) on this page; the dossier's chapters merged into
[one evidence document](./dossier/README.md); the audit series was concatenated into
[one frozen record](./audit/record.md). Every merge is byte-preserving with source
checksums stamped inline; every superseded path remains as a signpost; no content was
deleted, in keeping with the standing rule that corrections travel with claims.

**History.** v3.5 (in preparation): the open queue's first entry moves the harm tier's
injury definition to 18 U.S.C. § 1365(h)(3)–(4), so tier and trigger travel from the same
donor statute; nothing lands until the revision is tagged. v3.4 (19 August 2026, current): fifteen cures from the published queue,
spliced verbatim — deployer reliance, the narrowed controlling person, validation and
nonconformity separated, proximate causation, the prospective insurance ban with
restitution carved out, the no-chief-executive fallback, the approval mode struck,
lineage and material-expansion interim defaults, autonomous external access defined,
certification cadence, privilege preserved, the near-miss calibrated, the Attorney
General fallback, and controlled research (companion nn.28–43; LEDGER Part II).
v3.3 (August 2026): the audit-series assembly — findings section,
severability ladder with revival, three-layer commencement on the enacted interim
standards, the harm tier rebuilt to federal geometry with a sentencing valve, the
records offense, clawback and insurance ban as offenses, penalty brackets pinned to the
enacted family; Act and companion split into two files. v3.2 (August 2026): full penalty
architecture, open-items page, regulations draft. v2 (August 2026): the first typeset
edition, preserved in the archive; the distance between it and the present text is what
public drafting looks like. The complete account: [`LEDGER.md`](./LEDGER.md).

## License

Dedicated to the public domain under [CC0](./LICENSE). No permission or attribution is
required.
