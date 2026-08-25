# Known objections

This project publishes the strongest objections it knows of, with its answers, before any reviewer
arrives. Reviewers are asked to attack the draft, and this page is where the attack starts. These
are not objections the project intends to evade; they are the reason the review council exists.
Where the tagged statute already contains the answer, the section is cited — the strongest form of
pre-resistance is not "we would add a safeguard" but "it is already in the text."

## What we expect reviewers to attack

The project does not assume the proposed definitions are legally sufficient. The central review
questions include whether the enterprise category and its bracketed scale conditions are precise
enough; whether the responsible-corporate-officer doctrine can be adapted from food and drug law to
frontier AI; how responsibility should be allocated between model developers, compute suppliers,
and deployers; and what mens rea and safe-harbour provisions are constitutionally necessary. A
reviewer may conclude the central theory should be removed. That conclusion would be published.

## The objections and the answers

| Their objection | Why it is serious | The answer |
|---|---|---|
| "You are taking a technical term and making it a political label." | "Frontier" is not a settled legal category and moves over time. | Two defined terms: the technical *frontier-AI system* and the legal *covered frontier enterprise* ([the definition](./the_definition.md)). The Act regulates responsibility, not vocabulary — and the industry chose the word first, in its own frameworks and products. |
| "Wealth does not prove capability." | Market value belongs to shareholders and can be speculation. | Wealth alone covers nobody. The scale conditions operate only conjoined to a material frontier function, and the protective clause says so on the face of the definition (CURE 7). |
| "You cannot prove our model exceeded 10²⁶ operations." | Training figures are trade secrets; outside estimates can be wrong. | The figure is not proven by outside estimate: the developer certifies its own compute under SEC. 8, and lying in that certification is the offence. Self-designation (CURE 6) and Agency designation are independent routes that need no figure at all. And administrability is now conceded from both ends of the politics — chip location-verification as live federal policy, the forecasters' declaration-and-audit engineering ([two visions](./two_visions.md)). |
| "The threshold is arbitrary." | A model just below may outperform one just above. | 10²⁶ is one objective trigger among several routes, updatable by rule under SEC. 3 — and Meta's own framework adopts the same figure as its top-tier criterion, which is difficult to call arbitrary while using it. The forecasters' caution that compute units blur over time ([forecast arithmetic § 6](../research/forecast_arithmetic.md)) argues *for* the capability-designation routes riding beside the bright line — the Act's design already carries its critics' fix. |
| "*Dotterweich* and *Park* concern the Food, Drug, and Cosmetic Act." | The doctrine does not migrate automatically. | Agreed. The Act does not borrow liability; it enacts its own elements, and takes from the doctrine only the principle — duty follows the person standing in responsible relation to a public danger with power to prevent it. See [the case](./the_case.md). |
| "This is unconstitutional strict liability." | Criminal punishment without culpability raises due-process and fair-notice problems. | The Act is not outcome-liability. SEC. 6 requires a duty held, a failure of due care, and proof of every element; SEC. 1(a) states the public-welfare classification with its *Morissette* limits; the harm tier requires more, with proximate cause. Nobody is punished because a system surprised everyone. |
| "No executive can understand every technical decision." | Frontier development involves thousands of specialised decisions. | The duty is not omniscience; it is to establish, resource, supervise, and correct — and it attaches only to *final material independent decision authority*. SEC. 4(a) expressly excludes title, credentials, access, ministerial execution, and the giving of advice. |
| "Non-delegable duties are incompatible with modern management." | Delegation is how large organisations work. | Delegation of work is untouched. SEC. 4(c) bars only the delegation *of responsibility*: no safety officer, committee, subsidiary, contractor, auditor, or evaluator shields a person who retains the authority to prevent or correct. |
| "Our cloud or chip business is neutral infrastructure." | A supplier cannot police every customer. | Ordinary commodity supply is expressly out (CURE 7). A supplier is covered only at frontier scale, and its duties are the records, security, and reporting duties prescribed for *its own function* — never the developer's duties. No one answers for a layer they do not hold. |
| "We did not cause the harm — the customer or user did." | Intervening actors sit between development and harm. | Duties attach function by function under SEC. 2(a); the harm tier requires proximate cause; and independent duties (evaluation, certification, reporting) are breached or not regardless of downstream acts. |
| "Open-weight release means we lose control." | After release, the developer cannot intervene. | SEC. 1(b)(9) already answers: a release is a deployment, duties are those capable of performance *before* release — evaluation of the model as it can be modified, tamper-resistance, weight security to the moment of release (SEC. 2(a)). Lost downstream control does not erase the upstream decision. Use and study of lawfully obtained weights remain expressly protected. |
| "This chills research and innovation." | Legislatures hear this first. | SEC. 2(c) protects controlled research deployment; the records duties reward documentation; the reliance path in SEC. 2(b) gives small deployers a defined safe course. The duty begins at consequential scale, which is a choice, not an accident. |
| "This regulates speech and publication." | Weights, papers, and safety claims brush the First Amendment. | The Act regulates conduct: deployment, configuration, certification, records, reporting. SEC. 1(b)(9) protects use, study, and modification of lawfully obtained weights; no research conclusion or publication is an offence. |
| "A state cannot regulate a global supply chain." | Preemption and Commerce Clause challenges are real. | SEC. 1(c) requires an in-state nexus — conduct, availability to residents, substantial in-state effects — and SEC. 13 handles federal enactments expressly, with a review valve (CURE 2). The model-law form exists precisely so a federal twin can follow. |
| "Companies will divide the activity among subsidiaries." | Corporate separateness is a fundamental principle. | SEC. 4(a) reaches authority held "directly or indirectly … through any intermediary, entity, trust, or arrangement"; CURE 7 aggregates controlled subsidiaries, affiliates, joint ventures, and dedicated infrastructure arrangements for function and scale. Duty still lands only on persons who actually hold authority. |
| "Market values are too volatile to define legal status." | A company could enter or leave coverage on a market swing. | The scale figures are bracketed adopting-state choices, flagged as this project's proposals; review should test averaging windows, notice, and effective-date mechanics. The volatility objection is a drafting instruction, not a defeat. |
| "You rely on the companies' marketing language." | Marketing is not a confession. | Self-designation is one route among several, and it evidences a jurisdictional fact the developer remains free to rebut — having asserted it to sell the model. Compute, capability designation, and function stand independently of anyone's vocabulary; Tesla is covered analysis without ever using the word. |
| "An anonymous, AI-assisted project has no legal credibility." | Lawyers ask who is accountable for the text. | No claim of professional authority is made. The sources, version history, errata, AI-assistance disclosure, and hostile reviews are published; the text is written to be assessable without trusting its maintainer. That is why everything is versioned, hashed, and public domain. |

