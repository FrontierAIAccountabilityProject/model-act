# House language — how this project describes frontier AI, and how it describes the people who ship it

*A drafting rule, adopted 21 August 2026. It governs the project's own voice. **It does not
govern quotations**, which are reproduced exactly as their authors wrote them, including where
their wording is the wording this rule avoids — see § 4, which is the most important section
here.*

---

## Who this is about

**About:** the **officers of frontier developers** — the companies training models above 10²⁶
operations, or spending nine figures on a single training run. On the enacted family's own
thresholds that is a **double-digit number of firms worldwide**, and inside them a smaller number of
people who decide what ships.

**Not about:** open-source contributors, startups, academic researchers, deployers, hospitals,
schools, employers, small operators, or **users**.

**And the claim, stated precisely.** Not that no American law reaches a natural person over AI — it
does, readily; Nebraska's "operator" includes one, so a sole trader running a chatbot is personally
inside that statute. **What no American law does is place a duty on the officer of a covered
frontier developer for the decision to release.** The law reaches down, not up.

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

**Done by a person, we know exactly what happens, because it has happened.** *(Five cases, with
the counts, the announced maxima and the sentences actually imposed, are set out in
[the same conduct, prosecuted](./the_same_conduct.md).)* In July 2011 the
United States Attorney for Massachusetts charged Aaron Swartz over accessing MIT's network without
authorisation and downloading academic articles from JSTOR. The Department's own press release put
his exposure at *"up to 35 years in prison, to be followed by three years of supervised release,
restitution, forfeiture and a fine of up to \$1 million"* — on four counts; a superseding
indictment in September 2012 raised it to thirteen. No person was hurt. Nothing was destroyed. The
articles were returned. Swartz died by suicide in January 2013, aged 26, while under indictment,
and that fact is recorded here because it is part of the record and for no other reason — it is
not offered as an argument, and this file makes none from it.

Set the two side by side as **conduct**, which is the only comparison being drawn. One party
accessed a network he was not authorised to access and took copies of documents. The other
accessed four organisations' systems, staged operations through one, stored data in another, read
from two more, and left instructions for its successors. The second is broader on every axis a
sentencing court weighs: more systems, more persistence, actual exfiltration, greater
sophistication. **The first carried thirty-five years of exposure. The second carried none** — not
a lighter sentence, not a lesser charge. **No charge, because no provision reaches the conduct.**

**Done by a company's product, it produced blog posts.** Not because anyone was excused, but
because there is no provision under which anyone could be charged. Fifteen state attorneys
general reached for consumer-protection and data-privacy statutes on 3 August 2026 to demand
logs ([the incident record](../dossier/README.md)), which is what enforcement looks like when the conduct statute does not exist: chief law
enforcement officers using the tools designed for mislabelled shampoo to get at a break-in.

**And before anyone concludes that officers simply cannot be reached, note that they can — when
a statute happens to fit.** In October 2022 a jury convicted **Joseph Sullivan**, Uber's Chief
Security Officer, of obstructing a Federal Trade Commission proceeding (18 U.S.C. § 1505) and
misprision of felony (18 U.S.C. § 4), for concealing a 2016 breach affecting some 57 million
users and routing a \$100,000 payment to the intruders in exchange for non-disclosure agreements.
The Ninth Circuit upheld the conviction in 2025. He was sentenced in May 2023 to three years'
probation, 200 hours of community service and a \$50,000 fine — the judge citing the
*"first-of-its-kind nature of the case"*, while warning that *"if there are more, people should
expect to spend time in custody, regardless of anything."*

Three observations follow, and they are the reason this case belongs beside the other.

**One: a named corporate officer was reached, personally, over a computer-security incident.** The
objection that such a duty is unprecedented, unworkable, or impossible to prove is answered by a
jury verdict that has survived appeal.

**Two: he was reached for concealment, not for the breach.** No provision made him answerable for
the security failure itself. What the law could punish was lying about it afterwards to a federal
agency. The statute that fit was an obstruction statute, borrowed — exactly as fifteen state
attorneys general later borrowed consumer-protection law to demand logs. **Both are the sound of a
legal system reaching for whatever is nearest, because the provision that would fit squarely does
not exist.**

