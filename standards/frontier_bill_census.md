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
| Of those read: **actually frontier bills** | **5 of 7** — two were chatbot statutes miscategorised by the tracker |
| Highest penalty found | **\$20,000,000 per day** (H.R. 9917), payable by the company |

*The count moved from six to seven on 22 August 2026, and the artefact was the same one twice.
**California SB 53 had been read in full on 21 August — by a human eye, from the chaptered text,
graded ✅ — and was not being counted**, while its findings were being used in the rows below it:
the officers-and-directors line cited SB 53 inside a denominator SB 53 was not in. That is the
Illinois error repeated, so the fix is the same: it is counted now. The tally's promise is that it
never exceeds the rows actually read, and the corollary — that it must not fall short of them
either — is the half that failed twice. **Standing rule, added here: a row graded ✅ enters the
count in the same edit that grades it.***

*The count moved from four to six on 21 August 2026. New York was read that day. **Illinois had
been read and answered since the 20th and was not being counted**, because its row sits above as
the worked example rather than in the rows section — an accounting artefact of the file's layout,
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
| ⚠ **R** | The primary **was opened**, but read through automated retrieval — a summarising model stood between the text and the row | a human re-read; the locator is already in hand |
| ⚠ **F** | The primary **was not opened**; the row rests on a secondary quoting it | a fetch, and the fetchable locator is named in the row |
| ⚠ **P** | Read in part — some sections opened, others not | name which sections |

**Every row in this file currently carries ⚠ R**, and that is the honest grade rather than a
modest one: [E13](../ledger/errata.md) records automated retrieval nearly putting a false
correction into the evidence file, and [E14](../ledger/errata.md) records two primary sources
conflicting where a single fetch had reported certainty. Nothing here is quoted in a filing, a
post or a sponsor package until a human has read the enrolled text.

---

## The worked example — what a completed row looks like

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

**Confidence. ⚠ R.** The enacted chapter text was opened and searched directly, not read from a
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

#### Two details that settle how the text travelled

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

**So the finding is not that New York dropped an audit.** New York's bill, six days before it
passed, required a developer to designate senior personnel, had an independent auditor verify that
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
protection and a bar on unreasonably risky deployment. **Struck at the B amendment, six days before
passage.** Louisiana drafts the audit without the signature. **Dies in chamber.** Illinois enacts it.
**One survivor in four attempts.**

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

**The audit travelled. The signature did not.** On the Digest, Louisiana carries the annual
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
From the same day's second sweep, two federal ceiling instruments join the queue ⚠ (both carried
on reporting; verify against congress.gov before any row): the **TRUMP AMERICA AI Act**
(Blackburn — preemption of state frontier catastrophic-risk law; an FTC-enforced duty of care;
*"expressly preserves generally applicable law"*) and the **Great American AI Act** discussion
draft (Obernolte–Trahan, 4 June 2026 — three-year, development-only preemption; third-party
"Independent Verification Organizations"). Preliminary finding, same as ever, held to the
reporting: neither is described as reaching an officer.

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
