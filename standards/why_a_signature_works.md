# Why a signature works

*SEC. 8 requires a named person to certify a deployment decision. The objection is always that this
is paperwork — a formality that changes nothing, imposed on people already doing their best.*

***This file is the answer, and it is not an argument. It is a set of cases where the presence or
absence of one signed document decided what happened to somebody.***

---

## Who this is about

**About:** the officer of a frontier developer — the person inside a company training above 10²⁶
operations who decides that a system ships.

**Not about:** engineers, researchers, open-source contributors, deployers or users. SEC. 8 asks one
person to sign one thing. Nobody else acquires a duty because of it.

---

## 1. Twenty-eight years and twelve months

Two American executives presided over conduct that killed people. **Neither was charged with a
death.** One received the lightest sentence in [the gallery](./the_same_conduct.md) and one the
heaviest.

**Don Blankenship.** Twenty-nine miners died at Upper Big Branch. He was convicted of a single
**misdemeanour** — conspiracy to violate mine safety standards — acquitted of every felony, and
sentenced to **twelve months**, the statutory maximum.

**Stewart Parnell.** Nine people died and roughly seven hundred fell ill from salmonella in Peanut
Corporation products. He was sentenced to **twenty-eight years**.

Not one day of Parnell's sentence was for killing anyone.

**The twenty-eight years came from fraud counts, and the fraud was a document.** He had fabricated
**certificates of analysis** stating that product was free of pathogens when no test had been run,
or when the test had found them.

**Read those two together and the mechanism is unmistakable.** The variable that decided the
sentence was not the body count. **It was whether there existed a document the defendant had signed
that was untrue.**

Parnell signed, so the law had a purchase and used it. Blankenship signed nothing of that kind, so
twenty-nine deaths produced a regulatory misdemeanour with a one-year cap.

