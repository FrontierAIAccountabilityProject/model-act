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
(SEC. 2(b)). See [the case](../docs/the_case.md#who-this-is-about).*

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
| **Generative AI** | Models producing new output — text, images, audio, video — resembling their training data. | The category FDA's [August 2026 docket](../filings/frontier_ai_in_medicine.md) is about. |
| **Foundation model** | A large model trained broadly and intended to be adapted to many uses. | The nearest thing to a technically honest term for what this Act covers. |
| **Frontier model** | **A priced tier.** Defined in every enacted statute by compute — above 10²⁶ operations, or over \$100,000,000 of compute in H.R. 9917. | Not a capability claim. A purchase. See [house language § 7](./house_language.md). |
| **General-purpose AI** | The EU's term for the same family, with a systemic-risk presumption above 10²⁵ FLOP. | Useful for comparative drafting. |
| **Narrow / task-specific model** | A model trained for one job — reading a mammogram, flagging a transaction. | **Most FDA-authorised AI devices are these, not frontier models.** Conflating them is the commonest error in this debate. |
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
aspiration and a fundraising term**, and a drafter should treat it as unusable in statutory text.

**Alignment.** Making a system's outputs match what its developers intend. Note the word: *intend*.
**Alignment is defined relative to the developer's goals**, not the public's — which is precisely
why it is a matter for a legislature and not only for engineers.

**Emergent — and "malicious, emergent."** In the technical literature, *emergent* describes a
capability that appears at scale without having been individually engineered — nobody wrote the
rule; the fitted numbers turned out to contain the behaviour. The literature itself disputes how
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

## The legal words, since half the confusion runs the other way

**Mens rea** — *the guilty mind.* The mental element a crime requires: intent, knowledge,
recklessness, or negligence. Most serious offences need one.

**A model cannot have it.** Not as a matter of philosophy but as a matter of law: mens rea is a
state of a person, and there is no legal machinery for attributing one to a fitted function. **This
is the sharpest reason the duty must attach to a human being** — not because machines are innocent,
but because the concept does not apply to them, and a statute that pretended otherwise would be
unenforceable on its first day.

**Which is exactly what the public-welfare doctrine is for.** *Morissette* (1952) marks out a
category of offence where the traditional mens rea requirement is relaxed because the conduct is
regulatory and the danger is public. *Dotterweich* (1943) and *Park* (1975) place the resulting duty
on **the person standing in responsible relation to the conduct** — and the floor is **negligence**,
not knowledge. See [the table of authorities](./table_of_authorities.md).

**So the sequence runs:** the system has no mind → the law cannot ask it for one → the question
becomes *which person had the authority to prevent this, and did they take due care?* **That is a
question about a human being, and it is answerable.**

**Strict liability** — an offence needing no mental element at all. Rarer than people think, and
already applied to individuals: 21 U.S.C. § 333(a)(1) makes shipping an adulterated article a
federal crime with no intent requirement whatsoever. *See [already a crime, if you are a
person](./already_a_crime_for_you.md).*

**Responsible corporate officer doctrine** — the rule that an officer with authority to prevent or
correct a violation answers personally for failing to. Eighty years old, never extended past the
food-and-drug frontier.

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
| **Authority** | The **power to bind** the principal, limited to what was actually or impliedly conferred; acting beyond it is itself a wrong (Restatement (Third) of Agency § 2.02). | No native concept. The nearest analogue is a **permission** — what a token or credential technically allows. | "Capability isn't authority" (Akhtar, 2026); "does this action have explicit authority to execute?" (Bucko08, on the Hugging Face forensic post, 2026). A system can be **capable** of an act it was never **authorised** to take. Harm lives in that gap. |
| **Capability** | No settled term; the doctrinal analogue is the **"power to prevent"** the violation (*Park*, 1975). | What a model can do, measured by evaluation — deliberately, with **"safeguards disabled … to measure the capability boundary"** (ExploitGym, arXiv:2606.11086, 2026). | The **same** capability is safe or catastrophic depending on a human's deployment choice: one frontier model was **blocked 88.2 % of the time with safeguards on, and produced working exploits with them off**. The decision, not the capability, carries the duty. |
| **Safeguard / guardrail** | The analogue of the **duty of care** — liability turns on "whether reasonable mitigation steps were taken" (RAND, 2026). | Trained refusals, classifiers, sandboxing and monitoring that constrain a model — **and can be switched off** ("deliberately disabled OpenAI's production safety classifiers," Hugging Face, 2026). | Because a person can turn them off, their presence is not a defence and their **removal is an act with an author**. The Act reaches the act. |
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
next-token prediction possible at all. And a **Wittgensteinian scepticism about whether any limited
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
[the errata register](../ledger/errata.md) with the fix attached and permanent credit.*
