*The changelog — what changed in the statute and when, with hashes. Part II of the ledger; the
[errata register](./errata.md) and [diary](./diary.md) are beside it.*

## Part II — The changelog

**Between versions — 25 August 2026, seventh batch: the project acquires a front door.** No change
to any tagged text.

*The problem.* Everything in this repository is written for somebody who has already decided to be
here. There was no page that answered, for a stranger with thirty seconds, the question *what is
this and how much of it is there.* Outreach was consequently underselling the work: an apologetic
paragraph cannot tell a cold recipient the difference between a crank with a document and eleven
months of drafting with an errata register.

*The page.* [The project in one page](../docs/abstract.md). The problem in two sentences; what the
project is; **what exists, counted**; the five findings the research produced that are not published
anywhere else; what a reviewer is asked for and what they get back; and, in its own section, what
this is not — not law, not introduced, no endorsement, and nobody may say it survived review until
named reviewers sign.

*And the numbers on it are enforced rather than asserted.* `check_claims.py` now recomputes the
abstract's document count, statute section count, errata count and all three cure-queue counts from
the files, and fails the build if the page and the truth disagree. Where a number only grows it is
stated as a floor, so it stays true between sweeps rather than going stale on the next commit. That
is the same rule the register applies to everything else: a count that appears in recruitment copy
is checked wherever it appears.

*Linked from* the front page's contents list and the map, so it is reachable rather than merely
present.


**Between versions — 25 August 2026, sixth batch: three more Senate hearings, and the New York bill
in full.** No change to any tagged text. All four documents arrived as direct downloads with intact
text layers, so unlike the second batch there is no decode and no OCR: everything below is
quote-in-hand.

*The one that matters most.* **S. Hrg. 119-255, *Hidden Harms*** (Senate Judiciary Subcommittee on
Privacy, Technology, and the Law, 9 September 2025) — two former researchers at a frontier developer,
under oath, on how their own safety findings stopped existing. The subject is child safety on
virtual-reality platforms and parts of that record are distressing; **this project's use of it is
structural, narrow, and says so at every point of use.** What it supplies is the mechanism, and the
mechanism is the argument for every records duty in this Act: a ninety-day deletion policy for raw
research data, which exists for good privacy reasons, means that **striking a line from a report is
enough to make the observation behind it unrecoverable**. Nobody destroys anything; the compliant
path and the destructive path are the same path. Carried at
[who has to tell you](../standards/who_has_to_tell_you.md) § 4d with its limits attached — sworn
allegation, not adjudicated fact, the company was not a witness, and the subject is not
frontier-model risk.

*The ceiling campaign, from the podium.* **S. Hrg. 119-284, *AI've Got a Plan*** (Senate Commerce,
10 September 2025) — the Director of the Office of Science and Technology Policy as sole witness,
saying that state preemption "is something we look at closely". [Known
objections](../docs/known_objections.md) gains the section, including the concession Kratsios made
inside his own answer — that patchwork compliance "gives more power to large technology companies
that have armies of lawyers" — which is taken seriously and answered rather than quoted
triumphantly.

*And the New York row closes.* The complete twelve-page print of **S 1169-B** replaced the
four-page capture, and the word test was rerun on all of it: *officer* returns one hit and it is
"committee or officer of the state"; *certification* returns one and it is a subject of regulation,
not a duty; *criminal*, *felony*, *misdemeanor*, *signature*, *senior personnel*, *frontier* and
*catastrophic* return nil. **The lineage count is unchanged: four drafts of a frontier-safety audit,
one survivor.** Three of its provisions are now carried anyway, because they are drafted answers to
questions this project is still asking: § 110's auditor-independence machinery, which goes further
on independence than the enacted Illinois text or California SB 53; § 109(4)'s statutory anonymous
internal disclosure channel with a monthly status duty, which is precisely the machinery whose
absence the *Hidden Harms* witnesses describe; and § 114(2), which reverses the causation
presumption at the pleading stage and then refuses to let a completed audit discharge it — a
warning aimed straight at this Act's own architecture, and now a question for the enforcement lane.

*Housekeeping.* The March 2026 Commerce hearing is **S. Hrg. 119-505**; the number was in a display
font that would not decode and is confirmed from the congress.gov landing page. Every hedge about it
is discharged. **S. Hrg. 119-171** (*AI-Generated Deepfakes*, 21 May 2025) is catalogued, contents
and witness list read, body unread, and nothing relies on it.


**Between versions — 25 August 2026, fifth batch: the first full repository sweep, and a new tool
to make it repeatable.** No change to any tagged text.

*The tool.* `check_links.py` at the repository root, stdlib only, deterministic, no network. It
walks every markdown file in the tree and reports three things: relative links whose target does
not exist, anchors whose target heading or explicit `id` does not exist, and markdown files
nothing links to. It models GitHub's duplicate-heading rule, so a second heading with the same
words resolves to `-1` as it does on the site, and it carries one allowlist entry with its reason
attached, because a tombstone that explains itself is not an orphan. It runs beside
`check_claims.py` and, like it, exits non-zero on a finding.

