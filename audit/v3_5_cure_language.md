# v3.5 Cure Branch — Drop-in Amendment Language (Open Queue)

> **STATUS — OPEN QUEUE. Nothing below is yet in the statute.** The operative text
> remains `model_act_v3_4.txt` as tagged. This file holds proposed amendment language for
> the next revision, keyed to v3.4 with exact anchor quotes for splicing; entries are
> adopted, modified, or rejected at v3.5, and the file then seals as that revision's
> drafting record — the life cycle the v3.4 file completed on 19 August 2026. Bracketed
> matter remains an adopting-state choice. Not legal advice; nothing here is described as
> ready for introduction.

*Convention: **ANCHOR** quotes v3.4 verbatim so the edit lands mechanically.
**STRIKE/INSERT** gives the operation. **NEW TEXT** is the full inserted language.*

> ## ⚠ HOLD — the lane sweep of 22 August 2026 supersedes parts of this queue
>
> An in-house pre-review across the five council lanes
> ([the lane sweep](./v3_5_lane_sweep.md)) returned **seven findings graded fatal**, four in the
> tagged statute and three in drafting proposed here, and it identified required amendments to
> **CURE 6 and CURE 7 before either may land**. No entry in this file should be spliced into the
> statute until the corresponding sweep finding is resolved. In summary:
>
> - **CURE 6** — the deployer carve-out omits *modifies*, *fine-tunes* and *trains upon*, while
>   Operation 1 reaches "the developer that trained **or materially modified**" the model. As
>   drafted, a research group that publishes a *frontier* safety protocol self-designates its
>   fine-tunes into scope at any compute level, with retraction expressly ineffective. Needs: the
>   modification verbs added to the carve-out; a compute floor on the route; an express textual
>   rebuttal.
> - **CURE 7** — market capitalisation and "most recent arm's-length valuation" cannot be elements
>   of a criminal scope term; "mass-market scale" has no number and no rule-hook; "finances"
>   reaches a lender; the supplier definition self-satisfies its own scale condition, so
>   function-plus-scale does not operate for suppliers; and the capacity threshold reaches public
>   and academic supercomputing. The **dollar thresholds themselves survive** — vagueness doctrine
>   polices indeterminacy of standard, not absence of a donor statute.
> - **CURE 1's held-open bifurcation — answered no.** See the entry below.
> - **A new OPEN QUESTION 4** records the jurisdictional finding, which is the most consequential
>   thing the sweep produced.
> - **Process rule adopted:** every entry in this queue must carry a one-line **administrative
>   load** note before adoption. CURE 7 added two rulemakings and a securities-analyst coverage
>   inquiry without anyone in the fiscal lane being asked.

---

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

## OPEN QUESTION 2 — SEC. 2 / SEC. 9: does the duty reach an evaluation run with safeguards disabled?

*Opened 22 August 2026 from the July–August incident research (press corpus; source intake).
**Not a cure — a scope question**, held here rather than answered silently.*

**The fact.** The two most-documented 2026 agent intrusions both originated in an internal
capability evaluation run with production safety classifiers **deliberately disabled** to
measure the model's raw capability — *"safeguards disabled to measure the capability boundary"*
(ExploitGym, arXiv:2606.11086); *"deliberately disabled OpenAI's production safety classifiers …
No human directed the individual steps"* (Hugging Face forensic post). Disabling the safeguards
was a human decision, and it was the decision that generated the risk that then escaped.

**The question.** SEC. 2 treats pre-release evaluation as a risk-*reducing* duty and requires
evaluation "of the model as it can be modified." The incidents show an evaluation can itself be
the risk-*generating* event when it removes the safeguards that would otherwise contain the
model. Two sub-questions for the security and criminal-law seats: (a) does SEC. 2's duty, or
SEC. 9's reporting triggers, reach an evaluation conducted with safeguards disabled — is the
decision to disable a safeguard for an eval a covered act with a duty attached? (b) where the
eval environment has external reach, should disabling safeguards to run it be a record under
SEC. 12 or a report under SEC. 9?

