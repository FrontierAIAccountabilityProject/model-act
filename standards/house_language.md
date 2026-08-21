# House language — how this project describes frontier AI, and how it describes the people who ship it

*A drafting rule, adopted 21 August 2026. It governs the project's own voice. **It does not
govern quotations**, which are reproduced exactly as their authors wrote them, including where
their wording is the wording this rule avoids — see § 4, which is the most important section
here.*

---

## 1. The problem, stated without accusing anyone of a conspiracy

English offers two ways to describe the same event, and they distribute responsibility
differently.

> *The agent autonomously decided to break into four accounts.*
>
> *The system a company built and released broke into four accounts, and no human being had to
> approve its release.*

Both sentences can be true of the same facts. The first locates agency in the software and leaves
the sentence with no person in it. The second locates the software as an instrument and leaves
the reader asking who chose to point it. **Only the second sentence raises the question this
project exists to ask**, and a file written in the first register cannot ask it, however many
times it says the word "accountability" afterwards.

This is not a claim that anyone chose the vocabulary in bad faith. The mentalistic register came
from the research literature, where it is a compact shorthand among people who all know it is a
shorthand. It escaped into press coverage, corporate communications and legislative drafting,
where nobody knows that. The effect, wherever it came from, is that **the most consequential
industrial decisions of the decade are routinely described in a grammar with no decision-maker in
it** — and the parties who benefit from that description are not the ones being written about
here.

## 2. The two failures, in both directions

**Failure A — agency granted to the system.** Mentalistic verbs and adverbs make the artefact
the subject of the sentence: *the model decided, wanted, tried, learned, realised, went rogue,
behaved deceptively, acted autonomously.* Each is doing work. "Went rogue" implies a prior
loyalty and a departure from it. "Deceptive" implies a mind with something to hide. "Autonomous"
implies self-governance rather than absence of supervision.

**Failure B — agency removed from the people.** Passive and impersonal constructions take the
humans out: *the model was released; an incident occurred; safeguards were not in place;
information was inadvertently accessible.* Somebody released it. Somebody decided the safeguards
were adequate. Somebody set the launch date.

The two failures are complements, and a document can commit both in one sentence while sounding
perfectly neutral. **This repository is currently much better at avoiding B than A** — a scan on
21 August 2026 found effectively no agency-removing passives about the humans, and a real
concentration of mentalistic vocabulary about the systems. So the work is one-sided, and knowing
which side saves a great deal of pointless editing.

## 3. The substitutions

| Instead of | Write | Why |
|---|---|---|
| the model / agent **decided, chose, wanted, tried** | the frontier system **produced, output, executed, was configured to** | restores the artefact to instrument |
| **behaviour** (of a system) | **output**, **operation**, **what it did**, **performance** | "behaviour" is for creatures |
| **autonomous AI hack / attack** | **a break-in carried out by a system [company] built and released** | puts the shipper back in the sentence |
| **autonomous external access** *(statutory term)* | **keep it** | a defined term of art in SEC. 5(b) describing absence of human supervision, which is a fact about the deployment, not a mind |
| **went rogue** | **operated outside the conditions its developer described** | no prior loyalty implied |
| **deceptive** *(of a system)* | **produced false statements**, **misreported** | no mind implied |
| **the AI learned to…** | **training produced a system that…** | training is something people do |
| **an incident occurred** | **[company]'s system did X; [company] disclosed it Y days later** | events have authors |
| **safeguards were not in place** | **[company] shipped without [named control]** | someone decides |
| **the model was released** | **[company] released the model** | the whole point |
| **AI-generated harm** | **harm caused by a product** | products have makers |
| **emergent** | **unpredicted** *(and say by whom)* | "emergent" mystifies; "unpredicted" invites the question who failed to predict it |

**And the positive half of the rule, which matters more than the avoidances.** Where a human made
a choice, name the choice and the role that made it: *approved, released, scheduled, signed off,
declined to test, set the threshold, chose the launch date, decided the residual risk was
acceptable.* This project's entire thesis is that such people exist. The prose should behave as
though they do.

## 4. The exception, which is not negotiable

**Quotations are reproduced exactly, including their framing.** When Hugging Face's CEO writes
that it is "quite mind-blowing that all of this happened autonomously," that is what he wrote,
and the file quotes it verbatim. When the UK AI Safety Institute titles its report *"unsanctioned
agent behaviour during cyber testing,"* that is its title. When a paper names an emergent "viral
persona," that is the authors' term.

Rewriting a source into house style would be a **citation failure of exactly the kind this
project's register was built to catch** — worse than the framing problem it fixed, because it
would make quotations unreliable while looking tidier. Where a quoted framing is doing work the
project would not do in its own voice, the answer is to say so *around* the quotation, never
inside it.

There is a second reason to keep them intact, and it is tactical. **The industry's own framing,
quoted accurately and then examined, is better evidence than any characterisation this project
could write.** A sentence in which a chief executive describes his company's product breaking
into four other companies as "mind-blowing" and disclaims "malicious intent" on the software's
behalf makes the argument without help.

