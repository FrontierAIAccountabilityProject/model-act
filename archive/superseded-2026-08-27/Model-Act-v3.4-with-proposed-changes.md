# Model Act — Frontier AI Public Welfare Offenses

## v3.4, with every proposed change shown against the provision it would alter

*27 August 2026. **This is not a version of the Act.** It is the tagged text of v3.4 with each
drafted repair set beneath the provision it changes, so the statute and its known defects can be
read in one document. Assembled from the drafting record and the open-items list; where the three
disagree, those two govern.*

**Nothing below is adopted.** The operative text remains v3.4 as tagged. Each proposed change
carries the level of what is missing before it could land:

**1 Citation** — a quotation is verified and its page is not; needs a reporter print.  
**2 Document** — the text is not held at all.  
**3 Reading** — everything is held and nobody has read it against the Act.  
**4 Counsel** — read, and the reading does not settle it.  
**5 Decision** — advised on, and still a choice about what this Act should be.

**Nine of the twenty-three drafted amendments have been validated by nobody**, and the note says so
where that is true.

---


## SEC. 0. FINDINGS AND PURPOSE

### As tagged at v3.4

```
SEC. 0. FINDINGS AND PURPOSE (UNCODIFIED).
(a) The Legislature finds:
(1) Covered systems are deployed to, operated within, and made available to residents of this
State, and the deaths, injuries, intrusions and losses this Act addresses occur to persons and
property within this State.
(2) The protection of persons within this State from death and serious injury, and the punishment
of those whose failures of care cause it, is among the oldest and most traditional exercises of
this State's police power, and is the same power by which this State punishes homicide, reckless
endangerment, the endangerment of the public by the sale of adulterated or unsafe goods, and false
statements made to its own officers.
(3) The duties this Act imposes arise from the deployment, material expansion, release, or
operation of a covered system in or into this State, or from conduct in this State in relation to
such a system. This Act imposes no duty on any person by reason of research, training, or
development that neither occurs in this State nor concerns a covered system deployed or released
in or into this State.
(4) No provision of this Act requires any person to express, adopt, endorse, or refrain from
expressing any opinion, characterization, viewpoint, or contested position, or to alter the output
of any covered system. The statements this Act requires are statements of fact within the
knowledge of the person making them, made to a regulator.
(5) This Act draws no distinction between persons within and persons outside this State. It
confers no advantage on any in-state person and imposes no obligation on an out-of-state person
that it does not impose on an in-state person engaged in the same conduct with respect to the same
system.
(6) The obligations this Act imposes are, in substance, the obligations that responsible
developers, providers, and deployers of covered systems already represent that they discharge, and
the incremental burden of compliance is small in relation to the revenues of the persons on whom
it falls.
(7) This Act supplements and does not displace the generally applicable criminal and civil law of
this State, which applies to conduct concerning covered systems as it applies to all other
conduct.
(b) Purpose. The purpose of this Act is to place personal responsibility for the safety of covered
systems deployed, operated, or released in or into this State upon the natural persons who hold
practical authority over them, on the doctrine of United States v. Park, 421 U.S. 658 (1975), by
means that operate upon private conduct occurring in or directed into this State.
```

### Proposed changes

#### Decision 4 — SEC. 2(a) and SEC. 1(c): the Act does not reach the conduct it was written after

***Level 5.** Limb (i) ruled to land; limb (ii) open — extraterritoriality*

*The entry proposes no splice; see the drafting record.*

#### Amendment 19

*Never drafted — number and title only*


## SEC. 1. CLASSIFICATION AND DEFINITIONS

### As tagged at v3.4

```
SEC. 1. CLASSIFICATION AND DEFINITIONS. (a) Offenses under this Act are public welfare offenses
within the meaning of Morissette v. United States, 342 U.S. 246 (1952), except where a greater
mental state is expressly required.
(b) In this Act: (1) "Covered frontier model": a foundation model whose training and lineage
compute (initial training plus fine-tuning, reinforcement learning, and material modification
along the model's lineage, excluding unrelated experimental runs, as further specified by rule,
including the treatment of fine-tuning, distillation, merging, and aggregation) exceeds 10^26
integer or floating-point operations; or any model designated by the Agency under SEC. 3 as
frontier-equivalent by capability. The compute figure is a bright-line trigger; capability
designation under SEC. 3 reaches models below it. Designation is prospective only. Until a rule under SEC. 3 first
specifies the treatment of fine-tuning, distillation, merging, and aggregation: (A) a distinct
model derived from a covered frontier model is itself a covered frontier model only if the
compute applied in its derivation, together with the lineage compute otherwise attributable to
it under this paragraph, exceeds the figure in this paragraph, or the Agency prospectively
designates it; (B) derivation compute not exceeding [10^24] integer or floating-point operations
does not, standing alone, extend a lineage; and (C) records sufficient to compute lineage under
SEC. 12 shall be created and retained for any derivation whose compute exceeds [10^22] integer
or floating-point operations, whether or not the resulting model is covered, the records duty of
this subparagraph operating independently of coverage. (2) "Covered
system": a deployed configuration of a covered frontier model, including tools, memory, retrieval,
credentials, and permissions attached to it. (3) "Developer," "substantial modifier," "provider,"
"deployer": the entity that respectively trains, materially modifies, makes available, or operates
a covered model or system, directly or through any affiliate. Deployment through an affiliate is
deployment by the principal. Personal, noncommercial operation of a covered model for a person's
own use is not deployment. (4) "Controlling person": as defined in SEC. 4. (5) "Critical safety
incident": as defined in SEC. 9(a). (6) "Material expansion": a change that increases a
covered system's capabilities, autonomy, external access, or permissions beyond its validated
configuration, including the grant of a new class of tools, credentials, or permissions; the
enablement of an autonomous external-access capability; or the removal or material weakening of
a safeguard identified in the applicable validation. The Agency may elaborate this definition
prospectively by rule and may not narrow it; the definition operates of its own force from the
effective date, no rule being required. (7) "Unauthorized access": access to a system, data, or model weights for
which the person entitled to control them has not granted permission, whether or not technological
measures prevented or would have prevented the access; a defect in, or absence of, technical
access controls is not a grant of permission. (8) "Serious injury": an injury or illness that is
life-threatening, results in permanent impairment of a body function or permanent damage to a body
structure, or necessitates medical or surgical intervention to preclude such permanent impairment
or damage; "permanent" means irreversible, excluding trivial impairment or damage, per 21 C.F.R.
§ 803.3(w). (9) "Release": making the weights of a covered frontier model available for download,
transfer, or reproduction outside the releasing entity's control. A release is a deployment of a
covered system for purposes of this Act; duties in connection with a release are limited to those
capable of performance before the release. Nothing in this Act restricts any person's use, study,
or modification of lawfully obtained weights, except as part of the deployment of a covered
system. (10) "Autonomous external-access capability": the capability of a covered system, in its
deployed configuration, to initiate interactions with systems, services, accounts, or persons
outside the control of the deploying entity — including network requests, execution of code
affecting external systems, transactions, and communications — without the approval of a natural
person for each interaction. The Agency may specify classes of such capability by rule; the
absence of a rule neither suspends nor narrows SEC. 5(b) once the controls that section
presupposes have been prescribed under SEC. 3.
(c) Jurisdiction. This Act applies to conduct occurring in this State, to covered systems made
available to residents of this State, and to conduct intended to produce and producing substantial
effects within this State. Conduct occurring outside this State is relevant under this Act only as
evidence bearing on an element of an offense committed in or into this State. No person incurs a
duty under this Act by reason of conduct that neither occurs in this State nor concerns a covered
system deployed, released, or made available in or into this State. A person who does not deploy a
covered system in or into this State, does not make it available to residents of this State, and
does not release its weights, is not subject to this Act as to that system.
```

### Proposed changes

