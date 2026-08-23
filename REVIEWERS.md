# For reviewers

*This page is the reviewer's path: the ask, the reading order, your lane, and what happens to your
findings. A reviewer's time belongs to the text, so the path is bounded — and everything beyond it
is laid out, one file at a time, in [the map, Part I](./MAP.md), so anything you skip is a decision
rather than a guess.*

*Arrived from an invitation email that linked [the lane sweep](./audit/v3_5_lane_sweep.md)? That
document is step 2 of the path below, and its first line points back here.*

## The ask

One seat, one lane, scope in writing before work begins. The bounded form: the statute straight
through, your lane's section of the sweep, then **three findings of your choosing, verified or
refuted, with reasons** — a complete and publishable disposition, perhaps six to eight hours. The
full form: roughly ten to twenty hours across eight weeks, adjustable. Unpaid. Your disposition is
published as written, including "approved with reservations," including hostile. Under the
project's published rule, nobody — including the maintainer — may claim this text "survived
review" until named reviewers sign. That rule is why this page exists. **A disposition that
refutes one finding is worth more to this project than a full pass that agrees with everything.**

## What has been done here — the scope, shown

**The text.** A model state statute, SEC. 0 through SEC. 13, 611 lines, tagged and checksummed at
v3.4; [draft implementing regulations](./model_regulations_v1_draft.md); and
[a companion](./model_act_v3_4_companion.md) whose READ FIRST items map the constitutional attack
surface rather than concealing it.

