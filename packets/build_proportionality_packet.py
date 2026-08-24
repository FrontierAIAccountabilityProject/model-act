#!/usr/bin/env python3
"""Assemble packets/proportionality.md — the proportionality lane's reading copy.

Run from the repository root:  python3 packets/build_proportionality_packet.py

This builder holds the packet's authored text as its template and writes it out
verbatim: the authored text lives HERE, and every revision is made here and
regenerated — the .md is never edited by hand, so the regeneration rule is
enforceable from this revision forward. The sources cited inside the packet
remain the authority; if the packet and a source differ, the source is right and
the difference is a defect worth reporting. A future revision may upgrade this
builder to section-extraction in the manner of build_criminal_packet.py.
Stdlib only; deterministic; no network.
"""
import io

OUT = "packets/proportionality.md"

PACKET = r'''# The proportionality lane — one page

*A reading copy for the proportionality seat: the penalty architecture of the Model Act — Frontier AI Public Welfare Offenses, assembled as one document so the lane can be read, printed, and marked up whole. Assembled 24 August 2026; linked from the reviewer surfaces when the current review freeze lifts. The sources are the authority — [the statute](../model_act_v3_4.txt), [the drafting queue](../audit/v3_5_cure_language.md), [the prosecuted-conduct gallery](../standards/the_same_conduct.md), [the table of authorities](../standards/table_of_authorities.md) — and if this page and a source differ, the source is right and the difference is a defect worth reporting to FrontierAIAccountabilityProject@proton.me.*

## The ask

One seat, one lane, scope in writing before work begins. Unpaid. **The floor:** the statute straight through, then this packet, then **three findings, verified or refuted, with reasons** — a complete and publishable disposition, perhaps six to eight hours. **The whole seat:** the menu below worked through in full — every question answered, every drafted repair verified or refuted — roughly ten to twenty hours across eight weeks. Both are dispositions; both are published as written, including "approved with reservations," including hostile. A disposition that refutes one finding is worth more to this project than a full pass that agrees with everything.

One caution on reading state, stated once so nothing below misleads: the tagged text under review is [`model_act_v3_4.txt`](../model_act_v3_4.txt). Everything in [the open queue](../audit/v3_5_cure_language.md) — every CURE cited on this page — is drafted or hypothesised language, not enacted in the tagged statute, and the sweep-derived entries are expressly not maintainer-validated.

## Read first — the statute itself

The tagged text is not reproduced here. Read [`model_act_v3_4.txt`](../model_act_v3_4.txt) cover to cover in one sitting. Your sections: **SEC. 6** (the individual offence and its enhanced tier), **SEC. 7** (disgorgement and the insurance bar — the economic sanctions your clauses also reach), and **SEC. 10(b)–(c)** (the penalty brackets, the harm tier, and the sentencing valve). The companion's penalties note stands behind all three.

---

## I. The penalty architecture, walked

### The harm tier's federal geometry

SEC. 10(c)(2) is built on borrowed federal geometry, and [the table of authorities](../standards/table_of_authorities.md) lays the borrowings out row by row. The ceiling pair — twenty years where serious injury results, "any term of years or for life" where death results — is the consumer-product-tampering statute's, 18 U.S.C. § 1365(a), which is also the ceiling structure of the federal drug statute's death-results provision. From that second anchor the Act takes the per-victim counting practice and the but-for-plus-proximate-cause rule, stated in text at SEC. 10(c)(2)(D) with the victim's identity an element of each offence. What the Act **deliberately declines** is the federal mandatory floor: where the federal donor says not less than twenty years, the Act says "not less than [two] years" — bracketed, and held open for exactly this seat.

### The bracketed minimum, and the question the sweep could not settle

The in-house review found the [two]-year number defensible — it attaches only to a knowing or wilful violation that proximately causes death, and it is the lowest figure in its donor neighbourhood — but found it **"cosmetic without a non-suspension clause"**: in most states a minimum is satisfied by a suspended sentence with probation unless the statute says otherwise, and this one does not ([CURE 1's still-open item](../audit/v3_5_cure_language.md#cure-1--serious-injury-source-moves-to-18-usc--1365h34)). It also collides with the adopting state's own homicide grid with no priority rule. Whether a state's suspended-sentence law defeats the harm-tier minimum is a question the sweep expressly could not settle, and it is on your menu below.

### The valve — this lane's central open question

SEC. 10(c)(3) is the sentencing valve: concurrency as the default; consecutive service only on stated findings that the aggregate "is not disproportionate to the whole of the person's conduct and culpability"; a [forty]-year cap on stacked determinate terms. The companion's penalties note assembles it entirely from enacted sentencing law — the federal concurrency default, the Ohio findings-gated consecutive-service chapeau, the Kansas double rule applied to the twenty-year ceiling, and the Model Penal Code's stricter aggregate-cap tradition at § 7.06(1)(c), which caps consecutive terms at the longest term authorised for the highest grade of crime among the sentences, with no doubling ([the § 7.06 rows](../standards/table_of_authorities.md)).

The valve exists because the doctrine will not. Federal noncapital proportionality review "forbids only extreme sentences that are grossly disproportionate to the crime," successful challenges are exceedingly rare, and the federal unit of review is the count, not the aggregate — so a per-victim stack is federally unreviewable in both directions. The controlling law will therefore be the adopting states' own proportionality clauses — Illinois's "seriousness of the offense" with "the objective of restoring the offender to useful citizenship," Oregon's "all penalties shall be proportioned to the offense," Indiana's and West Virginia's — several of them stricter than the federal standard, all of them senior to any model act. The cautionary precedent the companion holds up is the nineteenth-century per-count machine itself: 307 small counts converted into 19,914 days at hard labour.

Whether the valve as drafted survives those fifty clauses is **the statute's own held question for this seat**: the companion's READ FIRST item 4 reads, in full, "A proportionality scholar should test the drafted sentencing valve against state constitutional clauses," and marks it **Open**. Nothing on this page pre-answers it. It is the centre of the lane.

### The brackets, pinned to figures governors already signed

The money side of SEC. 10 is drafted to sit inside the enacted family rather than beyond it. The entity ceiling of $[1,000,000] per violation per day has enacted siblings on [the authorities shelf](../standards/table_of_authorities.md): California's severity-scaled $1,000,000 penalty, New York's penalties adopted as caps, Illinois's penalty sections — three signed state statutes at the same figure. The individual brackets at SEC. 10(b) and (c)(1) take their classification from the food-and-drug misdemeanour structure and their amounts from the federal alternative-fine structure (twice the gross pecuniary gain), and SEC. 10(c)(4)'s closing sentence directs the court to the person's income and resources "so that like culpability bears like burden" — a means-sensitivity clause your lane should test against the same state clauses as the valve.

### Announced maxima against imposed sentences — the record

Before grading any ceiling in SEC. 10, read [the prosecuted-conduct gallery's table](../standards/the_same_conduct.md#the-table). Five prosecutions of individuals for computer-access conduct, none involving physical injury; in every row the maximum announced at charging exceeds the outcome by an order of magnitude or more. One row announces thirty-five years while the prosecution privately offers months; another announces roughly 440 years and ends in a single misdemeanour. The gallery's own finding: "the announced maximum is a communications instrument, not a forecast." Its executive rows show the same gap running the other way — the decisive variable in sentence severity was not the body count but the documentary record of knowledge. For a proportionality reviewer the question this record poses is precise: are this Act's announced ceilings — twenty years per injury, life per death — to be graded as sentences, or as the communications instrument the record shows maxima to be, and does a state constitutional clause care about the difference?

### Deterrence pricing — why the fine schedule is not the deterrent

The Act's premise is that entity fines are absorbed while decision-makers stay insulated; [the known-objections file](../docs/known_objections.md) states it as the case for the personal tier — a fine is "absorbed as an operating cost by shareholders and customers while the decision-maker stays insulated," and the deterrence-economics rows on [the authorities shelf](../standards/table_of_authorities.md) supply the theory: deterrence requires the expected sanction to exceed the benefit, a payable fine is a price, and fines alone cannot reach the judgment-proof or the equity-rich. [The forecasters' arithmetic, § 4](../research/forecast_arithmetic.md#4-why-the-fine-cannot-deter--their-own-magnitudes) prices the premise from the industry's own projections, marked ⚠ — that file's flag for forecast-grade material: projection leant on as projection, never as observed fact, and it should be graded accordingly here too. One figure stands for the rest: an industry projected to spend $2.4T of capital expenditure over 2028. Against balance sheets of that shape, § 4 concludes, no enactable fine schedule changes a decision — which is the Act's whole argument for custody, and a proportionality reviewer should say whether deterrence arithmetic of that kind is a permissible input to a proportionality analysis at all, or an aggravation of it.

---

## II. What has been drafted in response

*From [the open queue](../audit/v3_5_cure_language.md) — drafted and hypothesised language for a future revision, none of it in the tagged text. Each entry is a candidate finding; verifying or refuting one is a complete finding for the disposition.*

**[CURE 1](../audit/v3_5_cure_language.md#cure-1--serious-injury-source-moves-to-18-usc--1365h34) — the injury definition the harm tier turns on.** The tagged SEC. 1(b)(8) defines "serious injury" from a medical-device reporting regulation. CURE 1 moves the definition to 18 U.S.C. § 1365(h)(3)–(4) — the criminal definition of the same donor statute whose § 1365(a) geometry SEC. 10(c) already borrows — "so tier and trigger now travel together," and so the harm tier's construed phrase arrives with four decades of case law, including protracted impairment of a mental faculty. The queue's own design ruling matters to this lane: use the narrower (h)(3) for both reporting and conviction, because widening the reporting trigger widens a custodial offence. For proportionality purposes the injury definition **is** the tier's width: every widening of "serious bodily injury" multiplies the per-victim counts the valve must then hold. The entry also carries the still-open minimum discussed in Part I.

**[CURE 12](../audit/v3_5_cure_language.md#cure-12--sec-5d-restore-the-scienter-its-own-donor-requires) — the scienter the false-statement offence dropped.** SEC. 5(d) as tagged criminalises a false or misleading statement to the Agency with no mental state, while the companion's own note cites a federal donor requiring "knowingly and willfully." The sweep graded this fatal; the drafted repair requires knowledge or reckless disregard, adds a materiality-tied omissions limb, and protects a statement made after reasonable inquiry. It is a hypothesis, sweep-derived, not maintainer-validated. Your lane's interest is the gradient: a zero-fault offence feeding, through SEC. 6, into custodial exposure is a proportionality defect before it is a scienter defect, and [the known-objections file's strict-liability row](../docs/known_objections.md) — "Nobody is punished because a system surprised everyone" — is only true if repairs of this kind land.

---

## III. The question menu

Any three answered are a disposition; all of them, with the two repairs above verified or refuted, are the seat done whole. Replace any of them with findings of your own.

1. Does the SEC. 10(c)(3) valve survive the state proportionality clauses — the held READ FIRST item 4 question, and the lane's centre?
2. Does a state's suspended-sentence law defeat the bracketed [two]-year death-results minimum, and does the minimum need a non-suspension clause or deletion?
3. Is per-victim counting, with the victim's identity an element, defensible under clauses that grade the offence rather than the count — or is it the per-count machine the companion's own cautionary precedent warns against?
4. Is the [forty]-year aggregate cap the right formula, against the stricter no-doubling tradition of MPC § 7.06(1)(c)?
5. Given the prosecuted-conduct record's gap between announced maxima and imposed sentences, are the twenty-year and life ceilings honest instruments — and should a model act say anything about charging practice at all?
6. May deterrence arithmetic of the forecast-grade kind in § 4 legitimately inform a proportionality judgment, or does pricing the fine's failure concede the custody tier must do work fines constitutionally cannot?

## The other seats, and how this lane meets them

This review runs in parallel lanes — criminal law (under review now), enforcement, security, fiscal, proportionality, federalism, and torts/design, with open-source gated separately. Each seat reviews independently, and each disposition publishes independently, as written, so no lane waits on another. Findings that change text route through the public cure queue and the errata register, where every other lane sees them. The maintainer collates and responds separately and labelled, and may not overrule or edit a disposition. Anonymous outside contributions arrive through the repository's correction doors and are credited by election — one open drafting question has already been answered from outside this way. Reviewer identities are not shared between reviewers, and attribution is each reviewer's own election.

This lane specifically: proportionality consumes the criminal-law seat's reading of the tier structure and the enforcement seat's sense of what is actually chargeable, and its valve question runs alongside the federalism seat's constitutional work — two seats testing the same text against fifty constitutions from two directions.

## What to attack

The valve first — it is the statute's own held question, and nobody in-house could answer it. Then the minimum, then the counting rule, then the cap formula; then, if anything remains of the hours, the ceilings against the prosecuted-conduct record. A finding that the valve fails under any named state clause, with the reason, is worth more than agreement with everything on this page.

File a disposition by email to FrontierAIAccountabilityProject@proton.me — links or pasted text, no attachments — in any form: a memo, a marked-up copy of this packet, a numbered list of findings. It is published as written, credited or anonymous at your choice. Hostile is welcome; a finding that something is broken is the seat working, not failing.
'''

if __name__ == "__main__":
    io.open(OUT, "w", encoding="utf-8").write(PACKET)
    print("wrote", OUT)
