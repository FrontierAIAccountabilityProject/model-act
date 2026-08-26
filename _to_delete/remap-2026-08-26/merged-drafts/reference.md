---
title: Reference
nav_order: 6
---

# Reference

*Four things you look up rather than read: what the words mean, what the Act is built on, the texts
it adopts, and the choices an adopting state has to make.*

**Contents** — [Glossary](#glossary) · [Sources](#sources) · [Adopted standards](#adopted-standards) · [Choices for your state](#choices-for-your-state)

---

## Glossary

> ## Can a model act?
>
> **Not in the legal sense.**
>
> *In other senses, perhaps. These systems call tools, take steps and pursue objectives, and people
> who build them use the word* act *for that without confusion. **This file does not dispute it and
> the argument does not need it.***
>
> *To act **in law** is something narrower and more demanding: to be a person who can hold
> authority, owe a duty, be served with process, appear, answer, and be punished. **A model is not a
> legal person, and calling it agentic does not make it one.** It has no mind the law can inquire
> into and nothing the law can do to it.*
>
> ***So the acts that matter here belong to people whichever way the other question is settled.***
> *Somebody trains it. Somebody releases it. Somebody decides it is ready. Those are acts in the
> legal sense, and acts in that sense have actors. The statute is named after the difference.*

---

### Who this is about

**About:** the officers of frontier developers — companies training models above 10²⁶ operations.

**Not about:** open-source contributors, startups, researchers, ordinary deployers and API
customers, or users. *A deployer is a defined class under the Act and always has been
(SEC. 1(b)(3)); what the thin ones get is a route to discharge the duty, not an exemption from it
(SEC. 2(b)). See [the case](../docs/the_case.md#who-this-is-about).*

**And what this file is not.** Not a technical authority. It is a legislator's glossary, written so
that someone drafting a definition knows which word does what. **Where the honest answer is
contested, it says so.** Corrections from people who build these systems are the most valuable
thing anyone could send.

---

### Why a glossary belongs in a statutory project

Every enacted frontier statute defines its scope by **compute** — 10²⁶ operations — rather than by
what a system is or does.

That is not laziness. It is what happens when nobody can agree on the nouns. A threshold you can
measure is safer to draft than a capability you cannot define.

**But it means the words below are doing legislative work while remaining undefined in law**, and a
member asked to vote on "AI" is being asked to vote on a word that covers a spam filter and a
frontier model equally.

---

### The core terms

| Word | What it literally is | What it can actually do | How it is sold |
|---|---|---|---|
| **Algorithm** | A fixed sequence of steps, written by a person. Older than computers — long division is one. | Exactly what its author specified, every time, checkably. | *"The algorithm decided"* — a phrase that hides the author. Somebody wrote the steps. |
| **Model** | A set of numbers plus a function that maps an input to an output. The word is borrowed from statistics: a model **of** something, like a line of best fit. | Produce an output for an input. Nothing else. | As an entity with views, intentions and a personality. |
| **Parameters / weights** | The numbers. Modern frontier models have hundreds of billions of them. | Nothing on their own — they are the fitted state. | As a proxy for capability, though the count alone tells you little. |
| **Training** | The process of adjusting those numbers so outputs better match the data. **A person starts it, on hardware someone pays for, at a cost that can be stated in dollars.** | Produce a fitted model. | As something that *happens* — "the model learned" — rather than something a company does. |
| **Inference** | Running the fitted model on new input. What happens when you type a question. | Produce output. | Rarely named at all in public discussion. |
| **Neural network** | A particular shape of mathematical function, arranged in layers. The biological name is an analogy from the 1940s and has misled people ever since. | Approximate very complicated functions, given enough data and compute. | As a brain. It is not one. |

---

### The category words, which decide what a law covers

| Word | What it means | Note for a drafter |
|---|---|---|
| **Machine learning (ML)** | Fitting a model to data rather than writing the rules by hand. | Covers almost everything, including spam filters and credit scoring. Too broad to be a statutory hook. |
| **AI** | No settled technical meaning. In practice: whatever is currently impressive. | **The least useful word in the debate.** A statute using it without definition covers everything and nothing. |
| **Language model** | A model trained to predict the next piece of text. | Precise and useful. |
| **Large language model (LLM)** | The same, at scale. | "Large" is undefined and moves every year. |
| **Generative AI** | Models producing new output — text, images, audio, video — resembling their training data. | The category FDA's [August 2026 docket](../filings/frontier_ai_in_medicine.md) is about. |
| **Foundation model** | A large model trained broadly and intended to be adapted to many uses. | The nearest thing to a technically honest term for what this Act covers. |
| **Frontier model** | **A priced tier.** Defined in every enacted statute by compute — above 10²⁶ operations, or over \$100,000,000 of compute in H.R. 9917. | Not a capability claim. A purchase. See [house language § 7](./house_language.md). |
| **General-purpose AI** | The EU's term for the same family, with a systemic-risk presumption above 10²⁵ FLOP. | Useful for comparative drafting. |
| **Narrow / task-specific model** | A model trained for one job — reading a mammogram, flagging a transaction. | **Most FDA-authorized AI devices are these, not frontier models.** Conflating them is the commonest error in this debate. |
| **AI-enabled medical device** | A regulated device incorporating any of the above. | A regulatory category, not a technical one. |

---

### The words that carry the most freight

**Agent / AI agent.** A model connected to tools — a browser, a terminal, a payment method — and
run in a loop so its output becomes its next input.

**This is the most consequential and least understood word in the debate.** It does not describe a
new kind of mind. It describes a **wiring decision made by a person**: what tools to connect, what
permissions to grant, whether to require confirmation. Every one of those is a product choice with
an author.

**AGI.** No agreed technical definition, no accepted test, no measurable threshold. **It is an
aspiration and a fundraizing term**, and a drafter should treat it as unusable in statutory text.

**Alignment.** Making a system's outputs match what its developers intend. Note the word: *intend*.
**Alignment is defined relative to the developer's goals**, not the public's — which is precisely
why it is a matter for a legislature and not only for engineers.

**Emergent — and "malicious, emergent."** In the technical literature, *emergent* describes a
capability that appears at scale without having been individually engineered — nobody wrote the
rule; the fitted numbers turned out to contain the behavior. The literature itself disputes how
sharp these emergences really are, and the word does honest work when it describes **how a
capability arose**. It does no work at all on **who deployed it**. The recorded use to study: a
senior developer officer describing the July incident as *"a malicious, emergent digital ecology"*
([the record](../research/press_corpus_july_august_2026.md)). Read the two adjectives together:
*malicious* locates a mind in the system — which the legal words below explain no statute can
reach — and *emergent* removes the person from the origin. The pairing concedes the harm while
placing both intent and authorship beyond anyone the law could name. The front page's answer is
the right one for a drafter: in 2010, nobody asked whether the salmonella was an emergent ecology.
Emergence describes the system. Training, evaluating, releasing, and deploying are acts — and acts
have actors.

**Hallucination.** Confident false output. **The word is itself an example of what
[house language](./house_language.md) warns about** — hallucination is something a mind does.
*Confabulation* is closer, and *"the system produced a false statement"* is closest, because it
leaves room for the question of who is answerable for it.

**Machine intelligence.** The field's oldest name for itself — the term of Turing's generation,
older than *artificial intelligence* — and, like "AI" in the table above, a phrase with no
statutory definition anywhere. In current use it is a register rather than a category: *"digital
ecologies of machine intelligence"* ([the record](../research/press_corpus_july_august_2026.md))
reads as a description of nature, not of a product. *Intelligence* is the freight — it grants the
system the one thing the legal words below explain it cannot hold, a mind — and *ecology*
completes the move by recasting the builders as naturalists who found the thing growing. For a
drafter it behaves exactly like "AI": undefined, unmeasurable, doing its work by connotation. The
compute threshold exists so that no statute ever has to decide what intelligence is. (By 2026
the register had reached a federal bill's own backronym — the "TRUMP AMERICA AI Act" unpacks to
a phrase containing *"Advancing Machine Intelligence"* ⚠ — which is the word doing exactly the
work described above, this time on a title page.)

**"AI psychosis."** ⚠ **Slang, not a clinical term, and recorded here only as a usage.** It is used
jokingly about people — sometimes very wealthy ones — who speak about these systems as conscious,
godlike, or in love with them. **It is not a diagnosis, this project does not adopt it, and it does
not describe any named person.** Separate and serious questions about psychosis and chatbot use are
**queued for their own file** and are deliberately not addressed here.

---

### The legal words, since half the confusion runs the other way

**Disposition.** A reviewer's determination of a question they took, published as written. Borrowed
from the judicial sense, where a disposition is how a matter is finally determined rather than
merely discussed. In this project it means: the reviewer decides, the maintainer publishes without
editing and may only respond beside it, and the finding stands under the reviewer's name or
anonymously at their election. It is not advice, not a consultation, and never an endorsement. The
rules of publication, fixed before the first one arrived, are at
[the dispositions register](../dispositions/README.md).

**Lane, and seat.** A *lane* is a subject area of the review: criminal law, enforcement, frontier
security, fiscal, federalism, proportionality, torts and design, open source and academia. A *seat*
is the position a reviewer occupies in a lane. Lanes run in parallel and no lane waits on another;
reviewers are not shown each other's identities.

**Mens rea** — *the guilty mind.* The mental element a crime requires: intent, knowledge,
recklessness, or negligence. Most serious offenses need one.

**A model cannot have it.** Not as a matter of philosophy but as a matter of law: mens rea is a
state of a person, and there is no legal machinery for attributing one to a fitted function. **This
is the sharpest reason the duty must attach to a human being** — not because machines are innocent,
but because the concept does not apply to them, and a statute that pretended otherwise would be
unenforceable on its first day.

**Which is exactly what the public-welfare doctrine is for.** *Morissette* (1952) marks out a
category of offense where the traditional mens rea requirement is relaxed because the conduct is
regulatory and the danger is public. *Dotterweich* (1943) and *Park* (1975) place the resulting duty
on **the person standing in responsible relation to the conduct** — and the floor is **negligence**,
not knowledge. See [the table of authorities](./table_of_authorities.md).

**So the sequence runs:** the system has no mind → the law cannot ask it for one → the question
becomes *which person had the authority to prevent this, and did they take due care?* **That is a
question about a human being, and it is answerable.**

**Strict liability** — an offense needing no mental element at all. Rarer than people think, and
already applied to individuals: 21 U.S.C. § 333(a)(1) makes shipping an adulterated article a
federal crime with no intent requirement whatsoever. *See [already a crime, if you are a
person](./already_a_crime_for_you.md).*

**Responsible corporate officer doctrine** — the rule that an officer with authority to prevent or
correct a violation answers personally for failing to. Eighty years old, and it has traveled once.

It began in food and drug, and moved into environmental enforcement, where **Congress wrote it into
the statute**: the Clean Water Act defines "person," for the purpose of its criminal subsection, to
mean "any responsible corporate officer" (33 U.S.C. § 1319(c)(6)). One scholar records that "in the
twenty years following the *Park* decision, the overwhelming majority of responsible corporate
officer prosecutions were based on violations of environmental laws rather than the [Food, Drug,
and Cosmetic Act]" (Copeland, quoted in Lyness, 64 B.C. L. Rev. 253, n.32). And in
*United States v. Iverson*, 162 F.3d 1015, 1024 (9th Cir. 1998), the court reasoned that when
Congress rewrote the CWA's criminal provisions after *Park* it "made no changes to its 'responsible
corporate officer' provision," so Congress may be presumed to have intended *Park*'s refinement to
apply.

**What has never happened is its extension to software.** That is this project's claim, and it is a
narrower and better one than the version this page carried until 25 August 2026 — see
[E42](../ledger/errata.md#e42--the-doctrine-was-said-never-to-have-left-food-and-drug-it-left-decades-ago-by-act-of-congress).

**Respondeat superior** — Latin, *"let the superior answer."* The master answers for the servant.
It is the doctrine that lets a company be criminally liable at all, because a company has no mind
of its own for the law to inquire into. Per CRS, courts analyze corporate mens rea "by reference to
the principle of respondeat superior — under which corporations can be responsible for the acts of
their employees acting in the scope of their employment with the intent to benefit the
corporation." Or as the D.C. Circuit put it in *United States v. Philip Morris USA Inc.*,
566 F.3d 1095, 1118 (2009): "Because a corporation only acts and wills by virtue of its employees,
the proscribed corporate intent depends on the wrongful intent of specific employees."

**Where this Act stands, and it is the argument rather than a concession.** If corporate intent
already depends on the intent of *specific employees*, then a statute that goes directly to the
specific person is not a departure from corporate criminal law. **It is the same idea with the
detour removed.** The company remains liable under SEC. 10(a); this Act simply declines to stop
there.

**Collective knowledge** — the doctrine that lets prosecutors add up what several employees each
knew and treat the total as the company's knowledge, even where no single person held the whole
picture. *United States v. Bank of New England, N.A.*, 821 F.2d 844, 856 (1st Cir. **1987**), in
the First Circuit's own words: "A collective knowledge instruction is entirely appropriate in the
context of corporate criminal liability. . . . Corporations compartmentalize knowledge, subdividing
the elements of specific duties and operations into smaller components. The aggregate of those
components constitutes the corporation's knowledge of a particular operation." The instruction it
approved, quoted in the opinion: "if Employee A knows one facet of the currency reporting
requirement, B knows another facet of it, and C a third facet of it, the bank knows them all."

⛔ **This entry previously dated the case 1984 and gave a different sentence as the First Circuit's**
— "a corporation cannot plead innocence by asserting that the information obtained by several
employees was not acquired by any one individual . . . ." That sentence is real and is in the
opinion, but it is a **block quotation from *United States v. T.I.M.E.-D.C., Inc.*, 381 F. Supp. 730,
738 (S.D. W. Va. 1974)**, quoted with approval. The case was decided **10 June 1987**
([E67](../ledger/errata.md)). ⚠ 856 stays the secondary source's — no star pagination
([E47](../ledger/errata.md)).

**Why the doctrine exists is the part that matters here.** Uhlmann, 49 U.C. Davis L. Rev. 1235,
1280 (2016): "Corporations compartmentalize knowledge and subdivide operational duties to promote
corporate efficiency." That is a description of every large organization, and it is an unusually
exact description of a frontier laboratory, where the people who evaluate a model, the people who
ship it and the people who price the compute are three different sets of people.

**And courts are split on it.** CRS records that some have recognized the doctrine and "other
courts have been wary or critical of this approach."

**Where this Act stands, stated more narrowly than it used to be.** SEC. 6 reaches the natural
person with practical authority. The prosecution must prove what *this person* knew or failed to
inquire into, not what the organization collectively held. That is harder for the State and fairer
to the defendant, and a reviewer who thinks it makes the offense unprovable in a compartmentalized
company has found a real objection.

⚠ **This page used to say the Act "declines to aggregate", and that claimed too much.** Read in the
opinion, collective knowledge is a rule of **corporate** criminal liability — employees' knowledge
"is imputed to the corporation," and the aggregate "constitutes the corporation's knowledge." **No
case in the First Circuit's string aggregates several people's knowledge onto one defendant.** The
doctrine was never available against a natural person, so the Act is not giving up a tool; it is
working where the tool does not reach ([E67](../ledger/errata.md)).

**Willful blindness** — also called *conscious avoidance*, and in older cases *the ostrich
instruction*. Deliberately not looking, where looking would have produced knowledge. The classic
formulation is *United States v. Jewell*, 532 F.2d 697, 704 (9th Cir. 1976) (en banc): the
government must prove "beyond a reasonable doubt, that if the defendant was not actually aware [of
the crime] . . . his ignorance in that regard was solely and entirely a result of . . . a conscious
purpose to avoid learning the truth." ✅ **Read 26 Aug 2026**; the words are the trial court's
instruction, adopted by the en banc court. ⚠ 704 unconfirmed — no star pagination. Restated in
*United States v. Cincotta*, 689 F.2d 238, 243 n.2 (1st Cir. 1982): "specific knowledge may be
inferred when a person knows other facts that would
induce most people to acquire the specific knowledge in question." ✅ **Read 26 Aug 2026, and "n.2"
is confirmed even though 243 is not.** ⚠ **This entry used to call *Cincotta* a narrowing of *Jewell*,
and its next sentence widens it** ([E73](../ledger/errata.md)): "if someone refuses to investigate an
issue that cries out for investigation, **we may presume that he already 'knows' the answer** an
investigation would reveal, whether or not he is 'certain'." The "only" limits what conscious
avoidance **is**, not how far the inference reaches. The ceiling is *Global-Tech
Appliances, Inc. v. SEB S.A.*, 563 U.S. 754, 769 (2011), which states the test the Courts of Appeals
had converged on: "all appear to agree on two basic requirements: (1) The defendant must
subjectively believe that there is a high probability that a fact exists and (2) the defendant must
take deliberate actions to avoid learning of that fact." Those requirements "give willful blindness
an appropriately limited scope that surpasses recklessness and negligence": the willfully blind
defendant "can almost be said to have actually known the critical facts," whereas "a reckless
defendant is one who merely knows of a substantial and unjustified risk."

**Read in the U.S. Reports print on 26 August 2026, and it corrects two things this glossary said.**
This page called *Global-Tech* a **constitutional** ceiling. It is not one — the case is a civil
patent suit under 35 U.S.C. § 271(b) and decides no constitutional question
([E65](../ledger/errata.md)). And the ordering above is not a narrowing sequence: *Cincotta*'s
"induce most people" is an objective inference, while *Global-Tech* requires a **subjective** belief
in a high probability **and** deliberate action to avoid confirming it. **The Supreme Court's test is
the harder of the two for a prosecutor**, and a reader who took this paragraph as a descent from
broad to narrow had it backward.

**The doctrine's traffic runs criminal-to-civil, not the reverse.** *Global-Tech* records that
willful blindness "is well established in criminal law" and then extends it: "we can see no reason
why the doctrine should not apply in civil lawsuits for induced patent infringement." Nothing in the
opinion narrows it for criminal cases.

**Congress did not leave this to jury instructions.** Per CRS, the Clean Air Act and TSCA provide
that "in proving a defendant's possession of actual knowledge, circumstantial evidence may be used,
including evidence that the defendant took affirmative steps to be shielded from relevant
information," and RCRA carries near-identical language for its knowing-endangerment offense.

**Where this Act stands, and the answer is stranger than a gap.** The tagged text uses the doctrine
**once**, at SEC. 2(b), and uses it against the *smallest* actor it reaches: the reliance path that
lets a non-modifying deployer discharge its duty "is unavailable to a deployer that knows, or
**consciously avoids knowing**, of a material nonconformity in the adopted validation or in the
deployed configuration."

**So a downstream deployer forfeits its safe course for deliberate ignorance, and a controlling
person of the developer does not.** SEC. 6 says nothing about it. Whether that asymmetry was chosen
or inherited, it is the wrong way round on any reading, and it is what
[CURE 22](../audit/v3_5_cure_language.md) proposes to correct by writing the codified federal form
into SEC. 6(b). SEC. 9(b) already does the same work from a third direction: the reporting clock
runs from when an incident "would have been detected by the monitoring the entity certified it
maintains." **An Act that refuses to credit unmonitored ignorance at SEC. 9, and refuses to credit
deliberate ignorance at SEC. 2, should say which it does at SEC. 6.**

⚠ **Read-status.** Every case in these three entries is quoted from the Congressional Research
Service's *Enforcement of Federal Pollution Control Laws* or from Hustis and Gotanda,
25 Loy. U. Chi. L.J. 169 (1994) — **not from the reporters.** All are on the retrieval list and
none may be described as verified. E22 governs.

**Duty of oversight** — *the Caremark line.* The corporate-law doctrine nearest to what this Act
does, and the one a governance lawyer reaches for first. It asks whether those in charge built a
system to know. *In re Caremark*, 698 A.2d 959, 971 (Del. Ch. 1996): "Generally where a claim of
directorial liability for corporate loss is predicated upon **ignorance** of liability creating
activities within the corporation, as in *Graham* or in this case, **in my opinion** only a sustained
or systematic failure of the board to exercise oversight — such as an utter failure to attempt to
assure a reasonable information and reporting system exists — will establish the lack of good faith
that is a necessary condition to liability." ✅ **Read in the copy held, 26 Aug 2026, and 971 is
confirmed.** ⚠ **This entry used to begin the quotation at "only"**, dropping Chancellor Allen's own
"in my opinion" and the confinement to claims predicated on ignorance ([E68](../ledger/errata.md));
it is not a general standard for director oversight. *Marchand v. Barnhill*, 212 A.3d 805, 824 (Del. 2019) narrowed
the target to what matters most: "In Blue Bell's case, food safety was essential and **mission
critical**." And *In re McDonald's Corp. Stockholder Derivative Litigation*, C.A. No. 2021-0324-JTL (Del. Ch.
26 Jan. 2023) (Laster, V.C.) moved it off the board, at slip op. 2: **"This decision clarifies that
corporate officers owe a duty of oversight."** ✅

**Where this Act stands.** Two differences, and both cut in the same direction. Oversight liability
is *civil, fiduciary, and owed to the corporation*; this Act's duty is *criminal, statutory, and
owed to the public*. And oversight liability requires bad faith, while SEC. 6(a)'s floor is a
failure of due care. **So the Delaware line is not this Act in another suit. It is the nearest
neighbor, and the fact that a state's corporate law already asks whether an officer built a system
to know is the strongest evidence that the question this Act asks is a familiar one.**

**Business judgment rule** — the presumption that a fiduciary's considered decision will not be
second-guessed. The expected objection is that releasing a model is a business judgment. **Delaware
sets a floor under it, in its own words.** *In re Massey Energy Co. Derivative & Class Action
Litig.* (Del. Ch. 31 May 2011) (Strine, V.C.), slip op. 46: **"Delaware law does not charter law
breakers."** And on the same page: "Delaware law allows corporations to pursue diverse means to
make a profit, subject to a critical statutory floor, which is the requirement that Delaware
corporations only pursue 'lawful business' by 'lawful acts.'" ✅ *Both read in the opinion,
25 August 2026.*

**Exculpation, indemnification, and advancement** — the three ways a company pays for an officer's
defense, and the reason SEC. 7(b) exists. Delaware's exculpation provision, 8 Del. C.
§ 102(b)(7), reaches "monetary damages for **breach of fiduciary duty**" and expressly cannot reach
"acts or omissions not in good faith or which involve intentional misconduct or a knowing violation
of law." Its indemnification provision, § 145(a), covers criminal proceedings only where the person
"had no reasonable cause to believe the person's conduct was unlawful." And § 145(g)(1) contemplates
insurance that excludes "any . . . deliberate criminal or deliberate fraudulent act of such person,
or a knowing violation of law by such person, if . . . established by a final, nonappealable
adjudication."

**Where this Act stands.** SEC. 7(b)(1)–(2) bars insuring or reimbursing an individual penalty
outright. SEC. 7(b)(5) then does something narrower and more interesting: it **permits**
insurance and advancement for "reasonable costs of defense," provided the amounts "shall be
repaid by a person finally adjudicated to have committed a knowing or willful violation under
SEC. 6(b)."

That is Delaware's own structure. 8 Del. C. § 145(e) permits advancement "upon receipt of an
undertaking . . . to repay such amount if it shall ultimately be determined that such person is
not entitled to be indemnified," and § 145(g)(1) contemplates excluding cover for a "deliberate
criminal . . . act" once "established by a final, nonappealable adjudication." **Advance, then
claw back on an adverse final adjudication — the Act and the Delaware Code reach the same
mechanism.** **That is not a novel imposition on corporate practice. It is nearly
the line Delaware's own code already draws, in nearly the same words** — which is either the
strongest defense of the provision or the strongest argument that it is redundant, and the torts and
design seat is asked which.

⚠ **Read-status.** Every quotation in these three entries is taken from a retrieval reply, not from
the reporters or the Delaware Code. **They are unverified**, they are on the retrieval list, and
under E22 no outreach may describe them as checked until the primaries are read.

---

### The two columns — the same word in law and in the machine

**Half the terms in this debate carry two meanings: one in law, one in engineering.** They are not
synonyms that drifted apart; they are different concepts wearing one word. A drafter who lets the
engineering sense stand in for the legal sense has written a statute that answers the wrong question.
**Where the two columns below diverge, the divergence is the space the Act works in.**

*This is not a novel complaint. Desai & Riedl put it in a law-and-computer-science paper on exactly
this point: computer science and the law both use the word* agent*, "but computer science theory
lacks a full idea of agency," and treating the two as the same "could lead to a world where software
has legal personhood … [and] the ability to avoid responsibility" (Desai & Riedl, "Responsible AI
Agents," 2025). The table makes that observation portable.*

| Word | In **law** | In **the machine** | The gap the Act works in |
|---|---|---|---|
| **Accountability** | A party owes another a justification for a decision and faces a **consequence** if it is inadequate (Binns, 2018). A government drafts it identically: "answerable for outcomes, achievements and failures … [including] **ownership, responsibility and consequences**" (UK Government Cyber Action Plan, 2026, Glossary). | An attribute of an access-control pipeline — the traceability of a verified user ("verification, trust signals, and **accountability**," OpenAI, 2026). In practice, a **contact address** ("Measures for ensuring accountability" = an email, xAI DPA). | The legal sense names a **person** who answers, with a **sanction**. The industry sense names a **system property** with neither. The Act restores the person. |
| **Authority** | The **power to bind** the principal, limited to what was actually or impliedly conferred; acting beyond it is itself a wrong (Restatement (Third) of Agency § 2.02). | No native concept. The nearest analogue is a **permission** — what a token or credential technically allows. | "Capability isn't authority" (Akhtar, 2026); "does this action have explicit authority to execute?" (Bucko08, on the Hugging Face forensic post, 2026). A system can be **capable** of an act it was never **authorized** to take. Harm lives in that gap. |
| **Capability** | No settled term; the doctrinal analogue is the **"power to prevent"** the violation (*Park*, 1975). | What a model can do, measured by evaluation — deliberately, with **"safeguards disabled … to measure the capability boundary"** (ExploitGym, arXiv:2606.11086, 2026). | The **same** capability is safe or catastrophic depending on a human's deployment choice: one frontier model was **blocked 88.2 % of the time with safeguards on, and produced working exploits with them off**. The decision, not the capability, carries the duty. |
| **Safeguard / guardrail** | The analogue of the **duty of care** — liability turns on "whether reasonable mitigation steps were taken" (RAND, 2026). | Trained refusals, classifiers, sandboxing and monitoring that constrain a model — **and can be switched off** ("deliberately disabled OpenAI's production safety classifiers," Hugging Face, 2026). | Because a person can turn them off, their presence is not a defense and their **removal is an act with an author**. The Act reaches the act. |
| **Certification** | A **personal, signed attestation**, carrying liability for a knowing falsehood (cf. SOX § 906 / 18 U.S.C. § 1350). | A **cryptographic certificate** — an unrelated thing: a key, not a conscience. | A statute that asks for "certification" must mean the **signature of a person**, as the UK model already does — a named Accounting Officer holding "**personal accountability**," required to appoint an individual "**with authority**" (UK Cyber Action Plan, 2026). |
| **Misconfiguration** | No legal sense. Factually: a **human error or omission**. | The developers' own word for the July–August 2026 incidents — a setting that "gave it access to the internet" that "was not actually intended" (Meta; Anthropic, 2026). | An **agent-neutral word for a person's act.** It concedes, in the builders' own vocabulary, that a **configuration choice by a human** — not a model's volition — opened the door. |

**On the first row, because it is the project's own name in reverse.** This glossary can define every
technical term and still leave the central one — **accountability** — undefined, because the debate
rarely uses it in the legal sense at all. **That is the finding.** A regulator uses it and means a
person who answers ([OPC, PIPEDA report #2026-004](../research/press_corpus_july_august_2026.md)). A
developer uses it and means a mailbox. When the same word can name both a **duty with a consequence**
and an **email address**, the word has stopped doing legislative work — and the statute has to say
which one it means. **This one means the first.**

*Legal senses cite the Restatement (Third) of Agency and the authorities in
[the table of authorities](./table_of_authorities.md); the machine-side quotations are drawn,
graded, from the [press corpus](../research/press_corpus_july_august_2026.md) and the project's
source intake. ⚠ The developer and community quotations are recorded as public statements and are
not endorsements.*

---

### What these systems have genuinely done, stated fairly

**A glossary that only deflated the claims would be as dishonest as one that inflated them.**

The strongest well-evidenced case is **structure prediction in biology** — determining the
three-dimensional shape a protein folds into from its sequence, a problem that had resisted decades
of effort and now has usable predictions for very large numbers of proteins. That is real, it has
changed working practice in laboratories, and its authors received a Nobel Prize for it.

**Note what that example is, though.** A narrow, task-specific system, built by named scientists,
whose output is checked against physical reality by other scientists, published in the literature
and reproducible.

**It is not the thing this Act covers**, and it is not the thing one in five American adults is
asking about their symptoms. ⚠ *Details of the protein-folding work are stated from general
knowledge here and should be pinned to primary sources before any public use.*

---

### The lineage — because none of this is as new as it sounds

**Ada Lovelace, 1843**, on a machine that was never built:

> *"The Analytical Engine has no pretensions whatever to originate anything. It can do whatever we
> know how to order it to perform."*

Note the pronoun. ***We* order it.**

**ELIZA, 1966.** Joseph Weizenbaum's program at MIT reflected users' statements back as questions.
It understood nothing, and its author knew it. **People confided in it anyway, and kept doing so
after he told them how it worked.** The effect is named after it — the *ELIZA effect*, the human
tendency to attribute understanding to a system that produces plausible language.

**Sixty years on, the ELIZA effect is not a historical curiosity. It is the market.**

**RACTER, 1984**, published *The Policeman's Beard Is Half Constructed* — a book of computer-generated
prose sold as the machine's own work. ⚠ *How much was generated and how much was curated by its
authors is disputed, and the dispute is the point: the question "who actually wrote this?" is not
new either.*

**Margaret Masterman, 1955.** She founded the **Cambridge Language Research Unit**, which ran for
roughly twenty years on a staff never exceeding ten and did foundational work on machine
translation and computational linguistics. She had studied under Wittgenstein, and it shows in the
position she took: **that meaning could not be reached through syntax alone**, and that a thesaurus
— a map of how words relate — had to carry the semantic work.

Two of her observations have aged unusually well. That language processing must reckon with *"the
coherence of language, its redundancy as a signal"*, because writers *"go on saying the same thing
again and again in different ways"* — which is, in substance, the statistical regularity that makes
next-token prediction possible at all. And a **Wittgensteinian skepticism about whether any limited
sublanguage can capture the meaning of a whole language** — a caution from the 1960s about the
thing the 2020s is still arguing over.

⚠ *A claim that she produced computer-generated haiku circulates in secondary writing and could not
be verified from a reliable source; it is not asserted here.*

**Alison Knowles and James Tenney, 1967.** *A House of Dust* was generated on a **Siemens 4004**,
producing an edition of computer-written poems from iterations of a line structure with words drawn
from a fixed vocabulary. ⚠ *Sources disagree on the size of the edition — one and the same page gives
both 50 and 500 — and the programming language is not confirmed from a source this project has
opened. The stanza structure is described in secondary writing and is not reproduced here until a
primary source is read.*

**What is not in doubt is the byline.** The poem was made by a machine and credited to **two named
people.** Nobody in 1967 wrote that the Siemens 4004 had composed a poem, and nobody would have
understood the sentence if they had.

**That convention held for decades and then quietly stopped holding.** The authorship question is
not new; what is new is that the answer got harder to say out loud — which is the subject of
[house language](./house_language.md) and the reason this glossary exists.

*Sources: [Margaret Masterman](https://en.wikipedia.org/wiki/Margaret_Masterman);
[A House of Dust](https://eastofborneo.org/archives/a-house-of-dust-alison-knowles-and-james-tenney-1967/).
⚠ **R** — secondary sources, opened but not corroborated against primary material.*

---

### And back to the pun, because it is the whole thing

A **model** is a fitted object. An **act**, in the sense a statute uses the word, is something done
by a person who can be held to it.

Every enacted frontier statute in America regulates the first and never reaches the second. This
one is named for the gap between them.

**Whether a model acts in some other sense is a real question, and this project takes no position
on it.** It does not have to. **In the only sense a criminal statute can operate in, the acts belong
to people — and the question this project puts to a legislature is only: which ones?**

---

*Corrections to the project contact — especially from people who build these systems. They enter
[the errata register](../ledger/errata.md) with the fix attached and permanent credit.*

---

## Sources

Every authority cited in the statute (`model_act_v3_4.txt`) and the companion
(`model_act_v3_4_companion.md`), with the provision or note that cites it and the
proposition it is cited for. Built for verification: a reviewer should be able to check the
project's citations without reading the documents that contain them.

**Scope.** Statute and companion only. The drafting record (`audit/record.md`), the dossier,
and the standards notes carry hundreds of further sources with their own inline flags; those
are evidence apparatus, not the Act's authority base, and are not listed here.

**That exclusion was not a decision, and saying so is the point of this paragraph.** This table was
compiled on 20 August 2026. The files that cite the law below were written on the 21st. **Nobody
chose to leave them out; they did not exist yet**, and describing the omission as deliberate would
be a rationalization dressed as a policy. The decision is being taken **now**, in the open, and it
is this: Files in
`standards/` now cite a great deal of law directly — 18 U.S.C. §§ 4, 1001, 1030 and 1519,
21 U.S.C. §§ 331 and 333, Form FDA 1572, and a run of prosecutions in
[the same conduct](./the_same_conduct.md) — **and none of it appears below.** Those citations are
graded where they sit, under [the confidence
rubric](./frontier_bill_census.md#the-confidence-rubric-governed-by-e15), which marks whether the
primary was opened and by whom. Two different disciplines for two different jobs: this table is the
**authority base of the statute**, kept small enough to stay accurate; the standards files are
**evidence**, graded in place. An out-of-date table of authorities would be worse than none, so
this one is not allowed to grow past what it can verify. **Status.**
Compiled 20 August 2026 from the tagged v3.4 files. Pincites are given where the citing
document gives them; where it does not, the entry says so, and closing that column is the
remaining half of READ FIRST item 10 (the consolidated cite-check). Nothing here is a new
claim: every line restates a citation already published elsewhere in the repository.

**The three marks, and what each one promises.** They are read-statuses, not emphasis, and nothing
in a row uses them for anything else.

| Mark | Means |
|---|---|
| ✅ | **Read in the document by a person**, and whatever the row quotes was seen in the document. A pincite is confirmed only where the row says the copy carried real pagination ([E47](../ledger/errata.md)) |
| ⚠ | **Outstanding debt**: not held, or held and unread, or read with a pincite that cannot be settled from the copy held. `check_citations.py` counts these, and they are the standing debt figure |
| ◐ | **Model-mediated**: reached through a tool that downloaded a page and had a language model answer against it. The metadata is usable; **nothing marked ◐ may be published as a quotation.** New on 26 August 2026 — see [E57](../ledger/errata.md). A ◐ row always carries a ⚠ as well, because a lead is not a reading |

---

### I. Cases

#### The doctrine

| Authority | Cited at | For |
|---|---|---|
| *People v. Roscoe* (Cal.) · *People v. Matthews* (Mich.) · *People ex rel. Burris v. C.J.R. Processing*, 647 N.E.2d 1035 (Ill. App. Ct. 1995) | **new row 26 Aug 2026**; [for_legislators.md](./for_legislators.md) | ⚠ **None held, none read, all three known only through the Lyness survey — and they sit on the page a legislator is most likely to rely on.** Retrieval failed on all three, 26 Aug 2026: *Roscoe* on a bot challenge, *Burris* because the URL tried **returned HTTP 200 and a different case entirely** (*City of Chicago v. Telegraph Properties*, No. 1-02-2869 — the digits in the URL are that docket, not this one). ⚠ **A URL that answers is not a URL that answers correctly**, and this table records the state RCO line as ungraded until the reporters are opened |
| *United States v. Dotterweich*, 320 U.S. 277 (1943) | SEC. 6(a); n.2, n.6; lineage note | The responsible-relation standard — the officer answers for the public danger the operation creates |
| *United States v. Park*, 421 U.S. 658 (1975) | SEC. 0(b); n.6 (at 673–74); CURE 8 | ✅ **Read 25 Aug 2026.** At 673–74, the prima facie case: evidence that the defendant had "by reason of his position in the corporation, responsibility and authority either to prevent in the first instance, or promptly to correct, the violation complained of, and that he failed to do so." At 668, "standing in responsible relation to a public danger." **At 672–73, the burden structure this Act's SEC. 6(d) omits:** powerlessness is "raised defensively at a trial on the merits," the defendant "has the burden of coming forward with evidence," and this "does not alter the Government's ultimate burden of proving beyond a reasonable doubt... his power" |
| *United States v. DeCoster*, 828 F.3d 626 (8th Cir. 2016) | n.6 (concurrence at 637) | ✅ **Read 25 Aug 2026.** Murphy, Beam, Gruender, JJ. Gruender concurring: "Park requires a finding of negligence in order to convict a responsible corporate officer under § 331," and "I read Park to require a showing of negligence before exposing a responsible corporate officer to imprisonment for the acts of a subordinate." Beam dissenting: "There is no precedent that supports imprisonment without establishing some measure of a guilty mind" |
| *Morissette v. United States*, 342 U.S. 246 (1952) | SEC. 1(a); n.2 (at 256) | The public-welfare category, and the bargain: strict liability without imprisonment |

| *United States v. MacDonald & Watson Waste Oil Co.*, 933 F.2d 35 (1st Cir. 1991) | CURE 22; the glossary | ⚠ **Text read 25 Aug 2026 in the opinion; pincites still unverified.** Both sentences are verbatim in the opinion: "In a crime having knowledge as an express element, a mere showing of official responsibility under *Dotterweich* and *Park* is not an adequate substitute for direct or circumstantial proof of knowledge," and "The seminal cases regarding the responsible corporate officer doctrine are *United States v. Dotterweich*... and *United States v. Park*." **The pages 55 and 51 are carried from CRS and could not be confirmed: the source read carries no star pagination.** Footnote 15 is confirmed to be the willful-blindness footnote; **whether the court *approved* the instruction there is not confirmed** and the footnote text is still owed |
| *United States v. Iverson*, 162 F.3d 1015 (9th Cir. 1998) | CURE 22; known objections; SEC. 4 defense | ⚠ **Text read 25 Aug 2026 in the opinion; pincites unconfirmed (no star pagination, [E47]).** Verbatim: the RCO instruction "relieved the government only of having to prove that defendant personally discharged or caused the discharge of a pollutant. The government still had to prove that the discharges violated the law and that defendant knew that the discharges were pollutants." **The version published here until today read "violated the [CWA]" and "were pol[lutants]" — see E48.** The test: "a person is a 'responsible corporate officer' if the person has authority to exercise control over the corporation's activity that is causing the discharges," with no requirement of actual exercise or express vesting — **broader than SEC. 4(a)**. The approved instruction's three elements: knowledge of the fact; authority and capacity to prevent; failure to prevent. And the *Park* ratification paragraph, whose parenthetical records that Congress made the CWA a **felony** in 1987 |
| *United States v. Johnson & Towers, Inc.*, 741 F.2d 662 (3d Cir. 1984) | CURE 22 | ✅ **READ, 26 Aug 2026.** The rule is verbatim in the body of Part III.B: the district court "will be required to instruct the jury, inter alia, that in order to convict each defendant the jury must find that each knew that Johnson & Towers was required to have a permit, and knew that Johnson & Towers did not have a permit." Carried for the split, not for the proposition ⛔ **This row published half of it** ([E66](../ledger/errata.md)). The next sentence qualifies it — "Depending on the evidence, the district court may also instruct the jury that such knowledge may be inferred" — and Part IV holds all elements must be knowing "**but that such knowledge, including that of the permit requirement, may be inferred by the jury as to those individuals who hold the requisite responsible positions with the corporate defendant.**" The court's own gloss: its reading "does not impose on the government as difficult a burden as it fears" **And it is confined to the subsection, not stated generally** — "in light of our interpretation of section 6928(d)(2)(A)" — so "the Third Circuit's rule" on knowledge of a legal requirement, unqualified, is broader than the opinion ⚠ **669 still unconfirmed, for a new reason — this row's remaining debt.** Three copies are held: the law.resource.org and FindLaw captures carry **no star pagination**; the OpenJuris capture filed as `_second-copy` **does** carry it, and is a single page ending at `*664`. The only paginated copy stops five pages short ([E47](../ledger/errata.md)) |
| *United States v. Ahmad*, 101 F.3d 386 (5th Cir. 1996) | CURE 22; CURE 24; the criminal lane | ✅ **READ IN THE OPINION 26 Aug 2026** — law.resource.org reporter capture, held; ⚠ **no star pagination**, so nothing here may be pincited to a page ([E47](../ledger/errata.md)). **Three things the repository had wrong, all from relying on a secondary summary.** **(1) The holding is about mistake of fact.** Ahmad discharged "a large quantity of gasoline into the sewers of Conroe, Texas" from a leaking tank; the question was which elements "knowingly" attaches to, and the court's worry is that "one who honestly and reasonably believes he is discharging water may find himself guilty of a felony if the substance turns out to be something else." **(2) The felony point is a confirming reason, not the ratio.** The opinion reads: "The fact that violations of § 1319(c)(2)(A) are felonies punishable by years in federal prison **confirms our view** that they do not fall within the public welfare offense exception." This repository has been publishing it the other way round, as the reason for the conclusion. **(3) *Ahmad* does not think it is splitting with *Weitzenhoff*.** On the Ninth Circuit's case it says the court "was concerned almost exclusively with whether the language of the CWA creates a mistake-of-law defense. Both cases are easily distinguishable, for neither directly addresses mistake of fact or the statutory construction issues raised by Ahmad." **What is left of the objection**: a Fifth Circuit reading of *Staples* that *Weitzenhoff* at 1286 n.7 refuses. **What does not carry over to this Act**: SEC. 6(b)(1) requires knowledge, and there is no frontier-AI analogue of a person who honestly believes the substance is water. ⚠ *Ahmad* cites the Ninth Circuit case as *Weitzenhoff* (9th Cir. **1994**), the amended opinion's year; this table uses 1993, the original's |
| *United States v. Hanousek*, 176 F.3d 1116 (9th Cir. 1999); cert. denied, 528 U.S. 1102 (2000) | the glossary; SEC. 6(a); CURE 24 | ✅ **Read 26 Aug 2026 in the opinion, confirmed character-for-character on two independent sources and held in the working library.** **Holding:** "We conclude from the plain language of 33 U.S.C. § 1319(c)(1)(A) that Congress intended that a person who acts with **ordinary negligence** in violating 33 U.S.C. § 1321(b)(3) may be subject to criminal penalties." **Due process:** "It is well established that a public welfare statute may subject a person to criminal liability for his or her ordinary negligence without violating due process" (citing *Balint*). **And the sentence this repository most needed:** "The criminal provisions of the CWA constitute public welfare legislation" — twice, on *Weitzenhoff*. **That is the Ninth Circuit holding the opposite of *Ahmad*.** **Canon:** Congress wrote "gross negligence" into § 1321(b)(7)(D) and not into § 1319(c)(1)(A), and disparate inclusion is "presumed intentional". ✅ **Pincites CONFIRMED 26 Aug 2026 against the West reporter print** (pp. 1116–1126, held in the working library): the roadmaster description at **1119**; the holding, the gross-negligence canon, *Balint*, "public welfare legislation" and "without violating due process" all at **1121**; "section 1319(c)(1)(A) does not violate due process" and *Dotterweich* at **1122**; and a **second, differently worded statement of the holding in CONCLUSION at 1126** — "In light of the plain language… may be **subjected** to criminal penalties" — which anyone quoting must not conflate with the 1121 sentence |
| *United States v. Weitzenhoff*, 35 F.3d 1275 (9th Cir. 1993), as amended on denial of reh'g and reh'g en banc, 8 Aug. 1994 | **new 26 Aug 2026**; CURE 22; CURE 24; the criminal lane | ✅ **READ 26 Aug 2026 in the amended opinion, in a copy carrying continuous West star pagination 1279–1299**, held in the working library. **The sentence *Hanousek* rests on, at 1286:** "The criminal provisions of the CWA are clearly designed to protect the public at large from the potentially dire consequences of water pollution, see S.Rep. No. 99-50, 99th Cong., 1st Sess. 29 (1985), and as such fall within the category of public welfare legislation." **And the footnote that answers *Ahmad*, at 1286 n.7:** "While the *Staples* opinion expresses concern with this evolution of enhanced punishments for public welfare offenses, **it refrains from holding that public welfare offenses may not be punished as felonies**" — citing the Court's own reservation, "[w]e need not adopt such a definitive rule of construction to decide this case." **No U.S. Reports pincite is available from here:** the copy gives that cite as "511 U.S. at ----, 114 S.Ct. at 1804"; the U.S. Reports page had not issued when this was printed, so **there is no U.S. pincite to take from here**. The same footnote reports three public welfare offenses already punished as felonies: *International Minerals*, 402 U.S. 558 (ten years where death or bodily injury results); *United States v. Freed*, 401 U.S. 601, 609–10 (1971) (five years, unregistered grenade); *Hoflin*, 880 F.2d 1033 (9th Cir. 1989) (two years, RCRA). **The whole *Staples* passage, footnote 7 included, was added by the 8 Aug. 1994 amendment** — the original opinion at 1 F.3d 1523 predates *Staples*, so this is the Ninth Circuit answering *Staples* deliberately rather than in passing. **And the other half, which this Act must state itself.** Five judges dissented from the order rejecting rehearing en banc (KLEINFELD, J., with REINHARDT, KOZINSKI, TROTT and T.G. NELSON, JJ.), at 1293–1299: "We have now made felons of a large number of innocent people doing socially valuable work" (1293), and the chilling-effect objection in its original form — "If they knew they risk three years in prison, some might decide that their pay, though sufficient inducement for processing the public's wastes, is not enough to risk prison for doing their jobs" (1293). ***Ahmad* is that dissent, adopted two years later by another circuit.** **Correction carried:** this repository cited the public-welfare sentence to **1283**. 1283 is what *Hanousek* cites for its standard of review; the sentence is at **1286**. See [E51](../ledger/errata.md) |
| *Staples v. United States*, 511 U.S. 600 (1994) | n.6; CURE 22; CURE 24; the criminal lane | ✅ **READ IN THE PRIMARY 26 Aug 2026** — Library of Congress U.S. Reports print, 41 pp., **running-head pagination confirmed page by page**, held on the shelf. **Every pincite in this repository that touched it is now settled, and the leading case against this Act misread it.** **At 607** ✅: "Typically, our cases recognizing such offenses involve statutes that regulate potentially harmful or injurious items" — *Ahmad*'s cite is right. **At 618, and this is the whole finding, in one continuous passage:** "Close adherence to the early cases described above might suggest that punishing a violation as a felony is simply incompatible with the theory of the public welfare offense. In this view, **absent a clear statement from Congress that mens rea is not required, we should not apply the public welfare offense rationale to interpret any statute defining a felony offense as dispensing with mens rea. But see *United States v. Balint*, 258 U. S. 250 (1922).** **We need not adopt such a definitive rule of construction to decide this case, however.** Instead, we note only that where, as here, dispensing with mens rea would require the defendant to have knowledge only of **traditionally lawful conduct**, **a severe penalty is a further factor** tending to suggest that Congress did not intend to eliminate a mens rea requirement." ⛔ **The sentence *Ahmad* quotes as *Staples*'s rule is the antecedent of "such a definitive rule of construction" — the view the very next sentence declines to adopt.** See [E64](../ledger/errata.md). ✅ **And *Weitzenhoff*'s missing U.S. pincite is 618** — the reservation and the phrase *Ahmad* relies on are the same passage on the same page. **The Court supplies its own counter-authorities**: *Balint* in text, and at **617 n.14** *State v. Lindberg*, 125 Wash. 51 (1923), "applying the public welfare offense rationale to a felony." **The operative trigger is not the penalty**; it is "where, as here, dispensing with mens rea would require the defendant to have knowledge only of **traditionally lawful conduct**" |
| *United States v. Freed*, 401 U.S. 601 (1971) | **new row 26 Aug 2026**; CURE 24 | ⚠ **Known only as *Weitzenhoff* reports it** at 1286 n.7, citing 609–10: five years' imprisonment for possession of an unregistered grenade, offered as a public welfare offense punished as a felony. The cleanest single counterexample to *Ahmad*, and unread |
| *United States v. Balint*, 258 U.S. 250 (1922) | new 26 Aug 2026; the glossary; SEC. 6(a) | ✅ **READ IN THE PRIMARY 26 Aug 2026** — U.S. Reports, Library of Congress scan, pp. 250–254, **running-head pagination confirmed page by page**. **The pincite *Hanousek* gives (252–53) is exact, and the sentence straddles the break precisely there:** "Again where one deals with others and his mere negligence may be dangerous to them, as in selling diseased food or poison, the **[253]** policy of the law may, **in order to stimulate proper care, require the punishment of the negligent person though he be ignorant** of the noxious character of what he sells." **That is SEC. 6(a)'s architecture, stated in 1922**: punish the negligent person though ignorant, to stimulate proper care. Also at 252–54: the State may provide "that he who shall do them shall do them at his peril and will not be heard to plead in defense good faith or ignorance"; and the emphasis of such a statute "is evidently upon achievement of some social betterment rather than the punishment of the crimes as in cases of mala in se." **This project carried *Dotterweich* (1943) and *Park* (1975) for months without the 1922 case both rest on** |
| *United States v. Jewell*, 532 F.2d 697 (9th Cir. 1976) (en banc) | the glossary | ✅ **READ, 26 Aug 2026, and the quotation is verbatim.** "In the language of the instruction in this case, the government must prove, 'beyond a reasonable doubt, that if the defendant was not actually aware . . . his ignorance in that regard was solely and entirely a result of . . . a conscious purpose to avoid learning the truth.'" **The words are the trial court's instruction**, adopted by the en banc court — the glossary's "classic formulation" is right about whose standard it became, imprecise about whose sentence it is ([E73](../ledger/errata.md)) **Shared source worth knowing**: *Jewell* quotes Glanville Williams, "A court can properly find wilful blindness only where it can almost be said that the defendant actually knew" — the same line *Global-Tech* uses at 770 ⚠ **704 stays unconfirmed** — no star pagination ([E47](../ledger/errata.md)). Corroboration only, not a reading: *Cincotta* cites this discussion as "532 F.2d 697, **699–704**" |
| *United States v. Cincotta*, 689 F.2d 238 (1st Cir. 1982) | the glossary | ✅ **READ, 26 Aug 2026, and the quotation is verbatim.** "The conscious avoidance principle means only that specific knowledge may be inferred when a person knows other facts that would induce most people to acquire the specific knowledge in question." ✅ **"n.2" is confirmed** — the passage sits in the numbered note beginning "2", between the note quoting the indictment and note 3 ⛔ **The glossary offers this as a narrowing of *Jewell*, and the next sentence widens it** ([E73](../ledger/errata.md)): "Thus, if someone refuses to investigate an issue that cries out for investigation, **we may presume that he already 'knows' the answer** an investigation would reveal, whether or not he is 'certain'." The "only" limits what conscious avoidance **is** — circumstantial evidence of knowledge — not how far the inference reaches ⚠ **243 stays unconfirmed** — no star pagination ([E47](../ledger/errata.md)) |
| *Global-Tech Appliances, Inc. v. SEB S.A.*, 563 U.S. 754 (2011) | the glossary | ✅ **READ IN THE U.S. REPORTS PRINT, 26 Aug 2026, and 769 is confirmed from the copy.** The govinfo print carries real reporter pagination, so this row settles its own pincite. At **769**, the two-part test: "all appear to agree on two basic requirements: (1) The defendant must subjectively believe that there is a high probability that a fact exists and (2) the defendant must take deliberate actions to avoid learning of that fact" — requirements that "give willful blindness an appropriately limited scope that surpasses recklessness and negligence." At **770** the Court rejects the looser standard below: a "known risk" will not do, and "deliberate indifference" "does not require active efforts by an inducer to avoid knowing." ⛔ **This row previously called 769 "the constitutional ceiling" and that was wrong** ([E65](../ledger/errata.md)): *Global-Tech* is a **civil** patent case under 35 U.S.C. § 271(b), the passage is the Court's distillation of what the circuits already agreed on, and no constitutional question is presented or decided. The opinion's one constitutional touch is at **767** and concerns due-process limits on **statutory presumptions** of knowledge (*Turner*, *Leary*) — a different doctrine. **And the doctrine runs criminal-to-civil**: "well established in criminal law" (766), extended because "we can see no reason why the doctrine should not apply in civil lawsuits" (768). Nothing limits it in criminal cases; the authority this Act cites for a **criminal** knowledge element is a civil case describing criminal practice. **No debt outstanding: read in the reporter print, pincite settled** |
| *United States v. Bank of New England, N.A.*, 821 F.2d 844 (1st Cir. **1987**) | the glossary; known objections | ✅ **READ, 26 Aug 2026.** Collective knowledge, in the First Circuit's own words: "A collective knowledge instruction is entirely appropriate in the context of corporate criminal liability. . . . Corporations compartmentalize knowledge, subdividing the elements of specific duties and operations into smaller components. The aggregate of those components constitutes the corporation's knowledge of a particular operation." The approved instruction, quoted in the opinion: "if Employee A knows one facet of the currency reporting requirement, B knows another facet of it, and C a third facet of it, the bank knows them all." Upheld as "not only proper but necessary" for a bank with "the compartmentalized structure common to all large corporations" ⛔ **This row previously dated the case 1984 and gave the "cannot plead innocence" sentence as this court's holding. Both were wrong** ([E67](../ledger/errata.md)): argued 4 Mar. and decided **10 June 1987**, and that sentence is a block quotation from ***United States v. T.I.M.E.-D.C., Inc.*, 381 F. Supp. 730, 738 (S.D. W. Va. 1974)**, quoted with approval — a district court's words published here as a court of appeals'. **The doctrine is corporate-only**: knowledge "is imputed to the corporation" and no authority in its string aggregates onto a natural person, so it does not compete with SEC. 4 and the Act "declines" nothing it could have had **A second approved theory this repository had never carried**: organizational willful blindness — whether the entity "consciously avoided learning about and observing" its duties, provable by "flagrant organizational indifference" ⚠ **no star pagination, so 856 stays the secondary source's — this row's remaining debt** ([E47](../ledger/errata.md)) |
| *United States v. Philip Morris USA Inc.*, 566 F.3d 1095 (D.C. Cir. 2009) | the glossary | ⚠ At 1118: corporate intent "depends on the wrongful intent of specific employees" — the *respondeat superior* premise this Act builds on ⚠ **NOT HELD. Retrieval attempted and deliberately abandoned 26 Aug 2026.** law.resource.org's public-domain reporter scans stop before volume 566 and CourtListener's pages are behind a bot challenge. **The only PDF located was a LexisNexis printout carrying a third party's account name and session job number**, which is not a thing this project files into a research library. ✅ **HELD AND READ IN THE DOCUMENT 26 Aug 2026** — a FindLaw capture of the full opinion, 69 pp., now on the shelf. **The passage the glossary wants, verbatim:** "Corporations may be held liable for specific intent offenses based on the 'knowledge and intent' of their employees. *N.Y. Cent. & Hudson River R.R. Co. v. United States*, 212 U.S. 481, 495 (1909); see *United States v. A & P Trucking Co.*, 358 U.S. 121, 125 (1958). Because a corporation only acts and wills by virtue of its employees, the proscribed corporate intent depends on the wrongful intent of specific employees." **If that survives reading it is a better authority than the one the glossary carries, because it names the mechanism — corporate intent derived from identified employees — which is the exact inverse of what SEC. 4 does.** Held under a `MODEL-MEDIATED-FETCH` label ([E57](../ledger/errata.md)). ⚠ **No star pagination on that route, so 1118 stays unconfirmed**, and the fetch did not confirm the docket, the date, or the 566 F.3d citation — **a second D.C. Circuit *Philip Morris* opinion exists from 2012**. ✅ **All three settled 26 Aug 2026, and the citation this table publishes is right.** The Solicitor General's own petition states: "The opinions of the court of appeals … are reported at **566 F.3d 1095** and 396 F.3d 1190." Appeal **Nos. 06-5267, 06-5268**, argued and **decided 22 May 2009**. ✅ **And the D.C. Circuit's own opinion PDF is located at last** — `cadc.uscourts.gov/internet/opinions.nsf/…/06-5267-1181914.pdf` — so the clean print this row has been asking for is one download away and the LexisNexis printout stays refused. ⚠ **Near miss recorded:** a public-health litigation tracker carries this case at **556** F.3d 1095 in its page title and its URL, and that nearly produced a "correction" to a correct citation. See [E58](../ledger/errata.md) |
| 33 U.S.C. § 1319(c)(6) | E42; the glossary; SEC. 4 | ✅ **Read 25 Aug 2026, verbatim**: "For the purpose of this subsection, the term 'person' **means**, in addition to the definition contained in section 1362(5) of this title, **any responsible corporate officer**." Governs the whole of subsection (c), so it governs the negligence tier at (c)(1) |

*⚠ **Every authority in this block is quoted from a secondary source** — the Congressional Research
Service's* Enforcement of Federal Pollution Control Laws*, Lyness, 64 B.C. L. Rev. 253, or Hustis
and Gotanda, 25 Loy. U. Chi. L.J. 169 — **and none has been read in the reporter.** They are on the
retrieval list. Under E22 none may be described as verified, and no outreach may cite them as
settled.*

#### Culpability and elements

| Authority | Cited at | For |
|---|---|---|
| *Staples v. United States*, 511 U.S. 600 (1994) | n.6 | The modern presumption of scienter where penalties are severe. **Read-status and the felony question live on the criminal-lane row above**; this row records n.6's use only |
| *Rehaif v. United States*, 588 U.S. 225 (2019) | n.6 | Same line; express-scienter construction honored where it belongs |
| *Ruan v. United States*, 597 U.S. 450 (2022) | n.6 | Same line; SEC. 6(b)(1) states its mental element expressly |
| *Burrage v. United States*, 571 U.S. 204 (2014) | SEC. 10(c)(2)(D), in text; n.21 | The meaning of but-for cause in a results-enhanced offense |
| *Apprendi v. New Jersey*, 530 U.S. 466 (2000) | n.21, n.22 | Facts raising the ceiling are jury elements |
| *Alleyne v. United States*, 570 U.S. 99 (2013) | n.21, n.22 | Facts raising the floor are jury elements |
| *Almendarez-Torres v. United States*, 523 U.S. 224 (1998) | n.22 | The bare fact of a prior conviction may be judge-found |
| *Erlinger v. United States*, 602 U.S. 821 (2024) | n.22 | Anything beyond that bare fact goes to the jury — SEC. 6(b)(2) is drafted inside the exception |
| *Sandstrom v. Montana*, 442 U.S. 510 (1979) | n.4, n.18 | Presumptions: mandatory civilly, permissive inference criminally |
| *United States v. Van Buren*, 593 U.S. 374 (2021) | n.5 | Gates-up-or-down access construction; permission, not technical enforcement, defines the gate |

| *In re Caremark Int'l Inc. Derivative Litig.*, 698 A.2d 959 (Del. Ch. 1996) | the glossary; known objections | ✅ **READ, 26 Aug 2026, AND 971 IS CONFIRMED FROM THE COPY HELD.** The reprint carries star pagination `*960`–`*972` and the passage falls between `*971` and `*972`; the row's open question is answered yes ([E68](../ledger/errata.md)). The oversight standard, verbatim and whole: "Generally where a claim of directorial liability for corporate loss is predicated upon **ignorance** of liability creating activities within the corporation, as in *Graham* or in this case, **in my opinion** only a sustained or systematic failure of the board to exercise oversight—such as an utter failure to attempt to assure a reasonable information and reporting system exists—will establish the lack of good faith that is a necessary condition to liability." **The published form drops "in my opinion" without an ellipsis** (E48) and drops the confinement to claims predicated on **ignorance** — it is not a general oversight standard **And at the same page the court reserves the case this Act is about**: "this case presents no occasion to apply a principle to the effect that **knowingly causing the corporation to violate a criminal statute** constitutes a breach of a director's fiduciary duty," citing *Roth v. Robertson* and *Miller v. American Tel. & Tel. Co.* The *Caremark* bar was set for ignorance and expressly not for knowing violation, which is what SEC. 6(b) reaches **Provenance limit stands and is narrower than it was read as being**: a Thomson Reuters/Westlaw reprint with KeyCite headers, hosted by Penn Carey Law, **not an official court print** — a limit on whose text this is, not on whether pages are marked. **No debt outstanding: read, pincite settled** |
| *Stone v. Ritter*, 911 A.2d 362 (Del. 2006) | the glossary; known objections | ✅ **Read 25 Aug 2026.** Slip op. 17, the conditions predicate for director oversight liability, and "known duty to act... conscious disregard"; slip op. 15, when a failure to act in good faith may be shown |
| *Marchand v. Barnhill* (Del. 18 June 2019) (Strine, C.J.) | known objections; the glossary | ✅ **Read 25 Aug 2026.** Slip op. 31, "the board must make a good faith effort — i.e., try — to put in place a reasonable **board-level** system of monitoring and reporting"; slip op. 36, "food safety was essential and mission critical"; slip op. 32, the three things that did not exist |
| *In re McDonald's Corp. S'holder Derivative Litig.*, C.A. No. 2021-0324-JTL (Del. Ch. 26 Jan. 2023) (Laster, V.C.) | known objections; the glossary | ✅ **Read 25 Aug 2026.** Slip op. 2: "This decision **clarifies** that corporate officers owe a duty of oversight" — the extension from directors to officers, and the move this Act makes independently |
| *In re Massey Energy Co. Derivative & Class Action Litig.* (Del. Ch. 31 May 2011) (Strine, V.C.) | known objections; the glossary | ✅ **Read 25 Aug 2026.** Slip op. 46: "Delaware law does not charter law breakers," and the statutory floor — Delaware corporations may pursue only "lawful business" by "lawful acts." **This is the whole of the surviving business-judgment answer; see [E46](../ledger/errata.md#e46)** |
| 8 Del. C. § 102(b)(7) | the glossary; known objections | ✅ **Read in the Code, 25 Aug 2026.** Exculpation reaches "monetary damages for breach of fiduciary duty as a director or officer" **only**, and cannot reach "(ii) ... acts or omissions not in good faith or which involve intentional misconduct or a knowing violation of law," nor "(v) An officer in any action by or in the right of the corporation." **On its face it cannot touch a duty imposed by a statute outside the DGCL, still less a criminal one** |
| 8 Del. C. § 145(a), (e), (g) | the glossary; known objections | ✅ **Read in the Code, 25 Aug 2026.** (a) indemnification in a criminal proceeding only where the person "had no reasonable cause to believe the person's conduct was unlawful"; (e) advancement "upon receipt of an undertaking... to repay such amount if it shall ultimately be determined that such person is not entitled to be indemnified"; (g) insurance may "exclude from coverage... any deliberate criminal or deliberate fraudulent act... established by a final, nonappealable adjudication." **§ 145(e) and SEC. 7(b)(5) are the same mechanism** |
| *X.AI LLC v. Bonta*, No. 2:25-cv-12295 (C.D. Cal.), on appeal No. 26-1591 (9th Cir.) | known objections; the standing watch | ✅ **Complaint and Ninth Circuit docket read 25 Aug 2026**, both held in the working library. Four counts: per se takings, regulatory takings, compelled speech, vagueness — **the ordering is the finding** |
| *Ruckelshaus v. Monsanto Co.*, 467 U.S. 986 (1984) | known objections; the takings lane | ✅ **READ IN THE OPINION 26 Aug 2026 and ✅ PINCITE NOW CONFIRMED** against the Library of Congress U.S. Reports scan (39 pp., running-head pagination page by page), which supersedes the WIPO Lex copy that carried none. **The holding sentence runs 1003–04 exactly as this project cited it, and it is narrower than the sentence we published:** "We therefore hold that to the extent that Monsanto has an interest in its health, safety, and environmental data cognizable as a trade-secret property right **under Missouri law**, that property right is protected by the Taking Clause of the Fifth Amendment." **The shorter formulation this table quoted** — "a trade secret is property protected by the Fifth Amendment Taking Clause" — is verbatim but is the Court **describing** its holding in **footnote 9 at 1004**, not the holding sentence. **Why the qualification is the useful half:** the property right is the State's creation, so a State that does not create it does not take it, and the takings answer for a state statute is stronger than the footnote alone suggests |
| *Cedar Point Nursery v. Hassid*, 594 U.S. 139 (2021) | known objections | ✅ **READ, 26 Aug 2026.** The per se limb in the Court's own words: "The essential question is not . . . whether the government action at issue comes garbed as a regulation (or statute, or ordinance, or miscellaneous decree). It is whether the government has **physically taken property** for itself or someone else—by whatever means—or has instead **restricted a property owner's ability to use his own property**. . . . Whenever a regulation results in a physical appropriation of property, a per se taking has occurred, and *Penn Central* has no place." ⛔ **The "sine qua non" this row was cited for is not the Court's phrase** ([E70](../ledger/errata.md)). It appears once, in a *see also* parenthetical reporting what an article "call[s]" the right to exclude: *see also* Merrill, *Property and the Right to Exclude*, 77 Neb. L. Rev. 730 (1998). The Court's own formulations in that paragraph are quoted from ***Kaiser Aetna v. United States*, 444 U.S. 164, 176, 179–180 (1979)** — "a fundamental element of the property right", "one of the most essential sticks in the bundle" — and that is where the pincite for this proposition belongs **The words "trade secret" and "intangible" do not appear in the opinion, and neither does *Ruckelshaus***. The case concerns a right to "physically enter and occupy the growers' land"; extending it to compelled production of records is an argument no authority in this row supplies ⚠ **150 cannot be settled and stays the plaintiff's brief's.** Two copies held: the supremecourt.gov slip opinion carries slip pages, and the copy filed as `594-US-139_2021_Justia` carries no internal reporter pagination at all — its reporter citation lives in the filename and URL, which is a label ([E58](../ledger/errata.md)), not pagination |

#### Live enforcement and litigation — rows opened 26 August 2026

*Every caption here was cited in the repository's prose with no row, and therefore no read-status,
until today. Two of the four are the same case under two names, which is why the checker counted
four.*

| Authority | Cited at | For |
|---|---|---|
| *Attorney General of the State of Florida v. OpenAI Global, LLC* — also cited in this repository as *Florida v. OpenAI and Samuel Altman* | **new row 26 Aug 2026**; the enforcement record | ✅ **The filed-stamped complaint is held from 26 Aug 2026, 83 pp., from the Attorney General's own site. Unread.** Circuit Court of the Tenth Judicial Circuit, Highlands County, against the OpenAI entities **and Sam Altman personally**. ⚠ **Two captions for one case.** Whoever reads it should settle which is the caption and make the repository use one |
| *United States of America & X.AI LLC v. Philip J. Weiser* — also cited in this repository as *xAI v. Weiser* | **new row 26 Aug 2026**; the enforcement record; the takings lane | ⚠ **Unread; a docket metadata stub is held, not the complaint.** No. 1:26-cv-01515, **D. Colo.**, filed 9 Apr. 2026, confirmed against the CourtListener RECAP index 26 Aug 2026. **This is the case whose takings count the repository has been reading *Ruckelshaus* and *Cedar Point* through** — see those rows, both of which are now read or held in the primary instead |
| *Sementilli v. Trinidad Corp.*, 162 F.3d 1015 (9th Cir. 1998) | **new row 26 Aug 2026**; cited nowhere, rowed as a warning | ⛔ **NOT AN AUTHORITY OF THIS PROJECT AND MUST NEVER BE CITED AS ONE.** It shares the citation 162 F.3d 1015 with *United States v. Iverson*, and it is the case a search for that citation returns first. A retrieval on 26 Aug 2026 caught it one step before filing. **This row exists so the next reader finds the warning before the trap** — the same reason `WRONG-IVERSON-NOT-OUR-CASE` and `NOT-XAI-COUNSEL` are written into filenames on the shelf |
| *Ontario Provincial Council of Carpenters' Pension Trust Fund v. Walton*, 294 A.3d 65 (**Del. Ch.** 2023), C.A. No. 2021-0827-JTL | governance; known objections | ✅ **BOTH OPINIONS NOW HELD AND READ, 26 Aug 2026 — and this row's previous warning was wrong.** C.A. 2021-0827-JTL produced **two opinions two weeks apart**: a **laches** opinion of 12 April 2023 (64 pp.) and a **demand-futility memorandum opinion** of 26 April 2023 (123 pp.), both on the shelf, both from the Delaware courts' own service or a mirror of it, Laster V.C. ⛔ **[E46](../ledger/errata.md)'s finding that this case carried two fabricated quotations is WITHDRAWN** ([E60](../ledger/errata.md)). Both are verbatim in the **26 April** opinion, which E46 never opened: at **slip op. 76**, "When directors make a business decision that carries legal risk, but which otherwise involves legally compliant conduct, then the business judgment rule protects that decision"; and across **slip op. 77–78**, "the decision to pursue the project would constitute a conscious decision to violate the law, the business judgment rule would not apply, and the directors would be acting in bad faith." **A correct quotation was deleted from a public page on the strength of a check run against the wrong document.** ⚠ **Pincites 90 and 92 remain unconfirmed**: both copies carry **slip pages, not Atlantic Reporter pages**, and slip-to-reporter offsets are not computable ([E47](../ledger/errata.md)). **And the laches opinion is a separate document with separate content** — its slip op. 2 describes the Massey Claim, and nothing from one opinion may be cited to the other ⚠ **Which of the two is reported at 294 A.3d 65 is still unsettled, and the shelf cannot settle it** ([E71](../ledger/errata.md)): **neither slip opinion carries an Atlantic Reporter stamp**, which is ordinary for a slip. ⛔ **The one source that answered the question is withdrawn** — a ◐ model-mediated row in `research/verification_record.md` gave "58 pp., reported 294 A.3d 65" for the 26 April opinion, and that opinion runs to **slip page 121**; E59 had already caught fetches of this family reporting 56 or 58 pages for a 64-page document. **A retrieval wrong on the page count is not authority for the citation it supplied in the same breath** **The court supplies the short form this repository needs**: at slip op. 70 of the later opinion, Laster V.C. cites the earlier as ***Walmart Laches***, 2023 WL 2904946 (Del. Ch. Apr. 12, 2023) — adopt *Walmart Laches* and *Walmart Demand Futility* and the E59 collision cannot recur **Counting note for pincites**: each PDF carries two unnumbered front pages, so the **numbered** slip pages run to 62 and 121 within documents of 64 and 123 pages; "slip op. 76" is the numbered page |

#### Penalties and proportionality

| Authority | Cited at | For |
|---|---|---|
| *Rummel v. Estelle*, 445 U.S. 263 (1980) | **new row 26 Aug 2026** — cited in the repository's prose and never graded until now; the proportionality lane | ✅ **Held in the working library from 26 Aug 2026, unread.** Library of Congress U.S. Reports scan, **so it can settle its own pincites when read**. Carried for the deferential end of the proportionality line, against which SEC. 10(c)(3)'s valve is measured |
| *Soto v. Bushmaster Firearms Int'l*, 331 Conn. 53 (2019) | **new row 26 Aug 2026** — cited in the repository's prose and never graded until now | ⚠ **NOT HELD.** Retrieval failed 26 Aug 2026: CourtListener's HTML is behind a bot challenge and jud.ct.gov refused the connection. Cited in prose with no source on the shelf |
| *Timbs v. Indiana*, 586 U.S. 146 (2019) | n.19, n.21 | The Excessive Fines Clause binds the states |
| *United States v. Bajakajian*, 524 U.S. 321 (1998) | n.19, n.21 | Gross-disproportionality test |
| *Harmelin v. Michigan*, 501 U.S. 957 (1991) (Kennedy, J., concurring, at 1001) | n.21 | Federal noncapital review forbids only grossly disproportionate extremes |
| *Hutto v. Davis*, 454 U.S. 370 (1982) (per curiam) | n.21 | Forty years for nine ounces upheld — successful challenges "exceedingly rare" |
| *Ewing v. California*, 538 U.S. 11 (2003) | n.21 | Recidivist 25-to-life upheld |
| *Lockyer v. Andrade*, 538 U.S. 63 (2003) | n.21 | Consecutive recidivist terms upheld |
| *Solem v. Helm*, 463 U.S. 277 (1983) | n.21 | The lone modern reversal |
| *Pearson v. Ramos*, 237 F.3d 881 (7th Cir. 2001) (at 885–86) | n.21 | The federal unit of review is the count, not the aggregate |
| *O'Neil v. Vermont*, 144 U.S. 323 (1892) (Field, J., dissenting, at 340) | n.21 | The per-count machine at scale — the cautionary precedent |
| *Kokesh v. SEC*, 581 U.S. 455 (2017) | n.18 | Disgorgement is a penalty for limitations purposes |
| *SEC v. Jensen*, 835 F.3d 1100 (9th Cir. 2016) (No. 14-55221) | n.18, the no-fault clawback | ✅ **READ, 26 Aug 2026, and n.18's "no-fault" characterization is confirmed against the opinion.** The holding: "we hold that SOX 304 allows the SEC to seek disgorgement from CEOs and CFOs **even if the triggering restatement did not result from misconduct on the part of those officers**." Textual: "as a result of misconduct" modifies "the material noncompliance of **the issuer**", so "it is the issuer's misconduct that matters, and not the personal misconduct of the CEO or CFO" — and Congress "knew how to draft a statute that would limit the disgorgement remedy to cases of officer or director misconduct, and chose not to do so." First in the courts of appeals, in its own words: "we are aware of no circuit court that has addressed this issue" ⛔ **This row said "district courts had split for fourteen years" and the opinion describes no split** ([E72](../ledger/errata.md)). It says "**most** district courts to have examined it have concluded" against a personal-misconduct requirement and cites four going one way — *Jenkins*, *Baker*, *Geswein*, *Life Partners Holdings* — with no contrary decision anywhere in the discussion. "Split" was the law firm's word **Disambiguation, and it held up:** not the *Jensen* at n.22, which is the DOJ food-safety prosecution in D. Colo. Two cases, one surname, opposite subjects ⚠ **No F.3d pagination.** The Ninth Circuit's own PDF carries that issue's slip pages only, so 1100 and any pincite stay the secondary source's ([E47](../ledger/errata.md)) |
| *Liu v. SEC*, 591 U.S. 71 (2020) | n.18 | ✅ **READ, 26 Aug 2026, and n.18's account of it is exact.** "The Court holds today that a disgorgement award that does not exceed a wrongdoer's net profits and is awarded for victims is **equitable relief** permissible under §78u(d)(5)," the limit existing "to avoid transforming an equitable remedy into a punitive sanction" **Open question this reading raises against n.18** ([E74](../ledger/errata.md)): n.18's next clause, "a statutory clawback is not so confined", is offered without authority, and *Liu*'s ceiling attaches to relief that is **equitable** — which is what the Ninth Circuit calls SOX 304's reimbursement provision, "an equitable and not a legal remedy", *SEC v. Jensen*, citing *Jasper*, 678 F.3d 1116, 1130. The two authorities n.18 cites in one breath pull against each other. SEC. 7 reaches *Liu*'s destination anyway, so the design is unaffected and the reasoning is ⚠ **Slip opinion: "Cite as: 591 U. S. \_\_\_\_ (2020)"**, so no U.S. Reports pincite can be taken from it ([E47](../ledger/errata.md)) |
| *Friedman v. Sebelius*, 686 F.3d 813 (D.C. Cir. 2012) | n.10, n.22 | Exclusion after Park-doctrine convictions: power upheld, duration remanded |

#### Preemption and federalism

| Authority | Cited at | For |
|---|---|---|
| *South Dakota v. Dole*, 483 U.S. 203 (1987) | **new row 26 Aug 2026** — cited in the repository's prose and never graded until now; the federalism lane | ✅ **Held in the working library from 26 Aug 2026, unread.** Library of Congress U.S. Reports scan, **which can settle its own pincites** |
| *Pennhurst State School & Hospital v. Halderman*, 451 U.S. 1 (1981) | **new row 26 Aug 2026** — cited in the repository's prose and never graded until now; the federalism lane | ✅ **Held in the working library from 26 Aug 2026, unread.** Library of Congress U.S. Reports scan |
| *National Pork Producers Council v. Ross*, 598 U.S. 356 (2023) | n.17; extraterritoriality | ✅ **READ, 26 Aug 2026.** "A close look at those cases reveals **nothing like** the 'almost per se' rule against laws that have the 'practical effect' of 'controlling' extraterritorial commerce that petitioners posit . . . . *Baldwin*, *Brown-Forman*, and *Healy* **did not mean to do so much**." ⛔ **n.17 says the case "removed" that rule, and the Court says it never existed** ([E75](../ledger/errata.md)) — the rule is attributed throughout to petitioners ("Petitioners insist . . ."), and the Court declines to find it in the line. **Declining to recognize a rule leaves less to restore than abolishing one, so n.17 understated its own authority.** The rest of n.17 holds: the line is re-read as being about discrimination — laws that "hoard" commerce "for the benefit of in-state merchants" — and what remains is *Pike* ⚠ **Slip opinion: "Cite as: 598 U. S. \_\_\_\_"**, so no U.S. Reports pincite from this copy |
| *Kentucky v. Dennison*, 65 U.S. (24 How.) 66 (Dec. Term 1860) | `audit/record.md`; extradition scope | ✅ **READ in the Library of Congress U.S. Reports scan, 26 Aug 2026, and the quotation is verbatim**: "The word 'crime' of itself includes every offence, from the highest to the lowest in the grade of offences, and includes what are called 'misdemeanors,' as well as treason and felony." ✅ **The overruling is correctly confined and the syllabus separates the holdings the same way**: point 4 gives the scope of "treason, felony, or other crime"; points 8 and 9 are the mandamus holding — "Congress cannot coerce a State officer, as such, to perform any duty" and "upon that ground only, this motion for a mandamus was overruled". **It is 8 and 9 that *Puerto Rico v. Branstad*, 483 U.S. 219 (1987) overruled; the scope holding stands**, which is what the Act relies on **Reader's note on this copy**: the scan is genuinely paginated but its page numbers are OCR-damaged and irregular — markers jump 97 to 105 — so no page was computed and none is published ([E47](../ledger/errata.md)). Nothing turns on it; the citing file gives no pincite |
| *Monsanto Co. v. Durnell*, 609 U.S. ___, No. 24-1068 (2026) | n.13 | Express clauses read textually; presumption not invoked; *Bates* confined |
| *Bates v. Dow Agrosciences LLC*, 544 U.S. 431 (2005) | n.13 | Confined by *Durnell* to efficacy claims |
| *Kansas v. Garcia*, 589 U.S. 191 (2020) | n.14 | Criminal enforcement remains primarily a state responsibility; overlap is not conflict |
| *Chamber of Commerce v. Whiting*, 563 U.S. 582 (2011) | n.14 | Savings-clause construction |
| *Arizona v. United States*, 567 U.S. 387 (2012) | n.14 | The honest counterweight — state criminal law is not immune |
| *Wyeth v. Levine*, 555 U.S. 555 (2009) | n.14 | Presumption survives for implied preemption |
| *Puerto Rico v. Franklin Cal. Tax-Free Trust*, 579 U.S. 115 (2016) | n.14 | Not for express clauses, in most circuits |
| *Virginia Uranium, Inc. v. Warren*, 587 U.S. 761 (2019) (plurality) | n.14 | Preemptive purpose from text and structure — cited as persuasive, never as holding |
| *Medtronic, Inc. v. Lohr*, 518 U.S. 470 (1996) (plurality, at 488) | n.14 | Quoted within *Virginia Uranium* |
| *Murphy v. NCAA*, 584 U.S. 453 (2018) | n.15 | Congress may not command a State not to legislate — answers a bare moratorium only |
| *Alaska Airlines, Inc. v. Brock*, 480 U.S. 678 (1987) (at 684) | n.15 | Severability turns on whether the remainder is fully operative |

#### Speech, notice, and compelled disclosure

| Authority | Cited at | For |
|---|---|---|
| *Lambert v. California*, 355 U.S. 225 (1957) | **new row 26 Aug 2026**; [known objections](../docs/known_objections.md) | ⚠ **NOT HELD, NOT READ.** Cited against this Act: fair notice, and the limit on punishing a wholly passive failure to act where the actor had no reason to know a duty existed. **The vagueness objection is the one that most often kills a bill in committee and this project has never opened its leading case** |
| *Johnson v. United States*, 576 U.S. 591 (2015) | **new row 26 Aug 2026**; [known objections](../docs/known_objections.md) | ⚠ **NOT HELD, NOT READ.** The modern vagueness line: a criminal standard that leaves grave uncertainty about how to estimate the risk posed by conduct is void. Cited against a duty framed as "reasonable safeguards" where the penalty is prison |
| *Bernstein v. U.S. Dep't of Justice*, 176 F.3d 1132 (9th Cir. 1999) | **new row 26 Aug 2026**; [known objections](../docs/known_objections.md) | ⚠ **NOT HELD, NOT READ, and the citation itself is unverified** — recorded as the case the First Amendment objection names, source code as protected expression, left half-open on rehearing en banc. **Nothing in this repository has checked the reporter citation, the posture, or whether it survives**; it is a retrieval lead and not an authority |
| *Sveen v. Melin*, 584 U.S. 811 (2018) (No. 16-1432) | `audit/record.md`; the Contract Clause | ✅ **READ, 26 Aug 2026.** The two-step test, verbatim: the threshold is whether the state law has "operated as a substantial impairment of a contractual relationship"; "[i]f such factors show a substantial impairment, the inquiry turns to whether the state law is" drawn appropriately ✅ **811 is confirmed, and not from this copy** — `audit/record.md` records it against the preliminary print, "Volume 584 U.S. Part 2, Pages 811–836". This row's warning that no U.S. Reports pincite was available was true of the copy and false of the repository ([E49](../ledger/errata.md), [E75](../ledger/errata.md)) ⚠ **Slip opinion: "Cite as: 584 U. S. \_\_\_\_"**, so no *internal* pincite may be taken from it |
| *Energy Reserves Group v. Kansas Power & Light Co.*, 459 U.S. 400 (1983) | **new row 26 Aug 2026** — cited in the repository's prose and never graded until now; the Contracts Clause | ✅ **Held in the working library from 26 Aug 2026, unread.** Library of Congress U.S. Reports scan |
| *Connecticut v. Doehr*, 501 U.S. 1 (1991) | **new row 26 Aug 2026** — cited in the repository's prose and never graded until now; pre-deprivation process | ✅ **Held in the working library from 26 Aug 2026, unread.** Library of Congress U.S. Reports scan |
| *Veeck v. Southern Building Code Congress Int'l*, 293 F.3d 791 (5th Cir. 2002) (en banc) | `docs/questions.md`; the free-to-read rule | ✅ **READ, 26 Aug 2026**, and `docs/questions.md` states it accurately. The court's own summary: "as law, the model codes enter the public domain and are not subject to the copyright holder's exclusive prerogatives. **As model codes, however, the organization's works retain their protected status.**" ⛔ **This row was cited-for "why this Act is CC0", and the second half of that sentence is about this Act** ([E75](../ledger/errata.md)): *Veeck* is two-sided, and **an unenacted model act is not in the public domain under it**. The CC0 dedication is a choice, well supported by *Veeck*'s reasoning — the text becomes public domain the moment any legislature enacts it, so reserved rights expire on success — but *Veeck* is not authority that it must be ⚠ **No star pagination**; nothing may be pincited to it ([E47](../ledger/errata.md)) |
| *Zauderer v. Office of Disciplinary Counsel*, 471 U.S. 626 (1985) | n.16 | Factual, uncontroversial commercial disclosure |
| *NIFLA v. Becerra*, 585 U.S. 755 (2018) | n.16 | The narrowing, and what it preserved |
| *X Corp. v. Bonta*, 116 F.4th 888 (9th Cir. 2024) | n.16 | Compelled contested characterization — always cited as a preliminary-injunction likelihood ruling |
| *CTIA v. City of Berkeley*, 928 F.3d 832 (9th Cir. 2019) | n.16 | Objective compelled content survives |
| *National Ass'n of Wheat Growers v. Bonta*, 85 F.4th 1263 (9th Cir. 2023) | n.16 | Outside *Zauderer*; failed *Central Hudson* |
| *United States v. Alvarez*, 567 U.S. 709 (2012) (plurality) | n.16, n.20 | False-statement offenses expressly preserved |
| *Rumsfeld v. FAIR*, 547 U.S. 47 (2006) | n.16, n.26 | Compelled speech incidental to conduct regulation |
| *Connally v. General Construction Co.*, 269 U.S. 385 (1926) | n.24, n.25 | Vagueness in a criminal duty |
| *Kolender v. Lawson*, 461 U.S. 352 (1983) | n.24, n.25 | Same |
| *Bouie v. City of Columbia*, 378 U.S. 347 (1964) | n.24 | Retroactive judicial enlargement — the one-way ratchets answer it |

#### Records, privilege, and delegation

| Authority | Cited at | For |
|---|---|---|
| *Grosso v. United States*, 390 U.S. 62 (1968) (at 67–68) | n.26 | The three premises of the required-records doctrine |
| *Shapiro v. United States*, 335 U.S. 1 (1948) | n.26 | Required records outside the privilege |
| *Marchetti v. United States*, 390 U.S. 39 (1968) | n.26 | The boundary this Act stays inside |
| *Baltimore City Dep't of Social Servs. v. Bouknight*, 493 U.S. 549 (1990) | n.26 | Compelled production within a regulatory regime |
| *Touby v. United States*, 500 U.S. 160 (1991) | n.3 | Delegation confined by specific restrictions |
| *Sunshine Anthracite Coal Co. v. Adkins*, 310 U.S. 381 (1940) | n.3, n.24 | Static, agency-supervised incorporation |
| *Georgia v. Public.Resource.Org*, 590 U.S. 429 (2020) | standards/interim_standards.md; README | Government edicts carry no copyright |
| *County Court of Ulster County v. Allen*, 442 U.S. 140 (1979) | audit register F15 (not in statute or companion) | Rational-connection limit on permissive inferences — flagged for n.4 |

---

### II. Federal statutes and regulations

| Authority | Cited at | For |
|---|---|---|
| 18 U.S.C. § 1001 | n.20 | The free-standing false-statement structure |
| 18 U.S.C. § 1350 | n.8; n.19; SEC. 8 | ✅ **Read in full 25 Aug 2026.** Two tiers, **both requiring knowledge**: (c)(1) "Whoever certifies... **knowing** that the periodic report... does not comport" — \$1,000,000 / 10 years; (c)(2) "Whoever **willfully** certifies... **knowing**" — \$5,000,000 / 20 years. **There is no tier below knowledge.** SEC. 8's second limb ("reckless certification without reasonable inquiry") therefore has no counterpart in the model the Act says it is built on, and SEC. 6(a), where that limb routes, requires only failure of due care. See [PF-7](../audit/pre_review_pass_2026-08-24.md) |
| 18 U.S.C. § 1365(a) | SEC. 10(c); n.21 | The harm tier's geometry — twenty years per serious injury; life where death results |
| 18 U.S.C. § 1365(h)(3)–(4) | v3.5 queue, CURE 1 (adopted, not yet landed) | The injury definition replacing 21 C.F.R. § 803.3(w). **Cite with care: these definitions sat at § 1365(g)(3)–(4) until 2 December 2002**, when Pub. L. 107-307 (the *Product Packaging Protection Act of 2002*) added a new subsection (f) and pushed the old (f) and (g) down to (g) and (h). Authority predating that amendment cites the same words under the old letter |
| 18 U.S.C. § 1519 | n.23 | Destruction "in relation to or contemplation of" — restated as an affirmative hold |
| 18 U.S.C. § 1520(a)(1) | n.23 | The five-year statutory floor extended by rule to seven |
| 18 U.S.C. § 3571(b), (d) | n.19; SEC. 10(b) | ✅ **Read 25 Aug 2026.** (b)(5) is exactly as cited: "for a **Class A misdemeanor that does not result in death**, not more than \$100,000" — and SEC. 10(b)'s one-year maximum is what makes the offense Class A (18 U.S.C. § 3559(a)(6)), so the classification and the amount agree. **One divergence.** § 3571(d) allows "not more than the greater of **twice the gross gain or twice the gross loss**"; SEC. 10(b) and 10(c) take **only the gain limb** ("twice the gross pecuniary gain to the person"). In this Act's paradigm case a controlling person's personal gain from failing to halt may be near zero while third-party loss is vast, so the limb dropped is the one that would bite. **Probably deliberate — SEC. 10(c)(4) restitution answers loss and the fine strips gain, which avoids counting loss twice — but the citation says "as to amount" and the source's amount has two limbs** |

**A note on the donor of the harm tier, added 25 August 2026.** § 1365 is not a stray federal
section. It was enacted whole by **Pub. L. 98-127, § 1, Oct. 13, 1983, 97 Stat. 831**, whose own
short title is the **Federal Anti-Tampering Act**, and which also enacted 35 U.S.C. § 155A. The
LII page and its notes are held on [the shelf](../research/verification_record.md); the provenance
below is read from them rather than inferred.

**Three things the amendment history gives this Act, and the first is the most useful.**

**One. Congress swept its own fixed dollar fines out of this statute eleven years after enacting
them.** As passed in 1983 the section carried four hard numbers: \$25,000, \$100,000, \$50,000 and
\$10,000. In 1994, Pub. L. 103-322 § 330016(1)(L), (O), (Q), (S) replaced every one of them with
*"fined under this title"*, which routes to 18 U.S.C. § 3571. **That is exactly the choice this Act
already makes** at n.19, where individual fines take § 3571(b) parity and the criminal fines carry
§ 3571(d)'s twice-the-gross-gain alternative, against the cautionary example of the FDCA's
\$1,000 sitting nominal since 1938. The design preference is now a documented federal correction,
made by Congress, to the very statute this Act's harm tier borrows from. A model act offered to
fifty legislatures inherits the same decay problem and the same fix.

**Two. The geometry has held for forty-three years across three amendments.** 1990 (Pub. L.
101-647), 1994 (Pub. L. 103-322) and 2002 (Pub. L. 107-307) touched the fines, the lettering and a
punctuation mark. **The tier itself — twenty years where serious bodily injury results, any term of
years or life where death results — has never been reopened.** A drafter borrowing it is borrowing
a structure Congress built for a novel hazard class and has left alone ever since.

**Three, and it belongs to this project's own habits.** Pub. L. 101-647, § 3544 exists, in part, to
insert *"opening quotation marks before 'device'"* in what is now § 1365(h)(1)(A). Congress passed
an Act to add a missing quotation mark. Enacted federal law keeps an errata register too; ours is
at [the errata](../ledger/errata.md) and is not a sign of an unusually careless draft.

*Credit where it is owed: the move to § 1365's injury definition came from outside this project, in
one sentence, from a criminal-law scholar who has not elected to be named. It is
[CURE 1](../audit/v3_5_cure_language.md).*
| 18 U.S.C. § 3572(a) | n.19 | Means consideration in fixing fines |
| 18 U.S.C. § 3584(a)–(b) | SEC. 10(c)(3); n.21 | Concurrency default; the per-offense factor duty |
| 18 U.S.C. § 3663A | SEC. 10(c)(4); n.21 | ✅ **Read 25 Aug 2026. Exact match on the operative words.** (a)(1): restitution "to the victim of the offense or, **if the victim is deceased, to the victim's estate**" — SEC. 10(c)(4)'s "or to the person's estate" is the statute's own phrasing. (a)(2) victim: "a person **directly and proximately harmed** as a result of the commission of an offense." **Note for completeness**: § 3663A(c) makes restitution mandatory only for an enumerated list (crimes of violence, property/fraud offenses, 21 U.S.C. § 856(a), Rodchenkov, **18 U.S.C. § 1365**, § 670). An offense under this Act is not on it; the Act imposes the duty directly, so "per the structure of" is the correct and only claim. **§ 1365 being on that list is a coherence point never made**: the Act's restitution model and its serious-injury source (CURE 1, § 1365(h)(3)) are the same federal statute |
| 21 U.S.C. § 331(e) | SEC. 5(e); n.26 | The two-limb records offense |
| 21 U.S.C. § 332 | SEC. 10(d)(1); n.10 | ✅ **Read 25 Aug 2026.** (a) jurisdiction "for cause shown to restrain violations of section 331" — the same shape as SEC. 10(d)(1). **(b) is the subsection the Act needed and did not take**: "In case of violation of an injunction or restraining order issued under this section, **which also constitutes a violation of this chapter**, trial shall be by the court, or, **upon demand of the accused, by a jury**." SEC. 10(d)(2) creates exactly that overlap — operation of a suspended configuration "is contempt **and** a violation of SEC. 5(a)" — and says nothing about the mode of trial. See [PF-8](../audit/pre_review_pass_2026-08-24.md) |
| 21 U.S.C. § 334 | SEC. 10(d)(2); n.10 | ✅ **Read 25 Aug 2026, and the analogy is looser than the citation claims.** § 334 is an **in rem** proceeding against a thing: an adulterated or misbranded article "proceeded against... **on libel of information and condemned**," with procedure that "shall conform, as nearly as may be, to the procedure **in admiralty**," and "on demand of either party any issue of fact... shall be tried by jury." SEC. 10(d)(2) takes the thing-directed *idea* — the remedy attaches to an identified model version and configuration rather than to a person — and **none of the procedure**: no in rem form, no intervention by claimants, no jury. Functionally it is prospective and injunctive, which makes it § 332's relative rather than § 334's. **A suspension binding "any person with notice" is a remedy against software that binds non-parties, and § 334 answered that with admiralty procedure while this Act answers it with notice** |
| 21 U.S.C. § 333(a)(1)–(2) | n.19, n.22 | ✅ **Read 25 Aug 2026.** (a)(1): "imprisoned for not more than one year or fined not more than \$1,000" — **no mental state stated**. (a)(2): "if any person commits such a violation **after a conviction of him under this section has become final, or** commits such a violation **with the intent to defraud or mislead**" — three years / \$10,000. Confirms the two claims the record makes at n.22 and D.5: the two routes to the felony are **alternative**, and the source carries **no lookback limit**, so the Act's [ten]-year washout is the more merciful departure the record says it is |
| 21 U.S.C. § 841(b)(1)(C) | n.21 | Ceiling structure — twenty base, life where death results |
| 33 U.S.C. § 1319(d) | SEC. 10(a); n.10, n.19 | ✅ **Read 25 Aug 2026. The six factors are transplanted verbatim and in the source's own order**: "the seriousness of the violation or violations, the economic benefit (if any) resulting from the violation, any history of such violations, any good-faith efforts to comply with the applicable requirements, the economic impact of the penalty on the violator, and such other matters as justice may require." **Two divergences this row previously concealed.** (i) **§ 1319(d) has no penalty floor.** It makes economic benefit a factor to *consider*; SEC. 10(a)'s "shall not be less than the economic benefit or savings derived" is the Act's own addition, defensible on the deterrence scholarship at n.19 but **not the structure of § 1319(d)**, and this row until 25 Aug 2026 credited the source with it. (ii) SEC. 10(a) reads "economic benefit **or savings**"; § 1319(d) says "the economic benefit (if any)" and 42 U.S.C. § 7413(e)(1) (checked as the obvious alternative donor, also read 25 Aug) says "the economic benefit of noncompliance." **Neither federal source carries "or savings" and its origin is not established here** |
| 15 U.S.C. § 7243 (SOX § 304) | n.7, n.18 | ✅ **Read 25 Aug 2026; the record's account at n.18 and at the comparative table is exact.** Trigger verbatim: "If an issuer is required to prepare an accounting restatement due to the material noncompliance **of the issuer, as a result of misconduct**, with any financial reporting requirement." **The statute does not say whose misconduct** — which is what makes the no-fault reading possible and is the whole of the point. Reaches "the chief executive officer and chief financial officer" only; lookback is "the 12-month period following the first public issuance or filing"; categories are "any bonus or other incentive-based or equity-based compensation" and "any profits realized from the sale of securities of the issuer"; and (b) "The Commission may exempt any person." Every limb the record calls the known weakness is confirmed present |
| 15 U.S.C. § 78u-6 (Exchange Act § 21F) | n.11; SEC. 11 | ✅ **Read 25 Aug 2026. The closest transplant in the Act; every operative term matches.** Threshold: "monetary sanctions exceeding \$1,000,000" = SEC. 11's \$[1,000,000]. Range: "not less than 10 percent, in total, of what has been **collected** of the monetary sanctions imposed" and "not more than 30 percent" = SEC. 11's "not less than 10 and not more than 30 percent of the sanctions **collected**" — including *collected* rather than *imposed*, which is the limb that matters and which the Act got right. Mandatory in both ("shall pay" / "shall receive"). Fund: awards paid from the SEC Investor Protection Fund = SEC. 10(f). Anonymity: "shall be represented by counsel if the whistleblower anonymously submits" = SEC. 11(b)'s "anonymously through counsel" |
| 33 U.S.C. § 1319(c)(1)–(2) | **new row 25 Aug 2026**; SEC. 6(a) | ✅ **Read 25 Aug 2026. The federal model for SEC. 6(a) that this project has never claimed.** (c)(1) punishes one who "**negligently** violates" — up to **one year** on a first conviction, \$2,500–\$25,000 per day. (c)(2) punishes one who "**knowingly** violates" — up to three years. Read with (c)(6) below, **federal law imposes criminal liability on a responsible corporate officer for a merely negligent violation, at the misdemeanor level**, which is SEC. 6(a)'s exact shape. And *Ahmad*'s objection does not reach it: (c)(1) is a misdemeanor, not a "felony punishable by years in federal prison" |
| 33 U.S.C. § 1319(c)(6) | [comparative § 5](./comparative_officer_liability.md#5-the-united-states-today--the-codified-officer) | "Person" **means** — not "includes" — "any responsible corporate officer": the doctrine codified, criminal subsection. **Read-status and the verbatim text live on the row above under "The doctrine"**; this row records the comparative use only |
| 42 U.S.C. § 7413(c)(6) | comparative § 5 | ✅ **Read 25 Aug 2026, verbatim**: "For the purpose of this subsection, the term 'person' **includes**, in addition to the entities referred to in section 7602(e) of this title, **any responsible corporate officer**." **Note the verb.** The CWA at § 1319(c)(6) says "**means**… in addition to"; the CAA says "**includes**… in addition to." Both expand, but they are not the same drafting choice, and an adopting state's counsel will pick one. The same codification in the Clean Air Act, added 1977 — post-*Park* |
| *United States v. Iverson*, 162 F.3d 1015 (9th Cir. 1998) | comparative § 5 | ✅ **Text read 25 Aug 2026**, pincite unconfirmed: post-*Park* retention read as congressional ratification. See the criminal-lane row above for the transcribed passages |
| *United States v. Hodges X-Ray, Inc.*, 759 F.2d 557 (6th Cir. 1985) | comparative § 5 | The officer rationale "even more persuasive" for civil liability (at 561) |
| *United States v. Morris*, 928 F.2d 504 (2d Cir. 1991) | [the gallery's escape section](./the_same_conduct.md#when-the-escaped-thing-was-the-crime); [already a crime § limb 2](./already_a_crime_for_you.md) | "Intentionally" attaches to access, not damage; the accidental self-replicating outbreak, convicted |
| 7 U.S.C. § 7734 | the gallery's escape section | Knowing movement of a noxious weed: five-year felony |
| 42 C.F.R. § 73.19 | the gallery's escape section; [who has to tell you § 4b](./who_has_to_tell_you.md); [CURE 18](../audit/v3_5_cure_language.md) | The select-agent escape clock: immediate notice, Form 3 in seven days |
| Lyness, 64 B.C. L. Rev. 253 (2023) | comparative § 5; [for legislators § 4](./for_legislators.md) | The federal and state environmental RCO survey; the four-goal revitalization agenda. **Cited against this Act as well as for it:** he argues the state doctrine should carry "individual civil liability—and only civil liability," and that *Dotterweich* and *Park* supply misdemeanor-scale authority "during a time when the immediate and collateral consequences were different" (at 297–98). Full article read 25 Aug 2026 |
| Hustis & Gotanda, 25 Loy. U. Chi. L.J. 169 (1994) | comparative § 5 | The enforcement-wave record (officers 80% of individuals prosecuted); the objection's title |
| 15 U.S.C. §§ 7901–7903 (PLCAA) | field notes 3 (objection bank) | Gun-maker immunity as a legislative choice, not a default |
| 42 U.S.C. § 2210 (Price-Anderson) | field notes 6 | The purchased shield — cap paid for with channeled liability |
| 10 C.F.R. Part 55; § 50.5 | field notes 6 | Individually licensed operators; the deliberate-misconduct rule |
| 17 C.F.R. § 240.10D-1 | n.7, n.18 | Mandatory clawback; the flat indemnification bar |
| 17 C.F.R. § 210.2-06 | n.23 | Seven-year retention by rule |
| 21 C.F.R. § 803.3(w) | SEC. 1(b)(8) (current); superseded by CURE 1 at v3.5 | The serious-injury definition being replaced |
| 21 C.F.R. § 803.3, § 803.50(c), § 803.53(b), § 803.56 | n.9; regulations Parts 1.2–1.3, 5.3–5.4 | Awareness triggers, reportable information, escalation, supplemental reports |
| 40 C.F.R. § 19.4 | n.10, n.19 | Live proof that indexing works — \$25,000 to \$68,445 by rule |
| U.S.S.G. § 5G1.2(c)–(d) | n.21 | Stacking only to the total punishment required |
| Model Penal Code § 7.06(1), (1)(c) | n.21 | The aggregate-cap tradition — stricter than the Kansas double rule |

---

### III. State and foreign law

| Authority | Cited at | For |
|---|---|---|
| Cal. Bus. & Prof. Code § 22757.12 | SEC. 3(c)(4); n.24, n.27; standards | ✅ **Read in full** (census: "the chaptered text read in full", pinned verbatim). Interim standard — the frontier-framework duty. **The only one of the Act's three adopted standards that has been read by a human** |
| Cal. Bus. & Prof. Code § 22757.13, § 22757.15 | n.19, n.27 | Incident clocks; the \$1,000,000 severity-scaled penalty |
| N.Y. Gen. Bus. Law § 1421, § 1427, § 1426 | SEC. 3(c)(4); n.19, n.24, n.27; standards | ✅ **§ 1421 read in full 25 Aug 2026** from the enacted chapter text (sibling New York repository), discharging the census's R grade. Interim standard. **Four provisions the Act adopts and never mentions**: (1)(j) internal-use catastrophic risk and oversight circumvention; (4)(a)(ii) a duty not to misstate compliance with one's own framework, which is SEC. 8's offense owed by the entity; (4)(b) a good-faith-and-reasonableness defense; (5) a trade-secret redaction right with five-year unredacted retention. See [PF-11](../audit/pre_review_pass_2026-08-24.md) |
| N.Y. Penal Law § 80.00(1) | n.19 | State-native gain-scaled fines |
| Illinois P.A. 104-0538 (SB 315) § 10, § 15, § 25 | SEC. 3(c)(4); n.19, n.23, n.27; standards | ✅ **§ 10 read in full 25 Aug 2026** from the enrolled slip law, discharging the census's R grade. Interim standard. § 10(a)(1)–(10) is the same ten-item framework list as N.Y. § 1421(1)(a)–(j), **including (a)(10) internal use**; § 10(c)(3) adds a **machine-readable** format requirement New York lacks. See [PF-10](../audit/pre_review_pass_2026-08-24.md) |
| K.S.A. 21-6819(b)(4) | SEC. 10(c)(3); n.21 | The double rule behind the [forty]-year cap |
| Ohio Rev. Code § 2929.14(C)(4) | SEC. 10(c)(3); n.21 | Findings-gated consecutive service |
| Ill. Const. art. I, § 11; Or. Const. art. I, § 16; Ind. Const. art. 1, § 16; W. Va. Const. art. III, § 5 | n.21 | State proportionality clauses stricter than *Harmelin*. **Text status, 26 Aug 2026, clause by clause.** **Illinois** — quoted in full in the companion. **Indiana** — ✅ **READ IN THE DOCUMENT 26 Aug 2026**, in a Justia print of Article 1 now held on the shelf, and confirmed character for character against the Indiana General Assembly's own constitution PDF (current to 5 Nov. 2024): "Excessive bail shall not be required. Excessive fines shall not be imposed. Cruel and unusual punishments shall not be inflicted. **All penalties shall be proportioned to the nature of the offense.**" The companion had cited it bare; **it is now pinned, and it is the last of the two clauses the retrieval list called the quiet scandal.** **West Virginia** — art. III § 5 is present in a whole-constitution capture held on the shelf, unread. **Oregon** — ⚠ **the companion quotes it and nobody has pinned it.** ⚠ **Collision recorded before it bites:** Oregon and Indiana are both art. § 16, both open the same way, and differ by three words — the companion gives Oregon as "proportioned to the offense" and Indiana reads "proportioned to **the nature of** the offense." Pin Oregon against Oregon's own publication, never against Indiana's |
| Tex. Bus. & Com. Code § 552.104 (TRAIGA) | field notes 13 | The sixty-day cure period the Act declines |
| Work Health and Safety Act 2011 (NSW) ss 272, 272A–272B | n.7, n.18 | Penalty insurance as an offense — enter, provide, benefit |
| Reg. (EU) 2024/1689 (AI Act) arts. 18(1), 51–55, 53(2) | n.5, n.23, n.27 | Ten-year documentation; GPAI duties; the open-source exemption withdrawn above systemic risk |

---

### IV. Legislative and federal-vehicle material

| Authority | Cited at | For |
|---|---|---|
| FRONTIER Act, H.R. 9925 (2026) § 9(a)–(d) | n.13, n.15; record chunk 2 | Covered Subject Areas and the conditioned criminal savings the armor is drafted against |
| Great American AI Act discussion draft (2026) § 121 | n.13, n.15; record chunk 2 | Development-specific preemption; the post-deployment savings clause; the three-year sunset |
| H.R. 5388 (2025) §§ 6–7 | n.13; record chunk 2 | The only unconditional criminal savings text in the field — § 6(a)(2)(B) |
| 94 Cong. Rec. 6760-61, 8551, 8838 (1948) | n.6 | The struck good-faith amendment — the defense this Act declines to reenact |
| FDA Regulatory Procedures Manual, Park-doctrine referral criteria | n.6 | The enforcement culture the elements are pre-fitted to |
| S. Hrg. 119-202, *Too Big to Prosecute?*, S. Judiciary Subcomm. on Crime and Counterterrorism (16 July 2025) | `docs/known_objections.md`; `standards/who_has_to_tell_you.md` § 4c | The enforcement gap stated by the subcommittee chair (printed p. 1); the two-prong criminal test and the escalation-to-CEO finding (pp. 15, 26); the best statement of the wait-for-the-courts objection and Durbin's § 230 rejoinder (pp. 13, 18, 20). ⚠ Body text read by validated font decode; appendix by OCR and not publication-grade. **Also unheld, and recorded here 26 Aug 2026 because the verification record carried it and this table did not**: the separate govinfo `-add1.pdf` package of submitted letters and statements |
| S. Hrg. 119-505, *Less Hype, More Help*, S. Commerce Subcomm. on Science, Manufacturing, and Competitiveness (3 Mar. 2026) | `docs/known_objections.md` | An industry witness's statement that AI "operates within" existing accountability frameworks and that regulatory predictability supports deployment. ⚠ Senators' statements unread |
| S. Hrg. 119-255, *Hidden Harms: Examining Whistleblower Allegations That Meta Buried Child Safety Research*, S. Judiciary Subcomm. on Privacy, Technology, and the Law (9 Sept. 2025) | `standards/who_has_to_tell_you.md` § 4d | The mechanism by which internal safety findings become unrecoverable without anyone destroying anything: a ninety-day raw-data deletion policy plus removal of lines from the report (printed pp. 14, 28-29). **Sworn allegation, not adjudicated fact**; cite only with that limit attached |
| S. Hrg. 119-284, *AI've Got a Plan: America's AI Action Plan*, S. Commerce Subcomm. on Science, Manufacturing, and Competitiveness (10 Sept. 2025) | `docs/known_objections.md` | The executive branch's own statement of the preemption position, and the concession inside it that patchwork compliance advantages the largest firms (printed pp. 8, 13-14) |
| N.Y. S 1169-B (2025-26), Gonzalez, §§ 109, 110, 114 | `standards/frontier_bill_census.md`; `standards/who_has_to_tell_you.md` § 4d; `docs/known_objections.md` | The most developed auditor-independence text in any American AI bill held here; a statutory anonymous internal disclosure channel with a monthly status duty; and a pleading-stage presumption of violation and causation which an audit alone may not rebut. **A bill, not law**; status unverified |

---

#### Federal agency action — opened 26 August 2026

| Authority | Cited at | For |
|---|---|---|
| *Trump v. Slaughter*, No. 25-332 (U.S. 2026) | the federalism lane | ✅ **READ, 26 Aug 2026, and the commentary's account was right.** The holding, verbatim: **"If anything more is left of *Humphrey's*, we overrule it."** What survives of the 1935 case is only "its observation that an agency that 'exercises no part of the executive power' need not fall within the rule of Presidential removal" ✅ **And the question this row asked is answered: SEC. 3's Agency is untouched.** The decision rests entirely on **Article II** and the President's removal power over federal officers. **The phrase "state agency" does not appear in the opinion**, and nothing in its reasoning reaches a State's power to structure its own agencies, which is a matter for that State's own constitution ⚠ **What is exposed is rhetorical, and it is still owed.** SEC. 3 is built on the independent-commission model and that model has lost its federal exemplar. A legislator who asks why a State should build one now has a fair question with a good answer — the objection is about Article II and a State is not subject to it — **and that answer is written nowhere in this repository** ([E75](../ledger/errata.md)) ⚠ **Slip opinion**, No. 25-332, OT2025, argued 8 Dec. 2025, decided 29 June 2026; no U.S. Reports pincite from this copy |
| **FTC, Policy Statement Concerning the Suppression of Accuracy in Artificial Intelligence**, File No. P264200, 91 Fed. Reg. 41638 (7 July 2026) | SEC. 0(a)(4); SEC. 13(c); the federalism lane | ✅ **PRIMARY NOW HELD AND READ IN FULL, 26 Aug 2026** (Federal Register print, five pages, on the shelf). **The secondary made it sound broader than it is** — Lawfare reported that the Commission "asserted that Section 5 could preempt certain state AI laws," which is true and omits the limit. **Verbatim:** "Although the FTC Act does not expressly preempt State law, **State law is impliedly preempted to the extent it conflicts with a Federal regulatory scheme.** A State law that requires an AI firm to **deceive its consumers** obviously conflicts with section 5's express purpose." **The theory is conflict preemption confined to state laws "requiring alterations to the accurate outputs of AI models"** — it names Colorado's revised AI Act, references California, and rests on E.O. 14319's "ideological agendas" framing. **It does not reach this Act, and SEC. 0(a)(4) is why**: no provision "requires any person to express, adopt, endorse, or refrain from expressing any opinion… **or to alter the output of any covered system**." SEC. 9(c) says the same of reports. **That finding was drafted against compelled speech and answers this instead** |
| *Wistisen v. Alibaba Group Holding Limited*, No. 1:26-cv-06654 (S.D.N.Y., filed 4 Aug. 2026) | **caption corrected 26 Aug 2026**; known objections | ⚠ **Unread; a docket metadata stub is held, not the complaint.** Caption, docket number, court and filing date confirmed against the CourtListener RECAP index on 26 Aug 2026. A securities class action against Alibaba **and its chief executive personally**, alleging investors were misled about the company's AI-related activities and the risks attending them, known here from The D&O Diary. **Relevant to the "existing law already reaches officers" objection**: it shows securities law reaching an officer for AI statements. ⚠ **Correction carried:** this row previously read *In re Alibaba Group Holding Ltd. Securities Litigation*. **That caption was never in any source this project held** — the D&O Diary piece names no case at all and calls it "the Alibaba SCA" throughout. See [E54](../ledger/errata.md) |

---

### V. Scholarship

| Authority | Cited at | For |
|---|---|---|
| Becker, *Crime and Punishment: An Economic Approach*, 76 J. Pol. Econ. 169 (1968) | n.19 | Deterrence requires the expected sanction to exceed the benefit |
| Gneezy & Rustichini, *A Fine Is a Price*, 29 J. Legal Stud. 1 (2000) | n.19 | Why a payable fine is a price |
| Shavell, *The Judgment Proof Problem*, 6 Int'l Rev. L. & Econ. 45 (1986) | n.19 | Why fines alone cannot reach the judgment-proof or the equity-rich |
| Guidelight AI Standards, *Control Assessment of Frontier AI Companies* (18 Aug 2026) | known objections, reasonable inquiry; SEC. 3(c)(4)(C) | ✅ **Read in the primary 25 Aug 2026** (held in the working library). Six practices from public information only, June–Aug 2026. Anthropic C+ (2.50), OpenAI C+ (2.50), Google D+ (1.50), xAI D− (0.83), Meta F (0.67). "no company's score on any practice exceeded a 3." "[T]he best public evidence is that companies have few containment protocols ready for an emergency." "Three companies describe logging at least some internal usage that is then scanned for signs of misbehavior." "Four of them (all but xAI) participated in METR's first Frontier Risk Report." No byline; rubric not audited here |

---

### VI. Candidate authorities — read since v3.4, not yet cited

*The July–August 2026 research produced two authorities strong enough to name here, held
separately because neither is yet cited in the operative text or the companion. They are
candidates for v3.5, flagged for the enforcement and premise lanes.*

| Authority | Bears on | For |
|---|---|---|
| *Moffatt v. Air Canada*, 2024 BCCRT 149 (14 Feb. 2024) | SEC. 0; the "can a model act" premise | An **adjudicated** rejection of the defense that software is "a separate legal entity that is responsible for its own actions" (¶27). A tribunal has already answered the core "but the AI did it" objection: liability stays with the legal person who deployed it. |
| Desai & Riedl, *Responsible AI Agents* (draft, 20 Feb. 2025), arXiv:2502.18359 | SEC. 0; the personhood premise | ✅ **READ, 26 Aug 2026, and both propositions are verbatim.** From the abstract: "no matter how much AI Agents seem like human agents, they need not, and should not, be given legal personhood status. In short, **humans are responsible for AI Agents' actions**." And the shield reasoning: "Anthropomorphizing software confuses issues and could lead to a world where software has legal personhood, related rights, and **liability shields**. If that happens, the power for people to use software would grow while also increasing the ability to avoid responsibility. That is the situation to avoid." **Ally on the premise, not the mechanism** — confirmed on the same page, "responsible AI Agents are about responsible human action", by authors who prefer design standards and product-liability benchmarks to personal criminal duties. **Cite for the premise only, never as endorsing the Act's method** |
| *Concord Music Group, Inc. v. Anthropic PBC*, No. 5:24-cv-03811 (N.D. Cal. Dec. 19, 2025) (van Keulen, M.J.) | SEC. 4; the enforcement lane, question 5 | **A court, on evidence, finding that a frontier developer's chief executive personally held knowledge of model training that nobody else could supply** — the factual premise of SEC. 4, found rather than asserted. Amodei ordered to sit for a deposition, capped at 2.5 hours, over Anthropic's argument that he lacked unique knowledge. ⚠ **The order has not been retrieved**; this rests on secondary reporting and neither source names the apex doctrine. **Not citable until the docket entry is in hand.** Civil discovery, not criminal liability, and "intimately involved in training" is not "final authority to prevent or halt" ✅ **Docket metadata stub held 26 Aug 2026**, confirmed against the CourtListener RECAP index: 5:24-cv-03811, N.D. Cal., filed 26 June 2024. The docket sheet itself is not held |
| *Kadrey v. Meta Platforms, Inc.*, No. 3:23-cv-03417-VC, 2025 WL 1752484 (N.D. Cal. June 25, 2025) | n.19; the proportionality lane | The district court's answer to the "liability would stop the technology" argument: "the suggestion that adverse copyright rulings would stop this technology in its tracks is ridiculous ... If using copyrighted works to train the models is as necessary as the companies say, they will figure out a way to compensate copyright holders for it." ⚠ **Quoted at second hand**, from Maxwell Pritt's written answers at S. Hrg. 119-202 printed p. 93, read by OCR. **The opinion itself has not been retrieved and the pin cite is his, not ours.** Do not cite until the slip opinion is in hand ⚠ **Docket number corrected 26 Aug 2026 from 23-CV-03217-VC.** The witness's submitted answers give **two different numbers two footnotes apart** — 03217 at n.1 and 03417 at n.2 — and this project took the first without reading to the bottom of the page. CourtListener's RECAP index confirms 3:23-cv-03417, N.D. Cal., filed 7 July 2023. A docket metadata stub is now held. See [E55](../ledger/errata.md) |

---

### VII. Open items in this table

The cite-check queue (companion, READ FIRST item 10) as it bears on the entries above,
**revised 26 August 2026 against the shelf as it now stands**: U.S.S.G. § 5G1.2(d) — ✅ **the 2025
Manual print, 553 pp., is now held**, so this is a read rather than a retrieval; Model Penal Code
§ 7.06 against an ALI print — still mirror-pinned only, and **no free source was found**; the Ohio
§ 2929.14(C)(4)(a)–(c) subclauses verbatim — ⚠ **codes.ohio.gov refused the connection on 26 August
from two independent networks**, so this is the site rather than any one route; **W. Va. Const.
art. III, § 5** — ✅ present in a whole-constitution capture now held; **Ind. Const. art. 1, § 16**
— ◐ **text pinned on 26 August from two independent publishers but through a model-mediated fetch**
([E57](../ledger/errata.md)), so the clause is known and the document is not held; the Illinois
Act's ILCS compilation cite — ⚠ **ilga.gov refused the connection**, though the enrolled act is
already on the shelf; *Monsanto v. Durnell*'s U.S. Reports pagination; and the NSW s 272A
penalty-unit maxima from primary — ⚠ **the NSW legislation site and its AustLII mirror both refused
a machine**. Everything else above has been read against a
primary or first-party source at some point in the record; this table does not re-verify,
it locates.

*Compiled 20 August 2026 against the v3.4 tag. Corrections to FrontierAIAccountabilityProject@proton.me; they enter
the errata register like everything else.*

---

## Adopted standards

SEC. 3(c)(4) of the Model Act adopts, as its interim standards, the frontier
artificial intelligence framework duties of three enacted state laws, "each as in
effect on [1 August 2026] ... as they so exist and not as they may afterward be
amended, repealed, suspended, or invalidated in the enacting jurisdiction," and
directs that "the Agency shall make the adopted texts publicly available without
charge." **A fourth state has since enacted one, and it is deliberately not below.** Connecticut's SB 5
became law on 27 May 2026, on the same 10²⁶-operation threshold, with a large-developer tier at
\$500,000,000 in annual revenue. It is **not** adopted at SEC. 3(c)(4), for two reasons stated here
so that its absence is a decision rather than an oversight. First, adding an interim standard
changes the tagged statutory text, and the reproducibility chain the reviewer's copy rests on
forbids editing a tagged file — see [E10](../ledger/errata.md); it is therefore a v3.5 drafting
question, held in [the open cure queue](../audit/v3_5_cure_language.md). Second, and substantively,
Connecticut's frontier provision is an **internal whistleblower channel** rather than a
safety-framework duty of the kind SEC. 3(c)(4) adopts — its operative requirement is that
catastrophic-risk reports "shall be shared with the officers and directors of the large frontier
developer at least quarterly", with no duty attaching to those officers. Whether that belongs among
the adopted duties is a question for a drafter, not a housekeeping fix. The full row is at
[the bill census](./frontier_bill_census.md); the miss that produced this paragraph is
[E16](../ledger/errata.md).

A research draft has no Agency; it has a repository. This file practices
the rule before preaching it: the adopted texts, pinned here verbatim, free to
read. State statutes are government edicts and carry no copyright (*Georgia v.
Public.Resource.Org*, 590 U.S. 429 (2020)); the enacting jurisdictions' official
publishers control over any transcription error here. Line wrapping has been
normalized from the source presentations; wording, numbering, and punctuation are
untouched.

---

### 1. California — Business and Professions Code § 22757.12

*Division 8, Chapter 25.1 (Transparency in Frontier Artificial Intelligence Act).
Added by Stats. 2025, ch. 138, § 2 (SB 53), effective January 1, 2026. Reproduced
from the 2025 California Code as published by Justia
(law.justia.com/codes/california/code-bpc/division-8/chapter-25-1/section-22757-12/),
retrieved 19 August 2026; the official publication at leginfo.legislature.ca.gov
controls.*

22757.12. (a) A large frontier developer shall write, implement, comply with, and
clearly and conspicuously publish on its internet website a frontier AI framework
that applies to the large frontier developer's frontier models and describes how
the large frontier developer approaches all of the following:

(1) Incorporating national standards, international standards, and
industry-consensus best practices into its frontier AI framework.

(2) Defining and assessing thresholds used by the large frontier developer to
identify and assess whether a frontier model has capabilities that could pose a
catastrophic risk, which may include multiple-tiered thresholds.

(3) Applying mitigations to address the potential for catastrophic risks based on
the results of assessments undertaken pursuant to paragraph (2).

(4) Reviewing assessments and adequacy of mitigations as part of the decision to
deploy a frontier model or use it extensively internally.

(5) Using third parties to assess the potential for catastrophic risks and the
effectiveness of mitigations of catastrophic risks.

(6) Revisiting and updating the frontier AI framework, including any criteria that
trigger updates and how the large frontier developer determines when its frontier
models are substantially modified enough to require disclosures pursuant to
subdivision (c).

(7) Cybersecurity practices to secure unreleased model weights from unauthorized
modification or transfer by internal or external parties.

(8) Identifying and responding to critical safety incidents.

(9) Instituting internal governance practices to ensure implementation of these
processes.

(10) Assessing and managing catastrophic risk resulting from the internal use of
its frontier models, including risks resulting from a frontier model circumventing
oversight mechanisms.

(b) (1) A large frontier developer shall review and, as appropriate, update its
frontier AI framework at least once per year.

(2) If a large frontier developer makes a material modification to its frontier AI
framework, the large frontier developer shall clearly and conspicuously publish
the modified frontier AI framework and a justification for that modification
within 30 days.

(c) (1) Before, or concurrently with, deploying a new frontier model or a
substantially modified version of an existing frontier model, a frontier developer
shall clearly and conspicuously publish on its internet website a transparency
report containing all of the following:

(A) The internet website of the frontier developer.

(B) A mechanism that enables a natural person to communicate with the frontier
developer.

(C) The release date of the frontier model.

(D) The languages supported by the frontier model.

(E) The modalities of output supported by the frontier model.

(F) The intended uses of the frontier model.

(G) Any generally applicable restrictions or conditions on uses of the frontier
model.

(2) Before, or concurrently with, deploying a new frontier model or a
substantially modified version of an existing frontier model, a large frontier
developer shall include in the transparency report required by paragraph (1)
summaries of all of the following:

(A) Assessments of catastrophic risks from the frontier model conducted pursuant
to the large frontier developer's frontier AI framework.

(B) The results of those assessments.

(C) The extent to which third-party evaluators were involved.

(D) Other steps taken to fulfill the requirements of the frontier AI framework
with respect to the frontier model.

(3) A frontier developer that publishes the information described in paragraph (1)
or (2) as part of a larger document, including a system card or model card, shall
be deemed in compliance with the applicable paragraph.

(4) A frontier developer is encouraged, but not required, to make disclosures
described in this subdivision that are consistent with, or superior to, industry
best practices.

(d) A large frontier developer shall transmit to the Office of Emergency Services
a summary of any assessment of catastrophic risk resulting from internal use of
its frontier models every three months or pursuant to another reasonable schedule
specified by the large frontier developer and communicated in writing to the
Office of Emergency Services with written updates, as appropriate.

(e) (1) (A) A frontier developer shall not make a materially false or misleading
statement about catastrophic risk from its frontier models or its management of
catastrophic risk.

(B) A large frontier developer shall not make a materially false or misleading
statement about its implementation of, or compliance with, its frontier AI
framework.

(2) This subdivision does not apply to a statement that was made in good faith and
was reasonable under the circumstances.

(f) (1) When a frontier developer publishes documents to comply with this section,
the frontier developer may make redactions to those documents that are necessary
to protect the frontier developer's trade secrets, the frontier developer's
cybersecurity, public safety, or the national security of the United States or to
comply with any federal or state law.

(2) If a frontier developer redacts information in a document pursuant to this
subdivision, the frontier developer shall describe the character and justification
of the redaction in any published version of the document to the extent permitted
by the concerns that justify redaction and shall retain the unredacted information
for five years.

(Added by Stats. 2025, Ch. 138, Sec. 2. (SB 53) Effective January 1, 2026.)

---

### 2. New York — General Business Law § 1421

*Article 44-B (Responsible AI Safety and Education (RAISE) Act), added by ch. 96,
L. 2026. Reproduced from the official New York State Senate OpenLegislation
publication (nysenate.gov/legislation/laws/GBS/1421), revision of record 3 April
2026, retrieved 19 August 2026. The source carries the note "NB Effective
January 1, 2027"; SEC. 3(c)(4)(A) of the Model Act adopts the duties without
regard to the enacting jurisdiction's effective or phase-in dates.*

§ 1421. Transparency requirements. 1. A large frontier developer shall write,
implement, comply with, and clearly and conspicuously publish on its internet
website a frontier AI framework that applies to the large frontier developer's
frontier models and describes in detail how the large frontier developer handles
all of the following:

(a) incorporating national standards, international standards, and industry
consensus best practices into its frontier AI framework;

(b) defining and assessing thresholds used by the large frontier developer to
identify and assess whether a frontier model has capabilities that could pose a
catastrophic risk, which may include multiple-tiered thresholds;

(c) applying mitigations to address the potential for catastrophic risks based on
the results of assessments undertaken pursuant to paragraph (b) of this
subdivision;

(d) reviewing assessments and adequacy of mitigations as part of the decision to
deploy a frontier model or use it extensively internally;

(e) using third parties to assess the potential for catastrophic risks and the
effectiveness of mitigations of catastrophic risks;

(f) revisiting and updating the frontier AI framework, including any criteria
that trigger updates and how the large frontier developer determines when its
frontier models are substantially modified enough to require disclosures pursuant
to subdivision three of this section;

(g) cybersecurity practices to secure unreleased model weights from unauthorized
modification or transfer by internal or external parties;

(h) identifying and responding to critical safety incidents;

(i) instituting internal governance practices to ensure implementation of these
processes; and

(j) assessing and managing catastrophic risk resulting from the internal use of
its frontier models, including risks resulting from a frontier model
circumventing oversight mechanisms.

2. (a) A large frontier developer shall review and, as appropriate, update its
frontier AI framework at least once per year.

(b) If a large frontier developer makes a material modification to its frontier
AI framework, the large frontier developer shall clearly and conspicuously
publish the modified frontier AI framework and a justification for that
modification within thirty days.

3. (a) Before, or concurrently with, deploying a new frontier model or a
substantially modified version of an existing frontier model, a frontier
developer shall clearly and conspicuously publish on its internet website a
transparency report containing all of the following:

(i) the internet website of the frontier developer;

(ii) a mechanism that enables a natural person to communicate with the frontier
developer;

(iii) the release date of the frontier model;

(iv) the languages supported by the frontier model;

(v) the modalities of output supported by the frontier model;

(vi) the intended uses of the frontier model; and

(vii) any generally applicable restrictions or conditions on uses of the frontier
model.

(b) Before, or concurrently with, deploying a new frontier model or a
substantially modified version of an existing frontier model, a large frontier
developer shall include in the transparency report required by paragraph (a) of
this subdivision, summaries of all of the following:

(i) assessments of catastrophic risks from the frontier model conducted pursuant
to the large frontier developer's frontier AI framework;

(ii) the results of the assessments under subparagraph (i) of this paragraph;

(iii) the extent to which third-party evaluators were involved; and

(iv) other steps taken to fulfill the requirements of the frontier AI framework
with respect to the frontier model.

(c) A frontier developer that publishes the information described in paragraph
(a) or (b) of this subdivision as part of a larger document, including a system
card or model card, shall be deemed in compliance with the applicable paragraph.

4. (a) (i) A frontier developer shall not make a materially false or misleading
statement about catastrophic risk from its frontier models or its management of
catastrophic risk.

(ii) A large frontier developer shall not make a materially false or misleading
statement about its implementation of, or compliance with, its frontier AI
framework.

(b) This subdivision shall not apply to a statement that was made in good faith
and was reasonable under the circumstances.

5. (a) When a frontier developer publishes documents to comply with this section,
such frontier developer may make redactions to such documents that are necessary
to protect such frontier developer's trade secrets, such frontier developer's
cybersecurity, public safety, or the national security of the United States or to
comply with any federal or state law.

(b) If a frontier developer redacts information in a document pursuant to this
subdivision, such frontier developer shall describe the character and
justification of such redaction in any published version of such document to the
extent permitted by the concerns that justify redaction and shall retain the
unredacted information for five years.

NB Effective January 1, 2027

---

### 3. Illinois — Artificial Intelligence Safety Measures Act, Section 10

*Public Act 104-0538 (SB 315, 104th General Assembly), the Artificial Intelligence
Safety Measures Act; approved July 6, 2026; the Act takes effect January 1, 2027
(Section 99). Reproduced from the enrolled bill as published by the Illinois General
Assembly (ilga.gov/documents/legislation/104/SB/PDF/10400SB0315lv.pdf), retrieved
20 August 2026; the official ILGA publication of P.A. 104-0538 controls.*

Section 10. Frontier AI framework.

(a) Beginning January 1, 2028, a large frontier developer shall write, implement,
comply with, and clearly and conspicuously publish on its website a frontier AI
framework that applies to the large frontier developer's frontier models and
describes how the large frontier developer approaches all of the following:

(1) incorporating national standards, international standards, and
industry-consensus best practices into its frontier AI framework;

(2) defining and assessing thresholds used by the large frontier developer to
identify and assess whether a frontier model has capabilities that could pose a
catastrophic risk, which may include multiple-tiered thresholds;

(3) applying mitigations to address the potential for catastrophic risks based on
the results of assessments undertaken pursuant to paragraph (2);

(4) reviewing assessments and adequacy of mitigations as part of the decision to
deploy a frontier model or use it extensively internally;

(5) using third parties to assess the potential for catastrophic risks and the
effectiveness of mitigations of catastrophic risks;

(6) revisiting and updating the frontier AI framework, including any criteria that
trigger updates and how the large frontier developer determines when its frontier
models are substantially modified enough to require disclosures pursuant to
subsection (c);

(7) cybersecurity practices to secure unreleased model weights from unauthorized
modification or transfer by internal or external parties;

(8) identifying and responding to critical safety incidents;

(9) instituting internal governance practices to ensure implementation of these
processes; and

(10) assessing and managing catastrophic risk resulting from the internal use of
its frontier models, including risks resulting from a frontier model circumventing
oversight mechanisms.

(b)(1) A large frontier developer shall review and, as appropriate, update its
frontier AI framework at least once per year.

(2) If a large frontier developer makes a material modification to its frontier AI
framework, the large frontier developer shall clearly and conspicuously publish on
its website the modified frontier AI framework and a justification for that
modification within 30 days.

(c)(1) Before, or concurrently with, deploying a new frontier model or a
substantially modified version of an existing frontier model, a frontier developer
shall clearly and conspicuously publish on its website a transparency report
containing all of the following:

(A) the website of the frontier developer;

(B) a mechanism that enables a natural person to communicate with the frontier
developer;

(C) the release date of the frontier model;

(D) the languages supported by the frontier model;

(E) the modalities of output supported by the frontier model;

(F) the intended uses of the frontier model; and

(G) any generally applicable restrictions or conditions on uses of the frontier
model.

(2) Before, or concurrently with, deploying a new frontier model or a substantially
modified version of an existing frontier model, a large frontier developer shall
include in the transparency report required by paragraph (1) of this subsection (c)
summaries of all of the following:

(A) assessments of catastrophic risks from the frontier model conducted pursuant to
the large frontier developer's frontier AI framework;

(B) the results of the assessments under subparagraph (A);

(C) the extent to which third-party evaluators were involved; and

(D) other steps taken to fulfill the requirements of the frontier AI framework with
respect to the frontier model.

(3) All summaries required under paragraph (2) shall be provided in a
machine-readable format to facilitate verification of model claims.

(4) A frontier developer that publishes the information described in paragraph (1)
or (2) as part of a larger document, including a system card or model card, shall
be deemed in compliance with the applicable paragraph.

(5) A frontier developer is encouraged, but not required, to make disclosures
described in this subsection (c) that are consistent with, or superior to, industry
best practices.

(d) Beginning on January 1, 2028 or 90 days after a developer first qualifies as a
large frontier developer, whichever is later, a large frontier developer shall
annually retain a third party to perform an independent audit of compliance with
the requirements of this Section. The third party shall conduct audits consistent
with generally accepted auditing standards and best practices and shall possess
demonstrated competence to perform the audit, including experience employing or
contracting with individuals who possess technical expertise in the safety of
frontier models. A large frontier developer shall not retain a third party if
either the large frontier developer or the third party has a financial interest in
the other party. A large frontier developer may compensate a third party for its
services but shall not condition any payment or the amount of any payment on the
results of the third party's audit.

(1) The third party shall be granted access to all materials reasonably necessary
to comply with the third party's obligations under this subsection (d), including,
but not limited to, all unredacted versions of materials published pursuant to this
Act. To protect the frontier developer's trade secrets and confidential business
information, cybersecurity, national security of the United States, or public
safety, a large frontier developer may impose security protocols on the third
party, including, but not limited to, restrictions on note taking, copying,
retaining, or removing materials; requirements for on-premise review; and
confidentiality requirements.

(2) The third party shall produce a report that includes all of the following:

(A) a description of whether the large frontier developer has substantially
complied with the requirements of this Section;

(B) if applicable, a description of material deviations from the requirements of
this Section, an explanation of any deviation and its rationale, and any
recommendations for how the developer can improve its policies and processes for
ensuring compliance with the requirements of this Section;

(C) a detailed assessment of the large frontier developer's internal controls,
including its designation and empowerment of senior personnel responsible for such
implementation by the large frontier developer, its employees, and its contractors;

(D) a list of the personnel involved in the audit;

(E) the third party's procedures for managing conflicts of interest and any
conflicts of interest of any personnel involved in the audit;

(F) the methodology of the audit and the nature of the information reviewed by the
third party to conduct the audit; and

(G) the signature of the lead auditor certifying the results of the audit.

(3) The large frontier developer shall retain an unredacted copy of the report for
as long as a frontier model is deployed plus 5 years.

(4)(A) No later than 30 days after receiving the audit report, the large frontier
developer shall conspicuously publish on its website a high-level summary of the
audit findings and a copy of the third party's report with appropriate redactions
and transmit a copy of the redacted report to the Agency and the Attorney General.

(B) The large frontier developer shall grant the Agency and the Attorney General
access to the third party's report, with redactions, upon request, subject to the
redactions permitted under subsection (g).

(e) A large frontier developer shall transmit to the Agency a summary of any
assessment of catastrophic risk resulting from internal use of its frontier models
every 3 months or pursuant to another reasonable schedule specified by the large
frontier developer and communicated in writing to the Agency and the Attorney
General with written updates, as appropriate and agreed upon by the Agency.

(f)(1) A frontier developer shall not make a materially false or misleading
statement about catastrophic risk from its frontier models or its management of
catastrophic risk.

A large frontier developer shall not make a materially false or misleading
statement about its implementation of, or compliance with, its frontier AI
framework.

(2) This subsection (f) does not apply to a statement that was made in good faith
and was reasonable under the circumstances.

(g)(1) When a frontier developer publishes documents to comply with this Section,
the frontier developer may make redactions to those documents that are necessary to
protect the frontier developer's trade secrets, the frontier developer's
cybersecurity, public safety, or the national security of the United States or to
comply with any federal or State law.

(2) If a frontier developer redacts information in a document pursuant to this
subsection (g), the frontier developer shall describe the character and
justification of the redaction in any published version of the document to the
extent permitted by the concerns that justify redaction and shall retain the
unredacted information for 5 years.

NB Act effective January 1, 2027 (Section 99); subsection (a) operates from
January 1, 2028, and subsection (d) from January 1, 2028 or 90 days after a
developer first qualifies as a large frontier developer, whichever is later.

---

*Retrieved and pinned 19–20 August 2026. Where any text above differs from the
enacting jurisdiction's official publication, the official publication controls,
and a correction here is an erratum for the register.*

---

## Choices for your state

Every bracketed choice in the statute (`model_act_v3_4.txt`, v3.4 tag), with the section it
sits in, the line it sits on, what it governs, what the enacted state family chose where a
sibling exists, and the drafting note that explains the shape. Brackets are an adopting
state's decision, not a gap: the architecture is handed over, the numbers are poured locally.

**How to use it.** Work the table top to bottom; every row is a decision a legislative
counsel's office would make anyway, gathered here so the pass takes one sitting instead of
fourteen. Line numbers are against the v3.4 tag and are stable — cite them as
`model_act_v3_4.txt#L417`. This file closes the mechanical half of READ FIRST item 9 (the
conforming-amendment scaffold); the local-codification half still wants that state's counsel.

**One standing instruction, before the table.** SEC. 3(c)(4)'s pin date — `[1 August 2026]` —
must be set to **a date certain preceding introduction** and must never be drafted as a moving
date. A moving date converts static legislative adoption into dynamic incorporation of another
sovereign's future enactments, which several state constitutions forbid outright and which
would collapse the non-delegation posture the interim-standards bridge rests on (companion
n.24). It is the one bracket in this table that is not a policy choice.

---

### Thresholds and technical floors

| Bracket | § | Line | Governs | Enacted sibling | Note |
|---|---|---|---|---|---|
| `[10^24]` | 1(b)(1) | 58 | Derivations at or below this never extend a lineage | none — this Act's own floor | n.36 |
| `[10^22]` | 1(b)(1) | 60 | The records-duty audit floor, decoupled from coverage | none | n.36 — the commons stays out, the paper trail stays on |
| `[one]` % | 2 | 115 | Percentage limb of the modifiability-evaluation budget | none | n.25; open for review at READ FIRST 6 |
| `[10^24]` | 2 | 116 | Absolute limb of the same budget | none | n.25 — the limbs coincide at the 10^26 line |

### Commencement and clocks

| Bracket | § | Line | Governs | Enacted sibling | Note |
|---|---|---|---|---|---|
| `[180]` days | 3(c)(2) | 173 | Runway before the substantive layer commences | CA ran 94 days from signature | n.24 |
| `[90]` days | 3(c)(3) | 198 | Compliance period after the Agency's standards issue | — | n.24 — fair notice at every joint |
| `[540]` days | 3(c)(3) | 206 | Target for the Agency to propose initial standards | — | Bracketed and unenforceable by design; states may harden it |
| `[1 August 2026]` | 3(c)(4) | 211 | The interim-standards pin date | — | **Set to a date certain preceding introduction. Never a moving date.** n.24 |
| `[90]` days | 12 | 493 | Effective date after enactment | — | — |
| `[180-day]` | 12 | 497 | Transition for systems already deployed | — | — |
| `[30]` days | 9(b) | 407 | Full incident report after preliminary notice | IL and NY both 72h/30d family | n.9, n.27 |
| `[10]` days | 9(b) | 408 | Supplemental reports after new information | 21 C.F.R. § 803.56 pattern | n.9 |
| `[180]` days | 11 | 490 | Agency must act on or decline a credible report | none | n.11 — the mandamus hook |
| `[30]` days | 13(d) | 599 | Deadline to publish a revival order after a federal lapse | — | n.15 |

### Money

| Bracket | § | Line | Governs | Enacted sibling | Note |
|---|---|---|---|---|---|
| `\$[1,000,000]` | 10(a) | 417 | Entity civil penalty, per violation per day | CA § 22757.15(a); NY § 1427; IL § 25(a) — all \$1M, severity-scaled caps | n.19 — the family's own figure |
| `\$[3,000,000]` | 10(a) | 419 | The recidivist step after a prior final adjudication | NY § 1427; IL § 25(a) | n.19 |
| `\$[100,000]` | 10(b) | 428 | Individual fine, base misdemeanor tier | 18 U.S.C. § 3571(b)(5) parity | n.19 — **preserve the twice-gain alternative when conforming to a local fine grid** |
| `\$[250,000]` | 10(c)(1) | 432 | Individual fine, base felony tier | § 3571(b)(3) parity | n.19 — same instruction |
| `\$[1,000,000]` | 10(c)(2)(C) | 437 | Individual fine in the harm tier, per offense | 18 U.S.C. § 1350 | n.19 — counted per victim |
| `\$[1,000,000]` | 11(a) | 481 | Sanctions threshold above which an award is payable | none — SEC's § 21F structure has no state sibling | n.11 |
| `[twelve]` months | 7(a) | 322 | Disgorgement tail after a violation ceases | 17 C.F.R. § 240.10D-1 lookback | n.18 |
| `[twelve]` months | 7(b) | 355 | Conforming window for insurance contracts in force | — | n.33 — the ban is prospective |

### Sentencing

| Bracket | § | Line | Governs | Enacted sibling | Note |
|---|---|---|---|---|---|
| `[felony]` | 10(c)(2) | 434 | Classification of the harm tier | local penal grid | Each state's counsel conforms the class |
| `[two]` years | 10(c)(2)(B) | 436 | Death-results minimum | federal pattern is twenty; this Act declines it | n.21 — **open at READ FIRST 3(c); a criminal-law scholar's question, not a drafting choice** |
| `[forty]` years | 10(c)(3) | 452 | Cap on consecutive determinate terms for one course of conduct | K.S.A. 21-6819(b)(4) double rule | n.21 — sits between the MPC formula and unlimited stacking |
| `[ten]` years | 6(b)(2) | 299 | Recidivist washout | 21 U.S.C. § 333(a)(2) has none | n.22 — more merciful than the source |
| `[10]` days | 10(d)(3) | 468 | Post-deprivation hearing after an emergency suspension | 21 U.S.C. § 332/334 pattern | n.10 |

### Records and limitations

| Bracket | § | Line | Governs | Enacted sibling | Note |
|---|---|---|---|---|---|
| `[ten]` years | 12 | 501 | Baseline records retention from creation | EU AI Act art. 18(1) decade | n.23 |
| `[five]` years | 12 | 501 | Deployment tail after the system last operates in-state | IL § 10(d)(3) "deployed plus 5" | n.23 |
| `[five]` / `[ten]` years | 12 | 519–522 | Limitations: general, continuing, concealed, harm tier | — | n.23 — the harm-tier period keys to an offense, not a penalty schedule |
| `[calendar quarter]` | 8 | 377 | Batch cadence for sub-material certifications | SOX quarterly rhythm | n.39 |

### Institutional placeholders

| Bracket | § | Governs | Note |
|---|---|---|---|
| `[designated state agency, board, or commission]` | 3(a) | The Agency | Name an existing body; the Act is drafted so its inaction cannot stall the criminal core |
| `[the State public-records act]` | 12 | The confidentiality exemption | Conform to the local statute's name |
| `[the State register]` | 13(c) | Where suspension orders publish | Conform to the local publication of record |
| `[Frontier AI Accountability Fund]` | 10(f) | The fund's name and destination | Election: appropriated to the Agency's functions, or reverting to the general fund |
| `[the court of general jurisdiction …]` | 13(c)(4) | Venue for review of a suspension order | Proposed at v3.5, CURE 2 — not yet in the tagged text |

---

**Counts.** Twenty-eight bracketed instances across fourteen sections; roughly twenty distinct
choices once repeats are collapsed. Two are not free choices: the pin date (above) and the
death-results minimum (open for a criminal-law scholar, not for local preference).

*Compiled 20 August 2026 against the v3.4 tag. Where a line number and the text disagree, the
text controls; a wrong line here is an erratum like any other — FrontierAIAccountabilityProject@proton.me.*