**The self-scrutiny.** Eight drafting-era audits merged into [one record](./audit/record.md),
including [a hostile brief](./audit/record.md#chunk-7) written as opposing counsel would write it;
[a fifteen-fix cure queue](./audit/v3_4_cure_language.md) published *in advance* of the revision
that landed it, departure and destination diffable; [an open successor queue](./audit/v3_5_cure_language.md)
where findings become drafted language; [a five-lane in-house sweep](./audit/v3_5_lane_sweep.md)
that returned **seven defects graded fatal, four of them in the tagged statute**, published with
the front page naming them before it names anything else; and
[a standing watch](./audit/standing_watch_2026-08-20.md) on the federal vehicles and live
litigation, updated as they move.

**The evidence base.** [A press corpus](./research/press_corpus_july_august_2026.md) that grades
every source, maintains its own incident census — three developers, five incidents — rather than
importing any outlet's number, and filed an erratum when it failed that rule;
[the UK AISI incident report](./research/aisi_incident_inc_2026_07_28_01.md), read in full — the
record's one government-authored entry; [a live state-enforcement record](./research/state_enforcement_record_2026.md)
— the Florida suit naming an officer personally (now with its docket identity), the 42-state
investigation, the fifteen-state letter read in full and its signature block resolved against the
instrument, and the Pennsylvania licensure action against a chatbot's fabricated credentials; and
[a verification record](./research/verification_record.md) whose § 4 lists the claims that
**failed** verification and whose § 6 gives every instrument the project relies on a recorded
read-status.

**The standards shelf.** [Comparative officer liability](./standards/comparative_officer_liability.md)
across existing regimes; [a census of the frontier bills](./standards/frontier_bill_census.md);
[the interim standards](./standards/interim_standards.md) with the enacted state texts reproduced;
[a fiscal note](./standards/fiscal_note.md) that states its own defects; and close analyses of the
field's language and practice, named in the tour below.

**The ledger.** [An append-only errata register](./ledger/errata.md) — twenty entries under
numbers that reach E33, the numbers being identifiers rather than an ordering, each mistake
published with its fix attached, including entries that record a *rule* changing rather than a
claim failing. [A changelog](./ledger/changelog.md) with tag checksums. [A diary](./ledger/diary.md).

None of this claims quality. That claim is the one only you can supply, which is why this page
exists. It claims **checkability**: every layer above is built to be verified by someone who does
not trust us.

## The path — the six to eight hours

**0 · The front page.** [README](./README.md) — the argument in one paragraph, the coverage
table, and the status block that names the known defects first; the guide at its top maps the
rest of the page.

**1 · The statute.** [`model_act_v3_4.txt`](./model_act_v3_4.txt) — one sitting, cover to cover.

**2 · The sweep.** [The lane sweep](./audit/v3_5_lane_sweep.md) — the document that most changed
what your seat is for. Read it after the statute and before anything else; your lane's brief below
is written against it.

**3 · What we already know is wrong.** [The errata register](./ledger/errata.md), so no reviewer
spends an hour rediscovering a published mistake.

**4 · How to check us, and what the findings stand on.** [The verification record](./research/verification_record.md)
(§ 4 and § 6), [the press corpus](./research/press_corpus_july_august_2026.md), and beside them
[the table of authorities](./standards/table_of_authorities.md) — every citation with what it is
cited for, so verification is a scan rather than an excavation.

**5 · The queues.** [Sealed v3.4](./audit/v3_4_cure_language.md), then
[open v3.5](./audit/v3_5_cure_language.md) — where a finding from your review becomes drafted
language. CUREs 8–16 are sweep-derived and expressly not maintainer-validated; OPEN QUESTIONS are
decisions, not defects.

**6 · The companion.** [Drafting notes and READ FIRST items](./model_act_v3_4_companion.md) — skim
all, close-read where your lane points.

**7 · The hostile brief.** [The record, chunk 7](./audit/record.md#chunk-7) — if your objection is
already there, grade our answer; if it is not, that finding is what the seat is for.

**Lost at any point?** [The map](./MAP.md) answers "which file owns this question" for the whole
repository.

## On paper

The [reviewer's copy](./archive/model_act_v3_4_reviewers_copy.pdf) (17 pp.) is the statute with
the source file's own line numbers in the margin: a note at *p. 6, l. 236* names the same text as
[`model_act_v3_4.txt#L236`](./model_act_v3_4.txt#L236), so a marked-up printout travels back into
the repository without translation. It is built by [a committed script](./archive/build_reviewers_copy.py),
dates pinned to the tag, document ID derived from the source's own sha256 — two builds are
byte-identical, and [the explainer](./archive/REVIEWERS_COPY.md) carries the two-hash recipe that
proves the PDF is the statute and nothing else. Its predecessor was withdrawn because nobody could
prove that; the register remembers.

## The lanes — and what your seat is now for

The sweep changed the ask. It is no longer *find the defects*; each lane below states what the
sweep found in your area and what, if anything, has been drafted in response. **Your seat is to say
whether we are right, whether the fix is sound, and what we still cannot see.** A finding that the
sweep is wrong is the most valuable disposition this project can receive, because we have acted on
it. *Numbering note: "v3.4 cures" are the sealed set, already landed and diffable; "CURE 8–16" are
sweep-derived and expressly not maintainer-drafted; open questions are decisions, not defects.*

*Each lane is one table, same six rows: what you read, what the sweep found there, what has been
drafted in answer, the questions that are yours, the shelf, and the donor material the intake of
23–24 August added. Substance unchanged from the prose version this replaces; the changelog has
the date.*

### Criminal law

| | |
|---|---|
| **Your text** | SEC. 1, 4, 5–6, and 10(b)–(c) of the statute · v3.4 cures 2, 5, and 13 · the penalty and harm-tier chunks of [the record](./audit/record.md#chunk-3) |
| **The sweep's findings** *(all contestable)* | SEC. 6(a) **cannot be pleaded** — no element requires that a SEC. 5 violation occurred, nothing connects the due-care failure to it, and "the relevant risk" has no antecedent in the section · SEC. 5(d) is a **strict-liability false-statement crime** whose own drafting note cites a statute requiring knowledge · SEC. 6(b)(2) attaches a felony with no fault element · SEC. 6(e) silently widens the "practical power" SEC. 4(a) narrowed · SEC. 6(d) deletes *Park*'s production burden, which may be why the offense would never be charged |
| **Drafted in response** | CUREs 8, 11, 12 |
| **Your questions** | (1) Is the reconstructed SEC. 6(a) chargeable? (2) Is due care as an element the right cure for the *Alleyne* problem? (3) Does the restored burden survive? (4) Is CURE 1's answer — one injury definition, not two — right? (5–6) The two the sweep could not settle: does a state's suspended-sentence law defeat the harm-tier minimum, and does per-victim counting survive the state's merger doctrine? |
| **Your shelf** | the statute · the sweep's criminal section · CUREs 1, 8, 11, 12 · [comparative officer liability](./standards/comparative_officer_liability.md) · the companion where the lane points |
| **Donor, 23–24 Aug** | CURE 8's reconstruction now sits beside the *Dougherty* three-factor formulation the state courts adopted (the queue's fatals pass; [comparative § 5](./standards/comparative_officer_liability.md)) — checking one against the other is the fastest version of your first question |

### Enforcement and prosecution

| | |
|---|---|
| **Your text** | SEC. 5, 9, 10, and 12 · [chunk 3](./audit/record.md#chunk-3) and [chunk 5](./audit/record.md#chunk-5) of the record |
| **The sweep's findings** | **OPEN QUESTION 4 is the most consequential item in the repository** — SEC. 2(a)'s "and not otherwise" and SEC. 1(c) tether every duty to in-state deployment, while the 2026 incidents were *evaluation* conduct, mostly offshore, so five of six fall outside the Act at the threshold · SEC. 5(e) criminalises refusing a demand **no provision authorises** · SEC. 5(b), the only offense matching the conduct, is rule-gated into year four · SEC. 9(b)'s clock is unprovable against the real timelines and rewards certifying less monitoring · SEC. 3(c)(2)(D) makes the honest filer the easier defendant |
| **Drafted in response** | CUREs 9, 10, 14, 15, 16, and OQ4's amendment |
| **Your questions** | (1) Would you charge any of this? (2) Does the OQ4 amendment reach too far extraterritorially? (3) Are the four interim controls at CURE 10 the right four? (4) What does an attorney general's office actually do with this in year one? |
| **Your shelf** | the statute · the sweep's enforcement section · OPEN QUESTION 4 · [the state enforcement record](./research/state_enforcement_record_2026.md) · record chunks 3 and 5 |
| **Donor, 23–24 Aug** | From the queue's fatals pass: the select-agent comparator for CURE 10's four controls · a named public witness and an enforced state theory for CURE 16 · the Colorado repeal arc for OQ4's tier placement |

### Frontier security

| | |
|---|---|
| **Your text** | [the regulations](./model_regulations_v1_draft.md) as the primary text, then SEC. 2, 3, and 9(a) · v3.4 cures 11, 12, and 14 |
| **The sweep's findings** *(this lane's fixes are* not *drafted)* | The safeguards-disabled evaluation with external reach falls into a hole between SEC. 2(c) and SEC. 2(a), so **nothing in the Act reaches the most dangerous configuration in the 2026 record** · Part 6's control objectives are process without substance — the incident record names five contributing factors, none a model property, and **the intersection with Part 6's six objectives is empty** · the halt capability is specified in hours against a kill chain that completes in minutes · the monitoring objective permits the very asynchronous review that produced the detection gap · nothing requires proof of what was actually serving |
| **Drafted in response** | Nothing — **the seat is the response** |
| **Your questions** | (1) Where would practice laugh? (2) Should disabling a safeguard for an evaluation carry a duty — including the case *against*? (3) What six control objectives would you write instead? |
| **Your shelf** | the regulations' Part 6 · the sweep's security section · [the AISI incident file](./research/aisi_incident_inc_2026_07_28_01.md) · [the watch § 8](./audit/standing_watch_2026-08-20.md) · SEC. 2, 8, and 9 of the statute |
| **Donor, 23 Aug** | 42 C.F.R. §§ 73.11 and 73.19 — the select-agent security-plan and escape-notification pattern, the federal template for "secure and isolated" written down ([the gallery's escape section](./standards/the_same_conduct.md#when-the-escaped-thing-was-the-crime)); your question (3) now has a federal answer sheet to mark against |

### Open source and academia

| | |
|---|---|
| **Your text** | SEC. 1(b)(9) and 1(b)(1), SEC. 2's modification budget · v3.4 cures 1, 9, and 16 |
| **The sweep's findings** | SEC. 1(b)(1)(B)'s "does not, standing alone, **extend a lineage**" is undefined in a criminal scope term, and the hostile reading covers every fine-tune of every open-weight frontier model · the interim standards apply with the enacting states' revenue screens **deliberately stripped**, to a criminally enforced duty, from day 180 · SEC. 2(c) excludes the agentic and tool-use research it most needs to protect · SEC. 8's personal certification **survives inside** SEC. 2(c), so a university president must personally certify before a lab may stand up a contained instance · SEC. 10(d)(2) suspension reaches every downstream in-state operator of a released open-weight model |
| **Drafted in response** | CURE 13 only — the rest are unfixed |
| **Your questions** | (1) Is the severance rule right? (2) Is the [10^24] floor in the right place for 2026 hardware? (3) Would your institution's counsel permit a SEC. 2(c) deployment as drafted? |
| **Your shelf** | SEC. 1(b) and 2(c) of the statute · the sweep's open-source section · CURE 6 and its amendment block · [the definition](./docs/the_definition.md) |
| **Donor, 24 Aug** | The lineage-counting rule your lane attacks now has a bipartisan federal sibling — H.R. 8094 counts original run plus fine-tuning, RL and material modification above the same 10²⁶ line ([the definition](./docs/the_definition.md); the census row) — which reframes, without settling, both the [10^24]-floor question and CURE 13 |

### Fiscal and administration

| | |
|---|---|
| **Your text** | [the fiscal note](./standards/fiscal_note.md) as the primary text, then SEC. 10(a) and (f), SEC. 11, SEC. 3 · [chunk 3](./audit/record.md#chunk-3), part D |
| **The sweep's findings** *(none yet fixed)* | The note carries **no dollar figure anywhere** — honest, and administratively fatal, because "indeterminate" is the label that sends a bill to interim study · steady state exceeds startup, impossible on the statute's own clock · **no line for defending the Act**, though a first adopter's largest year-one legal cost is a pre-enforcement facial challenge · no corrections or judiciary impact section, which some states require before a felony bill is considered at all · the function table omits at least eight duties, including frontier-equivalent capability designation, the most technically demanding act in the Act · the whistleblower award is a mandatory entitlement on a fund that may be permanently empty |
| **Drafted in response** | Nothing — **the seat is the response.** The standing fiscal rule to hold us to: enforcement is never sold as self-funding, penalties are never booked as revenue, and startup costs are stated apart from steady state |
| **Your questions** | (1) Is a note with no numbers reportable in your state? (2) What would you need to make it so? (3) Should CURE 7 be sequenced to v4 on administrability grounds, as the sweep's fiscal lane recommends and the maintainer has not accepted? |
| **Your shelf** | the fiscal note · the sweep's fiscal section · SEC. 3, 10(f), and 12 of the statute · record chunk 3, part D |
| **Donor, 23 Aug** | The penalty brackets now carry enacted siblings ([bracketed matter](./standards/bracketed_matter.md) — CA/NY/IL all at \$1M) · the opposition's own cost claim — compliance "verifiable in seconds" — is logged at [the fiscal note § 5](./standards/fiscal_note.md) |

## Filing a disposition

Email FrontierAIAccountabilityProject@proton.me — links or pasted text, no attachments — in any
form: a memo, a marked-up copy, a numbered list of findings. Or, if you were contacted by the
maintainer through a different channel, reply on the channel you were contacted on. It is published
as written, credited or anonymous at the reviewer's choice; council seats publish with names, which
is the point of them. A finding that something is broken is the seat working, not failing: catches
enter [the errata register](./ledger/errata.md) with the fix attached, and the record of who caught
what is permanent.

## What a reviewer is not asked to do

Not to endorse, not to co-author, not to join the project's advocacy, and not to lend standing
beyond the written disposition. A reviewer will not be quoted as supporting the project beyond the
reviewer's written disposition. The request is limited: provide an expert assessment that can be
published under the reviewer's name.


## The state of play — every open item, one line each

*This table is the whole open programme. The [drafting file](./audit/v3_5_cure_language.md) behind
it is a working record — HOLDs, amendment blocks, entries in working order — and nobody is asked to
read it top to bottom: come here, pick your lane's rows, follow the links you need. States:
**DECISION** — the maintainer owes a call; **HELD** — a question awaiting a seat; **DRAFTED** —
language written and checked; **⚠ AMEND FIRST** — drafted, but the sweep requires named amendments
before it may land; **HYPOTHESIS** — sweep-derived language, expressly not settled drafting;
**NO DRAFTED RESPONSE** — the honest state, and why that lane's seat matters most.*

| Item | In one line | State | Lane |
|---|---|---|---|
| [OPEN QUESTION 1](./audit/v3_5_cure_language.md#open-question-1--sec-3c4-does-connecticut-become-a-fourth-interim-standard) | Does Connecticut become a fourth interim standard? Recommendation on file: exhibit, not adopted. | **DECISION owed at v3.5** | criminal law |
| [OPEN QUESTION 2](./audit/v3_5_cure_language.md#open-question-2--sec-2--sec-9-does-the-duty-reach-an-evaluation-run-with-safeguards-disabled) | Does the duty reach an evaluation run with safeguards disabled? Largely disposed if OQ4's amendment lands. | **HELD** | security · criminal law |
| [OPEN QUESTION 3](./audit/v3_5_cure_language.md#open-question-3--sec-4-the-third-party-evaluator--does-practical-authority-still-run-to-the-officer) | Third-party evaluator: does practical authority still run to the commissioning officer? | **HELD** | enforcement |
| [OPEN QUESTION 4](./audit/v3_5_cure_language.md#open-question-4--sec-2a-and-sec-1c-the-act-does-not-reach-the-conduct-it-was-written-after) | The Act does not reach the conduct it was written after — five of six incidents fall outside at the threshold. Amendment drafted. The single most important item. | **OPEN — amendment drafted** | enforcement · criminal · federalism |
| [CURE 1](./audit/v3_5_cure_language.md#cure-1--serious-injury-source-moves-to-18-usc--1365h34) | Injury definition moves to 18 U.S.C. § 1365(h)(3)–(4) — reaches mental-faculty impairment; addendum maps the old definition's blind spot. | **DRAFTED (outside-answered)** | criminal law |
| [CURE 2](./audit/v3_5_cure_language.md#cure-2--sec-13c-a-review-valve-on-the-suspension-order) | A review valve on the preemption suspension order, forward-only. | **DRAFTED** | federalism |
| [CURE 3](./audit/v3_5_cure_language.md#cure-3--the-regulations-conformed-to-v34) | The regulations conformed to v3.4 (near-miss, signatories, cadence, header). | **DRAFTED** | mechanical |
| [CURE 4](./audit/v3_5_cure_language.md#cure-4--sec-9a-the-two-characterisation-shaped-triggers-recast-as-observable-events) | The two characterisation-shaped reporting triggers recast as observable events (the VW defeat-device pattern). | **DRAFTED** | criminal · security |
| [CURE 5](./audit/v3_5_cure_language.md#cure-5--sec-8-punctuation) | SEC. 8 punctuation. | **DRAFTED (mechanical)** | — |
| [CURE 6](./audit/v3_5_cure_language.md#cure-6--sec-1b1-the-developers-own-designation-as-a-third-route-into-scope) | Self-designation route into scope — a developer's own 'frontier' claim as a jurisdictional fact. | **DRAFTED — ⚠ 4 amendments required first (incl. a First Amendment question)** | open-source · constitutional |
| [CURE 7](./audit/v3_5_cure_language.md#cure-7--the-covered-frontier-enterprise-scope-follows-the-ecosystem-duty-follows-the-function) | The covered frontier enterprise — compute suppliers and scale conditions. | **DRAFTED — ⚠ 7 amendments required first; fiscal lane recommends sequencing to v4 (undecided)** | all lanes |
| [CURE 8](./audit/v3_5_cure_language.md#cure-8--sec-6-the-individual-liability-offense-reconstructed) | SEC. 6 reconstructed so the central offense can be pleaded: predicate violation, nexus, Park's burden restored. | **HYPOTHESIS (sweep-derived)** | criminal law |
| [CURE 9](./audit/v3_5_cure_language.md#cure-9--sec-10e-the-access-authority-the-act-forgot-to-import) | The records-demand authority the Act forgot to import (§ 331(e) without § 374). | **HYPOTHESIS (sweep-derived)** | enforcement |
| [CURE 10](./audit/v3_5_cure_language.md#cure-10--sec-3c3-interim-controls-so-sec-5b-is-not-dormant-until-year-four) | Four interim controls so SEC. 5(b) is not dormant until year four. | **HYPOTHESIS (sweep-derived)** | enforcement · security |
| [CURE 11](./audit/v3_5_cure_language.md#cure-11--sec-5-name-the-obligor-sec-9b-write-the-duty-in-the-active-voice) | Name the obligor; write the reporting duty in the active voice. | **HYPOTHESIS (sweep-derived)** | criminal law |
| [CURE 12](./audit/v3_5_cure_language.md#cure-12--sec-5d-restore-the-scienter-its-own-donor-requires) | Restore the scienter SEC. 5(d)'s own donor requires. | **HYPOTHESIS (sweep-derived)** | criminal law |
| [CURE 13](./audit/v3_5_cure_language.md#cure-13--sec-1b1b-say-sever-not-extend) | 'Sever,' not 'extend' — the open-weight fine-tune lineage fix. | **HYPOTHESIS (sweep-derived)** | open-source |
| [CURE 14](./audit/v3_5_cure_language.md#cure-14--sec-9b-a-detection-clock-that-cannot-be-gamed-by-certifying-less-monitoring) | A detection clock that cannot be gamed, plus notice to the people whose systems were breached. | **HYPOTHESIS (sweep-derived)** | enforcement |
| [CURE 15](./audit/v3_5_cure_language.md#cure-15--sec-3c2-a-disclose-and-cure-valve-because-the-text-currently-punishes-candour) | A disclose-and-cure valve, because the text currently punishes candour. | **HYPOTHESIS (sweep-derived)** | enforcement |
| [CURE 16](./audit/v3_5_cure_language.md#cure-16--sec-1b7-a-deception-limb-because-van-buren-excludes-what-actually-happened) | A deception limb, because Van Buren excludes what actually happened. | **HYPOTHESIS (sweep-derived)** | enforcement |
| Security-lane findings | The SEC. 2(c)/2(a) hole around safeguards-disabled evaluations; Part 6's control objectives as process without substance; halt timing; monitoring. | **NO DRAFTED RESPONSE — the seat is the response** | security |
| Fiscal-lane findings | No dollar figures; no defence line; no corrections section; eight omitted duties; an entitlement on an empty fund. | **NO DRAFTED RESPONSE — the seat is the response** | fiscal |
| [CURE 17](./audit/v3_5_cure_language.md#cure-17--sec-11d-remedies-for-a-reporter-outside-employment) | Whistleblower remedies that fit a reporter outside employment — the record's actual reporter was one. | **HYPOTHESIS (intake-derived)** | criminal law |
| [CURE 18](./audit/v3_5_cure_language.md#cure-18--sec-9b-an-immediate-notice-tier-for-incidents-in-progress) | An immediate-notice tier for incidents in progress, on the select-agent escape-clock donor. | **HYPOTHESIS (intake-derived)** | enforcement · security |
| [CURE 19](./audit/v3_5_cure_language.md#cure-19--sec-0a-the-personhood-finding-the-states-have-begun-to-enact) | A SEC. 0 finding: a system is not a person. Gate mostly discharged — Idaho Code § 5-346 verbatim in hand; Utah identified; Tennessee's text still to pull. | **HYPOTHESIS (intake-derived)** | — |

## The whole repository

Everything here — every file, in chapter order, with what each is for — is at
[the map, Part I](./MAP.md). Nothing in it is required for a disposition; all of it is available
to one.

---

*Maintenance rule: when the reading order, the lanes, or the terms change, this page changes in the
same commit. The front page carries the banner and the terms; it does not grow this page back.*
