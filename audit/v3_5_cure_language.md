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

**Held open — one design note.** Whether the SEC. 9 *reporting* trigger should keep
broader language (report widely on the (h)(4) base; convict precisely on (h)(3)) while
the SEC. 10(c) *element* takes (h)(3) alone. Report-vs-element bifurcation is a
drafting-session decision for v3.5, flagged for the criminal-law seat alongside READ
FIRST 3(c), the bracketed [two]-year minimum, which this cure does not touch and which
remains open.

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

