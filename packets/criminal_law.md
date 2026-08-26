# The criminal-law lane — one page

*A reading copy for the criminal-law seat, assembled 24 August 2026 by
`packets/build_criminal_packet.py` from [the in-house sweep](../audit/v3_5_lane_sweep.md),
[the drafting queue](../audit/v3_5_cure_language.md), and
[the errata register](../ledger/errata.md). Those files are the authority; this page exists so
the lane can be read, printed, and marked up as one document. If this page and a source differ,
the source is right and the difference is a defect worth reporting to
FrontierAIAccountabilityProject@proton.me.*

*Arrived here directly? Your lane's table, the terms of the seat, and the other packets are on
[the reviewer page](../REVIEWERS.md); the index of packets is [beside this one](./index.md).*

## The ask

One seat, one lane, scope in writing before work begins. Unpaid. **The floor:** the statute
straight through, then this packet, then **three findings, verified or refuted, with reasons** — a
complete and publishable disposition, perhaps six to eight hours. **The whole seat:** the menu
below worked through in full — every question answered, every drafted repair verified or refuted —
roughly ten to twenty hours across eight weeks. Both are dispositions; both are published as
written, including "approved with reservations," including hostile. **A disposition that refutes
one finding is worth more to this project than a full pass that agrees with everything.**

**The arithmetic:** everything below is the menu — six questions, six drafted repairs. Any three
items are a complete disposition; all of them are the seat done whole. One answered question is
one finding. One repair verified, or refuted, is one finding. A defect of your own discovery
outranks anything on the menu.

## Read first — the statute itself

The tagged text is not reproduced here. Read `model_act_v3_4.txt` at the repository root (print
copy: `archive/model_act_v3_4_reviewers_copy.pdf`). Your sections: **SEC. 1, 4, 5–6, and
10(b)–(c)**, with the v3.4 cures 2, 5, and 13 and the penalty and harm-tier chunks of
[the drafting record](../audit/record.md#chunk-3--penalty-architecture-for-v33-sec-7-rework-and-bracket-calibration) behind them.

---

## I. What the in-house sweep found in this lane

*Reproduced verbatim from [the sweep](../audit/v3_5_lane_sweep.md). All of it is contestable;
contesting it is the seat.*

### F1 — SEC. 6(a) has no predicate-violation element and no nexus element *(criminal law)*

The offense reads: a controlling person "who had a duty concerning the relevant risk **or** the
practical power to … correct a violation of SEC. 5, and who failed to exercise due care, commits an
offense." Walked as a prosecutor must plead it, three holes open: **nothing requires that a
violation of SEC. 5 ever occurred** (it appears only as the object of the power, never as a fact to
be proved); **nothing connects the failure of due care to anything** (unlike SEC. 10(c)(2)(D),
which supplies causation for the harm tier); and "**the relevant risk**" has no antecedent inside
SEC. 6 — its only antecedent is SEC. 2(a), which does not commence until day 180, while SEC. 6
operates from the effective date.

Where it loses: demurrer for failure to charge an offense. Or the court construes an offense into
existence and the defendant wins on vagueness, because "being a person with power who failed to
exercise due care" is standardless.

**This is the one finding where the *State* loses rather than the defendant.** Drafted replacement
text is in the lane's working notes; the shape is (1) practical power, (2) failure of due care in
its exercise, (3) *and that violation occurred*, with an express statement that the State need not
prove sole causation but must prove due care was among the measures that would reasonably have
prevented it.

**Criminal law.** SEC. 6(b)(2) attaches a felony to a bare violation with no fault element and no
requirement of controlling-person status — and because SEC. 5(a) deployment continues, the same
continuing deployment that produced the first conviction triggers it the next day. SEC. 5(d) is a
**strict-liability false-statement crime**: the note cites 18 U.S.C. § 1001, which requires
"knowingly and willfully," and the text drops both. SEC. 6(e) silently widens SEC. 4(a)'s carefully
narrowed "practical power" by adding "to detect" and "the conditions giving rise to it" — two
definitions of one phrase, and the offense uses the wider. SEC. 6(d) deletes *Park*'s defendant
production burden, which is not a constitutional defect but is the reason the offense would never be
charged. "The same class of risk" and the undistributed "knowingly" in SEC. 6(b)(1) are the two
gateway terms to a life sentence and both are undefined. And nothing in SEC. 6 says that a person
who took every measure within her authority *has* exercised due care — 6(e) answers the power half
and nothing answers the care half.

**And the objection the sweep could not raise against itself, supplied from outside it.** The
survey this project's comparative section is built on argues the opposite conclusion from the same
doctrine. Sean Lyness, *Revitalizing the State Environmental Responsible Corporate Officer
Doctrine*, 64 B.C. L. Rev. 253 (2023), would revive the responsible corporate officer doctrine in
the states for **"individual civil liability—and only civil liability."** His reason bears directly
on SEC. 6 and is not answered anywhere in the sections above: *Dotterweich* and *Park* are
**misdemeanor** authority, decided "during a time when the immediate and collateral consequences
were different" (at 297-98). A misdemeanor conviction in 1943 and in 1975 did not carry what a
conviction carries now — the collateral consequences, the licensing bars, the immigration
consequences, the sentencing exposure. So the argument is not that officers should escape; it is
that the authorities the Act leans on will not bear the weight the Act puts on them, because the
Act's felony tier asks a misdemeanor doctrine to justify a life-maximum offense.

**Why this is in the sweep and not only in the objections file.** It is the one criticism of this
lane made in print, by name, by the scholar whose own state-by-state survey the Act cites for its
comparative claims. The lane's honest position is that the base tier answers it and the felony tier
may not: *Park* holds at the misdemeanor floor, and the sweep says so two sections down. What the
sweep does **not** have is an argument that the same authority reaches SEC. 6(b). **That gap is a
finding waiting to be made or refuted, and it is the single most valuable thing a criminal-law
reviewer could take up.** It is question 7 on the menu.

---

## II. What has been drafted in response

*Reproduced verbatim from [the queue](../audit/v3_5_cure_language.md), grading intact:
sweep-derived and intake-derived entries are hypotheses, expressly not settled drafting, and the
intake-derived entries are additionally AI-assisted and not maintainer-validated. Each entry is a
candidate finding — verifying or refuting one is a complete finding for the disposition.*

## OPEN QUESTION 1 — SEC. 3(c)(4): does Connecticut become a fourth interim standard?

*Status (24 Aug 2026, maintainer): **parked by decision** — no ruling until the Connecticut act
is retrieved and read (retrieval list). Working default: three interim standards suffice; the
read confirms or overturns it.*

*Resolved (24 Aug 2026, evening, under the same ruling's terms): the retrieval and read are
done. Connecticut's enacted act — P.A. 26-15 (2026) — adopts the frontier definitions (the 10²⁶
operations line; the five-hundred-million-dollar revenue tier) but attaches to frontier
developers only a whistleblower-channel duty (its § 2). It carries no due-care corpus a frozen
interim standard could adopt. **Three interim standards stand.** Collateral finds land at their
owners: the § 33(e) anti-defense clause (the half-statute page); the officer-knowledge quarterly
report (already owned by the census); the failed S.B. 2's NIST defense (⚠ inference from the
bill file and analysis; enactment-status check queued).*

*Opened 21 August 2026 by [E16](../ledger/errata.md). **Not a cure — a drafting decision**, held
here rather than made silently, because it changes the tagged statutory text and
[E10](../ledger/errata.md) forbids editing a tagged file outside a revision.*

**The fact.** Connecticut SB 5 was enacted 27 May 2026. It uses this Act's own threshold —
computing power greater than 10²⁶ integer or floating-point operations — with a "large frontier
developer" tier at \$500,000,000 in annual gross revenue. SEC. 3(c)(4) currently adopts three
enacted state laws. There are four.

