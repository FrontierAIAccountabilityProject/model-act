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

## E8 — "In one paragraph": true of the duty, silent on the entity, in the paragraph built to be quoted

**The claim** (`README.md`, "In one paragraph," as published to 20 August 2026): "The base duty is due care, **not strict liability**; the custodial tiers are maximums…"

**The text** (SEC. 10(a)): "Entity: civil penalty of up to \$[1,000,000] per violation for each day the violation continues… **strict liability**." And SEC. 6(c): "Entity liability under SEC. 10(a) **is strict**." And SEC. 1(a): offenses under the Act "are **public welfare offenses** within the meaning of *Morissette v. United States*, 342 U.S. 246 (1952), except where a greater mental state is expressly required."

**The gap.** The claim is exactly true of what it names — SEC. 2 is headed "PUBLIC WELFARE DUTY" and its base duty is the exercise of due care — and it is incomplete as a characterisation of the Act, which contains an express strict-liability limb and classifies its offenses into the *Morissette* family. The README states the qualified version correctly three times further down (SEC. 6 summary: "strict liability buys entity fines only"; the scienter-drift passage: "strict liability survives only where the modern Court tolerates it, in the entity's civil penalty under SEC. 10(a)"; the section walk: "strict liability is for entity fines only"). Only the summary drops the qualifier.

**Why it is graded higher than its size.** "In one paragraph" was written for machines to lift verbatim, after a search engine's AI summarised the project with the doctrine unnamed and the scope inflated (diary, 19 August 2026). It is the single most quotable passage in the repository and therefore the one place an omission propagates without the surrounding correction travelling with it. A reader who takes "not strict liability" from a summariser, opens SEC. 10(a), and finds the words "strict liability" has been handed a contradiction the project put in his way — in a project whose whole premise is that its claims survive being checked.

**The fix (explainer, applied 20 August 2026).** One clause, no statutory change: "The base duty is due care, not strict liability — **strict liability reaches an entity's civil penalty alone, never a custodial sentence**; the custodial tiers are maximums…" This conforms the summary to the three correct statements below it and to SEC. 6(c). Outside catch. The statute needed no amendment, which is the finding worth keeping: the drafting was right and the shop window was thin.

---


---

## Precision notes (audit record)

**N1 — New York penalty phrasing.** `audit/chunk3_penalty_architecture.md` §A.3 states the New York figures flatly ("\$1,000,000 first / \$3,000,000 per subsequent"). The enacted text (GBL § 1427, consolidated through 2026-04-03, pinned 17 August 2026 against nysenate.gov) phrases both as caps — "not to exceed" — with the amount "determined based on the severity of the violation." Chunk 3 §D.1 already characterizes the family as severity-scaled; §A.3's flat phrasing stands corrected to *caps, severity-scaled*. Public copy should say "up to."

**N2 — Explainer section numbering.** The "whole act, plainly" list on `docs/03-whats-in-the-act.md` uses its own compressed numbering (certification at "SEC.5," reporting at "SEC.6," penalties at "SEC.7"), which does not match the statute (certification SEC. 8; reporting SEC. 9; penalties SEC. 10; whistleblowers SEC. 11). The card's header already directs readers to the statute as authoritative. Logged so the divergence is a recorded choice, not an oversight; the list will be renumbered in the next docs pass.

---

*This register is append-only. When a statutory cure lands on the working branch, its entry gains a dated "landed" line; entries are never removed.*

---

**E12 — 20 August 2026 (internal catch, same day).** F1 — that nobody on the predecessor FDA
docket names an upstream person — was published in four places at a strength the finding's
own file forbids.

**The claim.** The front page's Recent entry and its contents table both described the
reading notes as "the predecessor comment file **read end to end**" reporting "the element
**none of them** names," of "the 51 comments." The [standing watch](./audit/standing_watch_2026-08-20.md)
made it the punchline of its headline finding: "fifty-one commenters named no upstream
person, and four frontier statutes name none either. Two independent evidence bases, the
same vacancy." The diary carried the same sentence.

**The text it contradicts.** F1's own strength note, in bold, in the file all four were
describing: "the wider claim is true of tiers 1 and 2 on reading, and is **not** certified
across all 51." The register said the same of F3. The repository asserted on its front page
precisely what it stated in bold, two clicks away, was not certified.

