# v3.4 Cure Branch — Drop-in Amendment Language (Working Draft)

> **STATUS — LANDED (19 August 2026).** Every cure below entered the statute verbatim
> at v3.4; the diff between this file and `model_act_v3_4.txt` is the review artifact.
> The housekeeping list at the foot was executed at the landing. The successor queue is
> [v3_5_cure_language.md](./v3_5_cure_language.md). This file is preserved unchanged below
> this line.

*Status: research draft for the public working branch. Cure language for maintainer review, keyed to `model_act_v3_3.txt` with exact anchor quotes for splicing. Cross-references: ERRATA E1–E5; the maintainers' cure queue (sixteen items, numbered as below). Bracketed matter remains an adopting-state choice. Not legal advice; named counsel review pending per the validation discipline. Nothing here is described as ready for introduction.*

*Convention: **ANCHOR** quotes v3.3 verbatim so the edit lands mechanically. **STRIKE/INSERT** gives the operation. **NEW TEXT** is the full inserted language.*

---

## CURE 1 — Deployer de-minimis and reliance rule
*Cures the deployer blast-radius defect (every wrapper a criminal-statute deployer); ERRATA E5. First in queue. Conduct- and configuration-based, never revenue.*

**Operation.** Designate the existing single paragraph of SEC. 2 as subsection **(a)**, headed "Duty."; append new subsection **(b)**.

**ANCHOR (end of SEC. 2):** "…until a rule first takes effect, the budget is that minimum."

**NEW TEXT — SEC. 2(b):**

> (b) Reliance by non-modifying deployers. A deployer that operates a covered system within a validated configuration, without material modification of the covered model and without attaching or granting tools, memory, retrieval, credentials, permissions, or external access beyond those identified in the validation on which it relies, discharges the duty of due care under subsection (a), as to the matters within the scope of that validation, by:
> (1) documented adoption, before deployment, of a validation under SEC. 3(b), or a provisional validation under SEC. 3(c)(2), prepared by the developer or provider of the covered system and identifying the model version and deployment configuration deployed;
> (2) preparation and retention under SEC. 12 of a manifest of every tool, memory, retrieval mechanism, credential, permission, and avenue of external access the deployer attaches or grants, demonstrating conformity to the validated configuration;
> (3) the monitoring within the deployer's control that the adopted validation or the applicable standards specify for the configuration; and
> (4) reporting under SEC. 9 of matters within the deployer's knowledge.
> Reliance under this subsection is unavailable to a deployer that knows, or consciously avoids knowing, of a material nonconformity in the adopted validation or in the deployed configuration, and lapses upon the deployer's material modification or material expansion of the covered system, from the time of that modification or expansion. Nothing in this subsection conditions any duty, or the discharge of any duty, upon the revenue, size, or resources of any person.

*Note for the changelog: this makes the explainer's startup sentence (E5) true on the face of the text — a non-modifying wrapper's duty is discharged by adoption, manifest, monitoring, and reporting.*

---

