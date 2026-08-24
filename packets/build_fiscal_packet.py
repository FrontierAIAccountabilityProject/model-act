#!/usr/bin/env python3
"""Assemble packets/fiscal.md — the fiscal lane's reading copy.

Run from the repository root:  python3 packets/build_fiscal_packet.py

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

OUT = "packets/fiscal.md"

PACKET = r'''# The fiscal lane — one page

*A reading copy for the fiscal seat: what enforcing this Act costs, on what rules the costing is made, and where the arithmetic is still owed. Assembled 24 August 2026; linked from the reviewer surfaces when the current review freeze lifts. Sources are [the fiscal note](../standards/fiscal_note.md), [the lane sweep](../audit/v3_5_lane_sweep.md), [the bill census](../standards/frontier_bill_census.md), [the forecasters' arithmetic](../research/forecast_arithmetic.md), and [the errata register](../ledger/errata.md). Those files are the authority; this page exists so the lane can be read, printed, and marked up as one document. If this page and a source differ, the source is right and the difference is a defect worth reporting to FrontierAIAccountabilityProject@proton.me.*

## The ask

One seat, one lane, scope in writing before work begins. Unpaid. **The floor:** the statute straight through, then this packet, then **three findings, verified or refuted, with reasons** — a complete and publishable disposition, perhaps six to eight hours. **The whole seat:** the menu below worked through in full — every question answered, every bracketed figure tested or replaced — roughly ten to twenty hours across eight weeks. Both are dispositions; both are published as written, including "approved with reservations," including hostile. **A disposition that refutes one finding is worth more to this project than a full pass that agrees with everything.**

Unlike the drafting lanes, this lane has no queue of cures to verify. The sweep's fiscal findings stand with **no drafted response — the seat is the response**. The note's own § 7 states the design intent: the brackets exist so that the reviewer's job is *"arithmetic on a stated basis, not invention from a blank page."*

## Read first — the statute itself

The tagged text is not reproduced here. Read `model_act_v3_4.txt` at the repository root. Your sections: **SEC. 3, SEC. 10(a) and (f), SEC. 11, and SEC. 12**, with [the fiscal note](../standards/fiscal_note.md) as the primary text and part D of [the drafting record, chunk 3](../audit/record.md#chunk-3) behind it.

---

## I. The rules the note is held to — and asks to be held to

The note opens with a standing rule, quoted so the seat can enforce it: **enforcement is never sold as self-funding, penalties are never booked as revenue, and startup costs are stated apart from steady state** ([the fiscal note](../standards/fiscal_note.md), head matter and § 6).

The revenue rule is the load-bearing one, and § 6 gives it three reasons stated plainly: the fund receives nothing until there is a successful action, and the Act is drafted to make successful actions rare; whistleblower awards under SEC. 11(a) are paid *from* the same fund at 10 to 30 per cent of sanctions collected, so a state that appropriates the fund to the Agency has two draws on one pool; and a regime whose budget depends on collections has a stated incentive to collect, which contradicts the Act's own argument that enforcement incentives should be legal rather than financial. The scoring posture the note asserts: *"cost is appropriated, recoveries are windfall, and the estimate is sound if not a dollar is ever collected."* Whether that posture is reportable in your state is question 1 below.

Structurally, the note traces cost to the provision that creates it. SEC. 3(b)'s no-pre-approval rule removes the licensing cost drivers — no application queue, no approval clock, no user-fee relationship — and § 5 names the two lines regimes of this kind discover after enactment: **re-adoption on amendment** (SEC. 3(a) converts a one-time rulemaking into a recurring one for any frequently revised incorporated standard) and **paywalled standards** (SEC. 3(a) requires incorporated material publicly available without charge, so an ordinarily-sold standard becomes a budget line or a declination).

## II. What the sweep found in this lane

*Reproduced from [the sweep](../audit/v3_5_lane_sweep.md) as carried at [REVIEWERS](../REVIEWERS.md); none yet fixed. All of it is contestable; contesting it is the seat.*

- The note carries **no dollar figure anywhere** — honest, and administratively fatal, because "indeterminate" is the label that sends a bill to interim study.
- Steady state exceeds startup, impossible on the statute's own clock.
- **No line for defending the Act**, though a first adopter's largest year-one legal cost is a pre-enforcement facial challenge.
- No corrections or judiciary impact section, which some states require before a felony bill is considered at all.
- The function table omits at least eight duties, including frontier-equivalent capability designation, the most technically demanding act in the Act.
- The whistleblower award is a mandatory entitlement on a fund that may be permanently empty.

The first finding has since acquired a partial answer, which is the next section.

## III. The first real-world price in the genre

On 24 August the note gained its § 6b: a state fiscal office has now priced an AI act. Colorado's Legislative Council Staff issued a fiscal note for SB 26-189 on 4 May 2026 — a **$100,403 General Fund appropriation**, **0.8 FTE** (an Assistant Attorney General for rulemaking and stakeholder engagement), **$120,596 total expenditures** with centrally appropriated costs stated separately, startup isolated to FY 2026-27, and out-year expenditures honestly zeroed ([the fiscal note § 6b](../standards/fiscal_note.md)).

The note is careful about what this does and does not do. It does not price this Act — Colorado's bill is a civil disclosure regime enforced by an existing office, while this Act stands up an Agency and a criminal docket — so the 0.8 FTE figure is *"a floor for the narrowest administrative posture, not an estimate."* What it supplies is the genre's method demonstrated on this subject matter: one named office, startup severed from steady state, revenue at zero. The seat's question 1 now has a comparative answer in hand: one state reported a note with numbers, and this is what its arithmetic looked like. Note the retrieval grade: the primary PDF is logged for the verification record's next update — **⚠**, this repository's flag for a claim recorded but whose primary is not yet retrieved, or (where marked forecast-grade) an estimate carrying its own published error bars rather than a fact; it appears again in § V and is explained only here.

## IV. What enforcement costs under each commencement posture

Fiscal consumes the enforcement seat's posture choices, because each has a price. The truth-telling, reporting, records, whistleblower, and administrative provisions operate **from the effective date**; the core SEC. 2 deployment duty begins at **provisional commencement after [180] days** on the SEC. 3(c)(4) interim standards, and the Agency's unfinished rulemaking does not postpone it ([the fiscal note § 3](../standards/fiscal_note.md); the commencement layers, and the copy error that hid them, are [E6](../ledger/errata.md#e6--commencement-the-copy-error-corrected-today)). So year one is startup-heavy — standards development at [2.0–3.0 FTE] plus contracted expertise, secure handling, intake systems — while the steady state from year two runs on report intake, whistleblower processing against the [180]-day act-or-declare clock (§ 4 calls it "the principal steady-state driver"), and standards re-adoption. The sweep's second finding — that the note's steady state exceeds its startup, impossible on the statute's own clock — is a direct check the seat can run on those two tables.

The Attorney General line is stated separately and deliberately unquantified: episodic, document- and expert-intensive matters against well-resourced defendants, with a first litigated case likely to cost materially more than later ones, and *"no amount is asserted here without a state-specific basis"* (§ 4). Whether that is a contingency figure or a reasoned non-quantification is question 3.

One posture cost the note does not carry at all, per the sweep: defending the Act. And one item the enforcement lanes would add to any posture: [CURE 7](../audit/v3_5_cure_language.md#cure-7--the-covered-frontier-enterprise-scope-follows-the-ecosystem-duty-follows-the-function), the covered-frontier-enterprise expansion, is ⚠ AMEND FIRST with seven amendments, and **the sweep's fiscal lane recommends sequencing it to v4 on administrability grounds — a recommendation the maintainer has not accepted**. That undecided recommendation is yours to press or withdraw (question 5). Note throughout that CURE 7 and everything else in the v3.5 queue is drafting, not law: **the tagged text is `model_act_v3_4.txt`**, and nothing in the queue is enacted.

## V. Why the entity fine cannot deter — the forecasters' magnitudes ⚠

The Act's premise is that entity fines are absorbed while decision-makers stay insulated. [The forecasters' arithmetic § 4](../research/forecast_arithmetic.md) prices that premise with the field's own projections, graded **⚠ forecast-grade** — serious estimates with published error bars, not facts, and the arithmetic is owned by that page, not this one. Two of its numbers suffice here: a projected $2.4T of industry CapEx over 2028, against a leading developer at $360B ARR growing at roughly 150 per cent annualised. Set the enacted penalty schedule beside that. [The census](../standards/frontier_bill_census.md) records the enacted siblings at **$1,000,000** for a first violation (Illinois; CA/NY/IL brackets all at $1M per [the donor note of 23 August](../REVIEWERS.md)), and the largest figure anywhere in the census — $20,000,000 per day, H.R. 9917 — attached to no personal consequence at all. The census's own conclusion: *"Penalty size and personal reach are not the same axis and do not move together."* Against balance sheets of the forecast shape, no fine a legislature would enact changes a decision — which is the fiscal half of the Act's argument for reaching the officer, and the reason the revenue rule in § I is not merely accounting hygiene: a fine that cannot deter certainly cannot fund.

## VI. The question menu

Any three answered are a disposition; all of them, with the sweep's six findings verified or refuted, are the seat done whole. Replace any with findings of your own — a defect of your own discovery outranks the menu.

1. **Is a note with no numbers reportable in your state?** What would you need to make it so? Colorado's § 6b arithmetic is the comparator in hand.
2. **Every bracketed figure** — the FTE ranges are structural defaults, not comparator-derived estimates; the note's § 7 calls them "the item most in need of replacement."
3. **The Attorney General line** — contingency figure or reasoned non-quantification?
4. **The paywall exposure and the fund election** (note §§ 5–6) — stated line or conditional note; and should the appropriated-to-Agency election carry a drafting warning of the SEC. 11 interaction?
5. **Should CURE 7 be sequenced to v4 on administrability grounds**, as the sweep's fiscal lane recommends and the maintainer has not accepted?
6. **Comparator selection** — whether any of the CA/NY/IL siblings carried a published fiscal note, and what it assumed; the note's § 7 judges pinning one "worth more than refining the brackets."

## The other seats, and how this lane meets them

The review runs in parallel lanes — criminal law (under review now), enforcement, security, fiscal, proportionality, federalism, torts/design, with open-source gated separately. Each seat reviews independently, and each disposition publishes independently, as written, so no lane waits on another. Findings that change text route through the public cure queue and the errata register, where every other lane sees them. The maintainer collates and responds separately and labelled, and may not overrule or edit a disposition. Anonymous outside contributions arrive through the repository's correction doors and are credited by election — one open drafting question has already been answered from outside this way. Reviewer identities are not shared between reviewers, and attribution is each reviewer's own election.

This lane's particular seam: fiscal consumes the enforcement seat's posture choices — each has a price — and disciplines every other lane, because the penalties-never-booked-as-revenue rule keeps the proportionality conversation honest, and a costing error found here propagates into every sponsor conversation the project ever has ([paths to enactment](../docs/paths_to_enactment.md) already cites the 0.8 FTE floor in its attorney-general vehicle).

## What to attack

The revenue rule's third reason, if you think a collections-funded regime can be run honestly. The claim that SEC. 3(b) removes the major preclearance cost drivers, if you know a no-approval regime that got expensive anyway. The Colorado floor, if you think a disclosure-regime comparator misleads more than it anchors. The steady-state tables, which the sweep says cannot exceed startup on the statute's own clock and do. The missing defence line, the missing corrections section, the eight omitted duties, the entitlement on the possibly-empty fund. And the § 5 opposition claim that compliance becomes *"verifiable in seconds"* — if that is right, the note overstates its own steady state and should say by how much.

File a disposition to FrontierAIAccountabilityProject@proton.me — links or pasted text, no attachments — in any form: a memo, a marked-up copy of this packet, a numbered list of findings. Or, if you were contacted by the maintainer through a different channel, reply on that channel. It is published as written, credited or anonymous at your choice. A finding that something is broken is the seat working, not failing.
'''

if __name__ == "__main__":
    io.open(OUT, "w", encoding="utf-8").write(PACKET)
    print("wrote", OUT)