*What the first run found across 101 markdown files.* Three dead file links, two anchors that were
false positives until the duplicate-heading rule went in, and nine files reachable from nowhere.
All of it is fixed, and two of the findings were serious enough to number:
**[E40](./errata.md#e40--the-council-was-described-as-five-seats-after-it-had-grown-to-eight)** —
the front page and the dossier both described the review council as five seats, and the dossier
named the five, three days after the count went to eight. Three lanes did not appear at all, so a
person qualified for federalism, proportionality or torts and design was being told by recruitment
copy that there was no seat for them.
**[E41](./errata.md#e41--three-packets-linked-to-a-path-the-projects-own-checker-already-knew-was-dead)**
— three packets opened with a link to `packets/README.md`, which does not exist. The project
already knew: `check_emails.py` bans that exact string so it can never leave in an email. Nothing
was checking the repository itself, which is the whole reason the new tool exists.

*Two navigation defects fixed and recorded here rather than as errata, being omissions rather than
false statements.* The **eight audit chunks** were named in prose in the drafting record and linked
from nowhere, so nothing in the repository reached them by clicking; `audit/README.md` now indexes
all eight with a note saying why the index was added. And **`research/canon_check_2026-08-24.md`**
was missing from the map that claims to record which file owns which question; it now has its row,
carrying its own house rule that nothing on the examiner's bookshelf may be cited until it has been
retrieved and read.

*And the front page gains the quotation.* The record table takes a thirteenth row for **16 July
2025**, and immediately beneath the table there is now a pull-quote: the chair of the Senate
Judiciary Subcommittee on Crime and Counterterrorism stating the enforcement gap in terms, with
the three limits printed beside it rather than left for a reader to discover — the subject is
copyright, no one proposed officer liability, and a chair's rhetorical question is a
characterisation and not a declination record. The expanded row is at
[the dated record](../docs/timeline.md).


**Between versions — 25 August 2026, fourth batch: a Senate subcommittee asks this project's own
question.** Five documents arrived, and one of them changes what the repository is entitled to
assert.

*The document.* **S. Hrg. 119-202, *Too Big to Prosecute?: Examining the AI Industry's Mass
Ingestion of Copyrighted Works for AI Training***, Senate Judiciary Subcommittee on **Crime and
Counterterrorism**, 16 July 2025. The saved PDF is a browser reprint whose fonts carry a shifted
encoding, so ordinary extraction returns ciphertext; the body text was recovered by a character
decode validated by reading, and the scanned appendix by OCR at the images' native 150 ppi. The
decode map, the artefact register and the graded citation set are in the library note, so no
quotation has to be re-derived.

*What it changes.* Until today the enforcement-gap premise — that conduct by frontier developers
goes unprosecuted that would be prosecuted in anybody else's hands — rested on this project's own
reasoning. It now rests on the subcommittee chair, in the printed record: "the FBI and the
Department of Homeland Security regularly prosecute individuals who engage in exactly the same kind
of behavior ... But have these Big Tech companies been prosecuted? No, of course not." Three limits
travel with it wherever it is used, and are stated at each use: the subject is copyright rather than
catastrophic risk, nobody at that hearing proposed officer liability, and neither *Dotterweich* nor
*Park* is mentioned.

*Where it landed.* [Known objections](../docs/known_objections.md) gains three sections: the
enforcement gap as stated by a Senate chair; the wait-for-the-courts objection in its best
available form, made under oath by Professor Edward Lee, with Senator Durbin's Section 230
rejoinder to it; and — from the mirror-image Commerce hearing of 3 March 2026 — an industry
witness telling the Senate that AI "operates within" existing accountability frameworks and that
regulatory predictability is what lets a company ship.
[Who has to tell you](../standards/who_has_to_tell_you.md) gains § 4c: Congress has already
legislated this file's central insight in a neighbouring subject matter, in the TRAIN Act (Welch
and Blackburn), whose text is **not** in hand and none of whose provisions are described.
[The table of authorities](../standards/table_of_authorities.md) gains both hearings, and
*Kadrey v. Meta* as a candidate authority quoted expressly at second hand and not to be cited until
the slip opinion is retrieved.

*And a tracker line that would have produced a false finding.* A commercial tracker describes
**New York S 1169-B** (Gonzalez) as requiring "independent audits of high risk AI systems", which
reads like a fifth attempt in the RAISE audit lineage and would have changed the census's
one-survivor-in-four line. The print says otherwise: it amends the **civil rights law**, defines
algorithmic discrimination by protected characteristic, and turns on consequential decisions about
employment, housing, credit and health care. It is New York's analogue of Colorado SB 24-205, not
of the RAISE Act. **The lineage count is unchanged.** The row is entered as an adjacent lineage so
nobody has to do it again — and it records the fact that matters for the outreach: **Gounardes is a
co-sponsor** of a bill that keeps a statutory audit section, in the same session in which the audit
came out of his own. ⚠ The capture is 4 pages of 12 and the finding is conditional on the rest.

*The New York floor question, discharged and empty.* Retrieval item 3 — the Senate floor transcript
for the passage date — is worked and returns a negative answer: RAISE was called as Calendar
No. 1889 on 12 June 2025, the roll was taken, and the bill passed **58 to 1** with Senator Cooney
the sole negative. No member laid it aside; no member asked why § 1421(4) had come out three days
earlier; there was no debate. The sponsor memoranda (item 2) become the highest-value unopened
source in the file. ⚠ The version read was a YouTube auto-caption, not the stenographic record;
nothing from it may be quoted verbatim until checked against `nysenate.gov/transcripts`. Reinvent
Albany's December 2025 FOIL study of the same chamber is carried as a caution on what that chamber
actually releases.

*Two errata, both from reading the project's own pages rather than the day's sources.*
**[E38](./errata.md#e38--the-packet-that-promised-the-whole-lane-and-left-out-the-only-published-criticism-of-it)**
— the criminal-law packet claimed to inline the whole lane and omitted the only published criticism
of it, Lyness's misdemeanour objection, on the eve of that packet being sent to Lyness himself. The
objection is now in the sweep, in the project's own words and against the project's own text, and
is question 7 on the packet's menu, with the honest statement that nothing in this repository yet
argues that misdemeanour authority reaches the felony tier at SEC. 6(b).
**[E39](./errata.md#e39--the-same-sentence-twice-in-two-packets-for-a-day)** — the filing
instruction printed twice in two packets. One sentence, both builders, all eight packets
regenerated.


**Between versions — 25 August 2026, third batch: the packets carry the day's record.** Four lanes
gain the material that arrived after they were written, each through its builder rather than by
hand.

*Proportionality* gains the threshold comparison: the enacted siblings trigger at "at least 50
deaths or $1 billion in damages," and not one disclosed incident of 2026 is known to have met any of
them. The section states the refusal as the lane's question rather than its premise, and concedes
that a 50-death threshold is a deliberate choice to keep novel criminal exposure away from the
merely alarming. *Torts and design* gains Judge Orrick's ruling in the Meta reduction-in-force case,
with the warning that the Act does not reach employment decisions and the ruling is authority for
nothing — it is quoted because the claim failed on what people outside the deciding system could
show, which is the asymmetry the records provisions are drafted against. *Federalism* gains the fact
that the largest developer asked a state to strengthen its statute while the ceiling campaign argues
patchwork burden, together with the counter-reading that a standard industry helped shape is how a
ceiling arrives with its fingerprints on it. *Open source* gains Kimi K3 breaking the UK AI Security
Institute's evaluation environment, in the population August's federal framework excludes by design.

*Also in this batch, from regenerating the three extraction packets:* the queue's own work reached
the pages a reviewer reads (OPEN QUESTION 1's resolution, the Connecticut act's whistleblower-only
duty, the Apollo donor note), a doubled sentence in the filing section of all three was removed, and
the paragraph explaining how a seat's work becomes v3.5 moved into the builders, having been lost
from two packets by an earlier hand-edit — the failure the builders' own docstrings warn against.
All eight packets round-trip stable; every cross-link checked.

**Between versions — 25 August 2026, second batch: what the day's record does to the argument.**
Four sources arrived and none of them stayed in the press corpus.

*The developer asked for the answer our own queue proposes.* OPEN QUESTION 2 asks whether a duty
should reach an evaluation run with safeguards disabled. On 21 August OpenAI asked California to
amend SB 53 to reach models "still in training or evaluation," defining the conduct as that "which
could bypass a third party's security controls and compromise the third party's confidential
information" — having opposed the statute's first version. The queue records this as a donor note
with a warning attached in the same paragraph: it is not an endorsement of this Act and must never
be described as one.

*The census gains its sharpest finding.* The enacted state frontier statutes turn on thresholds of
"at least 50 deaths or $1 billion in damages." Against that, the documented events of 2026 —
containment escapes, zero-days, a third party's servers reached, a national safety institute's
evaluation environment broken — produced neither, and on the same authority it is "unclear whether
any existing U.S. law requires reporting" of them. Not one disclosed incident of the year is known
to have triggered any enacted state statute. That answers the redundancy objection with a fact
rather than a preference, and the known-objections page now carries it as its own section.

*A court states the evidentiary problem this Act's plumbing exists to solve.* Twenty-six former Meta
employees alleged internal AI systems selected them for layoff; the judge declined interim relief
because "the record at the moment does not persuade me of the merits," calling it "an unusual, or a
new sort of issue" hard to gather evidence for. The Act does not reach employment decisions and the
ruling is authority for nothing. It is quoted because the claim failed on what a plaintiff outside
the system could show, which is the asymmetry every logging and retention duty here is drafted
against.

*And three items join the standing watch:* Montana's SB 25 under First Amendment challenge with a
September ruling expected, the first constitutional test of a state AI statute carrying criminal
exposure; whether California's amendments pass before its session ends; and an open-weight model
breaking the UK AI Security Institute's evaluation environment, which is the population August's
federal review framework excludes by design.

**Between versions — 25 August 2026, the word, the aim, and where this stands in the process.**
The project has been asking experts for something it had never defined. A *disposition* is now
defined where it is used: a reviewer's determination of a question, in the judicial sense of a
matter finally determined rather than merely discussed, published entire under their name or
anonymously, which the maintainer may answer beside but may not edit or overrule. The glossary
gains that entry and two more, *lane* and *seat*. The dispositions register states the aim in one
sentence — not approval, but a text attacked in public by people qualified to attack it, with the
results published whichever way they fall.

The same batch locates the project in the legislative process, using the process's own account of
itself. USA.gov lists a "petition by people or citizen groups who recommend a new or amended law"
as one of three recognised origins of a bill; the House's summary begins "First, a representative
sponsors a bill," and everything after that presupposes a sponsor this Act does not have. So the
Act sits before step one, in a space no procedure reaches — which is why the review structure had
to be invented rather than borrowed. Congress.gov's observation that policy expertise lives in
standing committees, whose members serve on few of them for many years, is the model the eight
lanes reproduce; its admission that "for many bills, the process will not follow the sequence of
congressional stages that are often understood to make up the legislative process" is the argument
for finding defects now rather than trusting a later stage to catch them.

Harvard's research guide supplies the standing and the strongest objection in the same paragraph.
Model acts "may be proposed by any individual or organization," and are "rarely enacted in
entirety" — so the form is open and the realistic success condition is being used as a basis. But
a uniform law "takes at least two years; some have taken 15 years," and this Act has existed since
June. That is quoted against ourselves on two surfaces, with the concession that nothing in the
project's method substitutes for years of committee scrutiny, and that a disposition finding the
text premature would be a legitimate outcome rather than a failure of the process.

**One claim of ours was withdrawn in the writing.** Both the front page and the reviewer page had
said that no producer of model legislation opens its drafting to outside experts. The Uniform Law
Commission's own site says its acts are "drafted in an open and deliberative process that draws on
the expertise of state-appointed commissioners, legal advisors and observers," with published
drafts and section-by-section readings at two annual meetings. The claim was wrong and is now the
narrower true one: what is unusual here is not that outsiders are consulted, but that a reviewer's
conclusion is published as theirs, unedited, beside a numbered register of the drafter's own
mistakes. The reviewer page's freeze, in place since the criminal-law packet was delivered, was
lifted by the maintainer to land this batch.

**Between versions — 24 August 2026, the reviewer page's doors.** The packets now greet a
reviewer at the top of the page and see them out at the bottom — the paper path offered before
the terms and after the map; CURE 19's row catches up with its own evening (the gate is
discharged, and the row now says so); one doubled conjunction removed.

**Between versions — 24 August 2026, last entry of the day — a status claim withdrawn, and the
diary written.** Four packets described the criminal-law lane as "under review now"; the true
state is a packet delivered and a call pending, and this project does not round that up. The
claim is removed at the builders and the packets regenerated: no lane is described as under
review until a named review exists. The diary carries the day.

**Between versions — 24 August 2026, the second retrieval wave — nineteen instruments, one
erratum, three ⚠ retirements.** No change to any tagged text. The maintainer pulled bands B and
D of the retrieval list in one evening and the reads land everywhere at once. **E36:** the
Colorado SB 26-189 figures this record carried were roughly double the final revised note's —
conformed on every surface to $46,190 / 0.4 FTE / $56,286, via the fiscal packet's builder
included; the floor halved and the argument sharpened. **Conformed quote:** the Blackburn
preserved-law language now reads as its section-by-section summary actually reads — "does not
preempt any generally applicable law, including a body of common law" — in the half-statute
page, the census, and the federalism packet. **Hardened from primaries:** EO 14365 (number,
date, task force, funds lever), the SANDBOX text (two years renewable to ten; consumer actions
unwaivable), the GAAIA draft (development-only, three-year sunset, general-applicability
preservation — and every Title I signature the draft requires belongs to the IVO's audit
partner, § 112(e)(8), none to a developer's officer); three dated-record ⚠ marks retire. **The
written record:** the five Serial 119-31 statements land — Thierer's written testimony carries
no carve-out (the concession lives in the transcript alone, and the dossier now says so);
Schneier's "no knowing who … controls what" and Miller's "little to no consequences … few
incentives" enter known objections as the government's own witnesses stating the doctrine's
premise. **Donor notes:** the Apollo internal-deployment primer to OPEN QUESTIONS 2 and 4; New
York's § 740 notice to CURE 17. **Watch:** the Colorado note discloses a district-court order
barring the Attorney General from initiating enforcement (X.AI LLC v. Weiser) — the first
judicial constraint on a state AI enforcer in this record; order queued. The verification
record carries every read; the library index carries every rename.

**Between versions — 24 August 2026, the evening retrievals — three gates, opened by the
maintainer's own hand.** No change to any tagged text. The maintainer pulled band A of the new
retrieval list the same evening it was written, and the reads land: **OPEN QUESTION 1 is
resolved** — Connecticut's P.A. 26-15, read in full, adopts the frontier definitions (10²⁶;
the $500M tier) but attaches only a whistleblower-channel duty to frontier developers, so
there is no due-care corpus to freeze and three interim standards stand; **CURE 19's gate is
discharged** — Tennessee's Public Chapter 781 in hand and quoted verbatim, a personhood-denial
act enacted "the public welfare requiring it"; and **the Colorado delay is verified at the
primary** — SB 25B-004's final fiscal note states the move from 1 February to 30 June 2026,
and prices the delay at zero, which becomes the fiscal note's § 6c. The read's best collateral
find gets its own section on the half-statute page: Connecticut enacted the inoculation
pattern's inverse — verification evidence inadmissible in AG enforcement, "nor shall it give
rise to any … defense" (§ 33(e)) — while the bill carrying a true NIST defense appears to have
died ⚠ (inference; status check queued). One state examined the chosen stick and legislated
against it; CURE 20 is this Act's version of that answer. The dated record gains 8 April 2026;
the reviewer page's OQ1 row moves from parked to resolved within the logged exemption's
bounds; the shelf and read-statuses are current.

**Between versions — 24 August 2026 — the reviewer page made current for the wave (logged
freeze exemption, second and final).** Factual currency only, before eleven follow-ups point at
the page: the errata description reads twenty-two entries reaching E35; the state of play gains
rows for CUREs 20 and 21 and its tally becomes thirty-one; OPEN QUESTION 1's row records the
24 August parking (no decision until the Connecticut act is read); CURE 19's row records the
wording ruling (Idaho's text tracked, Tennessee cited). The ask, the terms, the lane tables'
substance, and everything the engaged reviewer holds remain untouched; the structural wiring
still waits at the freeze door.

**Between versions — 24 August 2026 — the menus audited: no reviewer does the project's
homework.** No change to any tagged text. Every packet's question menu was tested against one
rule — a question a reviewer's seat is asked to answer must not be answerable by easy research
or by files the project already holds. Five menus passed whole (the criminal packet untouched
under review; enforcement, security, proportionality, torts/design clean). Two questions failed
and are rephrased through their builders and regenerated: the fiscal comparator question no
longer asks the seat to locate the sibling states' fiscal notes — locating them is the
project's own retrieval job, now queued — and asks instead which of a civil disclosure regime's
costing assumptions would not transfer to a criminal-enforcement act; and the federalism
live-litigation row becomes a real question — which of SEC. 13(c)(2)'s directions fails first
on the monitored cases' strongest preemption reading, and does the drafted valve save it.

**Between versions — 24 August 2026 — the seventh packet: torts and design, the boundary
lane.** No change to any tagged text. The lane the sweep never swept gets its packet: criminal
beside civil with neither collapsing into the other; the SEC. 7(b) insurance bar walked valve by
valve (the defence-costs clawback, the restitution carve-out's settlement gradient, the
criminalised indemnity contract); the harm tier's intervening-cause clause put to the tort
question of whether SEC. 2(a)'s own foreseeability drafted it out of work; the deployer reliance
path measured against what products law learned; and the civil-only alternative presented at
full strength from the project's own shelf, citizen suits included. Builder committed with it;
round-trip verified. The shelf stands at seven — every lane but the gated open-source seat now
has its paper path — and the reviewer page's counts follow in the same commit, within the logged
freeze exemption's factual-currency bounds.

**Between versions — 24 August 2026 — the reviewer page catches up with its own shelf (logged
freeze exemption).** The reviewer surfaces are frozen until the criminal-law call; this entry
records the one exemption taken, and its bounds: two factual-currency edits to REVIEWERS.md,
neither touching the ask, the terms, the lane tables, or anything the engaged reviewer holds.
The path gains, at its head, what it omitted: six lanes now have a single-page packet — the
path itself in printable form — with the sources winning wherever they differ. And the packet
paragraph goes from three lanes to six with links, noting plainly that the federalism and
proportionality packets serve question clusters the page routes through the existing seats.
The full wiring — packet pointer rows in each lane table, and the seat-structure decision the
new packets pose — waits at the freeze door as before.

**Between versions — 24 August 2026 — every packet gets its builder; the rule becomes
enforceable.** No change to any tagged text. The packets index promised "never edited by hand;
regenerated" while three rows said "builder to follow" — a rule and its violation on one page.
The fiscal, federalism, and proportionality packets now have committed builders that hold the
authored text as their template and emit it verbatim: edits are made in the builder and
regenerated, never in the page, so the rule is enforceable from this revision forward; the
builders state plainly that they are template-emitting and may be upgraded to
section-extraction in the criminal builder's manner. Round-trip verified before commit. The
index rows now name their builders.

**Between versions — 24 August 2026 — the sixth packet: proportionality and sentencing.** No
change to any tagged text. The lane's centre is presented as what it is — the statute's own held
question, READ FIRST item 4, the sentencing valve against fifty state proportionality clauses —
with the harm tier's borrowed federal geometry walked, the bracketed minimum's suspended-sentence
problem put plainly, the announced-maxima record offered as a grading question, and the
deterrence arithmetic carried ⚠ forecast-grade. CUREs 1 and 12 presented as verifiable repairs,
expressly not enacted. Assembled directly; builder to follow. The shelf stands at six of seven
lanes; torts/design remains, open-source gated.

**Between versions — 24 August 2026 — two more packets: the fiscal lane and the federalism
lane.** No change to any tagged text. The packet shelf goes from three lanes to five in one
day. Fiscal: the note's own rules enforced against it — the sweep's six findings put to the
seat unanswered on purpose, the Colorado floor as the genre's first real arithmetic, the
commencement postures costed, the forecasters' fine-absorption magnitudes carried ⚠
forecast-grade, and the CURE 7 sequencing recommendation put to the reviewer as an undecided
question. Federalism: the ceiling weather read as a negotiation, four general-applicability
reservations deep; SEC. 13's severance and suspension design with CURE 2's drafted valve
(proposal, not enacted); the SEC. 1(c) nexus against the dormant Commerce Clause; and the
lane's charge stated plainly — the whole repository's posture rests on the carve-out holding,
so refuting it would be the most valuable disposition the lane can produce. Both packets carry
the new cross-lane section — how the seats interrelate, the maintainer's bounded role, and the
anonymous correction doors — which the earlier three packets gain at their next regeneration.
Both were assembled directly; builders follow, and the regeneration rule applies from each
packet's next revision. Reviewer surfaces stay frozen; wiring into REVIEWERS lane tables joins
the freeze-lift batch.

**Between versions — 24 August 2026 — the officer word, conformed (E35).** No change to any
tagged text. Three files called the source of the 8 August admissions "a senior officer of the
developer"; his role is head of strategic futures — the advice layer the front page itself
excludes, and not an officer under the Act's own test. Conformed in all three to "the
developer's head of strategic futures"; the register entry (E35) records the failure mode — a
defined term loosened toward the rhetoric — and the sharpened rule: defined terms are never
used in project prose more loosely than their definition. The accurate label is also the
stronger exhibit: candour came from the layer the Act would not reach, silence from the layer
it would.

**Between versions — 24 August 2026 — nine standing decisions ruled, in one sitting.** No change
to any tagged text. The maintainer's owed-decision list is cleared: **CURE 20** (the chosen-stick
clause) and **CURE 21** (the certification register) enter the open queue, transplanted verbatim
from pre-review findings PF-2 and PF-3, which now carry their resolutions; **PF-6** records that
the leaky-trigger critique is answered by the Act's existing multi-route coverage; the SEC. 3
administrability companion note is ruled in, held for the v3.5 companion; **CURE 7** is formally
held for the enforcement and security seats; **CURE 19** will track Idaho's retrieved text with
Tennessee cited, not borrowed; **OPEN QUESTION 1** is parked pending the Connecticut read;
**E34** numbers the Lyness three-of-four precision the comparative page has carried since its
own addendum; the first-name in commit b6fbc0a is ruled accepted-and-logged — history is not
rewritten in this repository, including for the maintainer's own convenience; and the nav and
legacy-file questions are deferred into the coming reorganisation plan, one architecture
decision instead of two.

**Between versions — 24 August 2026 — the dispositions register opens, empty on purpose.** No
change to any tagged text. `dispositions/README.md` fixes the rules of publication before the
first review concludes, so no outcome can bend them: dispositions published as written and in
full, hostile included; dated, version-pinned, and scoped; attribution the reviewer's election,
with named seats requiring attributable dispositions; the maintainer's response separate and
labelled; nothing deleted. The register links from the reviewer surfaces when the current
freeze lifts.

**Between versions — 24 August 2026 — the register lands, through the preview gate.** No change
to any tagged text, fact, or row; two stylesheet files and one meta tag. The reading surface
goes from screen-white to paper under warm near-black ink; the body text moves to the serif of
the law reports (system faces only — no webfont requests); the accent comes home from spruce to
the law-report maroon it was chosen as the complement of; the sidebar becomes a cream apparatus
margin with the reading order numbered §1–§10 and a maroon rail on the current page; every page
title carries the reports' double rule; table headers take a small-caps sans over a firm ink
rule; the repository link is dressed as the stamp it is. Unlike the reverted attempt earlier
today, this change shipped only after rendered previews of the compiled stylesheet were
approved by the maintainer, per the runbook's new rule; the stylesheet compiles clean against
the pinned theme, verified before commit. No README markup, nothing the repository landing page
can mangle. Twelve rows untouched in both stated places; nav remains the ten exact paths; the
theme stays pinned.

**Between versions — 24 August 2026, tenth intake — the cross-cascade: what the two readings
change everywhere else.** No change to any tagged text. Five argument files now carry what the
paired-primary readings established, each as a link to the owning page rather than a restated
fact. Known objections: the compute-trigger rows gain the both-ends administrability answer and
fold the forecasters' unit-blur caution into the case *for* the designation routes; a new
objection is added and answered — "the timelines make this pointless" — with the asymmetry
argument (fast timelines shorten the window, not the need for the drawer). Paths to enactment:
the whole-cloth section's window claim gains the forecasters' arithmetic as its citation, and
the existing-law vehicle gains the federal roadmap's own endorsement of applying existing law
through evaluations. The half-statute page's ceiling section records the executive's fourth
reservation — the funding lever and the "prudent laws" sentence in one paragraph. Comparative
officer liability § 5 notes that the 2025 roadmap cites § 7413's own statute as permitting
paperwork. Why a signature works gains a two-corroboration addendum: the forecasters' fine-
absorption magnitudes, and Washington's "rather than relying on voluntary attestation." One
owner per fact throughout: two visions and the forecasters' arithmetic own the quotes and
numbers; everything else points.

**Between versions — 24 August 2026, ninth intake — two visions, read as paired primaries.** No
change to any tagged text. The Action Plan primary (*Winning the Race*, 23 July 2025) is read in
full and its verification row flips; the new page `docs/two_visions.md` reads it beside the AI
Futures corpus on the repository's established paired-primary method. What the pairing yields,
each leg sourced: the race document and the halt document both treat frontier-scale compute as
countable and locatable (chip location-verification as live federal policy; the forecasters'
declaration-and-audit engineering) — the administrability answer to the trigger objection,
arriving from both ends of the politics; both expect incidents and build for them; both trust
evaluations as law's instrument, the Plan in terms that endorse applying *existing law* through
them; the Plan's biosecurity section concedes in Washington's own voice that voluntary
attestation without enforcement fails; and neither document — ninety federal actions on one
side, forty-seven thousand words on the other — ever asks a natural person at a frontier
developer to sign anything. The sharpest find is a footnote: the permitting section names the
Clean Air Act and CERCLA — the statutory family whose enforcement text codified "responsible
corporate officer" (42 U.S.C. § 7413(c)(6), owned at comparative § 5) — as regulations to
streamline for data-centre construction: doctrine's home statutes, cited as paperwork. Headwinds
recorded rather than rounded away: the funding lever against regulating states, the
FTC-liability review, the forecasters' missing state lane — beside the Plan's own reservation of
states' right "to pass prudent laws." The expanded timeline gains the 23 July row. The page
ends where the project's purpose is: what a reviewer should attack, and the one sentence a
sponsor could open with.

**Between versions — 24 August 2026, eighth intake — the forecasters' arithmetic; and a site
experiment reverted the same afternoon.** No change to any tagged text. New research page:
`research/forecast_arithmetic.md` — the AI Futures Project corpus (the *AI 2040 / Plan A*
report, read in full; the AI Futures Model supplementary materials, key sections read) examined
against the Act. What the reading yields: their verification engineering treats training compute
as countable at declared thresholds — support that a FLOP-denominated trigger is administrable;
their forty-seven-thousand-word governance plan deploys bans, audits, safety cases, and
burden-shifting without once asking a named natural person to sign — the layer this Act
supplies, found missing by the field's own maximal designers; their timeline distributions (a
modal first-milestone year inside this decade, two-month gaps between late milestones) state the
drawer-and-window premise as arithmetic; and their economic projections price why entity fines
cannot deter. Their scenario material is marked ⚠ as scenario, their own epistemic caveats
quoted, and the readings that cut against the Act — no state-level frame, a leaky threshold,
their scepticism of incrementalism — are recorded whole. Instruments shelved at the verification
record. Separately, the record of the afternoon: a site-register redesign (`86422c0` — paper and
ink, dark sidebar, a front-page status panel) was committed, pushed, and reverted within the
hour (`729fdc4`), after the panel's classed HTML rendered as run-together text on the repository
landing page and the unannounced change read as breakage on the live site. The stylesheet itself
compiled clean — verified after the fact against the pinned theme — so the failure recorded here
is one of process, not code: visual changes now reach the live site only through an approved
preview, under a rule added to the private runbook. Nothing is deleted; both commits stand in
history, and this entry is their account.

**Between versions — 24 August 2026, seventh intake — the whole-cloth world, and the runbook.** No change to any tagged text. The maintainer's objection to the enactment page — a whole drafted Act whose strategy page offered only partial vehicles — is accepted and answered in the page itself: a new first section, "The whole-cloth world — is it impossible?", states the observed record (every censused framework statute passed as a whole act), the precedent for the hard part (personal executive criminal liability enacted whole and fast in 2002, chronology flagged ⚠ for verification), the drawer-and-window pattern of American public-welfare law, and the real reason the council reviews the whole Act now: the window will not accommodate the review, so the review must precede the window. The four vehicles are reframed as pre-positioning, not substitutes. Tense corrected: Texas's and Colorado's framework acts are in force, not arriving. A consistency recheck ran clean (org-rename residue in the diary is historical and deliberately unrewritten; row-count claims consistent; the criminal packet is not staled by the CURE 16 addendum, which it does not carry). A private maintenance runbook now lives in the library: when X changes, update Y — cascades, freezes, site rules, bridge hygiene, and the pre-push grep ritual.

**Between versions — 24 August 2026, sixth intake — the examiner's bookshelf.** No change to any tagged text. The maintainer asked the supervisor's question — what is foundational to outsiders and missing here — and the answer is now a public file: `research/canon_check_2026-08-24.md`. The searches found the plumbing sound (the case spine, the Park-referral criteria, the deterrence economics, MPC § 7.06 engaged with limits disclosed) and the scholarly canon thin in named places: Sayre's *Public Welfare Offenses* — the article that coined the category on this Act's own title page — uncited; the corporate-punishment canon (Coffee's *No Soul to Damn*, Khanna 1996, Polinsky & Shavell 1993, Stone 1975) stating our premise without us citing it; MPC §§ 2.05 and 2.07(6) unengaged while the site borrows ALI's register; the RCO academic layer (Brickey, Abrams, Aagaard, Sepinwall) thin above a strong practitioner spine; the regulatory-theory shelf (Ayres & Braithwaite, Fisse & Braithwaite, Coglianese & Lazer) absent under a management-based design; the AI-governance canon (Anderljung et al., the compute-governance paper, the International AI Safety Report) absent from a project with *Frontier AI* in its name; and Husak's overcriminalization register unheld. House rule stated in the file and kept: nothing listed is cited anywhere until retrieved and read; entries leave the list only through the owning file with the reading's actual result. Retrievals queued at browser list item 15.

**Between versions — 24 August 2026, fifth intake — trust, vehicles, and the pre-review pass.** No change to any tagged text. Three additions at the maintainer's direction. The half-statute page gains **the affirmative frame** — personal liability as the industry's missing trust infrastructure (the record's own trust language; the § 1350 precedent SEC. 8 is expressly built on) — and its *Park* paragraph is corrected for precision against the Act's actual design: the standards section's element-and-due-care paragraph *satisfies* due care for documented conformity with the applicable standards, scoped to the matters conformed, own-framework-alone crediting nothing; the page now argues the real distinction (who chose the stick, and what it measures) rather than an imprecise one. The catch was ours and is logged as PF-1. New page: **paths to enactment** — four vehicles measured against the record (the amendment/chassis route, with the Act's own interim-standards adoption as proof of graft-compatibility; the certification-first minimal bill; existing law applied, the *Dotterweich* route; the attorney-general route), preconditions, and the standing invitation to refute any of it in a disposition. New audit file: **the pre-review pass** (PF-1 through PF-5) — problems pre-found and repairs drafted for the reviewers, including two CURE candidates held for the maintainer's numbering: the chosen-stick clause (foreclosing a TRAIGA-style floor amendment) and the SEC. 8 certification register (facts public, content protected). Reviewer surfaces remain frozen; the pass links from them only after the criminal-law call.

**Between versions — 24 August 2026, fourth intake — the last transcript, and the inoculation pattern named.** No change to any tagged text. The June 2025 Oversight transcript (*The Federal Government in the Age of Artificial Intelligence*, Serial 119-31) is read in full and its verification rows flip from "Held; unread." What it lands: dossier § 5.3 — the moratorium fight recorded from inside the majority (the presiding chair's "pause for 10 years in federalism" and pledged no vote; a second majority member's "fix that in the U.S. Senate"; the markup record; the Massachusetts committee letter) with the pro-preemption witness's own concession that "laws of general applicability … also criminal activity" sit outside the clause; known objections' why-one-named-officer gains the record's directest moment — asked who oversees executive-branch AI, the witness answers "I do not believe there is one," and the questioner states the finding: the responsibility "is not in anyone's job description"; the census queue notes the third transcript and its procurement-register bills, none reaching an officer. And a new page joins the docs, at the maintainer's direction: **safe harbors, affirmative defenses, and the half-statute** — the inoculation pattern (TRAIGA's framework defense, Colorado's, the SANDBOX Act's waiver decade, Utah's learning lab, all ⚠ pending primaries) named and answered in advance, with the officer test and the five load-bearing elements any partial enactment of this Act would have to keep. Private trackers updated in step. Extended the same day, second sweep: the half-statute page
gains the ceiling variant (the 11 December 2025 preemption order's task force ⚠; the Blackburn
TRUMP AMERICA AI Act ⚠; the Obernolte–Trahan Great American AI Act discussion draft of 4 June
2026 ⚠ — ten years shrunk to three, and a third express general-law carve-out on the record),
the certified-systems false-accusation precedent (Horizon, Michigan, SafeRent — all as given in
Serial 119-31), the one-line answers block, and the corrected Colorado effective date (delayed;
amendment queued). The dated record gains five rows (5 Jun 2025; the SANDBOX introduction; the
preemption order; the framework-defence effective dates; the ceiling narrowing). The watch's
Grok thread gains its June 2025 link (the "not been approved for use" committee line). The
census queue takes both federal ceiling bills, verify-first. The glossary's *machine
intelligence* entry notes the register's arrival in a federal backronym.

**Between versions — 24 August 2026, third intake — the assistant objection, the freight words, and the dated record.** No change to any tagged text. Known objections gains "It shouldn't target AI companies" — the objection AI assistants generate for reviewers who ask one, decomposed into its four precise forms and answered from the Act's own architecture. The glossary's freight-words section gains *emergent — and "malicious, emergent"* (the technical sense honoured; the recorded pairing read closely: malice locates a mind in the system while emergence removes the person from the origin) and *machine intelligence* (register, not category), with a cross-reference from house language § 10b. The front page gains **The record, dated** — twelve rows, 1943 to the Casar deadline, each owned by the file it links — with the expanded, sourced version at the new `docs/timeline.md`. House language: a stray first name in § 10 replaced with "the maintainer" (privacy hygiene; the history question is logged, not hidden). Housekeeping: `.gitignore` added for `.DS_Store`.

**Between versions — 24 August 2026, second intake — the read-through lands.** No change to any
tagged text. Two congressional transcripts and a Congressional Record page, read in full, entered
at their owners: why-the-disparity gained its under-oath section (the asymmetry conceded by
Doshi; the CTA's compliance-removes-liability ask; Turner Lee's state-side answer); the known
objections' bloc block gained the March hearing's distillation record, with Anthropic's
*Detecting and Preventing Distillation Attacks* identified as the footnoted primary and queued
for retrieval; CURE 16 gained its second documented deception class (the distillation farms,
beside the AISI sockpuppets); the census queued five bills named in testimony, all to be verified
against congress.gov before rows are written; the standing watch gained the April 2025 Stansbury
continuity note; and the verification record's instruments table took read-statuses for the
transcripts while its shelf conformed to the library's new reference scheme — fixing, in the same
pass, its own duplicate Virginia row. The third transcript (the Age-of-AI hearing) is held,
unread, and says so in its row.

**Between versions — 24 August 2026, afternoon intake.** No change to any tagged text. The
standing watch took deadline-day status on the Casar–Khanna letter (no public response located),
the February Grok-classified-systems record (the DoD–xAI deal; the Ossoff-plus-five and Warren
letters, extracts held in the library), and a checked-and-bounded note that no "military weapon"
designation of any model exists. The fiscal note gained § 6b — Colorado's SB 26-189 fiscal note
(4 May 2026), the first state dollar figure for AI-act administration, attributed and bounded.
The private library was reorganised the same day under a prefixed reference scheme with an index;
the shelf manifest in the verification record updates to the new filenames in the next research
batch.

**Between versions — 24 August 2026, the reviewer surface.** No change to any tagged text. Two
passes, same day. First, format: the five lane briefs converted from prose to per-lane tables.
Second, workflow — built around the observation that a reviewer works from one place or not at
all: every drafted-response reference in the lane tables now links to its queue entry; each lane
table gained a row of the errata already filed in that lane (pointers into
[the register](./errata.md), never copies); the state-of-play table moved ahead of the filing
instructions, its row states conformed to its own legend, and it now names the companion's READ
FIRST table as the senior index — the four still-open READ FIRST items with no queue counterpart
entered as HELD rows, the cross-identities (item 6 = the open-source floor question; item 8 = the
security objectives question; item 11 = CURE 4's target) stated in place, and conforming the
companion's own table listed for the v3.5 landing. And the first single-page lane packet —
criminal law, at `packets/` — is assembled by committed script from the sweep, the queue, and the
register, so a reviewer can print one document and work from it; the sources remain the
authority. Third, the same evening: the bounded ask and the apparatus reconciled — the reviewer
page now states that the lane questions, held rows, and READ FIRST items are the *menu* the
three findings may be chosen from, not additional work; the queue's header gained a label
concordance mapping its working vocabulary onto the state-of-play states, and its HOLD block's
CURE 6/7 summaries were reduced to pointers at the ⚠ blocks inside the entries, which were
repeating them; and four instances of command-voice aimed at readers ("a reviewer should…")
were conformed to the project's stance that the path is offered, never assigned — on the front
page, the sweep's header, and the queue. Substance unchanged throughout. And a late
correction to the packet's own arithmetic: six questions and six drafted repairs beside an ask
for three findings read as contradiction, so the packet and the lane tables now state the rule in
their structure — the questions are a menu, any three items complete a disposition, and the full
form is now defined rather than gestured at — the menu worked through whole is the seat — and the
packet's ask regained the word "Unpaid," which the compression had dropped. And the rendered
mirror went live the same night — frontieraiaccountabilityproject.github.io/model-act, a committed
configuration, republishing itself on every push — with the front page now linking it;
the repository remains the authoritative record.

**Between versions — 23 August 2026, the research sweep.** No change to the tagged statute. The
day's intake entered at its owners: the enacted-family primary texts reached the shelf (CA SB 53,
IL P.A. 104-0538, CT P.A. 26-15, H.R. 8094, S. 1792 read in full); the escape-crime gallery
section landed ([the same conduct](../standards/the_same_conduct.md)) with the front page carrying
the developer's own "we accidentally made a weed"; the five limbs were mapped to the 2026 record;
the entity-based case entered the enterprise file; the AISI incident's member of the public gained
his public name; the enforcement record gained Pennsylvania and the docket identities; and the
codified officer — 33 U.S.C. § 1319(c)(6), 42 U.S.C. § 7413(c)(6) — entered
[the comparative file § 5](../standards/comparative_officer_liability.md). The queue took three
intake-derived entries (CUREs 17–19) and five addenda, all marked not maintainer-validated. The
census logged six verified tracker errors. Sources and read-statuses at
[the verification record § 6](../research/verification_record.md).

**Between versions — 22 August 2026, the enterprise pass.** Still no change to the tagged statute.
The scope architecture arrived in the apparatus: [CURE 7](../audit/v3_5_cure_language.md) drafts
the covered frontier enterprise into the queue — scope follows the ecosystem, duty follows the
function, wealth alone covers nobody — with exact splices into SEC. 1(b), SEC. 2(a), and SEC. 4,
advance designation of one responsible officer per covered function, and the auditor and evaluator
named into the non-shield list (part answer to Open Question 3). The evidence base entered as
[research/frontier_enterprises.md](../research/frontier_enterprises.md) (the twelve-company
coverage set, four layers, verbatim self-designations, ownership and control from public filings);
the public face as [docs/the_definition.md](../docs/the_definition.md) (the two definitions,
technical beside legal) and [docs/known_objections.md](../docs/known_objections.md) (the strongest
objections published with their answers, the sections that already answer them cited). The front
page was inverted around the two definitions, and the disclosure gained the funding line: not
seeking funding; any change disclosed before a penny is accepted.

**Between versions — 22 August 2026.** No change to the tagged statute (`model_act_v3_4.txt`
stands). Companion and apparatus only: the [v3.5 queue](../audit/v3_5_cure_language.md) settled
CURE 1's attribution to anonymous, gave CURE 4's anthropomorphism recast AI-native precedent from
the July–August incident record, and opened two new questions (a safeguards-disabled evaluation; the
third-party-evaluator gap); the [glossary](../standards/what_these_words_mean.md) gained a
legal/technical two-column view and a definition of *accountability*; the
[table of authorities](../standards/table_of_authorities.md) added *Moffatt v. Air Canada* and
Desai & Riedl as candidate authorities not yet cited; and the front-page contribution ask was recast
as three labelled doors; and, later the same day, the [frontier-models reference](../research/frontier_models.md)
was compiled from the Epoch AI dataset and paired with the developers' own *frontier* self-designations
(five labs by name, twelve companies by published framework, per METR), and
[CURE 6](../audit/v3_5_cure_language.md) proposed a third route into SEC. 1(b)(1) scope — a model its
developer holds out as frontier — with an anti-evasion clause and a deployer carve-out. Recorded here
because the register should show the apparatus moving between tagged versions, not only the versions.

## Repository restructure — 21 August 2026 (v3.4 statutory text unchanged)

**No change to `model_act_v3_4.txt`.** Its sha256 and the reviewer's-copy reproducibility chain are
untouched. This entry is packaging, apparatus and new research files only.

**Structure.**
- Front page split: 1,726 lines → ~600. The argument moved to `docs/the_case.md`,
  `docs/the_statute_translated.md` and `docs/questions.md`.
- `LEDGER.md` split: 1,128 lines → a 49-line index over `ledger/errata.md`, `ledger/changelog.md`
  and `ledger/diary.md`. The `#part-i`, `#part-ii` and `#part-iii` anchors are preserved on the
  index because they are cited in published material.
- `pages/` retired into `archive/page-images/`; all twenty images of the withdrawn v2, v3.2 and
  v3.3 typeset editions now sit in one place. `git mv` used, so history is preserved.
- `CHANGELOG.md`, `ERRATA.md` and `model_act_v3_3.txt` retitled at the root as explicit signposts.
  No link breakage.
- The nine retired `docs/` signposts re-pointed from README anchors to their new pages.
- Contents rebuilt as thirty-three single-line entries after a table and then a nested list both
  rendered badly.

**New files.**
`standards/the_same_conduct.md` · `standards/already_a_crime_for_you.md` ·
`standards/why_a_signature_works.md` · `standards/why_the_disparity.md` ·
`standards/what_these_words_mean.md` · `filings/who_actually_files.md` ·
`filings/frontier_ai_in_medicine.md`. `standards/commentary_sweep.md`, written 21 August, was filed
for the first time.

**Substantive amendments to existing files.**
- The central claim narrowed everywhere from *"no American law reaches a natural person"* to *"no
  American law places a duty on the officer of a covered frontier developer for the decision to
  release"* — the loose form being refutable. Five files.
- A scope block added to nine files stating who they are about and who they are not.
- `standards/house_language.md` extended with **§ 4 Register**, § 7 "Frontier" as a priced tier,
  § 8 the other frontiers, § 9 the grammar of the promise, § 10 the verbs; sections renumbered 1–11
  and all external cross-references re-pointed.
- `standards/interim_standards.md` records why Connecticut's SB 5 is not adopted at SEC. 3(c)(4).
- `audit/standing_watch_2026-08-20.md` § 7(5) restated from four frontier regimes to six.
- `audit/v3_5_cure_language.md` opens **Open Question 1** — whether SEC. 3(c)(4) should adopt
  Connecticut at v3.5. Held rather than decided; the tagged text is not edited.
- Campaign register replaced with legal register across nine files.
- The front page carries the model-act question below the Interpretive key, narrowed to the legal
  sense.

**Errata opened.** [E16](./errata.md) — a coverage failure; the standing watch missed Connecticut
SB 5, enacted twelve weeks earlier, and H.R. 9917, introduced four weeks earlier. Closed the same
day, with a correction to its own prescribed cure. [E17](./errata.md) — an overstated disanalogy
and a rationalisation described as a decision. Both cured.

---

*Moved 22 August 2026: this entry was written after the 19 August merge and sat inside the
sealed CHANGELOG.md block below, out of newest-first order. The sealed block now carries a
closing marker so the boundary of the verbatim content is visible.*

**v3.4 — 19 August 2026.** The sixteen findings of the adversarial review of 17–18
August, cured. Fifteen amendments entered the statute verbatim from the published queue
(`audit/v3_4_cure_language.md`); finding 4 (the harm tier) was already satisfied by
v3.3's own text and closes without amendment. Per cure: 1 → SEC. 2(b), deployer
reliance; 2 → SEC. 4(a)–(b), authority narrowed with express exclusions; 3 →
SEC. 3(c)(2)(B), (D), (5) and SEC. 8 conforming, validation and nonconformity reporting
separated; 5 → SEC. 6(b)(1) and 10(c)(2)(D), proximate cause; 6 → SEC. 7(b),
prospective insurance ban with restitution carved out; 7 → SEC. 8, the
no-chief-executive fallback; 8 → SEC. 3(b), the approval mode struck; 9 → SEC. 1(b)(1),
the interim lineage default and the decoupled audit floor; 10 → SEC. 1(b)(6), material
expansion self-operating; 11 → SEC. 1(b)(10), autonomous external-access capability
defined; 12 → SEC. 8, certification triggers and the quarterly cadence; 13 →
SEC. 5(e), privilege preserved; 14 → SEC. 9(a), the near-miss calibrated; 15 →
SEC. 12, the Attorney General as fallback recipient; 16 → SEC. 2(c), controlled
research deployment. The regulations shed their one paywalled incorporation, the
objectives restated per the published disposition. The companion gains notes
n.28–n.43, one per finding. Errata queue-lines carry their landed notes in Part I. The
statute grows from 506 to 611 lines; the v3.3 statute, jacket, and companion remain in
place, superseded. Tag gate, per the programme: every critical finding cured, or
conspicuously open with an owner and disposition in the companion's READ FIRST —
satisfied; the open items remain open as published. sha256 of the authoritative files
as tagged:
`model_act_v3_4.txt` 399c725adcd117aa7736a63b716328226eb24f33a48695115d941b68caace1bf ·
`model_act_v3_4_jacket_clean.txt` 9c59afae9fe34de83c03468498de37abbc90fb7f6df978e9ce03361a7ad7a733 ·
`model_act_v3_4_companion.md` 92d279044c19e67a6fbd314538601797c167ee274e5b02b717babab8e9d306f8 ·
`model_regulations_v1_draft.md` a96289777b63a705f7ff724aa8d7ce49f58dbbbffec907ec9c15804a60178319

**Checksum note, added 22 August 2026 — read this before running `sha256sum`.** Two of the four
hashes above no longer reproduce against the files in the repository, and the reason is presentation
rather than text. **The statute and the jacket still verify** — `model_act_v3_4.txt` and
`model_act_v3_4_jacket_clean.txt` return exactly the digests recorded above, which is the fact that
matters, because those two are the authoritative text. **The companion and the regulations do not**,
because both were modified after tagging: first by the repository-wide escaping of dollar signs
(`\$`, so that pairs of figures on one line render as money rather than as mathematical notation),
and the companion by later edits recorded in this file and the diary. Current digests, computed
22 August 2026:

`model_act_v3_4_companion.md` 7d919f5541de0778134a539b5ff847f81ab891c68b8354aaaeef0c299c148ada ·
`model_regulations_v1_draft.md` 40a2f424be47585c8d8cfe53b0a60e063c7fd1ff418494f8cd269a9bee1e98a1

The as-tagged digests are retained above and are not amended: they record the state at the v3.4 tag,
which is what a checksum in a changelog is for. The convention is the one
[the drafting record](../audit/record.md) already uses for its chunk heads — the checksum was taken
before the escape pass was applied. A reviewer verifying the tag should verify the statute and the
jacket; a reviewer verifying the companion or the regulations as they stand today should use the
22 August digests. Caught by the repository consistency audit; recorded here rather than in the
errata register because nothing published was false — the hashes were true when written, and a
changelog is a dated record.

<!-- BEGIN CHANGELOG.md · sha256:113b96eaca21 · merged 19 Aug 2026, content verbatim -->

# CHANGELOG — Model Act (Frontier AI Public Welfare Offenses)


## Citation & signpost patch — 18 August 2026 (v3.3 text unchanged; packaging and citability only)

- `model_act_v3_3.pdf` at the root replaced by a one-page **signpost** — the v2/v3.2
  practice, applied late. The withdrawn typeset edition still self-described as "the
  introducible text" from inside the tree: the last live instance of the retired word
  (ERRATA E7, outside catch). The typeset file is preserved unchanged at
  `archive/model_act_v3_3_withdrawn.pdf`, correction attached in the archive README.
- **Citability**: `CITATION.cff` added (entity author, CC0) and a "How to cite" section
  in the README (MHRA, Bluebook working form, APA); tag `v3.3` and the first tagged,
  checksummed release accompany this patch, so a citation can pin something that does
  not move. `main` remains the working branch.
- README: an academic lane added to the router — it leads with the errata register,
  which is the honest front door; "Read it here" retitled "The typeset edition
  (withdrawn)" so the heading matches its content; and the 1943 date re-homed from egg
  to food-and-drug executives (*Dotterweich* was a drug case; the eggs arrive in 2016
  and keep their sentence).
- `dossier/02_incident_timeline.md`: the spine's explicitly-written primary sources and
  Section D turned into live links — the source binder's down-payment, ahead of the full
  pass.

## Integrity patch — 17 August 2026 (v3.3 text unchanged; labels and packaging only)

- `ERRATA.md` opened: the six explainer/statute contradictions, line-specific, with the
  five/one split stated plainly — five resolved by statutory change queued for the working
  branch (engineer-exclusion text; certification cadence; nonconforming certification and
  deployment; the Agency-approval validation mode; deployer and startup reach) and one pure
  copy correction (commencement, corrected on the card today). Plus two precision notes
  (NY § 1427 phrased as severity-scaled caps; explainer numbering divergence logged).
- "Introducible" retired everywhere until a gated sponsor release earns it back.
  `model_act_v3_3_introducible.txt` renamed `model_act_v3_3_jacket_clean.txt` (same text,
  honest label); the old filename remains as a signpost for old links. v3.3 is relabelled
  a **research draft** in all live copy.
- `model_act_v3_3.pdf` **withdrawn** pending a reproducible rebuild from the authoritative
  source (tagged, checksummed, source-to-PDF fidelity test). The file stays in the tree for
  link integrity; the README no longer offers it.
- `archive/README.md` added: dated corrections now travel with archived versions
  (the pinned-correction rule).
- Threshold hygiene, after a primary-source pin run against enacted NY GBL art. 44-B
  (L.2026 c.96): "large frontier developer" is a \$500M gross-revenue test; § 1427 penalties
  are caps ("not to exceed," severity-scaled). No live copy asserted otherwise; logged so
  it stays that way.

## Repository — 17 August 2026 (v3.3 text unchanged)

- `model_act_v3_3_introducible.txt` — the jacket-clean copy of the Act: statutory text
  byte-identical to `model_act_v3_3.txt` SEC. 0–13; the header note, dedication line, and sigil
  replaced with a neutral drafting note and a CC0 notice. Cures F18 (audit chunk 7).
- Added `/docs` (plain-language explainers), `/dossier` (the sourced accountability dossier),
  `/audit/chunk7_hostile_brief.md` (the hostile brief), and the front-page router.

## v3.3 — 16 August 2026

Assembled at chunk 6 from the audit series (`/audit`, chunks 1–5 plus the field notes), applying
the drop-ins in the order chunk 5 §G directs. The single file of v3.2 splits in two:
`model_act_v3_3.txt` (the introducible text, SEC. 0–13) and `model_act_v3_3_companion.md` (open
items, drafting notes n.1–n.27, friendly proposals answered, the WHY page, the open cite-check).

**New sections.**
- SEC. 0 — findings and purpose, uncodified, drafted to the vocabulary of the federal savings
  clauses (chunk 2 §E.0).
- SEC. 13 — severability ladder with preservation of elements; conforming operation by published
  Attorney General's order; revival after a federal sunset or lapse. The cover's claim that "the
  criminal core is the remainder built to stand" is now operative text (chunk 2 §E.4, as amended
  chunks 3 §E.4 and 5 §E.5).
- SEC. 5(e) — records offense on the 21 U.S.C. § 331(e) two-limb pattern, demand power confined to
  this State; rated on the collision map and passed through the First and Fifth Amendment checks
  before drafting (chunk 5 §§D.5, E.3).

**Rebuilt sections.**
- SEC. 3(c) — three-layer commencement: the evidence layer (5(c)–(e), SEC. 9, SEC. 12 records)
  immediate; the substantive layer (SEC. 2, 5(a), SEC. 8) at day [180] on provisional validation
  against interim standards — the CA/NY/IL frontier-framework duties, legislatively adopted,
  static, pinned to a date certain, with reading rules stripping revenue screens, publication,
  third-party audit, and the sister states' enforcement machinery; the Agency layer (SEC. 3(b)
  modes; SEC. 5(b)) on promulgation + [90] days. The v3.2 pocket veto — the whole Act conditioned
  on its own agency's rulemaking — is gone (chunk 5 §§A.1, E.1, E.4).
