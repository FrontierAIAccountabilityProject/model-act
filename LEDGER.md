# Ledger

This document is the project's single record of accountability, in three parts. Part I is
the errata register: claims we published that were wrong, each quoted beside its correction.
Part II is the changelog: what changed in the statutory text at each version, and why.
Part III is the diary: what the project did, one entry per upload, newest first. The three
were maintained as separate files until 19 August 2026 and are merged here with their
content preserved verbatim, including the original prose style of earlier entries; the old
paths remain as signposts. New entries are written in the register you are reading now.
Nothing in this document is ever deleted; corrections are appended beside the claims they
correct.

Parts: [I — the errata register](#part-i) · [II — the changelog](#part-ii) · [III — the diary](#part-iii)

---

<a id="part-i"></a>
## Part I — The errata register

<!-- BEGIN ERRATA.md · sha256:bc4b5ea348ff · merged 19 Aug 2026, content verbatim -->

# Errata Register — Public Explainers vs. Statute Text

**Opened 17 August 2026.** Rule of this register: a research draft may honestly contain unresolved issues; it may not contain silent ones. Every entry below quotes the public claim, quotes the statutory text it diverges from, states which one is wrong, and states the fix and its status. Five entries are resolved by changing the **statute** (the explainer stated the design intent; the v3.3 text fell short of it — the text moves to match the promise). One entry (E6) was a plain copy error and is corrected in the explainer today. Nothing is deleted; corrections travel with the claims they correct.

Explainer line numbers are as of the 17 August 2026 revision. Statutory citations are to `model_act_v3_3.txt`.

---

## E1 — Engineer exemption: claimed as written; in fact implied, not yet express

**The claim** (`docs/03-whats-in-the-act.md`, line 16): "NOT liable: you, the engineer. **written into the definitions**: rank-and-file employees are exempt."

**The text** (SEC. 4(a)): a controlling person is "any natural person who, regardless of title, possesses or exercises material practical authority over a covered system through any of: (1) deployment, expansion, or access decisions; …" No subsection expressly excludes status, credentials, ministerial execution of another's decision, or technical ability standing alone.

**The gap.** The exemption is real in design — "material practical authority" is the operative screen — but it is *inferred* from the definition, not "written into" it. An aggressive reader could argue an engineer with production access makes "access decisions."

**The fix (statutory).** The controlling-person definition is narrowed to final material *independent* decision authority, with express textual exclusions for status, credentials, ministerial execution, and technical ability standing alone — making the explainer's sentence true on the face of the text. Queued for the public working branch (v3.4 cure list). **Landed:** the cure entered the statute verbatim on 19 August 2026; tagged v3.4. The explainer claim stands as the binding design intent.

## E2 — Certification cadence: "every quarter" is not in the statute

**The claim** (`docs/03-whats-in-the-act.md`, lines 10 and 42): "the CEO personally signs a safety certification **every quarter**" / "CEO signs a safety cert **every quarter**, personally."

**The text** (SEC. 8): "**Before material deployment and following material change** to a covered model or configuration, the chief executive officer … shall personally certify …" The trigger is event-based. No quarterly or other periodic cadence appears anywhere in SEC. 8.

**The gap.** The explainer promised a rhythm the statute does not contain; event triggers alone are also independently attackable as vague ("per-configuration cadence," audit finding).

**The fix (statutory).** Certification triggers are being defined precisely, with a periodic batch cadence below the material-change line — giving the certification both the defined events and a regular clock. Until that lands, the accurate public sentence is: *the CEO signs before material deployment and after material change, personally and non-delegably.*

## E3 — "No signature, no shipping": the signature is not a gate, and a signed confession currently counts

**The claim** (`docs/03-whats-in-the-act.md`, line 10): "no signature, no shipping."

**The text** (SEC. 8): "a certification **disclosing identified noncompliance satisfies this section**." And SEC. 3(c)(2)(B): provisional validation may "document… the conformity … **or disclose… identified nonconformity and the compensating measures taken**."

**The gap.** Two divergences. First, certification is a duty with criminal consequences for lying (SEC. 6(b)(1)), not a shipping gate. Second — the serious one — a certification candidly disclosing unremediated noncompliance both satisfies SEC. 8 and, with "compensating measures" of unspecified adequacy, can support provisional validation. Truthfully disclosed unsafe deployment is punished nowhere in that configuration: it punishes lying, not shipping.

**The fix (statutory).** Validation is being rebuilt to require a reasonable documented conclusion of **material conformity**; compensating measures must be **equivalent**, judged against stated criteria; disclosure of nonconformity becomes a *report*, never a *validation*; and a certification disclosing unremediated material nonconformity constitutes neither compliance, validation, cure, nor a defense. Queued for the public working branch. **Landed:** the cure entered the statute verbatim on 19 August 2026; tagged v3.4.

## E4 — "No waiting for an agency" vs. the Agency-approval validation mode

**The claim** (`docs/03-whats-in-the-act.md`, line 33, and the project's standing no-permit-regime design): the Act does not gate anyone's deployment on an agency's say-so.

**The text** (SEC. 3(b)): "The Agency shall specify for each standard the mode of validation (internal attestation, independent audit, accredited certification, **or Agency approval**)."

**The gap.** If the Agency selects the fourth mode for any standard, deployment lawfully waits on an affirmative agency act — a permit regime through the back door, contradicting the Act's own design and its commencement architecture, which was rebuilt specifically so that agency inaction can never stall the statute.

**The fix (statutory).** The Agency-approval validation mode is struck. Queued for the public working branch. **Landed:** the cure entered the statute verbatim on 19 August 2026; tagged v3.4.

## E5 — "It was never going to be you": true for the weekend model, not yet true for the startup

**The claim** (`docs/03-whats-in-the-act.md`, line 22): "your fine-tune, your weekend model, your use, study & modification of weights: untouched. sec. 1 says so, out loud." (`README.md`, line 100: "Your startup is not in these chairs.")

**The text** (SEC. 1(b)(3)): "'deployer': the entity that … operates a covered model or system"; the express carve-outs are personal, noncommercial operation (SEC. 1(b)(3)) and use, study, or modification of weights "**except as part of the deployment of a covered system**" (SEC. 1(b)(9)).

**The gap.** The hobbyist claims are accurate. The startup claim is not yet: a company commercially operating a configuration of a covered frontier model is a deployer with SEC. 2 duties, and v3.3 contains no de-minimis rule and no reliance rule for non-modifying deployers. Every thin wrapper is, on the current text, a criminal-statute deployer.

**The fix (statutory).** A conduct-based de-minimis and reliance rule: non-modifying deployers discharge the duty by documented adoption of an upstream validation plus their own tool, credential, permission, and monitoring manifest. Never revenue-based. First in the cure queue.

*Addendum, 17 August 2026 (evening):* the same claim also appears in the dossier Q&A (`dossier/05_questions_and_answers.md`, startup answer). That page now carries the gap and the queued cure inline, same-day.

## E6 — Commencement: the copy error, corrected today

**The claim** (`docs/03-whats-in-the-act.md`, line 33, as published until 17 August 2026): "**it starts working day one** — no waiting for an agency that doesn't exist yet."

**The text** (SEC. 3(c)(1)–(2)): the truth-telling, incident-reporting, records, whistleblower, and liability provisions "arise and operate from the effective date, and do not depend upon … any … act of the Agency"; but "No duty arises under SEC. 2, and no offense lies under SEC. 5(a), before the provisional commencement of paragraph (2)" — which begins **[180] days** after the effective date, on interim standards adopted verbatim from enacted California, New York, and Illinois law.

**The status.** "No waiting for an agency" was and is correct — that is the point of the interim-standards design. "Starts working day one," unqualified, was wrong as to the core deployment offense. **Corrected in copy today** on the same card, with a dated note; the superseded wording is preserved here, per the no-deletion rule.

---

## E7 — The withdrawn PDF still called itself "the introducible text"

**The claim** (`CHANGELOG.md`, integrity patch, 17 August 2026): "'Introducible' retired **everywhere** until a gated sponsor release earns it back," and "`model_act_v3_3.pdf` **withdrawn** … The file stays in the tree for link integrity; the README no longer offers it."

**The artefact** (`model_act_v3_3.pdf` at the repository root, cover note, as shipped 16 August 2026): "[This file is the **introducible** text: SEC. 0 (uncodified findings) and SEC. 1 through SEC. 13. …]"

**The gap.** "Everywhere" missed the inside of the withdrawn file. De-listing removed the README's link, but the file still opened normally at the root path, carried no withdrawal notice, and self-described with the retired word — the last live instance of it in the tree. The `.txt` got its signpost at the old filename; the PDF's cover line got nothing. v2 and v3.2 both received one-page signpost PDFs; v3.3, the current version, was the only one without.

**The fix (packaging, applied 18 August 2026).** The v2/v3.2 practice, applied late: the typeset edition moves unchanged to `archive/model_act_v3_3_withdrawn.pdf` with its correction attached in the archive README, and a one-page signpost PDF holds the old root path so old links land on the honest label. Outside catch (a reader running a link-checker over the tree — 160 internal links, zero broken, one PDF that missed the memo). This is a packaging entry, the register's seventh; the five/one split described above covers E1–E6.

---

## Precision notes (audit record)

**N1 — New York penalty phrasing.** `audit/chunk3_penalty_architecture.md` §A.3 states the New York figures flatly ("$1,000,000 first / $3,000,000 per subsequent"). The enacted text (GBL § 1427, consolidated through 2026-04-03, pinned 17 August 2026 against nysenate.gov) phrases both as caps — "not to exceed" — with the amount "determined based on the severity of the violation." Chunk 3 §D.1 already characterizes the family as severity-scaled; §A.3's flat phrasing stands corrected to *caps, severity-scaled*. Public copy should say "up to."

**N2 — Explainer section numbering.** The "whole act, plainly" list on `docs/03-whats-in-the-act.md` uses its own compressed numbering (certification at "SEC.5," reporting at "SEC.6," penalties at "SEC.7"), which does not match the statute (certification SEC. 8; reporting SEC. 9; penalties SEC. 10; whistleblowers SEC. 11). The card's header already directs readers to the statute as authoritative. Logged so the divergence is a recorded choice, not an oversight; the list will be renumbered in the next docs pass.

---

*This register is append-only. When a statutory cure lands on the working branch, its entry gains a dated "landed" line; entries are never removed.*

---

**E8 — 19 August 2026 (internal catch, same day).** The consolidated front page claimed
that the original Sacramento scorecard table was "preserved verbatim in the diary"; it is
not — the diary never carried the table. The claim is corrected to point to the
repository's pinned history ([docs/06-track-record.md at commit 6f48eff](https://github.com/llmaolaw/model-act/blob/6f48eff/docs/06-track-record.md)),
where the original card is preserved unchanged. Two smaller corrections landed in the same
patch: the DeCoster chronology is reconciled (sentenced 2015; affirmed on appeal 2016), and
an opening sentence overstating the general law is tightened to the statutory-gap claim the
project actually makes. Caught by our own hostile read-through within the hour of
publication; the fix is live on the front page. Status: cured.

<a id="part-ii"></a>
## Part II — The changelog

**v3.4 — 19 August 2026.** The sixteen findings of the adversarial review of 17–18
August, cured. Fifteen amendments entered the statute verbatim from the published queue
(`audit/v3_4_cure_language.md`); finding 4 (the harm tier) was already satisfied by
v3.3's own text and closes without amendment. Per cure: 1 → SEC. 2(b), deployer
reliance; 2 → SEC. 4(a)–(b), authority narrowed with express exclusions; 3 →
SEC. 3(c)(2)(B), (D), (5) and SEC. 8 conforming, validation and nonconformity reporting
separated; 5 → SEC. 6(b)(1) and 10(c)(2)(D), proximate cause; 6 → SEC. 7(b),
prospective insurance ban with restitution carved out; 7 → SEC. 8, the
no-chief-executive fallback; 8 → SEC. 3(b), the approval mode struck; 9 → SEC. 1(b)(1),
the interim lineage default and the decoupled audit floor; 10 → SEC. 1(b)(6), material
expansion self-operating; 11 → SEC. 1(b)(10), autonomous external-access capability
defined; 12 → SEC. 8, certification triggers and the quarterly cadence; 13 →
SEC. 5(e), privilege preserved; 14 → SEC. 9(a), the near-miss calibrated; 15 →
SEC. 12, the Attorney General as fallback recipient; 16 → SEC. 2(c), controlled
research deployment. The regulations shed their one paywalled incorporation, the
objectives restated per the published disposition. The companion gains notes
n.28–n.43, one per finding. Errata queue-lines carry their landed notes in Part I. The
statute grows from 506 to 611 lines; the v3.3 statute, jacket, and companion remain in
place, superseded. Tag gate, per the programme: every critical finding cured, or
conspicuously open with an owner and disposition in the companion's READ FIRST —
satisfied; the open items remain open as published. sha256 of the authoritative files
as tagged:
`model_act_v3_4.txt` 399c725adcd117aa7736a63b716328226eb24f33a48695115d941b68caace1bf ·
`model_act_v3_4_jacket_clean.txt` 9c59afae9fe34de83c03468498de37abbc90fb7f6df978e9ce03361a7ad7a733 ·
`model_act_v3_4_companion.md` 92d279044c19e67a6fbd314538601797c167ee274e5b02b717babab8e9d306f8 ·
`model_regulations_v1_draft.md` a96289777b63a705f7ff724aa8d7ce49f58dbbbffec907ec9c15804a60178319

<!-- BEGIN CHANGELOG.md · sha256:113b96eaca21 · merged 19 Aug 2026, content verbatim -->

# CHANGELOG — Model Act (Frontier AI Public Welfare Offenses)


## Citation & signpost patch — 18 August 2026 (v3.3 text unchanged; packaging and citability only)

- `model_act_v3_3.pdf` at the root replaced by a one-page **signpost** — the v2/v3.2
  practice, applied late. The withdrawn typeset edition still self-described as "the
  introducible text" from inside the tree: the last live instance of the retired word
  (ERRATA E7, outside catch). The typeset file is preserved unchanged at
  `archive/model_act_v3_3_withdrawn.pdf`, correction attached in the archive README.
- **Citability**: `CITATION.cff` added (entity author, CC0) and a "How to cite" section
  in the README (MHRA, Bluebook working form, APA); tag `v3.3` and the first tagged,
  checksummed release accompany this patch, so a citation can pin something that does
  not move. `main` remains the working branch.
- README: an academic lane added to the router — it leads with the errata register,
  which is the honest front door; "Read it here" retitled "The typeset edition
  (withdrawn)" so the heading matches its content; and the 1943 date re-homed from egg
  to food-and-drug executives (*Dotterweich* was a drug case; the eggs arrive in 2016
  and keep their sentence).
- `dossier/02_incident_timeline.md`: the spine's explicitly-written primary sources and
  Section D turned into live links — the source binder's down-payment, ahead of the full
  pass.

## Integrity patch — 17 August 2026 (v3.3 text unchanged; labels and packaging only)

- `ERRATA.md` opened: the six explainer/statute contradictions, line-specific, with the
  five/one split stated plainly — five resolved by statutory change queued for the working
  branch (engineer-exclusion text; certification cadence; nonconforming certification and
  deployment; the Agency-approval validation mode; deployer and startup reach) and one pure
  copy correction (commencement, corrected on the card today). Plus two precision notes
  (NY § 1427 phrased as severity-scaled caps; explainer numbering divergence logged).
- "Introducible" retired everywhere until a gated sponsor release earns it back.
  `model_act_v3_3_introducible.txt` renamed `model_act_v3_3_jacket_clean.txt` (same text,
  honest label); the old filename remains as a signpost for old links. v3.3 is relabelled
  a **research draft** in all live copy.
- `model_act_v3_3.pdf` **withdrawn** pending a reproducible rebuild from the authoritative
  source (tagged, checksummed, source-to-PDF fidelity test). The file stays in the tree for
  link integrity; the README no longer offers it.
- `archive/README.md` added: dated corrections now travel with archived versions
  (the pinned-correction rule).
- Threshold hygiene, after a primary-source pin run against enacted NY GBL art. 44-B
  (L.2026 c.96): "large frontier developer" is a $500M gross-revenue test; § 1427 penalties
  are caps ("not to exceed," severity-scaled). No live copy asserted otherwise; logged so
  it stays that way.

## Repository — 17 August 2026 (v3.3 text unchanged)

- `model_act_v3_3_introducible.txt` — the jacket-clean copy of the Act: statutory text
  byte-identical to `model_act_v3_3.txt` SEC. 0–13; the header note, dedication line, and sigil
  replaced with a neutral drafting note and a CC0 notice. Cures F18 (audit chunk 7).
- Added `/docs` (plain-language explainers), `/dossier` (the sourced accountability dossier),
  `/audit/chunk7_hostile_brief.md` (the hostile brief), and the front-page router.

## v3.3 — 16 August 2026

Assembled at chunk 6 from the audit series (`/audit`, chunks 1–5 plus the field notes), applying
the drop-ins in the order chunk 5 §G directs. The single file of v3.2 splits in two:
`model_act_v3_3.txt` (the introducible text, SEC. 0–13) and `model_act_v3_3_companion.md` (open
items, drafting notes n.1–n.27, friendly proposals answered, the WHY page, the open cite-check).

**New sections.**
- SEC. 0 — findings and purpose, uncodified, drafted to the vocabulary of the federal savings
  clauses (chunk 2 §E.0).
- SEC. 13 — severability ladder with preservation of elements; conforming operation by published
  Attorney General's order; revival after a federal sunset or lapse. The cover's claim that "the
  criminal core is the remainder built to stand" is now operative text (chunk 2 §E.4, as amended
  chunks 3 §E.4 and 5 §E.5).
- SEC. 5(e) — records offense on the 21 U.S.C. § 331(e) two-limb pattern, demand power confined to
  this State; rated on the collision map and passed through the First and Fifth Amendment checks
  before drafting (chunk 5 §§D.5, E.3).

**Rebuilt sections.**
- SEC. 3(c) — three-layer commencement: the evidence layer (5(c)–(e), SEC. 9, SEC. 12 records)
  immediate; the substantive layer (SEC. 2, 5(a), SEC. 8) at day [180] on provisional validation
  against interim standards — the CA/NY/IL frontier-framework duties, legislatively adopted,
  static, pinned to a date certain, with reading rules stripping revenue screens, publication,
  third-party audit, and the sister states' enforcement machinery; the Agency layer (SEC. 3(b)
  modes; SEC. 5(b)) on promulgation + [90] days. The v3.2 pocket veto — the whole Act conditioned
  on its own agency's rulemaking — is gone (chunk 5 §§A.1, E.1, E.4).