## The counter they will coordinate around

The industry's strongest collective position will be to accept a narrow technical definition and
reject the enterprise category: *frontier models deserve special treatment, but only the
organisations that train them should be covered; chips, cloud, data platforms, and deployment
should remain outside.* The response:

> Frontier risk is produced through a chain of controlled decisions. A model developer may control
> the weights; a cloud provider may control the compute; an infrastructure company may control
> access; an enterprise platform may control data and permissions; and a deployment company may
> control whether the system acts inside a critical institution. A law that covers only the model
> trainer leaves the other decisive points of control legally invisible.

## "You are criminalising uncertainty"

The Act would not criminalise uncertainty. It would criminalise the failure to manage uncertainty
by a person who held the authority, resources, and information to act. Liability requires a covered
activity, a person with practical authority, a defined duty, a failure to perform it, and the
applicable culpability — never an unexpected output alone. Uncertainty's legal function under the
Act is to produce a record: what was known, what was not, what was tested, who approved, what would
trigger a pause, who could stop it (SEC. 12). The recognised defences do the rest: the SEC. 4(a)
exclusions and the genuine-absence-of-authority answer preserve *Park*'s own limit — powerlessness
defeats liability; the reliance path (SEC. 2(b)) and controlled research deployment (SEC. 2(c))
give the diligent a defined safe course; and penalties are tiered, with the harm tier requiring
proximate cause and more. The shortest version:

