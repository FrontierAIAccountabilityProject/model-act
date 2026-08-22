# The map

*Every file in this repository, what it **owns**, and its status. This page exists because the
repository grew faster than its own index, and a reader — or a returning maintainer — could not
tell which file governed a question when two of them answered it.*

**The rule this page enforces: one owner per fact.** A concept is stated at full strength in
exactly one file. Every other file that touches it carries a pointer, never a restatement. Where
two files disagree, the owner governs. Drift is what happens when this rule is not written down,
and the corrections at [E25–E31](./ledger/errata.md) are what drift looked like on 22 August 2026.

**Status vocabulary.**

| Status | Meaning |
|---|---|
| **tagged** | Authoritative statutory text at a tagged version. Never edited outside a revision ([E10](./ledger/errata.md)). |
| **sealed** | Frozen with a checksum; corrections are recorded beside it, never inside it. |
| **live** | Maintained; edited as the project learns. |
| **queue** | Proposed language, not in any tagged text. |
| **append-only** | Written to, never rewritten; entries are permanent. |
| **signpost** | A retired path kept so old links still land. |

---

## The statute

| File | Owns | Status |
|---|---|---|
| [`model_act_v3_4.txt`](./model_act_v3_4.txt) | **The operative text.** SEC. 0–13. Everything else in this repository is apparatus around it. | tagged |
| [`model_act_v3_4_jacket_clean.txt`](./model_act_v3_4_jacket_clean.txt) | The same text stripped of apparatus, for a bill folder. | tagged |
| [`model_act_v3_4_companion.md`](./model_act_v3_4_companion.md) | Drafting notes n.1–n.43, the constitutional defence, and the READ FIRST open items. | tagged |
| [`model_regulations_v1_draft.md`](./model_regulations_v1_draft.md) | The draft implementing regulations. Unadopted; conformed to v3.4 by CURE 3. | live |
| [`model_act_v3_3.txt`](./model_act_v3_3.txt) | Superseded. | signpost |

## The argument — `docs/`

| File | Owns | Status |
|---|---|---|
| [`docs/the_case.md`](./docs/the_case.md) | **The argument end to end** — the problem, the precedents, the cross-examination, how a bill is handed over. | live |
| [`docs/the_definition.md`](./docs/the_definition.md) | **The two definitions of *frontier*** — the laboratories' technical one and this Act's legal one. Any file discussing what "frontier" means in law points here. | live |
| [`docs/known_objections.md`](./docs/known_objections.md) | **Every objection and its answer**, including the layered model (voluntary standards, agencies, fines, auditors, personal duties) and why one named officer. Objections are answered here and nowhere else. | live |
| [`docs/the_statute_translated.md`](./docs/the_statute_translated.md) | SEC. 0–13 in plain language beside what the text says. The statute governs where they differ. | live |
| [`docs/questions.md`](./docs/questions.md) | The doctrinal question ladder — the lawyer-and-machine register. (The plain-language register is dossier chapter 05, sealed.) | live |
| `docs/01-` … `docs/09-` | Retired paths from the pre-consolidation arrangement. | signpost |

## The evidence base — `research/`

| File | Owns | Status |
|---|---|---|
| [`research/verification_record.md`](./research/verification_record.md) | **Every source, URL, retrieval date and grade** behind the frontier-scope research — and § 4, the claims checked that **failed**. Nothing else maintains a competing source list. | live |
| [`research/frontier_enterprises.md`](./research/frontier_enterprises.md) | **The coverage set** — twelve companies across four layers, the selection test, the layer argument. The illustrative set lives here, never in the statute. | live |
| [`research/frontier_models.md`](./research/frontier_models.md) | **Compute and the threshold** — which models cross 10²⁶, the disclosure gap, the other legal definitions in force. | live |
| [`research/press_corpus_july_august_2026.md`](./research/press_corpus_july_august_2026.md) | **The incident count and the disclosure order.** Five incidents, three developers; the victim disclosed first. Every file citing incident numbers cites this one. | live |
| [`research/aisi_incident_inc_2026_07_28_01.md`](./research/aisi_incident_inc_2026_07_28_01.md) | The UK AISI incident report, read in full — the record's one independent, government-authored entry. | live |

## The record of accountability — `ledger/`

| File | Owns | Status |
|---|---|---|
| [`ledger/errata.md`](./ledger/errata.md) | **Every published claim this project got wrong**, with the fix. E1–E31. The project's only credential. | append-only |
| [`ledger/changelog.md`](./ledger/changelog.md) | **What changed in the statute and when**, with checksums. Also the "between versions" notes for apparatus movement. | append-only |
| [`ledger/diary.md`](./ledger/diary.md) | The working account, day by day, and the Recent artefact index. | append-only |
| [`LEDGER.md`](./LEDGER.md) · [`ERRATA.md`](./ERRATA.md) · [`CHANGELOG.md`](./CHANGELOG.md) | Index and historic register names; the anchors are cited in published material and still land. | signpost |

## The drafting record — `audit/`