#### Amendment 1 — "Serious injury" source moves to 18 U.S.C. § 1365(h)(3)–(4)

***Level 4.** Changes what the Act requires; needs counsel*

**Current text —**

> (8) \

**Would become —**

> (8) "Serious bodily injury": bodily injury which involves (A) a substantial risk of
> death; (B) extreme physical pain; (C) protracted and obvious disfigurement; or
> (D) protracted loss or impairment of the function of a bodily member, organ, or mental
> faculty. "Bodily injury" means (A) a cut, abrasion, bruise, burn, or disfigurement;
> (B) physical pain; (C) illness; (D) impairment of the function of a bodily member,
> organ, or mental faculty; or (E) any other injury to the body, no matter how temporary.
> Per 18 U.S.C. § 1365(h)(3)–(4).

#### Amendment 6 — SEC. 1(b)(1): the developer's own designation as a third route into scope

***Level 4.** Four required amendments unmet*

**Current text —**

> exceeds 10^26 integer or floating-point operations; or any model designated by the Agency under SEC. 3 as frontier-equivalent by capability.

**Would become —**

> exceeds 10^26 integer or floating-point operations; or a foundation model that its developer has designated, described, marketed, or publicly held out as a frontier model, or as operating at or near the frontier of artificial-intelligence capability — whether by so describing the model itself, or by so describing any safety, preparedness, risk-management, evaluation, or red-team framework, program, or function that governs the model — including a holding-out in a published framework or policy, in the name, charter, or mandate of an internal safety or red-team function, in product or marketing documentation, or in a public statement by a controlling person of the developer; and a holding-out within this subparagraph is not undone by its later withdrawal, deletion, or amendment; or any model designated by the Agency under SEC. 3 as frontier-equivalent by capability.

**Would become —**

> This subparagraph attaches to the developer that trained or materially modified the model. A person that only makes available, operates, integrates, resells, or deploys another developer's model does not become a developer, or a controlling person of a developer, by describing itself, its services, or that model as frontier.

#### Amendment 13 — SEC. 1(b)(1)(B): say "sever," not "extend"

***Level 4.** Open-source implications are policy*

**Current text —**

> (B) derivation compute not exceeding [10^24] integer or floating-point operations does not, standing alone, extend a lineage;

**Would become —**

> (B) a derivation whose compute does not exceed [10^24] integer or floating-point operations does
> not cause the resulting model to inherit any lineage compute of any antecedent model, and the
> resulting model is not a covered frontier model by reason of any antecedent model's compute; where
> a derivation exceeds that figure, the lineage compute of the antecedent model is attributable to
> the resulting model for purposes of subparagraph (A);

#### Amendment 16 — SEC. 1(b)(7): a deception limb, because *Van Buren* excludes what actually happened

***Level 2.** *Van Buren* not held*

**Current text —**

> a defect in, or absence of, technical access controls is not a grant of permission.

**Would become —**

> Access obtained by means of a false identity, a fabricated persona, a false statement of fact
> material to the grant, or content designed to induce another system or person to act on a false
> premise, is access for which permission has not been granted, notwithstanding that permission was
> formally given; but a mere violation of a term of service or use policy, without such falsity, is
> not unauthorized access.

#### Amendment 7 — the covered frontier enterprise: scope follows the ecosystem, duty follows the function

***Level 3, held.** Seven required amendments unmet*

**Current text —**

> The Agency may specify classes of such capability by rule; the absence of a rule neither suspends nor narrows SEC. 5(b) once the controls that section presupposes have been prescribed under SEC. 3.

**Current text —**

> each controlling person as to the exercise of the authority that person holds.

**Current text —**

> Liability is several as to each person independently meeting the elements of this Act.


## SEC. 2. PUBLIC WELFARE DUTY

### As tagged at v3.4

```
SEC. 2. PUBLIC WELFARE DUTY. (a) Duty. No covered system may be deployed in or into this State, or
materially expanded, unless each controlling person has exercised due care to ensure the system's
compliance with the safety, authorization, monitoring, incident-reporting, and deployment
standards applicable under SEC. 3. A duty under this Act arises upon, and by reason of, the
deployment, material expansion, release, or continued operation of a covered system in or into
this State, and not otherwise. Each duty under this Act attaches to the actor who controls the
relevant risk: the developer as to model evaluation and weight security; the provider and deployer
as to configuration, tools, permissions, and monitoring; the releasing provider as to pre-release
evaluation — including evaluation of the model as it can be modified, such as by removal of
safeguards or fine-tuning within a rule-specified compute budget — tamper-resistance assessment,
and weight security up to the moment of release; each controlling person as to the exercise of the
authority that person holds. The compute budget within which modification of a model is to be
evaluated shall be specified by rule and shall not be less than the greater of [one] percent of
the covered model's training and lineage compute, as computed under SEC. 1(b)(1), or [10^24]
integer or floating-point operations; until a rule first takes effect, the budget is that minimum.
(b) Reliance by non-modifying deployers. A deployer that operates a covered system within a
validated configuration, without material modification of the covered model and without
attaching or granting tools, memory, retrieval, credentials, permissions, or external access
beyond those identified in the validation on which it relies, discharges the duty of due care
under subsection (a), as to the matters within the scope of that validation, by: (1) documented
adoption, before deployment, of a validation under SEC. 3(b), or a provisional validation under
SEC. 3(c)(2), prepared by the developer or provider of the covered system and identifying the
model version and deployment configuration deployed; (2) preparation and retention under
SEC. 12 of a manifest of every tool, memory, retrieval mechanism, credential, permission, and
avenue of external access the deployer attaches or grants, demonstrating conformity to the
validated configuration; (3) the monitoring within the deployer's control that the adopted
validation or the applicable standards specify for the configuration; and (4) reporting under
SEC. 9 of matters within the deployer's knowledge. Reliance under this subsection is unavailable
to a deployer that knows, or consciously avoids knowing, of a material nonconformity in the
adopted validation or in the deployed configuration, and lapses upon the deployer's material
modification or material expansion of the covered system, from the time of that modification or
expansion. Nothing in this subsection conditions any duty, or the discharge of any duty, upon
the revenue, size, or resources of any person.
(c) Controlled research deployment. Making a covered system available solely to authenticated
researchers, under documented terms of access, within containment that (1) denies the system any
autonomous external-access capability, (2) denies the persistence of credentials, permissions,
and external effects beyond each session, and (3) is monitored, is a controlled research
deployment. A controlled research deployment satisfies SEC. 5(a), and discharges the duty of
subsection (a) as to it, upon a documented conformity assessment limited to the containment,
authentication, monitoring, and access-term controls of this subsection, retained and
transmitted as SEC. 3(c)(2)(C) provides. The duties of this Act attach in full upon any
deployment, expansion, or release beyond the terms of this subsection, from the time of that
deployment, expansion, or release. Nothing in this subsection limits SEC. 9 or SEC. 12, and
behavior within a controlled research deployment remains subject to the recording rule of
SEC. 9(a).
```

### Proposed changes

#### Decision 2 — SEC. 2 / SEC. 9: does the duty reach an evaluation run with safeguards disabled?

***Level 5.** Whether a configuration decision is a covered act*

*The entry proposes no splice; see the drafting record.*


## SEC. 3. DESIGNATED AGENCY; STANDARDS; COMMENCEMENT

### As tagged at v3.4