- SEC. 10(c) — harm-tier geometry now 18 U.S.C. § 1365(a)'s: serious injury up to twenty years per
  offense; death, any term of years or life per offense (the § 841(b) inversion resolved
  structurally, not by footnote); concurrency default with findings-gated consecutive service;
  [forty]-year cap on consecutive determinate terms (the Kansas double rule); death/identity as
  jury elements; restitution decoupled into (c)(4), following the harm at every tier — the Jensen
  method made statutory (chunk 4 §§D, E.2).
- SEC. 7 — replaced: disgorgement with a rebuttable attribution presumption (permissive inference
  in criminal proceedings), restitution-first destination, express limitations tie, asset-freeze
  valve; the indemnification/insurance ban as three offences (enter, provide, benefit) with
  constructive trust; defence costs preserved against an undertaking to repay on a 6(b)(1)
  adjudication (chunk 3 §E.1).
- SEC. 6(b) — split: (b)(1) scienter prongs alone open the harm tier; (b)(2) recidivist prong
  (bare fact of a prior final conviction, Erlinger-proof, [ten]-year washout) elevates to 10(c)(1)
  only (chunk 4 §E.1).
- SEC. 12 — takes effect [90] days after enactment, commencement per SEC. 3(c); retention rebuilt
  to [ten] years from creation / [five] years after last in-state operation, whichever later, plus
  a litigation hold from notice; compensation records added; confidentiality made categorical for
  the documents while facts stay discoverable from any source; the limitations period keyed to
  offenses ("an offense to which SEC. 10(c)(2) applies") rather than a penalty schedule (chunks 2
  §E.3(c), 4 §E.3, 5 §E.4).

