MODEL REGULATIONS — FRONTIER ARTIFICIAL INTELLIGENCE CONTROLS
Companion instrument to the Model Act (v3.3 line). ASSEMBLY DRAFT 1, conformed at v3.3 assembly (chunk 5 §E.6).
[Bracketed numbers = adopting-state choices. Structure implements the two-document
architecture: the Act carries offenses and power; these rules carry
machinery, amendable by the Agency under SEC. 3 without reopening the Act.]

------------------------------------------------------------------
PART 1 — DEFINITIONS
1.1 "Unauthorized access": access to a system, data, or model weights for
which the person entitled to control them has not granted permission,
whether or not technological measures prevented or would have prevented
the access. A defect in, or absence of, technical access controls is not
a grant of permission. [Van Buren gates construction; FN8 resolved.]
1.2 "Become aware": an entity becomes aware when any employee or
contractor acquires information that reasonably suggests a reportable
incident has occurred. For the accelerated tier (Part 5.2), the clock
runs from awareness of a person with supervisory, technical, or
incident-reporting responsibilities. [21 CFR 803.3 pattern.]
1.3 "Information reasonably suggesting": any information, including
professional, scientific, or technical facts, observations, or opinions.
[803.50(c) pattern — evaluations and red-team findings qualify.]
1.4 "Near-miss": an event that, but for intervention or chance, would
have constituted a reportable incident. [ICAO Annex 13 Note 1 principle,
counterfactual form.]
1.5 "Serious injury": as defined in SEC. 1(b)(8) of the Act (21 C.F.R.
§ 803.3(w) pattern).
1.6 "Model version and configuration": the trained weights identified by
version, together with the tools, permissions, system prompts, and
deployment parameters under which they operate. Validation, certification,
suspension, and reporting all attach to this unit.

PART 2 — STANDARDS INCORPORATED (SEC. 3(a))
2.1 The following are incorporated AS THEY EXIST ON [date], each
independently reviewed and adopted by the Agency, which retains authority
to modify or reject any provision; no future version applies absent a new
rule; all incorporated texts available free of charge from the Agency:
| Standard | Identified version | Role | Validation mode (3.1) |
|---|---|---|---|
| NIST AI RMF 1.0 | NIST AI 100-1 (Jan 26, 2023) | governance baseline; due-care measuring stick | internal attestation |
| NIST Generative AI Profile | NIST AI 600-1 (Jul 26, 2024) | pre-deployment testing; incident disclosure; risk taxonomy (crosswalks to Act SEC. 9(a)) | independent audit |
| ISO/IEC 42001 | :2023 (Dec 2023) | certifiable AI management system | accredited certification |
| NIST SSDF | SP 800-218 v1.1 + SP 800-218A (2024) | secure development; weights integrity | independent audit |
WATCH LIST (not incorporated; future rule only): CAISI evaluation
guidance; SP 800-53 AI overlays; NIST Critical Infrastructure Profile
(concept, Apr 2026).

PART 3 — VALIDATION
3.1 Before material deployment of a covered system, and after any
material change, the entity shall complete validation of the identified
model version and configuration against the applicable Part 2 standards
and the Part 6 control objectives, and retain the validation package.
3.2 A material change includes any change to weights, tools, permissions,
or deployment parameters that could reasonably affect a controlled
capability or safety property, and any change designated by rule.

PART 4 — CERTIFICATION (SEC. 8)
4.1 Signatories: the chief executive officer (non-delegable) and each
controlling person designated by rule.
4.2 Trigger: before material deployment; after any material change.
4.3 The certification states, per model version and configuration:
 (1) I have reviewed the validation package for this version and
     configuration.
 (2) Based on my knowledge, it contains no untrue statement of material
     fact and omits no material fact necessary to make it not misleading.
 (3) The covered system, as deployed in this configuration, conforms to
     the standards applicable under Part 2, except as stated in the
     attached schedule of exceptions and compensating controls.
 (4) I am responsible for the authorization, monitoring, and incident-
     detection controls prescribed for this system; they have been
     designed, including to ensure that material information concerning
     the covered system — including adverse or anomalous evaluation
     results — is made known to the certifying officers, particularly in
     the period preceding certification; their effectiveness has been
     evaluated as of a date within [30] days; my conclusions are stated
     herein.
 (5) I have disclosed to the Agency and to the board's designated
     oversight body all significant deficiencies and material weaknesses
     in those controls, and any deception of safety or monitoring
     controls, and any misconduct, whether or not material, involving
     personnel with significant control roles.
 (6) All material changes to the model, configuration, tools,
     permissions, or controls since the prior certification are
     identified herein.
[SOX 302/906 adaptation. Rep. 4 is the monitoring the entity "certified
it maintains" for the SEC. 9(b) clock; rep. 5 feeds the SEC. 6(b) notice
wire; rep. 6 operationalizes material change.]

