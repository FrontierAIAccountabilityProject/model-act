# Who has to tell you — the duty to disclose runs backwards

*Opened 22 August 2026, from a question put to the project: **why is the party that got breached the
one who has to disclose it, and why are they afraid to?***

*This file states a structural argument. **It is the least evidenced thing in this repository** and
is published at that strength deliberately — as a hypothesis with named checks owed, not a finding.
See the grading note at the end before quoting any of it.*

---

## Who this is about

**About:** where the legal duty to disclose a security failure lands, and who bears its cost.

**Not about:** any particular company's conduct in any particular breach. The examples below are
used for their structure. Nothing here alleges wrongdoing by anyone.

---

## 1. Three parties, and only one of them has to say anything

Take any large breach of software running in production. There are at least three parties:

**The party that wrote the defective code.** Ships a patch. Publishes a CVE with a severity score.
Owes no duty to any individual affected downstream, discloses to no regulator on their behalf, and
in the ordinary case bears no cost from the breach at all.

**The party that ran the software.** Must investigate, must notify regulators and affected people
under state breach-notification law, wears the headline, pays for credit monitoring, and is called
the victim.

**The people whose data it was.** Learn about it from a press release, often months late. Frequently
have no relationship with either of the first two parties and never chose to be in the database.

**The duty to disclose attaches to the middle one.** It does not attach upstream to whoever shipped
the defect, and it does not run to the people at the bottom except through the middle party's
obligation.

**So the person who decided the software was fit to ship tells nobody anything.** That is the same
vacancy [the census](./frontier_bill_census.md) finds in frontier statutes, appearing in a
completely different body of law.

---

## 2. And the disclosure duty is triggered by evidence — which is a thing you can not have

State breach-notification statutes generally turn on whether personal information **was, or is
reasonably believed to have been, acquired** by an unauthorised person. That is a sensible-looking
threshold. Read it as an incentive and it does something else.

**An organisation that logs comprehensively can tell what was taken, and must therefore disclose.**

**An organisation that logs almost nothing cannot tell, may honestly report that it found no
evidence of acquisition, and may owe no notification at all.**

> **The better your instrumentation, the more you must disclose. The worse it is, the less you must.**

⚠ **This is the central claim of this file and it is not yet established.** It is a reading of how
the statutory trigger interacts with logging practice. **This project has not read the statutes.**
What is owed is set out in § 5.

**If it holds, note what it makes of the rest of this repository.** Illinois requires an unredacted
audit report retained *"for as long as a frontier model is deployed plus 5 years."* New York's
S 6953-A required the same. **18 U.S.C. § 1519** puts twenty years on destroying a record to impede
a federal matter. **Every one of those provisions assumes the record exists.** A regime that
rewards never generating it in the first place is not defeated by any of them.

**And it is the same shape as the certification argument, inverted.** [Why a signature
works](./why_a_signature_works.md) records that Stewart Parnell's sentence came from a document he
signed that was untrue, and that Don Blankenship — who signed nothing of that kind — served twelve
months for twenty-nine deaths. **The law reaches the paper.** Which means the surest way to be
unreachable is to make no paper.

---

## 3. The word "victim" is carrying an argument

In consumer-credit and data-broker breaches the entity breached is routinely described as the
victim. **The people whose records were taken are frequently not that entity's customers**, have no
contract with it, cannot decline to be listed, and cannot leave.

**That is not an accusation. It is a description of the business.** A consumer-reporting agency's
data comes from the institutions that report to it, not from the people it reports on. The person in
the file is the subject of the product, not a party to it.

**So "victim" is doing real work.** It positions the breached entity as the injured party in the
public account of the event, which shapes what remedy is thought to be owed, and to whom.
[House language](./house_language.md) is about exactly this: a word that quietly assigns a role.

**The honest version needs three nouns, not two.** There is the party that was intruded upon; there
is the party whose information was taken; and there is the party whose software failed. **English
gives us one word — victim — and the public account usually spends it on the first.**

---

## 4. Why disclosure is feared, and what that costs everyone else

Disclosing a breach reliably produces a share-price fall, class actions, regulatory attention and a
permanent search result. **Not disclosing, where the trigger is not met, produces none of those.**
The incentive gradient runs against telling people.

**The cost of that is borne by people who are not party to the decision**, and it compounds: an
undisclosed breach is one nobody else can learn from. **Every organisation running the same software
stays exposed for as long as the silence lasts.**

**This is why mandatory disclosure exists at all.** The argument for it was never that the breached
organisation deserves punishment; it was that the information is a public good. **The gap this file
identifies is that the obligation was attached to the party with the least incentive to discharge it
and the most to lose by doing so — and not to the party that shipped the defect, who has neither the
incentive nor the obligation.**

---

## 5. What is owed before any of this is used

**Everything above is a structural argument built from general knowledge of how these regimes work.
It is the weakest material in this repository.** Grading it honestly:

| claim | status |
|---|---|
| Duty to notify attaches to the entity holding the data, not the software vendor | ⚠ believed general, **no statute read** |
| The trigger turns on evidence of acquisition | ⚠ believed general, **no statute read** |
| Therefore poor logging can reduce the duty | ⚠ **inference, not established.** The key claim |
| Breached entities face material disincentives to disclose | ⚠ uncontroversial, **unsourced here** |

**The checks, in order of value:**

1. **Read three state breach-notification statutes in full** — California, New York and Illinois are
   the natural set given what this project already holds — and record the exact trigger language.
2. **Establish whether any of them impose a logging or retention requirement** sufficient to prevent
   the "no evidence because no records" position. If one does, that is the model provision and this
   file's argument narrows to the states that lack it.
3. **Find whether a regulator has ever taken the position that inadequate logging does not excuse
   notification.** If so, the inference in § 2 is already law somewhere and should be cited rather
   than argued.
4. **Check whether any statute reaches the software vendor.** This project believes none does. That
   belief is untested.

⚠ **The line of inquiry came from anonymous public commentary** on breach reporting, which is not
evidence of anything and is not cited here as such. **It suggested a question. The question is worth
the work; the commentary is not a source.**

**Until items 1 and 2 are done, nothing in this file enters a filing, a sponsor package, an email or
a post.** [E15](../ledger/errata.md) exists because this project once graded a claim on who wrote a
source rather than on what it opened. This file has not opened anything.

---

*Corrections to the project contact — particularly from anyone who works in breach notification and
can tell us where this is wrong. They enter [the errata register](../ledger/errata.md) with the fix
attached and permanent credit.*
