# The open source and academia lane — one page

*A reading copy for the open-source and academic seat, assembled 25 August 2026. This lane was
deliberately gated behind the others: its questions cut against the statute's own convenience,
and the project wanted its answers to the other lanes on the record first. Sources are [the
drafting queue](../audit/v3_5_cure_language.md), [the two definitions page](../docs/the_definition.md),
[the bill census](../standards/frontier_bill_census.md), [the standing watch](../audit/standing_watch_2026-08-20.md),
and [the half-statute record](../docs/safe_harbors_and_affirmative_defenses.md). Those files are
the authority; if this page and a source differ, the source is right and the difference is a
defect worth reporting to FrontierAIAccountabilityProject@proton.me.*

*The ⚠ mark, preserved wherever the sources carry it, means a claim recorded from reporting or
an official summary whose primary instrument is not yet retrieved. The record grades itself;
this packet does not upgrade what its sources have not.*

## The ask

One seat, one lane, scope in writing before work begins. Unpaid. **The floor:** the statute
straight through, then this packet, then **three findings, verified or refuted, with reasons**, a
complete and publishable disposition, perhaps six to eight hours. **The whole seat:** the menu
worked through in full, roughly ten to twenty hours across eight weeks. Both are dispositions;
both are published as written, including hostile. **A disposition that refutes one finding is
worth more to this project than a full pass that agrees with everything.**

This lane exists because the statute's sharpest unresolved scope question is about released
weights, and the people best placed to attack it are the people who release them.

## Read first — the statute itself

The tagged text is not reproduced here. Read [`model_act_v3_4.txt`](../model_act_v3_4.txt) at
the repository root. Your sections: **SEC. 1(b)** (the covered-system definition and its lineage
rule), **SEC. 1(c)** (the release limb of the nexus), and the weight-security and pre-release
evaluation duties, with [the two definitions page](../docs/the_definition.md) behind the
threshold arithmetic.

---

## I. The question this lane owns: what does a release reach?

[CURE 13](../audit/v3_5_cure_language.md#cure-13--sec-1b1b-say-sever-not-extend) is the lane's
centre of gravity, and the queue's own grading is candid. Under a hostile reading of SEC.
1(b)(1)(B) as tagged, a downstream fine-tune of any released open-weight frontier model is
itself a covered system, which would put an open release's entire derivative tree inside the
Act. The drafted repair says **sever, not extend**: a derivative counts only when its own
lineage crosses the line. The repair is a proposal, not enacted text, and verifying or refuting
it is a finding. The questions underneath it are the ones an open-weight practitioner will see
fastest: whether lineage-compute accounting is even well defined across merges, distillations,
and continued pretraining; whether the [10²⁶] line is measurable by anyone outside the releasing
lab; and whether the release limb of SEC. 1(c), which reaches a person who "releases weights"
into the State, can be squared with the reality that a release is to everywhere at once.

## II. The asymmetry the record must defend

The Act's duties bind hardest before release: pre-release evaluation, weight security,
designation. An open release, once made, moves the model beyond the developer's power to
secure or recall, so the statute's architecture in effect asks the most of exactly the actors
whose distribution model forfeits later control. The record's defence is that this is the point:
the decisions that matter are the ones made while control still exists, and the officer who
signs is signing about that moment. The obvious counter, which this seat is invited to press, is
that the same architecture makes closed deployment the compliance-cheap path and taxes openness
as such, an outcome the project does not want and has not yet shown its text avoids. Nothing in
the tagged text or the queue resolves this cleanly. **Contesting or confirming the asymmetry is
the seat's largest single question.**

## III. The weather, which cuts both ways here

The federal review framework reported on 4 August 2026 ⚠ covers **closed models only**; open
models are excluded by design, with the reporting noting that could change ([the standing
watch](../audit/standing_watch_2026-08-20.md), 24 Aug addendum; primaries queued). Read one way,
that is space: whatever a state statute says about released weights, it is not saying it into a
field Washington has occupied. Read the other way, it is a warning: the federal exclusion
reflects a judgment that open-weight oversight is not yet tractable, and a state criminal
statute claiming otherwise carries the burden of showing its tools are real. The census's
convergence finding, that H.R. 8094 adopts the same lineage-compute counting above the same
[10²⁶] line, sits on the first side of that scale; the incident record of this summer, in which
agents built from released and closed systems alike escaped their evaluators ⚠, sits wherever
this seat says it sits.

## IV. The question menu

Any three answered are a disposition; all of them, with CURE 13's repair verified or refuted,
are the seat done whole. Replace any with findings of your own.

1. Does CURE 13's sever-not-extend repair actually close the derivative-tree reading, and is
   lineage-compute accounting well defined across merges, distillation, and continued
   pretraining?
2. Can anyone outside a releasing lab measure the [10²⁶] threshold, and what would an
   enforcement-grade measurement even look like?
3. Is the release limb of SEC. 1(c) coherent, given that a weight release is not directed at
   any state, and does the drafted nexus survive it?
4. Does the Act tax openness as such (§ II), and if so, what text would remove the tax without
   removing the duty?
5. Is the pre-release evaluation duty writable for an open release at all, and what would its
   conditions-of-evaluation clause need to say (the incident record of May to July 2026 is the
   live case)?
6. The academic half of the seat: what does the statute owe the research exemption, and does
   any current text distinguish a university fine-tune from a commercial one, and should it?

## The other seats, and how this lane meets them

The review runs in parallel lanes: criminal law, enforcement, security, fiscal, federalism,
proportionality, torts and design, and this one. Each seat reviews independently; each
disposition publishes independently, as written, so no lane waits on another. Findings that
change text route through the public cure queue and the errata register. That queue is how v3.4 becomes v3.5: each lane's verified findings are drafted as cures against the tagged text, and the assembled v3.5 carries every lane's accepted work, so a disposition here is a chapter of the next version, written alongside the other seats'. The maintainer collates
and responds separately and labelled, and may not overrule or edit a disposition. Reviewer
identities are not shared between reviewers, and attribution is each reviewer's own election.

For this lane specifically: security is the adjacent seat, because weight security and open
release are one question seen from two sides; and the federalism seat's ceiling analysis (§ III)
depends in part on how this lane answers question 3.

## What to attack

In descending order of consequence: the derivative-tree reading and its drafted repair; the
openness tax of § II; the measurability of the threshold from outside; the release limb of the
nexus; and the research exemption's absence. A finding that the Act cannot be drafted fairly for
open weights at all would be the most consequential disposition any lane has produced, and it
would be published like every other.

Email FrontierAIAccountabilityProject@proton.me, links or pasted text, no attachments, in any
form: a memo, a marked-up copy of this packet, a numbered list of findings. Or, if you were contacted by the maintainer through a different channel, reply on that channel. Published as
written, credited or anonymous at your choice. A finding that something is broken is the seat
working, not failing.
