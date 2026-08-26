---
title: "The internal review — an in-house pre-review, 22 August 2026"
parent: Revision
nav_order: 3
---

# The internal review — an in-house pre-review, 22 August 2026

*Arrived here from an invitation? This is step 2 of the reviewer path — the whole path, your topic's brief, and the terms: [REVIEWERS.md](./worklist.md). The whole repository, in chapter order: [the map, Part I](../README.md).*

> **This is not a review, and nothing here may be described as one.** The project's standing rule
> is that nobody, the maintainer included, may claim this text "survived review" until named
> reviewers sign. This document does not change that. It is **issue-spotting**, run in-house with
> AI assistance, against the five topics the [review council](../revision/worklist.md)
> defines — so that a reviewer's ten to twenty hours are not spent rediscovering what we could
> have found ourselves.
>
> **A reviewer arriving later can diff their findings against these.** Where a reviewer
> disagrees with a finding below, the reviewer is right and the disagreement is itself a finding.
> Where a reviewer finds something this sweep missed, that is the reviewer working, and it enters
> [the the corrections register](../corrections/corrections.md) with credit attached.

## Method, stated so it can be discounted

Five topics were run independently and in parallel, each against `model_act_v3_4.txt` read in full,
plus that topic's primary text, the Comments's Open issues index and relevant drafting notes, the
[open queue](./proposals.md), and — for the enforcement and security topics — the 2026
incident record in [`research/`](../appendix/). Each was instructed to be adversarial, to walk
concrete failure scenarios, and to be willing to conclude that a provision fails. No topic was shown
another topic's output.

**The limits, stated plainly.** This is one model's reading, run five times with different framing.
It has no professional responsibility, no license, no jurisdiction-specific practice knowledge, and
no exposure if it is wrong. It is not a substitute for the reviewers; it is a reason the reviewers are worth
filling, because it found more than a maintainer working alone would have.

---

## The headline

**The sweep found seven defects it graded fatal, four of them in the tagged statute and three in
the drafting this queue proposes.** It also found that two cures drafted on 22 August —
[Amendment 6](./proposals.md) and [Amendment 7](./proposals.md) — would, as written, make
the open-source and administrability positions materially *worse*, not better.

That is the most useful thing in this document. Cures written the same week were not stress-tested
before drafting; the internal review is that test, and it arrived in time.

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
text is in the topic's working notes; the shape is (1) practical power, (2) failure of due care in
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

The fix is the highest-value amendment the internal review produced: extend the duty-triggering conduct in
SEC. 2(a) to **evaluation, testing, or red-teaming of a covered model that is, or is intended to
be, deployed in-state, where the evaluation grants autonomous external access or removes a
safeguard present in a deployed configuration** — with the duty attaching to the person who
*commissioned* it as to the decisions that person had authority to make. That single amendment also
disposes of Decision 2 on the enforcement side and is a precondition to any useful answer to
Decision 3.

### F3 — SEC. 5(b) cannot be charged for years, and the harm tier cannot be charged at all on this record *(enforcement)*

SEC. 5(b) — operating with autonomous external access without prescribed controls — is the offense
whose elements actually match the 2026 conduct. But SEC. 3(c)(3) commences it only when the
controls "have been prescribed," and the Agency need only *propose* standards within [540] days.
Proposal, comment, adoption, then a 90-day compliance period: **year four at the earliest, on the
Act's own brackets.** Meanwhile SEC. 10(c)(2), the tier carrying the real penalties, requires death
or serious injury — and **not one of the six documented incidents produced any bodily injury.** The
year-one charging menu is failure to report, lying to the Agency, records offenses, and civil
penalties. The defense writes the press release: *the State has charged our client with late
paperwork.*

The proposed fix gives SEC. 5(b) an interim floor that does not wait on the Agency — four controls
the incident record names as absent by name: authentication to each external system with
default-deny, an enumerated destination allowlist kept as a SEC. 12 record, logging of every
external interaction, and a human-exercisable means of terminating external access.

### F4 — The Act criminalizes refusal to obey a demand it never authorizes anyone to make *(enforcement)*