*Sources: [DOJ, Blankenship sentencing](https://www.justice.gov/opa/pr/former-massey-energy-ceo-sentenced-year-federal-prison);
[DOJ, Parnell sentencing](https://justice.gov/archives/opa/pr/former-peanut-company-president-receives-largest-criminal-sentence-food-safety-case-two).
⚠ **R** under [the confidence rubric](./frontier_bill_census.md#the-confidence-rubric-governed-by-e15).*

---

## 2. Every adjacent field already does this, and none of them collapsed

**Clinical research.** Before a single participant is enrolled in an American drug trial, an
individual investigator signs **Form FDA 1572**. FDA's own instruction is that the signature
*"constitutes the investigator's affirmation that **he or she** is qualified to conduct the clinical
investigation and constitutes the investigator's written commitment to abide by FDA regulations."*
Not the institution. Not the sponsor. A named human, in their own name.

**Public companies.** After Enron, Congress required the chief executive and chief financial officer
to **personally sign** a certification that the financial statements fairly present the company's
condition — **18 U.S.C. § 1350**. False certification carries **\$1,000,000 and ten years** if
knowing, **\$5,000,000 and twenty years** if wilful.

The 2002 objections were the ones a frontier-officer duty attracts today: no competent person will
take the job; no individual can verify a large firm's whole position; the exposure is
disproportionate. **Twenty-four years later every public company in America has someone who signs.
They did not run out of chief financial officers.**

**Records.** Under **18 U.S.C. § 1519**, destroying a document with intent to impede a federal
matter carries **twenty years** — and it bites *"in relation to or contemplation of"* a matter, so
the offence is complete before any investigation opens.

**The heaviest penalty in this whole file is not for killing anyone. It is for what happened to a
piece of paper.**

*Sources: [FDA, Form 1572 instructions](https://www.fda.gov/media/79326/download);
[18 U.S.C. § 1350](https://legalclarity.org/what-is-section-906-of-the-sarbanes-oxley-act/);
[18 U.S.C. § 1519](https://www.law.cornell.edu/uscode/text/18/1519). ⚠ **R**.*

---

## 3. What a signature actually does, from the field that measured it

The best evidence that naming a person changes behaviour does not come from law. It comes from
surgery, where somebody ran the experiment.

The WHO safe surgery checklist runs nineteen checks at three pause points. One of them is not a
technical step at all: **the team members confirm they have been introduced by name and role.**

Atul Gawande, who led the work, records how that item landed:

> *"The introduction of names and roles at the start of an operating day proved a point of
> particularly divided view. From Delhi to Seattle, **the nurses seemed especially grateful for the
> step, but the surgeons were sometimes annoyed by it.** Nonetheless, most complied."*

**Read that twice.** The item that required people to say who they were was the most resisted on the
list — **resisted by the person with the most authority in the room, and valued by the people with
the least.**

Gawande records the objection verbatim too: *"This checklist is a waste of time."* And what adoption
actually required: *"a shift in authority, responsibility, and expectations about care."*

**That is SEC. 8, its objection, and its beneficiaries, observed in another field twenty years
early.**

*Source: Atul Gawande, *The Checklist Manifesto* (2009). ⚠ **R** — read from a digital copy on
21 August 2026; page references to be pinned against a paginated edition before publication.*

---

## 4. And the reason the frontier's own defence fails on Gawande's distinction

The same book supplies the distinction that decides whether a duty is fair. Following the
philosophers Gorovitz and MacIntyre, Gawande separates two ways of failing:

> *"The first is **ignorance** — we may err because science has given us only a partial
> understanding of the world and how it works… The second type of failure the philosophers call
> **ineptitude** — because in these instances the knowledge exists, yet we fail to apply it
> correctly."*

And then he reaches for the legal word himself, without being asked:

> *"It is not for nothing that the philosophers gave these failures so unmerciful a name —
> **ineptitude**. Those on the receiving end use other words, like **negligence** or even
> **heartlessness**."*

**The industry's defence is ignorance.** Nobody yet knows how to make these systems reliably safe,
so nobody can fairly be blamed for failing to.

**But the frontier safety frameworks are the industry's own written statement of what it does
know.** Evaluations. Capability thresholds. Deployment gates. Halt authority. Twelve companies have
published one. Where a developer does not do what its own framework says, **that is not ignorance —
it is the thing Gawande's philosophers named, and the word the people on the receiving end use for
it is negligence.**

Which is precisely the floor *Park* supplies and SEC. 6 adopts. **The frameworks the companies wrote
voluntarily are the standard of care they can be measured against.**

**And one more line from the same book, because it is the industry's proposal stated in advance:**
*"the traditional solution in most professions has not been to punish failure but instead to
encourage more experience and training."* More research. Better evaluations. Gawande's entire book
is the demonstration that this does not work at scale, in a field with far more training than this
one.

---

## 5. The gap, stated in one paragraph

Enacted frontier law requires **exactly one signature**, and it belongs to the auditor. Illinois
requires *"the signature of the lead auditor certifying the results."* The legislative instinct to
demand a named human signature exists, is already in force, and has been aimed at **the outside
contractor hired to inspect the work** — not at the officer who decides to ship.

Connecticut routes quarterly catastrophic-risk reports to *"the officers and directors of the large
frontier developer"* and asks nothing of them in return.

H.R. 9917 would mandate a shutdown capability and civil penalties of \$20,000,000 a day. **The only
human signature in the bill is the sponsor's own**, on the line marked *"(Original Signature of
Member)."*

And of twelve published frontier safety frameworks, **not one requires an attestation of a
deployment decision.** At the best-documented laboratory on earth there is a decision-maker and no
artefact of the decision.

**So the objection has the burden backwards.** A signature is not a novel formality being proposed
for an industry that has never faced one. **It is the ordinary instrument by which American law
reaches an executive at all** — and its absence at the compute frontier is not a gap in
transparency. It is the removal of the mechanism.

---

*Corrections to the project contact; they enter [the errata register](../ledger/errata.md) with the
fix attached and permanent credit.*