> Uncertainty is not the offence. Unmanaged uncertainty, concealed uncertainty, and continued
> deployment after material warning are the potential offences.

## Why not voluntary standards, more agencies, corporate fines, or auditors alone

Each mechanism solves a different problem, and the Act uses all of them — with personal
accountability as the missing layer, not a replacement.

| Mechanism | Good for | Why it cannot stand alone |
|---|---|---|
| Voluntary standards | Speed, flexibility, early cooperation | Written by the company, measured by the company's definitions, revocable when competition tightens |
| More agencies | Expertise, investigation, enforcement | Jurisdictional gaps; after-the-fact posture; nobody owns the combined frontier decision |
| Corporate fines | Remediation, restitution, incentives | Absorbed as an operating cost by shareholders and customers while the decision-maker stays insulated |
| Independent auditors | Verification, challenge, evidence | An auditor reports on the decision; it cannot own or stop it |
| Personal officer duties | Decision ownership, deterrence, an evidence trail | They need the other four around them |

The record supplies the demonstrations. On voluntary disclosure: in the most consequential 2026
incident, **the victim disclosed first** — Hugging Face published its own forensic reconstruction
of the intrusion it suffered; the public learned from the harmed party, not from the developer
([press corpus](../research/press_corpus_july_august_2026.md)). That is what SEC. 9's reporting
clocks exist to prevent: the company controlling the information, the response, and the narrative
without an accountable human decision-maker. On auditors: one outside evaluator's environment is common to
four of the five disclosed incidents, across two of the three disclosing developers — "the exact
same evaluation-environment issue" recurring — which is why the auditor and evaluator are now named
in SEC. 4(c)'s non-shield list (CURE 7, Operation 4): *an audit is a control on power, not a substitute for identifying who holds the
power.* A voluntary system can encourage responsibility. An agency can investigate it. A fine can
punish the company. Only a named responsible officer makes it difficult for the decision itself to
have no owner.

## Why one named officer

Because accountability fails when responsibility is distributed so widely that nobody can be
identified as the decision-maker. After a failure, every participant in a diffuse structure can
say: I only advised; I lacked final authority; the committee approved it; another team controlled
deployment; the company decided. A named officer prevents the decision from becoming legally
ownerless, creates a real stopping point — a human who can approve, delay, restrict, suspend — and
puts the deterrent where the authority is, instead of in a fine the balance sheet absorbs.

One person does not mean one person makes every technical decision, and it does not make a
scapegoat: under SEC. 4(c), designating a responsible person "neither diminishes nor creates any
presumption against the responsibility of any other controlling person," and liability is several.
The officer is an accountability anchor; everyone else who independently held authority remains
reachable. CURE 7 Operation 3 makes the anchor mechanical: one primary responsible officer
designated per covered function — development, compute, deployment, security — in a record, before
the activity begins, with authority always controlling over designation. It is also fairer than
the alternatives: more precise than punishing the entire company, narrower than exposing every
employee, and honest about where the power actually sat.

**The record now asks the question directly — added 24 August.** At the June 2025 Oversight
hearing (Serial 119-31, read in full), Rep. Pressley asked which government employee, agency, or
board is responsible for overseeing AI deployment across the executive branch against
civil-rights violations. The minority witness, a security technologist: *"I do not believe there
is one, so if this is a test, I just failed."* The questioner's own finding: *"The
responsibility of AI civil rights enforcement is not in anyone's job description, and that has
got to change."* The same witness had already stated this section's principle twice from the
table — of AI-drafted official reports with fabricated citations: *"it is the human who puts
their name to it, who says this is correct. They are the ones responsible"*; of automated purges
run without review: *"the AI did it, but blame the humans who asked the AI to do it."* When
responsibility is in nobody's job description, the failure is not mystery; it is design. SEC. 4's
designation rule exists to put it in exactly one.