**The argument for adopting it.** SEC. 3(c)(4) is drafted to track the enacted family, and a fourth
member of that family now exists on an identical threshold. Omitting it invites the reasonable
question why, and a reader who finds the omission before the file explains it will assume the
project did not know — which, until 21 August, was true.

**The argument against.** Connecticut's frontier provision is **not the same kind of duty**. The
three adopted standards impose safety-framework obligations on the developer. Connecticut's
operative requirement is an internal reporting channel: anonymous employee reports of catastrophic
risk that *"shall be shared with the officers and directors of the large frontier developer at
least quarterly,"* with a carve-out withholding a report from an officer it accuses — and **no duty
of any kind attaching to those officers.** Adopting it as an interim *standard* would import a
whistleblower mechanism into a slot built for framework duties, and SEC. 9 and SEC. 11 already
cover reporting and whistleblower protection from a different direction.

**The third option, which may be the right one.** Adopt nothing, and instead cite Connecticut in
the companion as the closest any legislature has come to the vacancy this Act fills — a statute
that puts catastrophic-risk information into named officers' hands quarterly and asks nothing of
them. **That is worth more to this project as an exhibit than as an adopted standard.**

**What is already done, pending the decision.** The absence is now explained where a reader will
look for it, at [the adopted texts](../standards/interim_standards.md), so it reads as a decision
rather than a gap. The full row is at [the bill census](../standards/frontier_bill_census.md).

**Status: open. Decision owed at v3.5. Do not edit the tagged v3.4 text.**

---

## CURE 1 — "Serious injury" source moves to 18 U.S.C. § 1365(h)(3)–(4)

*Resolves READ FIRST item 3(b) (companion): the harm tier's injury definition leaves
21 C.F.R. § 803.3(w), a reporting-regime definition, for the criminal definition of the
Federal Anti-Tampering Act, Pub. L. 98-127 (1983) — the same donor statute whose
§ 1365(a) geometry SEC. 10(c) already borrows, so tier and trigger now travel together.
Answered from outside by a criminal-law scholar; the reviewer did not elect named
attribution when asked on follow-up, so under the standing rule the attribution is
**anonymous** and settled. Ledger, 20 August 2026; attribution closed 22 August 2026.*

**Operation 1 — the definition.**

**ANCHOR (SEC. 1, definition (8)):** "(8) \"Serious injury\": an injury or illness that is
life-threatening, results in permanent impairment of a body function or permanent damage
to a body structure, or necessitates medical or surgical intervention to preclude such
permanent impairment or damage; \"permanent\" means irreversible, excluding trivial
impairment or damage, per 21 C.F.R. § 803.3(w)."

**NEW TEXT — definition (8), in full:**

> (8) "Serious bodily injury": bodily injury which involves (A) a substantial risk of
> death; (B) extreme physical pain; (C) protracted and obvious disfigurement; or
> (D) protracted loss or impairment of the function of a bodily member, organ, or mental
> faculty. "Bodily injury" means (A) a cut, abrasion, bruise, burn, or disfigurement;
> (B) physical pain; (C) illness; (D) impairment of the function of a bodily member,
> organ, or mental faculty; or (E) any other injury to the body, no matter how temporary.
> Per 18 U.S.C. § 1365(h)(3)–(4).

**Operation 2 — the rename cascade.** Every operative "serious injury" becomes "serious
bodily injury," so the construed phrase matches its four decades of case law. Seven
touch-points: SEC. 0(a)(2) (findings); SEC. 6(b) (harm-tier element); SEC. 9 (incident
definition; 24-hour imminent-risk clock); SEC. 10(c)(2) and its causation paragraph;
SEC. 10(c)(4) (restitution); SEC. 11 emergency suspension.

**Operation 3 — the regulations conform.** `model_regulations_v1_draft.md` Part 1.5 defines
"Serious injury" by cross-reference to SEC. 1(b)(8) "(21 C.F.R. § 803.3(w) pattern)"; the
parenthetical becomes wrong the moment Operation 1 lands. Strike it and read: *1.5 "Serious
bodily injury": as defined in SEC. 1(b)(8) of the Act (18 U.S.C. § 1365(h)(3)–(4) pattern).*
The regulations track the Act's defined term; they never restate it.

**Held open — one design note, now answered by the sweep: NO.** The question was whether the
SEC. 9 *reporting* trigger should keep broader language (report widely on the (h)(4) base; convict
precisely on (h)(3)) while the SEC. 10(c) *element* takes (h)(3) alone. **The criminal-law lane of
[the sweep](../audit/v3_5_lane_sweep.md) rejects the framing:** it assumes the reporting side is the safe
place for breadth, and in this Act it is not. SEC. 5(c) makes failure to report a prohibited act;
SEC. 6(a) attaches a custodial offense to a due-care failure as to it; both operate from the
effective date. Widening the SEC. 9 trigger therefore widens a crime punishable by imprisonment,
and (h)(4) reaches "a cut, abrasion, bruise … or any other injury to the body, no matter how
temporary." **Use (h)(3) for both.** If earlier warning is wanted, take it from an objective
observable with its own donor — an injury requiring medical treatment beyond first aid, within the
meaning of 29 C.F.R. § 1904.7(b)(5) — which is a fact rather than a characterization, and so keeps
faith with SEC. 9(c) and n.16.

**One further amendment the sweep requires.** Most state penal codes already define "serious bodily
injury" or "serious physical injury" differently, and the companion directs codification among the
offenses against the person. Two definitions of one term in one code is a construction trap
resolved against the State. Either use a statute-unique term — *covered serious bodily injury* — or
add: *"This definition governs this Act notwithstanding any other definition of the same or a
similar term in the law of this State."*

**Still open:** READ FIRST 3(c), the bracketed [two]-year minimum. The sweep finds the *number*
defensible — it attaches only to a knowing or willful violation that proximately causes death, and
is the lowest figure in its donor neighbourhood — but finds it **cosmetic without a non-suspension
clause**, because in most states a "minimum" is satisfied by a suspended sentence with probation
unless the statute says otherwise. It also collides with the state's own homicide grid with no
priority rule. Both need a criminal-law seat.

**Administrative load:** none. Definitional substitution only.

**Substantive note for the changelog.** Prong (D) reaches protracted impairment of a
*mental* faculty — coverage the § 803.3(w) body-function language never cleanly gave,
and the coverage an AI statute needs, arriving pre-litigated.

---

### ⚠ Addendum to CURE 1, 23 August 2026 — the operative definition's blind spot, mapped; what Operation 1 already closes; the residue

*Found outside the lanes, reading the definitions in order. Filed here rather than as a new open
question because the queue already holds most of the answer.*

**The blind spot in the operative text.** SEC. 1(b)(8) as tagged imports 21 C.F.R. § 803.3(w) — a
medical-device reporting definition, and an entirely somatic one: "body function," "body
structure," medical or surgical intervention. Walked through the Act, three consequences follow.
A person driven into psychiatric crisis by a covered system suffers no "serious injury" anywhere in
the operative text. It is therefore not a reportable incident: SEC. 9(a) lists "death or serious
injury materially caused by a covered system" (string occurs once), and psychological harm short of
death never enters the list — no 72-hour clock, no report, no record. And death enters only through
"materially caused" — the hardest element in precisely these cases — into a report that SEC. 9(c)
provides "is not required to be published."

