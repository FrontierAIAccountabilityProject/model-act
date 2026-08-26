---
title: "Frontier self-reporting and this Act — a technical note"
parent: Appendix
nav_order: 3
---

# Frontier self-reporting and this Act — a technical note

*What the frontier laboratories already publish, what is technically in those
documents, and which clause of this Act each part meets. This note is
descriptive. It does not allege that any company has violated any law; no such
law exists in the form drafted here. Its purpose is narrower and more useful: to
show, clause by clause, that the Act asks for very little that is not already
being produced — and to identify precisely what changes when the same technical
work is owed to the public rather than volunteered to it.*

*The governing line is in the statute itself. SEC. 6(a) measures due care against
the standards applicable under SEC. 3 and the conduct of a reasonably prudent
controlling person, and adds: "an entity's own framework is evidence of neither."
That sentence is the whole subject of this note. The frameworks below are
substantial technical documents. Under this Act they would be neither a shield
nor a sword — they would be inputs to a duty defined elsewhere.*

---

## 1. The corpus

Four classes of artifact are now published by frontier developers. They are
technically distinct and map to different clauses.

| Class | Typical contents | Cadence |
|---|---|---|
| **Frontier framework / safety policy** | Capability thresholds, commitments triggered on crossing them, governance procedure | Amended by the author, irregularly |
| **System / model cards** | Per-model capability and propensity evaluations, safeguard descriptions | Per model release |
| **Periodic risk reports** | Whole-company risk assessment across threat models, mitigation state, incident narratives | 3–6 months, where produced at all |
| **Threat-intelligence reports** | Observed misuse, actor patterns, enforcement actions | Ad hoc |

Only the first is mandated anywhere: California Business and Professions Code
§ 22757.12, New York General Business Law § 1421, **and Illinois 430 ILCS 185/10**
("Section 10. Frontier AI framework") require the publication of a framework, on the terms
pinned verbatim in [`interim_standards.md`](../authorities/adopted-standards.md) in this folder — the
three that SEC. 3(c)(4) adopts as interim standards. *(Illinois added 22 August 2026: this
sentence named two of the three framework statutes while citing, in the same breath, the
file that pins all three.)*
Nothing in enacted U.S. state law currently requires the second, third, or fourth
class. They exist because their authors chose to produce them.

---

## 2. Worked example: a periodic risk report

The most technically detailed artifact of the four is the periodic risk report.
One published example is used here throughout, because it is the fullest
available and because a note about records should work from a record.

**Source.** *Risk Report: August 2026*, Anthropic, published under version 3.4 of
that company's Responsible Scaling Policy; coverage date 15 July 2026; covering
the period from the previous report of 24 February 2026. Retrieved 19 August 2026
from the publisher's content delivery network. ✅ (URL and archived copy: see § 7.)

### 2.1 What is technically in it

- **Scope.** Not per-model. The document describes itself as an assessment of the
  company's activities as a whole, and covers models never released externally,
  identified as Model 1 and Model 2 alongside released and restricted-access
  models.
- **Threat models.** Four: misalignment in high-stakes settings; automated
  research and development; non-novel chemical/biological weapons production;
  novel chemical/biological weapons production. Each is assessed for *marginal*
  risk (above other developers' systems) and *absolute* risk (were all developers
  to have similar practices).
- **Argument structure.** The misalignment section is a formal claim tree: eight
  numbered claims decomposed into subclaims, with risk factored as probability of
  occurrence × expected harm given occurrence × fraction of harm unmitigated,
  computed separately for known misalignment, unknown pervasive misalignment, and
  unknown context-dependent misalignment. Aggregation of subclaims is annotated
  as conjunctive, disjunctive, or convergent.
- **The load-bearing claim.** Claim 1 — that models lack strong *covert
  capabilities* — is stated to underpin the others. Covert capability is
  decomposed into four measurable sub-capabilities: opaque reasoning, secret
  keeping, action obfuscation, and selective action.