```
SEC. 3. DESIGNATED AGENCY; STANDARDS; COMMENCEMENT. (a) The [designated state agency, board, or
commission] ("the Agency") shall adopt standards for covered systems by rule, after notice and
opportunity for technical submissions. The Agency may incorporate a specifically identified
version of a standard developed by another body only upon its own independent review, with power
to modify or reject, and no amendment to an incorporated standard takes effect in this State until
the Agency adopts it by the same procedure. All incorporated material shall be publicly available
without charge. Standards under this section shall be limited to safety, authorization,
monitoring, incident-reporting, and deployment controls for covered systems; shall be technically
feasible and evidence-based; and shall be proportionate to the risks presented.
(b) The Agency shall specify for each standard the mode of validation (internal attestation,
independent audit, or accredited certification). Validation attaches to an
identified model version and deployment configuration. A model validated without tools is not
validated as to any configuration granting external access or significant permissions. No
standard, rule, or mode of validation under this Act may condition any deployment, expansion,
or release upon the prior affirmative approval of the Agency or of any officer of this State.
(c) Commencement.
(1) Immediate operation. This Act operates from its effective date. The offenses under SEC. 5(c),
SEC. 5(d), and SEC. 5(e); the reporting duties of SEC. 9; the records duties of SEC. 12; and the
provisions of SEC. 1, SEC. 4, SEC. 6, SEC. 7, SEC. 10, SEC. 11, SEC. 13, and the remainder of
SEC. 12 arise and operate from the effective date, and do not depend upon the promulgation of any
standard, the adoption of any rule, or any other act of the Agency. No duty arises under SEC. 2,
and no offense lies under SEC. 5(a), before the provisional commencement of paragraph (2); no
offense lies under SEC. 5(b) before commencement under paragraph (3). This paragraph governs time;
SEC. 1(c) and SEC. 2 govern to whom, and by reason of what conduct, a duty attaches.
(2) Provisional commencement. Beginning [180] days after the effective date, and until superseded
under paragraph (3), the duties of SEC. 2 and the offense of SEC. 5(a) operate on the basis of
provisional validation, and the certification duty of SEC. 8 operates from the same day, the
applicable standards for its purposes being the interim standards of paragraph (4). Provisional
validation of a covered system consists of a documented conformity assessment, prepared or adopted
by an entity that develops, releases, provides, or deploys the covered system, that: (A)
identifies the model version and deployment configuration, including the tools, memory, retrieval,
credentials, and permissions attached; (B) states, after reasonable inquiry and on the basis of
the documented assessment, a reasonable documented conclusion that the covered system, and each
entity's practices concerning it, materially conform to the interim standards — where the
assessment identifies nonconformity with any interim standard, the conclusion may be stated only
if the assessment identifies, for each such nonconformity, an equivalent compensating measure in
effect (a measure shown, by documented analysis against the risk the departed-from standard
addresses, to provide protection equivalent to conformity) and states the analysis; and (C) is retained as a record under SEC. 12
and transmitted to the Agency on or before the deployment, material expansion, or release to which
it relates. Provisional validation attaches to the identified model version and deployment
configuration; a system provisionally validated without tools is not validated as to any
configuration granting external access or significant permissions.
(D) Nonconformity reports. A document that discloses identified nonconformity without stating
the conclusion subparagraph (B) requires, or whose compensating measures are not equivalent
within the meaning of that subparagraph, is a nonconformity report and not a provisional
validation. It shall be transmitted and retained as subparagraph (C) provides; it discharges no
duty under SEC. 2 and satisfies neither this paragraph nor SEC. 5(a); and its transmission is a
statement to the Agency for purposes of SEC. 5(d) and notice for purposes of SEC. 6(b)(1).
(3) Standards commencement. Upon the promulgation of standards under subsection (a) and the
running of a compliance period of [90] days, validation in the mode specified under subsection (b)
is the validation SEC. 5(a) requires for any deployment, material expansion, or release occurring
thereafter, and provisional validation ceases to satisfy SEC. 5(a) except as to covered systems
deployed before that day, for which the transition period of SEC. 12 runs from that day. The
offense under SEC. 5(b) commences when the controls it presupposes have been prescribed under this
section and the same compliance period has run. Conduct is judged by the standards applicable to
it at its time; no conduct lawful when done becomes unlawful by a later commencement, and no
provisional validation is invalidated retroactively. [The Agency shall propose initial standards
under subsection (a) within [540] days of the effective date.]
(4) Interim standards. The interim standards are the frontier artificial intelligence framework
duties enacted at Section 22757.12 of the California Business and Professions Code (ch. 138,
Stats. 2025), Section 1421 of the New York General Business Law (ch. 96, L. 2026), and Section 10
of the Illinois Artificial Intelligence Safety Measures Act (P.A. 104-0538), each as in effect on
[1 August 2026], which are adopted for the purposes of this Act as they so exist and not as they
may afterward be amended, repealed, suspended, or invalidated in the enacting jurisdiction. For
those purposes: (A) the duties apply to every covered frontier model and covered system, and to
each entity that develops, releases, provides, or deploys one, without regard to any revenue
threshold, exemption, effective date, phase-in date, or territorial term of the enacting
jurisdiction; (B) a duty to publish, or to transmit any document to an officer, agency, or the
public of an enacting jurisdiction, is performed under this Act by transmission to the Agency, and
publication is permitted but not required by this Act; (C) provisions respecting assessment or
audit by a third party do not apply, and conformity may be documented internally, independent
assessment being at the entity's election; (D) provisions respecting incident reporting,
penalties, enforcement, fees, assessments, and whistleblowers are not adopted, those subjects
being governed from the effective date by SEC. 9, SEC. 10, and SEC. 11 of this Act; and (E)
conformity documented for the purposes of any of the three enactments in an enacting jurisdiction
is conformity with the corresponding interim standard under this Act, to the extent of the matters
documented. The Agency shall make the adopted texts publicly available without charge.
(5) Element and due care. Absence of required validation is an element of the offense under
SEC. 5(a); the validation required is the provisional validation of paragraph (2) or the
validation of subsection (b), as applicable to the conduct at its time. Documented conformity with
the standards applicable at the time — interim or promulgated — satisfies the duty of due care
under SEC. 2 as to the matters conformed, a nonconformity report satisfying nothing under this
paragraph. An entity's own frontier artificial intelligence
framework, written and followed as an interim standard requires, is an object of the conformity
this paragraph credits; standing alone it remains evidence neither of due care nor of its absence,
per SEC. 6(a).
```

### Proposed changes

#### Amendment 10 — SEC. 3(c)(3): interim controls, so SEC. 5(b) is not dormant until year four

***Level 4.** Writes four technical controls in as offense elements*

**Current text —**

> offense under SEC. 5(b) commences when the controls it presupposes have been prescribed under this section and the same compliance period has run.

**Would become —**

> offense under SEC. 5(b) commences when the controls it presupposes have been prescribed under this
> section and the same compliance period has run; provided that from [180] days after the effective
> date, and until that commencement, SEC. 5(b) operates on the basis of the following interim
> controls, which the Agency may supersede but not narrow: (i) authentication of the covered system
> to each external system, service, or account it may reach, and denial by default of reach to any
> other; (ii) an enumerated allowlist of network destinations, maintained as a record under SEC. 12;
> (iii) logging of every external interaction initiated by the covered system, retained under
> SEC. 12; and (iv) a means, exercisable by a natural person, of terminating the system's external
> access.

#### Amendment 15 — SEC. 3(c)(2): a disclose-and-fix valve, because the text currently punishes candor

***Level 4.** The 90-day shelter's renewal is unstated*

**Would become —**

> (E) Disclosed nonconformity; limited period. Where a nonconformity report under subparagraph (D)
> is transmitted before the deployment, material expansion, or release to which it relates, or
> within [30] days of the entity's discovery of the nonconformity, no offense lies under SEC. 5(a),
> and no notice arises under SEC. 6(b)(1), by reason of the disclosed nonconformity for [90] days
> from transmission, provided that the report states a remediation plan and a completion date, the
> entity does not materially expand the covered system during that period, and the entity transmits
> a provisional validation or a further nonconformity report on or before the completion date. This
> subparagraph does not apply to a nonconformity the entity knew of and did not disclose, and
> confers no protection as to any matter not disclosed. The Agency, or the Attorney General before
> the Agency is organized, may shorten the period on written notice where the nonconformity presents
> an imminent risk.