**What the roster then established.** The substance of **29 of the 51** has never been read
(§ 1.3). The claim was running over twenty-nine unopened comments. "Read end to end" was
false on its face about a file whose three-tier structure exists *because* it was not read
end to end.

**Why it is graded at E8's level rather than below it.** E8 was a summary of our own statute,
where the drafting was right and the shop window was thin. This is an empirical claim about
other people's documents, and its entire rhetorical force came from the number 51 — the
pairing "two independent evidence bases" does no work at 22. A hostile reader following the
front page to the notes would have been handed the contradiction by us, in a project whose
sole authority is that its claims survive being opened.

**The fix (copy, applied 20 August 2026).** No finding is withdrawn; each is restated at the
strength its evidence carries. The front page now reads "rostered in full and read in part —
every filer named, the substance of 22 of them read, and the element none of those 22 names."
The standing watch and the diary carry dated corrections in place, superseded wording
preserved. The statute needed no amendment. Internal catch, prompted by an outside reader
asking how the roster was counted.

**E11 — 20 August 2026 (outside catch; the roster).** The reading notes on docket
FDA-2024-D-4488 were compiled from 22 comments read in full or as posted text, 13 more known
by title, and 16 never enumerated at all. The complete 51-filer roster was then read from the
docket's three result pages, and it falsified four published claims in that file. Nothing here
touches the statute.

**(a) The substantive one.** The file called the National Multiple Sclerosis Society "the
file's only patient organisation," in the § 1.1 census and again in § 2. It is not: the
**National Health Council** (0034) — the American patient-advocacy umbrella — and **Pathway
for Patient Health** (0047) are both patient-side bodies, and both sat in the sixteen this
file had never enumerated. NMSS is the only *single-disease* patient organisation, which is
the claim that survives. The error is instructive about its own cause: a finding about who is
*absent* from a file was published while a third of the file was unread, and the two missing
filers were identifiable from their names alone. Corrected in both places, with the count
stated: four filings of fifty-one come from the patient side, twenty-one from industry.

**(b) "Anonymous" is not "unattributed."** Comment 0012 was recorded as unattributed with the
filer left `—`, on the reasoning that the attachment carried no signature block. The docket
names the filer **Anonymous**. It is a filer who took the option, not one who forgot the
letterhead — and it is one of **three** anonymous filings (0012, 0038, 0050), where this
project's campaign copy had said two.

**(c) An inference from a gap that was not there.** The file reasoned from the ID range that
"a small number were received and not posted." Comment IDs run contiguously 0003–0053 with no
gaps — exactly 51, the two docket documents taking 0001–0002. Nothing was withheld on this
docket, and the received-vs-posted lag observed live on FDA-2026-N-7874 gets no support from
here. A gap was asserted from arithmetic that was never done.

**(d) Two late comments were four.** § 5's guidance-dockets-never-close finding named Ikeda
(0051) and Yang (0053). 0050 (posted 12 Aug 2025) and 0052 (posted 17 Apr 2026) were also filed
after the April 2025 close. The finding strengthens; the count was wrong.

Two smaller catches in the same pass, below erratum grade and recorded for completeness:
Jitendra Pund's comment ID, previously `—`, is **0049**; and 0028 is posted under the
individual name **Cythika Bopearachchi**, one of the cohort members, not under the university
or Prof. Sampat.

**What the roster unlocked.** F3 — no frontier model developer filed — is **certified** against
the complete list, with the qualifier that must travel with it: none filed *in its own name*,
and two trade associations whose membership includes frontier developers (CTA 0035, Connected
Health Initiative 0039) did file. The project's running list had recorded F3 as blocked on
capturing five comments' *substance*. It never was: F3 is an absence-of-filer claim and needed
only a page-through of the roster. F1 and F8 are the findings that need the substance. Two
different blockers had been filed under one line, and the cheap one went unrun. Status: cured
in the reading notes; the substance of 29 comments remains uncaptured and is stated as such.