SEC. 5(e) punishes refusing records "upon the lawful demand of the Agency or the Attorney General."
**No provision of the Act confers that demand power** — no inspection authority, no administrative
subpoena, no civil investigative demand, anywhere in SEC. 1–13 or the regulations. The Comments
names the donor: 21 U.S.C. § 331(e). But § 331(e) is parasitic on § 374, the FDCA's separate
inspection authority. **The Act took the offense and left the authority behind.** A demand with no
statutory basis is not lawful, so refusing it is not an offense, and the charging theory concedes it.

### F5 — The safeguards-off evaluation falls into a hole between SEC. 2(c) and SEC. 2(a) *(security)*

SEC. 2(c)'s controlled-research safe harbor requires containment denying autonomous external
access and denying persistence beyond each session. The configuration that produced every 2026
incident — external reach enabled, safeguards disabled — fails those conditions, so it gets no safe
harbor. But per F2 it is also not a deployment, so the general duty may not attach either.
**Nothing in the Act reaches the single most dangerous configuration in the record.** This is
Decision 2, answered: the gap is real, and the fix is F2's amendment rather than a new offense.

### F6 — Part 6's control objectives are process without substance *(security)*

The regulations' control objectives can be fully satisfied by an entity running a maximally
permissive configuration. The topic's framing observation is the sharpest sentence in the internal review:
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

**Amendment 6 needs three edits before it lands.** Its deployer carve-out lists "makes available,
operates, integrates, resells, or deploys" — and **omits *modifies*, *fine-tunes*, and *trains
upon***, while Operation 1's own attachment sentence reaches "the developer that trained **or
materially modified** the model." The two sentences are drafted against each other. As written, a
university group that publishes a "Frontier Safety Evaluation" protocol and applies it to models it
fine-tunes has self-designated those fine-tunes into scope **at any compute level, with retraction
expressly ineffective**. The rational response is to stop publishing safety frameworks, which
inverts the Act's purpose. Fixes: add the modification verbs to the carve-out; floor the route at a
compute threshold so it reaches undisclosed-compute flagships and not adapters; and give the
holding-out an express textual rebuttal.

**Amendment 7 needs four.** Market capitalization and "most recent arm's-length valuation" cannot be
elements of a criminal scope term — they change intraday, are outside the actor's control, and make
scope an expert-versus-expert question the State must prove beyond reasonable doubt. "Mass-market
scale" has no number and no rule-hook. "Finances" makes a lender a compute supplier. And the
supplier definition **self-satisfies its own scale condition**, so the conjunctive architecture the
cure advertises — function *plus* scale — does not operate for suppliers at all. Separately, at
mixed precision the capacity threshold reaches **public and academic supercomputing**, which needs
an express exclusion. The dollar thresholds themselves survive: vagueness doctrine polices
indeterminacy of standard, not absence of a donor statute.

**Amendment 1's held-open bifurcation: answered no.** Breadth on the reporting side is breadth in a
crime, because SEC. 5(c) makes failure to report a prohibited act carrying custody. Adopting the
broad injury base as a reporting trigger would start a 72-hour criminal clock on every bruise. Use
the narrow definition throughout; if earlier warning is wanted, get it from an objective observable
with its own donor, not from a broader injury concept. Also: most penal codes already define
"serious bodily injury" differently, so the Act needs a statute-unique term or an express
notwithstanding clause.

**SEC. 4(b)'s presumption should not extend to any covered frontier enterprise — extend it by
*function* instead.** A compute supplier's chief executive is not more likely than not to hold
practical authority over a *customer's* deployment decisions, so the inference fails
*Ulster County*. Amendment 7's own slogan is "duty follows the function"; a presumption keyed to
enterprise status contradicts the sentence it sits under.

**And a process finding worth more than any single fix: the cure queue has no fiscal gate.** Every
entry is assessed for legal soundness, preemption posture and drafting mechanics. None carries an
administrability or cost line — which is how Amendment 7 added two rulemakings and a securities-analyst
coverage inquiry without anyone in the fiscal topic being asked. **Every future queue entry should
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

