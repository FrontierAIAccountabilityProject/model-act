# What these words mean — a glossary for people who have to legislate about them

> ## Can a model act?
>
> **No. A person does.**
>
> *This project is called a Model Act. The joke is not decoration — it is the entire argument. A
> model is a fitted object: a large set of numbers that turns an input into an output. It does not
> act, decide, choose, want, or answer for anything. **Somebody trains it. Somebody releases it.
> Somebody decides it is ready.** Those are acts, and acts have actors. The statute is named after
> the difference.*

---

## Who this is about

**About:** the officers of frontier developers — companies training models above 10²⁶ operations.

**Not about:** open-source contributors, startups, researchers, deployers or users.

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
| **Frontier model** | **A priced tier.** Defined in every enacted statute by compute — above 10²⁶ operations, or over \$100,000,000 of compute in H.R. 9917. | Not a capability claim. A purchase. See [house language § 6](./house_language.md). |
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

**Hallucination.** Confident false output. **The word is itself an example of what
[house language](./house_language.md) warns about** — hallucination is something a mind does.
*Confabulation* is closer, and *"the system produced a false statement"* is closest, because it
leaves room for the question of who is answerable for it.

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

⚠ *Further entries queued: Margaret Masterman's computational linguistics and computer-generated
poetry at the Cambridge Language Research Unit, and Alison Knowles's* House of Dust *(1967). Both
to be pinned before publication.*

---

## And back to the pun, because it is the whole thing

A **model** is a fitted object. An **act** is something done by someone.

Every enacted frontier statute in America regulates the first and never reaches the second. This
one is named for the gap between them.

**A model cannot act. A person does. The question this project asks a legislature is only: which
one?**

---

*Corrections to the project contact — especially from people who build these systems. They enter
[the errata register](../ledger/errata.md) with the fix attached and permanent credit.*