**What Operation 1 already closes — and this addendum exists to say so before anyone files the
blind spot as a new defect.** The § 1365(h)(3)–(4) donor is not somatic. Under (h)(4)(D),
impairment of the function of a **mental faculty** is "bodily injury"; under (h)(3)(D), protracted
impairment of a mental faculty is **serious** bodily injury; and (h)(3)(A)'s substantial risk of
death reaches the life-threatening psychiatric emergency. Operation 2's rename cascade then carries
that limb into the SEC. 9 incident definition and the SEC. 10(c)(2) harm tier automatically. Four
decades of construction of the same words travel with it. The 22 August email raising this finding
with a plaintiff-side reader described the operative text accurately and this queue incompletely;
recorded here so the record is straight.

**The residue, stated so it is not mistaken for accident.** Three things stay true after CURE 1
lands. (1) Acute, non-protracted psychological harm without substantial risk of death remains
outside "serious bodily injury" — and the sweep's own ruling in this entry (use (h)(3) for both;
(h)(4) breadth widens a custodial offense) makes that a **choice**, not an oversight. The lever a
state wants for earlier warning is already named above: the 29 C.F.R. § 1904.7(b)(5) observable,
not a wider injury term. (2) Causation. "Materially caused" is where these cases are actually
fought — the live Florida record (see
[the state enforcement record](../research/state_enforcement_record_2026.md) § 1) is a criminal
investigation built on chat logs. Evidentiary, for the criminal-law lane; no drafted response.
(3) Even fully cured, every report runs to the Agency and SEC. 9(c) keeps it unpublished; no duty
anywhere in the Act tells an injured **person** anything. CURE 14's notice duty runs to persons
whose *systems* were accessed, not persons *injured*. Whether an injured-person notice belongs in a
public-welfare statute — or belongs to tort, discovery, and the enforcement record's FDUTPA lane —
is a design question for the plaintiff-side perspective and the legislative-sponsor audience, held
open here, undrafted.

**Administrative load:** none — this addendum drafts no operation; it maps consequences of the
operative text, records what CURE 1 already resolves, and holds one question open.

## CURE 8 — SEC. 6: the individual-liability offense, reconstructed

*Opened 22 August 2026 by [the lane sweep](../audit/v3_5_lane_sweep.md), criminal-law lane, from findings
graded **fatal**. **Sweep-derived language, not maintainer-drafted** — it has not been through the
scrutiny the v3.4 cures received, and it is published in that state deliberately. This is the most
important entry in the queue after OPEN QUESTION 4, because it repairs the offense the whole Act
exists to create.*

**The defect.** SEC. 6(a) cannot be pleaded. Walked as a prosecutor must plead it: nothing in the
subsection requires that **a violation of SEC. 5 ever occurred** — it appears only as the object of
the power, never as a fact to be proved, and the duty prong does not mention SEC. 5 at all. Nothing
**connects the failure of due care to anything**; unlike SEC. 10(c)(2)(D), which supplies causation
for the harm tier, "failed to exercise due care" floats free of any referent. And "**the relevant
risk**" has no antecedent inside SEC. 6 — its only antecedent is SEC. 2(a), which does not commence
until provisional commencement, while SEC. 6 operates from the effective date. Outcome: demurrer
granted for failure to charge an offense; or the court constructs an offense and the defendant wins
on vagueness, because "being a person with power who failed to exercise due care" is standardless.

**Operation 1 — the offense.**

**ANCHOR (SEC. 6(a), verbatim):** "A controlling person who had a duty concerning the
relevant risk or the practical power to detect, prevent, halt, restrict, or correct a violation of
SEC. 5, and who failed to exercise due care, commits an offense."

**NEW TEXT:**

> A person commits an offense who, being a controlling person as to a covered system, (1) had, by
> reason of that person's authority, the practical power to detect, prevent, halt, restrict, or
> correct a violation of SEC. 5 concerning that system or the conditions giving rise to it;
> (2) failed to exercise due care in the exercise of that authority; and (3) that violation of
> SEC. 5 occurred. The prosecution need not prove that the person's failure was the sole or
> principal cause of the violation; it must prove that the exercise of due care by the person was
> among the measures that would reasonably have prevented or corrected it.

The third clause states *Park*'s prima-facie theory as an element and restores the missing nexus
without importing a but-for requirement the base tier cannot bear.

**Operation 2 — the converse, which nothing in the Act currently supplies.** SEC. 6(e) says power
exists even where the person "could not have acted alone or instantly." Nothing says that a person
who took every measure within her authority **has** exercised due care. Without it, "she had the
power, with others, and it happened anyway" is a coherent closing argument — which is the collapse
of due care into strict liability that the *Park* dissent called "a virtual nullity."

**NEW TEXT — appended to SEC. 6(a):**

> A person who took the measures a reasonably prudent controlling person in like circumstances
> would have taken within the authority that person held has exercised due care, notwithstanding
> that the violation occurred or that other persons declined to act.

**Operation 3 — due care as an element, not a sentencing gate.**

**ANCHOR (SEC. 6(c), verbatim):** "No custodial sentence may be imposed absent proof of at least
the failure of due care described in subsection (a)."

**NEW TEXT:**

> The failure of due care described in subsection (a) is an element of every offense under this Act
> that carries a term of imprisonment, to be charged and found by the trier of fact beyond a
> reasonable doubt.

*Why:* as drafted, the fact that raises a sentence from non-custodial to custodial is a sentencing
gate rather than an element, which is the *Alleyne* / *Apprendi* problem. SEC. 10(c)(2)(D) already
does this correctly for the harm tier and SEC. 6(c) does not.

**Operation 4 — restore *Park*'s burden structure.** The companion at n.6 asserts that SEC. 6(d)
"is *Park* itself." The text says something different, and a defense-friendly court will read
"Genuine absence of power negates the element; it is not an affirmative defense" to mean the
defendant need produce nothing. Pre-indictment the State cannot see the delegation memoranda or the
reserved-matters schedule; against a structured defense it simply does not indict. **This is not a
constitutional defect. It is the reason the offense would never be charged.**

**✅ Verified 25 August 2026, and *Park* is more specific than this cure assumed.** Read at 672–73:
a claim that a defendant was "powerless" to prevent or correct the violation is "raised defensively
at a trial on the merits"; "the defendant has the burden of coming forward with evidence, but this
does not alter the Government's ultimate burden of proving beyond a reasonable doubt the defendant's
guilt, **including his power**, in light of the duty imposed by the Act, to prevent or correct the
prohibited condition." **That is the two-burden structure this operation proposes, in the Supreme
Court's own words** — production on the defendant, persuasion on the State, and power expressly
among the elements the State must prove. The sweep's finding that SEC. 6(d) deletes it stands, and
now stands on the opinion rather than on the companion's summary of it.

**NEW TEXT — appended to SEC. 6(d):**

> Evidence that the person, by reason of position, ownership, or authority, had responsibility and
> authority either to prevent the violation in the first instance or promptly to correct it, and did
> not do so, is sufficient to warrant a finding of practical power. A person contending that the
> measures required were objectively impossible, or beyond that person's authority, bears the burden
> of producing evidence of that fact; the prosecution retains the burden of persuasion on the
> element beyond a reasonable doubt.

**Operation 5 — conform SEC. 6(e) to SEC. 4(a).** SEC. 4(a) excludes "access to systems, weights, or
infrastructure" and closes "Authority under this section is the authority to decide, not the
capacity to act." SEC. 6(e) then defines the element to include "**to detect**" and "**or the
conditions giving rise to it**" — capacity, not decision. One phrase, two contents, and the section
supplying the element uses the wider. The SRE with production observability and the finance VP who
approved the compute invoice both qualify.

**ANCHOR (SEC. 6(e), verbatim):** "A person has practical power if, by reason of position,
ownership, or authority, the person had the ability and opportunity, alone or with others, to
detect, prevent, halt, restrict, or correct the violation or the conditions giving rise to it."

**NEW TEXT:**