**And the objection the internal review could not raise against itself, supplied from outside it.** The
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

**Why this is in the internal review and not only in the objections file.** It is the one criticism of this
topic made in print, by name, by the scholar whose own state-by-state survey the Act cites for its
comparative claims. The topic's honest position is that the base tier answers it and the felony tier
may not: *Park* holds at the misdemeanor floor, and the internal review says so two sections down. What the
sweep does **not** have is an argument that the same authority reaches SEC. 6(b). **That gap is a
finding waiting to be made or refuted, and it is the single most valuable thing a criminal-law
reviewer could take up.** It is question 7 on the menu.

**Enforcement.** SEC. 1(b)(7) adopts *Van Buren*'s narrowness, and *Van Buren* **excludes the most
serious thing that happened in 2026** — the AISI agent's fabricated identities, sockpuppet
endorsement and forged apology were all gates-*up* actions on a platform that permits anyone to
create accounts. The proposed fix adds a deception limb without abandoning *Van Buren*. SEC. 9(b)'s
constructive-detection limb is **perversely incentivized**: because the counterfactual is measured
against the entity's own certification, certifying thin monitoring buys a later clock start.
Walked against the real OpenAI timeline, **no start date survives** and the case fails at the first
element. SEC. 3(c)(2)(D) **punishes candor**: file honestly and you have no validation, daily
accrual, and self-inflicted SEC. 6(b)(1) notice; file an aggressive equivalence analysis and the
State must beat your expert. And SEC. 9 contains **no duty to notify the people whose systems were
breached** — every duty runs to the Agency, and SEC. 12 then seals the report.

**And the gap the internal review did not find, supplied from outside it on 25 August 2026: the apex-witness
problem.** Every offense in SEC. 6 turns on what a natural person knew, decided, or had the power to
prevent. Nothing in this repository asks the practical question that follows: **can the State
actually get that person into a chair.** American courts apply an apex-witness rule that shields
senior executives from depositions unless the party seeking one shows unique, non-duplicative
personal knowledge. It is a discovery doctrine rather than a criminal-procedure one, but the
posture it creates — the corporation offering subordinates instead of the officer — is exactly the
posture a SEC. 6 prosecution would meet, and the Act's SEC. 5 records duties are the only thing in
it that would answer.

**There is one data point and it cuts our way, which is precisely why it must be stated carefully.**
In *Concord Music Group, Inc. v. Anthropic PBC*, No. 5:24-cv-03811 (N.D. Cal.), Magistrate Judge
Susan van Keulen ordered on **19 December 2025** that **Dario Amodei sit for a deposition**, capped
at two and a half hours and permitted to be taken remotely. Anthropic had argued he did not possess
unique knowledge of the company's model-training process. Per the reporting, the court found that
depositions of other Anthropic founders had established he was *"intimately involved"* in training
the models, and that those founders were unable or unwilling to testify to key information solely
within his knowledge.

**What that does and does not establish, and the second half matters more.** It establishes that a
federal magistrate, on evidence, found the chief executive of a frontier developer to hold personal
knowledge of how its models were trained that nobody else could supply. That is the factual premise
of SEC. 4 — practical authority is real and identifiable — found by a court rather than asserted by
us. It does **not** establish that he held final authority to prevent or halt anything, which is a
different question; it is civil discovery, not criminal liability; and it is fact-specific to the
point of fragility, since the finding rested on what his co-founders said under oath. A defendant
whose subordinates are better rehearsed produces the opposite result.

⚠ **The order has not been retrieved.** Everything above is from secondary reporting, and neither
source names the apex doctrine. **Nothing may be cited to the court's own words until the order is
in hand.** Retrieval item: the docket is public at CourtListener and the order is Document 378 or
560 in the Justia listing for 5:24-cv-03811.

**This is now question 7 of the enforcement topic**, and it is the one the maintainer most wants
answered, because it is unanswerable from reading: *if a State charged a controlling person under
SEC. 6, what would it actually take to obtain that person's testimony, and do the Act's records
duties do the work the apex rule otherwise makes a plaintiff do?*

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
it in terms, and *Staples*' penalty-sensitivity does not bite at a misdemeanor.