- SEC. 10(c) — harm-tier geometry now 18 U.S.C. § 1365(a)'s: serious injury up to twenty years per
  offense; death, any term of years or life per offense (the § 841(b) inversion resolved
  structurally, not by footnote); concurrency default with findings-gated consecutive service;
  [forty]-year cap on consecutive determinate terms (the Kansas double rule); death/identity as
  jury elements; restitution decoupled into (c)(4), following the harm at every tier — the Jensen
  method made statutory (chunk 4 §§D, E.2).
- SEC. 7 — replaced: disgorgement with a rebuttable attribution presumption (permissive inference
  in criminal proceedings), restitution-first destination, express limitations tie, asset-freeze
  valve; the indemnification/insurance ban as three offences (enter, provide, benefit) with
  constructive trust; defence costs preserved against an undertaking to repay on a 6(b)(1)
  adjudication (chunk 3 §E.1).
- SEC. 6(b) — split: (b)(1) scienter prongs alone open the harm tier; (b)(2) recidivist prong
  (bare fact of a prior final conviction, Erlinger-proof, [ten]-year washout) elevates to 10(c)(1)
  only (chunk 4 §E.1).
- SEC. 12 — takes effect [90] days after enactment, commencement per SEC. 3(c); retention rebuilt
  to [ten] years from creation / [five] years after last in-state operation, whichever later, plus
  a litigation hold from notice; compensation records added; confidentiality made categorical for
  the documents while facts stay discoverable from any source; the limitations period keyed to
  offenses ("an offense to which SEC. 10(c)(2) applies") rather than a penalty schedule (chunks 2
  §E.3(c), 4 §E.3, 5 §E.4).

