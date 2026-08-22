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
| "You cannot prove our model exceeded 10²⁶ operations." | Training figures are trade secrets; outside estimates can be wrong. | The figure is not proven by outside estimate: the developer certifies its own compute under SEC. 8, and lying in that certification is the offence. Self-designation (CURE 6) and Agency designation are independent routes that need no figure at all. |
| "The threshold is arbitrary." | A model just below may outperform one just above. | 10²⁶ is one objective trigger among several routes, updatable by rule under SEC. 3 — and Meta's own framework adopts the same figure as its top-tier criterion, which is difficult to call arbitrary while using it. |
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

*The argument this page defends: [the case](./the_case.md). The definitions it defends:
[the definition](./the_definition.md). The operative language under attack:
[the statute](../model_act_v3_4.txt) and [the v3.5 queue](../audit/v3_5_cure_language.md).*
