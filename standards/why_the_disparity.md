# Why the disparity exists — twelve explanations, argued rather than assumed

*[The same conduct, prosecuted](./the_same_conduct.md) establishes the fact: American law reaches
individuals for unauthorized computer access with announced exposure from ten years to four
hundred and forty, and reaches the officer of a frontier developer not at all.*

***This file asks why, and refuses to answer it in one sentence.*** *Twelve explanations follow.
Several are exculpatory. Several are incompatible with each other. They are drawn deliberately from
across the political spectrum, because an explanation a reader already believes is the one that
gets them to the evidence — and because a file offering only villains would be answering a
different question from the one asked.*

---

## Who this is about

**About:** the officers of frontier developers — companies training above 10²⁶ operations.

**Not about:** open-source contributors, startups, researchers, ordinary deployers and API
customers, or users. *On deployers precisely, see [the case](../docs/the_case.md#who-this-is-about).*

**And what this file will not do.** Pick a winner. **Several of these explanations are true at
once**, and the useful question for a drafter is not *which one* but *which remedy each implies*,
because they do not all imply the same one.

---

## How to read the twelve

Each explanation gets four things:

**The case for it** — stated as its strongest advocate would state it, not as an opponent would.
**What would confirm it** — the evidence that would settle the matter.
**What it uniquely predicts** — the thing this explanation says and the others do not.
**What remedy it implies** — because that is the only part a legislature can act on.

**The spectrum labels are approximate and offered without endorsement.** They exist so a reader can
find the argument they already hold and check it, not to sort anyone.

---

## A · There is no artifact, so the law has nothing to grip

*Doctrinal · no political valence*

**The case for it.** Criminal law needs an act, an actor, and a mental state. A person at a keyboard
supplies all three cleanly. A deployment decision supplies none: it is made across meetings and
reviews, by shifting groups, with no document anyone owns. Prosecutors do not decline these cases
out of deference. **There is nothing to charge.**

**What would confirm it.** The pattern in [why a signature works](./why_a_signature_works.md):
twenty-eight years where a false certificate existed, twelve months where twenty-nine people died
and no comparable document did.

**What it uniquely predicts.** That creating the artifact — with nothing else changed — would by
itself produce enforcement. **This is a testable claim**, and Sarbanes-Oxley is the natural
experiment: personal certification produced prosecutions that had not existed before.

**Remedy implied.** SEC. 8. A required signature, and nothing more elaborate.

---

## B · The triggering event has not happened

*Historical · no political valence*

**The case for it.** Personal-liability regimes in America are **reactive without exception**. The
Steamboat Acts followed exploding boilers. The 1938 Food, Drug and Cosmetic Act followed a mass
poisoning. Mine safety followed disasters. Sarbanes-Oxley followed Enron. **No frontier-AI
mass-casualty event has occurred in the United States**, so the mechanism that produced every
previous regime has not been triggered.

**What would confirm it.** The historical record in
[house language § 8](./house_language.md), which is uniform.

**What it uniquely predicts.** That the law will arrive **after** a catastrophe rather than before —
and that arguments made beforehand will be ignored regardless of quality.

**Remedy implied, and it is uncomfortable for this project.** If B is the whole story, the Act
arrives when something terrible happens, and the value of drafting now is only that the text exists
when the moment comes. **That is a smaller claim than this project would like to make, and it may be
the true one.**

---

## C · Limited liability is working exactly as designed

*Market-liberal / conservative*

**The case for it.** The corporate veil is not a loophole. It is deliberate policy, several
centuries old, which exists so that capital will fund risky undertakings that individuals would
never personally guarantee. The responsible-officer doctrine is the **carved exception**, and it has
only ever been carved industry by industry, slowly, after specific demonstrated need — food and
drugs, mines, transport, securities. **Frontier AI simply has not been carved yet, and the burden is
on whoever wants the carve, as it was every previous time.**

**What would confirm it.** That the doctrine is genuinely narrow and industry-specific, which
[already a crime, if you are a person](./already_a_crime_for_you.md) shows: the statutes reaching
individuals are enumerated, not general.

**What it uniquely predicts.** That the argument will be won or lost **on the specifics of this
industry**, not on general principle — and that a proponent must show why AI belongs in the carved
list.

**Remedy implied.** A narrow, threshold-limited statute reaching a small covered class — which is
what a 10²⁶ threshold produces. **This explanation is a friend of the Act's design**, not an enemy.

---

## D · The intent asymmetry is real, and it is not an excuse

*Pro-industry · argued in good faith*

**The case for it.** Every defendant in the prosecution gallery did something deliberate. A company
whose system does something unanticipated has not. Criminal law is built around chosen wrongdoing,
and stretching it to cover unintended outputs of a complex artifact is a serious step that ought to
give a legislature pause. **The people running these companies are, in the main, trying.** Twelve of
them published safety frameworks nobody required.

**What would confirm it.** The frameworks themselves, read in
[the dossier](../dossier/README.md) — several are more demanding than any law requires.

**What it uniquely predicts.** That a knowledge-based standard would catch nobody, and that any
workable duty must run on **conduct before release** rather than outcomes after it.

**Remedy implied — and this is the one the Act adopts.** A **negligence floor**, not a knowledge
requirement, attached to the decision to proceed rather than to the harm. The release was intended
even where the harm was not. *Park* was built for exactly this.

---

## E · Prosecutorial economics

*Left-institutional, and also a small-government reading*

**The case for it.** An individual computer-crime case is cheap, winnable, and produces a press
release. A case against a defendant with unlimited counsel is slow, expensive, and losable.
Prosecutors allocate scarce resources rationally. **The pattern emerges with nobody intending it.**

**What would confirm it.** The plea data in [the gallery](./the_same_conduct.md): announced maxima
enormously in excess of what prosecutors actually sought, which is the signature of a system
optimizing for quick resolution.

**What it uniquely predicts.** That even *with* a statute, enforcement against well-resourced
defendants would be rare — so the deterrent would have to come from the duty's existence rather
than from frequent prosecution.

**Remedy implied.** Bright-line, documentary offenses that are cheap to prove: **a missing
signature is provable from an empty file**, which is why this Act's offenses are drafted as
record-based rather than harm-based.

---

## F · Causation is genuinely diffuse

*Technocratic*

**The case for it.** CFAA harm is traceable to one actor. Harm downstream of a general-purpose model
passes through deployers, integrators, professionals and users, each adding decisions. Legal systems
handle diffuse causation badly everywhere — this is not special pleading by anyone.

**What would confirm it.** That the same difficulty appears in unrelated fields: pollution,
pharmaceuticals, financial contagion.

**What it uniquely predicts.** That any harm-based statute will fail on proof, whatever its
penalties.

**Remedy implied.** Seat the offense in **conduct rather than consequence** — which is the design
choice behind SEC. 5(b) and the reason [the cross-examination](../docs/the_case.md) opens on an
intrusion rather than a death.

---

## G · Federalism, and the preemption shadow

*Constitutional*

**The case for it.** States that might act are drafting under threat of federal preemption; every
live federal vehicle contains a preemption clause. Congress moves slowly on anything contested.
**The result is not that nobody wants to act — it is that the actors who want to are unsure they
may.**

**What would confirm it.** The preemption analysis in the drafting record, and the enacted family's
conspicuous avoidance of anything that looks like a design mandate.

**What it uniquely predicts.** That state statutes will cluster in the **safest available space** —
transparency and reporting — which is precisely what [the census](./frontier_bill_census.md) found
across six regimes.

**Remedy implied.** Draft into the savings clauses rather than against the preemption clauses. **The
Act already does this**, which is why its offenses are framed as generally applicable criminal law
and false-statement offenses.

---

## H · Nobody has put the question to a legislature

*Institutional*

**The case for it.** A member reaching for a model reaches for what exists, and what exists is
entity-level duties. Counsel drafts; members originate. Staff time follows the bills in front of
them. **A question absent from the discourse produces no answer regardless of how much expertise is
available.**

**What would confirm it.** [The commentary sweep](./commentary_sweep.md): a dedicated academic gap
analysis enumerated twenty-six deficiencies in California's statute and **personal accountability
was not among them.** Three law firms briefed clients on exposure and none mentioned personal
exposure, because there is none to mention.

**What it uniquely predicts.** That the vacancy persists **among people acting in complete good
faith**, and would be closed by the question being asked well once.

**Remedy implied.** Exactly what this project is: a drafted answer, published where a staffer can
find it.

---

## I · The grammar removes the person before anyone gets to the law

*Cultural / linguistic*

**The case for it.** [House language](./house_language.md) sets it out: a vocabulary in which
systems think, decide and go rogue supplies a culprit who cannot be charged. English has an active
construction for the machine and none for the person shipping it. **A debate conducted in that
grammar cannot arrive at a defendant.**

**What would confirm it.** The frontier statutes' own drafting: six regimes, and the only human noun
in any of them is Connecticut's *officers and directors*, appearing as recipients of a report.

**What it uniquely predicts.** That the vacancy will appear **even in documents whose purpose is to
find gaps** — which is what the gap analysis did.

**Remedy implied.** No statutory remedy at all. This one is answered by writing differently, which
is why the language rule is a repository file and not a preamble.

---

## J · The national-security frame makes personal liability expensive to propose

*Hawkish / geopolitical*

**The case for it.** A legislator who proposes criminal exposure for American frontier officers can
be told, immediately and publicly, that they are handing the lead to Beijing. **That is a real
political cost and it is paid up front**, whatever the merits.

**What would confirm it.** The frequency of the argument in hearings and in industry submissions.

**What it uniquely predicts.** That the objection will be raised in **security** terms rather than
economic ones, and by people not otherwise engaged with the technology.

**Remedy implied, and it has an answer.** **PRC Criminal Law art. 31 already imposes dual
punishment** — the persons directly in charge and other directly responsible persons are reachable
in China in a way they are not in the United States. *See [the comparative
provisions](./comparative_officer_liability.md).* **The competitor being invoked has the rule
already.**

---

## K · This is the ordinary operation of corporate power, and AI is not special

*Left-structural*

**The case for it.** Capital has always externalized liability: through the veil, through
subsidiaries, through arbitration, through settlement without admission. **Treating frontier AI as
an anomaly mistakes a rule for an exception**, and a statute aimed at one industry leaves the
mechanism intact everywhere else.

**What would confirm it.** That the same pattern appears in unrelated sectors with no technological
novelty at all.

**What it uniquely predicts.** That closing this gap will produce **the next structure** — new
corporate forms, relocated decision-making, indemnities — rather than compliance.

**Remedy implied, and the Act takes it seriously.** Anti-evasion drafting: the companion is written
against a lineage of liability-evaporation structures, and SEC. 4's authority test is deliberately
indifferent to titles and corporate form for this reason.

---

## L · Lobbying and access

*Left · and placed last deliberately*

**The case for it.** The industry is extraordinarily well resourced, employs former officials, funds
research and trade associations, and files on the dockets that matter. [Who actually
files](../filings/who_actually_files.md) counts the room: twenty-one of fifty-one comments from
industry, four from the patient side.

**What would confirm it.** Disclosure filings, revolving-door records, and the composition data
already gathered.

**What it uniquely predicts.** That the vacancy would persist **even after the question was asked
well** — which is the one prediction that distinguishes L from H, and the one this project is,
unintentionally, a live test of.

**Remedy implied.** Nothing this Act contains. Access reform is a different statute and a different
project.

***Why it is twelfth rather than first.*** It is real, and it is the explanation a hostile reader
expects, discounts on sight, and uses to file the entire project under grievance. **Arriving after
eleven explanations that require nobody to be a villain, it lands as one factor among many** — which
is both more honest and more persuasive than leading with it. *A reader who thinks L is the whole
story should notice that A, B, C and H each predict the same vacancy with no bad actor anywhere.*

---

## The surveys agree — added 23 August

Two independent surveys of the 2026 landscape now state this file's finding in their own words.
CSIS, comparing nine frameworks across two continents (Caroli & Mehta, 3 Aug 2026, ⚠ P): *"Many of
the frameworks do not include the appointment of senior personnel to oversee the safety framework
… This may demonstrate a reluctance by policymakers to impose personal accountability by law, as
well as pushback from an industry comfortable with self-implementation of safety requirements but
opposed to highly prescriptive governance requirements that delineate specific top-level managers
responsible for the safety of models."* And CDT, surveying the year's most active legislative area
(20 Aug 2026, reusable with credit): across the chatbot-safety wave, *"[l]iability falls only on
the direct deployers … providing protection to original developers of foundation models."* The
law reaches down, not up — measured across 146 bills. Explanation **H** predicted that the vacancy
persists among people acting in good faith until the question is asked well once; two surveys have
now documented the vacancy without either treating it as a question. The same CSIS report supplies
the restraint corollary: on the one documented voluntary withholding of a frontier model, *"[n]o
authority could have compelled that decision … Only a legally binding regime can guarantee such
restraint as a matter of right rather than goodwill."*

## The record answers, under oath — added 24 August

Two congressional hearings, read in full, now carry the disparity in sworn testimony — the
asymmetry conceded, the immunity requested, and the state-side answer, all at the same tables.

**The asymmetry, conceded by a proponent of loosening it.** Rush Doshi (Council on Foreign
Relations; formerly the NSC's China directorate), to House Homeland Security on 17 March 2026:
*"We currently treat American AI companies, like Anthropic, with more regulatory scrutiny than we
treat Chinese ones, like DeepSeek."* His remedy runs the other way — restrict the foreign, relieve
the domestic — but the sentence concedes the frame this file documents: scrutiny is being assigned
by flag, and the argument is over which direction to level it. This Act's answer is that scrutiny
follows the risk and the power over it, whoever holds the flag.

**The immunity, requested in terms.** Kinsey Fabrizio, president of the Consumer Technology
Association, sworn before House Oversight on 17 September 2025: CTA *"has urged Congress to adopt
a 10-year pause on enforcement of state and local AI laws,"* and the federal framework sought is
*"tech-neutral,"* *"preemptive,"* *"risk based"* — and *"removes liability for companies that are
compliant."* The trade association that owns CES asked Congress, under oath, for a design in which
compliance purchases immunity. That is explanation **L** speaking in its own voice, and it is the
precise inverse of this Act's rule, under which compliance is the duty and immunity is nobody's to
purchase.

**The state-side answer, same table.** Nicol Turner Lee (Brookings), the minority witness at the
same hearing: the rejected moratorium *"would have threatened states' rights and the public
interest"*; since January, *"over a hundred measures across 38 states have been enacted to law"*;
and the sentence that prices the whole dispute — *"AGs are trying to figure out ways to keep our
grandmothers safe from AI. They are not necessarily trying to compete against China."*

*(Sources: House Homeland Security Subcommittee on Cybersecurity and Infrastructure Protection,
Serial 119-42, 17 Mar 2026; House Oversight Subcommittee on Cybersecurity, IT, and Government
Innovation, Serial 119-49, 17 Sep 2025 — the transcripts, read in full 24 Aug, held in the project library; rows at
[the verification record § 6](../research/verification_record.md).)*

## What a drafter should take from twelve explanations

**They do not all imply the same remedy, and that is the useful finding.**

- **A, E and F** all point to the same drafting choice: **documentary, conduct-based offenses**,
  provable from an absence rather than from a causal chain.
- **C and G** point to **narrow scope**: a high threshold, a small covered class, drafted into the
  savings clauses.
- **D** points to a **negligence floor** rather than a knowledge requirement.
- **H and I** are not answered by statute at all, but by asking the question and writing
  differently.
- **B and K** are cautions rather than remedies — that the law may arrive only after a catastrophe,
  and that closing one gap invites the next structure.
- **J** has a direct answer already on the books elsewhere.
- **L** is outside this Act's scope entirely.

**Every one of those is what this Act already does**, which is either evidence the design is sound
or evidence this file was written by the same person who wrote the Act. **It was.** A reader should
weigh it accordingly, and the explanations are set out above in their strongest form precisely so
that weighing is possible.

---

*Corrections to the project contact — especially from anyone who holds one of these explanations
and thinks it has been stated weakly. They enter [the errata register](../ledger/errata.md) with
the fix attached and permanent credit.*
