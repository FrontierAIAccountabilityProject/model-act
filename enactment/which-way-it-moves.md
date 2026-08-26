---
title: "Which way each provision moves"
parent: For Legislatures
nav_order: 6
---

# Which way each provision moves

*A reading of the Act by direction rather than by section number. Every provision below was read in
`model_act_v3_4.txt` on 25 August 2026, in one sitting, cover to cover. Where a claim here is not in
the tagged text it says so.*

**Why read it this way.** A statute can be described by what it prohibits, which is how the
[translation](./plain-english.md) reads it, or by what it *moves* — what leaves and does
not come back, what arrives and starts a clock, what passes through a structure without stopping.
The second reading is the one a defense team does first, because it shows where the exits are.

**And it is the reading that finds the asymmetries.** Anything that flows one way is a place the
drafter made a choice. Some of those choices are load-carrying and some are accidents, and the
difference is what a reviewer is for.

---

## Outward, and it does not come back

**A release is the point of no return, and the Act says so.** SEC. 1(b)(9) defines release as making
weights "available for download, transfer, or reproduction **outside the releasing entity's
control**," and provides that "a release is a deployment of a covered system for purposes of this
Act." Then the concession, in the same paragraph: **"duties in connection with a release are limited
to those capable of performance before the release."**

That sentence is the whole open-source question in twenty words. After release there is no halting,
no correcting, no restricting — so every duty that survives is a pre-release duty, and the officer's
window closes at the moment of publication. *A reviewer who thinks that makes the Act a de facto
release-permitting regime for open weights has the [open source lane's](../revision/worklist.md)
first question.*

**Deployment travels down a corporate structure and liability travels back up.** SEC. 1(b)(3):
"Deployment through an affiliate is deployment by the principal."

## Inward, and it starts a clock

**Notice arrives from anywhere, and it arrives at a person.** SEC. 9(b) runs the preliminary-report
clock from "credible notice to the entity **or any controlling person**." Not notice to a
compliance function, not notice through a channel: any controlling person.

**And the clock starts whether or not anyone looked.** The same subsection: the period runs from
when the incident was detected, "or **would have been detected by the monitoring the entity
certified it maintains under SEC. 8**." An entity that certified monitoring it did not perform is
treated as having known what that monitoring would have found. **This is the most quietly powerful
sentence in the Act**, and it is the reason the certification and the reporting clock are the same
mechanism seen from two ends.

**Notice can also be created by the defendant's own honesty, and this is a defect rather than a
design.** SEC. 3(c)(2)(D) provides that a nonconformity report "discharges no duty under SEC. 2 and
satisfies neither this paragraph nor SEC. 5(a); and its transmission is a statement to the Agency
for purposes of SEC. 5(d) and **notice for purposes of SEC. 6(b)(1)**."

SEC. 6(b)(1) is the felony tier, and its notice limb reaches a person who "deliberately fails to
halt a violation after notice." So filing an honest disclosure of nonconformity supplies the notice
element of the felony that a later failure to halt would complete. SEC. 6(b)(1) adds the same for
reports: "Notice under this paragraph includes any report or preliminary notice filed under SEC. 9
concerning the same class of risk."

**The candid filer is in a worse evidentiary position than the silent one, on the Act's own text.**
[CURE 15](../revision/proposals.md) is the drafted repair and it is unvalidated. *This is the
enforcement lane's sharpest live question.*

**And the same two sections run candor the other way, which nobody had put beside this.** SEC. 9(b)
starts the clock from what "would have been detected by the monitoring **the entity certified it
maintains under SEC. 8**." SEC. 8 provides that a certification "disclosing identified noncompliance
satisfies the duty to certify." So an entity that honestly discloses it does not maintain the
prescribed monitoring has, on the face of SEC. 9(b), certified **less** monitoring — and is deemed
to have known less. [CURE 14](../revision/proposals.md) identified this on 22 August as a
gaming problem and drafted the repair, measuring the counterfactual against the standard rather than
the entity's own certification.

**Read the two together and it is not two defects but one shape.** Through SEC. 8 and SEC. 9, the
Act **punishes candor about nonconformity and rewards candor about missing monitoring**. The
person who tells the truth about the system is worse off; the person who tells the truth about the
watching is better off. Neither result was chosen, both follow from routing evidentiary consequences
through documents the defendant writes, and **a reviewer who can say which one the drafter should
have preferred has answered a question this project has only been able to describe.**

## Deliberate ignorance costs the deployer its safe course, and costs the developer nothing

The Act uses the willful blindness idea **once**. SEC. 2(b), on the reliance path that lets a
non-modifying deployer discharge its duty: reliance "is unavailable to a deployer that knows, or
**consciously avoids knowing**, of a material nonconformity in the adopted validation or in the
deployed configuration."

**That is the only appearance of the doctrine in the statute, and it runs against the smallest actor
the Act reaches.** A downstream deployer forfeits its safe course for not looking. A controlling
person of the developer faces nothing of the kind, because SEC. 6 does not mention it.

The asymmetry is the wrong way round on any reading of the Act's own purpose, and it was not noticed
until the statute was read in one sitting on 25 August 2026
([E45](../corrections/corrections.md#e45--the-glossary-said-the-act-was-silent-on-willful-blindness-the-act-uses-it-once-against-the-wrong-person)).
[CURE 22](../revision/proposals.md) proposes the codified federal form — the Clean Air Act and
TSCA both provide that knowledge may be shown by "evidence that the defendant took affirmative steps
to be shielded from relevant information" — for SEC. 6(b). ⚠ *That federal language is quoted from a
secondary source and is unverified.*


## Authority passes through structures; responsibility does not pass out of them

Four provisions, each closing a different exit.

**Through entities.** SEC. 4(a): authority "may be held or exercised directly or indirectly,
individually or in concert with others, and **through any intermediary, entity, trust, or
arrangement**."

**Through appointments.** SEC. 4(c): "**Delegation does not relieve** a controlling person who
retains material authority... No appointment of a safety officer, compliance officer, committee,
subsidiary, contractor, or other intermediary shields a person who retains such authority."

**Through designees.** SEC. 8: "The chief executive officer's obligation **may not be delegated or
performed through any designee**." And, so that no corporate form escapes: "no entity may, by its
form of organization, leave this section without an obligated natural person."

**Through successors.** SEC. 12: "Dissolution, merger, conversion, division, or reorganization of an
entity does not abate any proceeding or extinguish any liability," and a successor "assumes the
predecessor's liabilities" — but "**nothing in this section transfers the criminal liability of any
natural person to any other person**."

**Note the direction of that last clause.** Entity liability follows the assets. Personal criminal
liability does not follow anything: it stays where it was incurred. Restructuring moves the company
and leaves the person behind.

## Money moves out and cannot be sent back

SEC. 7(b)(1) to (3) void insurance, indemnity, reimbursement and every disguised substitute —
"payment, loan, forgiveness of indebtedness, increase in compensation, gross-up, distribution, gift,
or other transfer of value whose purpose or predominant effect is to offset" the liability. Every
such arrangement is "**void and unenforceable in this State, whatever law is chosen to govern it**,"
with a constructive trust over anything received.

SEC. 10(e) closes it from the other side: "**Corporate payment of any penalty imposed on a natural
person does not extinguish individual liability and is a violation of SEC. 7(b).**" Paying it does
not discharge it, and paying it is itself an offense.

**One thing does flow back, and it is the exception that shows the design.** SEC. 7(b)(5) permits
insurance and advancement of "reasonable costs of defense," with repayment by a person "finally
adjudicated to have committed a knowing or wilful violation." That is **advance, then claw back on
an adverse final adjudication** — the same mechanism 8 Del. C. § 145(e) already uses, which is worth
knowing before anyone calls the provision novel. ⚠ *The Delaware comparison is unverified against
the code; see [the glossary](../authorities/glossary.md).*

## Records go in and never come out

**They are created before anyone needs them.** SEC. 12 requires "version identifiers, compute
records, evaluation results, tool and permission manifests, change histories, and the compensation
records upon which SEC. 7(a) operates," retained ten years from creation or five years after the
system last operates here, whichever ends later. SEC. 1(b)(1)(C) sets the records duty at a compute
figure **two orders of magnitude below coverage**, "whether or not the resulting model is covered,
the records duty of this subparagraph operating independently of coverage."

**They are frozen on notice.** From the moment the entity or any controlling person "has notice of a
critical safety incident, of an investigation, or of a proceeding," the records "shall be preserved
until the conclusion thereof."

**Confidentiality does not travel to the facts.** The reports may be sealed, but the exemption "does
not create any privilege for underlying facts, which remain subject to discovery and subpoena from
any source."

**And they survive both of the ways this Act could lose.** If a court severs a reporting duty,
SEC. 13(b)(5) provides that severance "does not sever the records duties or the offense that
enforces them." If Congress preempts one, SEC. 13(c)(2)(C) directs the Attorney General to preserve
"the obligation, under SEC. 12, to create and retain the records that would have supported the
report or certification."

**A preemption victory does not erase the record, and neither does a severability victory.** That is
the most consequential one-way provision in the Act and the one a defense team notices last.

---

## What flows one way in the defendant's favor

A reading that listed only the traps would be a dishonest reading. The same audit finds seven
provisions running the other direction, and they are not decoration.

**Nothing becomes retroactively unlawful.** SEC. 3(c)(3): "no conduct lawful when done becomes
unlawful by a later commencement, and no provisional validation is invalidated retroactively."
SEC. 1(b)(1): "Designation is prospective only." SEC. 12: "no retroactive liability."

**A suspension protects the conduct it covers, permanently.** SEC. 13(c)(3): no person "may be
convicted of an offense under this Act for conduct occurring during a period in which the provision
creating the offense stood suspended." And on revival, SEC. 13(d): "No person is liable under a
provision for conduct occurring before that date."

**Powerlessness is not a defense to be raised; it defeats the element.** SEC. 6(d): "Genuine absence
of power negates the element; it is not an affirmative defense."

**Status is never enough.** SEC. 4(a) excludes title, office, seniority, credentials, technical
ability, access, ministerial execution, and advice; "Authority under this section is the authority
to decide, not the capacity to act." SEC. 4(b) makes the chief-executive presumption **civil only**.

**The small deployer has a safe course.** SEC. 2(b), and expressly without a means test: "Nothing in
this subsection conditions any duty, or the discharge of any duty, upon the revenue, size, or
resources of any person."

**Contained research is carved out.** SEC. 2(c), the controlled research deployment.

**Third-party misuse is a defense.** SEC. 5(b): access procured by "a third party's intentional
misuse (including prompt injection or stolen credentials) is a defense unless the prescribed
controls against that class of misuse were absent."

**And two findings answer the two constitutional attacks before they are made.** SEC. 0(a)(4): no
provision "requires any person to express, adopt, endorse, or refrain from expressing any opinion,
characterization, viewpoint, or contested position, or to alter the output of any covered system."
SEC. 0(a)(5): the Act "draws no distinction between persons within and persons outside this State."

---

## What does not move at all, which is the problem

Two flows the Act was written to catch, and does not.

**Evaluation conduct.** Every duty arises "by reason of, the deployment, material expansion,
release, or continued operation of a covered system in or into this State, **and not otherwise**"
(SEC. 2(a)), and SEC. 1(c) confines the Act to conduct here. The 2026 conduct that motivated the
drafting was evaluation conduct, much of it offshore. **[OPEN QUESTION 4](../revision/proposals.md)
is this gap and it is the most consequential item in the repository.**

**The offense that matches the conduct.** SEC. 5(b) is gated on controls "prescribed under SEC. 3,"
and SEC. 3(c)(3) commences it only "when the controls it presupposes have been prescribed." On the
statute's own clock that is year four. Until then the subsection that most exactly describes an
agent reaching a third party's systems **cannot be charged at all**.

So the honest summary of the flow diagram is this. **Authority, notice, money and records all move
the way the drafter intended. The conduct does not.** What remains chargeable in the meantime is the
reporting failure and the certification — the paperwork, not the escape. See
[what a case would look like](./worked-case.md), which walks exactly that.

---

*Prompted by an outside reading that proposed twelve one-way flows in this Act. Eleven of its twelve
were sound and its statutory quotations were verbatim; the working through here is against the text
rather than against that list. Where this page differs from it, the text governs.*