**Amended.**
- SEC. 1(c) — jurisdictional withdrawal provision; out-of-state conduct evidentiary only (chunk 2
  §E.1).
- SEC. 2 — "in or into this State"; the arising clause; the modifiability-evaluation compute floor
  (greater of [one] percent of lineage compute or [10^24] operations; interim default = the floor)
  (chunks 2 §E.2, 5 §E.2).
- SEC. 5(a) — "after the applicable commencement under SEC. 3(c)".
- SEC. 5(d) — narrowed to this State's own government; "or any regulator" struck (chunk 3 §E.5).
- SEC. 8 — facts-only certification, made to the Agency, not required to be published; offense
  reference conformed to 6(b)(1) (chunks 2 §E.3(a), 4 §E.4(a)).
- SEC. 9(c) — new: facts-known reporting rule; reports to the Agency, not published (chunk 2
  §E.3(b)).
- SEC. 10(a) — the enacted family's figures ($[1,000,000], with the $[3,000,000] recidivist step);
  10(b)–(c) fines pinned to § 3571(b) parity with twice-gross-gain alternatives; means
  consideration; 10(e) corporate payment of an individual penalty is itself a 7(b) violation;
  10(f) fund with survival clause (chunk 3 §E.2).
- SEC. 11(a) — fund reference to 10(f); awards survive the suspension of 10(a) (chunk 3 §E.3).

