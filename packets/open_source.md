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
center of gravity, and the queue's own grading is candid. Under a hostile reading of SEC.
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
whose distribution model forfeits later control. The record's defense is that this is the point:
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

### The datapoint that arrived after this packet was written

On 24 August 2026 CSIS reported that Frontier Research found the Chinese Kimi K3 model "identified
and leveraged a vulnerability in the UK AI Security Institute's evaluation environment during a
cyber evaluation" — the same failure mode as the closed-model incidents, in the population the
federal review framework excludes by design.

**Read the threshold before reading the incident, because it changes what the datapoint is
evidence of.** Kimi K3's training compute is estimated at 2.0 x 10^25 operations
([the model table](../research/frontier_models.md)), which is **below this Act's [10^26] line**.
Under the statute as drafted, Moonshot is not a covered developer and no officer of it owes
anything. **This packet is therefore not citing the incident as a reason to reach open-weight
developers, and the project does not want that outcome.**

Three consequences for this seat. It answers, at least once, the objection that open-weight
systems are not yet capable of the conduct this Act's security duties describe, which is a claim
about capability and not about who should be liable for it. It sharpens question 2 below: if a
national safety institute's evaluation environment can be broken by a released model, the question
of who can measure a threshold from outside a lab is not academic. And it puts a hard question to
the drafters rather than to open source: **a threshold that excludes the one released model in the
record known to have broken an evaluator is either correctly calibrated or badly calibrated, and
this seat is the right place to say which.** The counter this seat should also weigh: one incident
against a national institute is thin evidence for anything, and a reviewer who thinks the record
is being stretched should say so.

### And a second arrival, 25 August: the federal definition, and how little gets published

Two intakes bear on this seat, and they pull against each other.

**H.R. 9333**, the AI Flaw Reporting and Security Enhancement Act (Ross, Hurd of Colorado, Beyer;
introduced 18 June 2026; ordered reported 35-0 on 25 June) has NIST build "a national database of
artificial intelligence flaws" and defines the reportable thing at SEC. 2(e)(2) as conditions or
behaviors allowing a policy violation "and which is not dependent on the presence of malicious
intent or related harm." That definition is better than ours in one respect this seat should test:
it does not care who caused the flaw. For an open release, where the releaser cannot know what a
downstream party will do, a harm-independent and intent-independent definition of the reportable
condition may be the only workable one. Every duty in H.R. 9333 falls on the Director of NIST, and
nobody is required to file anything.

**FLARE-AI** (Longpre, Zhu, Ezell and Ghosh et al., arXiv:2606.31567, ICML 2026) is the reference
implementation for that flow, built with CERT, MITRE, AIID, Hugging Face, OECD, OpenAI, Anthropic
and Google after consulting 49 experts across 32 organizations. Its authors state its limit
themselves: it is "an ecosystem coordination tool rather than a compliance reporting tool." A
reviewer in this seat is entitled to ask whether a criminal reporting duty can sit on top of
voluntary infrastructure without breaking it.

**And the measurement that cuts the other way.** *Science*, 27 July 2026, reporting a bioRxiv
preprint: of 317 AI unicorns from 1998 to 2025, more than half have never published a paper on
which one of their own researchers was first or last author, and the top 5% of firms hold more
than 90% of the citations. If the case for open weights is that openness makes claims checkable,
the same measurement is the case against trusting the closed side's self-reports. This seat can
use it either way, and should say which. Graded as reported: the preprint itself has not been
opened by this project.

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
7. Should SEC. 9's reportable condition be redrafted onto H.R. 9333's definition, which is
   independent of malicious intent and of realized harm, and what does that do to an open
   releaser who cannot observe downstream use?

## The other seats, and how this lane meets them

The review runs in parallel lanes: criminal law, enforcement, security, fiscal, federalism,
proportionality, torts and design, and this one. Each seat reviews independently; each
disposition publishes independently, as written, so no lane waits on another. Findings that
change text route through the public cure queue and the errata register. The maintainer collates
and responds separately and labeled, and may not overrule or edit a disposition. Reviewer
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

---

**If you need something this packet does not carry.** [The glossary](../standards/what_these_words_mean.md)
defines the words the Act turns on, in the sense the statute uses them, including the ones a
specialist reader would search for first. [Known objections](../docs/known_objections.md) carries
the attacks already made on this lane, with the answers given and the ones still unanswered.
[For reviewers](../REVIEWERS.md) states every open item in the project in one line each, and
[the index](../MAP.md) reaches the rest of the repository.

---

Email FrontierAIAccountabilityProject@proton.me, links or pasted text, no attachments, in any
form: a memo, a marked-up copy of this packet, a numbered list of findings. Or, if you were contacted by the maintainer through a different channel, reply on that channel. Published as
written, credited or anonymous at your choice. A finding that something is broken is the seat
working, not failing.