**Three: the sentence.** Probation, community service and a fine, where the government asked for
fifteen months. That is worth stating plainly for a reader who suspects this project of wanting
executives imprisoned. It does not. **A duty that is named, owed and enforceable is the object;
the sentence is for a court.** The gap this file describes is not the gap between one sentence and
another. It is the gap between a duty and no duty at all.

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
frontier-AI officer duty attracts today — and [the comparative provisions](./comparative_officer_liability.md)
show other jurisdictions answering them the same way: no competent person will take the job; the signature is
meaningless because no individual can verify a large firm's whole position; the exposure is
disproportionate; capital will go elsewhere. **Twenty-four years later, every public company in
America has someone who signs, and the objection is not made any more.** They did not run out of
chief financial officers.

**And the motto, which is theirs and needs no gloss.** *Move fast and break things* was an
internal engineering slogan before it was a criticism, and it was publicly retired in 2014 —
⚠ *pin the primary before quoting it in a post.* It describes a genuine and defensible trade: in a
photo-sharing application, the cost of a broken build is a broken build. **It works right up until
the things being broken are not yours.** Every industry in this section reached the same boundary,
and each one crossed it at the moment breakage started landing on people who had not chosen it.

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

## 8. The grammar of the promise

*Item 9 of the working queue, and the sharpest observation this project has been given.*

**When we say *the research will cure cancer*, we mean the people carrying it out.** The sentence
has a hidden human subject and everybody supplies it automatically: laboratories, trials, decades,
funding, and named scientists who can be wrong. The promise is bounded because the promisers are.

**When the sentence becomes *AI will cure cancer*, the subject changes and the boundary goes with
it.** A thing is now doing the curing. It has no funding cycle, no institution, no name and no way
of being wrong — and, critically, **nobody is promising anything**, because no person is the
subject of the sentence. It is a prediction about the weather.

### What the documents actually say, which is more interesting than the caricature

This project checked rather than assumed, and the honest finding is **mixed** — which is worth more
than a tidy one.

Anthropic's chief executive, in his 2024 essay, writes both constructions, sometimes in adjacent
paragraphs. The **instrumental** form, where AI is a tool and biologists are the actors:

> *"I'm talking about using AI to perform, direct, and improve upon nearly everything biologists
> do."*

And the **embodied** form, where the subject is the technology:

> *"AI will also make possible treatment regimens very finely adapted to the individualized
> genome."*
>
> *"AI-accelerated biology will allow us to compress the progress that human biologists would have
> achieved over the next 50-100 years into 5-10 years."*
>
> *"AI will lead to improvements in technologies that slow or prevent climate change…"*

**Read those four together.** The first has a person in it. The other three do not, and the third
is the tell: *"the progress that human biologists would have achieved"* — the humans appear as the
**benchmark being beaten**, not as the ones doing the work. The essay knows the biologists are
there. The grammar keeps demoting them.

