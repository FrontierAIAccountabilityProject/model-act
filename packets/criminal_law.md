# The criminal-law lane — one page

*A reading copy for the criminal-law seat, assembled 24 August 2026 by
`packets/build_criminal_packet.py` from [the in-house sweep](../audit/v3_5_lane_sweep.md),
[the drafting queue](../audit/v3_5_cure_language.md), and
[the errata register](../ledger/errata.md). Those files are the authority; this page exists so
the lane can be read, printed, and marked up as one document. If this page and a source differ,
the source is right and the difference is a defect worth reporting to
FrontierAIAccountabilityProject@proton.me.*

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
[the drafting record](../audit/record.md#chunk-3) behind them.

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

---

## II. What has been drafted in response

*Reproduced verbatim from [the queue](../audit/v3_5_cure_language.md), grading intact:
sweep-derived and intake-derived entries are hypotheses, expressly not settled drafting, and the
intake-derived entries are additionally AI-assisted and not maintainer-validated. Each entry is a
candidate finding — verifying or refuting one is a complete finding for the disposition.*

## OPEN QUESTION 1 — SEC. 3(c)(4): does Connecticut become a fourth interim standard?

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
meaning of 29 C.F.R. § 1904.7(b)(5) — which is a fact rather than a characterisation, and so keeps
faith with SEC. 9(c) and n.16.

**One further amendment the sweep requires.** Most state penal codes already define "serious bodily
injury" or "serious physical injury" differently, and the companion directs codification among the
offenses against the person. Two definitions of one term in one code is a construction trap
resolved against the State. Either use a statute-unique term — *covered serious bodily injury* — or
add: *"This definition governs this Act notwithstanding any other definition of the same or a
similar term in the law of this State."*

**Still open:** READ FIRST 3(c), the bracketed [two]-year minimum. The sweep finds the *number*
defensible — it attaches only to a knowing or wilful violation that proximately causes death, and
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
"is *Park* itself." The text says something different, and a defence-friendly court will read
"Genuine absence of power negates the element; it is not an affirmative defense" to mean the
defendant need produce nothing. Pre-indictment the State cannot see the delegation memoranda or the
reserved-matters schedule; against a structured defence it simply does not indict. **This is not a
constitutional defect. It is the reason the offense would never be charged.**

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
Washington's *McNamara* adds the SEC. 6(e) phrase itself: liability centred on "the corporate
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
offense with **no mental state at all** — not knowingly, not wilfully, not recklessly. The companion
at n.20 says the offense follows "the structure of 18 U.S.C. § 1001" — which requires "knowingly and
willfully" — and relies on the *Alvarez* plurality's carve-out, which preserves statutes punishing
*knowing* falsity. **A strict-liability false-statement offense is outside the carve-out the note
relies on.** An engineer who transmits a compute figure later shown wrong by an accounting
convention the Agency had not yet ruled on has committed it; entity liability is strict and
immediate, and SEC. 6(a) supplies a year's custody on due-care failure. "Misleading" makes it worse:
a literally true statement is criminal, with no scienter — the compelled-characterisation problem
the Act works hard to avoid at SEC. 8, SEC. 9(c) and n.16, reintroduced through the back door. And
this is the offense SEC. 13(b)(1) puts in the **first rank** and n.13 relies on as preemption-proof:
load-bearing, and the softest target in the Act.

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

Any three answered are a disposition; all six, with the repairs above verified or refuted, are
the seat done whole. Replace any of them with findings of your own.

1. Is the reconstructed SEC. 6(a) chargeable?
2. Is due care as an element the right cure for the *Alleyne* problem?
3. Does the restored burden survive?
4. Is CURE 1's answer — one injury definition, not two — right?
5. Does a state's suspended-sentence law defeat the harm-tier minimum? *(the sweep could not
   settle this)*
6. Does per-victim counting survive the state's merger doctrine? *(nor this)*

Senior to all six, from the companion's
[READ FIRST index](../model_act_v3_4_companion.md#read-first--open-items-for-the-next-revision-v35):
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

Email FrontierAIAccountabilityProject@proton.me — links or pasted text, no attachments — in any
form: a memo, a marked-up copy of this packet, a numbered list of findings. Or, if you were
contacted by the maintainer through a different channel, reply on the channel you were contacted
on. It is published as written, credited or anonymous at your choice; council seats publish with
names, which is the point of them. A finding that something is broken is the seat working, not
failing.