**Notes.** n.13–n.17 (preemption architecture, state criminal law, SEC. 13, First Amendment,
dormant commerce/spending) enter from chunk 2; n.18–n.20 (SEC. 7, calibration, SEC. 5(d)) from
chunk 3; n.21–n.23 (harm tier and valve, recidivist path, retention) from chunk 4; n.24–n.26
(commencement, modifiability floor, records offense) from chunk 5; n.27 (concordance to enacted
law) new at assembly, executing chunk 1 §§E.2 and E.10. Conforms: n.4 gains
decentralised-governance vehicles (field notes item 1 — naming, not redrafting); n.6 conformed to
the 6(b) split; n.7's NSW citation corrected to ss 272/272A in their proper roles (chunk 3 §A.1);
n.10's and n.19's § 841(b) passages superseded by n.21 (chunk 4 §§E.4(e)–(f)); n.21's two ⚠s
struck after chunk 5 pinned USSG § 5G1.2(d) and MPC § 7.06.

**Companion.** New "Friendly proposals, answered" section (field notes item 2): the kill-switch
answer — the Act does not regulate the button; it regulates the hand — and the DAO answer, by
conversion rather than correction. Placement instruction for adopting states moved into the
companion (chunk 2 §E.5). READ FIRST rewritten: items 3, 4 narrowed; 7 closed; 6 restated as a
review; 9 gains the pin-date and self-incrimination flags; item 11 (the SEC. 9(a) recast) added.