| File | Owns | Status |
|---|---|---|
| [`audit/v3_5_cure_language.md`](./audit/v3_5_cure_language.md) | **The open queue.** CURE 1–7 and OPEN QUESTIONS 1–3, each with an exact ANCHOR into v3.4 and its NEW TEXT. **CURE 6** owns the self-designation route; **CURE 7** owns the covered frontier enterprise and the function-matched officer. This is where a reviewer's finding becomes drafted language. | queue |
| [`audit/v3_4_cure_language.md`](./audit/v3_4_cure_language.md) | The fifteen cures that landed verbatim at v3.4 — the redline behind the current statute. | sealed |
| [`audit/record.md`](./audit/record.md) | The frozen drafting record, chunks 1–8, including [the hostile brief](./audit/record.md#chunk-7). | sealed |
| [`audit/standing_watch_2026-08-20.md`](./audit/standing_watch_2026-08-20.md) | The periodic re-sweep of live bills, litigation and federal vehicles — including what each sweep missed. | live |
| `audit/chunk1-8`, `audit/field_notes_for_assembly.md` | Components of the record, reached through it. | sealed |

## Reference and the research behind the claim — `standards/`

| File | Owns | Status |
|---|---|---|
| [`standards/what_these_words_mean.md`](./standards/what_these_words_mean.md) | **The vocabulary** — what a model, an agent, a frontier model literally are; *mens rea*; the legal/technical two-column view. | live |
| [`standards/frontier_bill_census.md`](./standards/frontier_bill_census.md) | **Every frontier AI bill in America**, read one at a time, with a tally that never exceeds the rows read. | live |
| [`standards/interim_standards.md`](./standards/interim_standards.md) | **The enacted standards SEC. 3(c)(4) freezes**, pinned verbatim, and why Connecticut is not among them. | live |
| [`standards/table_of_authorities.md`](./standards/table_of_authorities.md) | Every authority the statute and companion cite, with the proposition it is cited for. Scope limited to those two documents by its own rule. | live |
| [`standards/bracketed_matter.md`](./standards/bracketed_matter.md) | **Every bracketed choice** an adopting legislature must fill in, with what the enacted family chose. | live |
| [`standards/for_legislators.md`](./standards/for_legislators.md) | The sponsor's file: the four things checked so a legislative office need not. | live |
| [`standards/house_language.md`](./standards/house_language.md) | **The drafting rule** — how this project describes frontier AI and the people who ship it. | live |
| [`standards/why_a_signature_works.md`](./standards/why_a_signature_works.md) | The signature evidence — FDA 1572, Sarbanes-Oxley, and the accounting-officer precedent. | live |
| [`standards/the_same_conduct.md`](./standards/the_same_conduct.md) | The five prosecutions, with counts, announced maxima and sentences imposed. | live |
| [`standards/already_a_crime_for_you.md`](./standards/already_a_crime_for_you.md) | The statutory text behind "already a crime for an ordinary person." | live |
| [`standards/comparative_officer_liability.md`](./standards/comparative_officer_liability.md) | The comparative answer: s. 37 HSWA, PRC art. 31, § 130 OWiG, FSMA. | live |
| [`standards/why_the_disparity.md`](./standards/why_the_disparity.md) | Twelve explanations for the accountability gap, argued in their strongest form. | live |
| [`standards/frontier_self_reporting_note.md`](./standards/frontier_self_reporting_note.md) | What the laboratories already publish, and where an attestation would sit. | live |
| [`standards/commentary_sweep.md`](./standards/commentary_sweep.md) | What the existing commentary does and does not name. | live |
| [`standards/who_has_to_tell_you.md`](./standards/who_has_to_tell_you.md) | ⚠ **Hypothesis, graded as one** — the disclosure duty runs to the intruded-upon party. Not a finding. | live |
| [`standards/fiscal_note.md`](./standards/fiscal_note.md) | What the Act costs an adopting state; startup kept apart from steady state. | live |

## The evidence file — `dossier/`

| File | Owns | Status |
|---|---|---|
| [`dossier/README.md`](./dossier/README.md) | **The frozen August 2026 evidence record**, seven chapters concatenated with checksums: the power map, the incident timeline, the congressional record, wealth and control, the plain-language Q&A, the open letters. **Corrections live in its preamble, never inside the chapters.** For current positions, see `docs/`. | sealed |
| `dossier/00_`–`06_` | The original chapter paths. | signpost |

## Filings — `filings/`

| File | Owns | Status |
|---|---|---|
| [`filings/README.md`](./filings/README.md) | What has been filed, where, on what deadline. | live |
| [`filings/fda_2026_n_7874_comment.md`](./filings/fda_2026_n_7874_comment.md) | **Draft, not yet filed** — published as a draft so it can be criticised before it is sent. | live |
| [`filings/how_to_file_a_federal_comment.md`](./filings/how_to_file_a_federal_comment.md) | The field guide to regulations.gov. | live |
| [`filings/docket_fda_2024_d_4488_reading_notes.md`](./filings/docket_fda_2024_d_4488_reading_notes.md) · [`who_actually_files.md`](./filings/who_actually_files.md) · [`frontier_ai_in_medicine.md`](./filings/frontier_ai_in_medicine.md) · [`banked_threads.md`](./filings/banked_threads.md) | The docket research behind the filings. | live |

---

## Where to go for a question

| The question | The file that owns it |
|---|---|
| What does the Act actually say? | [the statute](./model_act_v3_4.txt) — nothing else is operative |
| What does "frontier" mean here? | [the definition](./docs/the_definition.md) |
| Which companies, and why those? | [the frontier enterprises](./research/frontier_enterprises.md) |
| Where did that quotation come from? | [the verification record](./research/verification_record.md) |
| How many incidents, and who disclosed? | [the press corpus](./research/press_corpus_july_august_2026.md) § 7 |
| What's the answer to *[objection]*? | [known objections](./docs/known_objections.md) |
| What is proposed but not yet law? | [the v3.5 queue](./audit/v3_5_cure_language.md) |
| What did the project get wrong? | [the errata register](./ledger/errata.md) |
| What changed, and when? | [the changelog](./ledger/changelog.md) |
| What should a reviewer read? | [the council section](./README.md#for-the-review-council) |

---

*Maintenance rule. A new file joins this map in the same commit that creates it, with its owned
concept named. A file that restates a fact owned elsewhere cites the owner instead — the discipline
[E29](./ledger/errata.md) exists to enforce. If this map and the repository disagree, the map is
wrong and the correction is an erratum like any other.*
