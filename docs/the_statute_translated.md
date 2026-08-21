*SEC. 0–13 in plain language, beside what the statute actually says. Split from the front
page on 21 August 2026. The authoritative text is [`model_act_v3_4.txt`](../model_act_v3_4.txt);
where this page and the statute differ, the statute governs and the difference is an
[erratum](../ledger/errata.md). The argument this serves is [the case](./the_case.md).*

<a id="the-statute-translated"></a>

# The statute, translated

What follows is the complete Act in plain language — every section, faithful to the
v3.4 text as landed. Two rules govern this translation. First: it is a translation,
not the text; where this summary and [the statute](../model_act_v3_4.txt) differ, the
statute controls, and the strict verification prompt in [Verify it](#verify-it) works
on this section too. Second: matter in [brackets] is an adopting state's choice — a
number or a name the legislature fills in, not a gap.

## At a glance

| § | In plain words |
|---|---|
| **0 — Findings & purpose** | Why the state may act: the harms land on its own residents, and protecting them from failures of care is the oldest police power there is. Every duty arises from conduct — deploying, expanding, releasing, operating in or into the state — never from research elsewhere. No compelled opinions, only statements of fact to a regulator. Purpose: *Park* — personal responsibility on the people with practical authority. |
| **1 — Definitions & reach** | Covered model: over 10^26 compute, or designated. Small derivations (≤[10^24]) never extend a lineage; record-keeping starts far lower anyway — the commons stays out, the paper trail stays on. Covered *system* = the model as deployed: tools, memory, credentials, permissions. Release = weights leaving your control; use, study, and modification of lawful weights untouched. Autonomous access = acting on the outside world without a human approving each step. Jurisdiction is conduct-based and symmetrical. |
| **2 — The duty** | No deployment or expansion without every controlling person's due care toward the standards. Each duty sits with whoever controls that risk — developers: evaluations and weight security; deployers: configuration and monitoring; releasers: evaluate the model *as it can be modified*, within a floored compute budget. The wrapper rule: run someone else's validated configuration untouched — adopt the validation, keep a manifest, monitor, report — and you are sheltered, until you modify or look away on purpose. The research door: real containment gets a light assessment; step outside it and the full Act attaches. |
| **3 — Agency, standards, commencement** | Standards must be feasible, proportionate, and free to read; validation pins to an exact version and configuration; and no rule may ever create a prior-approval gate — nothing exists to capture. Three layers: truth, reporting, and records offenses run from day one; at day [180] the core duty runs on interim standards borrowed verbatim from enacted California, New York, and Illinois law; the Agency's own standards take over prospectively when they issue. Disclosing nonconformity is a *report* — filed, retained, discharging nothing. |
| **4 — Controlling persons** | Whoever holds *final, material, independent decision authority* — any title, any structure, alone or in concert. Then the exclusions, in black letter: title, seniority, credentials, technical ability, access, executing someone else's decision, giving advice — none of it is authority. The authority to decide, not the capacity to act. Delegation shields no one who kept the power; liability is several. |
| **5 — The five prohibited acts** | Shipping without validation · operating uncontrolled autonomous access that causes a real breach (misuse defense — unless the controls against that class of misuse were simply absent) · failing to report · lying to the state · destroying or withholding the records (privilege preserved, facts always reachable). |
| **6 — Individual liability** | Duty or practical power, plus failure of due care, is the offense — *Dotterweich*'s responsible relation. Knowing, wilful, concealing, or ignoring notice: felony tier; where that is the but-for *and proximate* cause of death or serious injury, each victim is a separate offense, found by a jury. The floor: no prison without proven fault — strict liability buys entity fines only. |
| **7 — The money** | Disgorge everything the violation paid you — salary, bonus, equity, through any trust — plus [twelve] months. No one may insure, indemnify, or quietly offset an individual penalty: void, constructive trust, and doing it knowingly is itself felony-tier. Defense costs: advanceable, clawed back from the wilful. Restitution to victims: fully insurable, and always first. |
| **8 — The signature** | Before material deployment and after material change, the chief executive — or each most-senior person, severally; no organisation chart escapes into headlessness — personally certifies, on the Sarbanes–Oxley structure. Everything below the material line still certifies, batched quarterly. Facts after reasonable inquiry, no compelled opinions. Disclosing noncompliance satisfies the duty to certify — and defends against nothing. Knowingly false: felony. |
| **9 — The clock** | Report: weights loss, control loss, autonomous breaches, death or serious injury, deceived safeguards, genuine near-misses, adverse reproducible evaluations. Defenses that worked as designed: recorded, not reported — success is never punished. 72 hours preliminary (24 where lives are at imminent risk), [30] days full — and the clock runs from when the monitoring you certified would have caught it. Deleting the logs stops nothing. |
| **10 — The consequences** | Entities: up to \$[1,000,000] per violation per day, strict, never below the benefit gained. Individuals: misdemeanor base; felony tier; where people die or are seriously hurt — up to twenty years per injury, any term or life per death, per victim. Restitution outranks every penalty, fine, and disgorgement in the claim on a defendant's assets. Plus injunctions, model suspension (operating one anyway is contempt and a fresh offense), emergency halts, disqualification, debarment. A company paying an individual's fine extinguishes nothing — and is a new violation. |
| **11 — The insiders** | The inspectors already work at the laboratories; this section pays them: 10–30 percent of sanctions over \$[1,000,000], anonymous through counsel, gags void, retaliation bought back with reinstatement and double pay. The Agency must answer every credible report within [180] days. |
| **12 — The machinery** | Live in [90] days; the Attorney General receives filings until the Agency exists — no duty waits on furniture. Audit-grade records for [ten] years, plus a litigation hold. Security-sensitive material sealed — but facts are never privileged and enforcement is never restricted. Mergers carry entity liability to successors; no natural person's criminal liability ever transfers. Concealment moves the limitations clock to discovery. |
| **13 — The armour** | Everything severs, narrow before broad, the criminal core ranked first and declared enacted-regardless. No severance may strip a surviving offense of an element it needs; the fund survives everything. Preemption becomes administrable: published Attorney General orders suspend only what is actually preempted, only prospectively — and suspended is not repealed. If the federal law lapses, the provision revives within [30] days. |

The full translation follows, section by section.

**SEC. 0 — Findings and purpose.** The legislature's opening statement of why it may
act and what it intends. The harms happen to people and property inside the state;
protecting residents from death and injury caused by failures of care is the oldest
use of a state's police power — the same power behind its homicide, endangerment,
unsafe-goods, and false-statement laws. Every duty in the Act arises from *conduct* —
deploying, expanding, releasing, or operating a covered system in or into the state —
never from research or development that stays elsewhere. Nothing compels anyone to
express an opinion or alter a model's output: the only required statements are
statements of fact, made to a regulator. The Act treats in-state and out-of-state
actors identically, adds to (never replaces) ordinary criminal law, and states its
purpose plainly: personal responsibility for the safety of covered systems, placed on
the natural persons with practical authority over them, on the doctrine of *United
States v. Park*.

**SEC. 1 — Classification and definitions.** The Act's offenses sit in the
public-welfare lane — the *Morissette* category that has covered unsafe goods for
eighty years — except where the text expressly demands a guiltier mind. The key
definitions: a **covered frontier model** is one whose training-plus-lineage compute
exceeds 10^26 operations, or one the Agency prospectively designates as
frontier-equivalent; until rules refine lineage accounting, a derivative counts only
if its own derivation pushes the lineage past the line, small derivations (at or
below [10^24]) never extend a lineage by themselves, and record-keeping kicks in at a
much lower floor ([10^22]) whether or not the result is covered — the commons stays
out, the paper trail stays on. A **covered system** is the *deployed configuration*:
the model plus its tools, memory, retrieval, credentials, and permissions — because
that is the thing that acts in the world. Roles (developer, provider, deployer) track
who does what, affiliates count as their principals, and running a model privately
for your own use is not deployment. **Material expansion** — new classes of tools or
permissions, enabled autonomous access, weakened safeguards — is defined by the
statute itself, operative from day one, elaborable by rule but never narrowable.
**Unauthorized access** means access the owner never permitted; a broken lock is not
an invitation. **Serious injury** borrows the federal medical-device definition.
**Release** means making the weights available beyond your control — it counts as a
deployment, but only carries the duties performable *before* the weights leave; and
nothing in the Act restricts anyone's use, study, or modification of lawfully
obtained weights. An **autonomous external-access capability** is the system's
ability to reach out — network requests, code affecting other systems, transactions,
messages — without a human approving each interaction. Jurisdiction is conduct-based
and symmetrical: in-state conduct, systems made available to residents, or conduct
aimed at and hitting the state; someone who does none of those things owes the state
nothing as to that system.

**SEC. 2 — The public welfare duty.** The heart. No covered system may be deployed or
materially expanded in or into the state unless every controlling person has
exercised due care toward the applicable safety, authorization, monitoring,
reporting, and deployment standards. The duty follows the risk to whoever controls
it: the developer answers for model evaluation and weight security; providers and
deployers for configuration, tools, permissions, and monitoring; a releasing
provider for pre-release evaluation — including evaluating the model *as it can be
modified*, safeguards stripped or fine-tuned, within a compute budget floored at the
greater of [one] percent of lineage compute or [10^24] operations — plus
tamper-resistance and weight security up to the moment of release. Subsection (b) is
the wrapper rule: a deployer that runs a system exactly within someone else's
validated configuration — modifying nothing, attaching nothing beyond it — discharges
the duty by adopting that validation, keeping a manifest of every tool, credential,
and access path it grants, doing the monitoring within its control, and reporting
what it knows. The shelter is conduct-based, never revenue-based; it dies on actual
or wilfully-avoided knowledge of a real nonconformity, and it lapses the moment the
deployer starts modifying. Subsection (c) is the research door: giving authenticated
researchers access inside genuine containment — no autonomous external reach, no
credentials or effects persisting past a session, monitored — is a controlled
research deployment, satisfied by an assessment of the containment itself; step one
inch beyond those terms and the full Act attaches from that moment.

**SEC. 3 — The Agency, standards, and commencement.** The Agency writes the technical
standards, after notice and technical submissions, limited to safety, authorization,
monitoring, incident-reporting, and deployment controls — feasible, evidence-based,
proportionate. It may adopt an outside body's standard only after its own independent
review, only at a pinned version, and **everything incorporated must be free to
read**. It specifies how compliance is validated — internal attestation, independent
audit, or accredited certification — with validation glued to a specific model
version and configuration (validated without tools means *not* validated with them).
And one thing no rule may ever do: condition any deployment or release on the
Agency's prior approval — there is no permission gate to capture. Commencement runs
in three layers so nothing waits on bureaucratic diligence: from day one, the
truth-telling, reporting, and records offenses operate, along with all the machinery;
at day [180], the core deployment duty switches on against **interim standards
borrowed verbatim from three enacted state laws** (California's, New York's, and
Illinois's frontier-AI framework duties, frozen as of [1 August 2026]) — pinned
verbatim in [the adopted texts](../standards/interim_standards.md) — applied to
every covered entity without those states' revenue thresholds, with filings going to
this state's Agency, third-party audit optional, and this Act's own reporting and
penalty provisions governing throughout; provisional validation at this stage means a
documented, reasonable conclusion of *material conformity*, where any identified gap
must be covered by a demonstrated equivalent compensating measure — and a filing that
can't honestly say that is a **nonconformity report**: transmitted, retained, and
discharging nothing. When the Agency's own standards finally issue and a [90]-day
compliance period runs, they take over prospectively; conduct is always judged by the
standards of its time, and nothing lawful when done becomes unlawful later.

**SEC. 4 — Controlling persons.** Who the Act reaches. A controlling person is any
natural person — title irrelevant — holding *final, material, independent decision
authority* over a covered system: through deployment and access decisions; budgets,
compute, and risk policy; hiring, firing, and directing the people who decide; or
ownership and governance rights carrying practical power to halt. Authority counts
however held — directly, in concert, through any entity or trust. Then the express
exclusions, the engineer exemption on the face of the text: title alone, seniority,
credentials, technical ability, access to systems or weights, carrying out someone
else's decision, or giving advice — none of these, alone or together, is authority.
*The authority to decide, not the capacity to act.* Chief executives and controlling
shareholders are presumed in civil cases (rebuttable by proving genuine absence of
power); in criminal cases their status is merely evidence, and the prosecution keeps
its full burden. Delegation relieves no one who retains the power: no safety
officer, committee, or subsidiary shields the person who could still have said stop.
Liability is several — each person answers for their own elements.

**SEC. 5 — The prohibited acts.** Five, and they are the spine: (a) deploying a
covered system without the validation then required; (b) operating a system with
autonomous external-access capability without the prescribed controls, where that
failure materially causes unauthorized access to someone else's systems, data, or
weights — with a defense where a third party's intentional misuse (prompt injection,
stolen credentials) procured the access, *unless* the prescribed controls against
that class of misuse were simply absent; (c) failing to report under SEC. 9; (d)
false or misleading material statements about a covered system to the state; (e)
failing to keep, or refusing lawful access to, required records — with legal
privilege expressly preserved, and the underlying facts always reachable.

**SEC. 6 — Individual liability.** The *Park* rule, written down. A controlling
person who had a duty concerning the risk, or the practical power to detect,
prevent, halt, restrict, or correct a violation, and who failed to exercise due
care, commits an offense — the "responsible relation" of *Dotterweich*, with the
due-care element supplying the personal blameworthiness that imprisonment requires.
A company's own safety framework, by itself, proves neither care nor its absence.
The enhanced tier is for the guilty mind: knowingly causing, directing, concealing,
or facilitating a violation; deliberately failing to halt one after notice (and a
filed incident report *is* notice); or knowingly false certification — felonies. And
where such a violation is both the but-for *and proximate* cause of death or serious
injury, each victim is a separate offense, charged to a jury beyond reasonable
doubt. A repeat violation within [ten] years of a final conviction is a felony on
the fact of the record alone. The constitutional floor is explicit: **no one goes to
prison without at least a proven failure of due care** — strict liability is for
entity fines only. Practical power means meaningful measures were within the
person's authority — not that they could have acted alone or instantly — and its
genuine absence defeats the charge as a failed element, never as something the
defendant must prove.

**SEC. 7 — Personal economic consequences.** The money follows the person. On
adjudication, the court orders disgorgement of the benefits attributable to the
violation — salary, bonus, equity, distributions, gains on sales, through any entity
or trust — for the violation period plus [twelve] months; equity compensation during
a violation is presumed attributable to it (rebuttable civilly, a permissive
inference criminally); assets can be frozen ahead of judgment; and everything
recovered pays victims' restitution first, then the fund. Then the ban that makes it
real: no one may insure, indemnify, or otherwise offset another person's individual
penalty, fine, or disgorgement — no policy, no gross-up, no forgiven loan, no
disguised raise — every such arrangement void in the state whatever law it names,
its benefits held in constructive trust. An entity violating this is penalized; a
controlling person doing so *knowingly* has committed a felony-tier act. Two honest
carve-outs: defense costs may be advanced and insured (repayable by anyone finally
adjudicated a wilful violator), and **restitution to victims is fully insurable and
always paid first** — deterrence aims at the wrongdoer's penalties, never at the
victims' recovery. The ban is prospective, with a [twelve]-month window for
contracts already in force.

**SEC. 8 — Certification.** Before any material deployment, and after any material
change, the chief executive — or, where no such office exists, each most-senior
executive, severally; no corporate form escapes into headlessness — personally
certifies compliance with the applicable standards or discloses identified
noncompliance, on the structure every public-company CEO has signed since
Sarbanes–Oxley. "Material deployment" and "material change" are defined in the text
(first in-state deployment; new tool or permission classes; expanded autonomy;
weakened safeguards) and the Agency may sharpen but never narrow them; everything
*below* the material line still gets certified, batched, at least once each
[calendar quarter] in which changes occurred. The duty cannot be delegated. The
certification is statements of fact after reasonable inquiry — no one is compelled
to opine on a model's risks or merits. Disclosing noncompliance satisfies the duty
to certify, but constitutes neither compliance nor validation nor a defense, and a
certification carrying *unremediated* material nonconformity must say so on its
face. Filed with the Agency, not published. Knowingly false: felony. Recklessly
made, without the inquiry: the base offense.

**SEC. 9 — Incident reporting.** What must be reported: exfiltration or loss of
control of weights; loss of operator control; a system's autonomous access to
protected third-party systems; death or serious injury materially caused by a
system; a system deceiving its own safety or monitoring controls; a serious
near-miss — an event that only intervention *other than controls operating as
designed*, or plain chance, kept from being an incident; or a reproducible
evaluation finding of materially increased risk. Two calibrated exclusions: behavior
deliberately elicited and contained in a sandbox, and events caught by defenses
working exactly as designed before any external effect — both *recorded*, neither
*reported*, so defence-in-depth is never punished for succeeding. The clock:
preliminary notice within 72 hours of credible notice (24 where death or serious
injury is imminently risked), full report in [30] days — an unfinished
investigation extends nothing — updates within [10] days. And the clock's teeth: it
runs from when the incident was detected *or would have been detected by the
monitoring the entity certified it maintains*. Deleting the logs does not stop time.
Reports are facts-only — no compelled characterizations — filed with the Agency,
not published.

**SEC. 10 — Enforcement and penalties.** Entities: strict-liability civil penalties
up to \$[1,000,000] per violation per day (\$[3,000,000] after a prior final
adjudication), assessed on the classic Clean Water Act factors, never less than the
economic benefit of the violation, inflation-indexed by rule. Individuals: the base
offense is a [misdemeanor — up to a year, and up to \$[100,000] or twice the gain];
the enhanced tier a [felony — up to three years, \$[250,000] or twice the gain]; and
where death or serious injury results, the federal tampering geometry — up to twenty
years per person seriously injured, any term or life (minimum [two] years) per
person killed, per-victim counts as jury elements. Consecutive sentences require
stated findings and cap at [forty] years aggregate for one course of conduct — life
for death preserved. **Restitution to every victim is mandatory at every tier and
outranks every penalty, fine, and disgorgement in the claim on a defendant's
assets**; fines for natural persons scale to means, so like culpability bears like
burden. The remedy chest: injunctions; suspension of an identified model version
and configuration (operating a suspended one with notice is contempt *and* a fresh
offense); emergency ex-parte suspension on probable cause of imminent death or
serious injury, with a hearing within [10] days; disqualification from ever serving
as a controlling person; suspension and debarment from state contracting. The
Attorney General enforces. A company paying an individual's penalty extinguishes
nothing and is itself a violation. All recoveries, after restitution, feed the
[Frontier AI Accountability Fund], which pays whistleblower awards and survives the
severance of anything around it.

**SEC. 11 — Whistleblowers.** The inspectors already work at the laboratories; this
section pays them. Original information leading to sanctions over \$[1,000,000]
earns 10 to 30 percent of what is collected, on the SEC's own structure, paid from
the fund whatever the money's source. Reports may be anonymous through counsel;
identities are protected, including in the award. No one may impede communication
with the Agency — any gag or contractual condition purporting to is void.
Retaliation buys the reporter reinstatement, double back pay, and fees. The Agency
must act on, or publish a reasoned declination of, every credible report within
[180] days.

**SEC. 12 — Machinery.** Effect [90] days after enactment; until the Agency exists
to receive them, filings go to the Attorney General, who hands them over when it
does — no duty ever waits on furniture. A [180-day] transition for systems already
deployed; no retroactive liability, ever. Records sufficient for audit — versions,
compute, evaluations, tool and permission manifests, change histories, and the
compensation records disgorgement runs on — kept [ten] years, or [five] after the
system last operates in the state, whichever is later, with a litigation hold from
the moment of notice. Reports, certifications, and validation materials are exempt
from public-records disclosure and sealed where security-sensitive — but the
exemption creates no privilege, hides no underlying fact from discovery, and
restricts no enforcement use. Corporate shape-shifting buys nothing: mergers,
dissolutions, and asset sales carry the entity's liabilities to the successor —
while no natural person's criminal liability ever transfers to anyone. Limitations:
[five] years, from the last day of a continuing violation, from *discovery* where
concealed by affirmative act, and [ten] for the death-and-injury tier. The whole
Act is construed to reach the persons with the greatest practical authority, and
never to let anyone's liability be discharged through someone else's.

**SEC. 13 — Severability, conforming operation, and revival.** The armour. Every
provision severs; courts must cut narrow before broad, and cut in reverse rank
order — the criminal core (the offenses, SEC. 4 and 6, the operator-side duties,
the penalty spine, and the machinery that feeds them) is declared first-rank,
enacted-regardless; the developer-side and release duties, then certification and
reporting, stand in later ranks to absorb federal fire first. No severance may
strip a surviving offense of an element it depends on — the standards and
commencement provisions live on to serve any offense that survives, the civil and
criminal penalties sever independently of each other, and the fund persists
whatever falls. Conforming operation makes preemption administrable rather than
fatal: the Attorney General, by published order, suspends *only* what a federal
enactment actually preempts, *only* to that extent, *only* prospectively — with
standing directions to preserve operator-side duties where only developer
regulation is preempted, post-deployment application where only pre-deployment law
is reached, and the underlying record-keeping wherever a reporting duty falls; no
one can be convicted for conduct during a suspension. And revival: a suspended
provision is not repealed — when the federal enactment sunsets, lapses, or is
struck down, the Attorney General must publish a terminating order within [30]
days, and the provision wakes back up, prospectively. A federal switch-off statute
that later dies cannot leave this Act dark.

*That is the whole law. Fourteen sections; the doctrine is eighty years old; the
only new part is who it reaches. [Verify it](#verify-it).*


---

*Corrections to the project contact; they enter [the errata register](../ledger/errata.md) with the fix attached and permanent credit.*