**Amended.**
- SEC. 1(c) — jurisdictional withdrawal provision; out-of-state conduct evidentiary only (chunk 2
  §E.1).
- SEC. 2 — "in or into this State"; the arising clause; the modifiability-evaluation compute floor
  (greater of [one] percent of lineage compute or [10^24] operations; interim default = the floor)
  (chunks 2 §E.2, 5 §E.2).
- SEC. 5(a) — "after the applicable commencement under SEC. 3(c)".
- SEC. 5(d) — narrowed to this State's own government; "or any regulator" struck (chunk 3 §E.5).
- SEC. 8 — facts-only certification, made to the Agency, not required to be published; offense
  reference conformed to 6(b)(1) (chunks 2 §E.3(a), 4 §E.4(a)).
- SEC. 9(c) — new: facts-known reporting rule; reports to the Agency, not published (chunk 2
  §E.3(b)).
- SEC. 10(a) — the enacted family's figures (\$[1,000,000], with the \$[3,000,000] recidivist step);
  10(b)–(c) fines pinned to § 3571(b) parity with twice-gross-gain alternatives; means
  consideration; 10(e) corporate payment of an individual penalty is itself a 7(b) violation;
  10(f) fund with survival clause (chunk 3 §E.2).
- SEC. 11(a) — fund reference to 10(f); awards survive the suspension of 10(a) (chunk 3 §E.3).