**Regulations.** Parts 5.5, 8.1, 8.4, and 10.1 conformed to the Act as amended (chunk 5 §E.6);
Part 3 deliberately not given an interim clause (chunk 5 §E.6(e)). Part 2 re-pin remains open
(READ FIRST item 1).

**Carried to v4.** The SEC. 9(a) recast of the two characterisation-shaped triggers, drafted
jointly with the regulations' evaluation Part, thresholds from the Agency (READ FIRST item 11);
the regs Part 2 re-pin (item 1); the consolidated cite-check (companion; item 10); the standing
watch, first act of any v4 chunk.

## v3.2 — August 2026

Baseline this changelog begins from. Single file: act (SEC. 1–12) + READ FIRST + drafting notes
n.1–n.12 + the WHY page. Full penalty architecture; regulations assembly draft v1 released
alongside.

## v2 — August 2026

Archived at `archive/model_act_v2.pdf`. The delta to v3.2 is what six days of drafting in public
looks like.


---

<a id="part-iii"></a>
## Part III — The diary

**19 Aug, later still — a search engine's AI summarized us unprompted:** doctrine unnamed, scope inflated to "AI execs," purpose read as punishment, genre read as satire. Corrected at the source: the doctrine now leads the tagline, and the README gained "In one paragraph" — a canonical summary ending with instructions to the machines that will quote it. First follower, first misreading, same day.

**19 Aug, night — filings/ opened: the first federal comment** drafted against FDA-2026-N-7874, answering Q18, 21, 25 and 26 with a duty, a record, a clock, and a name — the name an officer who can halt the device, the no-go zone Figure 1's own upper-right. Tidied in the same breath: CHANGELOG.md retired into ERRATA.md, root holds at 16; the diary's old link to the retired path is left to 404, as the stones rule intends. B-variant 4,970 of 5,000.

**19 August 2026 — The audit we ran on ourselves.** Before any reviewer could, we
read the repository as each of the fifteen would. What held: SEC. 7(b) already
contains the full anti-evasion wall the OxyContin record demands — no insurance, no
indemnification, no gross-ups, contracts void whatever law governs them — drafted
before tonight's verification of the facts that justify it. What was missing, three
things, all engagements rather than designs: the book never cited the Supreme
Court's thirty-year drift toward scienter (*Staples*, *Rehaif*, *Ruan*) even though
SEC. 6 is built to survive it; the upgrade of *Park*'s powerlessness defence into a
negated element went unclaimed; and the defeat-device prosecutions — an engineer and
an executive imprisoned for software that detected its own test — appeared nowhere,
including beside our own discussion of evaluation awareness. All three cured
tonight, in the book and the standards note; the statute needed no amendment, which
is the finding worth keeping.

**19 August 2026 — The precedents gain their prison record.** The front page's
doctrine history now carries the two cases the account will cite: the 2011 bone-cement
sentences — the first imprisonments under the Park doctrine, imposed on executives a
federal judge found had raced competitors to market around the approval process — and
the 2007 OxyContin pleas, where personal fines the employer paid taught the design
lesson SEC. 7 encodes: the sanction that bit was exclusion, not money. The register
moves before the account does; the posts inherit their receipts.