One finding cuts unexpectedly in the project's favor. SEC. 13(b)(3) ranks the open-weight-relevant
duties **first to fall** in the severability ladder — so an open-source reader who reads to the end
finds their concerns already conceded as severable.

---

## What the internal review says about the review council

Two things worth saying to a prospective reviewer.

**First, the internal review did not replace the reviewers — it sharpened what they are for.** Every topic closed
with questions it could not answer: whether a state's suspended-sentence statutes defeat the harm
tier's minimum; whether per-victim counting survives the state's merger doctrine; whether an elected
prosecutor would ever charge this given the burden as drafted; whether a university's general
counsel would permit a controlled research deployment given SEC. 8; what a facial challenge
actually costs a first adopter. Those are practice questions, and no amount of reading substitutes
for someone who has declined a case for proof reasons.

**Second, it found problems in its own week's work.** Amendment 6 and Amendment 7 were drafted on 22 August
and would, unamended, have damaged the constituencies the Act is most careful about. That is the
argument for the reviewers stated better than any recruitment paragraph: work checked only by its author
fails in predictable directions, and this project's answer is to publish the failure rather than the
polish.

*Filed 22 August 2026. Findings enter [the v3.5 queue](./proposals.md) as drafted language
or as open questions with owners named; nothing in this document is in any tagged text. The
statute's status is unchanged: [v3.4](../act/model-act.txt), research draft, enacted nowhere,
claiming no completed review.*

---

## Addendum — one finding after the internal review, 23 August 2026

The day after this sweep closed, a walk through SEC. 1's definitions in order — not a topic, just
reading — produced one further finding: under the tagged text's injury definition
(21 C.F.R. § 803.3(w), entirely somatic), psychological harm is invisible to the SEC. 9(a) incident
list and to the harm tier, and death enters only through "materially caused" into a report SEC. 9(c)
leaves unpublished. It is recorded as an
[addendum to Amendment 1](./proposals.md) rather than as a new finding of this sweep, because
the queue already held most of the repair: Amendment 1's § 1365(h)(3)–(4) donor reaches protracted
impairment of a mental faculty, and the addendum maps what that closes and the residue it does not —
including that no duty anywhere in the Act runs to an injured person. The method point belongs in
this document: **the five topics did not find this, because none of the five was asked to read the
definitions against the harms in the 2026 consumer-facing record.** A sixth reading — the
plaintiff's — is not among the reviewers, and this is the finding that argues it should be.

*The addendum drafts no operation and changes no tagged text; the internal review's framing is unchanged —
this is not a review, and nothing here may be described as one.*

---

## Addendum — the delegation gap, 26 August 2026 *(criminal law / torts and design)*

**Raised from outside the project and not found by any of the five topics.** The obstacle to
individual liability is not the corporate veil and not entity structure. It is **delegation**: large
firms assign responsibility formally, to real people, three levels below the chief executive, and the
responsible-officer doctrine's premise is that the officer had the power to prevent.

**SEC. 4(b) is the provision written for this, and it is civil-only.** The chief executive is a
presumed controlling person in civil proceedings; in criminal proceedings status is merely "evidence
from which the trier of fact may infer," and the prosecution retains its burden on every element.
**In the tier that carries prison, there is no presumption.**

**And SEC. 4(a) is narrower than *Iverson*'s federal test on exactly this element** — final, material
and independent authority, against a federal standard that requires only authority to control and
expressly does not require that it be exercised or formally vested. The narrowing is defensible and
it is spent where the objection is strongest.

Filed as a [known objection](../commentary/objections.md). **The question — whether final material
independent authority can be proved beyond reasonable doubt against a firm that has documented the
opposite — belongs to the criminal-law reviewer and nobody in-house can settle it.**

---

## Addendum — the criminal topic's missing shelf, 25 August 2026

*Not a finding of this sweep. It comes from a vocabulary audit run two days later: the
lawyer-written documents in the working library were n-grammed against all files in the
repository, and a group of case names every criminal-law reviewer would reach for came back
**zero**. The method is recorded in the diary; the tool is `check_vocabulary.py`.*