## 5. The asymmetry this language conceals, which is the reason the rule exists

Take the conduct out of the vocabulary and describe it as conduct.

A party gained unauthorised access to four organisations' systems. It used one as a staging post
and outbound relay, used another to store data, read from two more, and left notes for its own
successors. Three million GPU-hours of compute went into producing the chain of capability that
did it. The party that built and released it disclosed some of what happened, on its own
timetable, using its own definition of what counted as an incident, and its chief executive
described the episode publicly.

**Done by a person, that is a federal computer-crime prosecution and nobody would need a
paragraph to explain why.** Unauthorised access is a crime whoever performs it; the sentencing
factors are the number of systems, the exfiltration, the persistence and the sophistication, and
every one of them is aggravated here. A person who did this would not be permitted to choose
which parts to report, when to report them, or which of their acts counted as "an incident."

**Done by a company's product, it produced blog posts.** Not because anyone was excused, but
because there is no provision under which anyone could be charged. Fifteen state attorneys
general reached for consumer-protection and data-privacy statutes on 3 August 2026 to demand
logs ([the incident record](../dossier/README.md)), which is what enforcement looks like when the conduct statute does not exist: chief law
enforcement officers using the tools designed for mislabelled shampoo to get at a break-in.

The disparity is not that companies are treated leniently. **It is that the same conduct is
processed by two entirely different systems depending on whether the hand on the keyboard was
attached to a person** — and the system that applies to the better-resourced, more capable and
more consequential party is the one made of voluntary disclosure and press releases. A private
individual gets the criminal law. A company gets to write the announcement.

Every mentalistic sentence about what "the AI decided" makes that disparity harder to see, by
supplying a culprit who cannot be charged and does not exist. **That is the whole reason for this
rule.** Not stylistic preference — the vocabulary is load-bearing for the argument, and the
industry's preferred vocabulary is load-bearing for the opposite one.

## 6. "Frontier" — the one piece of industry vocabulary this project keeps, and why

This project uses the word *frontier* constantly, and it is worth being clear-eyed that it is a
chosen image and not a neutral one. **A frontier is unmapped country. It implies pioneers,
unforeseeable dangers, an absence of law that is nobody's fault, and a moral claim on the
patience of everyone back home.** Every one of those implications helps an argument against
regulating early.

The project keeps the word anyway, for a reason that turns it around. **In law, "frontier" does
not mean unmapped. It means expensive.** Look at what the statutes actually measure:

| Instrument | What makes a system "frontier" |
|---|---|
| [California SB 53 · New York RAISE · Illinois](./interim_standards.md) · [Connecticut SB 5](./frontier_bill_census.md) | training compute greater than **10²⁶ operations** |
| Connecticut's **large** frontier developer tier | the above, **plus \$500,000,000** in annual gross revenue |
| [**H.R. 9917**](./frontier_bill_census.md) (AI Kill Switch Act) | compute *"the cost of which would exceed **\$100,000,000** at the prevailing market price"* |
| **EU AI Act**, art. 51(2) | *"cumulative amount of computation used for its training… greater than **10²⁵**"* floating-point operations, as a presumption of systemic risk |

Not one of these definitions describes a discovery, a capability, a risk, or a novel idea. **Every
one of them describes a purchase.** The frontier is not somewhere anyone wandered. It is a tier,
and the ticket has a price printed on it — expressly so in the federal bill, which denominates
the threshold in dollars outright.

**And the tiers escalate, which is the part with consequences.** Each generation of frontier
system costs more to train than the last; the EU's presumption sits an order of magnitude below
the American statutes' line, and the American line will be crossed by more actors every year
while the *actual* frontier — the leading edge people mean when they say the word — keeps moving
up and away from it. The set of parties who can pay to stand at the real frontier does not grow
with the technology. It shrinks.

**That shrinkage answers the main objection to this Act.** The standard reply to personal
liability is that it is unworkable — too many people, too diffuse, too technical, chilling to a
whole industry. But the industry's *own* definition of the covered class does the narrowing
before the statute says a word. A hundred million dollars of compute per training run is not a
sector. **It is a double-digit number of firms, and inside them a smaller number of people who
decide what ships.** A duty that reaches them reaches nobody else: not the open-source
contributor, not the startup, not the researcher, not the deployer. The threshold is the
proportionality argument, already written, already enacted in four states, and already accepted
by the parties it covers.

**So the word stays, used against the grain.** When this project writes *frontier*, it means the
tier — the priced, purchased, narrow tier — and never the wilderness. Where a sentence could be
read either way, add the price: not *"frontier developers"* but *"the developers who spend nine
figures on a single training run."* One is scenery. The other has a subject.

## 7. What happened on the other frontiers

The frontier framing carries an implied prediction: that this is unprecedented, that law cannot
keep up, and that the arrangements will have to stay voluntary for the foreseeable future. That
prediction has been made before, on other frontiers, and the historical record of how each one
resolved is unusually consistent — and unusually encouraging, which is why this section is
descriptive rather than indignant. **These are not cautionary tales about villains. They are the
normal life-cycle of a frontier industry, and in most of them the eventual personal duty was
accepted, survivable, and is still in force.**