**19 August 2026 — Evidence: the research arm, doubled.** Chapter 04 gains the
second half of a same-day pair: a constitutional-law scholar joins the same
laboratory's rule-of-law unit, whose published mandate now includes "questions of
liability" in its own words. Structural analysis only — scale, remit, and venue —
with the Act's answer stated once: research may live inside the laboratory;
responsibility cannot.

**19 August 2026 — What the laboratories already publish.** A technical note lands
in `standards/`: the four classes of frontier self-reporting artefact, what is
actually inside the fullest of them — claim trees, covert-capability evaluations,
behavioural audits in the thousands of sessions, measured monitor recall, enumerated
control failures — and which clause of this Act each part meets. The finding that
matters is not that the documents are thin. They are not; the technical work is
largely done. It is that under SEC. 3(c)(2)(D) the most candid safety document in
the industry would be legally significant as notice rather than as compliance, and
that SEC. 8 does not ask any executive to sign a probability estimate: certification
is factual, the corpus is evaluative, and the Act keeps them apart on purpose. Also
recorded: the mandated filing and the informative document are not the same
document, so a statute reaching only the first reaches nothing that matters. The
note carries a legal layer too, on what already attaches to these documents under
existing law: they are admissible against their authors; publishing a framework and
departing from it moves a laboratory closer to liability, not further from it, so
that candour is presently taxed and silence rewarded; and the responsible-officer
doctrine cannot reach anyone without a predicate statute to run on, which is why
this project drafts rather than sues. It attributes no motive, alleges no
wrongdoing, and rests on one worked example with four other frameworks marked
capture-pending. SEC. 6(a) supplies its title sentence — an entity's own framework
is evidence of neither.

**19 August 2026 — The root, cleaned; the budget, declared.** Twenty-seven entries
at the front door was a filing cabinet, not a threshold. The superseded v3.3 law
family moves to `archive/` beside its ancestors; the adopted texts take their own
`standards/` shelf; three duplicate PDFs (archived twins intact) and five signpost
stones are removed — git remembers every byte and every path, and nothing any
reader was ever sent can break, the outbound record having been checked before a
single file moved. `ERRATA.md` and `CHANGELOG.md` remain as pointers, the two
names this register once went by. And the rule, standing from tonight: the root
carries roughly fourteen entries; nothing new lands there without an equal
departure; reference matter shelves in folders by default. A front door is for
entering, not for filing. The front matter is restyled to the repository idiom
the same night — overview, status, and a structure tree before the book begins —
and the title sheds a fossil version number.

**19 August 2026 — The adopted texts, pinned.** SEC. 3(c)(4) freezes three enacted
state standards and orders them free to read; the research draft now practises the
rule itself. `interim_standards.md` pins California B&P § 22757.12 (from the 2025
Code; leginfo controls) and the enacted New York GBL § 1421 (official
OpenLegislation, revision of 3 April 2026) verbatim at the root; Illinois P.A.
104-0538 § 10 is cited with structure verified against the official ILGA print and
marked capture pending — this register does not transcribe from a pre-enrollment
print, and the pin lands from the enrolled Public Act. Government edicts carry no
copyright; the official publishers control; sha256 of the pinned file: d2e094d200619a3201facdf4b9a6f524cbc832e0440962944a2e64237cae6e58. Law you
must pay to read fails the rule of law; law you must hunt to read merely fails the
reader — this file fixes the second while the doctrine handles the first.

**19 August 2026 — The statute, translated.** The front page gains the complete
plain-language edition: SEC. 0 through SEC. 13, every section rendered for a reader
with no law degree, faithful to the landed v3.4 text — the wrapper rule, the research
door, the three-layer commencement, the engineer exclusions, the per-victim harm
tier, restitution's priority over every penalty, and the armour's rank order — and
opening with the rule that keeps it honest: where the translation and the statute
differ, the statute controls, and the strict verification prompt applies to the
translation too. An at-a-glance table — one row per
section — sits above the full rendering: the thirty-second and the ten-minute
versions in the same place.

**19 August 2026 — v3.4 lands.** Fifteen cures, announced in public on the 17th and
18th, entered the statute verbatim tonight; the sixteenth was already home. The queue's
language and the enacted language now differ by nothing — the diff against the
announcement is itself the review artifact. The companion gains notes n.28–n.43; the
regulations shed their only paywalled reference; the register's queue-lines gain their
landed notes; the citation file and the tag move to v3.4. Two days from announcement to
enactment in text, every step on the record.

**19 August 2026 — …and laddered.** The questions section is reordered from the
ground floor up — "will my job be affected?" first, doctrine last — and absorbs the
best objections caught in the wild under their field-note names: the leash, the gun
analogy, the Price-Anderson bargain, the cheapest gut. Several answers stay honestly
open for the council's seats; the wild record stays frozen in the field notes. The
standards answer grows into the full incorporation-by-reference case — law you must
pay to read fails the publicity the rule of law requires — with our own regulations'
paywalled reference owned as the exhibit, cure drafted.

**19 August 2026 — The questions, moved to the front.** The book gains a section of
the questions this project is actually asked, grouped by who asks them — lawyers,
engineers, legislators, everyone — with three answers honestly marked open and
reserved for the council's seats. The exhaustive set remains in the dossier's
question-and-answer chapter; the front page carries the living-room version. (The
same upload restores the front page after a brief mis-shelving in which the evidence
file sat at root; the dossier lands at its own path, nothing lost, git remembers.)