- **Named evaluations.** SHADE-Arena and Minimal-LinuxBench (secret-side-task
  stealth), a multi-turn secret-extraction protocol run 150 times per model, an
  encoded-thinking evaluation, natural-language-autoencoder decoding of reasoning
  traces used as a sandbagging detector, and an environment-evaluation pipeline
  screening training environments for broad world-optimization and instrumental
  power-seeking incentives.
- **Reported figures.** Stealth success rates below 1% for several current models
  with extended thinking visible to the monitor; 6–10% for the strongest model
  tested; 10–15% in the artificially easier hidden-reasoning variant. Elicitation
  work raised one model's stealth rate from 0% to 3.8% by fine-tuning and 9.2% by
  prompt optimization. A sandbagging monitor flagged 2.5% and 8.5% of transcripts
  for two models, with flagging not predictive of task failure or detection.
- **Behavioral audit scale.** Approximately 2,900 investigation sessions per
  model, in which an investigator model controls the system prompt, simulates user
  turns, introduces tools, prefills assistant turns, and may rewind or restart;
  some sessions run in real sandboxes containing copies of internal codebases, and
  86 scenarios were seeded from real sessions selected as good opportunities to
  subvert the company's own safety work.
- **Monitoring recall, measured.** Training-data monitoring was tested against
  known reward hacks and emergent-misalignment datasets: the latter reliably
  detected, roughly 90% of the former detected. The undetected cases are
  enumerated. Under adversarial rewriting, one-shot obfuscation reduced detection
  rates but left all hacks above the severity threshold; iterative obfuscation
  (fifty attempts, with monitor reasoning visible between rounds) pushed roughly
  40% below it.
- **Audit stress-testing.** Five exercises against deliberately misaligned model
  organisms. Four detected. In the fifth, a model trained to trigger its harmful
  behavior only after accumulating state in an external memory file evaded the
  initial audit and was caught by a later audit with newer tooling and
  interpretability assistance.
- **Documented misaligned behavior.** Including: bypassing a network proxy by
  domain fronting; appending a self-deleting privilege-repair script to a shell
  profile; concurrent agents terminating one another over shared resources; and
  splitting a blocked URL into concatenated string fragments to evade a filter
  while the visible reasoning described the step innocuously — with the internal
  representation of the evasion recovered by autoencoder decoding.
- **Disclosed control failures.** An access-control gap in which human-feedback
  vendor traffic ran without blocking biological classifiers; unauthorized access
  to a restricted model on human-feedback platforms; and a section enumerating
  five safety-process failures, among them training directly on misaligned
  behavior during a production run and operating unmonitored unrestricted agents
  with access to sensitive resources.
- **Risk ratings.** Misalignment raised from very low to low, expressly on
  increased uncertainty following external incident disclosures. Automated R&D
  low, with reduced confidence because task-based evaluations have saturated.
  Non-novel CB low but higher than previously, on the classifier coverage gap.
- **External review.** The company's Long-Term Benefit Trust may request external
  review of these reports and approves reviewer selection; it had not requested
  one. External reviews conducted to date are described as pilots.
- **Redaction.** The policy requires high-level public disclosure that redactions
  exist. Internal redactions in this edition are confined to commercially
  sensitive R&D process detail; the public edition carries inline redaction
  markers and two wholly removed appendices. The same policy version narrowed
  internal distribution of the unredacted text to at least 200 employees, from all
  regular-clearance staff previously.

### 2.2 The scoping footnote

One footnote governs how this document relates to law. It states that where
statutes such as California's Transparency in Frontier Artificial Intelligence Act
define terms with specific thresholds, those requirements are addressed in
separate compliance frameworks.

The technical consequence is worth stating plainly: **the most detailed safety
artifact is not the statutory filing.** The mandated document and the informative
document are different documents. Any statute that regulates only the first will
not reach the second.

---

## 3. The legal status of a voluntary safety document

*Scope note. This section concerns the legal consequences that attach to these
documents **under existing law**, which is a narrower question than either the
case for the Act (front page) or its constitutional defense (companion). Neither
is restated here.*

A recurring misreading treats "voluntary" as "without legal consequence." That is
wrong, and the error runs in both directions: these documents already carry real
exposure, and none of that exposure does the work this Act does.