#### Amendment 23 — SEC. 3(c)(4)(B): restore the publication the allied statutes require, on their own redaction terms

***Level 4.** Changes what the Act requires*

**Current text —**

> a duty to publish, or to transmit any document to an officer, agency, or the public of an enacting jurisdiction, is performed under this Act by transmission to the Agency, and **publication is permitted but not required by this Act**.

**Would become —**

> (B) A duty to publish under an interim standard is performed under this Act by publication in the
> manner that standard requires, together with transmission to the Agency; a duty to transmit a
> document to an officer or agency of an enacting jurisdiction is performed under this Act by
> transmission to the Agency alone. A person publishing under this subparagraph may redact, and
> shall describe the character and justification of each redaction, on the terms of Section
> 22757.12(f) of the California Business and Professions Code as adopted by this paragraph; the
> unredacted document is a record under SEC. 12 and is retained, produced, and treated as SEC. 12
> provides.

**Would become —**

> Nothing in this subparagraph requires the publication of a report under SEC. 9, a certification
> under SEC. 8 beyond the facts stated in any register maintained under that section, or validation
> materials under subsection (b) or paragraph (2). Those materials are governed by SEC. 12.

#### Amendment 26 — SEC. 3(c)(4): the disapplication list, repaired against a full read of all three adopted standards

***Level 3.** Research complete; needs a reading*

**Current text —**

> (C) provisions respecting assessment or audit by a third party do not apply, and conformity may be documented internally, independent assessment being at the entity's election.

**Current text —**

> (D) provisions respecting incident reporting… are not adopted, those subjects being governed from the effective date by SEC. 9, SEC. 10, and SEC. 11 of this Act.

**Would become —**

> (C) provisions requiring assessment or audit by a third party do not apply, independent assessment
> being at the entity's election and conformity being documentable internally; but provisions
> requiring an entity to state whether, and to what extent, third-party assessment was used **do**
> apply, and are performed as subparagraph (B) provides.

#### Amendment 20 — the chosen-stick clause: conformity outside the Act credits nothing

***Level 4.** Too harsh on good-faith compliers?*

*The entry proposes no splice; see the drafting record.*

#### Decision 1 — SEC. 3(c)(4): does Connecticut become a fourth interim standard?

***Level 2.** Connecticut's enacted act not held*

*The entry proposes no splice; see the drafting record.*


## SEC. 4. CONTROLLING PERSONS

### As tagged at v3.4

```
SEC. 4. CONTROLLING PERSONS. (a) A controlling person is any natural person who, regardless of
title, possesses or exercises final material independent decision authority over a covered system through any of:
(1) deployment, expansion, or access decisions; (2) budgets, compute, infrastructure, or risk
policy; (3) appointment, removal, direction, or supervision of persons exercising such authority;
or (4) ownership, voting, contractual, governance, or other rights conferring practical power to
prevent, halt, restrict, or correct a deployment or violation. Authority under this section may be
held or exercised directly or indirectly, individually or in concert with others, and through any
intermediary, entity, trust, or arrangement. The following, standing alone or in combination
only with each other, do not constitute authority under this section: title, office, seniority,
or status; professional credentials or technical ability; access to systems, weights, or
infrastructure; the ministerial execution, implementation, or communication of a decision made
by another; or the provision of advice, analysis, or recommendation to a person holding decision
authority. Authority under this section is the authority to decide, not the capacity to act.
(b) The following are presumed controlling persons in any civil proceeding, absent proof of
genuine absence of practical authority: (1) the chief executive officer of a developer or
provider, or of any entity that directly or indirectly controls a developer or provider; and (2)
any person holding ownership, voting, contractual, or governance rights sufficient, alone or in
concert with others, to direct or replace the management of a developer or provider, or of any
entity that directly or indirectly controls it. In any criminal proceeding, such status is
evidence from which the trier of fact may infer controlling-person status; the prosecution retains
its burden on every element under SEC. 6(d). Substance controls over title. Status is never a
substitute for authority.
(c) Non-delegable responsibility. Delegation does not relieve a controlling person who retains
material authority to prevent, halt, restrict, or correct a violation. No appointment of a safety
officer, compliance officer, committee, subsidiary, contractor, or other intermediary shields a
person who retains such authority. The designation of any person as responsible for compliance
neither diminishes nor creates any presumption against the responsibility of any other controlling
person. Liability is several as to each person independently meeting the elements of this Act.
```

### Proposed changes

#### The presumption that reaches the people this Act was written for stops at the criminal door

***Level 5. The largest open question in the Act.***

SEC. 4(b)(2) presumes a controlling person is anyone holding rights sufficient to direct or
replace management — and **that presumption operates in civil proceedings only**. Where the
remedy is money the person holding the votes is presumed responsible; where it is prison, not.
That is inverted for a statute premised on a fine being absorbed and a sentence not being.

Three drafted parts, at `_internal/PROPOSAL_DEC-5_criminal-tier-inference.md`: a SEC. 0 finding
supplying the rational connection; *Park*'s production burden restored via Amendment 8
Operation 4; and Amendment 7 Operation 3 severed so the authority record exists in advance.
**Gated on *County Court of Ulster County v. Allen*, 442 U.S. 140 (1979), which is not held.**

#### Decision 3 — SEC. 4: the third-party evaluator — does practical authority still run to the officer?

***Level 5.** Whether authority reaches a commissioning officer*

*The entry proposes no splice; see the drafting record.*


## SEC. 5. PROHIBITED ACTS

### As tagged at v3.4

```
SEC. 5. PROHIBITED ACTS. (a) Deployment of a covered system without validation required under
SEC. 3, after the applicable commencement under SEC. 3(c).
(b) Operating a covered system having autonomous external-access capabilities without the
authorization, privilege, monitoring, and enforcement controls prescribed under SEC. 3, where that
failure materially causes the system to obtain unauthorized access to any third-party system,
data, or model weights. Access procured by a third party's intentional misuse (including prompt
injection or stolen credentials) is a defense unless the prescribed controls against that class of
misuse were absent.
(c) Failure to report as required by SEC. 9.
(d) A false or misleading statement of material fact concerning a covered system, made to the
Agency, or to any agency or officer of this State in connection with the agency's or officer's
official functions.
(e) Failure to establish, maintain, or preserve any record required by SEC. 12 or by rule under
SEC. 3, or refusal to permit, upon the lawful demand of the Agency or the Attorney General or upon
order of a court of this State, access to or verification or copying of any such record. Nothing in this paragraph
abrogates any privilege recognized by the law of this State; a good-faith assertion of
privilege, made in the manner the law provides, is not a refusal under this paragraph.
Underlying facts remain subject to discovery and subpoena from any source, per SEC. 12.
```

### Proposed changes

#### Amendment 11 — SEC. 5: name the obligor; SEC. 9(b): write the duty in the active voice

***Level 3.** Two operations name two different actor classes*

**Current text —**

> Preliminary notice to the Agency within 72 hours of credible notice to the entity or any controlling person

**Would become —**

> A violation of this section is committed by each entity that deploys, releases, provides, or
> operates the covered system to which the prohibited act relates, and, for purposes of SEC. 6, by
> each controlling person of such an entity who meets the elements of that section.

**Would become —**

> Each entity that develops, releases, provides, or deploys the covered system shall transmit to the
> Agency a preliminary notice within 72 hours of credible notice to the entity or any controlling
> person

#### Amendment 12 — SEC. 5(d): restore the scienter its own donor requires

***Level 2.** *Alvarez* not held*

**Current text —**

> (d) A false or misleading statement of material fact concerning a covered system, made to the Agency, or to any agency or officer of this State in connection with the agency's or officer's official functions.

**Would become —**