PART 5 — INCIDENT REPORTING (SEC. 9)
5.1 Reportable categories: per SEC. 9(a) taxonomy, including near-misses
under 1.4.
5.2 Clocks: (a) imminent-harm tier — notice within [24] hours of
awareness under 1.2's responsible-person trigger; (b) standard tier —
preliminary notice within [72] hours of entity awareness; (c) FULL REPORT
within [30] days of preliminary notice; investigation incompleteness does
not extend the deadline — report what is known and supplement.
5.3 Supplemental reports: material new information within [10] days of
awareness. [803.56 pattern.]
5.4 SAME-CLASS ESCALATOR: the Agency may designate an event class for
accelerated reporting; upon designation, every subsequent event of the
same nature involving the same or a substantially similar system reports
on the accelerated clock without further request. [803.53(b) pattern.]
5.5 A report is not an admission, but fixes notice for purposes of
SEC. 6(b)(1) as provided in the Act.

PART 6 — CONTROL OBJECTIVES [GMP pattern throughout: written /
followed / documented contemporaneously / reviewed by designated function]
6.1 Authorization boundaries: there shall be written authorization
boundaries for each covered system configuration; the boundaries shall be
enforced by technical controls; enforcement and exceptions shall be
logged contemporaneously; logs shall be reviewed by the designated safety
function at [interval], and the review documented.
6.2 Monitoring and detection: [same clock structure as Part 5] for anomalous
capability expression, unauthorized access attempts, and loss-of-control
indicators.
6.3 Halt capability: there shall be a written, tested procedure by which
deployment of any configuration can be suspended within [X hours];
tests shall be conducted at [interval] and documented.
6.4 Access control to weights: [Part 5 clock structure] covering personnel,
credentials, exfiltration monitoring.
6.5 Evaluation records: capability and safety evaluations shall be
documented at the time of performance and retained; adverse or anomalous
results shall be escalated in writing to the designated safety function
and to each certifying officer.
6.6 Change management: material changes require documented pre-change
review against Part 3.2.
[Enforcement logic throughout: absence of the writing or the record is
itself the violation — provable from the filing cabinet.]

PART 7 — SUSPENSION AND HALT (SEC. 10)
7.1 In personam: the Attorney General may seek an injunction restraining
any entity or controlling person from deployment or expansion in
violation of the Act.
7.2 In rem-style: the Agency or court may suspend an identified model
version and configuration; operation of a suspended configuration in this
State by any person with notice constitutes contempt and a new offense
under SEC. 5(a).
7.3 Emergency: ex parte suspension on probable cause of imminent risk of
death or serious injury; post-deprivation hearing within [10] days.
[FDCA 332/334 two-track, dangerous-to-health valve modernized.]

PART 8 — CIVIL PENALTY COMPUTATION (SEC. 10(a))
8.1 Per violation, per day the violation continues: up to $[1,000,000] per
violation per day or, after a prior final adjudication of a violation by
the same person, up to $[3,000,000] per violation per day, per SEC. 10(a).
8.2 Factors: seriousness; economic benefit or savings from noncompliance;
history; good-faith efforts; economic impact on the violator; other
matters as justice requires. [CWA 309(d) pattern.]
8.3 FLOOR: a penalty shall not be less than the economic benefit or
savings derived from the violation, as found by the court.
8.4 Monetary recoveries are deposited and applied per SEC. 10(f); awards
under SEC. 11 are paid from the fund it establishes.

PART 9 — WHISTLEBLOWER PROCEDURES (SEC. 11)
9.1 Reports: any channel designated by the Agency; anonymous through
counsel permitted; identity protected including at award.
9.2 Award: [10-30]% of monetary sanctions collected where sanctions
exceed $[1,000,000], per SEC. 11.
9.3 The Agency acts upon, or publishes a reasoned declination of, any
credible report within [180] days.
9.4 Security-sensitive material in reports is handled under Part 10.
[21F structure.]

PART 10 — RECORDS AND CONFIDENTIALITY (SEC. 12)
10.1 Retention: validation packages, certifications, logs, evaluation
records, and reports: for the periods provided by SEC. 12 of the Act.
10.2 Public-records exemption per the SEC. 12 sensitive-information
clause: channel protected; no use-immunity; underlying facts never
privileged. [CIRCIA-pattern protected channel; no use-immunity conferred.]
------------------------------------------------------------------
ASSEMBLY STATUS: assembly draft, released alongside Model Act v3.2 and
conformed to v3.3 at chunk 6 (Parts 5.5, 8.1, 8.4, 10.1, per chunk 5 §E.6;
Part 3 deliberately carries no interim clause — the interim regime lives in
SEC. 3(c) of the Act, per chunk 5 §E.6(e)). The Part 2 version pins await
re-pin at adoption (READ FIRST item 1). Bracketed figures are
adopting-state choices; source-pattern notes in brackets cite the lineage
of each part. Public domain.