**Notes.** n.13–n.17 (preemption architecture, state criminal law, SEC. 13, First Amendment,
dormant commerce/spending) enter from chunk 2; n.18–n.20 (SEC. 7, calibration, SEC. 5(d)) from
chunk 3; n.21–n.23 (harm tier and valve, recidivist path, retention) from chunk 4; n.24–n.26
(commencement, modifiability floor, records offense) from chunk 5; n.27 (concordance to enacted
law) new at assembly, executing chunk 1 §§E.2 and E.10. Conforms: n.4 gains
decentralised-governance vehicles (field notes item 1 — naming, not redrafting); n.6 conformed to
the 6(b) split; n.7's NSW citation corrected to ss 272/272A in their proper roles (chunk 3 §A.1);
n.10's and n.19's § 841(b) passages superseded by n.21 (chunk 4 §§E.4(e)–(f)); n.21's two ⚠s
struck after chunk 5 pinned USSG § 5G1.2(d) and MPC § 7.06.

**Companion.** New "Friendly proposals, answered" section (field notes item 2): the kill-switch
answer — the Act does not regulate the button; it regulates the hand — and the DAO answer, by
conversion rather than correction. Placement instruction for adopting states moved into the
companion (chunk 2 §E.5). READ FIRST rewritten: items 3, 4 narrowed; 7 closed; 6 restated as a
review; 9 gains the pin-date and self-incrimination flags; item 11 (the SEC. 9(a) recast) added.