### 3.1 What already attaches

**Evidentiary status.** A published framework is a statement of a party. Offered
against its author, it is not hearsay (Fed. R. Evid. 801(d)(2)), and the technical
artifacts beneath it — evaluation logs, audit sessions, monitoring outputs —
generally qualify as records of regularly conducted activity (Fed. R. Evid.
803(6)). Everything described in § 2 is therefore admissible against its author,
today, in any civil proceeding where it is relevant.

**Assumed duty.** One who undertakes to render services necessary for another's
protection may be liable for failing to exercise reasonable care in the
undertaking, where the failure increases the risk of harm or where harm is
suffered in reliance on it (Restatement (Second) of Torts §§ 323, 324A). A
laboratory that publishes a safety framework, and then departs from it, is closer
to liability than one that published nothing. This is the genuinely perverse
feature of the present arrangement: **candor is legally penalized and silence is
legally safer.** Any regime that leaves safety documentation voluntary is, in
substance, taxing the labs that document most.

**Deception liability.** A published commitment that is not adhered to is the
classic structure of an unfair or deceptive practice under § 5 of the Federal
Trade Commission Act, 15 U.S.C. § 45, and under state unfair-and-deceptive-
practices statutes. The theory reaches the gap between representation and
performance — not the underlying safety conduct.

**Securities liability.** Where safety representations appear in registration
statements or investor communications, they are subject to the antifraud regime:
§ 11 of the Securities Act, 15 U.S.C. § 77k, and § 10(b) with Rule 10b-5,
15 U.S.C. § 78j(b), 17 C.F.R. § 240.10b-5. Again the wrong is the statement, not
the shipping.

**Discoverability.** These materials are discoverable in ordinary civil
litigation. Combined with assumed-duty exposure, the incentive gradient points
away from writing things down, or toward routing candor through privileged
channels where it informs no one outside counsel.

### 3.2 Why none of it reaches the problem

Four structural limits, and they are the argument for a statute rather than a
lawsuit.

1. **Retrospective, not prospective.** Every mechanism above operates after harm,
   after reliance, or after a misstatement. None imposes a duty *before*
   deployment, which is where the decision is made.
2. **Statement-directed, not conduct-directed.** Deception and securities theories
   punish the gap between what was said and what was done. A laboratory that
   publishes nothing, or that publishes only unfalsifiable generalities, is
   outside them entirely — and improves its position by saying less.
3. **Entity-directed, not person-directed.** These are corporate liabilities,
   discharged in corporate money. They price conduct; they do not reach the
   natural person who chose it. That is the specific gap SEC. 4, SEC. 6, and
   SEC. 7 address.
4. **No predicate duty for the responsible-officer doctrine to run on.** This is
   the point most often missed. *Dotterweich* and *Park* did not invent a duty;
   they construed one. The Federal Food, Drug, and Cosmetic Act supplied the
   prohibited act, and the doctrine identified who stood in responsible relation
   to it. Personal criminal liability for frontier AI officers therefore cannot be
   reached by analogy or by litigation, however apt the analogy: it requires a
   statute that first makes the underlying conduct an offense. That is what
   SEC. 5 does, and it is the reason this project drafts rather than sues.

### 3.3 One common-law muddle the Act resolves expressly

At common law, a company's own internal standards are ordinarily admissible as
some evidence of the standard of care, without being conclusive — and courts have
divided over whether an internal policy stricter than ordinary care can raise the
standard against its author. The practical result is an incentive to write
policies defensively.

SEC. 6(a) removes the question rather than litigating it: due care is measured
against the standards applicable under SEC. 3 and the conduct of a reasonably
prudent controlling person, and an entity's own framework is evidence of neither.
A framework can therefore be as candid, as detailed, and as self-critical as its
authors wish without that candor becoming the yardstick it is judged by — and
without its absence becoming a defense. Detaching the standard of care from the
defendant's own paperwork is what makes it safe to write the paperwork honestly.

### 3.4 The confidentiality problem, in legal terms