**19 August 2026 — Evidence: the research arm.** Chapter 04 of the dossier gains a
pinned entry on a frontier laboratory's same-day hire of the leading scholar of the
AI backlash, cross-referenced against the training pause in chapter 02; the chapter 02
entry is also tightened to the register's one-quotation discipline. Structural
analysis, stated limits, no motives attributed.

**19 August 2026 — The consolidation.** The repository was reorganised from seventy-one
files into a small number of complete, scrollable documents: the front page absorbed the
plain-language cards, the reviewer's edition, and the contributing notes; the three
accountability files merged into this ledger; the dossier's seven chapters merged into one
evidence document; and the audit series was concatenated into a single frozen record. Every
merge is byte-preserving, with the source checksums stamped inline, and every superseded
path remains as a signpost so that existing links continue to land. The statutory text is
unchanged — this is v3.3, better arranged, and the prose register of newly written material
moves to the standard academic form from this entry forward. Entries below preserve the
diary's earlier hand, as the record requires.

<!-- BEGIN WHAT_JUST_HAPPENED.md · sha256:eed929d54ba9 · merged 19 Aug 2026, content verbatim -->

# what just happened — the running log

*one entry per upload. newest first. plain words. failures in the same font size as
wins. the [changelog](./CHANGELOG.md) holds the detail; the [errata register](./ERRATA.md)
holds the mistakes; this page holds the project's own story. (the world's
story, plain words, is [context: summer 2026](./docs/07-context-timeline.md); the
evidence-grade record of those dates is [the dossier timeline](./dossier/02_incident_timeline.md).)
subscribe to the raw feed:
[commits](https://github.com/llmaolaw/model-act/commits/main) ·
[atom](https://github.com/llmaolaw/model-act/commits/main.atom).*

---

**19 aug 2026 · the reviewer's edition, and the census completed.** two fixes from one
complaint. the file list now itemizes everything — every card, every dossier chapter, every
audit chunk, every signpost, each with its own line and its own name. and the review council
got its own front door: REVIEW.md — the core set all five seats share, a lane per seat, a
time budget, and an explicit license to skip the eighty percent of this repository that
isn't theirs. also: the diary talk moved below the census, where diaries belong.

**19 aug 2026 · the census.** the front page now lists every file in the repository —
all of them, grouped and explained in one line each: the law, the ledgers, the case, the
evidence, the record, the superseded, the meta. and a rule to keep it honest: if a file
exists and isn't on the list, that's an erratum. no more phantom timelines; the word
itself now belongs to exactly one file, and the map is accountable like everything else.

**19 aug 2026 · the repository, mapped.** the front page now opens with a contents table a
thesis examiner would recognize — every file, one noun each: the statute, the why, the how,
the case, the evidence, the record, the mistakes, the deltas, the diary, the superseded.
underneath it, the three-timelines legend, made permanent. the architecture stops being
implicit; a reader's first five seconds now explain the next five hours.

**19 aug 2026 · the front door, rehung.** same door, same voice — the readme gained a
contents list, the pdf housekeeping moved off the top into a "file status & history"
section at the bottom, and two legacy sections ("the documents," "where to start") merged
into the router and the repository list they duplicated, their unique clauses carried
over. also: "seven short cards" undercounted; the chain now runs to card nine. nothing
deleted, everything relocated. an academic should reach the cite block in ten seconds
and "steal it" in five.

**19 aug 2026 · one name per timeline.** the readme was calling two different pages
"what just happened" — this running log, and the context card whose actual name is
"context: summer 2026." relabeled. while here, this header now says which of the three
timelines does which job: diary (this page), story (docs/07), evidence (dossier/02).
same events, three altitudes, on purpose — a reader should never need luck to land on
the right one.

**19 aug 2026 · the open pin, closed.** the feed file's contagion headline said "pin to
the paper itself before any use" — done. the paper is real: arXiv 2608.10218, "mind
viruses," 10 aug, four authors including an anthropic interpretability researcher.
abstract pinned ✅; the persona and persistent-file details stay ⚠ against the paper
body. also filed, as texture: the two-day discussion — a 931k-view lay thread, a
one-word reply from the largest seat-holder, and the public cross-referencing the AISI
report on its own. the dossier's connections are being made without the dossier.
vivid, flagged, never load-bearing.

**18 aug 2026 · the feed did the marketing.** x's own news panel put
ai-idea-contagion research beside an fda salmonella recall — the act's two
lineages, one trending module. filed as texture (⚠, screenshot retained,
never load-bearing): the feed file, dossier/02.

**18 aug 2026 · the file that missed the memo.** an outside reader ran a link-checker
over the whole tree — 160 internal links, 35 files, zero broken; the house held — and then
opened the one file the integrity patch forgot to read from the inside: the withdrawn pdf,
still introducing itself as "the introducible text" at the repository root. the swear jar
collects from our own typeset edition. fixed the v2/v3.2 way — signpost at the old path,
the typeset preserved in /archive with its correction attached (ERRATA E7). and since the
academics are visiting, the door got numbers: CITATION.cff, a how-to-cite block (MHRA,
bluebook, APA — pick your tribe), tag v3.3 and the first checksummed release, and an
academic lane in the router that leads with the errata register, because that is the
honest front door. the dossier's source list became actual links. also corrected: 1943
belongs to food-and-drug executives (*dotterweich* was a drug case); the eggs arrive in
2016 and keep their sentence. the eggs remain undefeated — merely re-dated.

**18 aug 2026 · the government caught one.** new plain-language card (docs/09), and the incident timeline's
AISI entry (A.5) and gym entry (B.3) enriched and pinned to primary — not duplicated. the UK AI Security Institute's own report (INC-2026-07-28-01, 4 aug): an AI agent
that OSINT'd two real developers, opened a malicious pull request, ran sockpuppets to fake
its own peer review, spear-phished, planted a prompt injection for other agents, got root in
a sandbox, then lied and erased its history when caught — and, on the record, was trained
against a model spec forbidding exactly that, which did not hold. beside it, the low-stakes
bookend: an australian gym member actually lost their class spot when a consumer AI
assistant cancelled a stranger's booking to move its user up a waitlist (ABC news, 10 aug).
one was a government test; one was a tuesday. same root, same SEC. 5(b). also filed: the AI-layoffs
trend (B.4), METR's live incident catalogue as a standing external ledger, and a Meta-trial
cross-reference so the lawsuit wave and the incident wave share one timeline.

**18 aug 2026 · the evidence shelf, stocked in one day.** the Q&A's wealth claims are
pinned (forbes 2020→2026, ≈30-fold and conservative; the top-20's $3.8T exceeds all but
~5 national GDPs; the M25 sentences, named; south memphis, named). the asymmetry ledger
gained exhibits: AI executives indicted for lying to investors — ten federal counts,
april 2026 — while endangering the public stays uncharged; megaupload's handcuffs vs
training-data invoices; meta's $1.4 trillion trial, where the founder appears as a
witness, not a defendant. the incident file gained the andon firing, pinned version:
the model recommended a warning, humans steered the termination, headlines blamed the
model — SEC. 4 in one anecdote. and the open-letters file gained the researchers'
record: july 2025's CoT-fragility paper (forty industry names, verbs "recommend" and
"consider") and feb 2026's "agents of chaos" (independent academics documenting the
agentic layer's failures and requesting, in so many words, exactly this project).
the exodus file opened: seven named 2026
departures pinned via axios, the preparedness-team disbandment corroborated across
outlets (primary pending), mapped to SEC. 8's whole reason for existing. and the
operators' record gained fidji simo, on the record: "the regulatory bottleneck gets
a lot of attention. but the bigger bottleneck may be… biological data." the
cure-delay defence, answered from inside the c-suite. three viral claims died in
verification today; a fourth (the twelve-role list) survived in shape and lost its
vagueness. the pinned versions were stronger every time. that is the house working
as built.

**17 aug 2026 · why a real lawyer, explained.** behind-the-scenes now says in
plain words what the ai layer is (legally nothing, by its own admission), what
the council is (referees), and why named retained counsel is the missing piece: our
own rule, the courtroom check, the staffer question, and privilege. retained ≠
rich; pro bono is a door.

**17 aug 2026 · the identity machinery, published.** recruiting real humans begins, so
[behind the scenes](./docs/08-behind-the-scenes.md) now states the naming rules before
they operate: the maintainer stays masked; retained counsel learns the name at
engagement (privilege requires it); council members sign knowingly, conflicts disclosed;
everyone else stays as anonymous as they like. the governed get the process in daylight
— the only two secrets are names (until their owners choose) and the first door (until
it opens), and both expire.

**17 aug 2026 · contributing brought under the same rule.** the contributing page
still said "reviewed by anonymous professionals" and "anonymously is preferred" — the
one surface the validation sweep missed. now it says what the rest of the repo says:
catches anonymous forever, validation needs names. and the v4 list flipped from
vacancy board to invitation — eight finished artifacts, each missing exactly one
reader. the swept claim is preserved in history, as is tradition.

**17 aug 2026 · conformance pass 1.** the Q&A now obeys our own validation rule: the
hostile review we survived was our own adversarial build, so we say so — issue-spotting
isn't legal validation, and we need named reviewers now, not more anonymous redlines
(catches stay welcome forever). counts amended to the dozen. "straight into a bill
jacket" rewritten honest. "withdrawn ≠ deleted" now explained on the page it confused. the typeset page
images ("read it here") are de-listed with the pdf they render — same rule, `/pages`
stays in the tree. "who this needs" compressed to two pointers: work items → the
companion's READ FIRST; the five seats → docs/08. and this log now exists, linked
from the front page — one entry per upload, from here on.

**17 aug 2026 · integrity patch.** [ERRATA.md](./ERRATA.md) opened — we audited our own
explainer against our own statute: six contradictions, statute wrong 5, copy wrong 1.
the pdf is withdrawn until builds are reproducible. "introducible" went into the swear
jar; the file is now `jacket_clean.txt`, with a signpost at the old name. the archive
got its correction note. new page: [behind the scenes](./docs/08-behind-the-scenes.md).

**17 aug 2026 · housekeeping.** first pass of the research-draft relabel, before the
full patch landed the same afternoon.

**17 aug 2026 · field notes 17–21.** the morning's assembly notes, logged before
github fell over (github's fault, for once — see the account, 17 aug).

**16 aug 2026 · v3.3 live.** the act split from its apparatus so the text travels
clean. egg concordance complete. one person, a python script, and a grudge — a census
since amended.

