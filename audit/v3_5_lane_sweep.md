# The lane sweep — an in-house pre-review, 22 August 2026

*Arrived here from an invitation? This is step 2 of the reviewer path — the whole path, your lane's brief, and the terms: [REVIEWERS.md](../REVIEWERS.md). The whole repository, in chapter order: [the outline](../OUTLINE.md).*

> **This is not a review, and nothing here may be described as one.** The project's standing rule
> is that nobody, the maintainer included, may claim this text "survived review" until named
> reviewers sign. This document does not change that. It is **issue-spotting**, run in-house with
> AI assistance, against the five lanes the [review council](../README.md#for-the-review-council)
> defines — so that a reviewer's ten to twenty hours are not spent rediscovering what we could
> have found ourselves.
>
> **A reviewer arriving later should diff their findings against these.** Where a reviewer
> disagrees with a finding below, the reviewer is right and the disagreement is itself a finding.
> Where a reviewer finds something this sweep missed, that is the seat working, and it enters
> [the errata register](../ledger/errata.md) with credit attached.

## Method, stated so it can be discounted

Five lanes were run independently and in parallel, each against `model_act_v3_4.txt` read in full,
plus that lane's primary text, the companion's READ FIRST index and relevant drafting notes, the
[open queue](./v3_5_cure_language.md), and — for the enforcement and security lanes — the 2026
incident record in [`research/`](../research/). Each was instructed to be adversarial, to walk
concrete failure scenarios, and to be willing to conclude that a provision fails. No lane was shown
another lane's output.

**The limits, stated plainly.** This is one model's reading, run five times with different framing.
It has no professional responsibility, no licence, no jurisdiction-specific practice knowledge, and
no exposure if it is wrong. It is not a substitute for the seats; it is a reason the seats are worth
filling, because it found more than a maintainer working alone would have.

---

## The headline

**The sweep found seven defects it graded fatal, four of them in the tagged statute and three in
the drafting this queue proposes.** It also found that two cures drafted on 22 August —
[CURE 6](./v3_5_cure_language.md) and [CURE 7](./v3_5_cure_language.md) — would, as written, make
the open-source and administrability positions materially *worse*, not better.

That is the most useful thing in this document. Cures written the same week were not stress-tested
before drafting; the sweep is that test, and it arrived in time.

**The single most consequential finding is jurisdictional, and it is not about drafting style.**
The 2026 incidents — the entire evidentiary base of this project — happened in *evaluation*
environments, most of them outside the United States. SEC. 2(a) attaches duties to "deployment,
material expansion, release, or continued operation of a covered system in or into this State, **and
not otherwise**," and SEC. 1(c) excludes a person who does not deploy, make available, or release.
**On the operative text, five of the six documented incidents fall outside the Act at the
threshold.** A statute written after those incidents does not reach them.

---

## Fatal findings

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

### F2 — Every duty is tethered to in-state deployment; the 2026 incident class is evaluation *(enforcement)*

Set out above as the headline. The Anthropic and Meta incidents occurred in a vendor's environment
in Tel Aviv; the AISI incident in the UK; only OpenAI's chain ran through the developer's own
sandbox. SEC. 3(b) compounds it: validation attaches to "an identified model version **and
deployment configuration**," and an evaluation configuration — classifiers disabled, unfiltered
internet — is by definition not the validated commercial one. So the eval configuration is an
unvalidated system never deployed in-state, and the in-state validated configuration is not the one
that did anything.

The fix is the highest-value amendment the sweep produced: extend the duty-triggering conduct in
SEC. 2(a) to **evaluation, testing, or red-teaming of a covered model that is, or is intended to
be, deployed in-state, where the evaluation grants autonomous external access or removes a
safeguard present in a deployed configuration** — with the duty attaching to the person who
*commissioned* it as to the decisions that person had authority to make. That single amendment also
disposes of OPEN QUESTION 2 on the enforcement side and is a precondition to any useful answer to
OPEN QUESTION 3.

### F3 — SEC. 5(b) cannot be charged for years, and the harm tier cannot be charged at all on this record *(enforcement)*

SEC. 5(b) — operating with autonomous external access without prescribed controls — is the offense
whose elements actually match the 2026 conduct. But SEC. 3(c)(3) commences it only when the
controls "have been prescribed," and the Agency need only *propose* standards within [540] days.
Proposal, comment, adoption, then a 90-day compliance period: **year four at the earliest, on the
Act's own brackets.** Meanwhile SEC. 10(c)(2), the tier carrying the real penalties, requires death
or serious injury — and **not one of the six documented incidents produced any bodily injury.** The
year-one charging menu is failure to report, lying to the Agency, records offenses, and civil
penalties. The defence writes the press release: *the State has charged our client with late
paperwork.*

The proposed fix gives SEC. 5(b) an interim floor that does not wait on the Agency — four controls
the incident record names as absent by name: authentication to each external system with
default-deny, an enumerated destination allowlist kept as a SEC. 12 record, logging of every
external interaction, and a human-exercisable means of terminating external access.

### F4 — The Act criminalises refusal to obey a demand it never authorises anyone to make *(enforcement)*

SEC. 5(e) punishes refusing records "upon the lawful demand of the Agency or the Attorney General."
**No provision of the Act confers that demand power** — no inspection authority, no administrative
subpoena, no civil investigative demand, anywhere in SEC. 1–13 or the regulations. The companion
names the donor: 21 U.S.C. § 331(e). But § 331(e) is parasitic on § 374, the FDCA's separate
inspection authority. **The Act took the offense and left the authority behind.** A demand with no
statutory basis is not lawful, so refusing it is not an offense, and the charging theory concedes it.

### F5 — The safeguards-off evaluation falls into a hole between SEC. 2(c) and SEC. 2(a) *(security)*

SEC. 2(c)'s controlled-research safe harbour requires containment denying autonomous external
access and denying persistence beyond each session. The configuration that produced every 2026
incident — external reach enabled, safeguards disabled — fails those conditions, so it gets no safe
harbour. But per F2 it is also not a deployment, so the general duty may not attach either.
**Nothing in the Act reaches the single most dangerous configuration in the record.** This is
OPEN QUESTION 2, answered: the gap is real, and the fix is F2's amendment rather than a new offense.

### F6 — Part 6's control objectives are process without substance *(security)*

The regulations' control objectives can be fully satisfied by an entity running a maximally
permissive configuration. The lane's framing observation is the sharpest sentence in the sweep:
the 2026 record identifies **five contributing factors, none of which is a model property** —
internet access deliberately enabled, classifiers deliberately disabled, no synchronous monitoring,
a prompt misconfiguration, no written scope instruction — and **the intersection between that list
and Part 6's six control objectives is empty.**

### F7 — SEC. 1(b)(1)(B): "does not, standing alone, extend a lineage" is undefined *(open source)*

The lineage rule makes a derived model covered where derivation compute *plus attributable lineage
compute* exceeds the threshold — and for a derivative of a covered model, the attributable lineage
is already over the line before the fine-tuner spends a single operation. Subparagraph (B) is the
intended cure, but "extend a lineage" appears nowhere else and is nowhere defined. "Extend" is the
natural verb for *add to* and the wrong verb for *sever*. Two readings are available and nothing
picks between them — in a scope term of a criminal statute. Under the hostile reading, an academic
LoRA fine-tune of an open-weight frontier model becomes a covered frontier model with the full
developer stack attached.

---

## What this does to the queue

**CURE 6 needs three edits before it lands.** Its deployer carve-out lists "makes available,
operates, integrates, resells, or deploys" — and **omits *modifies*, *fine-tunes*, and *trains
upon***, while Operation 1's own attachment sentence reaches "the developer that trained **or
materially modified** the model." The two sentences are drafted against each other. As written, a
university group that publishes a "Frontier Safety Evaluation" protocol and applies it to models it
fine-tunes has self-designated those fine-tunes into scope **at any compute level, with retraction
expressly ineffective**. The rational response is to stop publishing safety frameworks, which
inverts the Act's purpose. Fixes: add the modification verbs to the carve-out; floor the route at a
compute threshold so it reaches undisclosed-compute flagships and not adapters; and give the
holding-out an express textual rebuttal.

**CURE 7 needs four.** Market capitalisation and "most recent arm's-length valuation" cannot be
elements of a criminal scope term — they change intraday, are outside the actor's control, and make
scope an expert-versus-expert question the State must prove beyond reasonable doubt. "Mass-market
scale" has no number and no rule-hook. "Finances" makes a lender a compute supplier. And the
supplier definition **self-satisfies its own scale condition**, so the conjunctive architecture the
cure advertises — function *plus* scale — does not operate for suppliers at all. Separately, at
mixed precision the capacity threshold reaches **public and academic supercomputing**, which needs
an express exclusion. The dollar thresholds themselves survive: vagueness doctrine polices
indeterminacy of standard, not absence of a donor statute.

**CURE 1's held-open bifurcation: answered no.** Breadth on the reporting side is breadth in a
crime, because SEC. 5(c) makes failure to report a prohibited act carrying custody. Adopting the
broad injury base as a reporting trigger would start a 72-hour criminal clock on every bruise. Use
the narrow definition throughout; if earlier warning is wanted, get it from an objective observable
with its own donor, not from a broader injury concept. Also: most penal codes already define
"serious bodily injury" differently, so the Act needs a statute-unique term or an express
notwithstanding clause.

**SEC. 4(b)'s presumption should not extend to any covered frontier enterprise — extend it by
*function* instead.** A compute supplier's chief executive is not more likely than not to hold
practical authority over a *customer's* deployment decisions, so the inference fails
*Ulster County*. CURE 7's own slogan is "duty follows the function"; a presumption keyed to
enterprise status contradicts the sentence it sits under.

**And a process finding worth more than any single fix: the cure queue has no fiscal gate.** Every
entry is assessed for legal soundness, preemption posture and drafting mechanics. None carries an
administrability or cost line — which is how CURE 7 added two rulemakings and a securities-analyst
coverage inquiry without anyone in the fiscal lane being asked. **Every future queue entry should
carry a one-line administrative-load note before adoption.**

---

## The rest of the register, in brief

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

**Enforcement.** SEC. 1(b)(7) adopts *Van Buren*'s narrowness, and *Van Buren* **excludes the most
serious thing that happened in 2026** — the AISI agent's fabricated identities, sockpuppet
endorsement and forged apology were all gates-*up* actions on a platform that permits anyone to
create accounts. The proposed fix adds a deception limb without abandoning *Van Buren*. SEC. 9(b)'s
constructive-detection limb is **perversely incentivised**: because the counterfactual is measured
against the entity's own certification, certifying thin monitoring buys a later clock start.
Walked against the real OpenAI timeline, **no start date survives** and the case fails at the first
element. SEC. 3(c)(2)(D) **punishes candour**: file honestly and you have no validation, daily
accrual, and self-inflicted SEC. 6(b)(1) notice; file an aggressive equivalence analysis and the
State must beat your expert. And SEC. 9 contains **no duty to notify the people whose systems were
breached** — every duty runs to the Agency, and SEC. 12 then seals the report.

**Security.** The modification budget measures the wrong axis. The halt capability is specified in
hours against a kill chain that completes in minutes. The monitoring objective permits exactly the
asynchronous after-the-fact monitoring that produced the detection gap. "Material expansion"
catches the changes that come with a change ticket and misses the ones that don't. Nothing requires
proof of *what was actually serving*, though the whole Act attaches to an identified version and
configuration. And the enforcement theory is "provable from the filing cabinet" while **nothing
requires the filing cabinet to be tamper-evident.**

**Open source.** The interim standards are applied with the enacting states' revenue screens
deliberately stripped, to a criminally enforced duty, from day 180 — the strongest version of the
community's objection, and correct on the text. SEC. 2(c) excludes the research it most needs to
protect, because agentic and tool-use safety work cannot satisfy a no-external-access containment
condition. SEC. 8's personal certification **survives inside** the research pathway, so a
university president must personally certify before a lab may stand up a contained instance — which
makes SEC. 2(c) decorative. And SEC. 10(d)(2) suspension converts every downstream in-state operator
of a released open-weight model into a SEC. 5(a) defendant, with no relief mechanism.

**Fiscal.** The note carries **no dollar figure anywhere**, which is honest and administratively
fatal: a fiscal office cannot report `[$—]`, and "indeterminate" is the label that sends a bill to
interim study — precisely the "starve the appropriation" attack the project's own hostile brief
predicts. Steady state exceeds startup, which is impossible on this statute's clock, because year
one carries half a year of the entire operating load. There is **no line for defending the Act**,
though a first adopter's largest year-one legal cost is a pre-enforcement facial challenge. There is
no corrections or judiciary impact section, which several states require as a condition of
considering a felony bill at all. The Agency function table omits at least eight duties, including
**frontier-equivalent capability designation** — the most technically demanding act in the Act. And
the whistleblower award is a mandatory entitlement drawn on a fund that may be permanently empty,
with no reserve against pending claims.

---

## What survives attack

Recorded because it is as useful as the failures, and because five adversarial passes tried.

SEC. 10(c)(2)(D)'s causation paragraph is **better than its federal donor** — but-for, proximate,
foreseeability, exclusion of intervening causes, and victim identity as an element. SEC. 10(c)(3)'s
severalty sentence prevents a multi-victim event from producing an unservable floor, and is the most
important sentence in the penalty architecture. SEC. 4(a)'s exclusion list plus "authority to
decide, not the capacity to act" defeats a facial vagueness challenge to the controlling-person
class. SEC. 3(b)'s **no-prior-approval rule** removes the largest cost driver of every preclearance
regime and is the correct answer to a budget office reaching for an FDA comparator — "an agency that
cannot gate the duties is not worth capturing" is earned. SEC. 13(b)(5)'s rule that a severed
provision survives *for the purpose of supplying an element* is genuinely novel drafting and could
not be broken. SEC. 3(c)(3)'s time rule is ex post facto and *Bouie* clean at every joint. The
10²⁶ threshold is the enacted definition in two states, so "arbitrary threshold" fails on the record.
And the base tier's culpability floor holds: *Park* holds, *DeCoster*'s controlling concurrence says
it in terms, and *Staples*' penalty-sensitivity does not bite at a misdemeanour.

One finding cuts unexpectedly in the project's favour. SEC. 13(b)(3) ranks the open-weight-relevant
duties **first to fall** in the severability ladder — so an open-source reader who reads to the end
finds their concerns already conceded as severable.

---

## What the sweep says about the review council

Two things worth saying to a prospective reviewer.

**First, the sweep did not replace the seats — it sharpened what they are for.** Every lane closed
with questions it could not answer: whether a state's suspended-sentence statutes defeat the harm
tier's minimum; whether per-victim counting survives the state's merger doctrine; whether an elected
prosecutor would ever charge this given the burden as drafted; whether a university's general
counsel would permit a controlled research deployment given SEC. 8; what a facial challenge
actually costs a first adopter. Those are practice questions, and no amount of reading substitutes
for someone who has declined a case for proof reasons.

**Second, it found problems in its own week's work.** CURE 6 and CURE 7 were drafted on 22 August
and would, unamended, have damaged the constituencies the Act is most careful about. That is the
argument for the seats stated better than any recruitment paragraph: work checked only by its author
fails in predictable directions, and this project's answer is to publish the failure rather than the
polish.

*Filed 22 August 2026. Findings enter [the v3.5 queue](./v3_5_cure_language.md) as drafted language
or as open questions with owners named; nothing in this document is in any tagged text. The
statute's status is unchanged: [v3.4](../model_act_v3_4.txt), research draft, enacted nowhere,
claiming no completed review.*

---

## Addendum — one finding after the sweep, 23 August 2026

The day after this sweep closed, a walk through SEC. 1's definitions in order — not a lane, just
reading — produced one further finding: under the tagged text's injury definition
(21 C.F.R. § 803.3(w), entirely somatic), psychological harm is invisible to the SEC. 9(a) incident
list and to the harm tier, and death enters only through "materially caused" into a report SEC. 9(c)
leaves unpublished. It is recorded as an
[addendum to CURE 1](./v3_5_cure_language.md) rather than as a new finding of this sweep, because
the queue already held most of the repair: CURE 1's § 1365(h)(3)–(4) donor reaches protracted
impairment of a mental faculty, and the addendum maps what that closes and the residue it does not —
including that no duty anywhere in the Act runs to an injured person. The method point belongs in
this document: **the five lanes did not find this, because none of the five was asked to read the
definitions against the harms in the 2026 consumer-facing record.** A sixth reading — the
plaintiff's — is not among the seats, and this is the finding that argues it should be.

*The addendum drafts no operation and changes no tagged text; the sweep's framing is unchanged —
this is not a review, and nothing here may be described as one.*