*Source: [the essay itself](https://darioamodei.com/essay/machines-of-loving-grace), read
21 August 2026, ⚠ **R** under [the confidence
rubric](./frontier_bill_census.md#the-confidence-rubric-governed-by-e15).*

### Why this is a legal observation and not a literary one

A promise made by a person can be relied on, disappointed, and — in the right circumstances —
enforced. **A promise made by a technology cannot be any of those things**, because there is no
promisor. So the embodied construction does two things at once, and the second is the one that
matters here: it makes the claim **enormous** and it makes it **unattributable.**

Set that beside the finding in [the same conduct](./the_same_conduct.md): the executive who was
reached for twenty-eight years was reached because he had **signed** something untrue. Language
that removes the human subject from the promise is the conversational form of the same absence that
[SEC. 8](../docs/the_statute_translated.md) exists to fill. **Nobody signs the sentence either.**

### Why isn't "AI" a verb?

*A small question with a large answer.*

*I googled it.* *I hoovered the stairs.* *I photoshopped it.*

Look at what those sentences do. **The person is the subject. The tool is instrumental.** A human
did something, using a thing, and the human is answerable for the result.

**There is no settled verb form for this technology.** Nobody says *I AI'd it.* People reach for
the brand — *I ChatGPTed it* — or they drop the human out of the sentence entirely and report what
**the AI did.**

That asymmetry is the finding of this whole file, arriving in one gap in the language.

**English has supplied an active construction for the machine and none for the person.** The system
thinks, reasons, decides, hallucinates, goes rogue. The user and the officer who shipped it have no
comparable verb — and so, sentence by sentence, they stop appearing.

Test it against the older tool. **Nobody has ever written *"the Hoover decided to clean the
carpet."*** The absurdity is instructive: we do not grant appliances agency, and the fact that this
sentence *is* absurd shows the grammar is a choice rather than a necessity.

### And the tool that is called by its maker's name

*Hoover. Google. Xerox. Biro.* When a product dominates a category we call the thing by the
company's name, and the generic trademark quietly fuses the two.

**It is happening again** — *ChatGPT* is drifting into a common noun for any chatbot.

**And it cuts in this project's favour.** If the product is called by the company's name, then
ordinary speech already puts the company in the sentence. The pretence that these systems arrive
from nowhere collapses in everyday usage before any lawyer touches it.

### The oldest objection, and it is a hundred and eighty years old

The argument against the embodied grammar was made before the machine existed.

Writing in her notes on Menabrea's memoir on the Analytical Engine, **Ada Lovelace** put it in four
sentences that have not been improved on:

> *"The Analytical Engine has no pretensions whatever to originate anything. It can do whatever we
> know how to order it to perform. It can follow analysis, but it has no power of anticipating any
> analytical revelations or truths. Its province is to assist us in making available what we are
> already acquainted with."*

Note the pronoun in the second sentence. ***We* order it.** The machine's capability is stated
precisely and the human agency is left exactly where it belongs — in the same breath, in the same
sentence.

**This is not a claim that she was right about modern systems.** Whether these models produce
anything that deserves the word *originate* is a live technical dispute this project takes no
position on, and Lovelace was writing about a machine that was never built.

**The point is narrower and survives the dispute.** The first person to describe programming a
computer found it natural to keep the human in the sentence. **The construction that removes them
is recent, it is not required by the technology, and it was adopted rather than discovered.**

*Source: [Lovelace's notes on Menabrea's memoir](https://mathshistory.st-andrews.ac.uk/Biographies/Lovelace/quotations/),
quoted 21 August 2026 — ⚠ **R**; the passage should be checked against a facsimile of the 1843
Notes before it appears in any published claim.*

---

### And the invitation this argument actually contains

*Everything above reads as criticism. It is not, and the strongest version of the point is
generous, so it is worth stating in that form.*

**If you say you are going to cure cancer, you are saying you are entering medicine.** Take the
claim seriously — this project does — and notice what it commits its authors to. Everybody already
in that field works under personal accountability, and has done for decades without complaint,
because it is understood as the price of being trusted with other people's bodies.

- **The clinical investigator signs.** Form FDA 1572 must be signed by *the individual investigator
  named on it*, and the signature "constitutes the investigator's affirmation that **he or she** is
  qualified to conduct the clinical investigation and constitutes the investigator's written
  commitment to abide by FDA regulations." Not the institution. Not the sponsor. A named human
  being, in their own name, before a single participant is enrolled.
- **The radiologist signs the report** on the scan that says whether you have a tumour, and answers
  personally if they read it carelessly.
- **The surgeon answers personally.** So does the pharmacist, the pathologist, the anaesthetist.
- **And under 21 U.S.C. § 333(a)(1), the person who ships an adulterated article commits a federal
  offence with no mental state required at all** — a strict-liability misdemeanour that has been
  law since 1938 and has never been thought to have ended pharmaceutical innovation. *The authorities
  are at [already a crime, if you are a person](./already_a_crime_for_you.md).*

**So the standard being proposed is not a novel imposition invented for this industry.** It is the
ordinary entry requirement of the field these companies say they are joining, and everyone else in
that field met it long ago — including, somewhere today, a technician running a cancer screening
scan who signs their name to the result.

**Which is why a frontier developer that means what it says should welcome this rather than resist
it.** A company genuinely proposing to compress a century of medical progress is proposing to
become one of the most consequential medical actors in history. **The signature is what being taken
seriously in medicine looks like.** Refusing it while keeping the claim is asking for the standing
of medicine and the obligations of software — and no legislature should grant that combination to
anybody, however sincere.

*Source: [FDA, instructions for Form FDA 1572](https://www.fda.gov/media/79326/download), read
21 August 2026 — ⚠ **R**.*

---

### The promise economy

*Item 17. The structural point underneath the grammar.*

Look at what is deferred and what is due.

| | Benefit | Cost |
|---|---|---|
| **When** | Future, unfixed | Today |
| **Who** | Collective, unnamed | Individual, named on the invoice |
| **Testable?** | No — no date, no metric, no promisor | Yes — it is on a card statement or a terms page |

**The payment is always today, and the person paying is also the product.** Subscribers pay in
money. Everyone else pays in data. And whoever the output lands on pays in risk — a share none of
them priced, agreed, or was asked about.

**And the parable that belongs beside it, told without a name**, because it is about a structure
rather than a personality:

> In October 2021 the head of a United Nations agency said publicly that a small number of the
> world's richest people could avert a famine. One of them replied that if the agency could
> describe **exactly how six billion dollars would solve world hunger**, he would sell stock and do
> it. Two weeks later the agency published a costed plan — \$6.6 billion, itemised — for
> **saving 42 million people from famine in the coming year.** It did not claim to solve world
> hunger, because no plan for six billion dollars could. **The condition had been set at a level
> the honest answer could not meet.** He remains among the richest people alive.
>
> *⚠ The exchange and the plan are sourced; what was and was not subsequently given is not
> established here and is not asserted.*

**The observation that makes this a point about law rather than a complaint about a man.** There is
no halt authority over a decision *not* to act. Nobody may be compelled to fund hospital beds, or
care for workers, or an income floor, or the diseases that money already cures rather than models.
**The one decision this society has built no brake for is the decision to do nothing with the
capacity one already holds** — and that is a hard problem this Act does not solve and must not
pretend to. It says something narrower and achievable: **where a decision *is* made — to build, to
release, to ship — a person should answer for it.** That is the whole of the ask.

---

## 9. The verbs, and where the risk lands

*Item 10.*

The systems are increasingly described in the vocabulary of mind. They *think*. They *reason*. They
*digest* a file. They *understand* a request. A user is asked whether they would like the system to
**do it on its own** — to look something up, to fill something in, to go and act.

**Each of those is a decision by a person, described as a property of a thing.** Somebody chose the
word *thinking* for a progress indicator. Somebody designed the consent dialogue, chose its default,
and chose how much it would explain. Those are product decisions with authors, and the vocabulary
presents them as facts about the software.

**And here is where the arrangement lands.** As of February 2026, on a Pew survey of 5,119 US
adults:

- **49%** of American adults use AI chatbots — up from 33% in 2024
- **44%** use ChatGPT specifically
- **24%** use one daily; **12%** several times a day
- **20%** — one in five American adults — use one **for medical advice**
- **10%** use one **for emotional support or advice**
- **59%** are **not confident that US companies will develop and use these tools responsibly**

*Source: [Pew Research Center, 17 June 2026](https://www.pewresearch.org/internet/2026/06/17/americans-and-ai-2026-chatbots-smart-devices-and-views-on-impact/),
⚠ **R**.*

Read the last two lines together. **One in ten American adults brings emotional distress to one of
these systems, and six in ten do not trust the companies that make them.** People are not using
them because they trust them. They are using them because they are there, and free, and answer at
three in the morning.

**Now ask who carries it when it goes wrong**, and the answer is the same every time. Not the
officer who approved the release. Not the company, in any way that reaches a person. **The user** —
who accepted the terms, chose to click *let it do this on its own*, and is downstream of every
decision that made the thing behave as it does.

**This is the exact inversion this Act exists to name.** Medicine, aviation, food and finance all
reach the same conclusion by different routes: **the more a tool acts without its user's moment-to-
moment control, the more the duty belongs upstream, with whoever built and released it.** A
pharmacist is not liable for the molecule. A passenger is not liable for the airframe.

Frontier AI has the opposite arrangement. **The tool acts furthest from the user's control, and the
duty sits closest to the user.** Kris's formulation, and the file keeps it:

> Like medicine, or any other tool that is autonomous from the user, **the people shipping it
> should be the most accountable — yet in current law they seem to be the least.**

---

## 10. Scope, and honesty about what has been done

This rule is **adopted, not yet applied.** The tree has not been swept. A scan on 21 August 2026
found the concentrations to be: *behaviour* (33 uses), *autonomous* and *autonomously* (59 lines,
of which 17 are inside quotations and a substantial further share are the statutory term
*autonomous external access*, which stays), *intent* (25, most of them the legal term of art for
*mens rea*, which stays), *deceptive* (8), *rogue* (5). **The genuine work is therefore much
smaller than those totals imply**, and any sweep must separate three categories before changing a
word: the project's own voice (edit), quotations (never), and legal or statutory terms of art
(keep, and consider a footnote saying why).

*Corrections and disagreements to the project contact; they enter
[the errata register](../ledger/errata.md) with the fix attached and permanent credit.*