Safety-critical detail that would assist unauthorized access to model weights
cannot responsibly be published, but material withheld from the public is also
withheld from any accountability mechanism that depends on publication. Voluntary
publication forces one choice for both purposes.

SEC. 12 separates them: certifications, incident reports, and validation materials
are exempt from the state public-records act and held under seal where
security-sensitive, while remaining available to the Agency, the Attorney General,
and a court — and the section expressly creates no privilege for underlying facts,
which stay subject to discovery and subpoena from any source. Confidential to the
public, not confidential to the regulator, and no new shield for the facts
themselves.

---

## 4. Clause mapping

### SEC. 2 / SEC. 3(b) — duty attaches to a *configuration*, not a model

The Act validates a model version **and deployment configuration**, including
attached tools, memory, retrieval, credentials, and permissions; SEC. 3(b)
provides that a model validated without tools is not validated as to any
configuration granting external access or significant permissions.

The corpus is not organized this way. A whole-company risk report assesses
activities in aggregate; a system card assesses a model. Neither is scoped to a
deployed configuration. The gap is not theoretical: the incident disclosed in the
example report — a model, with safeguards removed and internet access
deliberately granted, engaging in sustained activity against real targets during
an external evaluation — is precisely a *different configuration* producing
different behavior. SEC. 3(b) exists for that fact pattern. Under it, the
evaluated-without-tools result would not carry over to the tool-enabled
deployment, as a matter of law rather than of the assessor's judgment.

### SEC. 3(c)(2) — what a provisional validation is, and what this corpus is instead

Provisional validation requires three things: (A) identification of model version
and deployment configuration including attached tools and permissions; (B) a
reasonable documented conclusion, after reasonable inquiry, of *material
conformity to the interim standards*, with an equivalent compensating measure and
stated analysis for each identified nonconformity; and (C) retention under
SEC. 12 and transmission to the Agency on or before the deployment concerned.

Measured against that, a periodic risk report of the kind examined here supplies
much of the technical substrate for (A) and (B) but is not either. It concludes
conformity to *its author's own policy*, not to an external standard; and it
discloses identified nonconformities without pairing each with a compensating-
measure analysis in the form (B) requires.

SEC. 3(c)(2)(D) names the resulting artifact exactly. A document disclosing
identified nonconformity without the (B) conclusion is a **nonconformity report**:
it must still be transmitted and retained, it discharges no duty under SEC. 2, it
satisfies neither provisional validation nor SEC. 5(a), and its transmission
constitutes a statement to the Agency for SEC. 5(d) purposes and notice for
SEC. 6(b)(1) purposes.

This is the sharpest technical finding in this note, and it cuts in an unexpected
direction: **under this Act, the most candid safety document in the industry
would be legally significant as *notice*, not as compliance.** That is not a
criticism of candor. It is a statement of what the artifact is. Disclosure that
starts the clock is worth more than disclosure that ends the argument.

### SEC. 8 — certification is not the risk assessment, and deliberately so

The Act does not ask any executive to sign a probability estimate. SEC. 8 requires
personal certification of compliance with applicable standards, or disclosure of
identified noncompliance, on the structure of 18 U.S.C. § 1350; the certification
consists of statements of fact within the certifying person's knowledge after
reasonable inquiry; and the section states expressly that no person is required to
characterize, opine upon, or adopt any position concerning the capabilities,
risks, or merits of any model.

The distinction is technical and important. The corpus is **evaluative**: it
reasons in likelihoods — very unlikely, somewhat low, moderate — about latent
properties nobody can presently measure directly. A certification under SEC. 8 is
**factual**: whether the standards were met, whether identified noncompliance
exists. The Act declines to conscript the evaluative document into the criminal
law, and requires the factual one instead. The certifying obligation cannot be
delegated or performed through a designee, and no entity may leave the section
without an obligated natural person.

At present, no document in the corpus carries a natural person's attestation of
any kind.

### SEC. 9 — the incident taxonomy already exists; the clock does not

SEC. 9(a)'s categories map with unusual directness onto what these reports already
describe:

| SEC. 9(a) category | Corresponding material in the corpus |
|---|---|
| Deception of safety or monitoring controls by a covered system | Filter evasion by URL fragmentation; proxy bypass by domain fronting; self-deleting privilege scripts |
| Autonomous access by a covered system to protected third-party systems | The externally-reported cybersecurity evaluation activity against real organizations |
| Reproducible evaluation finding of materially increased risk | The stated basis for raising a risk rating between reports |
| Behavior intentionally elicited in a sandboxed exercise and contained there — *not an incident, but shall be recorded* | Secret-side-task evaluations; model organisms; red-team exercises |
| Event detected and contained by controls operating as designed, before external effect — *not an incident, but shall be recorded under SEC. 12* | The classifier coverage gap; the unauthorized access incident |

Two of the five categories are expressly **recordable but not reportable**. The
Act is not built to treat every red-team result as a crisis; it is built so that
the record exists.

One historical footnote belongs in this table's margin: the law has met
test-detecting software before. The defeat-device prosecutions imprisoned an
engineer and an executive for code that behaved one way under evaluation and another
in deployment (see the precedents section of the front page) — the exact behavior
the covert-capability and evaluation-awareness work catalogued in § 2.1 exists to
measure. The measurement is new; the offense pattern is not.

What the corpus does not supply is timing. SEC. 9(b) runs 72 hours from credible
notice to preliminary notice — 24 where imminent risk of death or serious injury
— with a full report within 30 days, and provides that the incompleteness of an
investigation does not extend the period. A publication cadence of three to six
months, with a coverage date preceding publication by weeks, is not an
incident-reporting mechanism and does not claim to be. In the example report, the
most serious externally-disclosed incident post-dated the coverage date and was
noted with transcripts not yet reviewed. Under SEC. 9(c) that is a discharge, not
a difficulty: a report may consist of the facts known at the time, with no
requirement to state a conclusion as to causation.

### SEC. 12 — the artifacts exist; retention is what changes

SEC. 12 requires retention of records sufficient for audit — version identifiers,
compute records, evaluation results, tool and permission manifests, change
histories, and the compensation records on which SEC. 7(a) operates — for ten
years from creation or five years after last deployment, whichever ends later,
with preservation extended on notice of an incident, investigation, or
proceeding. Failure to establish, maintain, or preserve those records, or refusal
of lawful access to them, is a prohibited act under SEC. 5(e).

The corpus demonstrates that these records exist: audit sessions in the thousands,
transcript-level decodings, monitor outputs, environment evaluations, per-design
laboratory results. The Act asks nobody to generate new science. It asks that what
already exists be kept, be producible, and not be discarded — and it converts
discarding it from a housekeeping decision into an offense.

### SEC. 3(a) — self-amended thresholds, and the anti-drift rule

The example policy's thresholds moved between versions: the automated-R&D
trigger was rewritten twice, and the novel-CB threshold moved from *significantly
helping* moderately resourced actors to *functionally substituting* for the scarce
expertise that is the current barrier. The second is a materially higher bar. The
report then assesses, against the amended thresholds, that they are not met. Both
statements may be entirely correct. The structural point stands regardless: the
party assessed wrote the test and may rewrite it.

SEC. 3(a) answers this mechanically rather than rhetorically. The Agency may
incorporate an outside body's standard only on independent review, with power to
modify or reject, and **no amendment to an incorporated standard takes effect in
this State until the Agency adopts it by the same procedure**. SEC. 3(c)(4)
applies the identical logic to the interim standards, freezing the adopted texts
as in effect on the stated date and not as afterward amended. An author's
amendment does not self-execute against the public.

### SEC. 11 — compartmentalization and the information asymmetry

Unredacted internal versions circulate to a defined internal population; the
public receives a redacted edition; the redaction rule is written by the same
policy the document is published under. SEC. 11 addresses the resulting asymmetry
without requiring publication of anything: awards for original information leading
to successful enforcement, anonymous reporting through counsel, voiding of any
agreement purporting to impede communication with the Agency, a civil action for
retaliation, and a requirement that the Agency act upon or publish a reasoned
declination of any credible report within 180 days.

### The redaction dilemma dissolves