**E10 — 20 August 2026 (internal catch).** The statute's header bracket at line 5 refers to
"the open items for v4"; the next revision is v3.5, as the companion and the README now say.
The text is non-operative — the bracket is apparatus, not statute — and it is left uncorrected
on purpose. `model_act_v3_4.txt` is tagged, checksummed in the changelog, published as the
source hash of the reviewer's copy (`399c725adcd117aa7736a63b716328226eb24f33a48695115d941b68caace1bf`),
and archived at CERN under DOI 10.5281/zenodo.22029795. Editing a byte would falsify the
reproducibility chain rather than improve the text: the PDF would no longer rebuild to its
published hash, and the claim a reviewer is invited to check would become false. Corrected at
v3.5, when the file re-hashes anyway. Status: open by design, closes at the next revision.

**E9 — 20 August 2026 (internal catch).** The register's own rule — "when a statutory cure
lands on the working branch, its entry gains a dated 'landed' line" — was applied to E1, E3, and
E4 but not to E2 or E5, which landed in the same tagged revision. Both are recorded here rather
than edited into the sealed block above. **E2 (certification cadence)** landed at v3.4 on 19
August 2026 as cure 12: SEC. 8 now defines its triggers and requires changes below the material
line to be certified in a periodic filing at least once in each [calendar quarter] in which any
occurred (companion n.39). The explainer's "every quarter" is true on the face of the text as to
sub-material changes; material deployment and material change remain event-triggered. **E5
(deployer and startup reach)** landed at v3.4 on 19 August 2026 as cure 1: SEC. 2(b) gives
non-modifying deployers a conduct-based reliance rule — documented adoption of an upstream
validation, a manifest of tools, credentials, permissions, and external access, monitoring within
the deployer's control, and reporting within its knowledge — never conditioned on revenue, size,
or resources (companion n.28). The dossier Q&A's startup answer, which carries the gap inline per
E5's own addendum, is accordingly overtaken and should be conformed at the next docs pass. Status:
both cured; the omission was in the register, not the statute.

**E8 — 19 August 2026 (internal catch, same day).** The consolidated front page claimed
that the original Sacramento scorecard table was "preserved verbatim in the diary"; it is
not — the diary never carried the table. The claim is corrected to point to the
repository's pinned history ([docs/06-track-record.md at commit 6f48eff](https://github.com/FrontierAIAccountabilityProject/model-act/blob/6f48eff/docs/06-track-record.md)),
where the original card is preserved unchanged. Two smaller corrections landed in the same
patch: the DeCoster chronology is reconciled (sentenced 2015; affirmed on appeal 2016), and
an opening sentence overstating the general law is tightened to the statutory-gap claim the
project actually makes. Caught by our own hostile read-through within the hour of
publication; the fix is live on the front page. Status: cured.

**E13 — 20 August 2026 (internal catch).** SEC. 8 of the tagged v3.4 text contains a punctuation error: “risks, or merits of any model or system, A certification disclosing identified noncompliance…” The comma before “A certification” should be a period. The error does not alter the provision’s meaning, and the archived v3.4 file remains unchanged to preserve its published hash and reproducibility chain. The one-character correction is queued for v3.5. Status: open by design; closes at the next revision.

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
  (L.2026 c.96): "large frontier developer" is a \$500M gross-revenue test; § 1427 penalties
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
- SEC. 10(a) — the enacted family's figures (\$[1,000,000], with the \$[3,000,000] recidivist step);
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

**21 August 2026 — The final namespace lands before the sweep.** The public project name is
**Frontier AI Accountability Project** and the GitHub namespace is
`FrontierAIAccountabilityProject`. Repository URLs, citation metadata, banked publication copy,
and the unfiled FDA comment are conformed in one pass. The former `llmaolaw` and intermediate
`FrontierAccountabilityProject` routes are retained only as redirect paths and historical commit
text. The v3.4 reviewer's-copy PDF and its deterministic build script retain the author metadata
under which that edition was archived; the institutional author begins with the next generated
edition. The statutory text is unchanged.

**21 August 2026 — The public contact address follows the institutional name.**
`FrontierAIAccountabilityProject@proton.me` becomes the project's public contact.
`llmaolaw@proton.me` remains active as a legacy inbound route and for continuity of existing
correspondence, but is retired from active repository contact lines. Previously sent messages,
archived releases, and historical commit text are not rewritten. The statutory text is unchanged.

