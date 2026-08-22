# Already a crime, if you are a person

*SEC. 5 of this Act creates five offences. A reasonable reader asks whether they are novel, or
harsh, or the sort of thing a legislature has never asked of anybody. **The answer is that all
five are already crimes in the United States, for ordinary people, today** — most of them with
heavier maximum penalties than this Act proposes, several with no requirement of intent at all,
and every one of them applied routinely to individuals with no institution behind them.*

*This file exists because the objection to a frontier-officer duty is always that it would be
extraordinary. It would not be extraordinary. **It would be ordinary — applied to people it
currently is not applied to.** Companion to [the same conduct,
prosecuted](./the_same_conduct.md), which supplies the cases.*

---

## Who this is about

**About:** the **officers of frontier developers** — the companies training models above 10²⁶
operations, or spending nine figures on a single training run. On the enacted family's own
thresholds that is a **double-digit number of firms worldwide**, and inside them a smaller number of
people who decide what ships.

**Not about:** open-source contributors, startups, academic researchers, hospitals, schools,
employers, small operators, ordinary deployers and API customers, or **users**. *On deployers,
precisely: the Act has always defined deployer as a covered class (SEC. 1(b)(3)) and has always
given the thin ones a route to discharge the duty rather than an exemption from it — adopt the
upstream validation, keep the manifest, monitor, report (SEC. 2(b)). What the open queue would add
at [CURE 7](../audit/v3_5_cure_language.md) reaches a deployer only at consequential scale — mass
market, or into government, military, financial, health or critical-infrastructure functions — and
only for its own deployment decisions, never as the developer of a model it did not train. A
company using a commercial model through an API is not covered by that fact.*

**And the claim, stated precisely.** Not that no American law reaches a natural person over AI — it
does, readily; Nebraska's "operator" includes one, so a sole trader running a chatbot is personally
inside that statute. **What no American law does is place a duty on the officer of a covered
frontier developer for the decision to release.** The law reaches down, not up.

---
## The five limbs, and the statute that already reaches you

| SEC. 5 offence | Already a crime for a natural person under | Maximum | Intent needed? |
|---|---|---|---|
| **Shipping without validation** | 21 U.S.C. § 331 with § 333(a)(1) — introducing an adulterated or misbranded article into interstate commerce | 1 year; **3 years** with intent to defraud or mislead (§ 333(a)(2)) | **None.** A strict-liability misdemeanour |
| **Operating uncontrolled autonomous access that causes a breach** | 18 U.S.C. § 1030 — the Computer Fraud and Abuse Act | 1–10 years per count, enhanceable | Knowledge of unauthorised access; **no injury or proven loss required** |
| **Failing to report** | 18 U.S.C. § 4 — misprision of felony | **3 years** | Knowledge plus an affirmative act of concealment |
| **Lying to the State** | 18 U.S.C. § 1001 — false statements | **5 years** | Knowingly and wilfully. **No oath required** |
| **Destroying or withholding records** | 18 U.S.C. § 1519 — destruction or falsification of records | **20 years** | Knowingly, with intent to impede — **and no investigation need yet exist** |

**Read the right-hand columns before the left.** The heaviest penalty in the table is not for
killing anyone. It is twenty years for **destroying a document** — and § 1519 reaches conduct
undertaken merely "in relation to or contemplation of" a federal matter, meaning **the shredding is
a crime before anybody opens an investigation.** The second heaviest is five years for **saying
something untrue to a federal official**, sworn or unsworn, in any matter within federal
jurisdiction.

---

## Limb by limb

### 1. Shipping without validation

21 U.S.C. § 333(a)(1): *"Any person who violates a provision of section 331 of this title shall be
imprisoned for not more than one year or fined not more than \$1,000, or both."*

**No mental state appears in that sentence, and none is required.** This is the strict-liability
public-welfare misdemeanour that *Dotterweich* (1943) and *Park* (1975) built the responsible
corporate officer doctrine on top of — and it is the statute this Act is modelled on. A person who
introduces an adulterated article into commerce commits a federal crime whether or not they knew,
intended, or were personally careless.

**The comparison that does the work.** A shift supervisor at a food plant is inside that statute
today. The officer who decides to release a frontier system is inside no statute at all. The
difference is not culpability, scale, or the seriousness of the potential harm. It is which
industry a legislature has got round to.

### 2. Operating uncontrolled autonomous access that causes a breach