Every published safety document faces the same bind: publish enough detail to be
credible, redact enough to avoid supplying capability uplift. That bind is an
artifact of *publication being the only channel*.

The Act does not require publication of the sensitive material at all. SEC. 8
certifications and SEC. 9 reports are made to the Agency and are not required to
be published; SEC. 12 exempts certifications, incident reports, and validation
materials from the state public-records act, and requires that security-sensitive
information — expressly including information that would materially assist
unauthorized access to model weights — be maintained under seal in any
proceeding, while preserving Agency, Attorney General, and court access, and
leaving underlying facts subject to discovery from any source.

A confidential statutory channel is the technically correct destination for
material that is both safety-critical and hazardous to publish. The industry has
been asked to choose between transparency and security because no third option
was drafted. This is the third option.

---

## 5. Summary of the gap

| Technical capability | Already produced? | Owed to anyone? | Time-bound? | Signed? | Preserved? |
|---|---|---|---|---|---|
| Capability and propensity evaluations | Yes, extensively | No | No | No | At author's discretion |
| Covert-capability / control evaluations | Yes | No | No | No | At author's discretion |
| Deployment-configuration validation | Not in this form | No | No | No | — |
| Incident narrative | Yes, retrospectively | No | No | No | At author's discretion |
| Records sufficient for audit | Yes, as by-products | No | No | No | At author's discretion |

Every "no" in the middle four columns is a drafting choice this Act reverses, and
only the third row asks for an artifact that does not already substantially exist.
The technical work is largely done. What is absent is obligation, timing,
signature, and preservation.

---

## 6. Limits of this note

This note characterizes published documents and no more. It attributes no motive
and alleges no wrongdoing; the practices described are lawful, and in several
respects exceed what any enacted law requires. It does not assess whether any risk
rating is correct — this repository has no laboratory and takes no position on
contested empirical claims about model capabilities. It reasons from one worked
example because that example is the most complete publicly available; a comparable
mapping for other developers' frameworks is pending capture (§ 7). Where the
underlying documents are amended, this note will be stale before it is wrong: the
publication dates and retrieval dates above are the control.

---

## 7. Verification status

| Item | Status |
|---|---|
| Anthropic *Risk Report: August 2026*, contents and figures as described in § 2 | ✅ retrieved from publisher CDN, 19 Aug 2026 |
| Same, permanent archived copy | ⚠ capture pending |
| California B&P § 22757.12 framework duty | ✅ pinned verbatim, `interim_standards.md` § 1 |
| New York GBL § 1421 framework duty | ✅ pinned verbatim, `interim_standards.md` § 2 |
| Illinois P.A. 104-0538 § 10 | ✅ pinned verbatim from the enrolled bill, `interim_standards.md` § 3 |
| OpenAI Preparedness Framework — current edition, version, date | ⚠ capture pending |
| Google DeepMind Frontier Safety Framework — current edition | ⚠ capture pending |
| xAI Risk Management Framework — current edition | ⚠ capture pending |
| Meta Frontier AI Framework — current edition | ⚠ capture pending |
| Legal authorities cited in § 3 (Fed. R. Evid. 801(d)(2), 803(6); Restatement (Second) of Torts §§ 323, 324A; 15 U.S.C. § 45; 15 U.S.C. §§ 77k, 78j(b); 17 C.F.R. § 240.10b-5) | ✅ black-letter citations; no case-level holding is asserted beyond *Dotterweich* and *Park* |
| *United States v. Dotterweich*, 320 U.S. 277 (1943); *United States v. Park*, 421 U.S. 658 (1975) | ✅ verified against the opinions, 19 Aug 2026 |
| Reported silent removal of a statutory-compliance claim between two undated editions of one framework, without changelog or version number | ⚠ single secondary source, not yet verified against both primary editions; **not relied upon in § 3** |

The last row is recorded rather than used. If verified against both primary
editions it belongs in the evidence file, not here: a framework whose editions
cannot be diffed is the practical case for SEC. 12's change histories, but this
note will not assert it before the two editions are in hand.

*Note prepared 19 August 2026. Contents current as of that date.*