> A person has practical power if, by reason of the authority described in SEC. 4(a), the person had
> the ability and opportunity, alone or in concert with others, to prevent, halt, restrict, or
> correct the violation, or to require that it be detected or corrected by others. Capacity to act
> without authority to decide is not practical power.

**Held open.** SEC. 6(b)(2)'s recidivism felony has no fault element and no requirement of
controlling-person status, and because SEC. 5(a) deployment continues, the same continuing
deployment that produced the first conviction triggers it the next day. SEC. 6(b)(1)'s "same class
of risk" and its undistributed "knowingly" are the two gateway terms to a life sentence and both are
undefined. The sweep drafted language for each; both need a criminal-law seat before they enter this
queue as operations.

**Administrative load:** none. Element restructuring only.

---

*The knowledge-element repair to the above, opened 25 August after a vocabulary audit found
the case law this lane was missing:*

## CURE 22 — SEC. 6(b): the felony tier's knowledge element, and one word that is not American

*Opened 25 August 2026, not from a lane seat but from a vocabulary audit: the library's
lawyer-written documents were n-grammed against all 102 files here, and a case name that every
criminal-law reviewer would reach for came back **zero**. The method is recorded in
[the diary](../ledger/diary.md). Treat this entry as sweep-grade, not maintainer-drafted.*