> (d) A statement of material fact concerning a covered system, made to the Agency or to any agency
> or officer of this State in connection with official functions, that the person making it knows to
> be false, or makes with reckless disregard of its truth or falsity, or that omits a material fact
> necessary to make the statements made not misleading where the person knows of the omission. A
> statement made after reasonable inquiry, on the basis of facts then known to the person making it,
> is not a violation of this paragraph.


## SEC. 6. INDIVIDUAL LIABILITY

### As tagged at v3.4

```
SEC. 6. INDIVIDUAL LIABILITY. (a) Offense. A controlling person who had a duty concerning the
relevant risk or the practical power to detect, prevent, halt, restrict, or correct a violation of
SEC. 5, and who failed to exercise due care, commits an offense. Such a person stands in
responsible relation to the public danger within the meaning of United States v. Dotterweich, 320
U.S. 277, 281 (1943); the due-care element supplies the personal blameworthiness that custody
additionally requires. Due care under this Act is measured against the standards applicable under
SEC. 3 and the conduct of a reasonably prudent controlling person in like circumstances; an
entity's own framework is evidence of neither.
(b) Enhanced tier. (1) A person who knowingly or wilfully causes, directs, conceals, or materially
facilitates a violation of SEC. 5, or who deliberately fails to halt a violation after notice, or
who knowingly makes a false certification under SEC. 8, is subject to the felony penalties of
SEC. 10(c). Where a violation described in this paragraph is a but-for and proximate cause of death or of
serious injury to any person, the penalties of SEC. 10(c)(2) apply, and each person killed or
seriously injured constitutes a separate offense. Notice under this paragraph includes any report
or preliminary notice filed under SEC. 9 concerning the same class of risk.
(2) A person who commits any violation of SEC. 5 within [ten] years after a prior conviction of
that person under this Act has become final is subject to the felony penalties of SEC. 10(c)(1).
This paragraph operates upon the fact of the prior conviction, its finality, and the date of the
new violation, and upon nothing else; it neither requires nor permits inquiry into the conduct
underlying the prior conviction. The penalties of SEC. 10(c)(2) do not apply by reason of this
paragraph.
(c) Culpability floor. No custodial sentence may be imposed absent proof of at least the failure
of due care described in subsection (a). Entity liability under SEC. 10(a) is strict.
(d) The prosecution bears the burden of proving each element, including the person's practical
power, beyond a reasonable doubt. Genuine absence of power negates the element; it is not an
affirmative defense.
(e) Construction. A person has practical power if, by reason of position, ownership, or authority,
the person had the ability and opportunity, alone or with others, to detect, prevent, halt,
restrict, or correct the violation or the conditions giving rise to it. This section does not
require that the person could have acted alone or instantly, only that meaningful measures were
within the person's authority.
```

### Proposed changes

#### Amendment 8 — SEC. 6: the individual-liability offense, reconstructed

***Level 4. The offense cannot be pleaded as drafted.** Unvalidated*

**Current text —**

> A controlling person who had a duty concerning the relevant risk or the practical power to detect, prevent, halt, restrict, or correct a violation of SEC. 5, and who failed to exercise due care, commits an offense.

**Current text —**

> No custodial sentence may be imposed absent proof of at least the failure of due care described in subsection (a).

**Current text —**

> A person has practical power if, by reason of position, ownership, or authority, the person had the ability and opportunity, alone or with others, to detect, prevent, halt, restrict, or correct the violation or the conditions giving rise to it.

#### Amendment 22 — SEC. 6(b): the felony tier's knowledge element, and one word that is not American

***Level 1.** Blocked on *MacDonald & Watson* n.15*

**Current text —**

> A person who knowingly or wilfully causes, directs, conceals, or materially facilitates a violation of SEC. 5, or who deliberately fails to halt a violation after notice, or who knowingly makes a false certification under SEC. 8, is subject to the felony penalties of SEC. 10(c).

**Would become —**

> In proving that a person acted knowingly or willfully under this subsection, circumstantial
> evidence may be used, including evidence that the person took affirmative steps to be shielded
> from information that would have disclosed the violation or the conditions giving rise to it.
> Responsibility and authority under SEC. 6(d), standing alone, do not establish knowledge.


## SEC. 7. PERSONAL ECONOMIC CONSEQUENCES

### As tagged at v3.4

```
SEC. 7. PERSONAL ECONOMIC CONSEQUENCES.
(a) Disgorgement. On conviction or civil adjudication of a violation, the court shall order the
person adjudicated to disgorge the economic benefits attributable to the violation — including
salary, bonus, incentive- or equity-based compensation, distributions, profits realized on the
sale or transfer of any interest, and any increase in the value of any interest, whether received
directly or through any entity, trust, or arrangement — received or accrued during the period of
the violation and the [twelve] months following its cessation or concealment. Incentive- or
equity-based compensation received by a controlling person during the period of a violation is
presumed attributable to the violation to the extent the violation materially contributed to the
results on which it was paid; the presumption is rebuttable in a civil proceeding and operates in
a criminal proceeding only as a permissive inference. The court may reduce or decline recovery
only upon a finding that the direct costs of recovery would exceed the amount recoverable. Amounts
disgorged shall be applied first to restitution ordered under SEC. 10(c)(4), and the remainder
deposited in the fund established by SEC. 10(f). A claim under this subsection is subject to the
limitations periods of SEC. 12. On a showing of probable adjudication and risk of dissipation, the
court may restrain transfers of, or require the escrow of, assets up to the amount reasonably
necessary to satisfy the anticipated order.
(b) No indemnification or insurance. (1) No person may (A) enter into, renew, or materially amend a
contract of insurance or other arrangement under which any person is covered, in whole or in part,
against liability for an individual penalty, fine, or disgorgement imposed under this
Act; (B) provide, underwrite, or pay a benefit under such a contract or arrangement, or pay or
reimburse, directly or indirectly, any part of such a liability imposed on another person; or (C)
demand, accept, or retain such a benefit, payment, or reimbursement. (2) No person may make,
offer, solicit, or receive any payment, loan, forgiveness of indebtedness, increase in
compensation, gross-up, distribution, gift, or other transfer of value whose purpose or
predominant effect is to offset, in whole or in part, a liability described in paragraph (1). (3)
Every contract, arrangement, or transfer described in this subsection is void and unenforceable in
this State, whatever law is chosen to govern it, to the full extent of this State's jurisdiction;
and any benefit received under one is held in constructive trust for the persons and fund to which
subsection (a) applies. (4) A violation of this subsection is a violation of this Act for purposes
of SEC. 10(a); a knowing violation by a controlling person is a violation of SEC. 5 for purposes
of SEC. 6(b)(1). (5) This subsection does not restrict the purchase or provision of insurance for,
or the payment, advancement, or indemnification of, reasonable costs of defense, provided that
amounts advanced or indemnified shall be repaid by a person finally adjudicated to have committed
a knowing or wilful violation under SEC. 6(b), to the extent attributable to the defense of that
violation; and it does not restrict indemnification of a person not adjudicated liable under this
Act. (6) Application. Paragraph (1) applies to contracts and arrangements entered into, renewed,
or materially amended on or after the effective date of this Act. A contract or arrangement in
force on the effective date may be maintained until its first renewal, expiration, or material
amendment, and in any event no longer than [twelve] months after the effective date, after which
maintaining it is a violation of paragraph (1). (7) Restitution preserved. This subsection does
not restrict the purchase or provision of insurance for, or the payment, advancement, or
indemnification of, restitution ordered under SEC. 10(c)(4); amounts paid under any such
arrangement shall be applied to restitution before any other liability, and no such payment
extinguishes any other liability of any person.
(c) Construction. Disgorgement under subsection (a) is remedial, is additional to any penalty or
fine, and shall not be credited against one; no single benefit shall be disgorged more than once.
Nothing in this section limits any remedy under SEC. 10.
```

**No change proposed.**