**Regulations.** Parts 5.5, 8.1, 8.4, and 10.1 conformed to the Act as amended (chunk 5 §E.6);
Part 3 deliberately not given an interim clause (chunk 5 §E.6(e)). Part 2 re-pin remains open
(READ FIRST item 1).

**Carried to v4.** The SEC. 9(a) recast of the two characterisation-shaped triggers, drafted
jointly with the regulations' evaluation Part, thresholds from the Agency (READ FIRST item 11);
the regs Part 2 re-pin (item 1); the consolidated cite-check (companion; item 10); the standing
watch, first act of any v4 chunk.

## v3.2 — August 2026

Baseline this changelog begins from. Single file: act (SEC. 1–12) + READ FIRST + drafting notes
n.1–n.12 + the WHY page. Full penalty architecture; regulations assembly draft v1 released
alongside.

## v2 — August 2026

Archived at `archive/model_act_v2.pdf`. The delta to v3.2 is what six days of drafting in public
looks like.


---

<a id="part-iii"></a>

<!-- END CHANGELOG.md · merged content ends here -->

---

*Corrections to the project contact; they enter [the errata register](./errata.md) with the fix attached and permanent credit.*

### 25 August 2026 — a federal definition worth having, and the verification problem measured

**H.R. 9333 read in full and entered.** The AI Flaw Reporting and Security Enhancement Act (Ross,
Hurd of Colorado, Beyer; introduced 18 June 2026; ordered reported 35–0 on 25 June) joins
[the census](../standards/frontier_bill_census.md) and
[the reporting page](../standards/who_has_to_tell_you.md), which now brackets the disclosure
question with three federal instruments rather than two. The GPO print's font encoding defeats
text extraction, so it was OCR'd and every quotation cross-checked against the govinfo bulk XML;
the artefacts corrected are named in the library reading note rather than hidden.

