# The frontier bill census — every frontier AI bill in America, read

*Companion to [the adopted texts](./interim_standards.md), which pins what the enacted statutes
say; to [the commentary sweep](./commentary_sweep.md), which asks whether anyone writing about
them has noticed; and to [the sponsors' file](./for_legislators.md), which states the finding
these rows are evidence for. Terms used here follow [the house language rule](./house_language.md).*

*The question: **does it reach the officer of a frontier developer?** Not the company, and not
just any human being — the person inside a covered developer who decides that a system ships, and
who could be named, could owe a duty, could sign something, and could answer personally when it
goes wrong.*

*Status: **in progress.** Every row below is either **read** and answered, or marked
**⚠ unverified** and answered by nobody. No row is filled by inference, and no total is claimed
until the rows support it.*


---

## Who this is about, and who it is not

**About:** the **officers of frontier developers** — the small number of companies training models
above 10²⁶ operations, or spending nine figures on a single training run. On the enacted family's
own thresholds that is a **double-digit number of firms worldwide**, and inside them a smaller
number of people who decide what ships.

**Not about:** open-source contributors. Startups. Academic researchers. Hospitals, schools,
employers and ordinary deployers using these tools. Small operators. **Users.** *(On deployers
precisely — a defined class under the Act, given a route to discharge the duty rather than an
exemption from it — see [the case](../docs/the_case.md#who-this-is-about).)*

**And a distinction this project got wrong at first, corrected here.** It is not true that *no
American law reaches a natural person* in connection with AI — it does, and readily. Nebraska's
Conversational AI Safety Act defines an "operator" as a *person*, which includes a natural person,
so a sole trader running a chatbot is inside it in his own name. Other bodies of law reach sellers
and distributors too.

**The true claim is narrower and worse.** *No American law places a duty on the officer of a
covered frontier developer for the decision to release.* The law reaches **down** to the smallest
participant and **not up** to the largest. That is the finding, and it is sharper than the
overstatement it replaces.

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
| **Read and answered** | **7** (H.R. 9917, Connecticut SB 5, Idaho S 1297, Nebraska LB 525, Illinois P.A. 104-0538, New York ch. 96 of 2026, California SB 53) |
| Of those read: reaching a natural person **as an officer of a developer** | **0** |
| Of those read: naming officers and directors in the operative text | **2** (Connecticut and California SB 53 — both as recipients of a quarterly report, no duty attaching to either) |
| Of those read: requiring a human signature **from anyone at all** | **1** (Illinois — and it is the outside auditor's) |
| Of those read: requiring a signature from **anyone inside the developer** | **0** |
| Of those read: any criminal liability at all, entity or person | **0** |
| Of those read: **actually frontier bills** | **5 of 7** — two were chatbot statutes miscategorized by the tracker |
| Highest penalty found | **\$20,000,000 per day** (H.R. 9917), payable by the company |

*The count moved from six to seven on 22 August 2026, and the artifact was the same one twice.
**California SB 53 had been read in full on 21 August — by a human eye, from the chaptered text,
graded ✅ — and was not being counted**, while its findings were being used in the rows below it:
the officers-and-directors line cited SB 53 inside a denominator SB 53 was not in. That is the
Illinois error repeated, so the fix is the same: it is counted now. The tally's promise is that it
never exceeds the rows actually read, and the corollary — that it must not fall short of them
either — is the half that failed twice. **Standing rule, added here: a row graded ✅ enters the
count in the same edit that grades it.***

*The count moved from four to six on 21 August 2026. New York was read that day. **Illinois had
been read and answered since the 20th and was not being counted**, because its row sits above as
the worked example rather than in the rows section — an accounting artifact of the file's layout,
not a second reading. It is counted now, and the signature line is split in two so that Illinois's
one human signature cannot be mistaken for the thing this census is looking for.*

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

[E15](../ledger/errata.md) fixed what ✅ means for this project: **a ✅ requires that this project
opened the source, not merely that a first party wrote it.** A census of statutes needs one
further distinction, because there are two different ways a row can fall short, and collapsing
them hides which fix is owed.

| Grade | Meaning | The fix owed |
|---|---|---|
| ✅ | The enrolled or introduced text was opened **and read by a human eye** | none |
| ⚠ **R** | The primary **was opened**, but read through automated retrieval — a summarizing model stood between the text and the row | a human re-read; the locator is already in hand |
| ⚠ **F** | The primary **was not opened**; the row rests on a secondary quoting it | a fetch, and the fetchable locator is named in the row |
| ⚠ **P** | Read in part — some sections opened, others not | name which sections |

**Every row in this file currently carries ⚠ R**, and that is the honest grade rather than a
modest one: [E13](../ledger/errata.md) records automated retrieval nearly putting a false
correction into the evidence file, and [E14](../ledger/errata.md) records two primary sources
conflicting where a single fetch had reported certainty. Nothing here is quoted in a filing, a
post or a sponsor package until a human has read the enrolled text.

---

## The worked example — what a completed row looks like

### CONNECTICUT — SB 2 (2025) — the predecessor, and why it is not in this census

**Status:** substitute bill, January Session 2025 · **Read in full:** 25 August 2026 ·
**Source:** the R04 substitute text, held in the working library

**It is not a frontier bill, and the word test settles it.** *Frontier* — **zero occurrences.**
*Signature* zero, *natural person* zero, *knowingly* zero, *willful* zero, *indemnification* zero,
*whistleblower* zero, *penalty* zero. The single hit for *criminal* is a compliance carve-out for
responding to "a civil, criminal or regulatory inquiry," and the single hit for *personally* is
"personally identifying information."

**Its thirteen references to an *officer* are all to officers of the State** — the Chief Data
Officer, the Chief Information Officer, the chief executive officer of Connecticut Innovations. Not
one is an officer of a regulated developer.

So SB 2 is a general artificial-intelligence act — consequential decisions, state-agency governance,
workforce provisions — and it belongs outside a census of frontier bills. **This entry exists so
that its absence is a recorded decision rather than an oversight**, and because it is the only
document in the working library the repository had never once mentioned before today.

**What it is good for is the arc.** Connecticut tried broad in 2025 and enacted narrow in 2026: SB 5
became Public Act 26-15, and *frontier* appears in it twenty-nine times. **Broad AI act attempted,
frontier-specific act passed** — which is a data point for anyone arguing about the right scope of a
first instrument.

---

### CONNECTICUT — the officer provision, read closely — added 25 August 2026

*This census already records that Connecticut is one of two enactments naming officers and
directors in operative text, "both as recipients of a quarterly report, no duty attaching to
either." Having now read the provision in full, that row understates what is there.*

**Public Act 26-15 § (c)(2)(A):** each covered-employee report on catastrophic risk, and each update
to it, "shall be shared with **the officers and directors of the large frontier developer at least
quarterly**."

**And subparagraph (B):** "If a covered employee has alleged wrongdoing by an officer or director of
the large frontier developer in a report... neither such report nor any reasonable update... **shall
be shared with such officer or director**."

**Read those two together and Connecticut has legislated the exact moment this Act is about.** A
warning about catastrophic risk travels, by statute, on a quarterly cadence, to a named officer. The
legislature thought hard enough about that arrival to write a carve-out for the case where the
officer is the subject of the complaint — which is a considered judgment about officers receiving
warnings.

**And then nothing follows.** No duty attaches on receipt. No obligation to inquire, to act, to halt,
or to record what was done. The officer is a recipient and remains one.

**This is the strongest single fact in the census for this project's central claim**, and it is
stronger than "no state reaches an officer." It is that a state legislature has already routed the
warning to the officer's desk on a schedule, thought about who should not receive it, and stopped at
the delivery.

*⚠ Read from the enacted chapter text held in the library. The quarterly-sharing and wrongdoing
provisions were read in full on 25 August 2026; the surrounding subsection numbering is as printed
in Public Act No. 26-15.*


### ILLINOIS — SB 3261 — Artificial Intelligence Public Safety and Child Protection Transparency Act

**Status:** introduced, pending · **Session:** 104th General Assembly, 2025–26 · **Introduced:**
3 February 2026 by **Sen. Mary Edly-Allen** · **Effective date if enacted:** 1 January 2027 ·
**Checked:** 25 Aug 2026 · **Source:** introduced text, read in full

**Word test.** *Signature* — **zero**. *Certify*, *certification* — **zero**. *Natural person* —
zero. *Personally* — zero. *Criminal*, *knowingly*, *willful* — **zero**. *Indemnification* — zero.
*Officer* appears three times and never as a duty-holder: once for information "shared with officers
and directors," twice in the whistleblower section describing wrongdoing **by** an officer.

**What it does.** Section 15 requires a large frontier developer or large chatbot provider to
"write, implement, comply with, and clearly and conspicuously publish on its website a public safety
and child protection plan." Section 20 requires safety-incident reporting to the Attorney General.
Section 30 protects whistleblowers. Section 35 requires an annual third-party audit. Section 40 sets
civil penalties. Section 25 gives the Attorney General rulemaking.

**And this is the finding.** Its enacted sibling, P.A. 104-0538, at least takes **one** human
signature: the lead auditor's, at 430 ILCS 185/10(d)(2)(G). **SB 3261 takes none.** Section 35
requires the auditor to produce a report and requires only that the auditor "employ or contract one
or more individuals with expertise in corporate compliance and one or more individuals with
technical expertise in the safety of foundation models" — named roles inside the *auditor*, and no
signature from any of them either.

**So the same legislator has now written two frontier-AI instruments. The enacted one takes the
outside auditor's signature. The pending one takes nobody's.** Both describe, in detail, an
organization that must plan, monitor, assess and report — and neither identifies a person who
answers if it does not.

**One provision worth flagging for the fiscal and torts lanes.** Section 45, "Loss of equity," reads
in full: "The loss of value of equity does not count as damage to or loss of property for the
purposes of this Act." A deliberate limit on what counts as harm, and the only place in the bill
where the drafter chose to narrow rather than describe.

**Who owes the duty.** The large frontier developer or large chatbot provider, as an entity.
**Does a human sign?** **No — nobody at all.**
**Who pays.** The entity: up to \$1,000,000 per violation for a large frontier developer, up to
\$50,000 for a large chatbot provider, recovered by the Attorney General in a civil action. No
private right of action.
**Criminal exposure.** **None.** The word does not appear.


### ILLINOIS — P.A. 104-0538 — Artificial Intelligence Safety Measures Act

**Status:** enacted · **Session:** 2026 · **Checked:** 20 Aug 2026 · **Source:** enrolled bill,
pinned verbatim at [the adopted texts](./interim_standards.md)

**Word test.** *Signature* hits — **and this is the finding**: the Act requires "the signature
of the lead auditor certifying the results," at **430 ILCS 185/10(d)(2)(G)**. *Officer* does not
appear in the sense of a corporate officer owing a duty. No *natural person*, no *personally*, no
*certify* by a developer's executive.

**And the two provisions sit four items apart in the same list.** The audit report must contain
**(C)** *"a detailed assessment of the large frontier developer's internal controls, including its
designation and empowerment of senior personnel responsible for such implementation by the large
frontier developer, its employees, and its contractors"* and **(G)** the lead auditor's signature.
**Illinois requires an auditor to verify that a responsible person exists and is empowered — and
then takes the signature from the auditor.** The person whose existence and authority were just
confirmed signs nothing.

**Who owes the duty.** The frontier developer, as an entity.
**Does a human sign?** **Yes — the auditor.** The outside contractor hired to inspect the work
signs; nobody inside the developer does.
**Who pays.** The entity: civil penalties not exceeding \$1,000,000 for a first violation,
\$3,000,000 for subsequent, enforced exclusively by the Attorney General, no private right of
action.
**Criminal exposure.** None reaching a natural person.

**Verdict.** *Illinois knows how to require a named human signature — and asks it of the
inspector rather than the officer who decides to ship.*

**Confidence. ✅ throughout, corrected 21 August 2026.** The statute is pinned verbatim at
[the adopted texts](./interim_standards.md), and the auditor-signature line sits inside that same
pinned block at (d)(2)(G) — reconciled the same day against the enrolled text held in the Illinois
repository, where the two copies agree word for word.

*This row previously graded the auditor line **⚠ F**, on the reasoning that it was "quoted from a
law-firm alert" and that "the enrolled text has not been opened for that sentence." **The enrolled
text had been opened — by this project, and pinned in its own adopted-texts file, before the census
was written.** The grade was not too cautious in principle; it was wrong about what the repository
already held. Recorded rather than silently upgraded, because it is the mirror image of
[E15](../ledger/errata.md): that entry graded a claim too high by asking who wrote the source, this
one graded a claim too low by not checking what we had already read. **Both are the same failure to
look, and only one of them looks like diligence.***

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
[house language § 7](./house_language.md), which sets out what every frontier definition in force
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

*This row closes a queue item.* [E15](../ledger/errata.md) listed "the AI Kill Switch Act's
thresholds, penalties, and red-teaming carve-out" as ⚠ pending fetch with no primary opened. The
primary is now open and the three items are answered — at ⚠ R, not ✅, because opening a document
through a summarizing model is not the same as reading it.

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
*felony*, *imprison*, *knowingly*, *willful* — **all absent.**

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

**Verdict.** *Connecticut is the **second** American statute to put catastrophic-risk reports into
a named officer's hands every quarter — after California's SB 53 — and the only thing either asks
that officer to do with them is receive them.* **The recurrence is the finding, not the primacy:**
two legislatures, fourteen months apart, independently decided the officers should be told, and
neither asked the officer told to do anything at all. *(Verdict conformed 22 August 2026:
[E20](../ledger/errata.md) corrected this row's tally to two and named both, and this sentence —
the quotable one — was not conformed with it.)*

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
[E13](../ledger/errata.md), the quoted clause must be re-read by a human against the enrolled act
before it is used in any public claim, post or filing — **and this is the row most likely to be
quoted, so it is the row that most needs it.**

---

### IDAHO — S 1297 — Conversational AI Safety Act

**Status:** **enacted**, signed 31 Mar 2026, Session Law ch. 249; effective **1 July 2027** ·
**Session:** 2026 · **Checked:** 21 Aug 2026 · ✅ **Primary now held on the shelf, 26 Aug 2026** — the engrossed print, "SENATE BILL NO. 1297, As Amended, BY STATE AFFAIRS COMMITTEE," 3 pp., from the Idaho legislature's own site, which refused a machine on the same day. **Held, not yet read through.** · **Source:** engrossed/enrolled text, Idaho
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

### NEW YORK — S 8828 (ch. 96 of 2026) — Responsible AI Safety and Education (RAISE) Act

**Status:** **enacted**, signed 19 Dec 2025, chapter-amended 2026, effective **1 Jan 2027** ·
**Session:** 2025–26 · **Checked:** 21 Aug 2026 · **Source:** the enacted chapter text, pinned
verbatim in the project's [New York repository](https://github.com/FrontierAIAccountabilityProject/raise-officer-certification)
· **Sponsors:** Senator Andrew Gounardes, Assemblymember Alex Bores

**A real frontier statute**, on the enacted family's own terms: article 44-B of the General
Business Law, duties on *large frontier developers*, frontier AI frameworks, transparency reports,
catastrophic-risk assessment and incident reporting.

**Word test — and this row is the shortest in the file for a reason.** *Audit* — **absent, no
occurrences.** *Signature*, *shall sign* — **absent.** *Certify*, *certification* — **absent.**
*Officer* — hits only as *"public officers law"*, a records provision, and is a false positive on
the question. *Natural person* — **one occurrence**, at *"a mechanism that enables a natural person
to communicate with the"* division: a communication channel, not a duty-bearer.

**Who owes the duty.** The frontier developer, as an entity, throughout.

**Does a human sign?** **No. Nothing. Nobody.** Illinois at least requires one human signature and
gives it to the outside auditor; **New York does not require a signature at all.**

**Who pays.** The entity, on the Attorney General's action. No individual liability.

**Criminal exposure.** None reaching a natural person.

**And the provision that comes closest.** The Act bars a developer from making *"a materially false
or misleading statement about catastrophic risk from its frontier models"* — the nearest thing in
enacted American frontier law to this project's truth-telling limb. **It is a duty not to lie, owed
by a company, with nobody required to put a name to the statement.** A false statement with no
signatory is a provision without a defendant.

**Verdict.** *New York wrote a duty not to lie about catastrophic risk and left the line where a
human being would sign it blank.*

**Confidence. ✅ Read in full 25 August 2026** (superseding the ⚠ R grade this row carried until then, which read: "opened and searched directly, not read from a summary; not yet read by a human eye"). § 1421 was read entire from the enacted chapter text; see [PF-11](../audit/pre_review_pass_2026-08-24.md) for the four provisions SEC. 3(c)(4) adopts and never mentions. The original note continued: the enacted chapter text was opened and searched directly, not read from a
summary. Not yet read by a human eye.

---

### The lineage finding — Illinois's signature is New York's deleted subdivision

*Opened 21 August 2026. **Embargo lifted the same night: S 6953-A was read in full, directly from
nysenate.gov, by the project maintainer.** The text is pinned verbatim at
`research/raise_act_s6953a_2025_prior_version.txt` in the
[New York repository](https://github.com/FrontierAIAccountabilityProject/raise-officer-certification).
**Graded ✅.***

The queued question was whether an earlier version of the RAISE Act contained an audit requirement
that was later removed. **It did. It is § 1421(4), and what came out with it was very much larger
than an audit.**

#### The provisions, with their subdivisions

**New York S 6953-A § 1421(4)(A):**

> BEGINNING ON THE EFFECTIVE DATE OF THIS ARTICLE, OR **NINETY DAYS AFTER A DEVELOPER FIRST
> QUALIFIES AS A LARGE DEVELOPER, WHICHEVER IS LATER**, A LARGE DEVELOPER SHALL ANNUALLY RETAIN A
> THIRD PARTY TO PERFORM AN INDEPENDENT AUDIT OF COMPLIANCE WITH THE REQUIREMENTS OF THIS SECTION.
> SUCH THIRD PARTY SHALL CONDUCT AUDITS CONSISTENT WITH BEST PRACTICES.

**§ 1421(4)(C)(III):**

> A DETAILED ASSESSMENT OF THE LARGE DEVELOPER'S INTERNAL CONTROLS, INCLUDING ITS **DESIGNATION AND
> EMPOWERMENT OF SENIOR PERSONNEL** RESPONSIBLE FOR **ENSURING COMPLIANCE** BY THE LARGE DEVELOPER,
> ITS EMPLOYEES, AND ITS CONTRACTORS

**§ 1421(4)(C)(IV):**

> THE SIGNATURE OF THE LEAD AUDITOR CERTIFYING THE RESULTS OF THE AUDIT.

**§ 1421(4)(D):**

> THE LARGE DEVELOPER SHALL RETAIN AN UNREDACTED COPY OF THE REPORT FOR AS LONG AS A FRONTIER MODEL
> IS DEPLOYED PLUS FIVE YEARS.

#### The same provisions, as Illinois enacted them

| New York S 6953-A, struck June 2025 | Illinois 430 ILCS 185/10(d), in force |
|---|---|
| § 1421(4)(A) — annual independent third-party audit, *"ninety days after a developer first qualifies… whichever is later"* | **(d)** — *"Beginning on January 1, 2028 or 90 days after a developer first qualifies as a large frontier developer, whichever is later"* |
| § 1421(4)(C)(III) — designation and empowerment of senior personnel | **(d)(2)(C)** — designation and empowerment of senior personnel |
| § 1421(4)(C)(IV) — signature of the lead auditor | **(d)(2)(G)** — signature of the lead auditor |
| § 1421(4)(D) — unredacted copy, deployed plus five years | **(d)(3)** — unredacted copy, deployed plus 5 years |

**Illinois 430 ILCS 185/10(d)(2)(C) and (G) — the two provisions this project's Illinois proposal
is built on — are New York S 6953-A § 1421(4)(C)(III) and (IV).**

#### Two details that settle how the text traveled

**One — the ninety-day clause is New York's, and Illinois carries it verbatim.** California's
SB 1047 has no such clause; it opens flatly with *"Beginning January 1, 2028."* New York's opens
*"beginning on the effective date of this article, or ninety days after a developer first qualifies
as a large developer, whichever is later."* **Illinois has both**: SB 1047's hard date and New
York's ninety-day alternative, in one sentence. *(This corrects an earlier version of this file,
which attributed the commencement construction to SB 1047 alone.)*

**Two — Illinois changed four words, and the change left an orphan.** New York required assessment
of senior personnel responsible for **"ensuring compliance by"** the developer. Illinois has senior
personnel responsible for **"such implementation by"** the developer. **In New York the phrase has a
clear referent. In Illinois, *such implementation* refers back to nothing in the surrounding list**
— (A) and (B) speak of compliance with the Section, not of any implementation. The Illinois clause
is grammatically stranded in a way its source was not, which is what an edit made during
transplantation looks like.

#### What else went out with it

The audit was not the only thing struck. Running the same terms against the enacted chapter text
returns **zero occurrences of every one of these**, each of which appears in S 6953-A:

| provision in S 6953-A | in the enacted law |
|---|---|
| § 1420(12)(G) — the safety protocol must *"DESIGNATE SENIOR PERSONNEL TO BE RESPONSIBLE FOR ENSURING COMPLIANCE"* | **absent** |
| § 1421(2) — *"A LARGE DEVELOPER SHALL NOT DEPLOY A FRONTIER MODEL IF DOING SO WOULD CREATE AN UNREASONABLE RISK OF CRITICAL HARM"* | **absent** |
| § 1421(4) — the audit, in its entirety | **absent** |
| § 1421(6) — *"SHALL NOT KNOWINGLY MAKE FALSE OR MATERIALLY MISLEADING STATEMENTS"* | **absent** in that form |
| § 1422(5)(A)(ii) — **corporate officers** included as protected employees | **absent** |
| § 1423(2)(B) — *"A COURT SHALL DISREGARD CORPORATE FORMALITIES AND IMPOSE JOINT AND SEVERAL LIABILITY ON AFFILIATED ENTITIES"* | **absent** |

**So the finding is not that New York dropped an audit.** New York's bill, in the print that stood
from 3 to 9 June 2025, required a developer to designate senior personnel, had an independent auditor verify that
those personnel were designated *and empowered*, took that auditor's signature, protected corporate
officers who raised risks, barred deployment at unreasonable risk of critical harm, and told courts
to pierce the corporate veil where the structure was built to frustrate recovery.

**The enacted law has none of those six.** What survives is transparency: publish a framework,
report incidents, do not make materially false statements about catastrophic risk.

> **This is the closest any American legislature has come to the thing this project asks for, and
> it existed for six days.**

#### Stated with the limits intact

**This file records what the texts say and nothing else.** It does not say why the provisions came
out, who asked, or what was traded for what. **It is not a claim about the sponsors**, who wrote the
provisions in the first place and are the reason there is anything to compare. Amendments during
passage are ordinary legislative practice, and a bill that passes without a provision is a bill that
passed.

**The dates, which are the only chronology asserted:** `PRINT NUMBER 6953A` on **3 June 2025**;
`PRINT NUMBER 6953B` on **9 June 2025**; passed both houses **12 June**; signed **19 December 2025**
as chapter 699; chapter-amended 2026 as chapter 96.

**Confidence. ✅ for S 6953-A** — read in full from the New York Senate's own page by a human, and
pinned verbatim in this project's own repository, which is the standard [E15](../ledger/errata.md)
set. **⚠ R for the enacted-text comparisons**, which were run by automated search against the
project's pinned copy of chapter 96. **⚠ R for SB 1047.**

---

### And it did not start in New York. Four drafts, one survivor.

*Traced 21 August 2026. ⚠ **Still ⚠ R — SB 1047 and SB 53 were each retrieved once and neither has been read by a human eye. The New York half of the lineage is now ✅; the California half is not.***

The obvious next question was where New York got the language. **California, and there is a date in
it that proves copying rather than convergence.**

**California SB 1047 (2023–24), vetoed by Governor Newsom in September 2024**, at § 22603(e):

> Beginning January 1, 2028, a developer of a covered model shall annually retain a third-party
> auditor that conducts audits consistent with best practices for auditors to perform an
> independent audit of compliance with the requirements of this section.

and at § 22603(e)(2)(D):

> The signature of the lead auditor certifying the results of the auditor.

**Illinois, 430 ILCS 185/10(d), enacted 2026:**

> **Beginning on January 1, 2028** or 90 days after a developer first qualifies as a large frontier
> developer, whichever is later, a large frontier developer shall annually retain a third party to
> perform an independent audit of compliance with the requirements of this Section. The third party
> shall **conduct audits consistent with generally accepted auditing standards and best practices**…

**Look at the date.** In a bill drafted in 2024, *January 1, 2028* is a four-year runway — a
sensible lead time for an obligation nobody has built capacity for yet. In a statute enacted in
2026 it is two years, and in a statute whose other duties commence in 2027 it is simply inherited.
**A commencement date that made sense in the bill it came from and less sense in the one it landed
in is a fingerprint.** So is *audits consistent with … best practices*, carried across three
drafts.

**The provision's full record, stated with the differences intact:**

| | what happened to the audit and the lead-auditor signature |
|---|---|
| **California SB 1047** (2024) | Drafted in full. **The entire bill was vetoed** — the audit was not singled out, and this must not be described as a removal |
| **New York S 6953 / S 6953-A** (2025) | Drafted in full. **Removed at the B amendment**; the bill then passed and was signed without it |
| **California SB 53** (2025, enacted) | ⚠ **No occurrence of *audit* at all.** California's successor statute does not carry the provision its own vetoed bill had drafted |
| **Illinois P.A. 104-0538** (2026, enacted) | **Enacted, and in force.** The only surviving instance in American law |
| **Louisiana SB 474** (2026) | Audit drafted, **signature not**. **Died in chamber** without a vote on its merits — see the section below |

**Five drafts. One survivor.** And the survivor is the sole reason the census can report that any
enacted American frontier statute requires a human signature at all.

**Three things this does not establish, named so nobody reads them in.** It says nothing about
*why* the provision came out in New York, or who asked. It does not treat California's veto as a
judgment on the audit — the Governor vetoed the whole bill, on grounds this file has not read.
And it does not claim the drafters copied one another knowingly; **shared model language and shared
advocacy drafting produce the same textual fingerprints as copying**, and the census cannot tell
those apart from the text alone.

**What it does establish is enough.** The audit-and-signature provision is not an Illinois
peculiarity and not an oversight elsewhere. **It is a specific, repeatedly drafted piece of text
that four legislatures had in front of them, and it is in force in one.**

**Confidence. ⚠ R, and the weakest link is named.** SB 1047 and SB 53 were each read once, through
LegiScan's copy of the bill text — a third-party host of a primary document, retrieved
automatically. The Illinois text is held verbatim by this project and is the strongest element
here. **SB 53's nil result rests on a single retrieval and should be re-run before it is quoted**;
a negative finding from one fetch is the shape of [E11(c)](../ledger/errata.md), where this project
asserted a gap from arithmetic it never did.

---

### California SB 53, read in full — and it is the text New York now has

*Read 21 August 2026 from the chaptered text, in full, by the project maintainer. **✅.** This
replaces the single automated retrieval the file previously relied on, and that retrieval was
right about the nil result and blind to everything else in this section.*

**The nil result stands.** Chapter 138 of 2025 contains **no occurrence of `audit`, `signature`,
`certify` or `certification`.** California's enacted statute does not carry the provision
California's own vetoed bill drafted.

#### But it does name officers and directors, and the census said it did not

**Labor Code § 1107.1(e)(2)(A)**, added by SB 53:

> Except as provided in subparagraph (B), the disclosures and responses of the process required by
> this subdivision **shall be shared with officers and directors of the large frontier developer at
> least once each quarter.**

**(B)** disapplies it to an officer or director accused of the wrongdoing.

**This is the Connecticut provision.** This census records Connecticut SB 5 as routing quarterly
anonymous catastrophic-risk reports to *"the officers and directors of the large frontier
developer"* and attaching no duty to receiving them, and reported it as **the only** instrument
naming officers and directors in operative text. **That was wrong.** California does the same thing,
on the same quarterly cadence, with the same absence of any consequent obligation. The tally is
corrected above from one to two. *Filed as [E20](../ledger/errata.md).*

**And the correction strengthens what Connecticut was evidence for.** One state routing risk reports
to named officers and asking nothing of them is a drafting choice. **Two states doing it identically
is a template.**

#### The larger finding: New York's enacted Act is substantially this statute

Three provisions, compared against the project's pinned copy of New York chapter 96 of 2026:

| California SB 53 | New York, enacted |
|---|---|
| § 22757.12(c)(1)(B) — *"A mechanism that enables a natural person to communicate with the frontier developer"* | *"a mechanism that enables a natural person to communicate with the"* division — **the sole occurrence of *natural person* in New York's enacted law** |
| § 22757.12(c)(2)(C) — *"The extent to which third-party evaluators were involved"* | *"the extent to which third-party evaluators were involved"* — **verbatim** |
| § 22757.12(e)(1)(A) and (B) — *"materially false or misleading statement about catastrophic risk… or its management of catastrophic risk"* and *"…about its implementation of, or compliance with, its frontier AI framework"* | **both, verbatim, in the same order** |

**So the provision this file called "the one that comes closest" in New York's enacted law — the
duty not to make materially false statements about catastrophic risk — is California's sentence.**

#### Two lineages, and only one of them spread

Set the two traces beside each other.

**The accountability line.** California SB 1047 drafts an annual independent audit, a lead-auditor
signature, and assessment of designated and empowered senior personnel. **Vetoed with its bill.**
New York carries it at S 6953-A § 1421(4), together with veil-piercing, officer whistleblower
protection and a bar on unreasonably risky deployment. **Struck at the B amendment on 9 June 2025,
three days before passage, after six days in the bill.** Louisiana drafts the audit without the signature. **Dies in chamber.** Illinois enacts it.
**One survivor in four attempts.**

**And the largest unanswered question in this file sits inside that sentence.** This census records
*that* § 1421(4) was struck at the B amendment on 9 June 2025, three days before passage and six
days after it was introduced. **It does not record why,
because nobody has written it down.** Not the sponsors, not the press, not the advocacy record this
project has read. The possibilities are not equivalent and the difference matters to every drafter
who comes after: the provision may have been traded for votes, it may have been a casualty of
drafting convention in a fast amendment, or **somebody may have made a substantive argument against
it that this project ought to be taking seriously and currently is not.**

**This is not a rhetorical question.** If the third possibility is the true one, the strongest
objection to this Act's central mechanism already exists, was persuasive enough to move a
legislature in three days, and is unrecorded. A drafter who does not go looking for it is choosing
not to know. **The route to an answer is the two sponsors and their counsel**, and it is being
asked. As of 25 August 2026 the cheapest public route — the Senate floor record of the passage
date — has been worked and came back empty: the bill passed 58 to 1 with no debate and no member
raising the strike (item 3 below). That does not weaken the question. It narrows it, and it means
nobody has ever had to answer it in public. Whatever comes back is published as given, including that the provision was wrong.

*(Open item. Any reader who knows what happened between 3 and 12 June 2025, or who has a primary
document from those days, is asked to send it; it enters the record with attribution unless anonymity is
preferred.)*

#### How this question actually gets answered, in order of what it costs

*A question stated and not worked is a decoration. New York leaves a paper trail and most of it is
free. This is the retrieval program, ranked by cost, with what each source can and cannot show.
Nothing below is a finding; it is a list of places the finding might be.*

**Free, online, do these first.**

1. **The A print against the B print, side by side, from the Senate's own system.** Establishes
   exactly what came out, to the word. Partly done; the diff is what produced § 1421(4) above. What
   it cannot show is why.
2. **The sponsor's memorandum on each print.** New York publishes a sponsor memo with the bill, and
   it is revised when the bill is. A memo that changes its justification between the A and B prints
   is the cheapest possible evidence of what the sponsors thought they were doing. **Nobody has
   compared them. Since item 3 came back empty, this is now the highest-value unopened source in
   the whole file.**
3. **The Senate floor transcript for the passage date.** ✅ **Discharged, 25 August 2026, and the
   answer is a negative one: the floor is silent.** RAISE was called as Calendar No. 1889 on the
   supplemental calendar of 12 June 2025. The title was read, the last section was read, the roll
   was called, Senator Gounardes explained his vote, and the bill passed **58 to 1**, the single
   negative being Senator Cooney. **No member laid the bill aside. No member asked why the audit
   provision had come out three days earlier. There was no debate.** So the third possibility above
   cannot be answered from the floor, because the floor never took it up. Working record:
   `library/RECORD_NY-Senate_Floor-transcript_2026-06-12_RAISE-passage_AUTOCAPTION.md`.
   ⚠ **The version read was a YouTube auto-caption, not the stenographic record**, and it is
   visibly noisy. What an auto-caption can carry without further checking is the procedural record:
   what was called, who spoke, and how the vote fell. **Nothing from it may be published as a
   verbatim quotation until it is checked against the stenographic transcript.** That check is
   still owed, and as of 25 August 2026 the locator is in hand, which is the part that used to be
   missing: the Senate's session page for 12 June 2025 links a transcript at

   <https://www.nysenate.gov/transcripts/2025-06-12t1338>

   ⚠ Automated retrieval of that page returns a truncated document that stops at Calendar No. 1374,
   short of RAISE at 1889, so **the stenographic text of the passage has still not been read.** The
   remaining work is to open that transcript by hand and read from Calendar 1374 to the end. Note
   also that the session page gives a start time of 10:00 a.m. while the transcript is timestamped
   13:38, so there may be more than one transcript for the day; check before concluding the roll
   call is absent from it.
4. **The Assembly debate transcript** for the companion. Assembly debate transcripts are held by
   the Assembly Public Information Office and archived through the State Archives finding aids;
   they are not always as easy to pull as the Senate's, but they exist.
5. **The six-day press window.** Politico New York, City & State, Times Union, Spectrum, Gothamist,
   searched to the day. Late amendments to a watched bill are usually reported by somebody.
6. **Lobbying filings** with the New York Commission on Ethics and Lobbying in Government: who
   registered on this bill, and for whom. That will not give the argument, but it names who was in
   the room while it was being made.

   **A caution on what New York actually releases, added 25 August 2026.** Reinvent Albany's
   December 2025 study of the same chamber records that a Freedom of Information Law request to the
   New York Senate returned **floor votes for 2024 and 2025 but not committee votes**, and that the
   Senate does not publish members' confirmation votes on its website at all, in contrast to the
   U.S. Senate, the New York City Council, and California, Illinois, Pennsylvania and Vermont. That
   study is about confirmations rather than bills, so it is not directly on point; it is here
   because it is third-party evidence about this chamber's record-keeping, and it means the
   program above should not assume committee-level material will be produced on request. Source
   at `library/REPORT_Reinvent-Albany_NY-Senate-confirmation-vote-transparency_2025-12.pdf`.

**Costs a request, and is the richest single source.**

7. **The bill jacket.** After a New York bill is signed, the Governor's Counsel compiles a jacket:
   agency memoranda, the sponsors' letters, and letters for and against from anyone who wrote in.
   Jackets are held by the New York State Library (`nysl.nysed.gov/billjack`) and the State Archives
   (Series 12590), and several New York court law libraries provide public access. **If a
   substantive argument against the audit-and-signature provision was ever written down by anyone,
   this is the likeliest place it survives.**

   **And the honest limit on it, stated before anyone gets excited.** A jacket captures what was
   sent *to the Governor about the bill as passed*. The B amendment happened in the legislature,
   three days earlier. So the jacket is strong evidence about who opposed the provision and on what
   grounds, and it is **not** direct evidence of the legislature's own reason for striking it. A
   recent jacket may also not be processed yet.

**People, which is where the answer probably actually lives.**

8. **The two sponsors and their counsel.** Being asked. Senator Gounardes is the surviving author.
9. **The advocacy organizations that worked the bill.** Whoever was pushing RAISE knows what was
   traded, and several of them publish.

**The rule that applies to all of it.** Whatever comes back is published as given, including, and
especially, "the provision was struck because it was wrong, and here is the argument." A project
that asks for hostile review and then buries the one hostile answer it went looking for would
deserve everything that followed.

**The transparency line.** California SB 53 — framework, transparency report, incident reporting,
no audit, no signature, officers and directors as recipients of a quarterly report they owe nothing
about. **Enacted in California. Substantially adopted in New York's enacted text. The
officers-and-directors mechanism appears identically in Connecticut.** Three states.

> **The model with a person accountable in it has been drafted four times and enacted once. The
> model without one has been enacted three times in a year.**

That is the census's finding, stated at last with a mechanism rather than as an absence.

#### What is not claimed

**Direction of travel is not established by textual identity alone.** These provisions may descend
from a common draft, from the same advocacy or model-legislation source, or from legislatures
reading each other. **This file records that the texts are the same and does not assert who copied
whom.** The dates are compatible with California-to-New-York — SB 53 chaptered 29 September 2025,
New York's chapter amendment in 2026 — but compatible is not the same as demonstrated.

**Nor is any of this a criticism of the transparency model**, which does real work: mandatory
frameworks, incident reporting to a state agency, whistleblower protection with fee-shifting and a
reversed burden of proof. **The observation is narrower.** Every duty in it runs to a company, and
where a human being is named, it is to receive a report.

**Confidence. ✅** for SB 53 — the chaptered text read in full. **⚠ R** for the comparisons against
New York chapter 96, run by automated search against this project's pinned copy. **⚠ R** for
SB 1047, still read once and not by a human eye.

---

### Searching for the provision's own words found a bill no list of ours contained

**Method note, and it is the most useful thing in this section.** Every coverage failure this
project has recorded — [E16](../ledger/errata.md) above all — came from assembling a watch out of
lists: trackers, prior adoptions, states already known. **This search was run the other way.** The
query was the provision's own language, not a jurisdiction. It immediately returned an instrument
that appears **nowhere in this repository**, in a state no list here has ever named.

**LOUISIANA — SB 474 (2026 Reg. Sess.) — Protecting Louisiana's Infrastructure from Artificial
Intelligence Risk Act.** Sen. **Gregory Miller (R)**. Introduced 31 March 2026. **Died in chamber**,
last action 21 April 2026: *"Read by title and returned to the Calendar, subject to call."*
Proposed effective date 1 January 2027.

From the bill's official Digest:

> Proposed law requires a large frontier AI developer, **beginning July 1, 2028**, and annually
> thereafter, to retain an **independent third-party auditor** to assess compliance with its
> frontier AI framework and identify any material deviations from the framework.

**The audit traveled. The signature did not.** On the Digest, Louisiana carries the annual
independent third-party audit and **no lead-auditor signature**, and the commencement date has been
moved off the inherited 1 January 2028 to 1 July 2028 — the one place the drafting was adjusted
rather than carried.

**And it disposes of the reading that this is a partisan provision.** A Republican senator in
Louisiana put the same audit requirement in front of his chamber that a Democratic senator put in
front of California's. It died without a vote on its merits.

⚠ **Confidence: ⚠ F on the operative text.** Only the **Digest** — Louisiana's official
staff-prepared summary, published with the bill — has been read. The Digest is not the statute, and
the word test above is a test of a summary. **The engrossed text is owed** and is at
<https://legiscan.com/LA/text/SB474/2026>. Status and sponsor are from LegiScan, ⚠ **R**.

### The federal instinct points the same way: certify the inspector

**VET AI Act — Validation and Evaluation for Trustworthy Artificial Intelligence Act.** Senators
**John Hickenlooper (D-CO)** and **Shelley Moore Capito (R-WV)**, introduced **25 July 2024**. Also
absent from this repository until now.

It does not mandate an audit of anyone. It directs **NIST** to develop *voluntary* specifications
and guidelines for third-party evaluators, and would establish an advisory committee to recommend
criteria for *"individuals or organizations seeking to obtain certification of their ability to
conduct internal or external assurance for AI systems."*

**Read that against Illinois and the pattern is the finding.** Illinois requires one human
signature and takes it from the auditor. The federal proposal reaches for a human too — and reaches
for **the auditor again**, to credential him.

> **When American AI law goes looking for a person, it finds the inspector.** It has now done so in
> an enacted state statute, a bipartisan federal bill, and — in the negative — in every instrument
> that dropped the provision. **The officer who decides that a system ships has not been reached in
> any of them.**

That is no longer a claim about a gap. It is a claim about a **habit**, and the habit is
documented across five states, one federal chamber and three years.

⚠ *VET AI is described from its sponsors' own press release, read once. The bill text has not been
opened and no bill number is asserted here. Whether it has been reintroduced in a later Congress is
**not established**.* ⚠ **R**.

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

- [x] Illinois — P.A. 104-0538 *(worked example above; row complete, auditor line now ✅ and cited
  at 430 ILCS 185/10(d)(2)(G))*
- [x] **New York — S 8828, ch. 96 of 2026** *RAISE Act* — done, 21 Aug. *Enacted; a real frontier
  statute, and it requires no signature from anyone.*
- [x] **New York — S 6953-B** — done, 21 Aug. *The B text carries no audit, no signature, no
  certification. The audit was gone before passage, not in the chapter amendment.*
- [x] **New York — S 6953-A** — **done, 21 Aug, ✅.** Read in full from nysenate.gov by the
  maintainer and pinned verbatim in the New York repository. The audit is § 1421(4); Illinois's
  (d)(2)(C) and (G) are its (C)(III) and (C)(IV). **Embargo lifted.**
- [x] **California — SB 53** *Transparency in Frontier Artificial Intelligence Act* — **done,
  21 Aug, ✅.** Chaptered text read in full. No *audit*, no *signature*, no *certify*. Names
  officers and directors at Labor Code § 1107.1(e)(2)(A). See the section above.
- [x] **California — SB 1047** (2023–24, vetoed) — traced 21 Aug. *Not an enacted statute and so
  not a census row, but the origin of the audit and lead-auditor language. See the lineage
  sections above.*
- [ ] **California — SB 53, full row** — the word test is done; the four questions are not.
- [ ] **Louisiana — SB 474** (2026, died in chamber) — ⚠ **Digest only.** The operative engrossed
  text has not been opened: <https://legiscan.com/LA/text/SB474/2026>. A full row is owed, and
  Louisiana must be added to the state list below, where it has never appeared.
- [ ] **Federal — VET AI Act** (Hickenlooper/Capito, 25 July 2024) — press release only. Bill
  number not asserted; text not opened; later-Congress reintroduction not established.

**Checked 25 August 2026, and it is not what a tracker summary made it look like:**

- [x] **New York — S 1169-B** (Gonzalez) — *the New York AI Act.* Checked against the LegiScan
  print, and **it is not a fifth attempt in the RAISE audit lineage.** A commercial tracker
  describes it as requiring "independent audits of high risk AI systems", which reads at a glance
  like a fourth-and-a-half data point for the finding above. It is not. S 1169-B amends the **civil
  rights law** and the executive law; it defines *algorithmic discrimination* by protected
  characteristic; it turns on *consequential decisions* about employment, education, housing,
  family planning, health care, financial services and legal services. Its audit is a
  discrimination audit of a deployed decision system. It is New York's analogue of Colorado
  SB 24-205, not of the RAISE Act. **The lineage count is unchanged: four drafts of a
  frontier-safety audit, one survivor.** S 1169-B is recorded here as an adjacent lineage so that
  the next person who reads that tracker line does not have to do this again.

  Two things it does establish, both quoted in
  `library/NOTES_Reading_New-intakes-batch-2_2026-08-25.md`:

  - **Senator Gounardes is a co-sponsor.** The sponsor line names "Sens. GONZALEZ, BAILEY,
    BRISPORT, BYNOE, CLEARE, FAHY, FERNANDEZ, **GOUNARDES**, HINCHEY, JACKSON, KRUEGER, LIU, MAY,
    PARKER, PERSAUD, RIVERA, SALAZAR, SANDERS, WEBB". So in the same two-year session in which the
    audit came out of his own bill between prints A and B, he put his name to a different bill that
    keeps a statutory audit section and defines an independent auditor. That is evidence he has not
    abandoned independent audit as an instrument, and it is a reason to put the § 1421(4) question
    to him as a live question rather than as an accusation.
  - **Article 10-A carries § 110 "Audits"** and § 105(3) defines "Auditor" as "an independent
    entity including but not limited to an individual, non-profit, firm, corporation, partnership,
    cooperative, association, academic institution, or group affiliated with an academic
    institution, commissioned to perform an audit."

  **Closed the same day on the full text.** The complete twelve-page print was obtained from the
  New York Assembly's own bill-text service and the word test run on all of it. *Officer* returns
  one hit and it is "committee or officer of the state" in the jurisdictional-scope section.
  *Director*, *senior personnel*, *signature*, *misdemeanor*, *felony*, *criminal*, *frontier* and
  *catastrophic* return **nil**. *Certification* returns one hit, in the list of consequential
  decisions ("Accreditation; Certification; Admissions"), which is a subject of regulation and not
  a duty. **S 1169-B puts no duty on any natural person, and its enforcement at § 114(1) is civil
  only:** an attorney-general application for an injunction without proof of injury, and civil
  penalties of not more than $25,000 per violation against a developer and $10,000 against a
  deployer.

  **Two provisions in it are worth the census's attention even though the row is adjacent.**

  **§ 110 is the most developed auditor-independence text in any American AI bill this project
  holds**, and it is doing in a live New York bill the job that RAISE's § 1421(4) was drafted to
  do. It bars any auditor who has provided "any auditing or non-auditing service including, but
  not limited, to financial auditing, cybersecurity auditing, or consulting services of any type,
  to the commissioning company in the past twelve months", and any auditor who "is, will be, or
  plans to be engaged in the business of developing or deploying an AI system that can compete
  commercially" within five years. It provides that "[f]ees paid to auditors may not be contingent
  on the result of the audit and the commissioning company shall not provide any incentives or
  bonuses for a positive audit result." It entitles the auditor to "complete and unredacted copies
  of all reports previously filed". And at (7) it provides that an audit "may be completed in part,
  but shall not be completed entirely, with the assistance of an AI system", and bars drafting one
  with an AI system "without meaningful human review and oversight". **Nothing in the enacted
  Illinois text, or in California SB 53, goes this far on independence.**

  Its valve at § 110(4) is also its loophole, and the proportionality lane should look at it: an
  in-house employee auditor is permitted where an independent audit "exceeds one percent of the
  fair market value" of the developer or deployer. A percentage-of-value ceiling protects the
  smallest party in principle and, in practice, is unreachable for the largest developers and easy
  for a small one. That is an observation about somebody else's drafting, offered as one.

  **§ 114(2) reverses the causation presumption at the pleading stage**, and then declines to let
  an audit discharge it: the court "shall presume the specified AI system was created and/or
  operated in violation" and caused the harm, rebuttable only by clear and convincing evidence,
  and "the mere existence of such an audit, without additional evidence, shall not be considered
  clear and convincing evidence." Both halves bear on this project: the first is a route it has
  not taken, and the second is a warning about the route it has. Carried into
  [known objections](../docs/known_objections.md).

  ⚠ The status reported by the tracker ("Engrossed - Dead, delivered to Assembly, 3 June 2026") is
  **not** verified against a primary source and is not asserted here. Quotations and the full word
  test at `library/NOTES_Reading_Three-more-hearings-and-S1169-full_2026-08-25.md` § 4.

**Done 23 August, from the day's intake** *(each against primary text; the tracker's category
was wrong in every checked case, which is now six reasons not to trust the list)*:

- [x] **Federal — S. 1792** — done, 23 Aug, ✅ **primary XML read in full** (public domain; held
  on [the shelf](../research/verification_record.md)). The **AI Whistleblower Protection Act**
  (Grassley + five, bipartisan; introduced 15 May 2025) — anti-retaliation only, employees and
  contractors; **no disclosure mandate; no officer duty; no signature.** The tracker filed it as
  "safety incident reporting"; it is not. Full reading at
  [who has to tell you § 4b](./who_has_to_tell_you.md).
- [x] **New York — S 10456** — done, 23 Aug, ✅ **primary full text in hand** (one-section bill).
  Gounardes (RAISE's own sponsor): the DIGIT office in the Department of Financial Services must
  adopt **minimum standards** for large frontier developers' frameworks by 1 July 2028, reviewed
  annually against "critical safety incidents that have occurred." The family's author legislating
  the grade-your-own-homework problem — movement toward substance, none toward persons. Bonus: its
  effective-date clause fixes RAISE's proper citation as **GBL Article 44-B, ch. 96 of 2026**.
- [x] **California — AB 2653** — identified, 23 Aug, ⚠. A **Public Contract Code**
  state-procurement reporting bill (Asm. Lee; held under submission May 2026), not frontier
  governance; the tracker's "frontier model disclosure" category is its sixth verified error. No
  row owed; leginfo link banked.

**Added to the queue 23 August** *(leads from CSIS 3 Aug, CDT 20 Aug, and a law-firm alert of
10 Jun — secondaries with primary links carried; nothing below is asserted until its text is
opened)*:

- [ ] **Colorado — SB 26-189** — the transparency-only replacement after SB 24-205's repeal;
  effective 1 Jan 2027. The repeal's litigation context — *xAI LLC v. Weiser*, No. 1:26-cv-01515
  (D. Colo.), the United States intervening against the state — is held at
  [the enforcement record § 6](../research/state_enforcement_record_2026.md).
- [ ] **Virginia — HB 797** — enacted IVO licensing via VITA (CDT). The Senate-side substitute,
  SB 384, is on [the shelf](../research/verification_record.md) and is not the enacted vehicle.
- [ ] **Washington — SB 5395** — health-insurance AI open to audit by the Insurance Commissioner;
  the narrow end of the audit spectrum (CDT).
- [ ] **Michigan — HB 4668** and **Massachusetts — S 2630** — the pending frontier-family bills
  in the CSIS nine-framework comparison; texts unopened.
- [ ] **Idaho and Tennessee — the AI-personhood-denial acts** (CDT) — statutes providing AI
  systems are not legal persons. Bill numbers to confirm; primary texts unopened; used at
  [known objections](../docs/known_objections.md) at the surveyor's grade only.
- [x] **Federal — H.R. 8094** — done, night of 23–24 Aug, ✅ **primary read in full, all sixteen
  pages** (introduced print on [the shelf](../research/verification_record.md)). The **AI
  Foundation Model Transparency Act of 2026** (Beyer, Lawler, Jacobs — bipartisan; introduced
  26 Mar 2026; Energy & Commerce). FTC-administered transparency regulations for foundation
  models; enforcement as an FTC unfair-or-deceptive-practices rule violation, entity-level; a
  full open-source exemption; small-business grace period. **No officer, no signature, no
  incident reporting, and no preemption provision anywhere in it.** The row's find is the
  coverage clause, (l)(3)(A)(iv): a covered entity includes one whose model *"was trained using
  a quantity of computing power greater than 10²⁶ integer or floating point operations,
  including computing used by the entity for the original training run and for any subsequent
  fine-tuning, reinforcement learning, or other material modifications the entity applies"* —
  **this Act's lineage-compute counting, in a bipartisan federal bill**, beside a
  capability-risk trigger, two adoption-scale triggers (10M users; 10M downloads), and
  rule-updatable thresholds. The drafting convergence is recorded at
  [the definition](../docs/the_definition.md); the central finding stands — another federal
  vehicle, and nobody in it is a person.
  **Update, same evening:** mostly resolved, with two corrections to the surveyor. Idaho is
  **H.B. 720 (2022)** — not a 2026 act — Idaho Code § 5-346, operative sentence retrieved
  verbatim. **Utah H.B. 249 (2024)** joins the enacted set (the surveyor omitted it here).
  Tennessee is **SB 837 / HB 849** (114th G.A.), identified, enrolled text still to pull. North
  Dakota proposed and then amended the ban away — a caution against overcounting. Scholarly map:
  Liebman, 61 Wake Forest L. Rev. 115 (2026). Rows on these enter when the remaining texts are
  opened; [CURE 19](../audit/v3_5_cure_language.md) carries the drafting consequence.

**Done 25 August, from the day's intake:**

- [x] **Federal — H.R. 9333** — done, 25 Aug, ✅ **primary read in full, all seven pages**
  (GPO introduced print on [the shelf](../research/verification_record.md); the print's font
  encoding defeats text extraction, so it was OCR'd at 300 dpi and every quotation below was
  **cross-checked against the govinfo bulk XML**). The **AI Flaw Reporting and Security
  Enhancement Act** — Ross, with Hurd of Colorado and Beyer; bipartisan; introduced 18 June 2026;
  Science, Space, and Technology; **ordered reported 35–0 on 25 June 2026**. NIST, consulting CISA,
  runs a program supporting *"the voluntary reporting, collection, and tracking of artificial
  intelligence flaws"*, convenes a multi-stakeholder process to define nine terms
  (vulnerabilities, failure modes, accidents, failures, hazards, catastrophes, misuse, incidents,
  adverse events), and builds *"a national database of artificial intelligence flaws or the
  modification of an existing national database"*. **Every duty in the Act falls on the Director
  of NIST.** The word test returns nil for *officer*, *director*, *executive*, *certify*,
  *attest*, *signature*, *criminal*, *misdemeanor*, *felony* and *penalty*; *voluntary* appears in
  the long title, in (a), in (c)(1) and in (d)(3).

  **The row's find is the definition at § 2(e)(2)**, and it is the most useful sentence any
  federal vehicle has given this project:

  > (2) ARTIFICIAL INTELLIGENCE FLAW.—The term "artificial intelligence flaw" means a set of
  > conditions or behaviors that allow the violation of an explicit or implicit policy related to
  > the safety, security, or other undesirable effects from use of an artificial intelligence
  > system, including artificial intelligence vulnerabilities and artificial intelligence
  > incidents, **and which is not dependent on the presence of malicious intent or related harm.**

  A federal statutory definition of *flaw* that is expressly independent of both intent and harm,
  reported out of committee without a dissenting vote. That is the architecture SEC. 9 of this Act
  needs — a thing is reportable because of what it is, not because someone meant it or someone
  has been hurt yet. The drafting consequence is carried at
  [the reporting duty](./who_has_to_tell_you.md) and at
  [CURE 17/18](../audit/v3_5_cure_language.md).

  **And the census's finding survives in a new register.** H.R. 9333 builds the receiving end that
  a reporting duty presupposes — the database — and creates no duty on anyone to file into it.
  Infrastructure, unanimously; the person, not at all. *(Reading note with every quotation and the
  OCR artifacts named: `library/NOTES_Reading_HR9333-FLARE-Science_2026-08-25.md`.)*

- [x] **New York — the FOCUS Act** — done, 25 Aug, ✅ **primary read in full** (Fostering Optimal
  Classroom Use of Screens; Gounardes, introduced 21 Aug 2026; drafting commission print
  16298-02-6-1, dated 19 Aug, on [the shelf](../research/verification_record.md); no bill number
  yet, consistent with a draft for the 2027 session). **No row is owed on this census's own
  question** — it is an education-law bill about screens and ed tech, not a frontier statute, and
  it is recorded here because of who wrote it and what its structure shows.

**The word test, run on the text.** *Officer*, *director*, *executive*, *misdemeanor*,
*felony*, *chief* and *president*: **nil.** *Certification* appears once and means the registry's
own process. *Signature* appears only on the drafting commission's cover sheet. *Criminal* appears
once, inside a data-disclosure carve-out for complying with an inquiry. *Personally* appears three
times and every one is *"personally identifiable information."* And **the single occurrence of
"natural person" in the whole Act is § 33's data-protection carve-out**, *"(9) protecting the vital
interests of a natural person"* — the data subject, not a duty-bearer.

**What the Act does place, and how close it comes.** Providers must register with the Attorney
General and show, among other things, *"at least one independent study to lead to improved academic
performance in users related to specific curriculum objectives"*; *"Schools may only offer, deploy,
or provide educational technology to a pupil that is included in the registry."* The Attorney
General runs a public complaints website, and may act where a provider *"has falsely attested that
such provider meets the registration requirements."* Enforcement, at § 39, runs where *"any
educational technology provider or any device provider has knowingly subverted the purposes"* of
the operative sections, and yields injunction, restitution, destruction of unlawfully obtained
data, damages and civil penalties.

**So there is an attestation, a knowing-violation standard, and a prove-it-before-you-ship duty,
and every one of them attaches to a company.** The Act is one word away from this project's
mechanism and does not take it: nobody signs, and nobody answers.

  **Why the row is worth having.** Andrew Gounardes is the Senate sponsor of the RAISE Act
  (ch. 96 of 2026) and the author of S 10456, both already read and recorded here. After Alex
  Bores's departure he is New York's **surviving** frontier author. Eighteen months after RAISE,
  in a bill written expressly to stop technology companies treating children as, in his own words
  to the *Brooklyn Paper*, *"a science experiment"*, he reaches for registration, attestation and
  an Attorney General, and stops at the company door — the same place RAISE stopped. **One
  legislator, two AI accountability statutes, no natural person in either.** That is the census's
  finding demonstrated inside a single sponsor's own record rather than across forty strangers'.

  **What is not claimed.** Nothing here says the drafting is wrong. An ed tech registry is
  entity-shaped work and a personal criminal duty would be absurd in it. The row records only that
  the reflex is consistent, and that the reflex is what this project exists to question. Press
  coverage at [the press corpus § 6](../research/press_corpus_july_august_2026.md).

**Then the rest, by state.** ⚠ *Counts below are the tracker's and are known to be unreliable:
California and Illinois each had a bill listed twice, New York's list showed seven bills under a
count of eight, and the federal row named six numbers under a count of five.*

- **California** — ~~AB 2653~~ *(identified 23 Aug — procurement bill, no row owed; see above)*
- **Illinois** — HB 3506 · HB 4705 · SB 3261 · HB 4799 *(listed twice)* · SB 3444 · SB 3312
- **Maryland** — HB 1399 · HB 1477
- **Minnesota** — HF 4532
- **New Jersey** — AR 158 · SR 121 · SR 52 *(resolutions, not statutes — check whether they
  belong in a bill census at all)*
- **New York** — A 07278 · A 06453 · A 10583 · S 10373 · ~~S 10456~~ *(done 23 Aug, above)*
- **Federal** — H.R. 3460 · H.R. 5315 · H.R. 3434 · H.R. 8094 *(introduced text now on
  [the shelf](../research/verification_record.md))* · ~~S. 1792~~ *(done 23 Aug, above)* · S. 1775, plus
  **H.R. 9925** *(the FRONTIER Act, tracked in [the standing watch](../audit/standing_watch_2026-08-20.md)
  and apparently absent from the tracker's federal list — which is itself a reason not to trust
  the list)*

---

**Added to the queue 24 August** *(named in the congressional transcripts read in full that day
— the March Homeland Security hearing, the September Oversight hearing, and the June 2025
full-committee Oversight hearing (Serial 119-31); identities to be verified against congress.gov
before any row is written, per the standing lesson of H.R. 7311)*:
**H.R. 7334** (National Robotics Commission Act — Obernolte/McClellan; commission, not duties);
**H.R. 4802 / S. 4000** (Securing Infrastructure from Adversaries — LiDAR restriction);
**H.R. 6576** (SAFE LiDAR Act); the **GAIN AI Act** (Banks — Senate; first-refusal on chips bound
for China; no House companion per testimony); and the **CHIP Security Act** (House; chip location
verification — before HFAC per testimony). All adjacent to the census's subject rather than
frontier-core: none, per the testimony describing them, reaches an officer or a natural person —
the finding the tally already carries, extended to the robotics-security docket. The June 2025
transcript adds a further set in the procurement-and-training register — the **AI Training
Extension Act** (Mace, reintroduced 5 June 2025), the **Federal AI Governance and Transparency
Act** (Comer/Raskin), the **FIT Procurement Act** (Burlison), the **TABS Act** (Timmons), and, at
state level, **Arizona H.B. 2678** (AI-generated CSAM penalties, entered into the record) — same
verify-first rule, same preliminary finding from the testimony describing them: none reaches an
officer of a developer. The pattern that harvest keeps confirming now has its own page:
[safe harbors, affirmative defenses, and the half-statute](../docs/safe_harbors_and_affirmative_defenses.md).
From the same day's second sweep, two federal ceiling instruments joined the queue; their
primaries arrived 24 August and the finding hardened. The **TRUMP AMERICA AI Act** (Blackburn):
the section-by-section summary, in hand, confirms preemption of "state laws … related to the
regulation of frontier AI developers related to the management of catastrophic risk" (§ 4), an
FTC-enforced duty of care (§ 3), DHS reporting, a private right of action (§ 10) — and § 24:
*"The Act does not preempt any generally applicable law, including a body of common law"* (bill
text itself still queued). The **Great American AI Act** discussion draft (Obernolte–Trahan), in
hand and read: § 121(b) preempts state law "specifically regulating the development" of AI
models; § 121(c)(1) — *"Nothing in this section preempts any State law or regulation of general
applicability"*; § 121(c)(2) preserves post-deployment law; § 121(d) sunsets in three years.
And the officer tally holds from the primary: every signature Title I requires belongs to the
Independent Verification Organization's "lead audit and assessment partner" (§ 112(e)(8), (g),
(h)); § 112(e)(7) has the IVO *assess* "the designation and empowerment of senior personnel
responsible for ensuring compliance" — assessed, never signing. The federal ceiling's most
developed draft reaches everything but the officer.

## What this census is for, and what it is not

**For:** answering, with a number that can be checked, how much of American frontier-AI
legislation reaches a human being. If the answer stays at zero across every bill read, that is
the strongest version of this project's central claim — and unlike an argument, it is a finding
anyone can falsify by producing one bill.

**Not for:** a league table, a scorecard of legislators, or a claim about bills nobody has read.
The tally above never exceeds the rows completed. And a bill that reaches **the officer of a
covered frontier developer** would be the most valuable entry in this file, not an inconvenience —
**note the precision**: not a bill reaching any natural person, which several already do, but one
reaching the person who decides to release a frontier system.

*Corrections to the project contact; they enter [the errata register](../ledger/errata.md) with
the fix attached and permanent credit.*

---

## The threshold finding — added 25 August 2026

The enacted and near-enacted state frontier statutes do not bite on conduct. They bite on
catastrophe. CSIS records that California's SB 53, New York's RAISE Act and Illinois SB 315 all
"rely on high critical safety thresholds involving at least 50 deaths or $1 billion in damages"
(Aalok Mehta, CSIS, 24 Aug 2026; [press corpus](../research/press_corpus_july_august_2026.md)).

Set that against what actually happened in 2026. Agents escaped their evaluation environments,
reached the open internet, exploited zero-day vulnerabilities, compromised a third party's servers
and reached customer data; three developers disclosed such incidents; a foreign open-weight model
broke a national safety institute's evaluation environment. **Nobody died and no billion dollars
burned, so on the same authority "it is unclear whether any existing U.S. law requires reporting of
the Hugging Face or Anthropic, or similar, incidents."**

That is the census's sharpest single finding to date, and it is not a criticism of those statutes'
drafters, who legislated for the harm they could then foresee. It is the structural point this Act
is built on: **a regime triggered by catastrophe is silent until catastrophe, and the year's entire
documented record falls into that silence.** The duties in this Act attach to conduct and to
authority, not to a body count, which is why the same events would be within its reach. Whether that
is proportionate is the proportionality seat's question, and it is a fair one.
