---
title: "What these words mean — a glossary for people who have to legislate about them"
parent: Authorities
nav_order: 2
---

# What these words mean — a glossary for people who have to legislate about them

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

## Who this is about

**About:** the officers of frontier developers — companies training models above 10²⁶ operations.

**Not about:** open-source contributors, startups, researchers, ordinary deployers and API
customers, or users. *A deployer is a defined class under the Act and always has been
(SEC. 1(b)(3)); what the thin ones get is a route to discharge the duty, not an exemption from it
(SEC. 2(b)). See [the case](../commentary/the-case.md#who-this-is-about).*

**And what this file is not.** Not a technical authority. It is a legislator's glossary, written so
that someone drafting a definition knows which word does what. **Where the honest answer is
contested, it says so.** Corrections from people who build these systems are the most valuable
thing anyone could send.

---

## Why a glossary belongs in a statutory project

Every enacted frontier statute defines its scope by **compute** — 10²⁶ operations — rather than by
what a system is or does.

That is not laziness. It is what happens when nobody can agree on the nouns. A threshold you can
measure is safer to draft than a capability you cannot define.

**But it means the words below are doing legislative work while remaining undefined in law**, and a
member asked to vote on "AI" is being asked to vote on a word that covers a spam filter and a
frontier model equally.

---

## The core terms

| Word | What it literally is | What it can actually do | How it is sold |
|---|---|---|---|
| **Algorithm** | A fixed sequence of steps, written by a person. Older than computers — long division is one. | Exactly what its author specified, every time, checkably. | *"The algorithm decided"* — a phrase that hides the author. Somebody wrote the steps. |
| **Model** | A set of numbers plus a function that maps an input to an output. The word is borrowed from statistics: a model **of** something, like a line of best fit. | Produce an output for an input. Nothing else. | As an entity with views, intentions and a personality. |
| **Parameters / weights** | The numbers. Modern frontier models have hundreds of billions of them. | Nothing on their own — they are the fitted state. | As a proxy for capability, though the count alone tells you little. |
| **Training** | The process of adjusting those numbers so outputs better match the data. **A person starts it, on hardware someone pays for, at a cost that can be stated in dollars.** | Produce a fitted model. | As something that *happens* — "the model learned" — rather than something a company does. |
| **Inference** | Running the fitted model on new input. What happens when you type a question. | Produce output. | Rarely named at all in public discussion. |
| **Neural network** | A particular shape of mathematical function, arranged in layers. The biological name is an analogy from the 1940s and has misled people ever since. | Approximate very complicated functions, given enough data and compute. | As a brain. It is not one. |

---

## The category words, which decide what a law covers

| Word | What it means | Note for a drafter |
|---|---|---|
| **Machine learning (ML)** | Fitting a model to data rather than writing the rules by hand. | Covers almost everything, including spam filters and credit scoring. Too broad to be a statutory hook. |
| **AI** | No settled technical meaning. In practice: whatever is currently impressive. | **The least useful word in the debate.** A statute using it without definition covers everything and nothing. |
| **Language model** | A model trained to predict the next piece of text. | Precise and useful. |
| **Large language model (LLM)** | The same, at scale. | "Large" is undefined and moves every year. |
| **Generative AI** | Models producing new output — text, images, audio, video — resembling their training data. | The category FDA's [August 2026 docket](../filed-comments/frontier-ai-in-medicine.md) is about. |
| **Foundation model** | A large model trained broadly and intended to be adapted to many uses. | The nearest thing to a technically honest term for what this Act covers. |
| **Frontier model** | **A priced tier.** Defined in every enacted statute by compute — above 10²⁶ operations, or over \$100,000,000 of compute in H.R. 9917. | Not a capability claim. A purchase. See [house language § 7](./house-style.md). |
| **General-purpose AI** | The EU's term for the same family, with a systemic-risk presumption above 10²⁵ FLOP. | Useful for comparative drafting. |
| **Narrow / task-specific model** | A model trained for one job — reading a mammogram, flagging a transaction. | **Most FDA-authorized AI devices are these, not frontier models.** Conflating them is the commonest error in this debate. |
| **AI-enabled medical device** | A regulated device incorporating any of the above. | A regulatory category, not a technical one. |

---

## The words that carry the most freight

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
([the record](../appendix/press-corpus.md)). Read the two adjectives together:
*malicious* locates a mind in the system — which the legal words below explain no statute can
reach — and *emergent* removes the person from the origin. The pairing concedes the harm while
placing both intent and authorship beyond anyone the law could name. The front page's answer is
the right one for a drafter: in 2010, nobody asked whether the salmonella was an emergent ecology.
Emergence describes the system. Training, evaluating, releasing, and deploying are acts — and acts
have actors.

**Hallucination.** Confident false output. **The word is itself an example of what
[house language](./house-style.md) warns about** — hallucination is something a mind does.
*Confabulation* is closer, and *"the system produced a false statement"* is closest, because it
leaves room for the question of who is answerable for it.

**Machine intelligence.** The field's oldest name for itself — the term of Turing's generation,
older than *artificial intelligence* — and, like "AI" in the table above, a phrase with no
statutory definition anywhere. In current use it is a register rather than a category: *"digital
ecologies of machine intelligence"* ([the record](../appendix/press-corpus.md))
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

## The legal words, since half the confusion runs the other way

**Disposition.** A reviewer's determination of a question they took, published as written. Borrowed
from the judicial sense, where a review is how a matter is finally determined rather than
merely discussed. In this project it means: the reviewer decides, the maintainer publishes without
editing and may only respond beside it, and the finding stands under the reviewer's name or
anonymously at their election. It is not advice, not a consultation, and never an endorsement. The
rules of publication, fixed before the first one arrived, are at
[the reviews register](../revision/reviews-received.md).

**Lane, and reviewer.** A *topic* is a subject area of the review: criminal law, enforcement, frontier
security, fiscal, federalism, proportionality, torts and design, open source and academia. A *reviewer*
is the position a reviewer occupies in a topic. Lanes run in parallel and no topic waits on another;
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
not knowledge. See [the table of authorities](./table-of-authorities.md).

**So the sequence runs:** the system has no mind → the law cannot ask it for one → the question
becomes *which person had the authority to prevent this, and did they take due care?* **That is a
question about a human being, and it is answerable.**

**Strict liability** — an offense needing no mental element at all. Rarer than people think, and
already applied to individuals: 21 U.S.C. § 333(a)(1) makes shipping an adulterated article a
federal crime with no intent requirement whatsoever. *See [already a crime, if you are a
person](../commentary/already-a-crime.md).*

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
[E42](../corrections/corrections.md#e42--the-doctrine-was-said-never-to-have-left-food-and-drug-it-left-decades-ago-by-act-of-congress).

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
([E67](../corrections/corrections.md)). ⚠ 856 stays the secondary source's — no star pagination
([E47](../corrections/corrections.md)).

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
working where the tool does not reach ([E67](../corrections/corrections.md)).

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
and its next sentence widens it** ([E73](../corrections/corrections.md)): "if someone refuses to investigate an
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
([E65](../corrections/corrections.md)). And the ordering above is not a narrowing sequence: *Cincotta*'s
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
[Amendment 22](../revision/proposals.md) proposes to correct by writing the codified federal form
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
"in my opinion" and the confinement to claims predicated on ignorance ([E68](../corrections/corrections.md));
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
design reviewer is asked which.

⚠ **Read-status.** Every quotation in these three entries is taken from a retrieval reply, not from
the reporters or the Delaware Code. **They are unverified**, they are on the retrieval list, and
under E22 no outreach may describe them as checked until the primaries are read.

---

## The two columns — the same word in law and in the machine

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
person who answers ([OPC, PIPEDA report #2026-004](../appendix/press-corpus.md)). A
developer uses it and means a mailbox. When the same word can name both a **duty with a consequence**
and an **email address**, the word has stopped doing legislative work — and the statute has to say
which one it means. **This one means the first.**

*Legal senses cite the Restatement (Third) of Agency and the authorities in
[the table of authorities](./table-of-authorities.md); the machine-side quotations are drawn,
graded, from the [press corpus](../appendix/press-corpus.md) and the project's
source intake. ⚠ The developer and community quotations are recorded as public statements and are
not endorsements.*

---

## What these systems have genuinely done, stated fairly

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

## The lineage — because none of this is as new as it sounds

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
[house language](./house-style.md) and the reason this glossary exists.

*Sources: [Margaret Masterman](https://en.wikipedia.org/wiki/Margaret_Masterman);
[A House of Dust](https://eastofborneo.org/archives/a-house-of-dust-alison-knowles-and-james-tenney-1967/).
⚠ **R** — secondary sources, opened but not corroborated against primary material.*

---

## And back to the pun, because it is the whole thing

A **model** is a fitted object. An **act**, in the sense a statute uses the word, is something done
by a person who can be held to it.

Every enacted frontier statute in America regulates the first and never reaches the second. This
one is named for the gap between them.

**Whether a model acts in some other sense is a real question, and this project takes no position
on it.** It does not have to. **In the only sense a criminal statute can operate in, the acts belong
to people — and the question this project puts to a legislature is only: which ones?**

---

*Corrections to the project contact — especially from people who build these systems. They enter
[the the corrections register](../corrections/corrections.md) with the fix attached and permanent credit.*