The Computer Fraud and Abuse Act reaches unauthorised access as such. [The
gallery](./the_same_conduct.md) sets out what that has meant in practice for five individuals:
announced exposure from ten years to four hundred and forty, sentences up to forty-one months, and
in not one case any physical injury or, mostly, any proven loss. One defendant was prosecuted for
reading a page a company had published by accident.

**On the misuse defence.** This Act excuses a developer where a third party misused the system —
*unless the controls against that class of misuse were simply absent.* That carve-out is not an
invention either. It is how the law already treats a person who leaves the means of harm
unsecured: the intervening wrongdoer does not break the chain where the defendant's own duty was to
guard against exactly that wrongdoer. Negligent-storage and entrustment offences run on the same
logic, and so does the ordinary rule that foreseeable criminal misuse is not a superseding cause.

### 3. Failing to report

18 U.S.C. § 4, misprision of felony: three years. Concealment of a felony you know about is itself
a crime, and it was the charge that reached **Uber's Chief Security Officer** in 2022 — a named
corporate officer, convicted, affirmed on appeal in 2025.

**And note what he was reached for.** Not the breach. The concealment. There was no provision under
which the security failure itself made anyone personally answerable, so the prosecution used an
obstruction statute and a concealment statute — borrowing, exactly as fifteen state attorneys
general later borrowed consumer-protection law to demand logs. **When the fitting provision does not
exist, the system reaches for whatever is nearest.** This Act's contribution is to supply the
fitting provision rather than another borrowing.

Reporting duties enforced by criminal penalty against ordinary individuals are unremarkable
elsewhere too: leaving the scene of an accident, mandatory abuse reporting in most states, and
failure to file a tax return (26 U.S.C. § 7203, a misdemeanour).

### 4. Lying to the State

18 U.S.C. § 1001: five years, for knowingly and wilfully making a materially false statement in any
matter within federal jurisdiction. **No oath. No proceeding. No requirement that anyone relied on
it.** An ordinary person who gives a false answer to a federal investigator has committed a
five-year felony.

SEC. 5(d) of this Act asks less than § 1001 already asks of everyone.

### 5. Destroying or withholding the records

18 U.S.C. § 1519, in full, because the length of it is the point:

> *"Whoever knowingly alters, destroys, mutilates, conceals, covers up, falsifies, or makes a false
> entry in any record, document, or tangible object with the intent to impede, obstruct, or
> influence the investigation or proper administration of any matter within the jurisdiction of any
> department or agency of the United States or any case filed under title 11, or in relation to or
> contemplation of any such matter or case, shall be fined under this title, imprisoned not more
> than 20 years, or both."*

**Twenty years.** Enacted as part of Sarbanes-Oxley, after Enron, precisely because a legislature
concluded that the destruction of a record can be as grave as the underlying wrong — and that the
duty must bite before an investigation exists, or it bites too late to matter.

This Act's SEC. 12 retention rule, and its records offence, ask for **less** than § 1519 already
asks. And the Act's privilege position is the conservative one: privilege is preserved; facts
remain reachable. The rule that a fact does not become privileged by being written down in a
lawyer's presence is not this project's innovation.

---

## What the table means for the objection

The objection is that personal criminal liability for shipping decisions would be a radical
extension of the criminal law into an industry that cannot bear it.

**Every limb of SEC. 5 already exists, aimed at individuals, mostly with heavier maxima, and one of
them with no intent requirement whatsoever.** A person who mislabels a jar is inside a
strict-liability federal offence. A person who shreds a document in contemplation of a federal
matter faces twenty years. A young man who downloaded articles he was entitled to read faced a
public figure of thirty-five.

**And the direction of the gap, stated exactly.** The five statutes above reach natural persons
without difficulty — including small operators, shift supervisors and sole traders. What none of
them reaches is **the officer of a covered frontier developer, for the decision to release.** The
law is not absent. It is pointed downward.

**The extension this Act proposes is not of the criminal law. It is of its reach.** The five duties
are the ordinary duties of a person who ships things, reports things, tells the truth to the
government and keeps the records. What is unusual is not that a statute would impose them. **It is
that, at the compute frontier, no statute currently does.**

---

*Every statutory quotation above was read at Cornell's Legal Information Institute on 21 August
2026 and is marked ⚠ R under [the confidence
rubric](./frontier_bill_census.md#the-confidence-rubric-governed-by-e15) — opened, not yet re-read
by a human eye, and not to be quoted in a filing until it is. Corrections to the project contact;
they enter [the errata register](../ledger/errata.md) with credit.*