**The written record, added 24 August.** The five witness statements from the June 2025
hearing are now in hand, and none of the five names any officer responsible for executive-branch
AI — corroborating in writing what the transcript caught live. Two lines carry the weight: the
security witness — *"there is no knowing who — inside or outside of government — controls
what"* — and the fraud-analytics witness on why the condition persists: *"with little to no
consequences of this failure to invest, there are few incentives for them to do otherwise."*
Consequence-free authority producing exactly the under-investment the record documents is the
responsible-officer doctrine's premise, stated by the government's own witnesses.

## Three additions from the August record — added 23 August

**The temperament, stated by its best writer.** The strongest current statement of the opposing
disposition is Ball (FAI, May 2026, before his OpenAI role): *"a machine-enabled future means
machine-enabled tragedies, both accidents and those intentionally caused by malicious actors. We
must be steely-eyed about this, not cowed."* The answer is not that tragedy can be legislated away
— it is that *steely-eyed* has a legal meaning, and it is the one this Act supplies: a machine
future that tolerates tragedy without owners is not steely-eyed, it is ownerless. The same essay
concedes the cost point: autonomous systems make *"compliance … verifiable in seconds"* — the
records architecture's expense argued away by its opponents' own futurist
([press corpus § 5](../research/press_corpus_july_august_2026.md); the fiscal use at
[the fiscal note](../standards/fiscal_note.md)).

**"Development will flee" now runs into a mapped world.** The claimed destination regulates:
China has operated security-reviewed AI regulation since 2017 and proposes a global governance
body (ANSI summary, ⚠ P). And the flight itself now has a bloc price: Reuters reports the U.S.
preparing to tell partner countries they must choose between the U.S.-led AI coalition and
Beijing's framework — exclusion being the cost of signing both (Reuters, 14 and 19 Aug 2026, ⚠ P).
An officer-liability statute does not move the development offshore any faster than the offshore
already regulates — and the genuinely open offshore question, evaluation conduct, is held
honestly at OPEN QUESTION 4, not here.