**The defect, in one line.** [CURE 8](../audit/v3_5_cure_language.md#cure-8--sec-6-the-individual-liability-offense-reconstructed)
builds a burden-shifting presumption out of official responsibility, and SEC. 6(b)(1) makes
knowledge an express element. There is a leading appellate decision holding that the first cannot
supply the second, and this repository had never cited it.

**ANCHOR (SEC. 6(b)(1), verbatim from the tagged text):** "A person who knowingly or wilfully
causes, directs, conceals, or materially facilitates a violation of SEC. 5, or who deliberately
fails to halt a violation after notice, or who knowingly makes a false certification under SEC. 8,
is subject to the felony penalties of SEC. 10(c)."

### The authority the repository was missing

*United States v. MacDonald & Watson Waste Oil Co.*, 933 F.2d 35 (1st Cir. 1991) — the same
decision that calls *Dotterweich* and *Park* "the seminal cases regarding the responsible corporate
officer doctrine," at 51 — holds at 55:

> "In a crime having knowledge as an express element, a mere showing of official responsibility
> under *Dotterweich* and *Park* is not an adequate substitute for direct or circumstantial proof
> of knowledge."

⚠ **Quoted from two secondary sources, not from the reporter.** Lyness, 64 B.C. L. Rev. 253, at
n.148, and the Congressional Research Service's *Enforcement of Federal Pollution Control Laws*,
which cites the same page. **Until the slip opinion is read this cure may not be described as
verified, and no outreach may cite it as settled.** E22 governs.

### Why it bites here, and exactly where

CURE 8's Operation 4 proposes appending to SEC. 6(d):

> Evidence that the person, by reason of position, ownership, or authority, had responsibility and
> authority either to prevent the violation in the first instance or promptly to correct it, and did
> not do so, is sufficient to warrant a finding of practical power.

That is *Park*'s burden structure, and for SEC. 6(a) it is right: the elements there are practical
power and a failure of due care, neither of which is knowledge. It is the precise thing
MacDonald & Watson forbids at SEC. 6(b)(1), where the element **is** "knowingly or wilfully."

**So the cure as drafted works at the base tier and fails silently at the felony tier** — the tier
that carries the sentence the Act exists to make available. CURE 8's own *Held open* paragraph
half-saw this, calling SEC. 6(b)(1)'s "knowingly" undistributed. It did not know there was a case
on it.

**The circuits are not unanimous, and the disagreement runs the other way.**
*United States v. Johnson & Towers, Inc.*, 741 F.2d 662, 669 (3d Cir. 1984) requires the jury to
find that each defendant "knew that Johnson & Towers was required to have a permit, and knew that
Johnson & Towers did not have a permit" — a knowledge-of-the-law requirement the First Circuit and
most others reject. CRS carries the split under a *But see* signal. ⚠ Also unread in the original.

### Operation 1 — take the bridge the pollution statutes already codified

The federal answer to MacDonald & Watson is not to abandon the knowledge element. It is willful
blindness, and Congress wrote it into the statutes rather than leaving it to instructions. Per CRS:
the CAA and TSCA provide that "in proving a defendant's possession of actual knowledge,
circumstantial evidence may be used, including evidence that the defendant took affirmative steps
to be shielded from relevant information," and RCRA carries near-identical language for its knowing
endangerment offense. MacDonald & Watson itself carries a willful blindness instruction at
footnote 15. ⚠ **What the footnote does with it is not confirmed.** The opinion was read on
25 August 2026 and n.15 is the willful-blindness footnote, but the source carried no star pagination
and the footnote's own text was not recovered, so *whether the First Circuit approved the
instruction or merely recited it* is open — and this Operation leans on the approval. **A reviewer
with reporter access should settle it first; if the court did not approve it, Operation 1 loses its
federal anchor and stands on the CAA and TSCA text alone.** The constitutional ceiling is
*Global-Tech Appliances, Inc. v. SEB S.A.*, 563 U.S. 754, 769 (2011). ⚠ CRS and *Global-Tech*
remain unread in the original.

**NEW TEXT — appended to SEC. 6(b):**

> In proving that a person acted knowingly or willfully under this subsection, circumstantial
> evidence may be used, including evidence that the person took affirmative steps to be shielded
> from information that would have disclosed the violation or the conditions giving rise to it.
> Responsibility and authority under SEC. 6(d), standing alone, do not establish knowledge.

The second sentence is the concession, and it is written against the Act's own convenience. It
states MacDonald & Watson as a limit on the statute rather than waiting for a defendant to state it
first. **A reviewer who thinks the first sentence swallows the second has found the objection this
cure most needs.**

### Operation 2 — one word, and it is in the tagged text

SEC. 6(b)(1) reads "knowingly or **wilfully**"; SEC. 7(b)(5)'s defense-costs proviso reads "a knowing or
**wilful** violation." That is British spelling on the operative mens rea term of an American felony
provision, and it is the only British spelling left in `model_act_v3_4.txt`. Three consequences,
in ascending order of seriousness: a legislative counsel running a conformity check sees an
instrument that does not match its own jurisdiction's usage; a reader searching "willful" in this
site's search bar does not find the felony tier; and the whole federal willful-blindness line above
is indexed under a spelling the Act does not use.

**NEW TEXT:** in SEC. 6(b)(1) and SEC. 7(b)(5), read *willfully* as **willfully** and *willful* as
**willful**.

*Why this is a cure and not a correction.* `model_act_v3_4.txt` is tagged and checksummed. A change
to it is an amendment with a number, not a sweep — so the commentary around it was normalized to
American spelling on 25 August 2026 by `check_spelling.py` and the instrument was left alone,
pending this operation at the revision.

### What the repository owes the reader beside the objection

Lyness does not accept MacDonald & Watson's reasoning as the end of it. At n.150: "This conclusion
ignores that both the CWA and the CAA have versions of the doctrine with a mens rea element of
'knowingly.'" And at the text his footnote 152 supports: the strict-liability form of the doctrine
"may be inappropriate under the RCRA's statutory language, but there is still room under the RCRA
to prosecute responsible corporate officers, at least in instances where 'knowledge' is implied by
the evidence."

**That is the shape of the answer.** MacDonald & Watson does not bar a knowledge-tier RCO offense.
It bars using responsibility as a *substitute* for knowledge. The Act may keep its felony tier; it
may not reach it through SEC. 6(d).


### The answer the same line already supplies, and it is better than the objection

*United States v. Iverson*, 162 F.3d 1015 (9th Cir. 1998) is a Clean Water Act prosecution in which
the responsible-corporate-officer instruction was given and upheld. The court described exactly what
the instruction did and did not do — ✅ **read in the opinion 25 August 2026, transcribed
character for character**:

> "Read together with the previous instruction, the 'responsible corporate officer' instruction
> relieved the government only of having to prove that defendant personally discharged or caused the
> discharge of a pollutant. The government still had to prove that the discharges violated the law
> and that defendant knew that the discharges were pollutants. Thus, read as a whole, the
> instructions were not erroneous in the manner that defendant asserts."

**Two words in the version this project published until today were not the court's.** We printed
"violated the **[CWA]**" where the opinion says "violated the **law**", and "were **pol[lutants]**"
where it says "were **pollutants**" — editorial brackets that were never in the original and, in the
first case, narrowed a general word into a specific statute. See [E48](../ledger/errata.md). The
pincite 1026 is still the secondary source's: the text was read in a source carrying no star
pagination, so under [E47](../ledger/errata.md) the page is unconfirmed.
**That is the whole architecture in one sentence, and it is the architecture this cure proposes.**
Responsible-officer status replaces the **act** element. It does not replace the **knowledge**
element. MacDonald & Watson and *Iverson* are not in tension: the first forbids using responsibility
as a substitute for knowledge, and the second confirms that an RCO instruction which does not
attempt that substitution survives.

So SEC. 6(b)(1) may keep its felony tier and its "knowingly or wilfully," provided the prosecution
proves knowledge by ordinary means — including the willful blindness route Congress codified. What
it may not do is reach knowledge through SEC. 6(d).

**And *Iverson* carries a second holding this project has never used.** On why *Park*'s refinement
applies to the CWA at all — ✅ **read in the opinion 25 August 2026, the paragraph entire**:

> "In 1987, after the Supreme Court decided Park, Congress revised and replaced the criminal
> provisions of the CWA. (Most importantly, Congress made a violation of the CWA a felony, rather
> than a misdemeanor.) In replacing the criminal provisions of the CWA, Congress made no changes to
> its 'responsible corporate officer' provision. That being so, we can presume that Congress intended
> for Park's refinement of the 'responsible corporate officer' doctrine to apply under the CWA."

**A legislature that re-enacts around a doctrine adopts it.** That is an argument available to any
state adopting this Act on top of a framework statute it has already passed.

**The parenthetical is the part this project needed and did not have.** Our published version cut the
paragraph off before it and dropped the closing "under the CWA" without an ellipsis. Restored, the
paragraph says something the criminal lane has been arguing around all day: **the Ninth Circuit
applied *Park*'s responsible-officer refinement to a statute it had just told us Congress made a
felony.** *Ahmad*, below, says CWA discharges cannot be public welfare offenses precisely *because*
they are "felonies punishable by years in federal prison." *Iverson* supplies the premise of
*Ahmad*'s argument in a parenthetical and then declines its conclusion.

**Those two are not squarely reconcilable and neither case tries.** The reconciliation this cure
offers — that RCO relieves the act element while knowledge is proved by ordinary means — is
available on both sets of facts, and it is *our* reconciliation, not a court's. **A reviewer who
thinks a felony tier cannot rest on a doctrine grown in the misdemeanor soil of *Dotterweich* has
the two cases lined up to say so.**

⚠ The pincites 1024 and 1023–24 are still the secondary source's; the source read carries no star
pagination ([E47](../ledger/errata.md)). Lyness, 64 B.C. L. Rev. 253, remains unread in the original.

### Operation 3 — the instruction a circuit has already approved, which the Act should be measured against

*Iverson* sets out the responsible-corporate-officer instruction the district court gave and the
Ninth Circuit upheld. ✅ **Read in the opinion 25 August 2026:**

> "1. That the defendant had knowledge of the fact that pollutants were being discharged to the sewer
> system by employees of CH2O, Inc.; 2. That the defendant had the authority and capacity to prevent
> the discharge of pollutants to the sewer system; and 3. That the defendant failed to prevent the
> on-going discharge of pollutants to the sewer system."

**Knowledge of the fact. Authority and capacity to prevent. Failure to prevent.** That is a
three-element structure, approved on appeal in a federal criminal prosecution, and it is very close
to what [CURE 8](../audit/v3_5_cure_language.md#cure-8--sec-6-the-individual-liability-offense-reconstructed) reconstructs SEC. 6
into. **Element 1 is knowledge of the fact, not knowledge of illegality** — which is also the answer
to *Johnson & Towers*'s outlier requirement that the defendant know a permit was required.

**And the test behind the instruction is narrower in the Act than in the circuit.** *Iverson* states
it directly:

> "Under the CWA, a person is a 'responsible corporate officer' if the person has authority to
> exercise control over the corporation's activity that is causing the discharges. There is no
> requirement that the officer in fact exercise such authority or that the corporation expressly vest
> a duty in the officer to oversee the activity."

Set that beside SEC. 4(a). The Act agrees on both of *Iverson*'s negatives — it reaches a person who
"possesses **or** exercises" the authority, and SEC. 4(b) provides that "substance controls over
title" — but it then adds three qualifiers the federal test does not have. Authority must be
**final**, **material** and **independent**, and SEC. 4(a) excludes by name "title, office, seniority,
or status; professional credentials or technical ability; access to systems, weights, or
infrastructure; the ministerial execution... of a decision made by another; or the provision of
advice, analysis, or recommendation."

**So on the authority element this Act is narrower than the standard a federal court of appeals has
already approved in a criminal case.** That is an answer to the overbreadth objection the project did
not previously have, and it should be stated wherever SEC. 4 is defended.

**One drafting collision, and it is a word rather than a doctrine.** The approved instruction's
element 2 is "the authority **and capacity** to prevent." SEC. 4(a) closes with "the authority to
decide, **not the capacity to act**." The two senses differ — the instruction means power over the
outcome, the Act means the ability to perform the operation personally, which is how it keeps the
engineer with root access outside SEC. 4 — but the same word does opposite work in the Act and in
the instruction it most resembles, and SEC. 6(d)'s "genuine absence of power" is *Iverson*'s sense,
not SEC. 4(a)'s. **A legislative counsel will circle this. It costs nothing to fix and it has not
been fixed.**

### The best objection, stated because this cure would rather lose here than in a hearing

*United States v. Ahmad*, 101 F.3d 386, 391 (5th Cir. 1996) holds that illegal discharges under the
CWA are **not** public welfare offenses, because they are "felonies punishable by years in federal
prison" and "dispensing with mens rea would require the defendant to have knowledge only of
traditionally lawful conduct" (quoting *Staples*, 511 U.S. at 618). And Justice Thomas, dissenting
from the denial of certiorari in *Hanousek v. United States*, 528 U.S. 1102 (2000): the CWA "imposes
criminal liability for persons using standard equipment to engage in a broad range of ordinary
industrial and commercial activities."

**Read against this Act, that is an attack on the felony tier's entire framing**, and it is
sharper than the knowledge objection this cure was opened to answer. Training and deploying a model
is ordinary commercial activity. If a court took *Ahmad*'s view, the public-welfare label would not
carry SEC. 6(b) at all, and the tier would need a conventional mens rea of its own rather than a
relaxed one. **No one in-house can settle that. It is the criminal-law seat's question and it
belongs at the top of that seat's list.**

⚠ Both quoted from the CRS report *Enforcement of Federal Pollution Control Laws*, not from the
reporters. E22 governs.

**Administrative load:** none. Element and evidence provisions only.

**Held open for the criminal-law seat.** Whether the shielding sentence and the SEC. 6(d) carve-out
can coexist without the first eating the second; whether a state that has not adopted a
willful-blindness instruction can be given one by statute; and whether the Act should follow the
First Circuit or the Third on knowledge of the permit requirement, which here means knowledge that
SEC. 5 applied at all.

---
## CURE 24 — SEC. 8: the certification's lower tier names a mental state SEC. 6(a) does not require

*Opened 25 August 2026 from [PF-7](../audit/pre_review_pass_2026-08-24.md), on reading 18 U.S.C. § 1350 and
33 U.S.C. § 1319(c) in the primary. Numbered 26 August 2026.*

### The defect

**ANCHOR (SEC. 8, closing sentence, verbatim):** "Knowing false certification is an offense under
SEC. 6(b)(1); **reckless certification without reasonable inquiry** is an offense under SEC. 6(a)."

SEC. 6(a)'s element is that the person "failed to exercise due care," measured against "the conduct
of a reasonably prudent controlling person in like circumstances." **That is negligence.** SEC. 8
advertises recklessness, which is higher. A certification made negligently without reasonable
inquiry satisfies SEC. 6(a) while SEC. 8 says it does not.

**It is a fair-notice defect in the one provision the Act exists to make a natural person sign.**

### What the models actually say

**18 U.S.C. § 1350 — ✅ read in full 25 Aug 2026 — has no tier below knowledge.** (c)(1): "knowing"
— \$1,000,000 / 10 years. (c)(2): "willfully… knowing" — \$5,000,000 / 20 years. An executive who
certifies without adequate inquiry, not knowing the report is non-compliant, commits no offense
under it. **So § 1350 cannot be the donor of SEC. 8's second limb, and the Act names no other.**

**33 U.S.C. § 1319(c) — ✅ read in full 25 Aug 2026 — is the donor.** (c)(1) punishes one who
"**negligently** violates," imprisonment not more than one year on a first conviction; (c)(6)
provides that for the whole of subsection (c) "the term 'person' **means**, in addition to the
definition contained in section 1362(5), **any responsible corporate officer**." **Federal law has
imposed criminal liability on a responsible corporate officer for merely negligent violation, at the
misdemeanor level, since 1987.** That is SEC. 6(a) limb for limb, including SEC. 10(b)'s one-year
ceiling.

### Operation 1 — the tagged text, one clause

**NEW TEXT — replacing SEC. 8's closing sentence:**

> Knowing false certification is an offense under SEC. 6(b)(1); certification without reasonable
> inquiry is an offense under SEC. 6(a), which requires proof of the failure of due care described in
> that subsection.

### Operation 2 — the companion, one citation

n.8 defends SEC. 8 from § 1350 by argument from practice — its maxima are three to six times this
Act's base felony tier, and "executives have signed under harsher terms every quarter since 2002."
**That argument reaches the ceiling and is silent on the floor.** The note should carry
§ 1319(c)(1) with (c)(6) as the second model, and *United States v. Hanousek*, 176 F.3d 1116
(9th Cir. 1999) — ✅ **read in the opinion 26 August 2026, confirmed character for character on two
independent sources and held in the working library** — for the holding:

> "We conclude from the plain language of 33 U.S.C. § 1319(c)(1)(A) that Congress intended that a
> person who acts with **ordinary negligence** in violating 33 U.S.C. § 1321(b)(3) may be subject to
> criminal penalties."

⚠ Pincites remain unconfirmed: no source located carries reporter star pagination ([E47](../ledger/errata.md)).

### What the read produced beyond the holding, and it is larger than this cure

**One. There is a circuit split on the question the criminal lane calls unanswerable, and this
project has been citing only one side of it.** *Hanousek* holds, twice, that "**The criminal
provisions of the CWA constitute public welfare legislation**," resting on *United States v.
Weitzenhoff*, 35 F.3d 1275, 1283 (9th Cir. 1993). *Ahmad* holds the opposite — that CWA discharges
are **not** public welfare offenses, because they are "felonies punishable by years in federal
prison." **The lane sweep records *Ahmad* as the sharpest attack available and says nobody in-house
can settle it.** It can be answered, by a case this repository already held and had filed under
objections. *Weitzenhoff* is now a flagged row and is the next retrieval.

**Two. The due process answer is broader than SEC. 6(a) and the Act has never stated it.** Verbatim:

> "It is well established that a public welfare statute may subject a person to criminal liability
> for his or her **ordinary negligence without violating due process**."

citing *United States v. Balint*, 258 U.S. 250, 252–53 (1922) — **the 1922 case both *Dotterweich*
and *Park* rest on, and which was absent from this repository until today.** That sentence is the
constitutional defense of SEC. 6(a)'s entire design, and [known objections](../docs/known_objections.md)
argues the point without it.

**Three. The canon in *Hanousek* makes this cure urgent rather than tidy.** The court reasoned that
Congress wrote "gross negligence" into 33 U.S.C. § 1321(b)(7)(D) and **not** into § 1319(c)(1)(A),
and that "where Congress includes particular language in one section of a statute but omits it in
another section of the same Act, it is generally presumed that Congress acts intentionally and
purposely in the disparate inclusion or exclusion."

**Apply that to this Act's own text.** SEC. 8 says "**reckless** certification without reasonable
inquiry"; SEC. 6(a), where SEC. 8 sends it, requires only the failure of due care. **A court applying
*Hanousek*'s canon would presume that disparity deliberate and give it meaning** — most likely by
reading SEC. 8's second limb as reaching only recklessness, which is not what SEC. 6(a) says. The
mismatch is not untidy drafting. It is drafting a court has a rule for.

**Four, recorded because it points the other way.** Hanousek was a **roadmaster** — "responsible
under his contract for every detail of the safe and efficient maintenance and construction of track,
structures and marine facilities of the entire railroad." **Not an officer.** The CWA's responsible
person therefore reaches an operational supervisor, where SEC. 4(a) expressly excludes "the
ministerial execution, implementation, or communication of a decision made by another." **This Act
is narrower than its own model, for the third time this week.**

**And it takes the sting out of *Ahmad*.** *Ahmad* refuses public-welfare treatment to CWA discharges
because they are "felonies punishable by years in federal prison." **§ 1319(c)(1) is a misdemeanor.**
Whatever *Ahmad* does to a felony tier it does not reach a one-year negligence offense, which makes
SEC. 6(a) the least exposed part of the federal analogy rather than the most.

**The alternative a reviewer should weigh and this cure rejects:** raise SEC. 6(a) to the recklessness
SEC. 8 advertises. That buys the § 1350 analogy and abandons the negligence floor *DeCoster* says
*Park* supplies — trading a defensible doctrine for a defensible analogy.

**Administrative load:** none.
## CURE 25 — SEC. 10(d): the FDCA remedies are cited and their protections are not taken

*Opened 25 August 2026 from [PF-8](../audit/pre_review_pass_2026-08-24.md), on reading 21 U.S.C. §§ 332 and
334 in the primary. Numbered 26 August 2026.*

### Operation 1 — the jury the source supplies in exactly this case

SEC. 10(d)(2) provides that operation of a suspended configuration by a person with notice "is
**contempt and a violation of SEC. 5(a)**." That double character is the precise case
21 U.S.C. § 332(b) legislates for — ✅ read 25 Aug 2026:

> "In case of violation of an injunction or restraining order issued under this section, **which also
> constitutes a violation of this chapter**, trial shall be by the court, or, **upon demand of the
> accused, by a jury**."

**The Act cites § 332 for the injunction and drops § 332(b).** Ordinary law supplies a jury only where
the contempt sentence is serious; § 332(b) supplies it by statute whenever the two characters
overlap. **A defendant protection lost by omission.**

**NEW TEXT — SEC. 10(d), new final sentence:**

> In any proceeding for contempt of an order under this subsection where the conduct also constitutes
> a violation of SEC. 5, trial shall be by the court or, upon demand of the accused, by a jury.

### Operation 2 — the § 334 citation over-claims

§ 334 — ✅ read 25 Aug 2026 — is *in rem*: an article "proceeded against… on **libel of information
and condemned**," procedure conforming "as nearly as may be, to the procedure **in admiralty**," and
"on demand of either party any issue of fact… shall be tried by jury." SEC. 10(d)(2) takes the
thing-directed idea and none of the apparatus, while binding "any person with notice."

**Functionally it is prospective and injunctive — § 332's relative, not § 334's.** Either re-cite it
to § 332 and describe it as the injunction it is, which costs nothing; or keep the § 334 framing and
import what makes an in rem remedy fair — a right for any person claiming an interest in the
identified configuration to appear and contest before the suspension binds them.

**And it touches the takings lane.** A remedy operating on the thing rather than on conduct sits
closer to *Cedar Point*'s per se limb than to *Penn Central*'s regulatory one, and
[known objections](../docs/known_objections.md) does not make that connection.

**Administrative load:** none for the re-citation; an appearance procedure for the alternative.

## Addendum — the criminal lane's missing shelf, 25 August 2026

*Not a finding of this sweep. It comes from a vocabulary audit run two days later: the
lawyer-written documents in the working library were n-grammed against all files in the
repository, and a group of case names every criminal-law reviewer would reach for came back
**zero**. The method is recorded in the diary; the tool is `check_vocabulary.py`.*

**What was absent.** *MacDonald & Watson*. *Johnson & Towers*. *Iverson*, except in passing.
*Hanousek*. *Jewell*. *Global-Tech*. *Bank of New England*. *Ahmad*. **Respondeat superior**,
**collective knowledge**, **willful blindness** and **conscious avoidance** — none of them present
in a repository whose central offense is a knowledge-and-authority offense.

**Why it matters to this lane specifically, and not as a matter of presentation.** This sweep
graded SEC. 6(a) fatal and drafted CURE 8, whose Operation 4 proposes that evidence of
responsibility and authority "is sufficient to warrant a finding of practical power." That is
*Park*'s burden structure and it is right for the base tier. **It is the precise move
*United States v. MacDonald & Watson Waste Oil Co.*, 933 F.2d 35, 55 (1st Cir. 1991) forbids where
knowledge is an express element** — which is what SEC. 6(b)(1) makes it. So the cure this sweep
drafted works at the misdemeanor tier and fails silently at the felony tier, and the sweep's own
*Held open* paragraph half-saw it, calling SEC. 6(b)(1)'s "knowingly" undistributed without knowing
there was a case on the point.

**The repair is [CURE 22](../audit/v3_5_cure_language.md), and the answer comes from the same line rather
than from us.** *United States v. Iverson*, 162 F.3d 1015 (9th Cir. 1998) — ✅ read in the opinion
25 August 2026, pincite unconfirmed: the responsible-officer instruction "relieved the government
only of having to prove that defendant personally discharged or caused the discharge of a pollutant.
The government still had to prove that the discharges violated the law and that defendant knew that
the discharges were pollutants." Responsibility replaces the act element, not the knowledge element.

**And the objection this lane most needs is now on the shelf too.** *United States v. Ahmad*,
101 F.3d 386, 391 (5th Cir. 1996) holds that CWA discharges are **not** public welfare offenses,
because they are "felonies punishable by years in federal prison." Training and deploying a model is
ordinary commercial activity. **If a court took that view, the public-welfare framing would not
carry SEC. 6(b) at all**, and the felony tier would need a conventional mens rea rather than a
relaxed one. That is a sharper attack than anything this sweep produced, and nobody in-house can
settle it.

**The method point, which belongs here rather than in the cure.** The five lanes did not find this,
because none of the five was asked *what a specialist would look for and fail to find*. Asking what
is absent is a different instrument from asking what is wrong, and on its first run it produced a
front-page erratum ([E42](../ledger/errata.md)) and this addendum.

⚠ *Every authority named above is quoted from a secondary source and unread in the reporter. E22
governs: none may be described as verified.*

*From the queue's fatals pass, same file — the state-court cross-check:*

**To CURE 8 (SEC. 6(a) reconstructed) — the reconstruction matches the doctrine the state courts
already use.** *In re Dougherty*, 482 N.W.2d 485, 490 (Minn. Ct. App. 1992), states three factors
— "(1) the individual must be in a position of responsibility which allows the person to influence
corporate policies or activities; (2) there must be a nexus between the individual's position and
the violation in question such that the individual could have influenced the corporate actions
which constituted the violations; and (3) the individual's actions or inactions facilitated the
violations" — and the survey in hand records those factors "adopted by other state courts as the
essential elements" (California, Connecticut, Illinois, Indiana all citing it; Lyness, 64 B.C. L.
Rev. at 287–88). Operation 1's three elements are the same architecture: authority, nexus to an
actual violation, facilitation-by-failure. The sweep's hypothesis, drafted from *Park* alone,
independently converged on the formulation thirty years of state case law settled on — which is
evidence the fix is sound, and a citation for the criminal-law seat to check it against.
Washington's *McNamara* adds the SEC. 6(e) phrase itself: liability centered on "the corporate
officer's ability to prevent or correct a violation of the relevant statute" (292 P.3d 812, 831
(Wash. Ct. App. 2013)). One further reference for the seat: Ferzan, *Probing the Depths of the
Responsible Corporate Officer's Duty*, 12 Crim. L. & Phil. 455 (2018) (the mens-rea-depth debate;
not in hand).