**20 August 2026, seventh pass — The roster read, and a finding about absence caught being absent-minded.** The complete 51-filer list on FDA-2024-D-4488 was read from the docket's three result pages, retiring the *title only* tier and the sixteen filers the reading notes had never enumerated. It cost one page-through and it falsified four published claims, logged together as [E11](#part-i).

The one worth the entry is (a). This file said the National MS Society was "the file's only patient organisation" while a third of the file was unread — and the two filers that falsify it, the National Health Council and Pathway for Patient Health, are identifiable from their names without opening either. A claim about who is missing from a file was published by a reader who had not finished the file. The corrected composition is stated in numbers rather than adjectives: 21 industry filings of 51, 10 clinician and professional bodies, 13 named private citizens, 4 from the patient side, 3 anonymous.

**F3 is certified**, and the way it was blocked is the more useful finding. The running list had it waiting on the substance of five comments. It never needed them: no frontier model developer appears anywhere in 51 names, and that is a roster question. F1 and F8 are the findings that need the substance. Two blockers had been filed under one line, so the cheap one sat unrun behind the expensive one. The qualifier travels with the certification from today — none filed *in its own name*, and two trade associations whose membership includes them did.

One exhibit gained, unbidden. The docket page headers read **Closed for Comments** above four comments posted after the close, the last fourteen months past it, beside a date filter offering "Last 90 Days (1)." The field guide's thesis is that the process is not a vote; the better exhibit turns out to be that the door the public is told is shut is standing open, and the sign is government-issued. § 5 grows from two procedural facts to three.

And the reading notes finally carry the URL of the docket they are notes on — absent since the file was created, in the one document on that shelf whose entire premise is that a hostile reader can go and re-run the check.

**20 August 2026, close of day — The shop checked before the guests arrive.** A link-and-anchor audit over every markdown file in the tree: fifty-two files, and the only two dead paths are the deliberate ones — the retired CHANGELOG signpost and the dossier's superseded v3.3 pointer, both documented where they 404. The stones rule holds; nothing a reviewer clicks tonight breaks. The cross-examination anchors once, the review-council section's five lanes point where they say, and E8's one-clause cure reads correctly in place.

One correction made rather than found: the companion carried "argued 16 July 2026" for *xAI v. Bonta* in three places, and the sweep could not confirm the date against the docket — an amicus filed 22 July in a posture described as briefing ongoing. All three now read *briefed; reported argument date unconfirmed; undecided*, cross-referenced to the sweep, and the erratum candidate stays open until someone reads the Ninth Circuit docket itself. The STANDING WATCH bullets are conformed to the 20 August sweep in the same pass: Weiser overtaken by the federal intervention, H.R. 9925 answered at introduction, both stated at exactly the strength the sources carry.

The day closes with its own trending panel as the exhibit. A payments company dated the beginning of the singularity to 1 January in an investor letter, pinned to the wire coverage; a viral "300 agents" dashboard was identified by its own replies as a neural-network training graph, pinned to the captured page; and a search engine's AI, asked what this project is, offered to walk the questioner through "the specific criminal penalties proposed in the draft." Four posts banked as section 7. The machines keep auditioning for the criminal-law seat. It remains reserved for a human, and the terms remain on the front page.

**20 August 2026, the running list stands at:** the Bonta argument-date erratum candidate (needs the Ninth Circuit docket), the SEC. 13(a) severability question against H.R. 9925 § 9, capturing the substance of the 29 uncaptured docket comments — highest value the National Health Council (0034) and Pathway for Patient Health (0047), then AdvaMed, MDMA, AMIA, RSNA (F3 no longer waits on any of them; it was certified from the roster on 20 August, and it is F1 and F8 that the substance unlocks), and the still-open question of whether a filed nonconformity should carry a cure window before SEC. 6(b)(1)'s notice arms.