**"The AI did it" is now foreclosed by statute in two states.** Idaho and Tennessee have enacted
laws providing that AI systems are not legal persons — ensuring, in the surveying organisation's
words, that liability falls *"on formal legal persons (either individuals or corporations) rather
than on AI systems"* (CDT, 20 Aug 2026, reusable with credit; primary texts queued at
[the census](../standards/frontier_bill_census.md#the-queue)). Two legislatures have already
answered the personhood deflection. The only question left standing is *which* legal person —
which is this Act's entire subject.

**The bloc objection now has a hearing transcript — added 24 August.** House Homeland Security's
March hearing describes the PRC threat in this objection's own register: an *"industrial-scale
campaign"* of model distillation using *"third-party routers and networks of unauthorized
resellers to circumvent existing safeguards"* — *"proxy networks and fraudulent accounts to farm
millions of interactions from American models"* — producing distilled systems that *"bypass the
critical safety guardrails embedded in U.S. systems"* (Serial 119-42, 17 Mar 2026, read in full;
the developer's own disclosure is footnoted there as Anthropic's *Detecting and Preventing
Distillation Attacks*, 23 Feb 2026 — retrieval queued). Read the description as an enforcement
problem and it makes this Act's argument: theft-by-deception is detected and attributed through
exactly the artifacts SEC. 12 requires kept — access logs, interaction records, version and
configuration identity — and the deception limb proposed at
[CURE 16](../audit/v3_5_cure_language.md#cure-16--sec-1b7-a-deception-limb-because-van-buren-excludes-what-actually-happened)
is what makes the conduct chargeable when it happens here. A records regime is not the opposite
of competing with the bloc; it is the attribution machinery a state needs before it can even say
what was taken.

## "So this is an FDA for AI?" — no, and the difference is the design — added 24 August

The question arrives from both directions: critics who fear a licensing agency, and allies who
ask why the Act does not create one. The answer is on the statute's face. SEC. 3(b): *"No
standard, rule, or mode of validation under this Act may condition any deployment, expansion, or
release upon the prior affirmative approval of the Agency or of any officer of this State."*
**The Act takes the FDA's doctrine and refuses the FDA's licence.** From food-and-drug law it
borrows the responsible-relation principle — duty on the person standing between a public danger
and the public — and the post-market machinery: records, reporting clocks, certification,
enforcement. What it deliberately does not borrow is premarket approval: no queue outside an
agency's door, no examiner deciding what may ship, no bottleneck for the innovation objection to
point at.

The literature the project holds argues both sides, and the design answers each. Against
approval-regulation: the pharmaceutical model fits a protracted, stable development process, and
frontier development "could not be more different" (the entity-based paper's contrast, citing
Carpenter & Ezell's *An FDA for AI?* — the pitfalls analysis). For it: the 2026 record shows the
government reaching for pre-release review the moment a model frightened it — the Mythos
restriction, the White House's brief exploration of predeployment review, the voluntary
framework it settled into (E.O. 14409), and CAISI's predeployment agreements
([the census](../standards/frontier_bill_census.md) and
[the watch](../audit/standing_watch_2026-08-20.md) own the facts). The survey literature's own
verdict is that a licensing or pretesting regime *"can only be part of the story"* — effective
governance also requires *"continuous postmarket monitoring, incident response, and enforcement
mechanisms"* (CSIS, Aug 2026, ⚠ P). **That second half is what this Act is.** Where the voluntary
predeployment regime depends on the developer's continued goodwill, the Act attaches duties that
survive the handshake — and it does so without ever making the State a gatekeeper, which is both
the constitutional posture (no prior restraint anywhere in the design) and the honest answer to
the innovation objection: nothing in this Act delays a single deployment by a single day. It
prices the decision; it never takes the decision away.

**A characterisation of ours, corrected, 25 August.** This project had filed Emilia Javorsky, on
the strength of her Noema essay's title, as the clearest advocate of the approval model and
therefore the natural opponent of this design. Her March 2026 essay *How AI Can, and Can't, Cure
Cancer* (read in full; in the source library) does not support that filing, and the error is
recorded here rather than quietly dropped, because inferring a position from a title is exactly
what this project's own rule forbids.

Her assessment of the agency is not the one an approval-model advocate would write:

> "The FDA is thought of as an agency designed to make sure new drugs are safe and effective prior
> to being sold in the United States, but as with all things, the devil is in the details. Close
> examination reveals a 20th century agency ill-equipped to manage accelerating scientific
> understanding."

And her account of why the sector resists structural constraint reads as this Act's own premise,
stated by a physician:

> "Having spent the duration of their life cycles largely free from liability under Section 230,
> and as they are currently advocating for federal AI amnesty, Silicon Valley is uniquely
> ill-prepared to confront the significant regulatory constraints governing the transition of
> successful science into approved therapy."

**Why this matters beyond the correction.** The essay also supplies a clinician's answer to the
acceleration argument that shadows every AI regulation debate, that constraint delays cures. Her
finding, from having taken therapies from bench to bedside, is: "I have seen how a new therapy is
developed, and intelligence, super or otherwise, was definitely not the bottleneck." That is the
same conclusion Kierans, Casper & Ghosh reach from alignment research, by a wholly independent
route. Two fields, one finding: the binding constraint is institutional. **The Act's use of this
is bounded.** Neither author is claimed as a supporter, and neither has been asked. What the
convergence supports is narrower: the premise that legal and institutional architecture is the
place where outcomes are actually decided.

## "It shouldn't target AI companies" — the objection an assistant will raise — added 24 August

Ask a general-purpose AI assistant to review this Act and some version of that sentence tends to
come back. It is worth answering in advance precisely because it will be generated fresh, in
confident prose, for every reviewer who asks — and because each specific thing it can mean is
already answered, mostly on this page. (This project is AI-assisted and discloses it; the point is
not that assistants are wrong to check. It is that the generic objection dissolves into four
specific ones the moment it is made precise.)

**If it means "the Act singles out an industry":** it does not target companies, and no company is
named in the operative text. Coverage attaches to a hazard — defined capability, function, and
scale thresholds — exactly as food-and-drug law attaches to whoever ships the adulterated lot and
environmental law to whoever holds the permit. The responsible-corporate-officer doctrine is the
general law of hazardous enterprise, applied for eighty years to drug shippers, grocery-chain
presidents, and egg producers. The Act does not single frontier AI out of the ordinary law; it
ends frontier AI's exemption from it.

**If it means "regulate uses, not developers":** that is the coordinated counter answered above —
a law that reaches only the point of use leaves the decisive points of control legally invisible.
The record now carries the industry's own version, sworn to Congress: a *"tech-neutral,
preemptive … risk based"* framework that *"removes liability for companies that are compliant"*
([why the disparity](../standards/why_the_disparity.md)). The Act is risk-based in the only sense
that survives that request: the risk decides who is covered, and compliance is the duty — never
the immunity.

**If it means "it chills the small and the open":** the thresholds exclude small labs by design;
controlled research deployment is protected (SEC. 2(c)); use, study, and modification of lawfully
obtained weights are expressly protected (SEC. 1(b)(9)); the table above answers the innovation
and speech forms directly.

**And if it means "the burden should fall on people, not companies":** that is not an objection to
this Act; that is this Act. The duties reach the natural person who held final material authority
— the entity sits at the trigger, the person answers for the duty. An assistant raising this
version has read the design correctly and objected to its own summary.

A practical note for a reviewer working with an assistant: the per-lane errata on
[the reviewer page](../REVIEWERS.md) exist because assistants reproduce known misreadings of this
draft. Check the generated objection against this page and against your lane's errata row before
spending your hours on it — and if your assistant produces a version none of the four above
covers, that is worth sending: a genuinely new objection is the most valuable mail this project
receives. And when the assistant's version arrives dressed as *"the states are already
handling this"* — an affirmative-defense statute here, a sandbox there — the pattern has its own
page: [safe harbors, affirmative defenses, and the half-statute](./safe_harbors_and_affirmative_defenses.md).


## "You will delay the cures" — the acceleration objection, answered with clinical numbers — added 25 August

The objection is rarely stated in a hearing room in these words, but it underwrites most of the
others: constrain frontier AI and you postpone the medicine it would otherwise deliver. It is the
most emotionally powerful thing said against regulation of this technology, and it is usually
answered with assertion. It can be answered with evidence.

The evidence used here is a physician's, not a lawyer's. Emilia Javorsky, MD, MPH, Director of the
Futures Program at the Future of Life Institute, published *How AI Can, and Can't, Cure Cancer*
in March 2026 (read in full; in the project's source library). She is not a critic of the
technology, and her essay's closing sections argue for scaling AI tools in oncology. Her account
of what actually gates medical progress is the point:

> "I have seen how a new therapy is developed, and intelligence, super or otherwise, was
> definitely not the bottleneck."

**The arithmetic of acceleration.** Her numbers are specific enough to argue with:

> "On average, it takes 10.5 years for a drug to move from Phase I through regulatory approval.
> For drugs entering Phase I, 90% will fail somewhere along the pathway, with lack of clinical
> efficacy representing 40-50% of failures and safety concerns another 30%. This is not a problem
> of insufficient intelligence in trial design, it's the inherent challenge of safely testing
> interventions in humans on biological timescales."

And on what the compression claims are worth:

> "while AI's role in accelerating drug discovery sounds like a 90% improvement to the public, the
> reality is more modest, perhaps 10-20% time savings because you're only radically condensing the
> initial pre-clinical phase of drug development."

**The case that settles it.** Her strongest example is a controlled experiment nobody designed. In
2020 AI identified a novel antibiotic candidate, Halicin. The science worked:

> "Unlike HAL, the AI worked. The chemistry worked. The mouse studies worked. Further, compared to
> most drugs, antibiotics that work in mice have a high predictive value to work in humans. The
> clinical need is desperate, with antibiotic resistance killing an estimated 1.27 million people
> globally each year. But, five years later, where are these antibiotics? The problem wasn't with
> the science, it was with the market."

Three companies are named as the pattern: Achaogen bankrupt in 2019 despite FDA approval for
plazomicin, Melinta in bankruptcy, Aradigm out of antibiotics altogether. **A capability that
existed did not become a medicine, and no amount of additional capability would have changed
that.** Whatever is holding back the cure, on this evidence it is not a shortage of intelligence,
and a statute that reaches the people who decide is not competing with the cure for the same
scarce resource.

**The deeper point, and why it belongs on this page rather than a footnote.** Javorsky's account
of how the technology sector's optimising culture behaves when it meets a complex system is the
externality argument this Act rests on, arrived at from medicine:

> "In optimizing for user engagement, narrow AI algorithms successfully drove profits but also
> left behind increased rates of depression, impaired cognitive development in youth, erosion of
> social trust, and the spread of misinformation. From Big Tech's perspective, this approach
> proved extraordinarily profitable and the negative externalities were borne by users and
> society, not the companies."

That last sentence is the case for personal liability stated in economic terms. Where the gains
are internal and the costs external, entity-level penalties are priced in as a cost of doing
business; the responsible corporate officer doctrine exists precisely because some decisions must
be made by a person who cannot hand the bill to someone else.

**What is claimed and what is not.** Dr Javorsky has not been asked about this Act, has not
reviewed it, and is not claimed as a supporter; nothing in her essay addresses officer liability.
The essay is cited for three findings within her expertise: that intelligence is not the binding
constraint in therapeutic development, that acceleration claims are overstated by roughly an order
of magnitude, and that market structure can strand a working discovery. A reviewer who thinks this
page leans on her further than those findings support should say so, and the disposition would be
published.


## "The states have already legislated, so this is redundant" — added 25 August 2026

The objection has force: California, New York and Illinois have enacted frontier AI statutes, and a
legislator asked to consider a fourth instrument is entitled to ask what it adds.

**What it adds is a trigger.** Those statutes, on CSIS's account, "rely on high critical safety
thresholds involving at least 50 deaths or $1 billion in damages" (Aalok Mehta, 24 Aug 2026). Now
apply that to the documented events of 2026: agents escaped their evaluation environments, reached
the open internet, exploited zero-days, compromised a third party's servers, and reached customer
data; three developers disclosed such incidents; a foreign open-weight model broke a national safety
institute's evaluation environment. On the same authority, "it is unclear whether any existing U.S.
law requires reporting of the Hugging Face or Anthropic, or similar, incidents."

**Not one of the year's disclosed incidents is known to have triggered any enacted state statute.**
Every disclosure that reached the public did so voluntarily, or because the victim went first.

That is the redundancy answered. A regime triggered by catastrophe is silent until catastrophe; this
Act's duties attach to conduct and to authority instead, which is why the same events would fall
inside it. The honest cost of that choice is that it reaches conduct which harms nobody, and a
reviewer who thinks the trade is wrong should say so.

## "You cannot prove an AI system caused the harm" — added 25 August 2026

This objection is usually raised in the abstract. It now has a courtroom.

Twenty-six former Meta employees, all on protected leave during a May 2026 reduction in force,
alleged the company "used a constellation of internal artificial intelligence systems," including
one monitoring "employees' keystrokes and computer activity," to "score, rank and select employees
for inclusion on the list." On 24 August 2026 U.S. District Judge William Orrick declined a
preliminary injunction:

> "I have a record I have to deal with and the record at the moment does not persuade me of the
> merits."

> "the plaintiffs' evidence raised some potential questions about Meta's categorical denial of any
> impact of AI in the termination process, and they provide further evidence of harm, but they don't
> persuade me that injunctive relief is warranted."

He called it "an unusual, or a new sort of issue" that was hard to gather evidence for at the outset
(Courthouse News, 24 Aug 2026; [press corpus](../research/press_corpus_july_august_2026.md)).

**The answer, and it is the whole reason the records provisions exist.** The claim did not fail
because automated decision-making is unprovable in principle. It failed on the record available to a
plaintiff who was outside the system that made the decision. Every logging, retention and reporting
duty in this Act is drafted against precisely that asymmetry: not to prove liability, but to ensure
that the facts exist somewhere a court can reach them, created before anyone knew they would be
needed. A statute that imposes duties without requiring the records that would show whether they
were met is decorative, which is why the enforcement and security lanes are asked whether these
records could actually be produced.

**What this case is not.** It is not authority for anything, it is a denial of interim relief on an
incomplete record, and this Act does not reach employment decisions at all. It is quoted because it
is the clearest judicial statement yet of the evidentiary problem the Act's plumbing exists to
solve.

## "The timelines make this pointless" — added 24 August

The objection, stated at its strongest: the field's own forecasters put the modal year for
transformative capability inside this decade, with intervals between late milestones measured
in months — so a state statute drafted on legislative time regulates a world that will have
ended before third reading. It deserves a serious answer because the numbers behind it are
serious ([the forecasters' arithmetic](../research/forecast_arithmetic.md), § 3).

The answer is that the objection defeats the wrong plan. It is fatal to *beginning* drafting
when the window opens — which is precisely this project's position
([paths to enactment](./paths_to_enactment.md)): public-welfare statutes pass in the weeks
after the failure that makes them undeniable, and what passes is whatever reviewed text
already exists. Fast timelines shorten the window; they do not shorten the need for the
drawer — they are the case for filling it now. And if the forecasters are wrong and the
decade is ordinary, the Act costs what a vetted draft costs: nothing, until a legislature
wants it. The asymmetry runs one way. A reviewer who believes the timeline objection should
say in a disposition which leg fails: the window pattern, the arithmetic, or the asymmetry.

*The argument this page defends: [the case](./the_case.md). The definitions it defends:
[the definition](./the_definition.md). The operative language under attack:
[the statute](../model_act_v3_4.txt) and [the v3.5 queue](../audit/v3_5_cure_language.md).*

**The answer sharpened, 25 August, from inside the alignment field.** The objection assumes
technical progress outruns legal process, so institutions arrive too late to matter. The strongest
published statement of the contrary case is Kierans, Casper & Ghosh, *Intelligence Is Not the
Bottleneck: Structural Barriers to Automating Alignment Research* (2026, read in full; in the
project's source library). It names the claim it rejects: that "datacenters full of research
agents will compress a decade's worth of alignment research progress into 6-12 months." Its
finding is that "structural barriers, not intelligence, are the principal bottleneck," and its
central sentence is the one this Act is built on:

> "The parts of alignment that remain unsolved are not waiting for smarter, more numerous
> researchers; they depend on whether we build mechanisms that allow accelerated research to
> accumulate into something reliable. That is not yet happening, at least to public knowledge."

Two further observations from the same paper bear directly on the objection's provenance. First,
the assumption is convenient for the people who hold it: it "offers a very convenient agenda for
companies who are racing to develop increasingly powerful AI." Second, without institutional
work, automated alignment "might be abused as a safety-washed euphemism for automating AI
capabilities progress."

If that analysis is right, the timelines objection inverts: a constraint that is institutional
rather than technical is not outrun by capability, and building durable legal mechanisms is the
work rather than a distraction from it. **The Act's stake in this is honest and limited.** It does
not claim the paper endorses officer liability; it claims the paper undercuts the premise that
legal architecture cannot matter on these timescales. A reviewer who thinks that reading stretches
the paper should say so, and the disposition would be published.