## SEC. 8. CERTIFICATION

### As tagged at v3.4

```
SEC. 8. CERTIFICATION. Before material deployment and following material change to a covered
model or configuration, the chief executive officer (or, where no such office
exists, each natural person exercising the most senior executive authority over the entity,
severally), and each controlling person designated by rule, shall personally certify compliance with the applicable standards or disclose identified
noncompliance, on the structure of 18 U.S.C. § 1350. For purposes of
this section: "material deployment" means the first deployment of an identified model version in
or into this State, and any deployment following a material expansion or a material change;
"material change" means a change granting a new class of tools, credentials, or permissions,
materially expanding capability or autonomy, or removing or materially weakening a safeguard
identified in an applicable validation. The Agency may elaborate these definitions prospectively
by rule and may not narrow them. Changes to a covered model or configuration below the material
line shall be certified in a periodic certification covering every such change in the period,
filed not less often than once in each [calendar quarter] in which any such change occurred; a
periodic certification is a certification under this section, with the consequences this section
and SEC. 6 attach. The chief executive officer's obligation may
not be delegated or performed through any designee. The Agency may by rule designate the
certifying office or offices for forms of organization lacking a chief executive officer; no
designation diminishes the several obligation stated in this section, and no entity may, by its
form of organization, leave this section without an obligated natural person. The certification consists of statements of
fact within the certifying person's knowledge after reasonable inquiry. No person is required by
this section to characterize, opine upon, or adopt any position concerning the capabilities,
risks, or merits of any model or system, A certification disclosing identified noncompliance satisfies
the duty to certify under this section; it constitutes neither compliance with the applicable
standards, nor validation, nor cure of, nor a defense to, any violation of this Act, and a
certification disclosing unremediated material nonconformity — nonconformity not addressed by an
equivalent compensating measure within the meaning of SEC. 3(c)(2) — shall so state on its face. A certification is made to the Agency and is not required to be published.
Knowing false certification is an offense under SEC. 6(b)(1); reckless certification without
reasonable inquiry is an offense under SEC. 6(a).
```

### Proposed changes

#### Amendment 5 — SEC. 8 punctuation

***Level 3. Mechanical.** A comma where a period belongs*

**Current text —**

> risks, or merits of any model or system, A certification disclosing identified noncompliance

#### Amendment 21 — SEC. 8: the certification register, facts public, content protected

***Level 4.** Trade secret and public records*

*The entry proposes no splice; see the drafting record.*

#### Amendment 24 — SEC. 8: the certification's lower tier names a mental state SEC. 6(a) does not require

***Level 4.** SEC. 8 names a mental state SEC. 6(a) does not require*

**Current text —**

> Knowing false certification is an offense under SEC. 6(b)(1); **reckless certification without reasonable inquiry** is an offense under SEC. 6(a).

**Would become —**

> Knowing false certification is an offense under SEC. 6(b)(1); certification without reasonable
> inquiry is an offense under SEC. 6(a), which requires proof of the failure of due care described in
> that subsection.


## SEC. 9. INCIDENT REPORTING

### As tagged at v3.4

```
SEC. 9. INCIDENT REPORTING. (a) "Critical safety incident": exfiltration or loss of control of
model weights; loss of operator control of a covered system; autonomous access by a covered system
to protected third-party systems; death or serious injury materially caused by a covered system;
deception of safety or monitoring controls by a covered system; a serious near-miss, meaning an
event that, but for intervention other than controls
operating as designed, or but for chance, would have constituted an incident under this
subsection; or a reproducible evaluation finding of materially increased risk. Behavior
intentionally elicited in a sandboxed exercise and contained there is not an incident but shall be
recorded. An event detected and contained by controls operating as designed, before any effect
outside the systems of the entity whose controls contained it, is not an incident under this
subsection but shall be recorded under SEC. 12.
(b) Preliminary notice to the Agency within 72 hours of credible notice to the entity or any
controlling person (24 hours where there is imminent risk of death or serious injury); full report
within [30] days of the preliminary notice, the incompleteness of an investigation not extending
the period; material updates within [10] days of awareness thereafter. The period runs from when
the incident was detected, or would have been detected by the monitoring the entity certified it
maintains under SEC. 8.
(c) A report under this section may consist of the facts known to the reporting person at the time
of the report. No person is required to characterize an event, to state a conclusion as to
causation or risk, or to adopt any contested description; the obligation is discharged by a timely
statement of the facts then known, supplemented as required by subsection (b). A report is made to
the Agency and is not required to be published.
```

### Proposed changes

#### Amendment 4 — SEC. 9(a): the two characterization-shaped triggers, recast as observable events

***Level 4.** Are the recast events provable?*

**Current text —**

> deception of safety or monitoring controls by a covered system;

**Current text —**

> or a reproducible evaluation finding of materially increased risk.

**Would become —**

> a divergence, reproducible on the entity's own records, between a covered system's
> behavior under evaluation, testing, or monitoring conditions and its behavior in
> deployment conditions not otherwise materially different, or between the state of a
> covered system as reported to or recorded by a safety or monitoring control and its
> actual state, where in either case the divergence defeats, suppresses, or materially
> degrades the operation of the control. No finding as to any intent, awareness, purpose,
> or mental state of a covered system is required, and none may be inferred from this
> paragraph; the facts to be reported are the divergence, its reproducibility, and its
> effect upon the control;

#### Amendment 14 — SEC. 9(b): a detection clock that cannot be gamed by certifying less monitoring

***Level 3.** Sound as drafted on five attacks*

**Current text —**

> The period runs from when the incident was detected, or would have been detected by the monitoring the entity certified it maintains under SEC. 8.

**Would become —**

> The period runs from the earliest of: (i) actual detection of the incident by the entity or any
> controlling person; (ii) receipt by the entity or any controlling person of information from any
> source, including a public statement by a person affected, from which a reasonably prudent person
> in the entity's position would inquire whether a covered system of the entity was involved, the
> period then running from the third day after receipt; and (iii) the time at which the incident
> would have been detected by monitoring conforming to the applicable standards under SEC. 3,
> whether or not the entity maintained it. An entity's failure to maintain monitoring required by
> the applicable standards does not extend any period under this subsection.

**Would become —**

> (d) Notice to affected persons. Within [10] days of the preliminary notice under subsection (b),
> an entity shall give notice of the facts then known to each person whose system, data,
> credentials, or accounts a covered system of the entity accessed without authorization, so far as
> that person is identifiable by the entity after reasonable inquiry, and shall record the inquiry
> under SEC. 12. Where the entity cannot identify a person but another entity can, notice to that
> other entity, together with a request to inform the person, discharges this subsection only if the
> entity records the request and the response. The Attorney General may, on written application,
> delay notice under this subsection for a stated period where notice would impede an active
> criminal investigation or materially increase the risk of further unauthorized access. This
> subsection requires no characterization, no conclusion as to causation or risk, and no
> publication; SEC. 9(c) applies to notice under this subsection.


## SEC. 10. ENFORCEMENT AND PENALTIES

### As tagged at v3.4

