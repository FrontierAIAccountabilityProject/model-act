# The frontier bill census — every frontier AI bill in America, read

*Companion to [the adopted texts](./interim_standards.md), which pins what the enacted statutes
say; to [the commentary sweep](./commentary_sweep.md), which asks whether anyone writing about
them has noticed; and to [the sponsors' file](./for_legislators.md), which states the finding
these rows are evidence for. Terms used here follow [the house language rule](./house_language.md).*

*The question: **does it reach a natural person?** Not the company — a human being who can be
named, who owes a duty, who signs something, or who answers personally when it goes wrong.*

*Status: **in progress.** Every row below is either **read** and answered, or marked
**⚠ unverified** and answered by nobody. No row is filled by inference, and no total is claimed
until the rows support it.*

---

## The method, stated so anyone can re-run it

For each bill, three steps and a verdict.

**Step 1 — pin the bill.** Primary source only: the state legislature's own system, or
LegiScan's copy of the enrolled text. Not a tracker, not a law-firm alert, not a summary. Record
the bill number **as the official record gives it**, the session, the current status and the
date checked. Commercial trackers are used to *find* bills, never to describe them — the
tracker that produced this list reported at least three bills twice and gave two state counts
that did not match its own lists.

**Step 2 — run the word test.** Search the bill text for each of:

> *natural person · individual · officer · director · executive · personally · certify ·
> certification · attest · signature · sign · criminal · misdemeanor · felony · imprison ·
> responsible corporate officer · knowingly · wilful/willful*

Record **hits and their context**, not just counts. A hit on "officer" that turns out to be
"peace officer" or "the Attorney General or their officer" is not a hit on the question — say
so in the row rather than letting the count carry a false positive.

**Step 3 — answer four questions.**

1. **Who owes the duty?** Entity, individual, or both.
2. **Does any named human sign anything?** If yes, who, and under what penalty for signing
   falsely.
3. **Who pays?** Civil penalty from the corporate treasury, personal liability, or both.
4. **Is there criminal exposure, and does it stop at the entity?**

**The verdict line.** One sentence, written so it could be quoted. This is the part that makes
the census readable rather than a spreadsheet: each bill gets a sentence that says what it
chose to do about the person.

---

## The tally

*Updated as rows are completed. This is the only place a total appears, and it never exceeds
the number of rows actually read.*

| | Count |
|---|---|
| Frontier bills identified (⚠ tracker figure, duplicates suspected) | ~34, across 10 states + federal |
| **Read and answered** | **4** (H.R. 9917, Connecticut SB 5, Idaho S 1297, Nebraska LB 525) |
| Of those read: reaching a natural person **as an officer of a developer** | **0** |
| Of those read: naming officers and directors in the operative text | **1** (Connecticut, as recipients of a report — no duty attaches) |
| Of those read: requiring a human signature | **0** |
| Of those read: any criminal liability at all, entity or person | **0** |
| Of those read: **actually frontier bills** | **2 of 4** — two were chatbot statutes miscategorised by the tracker |
| Highest penalty found | **\$20,000,000 per day** (H.R. 9917), payable by the company |

---

## The entry template

*Copy this block for each bill.*

```
### [STATE] — [BILL NO.] — [short title]

**Status:** [introduced / in committee / passed one chamber / passed both / enacted / dead]
· **Session:** [ ] · **Checked:** [date] · **Source:** [primary URL]

**Word test.** [terms hit, with context — and the false positives named as false positives]

**Who owes the duty.** [ ]
**Does a human sign?** [ ]
**Who pays.** [ ]
**Criminal exposure.** [ ]

**Verdict.** [one quotable sentence]

**Confidence.** [grade — see the rubric below]
```

### The confidence rubric, governed by E15

[E15](../LEDGER.md#part-i) fixed what ✅ means for this project: **a ✅ requires that this project
opened the source, not merely that a first party wrote it.** A census of statutes needs one
further distinction, because there are two different ways a row can fall short, and collapsing
them hides which fix is owed.

| Grade | Meaning | The fix owed |
|---|---|---|
| ✅ | The enrolled or introduced text was opened **and read by a human eye** | none |
| ⚠ **R** | The primary **was opened**, but read through automated retrieval — a summarising model stood between the text and the row | a human re-read; the locator is already in hand |
| ⚠ **F** | The primary **was not opened**; the row rests on a secondary quoting it | a fetch, and the fetchable locator is named in the row |
| ⚠ **P** | Read in part — some sections opened, others not | name which sections |

**Every row in this file currently carries ⚠ R**, and that is the honest grade rather than a
modest one: [E13](../LEDGER.md#part-i) records automated retrieval nearly putting a false
correction into the evidence file, and [E14](../LEDGER.md#part-i) records two primary sources
conflicting where a single fetch had reported certainty. Nothing here is quoted in a filing, a
post or a sponsor package until a human has read the enrolled text.

---

## The worked example — what a completed row looks like

### ILLINOIS — P.A. 104-0538 — Artificial Intelligence Safety Measures Act

**Status:** enacted · **Session:** 2026 · **Checked:** 20 Aug 2026 · **Source:** enrolled bill,
pinned verbatim at [the adopted texts](./interim_standards.md)

**Word test.** *Signature* hits — **and this is the finding**: the Act requires "the signature
of the lead auditor certifying the results." *Officer* does not appear in the sense of a
corporate officer owing a duty. No *natural person*, no *personally*, no *certify* by a
developer's executive.

**Who owes the duty.** The frontier developer, as an entity.
**Does a human sign?** **Yes — the auditor.** The outside contractor hired to inspect the work
signs; nobody inside the developer does.
**Who pays.** The entity: civil penalties not exceeding \$1,000,000 for a first violation,
\$3,000,000 for subsequent, enforced exclusively by the Attorney General, no private right of
action.
**Criminal exposure.** None reaching a natural person.

**Verdict.** *Illinois knows how to require a named human signature — and asks it of the
inspector rather than the officer who decides to ship.*

**Confidence. Split, and the split is the point of the rubric.** The statute itself is **✅** —
pinned verbatim at the adopted texts. The auditor-signature line is **⚠ F**: it is quoted from a
law-firm alert, and the enrolled text has not been opened for that sentence. It is also the most
quoted line in this whole file, which is exactly why it carries the weaker of the two grades
until someone fetches it.

---

## The rows

### FEDERAL — H.R. 9917 — AI Kill Switch Act

**Status:** introduced 23 July 2026, 119th Congress · **Sponsors:** Rep. Ted W. Lieu (D, Los
Angeles County) and Rep. **Nathaniel** Moran (R, Texas) — **both Representatives**; this is not
the Senator of the same surname · **Checked:** 21 Aug 2026 · **Source:** bill text as published
by the lead sponsor's office; press release of the same date

**Word test.** *Officer*, *director*, *executive*, *natural person*, *personally*, *certify*,
*certification*, *attest*, *criminal*, *misdemeanor*, *felony*, *imprison*, *knowingly*,
*willful*, *responsible corporate officer* — **every one absent.** *Individual* — one hit, and it
is the victim, not the duty-holder: a covered incident includes an occurrence that *"causes the
death of not fewer than 10 individuals."* *Signature* — **one hit in the entire bill**, and it is
the line *"(Original Signature of Member)"* on the introduction page.

**Who owes the duty.** The covered entity. The bill does not use the term "covered developer" at
all; its central defined object is **"covered technology"** — the system, not the maker and not
the person. Duties run to maintaining the technical capability to throttle, suspend or shut down,
to incident reporting, and to preserving weights and telemetry on a Homeland Security order.

**Does a human sign?** No.

**Who pays.** The entity, and heavily: a civil penalty of up to **\$2,000,000 for each day** a
violation occurs, rising to **\$20,000,000 for each day** for violations of subsection (c) — the
emergency-order provision requiring preservation of model weights and telemetry, notification of
operators and users so far as practicable, and confirmation of compliance.

**Criminal exposure.** **None at all** — not against a person, and not against the entity either.
This is the largest money penalty in the census attached to the smallest personal consequence.

**Verdict.** *The AI Kill Switch Act requires every covered developer to build a brake, tells
nobody who must pull it, and the only human signature it requires anywhere is the sponsor's own
on the front page.*

**The threshold, and why it is a drafting argument** — the general form of the point is at
[house language § 6](./house_language.md), which sets out what every frontier definition in force
actually measures.
 Covered technology is defined by **the cost
of the compute**: a system *"developed utilizing a quantity of computing power the cost of which
would exceed \$100,000,000 at the prevailing market price."* Every state frontier statute read so
far uses **operations** — ten to the twenty-sixth. A dollar-denominated threshold moves with the
market it measures: the same training run falls out of coverage as compute gets cheaper, with no
legislature voting on anything. An operations threshold is a physical quantity and stays put. This
is a comparison the census can make because it read both, and it is offered as drafting
observation, not criticism of a bill whose central instinct — that someone must be able to stop
the thing — this project shares.

**The carve-out, stated exactly.** The exclusion for testing is **definitional, and sits at the
opening of the definition it governs.** A "covered incident" means an occurrence of the listed
harms *"outside of red-teaming or other structured testing"*; a "loss-of-control scenario"
likewise means one in which a covered technology pursues, *"outside of red-teaming or other
structured testing,"* an unintended goal. Red-teaming is itself defined at (g)(8) as structured
testing that is controlled, simulates real conditions and uses adversarial methods. The effect is
not an exemption a developer must plead — the event is simply not a covered incident. **⚠ Open
question, not a finding:** the project's own case studies are demonstrations conducted under
structured conditions. Whether each of them would fall inside this carve-out has **not been
checked**, and the census will not say that it does until every case study has been read against
the (g)(8) definition one at a time. That check is in the queue below.

**Confidence. ⚠ R.** The sponsor's published bill text was opened directly — not a secondary
quoting it — and the threshold, the penalty tiers and the placement of the carve-out were each
confirmed on a second pass. It has not been read by a human eye. Congress.gov could not be
retrieved (robots), so cosponsor count and committee referral are **unrecorded, not zero**.

*This row closes a queue item.* [E15](../LEDGER.md#part-i) listed "the AI Kill Switch Act's
thresholds, penalties, and red-teaming carve-out" as ⚠ pending fetch with no primary opened. The
primary is now open and the three items are answered — at ⚠ R, not ✅, because opening a document
through a summarising model is not the same as reading it.

---

### CONNECTICUT — SB 5 (P.A. 26-15) — An Act Concerning Online Safety

**Status:** **enacted**, signed 27 May 2026; whistleblower provisions effective 1 Oct 2026, the
internal reporting process required by 1 Jan 2027 · **Session:** 2026 · **Checked:** 21 Aug 2026
· **Source:** chaptered text, LegiScan copy of the enrolled act

**Word test.** *Officer* — **hit, and it is the most important hit in the census so far.**
*Director* — hit, same clause. *Frontier* — hit; this is a genuine frontier statute, with the
familiar threshold: a frontier developer is one training a foundation model using *"a quantity
of computing power that is greater than ten to the twenty-sixth power integer or floating-point
operations"*, and a **large** frontier developer adds annual gross revenues over \$500,000,000.
*Certification* — hit, but a **false positive** on our question: it is an employee's
certification to an employer in the employment-discrimination section, not a developer's
attestation. *Natural person*, *personally*, *attest*, *signature*, *criminal*, *misdemeanor*,
*felony*, *imprison*, *knowingly*, *wilful* — **all absent.**

**Who owes the duty.** The frontier developer, as an entity. Large frontier developers must
establish a channel for covered employees to submit anonymous reports of catastrophic risk,
update the reporting employee, and notify employees of their rights.

**Does a human sign?** No. But something new happens: **named corporate roles appear in the
operative text as recipients.** Section 2(c)(2)(A): *"Each report submitted… and each reasonable
update provided… shall be shared with the officers and directors of the large frontier developer
at least quarterly."* And a carve-out that shows the drafters were thinking about those people
as potential wrongdoers: where a covered employee alleges wrongdoing by an officer or director,
neither the report nor any update is shared with that officer or director.

**Who pays.** The entity. Civil penalty **not exceeding \$1,000 per violation**, Attorney General
only, no private right of action. (Other sections of the Act route violations through the
unfair-trade-practices statute, again AG-enforced, again no private right.)

**Criminal exposure.** None, at the entity or anywhere else.

**Verdict.** *Connecticut is the first American statute to put catastrophic-risk reports into a
named officer's hands every quarter — and the only thing it asks that officer to do with them is
receive them.*

**Why this row matters more than its penalty.** The *Park* formula is authority, knowledge, and
failure to act. Connecticut has now legislated the knowledge: quarterly, in writing, to officers
and directors by name of office. It attaches no duty to that knowledge, no response obligation,
no signature and no liability — the whole enforcement weight remains a \$1,000 corporate penalty.
This is not a counter-example to the project's finding. It is the closest a legislature has come
to the vacancy, and it stops one clause short.

**Confidence. ⚠ R + P.** The chaptered PDF was opened, and read **in part**: Section 2 and the
enforcement provisions, not the whole Act, which also carries employment, healthcare and
online-safety titles this row does not speak to. The officers-and-directors clause and the
compute threshold were each confirmed against a second independent source. Per
[E13](../LEDGER.md#part-i), the quoted clause must be re-read by a human against the enrolled act
before it is used in any public claim, post or filing — **and this is the row most likely to be
quoted, so it is the row that most needs it.**

---

### IDAHO — S 1297 — Conversational AI Safety Act

**Status:** **enacted**, signed 31 Mar 2026, Session Law ch. 249; effective **1 July 2027** ·
**Session:** 2026 · **Checked:** 21 Aug 2026 · **Source:** engrossed/enrolled text, Idaho
Legislature

**First finding: this is not a frontier bill.** It regulates public-facing chatbots. *Frontier*,
*compute* and *training* do not appear anywhere in it. It was on the tracker's frontier list; it
does not belong there, and the census records that rather than quietly dropping the row.

**Word test.** *Natural person* — hit, in the definition, and the definition is the finding:
*"'Individual' means a natural person or legal entity."* *Knowingly* — hit: *"An operator shall
not knowingly and intentionally cause or program…"* *Officer*, *director*, *executive*,
*personally*, *certify*, *certification*, *attest*, *signature*, *sign*, *criminal*,
*misdemeanor*, *felony*, *imprison*, *willful* — **all absent.**

**Who owes the duty.** The operator: *"a person who develops and makes available a conversational
AI service to the public."* Note **develops *and* makes available** — Idaho requires both.

**Does a human sign?** No.

**Who pays.** The operator. *"[C]ivil penalties of one thousand dollars (\$1,000) per violation,
not to exceed five hundred thousand dollars (\$500,000) per operator, or actual damages,
whichever is greater"*, sought by the Attorney General, no private right of action.

**Criminal exposure.** None.

**And the provision that runs the wrong way.** *"This chapter shall not create liability for the
developer of an AI model for any violation of this chapter by an AI system developed by a third
party to provide a conversational AI service."* Idaho did not merely omit upstream
accountability. It **legislated the exclusion**, in terms, in an enacted statute.

**Verdict.** *The one time Idaho writes "natural person" it is to fold the human into the
company, and the one time it mentions the model developer it is to say they are not liable.*

**Confidence. ⚠ R.** The legislature's own PDF was opened; quotations verified on a second pass
against that same primary. Not yet read by a human eye.

---

### NEBRASKA — LB 525 — Agricultural Data Privacy Act **and** Conversational Artificial Intelligence Safety Act

**Status:** **enacted**, approved by the Governor 14 Apr 2026 · **Session:** 109th Legislature ·
**Checked:** 21 Aug 2026 · **Source:** slip law, Nebraska Legislature

**Also not a frontier bill.** *Frontier*, *compute* and *training* are absent. Same tracker
error as Idaho, and the pairing with an agricultural-data statute in one vehicle is a further
sign the list was assembled by keyword.

**Word test.** *Natural person* — hit, twice, and the pair is worth reading together: *"Individual
means a natural person"* (§ 13(3)) and *"Person means a natural person or legal entity"*
(§ 13(7)). *Knowingly* — hit, in the same prohibition Idaho uses. *Officer*, *director*,
*executive*, *personally*, *certify*, *certification*, *attest*, *signature*, *sign*, *criminal*,
*misdemeanor*, *felony*, *imprison*, *willful* — **all absent.**

**Who owes the duty.** The operator: *"a person who makes available a conversational artificial
intelligence service to the public"* (§ 13(6)). Because "person" includes a natural person, a
sole operator **is** reachable in his own name — so Nebraska does reach a natural person, but
only the smallest one in the chain. The individual it can find is the man running a chatbot from
a bedroom; the officer of a company training a foundation model is not in the statute at all.

**Does a human sign?** No.

**Who pays.** The operator. *"Civil penalties of at least one thousand dollars per violation, but
in no event more than five hundred thousand dollars per operator"*, plus actual damages,
equitable relief, and costs and fees; Attorney General enforcement — **notably on behalf of the
State "or on behalf of any person aggrieved"**, though the Act expressly creates no private right
of action.

**Criminal exposure.** None.

**Verdict.** *Nebraska's law can reach a natural person — the one operating the chatbot alone,
never the one who built the model it runs on.*

**Confidence. ⚠ R.** The legislature's own slip-law PDF was opened. Not yet read by a human eye.

---

## What the first three rows establish

**One.** Two of the three bills a commercial tracker classified as frontier legislation are
chatbot statutes with no frontier provision in them. Any count of "frontier AI bills" drawn from
that list is wrong before anyone reads a word, which is why this census exists.

**Two.** All three converge on the same architecture the enacted family already showed:
Attorney-General-only enforcement, no private right of action, penalties in the same range, paid
by the entity. Three legislatures, three drafting teams, one shape.

**Three, and this is the one to carry.** Connecticut has now written *officers and directors*
into a frontier statute, and given them quarterly reports of catastrophic risk. What it did not
write is the next sentence.

**Four.** Penalty size and personal reach are not the same axis and do not move together.
H.R. 9917 carries the largest number in the census — twenty million dollars a day — and the least
personal consequence of any bill read: no officer, no signature, no criminal provision at all.
A legislature can raise the price of a corporate failure indefinitely without ever naming a
human being, and this bill is the clearest demonstration of it yet found.

---

## The queue

*Bill numbers **as reported by a commercial tracker on 21 August 2026** — every one needs
confirming against the official record, and the duplicates flagged below are the tracker's, not
the legislature's.*

**First, because they are potential counter-examples to the project's central finding and appear
nowhere in this repository:**

- [x] **Idaho — S 1297** — done. *Enacted, and not a frontier bill.*
- [x] **Nebraska — LB 525** — done. *Enacted, and not a frontier bill.*
- [x] **Connecticut — SB 5** — done. *Enacted; a real frontier statute, and it names officers.*

- [x] **Federal — H.R. 9917** — done. *The AI Kill Switch Act. Introduced 23 July 2026 and absent
  from the tracker's federal list entirely — a fifth reason not to trust that list.*

**Raised by the H.R. 9917 row, and owed before any of it is published:**

- [ ] **Read each of the project's case studies against the (g)(8) definition of red-teaming** —
  controlled, simulating real conditions, adversarial methods — and record, one by one, whether
  the incident would be a "covered incident" under H.R. 9917. If the answer is no for a case
  study, say so for that case study. **No aggregate claim ("it would exempt all of them") is to
  be made until every one has been checked individually**, and if the answers differ the finding
  is the difference, not the headline.

**Then the enacted three, to confirm what the project already believes:**

- [x] Illinois — P.A. 104-0538 *(worked example above; auditor line still ⚠)*
- [ ] **California — SB 53** *Transparency in Frontier Artificial Intelligence Act*
- [ ] **New York — S 6953-B** *RAISE Act*

**Then the rest, by state.** ⚠ *Counts below are the tracker's and are known to be unreliable:
California and Illinois each had a bill listed twice, New York's list showed seven bills under a
count of eight, and the federal row named six numbers under a count of five.*

- **California** — AB 2653 *(listed twice by the tracker)*
- **Illinois** — HB 3506 · HB 4705 · SB 3261 · HB 4799 *(listed twice)* · SB 3444 · SB 3312
- **Maryland** — HB 1399 · HB 1477
- **Minnesota** — HF 4532
- **New Jersey** — AR 158 · SR 121 · SR 52 *(resolutions, not statutes — check whether they
  belong in a bill census at all)*
- **New York** — A 07278 · A 06453 · A 10583 · S 10373 · S 10456
- **Federal** — H.R. 3460 · H.R. 5315 · H.R. 3434 · H.R. 8094 · S. 1792 · S. 1775, plus
  **H.R. 9925** *(the FRONTIER Act, tracked in [the standing watch](../audit/standing_watch_2026-08-20.md)
  and apparently absent from the tracker's federal list — which is itself a reason not to trust
  the list)*

---

## What this census is for, and what it is not

**For:** answering, with a number that can be checked, how much of American frontier-AI
legislation reaches a human being. If the answer stays at zero across every bill read, that is
the strongest version of this project's central claim — and unlike an argument, it is a finding
anyone can falsify by producing one bill.

**Not for:** a league table, a scorecard of legislators, or a claim about bills nobody has read.
The tally above never exceeds the rows completed, and a bill that reaches a natural person would
be the most valuable entry in the file, not an inconvenience.

*Corrections to the project contact; they enter [the errata register](../LEDGER.md#part-i) with
the fix attached and permanent credit.*