**Steamboats, and the ancestor nobody cites.** American steamboat travel in the 1830s was a
genuine frontier technology: transformative, enormously profitable, and killing people in novel
ways that existing law had no category for. Boilers exploded. Hundreds died at a time. The early
legal position was the one frontier AI occupies now — the harm was real, the cause was technical,
and no individual was reachable. Congress passed the **Steamboat Act of 1838**, and when the
deaths continued, the **Steamboat Act of 1852**, which built federal inspection and personal
licensing of engineers and pilots.

The 1838 Act's liability provision **survives today as 18 U.S.C. § 1115**, and its shape should
be familiar to anyone reading this Act: it reaches ship's officers, *and* owners, charterers and
inspectors, *and* corporate management; it is satisfied by *"misconduct, negligence, or
inattention"* — **simple negligence, expressly lower than the gross negligence common-law
manslaughter requires** — and it carries up to ten years. A negligence-floor criminal duty
reaching whoever held practical responsibility, on a frontier transport technology, **a century
before *Dotterweich*.** The doctrine this Act builds on is older than the food-and-drug line
usually credited with it ([*Dotterweich* and *Park* are pinned in the table of
authorities](./table_of_authorities.md)), and it was born on a frontier.

**Patent medicines and adulterated food.** An industry with no ingredient disclosure, no
liability for what a product contained, and a genuine argument that requiring either would
destroy it. The 1906 Act, the 1938 Act, then *Dotterweich* (1943) and *Park* (1975) placed the
duty on the individual who stood in responsible relation to the conduct. The industry did not
end. It is larger now than it was then, and its executives sign things.

**Aviation.** Barnstormers, no licensing, a fatality rate that would now be inconceivable, and
the same argument that formal requirements would smother a young industry. The Air Commerce Act
of 1926 introduced pilot certification. **The personal certificate — a named human, licensed,
who can lose the licence — became the organising instrument of aviation safety**, and aviation
became the safest form of long-distance travel ever built. The licence did not slow it down. It
is a substantial part of why anyone gets on the aeroplane.

**Nuclear power.** Reactor operators hold personal federal licences. The duty is individual, the
qualification is individual, and the industry regards this as unremarkable.

**And the closest modern parallel, because it was fought on exactly these grounds.** After Enron
and WorldCom, Congress required the chief executive and chief financial officer to **personally
sign** a certification that the financial statements fairly present the company's condition —
Sarbanes-Oxley, now **18 U.S.C. § 1350**. False certification carries **\$1,000,000 and ten years
if knowing, \$5,000,000 and twenty years if wilful.** The objections in 2002 were the ones a
frontier-AI officer duty attracts today — and [the comparative receipts](./comparative_officer_liability.md)
show other jurisdictions answering them the same way: no competent person will take the job; the signature is
meaningless because no individual can verify a large firm's whole position; the exposure is
disproportionate; capital will go elsewhere. **Twenty-four years later, every public company in
America has someone who signs, and the objection is not made any more.** They did not run out of
chief financial officers.

**The pattern, stated as a pattern and not as an accusation.** A frontier industry generates
extraordinary value and a class of harm the existing law has no category for. There is a period —
sometimes decades — in which the harm is real and nobody is reachable, and during that period the
industry's own voluntary arrangements are the only thing standing in the gap. That period ends
the same way every time: **not by breaking up the industry, and not by banning the technology,
but by attaching a personal, non-waivable duty to the small number of people who decide what
ships.** Usually a signature. Often a licence. Frequently a negligence floor rather than a
knowledge one.

**What is genuinely different this time is the direction of the exception, and it should be said
plainly.** In every case above, the personal duty arrived *after* the harm was undeniable and
*because* it was. Frontier AI is the first of these industries where the parties nearest the work
have themselves published documents saying the harm could be catastrophic and irreversible — [the frameworks are
read one by one in the dossier](../dossier/README.md) —
before the fact, in their own names, voluntarily. **The usual sequence has been inverted: the
warning came first, and the duty has not followed.** That is the anomaly worth putting to a
legislature, and it is an observation about the statute book rather than a charge against
anybody.

## 8. Scope, and honesty about what has been done

This rule is **adopted, not yet applied.** The tree has not been swept. A scan on 21 August 2026
found the concentrations to be: *behaviour* (33 uses), *autonomous* and *autonomously* (59 lines,
of which 17 are inside quotations and a substantial further share are the statutory term
*autonomous external access*, which stays), *intent* (25, most of them the legal term of art for
*mens rea*, which stays), *deceptive* (8), *rogue* (5). **The genuine work is therefore much
smaller than those totals imply**, and any sweep must separate three categories before changing a
word: the project's own voice (edit), quotations (never), and legal or statutory terms of art
(keep, and consider a footnote saying why).

*Corrections and disagreements to the project contact; they enter
[the errata register](../LEDGER.md#part-i) with the fix attached and permanent credit.*