## CURE 11 — SEC. 5: name the obligor; SEC. 9(b): write the duty in the active voice

*Opened 22 August 2026 by [the lane sweep](../audit/v3_5_lane_sweep.md), criminal-law lane. Sweep-derived.*

**The defect.** SEC. 5(a) reads "Deployment of a covered system without validation" — deployment
**by whom**? SEC. 5(c) reads "Failure to report as required by SEC. 9" — and SEC. 9(b) is written
entirely in the passive: "Preliminary notice to the Agency within 72 hours…" **No person is
commanded to report anywhere in the Act.** A defendant charged under SEC. 6(b)(1) with concealing a
SEC. 5(c) violation moves to dismiss on the ground that SEC. 9 imposes no duty on any identified
person, so no one can violate SEC. 5(c). Lenity does the rest. This matters most in the first
[180] days, when SEC. 5(c), (d) and (e) are the only live offenses.

**Operation 1 — a chapeau to SEC. 5.**

**NEW TEXT — inserted at the head of SEC. 5:**

> A violation of this section is committed by each entity that deploys, releases, provides, or
> operates the covered system to which the prohibited act relates, and, for purposes of SEC. 6, by
> each controlling person of such an entity who meets the elements of that section.

**Operation 2 — SEC. 9(b) in the active voice.**