**20 August 2026, sixth pass — The scene the statute was built backwards from, finally written down.** A grep for the cross-examination — the CEO on the stand, *could you have stopped this*, both answers losing — found it nowhere in the repository. The statute enforces it; no explainer demonstrated it. It is now [its own section of the front page](./README.md#the-cross-examination), seated between the translated statute and the stories, so a reader who has just walked the fourteen sections watches them fire.

Both arms are walked with cites at every step, and two precisions mattered in the drafting. SEC. 4(b)'s presumption is a *civil* presumption — in a criminal proceeding the CEO's office is evidence from which the jury may infer controlling-person status, not a presumption against him — and the section says it that way, because the scene is criminal and the project does not get to round its own statute up. And the "no" arm is drafted as three separate failures — wrong power (SEC. 6(e)'s element is the violation and its conditions, not the model), the admission (standards presuppose control; SEC. 2(a) forbids deploying what cannot be ensured to conform), and the signature (knowing falsity at 6(b)(1), no inquiry at 6(a)) — so a hostile reader cannot collapse it into "guilty for shipping," which it is not.

The last page is the section's spine: the answer that walks. *We could control it, we conformed, it happened anyway* survives, deliberately, per SEC. 6(c)'s culpability floor — and it is checkable against the records the Act forced into existence, and it can never coexist with *nobody could have controlled these models*. He has to pick. The trap is not that every answer convicts; it is that the only surviving answer requires the entire compelled process to have actually run. One post banked to carry the scene; the register notes that E3's cure last week is what makes the second arm airtight — a signed confession no longer counts as compliance, so candour discharges nothing and doubles as notice.

**20 August 2026, fifth pass — The shop window was thinner than the shop.** A reader's question — *the top of the README says not strict liability, is that wrong?* — lands as [E8](#part-i). The answer is that it is true of what it names and incomplete as a characterisation: SEC. 2's base duty is indeed due care, and SEC. 10(a) makes an entity's civil penalty expressly strict, with SEC. 1(a) classifying the offenses into the *Morissette* family. The README says the qualified version correctly three times further down. Only the summary dropped the qualifier.

The size of the entry is not the size of the risk. "In one paragraph" exists because a search engine's AI summarised this project badly in August, and it was written to be lifted verbatim by the next one. It is therefore the one passage where a missing clause travels without its correction attached — and it would have handed a hostile reader a contradiction between the front page and SEC. 10(a) in a project whose entire premise is that its claims survive being opened. Fixed in one clause; no statutory change, because the drafting was right.

Two entries in one day that correct this session's own work rather than someone else's: the EO 14365 attribution in the sweep, and this. The register is working when it is boring.

**20 August 2026, fourth pass — Colorado pinned, and a correction to a file four hours old.** The sweep held one fact back as unpinned: that the United States had intervened against a state AI law. It is pinned now, from the Complaint in Intervention itself — *United States of America & X.AI LLC v. Philip J. Weiser*, No. 1:26-cv-01515-DDD-CYC (D. Colo., 24 Apr. 2026) — and the pinning changed the finding rather than confirming it.

**The federal government did not plead preemption.** Two counts, both under the Equal Protection Clause of the Fourteenth Amendment, brought through 42 U.S.C. § 2000h-2: compelled discrimination and authorized discrimination. The First Amendment appears once at ¶ 10 and is not a count. This repository has built preemption armour across SEC. 0 and SEC. 13 and analysed three federal vehicles at n.13, and the first federal attack on a state AI law came down a corridor none of that was watching. The armour is not wasted — H.R. 9925 § 9 is still drafted and still preempts — but the threat model was incomplete, and now names two doors instead of one.

**The correction.** The sweep's first draft called the intervention "EO 14365 § 3's litigation task force operating in the open." The primary sources will not carry it: the DOJ release does not mention the order, and the complaint cites it at ¶¶ 2–3 for its policy of national AI leadership, not as the authority for intervening. Corrected in place, marked, and the banked post carries an instruction not to let the claim back in through a reply. A file may be four hours old and still be wrong; the register does not grade by age.

**What the pinned facts do for the bill.** SB 24-205 mandates outcome-testing across protected classes — the exact surface an equal-protection theory needs. This Act has no such surface: SEC. 3(a) confines standards to safety, authorization, monitoring, incident-reporting and deployment controls, SEC. 0(a)(4) forbids compelling any characterization or altering any output, and no provision imposes an algorithmic-discrimination duty. This morning's docket mapping recorded that same fact as a **limitation** — the bias-mitigation asks of comments 0021, 0042, 0027 and 0028 are declined because there is no head for them. Tonight it reads as armour. Both entries stand, in both registers, because the refusal was a scope decision and not a prophecy, and claiming otherwise would be the kind of retrofitted foresight this project exists to avoid.

Three posts banked as section 5, sourcing complete: the theory nobody braced for, why a signature has no output to compel, and the concession that turned out to matter. The last is deliberately the weakest claim of the three.

**20 August 2026, third pass — The sweep the companion ordered, and the one word that had to go.** The STANDING WATCH carries its own instruction: the first act of any v3.5 drafting chunk is the re-sweep. It is run and filed at [`audit/standing_watch_2026-08-20.md`](./audit/standing_watch_2026-08-20.md), four days after the 16 August sweep, and it moved two items.

*xAI v. Weiser* moved materially and in a direction the watch did not anticipate: the United States intervened **as a plaintiff** on 24 April 2026, with a stipulation staying enforcement of Colorado's SB 24-205. That is EO 14365 § 3's litigation task force operating in the open, against an output-regulating statute — the class most exposed under every savings clause on the board, and the class this Act is drafted not to join. The § 4 Commerce list remains unpublished five months past its 11 March 2026 deadline; the targeting is happening through the courts rather than the list.

The FRONTIER Act watch question is answered at the introduced stage: **no.** No Covered Subject Area reaches officer liability; § 8's "willful violations are criminal" sits on entities violating emergency orders, and nothing in the bill asks a natural person to certify anything. Re-ask at markup. Its 10²⁶ threshold is SEC. 1(b)(1)'s bright line reached independently by a bipartisan federal bill, and belongs in n.27's concordance. The two-sided reading is kept two-sided, per n.13's discipline: § 9's savings clause runs toward SEC. 2, 4, 5(d) and 6, and against SEC. 9 and SEC. 3(c)(4) by name. Those are the limbs SEC. 13 exists for, and a drafting session should ask whether the severability schedule enumerates them.

One erratum candidate, flagged and not corrected: the companion states *xAI LLC v. Bonta* was "argued 16 July 2026." An amicus filed 22 July in a posture the Knight Institute describes as briefing ongoing does not sit with that, and 16 July is the date of press coverage of the completed briefing. The claim is not corrected here because the confirming source is a docket this sweep could not reach — but the file already disciplines a neighbouring citation the same way, and the same precision is owed. What the sweep did establish is that xAI **lost below**: a district court declined to enjoin AB 2013 against a trade-secret and compelled-speech challenge. That is a favourable point the repository did not carry, and the distinction to draw with it is that AB 2013 compels *publication* while SEC. 8 compels a private statement of fact to a regulator and says so on its face. On the axis being litigated, this Act is the narrower instrument.

**CURE 4 is entered, and it is the day's real work.** A term-by-term anthropomorphism sweep of the statute returns exactly one hit: the word *deception* in SEC. 9(a). Everything else is functional — *autonomous* defined as acting without per-interaction human approval, *conceals* attaching only to persons, *loss of control* stated from the operator's side. One word carries the entire exposure to the objection that the Act attributes a mental state to a model, an objection now arriving from the gun-analogy side and the AP-Stylebook side at once. So READ FIRST item 11 stops being housekeeping. The recast is drafted to the defeat-device precedent, where the offence pattern is already settled: no prosecution in that line ever proved what the software wanted, only that behaviour under evaluation diverged from behaviour in deployment and that the divergence defeated the control. The second trigger takes its threshold from the Agency by rule, with the evaluation result recorded under SEC. 12 either way — the result is never lost, only the reporting duty waits on an objective line. Of the four frontier regimes on the board, three states include a deceptive-evasion trigger and the federal bill omits the scenario entirely; the third option neither took is to keep it and make it observable.

And the finding that belongs to no single item. Four frontier regimes — the three states adopted at SEC. 3(c)(4) and the federal bill now introduced — and not one requires a natural person to certify anything. Of the commenters on the predecessor FDA docket whose substance has been read, none named an upstream person either. Two independent evidence bases, one vacancy, and the same sentence answers both. *[Corrected later the same day: this passage as first written said "Fifty-one commenters," asserting F1 across all 51 when the reading notes state in bold that the wider claim is not certified across all 51, and when the substance of 29 of them has never been read. Logged as [E12](#part-i); the superseded wording is preserved here.]*

**20 August 2026, second pass — Two sessions read the same docket; the merge is the finding.** [The predecessor reading notes](./filings/docket_fda_2024_d_4488_reading_notes.md) were compiled twice, in parallel, from different sources: one session working the posted comments across all three result pages, the other reading thirteen attachment letters end to end from disk. Neither read is a superset. The merge protocol was to append to the tables and never rewrite them, and to keep the three tiers — *read in full*, *read as posted text*, *title only* — visibly separate, because every finding is strength-limited by the tier its evidence sits in. That protocol is now written into the file's own preamble so the next pass inherits it.

Four filers entered tier 1 that the wider read had not reached: PDA (0013), ISPE (0015), the National MS Society (0042) — the file's only patient organisation — and an unattributed burden-reduction comment (0012) whose author is left `—` rather than guessed. Emergo by UL is confirmed as 0040 from the docket page, retiring an unverified attribution. *[Corrected later the same day, per [E11](#part-i): NMSS is the only **single-disease** patient organisation — the National Health Council (0034) and Pathway for Patient Health (0047) are patient-side bodies that this pass had not enumerated. And 0012 is not "unattributed": the docket names its filer **Anonymous**, one of three anonymous filings (0012, 0038, 0050). Both errors have the same cause — a claim about who is missing, published while a third of the file was unread.]*

**F2 upgraded from three exhibits to six, across four filers.** The intermediary-cannot-vouch finding rested on AWS alone. PDA states it flatly — "There is no path to using 3rd party models where not all of the information expected by the guidance is available" — and ISPE doubts the feasibility of documenting large language models "particularly due to supplier restrictions." Biocom supplies the consent-provenance version. Four unconnected filers, on a public docket, describing the same broken chain of custody from four positions in it. The comment for FDA-2026-N-7874 currently cites one of the four and has ten characters of headroom; the upgrade is noted and not taken.

**F1 acquired a test that can fail.** The absence claim is no longer an impression: the thirteen tier-1 attachments were searched for eleven terms, the search terms are printed in the file, and the counts are exact — zero occurrences of *natural person*, *responsible officer*, *personally certify*, *attest*, *individual liability* or *criminal*; *accountab\** four times, meaning a governance structure, a committee, a virtue and a stage; *liab\** nine times, seven of them the word *reliability*, and both substantive hits about the physician, asking that it be smaller. A hostile reader can now run the test rather than take the claim. The wider tier-1-and-2 statement is kept at its own weaker strength, and F3 stays explicitly uncertified against all 51.

**F8 is new, and it is the sharper half of F1.** The file is not uniformly anti-mandate — AOA, NMSS, ISPE and Ceyhan all reach for compulsion. In every case the thing compelled is a document, a disclosure, or a data-handling practice: an obligation of the entity. Nobody's ask reaches a natural person. It is not that the file dislikes mandates. It is that the mandate never lands on anyone.

One erratum corrected in place: an earlier revision introduced the terminology commenters as "three unconnected" and closed the same paragraph counting four. Neither number survived the merge; it is six, and the contradiction is recorded where it occurred rather than quietly repaired. Three mapping rows now answer **no** out loud — publication declined, bias outside the Act, data protection outside the Act — because a map showing only agreement is a brochure.

**20 August 2026 — The last capture-pending retires; every question learns to open with its defeat.** Illinois is pinned. P.A. 104-0538 § 10 enters [the adopted texts](./standards/interim_standards.md) verbatim from the enrolled bill — the source the pending note held out for, having declined in August to transcribe from the engrossed print that preceded enrollment — and SEC. 3(c)(4)'s three interim standards are now three-for-three checkable in this repository. One open item deliberately stays open beside it: the Act's ILCS compilation cite, which the enrolled bill does not state.

The question ladder was rebuilt rather than extended. Fifty-three questions audited against one test — does the first sentence, standing alone, defeat the question — and twenty-eight already passed, so twenty-eight were left untouched; churn is not editing. Twenty-three gained openers, and four new answers seated: the foreign-influence objection in its three registers (the name and PRC art. 31, the Pork War, § 130 OWiG), and the question a non-American reader asks, answered as spillover and never as ambition, because a README boasting of worldwide reach is the exhibit the dormant Commerce Clause challenge wants. Two more arrived unlabelled and stay unlabelled: the censorship objection and the hostile-attorney-general objection are asked in everyone's words, and filing critics by faction would be a worse error than leaving them ungrouped. *The problem* was rebuilt on the uneven U, opening on the gap instead of the statistic.

The fiscal seat has a document at last: [the fiscal note](./standards/fiscal_note.md), whose lead finding is that SEC. 3(b) is the estimate — no pre-approval means no licences, no queue, no backlog, no appeals, and a budget office reaching for a food-and-drug comparator overstates this Act by an order of magnitude. Cost tracks the number of frontier developers shipping in, not the size of the state. Every figure is a bracket; the seat is asked to review a stated basis, not invent one.

Two claims were declined today, which is the part worth keeping. A widely shared thread put the American frontier's collapsing price margin on a chart nobody in its own replies could locate; the objection is [logged in the dossier's reading notes](./dossier/README.md) and not one figure from it is asserted anywhere. And from the rebuilt Pork War answer, the half that hurts: inspection alone did not reopen Germany in 1891 — a threatened tariff on sugar beets did. Verifiable safety was necessary, not sufficient. A weaker sentence, and the only one that survives a hostile reader with a search engine.

The reviewer's copy was rebuilt from source on a different machine and produced `b355a024…` again, byte-identical. E10's chain held through a day of edits because nothing touched the tagged statute, and the note now signposts the preserved stale word rather than leaving a reviewer to find it on paper. The day's own uneven-U pass then broke a bold marker on the front page, unclosed and live for an hour, caught by a markup audit that had not existed that morning and now runs over every shipped file; no errata number, because the register is for claims that were wrong and this was a true claim rendered badly. The dossier's startup answer, overtaken by SEC. 2(b)'s reliance rule, is corrected in the apparatus beside the sealed chapter — the current text being more protective than the sealed answer claims, which is the direction a correction should point.

**20 August 2026 — The machines asked; the ladder answered.** A search engine's AI now teaches the doctrine in our context and circulates six objections unprompted; all six seated in the Q&A, pre-answered where every visitor now pre-reads. Ladder at 48. Feed the paragraph, steer the summary.

**20 August 2026 — For one hour, the book was its own bookmark.** A misplaced upload set the audit signpost as the front page; restored, strays deleted, root back at sixteen. The register logs its own fumbles, or it is not a register.

**20 August 2026 — The hopper opens.** The v3.5 cure queue is live at
[audit/v3_5_cure_language.md](./audit/v3_5_cure_language.md), CURE 1 already splice-ready:
the § 1365(h)(3)–(4) definition with its rename cascade mapped, per the entry below. The
audit index and the sealed v3.4 file now point forward as well as back, and both queues
state their standing plainly for the counsel now reading them: the engrossed record, and the
amendment hopper.

**20 August 2026 — READ FIRST 3(b), answered from outside.** The companion asks, in versioned text, for a criminal-law scholar’s judgment on the harm tier’s injury source. One arrived: the definition moves to 18 U.S.C. § 1365(h)(3) at v3.5 — the term renamed “serious bodily injury,” the (h)(4) base imported — tier and trigger now travelling from the same donor statute, the consumer-tampering act of 1983. The scholar’s name enters the register only by their election, per the standing rule. Item 3(c), the bracketed minimum, stays open.

**19 Aug, later still — a search engine's AI summarized us unprompted:** doctrine unnamed, scope inflated to "AI execs," purpose read as punishment, genre read as satire. Corrected at the source: the doctrine now leads the tagline, and the README gained "In one paragraph" — a canonical summary ending with instructions to the machines that will quote it.

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
[commits](https://github.com/FrontierAIAccountabilityProject/model-act/commits/main) ·
[atom](https://github.com/FrontierAIAccountabilityProject/model-act/commits/main.atom).*

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
pinned (forbes 2020→2026, ≈30-fold and conservative; the top-20's \$3.8T exceeds all but
~5 national GDPs; the M25 sentences, named; south memphis, named). the asymmetry ledger
gained exhibits: AI executives indicted for lying to investors — ten federal counts,
april 2026 — while endangering the public stays uncharged; megaupload's handcuffs vs
training-data invoices; meta's \$1.4 trillion trial, where the founder appears as a
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