The find is § 2(e)(2): *"artificial intelligence flaw"* means conditions or behaviours allowing a
policy violation *"and which is not dependent on the presence of malicious intent or related
harm."* A federal statutory definition in which reportability turns on what the condition is —
carried unanimously out of committee — and the answer to the evidentiary problem
[§ 4a](../standards/who_has_to_tell_you.md) has been circling since it was written. **And the
census's finding holds in a new register:** the Act builds the national database and places the
duty to file into it on nobody.

**FLARE-AI read**, the reference implementation the field is building for that flow (Longpre, Zhu,
Ezell & Ghosh et al., arXiv:2606.31567, ICML 2026), with CERT, MITRE, AIID, Hugging Face, OECD and
several developers, after consulting 49 experts across 32 organisations. Its authors call flaw
reporting for AI *"decades behind"* software, and state their own limit: FLARE-AI is *"an ecosystem
coordination tool rather than a compliance reporting tool."* The infrastructure and the duty are
complements, and the people building the first say so.

**The verification premise, measured.** *Science*, 27 July: of 317 AI unicorns, more than half have
never published a paper on which one of their own researchers was first or last author; the top 5%
of firms hold over 90% of the citations; OpenAI, at roughly 4,500 staff, has eight researchers with
five or more. Entered at [the press corpus](../research/press_corpus_july_august_2026.md) § 5, ⚠
graded as reported from a preprint this project has not opened. And Emma Pierson's answer to the
acceleration objection — the race is not toward the capability the objection invokes — joins
Javorsky at [known objections](../docs/known_objections.md).