**What was absent.** *MacDonald & Watson*. *Johnson & Towers*. *Iverson*, except in passing.
*Hanousek*. *Jewell*. *Global-Tech*. *Bank of New England*. *Ahmad*. **Respondeat superior**,
**collective knowledge**, **willful blindness** and **conscious avoidance** — none of them present
in a repository whose central offense is a knowledge-and-authority offense.

**Why it matters to this topic specifically, and not as a matter of presentation.** This sweep
graded SEC. 6(a) fatal and drafted Amendment 8, whose Operation 4 proposes that evidence of
responsibility and authority "is sufficient to warrant a finding of practical power." That is
*Park*'s burden structure and it is right for the base tier. **It is the precise move
*United States v. MacDonald & Watson Waste Oil Co.*, 933 F.2d 35, 55 (1st Cir. 1991) forbids where
knowledge is an express element** — which is what SEC. 6(b)(1) makes it. So the cure this sweep
drafted works at the misdemeanor tier and fails silently at the felony tier, and the internal review's own
*Held open* paragraph half-saw it, calling SEC. 6(b)(1)'s "knowingly" undistributed without knowing
there was a case on the point.

**The repair is [Amendment 22](./proposals.md), and the answer comes from the same line rather
than from us.** *United States v. Iverson*, 162 F.3d 1015 (9th Cir. 1998) — ✅ read in the opinion
25 August 2026, pincite unconfirmed: the responsible-officer instruction "relieved the government
only of having to prove that defendant personally discharged or caused the discharge of a pollutant.
The government still had to prove that the discharges violated the law and that defendant knew that
the discharges were pollutants." Responsibility replaces the act element, not the knowledge element.

**And the objection this topic most needs is now on the source library too.** *United States v. Ahmad*,
101 F.3d 386 (5th Cir. 1996) holds that the § 1319(c)(2)(A) offenses before it are **not** public
welfare offenses. ✅ **Read in the opinion 26 August 2026**, which corrected two things this sweep
had published: the ground is **mistake of fact**, not the penalty, and the penalty is offered as
what "**confirms our view**" ([E56](../corrections/corrections.md)). Training and deploying a model is
ordinary commercial activity. **If a court took that view, the public-welfare framing would not
carry SEC. 6(b) at all**, and the felony tier would need a conventional mens rea rather than a
relaxed one. That is a sharper attack than anything this sweep produced.

**Answered 26 August 2026, and the sentence above overstated the difficulty.** ✅ *United States v.
Weitzenhoff*, 35 F.3d 1275, 1286 n.7 (9th Cir. 1993) (as amended 8 Aug. 1994), read in the amended
opinion in a star-paginated copy: "While the *Staples* opinion expresses concern with this evolution
of enhanced punishments for public welfare offenses, **it refrains from holding that public welfare
offenses may not be punished as felonies**." *Ahmad*'s argument is that *Staples* settled the point;
the Ninth Circuit reads the same passage as expressly refusing to. *Hanousek*, 176 F.3d 1116,
1122 n.4, then rejects the penalty argument by name. **What survives is a circuit split, which a
state legislature can be told about, and not an unanswerable objection.** The full-strength version
of the objection is the five-judge dissent from rehearing en banc in *Weitzenhoff* at 1293–1299, and
the criminal-law reviewer should be handed that rather than *Ahmad*'s summary of it. See
[Amendment 22](./proposals.md) and [Amendment 24](./proposals.md).

**And the method point this correction earns.** "Nobody in-house can settle it" was written about a
case whose answer was one citation away inside a case the repository already held. **The sentence
should have read: nobody in-house has *read* enough to settle it.** Those are different claims, and
only one of them is checkable.

**The method point, which belongs here rather than in the cure.** The five topics did not find this,
because none of the five was asked *what a specialist would look for and fail to find*. Asking what
is absent is a different instrument from asking what is wrong, and on its first run it produced a
front-page erratum ([E42](../corrections/corrections.md)) and this addendum.

⚠ *Every authority named above is quoted from a secondary source and unread in the reporter. E22
governs: none may be described as verified.*

