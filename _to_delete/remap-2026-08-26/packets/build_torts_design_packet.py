#!/usr/bin/env python3
"""Assemble packets/torts_design.md — the torts and design lane's reading copy.

Run from the repository root:  python3 packets/build_torts_design_packet.py

This builder holds the packet's authored text as its template and writes it out
verbatim: the authored text lives HERE, and every revision is made here and
regenerated — the .md is never edited by hand. The sources cited inside the
packet remain the authority; if the packet and a source differ, the source is
right and the difference is a defect worth reporting. A future revision may
upgrade this builder to section-extraction in build_criminal_packet.py's manner.
Stdlib only; deterministic; no network.
"""
import io

OUT = "packets/torts_design.md"

PACKET = r'''# The torts and design lane — one page

*A reading copy for the torts/design seat, assembled 24 August 2026 from
[the tagged statute](../model_act_v3_4.txt), [comparative officer liability](../standards/comparative_officer_liability.md),
[already a crime, if you are a person](../standards/already_a_crime_for_you.md),
[the same conduct, prosecuted](../standards/the_same_conduct.md),
[known objections](../docs/known_objections.md), and [the drafting queue](../audit/v3_5_cure_language.md).
Those files are the authority; this page exists so the lane can be read, printed, and marked up as
one document. If this page and a source differ, the source is right and the difference is a defect
worth reporting to FrontierAIAccountabilityProject@proton.me. Assembled 24 August 2026; linked from
the reviewer surfaces when the current review freeze lifts.*

*The purpose in one line: this lane polices the boundary the whole Act assumes — that a criminal
public-welfare duty and civil liability run beside each other without either collapsing into the
other.*

## The ask

One seat, one lane, scope in writing before work begins. Unpaid. **The floor:** the statute
straight through, then this packet, then **three findings, verified or refuted, with reasons** — a
complete and publishable disposition, perhaps six to eight hours. **The whole seat:** the menu
below worked through in full — every question answered, every drafted repair verified or refuted —
roughly ten to twenty hours across eight weeks. Both are dispositions; both are published as
written, including "approved with reservations," including hostile. **A disposition that refutes
one finding is worth more to this project than a full pass that agrees with everything.**

**The arithmetic:** everything below is the menu. Any three items are a complete disposition; all
of them are the seat done whole. One answered question is one finding. One drafted repair verified,
or refuted, is one finding. A defect of your own discovery outranks anything on the menu.

## Read first — the statute itself

The tagged text is not reproduced here, and the v3.5 queue's drafted language is **not enacted
anywhere** — the operative text is `model_act_v3_4.txt` at the repository root (print copy:
`archive/model_act_v3_4_reviewers_copy.pdf`). Your sections: **SEC. 2** (the duty, the deployer
reliance path at 2(b), controlled research deployment at 2(c)), **SEC. 6–7** (the harm tier's
causation element via SEC. 10(c)(2)(D); disgorgement and the indemnification/insurance bar), and
**SEC. 10(c)–(d) and SEC. 11** behind them.

One grading mark recurs in the shelf files and travels into this page unchanged: **⚠** marks a
claim that is recorded but whose primary source has not yet been retrieved or re-read by a human
eye — or, in the forecasting material, a claim that is forecast-grade rather than record-grade.
[The gallery](../standards/the_same_conduct.md) states the rule at its foot: where a row is marked
⚠, a primary source has not been retrieved. Treat every ⚠ item as verifiable, not verified.

---

## I. What this lane holds — five questions the shelf already frames

*This lane was not one of the in-house sweep's five; no sweep findings sit behind it and little has
been drafted in response to it. The seat is closer to the security and fiscal position — the
response is substantially the seat — but the shelf below frames each question with material already
on file. All of it is contestable; contesting it is the seat.*

### 1. Parallel lanes — criminal beside civil, neither substituting

The Act's own theory of the civil relationship is stated across three files. The mechanism table at
[known objections](../docs/known_objections.md) holds that corporate fines are "absorbed as an
operating cost" while the decision-maker stays insulated — the argument that civil and
administrative money alone cannot carry deterrence. [Comparative § 5](../standards/comparative_officer_liability.md)
(its codified-officer provisions retrieved verbatim, ⚠ R under the census rubric) records the
doctrine running in **both** lanes already: the responsible-corporate-officer phrase enacted twice
in the federal criminal definitions of "person," and the case law extending the rationale to civil
penalties as "even more persuasive where only civil liability is involved."

The statute itself keeps the lanes coupled at exactly one joint: SEC. 7(a) disgorgement triggers
"on conviction **or civil adjudication** of a violation," and its attribution presumption "is
rebuttable in a civil proceeding" but "operates in a criminal proceeding only as a permissive
inference." Nothing else in the Act creates a private civil action except the SEC. 11(d)
retaliation suit. The lane's first question is whether that architecture holds: does a criminal
public-welfare duty measured against SEC. 3 standards leak into the civil standard of care (the
negligence-per-se route a tort scholar sees immediately), and is that leakage a feature the design
intends or a consequence it has not priced? The Act does not address it; no file on the shelf does.

### 2. SEC. 7(b) — the indemnification and insurance bar, and the settlement economy

SEC. 7(b) voids insurance, indemnification, and every disguised transfer — "payment, loan,
forgiveness of indebtedness … gross-up" — against an individual penalty, fine, or disgorgement,
"whatever law is chosen to govern it," with a constructive trust on any benefit received. Three
valves are drafted into it, and each is this lane's to test:

- **Defense costs** survive at (b)(5), with clawback from a person "finally adjudicated to have
  committed a knowing or willful violation under SEC. 6(b)." That is the D&O practice question: a
  defense-costs-only tower with conduct-based recoupment is a known insurance form, but the Act
  imposes it by statute on every covered person at once, and (b)(6) sunsets existing arrangements
  at first renewal or a bracketed outside date. Does that transition clause distort renewals, and
  does the clawback trigger (final adjudication of the felony tier only) leave the base-tier
  due-care conviction fully insurable as to defense while its penalty is uninsurable?
- **Restitution** survives at (b)(7): insurance and indemnification of restitution under
  SEC. 10(c)(4) is expressly permitted, applied to restitution before any other liability, and "no
  such payment extinguishes any other liability of any person." SEC. 10(c)(4) separately gives
  restitution "priority over every penalty, fine, and disgorgement." Is the carve-out drawn right?
  The design plainly wants victims paid first from any source, but a carve-out that makes the
  victim-facing head of liability the one insurable head creates a settlement gradient — money
  flows to the label that insurance reaches — and whether that gradient helps victims or distorts
  characterization of settlements is a question products and insurance practice answers better
  than criminal drafting does.
- **The bar is itself an offense**: (b)(4) makes violating it a SEC. 10(a) entity violation, and a
  knowing violation by a controlling person a SEC. 5 violation for SEC. 6(b)(1) purposes — the
  felony tier. Test whether criminalizing the indemnity contract, rather than merely voiding it,
  is proportionate to its function; that reading feeds the proportionality seat directly.

### 3. Proximate cause in the harm tier, measured against tort doctrine

The harm tier's causation element is SEC. 10(c)(2)(D): "results" requires but-for cause "within
the meaning given in Burrage v. United States" **and** proximate cause — the death or serious
injury "a reasonably foreseeable consequence of the violation" and "not the product of an
independent, unforeseeable intervening cause," charged and found beyond a reasonable doubt.

That is tort superseding-cause vocabulary carried into a felony element, and the shelf argues both
halves of it. [Known objections](../docs/known_objections.md) answers the intervening-actor row —
"We did not cause the harm — the customer or user did" — with three moves: duties attach function
by function under SEC. 2(a); the harm tier requires proximate cause; and the independent duties
(evaluation, certification, reporting) "are breached or not regardless of downstream acts."
[Already a crime](../standards/already_a_crime_for_you.md) supplies the tort rule in terms: the
intervening wrongdoer does not break the chain where the defendant's own duty was to guard against
exactly that wrongdoer, and "foreseeable criminal misuse is not a superseding cause."

The seat's question is whether the criminal element does what the tort rule does when **the
deployer stands between developer and victim**. SEC. 2(a) allocates the duty to "the actor who
controls the relevant risk" — developer, provider, deployer, releasing provider, each named with a
function. A deployer's material modification is precisely the kind of intervening act a defense
will call independent; is a modifying deployer "unforeseeable" within (c)(2)(D) when SEC. 2(a)'s
own release-evaluation duty requires evaluating "the model as it can be modified"? A statute that
requires pre-release evaluation of modification arguably makes modification foreseeable as a
matter of its own text — which would leave the intervening-cause clause with almost no work in the
developer-defendant case. Whether that is the right answer, or a trap, is a tort causation
question, and nobody in-house has walked it.

### 4. SEC. 2(b) — deployer reliance as the small actor's safe course

SEC. 2(b) lets a non-modifying deployer discharge the duty of due care by documented adoption of
an upstream validation, a manifest of everything attached, the monitoring the validation
specifies, and reporting of matters within its knowledge — with reliance "unavailable to a
deployer that knows, or consciously avoids knowing, of a material nonconformity," and lapsing on
material modification. [Already a crime](../standards/already_a_crime_for_you.md) states the
design intent: the thin deployers get "a route to discharge the duty rather than an exemption from
it."

The lane's question is the resemblance this structure bears to the reliance and innocent-seller
defenses products law grew — the downstream party who passes on a validated article, without
altering it, on the maker's documentation. Products law learned where those defenses fail: the
seller who repackages, the reliance that survives red flags, the paper conformity that diverges
from the shipped configuration. SEC. 2(b) answers each in its own terms (the manifest; the
conscious-avoidance cut-off; lapse on modification) — the seat is asked whether those answers
match what the civil doctrine's failures actually taught, and in particular whether "material"
modification and "material" nonconformity, undefined here, will bear the weight the safe course
puts on them in a criminal statute.

### 5. The civil-only alternative, and the citizen suit the Act deliberately lacks

The strongest scholarly form of this lane's central objection is on the shelf, and the shelf states
it against interest. [Comparative § 5's addendum](../standards/comparative_officer_liability.md)
records that the survey scholarship it relies on argues for individual **civil** liability and
"only civil liability," expressly excluding the criminal form from its agenda — and that its
program names a mechanism this Act deliberately lacks: **citizen suits**. The addendum's own
words: the Act's "route for private information is the SEC. 11 award (private knowledge funding
public enforcement), not a private action."

SEC. 11(a) is that answer in text: an any-person award of a fixed share of collected sanctions, per
the § 78u-6 structure, payable from the SEC. 10(f) fund "whatever the source of the amounts in it,"
with anonymity through counsel and gag clauses void. The queue extends it as hypothesis only:
[CURE 17](../audit/v3_5_cure_language.md#cure-17--sec-11d-remedies-for-a-reporter-outside-employment)
would refit SEC. 11(d)'s employment remedies for a reporter outside employment — drafted,
intake-derived, expressly not settled. The seat's question is the design choice itself: is an
award-funded informant mechanism an adequate substitute for the citizen suit's function — private
enforcement when public enforcement stalls — given that [comparative § 5's](../standards/comparative_officer_liability.md)
own numbers show federal enforcement falling to a twenty-year low, which is the scenario citizen
suits exist for? A disposition that says the civil-only architecture is right, and the criminal
form should go, would be published like any other; [known objections](../docs/known_objections.md)
says so on its face.

### 6. The design-defect analogy — can "failure of due care" be pleaded the way design defect is?

SEC. 6(a) measures due care "against the standards applicable under SEC. 3 and the conduct of a
reasonably prudent controlling person in like circumstances; an entity's own framework is evidence
of neither." That last clause is the Act refusing the manufacturer's-own-specification defense,
and [the case](../docs/the_case.md) uses the analogy expressly: under SEC. 8's controls clause,
"wilful blindness becomes a design defect the officer certified against."

Products law spent decades learning how to plead and prove a design choice as a defect — the
alternative-design showing, risk-utility balancing, the state-of-the-art fight, the expert
economy those tests created. The criminal form here asks a jury to find, beyond reasonable doubt,
a failure of due care in a design or training decision, against agency standards that (per SEC. 3
and the queue's commencement findings) may not yet exist when SEC. 6 begins to operate. The seat's
question: does the criminal element need what products law learned — an alternative-measures
showing, a state-of-knowledge anchor, a defined role for industry custom now that the entity's own
framework is excluded — or does the [CURE 8](../audit/v3_5_cure_language.md#cure-8--sec-6-the-individual-liability-offense-reconstructed)
reconstruction (hypothesis, not enacted: authority, nexus to an actual violation, and a converse
clause providing that a person who took the measures a reasonably prudent controlling person would
have taken *has* exercised due care) already supply the equivalent? Checking CURE 8's converse
clause against how design-defect proof actually runs is this lane's fastest complete finding.

---

## II. What has been drafted in response

*Little — which is the honest state of this lane, and why the seat matters. The queue entries that
touch it are reproduced in the criminal packet and owned by [the queue](../audit/v3_5_cure_language.md);
all are graded there, none is enacted, and the tagged v3.4 text is not to be edited outside a
revision.*

- **[CURE 8](../audit/v3_5_cure_language.md#cure-8--sec-6-the-individual-liability-offense-reconstructed)**
  (sweep-derived hypothesis) — the reconstructed SEC. 6(a) with the converse due-care clause § I.6
  asks you to test.
- **[CURE 14](../audit/v3_5_cure_language.md#cure-14--sec-9b-a-detection-clock-that-cannot-be-gamed-by-certifying-less-monitoring)**
  (sweep-derived hypothesis) — its notice duty runs to persons whose *systems* were accessed, not
  persons *injured*; the CURE 1 addendum in [the queue](../audit/v3_5_cure_language.md) holds open,
  undrafted, whether an injured-person notice belongs in a public-welfare statute or "belongs to
  tort, discovery, and the enforcement record's FDUTPA lane" — a question addressed to exactly
  this seat.
- **[CURE 17](../audit/v3_5_cure_language.md#cure-17--sec-11d-remedies-for-a-reporter-outside-employment)**
  (intake-derived hypothesis) — the outside-reporter remedies at § I.5.
- **The citizen-suit discussion** — [comparative § 5](../standards/comparative_officer_liability.md)
  notes the bracketed-matter file "does not currently discuss" the choice "and a drafting session
  may wish to." Nothing is drafted. The seat is the response.

## III. The question menu

Any three answered are a disposition; all six, with the drafted items above verified or refuted,
are the seat done whole. Replace any of them with findings of your own.

1. Does the criminal duty leak into the civil standard of care (negligence per se), and does the
   design intend it?
2. Is the SEC. 7(b) restitution carve-out drawn right, or does it bend settlements toward the one
   insurable label?
3. Does SEC. 7(b)'s defense-costs valve and sunset clause distort D&O practice, and is
   criminalizing the indemnity contract itself proportionate?
4. Does SEC. 10(c)(2)(D)'s intervening-cause clause do any work against a developer when SEC. 2(a)
   makes deployer modification foreseeable by its own text?
5. Does SEC. 2(b)'s reliance path incorporate what products law learned about downstream reliance
   defenses — and can "material" bear its criminal weight undefined?
6. Is the SEC. 11 award an adequate substitute for the citizen suit the civil-only scholarship
   proposes — or should this Act be civil?

## IV. The errata already filed near this lane

- [E8](../ledger/errata.md#e8--in-one-paragraph-true-of-the-duty-silent-on-the-entity-in-the-paragraph-built-to-be-quoted)
  — the entity tier is strict liability; the front-page summary once said otherwise. It bounds
  every parallel-lanes argument you make: the strictness sits on the entity, the due-care floor on
  the person.
- [E5](../ledger/errata.md#e5--it-was-never-going-to-be-you-true-for-the-weekend-model-not-yet-true-for-the-startup)
  — "it was never going to be you": true of the weekend model, not yet of the startup; relevant to
  how far SEC. 2(b)'s safe course actually reaches.

Method-wide entries — E21, E22 (extended by E32), E27, E33 — govern how every date, quotation,
count, and file-status claim in the evidence base was made; [the register](../ledger/errata.md) is
short and worth ten minutes.

## A court states the evidentiary problem — added 25 August 2026

Twenty-six former Meta employees, all on protected leave during a May 2026 reduction in force,
alleged the company "used a constellation of internal artificial intelligence systems," including
one monitoring "employees' keystrokes and computer activity," to "score, rank and select employees
for inclusion on the list." On 24 August 2026 U.S. District Judge William Orrick declined interim
relief: *"I have a record I have to deal with and the record at the moment does not persuade me of
the merits."* He allowed that the evidence "raised some potential questions about Meta's categorical
denial of any impact of AI in the termination process," and called the matter "an unusual, or a new
sort of issue" that was hard to gather evidence for at the outset (Courthouse News, 24 Aug 2026;
[press corpus](../research/press_corpus_july_august_2026.md)).

**This Act does not reach employment decisions, and the ruling is authority for nothing** — it is a
denial of interim relief on an incomplete record. It sits in this packet because it is the clearest
judicial statement yet of the problem this lane exists to solve. The claim did not fail because
automated decision-making is unprovable in principle. It failed on the record available to people
standing outside the system that decided about them.

That asymmetry is the design question for this seat. Every logging, retention and reporting duty in
the Act is drafted to make the facts exist somewhere reachable, created before anyone knew they
would be wanted. Whether the duties as drafted would actually produce a record a court could use —
or whether they would produce a compliance artifact that answers a different question — is a finding
this lane can make and no other can.

## The other seats, and how this lane meets them

The review runs in parallel lanes — criminal law, enforcement, security,
fiscal, proportionality, federalism, torts/design, and open source and academia. Each seat
reviews independently, and each disposition publishes independently, as written, so no lane waits
on another. Findings that change text route through the public cure queue and the errata register,
where every other lane sees them. That queue is how v3.4 becomes v3.5: each lane's verified findings are drafted as cures against the tagged text, and the assembled v3.5 carries every lane's accepted work, so a disposition here is a chapter of the next version, written alongside the other seats'. The maintainer collates and responds separately and labeled,
and may not overrule or edit a disposition. Anonymous outside contributions arrive through the
repository's correction doors and are credited by election — one open drafting question has
already been answered from outside this way. Reviewer identities are not shared between reviewers,
and attribution is each reviewer's own election. This lane's particular relation to the rest:
torts/design polices the boundary every other lane assumes — that criminal and civil liability run
in parallel without either collapsing into the other — and its reading of the insurance ban feeds
the proportionality seat's deterrence question directly.

## What to attack

The softest targets, in this lane's own order: the restitution carve-out's settlement gradient
(§ I.2); the intervening-cause clause that may have drafted itself out of work (§ I.3); the
undefined "material" on which the entire SEC. 2(b) safe course hangs (§ I.4); and the civil-only
alternative, argued at strength on the project's own shelf and answered only by a design choice
(§ I.5). If your conclusion is that the criminal architecture should yield to a civil one, say so:
that disposition is publishable here, and the project's own files carry the argument's best form.

---

**If you need something this packet does not carry.** [The glossary](../standards/what_these_words_mean.md)
defines the words the Act turns on, in the sense the statute uses them, including the ones a
specialist reader would search for first. [Known objections](../docs/known_objections.md) carries
the attacks already made on this lane, with the answers given and the ones still unanswered.
[For reviewers](../REVIEWERS.md) states every open item in the project in one line each, and
[the index](../MAP.md) reaches the rest of the repository.

---

File it: email FrontierAIAccountabilityProject@proton.me — links or pasted text, no attachments —
in any form: a memo, a marked-up copy of this packet, a numbered list of findings. Or, if you were
contacted by the maintainer through a different channel, reply on the channel you were contacted
on. It is published as written, credited or anonymous at your choice. A finding that something is
broken is the seat working, not failing.
'''

if __name__ == "__main__":
    io.open(OUT, "w", encoding="utf-8").write(PACKET)
    print("wrote", OUT)