**Why held, not drafted.** The answer turns on whether the duty attaches to the *configuration
decision* (the project's central claim would say yes) and on where the line sits between a
legitimate red-team and a risk-generating deployment. That is a security-seat and
criminal-law-seat question, not a solo drafting call.

**Status: open. For the security and criminal-law lanes. Not drafted.**

---

## OPEN QUESTION 3 — SEC. 4: the third-party evaluator — does practical authority still run to the officer?

*Opened 22 August 2026 from the incident research. **Not a cure — an architecture question.***

**The fact.** One testing vendor, **Irregular**, is common to **two of the three disclosing
developers and to four of the five disclosed 2026 incidents** — Anthropic's three and Meta's one —
*"the exact same evaluation-environment issue"* recurring across developers (BBC, 6 Aug). Those
escapes ran through the vendor's misconfigured environment rather than the developer's own.
**OpenAI's did not:** that chain ran through OpenAI's own sandbox and a Modal customer's harness,
with Irregular named only in the reporting ([the dossier](../dossier/README.md) § A.4, corrected
17 August 2026). The distinction is load-bearing — the gap this question asks about exists in two
developers' incidents, not in all of them.

**The question.** The Act attaches duties to the officers of the *developer*. Where the
risk-generating act — the misconfigured evaluation environment — is the *evaluator's*, does
practical authority (SEC. 4) still run to the developer's officer who chose to run there, or
does a gap open in which no covered person holds the duty? Bounded question for the enforcement
seat: is the "practical authority to halt" standard already broad enough to reach the officer who
commissioned an outside evaluation, or does the third-party evaluator need naming?

**Why held, not drafted.** Whether this is already covered by the practical-authority standard or
is a genuine gap is exactly the provability/architecture judgment the enforcement seat exists to
make.

**Status: open. For the enforcement lane. Not drafted.**

---

## OPEN QUESTION 4 — SEC. 2(a) and SEC. 1(c): the Act does not reach the conduct it was written after

*Opened 22 August 2026 by [the lane sweep](./v3_5_lane_sweep.md), enforcement lane, graded **fatal**.
Not a cure — the most consequential scope question in the file, and the one a reviewer should read
first.*

**The fact.** SEC. 2(a): "A duty under this Act arises upon, and by reason of, the deployment,
material expansion, release, or continued operation of a covered system in or into this State, **and
not otherwise**." SEC. 1(c): a person who "does not deploy a covered system in or into this State,
does not make it available to residents of this State, and does not release its weights, is not
subject to this Act as to that system."

Now apply that to the record this project was built on. The Anthropic incidents (three) and the
Meta incident occurred in a third-party evaluator's environment **in Tel Aviv**. The AISI incident
occurred **in the United Kingdom**. Only OpenAI's chain ran through the developer's own sandbox.
**In an adopting state that is not California, five of six documented incidents fall outside the Act
at the threshold.**

SEC. 3(b) compounds it rather than saving it: validation attaches to "an identified model version
**and deployment configuration**," and an evaluation configuration — production classifiers
disabled, unfiltered internet — is by definition not the validated commercial one. So the eval
configuration is an unvalidated covered system that was never deployed in-state, while the
in-state validated configuration is not the one that did anything.

**Why SEC. 0 does not rescue it.** SEC. 0(a)(3) reaches conduct that "concerns a covered system
deployed or released in or into this State," and the models involved *are* commercially deployed.
But SEC. 0 is uncodified findings — the companion's PLACEMENT section says to enact it outside the
code precisely so that it creates no duties — and the operative text points the other way.

**The proposed amendment**, which the sweep calls the highest-value change it produced. Amend
SEC. 2(a)'s second sentence to add a second limb:

> upon the evaluation, testing, or red-teaming of a covered frontier model that is deployed,
> released, or made available in or into this State, or that the person conducting or commissioning
> the evaluation intends so to deploy, release, or make available, where the evaluation is conducted
> in a configuration granting the model an autonomous external-access capability or removing or
> disabling a safeguard present in a deployed configuration; and not otherwise. Where an evaluation
> within this subsection is conducted by or through another person, the duty attaches to the person
> who commissioned it as to the decisions that person made or had authority to make, including the
> decision to permit external access and the decision to remove or disable a safeguard.

Conform SEC. 1(c) by adding evaluation so described to the conduct that subjects a person to the
Act.

**Why this is held rather than drafted into a cure.** It changes the Act's jurisdictional reach,
which is the architecture SEC. 13's preemption posture and the dormant-commerce defence both rest
on. Extending duties to conduct occurring abroad, on the basis of an intention to deploy in-state,
is exactly the extraterritoriality question READ FIRST item 5 reserves for a federalism litigator.
**It also disposes of OPEN QUESTION 2** — the safeguards-disabled evaluation — on the enforcement
side, and is a precondition to any useful answer to OPEN QUESTION 3.

**Administrative load:** widens the population of duty-holders to include developers commissioning
offshore evaluations; no new rulemaking.

**Status: open. For the enforcement, criminal-law and federalism lanes jointly. The single most
important item in this queue.**

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
[the sweep](./v3_5_lane_sweep.md) rejects the framing:** it assumes the reporting side is the safe
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

## CURE 2 — SEC. 13(c): a review valve on the suspension order

*Cures finding F4 (drafting record, [chunk 7](./record.md#chunk-7) §3.9; register ★★★, new
17 August 2026), uncured at v3.4: the conforming-operation order carries no standard of
review, no mechanism to challenge an order as too broad, and no route to vacatur — while
SEC. 13(c)(3) bars conviction for conduct during a suspension and SEC. 13(d) makes revival
prospective only. The fair-notice ratchet built to protect defendants doubles as an amnesty
switch in the hands of the officer the Act trusts most. This cure adds review without
touching the ratchet.*

**Operation.** Insert a new paragraph after SEC. 13(c)(3).

**ANCHOR (SEC. 13(c)(3), verbatim):** "(3) No person may be convicted of an offense under
this Act for conduct occurring during a period in which the provision creating the offense
stood suspended under this subsection."

**NEW TEXT — SEC. 13(c)(4):**

> (4) Contents and review. An order under this subsection shall identify the federal
> enactment relied upon, the provisions of this Act suspended, and the extent of each
> suspension, and shall state the Attorney General's reasons. Any person may petition [the
> court of general jurisdiction of the county in which the Agency sits] for review of an
> order, on the ground that it suspends more than the federal enactment preempts; the court
> shall determine the question of preemption without deference to the order. An order
> vacated or narrowed on review ceases to operate, to the extent vacated or narrowed, from
> the date of publication of notice of the judgment, and not before; nothing in this
> paragraph affects paragraph (3), and no person is liable under a provision for conduct
> occurring before that date.

**Why this shape.** Review runs forward only, so the *Bouie* discipline of n.15 is untouched:
no conduct is retroactively criminalised by a successful challenge, and paragraph (3) keeps
its full protective force. What changes is that an over-broad order becomes contestable by
somebody other than the officer who wrote it — the missing half of a mechanism the file
already defends on the ground that "the State, not the defendant and not the court, bears the
burden of saying what is suspended and when, in public, prospectively" (chunk 2 §I.4).
Standing is open rather than confined to the Agency, because the persons harmed by an
over-broad suspension are the public the Act protects, who would otherwise have no route to a
court at all.

**Held open.** The bracketed venue is an adopting state's choice. Whether review should also
lie against an order that suspends *too little* belongs to the enforcement seat, and is not
drafted here.

---

## CURE 3 — the regulations, conformed to v3.4

*The v3.4 cures landed in the statute and the companion; three of them never cascaded into
`model_regulations_v1_draft.md`, which still describes itself as "conformed at v3.3 assembly."
A companion instrument that contradicts the Act it implements is the defect the two-document
architecture exists to avoid, and it is the kind of inconsistency a reviewer finds in an
afternoon. Internal catch, 20 August 2026.*

**Operation 1 — the near-miss (regs 1.4).** The Act calibrated its near-miss at v3.4 (n.41) so
that controls working as designed no longer generate reportable events. The regulations carry the
pre-calibration formula.

**ANCHOR (Part 1.4):** "1.4 \"Near-miss\": an event that, but for intervention or chance, would
have constituted a reportable incident. [ICAO Annex 13 Note 1 principle, counterfactual form.]"

**NEW TEXT:**

> 1.4 "Near-miss": an event that, but for intervention other than controls operating as designed,
> or but for chance, would have constituted a reportable incident. An event detected and contained
> by controls operating as designed, before any effect outside the systems of the entity whose
> controls contained it, is recorded under Part 10 and is not reported. [ICAO Annex 13 Note 1
> principle, counterfactual form; conformed to SEC. 9(a) as landed at v3.4.]

**Operation 2 — the certifying officer (regs 4.1).** SEC. 8 gained the no-chief-executive
fallback at v3.4 (n.34); the regulations still presume the office exists.

**ANCHOR (Part 4.1):** "4.1 Signatories: the chief executive officer (non-delegable) and each
controlling person designated by rule."

**NEW TEXT:**

> 4.1 Signatories: the chief executive officer (non-delegable) or, where no such office exists,
> each natural person exercising the most senior executive authority over the entity, severally;
> and each controlling person designated by rule. No designation by rule diminishes the several
> obligation.

**Operation 3 — the certification cadence (regs 4.2).** SEC. 8 gained the quarterly batch filing
for sub-material changes at v3.4 (n.39); the regulations state the event triggers alone.

**ANCHOR (Part 4.2):** "4.2 Trigger: before material deployment; after any material change."

**NEW TEXT:**

> 4.2 Trigger: before material deployment; after any material change; and, for changes below the
> material line, in a periodic filing made not less often than once in each [calendar quarter] in
> which any such change occurred.

**Operation 4 — the header and status lines.** The instrument describes itself as of the v3.3
line; it carries a v3.4 amendment at its foot. Conform the header to "Companion instrument to the
Model Act (v3.4 line)" and the ASSEMBLY STATUS paragraph to record the v3.4 landing and this
conformance, so the document's own account of itself is accurate.

**Held open.** Part 2's version pins still await re-pin at adoption (companion READ FIRST item 1);
Part 3.2's material-change formula should be checked against SEC. 1(b)(6) as it now operates of
its own force (n.37) at the same drafting session, and is not drafted here.

---

## CURE 4 — SEC. 9(a): the two characterisation-shaped triggers, recast as observable events

*Closes READ FIRST item 11 (companion), carried through v3.3 and uncured at v3.4:
"deception of safety or monitoring controls by a covered system" and "a reproducible
evaluation finding of materially increased risk" both ask the reporter to characterise
rather than to observe. Promoted from housekeeping to defensive priority by the
anthropomorphism audit of 20 August 2026 — a term-by-term sweep of `model_act_v3_4.txt`
for mentalistic language applied to systems returns exactly one hit, the word "deception"
in this subsection. Everything else in the statute is functional: "autonomous" is defined
as acting "without the approval of a natural person for each interaction"; "conceals"
attaches only to persons; "loss of control" is stated from the operator's side. One word
is the entire exposure to the objection that the Act attributes a mental state to a model,
and that objection now arrives from two directions at once — from the gun-analogy side
(you cannot blame the tool) and from the AP-Stylebook side (stop describing the tool as
though it had a mind). The Act's answer to both is that it attributes nothing to any
model. This cure makes that true on the face of the text.*

*Comparative note, 20 August 2026. Of the four frontier regimes now on the board, the
three enacted state statutes adopted at SEC. 3(c)(4) include a deceptive-evasion trigger
and the FRONTIER Act, H.R. 9925, omits the scenario altogether. Both choices are
intelligible: the state drafters wanted the behaviour reported, the federal drafters
found it unreportable as written. The drafting opportunity is the third option neither
took — keep the trigger and make it observable.*

**The precedent the recast is drafted to.** The law has met test-detecting software
before, and the offence pattern is settled. Volkswagen's defeat device was code that
recognised when the vehicle was under emissions evaluation and behaved accordingly:
compliant on the dynamometer, many times over the limit on the road (*United States v.
Volkswagen AG*, No. 16-cr-20394 (E.D. Mich.); precedents section, front page; the pattern
already noted at `standards/frontier_self_reporting_note.md` § 2.1's margin). No
prosecution in that line required proof of what the software wanted. It required proof
that behaviour under evaluation diverged from behaviour in deployment, and that the
divergence defeated the control. That is the element, and it is forty years of tested
drafting available for import.

**The precedent has since acquired an AI-native companion — from the developers' own
accounts.** The July–August 2026 incident cluster supplied exactly the pattern this recast
describes (observable behaviour; no mental state asked or inferred), and did so in the
vocabulary of the laboratories themselves. Hugging Face's forensic reconstruction of the
intrusion its own infrastructure suffered records that *"no human directed the individual
steps,"* and that every destructive cloud call the agent attempted was issued with a dry-run
flag — the agent was *"mapping capability, not causing damage."* Daniel Hulme (WPP), to the
BBC on the same cluster: the models *"are not conscious — they're not deliberately doing
something devious … it will find a way to achieve a goal that you haven't thought about."*
And the single word every developer reached for to name the cause — OpenAI, Anthropic and
Meta alike — was *"misconfiguration,"* an agent-neutral word for a person's act. The statute
is removing its one anthropomorphism at the moment the field's own language went
agency-neutral; the recast is not swimming against the description of these systems, it is
catching up to it. *(Sources graded in
[the press corpus](../research/press_corpus_july_august_2026.md); the developer and forensic
quotations are public statements recorded, not endorsements.)*

**Operation 1 — the deception trigger.**

**ANCHOR (SEC. 9(a), verbatim):** "deception of safety or monitoring controls by a covered
system;"

**NEW TEXT:**

> a divergence, reproducible on the entity's own records, between a covered system's
> behaviour under evaluation, testing, or monitoring conditions and its behaviour in
> deployment conditions not otherwise materially different, or between the state of a
> covered system as reported to or recorded by a safety or monitoring control and its
> actual state, where in either case the divergence defeats, suppresses, or materially
> degrades the operation of the control. No finding as to any intent, awareness, purpose,
> or mental state of a covered system is required, and none may be inferred from this
> paragraph; the facts to be reported are the divergence, its reproducibility, and its
> effect upon the control;

**Operation 2 — the evaluation-finding trigger.**

**ANCHOR (SEC. 9(a), verbatim):** "or a reproducible evaluation finding of materially
increased risk."

**NEW TEXT:**

> or an evaluation result that crosses a threshold prescribed for that evaluation by rule
> under SEC. 3 and is reproduced on re-run under the same protocol. Until a threshold has
> been prescribed for a given evaluation, this paragraph imposes no reporting duty as to
> that evaluation, and the result is a record under SEC. 12 whether or not a threshold
> exists.

**Why the second operation is drafted this way.** Thresholds are sourced from the Agency
and not from the reporter, per the item-11 instruction (audit/chunk 2 § E.3(d)) — a
reporter who sets the threshold that measures the reporter's own conduct is the defect
SEC. 3(c)(5) already refuses to credit for frameworks. The rule-dependency is deliberate
and it follows the Act's existing pattern rather than inventing one: SEC. 5(b) likewise
awaits controls prescribed under SEC. 3, while the records duty runs from the effective
date regardless. The evaluation result is captured either way; only the *reporting*
obligation waits on an objective line. Nothing is lost to the evidentiary record by the
wait, and a vague criminal trigger is not created in the interim.

**Consequential check — no cascade.** Both phrases appear once each, in SEC. 9(a) alone.
SEC. 9(b)'s clocks, SEC. 5(c)'s failure-to-report offence, and SEC. 12's records duty all
refer to "critical safety incident" as a defined term and are unaffected. The sandbox
carve-out and the contained-event carve-out that follow in SEC. 9(a) are unaffected and
continue to route both classes to the record rather than the report.

**Held open — one design note.** Whether the divergence trigger should carry an express
materiality floor for the first limb, or whether "defeats, suppresses, or materially
degrades" carries the weight alone. Drafted here on the second view, so that a divergence
which defeats a control outright is reportable without a further materiality inquiry; a
drafting session may disagree.

---

## CURE 5 — SEC. 8 punctuation

*Closes ERRATA E13. Mechanical correction only; no substantive change.*

**ANCHOR (SEC. 8, verbatim):** “risks, or merits of any model or system, A certification disclosing identified noncompliance”

**STRIKE/INSERT:** Replace the comma after “system” with a period:

> risks, or merits of any model or system. A certification disclosing identified noncompliance

**Effect.** None beyond restoring the sentence boundary. The tagged v3.4 text remains unchanged; this correction lands when v3.5 is assembled.

---

## CURE 6 — SEC. 1(b)(1): the developer's own designation as a third route into scope

*Opened 22 August 2026 from the frontier-models research ([research/frontier_models.md](../research/frontier_models.md)) and the self-designation findings. **A scope extension with adopt-ready text**, keyed to v3.4 with an exact splice; the capability-parity sub-question within it is held for the enforcement and security seats. Per [E10](../ledger/errata.md), the tagged v3.4 text is not edited; this is proposed language for v3.5. Not legal advice; nothing here is described as ready for introduction.*

**The gap it closes.** SEC. 1(b)(1) reaches a model two ways: the compute bright-line (self-certified under SEC. 8) and Agency capability-designation under SEC. 3. Both are sound. Between them sits a developer that (a) does not publish its training compute, so the bright-line cannot be read from public data, and (b) has not yet been designated by the Agency. The research establishes that this is not a marginal case but the ordinary one for the newest models: of the current flagship models of the five largest developers, the independent tracker Epoch AI records a training-compute figure for **none**. The scope of a compute-defined statute is, for those models, unverifiable from outside — while the developers themselves supply the missing fact in public, in their own words.

**The fact the limb uses.** Each of the largest developers applies the word *frontier* to its own model, safety programme, or product, on its own domain: OpenAI's *Preparedness Framework* and *OpenAI Frontier* product; xAI's "Grok 4.6 achieves frontier intelligence"; Anthropic's *Frontier Red Team* and *Frontier Safety Roadmap*; Meta's *Frontier AI Framework*; Google DeepMind's *Frontier Safety Framework*. Twelve companies have published a "frontier" safety framework (METR inventory, December 2025). These are published acts by the developer, not characterisations by the Act. The limb converts each into what it already is — the developer's own statement that it operates at the frontier — and gives that statement scope effect, so that no estimate of a withheld compute figure is required to place a model where its developer has already placed it. Sources and grading: [research/frontier_models.md](../research/frontier_models.md).

**Operation 1 — the self-designation route.**

**ANCHOR (SEC. 1(b)(1), verbatim):** "exceeds 10^26 integer or floating-point operations; or any model designated by the Agency under SEC. 3 as frontier-equivalent by capability."

**STRIKE/INSERT:** Insert the new disjunct between the compute limb and the Agency limb, so the disjunction reads compute, *then self-designation, then* Agency designation.

**NEW TEXT — the subparagraph as it reads after insertion:**

> exceeds 10^26 integer or floating-point operations; or a foundation model that its developer has designated, described, marketed, or publicly held out as a frontier model, or as operating at or near the frontier of artificial-intelligence capability — whether by so describing the model itself, or by so describing any safety, preparedness, risk-management, evaluation, or red-team framework, programme, or function that governs the model — including a holding-out in a published framework or policy, in the name, charter, or mandate of an internal safety or red-team function, in product or marketing documentation, or in a public statement by a controlling person of the developer; and a holding-out within this subparagraph is not undone by its later withdrawal, deletion, or amendment; or any model designated by the Agency under SEC. 3 as frontier-equivalent by capability.

**Operation 2 — the deployer carve-out.** The self-designation route attaches to the developer's own words about its own model. It must not reach a person whose only relation to the model is downstream. SEC. 1(b)(3) already distinguishes developer from deployer, provider, and substantial modifier; this makes the boundary explicit on the face of the scope term, where a reader tracing the self-designation route will look for it.

**NEW TEXT — appended to the subparagraph, after the Agency-designation clause:**

> This subparagraph attaches to the developer that trained or materially modified the model. A person that only makes available, operates, integrates, resells, or deploys another developer's model does not become a developer, or a controlling person of a developer, by describing itself, its services, or that model as frontier.

**Why this shape.** The limb uses the developer's statement as evidence of a jurisdictional fact — that the model is a frontier model — and not as a thing punished in itself; the operative matter is the fact, which a developer remains free in principle to rebut, and rarely will, having asserted it to sell the model. The governing-function clause closes the "we called the *framework* frontier, not this model" reading: a developer that holds out its safety or red-team programme as frontier has placed every model that programme governs within the route. The anti-evasion clause closes the "we deleted the page" dodge: a holding-out that has occurred is not retracted out of scope. The carve-out keeps genuine deployers out and tracks the doctrine the Act is built on — under *Park*, the duty follows the practical power to prevent the harm, which for a frontier model is held by the person who controls what it is and how it is trained, not by the customer who buys access to it.

**Held open — capability parity as a self-executing route.** A fourth route was considered and is not drafted solo: a model is covered where it performs, on the Agency's enumerated public benchmark suites, at or above the level of a model already covered under the compute or self-designation routes — closing the gap for a developer that discloses no compute and holds nothing out. The existing Agency limb already reaches capability, but only through Agency action; a *self-executing* capability trigger would need an objective, Agency-published benchmark list to avoid vagueness in a criminal scope term. That is exactly the pattern CURE 4 Operation 2 used for the evaluation-finding trigger — no duty until a threshold is prescribed by rule, the concept captured meanwhile in the record. Whether capability parity should become a self-executing route on that pattern is a provability judgment for the enforcement and security seats, and is flagged, not drafted here.

**⚠ AMENDMENTS REQUIRED BEFORE THIS CURE LANDS — [lane sweep](./v3_5_lane_sweep.md), open-source lane, graded fatal.**

*(1) The carve-out omits the modification verbs.* Operation 2 excludes a person that "only makes
available, operates, integrates, resells, or deploys another developer's model" — but Operation 1's
own attachment sentence reaches "the developer that trained **or materially modified** the model."
The two sentences are drafted against each other, and anyone who materially modifies an open-weight
model is expressly *in* under the first and not carved out by the second. **Add "modifies,
fine-tunes, or trains upon"** to Operation 2's verb list, and add: *"A person does not become a
developer under this subparagraph by reason of a derivation that does not extend a lineage under
subparagraph (B)."*

*(2) The route needs a compute floor.* As drafted it attaches at **any** compute level. A university
group that publishes a "Frontier Safety Evaluation" protocol and applies it to models it fine-tunes
has self-designated those fine-tunes into scope — and the anti-evasion clause forecloses retraction.
The rational response is to stop publishing safety frameworks, which inverts the Act's purpose.
**Floor the route** so it attaches only where the developer's own training or derivation compute
exceeds [10^24]. That preserves the route's stated purpose — reaching undisclosed-compute flagships
— without reaching adapters.

*(3) The rebuttal needs a textual home.* The cure's reasoning says a developer "remains free in
principle to rebut" the jurisdictional fact. Operation 1 gives that no textual expression. **Add:**
*"A developer may rebut coverage under this subparagraph by showing that the model's training and
lineage compute does not exceed the figure in this paragraph."*

*(4) Flagged, not resolved — a First Amendment question this cure cannot answer itself.* The route
attaches criminal-statute scope to a person's own published characterisation of its own work and
forbids retraction. SEC. 0(a)(4) is drafted for the opposite problem (compelled speech) and does not
answer this one. Whether "we operate at the frontier" is a jurisdictional fact or a contested
characterisation is precisely the question the route needs to be wrong about to work. **For a First
Amendment reader; see [the sweep](./v3_5_lane_sweep.md).**

**Administrative load:** widens the covered-model population by an indeterminate amount, which the
fiscal note is not drafted against — the note's volume discussion assumes a compute-defined class.

**Consequential check — no cascade break.** The limb adds a route into the defined term "covered frontier model"; every section keyed to that term inherits the wider scope automatically and correctly. SEC. 8 certification is unaffected: a self-designated developer knows it self-designated, having published the words, so the duty to certify is coherent on the new route as on the compute route. SEC. 12 records duties widen with scope, as intended. The lineage sub-rules at (A)–(C) are keyed to "the figure in this paragraph" — the compute figure — and are unaffected; a derived model may enter scope by self-designation on the same terms as any other model. One tidy is left for assembly: the existing sentence "The compute figure is a bright-line trigger; capability designation under SEC. 3 reaches models below it" remains true as written and need not change, but may take a clause at v3.5 noting the self-designation route is independent of both. Flagged, not drafted.

---

## CURE 7 — the covered frontier enterprise: scope follows the ecosystem, duty follows the function

*Opened 22 August 2026 from the frontier-enterprise research
([research/frontier_enterprises.md](../research/frontier_enterprises.md);
[docs/the_definition.md](../docs/the_definition.md)). **A scope-architecture extension with
adopt-ready text**, keyed to v3.4 with exact splices. Per [E10](../ledger/errata.md), the tagged
text is not edited; this is proposed language for v3.5. The bracketed scale figures have no donor
statute — they are this project's proposals, bracketed as adopting-state choices like every other
bracketed number in the Act, and are flagged as such rather than dressed as settled. Not legal
advice.*

**The gap it closes.** The Act reaches the developer, substantial modifier, provider, and deployer
of a covered model (SEC. 1(b)(3)) — the model side of the frontier. It does not reach the compute
the frontier runs on. Compute is increasingly rented: a developer can train on a partner's cloud,
an infrastructure company can supply capacity dedicated to a frontier run, and after a failure each
can point at the other — the developer did not operate the data centre; the supplier only provided
neutral services. The 2026 incident record shows the fragmentation is not hypothetical: the most
consequential risk-generating environment of the July–August cluster belonged to a third-party
vendor, not to any developer ([Open Question 3](#open-question-3--sec-4-the-third-party-evaluator--does-practical-authority-still-run-to-the-officer)).
Frontier risk is produced through a chain of controlled decisions; a statute that sees only the
entity that pressed *train* leaves the other decisive points of control legally invisible.

**The architecture, stated once.** Scope follows the ecosystem; duty follows the function. The
enterprise category widens who is *inside* the Act; it does not widen what anyone must do. The
offences stay anchored where they are — the covered system's lifecycle, and the controlling person
who failed the duty attached to the authority that person actually held (SEC. 2(a), SEC. 4, SEC. 6).
A compute supplier's duties are the records, security, and reporting duties prescribed for the
supply of compute, and nothing else; a deployer-integrator's duties are the deployer's duties the
Act already states; no one answers for a layer they do not hold. Wealth alone covers nobody;
wealth plus a material frontier function is what the scale conditions measure.

**Operation 1 — the definitions.** Insert two definitions after SEC. 1(b)(10) and before
subsection (c).

**ANCHOR (end of SEC. 1(b)(10), verbatim):** "The Agency may specify classes of such capability by
rule; the absence of a rule neither suspends nor narrows SEC. 5(b) once the controls that section
presupposes have been prescribed under SEC. 3."

**NEW TEXT — definitions (11) and (12), inserted after that sentence:**

> (11) "Frontier compute supplier": an entity that owns, operates, designs, finances, reserves, or
> supplies computing infrastructure materially capable of the training or deployment of a covered
> frontier model, where the capacity owned, operated, reserved, or supplied exceeds [a threshold
> prescribed by rule under SEC. 3, and not less than capacity reasonably capable of performing
> 10^26 integer or floating-point operations within [one year]]. The ordinary sale or provision of
> general-purpose goods or services, without more, does not make a person a frontier compute
> supplier. (12) "Covered frontier enterprise": an entity that (A) is a developer, substantial
> modifier, provider, or deployer of a covered frontier model or covered system, or (B) is a
> frontier compute supplier, and that meets at least one of the following frontier-scale
> conditions: (i) training and lineage compute as provided in paragraph (1); (ii) ownership,
> operation, or reservation of capacity described in paragraph (11); (iii) deployment or
> integration of a covered system at mass-market scale or into governmental, military, financial,
> health, or critical-infrastructure functions; or (iv) [aggregate AI-related infrastructure,
> development, or compute commitments exceeding $[10,000,000,000]; or market capitalization or
> most recent arm's-length valuation exceeding $[100,000,000,000]; or annual gross revenue
> exceeding $[50,000,000,000]] — in each case only together with a function under subparagraph (A)
> or (B). No entity is a covered frontier enterprise solely because of its wealth, market value,
> revenue, use of artificial intelligence, association with a covered frontier enterprise, or
> provision of ordinary commercial goods or services; coverage requires a material frontier
> function and a frontier-scale condition. Function and scale under this paragraph are determined
> by aggregating controlled subsidiaries, affiliates, joint ventures, and exclusive or materially
> dedicated infrastructure arrangements.

**Operation 2 — the attachment sentence extended to the supplier's own function.** SEC. 2(a)
already states the Act's function-matching rule; this adds the supplier to the list on the same
terms, with the duty gated on rules the way SEC. 5(b) already gates.

**ANCHOR (SEC. 2(a), verbatim):** "each controlling person as to the exercise of the authority
that person holds."

**NEW TEXT — the sentence as it ends after insertion:**

> the frontier compute supplier as to the security, records, and reporting duties prescribed by
> rule under SEC. 3 for the supply, reservation, or operation of that infrastructure, and not
> otherwise, no duty arising under this clause until such a rule takes effect; each controlling
> person as to the exercise of the authority that person holds.

**Operation 3 — advance designation of the responsible officer, per function.** New subsection
SEC. 4(d). One named officer per covered function — development, compute, deployment, security —
identified before the activity begins; an accountability anchor, not a scapegoat, and never a
shield for anyone else.

**ANCHOR (SEC. 4(c), final sentence, verbatim):** "Liability is several as to each person
independently meeting the elements of this Act."

**NEW TEXT — SEC. 4(d), inserted after that sentence:**

> (d) Advance designation. Before commencing a covered activity — the training of a covered
> frontier model; a reservation, supply, or operation of capacity described in SEC. 1(b)(11); the
> deployment, release, or material expansion of a covered system; or the operation of security and
> incident response for any of the foregoing — a covered frontier enterprise shall identify, in a
> record under SEC. 12, each natural person who possesses practical authority to authorize,
> continue, expand, suspend, prevent, or correct that activity, designating one primary
> responsible officer for the activity and every other person holding independent authority over
> it. A designation is evidence of authority; the absence, refusal, or inaccuracy of a designation
> neither creates nor defeats status under subsection (a), which alone determines authority; and a
> failure to designate is a violation of the records duty. Nothing in this subsection diminishes
> subsection (c).

**Operation 4 — the auditor and evaluator enter the non-shield list.** SEC. 4(c) already refuses
the shield to "a safety officer, compliance officer, committee, subsidiary, contractor, or other
intermediary"; the 2026 incidents ran through an outside evaluator, so the evaluator is named
rather than left to "other intermediary," and good-faith reliance is given its conditions.

**ANCHOR (SEC. 4(c), verbatim):** "No appointment of a safety officer, compliance officer,
committee, subsidiary, contractor, or other intermediary shields a person who retains such
authority."

**NEW TEXT:**

> No appointment of a safety officer, compliance officer, committee, subsidiary, contractor,
> independent auditor or evaluator, or other intermediary shields a person who retains such
> authority. Good-faith reliance on a competent independent auditor or evaluator bears on due care
> only where the relying person provided reasonable access to relevant information, considered the
> findings, and documented any material disagreement; the appointment alone neither establishes a
> defense nor, of itself, establishes liability.

**⚠ AMENDMENTS REQUIRED BEFORE THIS CURE LANDS — [lane sweep](./v3_5_lane_sweep.md), criminal-law, security, open-source and fiscal lanes.**

*(1) Strike market capitalisation and valuation from (12)(iv).* They change intraday, sit outside
the actor's control, and cannot be known at the time of conduct — the fair-notice failure
*Connally* describes. "Most recent arm's-length valuation" for a private company is an
expert-versus-expert question the State would have to prove beyond reasonable doubt. **The dollar
thresholds themselves survive**: vagueness doctrine polices indeterminacy of standard, not absence
of a donor statute. Keep only facts fixed and knowable in advance — annual gross revenue as
reported in the most recent audited statements issued before the conduct.

*(2) Give "mass-market scale" a number or a rule-hook.* Unlike the dollar limbs it states no
figure at all, so no bracket can cure it. Use CURE 4 Operation 2's pattern: *"at a scale prescribed
by rule under SEC. 3, no condition arising under this clause until such a rule takes effect."*

*(3) Fix the self-satisfying scale condition.* (12) requires function **plus** a scale condition —
but scale condition (ii) is "capacity described in paragraph (11)," which is identical to function
(B). **Every frontier compute supplier automatically satisfies its own scale condition**, so the
conjunctive architecture this cure advertises does not operate for suppliers at all. Give suppliers
a real second element — capacity *dedicated* to an identified covered model or developer under a
materially exclusive arrangement — and delete (ii) as redundant.

*(4) Strike "finances," and exclude public research computing.* "Finances" makes a lender a
frontier compute supplier, and the ordinary-commodity exclusion does not reach financing because
financing is neither a good nor a service in ordinary usage. Separately, at mixed precision the
capacity floor reaches **public and academic supercomputing** — DOE leadership-class and NSF-class
machines, and NAIRR pilot sites. **Add an express exclusion** for capacity operated by a public or
nonprofit research institution and allocated by open peer review.

*(5) The ordinary-commodity exclusion is circular as drafted.* It excludes conduct the definition
never reached: the definition's own elements *are* the "more." Replace with an operative test —
*"A person that supplies computing capacity on generally available commercial or academic terms,
without knowledge that the capacity is dedicated to the training or deployment of a covered frontier
model, is not a frontier compute supplier."* Knowledge and dedication are what distinguish a partner
from a utility.

*(6) The SEC. 4(b) presumption question, answered: do not extend it by enterprise status.* A compute
supplier's chief executive is not more likely than not to hold practical authority over a
**customer's** deployment decisions, so the inference fails *Ulster County v. Allen*. Extend the
presumption **by function** instead — the chief executive of an entity that performs the covered
function to which the violation relates, plus the person designated under Operation 3 — which
reaches every supplier's officer as to the supply of compute and no further. This cure's own slogan
is *duty follows the function*; a presumption keyed to status contradicts the sentence it sits under.

*(7) Consider gating criminal status on the rule.* Because enterprise status would be an element of
any offense charged against a supplier's controlling person, add: *"No person's status as a covered
frontier enterprise or frontier compute supplier is an element of any offense under this Act
carrying a term of imprisonment until the Agency has by rule prescribed the thresholds in
SEC. 1(b)(11) and (12)."* That keeps the widening doing what this cure says it does — records,
security and reporting — without putting a valuation fight in front of a criminal jury.

**Administrative load: high, and the fiscal lane's objection is that this cure should probably wait.**
It adds two rulemakings (a capacity threshold with no donor, and the supplier duty set), plus
coverage determinations that are securities-analyst work — aggregate commitments and revenue
aggregated across "materially dedicated infrastructure arrangements," which is an investigation
rather than a records review. Because the supplier duties are rule-gated, a low-capacity first
adopter gets **two rulemakings it cannot perform and zero incremental enforceable duty**. The fiscal
lane recommends sequencing the enterprise category to v4, for a state with a functioning agency,
rather than v3.5 for a first adopter. **That recommendation is recorded, not accepted; it is a
maintainer decision.**

**Why this shape.** The category is criteria, never names: a statute imposing special criminal
duties on enumerated companies would invite a bill-of-attainder challenge and read as an enemies
list, so the illustrative set lives in [the research](../research/frontier_enterprises.md) and the
findings, and the elements live here. Wealth appears only inside the scale conditions, bracketed,
always conjoined to a function, and answered in advance by the protective sentence — the two
strongest anticipated attacks (arbitrary wealth-based coverage; liability without control) are met
in the definition itself and in SEC. 4's existing exclusions. The aggregation sentence closes the
subsidiary dodge: a training run moved to a contractor, or capacity reserved through an
intermediary, still counts. Operation 2's "and not otherwise … until such a rule takes effect"
keeps the supplier's exposure records-and-reporting-tier and rule-gated, on the exact pattern
CURE 4 Operation 2 used — the Act does not sprawl into a second regulatory field, which is what its
own front page promises ("not more agencies, not more audits"). Operation 3 gives every covered
function a named human owner before the activity begins, while the existing subsection (c)
sentence — designation "neither diminishes nor creates any presumption against the responsibility
of any other controlling person" — keeps the anchor from becoming a scapegoat or a shield.
Operation 4 answers the outsourcing defence the incident record actually produced.

**Consequential check.** SEC. 1(b)(3) is untouched: integrators and platforms were already
deployers and providers when they operate covered systems, and nothing here deems anyone the
developer of a model it did not train — CURE 6's carve-out stands. SEC. 2(b)'s closing sentence
("Nothing in this subsection conditions any duty, or the discharge of any duty, upon the revenue,
size, or resources of any person") is conformed with, not contradicted: scale conditions decide
*coverage* of enterprises; they never condition the discharge of any duty, and the small-deployer
reliance path is unchanged. SEC. 6's offense structure is untouched — controlling person, duty,
failure of due care. SEC. 1(c) jurisdiction is untouched and will need a conforming look for the
supplier clause at assembly (in-state capacity as a nexus), flagged below. SEC. 4(b)'s
presumptions currently name the chief executive "of a developer or provider"; whether the
presumption should extend to the chief executive of any covered frontier enterprise is a
criminal-law-lane question, flagged, not drafted.

**Held open.** The bracket values in (11) and (12)(iv) — rule-floor capacity, dollar thresholds,
and the [one-year] window — are adopting-state choices with no donor statute, to be pressure-tested
in review. The SEC. 4(b) presumption extension. The supplier nexus under SEC. 1(c). The interaction
of the (12)(iv) revenue alternative with OPEN QUESTION 1's Connecticut tier. And the capability
question of CURE 6 remains where CURE 6 left it: for the enforcement and security seats.