**ANCHOR (SEC. 9(b), verbatim):** "Preliminary notice to the Agency within 72 hours of credible
notice to the entity or any controlling person"

**NEW TEXT:**

> Each entity that develops, releases, provides, or deploys the covered system shall transmit to the
> Agency a preliminary notice within 72 hours of credible notice to the entity or any controlling
> person

**Administrative load:** none.

---

## CURE 12 — SEC. 5(d): restore the scienter its own donor requires

*Opened 22 August 2026 by [the lane sweep](../audit/v3_5_lane_sweep.md), criminal-law lane, graded
**fatal**. Sweep-derived.*

**The defect.** SEC. 5(d) makes a "false or misleading statement of material fact" to the Agency an
offense with **no mental state at all** — not knowingly, not willfully, not recklessly. The companion
at n.20 says the offense follows "the structure of 18 U.S.C. § 1001" — which requires "knowingly and
willfully" — and relies on the *Alvarez* plurality's carve-out, which preserves statutes punishing
*knowing* falsity. **A strict-liability false-statement offense is outside the carve-out the note
relies on.** An engineer who transmits a compute figure later shown wrong by an accounting
convention the Agency had not yet ruled on has committed it; entity liability is strict and
immediate, and SEC. 6(a) supplies a year's custody on due-care failure. "Misleading" makes it worse:
a literally true statement is criminal, with no scienter — the compelled-characterization problem
the Act works hard to avoid at SEC. 8, SEC. 9(c) and n.16, reintroduced through the back door. And
this is the offense SEC. 13(b)(1) puts in the **first rank** and n.13 relies on as preemption-proof:
central, and the softest target in the Act.

