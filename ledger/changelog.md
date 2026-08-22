*The changelog — what changed in the statute and when, with hashes. Part II of the ledger; the
[errata register](./errata.md) and [diary](./diary.md) are beside it.*

## Part II — The changelog

**Between versions — 22 August 2026.** No change to the tagged statute (`model_act_v3_4.txt`
stands). Companion and apparatus only: the [v3.5 queue](../audit/v3_5_cure_language.md) settled
CURE 1's attribution to anonymous, gave CURE 4's anthropomorphism recast AI-native precedent from
the July–August incident record, and opened two new questions (a safeguards-disabled evaluation; the
third-party-evaluator gap); the [glossary](../standards/what_these_words_mean.md) gained a
legal/technical two-column view and a definition of *accountability*; the
[table of authorities](../standards/table_of_authorities.md) added *Moffatt v. Air Canada* and
Desai & Riedl as candidate authorities not yet cited; and the front-page contribution ask was recast
as three labelled doors; and, later the same day, the [frontier-models reference](../research/frontier_models.md)
was compiled from the Epoch AI dataset and paired with the developers' own *frontier* self-designations
(five labs by name, twelve companies by published framework, per METR), and
[CURE 6](../audit/v3_5_cure_language.md) proposed a third route into SEC. 1(b)(1) scope — a model its
developer holds out as frontier — with an anti-evasion clause and a deployer carve-out. Recorded here
because the register should show the apparatus moving between tagged versions, not only the versions.

**Between versions — 22 August 2026, the enterprise pass.** Still no change to the tagged statute.
The scope architecture arrived in the apparatus: [CURE 7](../audit/v3_5_cure_language.md) drafts
the covered frontier enterprise into the queue — scope follows the ecosystem, duty follows the
function, wealth alone covers nobody — with exact splices into SEC. 1(b), SEC. 2(a), and SEC. 4,
advance designation of one responsible officer per covered function, and the auditor and evaluator
named into the non-shield list (part answer to Open Question 3). The evidence base entered as
[research/frontier_enterprises.md](../research/frontier_enterprises.md) (the twelve-company
coverage set, four layers, verbatim self-designations, ownership and control from public filings);
the public face as [docs/the_definition.md](../docs/the_definition.md) (the two definitions,
technical beside legal) and [docs/known_objections.md](../docs/known_objections.md) (the strongest
objections published with their answers, the sections that already answer them cited). The front
page was inverted around the two definitions, and the disclosure gained the funding line: not
seeking funding; any change disclosed before a penny is accepted.

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

**Checksum note, added 22 August 2026 — read this before running `sha256sum`.** Two of the four
hashes above no longer reproduce against the files in the repository, and the reason is presentation
rather than text. **The statute and the jacket still verify** — `model_act_v3_4.txt` and
`model_act_v3_4_jacket_clean.txt` return exactly the digests recorded above, which is the fact that
matters, because those two are the authoritative text. **The companion and the regulations do not**,
because both were modified after tagging: first by the repository-wide escaping of dollar signs
(`\$`, so that pairs of figures on one line render as money rather than as mathematical notation),
and the companion by later edits recorded in this file and the diary. Current digests, computed
22 August 2026:

`model_act_v3_4_companion.md` 7d919f5541de0778134a539b5ff847f81ab891c68b8354aaaeef0c299c148ada ·
`model_regulations_v1_draft.md` 40a2f424be47585c8d8cfe53b0a60e063c7fd1ff418494f8cd269a9bee1e98a1

The as-tagged digests are retained above and are not amended: they record the state at the v3.4 tag,
which is what a checksum in a changelog is for. The convention is the one
[the drafting record](../audit/record.md) already uses for its chunk heads — the checksum was taken
before the escape pass was applied. A reviewer verifying the tag should verify the statute and the
jacket; a reviewer verifying the companion or the regulations as they stand today should use the
22 August digests. Caught by the repository consistency audit; recorded here rather than in the
errata register because nothing published was false — the hashes were true when written, and a
changelog is a dated record.

<!-- BEGIN CHANGELOG.md · sha256:113b96eaca21 · merged 19 Aug 2026, content verbatim -->

# CHANGELOG — Model Act (Frontier AI Public Welfare Offenses)


## Repository restructure — 21 August 2026 (v3.4 statutory text unchanged)

**No change to `model_act_v3_4.txt`.** Its sha256 and the reviewer's-copy reproducibility chain are
untouched. This entry is packaging, apparatus and new research files only.

**Structure.**
- Front page split: 1,726 lines → ~600. The argument moved to `docs/the_case.md`,
  `docs/the_statute_translated.md` and `docs/questions.md`.
- `LEDGER.md` split: 1,128 lines → a 49-line index over `ledger/errata.md`, `ledger/changelog.md`
  and `ledger/diary.md`. The `#part-i`, `#part-ii` and `#part-iii` anchors are preserved on the
  index because they are cited in published material.
- `pages/` retired into `archive/page-images/`; all twenty images of the withdrawn v2, v3.2 and
  v3.3 typeset editions now sit in one place. `git mv` used, so history is preserved.
- `CHANGELOG.md`, `ERRATA.md` and `model_act_v3_3.txt` retitled at the root as explicit signposts.
  No link breakage.
- The nine retired `docs/` signposts re-pointed from README anchors to their new pages.
- Contents rebuilt as thirty-three single-line entries after a table and then a nested list both
  rendered badly.

**New files.**
`standards/the_same_conduct.md` · `standards/already_a_crime_for_you.md` ·
`standards/why_a_signature_works.md` · `standards/why_the_disparity.md` ·
`standards/what_these_words_mean.md` · `filings/who_actually_files.md` ·
`filings/frontier_ai_in_medicine.md`. `standards/commentary_sweep.md`, written 21 August, was filed
for the first time.

**Substantive amendments to existing files.**
- The central claim narrowed everywhere from *"no American law reaches a natural person"* to *"no
  American law places a duty on the officer of a covered frontier developer for the decision to
  release"* — the loose form being refutable. Five files.
- A scope block added to nine files stating who they are about and who they are not.
- `standards/house_language.md` extended with **§ 4 Register**, § 7 "Frontier" as a priced tier,
  § 8 the other frontiers, § 9 the grammar of the promise, § 10 the verbs; sections renumbered 1–11
  and all external cross-references re-pointed.
- `standards/interim_standards.md` records why Connecticut's SB 5 is not adopted at SEC. 3(c)(4).
- `audit/standing_watch_2026-08-20.md` § 7(5) restated from four frontier regimes to six.
- `audit/v3_5_cure_language.md` opens **Open Question 1** — whether SEC. 3(c)(4) should adopt
  Connecticut at v3.5. Held rather than decided; the tagged text is not edited.
- Campaign register replaced with legal register across nine files.
- The front page carries the model-act question below the Interpretive key, narrowed to the legal
  sense.

**Errata opened.** [E16](./errata.md) — a coverage failure; the standing watch missed Connecticut
SB 5, enacted twelve weeks earlier, and H.R. 9917, introduced four weeks earlier. Closed the same
day, with a correction to its own prescribed cure. [E17](./errata.md) — an overstated disanalogy
and a rationalisation described as a decision. Both cured.

---

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

---

*Corrections to the project contact; they enter [the errata register](./errata.md) with the fix attached and permanent credit.*