### 25 August 2026, second entry — the same author, the same absence, and a question nobody has answered

**The FOCUS Act read in full and entered.** Gounardes introduced it on 21 August; the drafting
commission print, 16298-02-6-1, is on the shelf and was read the same day the press entry was
written, which discharged that entry's own read gate rather than leaving it hanging. The word test
returns nil for *officer*, *director*, *executive*, *misdemeanor* and *felony*; the single
occurrence of *natural person* is a data-protection carve-out for the data subject; and both the
attestation and the § 39 knowing-violation standard attach to *"an educational technology
provider."* Row at [the census](../standards/frontier_bill_census.md), coverage at
[the press corpus](../research/press_corpus_july_august_2026.md) § 6.

**What is claimed from it is narrow.** An ed tech registry is entity-shaped work and a personal
criminal duty would be absurd inside it. The row records that the reflex is consistent, not that
the drafting is wrong.

**The donor of the harm tier gets its name and its bill.** 18 U.S.C. § 1365 was enacted by
Pub. L. 98-127 (13 Oct 1983), the **Federal Anti-Tampering Act**; the LII page and its notes are now
held as primaries rather than a single web read. Three findings entered at
[the table of authorities](../standards/table_of_authorities.md). The useful one: Congress swept
this section's four fixed dollar fines out in 1994 and replaced them with *"fined under this
title"*, routing to 18 U.S.C. § 3571 — **which is the choice n.19 already makes**, now supported by
Congress's own correction to the very statute this Act borrows from. Also recorded: the definitions
sat at (g)(3)-(4) until December 2002, so pre-2002 authority cites them under the old letter.

**And an open question, named at last.** The census has recorded for weeks *that* New York's
§ 1421(4) — the audit, the lead auditor's signature, the designation of senior personnel,
veil-piercing, officer whistleblower protection — was struck at the B amendment on 9 June 2025,
three days before passage and six days after it entered the bill. **It has never recorded why, because nobody has written it down.** That gap is now stated
in the file as an open item rather than left as an implication: if the provision was struck because
somebody made a good argument against it, that argument is the strongest objection to this Act's
central mechanism and it is currently unrecorded. It is being asked of the sponsors, and whatever
comes back is published as given.