```
SEC. 10. ENFORCEMENT AND PENALTIES. (a) Entity: civil penalty of up to $[1,000,000] per violation
for each day the violation continues or, where the violation occurs after a prior adjudication of
a violation by the same person has become final, up to $[3,000,000] per violation for each day the
violation continues; strict liability. In assessing the amount, the court shall consider the
seriousness of the violation; the economic benefit or savings resulting from it; any history of
violations; good-faith efforts to comply; the economic impact of the penalty on the violator; and
such other matters as justice may require, per the structure of 33 U.S.C. § 1319(d). A penalty
under this subsection shall not be less than the economic benefit or savings derived from the
violation, as found by the court. Penalty amounts under this Act shall be adjusted annually for
inflation by Agency rule, in the manner of 40 C.F.R. part 19.
(b) Individual offense under SEC. 6(a): [misdemeanor; imprisonment up to one year; fine up to
$[100,000] or, if greater, twice the gross pecuniary gain to the person derived from the
violation], per the structure of 21 U.S.C. § 333(a)(1) as to classification and of 18 U.S.C.
§ 3571(b)(5) and (d) as to amount.
(c)(1) Enhanced tier under SEC. 6(b): [felony; imprisonment up to three years; fine up to
$[250,000] or, if greater, twice the gross pecuniary gain to the person derived from the
violation].
(c)(2) Enhanced tier under SEC. 6(b)(1) where death or serious injury results: [felony]. (A) Where
serious injury results, imprisonment up to twenty years for each offense. (B) Where death results,
imprisonment for any term of years or for life for each offense, and not less than [two] years.
(C) In either case, a fine up to $[1,000,000] for each offense or, if greater, twice the gross
pecuniary gain to the person derived from the violation. (D) "Results" requires that the violation be
both a but-for cause, within the meaning given in Burrage v. United States, 571 U.S. 204 (2014),
and a proximate cause of the death or serious injury: the death or serious injury must have been
a reasonably foreseeable consequence of the violation and not the product of an independent,
unforeseeable intervening cause. That death or serious injury so resulted, and
the identity of each person killed or seriously injured, are elements of each such offense, to be
charged and found by the trier of fact beyond a reasonable doubt.
(c)(3) Concurrent and consecutive service. Terms of imprisonment imposed under this Act at the
same time run concurrently unless the court orders consecutive service. The court may order
consecutive service only upon findings, stated on the record, that consecutive service is
necessary to reflect the seriousness of each offense, the culpability found under SEC. 6, and the
totality of the harm, and that the aggregate term is not disproportionate to the whole of the
person's conduct and culpability. The aggregate of the determinate terms ordered to run
consecutively for offenses under this Act arising out of the same violation or course of conduct
shall not exceed [forty] years. Nothing in this paragraph limits the imposition of a term of
imprisonment for life where death results. A minimum term under this subsection attaches to each
offense severally and is satisfied by concurrent service.
(c)(4) Restitution. Whenever death or serious injury results from an offense under this Act,
whatever its tier, the court shall order restitution to each person killed or seriously injured,
or to the person's estate, per the structure of 18 U.S.C. § 3663A; "results" bears the same
meaning as in paragraph (2). Restitution has priority over every penalty, fine, and disgorgement
in the application of a defendant's assets. In fixing a fine for a natural person under this Act,
the court shall consider the person's income, earning capacity, and financial resources, so that
like culpability bears like burden.
(d) Remedies additionally include: (1) injunction against any entity or controlling person
restraining deployment, expansion, or continued operation in violation of this Act, per the
structure of 21 U.S.C. § 332; (2) suspension of an identified model version and configuration, per
the structure of 21 U.S.C. § 334; operation of a suspended configuration in this State by any
person with notice of the suspension is contempt and a violation of SEC. 5(a); (3) on probable
cause of imminent risk of death or serious injury, emergency suspension ex parte, with a
post-deprivation hearing within [10] days; (4) disqualification from acting as a controlling
person of any covered system; and (5) suspension and debarment modelled on FAR subpart 9.4.
(e) The Attorney General enforces this Act. Corporate payment of any penalty imposed on a natural
person does not extinguish individual liability and is a violation of SEC. 7(b).
(f) Fund. The [Frontier AI Accountability Fund] is established. All penalties, fines,
disgorgement, and other monetary recoveries under this Act, after satisfaction of restitution,
shall be deposited in the fund; awards under SEC. 11 are paid from it; the balance [is
appropriated to the Agency's functions under this Act / reverts to the general fund, at the
adopting state's election]. The fund continues in operation, fed by every source not suspended or
invalidated, notwithstanding the suspension or invalidity of any single provision of this section.
```

### Proposed changes

#### Amendment 9 — SEC. 10(e): the access authority the Act forgot to import

***Level 4.** § 374 does not supply the model*

**Current text —**

> The Attorney General enforces this Act.

**Would become —**

> (e) Access and demand. The Agency and the Attorney General may, upon reasonable notice and during
> ordinary business hours, require any person subject to this Act to produce for inspection,
> verification, and copying any record required to be established, maintained, or preserved under
> SEC. 12 or by rule under SEC. 3, and may require a written response, under oath, to
> interrogatories reasonably related to the existence, location, custody, and completeness of such
> records. A demand shall be in writing, shall identify the records sought with reasonable
> particularity, and shall state the provision of this Act to which they relate. On petition of the
> person served, [the court of general jurisdiction of the county in which the Agency sits] may
> quash or modify a demand that is unreasonable or oppressive; on petition of the Attorney General,
> that court may enforce it. A demand under this subsection is a lawful demand for purposes of
> SEC. 5(e). Nothing in this subsection authorizes entry upon premises, or access to any material,
> beyond what is reasonably necessary to obtain the records demanded.

#### Amendment 25 — SEC. 10(d): the FDCA remedies are cited and their protections are not taken

***Level 4.** Is taking the FDCA protections coherent?*

**Would become —**

> In any proceeding for contempt of an order under this subsection where the conduct also constitutes
> a violation of SEC. 5, trial shall be by the court or, upon demand of the accused, by a jury.


## SEC. 11. WHISTLEBLOWERS

### As tagged at v3.4

```
SEC. 11. WHISTLEBLOWERS. (a) Award. A person who voluntarily provides the Agency with original
information leading to a successful enforcement action under this Act in which monetary sanctions
exceed $[1,000,000] shall receive not less than 10 and not more than 30 percent of the sanctions
collected, per the structure of 15 U.S.C. § 78u-6. Awards are paid from the fund established by
SEC. 10(f). Awards remain payable from the fund whatever the source of the amounts in it; the
suspension or invalidity of SEC. 10(a) does not suspend this section. (b) A report may be made
anonymously through counsel; the Agency shall protect the reporting person's identity, including
in any award. (c) No person may take any action to impede an individual from communicating with
the Agency concerning a possible violation of this Act; any agreement or condition purporting to
do so is void. (d) Retaliation against a person for reporting, internally or to the Agency, gives
rise to a civil action for reinstatement, double back pay, and fees. (e) The Agency shall act
upon, or publish a reasoned declination of, any credible report within [180] days. (f) Rules under
SEC. 3 shall provide for the handling of security-sensitive information in reports and awards.
```

### Proposed changes

#### Amendment 17

*Never drafted — number and title only*


## SEC. 12. MACHINERY

### As tagged at v3.4

```
SEC. 12. MACHINERY. This Act takes effect [90] days after enactment; until the Agency is
designated and organized to receive them, transmission to the Attorney General satisfies any
requirement under this Act of transmission to the Agency, and the Attorney General shall
transfer the materials to the Agency upon its organization; duties and offenses commence
as provided by SEC. 3(c); [180-day] transition for covered systems deployed before the
commencement applicable to them under SEC. 3(c), running from that commencement; no retroactive
liability; records sufficient for audit (version identifiers, compute records, evaluation results,
tool and permission manifests, change histories, and the compensation records upon which SEC. 7(a)
operates) retained for [ten] years from creation, or for [five] years after the covered system
last operates in or is last deployed in or into this State, whichever period ends later; and, from
the time the entity or any controlling person has notice of a critical safety incident, of an
investigation, or of a proceeding under this Act to which the records are reasonably relevant, the
records shall be preserved until the conclusion thereof; confidentiality of reported material as
follows: reports under SEC. 9, certifications under SEC. 8, and validation materials under SEC. 3
are exempt from disclosure under [the State public-records act], and to the extent they contain
security-sensitive information — including information that would materially assist unauthorized
access to model weights or covered systems — shall be maintained under seal in any proceeding;
this exemption does not limit access by the Agency, the Attorney General, or a court under seal,
does not exempt any person from any obligation to disclose under any other law, does not create
any privilege for underlying facts, which remain subject to discovery and subpoena from any
source, and does not restrict any use of any material in an enforcement proceeding under this Act.
Dissolution, merger, conversion, division, or reorganization of an entity does not abate any
proceeding or extinguish any liability under this Act; a surviving, resulting, or successor
entity, and any entity that acquires substantially all of a covered entity's assets and continues
its business, assumes the predecessor's liabilities under this Act; nothing in this section
transfers the criminal liability of any natural person to any other person. A prosecution under
this Act shall be commenced within [five] years after the violation; for a continuing violation,
within [five] years after its last day; where the violation was concealed by an affirmative act,
within [five] years after its discovery by the Agency or the Attorney General; a prosecution for
an offense to which SEC. 10(c)(2) applies may be commenced within [ten] years. This Act shall be
construed to reach the persons with the greatest practical authority over covered systems; it
shall not be construed to permit the discharge of any person's liability through the liability of
another. Nothing in this Act displaces any other remedy of this State.
```