## CURE 2 — Controlling person narrowed; express exclusions
*Cures the executor-overreach defect (definition reached executors of others' decisions); ERRATA E1. Floor element (1).*

**ANCHOR (SEC. 4(a)):** "possesses or exercises material practical authority over a covered system through any of:"

**STRIKE:** "material practical authority" → **INSERT:** "final material independent decision authority"

**ANCHOR (end of SEC. 4(a)):** "…through any intermediary, entity, trust, or arrangement."

**INSERT after it:**

> The following, standing alone or in combination only with each other, do not constitute authority under this section: title, office, seniority, or status; professional credentials or technical ability; access to systems, weights, or infrastructure; the ministerial execution, implementation, or communication of a decision made by another; or the provision of advice, analysis, or recommendation to a person holding decision authority. Authority under this section is the authority to decide, not the capacity to act.

**Conforming edit (SEC. 4(b), final sentence):** after "Substance controls over title." insert: "Status is never a substitute for authority."

*Note: SEC. 6(e)'s "practical power" construction is untouched — power is the liability element; this cure narrows who is a controlling person at all. The engineer exemption is now written into the definitions, as the explainer promised.*

---

## CURE 3 — Provisional-validation rebuild; disclose-and-deploy becomes a report
*Cures the disclose-and-deploy defect; ERRATA E3 (with the SEC. 8 conforming edit below). Drives the floor rule.*

**ANCHOR (SEC. 3(c)(2)(B)):** "documents the conformity of the covered system, and of each entity's practices concerning it, with the interim standards, or discloses identified nonconformity and the compensating measures taken; and"

**STRIKE that subparagraph in full; INSERT:**

> (B) states, after reasonable inquiry and on the basis of the documented assessment, a reasonable documented conclusion that the covered system, and each entity's practices concerning it, materially conform to the interim standards. Where the assessment identifies nonconformity with any interim standard, the conclusion may be stated only if the assessment identifies, for each such nonconformity, an equivalent compensating measure in effect — a measure shown, by documented analysis against the risk the departed-from standard addresses, to provide protection equivalent to conformity — and states the analysis; and

**INSERT new paragraph after SEC. 3(c)(2)(C):**

> (D) Nonconformity reports. A document that discloses identified nonconformity without stating the conclusion subparagraph (B) requires, or whose compensating measures are not equivalent within the meaning of that subparagraph, is a nonconformity report and not a provisional validation. It shall be transmitted and retained as subparagraph (C) provides; it discharges no duty under SEC. 2 and satisfies neither this paragraph nor SEC. 5(a); and its transmission is a statement to the Agency for purposes of SEC. 5(d) and notice for purposes of SEC. 6(b)(1).

**Conforming edit (SEC. 3(c)(5), second sentence):** after "satisfies the duty of due care under SEC. 2 as to the matters conformed" insert ", a nonconformity report satisfying nothing under this paragraph".

---

## CURE 4 — Harm-tier rebuild
*The harm-tier findings. **Deferred by decision** (maintainer decision, to be recorded in the changelog on landing): research model only; out of bill one. No text lands on this branch. The rebuilt tier (recklessness toward the risk of the relevant injury; extreme indifference for any life ceiling; direct and proximate causation; no paperwork predicate; no mandatory minimum; state-native injury definitions) remains a bound research module.*

---

## CURE 5 — Direct and proximate causation
*Cures the but-for-only causation defect as applied to the existing tier and restitution.*

**ANCHOR (SEC. 6(b)(1)):** "is a but-for cause of death or of serious injury to any person"

**STRIKE/INSERT:** "is a but-for and proximate cause of death or of serious injury to any person"

**ANCHOR (SEC. 10(c)(2)(D)):** "\"But-for cause\" bears the meaning given in Burrage v. United States, 571 U.S. 204 (2014); that death or serious injury resulted,"

**STRIKE that opening clause; INSERT:**

> (D) "Results" requires that the violation be both a but-for cause, within the meaning given in Burrage v. United States, 571 U.S. 204 (2014), and a proximate cause of the death or serious injury: the death or serious injury must have been a reasonably foreseeable consequence of the violation and not the product of an independent, unforeseeable intervening cause. That death or serious injury so resulted,

*(SEC. 10(c)(4) already provides that "results" bears the same meaning as in paragraph (2); restitution is conformed automatically.)*

---

## CURE 6 — Insurance ban made prospective; restitution carved out
*Cures the retroactive-insurance and restitution-coverage defects.*

**ANCHOR (SEC. 7(b)(1)(A)):** "enter into, renew, or maintain a contract of insurance or other arrangement under which any person is covered, in whole or in part, against liability for an individual penalty, fine, disgorgement, or restitution imposed under this Act"

**STRIKE/INSERT (two edits):** "enter into, renew, or maintain" → "enter into, renew, or materially amend"; "penalty, fine, disgorgement, or restitution" → "penalty, fine, or disgorgement".

**INSERT new paragraphs after SEC. 7(b)(5):**

> (6) Application. Paragraph (1) applies to contracts and arrangements entered into, renewed, or materially amended on or after the effective date of this Act. A contract or arrangement in force on the effective date may be maintained until its first renewal, expiration, or material amendment, and in any event no longer than [twelve] months after the effective date, after which maintaining it is a violation of paragraph (1).
> (7) Restitution preserved. This subsection does not restrict the purchase or provision of insurance for, or the payment, advancement, or indemnification of, restitution ordered under SEC. 10(c)(4); amounts paid under any such arrangement shall be applied to restitution before any other liability, and no such payment extinguishes any other liability of any person.

---

## CURE 7 — No-chief-executive fallback
*Cures the declinable-office defect; ERRATA queue.*

**ANCHOR (SEC. 8, first sentence):** "the chief executive officer, and each controlling person designated by rule, shall personally certify"

**STRIKE/INSERT:** "the chief executive officer (or, where no such office exists, each natural person exercising the most senior executive authority over the entity, severally), and each controlling person designated by rule, shall personally certify"

**INSERT after the non-delegation sentence ("…performed through any designee."):**

> The Agency may by rule designate the certifying office or offices for forms of organization lacking a chief executive officer; no designation diminishes the several obligation stated in this section, and no entity may, by its form of organization, leave this section without an obligated natural person.

---

## CURE 8 — Agency-approval validation mode struck
*Cures the back-door permit-regime defect; ERRATA E4.*

**ANCHOR (SEC. 3(b)):** "(internal attestation, independent audit, accredited certification, or Agency approval)"

**STRIKE/INSERT:** "(internal attestation, independent audit, or accredited certification)"

**INSERT at the end of SEC. 3(b):**

> No standard, rule, or mode of validation under this Act may condition any deployment, expansion, or release upon the prior affirmative approval of the Agency or of any officer of this State.

---

## CURE 9 — Interim lineage default; records duty decoupled at a lower audit floor
*Cures the lineage-ambiguity defect.*

**ANCHOR (SEC. 1(b)(1)):** "Designation is prospective only."

**INSERT after it:**

> Until a rule under SEC. 3 first specifies the treatment of fine-tuning, distillation, merging, and aggregation: (A) a distinct model derived from a covered frontier model is itself a covered frontier model only if the compute applied in its derivation, together with the lineage compute otherwise attributable to it under this paragraph, exceeds the figure in this paragraph, or the Agency prospectively designates it; (B) derivation compute not exceeding [10^24] integer or floating-point operations does not, standing alone, extend a lineage; and (C) records sufficient to compute lineage under SEC. 12 shall be created and retained for any derivation whose compute exceeds [10^22] integer or floating-point operations, whether or not the resulting model is covered, the records duty of this subparagraph operating independently of coverage.

---

## CURE 10 — "Material expansion" defined in statute; rule elaborates, never supplies
*Cures the rule-only-definition defect.*

**ANCHOR (SEC. 1(b)(6)):** "\"Material expansion\": a change, defined by rule, that increases a covered system's capabilities, autonomy, external access, or permissions beyond its validated configuration."

**STRIKE the definition in full; INSERT:**

> (6) "Material expansion": a change that increases a covered system's capabilities, autonomy, external access, or permissions beyond its validated configuration, including the grant of a new class of tools, credentials, or permissions; the enablement of an autonomous external-access capability; or the removal or material weakening of a safeguard identified in the applicable validation. The Agency may elaborate this definition prospectively by rule and may not narrow it; the definition operates of its own force from the effective date, no rule being required.

---

## CURE 11 — Autonomous external-access capability: statutory description plus rule-hook
*Cures the undefined-trigger defect.*

**Operation.** Add new SEC. 1(b)(10) after paragraph (9).

**NEW TEXT — SEC. 1(b)(10):**

> (10) "Autonomous external-access capability": the capability of a covered system, in its deployed configuration, to initiate interactions with systems, services, accounts, or persons outside the control of the deploying entity — including network requests, execution of code affecting external systems, transactions, and communications — without the approval of a natural person for each interaction. The Agency may specify classes of such capability by rule; the absence of a rule neither suspends nor narrows SEC. 5(b) once the controls that section presupposes have been prescribed under SEC. 3.

---

## CURE 12 — Certification triggers defined; periodic batch cadence below the material line
*Cures the undefined-cadence defect; ERRATA E2. Supplies the statutory minimum definition of "material deployment."*

**ANCHOR (SEC. 8, first sentence):** "Before material deployment and following material change to a covered model or configuration,"

**INSERT after the first sentence's period ("…on the structure of 18 U.S.C. § 1350."):**

> For purposes of this section: "material deployment" means the first deployment of an identified model version in or into this State, and any deployment following a material expansion or a material change; "material change" means a change granting a new class of tools, credentials, or permissions, materially expanding capability or autonomy, or removing or materially weakening a safeguard identified in an applicable validation. The Agency may elaborate these definitions prospectively by rule and may not narrow them. Changes to a covered model or configuration below the material line shall be certified in a periodic certification covering every such change in the period, filed not less often than once in each [calendar quarter] in which any such change occurred; a periodic certification is a certification under this section, with the consequences this section and SEC. 6 attach.

---

## CURE 13 — Records offense: privilege preserved, facts reachable
*Cures the privilege-collision defect.*

**ANCHOR (SEC. 5(e)):** "access to or verification or copying of any such record."

**INSERT after it:**

> Nothing in this paragraph abrogates any privilege recognized by the law of this State; a good-faith assertion of privilege, made in the manner the law provides, is not a refusal under this paragraph. Underlying facts remain subject to discovery and subpoena from any source, per SEC. 12.

---

## CURE 14 — Near-miss: contained-by-design is recorded, not reported
*Cures the recursive near-miss defect.*

**ANCHOR (SEC. 9(a)):** "a serious near-miss, meaning an event that, but for intervention or chance, would have constituted an incident under this subsection"

**STRIKE/INSERT:** "a serious near-miss, meaning an event that, but for intervention other than controls operating as designed, or but for chance, would have constituted an incident under this subsection"

**ANCHOR (SEC. 9(a), final sentence):** "Behavior intentionally elicited in a sandboxed exercise and contained there is not an incident but shall be recorded."

**INSERT after it:**

> An event detected and contained by controls operating as designed, before any effect outside the systems of the entity whose controls contained it, is not an incident under this subsection but shall be recorded under SEC. 12.

---

## CURE 15 — Fallback recipient until the Agency exists
*Cures the agencyless-transmission defect.*

**ANCHOR (SEC. 12, first sentence):** "This Act takes effect [90] days after enactment;"

**INSERT immediately after that clause:**

> until the Agency is designated and organized to receive them, transmission to the Attorney General satisfies any requirement under this Act of transmission to the Agency, and the Attorney General shall transfer the materials to the Agency upon its organization;

---

## CURE 16 — Conduct-based controlled research
*Cures the undrafted-research-module gap; maintainer module, drafted.*

**Operation.** Append new subsection **(c)** to SEC. 2 (after the subsection added by Cure 1).

**NEW TEXT — SEC. 2(c):**

> (c) Controlled research deployment. Making a covered system available solely to authenticated researchers, under documented terms of access, within containment that (1) denies the system any autonomous external-access capability, (2) denies the persistence of credentials, permissions, and external effects beyond each session, and (3) is monitored, is a controlled research deployment. A controlled research deployment satisfies SEC. 5(a), and discharges the duty of subsection (a) as to it, upon a documented conformity assessment limited to the containment, authentication, monitoring, and access-term controls of this subsection, retained and transmitted as SEC. 3(c)(2)(C) provides. The duties of this Act attach in full upon any deployment, expansion, or release beyond the terms of this subsection, from the time of that deployment, expansion, or release. Nothing in this subsection limits SEC. 9 or SEC. 12, and behavior within a controlled research deployment remains subject to the recording rule of SEC. 9(a).

---

## REGS PATCH — the paywalled-standard defect
*`model_regulations_v1_draft.md`, incorporation table: the ISO/IEC 42001:2023 row incorporates a paywalled standard against SEC. 3(a)'s own rule ("All incorporated material shall be publicly available without charge"). Options, per the disposition: (a) strike the row; or (b) retain the control objectives by restating them in the regulations' own words (facts and control objectives are not copyrightable; the standard's text is), marked "restated, not incorporated." Recommended: (b), with a one-line note that accredited certification to the standard remains a permissible validation mode where an entity elects it — election is not incorporation.*

---

## HOUSEKEEPING ON LANDING

1. ERRATA E1–E5: flip each status line from "queued for the public working branch" to "landed on the working branch, [date]; tagged at v3.4."
2. CHANGELOG: one entry per cure, finding numbers cited; the five/one errata split restated.
3. Explainers: docs/03 sentences become true as written for E1 (engineer exclusion now express), E3 (disclose-and-deploy now a report), E4 (approval mode struck), E5 (wrapper rule); E2's accurate sentence gains the periodic cadence.
4. Conformity check before tagging: SEC. 13(b) severability ranks reference SEC. 2 "duties … as applied to a person in that person's capacity as a provider or deployer" — new SEC. 2(b) and (c) ride within that reference; no renumbering elsewhere; new SEC. 1(b)(10) collides with nothing (prior list ends at (9)).
5. The word this branch never uses: the one in the swear jar.