**Operation.**

**ANCHOR (SEC. 5(d), verbatim):** "(d) A false or misleading statement of material fact concerning
a covered system, made to the Agency, or to any agency or officer of this State in connection with
the agency's or officer's official functions."

**NEW TEXT:**

> (d) A statement of material fact concerning a covered system, made to the Agency or to any agency
> or officer of this State in connection with official functions, that the person making it knows to
> be false, or makes with reckless disregard of its truth or falsity, or that omits a material fact
> necessary to make the statements made not misleading where the person knows of the omission. A
> statement made after reasonable inquiry, on the basis of facts then known to the person making it,
> is not a violation of this paragraph.

The reckless limb preserves SEC. 8's closing sentence — reckless certification without reasonable
inquiry remains an offense — without leaving the base offense at zero fault.

**Administrative load:** none.

---

### CURE 17 — SEC. 11(d): remedies for a reporter outside employment

*Donor note (24 Aug, evening): New York's own Labor Law § 740 notice (in hand) marks the
comparator's edge exactly — it protects "an individual who performs services for and under the
control and direction of an employer," former employees and dependent contractors included,
against employer retaliation, and reaches no outside reporter and no non-employment reprisal.
The employment-shaped remedy is the gap this cure exists to close.*

*The record's only actual frontier whistleblower was an outside member of the public — the AISI
incident's ⟨PERSON_C⟩, publicly identified 20 August ([the incident file § 5](../research/aisi_incident_inc_2026_07_28_01.md))
— whose retaliation was being hacked and publicly discredited by the agent's sockpuppets. SEC.
11(a)'s award is already any-person (§ 78u-6 structure) and would have reached him; SEC. 11(d)'s
remedies would not: reinstatement and back pay are employment remedies. The federal draft in this
field, S. 1792 (primary text in hand), protects employees and contractors only — the Act can
protect the person Congress's draft forgot, but only if (d)'s remedies fit him.*

**ANCHOR (SEC. 11(d), verbatim):** "(d) Retaliation against a person for reporting, internally or
to the Agency, gives rise to a civil action for reinstatement, double back pay, and fees."

**NEW TEXT:**

> (d) Retaliation against a person for reporting, internally or to the Agency, gives rise to a
> civil action for reinstatement, double back pay, and fees; and, where the person stands in no
> employment or contractual relationship with the retaliating person, or where those remedies do
> not lie, for actual damages, injunctive relief, and fees. Retaliation under this subsection is
> any adverse action taken because of the report, whether or not an employment relationship
> exists.

**Administrative load:** none. Remedy conforming only.

---

## III. The question menu

Any three answered are a disposition; all seven, with the repairs above verified or refuted, are
the seat done whole. Replace any of them with findings of your own.

1. Is the reconstructed SEC. 6(a) chargeable?
2. Is due care as an element the right cure for the *Alleyne* problem?
3. Does the restored burden survive?
4. Is CURE 1's answer — one injury definition, not two — right?
5. Does a state's suspended-sentence law defeat the harm-tier minimum? *(the sweep could not
   settle this)*
6. Does per-victim counting survive the state's merger doctrine? *(nor this)*
7. **Does misdemeanor authority reach a felony tier?** *Dotterweich* and *Park* are misdemeanor
   cases. Lyness argues the state doctrine should carry individual **civil** liability and only
   civil liability, on the ground that those cases were decided "during a time when the immediate
   and collateral consequences were different" (64 B.C. L. Rev. 253, 297-98). The sweep's own
   answer stops at the base tier: *Park* holds, and *Staples*' penalty-sensitivity "does not bite
   at a misdemeanor." **Nothing in this repository argues that the same authority reaches
   SEC. 6(b).** Either supply that argument or refute it; either way it is a finding, and it is the
   one the maintainer most wants answered. *(Added 25 August 2026; the sweep's own statement of it
   is in Part I above.)*

Senior to all six, from the companion's
[READ FIRST index](../model_act_v3_4_companion.md#read-first--questions-for-the-next-revision-v35):
item 3's remainder (the death-results minimum and the report-versus-element distinction) and
item 4 (the sentencing valve against state proportionality clauses) are this lane's too.

## IV. The errata already filed in this lane

- [E1](../ledger/errata.md#e1--engineer-exemption-claimed-as-written-in-fact-implied-not-yet-express)
  — the engineer exemption was claimed as written; it is implied, not yet express.
- [E8](../ledger/errata.md#e8--in-one-paragraph-true-of-the-duty-silent-on-the-entity-in-the-paragraph-built-to-be-quoted)
  — the entity tier is strict liability; the front-page summary once said otherwise.

Method-wide entries — E21, E22 (extended by E32), E27, E33 — govern how every date, quotation,
count, and file-status claim in the evidence base was made;
[the register](../ledger/errata.md) is short and worth ten minutes.

## V. Filing

## The other seats, and how this lane meets them

The review runs in eight parallel lanes: criminal law, enforcement, frontier security, fiscal and
administration, federalism and preemption, proportionality and sentencing, torts and design, and
open source and academia. Each seat reviews independently and each disposition publishes
independently, as written, so no lane waits on another. Findings that change text route through the
public cure queue and the errata register, where every other lane sees them. The maintainer collates
and responds separately and labeled, and may not overrule or edit a disposition. Anonymous outside
contributions arrive through the repository's correction doors and are credited by election — one
open drafting question has already been answered from outside this way. Reviewer identities are not
shared between reviewers, and attribution is each reviewer's own election.

**This lane specifically.** Criminal law gates the others in one direction: if the offense structure does not hold, the enforcement seat has nothing to charge and the proportionality seat nothing to grade. It meets the proportionality lane on the tier structure and the misdemeanor question, and the enforcement lane on what a prosecutor could actually prove.

*How this seat's work becomes the next version: verified findings are drafted as cures against the
tagged v3.4 text in the public queue, and the assembled v3.5 carries every lane's accepted work, so
a disposition here is a chapter of the next version, written alongside the other seats'. Reviewer
identities are never shared between reviewers. The nearest familiar analogy is a conference paper
rather than peer review: you take a seat, do the work, and it is published as yours — see
[the dispositions register](../dispositions/README.md) for the rules, fixed before the first one
arrived.*


---

**If you need something this packet does not carry.** [The glossary](../standards/what_these_words_mean.md)
defines the words the Act turns on, in the sense the statute uses them, including the ones a
specialist reader would search for first. [Known objections](../docs/known_objections.md) carries
the attacks already made on this lane, with the answers given and the ones still unanswered.
[For reviewers](../REVIEWERS.md) states every open item in the project in one line each, and
[the index](../MAP.md) reaches the rest of the repository.

---

Email FrontierAIAccountabilityProject@proton.me — links or pasted text, no attachments — in any
form: a memo, a marked-up copy of this packet, a numbered list of findings. Or, if you were
contacted by the maintainer through a different channel, reply on the channel you were contacted
on. It is published as written, credited or anonymous at your choice; council seats publish with
names, which is the point of them. A finding that something is broken is the seat working, not
failing.