**No change proposed.**


## SEC. 13. SEVERABILITY, CONFORMING OPERATION, AND REVIVAL

### As tagged at v3.4

```
SEC. 13. SEVERABILITY, CONFORMING OPERATION, AND REVIVAL.
(a) Severability. The provisions of this Act are severable. If any provision, or any application
of any provision to any person, capacity, class of persons, or circumstance, is held invalid or
unenforceable, the holding does not affect any other provision or application that can be given
effect without it, and this Act shall be construed and enforced to the maximum extent it may
lawfully operate.
(b) Order of severance. Where a court can preserve the operation of this Act by severing a
narrower provision or application rather than a broader one, it shall do so, and shall sever
later-listed matter before earlier-listed matter:
(1) First rank. The offenses under SEC. 5(b) and SEC. 5(d); the offense under SEC. 5(a) as applied
to the deployment (otherwise than by release), material expansion, or continued operation of a
covered system in or into this State; SEC. 4 and SEC. 6; the remedies and penalties of SEC. 7 and
SEC. 10(b) through (f) as applied to those offenses, and SEC. 10(a) as applied to those offenses;
the duties of SEC. 2 as applied to a person in that person's capacity as a provider or deployer;
and SEC. 1, SEC. 3(a), SEC. 3(c), and the provisions of SEC. 12 governing limitations, transition,
retroactivity, and successor liability.
(2) Second rank. SEC. 11; the remaining provisions of SEC. 12; the offense under SEC. 5(e), except
as provided in paragraph (3).
(3) Third rank. The duties of SEC. 2 and SEC. 3 as applied to a person in that person's capacity
as a developer, including pre-release evaluation and weight security; SEC. 5(a) as applied to a
release; SEC. 5(e) as applied to records of pre-release evaluation held by a person in that
person's capacity as a developer; the validation modes of SEC. 3(b) requiring assessment by a
person other than the developer.
(4) Fourth rank. SEC. 8; SEC. 9; SEC. 5(c).
(5) Preservation of elements. No provision shall be severed to an extent that deprives a surviving
offense of an element, a definition, a standard, a limitations period, or a commencement condition
on which that offense depends. A provision of a later rank that supplies such matter to an offense
of an earlier rank continues in effect for that purpose notwithstanding its severance for every
other purpose. In particular, SEC. 3(a) and SEC. 3(c) continue in effect to supply the content of,
and the commencement condition for, any surviving offense under SEC. 5. The civil penalty of
SEC. 10(a) and the criminal penalties of SEC. 10(b) and (c) sever independently of one another;
the invalidity or suspension of either, in whole or as applied, does not affect the other; and the
fund under SEC. 10(f) continues in operation whatever else is severed, fed by the sources that
remain. The offense under SEC. 5(e) and the duties of SEC. 12 sever independently of one another:
severance or suspension of the offense leaves the duties enforceable under SEC. 10(a), and
severance of any reporting or certification duty does not sever the records duties or the offense
that enforces them.
(6) Declared intent. The Legislature declares that it would have enacted the provisions of each
rank irrespective of the invalidity of any later rank, and specifically that it would have enacted
the first rank, together with the matter preserved to it by paragraph (5), had it known that no
later rank could take effect.
(c) Conforming operation. (1) The Attorney General shall, by order published in [the State
register], determine whether and to what extent any Act of Congress, or any regulation having the
force of law, preempts the application of any provision of this Act. Upon publication, the
provision is suspended to the extent, and only to the extent, stated in the order. A provision is
suspended under this subsection only by such an order, or by a final judgment no longer subject to
appeal in a proceeding to which this State was a party; and a suspension applies only to conduct
occurring after the date of publication of the order or of notice of the judgment.
(2) In making a determination under paragraph (1), the Attorney General shall preserve the
operation of this Act to the greatest extent lawfully available, and shall have regard to the
following, which are stated as directions to the Attorney General and not as conditions of any
person's liability:
(A) where the federal enactment conditions the preservation of State authority upon the absence of
obligations imposed on developers with respect to the development, training, evaluation, or
release of a model, the order shall suspend the duties of this Act as applied to persons in the
capacity of a developer with respect to those matters, and shall preserve them as to every other
person, capacity, and matter;
(B) where the federal enactment reaches only laws regulating conduct prior to deployment, the
order shall preserve this Act as applied to conduct occurring upon or after deployment;
(C) where the federal enactment reaches a duty to report or to certify to the Agency, the order
shall preserve the obligation, under SEC. 12, to create and retain the records that would have
supported the report or certification, and those records shall be produced upon lawful process; an
order preserving the obligation preserves the offense under SEC. 5(e) with respect to it; and
(D) where the federal enactment reaches only laws that target developers of artificial
intelligence models, the order shall so state, and nothing in this Act limits the application to
any person of the generally applicable criminal law of this State, including the law of homicide,
reckless endangerment, endangerment by unsafe or adulterated goods, and false statement to a
public officer, which applies to conduct concerning covered systems as it applies to all other
conduct.
(3) No person may be convicted of an offense under this Act for conduct occurring during a period
in which the provision creating the offense stood suspended under this subsection.
(d) Revival. A provision suspended under subsection (c) is not repealed. The Attorney General
shall, within [30] days after the expiration, sunset, non-reauthorization, repeal, or judicial
invalidation of the federal enactment stated in the order, or after a final judgment no longer
subject to appeal determining that the enactment does not preempt the provision, publish an order
terminating the suspension. The provision resumes operation on the date of publication of that
order and applies to conduct occurring on or after that date. No person is liable under a
provision for conduct occurring before that date.
(e) No inference. A suspension under subsection (c) is not evidence that the suspended provision
was invalid, and does not affect liability for conduct occurring before the suspension took
effect.

This text is dedicated to the public domain under CC0 1.0. It may be reproduced, adapted, and
introduced, in whole or in part, without attribution or permission.
```

### Proposed changes

#### Amendment 2 — SEC. 13(c): a review valve on the suspension order

***Level 4.** Administrative law*

**Current text —**

> (3) No person may be convicted of an offense under this Act for conduct occurring during a period in which the provision creating the offense stood suspended under this subsection.

**Would become —**

> (4) Contents and review. An order under this subsection shall identify the federal
> enactment relied upon, the provisions of this Act suspended, and the extent of each
> suspension, and shall state the Attorney General's reasons. Any person may petition [the
> court of general jurisdiction of the county in which the Agency sits] for review of an
> order, on the ground that it suspends more than the federal enactment preempts; the court
> shall determine the question of preemption without deference to the order. An order
> vacated or narrowed on review ceases to operate, to the extent vacated or narrowed, from
> the date of publication of notice of the judgment, and not before; nothing in this
> paragraph affects paragraph (3), and no person is liable under a provision for conduct
> occurring before that date.
