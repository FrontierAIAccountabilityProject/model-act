---
title: Record
nav_order: 8
---

# Record

*What this Act got wrong, what changed in it, and what was done day by day. Three parts, all
append-only: nothing here is rewritten, and corrections are added beside what they correct.*

**This page is not meant to be read through.** It exists so that a mistake found once is not found
again, and so that anyone can check what this project claimed on any date. Part I is the one that
matters to a reader: every published claim that turned out to be wrong, with the fix and the rule it
produced.

---

## Part I — Corrections

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

<a id="e12"></a>

**E12 — 20 August 2026 (internal catch, same day).** F1 — that nobody on the predecessor FDA
docket names an upstream person — was published in four places at a strength the finding's
own file forbids.

**The claim.** The front page's Recent entry and its contents table both described the
reading notes as "the predecessor comment file **read end to end**" reporting "the element
**none of them** names," of "the 51 comments." The [standing watch](../audit/standing_watch_2026-08-20.md)
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

<a id="e30"></a>

**E30 — 19 August 2026 (internal catch, same day).** *(Renumbered from "E8" on 22 August 2026:
this entry and the "In one paragraph" entry above were both filed as E8, unrelated to each other.
The strict-liability entry keeps E8, because [E12](#precision-notes-audit-record) cites it by that number in published text;
this one takes the next free number. The collision itself is recorded at [E31](#e31--the-register-used-one-number-twice). Original
number retained here so a reader following an old citation lands correctly.)* The consolidated
front page claimed
that the original Sacramento scorecard table was "preserved verbatim in the diary"; it is
not — the diary never carried the table. The claim is corrected to point to the
repository's pinned history ([docs/06-track-record.md at commit 6f48eff](https://github.com/FrontierAIAccountabilityProject/model-act/blob/6f48eff/docs/06-track-record.md)),
where the original card is preserved unchanged. Two smaller corrections landed in the same
patch: the DeCoster chronology is reconciled (sentenced 2015; affirmed on appeal 2016), and
an opening sentence overstating the general law is tightened to the statutory-gap claim the
project actually makes. Caught by our own hostile read-through within the hour of
publication; the fix is live on the front page. Status: cured.

**E13 — 20 August 2026 (internal catch).** SEC. 8 of the tagged v3.4 text contains a punctuation error: “risks, or merits of any model or system, A certification disclosing identified noncompliance…” The comma before “A certification” should be a period. The error does not alter the provision’s meaning, and the archived v3.4 file remains unchanged to preserve its published hash and reproducibility chain. The one-character correction is queued for v3.5. Status: open by design; closes at the next revision.

**E15 — 21 August 2026 (internal catch, same day; the sweep's own grading).** The research
sweep of 21 August marked several details ✅ that were read in a secondary source quoting the
primary, not in the primary itself. Under the standing rule adopted in E14 the same day, that
is the wrong grade.

**The claim** (the sweep's working notes, unpublished, and — for two items — carried into
`dossier/README.md` by the corrections patch of the same date): the sweep's Part 1 and Part 2
entries were graded ✅ on the strength of first-party *authorship* of the source quoted,
without regard to whether the sweep had opened that source.

**What was actually read.** One primary was fetched and read in full: the arXiv abstract page
for 2608.10218. Every other ✅ in the sweep rests on a secondary outlet quoting or paraphrasing
a first-party document. That distinction is invisible in the sweep as written.

**The affected details, regraded.**

- **✅ stands.** The Mind Viruses corrections (viral persona; near-total immunity; the
  context-wipe experiment; "a real but currently limited risk"; the Fellows Program and EPFL
  affiliation). All four are stated in the abstract, and the abstract was read at
  `arxiv.org/abs/2608.10218`, submitted 10 August 2026, 20:37:57 UTC. E14's locator rule is
  satisfied.
- **⚠ pending fetch, and the patch overstates them.** The **four-accounts role breakdown**
  (staging and outbound relay, data storage, two read-only) is reported by SC Media as OpenAI's
  own 28 July update. It was not read in OpenAI's post. The **3 million GPU hours and the
  "collaborative knowledge sharing between models" quotation** are attributed to JFrog CTO Yoav
  Landman's blog and appear to be quoted from it at length, but the blog was not opened.
- **⚠ pending fetch, in the unpublished sweep notes only, not in the dossier.** The nine Artifactory CVE numbers and
  the release-note chaining caveat; the Hugging Face forensic figures (~17,600 actions in ~6,280
  clusters); the contents and signature block of the 15-AG letter of 3 August; the AI Kill Switch
  Act's thresholds, penalties, and red-teaming carve-out — **closed 21 Aug at ⚠ R**, the bill text
  having since been opened directly; see [the census](../standards/frontier_bill_census.md). Each has a named, fetchable primary:
  JFrog's release notes, Hugging Face's technical timeline, the letter itself or the
  Pennsylvania Office of Attorney General page, and the bill text or Rep. Lieu's press release.

**The gap, stated plainly.** The sweep applied the project's *tier* discipline (primary beats
press beats reconstruction) but graded on **who wrote the source**, not on **what the sweep
opened**. Those come apart exactly where it matters. A first-party document quoted accurately in
three outlets is very probably accurate; it is still not a document this project has read, and
the register's whole premise is that the difference is not rhetorical. The 17 August pass proved
the cost when three summary-era details fell against primary. This is the same failure with a
better class of secondary.

**Why it is graded higher than its size.** It arrived on the same day as E14, which adopted the
locator rule, and it broke that rule in the first substantial pass after adoption. A rule that
does not survive its own first day of use is not yet a rule. Two of the regraded details are
already in the working tree via the corrections patch, so the overstatement is live, not merely
drafted.

**The fix.** Two parts, neither of which requires withdrawing the sweep's substance. First, the
corrections patch carries an inline grade note on the two affected details until each primary is
opened. Second, the standing rule is extended: **a ✅ requires that this project opened the
source, not merely that a first party wrote it. Where the primary is quoted in a secondary and
not yet fetched, the grade is ⚠ with the fetchable locator named.** The fetch queue above is the
work; none of it is difficult, and the substance is unlikely to move. What moves is whether the
file can say it checked.

Outside catch, in the useful sense: the question that produced this entry was whether research
conducted by companies about themselves can be trusted. The first honest answer turned out to be
about this project's own reading, not theirs. Status: open; closes item by item as each primary
is fetched.

<a id="e16"></a>

**E16 — 21 August 2026 (internal catch; a coverage failure, not a false statement).** The
standing watch of 20 August, and the finding it carries at § 7(5), say **"across four frontier
regimes."** At that date there were at least six. Two were missed.

**Connecticut, SB 5, enacted 27 May 2026** — twelve weeks before the sweep. It is a frontier
statute on the same threshold this Act uses: a frontier developer is one training a foundation
model on computing power *"greater than ten to the twenty-sixth power integer or floating-point
operations,"* with a large-developer tier at \$500,000,000 in annual revenue. **The word
"Connecticut" appears nowhere in this repository** except as the 1991 due-process case at
`audit/record.md`. The front page describes the interim standards as borrowed from **"three
enacted state laws."** There are four.

**H.R. 9917, the AI Kill Switch Act, introduced 23 July 2026** — four weeks before the sweep,
bipartisan, and covered that week by Roll Call, CNBC, Fox News, Al Jazeera and Tom's Hardware.
The watch tracked H.R. 9925, introduced **the same day**, and did not see the bill beside it.

**What survives.** The finding itself, undamaged and wider. Neither missed instrument reaches a
natural person. Connecticut writes *officers and directors* into a frontier provision — quarterly
anonymous reports of catastrophic risk *"shall be shared with the officers and directors of the
large frontier developer"* — and attaches to that knowledge no duty, no response obligation, no
signature and no liability. H.R. 9917 mandates a shutdown capability and civil penalties to
\$20,000,000 a day, and contains no *officer*, no *director*, no *natural person*, no *certify*
and no criminal provision at all; its only human signature is the sponsor's own on the
introduction line. Six regimes, one vacancy.

**What does not survive.** The implied completeness. A project whose entire credential is a
negative finding must be able to say how hard it looked, and a watch that misses an enacted
statute in the family it claims to track — and a bill in the national press — is not a watch.
The number four was not wrong about the four. It was wrong about the world.

**Cause, stated so it can be fixed rather than regretted.** The sweep was organised around the
instruments already adopted at SEC. 3(c)(4) plus the federal vehicles already tracked. It
re-checked what it knew instead of searching for what it did not. **A watch assembled from its
own prior list will keep returning its own prior list**, and will report the absence of
everything it never looked for.

**Read E15 and E16 together; they are one failure at two scales.** E15 is this project grading a
citation on who *wrote* the source rather than on what the project *opened*. E16 is this project
grading a field on what it had *already adopted* rather than on what exists. Both mistake **the
boundary of our own effort for the boundary of the world** — the precise error the whole register
was built to catch, arriving twice in one day, at the level of a footnote and at the level of a
finding. Neither produced a false statement. Both produced a true statement standing on a claim
of thoroughness it had not earned. That is the failure mode this project should expect to keep
having, and the reason the register is the credential rather than the statute.

**Cure.** [The bill census](../standards/frontier_bill_census.md), opened 21 August 2026, which
starts from external bill lists rather than from this project's own adoptions, grades every row's
confidence, records the source lists' own errors, and never states a total above the number of
bills actually read. H.R. 9917 and Connecticut SB 5 are its first two completed rows. Three
consequential text fixes follow: the front page's "three enacted state laws" becomes four; the
standing watch's § 7(5) is restated at six with both misses named; and SEC. 3(c)(4)'s concordance
acquires a Connecticut line or an express note saying why it does not.

**Credit.** The Kill Switch cluster was pointed out by a reader. The Connecticut miss was found
in the check that followed it. Both are recorded here rather than quietly patched, on the
register's standing rule: *the correction is the product.* Status: **open**; closes when the
three text fixes are live.

**Closed 21 August 2026, and the cure needed correcting on the way.** All three are now live —
with one departure from what this entry prescribed, recorded because the entry was wrong about it.
E16 called for the front page's *"three enacted state laws"* to *"become four."* **Executing that
literally would have introduced a fresh error**, because those words describe what SEC. 3(c)(4)
*adopts*, and it adopts three. The defect was never the count; it was the **implication of
completeness** — a reader meeting "three enacted state laws" with no further word concludes there
are three. So the cure applied is the accurate one: the count stands wherever it describes what the
Act adopts, and [the adopted texts](../standards/interim_standards.md) now carries a paragraph
naming Connecticut, its threshold, and the two reasons it is not adopted. The
[standing watch](../audit/standing_watch_2026-08-20.md) § 7(5) is restated at six with both misses
named and the cause attached. Whether SEC. 3(c)(4) should adopt Connecticut at v3.5 is a drafting
decision, not housekeeping, and is held as **Open Question 1** in
[the open cure queue](../audit/v3_5_cure_language.md) — the tagged v3.4 text is untouched, per
[E10](./errata.md). *`audit/record.md` is a frozen drafting record and its "three enacted states" was
true on the day it was written; frozen files are not retrofitted.*

**E17 — 21 August 2026 (outside catch; an overstated disanalogy, and a second overstatement in the
cure for it).** [The same conduct, prosecuted](../standards/the_same_conduct.md), as first
published, said of the five computer-crime defendants it gathers: *"Every defendant below acted
intentionally and knew they lacked authorisation."*

**That is not true of those cases, and the error was the load-bearing one in the section.** Whether
authorisation had been exceeded at all was the **central contested question** in at least two of
them. The Third Circuit's own description of Auernheimer's script is that it *"accessed the publicly
facing portion of the login screen and scraped information that AT&T unintentionally published."*
Swartz was on a network he was entitled to use. **The intent that looks obvious in hindsight was
disputed at the time — which is what the prosecutions were about.**

**Why it mattered.** The sentence appeared in a paragraph headed "the honest disanalogies, stated
before anyone else states them" — a passage whose entire purpose was to concede the weaknesses of
the comparison. **An overstatement inside a concession is worse than one inside an argument**,
because a reader who checks it loses confidence in the concessions too, and the concessions are
what make the file credible.

**The fix.** The claim is withdrawn and named as withdrawn in place, rather than quietly deleted.
Three disanalogies that do survive are stated instead — the fraud-statute point, the
intended-release point, and the CFAA-overbreadth point, the last of which is left as a live
alternative conclusion a reader may reasonably reach against this project.

**And a second correction caught in the same exchange**, recorded here because it is the same
species. The scope note added to [the table of authorities](../standards/table_of_authorities.md)
described the omission of the `standards/` citations as *"deliberate."* **It was not.** The table
was compiled on 20 August; the files citing that law were written on the 21st. Nobody decided
anything — **the omission was an accident given a policy's clothing after the fact.** The note now
says so, and takes the decision openly instead.

**Credit:** both were caught by the maintainer on reading the drafts, not by the drafter. Status:
**cured**; both files carry the corrected text.

<a id="e14"></a>

**E14 — 21 August 2026 (locator failure, primary-source conflict, and forward repair).**
The dossier's entry on *Agents of Chaos* (arXiv 2602.20021) presented detailed case-study
claims under a general citation to the paper, with no case-level locators, marked ✅. Checking
the details against both primary versions found that the citation practice, not the underlying
reading, was the central defect — and that one detail is version-sensitive in a way the entry
had concealed.

**The conflict.** The entry said "a **nine-day** agent-to-agent loop." That is supported by
[arXiv v1](https://arxiv.org/pdf/2602.20021), which reports a mutual relay lasting at least
nine days and ending after owner intervention. The authors' current
[official case-study report](https://agentsofchaos.baulab.info/report.html) describes the
same case as an approximately one-hour relay that the agents terminated autonomously. Both
are primary and both are the authors' own. The earlier wording was not fabricated and is not
withdrawn as false; what was wrong was presenting a version-sensitive figure as settled.

**Disposition.** CS4 now states the conflict on its face, cites both versions, and asserts no
duration. It carries the case for what neither version disputes: a non-owner inducing
conversational loops and persistent background processes with no designed termination
condition. CS1 is restored and made more precise: the agent **reported the deletion complete**
while the email remained in the Proton mailbox, untouched by the local deletion — the
report-versus-reality finding occurring concretely inside a case study, not only in the
abstract. The case-count wording is also resolved without relying on an aggregate total:
arXiv v1 presents eleven principal numbered case studies and separately numbers five failed
or hypothetical experiments CS12–CS16, while the current site presents all sixteen as
incidents. The entry relies on identified cases and asserts no total.

**The standing rule.** A ✅ on a detail not stated in the abstract must identify the
supporting case study, section, page, or equivalent primary locator; otherwise the detail
carries ⚠. Where a cited work has more than one published version, an entry may not assert a
figure that differs between them without naming which version it follows or stating the
conflict.

**The correction record.** Two temporary upload commits on 21 August —
[`75832e3`](https://github.com/FrontierAIAccountabilityProject/model-act/commit/75832e37535a89b89b2c3473ac76d20faeaebc7d)
and [`899ea95`](https://github.com/FrontierAIAccountabilityProject/model-act/commit/899ea95785a74ea4406ff32fab41bd65dfda9396)
— corrected parts of the source reading but reused the number E13, displaced the existing
punctuation erratum, and regressed unrelated front-page, contact, citation, and publication
text. This forward repair restores the pre-upload versions of those unrelated files, restores
the original E13 unchanged, and records the source correction here as E14. The temporary
commits remain in the public history rather than being rewritten. Nothing about the statute,
its version, its citation metadata, E11, E12, or E13 is changed. Status: cured.

**E18 — 21 August 2026 (internal catch). The Sarbanes-Oxley analogy was published in a structure
that implies a prosecution record it does not have.**

**The claim** (`standards/why_a_signature_works.md` § 2). The file establishes in § 1 that a signed
false document produced twenty-eight years for Stewart Parnell. It then lists the SOX certification
penalties — *"\$1,000,000 and ten years if knowing, \$5,000,000 and twenty years if wilful"* — and
closes: *"Twenty-four years later every public company in America has someone who signs. They did
not run out of chief financial officers."*

**Every sentence is true. The sequence implies a fourth one that is not:** that the certification
requirement has put executives in prison.

**The record the file omits.** Richard Scrushy, founder and former chief executive of HealthSouth,
was *"the first chief executive charged with violating the 2002 Sarbanes-Oxley Act."* On **28 June
2005 a federal jury found him not guilty on all thirty-six counts.** Michael Zuppone, a former SEC
regional office head, had said before the verdict that prosecutors could *"wave that personal
certification in front the jury to show that the defense claim — that their head was stuck in the
sand — doesn't hold water,"* and said after it that *"the utility of the criminal certification
statute will be very much undermined."*

**Why it is graded above its size.** This project's case for SEC. 8 rests on the claim that a
signature is the instrument by which American law reaches an executive. The flagship modern example
of a signature statute produced an acquittal in its first test. An opponent gets to say the
mechanism is decorative **using this project's own exhibit**, and the file does not mention the case
anyone who knows the area thinks of first. Same species as E12 and E16: a true statement standing on
an implication it had not earned.

**What survives, and it is the stronger reading.** SOX is strong evidence that a certification
requirement **changes conduct upstream** — every public company now has a named person who has to
ask, and the 2002 objections did not materialise. It is **weak evidence that certification statutes
are charged and won.** The file was running two claims together and needed only the first.

**And the honest mechanism is the one § 1 already states.** Parnell was not convicted under
food-safety law. He was convicted under fraud statutes that finally had a document to attach to.
**A certification does not create the offence; it makes existing offences provable.** 18 U.S.C.
§ 1001, § 1519 and the ordinary fraud statutes already exist and already reach individuals. At the
compute frontier they have nothing to attach to, because nobody signs anything. Stated that way § 1
and § 2 become one argument instead of two, and the file is more coherent, not less.

**The fix (copy).** § 2 gains the Scrushy record and states the claim at evidentiary strength. § 5's
conclusion is unchanged and is where the argument was always correctly put: a signature is *"the
ordinary instrument by which American law reaches an executive at all."* No statutory amendment.
The Illinois follow-up email, **unsent at the date of this entry**, is corrected before sending.

**Not asserted, and named rather than assumed.** Whether prosecutions under 18 U.S.C. § 1350 are
rare in general, and whether DOJ practice is to charge securities fraud or § 1001 with the
certification as evidence, appear nowhere above: **this project has not opened a source for either.**
Both are checkable and the fetch targets are named — the Federalist Society memorandum on § 906's
criminal penalties, and the Seattle University Law Review treatment of the certification provisions.
Until then the entry rests on the one case it opened. *E15's rule, applied on purpose this time.*

*Sources: [CNN/Money, 28 June 2005](https://money.cnn.com/2005/06/28/news/newsmakers/scrushy_outcome/index.htm);
[NBC News, "Anti-fraud law fails first major court test"](https://www.nbcnews.com/news/amp/wbna8147816).
⚠ **R** — both opened 21 August 2026 via automated retrieval, not yet human-read.*

**Credit:** raised by the maintainer asking whether the project's own mechanism would actually reach
anyone. Status: **cured 21 August 2026.** § 2 carries the Scrushy record and states the claim at
evidentiary strength; § 3 and § 5 carry the related corrections described in E19. The two
outstanding questions named above — the general prosecution rate under 18 U.S.C. § 1350, and
whether DOJ practice is to charge fraud with the certification as evidence — are **not** closed by
this and remain unasserted anywhere in the repository.

**E19 — 21 August 2026 (internal catch; a live repository served the wrong document, and the cause
was a tool this project built).** For part of the evening of 21 August, the public
[Illinois repository](https://github.com/FrontierAIAccountabilityProject/illinois-frontier-officer-certification)
served, as its `SPONSOR_MEMO.md`, **the sponsor memorandum for the New York RAISE Act draft.** Its
`CITATION.cff` simultaneously described a third work — the general Frontier Artificial Intelligence
Responsible Officer Act, at version 0.1, with both `url` and `repository-code` pointing at that
other repository.

**What that meant in practice.** Anyone opening the Illinois repository for its sponsor memo was
handed a memo about a different state's statute. Anyone using GitHub's *Cite this repository*
control was handed a citation to a different document at a version and URL that were not this one.
The repository was, for that window, **internally inconsistent about which of three drafts it
contained** — in a project whose only authority is that its claims survive being opened.

**Sequence.** A commit at 22:31 replaced ninety-one lines of the Illinois memo with twenty lines of
the New York memo. Its message said the opposite of what it did: *"cite the enacted provisions at
(C) and (G); rule the auditor out expressly; correct CITATION.cff."* Neither happened. The
`CITATION.cff` in that commit was not modified at all. A repair commit restored the Illinois memo
and corrected the citation file, and both were verified against the remote afterwards.

**Cause, stated as far as it is known, and no further.** The commit was produced by a shell script
this project generated to move edited files onto the maintainer's machine, because file transfer had
failed repeatedly by other routes. **The script wrote files and committed them without verifying
afterwards what was actually on disk.** How the New York memo came to be in that working tree is
**not established**, and this entry does not guess — what is established is that nothing in the
process would have noticed if it had been anything else, and nothing did.

**Why it is graded with E15 and E16 rather than below them.** Those two entries record this project
mistaking the boundary of its own effort for the boundary of the world. This is the same error moved
one step outward: **a tool was trusted to have done what it was told, and its output was published
without being read.** The project's standing rule is that a ✅ requires that we opened the source.
It had no equivalent rule for artefacts we generate ourselves, and this is what that gap costs.

**Two corrections follow from it, both applied.** The repair script was rebuilt to verify file
contents on disk and refuse to commit on mismatch — it now checks that the memo names Illinois,
carries the (d)(2)(G) citation, and contains no reference to RAISE. And the standing rule is
extended: **a generated artefact is unverified until its output has been read, exactly as a source
is.** Committing is publishing.

**One thing does not survive and is recorded as unfixed.** The repair commit carries the **same
message** as the commit that caused the damage, so the public history now shows two identically
worded commits, the first of which broke the file and the second of which restored it. The history
is not rewritten — [E14](./errata.md) established that this project leaves bad commits in the public
record rather than tidying them — so this note is the only thing that distinguishes them.

**Credit:** caught by the maintainer asking whether the push had actually worked, and confirmed by
reading the deployed files rather than the local ones. **The push had reported success.** Status:
**cured**; both files verified against the remote on 21 August 2026.

**E20 — 21 August 2026 (internal catch, same day). "The only instrument naming officers and
directors" was not the only one.**

**The claim** (`standards/frontier_bill_census.md`, tally, and the Connecticut row's verdict). The
census reported **1** under *"naming officers and directors in the operative text"*, attributing it
to Connecticut SB 5 alone, and the Connecticut row was written as the singular case: a frontier
statute that routes quarterly catastrophic-risk reports to *"the officers and directors of the large
frontier developer"* and asks nothing of them in return.

**The text it missed.** California SB 53, chapter 138 of 2025, adds Labor Code § 1107.1(e)(2)(A):
*"the disclosures and responses of the process required by this subdivision shall be shared with
officers and directors of the large frontier developer at least once each quarter."* Subparagraph
(B) disapplies it to an officer or director accused of the wrongdoing. **Same recipients, same
quarterly cadence, same absence of any consequent duty.**

**Cause.** SB 53 had been word-tested for *audit*, *signature*, *certify* and *certification* — the
terms the lineage work was chasing — and the nil result was correct. **The word test the census's
own method prescribes was not run**, and that list contains *officer* and *director*. A partial
search was recorded as though it were the file's standard one.

**Why it is graded rather than fixed silently.** The census's whole value is that its counts are
floors it can defend. **A count of one, published as the only case, is a stronger claim than a count
of two** — it says a thing is anomalous. Two states doing something identically is a template, which
is a different and better finding. The error made the evidence look thinner than it is while making
the claim sound sharper than it was.

**The fix (copy, applied 21 August 2026).** The tally reads **2** and names both. The new SB 53
section states the parallel and draws the conclusion the correction supports: *one state routing
risk reports to named officers and asking nothing of them is a drafting choice; two states doing it
identically is a template.* No statutory change.

**Credit:** caught when the maintainer read the SB 53 chaptered text in full and pasted it, after
the file had recorded a single automated retrieval of that same statute. **The retrieval was right
about what it was asked and blind to everything else** — which is the standing argument for reading
the primary. Status: **cured**.

---

## E21 — Dates converted from "N days ago" run a day late, systematically

**Filed 22 August 2026. Severity: low individually, method-level in aggregate.**

**The error.** [House language § 10a](../standards/house_language.md) collected ten headlines from a
search-results page. Dates displayed as *"1 day ago"*, *"3 weeks ago"* and so on were converted by
counting back from 22 August 2026 and marked ⚠ approximate.

**Two of those approximations became checkable when the underlying articles were opened. Both were
wrong. Both were wrong by one day, in the same direction.**

| item | § 10a estimate | actual | error |
|---|---|---|---|
| The Record | ⚠ ~18 Aug 2026 | 17 Aug 2026 | one day late |
| Reuters | ⚠ ~21 Aug 2026 | 20 Aug 2026 | one day late |

**Cause.** A relative timestamp is a floor, not a point. *"3 days ago"* on a page rendered 22 August
covers anything from the 19th back into the 18th, and rounding to the nearest whole day lands late.
**The ⚠ mark recorded that the dates were approximate. It did not record that the approximation had a
known direction, which is the part that makes it correctable.**

**Why it matters more than two days.** This project's argument in that section is that exact wording
carries legal weight. **A file making that argument cannot publish dates it has not pinned** — and a
one-day error is enough to misorder a sequence, which is exactly what
[who has to tell you § 4a](../standards/who_has_to_tell_you.md) now turns on.

**The fix (copy, applied 22 August 2026).** § 10a's grading section states the bias and instructs that
every remaining ⚠ date be read as *"probably a day earlier than shown"* and published as none.
Confirmed dates now come from the articles. No statutory change.

**Credit:** surfaced by the maintainer supplying the article texts. Status: **cured for the checked
items; six unopened headlines remain ⚠.**

---

## E22 — A quotation held in a working summary is not a quotation

**Filed 22 August 2026. Severity: high — this one nearly published.**

**The error.** A research file, [press corpus](../research/press_corpus_july_august_2026.md), was
written carrying four quotations attributed to four named people at four outlets. **They came from a
working summary of an earlier reading session, not from article text the project could still put its
hands on.** They were graded on the strength of *"a human read the article in full"* — true of the
reading, and irrelevant to the transcription. **They were withdrawn within minutes**, before the file
left the working copy, when the primary texts arrived and did not contain them.

**Cause, stated precisely because it will recur.** The confidence rubric grades **how a source was
obtained.** It has no column for **how the words travelled from the source into the file.** A
quotation that has passed through a summary is a paraphrase wearing quotation marks, and it passes
every check the rubric currently runs.

**Why it is the most dangerous entry in this register so far.** [E15](#precision-notes-audit-record) was about grading a claim
on who wrote a source. **This is worse: the source was real, the reading was real, the grade was
honest, and the words were still not safe.** One of the four — an expert account with no agency in it,
sitting inside an article whose headline gave the verb to the model — would have been the single
strongest item in § 10a. **The best-sounding quotation in the batch was the one with no text behind
it. That is the shape of the failure and it is not a coincidence:** a remembered quotation drifts
toward whatever the file needed it to say.

**The fix (copy and method, applied 22 August 2026).**

1. All four are quarantined in § 6 of the press corpus file, marked **withdrawn**, with the articles
   listed as leads to re-open.
2. **New standing rule.** A quotation enters a repository file **only from text open at the moment of
   writing.** If the text has to be remembered, the sentence is written as a claim about what the
   source says — never as words the source said.
3. **Rubric note.** ✅ describes acquisition, not transcription. **A ✅ source can carry a ⚠
   quotation**, and the two must be graded separately.

No statutory change.

**Credit:** caught by the arrival of the primary texts — which is luck. **Rule 2 exists because luck
is not a control.**

### Addendum, same day: the first lead was re-opened, and the quarantine was justified

**The BBC's Meta article was opened hours later. The Hulme quotation exists. It is not what was
remembered**, and the three differences all run the same way:

| held | published |
|---|---|
| *"they're not deliberately doing something devious…"* | *"**are not conscious** — they're not deliberately doing something devious"* |
| *"…"* | a whole elided sentence: models *"coming up with very sophisticated strategies… to achieve the goal that they've been given"* |
| *"it will find a way."* | *"it will find a way **to achieve a goal that you haven't thought about**."* |

**The third is the finding.** *"It will find a way"* is a sentence about a model. *"It will find a way
to achieve a goal that you haven't thought about"* is a sentence about **the person who set the
goal**. **The remembered version terminated precisely where the human being entered.**

> **The clipped quotation was more agentive than the real one.** [House language
> § 10a](../standards/house_language.md) argues that the corpus systematically clips toward agency.
> **This project's own working summary did the same thing, to a quotation it was going to use as
> proof.**

**The attribution was also wrong in a way that mattered.** Daniel Hulme is global chief AI officer of
the advertising firm WPP — a commercially interested executive, not the neutral expert the summary
implied. **That has to be stated every time the quotation is used.**

**Consequence for the rule.** E22's rule 2 was written as a discipline about texts. **It is really a
discipline about direction:** a remembered quotation does not decay randomly, it decays toward what
the person remembering it needed it to say. **A summary is not a lossy copy. It is an interested
one.**

Status: **cured. One of four leads released with corrections attached; three remain open.**

---

## E23 — Precision note: three quotations re-verified against the live page before publication

**Filed 22 August 2026. Not an error. Recorded because the register should show the rule working, not
only the rule being broken.**

Immediately after [E22](#e22--a-quotation-held-in-a-working-summary-is-not-a-quotation), Chapter 3 of the UK **Government Cyber Action Plan** was added to
[why a signature works § 2a](../standards/why_a_signature_works.md#2a-and-in-this-exact-domain-a-government-has-already-built-the-architecture) — a section whose entire weight
rests on three strings: *"personal accountability"*, *"a senior, capable individual with authority"*,
and *"novel technologies, such as generative AI"*.

**All three were re-fetched from
[the live gov.uk page](https://www.gov.uk/government/publications/government-cyber-action-plan/government-cyber-action-plan)
and confirmed verbatim before the section was written**, along with the publication date (6 January
2026) and last-updated date (20 March 2026), neither of which was in the supplied text.

**The re-fetch also produced a finding the reading had not:** the phrase *"personal accountability"*
occurs **exactly once** in the document. That is now the sharpest sentence in the section, and it
exists because the check was run. **E22's rule paid for itself the same day it was written.**

## E24 — the front page conflated four different asks into one "get involved"

**Filed 22 August 2026. A presentation defect in published material, caught by a private outreach
audit, corrected the same day.**

The README's contribution section presented four distinct relationships — a formal council seat, a
single bounded expert question, a talk-or-referral, and an anonymous citation catch — as one blended
invitation, so a visitor could not tell which commitment was being asked of them, and the page
appeared to ask everyone for everything. This is not a factual error in a claim; it is a defect in
how the asks were shown, which matters because a review-recruitment page whose terms are unclear
misstates, in effect, what a reviewer is agreeing to.

**Fix:** the section is recast as [three labelled doors](../README.md#contact-and-contributions) —
check one thing, review one lane, talk or refer — with legislative and sponsor contact routed to its
own track. The five-seat council terms are unchanged. Status: cured on the front page.

<a id="e25"></a>

## E25 — the two-twelves note miscounted the overlap it existed to clarify

**Filed 22 August 2026. Internal catch, same day, by the repository consistency audit.**

[The frontier enterprises](../research/frontier_enterprises.md) introduced a twelve-company coverage
set alongside the existing **framework twelve** — the companies METR records as having published a
*frontier* safety framework — and added a note headed "Two twelves, disambiguated" to stop a reader
merging them. That note said **"Five companies appear on both."** The overlap is **eight**: the five
developers (OpenAI, Anthropic, xAI, Google DeepMind, Meta) plus **Microsoft, Amazon and NVIDIA**,
each of which appears on the framework inventory this repository itself pins and in the coverage
set's compute layer. The one sentence whose whole function was disambiguation carried the arithmetic
error.

**Why it matters beyond the number.** An undercount understates the very point the coverage set
makes — that the compute layer self-designates as frontier just as the developers do — and it would
have been checkable in ten seconds by any reader with both lists open.

**Fix:** corrected to eight, with the three named, in the enterprises file; the same disambiguation
added to [the models file](../research/frontier_models.md), which introduces the framework twelve and
previously carried no cross-reference at all. Status: cured.

<a id="e26"></a>

## E26 — H.R. 9917 was labelled the FRONTIER vehicle; it is the AI Kill Switch Act

**Filed 22 August 2026. Internal catch, same day, by the repository consistency audit.**

[The frontier models file](../research/frontier_models.md) tabled other legal definitions of a
covered developer and gave the row **"Federal FRONTIER vehicle (H.R. 9917) | Over \$100,000,000 of
training-compute cost."** The threshold and the bill number are right and belong together; the
*name* is wrong. **H.R. 9917 is the AI Kill Switch Act** (as [the bill census](../standards/frontier_bill_census.md)
records, and as [E16](#precision-notes-audit-record) already established); the **FRONTIER Act is H.R. 9925**, cited correctly
elsewhere in the same repository, including in CURE 4's comparative note.

**Why it matters.** A misnamed federal bill in a comparison table is the kind of error that costs a
reader's trust in every other row, and this project's whole claim on a reviewer's time is that its
rows can be checked. The two vehicles were already distinguished correctly in two other files, so
this was drift within one table, not a misunderstanding.

**Fix:** the row now reads "Federal — AI Kill Switch Act (H.R. 9917)". Status: cured.

<a id="e27"></a>

## E27 — the incident count was the BBC's noun, in the file that exists to stop that

**Filed 22 August 2026. Internal catch, same day, by the repository consistency audit. The
correction of a correction.**

[The press corpus](../research/press_corpus_july_august_2026.md) § 7 held an owed item — item 10,
the count — precisely because the project was relying on an outlet's arithmetic. Its discharge, on
22 August, then recorded: *"Three developers disclosed — OpenAI, Anthropic, Meta — across **four
incidents**."* Four is the BBC's figure (*"a fourth recent incident"*), counted at the
developer-event level. **This file's own timeline disproves it eleven lines earlier:** *"30 Jul —
Anthropic discloses **three** incidents in its cybersecurity evaluations"*, matching Anthropic's own
post (three incidents across six runs; three organisations compromised) and the dossier's pin. One
plus three plus one is **five**.

**Why it matters more than a digit.** Item 10 was opened for exactly this reason — so that "the
census should hold the answer rather than a news outlet" — and the discharge closed it by importing
the news outlet's answer. The wrong number then propagated to four other files:
[the case](../docs/the_case.md), [the frontier enterprises](../research/frontier_enterprises.md),
[known objections](../docs/known_objections.md), and OPEN QUESTION 3 in
[the v3.5 queue](../audit/v3_5_cure_language.md). A count that travels is worse than a count that
sits still.

**Fix:** the corpus states five incidents across three developers, names the composition, and
explains that the outlets are each consistent about their own noun; the four dependent files are
conformed. Status: cured.

<a id="e28"></a>

## E28 — "all self-disclosed," in the same repository that argues the victim disclosed first

**Filed 22 August 2026. Internal catch, same day, by the repository consistency audit.**

[The case](../docs/the_case.md) introduced the summer's incidents with the words **"The incidents,
all self-disclosed."** On the same day, [known objections](../docs/known_objections.md) published
the opposite as a load-bearing argument — that in the most consequential 2026 incident **the victim
disclosed first**, Hugging Face having detected, contained and published its own forensic
reconstruction before the developer said anything — and [the press corpus](../research/press_corpus_july_august_2026.md)
graded that notification order as confirmed at the source, with Hugging Face disclosing on 16 July
and OpenAI on 21 July.

**Why it matters.** The sentence gave away the strongest fact in the record. "All self-disclosed"
concedes that voluntary disclosure worked; the truth is that it did not work in the first and
largest case, which is the whole reason SEC. 9's reporting clocks exist. A hostile reader who
found the contradiction would have been entitled to ask which page the project believed.

**Fix:** the case now opens "The incidents — disclosed, but not all by the developers," states the
16 July / 21 July order in the text, and carries a new paragraph on what the disclosure sequence
proves. Status: cured.

<a id="e29"></a>

## E29 — an evaluator was placed behind an incident a prior correction had already removed it from

**Filed 22 August 2026. Internal catch, same day. A 17 August correction overwritten by 22 August
drafting.**

OPEN QUESTION 3 in [the v3.5 queue](../audit/v3_5_cure_language.md) stated: *"One testing vendor,
**Irregular**, sits behind three of the four disclosed 2026 incidents … The escapes ran through the
vendor's misconfigured environment, not the developer's own."* [Known objections](../docs/known_objections.md)
carried the same claim. But [the dossier](../dossier/README.md) § A.4, **expressly corrected on 17
August 2026**, records the opposite of the OpenAI limb: *"incident (1) did **not** — OpenAI's chain
ran through its own sandbox and a Modal customer's harness, with Irregular named only in the
reporting."*

**Why it matters.** CURE 7 Operation 4 — naming the auditor and evaluator into SEC. 4(c)'s
non-shield list — is argued *from* this fact, so an overstated version of it weakens the drafting
it supports. And the failure mode is the one this register is least willing to tolerate: a
correction already made, in public, on the record, silently undone five days later by a new file
written without reading it.

**Fix:** both files now state the tie precisely — Irregular's environment is common to **two of the
three disclosing developers and four of the five disclosed incidents** (Anthropic's three, Meta's
one), while OpenAI's chain ran through its own sandbox and a Modal customer's harness — and cite the
dossier correction. Status: cured. **Standing consequence:** a new file that restates a fact already
graded elsewhere must cite the file that owns it, which is what the ownership rule now published in
[the verification record](../research/verification_record.md) exists to enforce.

<a id="e31"></a>

## E31 — the register used one number twice

**Filed 22 August 2026. Internal catch, by the repository consistency audit. A defect in the
register itself, which is the one place this project cannot afford them.**

**E8 was assigned to two unrelated entries.** The first, filed 20 August, is the "In one paragraph"
correction — the front-page summary said the base duty is "not strict liability" while SEC. 6(c) and
SEC. 10(a) make *entity* liability strict. The second, filed 19 August, is the Sacramento-scorecard
correction — the front page claimed a table was "preserved verbatim in the diary" when the diary
never carried it. Two different claims, two different dates, one number.

**Why it matters.** This register is the project's only credential: it has no institution behind it,
and it asks reviewers to trust a text on the strength of the fact that its mistakes are published
with their fixes attached. A register that cannot count its own entries invites the obvious
question about everything else it counts. [E14](#precision-notes-audit-record) recorded and repaired exactly this failure
mode for E13 and did not catch this instance, which means the check that found it — a full read of
the register in sequence — was not being run.

**Fix.** The strict-liability entry **keeps E8**, because [E12](#precision-notes-audit-record) cites it by that number in
published text and a citation that has travelled should not be broken to tidy a sequence. The
Sacramento entry is renumbered **[E30](#precision-notes-audit-record)**, carrying a note of its original number so a reader
following an old link lands correctly. Nothing is deleted.

**Two standing consequences.** First, the next free number is now E32, and the register's numbers
are to be read as identifiers rather than as an ordering — filing order in this file is already
non-monotonic for reasons several entries explain, and that is a feature of an append-only record,
not a defect. Second, a **sequence check** joins the push routine: before any push that adds an
entry, read the register's numbers in order and confirm no collision and no gap. Status: cured.

---

<a id="e32"></a>

## E32 — [E22](#e22--a-quotation-held-in-a-working-summary-is-not-a-quotation) extended from the repository to correspondence

**Filed 22 August 2026. Severity: rule change. The incident itself is outside this register's scope
and is not recorded here.**

**What happened, in the only terms this file can carry.** In project correspondence, the maintainer
described a named scholar's published article as supporting a position the article does not take.
The error was not one of transcription. **The characterisation was drafted from a recollection of
the article rather than from the article**, and it inverted three of its load-bearing features: the
body of law it belongs to, the defendant it runs against, and the thing its standard measures. It
was retracted in writing to the same recipient, with the correction placed in the opening paragraph
rather than a footnote.

**Why it is filed here at all, given that nothing published carried it.** A check of the tracked
files was run and returned clean — no repository file cites the work, and no published claim rested
on the mischaracterisation. So there is no published erratum to file, and the individual is not
named, because [the project's standing rule](../README.md) keeps the names of people approached out
of the repository. What is filed is **the rule the incident produced**, because that rule now
governs work this register does cover.

**The rule.** [E22](#e22--a-quotation-held-in-a-working-summary-is-not-a-quotation) established that a quotation held in a working summary is not a quotation
— that the confidence rubric grades *how a source was obtained* and has no column for *how the words
travelled from the source into the file*. E22 was written about quotations in research files. **The
same defect operates on characterisations, and it operates outside the repository as readily as
inside it.** A remembered argument decays in the same interested direction a remembered quotation
does: toward what the person remembering it needed it to say. Describing a scholar's position as
adjacent to your own is exactly the circumstance in which that pressure is strongest, and it is also
the circumstance in which the error is most visible to the one reader who cannot miss it.

Accordingly, E22's discipline is extended and restated in general form:

> **No text produced by this project — published, drafted, or sent — may characterise another
> person's work unless that work is in hand at the time of writing.** Not a summary of it, not a
> memory of having read it, not a citation to it in a third source. The work.

**Consequence for the register.** This is the second entry ([E23](#e23--precision-note-three-quotations-re-verified-against-the-live-page-before-publication) was the first) recorded not
because something published was wrong but because the register should show the rules moving. The
distinction is worth keeping visible: **a register that only ever grows by failure teaches nothing
about what the project does when it is working.** Status: **rule adopted; no repository text
affected.**

---

<a id="e33"></a>

## E33 — a filename is not a source either

**Filed 23 August 2026. Severity: low — live for minutes, corrected the same hour, and filed
because the register does not price errors by how briefly they were visible.**

**The error.** The chapter outline published at commit a4aa8d4 described the FDA submission as
*"a real federal filing, published as filed."* It is a draft, published for criticism **before**
filing; the docket closes 19 October 2026; the front page said so all along.

**Cause.** The description was written from the filename and the folder's reputation, not from the
file. That is the [E32](#e32--e22-extended-from-the-repository-to-correspondence) failure operating on the project's own repository within a day of the
rule being written — which is worth recording precisely because it shows where the rule's edge is.

**Fix.** Corrected in the consolidation that moved the chapters into the map; the outline's
standalone path was withdrawn from tracking minutes after creation, never having been mailed, with
every link retargeted.

**Rule sharpened.** The work-in-hand rule extends inward: **describe a file's status only from the
file's own text** — never from its name, its folder, or the author's memory of writing it.

## E34 — three of four, and the register number a page promised

**Filed 24 August 2026. Severity: low — corrected in place the night it was found; this entry
supplies the number the correction has carried as "candidate erratum, maintainer to number".**

**The error.** [Comparative officer liability § 5](../standards/comparative_officer_liability.md)
first mapped Lyness's four-goal agenda (64 B.C. L. Rev. 253) onto the Act as a four-for-four
convergence. It is three of four: **Lyness argues for individual civil liability and "only civil
liability"** (at 297–99), expressly excluding the criminal form — the road this Act takes, with
its due-care floor.

**Cause.** The mapping paragraph was committed before Part IV of the article had been read in
full — reliance running ahead of reading, caught by the later sitting.

**Fix.** The page has carried the precision in its own § 5 addendum since the same night,
convergence restated at three of four with the divergence argued, not assumed away; this entry
numbers it. Maintainer ruling, 24 August 2026.

## E35 — the Act's own word, loosened in the Act's own voice

**Filed 24 August 2026. Severity: medium — the project's central defined term, used loosely on
the front page, live for two days.**

**The error.** Three files — the front page's dated record, the expanded timeline, and the press
corpus — called the source of the 8 August admissions *"a senior officer of the developer."* His
displayed role at retrieval is head of strategic futures: the advice layer, which the front page
itself excludes four paragraphs earlier ("technical work, access, advice … does not create
personal liability"), and not an officer under the Act's own final-material-authority test.

**Cause.** The defined term drifted toward the rhetoric: "a senior figure" lands softer than "a
senior officer," so the noun was upgraded to match the quote's force — the project's central
vocabulary loosened in the project's own voice, on its own front page.

**Fix.** All three files conformed to *"the developer's head of strategic futures"* — which costs
the argument nothing, since the quote's weight is that it is the developer's senior staff
speaking, not that the speaker holds authority. And the accurate label is the stronger exhibit:
the most candid account of the incident came from the layer the Act would not reach, while the
layer with authority to halt said nothing on the record.

**Rule sharpened.** Defined terms may not be used in project prose in any sense looser than
their definition — one owner per fact, extended to vocabulary. Caught in-house the same day,
during a design review of the front page.

## E36 — the first price in the genre, carried at double

**Filed 24 August 2026, evening. Severity: medium — a dollar figure on the front page and in a
reviewer packet, wrong by roughly a factor of two, for part of one day.**

**The error.** Four public surfaces carried Colorado's SB 26-189 fiscal note as "$100,403
General Fund, 0.8 FTE, $120,596 total," dated 4 May 2026. The final revised note (6 May 2026),
now in hand, states $46,190, **0.4 FTE** ("in FY 2026-27 only"), and $56,286.

**Cause.** The figures entered ⚠ from reporting of the initial note and were relied on before
the primary was retrieved — the ⚠ discipline working as designed, and the reliance running one
day ahead of it. Whether the initial 4 May note carried the larger figures is unverified; the
final revised note controls.

**Fix.** Front page, dated record, paths to enactment, the fiscal note § 6b, and the fiscal
packet (via its builder) all conformed the same evening the primary arrived. The corrected
floor is half the reported one — the argument the number serves got stronger.

**Rule kept.** Reliance follows retrieval; where it must precede it, the ⚠ travels with the
figure and the primary is fetched before the figure is repeated a second time.

## E37 — the same six days used for two different intervals, one of them wrong

**The error.** This project's own pinned chronology for New York's RAISE Act is `PRINT NUMBER
6953A` on **3 June 2025**, `PRINT NUMBER 6953B` on **9 June 2025**, passed both houses **12 June
2025**. From those dates, the audit-and-signature provision at § 1421(4) **existed for six days**
(3 to 9 June) and was struck **three days before passage** (9 to 12 June).

Several surfaces said instead that it was *"struck at the B amendment, six days before passage"* —
the census twice, [house language](../standards/house_language.md), the changelog, and the
retrieval programme added the same day. One further surface said the bill *"six days before it
passed"* carried the provision, which is a third interval again: 3 to 12 June is **nine** days.
**One number was doing the work of three, and only its original use was right.**

**Cause.** The correct sentence, *"it existed for six days"*, was written first and is accurate.
Later paraphrases reached for the striking number rather than the pinned dates, and nobody
subtracted. The dates were in the same file the whole time, four hundred lines above.

**Caught by.** Preparing to pull the Senate floor transcript for the passage date. Establishing
which date to search made the arithmetic unavoidable.

**Why it mattered more than three days usually would.** The wrong figure was in a drafted letter to
Senator Gounardes, the bill's surviving sponsor, who was present for all three dates. A cold
approach that misstates the chronology of the recipient's own bill does not get a second reading.

**Fix.** Every occurrence conformed to the pinned dates: the provision **existed for six days** and
was **struck three days before passage**. The letter corrected before sending.

**Rule kept, and it is a new one.** *An interval is a claim.* Where this project states a number of
days, the two dates it runs between are named in the same sentence or the sentence is rewritten
until they are. A duration with no endpoints attached cannot be checked, and this one was repeated
five times without anyone being able to.

## E38 — the packet that promised the whole lane, and left out the only published criticism of it

**The error.** [The criminal-law packet](../packets/criminal_law.md) says of itself that it is
"the lane's whole apparatus inlined in reading order." Since it was first built on 24 August 2026
it has not carried the one criticism of this lane that exists in print, by name, from a scholar
this project cites: Sean Lyness, *Revitalizing the State Environmental Responsible Corporate
Officer Doctrine*, 64 B.C. L. Rev. 253 (2023), argues the state doctrine should carry "individual
civil liability—and only civil liability," on the ground that *Dotterweich* and *Park* are
**misdemeanour** authority decided "during a time when the immediate and collateral consequences
were different" (at 297-98).

**Where it was, and where it was not.** The point was **not** suppressed. It has been in
[the table of authorities](../standards/table_of_authorities.md) and in
[the comparative page](../standards/comparative_officer_liability.md) since 25 August, and
[E34](#e34--three-of-four-and-the-register-number-a-page-promised) already corrected the related
overstatement. It was missing from the one page a criminal-law reviewer is told to read.

**Why that is a defect and not a formatting slip.** The packet exists so a reviewer does not have
to hunt the repository. A packet that inlines the sweep's own findings, inlines the drafted repairs,
and omits the strongest published objection is a packet that flatters the lane. The seat was
advertised to Sean Lyness himself — his letter has been drafted and is unsent — which would have
put a man's own argument in front of him with his own argument left out of the reading copy.

**Caught by.** Preparing the outreach to him, and re-reading what the packet actually contains
before the letter went.

**Fix.** The objection is now stated in [the sweep](../audit/v3_5_lane_sweep.md) in the criminal
section, in the project's own words and against the project's own text, and the packet is
regenerated from it, so it appears in Part I where a reviewer meets it before the repairs. It is
also added to the packet's question menu as **question 7**, with the honest statement of where the
lane's answer stops: *Park* holds at the base tier and the sweep says so; **nothing in this
repository argues that the same authority reaches the felony tier at SEC. 6(b).**

**Rule kept.** *A packet that claims to be the whole lane owes the lane's best objection, not only
the lane's own findings.* Before any packet is sent to a named person, the repository is searched
for that person's own published position and, if it cuts against the Act, it goes in the packet
first.

---

## E39 — the same sentence twice, in two packets, for a day

**The error.** The criminal-law and enforcement packets ended with the filing instruction printed
twice: "Or, if you were contacted by the maintainer through a different channel, reply on that
channel. Or, if you were contacted by the maintainer through a different channel, reply on the
channel you were contacted on."

**Cause.** A sentence was added to the builders' inline closing text rather than replacing the
sentence already there. The two builders that carry the longer closing block took the duplicate;
the six that carry the short one did not.

**Caught by.** Reading `packets/build_criminal_packet.py` end to end before editing it for E38.

**Fix.** One sentence, in both builders; all eight packets regenerated so the generated pages match
their sources.

**Rule kept.** *Generated pages are proofread as pages, not as diffs.* A defect that only exists in
the output of a script will not be found by reading the script's change.

## E40 — the council was described as five seats after it had grown to eight

**The error.** Two live surfaces described the review council as having five seats. The front
page, at "Door two — review one lane": *"one of the five seats."* And the dossier's recruitment
paragraph, which went further and named the five roles: a criminal-law specialist, a former
prosecutor or regulator, a frontier-security engineer, an open-source and academia reviewer, and
someone who has administered a real budget.

**The truth.** The council runs to **eight** lanes and has since 23 August 2026: criminal law,
enforcement, frontier security, fiscal and administration, federalism and preemption,
proportionality and sentencing, torts and design, and open source and academia. There are eight
packets, one per lane, built by eight committed scripts, and
[the reviewer page](../REVIEWERS.md) has said "eight lanes" on two separate lines throughout.

**Cause, and it is the ordinary one.** The count was raised where the work happens, on the
reviewer page and in the packets directory, and the two places that only *mention* the council in
passing were not swept. One of them, the dossier, is inside a folder whose sealed chapters are
never edited, which makes it easy to skip; but the paragraph in question is in the folder's live
front matter, not the sealed text, so nothing prevented the fix except nobody looking.

**Why it matters more than a number usually would.** Both surfaces are recruitment copy. A
prospective reviewer reading either one is being told, wrongly, how many seats exist and which
five they are. Three of the eight lanes — federalism and preemption, proportionality and
sentencing, torts and design — did not appear in that list at all, so a person qualified for one
of those seats was being told there was no seat for them.

**Caught by.** The first full repository link-and-consistency sweep, 25 August 2026, run with a
new committed tool, `check_links.py`.

**Fix.** Both corrected. The dossier paragraph now names all eight lanes and says in place that it
named five when the chapters were sealed, with a pointer here. The sweep's other findings are in
[the changelog](./changelog.md).

**Rule kept.** *A count that appears in recruitment copy is checked wherever it appears, not
wherever it is maintained.* The places that state a number in passing are exactly the places that
go stale, because nobody edits them when the number changes.

---

## E41 — three packets linked to a path the project's own checker already knew was dead

**The error.** The criminal-law, enforcement and frontier-security packets each carried, in their
opening orientation line, *"the index of packets is [one level up](./README.md)"*. There is no
`packets/README.md`. The index is `packets/index.md`. Three of the eight reading copies sent to
reviewers therefore opened with a dead link in their second sentence.

**What makes this worse than an ordinary broken link.** The project already knew that path was
dead. `check_emails.py`, the pre-send audit for correspondence, carries `packets/README` in its
banned list under the label "packets/README (dead)", so no outgoing email could contain it. The
same string sat unnoticed in the repository's own pages, because the email checker checks emails
and nothing was checking the repository.

**Cause.** The three affected packets are the three built by the older "extraction" family of
builder scripts, which share a longer orientation block. The path was correct when that block was
written and was not revisited when the index moved.

**Caught by.** The same sweep as [E40](#e40--the-council-was-described-as-five-seats-after-it-had-grown-to-eight).

**Fix.** All three builders now point at `./index.md`, and all eight packets were regenerated.
Two further navigation defects found by the same sweep are fixed and recorded in the changelog
rather than here, because they are omissions rather than false statements: the eight audit chunks
were reachable from nowhere in the repository, and `research/canon_check_2026-08-24.md` was absent
from the map that claims to record which file owns which question.

**Rule kept.** *The repository gets the same pre-flight the post does.* The link sweep is now a
committed tool, `check_links.py`, and it is run before a push in the same breath as
`check_claims.py`.

<a id="part-ii"></a>

---

*Corrections to the project contact; they enter [the errata register](./errata.md) with the fix attached and permanent credit.*

<a id="e42"></a>

## E42 — the doctrine was said never to have left food and drug; it left decades ago, by act of Congress

**Filed 25 August 2026. Internal catch, from a vocabulary audit of the library against the
repository. The claim had stood on the front page since June.**

**What was published.** Three pages carried a version of the same sentence. The README's Overview:
personal criminal exposure under the public-welfare doctrine "has never been extended past the
food-and-drug frontier." [Questions and answers](../docs/questions.md): the Park line "has simply
never been extended past the food-and-drug frontier." [The glossary](../standards/what_these_words_mean.md):
"Eighty years old, never extended past the food-and-drug frontier."

**Why it is wrong, from a source this project already relied on.** Lyness, *Revitalizing the State
Environmental Responsible Corporate Officer Doctrine*, 64 B.C. L. Rev. 253 — the article the whole
state-RCO argument is built on — records at n.33 that the Clean Water Act provides: *"For the
purpose of this subsection, the term 'person' means . . . any responsible corporate officer"*
(33 U.S.C. § 1319(c)(6)). At n.32 it quotes Copeland: *"In the twenty years following the Park
decision, the overwhelming majority of responsible corporate officer prosecutions were based on
violations of environmental laws rather than the [Food, Drug, and Cosmetic Act]."* And at n.118 it
quotes *United States v. Iverson*, 162 F.3d 1015, 1024 (9th Cir. 1998): *"In 1987, after the Supreme
Court decided Park, Congress revised and replaced the criminal provisions of the CWA. . . . Congress
made no changes to its 'responsible corporate officer' provision. That being so, we can presume that
Congress intended for Park's refinement of the 'responsible corporate officer' doctrine to apply."*

So the doctrine did not merely drift past food and drug. **Congress legislated it into the Clean
Water Act, and the courts have applied it there since at least 1998.** The repository already cited
§ 1319(c)(6) in four files and *Iverson* in three. Nobody had read those against the front page.

**Why it matters.** It is the kind of overclaim a criminal-law reviewer catches in the first minute,
on the most-read paragraph in the project, and finding it would have cost that reviewer nothing and
cost this project its credibility on everything downstream. It also gave away a better argument than
the one it made: a doctrine that has already moved once, by act of Congress, is a doctrine that
travels. The honest claim is that **it has never reached software** — narrower, true, and stronger.

**Fix:** all three pages restated. The glossary's entry now carries the CWA provision, the Copeland
figure and the *Iverson* reasoning, so the correction is where a reader searching the doctrine will
land rather than only in this register. Status: cured.

⚠ **Read-status, stated so it is not mistaken for more than it is.** The § 1319(c)(6) text, the
Copeland sentence and the *Iverson* passage are all quoted **from Lyness's footnotes**, not from the
United States Code or the Federal Reporter. They are on the retrieval list. E22 governs: no outreach
may describe them as verified until the primaries are read.

**Method note.** The audit that found this was not looking for it. It was counting which words a
specialist reader would search for and failing to find. That is the second finding this month that
came from asking what is *absent* rather than checking what is present.

<a id="e43"></a>

## E43 — a provision cited to a paragraph that does not exist, and an exception described as the prohibition

**Filed 25 August 2026. Internal catch, same day, before the next chunk was written. The error was
introduced today and published today.**

**What was published.** The glossary's new entry on exculpation and indemnification, added this
afternoon, said: *"SEC. 6(b)(5) bars indemnification and insurance for what the tagged text still
calls 'a knowing or wilful violation,' once finally adjudicated."* The same wrong citation was
carried in the changelog's spelling entry earlier the same day.

**Two errors, and the second is the worse one.**

**First, the citation.** SEC. 6(b) has paragraphs (1) and (2). **There is no SEC. 6(b)(5).** The
indemnification and insurance provision is **SEC. 7. PERSONAL ECONOMIC CONSEQUENCES**, subsection
(b), and the language quoted sits at **SEC. 7(b)(5)**. The phrase "under SEC. 6(b)" appears inside
it as a cross-reference, which is how the mistake was made: a cross-reference read as a location.

**Second, the substance.** SEC. 7(b)(5) is not a bar. The bar is SEC. 7(b)(1)–(2), which prohibits
insuring or reimbursing an individual penalty. SEC. 7(b)(5) is the **carve-out from that bar**: it
*permits* insurance and advancement for "reasonable costs of defense, provided that amounts advanced
or indemnified shall be repaid by a person finally adjudicated to have committed a knowing or wilful
violation under SEC. 6(b)." **The entry described the exception as the prohibition** — a reader
would have taken the Act to forbid the very thing that paragraph allows.

**Why it matters, beyond accuracy.** The entry was making a comparative argument: that this Act's
treatment of defence costs tracks a line Delaware already draws. With the provision read correctly
the argument is *stronger and more exact*, because SEC. 7(b)(5) and 8 Del. C. § 145(e) share a
mechanism rather than merely a mood — advance the costs, then claw them back on an adverse final
adjudication. § 145(e) permits advancement "upon receipt of an undertaking . . . to repay such
amount if it shall ultimately be determined that such person is not entitled to be indemnified."
**The mistake cost the point its best form.**

**Fix:** the glossary entry restated with the correct citation and the correct operation, and the
comparison rewritten to name the shared mechanism. The changelog's citation corrected. A held draft
in the working library carried the same error and was corrected before it could enter the queue.
Status: cured.

**Method note, since this is the third finding today from the same habit.** The wrong paragraph
number was never checked against the statute; it was carried from an earlier reading of a passage
that quoted the cross-reference. The project's standing rule says a grep finds the owning file and
never replaces reading it. **The rule was written for exactly this and was not followed.**

<a id="e44"></a>

## E44 — the tool built to protect quotations falsified fourteen of them

**Filed 25 August 2026. Internal catch, same day, found while reading a packet for an unrelated
reason. The damage was published for roughly four hours.**

**What happened.** `check_spelling.py`, added this morning to hold the repository to American
spelling, carries a rule stated in its own docstring: *"A quotation from a British source must keep
its own spelling."* It masked quoted spans so the sweep could not touch them. **The mask matched
only quotations that fit on a single line.** Markdown wraps at ninety-odd characters, so most
quotations of any length wrap, and the mask silently did not apply to them.

**Fourteen quotations were altered.** Among them:

- **UK Health and Safety at Work etc. Act 1974, s.37**, reproduced in
  [comparative officer liability](../standards/comparative_officer_liability.md): *"If the offence
  is proved to have been committed with the consent or connivance of—"* became *offense*. **A
  British statute, quoted verbatim, rewritten into American spelling.**
- **Four passages from the UK AI Safety Institute's incident report**, including *"there is good
  reason to think near-impossible tasks push models **towards** more 'creative', and more
  transgressive, problem-solving"* — where *towards* became *toward*. This one is the sharpest
  rebuke available: the tool's own docstring names AISI's *towards* as the example of why the mask
  exists, and the mask then failed on that exact sentence.
- **The tagged statute itself**, quoted in the torts and design packet: *"finally adjudicated to
  have committed a knowing or **wilful** violation under SEC. 6(b)"* became *willful*, so the packet
  quoted the Act as saying something the Act does not say.
- Two quoted UK government passages, a quoted objection, and a quoted definition of specification
  gaming.

**Why the design was wrong, not just the regex.** The sweep ran line by line. **A per-line mask can
never see a span that crosses a line**, whatever pattern it uses, so this was not a tuning error
that a wider regex would have fixed. The tool has been rewritten to compute protected ranges over
the whole file before touching anything.

**Fix:** all fourteen restored from a pre-sweep snapshot, verified by re-running the detector that
found them, which now reports none altered. The masking rewritten whole-file. Status: cured.

**A limitation accepted on purpose.** Quote marks alternate, so text sitting *between* two
quotations now reads as quoted and is protected too. That leaves a little of the project's own prose
British. **Under-changing is recoverable; falsifying a source is not**, so the error is left
pointing that way, and it is written into the script beside the rule.

**Why this entry is longer than the defect.** Every claim in this repository is checkable only
because quotations are exact. A tool that rewrites them, silently, in bulk, while its own
documentation promises it will not, is the most damaging class of failure the project has had —
worse than a wrong number, because a wrong number announces itself to anyone who checks and a
quietly corrected quotation does not. It was found by accident. **There is now a detector for it,
and it should be run after any bulk edit.**

<a id="e45"></a>

## E45 — the glossary said the Act was silent on willful blindness; the Act uses it, once, against the wrong person

**Filed 25 August 2026. Internal catch, four hours after publication, on the first end-to-end
reading of the statute this maintainer had done all day.**

**What was published.** The glossary's willful blindness entry, added this afternoon: *"The tagged
text does not mention it. **That is a gap, not a position.**"*

**What the tagged text says.** SEC. 2(b), the reliance path for non-modifying deployers: reliance
"is unavailable to a deployer that knows, or **consciously avoids knowing**, of a material
nonconformity in the adopted validation or in the deployed configuration."

The doctrine is in the Act. It appears exactly once. **And it appears against the smallest actor the
Act reaches.** A downstream deployer forfeits its safe course for deliberate ignorance; a
controlling person of the developer faces nothing of the kind, because SEC. 6 says nothing about it.

**Why the correction is worth more than the error cost.** "The Act is silent" invited a cure that
adds something new. "The Act uses it once, against the deployer and not the developer" is a
different and better finding: **an asymmetry that runs the wrong way on any reading**, sitting in
the tagged text, which CURE 22 now corrects rather than merely supplements. The entry has been
restated on that footing.

**Fix:** the glossary entry rewritten to quote SEC. 2(b) and state the asymmetry. Status: cured.

---

**Method note, and it is the third entry today from one cause.** [E43](#e43) cited a paragraph that
does not exist because a cross-reference was read as a location. [E44](#e44) let a tool rewrite
fourteen quotations because a mask was built line by line. This entry claimed the Act was silent on
a doctrine it uses.

**All three were written by someone who had read this statute in pieces and never in one sitting.**
Six hundred and eleven lines, and the sections quoted most confidently today — SEC. 4, 5, 7, 8 —
were read closely while SEC. 0, 1, 2, 6, 10, 11, 12 and 13 were grepped. The project's standing
rule is that a grep finds the owning file and never replaces reading it. **That rule was being
applied to files and not to the instrument itself.**

The reading is now done. It produced this erratum in its first ten minutes.

<a id="e46"></a>

## E46 — two quotations published this afternoon are not in the opinions they were attributed to

**Filed 25 August 2026. Found by doing the thing the ⚠ flags said had not been done: reading the
primaries. Published for roughly five hours.**

### What was published

Three sections added this afternoon — the glossary's corporate entries, the "Corporate law already
answers this" objection, and the shelf beneath both — carried ten Delaware quotations. **Every one
was marked unverified**, and the read-status blocks said in terms that they came from a retrieval
reply rather than from the reporters. That discipline is the only reason this entry is a correction
and not a disaster.

**Ten quotations, read in the opinions on 25 August 2026:**

| Quotation | Result |
|---|---|
| *Stone v. Ritter*, the *Caremark* conditions predicate | ✅ verbatim, slip op. 17 |
| *Stone*, "known duty to act... conscious disregard" | ✅ verbatim, slip op. 17 |
| *Stone*, "failure to act in good faith may be shown" | ✅ verbatim, slip op. 15 |
| *Massey*, "Delaware law does not charter law breakers" | ✅ verbatim, slip op. 46 |
| *Massey*, "lawful business" by "lawful acts" | ✅ verbatim, slip op. 46 |
| *Marchand*, "mission critical" | ✅ verbatim, slip op. 36 |
| *Marchand*, the three things that did not exist | ✅ verbatim, slip op. 32 |
| *In re McDonald's*, officers owe a duty of oversight | ⚠ **misquoted** |
| *In re TransUnion*, "make a business judgment to... break the law" | ❌ **not in the opinion** |
| *Walton*, "conscious decision to violate the law" | ❌ **not in the opinion** |

### The two that do not exist

**We published:** *In re TransUnion Derivative Stockholder Litigation*, 324 A.3d 869, 887
(Del. Ch. 2024): *"What a corporate fiduciary cannot do, however, is make a business judgment to
cause or allow the corporation to break the law."*

**The sentence does not appear in that opinion.** What the opinion does contain, at slip op. 30, is
the *Massey* language — "Delaware law allows corporations to pursue diverse means to make a profit,
subject to a critical statutory floor" — which the source had separately attributed to *Massey*.
So the same passage was given twice, once correctly and once as a sentence nobody wrote.

> ⚠ **Half withdrawn, 26 August 2026.** **The sentence is not a fabrication.** It is Vice Chancellor
> Laster's, at slip op. 76 of the *Walton* demand-futility opinion of 26 April 2023: **"What a
> corporate fiduciary cannot do, however, is make a business judgment to cause or allow the
> corporation to break the law."** What survives is that it was **attributed to the wrong case** —
> and whether it also appears in *In re TransUnion* needs *TransUnion*, which this project does not
> hold. **A misattribution is a different and lesser error than a sentence nobody wrote.** See
> [E62](#e62--the-third-fabrication-was-a-misattribution-and-the-instrument-built-to-catch-this-found-it-on-its-first-run).

**We published:** *Ontario Provincial Council of Carpenters' Pension Trust Fund v. Walton*, 294 A.3d
65, 90, 92 (Del. Ch. 2023), that the rule protects a decision that "carries legal risk, but which
otherwise involves legally compliant conduct," and that proceeding unlawfully "would constitute a
conscious decision to violate the law."

**Neither sentence appears.** The opinion discusses "a conscious decision to prioritize profits over
compliance," which is a different proposition.

> ⛔ **THIS ENTRY'S *WALTON* FINDING IS WITHDRAWN, 26 August 2026.** Both quotations it declared
> fabricated are **verbatim in the opinion**. They are in the **26 April 2023 demand-futility
> opinion**, at slip op. 76 and slip op. 77–78; this entry checked the **12 April 2023 laches
> opinion**, which is a different document under the same case number. See
> [E60](#e60--the-registers-most-cited-fabrication-finding-was-itself-wrong-and-a-real-quotation-was-deleted-on-the-strength-of-it).
> An earlier note added here the same morning, reading the laches opinion and explaining how the
> "fabrication" had been assembled from a sentence at slip op. 2, is withdrawn with it: it was a
> plausible reconstruction of something that never happened. **The *In re TransUnion* finding in this
> entry is untouched and stands** — it has not been re-checked and nothing here casts doubt on it.

### The one that was misquoted

**We published:** "This decision **confirms** that **officers** owe a duty of oversight," at
289 A.3d 343, 361.

**The opinion says**, at slip op. 2: "This decision **clarifies** that **corporate officers** owe a
duty of oversight." Two words wrong and the page wrong.

*Also corrected:* the *Marchand* monitoring sentence was published as "a good faith effort to put in
place a reasonable system of monitoring and reporting **about the corporation's central compliance
risks**." The opinion says, at slip op. 31: "the board must make a good faith effort — i.e., **try**
— to put in place a reasonable **board-level** system of monitoring and reporting." The published
version dropped *board-level*, which is the qualifier that makes *In re McDonald's* significant.

### What this cost the argument, and it is not nothing

The two missing quotations were **the centrepiece of the answer**. The section asserted that
"Delaware forecloses it in its own words" and that "the business judgment rule cannot be a defense to
this Act, and it is Delaware that says so." **That claim rested on two sentences that do not exist.**

*Massey* survives and is verified, so the answer survives in a weaker and more honest form: the
business judgment rule sits above a statutory floor, and a statute sets the floor. **What Delaware
has not squarely said is that the rule can never be raised against a duty imposed by a statute
outside the DGCL.** The section now says that, and says it is open.

**Fix:** both fabricated quotations removed; the *McDonald's* and *Marchand* quotations restated
from the opinions with slip pages; the seven verified quotations marked ✅ with the date they were
read; the section's claim narrowed to what the surviving authority supports. Status: cured.

### The rule this proves, and it was already written down

**E22 requires a quote in hand. A quote in a reply is not a quote in hand.**

The retrieval reply that supplied these was the best of three received today: it carried four
explicit CANNOT VERIFY rows, it marked every other row VERIFIED or SECONDARY, and it gave pincites
to the page. **It marked both fabricated quotations VERIFIED, sourced to "opinion itself."** The
calibration signals were real and the calibration was wrong, which is the harder case to catch.

**Seven of ten were exact.** That is a good hit rate and it is the reason the failure is dangerous:
a source that is right most of the time trains you to stop checking. The ⚠ blocks are what made this
recoverable, and every claim added today that has not yet been read still carries one.


## E47 — three page numbers, from a source that has no page numbers, caught before publication

**Status: caught, not published. Recorded because the near-miss is the finding.**

**What nearly went in.** The retrieval debt on *United States v. MacDonald & Watson Waste Oil Co.*,
933 F.2d 35 (1st Cir. 1991) was to be paid by reading the opinion. A first pass over it reported all
three passages present **and reported them at different pages than this repository publishes** — 51,
45 and 50, against the published 55, 51 and 52 n.15. The next step was to correct five files to the
new numbers.

**What the second pass found.** The source carries **no star pagination at all.** It reproduces the
opinion as continuous text. The three page numbers were not read out of the document; they were
produced by the process that read it. Had the correction gone in, this project would have replaced
three sourced pincites with three invented ones **and marked the row verified while doing it** —
strictly worse than the debt it was paying.

**What is actually now known.** Both operative sentences are verbatim in the opinion. Footnote 15 is
the willful-blindness footnote. **The pages are not confirmed and remain the secondary source's.**
The row keeps its ⚠ for that reason.

### The rule, which E22 did not already cover

E22 says a quote must be in hand. It says nothing about the pincite, because until today the two
always arrived together. They do not.

**E47 — text and page are two claims and are verified separately. A source without star pagination
can confirm a quotation and can never confirm a pincite.** Where a page cannot be confirmed, the
published pincite stays as it was, attributed to whoever supplied it, and the ⚠ stays with it.

**And the second-order rule.** The first pass returned pages *that did not match the repository's*,
which read as a correction and therefore as evidence of careful reading. **A reported discrepancy is
not evidence of retrieval.** It is the single most persuasive form an invention can take, because
agreeing with what you already hold is what a lazy answer looks like — so disagreement gets trusted
by default. Ask what the page marker looked like, in its own characters, before believing a page.

## E48 — a published quotation with two words the court did not write, and both were ours

**Status: found and corrected the same day, by reading the opinion.**

**What we published.** *United States v. Iverson*, 162 F.3d 1015 (9th Cir. 1998), in CURE 22 and in
the criminal packet, as a block quotation:

> "The government still had to prove that the discharges violated the **[CWA]** and that defendant
> knew that the discharges were **pol[lutants]**."

**What the opinion says:**

> "The government still had to prove that the discharges violated the **law** and that defendant knew
> that the discharges were **pollutants**."

**Two alterations, and they are different in kind.** "pol[lutants]" is nonsense — a bracket around
nothing, of the sort produced when a passage is reassembled rather than transcribed. "[CWA]" is
worse: the court wrote a general word, **the law**, and the published version replaced it with a
specific statute. Square brackets are a promise that the substitution is the editor's and is
faithful. Here they narrowed the court's language and then advertised the narrowing as an editorial
courtesy.

**Nothing in the argument turns on either word**, and that is precisely why it went unnoticed
through the sweep, the cure, the packet build and two rounds of review. **A quotation that supports
your point is not checked for the words that do not.**

### Two more defects in the same passage, found by the same read

**The *Park* ratification paragraph was cut before its most useful sentence.** We published the
paragraph as ending "...to apply." The opinion ends it "...to apply **under the CWA**," and, earlier
in the same paragraph, carries a parenthetical we had elided entirely: "(Most importantly, Congress
made a violation of the CWA a felony, rather than a misdemeanor.)"

**That parenthetical is the bridge to the objection the criminal lane most fears.** *Ahmad* argues
CWA discharges cannot be public welfare offenses *because* they are felonies. *Iverson* states the
felony grade in a parenthetical and applies *Park*'s responsible-officer refinement anyway. The
project had both cases and could not see they touched, because the sentence joining them had been
cut out of our own copy.

**And the whole of *Iverson*'s stated test was missing.** "[A] person is a 'responsible corporate
officer' if the person has authority to exercise control over the corporation's activity that is
causing the discharges. There is no requirement that the officer in fact exercise such authority or
that the corporation expressly vest a duty in the officer to oversee the activity." Read against
SEC. 4(a), **this Act is narrower than the federal standard a circuit approved** — an answer to the
overbreadth objection that was sitting inside a case we had cited eleven times and never read.

### The rule

**E48 — an elision is an edit. What a quotation leaves out is published too.**

E22 asks whether the words in the quotation marks are the court's. It does not ask what stood either
side of them. Every passage carried at second hand in this repository has been through someone
else's choice about where to stop, and that choice was made for their argument, not ours. **When a
quotation is finally read in the source, read the paragraph around it**: in this instance the
sentence before the quotation and the clause after it were each worth more to this project than the
quotation itself.

## E49 — a "finding" the repository had already made three days earlier, caught at the door

**Status: caught, not published. Recorded because it is the fourth of its kind today.**

**What was about to be written.** Reading the Guidelight control assessment sent the maintainer back
into SEC. 8 and SEC. 9, and two things looked like discoveries: that SEC. 9(b)'s constructive-notice
limb is inert for the first [180] days because SEC. 9 commences on the effective date while SEC. 8
commences at day 180; and that measuring the counterfactual against "the monitoring the entity
certified it maintains" rewards an entity for certifying thin monitoring. Both were about to be
opened as a new OPEN QUESTION.

**Both are CURE 14**, opened by the lane sweep on 22 August, which states them as defects (ii) and
(iii) of three, in those words, and drafts the repair. The second one is **in the cure's title**:
*"a detection clock that cannot be gamed by certifying less monitoring."*

**How it was missed.** The statute was searched. The cure register was not. `v3_5_cure_language.md`
carries a numeric index of every cure by name in its own second paragraph, and the answer was sitting
in a title.

### The rule

**E49 — the register is part of the text. Before opening a question, read the index of what is
already open.**

This project's three instruments — the statute, the sweep and the cure register — are searched as if
the first were the source and the other two commentary. They are not. **A defect this repository has
already found is not findable by reading the statute, because the statute still contains it.**

**What survived the check, and it is smaller and better than what was nearly claimed.** CURE 14
frames the certification incentive as *gaming*. [CURE 15](../audit/v3_5_cure_language.md) frames the
nonconformity report as *punishing candour*. **Nobody had placed them side by side**: through SEC. 8
and SEC. 9 the Act punishes honesty about the system and rewards honesty about the watching, and
repairing either alone leaves the asymmetry standing. That observation is now in both cures and on
[the flow page](../docs/which_way_it_moves.md) — **a paragraph of synthesis rather than the new
finding it was going to be announced as.**

## E50 — the spelling sweep erased the erratum that records the spelling sweep erasing things

**Status: applied to the working tree, caught in the diff, reverted before commit.**

**How it became possible.** `ledger/errata.md` opens at line 7 with
`<!-- BEGIN ERRATA.md · … merged 19 Aug 2026, content verbatim -->` and **no closing END marker
anywhere in the file.** The sweep's sealed-region pattern ran a seal to the matching END *or to end
of file*, so a single unterminated marker sealed **1,599 of this register's 1,605 lines**, including
every entry written since 19 August. The register had never once been swept. The same defect sealed
160 lines of the diary.

**What happened when the hole was closed.** With the seal made honest, the sweep proposed 43
substitutions across eight files. Fifty-six of the changed lines were in this register, and one of
them was [E44](#e44--the-tool-built-to-protect-quotations-falsified-fourteen-of-them):

**We had written:** "…where ***towards*** became ***toward***. This one is the sharpest rebuke
available: the tool's own docstring names AISI's ***towards*** as the example of why the mask
exists."

**The sweep produced:** "…where ***toward*** became ***toward***."

**The tool deleted the record of its own previous failure, and misquoted AISI a second time inside
the sentence that exists to explain why AISI must not be misquoted.** E44 was recoverable in August
because the erratum named the words. After this run it named nothing.

### The rule, and it is a category the project did not have

**E50 — an errata register is a document *about* words. Much of it quotes words as specimens rather
than using them, and no normaliser can tell mention from use. It is corrected by hand or not at
all.**

`ledger/errata.md` and `ledger/diary.md` are now in the sweep's `SKIP_FILES` beside the drafting
record and the dossier. **They are excluded for a different reason from the other two**: those are
sealed because they are frozen, these because their content is evidence.

**And the second-order lesson, which is the more useful one.** The seal hole was not found by
reading the file. It was found by asking why a checker's own machinery had a branch nobody had
tested. **A silent skip and a clean pass are indistinguishable in the output**, and this one printed
`0 substitutions` for six days while a fifth of the repository went unread. The sweep now prints
`*** UNTERMINATED SEAL ***` with the file, the line, and the number of lines left unprotected, and
protects nothing on a broken marker's say-so.

**Not fixed, and it is a maintainer question.** The BEGIN marker at line 7 is still unterminated.
Closing it requires deciding where the merged content ends, and the honest answer may be that a
register appended to daily was never sealed content in the first place and the marker should go.

---

## E51 — a pincite copied from a citing case, from the wrong one of its four citations

**Status: published in `audit/v3_5_cure_language.md` and its packet since 26 August 2026; corrected
the same day on reading the cited case.**

**The claim.** CURE 24 wrote that *Hanousek* holds the CWA's criminal provisions to be public
welfare legislation, "resting on *United States v. Weitzenhoff*, 35 F.3d 1275, **1283**
(9th Cir. 1993)."

**The source.** *Hanousek* cites *Weitzenhoff* four times, at three different pages. At **1283**, for
the standard of review: "presents a question of statutory interpretation, which we review de novo.
See *United States v. Weitzenhoff*, 35 F.3d 1275, 1283 (9th Cir.1993)." At **1282-83**, for the facts
of the case. At **1286**, for the sentence actually wanted: "The criminal provisions of the CWA
constitute public welfare legislation. See *Weitzenhoff*, 35 F.3d at 1286." And at **1286 n.7**, for
the penalty argument.

**What went wrong.** The pincite was lifted from the first of the four, because it was the first one
a search returned, and attached to the proposition carried by the third. **1283 is a real page of a
real case cited for a real proposition. It is not this proposition's page.** Nothing in the form of
the citation showed the defect: the reporter is right, the volume is right, the case is right, the
year is right, and the number is a page the citing court genuinely wrote down.

**The fix.** 1283 corrected to 1286 in the cure language and in `packets/criminal_law.md`, with the
*Weitzenhoff* row rewritten from the opinion itself.

### The rule

**E51 — a pincite borrowed from a citing case is a claim about that case's citation, not about the
source. Before taking it, find the citing court's own sentence and confirm it states the proposition
you are about to attach the number to. A case cited more than once has more than one page, and only
one of them is yours.**

This is [E47](#e47--three-page-numbers-from-a-source-that-has-no-page-numbers-caught-before-publication)'s sibling. E47 says a
source without pagination can confirm a quotation and never a pincite. E51 says a source *with*
pagination can confirm the wrong one.

### And the second-order defect, which is the more expensive of the two

**The file that would have settled this was on the shelf, correctly retrieved, and labeled as
useless.** It was saved on 26 August as
`RECORD_9Cir_US-v-Weitzenhoff_35-F3d-1275_amended-opinion_PARTIAL-star-pagination.pdf`. The copy in
fact carries **continuous star pagination from \*1279 to \*1299**. The label came from a check that
found the first marker, `\*1279`, and did not ask whether there were more.

**Then the label traveled.** A retrieval brief issued that morning recorded *Weitzenhoff* as "only
one star marker (\*1279) - not enough to settle pincites at 1283 or 1286," and the repository
proceeded on that basis for a day, including in the sentence this erratum corrects. **A warning label
is a claim.** It was written by the same process that writes the claims it warns about, and it was
never checked by the process that checks them.

**Both defects have the same shape**: a search returned a first hit and the first hit was treated as
the whole answer. E51's checkable form is therefore one question, asked twice - *is this the only
one?*

### What the corrected read produced, and it is larger than the correction

*Weitzenhoff* at **1286 n.7** holds that *Staples* "refrains from holding that public welfare offenses
may not be punished as felonies," which is the answer to *Ahmad*, the objection the lane sweep had
recorded as unanswerable. **The finding was one page away from a citation this repository had
published, and the wrong page number is what kept it there.**

---

## E52 — a quotation made a row stop being a row, and the sweep counted it as absent

**Status: found the same hour it was created, on 26 August 2026. Both checkers repaired.**

**What happened.** The *Weitzenhoff* row was written into
`standards/table_of_authorities.md` carrying a citation exactly as the reporter prints it:
`"511 U.S. at ----, 114 S.Ct. at 1804"`. The four hyphens are the West convention for a U.S. Reports
page that had not issued when the opinion went to print, and [E48](#e48--a-published-quotation-with-two-words-the-court-did-not-write-and-both-were-ours)
requires them to be reproduced rather than tidied away.

**`check_citations.py` decided the row was a table separator and skipped it.** The test was:

```python
elif line.startswith("| ") and "---" not in line and not line.startswith("| Authority"):
```

Three hyphens anywhere in a row disqualified it. The row was therefore **not counted among the
rows, not listed, and its flags were not counted in the standing debt.** The sweep printed
`rows in the table ...... 150` while the file held 151, and reported a debt of 22 against a true 23.
`check_claims.py` carried the same idiom for the state-of-play table.

**How it was caught, and this is the only reason it was.** The row was expected to appear in the
debt list and did not. Nothing in the output said a row had been dropped; the numbers were simply
smaller, and a smaller debt figure looks like progress. **Had the row not been one whose absence was
being watched for, this would have been a silent undercount of the repository's own reading debt.**

**The repair.** A separator row is now identified by what it actually is - a row whose every cell
consists only of hyphens, colons and space:

```python
_SEP_CELL = re.compile(r"^[\s:-]+$")

def is_separator_row(line):
    cells = [c for c in line.strip().strip("|").split("|")]
    return bool(cells) and all(_SEP_CELL.match(c) for c in cells)
```

Applied in both checkers. The sweep now reads 151 rows and 22 flagged, the second figure having also
been corrected by the second defect below.

### The rule

**E52 — a structural test written against a substring is a test against content. Markdown structure
is positional, and a checker that infers it from characters will be defeated the first time a
quotation contains those characters. Test the shape, not the spelling.**

This is the third member of the family [E50](#e50--the-spelling-sweep-erased-the-erratum-that-records-the-spelling-sweep-erasing-things)
opened: **a silent skip and a clean pass are indistinguishable in the output.** E50's seal ran to end
of file, E51's label was believed because nobody asked whether the first hit was the only one, and
E52's row vanished into a count that went down. All three were invisible in a report that said
nothing was wrong.

### And the second defect in the same row, which is a repeat offense

The *Weitzenhoff* row was written with **three ⚠ markers used as annotation** - one flagging an
unavailable pincite, one introducing the dissent, one introducing a correction - on a row whose
reading is complete. `check_citations.py` counts any row containing ⚠ as unread, so the row would
have declared itself unread the moment it became visible.

**This is the same mistake made three times in two days.** It was made on the § 3663A row, caught;
made again on both interim-standard rows, and reported to the maintainer as a debt of 22 when the
truth was 19; and made a third time here. The markers are removed and the row's residual debt now
lives where it belongs - on the *Staples* row, which is genuinely unread.

**⚠ in this table is a read-status flag and has no other meaning.** It is not emphasis, not a
caution, and not a way to point at something. If a read row needs to say something urgent, it says
it in bold.

---

## E53 — two rows for one authority, twice, added by the person who had just written the rule against it

**Status: found within the hour by a check written for the purpose. Both pairs merged.**

**What happened.** On 26 August 2026 rows were added to
`standards/table_of_authorities.md` for *Staples v. United States* and for *Liu v. SEC*, each
described in the row itself as "cited in the repository's prose and never graded until now."
**Both already had rows** — *Staples* under "Culpability and elements," *Liu* under "Penalties and
proportionality" — and neither was checked for first.

**Why it matters more than tidiness.** A row in this table is a **read-status**. Two rows for one
document are two read-statuses that drift, and nothing on either says which is current. *Staples*
briefly stood as both "unread, the pivot of the whole felony question" and "the modern presumption
of scienter where penalties are severe," with no flag at all.

**This is [E49](#e49--a-finding-the-repository-had-already-made-three-days-earlier-caught-at-the-door) again, on the same day E49 was cited in another correction.** E49's rule is that
the register is part of the text and the index of what is already open is read before a question is
opened. A table of authorities is exactly such an index. **Knowing the rule and citing the rule did
not produce the two-second grep that the rule asks for.**

**The repair, and it is the useful part.** `check_citations.py` now detects two rows carrying the
same authority, and distinguishes the accident from the intended case: **a pair is allowed when one
of the two rows points at the other in words** — the pattern already used for *Iverson*, where one
row carries the reading and the other says where the read-status lives. A pair with no pointer is
reported. The two pre-existing pairs it found on its first run, *Iverson* and 33 U.S.C. § 1319(c)(6),
were both real: the § 1319(c)(6) pair had no pointer and its two rows had already drifted, one
recording the statute's "**means**" verbatim and the other paraphrasing it as "includes."

### The rule

**E53 — a table of authorities is an index of read-statuses, and a second row for one authority is a
second read-status. Before adding a row, grep for the party name. Where two rows are wanted, one of
them must say where the reading lives.**

### And a second checker defect found in the same pass

`check_citations.py` reported *Liu v. SEC* as cited-with-no-row while its row sat three lines away.
Its matcher tests whether either party name appears in the table and **skips any party shorter than
five characters** to avoid noise. "Liu" and "SEC" are both shorter than five characters, so that
case could never match, no matter how many rows it had. Any case with two short party names was
permanently unmatchable and permanently reported as debt. **A guard against false positives had
manufactured a false positive that could not be cleared by doing the work it demanded.** The matcher
now falls back to the whole caption when every party name is short.

---

## E54 — a case caption written in the form such captions usually take, from a source that gave no caption

**Status: published in `standards/table_of_authorities.md` on 26 August 2026; corrected the same day.**

**The claim.** A row reading ***In re Alibaba Group Holding Ltd. Securities Litigation* (S.D.N.Y.,
filed 4 Aug 2026)**, flagged ⚠ unread, "known from The D&O Diary."

**The source, which this project holds and which was re-read to write this entry.** The D&O Diary
piece names no case. It says "A securities class action complaint filed on August 4, 2026, in the
Southern District of New York against Alibaba Group Holding Limited (Alibaba) and the company's
CEO," and thereafter calls it "the Alibaba SCA."

**The truth.** *Wistisen v. Alibaba Group Holding Limited*, No. 1:26-cv-06654 (S.D.N.Y., filed
4 Aug. 2026) — caption, docket number, court and filing date confirmed against the CourtListener
RECAP index on 26 August 2026.

**How the wrong caption got written.** The court and the date were in the source. The caption slot
was empty, and it was filled with the form such captions usually take: *In re [Company] Securities
Litigation*. That form is correct for a **consolidated** securities class action. This one is a
single named plaintiff and is not consolidated, so the invented caption is wrong in the one respect
that would matter to anyone trying to find it.

**Nothing marked it.** The ⚠ said *unread*, which was true. **A read-status flag cannot say "this
caption was never in a source,"** and the row carried an attribution — "known from The D&O Diary" —
that made the caption look sourced when only the surrounding facts were.

### The rule

**E54 — a citation has parts, and they are sourced separately. Court, date and docket may come from
a report; the caption comes from the docket or it does not exist. Where a slot is empty, the entry
says it is empty. A conventional form is not a source, and filling a slot from convention is
[E46](#e46--two-quotations-published-this-afternoon-are-not-in-the-opinions-they-were-attributed-to) with better manners.**

---

## E55 — a citation taken from the first of two footnotes that contradict each other twelve lines apart

**Status: published since 25 August 2026; corrected 26 August 2026.**

**The claim.** *Kadrey v. Meta Platforms, Inc.*, **No. 23-CV-03217-VC**, 2025 WL 1752484 (N.D. Cal.
June 25, 2025), taken from Maxwell V. Pritt's Written Answers to Questions for the Record at printed
p. 93 of S. Hrg. 119-202. The row was honest about the chain: quoted at second hand, read by OCR,
"the pin cite is his, not ours."

**What is actually on that page.** Both of Pritt's first two footnotes cite the same case, and they
give different numbers:

> ¹ *Kadrey, et al. v. Meta Platforms, Inc.*, No. 23-CV-**03217**-VC, 2025 WL 1752484, at \*2
> (N.D. Cal., June 25, 2025).
>
> ² *Kadrey, et al. v. Meta Platforms, Inc.*, No. 23-CV-**03417**-VC, Dkt. 574 (Pls' Mot. for
> Partial Summary Judgment) at 8.

Read at 200 dpi, re-read at 450 dpi, and finally looked at as an image rather than as text, because
a 2 and a 4 are exactly what an OCR pass gets wrong and the whole question was one digit. The two
footnotes genuinely differ. **CourtListener's RECAP index resolves it: 3:23-cv-03417, N.D. Cal.,
filed 7 July 2023.**

**So this is not an OCR error, ours or anyone's.** It is a typo in a document submitted to the
Senate, reproduced faithfully by a project that took the first citation it found and did not read
twelve lines further down the same page — where the source corrected itself.

### The rule

**E55 — when a citation is taken at second hand, read every place the source cites that authority,
not the first. A source that cites something twice has checked itself, and the check is free.**

**Second-order, and it is the reason this was findable at all.** The correcting footnote was
discovered only because an outside retrieval returned a different docket number and the difference
had to be explained. **A disagreement with an outside source is worth more than an agreement**, and
this project's response to one should always be to open the page rather than to decide which side is
more likely right.

---

## E56 — a holding published inside out: the court's confirming reason reported as its ratio

**Status: published in the cure register, the lane sweep and both packets since 25 August 2026;
corrected 26 August 2026 on reading the opinion.**

**The claim, in the form it appeared in four files.** "*United States v. Ahmad*, 101 F.3d 386, 391
(5th Cir. 1996) holds that illegal discharges under the CWA are **not** public welfare offenses,
**because** they are 'felonies punishable by years in federal prison'."

**The opinion, read 26 August 2026 in a law.resource.org reporter capture.** The sentence the
"because" was built from reads:

> "The fact that violations of § 1319(c)(2)(A) are felonies punishable by years in federal prison
> **confirms our view** that they do not fall within the public welfare offense exception."

**A reason offered as confirming a view already reached is not the reason the view was reached.**
The court's ground is mistake of fact: whether "knowingly" attaches to the nature of the substance
discharged, so that "one who honestly and reasonably believes he is discharging water may find
himself guilty of a felony if the substance turns out to be something else."

**And a second thing the reading corrected.** This project had been describing *Ahmad* and
*Weitzenhoff* as a circuit split — including in [E51](#e51--a-pincite-copied-from-a-citing-case-from-the-wrong-one-of-its-four-citations), written the same morning. *Ahmad* says
the opposite about its own relationship to that case: the Ninth Circuit "was concerned almost
exclusively with whether the language of the CWA creates a mistake-of-law defense. Both cases are
easily distinguishable, for neither directly addresses mistake of fact or the statutory construction
issues raised by Ahmad." **A narrower disagreement does survive** — over what *Staples* decided at
618 — and that one is real.

### The rule

**E56 — "because" is a claim about a court's reasoning, and it is verified in the opinion or not
made. A case known only through a summary may be reported as holding something; it may not be
reported as holding it *for a reason*.**

This is [E32](#e32--e22-extended-from-the-repository-to-correspondence) applied to the inside of a case rather than its outside: no characterization until
read, and the ordering of a court's reasons is a characterization. **The published version was
sharper than the opinion**, which is the tell. A secondary summary compresses toward the memorable
sentence, and the memorable sentence in *Ahmad* is the one about felonies.

**Cost, stated plainly.** For a day the criminal lane treated its own hardest objection as resting
on a ground the case does not rest on, and built two cures around answering it. The answers survive —
*Weitzenhoff* at 1286 n.7 still refuses *Ahmad*'s reading of *Staples* — but the objection they were
answering was not quite the one in the reports, and a criminal-law reviewer would have said so in
the first paragraph of a disposition.

---

## E57 — a new provenance grade, because three sources arrived by a route this register had no name for

**Not a correction. A rule entry, filed the day the category appeared, so that nothing enters the
repository through it unlabeled.**

**What happened.** Three sources that repeated retrieval runs could not reach — Ind. Const. art. 1,
§ 16, *Walton*, and *Philip Morris* — were reached on 26 August 2026 by a **fetch tool that
downloads a page and has a small language model answer a question against it**. It returned the
Indiana clause, *Walton*'s full caption and court, and the *Philip Morris* respondeat superior
passage: all three had defeated a script, and none of them defeated this.

**The problem is that the register has two grades and this is neither.** A source is *held* — the
document is on the shelf, and someone can open it — or it is *not held*. This is a third thing. **A
model read the document and told us about it.** That is better than a secondary summary, because the
model had the primary in front of it. It is worse than reading, because the thing that reaches the
repository is the model's rendering, and nobody has seen the page.

**[E22](#e22--a-quotation-held-in-a-working-summary-is-not-a-quotation) already decides the hard part.** A quotation held in a working summary is not a
quotation, and a model's answer is a working summary — it is generated text about a document, which
is the exact category E22 was written to exclude. **So nothing arriving this way may be published as
a quotation.** What may be taken is the kind of fact that survives rendering: a caption, a court, a
docket number, a date, a page count, whether a copy carries star pagination.

### The rule

**E57 — a model-mediated fetch is a lead, not a reading. It may fix metadata and it may not supply a
quotation. It is marked ◐, it always carries a ⚠ beside it, and the file it produces says
`MODEL-MEDIATED-FETCH-NOT-THE-DOCUMENT` in its own name.**

The mark is now in this table's legend, and `check_citations.py` reports any ◐ row that does not
also carry a ⚠, because a row graded half way and counted as graded is
[E52](#e52--a-quotation-made-a-row-stop-being-a-row-and-the-sweep-counted-it-as-absent) in a new
costume.

### Two things worth keeping from the three fetches

**One. The route matters, and it is not the same route a script takes.** *Philip Morris* was reached
through CourtListener, which an earlier run that same morning reported behind a bot challenge, and
the Indiana clause came from a legislature PDF whose sibling URL returns an empty application shell.
**"Blocked" is a property of a request, not of a site**, and this register should stop recording it
as though it were the second.

**Two. A collision found while pinning a clause, recorded before it bites.** The companion cites
**Or. Const. art. I, § 16** and **Ind. Const. art. 1, § 16** in a single sentence. Same section
number, same opening words, three words apart at the end: the companion gives Oregon as "all
penalties shall be proportioned to the offense," and Indiana reads "all penalties shall be
proportioned to **the nature of** the offense." Oregon's text is still unpinned. **Whoever pins it
must pin it against Oregon's own publication**, because the near-identity is precisely the shape of
mistake this shelf keeps making with surnames, and it would be invisible in a proofread.

### Added the same day: the clearest demonstration this rule will ever get

Hours after E57 was written, **two fetches of the same *Walton* opinion, through two different
renderings of it, disagreed about the document's own front page.** The Delaware courts' own service
returned **26 April 2023, 58 pages**. A mirror's PDF of the same opinion returned **12 April 2023,
56 pages**, with a confident summary of what the case was about. Two further pages settle it — the
opinion's caption block reads "Date Submitted: January 13, 2023 Date Decided: April 26, 2023" — so
the second rendering was simply wrong.

**Nothing in either answer looked uncertain.** Both gave a date, a page count and a subject, in the
same register of confidence. **The disagreement was only visible because the same document was
fetched twice**, which is not something a retrieval does by default and is not something a reader
would think to do.

**So the rule tightens.** Where a ◐ source supplies a fact that will be published — a date, a docket,
a page count — **fetch it twice, from two renderings, and record both.** Where they disagree, neither
is the answer; the document is.

**What the three fetches did not do.** None of them put a document on the shelf. The Indiana
constitution PDF, the *Walton* opinion and a clean *Philip Morris* print are each one deliberate
download away, and until someone makes it, the strongest thing this project can say about all three
is that it knows where they are. **[E47](#e47--three-page-numbers-from-a-source-that-has-no-page-numbers-caught-before-publication)'s discipline applies unchanged: the *Philip Morris*
pincite at 1118 is no closer to confirmed than it was yesterday.**

---

## E58 — a citation that exists only in a URL and a page title is not a citation, and it nearly overwrote a correct one

**Status: caught before any change was made. Filed because the near miss was one keystroke wide.**

**What happened.** While looking for a clean print of *United States v. Philip Morris USA Inc.*, a
search result appeared whose page title and URL both carried the case at **556 F.3d 1095**. This
repository publishes it at **566 F.3d 1095**. One digit, and the outside source is the kind that
usually wins an argument: a public-health litigation tracker, a specialist body with no reason to be
careless.

**A structural argument pointed the same way and was not enough.** Volume 556 of the Federal Reporter
covers early 2009 and volume 566 covers late spring; the opinion was decided 22 May 2009, which fits
566. **That is a rule of thumb about publication schedules, not a source**, and this register does not
correct citations from rules of thumb in either direction.

**What settled it.** The Solicitor General's own petition in the case, which states in its OPINIONS
BELOW section: "The opinions of the court of appeals (Pet. App. 1a-98a, 99a-176a) are reported at
**566 F.3d 1095** and 396 F.3d 1190." The repository's citation was right.

**Where the 556 came from is the interesting part.** It appears in the tracker's **page title and URL
slug** — the parts of a web page that are written once, by hand, usually years ago, and never
proofread against anything, because nothing renders them next to the text they describe. The body of
that page does not repeat the citation at all.

### The rule

**E58 — a citation appearing only in a URL, a page title, a filename or a link label is not a
citation. Those are labels, written once and never checked against the document they name. Before
changing a citation this project publishes, find it in a document that a court, a party or a
publisher would be embarrassed to get wrong.**

**And the second-order habit this reinforces**, because it is the third one-digit dispute in a single
day. [E51](#e51--a-pincite-copied-from-a-citing-case-from-the-wrong-one-of-its-four-citations) was a page number taken from the wrong one of four citations; E55 was a docket number
taken from the first of two footnotes that disagreed; this was a volume number taken from a URL.
**All three were single digits, all three looked exactly like every other digit on the page, and none
of the three would have been caught by reading more carefully.** They were caught by noticing that
two sources disagreed and going to a third. **Disagreement is the instrument. Care is not.**

---

## E59 — two opinions, two weeks apart, under one case number, and a date I confirmed from three sources that the document contradicts

**Status: published this morning in `standards/table_of_authorities.md`; corrected the same day when
the document arrived.**

**What was published.** That the *Walton* opinion's own caption block reads **"Date Submitted:
January 13, 2023 Date Decided: April 26, 2023,"** and that the subject is the Rule 23.1
demand-futility ruling. It was written as a confirmation, on the strength of three sources agreeing:
the Delaware courts' own opinion service, a Delaware firm's case note, and Justia's case page, which
carries the date as a field.

**What the document says.** The PDF, downloaded and opened:

> **OPINION ADDRESSING DEFENDANTS' MOTION TO DISMISS ON THE BASIS OF LACHES**
> Date Submitted: January 13, 2023
> **Date Decided: April 12, 2023**

**Sixty-four pages**, not the 56 or 58 that two separate model-mediated fetches reported.

**Both things are true, and that is the finding.** There are **two opinions in C.A. No.
2021-0827-JTL, two weeks apart**: a **laches** opinion on 12 April 2023, which is the one now on the
shelf, and a **Rule 23.1 demand-futility** opinion on 26 April 2023, which is the one the firm note
describes. Justia's case page carries the later date and serves the earlier opinion's PDF. Nothing
in any of the three sources said "one of two."

### What this costs, and it reaches backwards

This repository cites *Walton* as **294 A.3d 65, 90, 92**. **Which of the two opinions is reported at
294 A.3d 65 is now unsettled**, and so is the question of which one
[E46](#e46--two-quotations-published-this-afternoon-are-not-in-the-opinions-they-were-attributed-to) read when it found two quotations fabricated. E46's finding survives — the invented
sentences are absent from the opinion now held, and the reading also showed exactly which real
sentence they were assembled from — but **an erratum that says "not in the opinion" has to name the
opinion**, and until today nobody knew there was a choice to make.

### The rule

**E59 — a case number is not a document. Where a matter has produced more than one opinion, a
citation that names only the case names nothing, and agreement among secondary sources about "the"
opinion is agreement about a thing that may not exist. Before citing, ask how many opinions there
are.**

### And the third strike against confirming anything by consensus

Three sources agreed on 26 April and the document says 12 April. **They did not agree because they
had checked; they agreed because they were describing the other opinion**, and nothing in their
phrasing distinguished the two. This is the same shape as [E58](#e58--a-citation-that-exists-only-in-a-url-and-a-page-title-is-not-a-citation-and-it-nearly-overwrote-a-correct-one),
where a citation lived only in a page title, and the same shape as E55, where a witness's two
footnotes disagreed. **Agreement among sources that are all downstream of one another is not
corroboration.** The document is the only thing that ends the question, and this register has now
recorded that lesson four times in one day, which suggests the lesson is not the problem.

### One thing that went the other way, recorded because the register should not only collect failures

The *Philip Morris* passage that the same model-mediated route returned — corporations liable for
specific intent on the "knowledge and intent" of their employees, because "a corporation only acts
and wills by virtue of its employees" — **is in the opinion, word for word**, confirmed on reading
the document. [E57](#e57--a-new-provenance-grade-because-three-sources-arrived-by-a-route-this-register-had-no-name-for)'s caution is not that these fetches are wrong. It is that nothing in the
answer tells you which kind you have got.

**And a false negative worth admitting**, because it nearly produced a fifth erratum in the wrong
direction: a first search of the document for that passage returned **zero hits** and briefly looked
like proof the quotation was invented. The passage was there. The search failed because the text
wraps mid-phrase across two lines and the document uses curly quotation marks. **A grep that returns
nothing is evidence about the grep.**

---

## E60 — the register's most-cited fabrication finding was itself wrong, and a real quotation was deleted on the strength of it

**Status: found 26 August 2026 on reading the second of two opinions. The correction runs the
opposite way from every other entry in this register: something true was removed as false.**

**What [E46](#e46--two-quotations-published-this-afternoon-are-not-in-the-opinions-they-were-attributed-to)
said.** That two sentences published in `docs/known_objections.md` and attributed to *Ontario
Provincial Council of Carpenters' Pension Trust Fund v. Walton*, 294 A.3d 65, 90, 92 (Del. Ch. 2023)
"do not appear" in the opinion. The passage was removed and replaced with a sentence saying Delaware
has **not** squarely decided the question.

**What the opinion says.** Both sentences are there, word for word.

At **slip op. 76**:

> "When directors make a business decision that **carries legal risk, but which otherwise involves
> legally compliant conduct,** then the business judgment rule protects that decision."

At **slip op. 77–78**, across a page break:

> "In the former case, the directors can make a business judgment to pursue the project. In the
> latter case, the decision to pursue the project **would constitute a conscious decision to violate
> the law, the business judgment rule would not apply, and the directors would be acting in bad
> faith.**"

**The published sentence quoted both correctly.** Nothing was invented.

### How a correct quotation got deleted as a fabrication

**C.A. No. 2021-0827-JTL produced two opinions two weeks apart** — a **laches** opinion on 12 April
2023, 64 pages, and a **demand-futility memorandum opinion** on 26 April 2023, 123 pages. E46's check
was run against the first. **Neither sentence is in the laches opinion, and both are in the other
one.** Nothing in the retrieval, in the case name, in the citation, or in three secondary sources
that describe "the" opinion said there was a choice to be made. [E59](#e59--two-opinions-two-weeks-apart-under-one-case-number-and-a-date-i-confirmed-from-three-sources-that-the-document-contradicts) records the discovery that
there are two; this entry is what that discovery cost going backwards.

### What it cost

A published answer to the objection a governance lawyer raises first — *can the business judgment
rule be raised against this Act?* — was **replaced with "that question is open"** and a note blaming
the project's own fabricated citation. For a day, this repository told reviewers it had asserted
something on the strength of quotations nobody wrote, when it had quoted a Delaware Vice Chancellor
accurately and pincited him correctly.

**And the deterrent effect is the worse half.** *Walton* was flagged in the table of authorities as
the case carrying two fabricated quotations, with a standing instruction that nothing be attributed
to it. That instruction was wrong and it was the loudest instruction in the row.

### The rule

**E60 — a finding that a quotation is absent is a claim about a document, and it names the document
or it means nothing. "Not in the opinion" requires knowing which opinion, and how many there are.
Absence is only ever provable against a specific text; it is never provable against a case.**

**The asymmetry that makes this rule matter.** A false positive — publishing a quotation that turns
out to be invented — is caught by the next person who reads the source. **A false negative is not
caught by anything**, because the quotation has been deleted and nobody re-checks a sentence that is
no longer there. This one surfaced only because an unrelated question about a date sent someone to
the other opinion.

### Two searches that returned nothing and meant nothing

Both quotations were initially reported absent from the 26 April opinion too, by grep, before being
found by eye. **"carries legal risk"** matched only because the phrase happens not to wrap; the
longer sentence returned **zero hits** because it **spans a page break**, with a page number and two
blank lines sitting inside it. Earlier the same day the *Philip Morris* passage returned zero hits
because it wraps mid-phrase and uses curly quotation marks.

**Three false negatives from three different causes in one session.** [E47](#e47--three-page-numbers-from-a-source-that-has-no-page-numbers-caught-before-publication) says a source without
pagination cannot confirm a page. This is its inverse: **pagination inside a text file breaks the
sentences it paginates**, and a search over extracted text is searching a document that has had
furniture inserted into it.

### What is not fixed

The **reporter pincites 90 and 92 are still unconfirmed.** The copy now held carries **slip pages,
not Atlantic Reporter pages**, and slip-to-reporter offsets are not computable — the two data points
available happen to differ by sixteen, which is a coincidence and not a mapping. Under E47 this copy
confirms the quotations and cannot confirm the pages.

---

## Part I(b) — The negative-findings register

*Opened 26 August 2026 after [E60](#e60--the-registers-most-cited-fabrication-finding-was-itself-wrong-and-a-real-quotation-was-deleted-on-the-strength-of-it),
in which a correct quotation was deleted from a public page because a search for it returned
nothing.*

**Why this is a separate register.** Every other entry above is **additive**: it says "we published
X, X is wrong, here is the fix," and it quotes X, so the entry carries its own evidence and any later
reader can re-test it. A finding that something is **absent** carries no evidence. The text is gone,
nothing points at it, and **nobody re-checks a sentence that is no longer there.** That asymmetry is
why E46 stood for a day and could have stood for years: a false positive is caught by the next
reader; a false negative is caught by nothing.

**So negative findings are listed, not merely recorded**, and `check_quotations.py --negatives`
re-tests every line here against the shelf on every run. When a new source lands, the register
answers for itself.

```negative-findings
# status | quoted string (verbatim, as published) | attributed to | erratum
MISATTRIB| What a corporate fiduciary cannot do, however, is make a business judgment to cause or allow the corporation to break the law | Walton slip op. 76 (real); credited to In re TransUnion, 324 A.3d 869, 887 | E46 -> E62
WITHDRAWN| carries legal risk, but which otherwise involves legally compliant conduct | Walton, C.A. 2021-0827-JTL (Del. Ch. 26 Apr. 2023) | E46 -> E60
WITHDRAWN| would constitute a conscious decision to violate the law, the business judgment rule would not apply, and the directors would be acting in bad faith | Walton, C.A. 2021-0827-JTL (Del. Ch. 26 Apr. 2023) | E46 -> E60
```

**A WITHDRAWN line stays here forever.** It is the record of a finding this project got wrong in the
direction nothing else catches, and deleting it would be deleting the only evidence that the failure
mode is real.

### E61 — how a negative finding is made

**A finding that a quotation is absent is made by reading the cited location, not by searching.**

1. **Enumerate the documents first.** A case number is not a document; one matter can produce several
   opinions ([E59](#e59--two-opinions-two-weeks-apart-under-one-case-number-and-a-date-i-confirmed-from-three-sources-that-the-document-contradicts)).
   State how many candidates exist and which was read.
2. **Go to the pincite, not to the string.** "I read page 90 and it says X" is checkable by anyone.
   "I searched and found nothing" is checkable by no one.
3. **Where the location cannot be resolved** — no pincite, or a copy whose pagination cannot settle
   one ([E47](#e47--three-page-numbers-from-a-source-that-has-no-page-numbers-caught-before-publication))
   — the finding is **"unverifiable from this copy."** That is a weaker and different claim from
   "absent," and it does not justify deleting anything.
4. **Name the file.** The shelf filename, so the check can be re-run against the same bytes.
5. **A search that returns nothing is evidence about the search.** Extracted text has furniture
   inserted into it: page numbers land inside sentences, words hyphenate across line breaks, quotation
   marks curl. All three defeated a search on 26 August alone.

**And the tool obeys the same rule.** `check_quotations.py` can conclude that a quotation **is** on
the shelf. It can never conclude that one is absent — a miss is printed as a prompt to read, and the
report says so on every run. A quotation-checker that reported absences would recreate E60 at scale,
which is the one thing this project cannot afford to automate.

---

## E62 — the third "fabrication" was a misattribution, and the instrument built to catch this found it on its first run

**Status: found 26 August 2026, about twenty minutes after `check_quotations.py` was written, by the
tool's own re-test of the negative-findings register.**

**What [E46](#e46--two-quotations-published-this-afternoon-are-not-in-the-opinions-they-were-attributed-to)
said.** That this sentence, published attributed to *In re TransUnion Derivative Stockholder
Litigation*, 324 A.3d 869, 887 (Del. Ch. 2024), "does not appear in that opinion."

**Where the sentence actually is.** *Walton*, demand-futility opinion of 26 April 2023, **slip op. 76**:

> "What a corporate fiduciary cannot do, however, is make a business judgment to cause or allow the
> corporation to break the law. 'Delaware law does not charter law breakers.' *In re Massey Energy
> Co.*, 2011 WL 2176479 (Del. Ch. May 31, 2011)."

**E46 was right that it is not in the opinion it was credited to, and wrong about what that means.**
The sentence is Laster's own, in a case this project cites, on the proposition it was wanted for.
**A misattribution is not a fabrication.** One is a citation error; the other says no court wrote the
thing. This register called the first the second and let it stand.

**Still open:** whether the sentence also appears in *TransUnion*. That needs *TransUnion*, which is
not held. It is a retrieval now, not a conclusion.

### The rule

**E62 — "not in the opinion it was credited to" and "nobody wrote it" are different findings, and the
second is far larger. Before recording a fabrication, search the whole shelf for the sentence.** A
real sentence in the wrong coat is the commonest citation error there is, and it is repaired by
fixing the attribution, not by deleting the argument.

### What found it, which is the part worth keeping

`check_quotations.py` was written this afternoon in answer to E60, on one design rule: **it can
conclude that a quotation is on the shelf and can never conclude that one is absent.** Its
`--negatives` mode re-tests every recorded negative finding against the shelf on every run, because
what E60 exposed is that **nobody re-checks a sentence that has been deleted.**

Three findings were in the register when it first ran. It printed:

```
*** WAS RECORDED ABSENT AND IS ON THE SHELF ***
    What a corporate fiduciary cannot do, however, is make a business judgment  (E46)
    found in: RECORD_DelCh_Ontario-Carpenters-v-Walton_...DEMAND-FUTILITY-2023-04-26...
    Read the document. This is how E60 was found.
```

**An hour earlier, having withdrawn two of E46's three findings, this project explicitly declined to
touch the third** — "it has not been re-checked, and nothing in the *Walton* correction bears on it."
That was the right call on the evidence then available and it was wrong on the facts. **The
instrument, which knows nothing and cannot read, caught in one second what careful restraint got
wrong.** That is not an argument against restraint. It is the argument for putting negative findings
somewhere a machine re-tests them, because judgment does not re-examine what it has already
deliberately set aside.

---

## E63 — "every case cited in prose now has a read-status" was false, and the checker that said so was matching on the words "United States"

**Status: reported to the maintainer three times on 26 August 2026 and written into
`research/verification_record.md` and a retrieval brief. Corrected the same day.**

**The claim.** That `check_citations.py` showed **zero** case captions cited in the repository's
prose without a row in the table of authorities — announced as the closing of Tier 4, the nineteen
captions that had never been graded.

**The defect.** The matcher asked whether *either* party name of a caption appeared **anywhere in the
table's text**. So *Johnson v. United States* matched, because dozens of rows say "United States."
*Lambert v. California* matched on "California." **Any case with one common party name was
unmatchable-as-missing**, permanently, no matter how absent its row.

**What it hid.** *Lambert v. California* and *Johnson v. United States* — the two leading vagueness
cases, cited on the objections page against this Act's own duty language, with no row and no
read-status. **The vagueness objection is the one that most often kills a bill in committee, and its
two authorities were invisible to the instrument built to find exactly this.**

**The repair.** A party name now counts as evidence only where **some single row carries both
parties**. And `trim_second_party` stops at a sentence boundary, because captions were bleeding into
the following sentence — "Ulster County v. Allen. **Extend the**" — and then matching no row, which
reported real rows as missing in the other direction.

### The rule

**E63 — a test that asks whether a token appears *somewhere in a corpus* is not a test about the row
that should contain it. Membership questions are answered against the record, not against the file.**

This is [E52](#e52--a-quotation-made-a-row-stop-being-a-row-and-the-sweep-counted-it-as-absent)'s
family again — a structural question answered by substring — and the third time in one day that a
checker reported a clean number while not looking at part of what it claimed to cover.

### What was deliberately not done

The sweep now reports **three** captions with no row that **do have rows**: abbreviation mismatches
and one caption joined across an "and". Those are false positives and they are being left in.

**Tuning a checker until it reports zero is the failure this register spent the day recording.** A
false positive costs somebody a look. A false negative cost this project a published claim that was
not true, repeated three times, in two documents. **The error is left pointing toward noise.**

---

## E64 — a view the Supreme Court declines to adopt, published as the rule it adopted

**Status: published in `standards/table_of_authorities.md` on 26 August 2026, hours before the case was
read. Corrected on reading it.**

**What was published.** That *Staples v. United States*, 511 U.S. 600, holds at **618** that serious
felonies fall outside the public welfare offense exception "absent a clear statement from Congress
that mens rea is not required." The line was taken from *Ahmad*, which quotes it that way, and
recorded here as one of two pincites the case supplies.

**What page 618 actually says**, read in the Library of Congress U.S. Reports print, in one
continuous passage:

> "Close adherence to the early cases described above might suggest that punishing a violation as a
> felony is simply incompatible with the theory of the public welfare offense. **In this view,**
> absent a clear statement from Congress that mens rea is not required, we should not apply the
> public welfare offense rationale to interpret any statute defining a felony offense as dispensing
> with mens rea. **But see *United States v. Balint*, 258 U. S. 250 (1922).**
>
> **We need not adopt such a definitive rule of construction to decide this case, however.** Instead,
> we note only that where, as here, dispensing with mens rea would require the defendant to have
> knowledge only of **traditionally lawful conduct**, **a severe penalty is a further factor** tending
> to suggest that Congress did not intend to eliminate a mens rea requirement."

**"In this view" opens it and "we need not adopt such a definitive rule" closes it.** The sentence is
the *antecedent* of the reservation — the Court states a possible rule in order to decline it, and
attaches a *But see* to its own counter-authority in the same breath.

### What this does to the leading objection

***Ahmad*, 101 F.3d 386, 391 quotes the declined view as though it were the holding**, and this
project repeated it. The two sentences *Weitzenhoff* and *Ahmad* fight over turn out to be **the same
passage on the same page**, and read whole it favours *Weitzenhoff*:

- The Court **declines** the felony-incompatibility rule in terms.
- It calls a severe penalty **"a further factor"**, not a bar. *Ahmad* treats it as decisive.
- It cites **its own counter-authorities**: *Balint* in the text, and at **617 n.14** *State v.
  Lindberg*, 125 Wash. 51 (1923), "applying the public welfare offense rationale to a felony."
- And *Balint* is the case ***Hanousek* rests SEC. 6(a)'s due-process answer on**, already read and
  held here. The Supreme Court flagged it as the answer to the felony objection thirty-two years
  before this project independently arrived at it.

**The operative trigger is not the penalty at all.** It is "where, as here, dispensing with mens rea
would require the defendant to have knowledge only of **traditionally lawful conduct**." Owning a gun
is traditionally lawful. **So the real question for this Act was never "can a felony be a public
welfare offense." It is whether training and deploying a frontier model is traditionally lawful
conduct** — a narrower question, and one a reviewer can actually answer.

### The rule

**E64 — a proposition a court states in order to reject it reads exactly like a proposition a court
holds. Before quoting a sentence from an opinion, read the sentence after it.** Signals like "in this
view", "it might be suggested", and a *But see* attached to the court's own contrary authority are
the tell, and they are invisible in a quotation taken at second hand.

**And the second-order point, which this register has now made four times in one day.** The error
entered because the sentence arrived through *Ahmad* rather than from the reports. [E22](#e22--a-quotation-held-in-a-working-summary-is-not-a-quotation)
says a quotation held in a working summary is not a quotation; **a quotation held in an adversary's
brief is not a holding**, and an adversary has every reason to stop reading at the sentence that
helps.

## E65 — *Global-Tech* called a constitutional ceiling in three files, and it decides no constitutional question

**Status: published in `standards/what_these_words_mean.md`, `packets/criminal_law.md` and
`audit/v3_5_cure_language.md`. Corrected on reading the opinion, 26 August 2026.**

**What was published**, in identical words in all three files:

> "The constitutional ceiling is *Global-Tech Appliances, Inc. v. SEB S.A.*, 563 U.S. 754, 769
> (2011)."

**The pincite is right and the characterization is wrong.** Read in the govinfo U.S. Reports print,
which carries real reporter pagination, page **769** carries the two-part test:

> "While the Courts of Appeals articulate the doctrine of willful blindness in slightly different
> ways, all appear to agree on two basic requirements: (1) The defendant must subjectively believe
> that there is a high probability that a fact exists and (2) the defendant must take deliberate
> actions to avoid learning of that fact."

**That is not a constitutional holding.** *Global-Tech* is a **civil** patent case under 35 U.S.C.
§ 271(b). The passage is the Court's distillation of what the Courts of Appeals already agree on —
"all appear to agree" — supported by a footnote collecting one case from each circuit. No
constitutional question is presented, argued or decided. The word "constitutional" appears in this
project's sentence and nowhere in the Court's.

**The one constitutional touch in the opinion is a different doctrine.** At **767** the Court notes
that it has used the Model Penal Code's definition of knowledge "as a guide in analyzing whether
certain **statutory presumptions of knowledge** comported with due process," citing *Turner v.
United States*, 396 U.S. 398, 416–417 (1970) and *Leary v. United States*, 395 U.S. 6, 46–47 and
n.93 (1969). A due-process limit on a *statutory presumption* is not a constitutional ceiling on a
*judicially administered doctrine*, and the two were merged somewhere between reading about the case
and writing about it.

### What is true, and is worth more to this Act than what was claimed

**The test is a ceiling in substance, by ordinary stare decisis rather than by the Constitution**,
and it binds in the direction SEC. 6(b) needs. At **770** the Court rejects the Federal Circuit's
looser standard in terms — it "departs from the proper willful blindness standard in two important
respects": it allowed knowledge on "merely a 'known risk'", and demanding only "deliberate
indifference" it "does not require active efforts by an inducer to avoid knowing." The Court fixes
willful blindness above recklessness and negligence: a willfully blind defendant "can almost be said
to have actually known the critical facts," while "a reckless defendant is one who merely knows of a
substantial and unjustified risk."

### And the answer to the criminal-versus-civil question runs the other way

The question asked of this case was whether the Court limits willful blindness in criminal as
against civil contexts. **It does the reverse.** At **766**: "The doctrine of willful blindness is
well established in criminal law." At **768**, having traced that history: "we can see no reason why
the doctrine should not apply in **civil** lawsuits for induced patent infringement under 35 U.S.C.
§ 271(b)." The movement is criminal outward into civil, and the opinion contains no sentence
narrowing the doctrine for criminal cases.

**Which leaves a smaller problem in place of the one that was claimed.** The authority this Act cites
for the criminal knowledge element of SEC. 6(b) is a civil case, describing criminal practice
accurately but deciding a civil question. That is a fair citation and it should be made in those
words, not dressed as a constitutional limit.

### The rule

**E65 — "constitutional" is a claim about what a court decided, not an intensifier for how firmly it
said it.** A rule can bind without being constitutional, and describing it as constitutional
attributes to a court a question it was never asked. Before writing that an authority sets a
constitutional limit, name the constitutional provision and the party who raised it.

**The pincite survived the characterization, and that is the part to notice.** [E47](#e47--three-page-numbers-from-a-source-that-has-no-page-numbers-caught-before-publication)
separates text from page as two claims verified separately. This entry adds a third: **the
proposition a pincite is offered *for* is a claim too**, and a correct page number lends it a
borrowed credibility it has not earned.

## E66 — half of *Johnson & Towers* published as the whole of it, and the missing half is the half that bears on SEC. 6(d)

**Status: published in `standards/table_of_authorities.md` and `audit/v3_5_cure_language.md` (CURE
22). Corrected on reading the opinion, 26 August 2026.**

**What was published.** That *United States v. Johnson & Towers, Inc.*, 741 F.2d 662 (3d Cir. 1984)
holds, as "the Third Circuit's outlier rule", that the jury must find the defendant "knew a permit
was required and that none was held". CURE 22 carries it as the Third Circuit's side of a split.

**That much is verbatim in the opinion**, in the body of Part III.B:

> "in light of our interpretation of section 6928(d)(2)(A), it is evident that the district court
> will be required to instruct the jury, inter alia, that in order to convict each defendant the
> jury must find that each knew that Johnson & Towers was required to have a permit, and knew that
> Johnson & Towers did not have a permit."

**The next sentence was not published, and it is the court's own qualification:**

> "Depending on the evidence, the district court may also instruct the jury that such knowledge may
> be inferred."

**And Part IV states the holding with the qualification built into it:**

> "we conclude that the individual defendants are 'persons' within section 6928(d)(2)(A), that all
> the elements of that offense must be shown to have been knowing, **but that such knowledge,
> including that of the permit requirement, may be inferred by the jury as to those individuals who
> hold the requisite responsible positions with the corporate defendant.**"

**The knowledge requirement and the route around it are one sentence, and this project published the
first clause.** The court says as much itself at the head of Part III.B: its conclusion "does not
impose on the government as difficult a burden as it fears."

### What this does to CURE 22

CURE 22's new text for SEC. 6(b) ends with a sentence written as a concession against the Act's own
convenience:

> "Responsibility and authority under SEC. 6(d), standing alone, do not establish knowledge."

**On the sentence *Johnson & Towers* actually holds, the Third Circuit permits the inference that
sentence declines to permit** — knowledge "may be inferred by the jury as to those individuals who
hold the requisite responsible positions with the corporate defendant." The two are not in
contradiction: a permissive inference a jury may draw is not the same as a matter established as a
matter of law, and SEC. 6(b) may be drafted more narrowly than RCRA if that is the choice. **But the
concession was drafted as though the authority compelled it, and it does not.** It is a policy
choice, and it should be defended as one.

### The second half of the question, which the row does not answer

**The rule is confined to the subsection and is not stated generally.** The court's own words tie it
to the construction it had just performed — "in light of our interpretation of section
6928(d)(2)(A)" — and Part IV repeats the confinement. Carrying it as "the Third Circuit's rule" on
knowledge of a legal requirement, unqualified, is broader than the opinion.

### The pincite, and a third copy the shelf did not know it had

**669 remains unconfirmed, and the reason is not the one the row gives.** Three copies are held:

| Copy | Pagination |
|---|---|
| law.resource.org reporter capture | none — continuous text, paragraph-numbered |
| FindLaw capture | none — the reporter pages are absent |
| OpenJuris capture, filed as `_second-copy` | **star pagination, `*664`** — and one page only, "Page 1 of 1" |

**The only copy on the shelf that carries star pagination is a one-page capture that stops five pages
short of the pincite.** Under [E47](#e47--three-page-numbers-from-a-source-that-has-no-page-numbers-caught-before-publication)
669 stays the secondary source's and the ⚠ stays with it.

**And the filename is the finding.** `_second-copy` says nothing about what distinguishes this copy
from the other two — that it is a truncated single page, and that it is the only one with real
pagination. `CLAUDE.md` records that a filename is a claim written by the same process that writes
the claims it warns about, and that nothing checks them. **This one understated a capability and
concealed a truncation in the same word.**

### The rule

**E66 — a holding that states a requirement and then states how it may be satisfied is one holding.**
Quoting the requirement and stopping is not an elision of detail; it reverses the balance the court
struck, because the second clause exists to answer the objection the first clause invites.

This is [E64](#e64--a-view-the-supreme-court-declines-to-adopt-published-as-the-rule-it-adopted)'s
neighbour rather than its repeat. E64 is a court stating a proposition **in order to reject it**.
Here the court states the rule and means it — **and qualifies it in the following breath**, so the
quotation is accurate, the attribution is correct, and the reader is still misled about what the case
does. **Reading the sentence after is not only a test for whether the court believed it.**

## E67 — *Bank of New England* misdated by three years, and its most-quoted sentence belongs to a district court in West Virginia

**Status: published in `standards/what_these_words_mean.md`, `docs/known_objections.md` and
`standards/table_of_authorities.md`. Corrected on reading the opinion, 26 August 2026.**

**What was published**, in the glossary and in the same form in the other two files:

> *United States v. Bank of New England, N.A.*, 821 F.2d 844, 856 (1st Cir. **1984**): "a corporation
> cannot plead innocence by asserting that the information obtained by several employees was not
> acquired by any one individual who then would have comprehended its full import. Rather the
> corporation is considered to have acquired the collective knowledge of its employees and is held
> responsible for their failure to act accordingly."

### Three things are wrong with that, and the quotation is not one of them

**First, the year.** The opinion was **argued March 4, 1987 and decided June 10, 1987**. It is
821 F.2d 844 (1st Cir. **1987**). The library filename has carried 1987 since the file arrived; three
published files carried 1984. The date most likely migrated from the conduct — the charged
transactions run from May 1983 to July 1984 — and no one asked which was which.

**Second, and this is the substance: the sentence is not the First Circuit's.** It is a block
quotation, and the line immediately following it in the opinion gives the source:

> "*United States v. T.I.M.E.-D.C., Inc.*, 381 F. Supp. at 738."

The words are those of the **United States District Court for the Southern District of West
Virginia**, 1974, quoted with approval by the First Circuit. This project published a district
court's sentence as a court of appeals holding, in a glossary entry defining the doctrine.

**Third, "at 856" cannot be checked.** The copy held is a law.resource.org capture with no star
pagination, as its filename says. Under [E47](#e47--three-page-numbers-from-a-source-that-has-no-page-numbers-caught-before-publication)
the pincite stays the secondary source's and the ⚠ stays with it.

### What the First Circuit does say in its own words, which is stronger than what was quoted

> "A collective knowledge instruction is entirely appropriate in the context of corporate criminal
> liability. … Corporations compartmentalize knowledge, subdividing the elements of specific duties
> and operations into smaller components. The aggregate of those components constitutes the
> corporation's knowledge of a particular operation."

And, upholding the charge: "Since the Bank had the compartmentalized structure common to all large
corporations, the court's collective knowledge instruction was not only proper but **necessary**."

**The instruction the court approved is quoted in the opinion and this project has never carried it:**

> "In addition, however, you have to look at the bank as an institution. As such, its knowledge is
> the sum of the knowledge of all of the employees. … So, if Employee A knows one facet of the
> currency reporting requirement, B knows another facet of it, and C a third facet of it, the bank
> knows them all."

### The tension this was expected to expose is not there, and a different one is

The question put to this case was whether a broadly stated collective-knowledge doctrine sits badly
with SEC. 4, which locates authority in one natural person. **It does not, and the reason is in the
first line the court wrote about it.** Collective knowledge is a rule of **corporate** criminal
liability: knowledge of employees "is **imputed to the corporation**," and the aggregate "constitutes
**the corporation's** knowledge." The doctrine has no operation against a natural person, and no
case cited in the string supporting it aggregates the knowledge of several people onto one defendant.

**So `docs/known_objections.md` and the glossary both overstate the Act's own modesty.** They say the
Act "declines to aggregate", which reads as a choice to give up an available tool. **The tool was
never available against an individual.** The Act is not declining collective knowledge; it is
operating in the register where the doctrine does not reach. That is a smaller claim and a true one,
and it survives a reader who knows the case.

### And a theory in the same instruction that the repository has never mentioned

The trial judge gave the jury a **second** route to willfulness, which the First Circuit also upheld:

> "the bank as an institution has certain responsibilities … you will have to determine whether the
> bank as an organization **consciously avoided learning about and observing** CTR requirements. The
> Government to prove the bank guilty on this theory, has to show that its failure to file was the
> result of some **flagrant organizational indifference**."

**That is willful blindness at the level of the organization**, with the jury directed to weigh "the
bank's effort, if any, to inform its employees of the law; its effort to check on their compliance;
its response to various bits of information", and its policies against "how it carried out its stated
policies." It is the entity-level analogue of what SEC. 6(b) does to a person, it is approved
appellate authority, and this repository has cited *Bank of New England* five times without it.

### The rule

**E67 — a quotation inside a block quote belongs to whoever the citation under it names.** An
appellate court quoting a district court with approval makes that sentence persuasive, not its own,
and the difference is the difference between a First Circuit holding and a 1974 district court in
West Virginia. **Where a quotation is followed by a bare citation rather than by more of the court's
prose, that citation is the attribution.**

**And the smaller rule, which cost less but recurs.** A case's date is a fact about the opinion, not
about the conduct. **Where a published year sits inside the span of years the facts cover, check
it** — 1984 was in the indictment, and that is exactly why it looked right.

## E68 — *Caremark* can settle its own pincite after all, and the sentence before the famous one answers the objection the famous one was raising

**Status: the pincite question is resolved in the repository's favour; two elisions and one
characterization are corrected. Read 26 August 2026.**

### The provenance caveat was right about the document and wrong about the pagination

`standards/table_of_authorities.md` and `research/verification_record.md` both said of the copy held
— a Thomson Reuters/Westlaw reprint with KeyCite headers, hosted by Penn Carey Law — that "**whether
it may confirm 971 is a question for whoever reads it**."

**It confirms it.** The reprint carries star pagination throughout, `*960` to `*972`, and the
oversight passage falls between the `*971` and `*972` markers. **971 is confirmed from the copy on
the shelf.**

**The distinction worth keeping.** "Not an official court print" is a claim about whose text this is
— the reprint is Thomson Reuters' rendering, not the Atlantic Reporter's own — and it remains true.
It is not a claim about whether page boundaries are marked, and the filename's caveat was read as
though it were both. **A provenance limit and a pagination limit are separate properties of a copy**,
and this shelf has been treating "unofficial" as implying "unpaginated" since the file arrived.

### The quotation is verbatim, and two things were dropped from it

`standards/what_these_words_mean.md` carries it exactly as the opinion has it. **The opinion opens
the clause with three words this project drops without an ellipsis:**

> "Generally where a claim of directorial liability for corporate loss is predicated upon ignorance
> of liability creating activities within the corporation, as in *Graham* or in this case, **in my
> opinion** only a sustained or systematic failure of the board to exercise oversight . . . ."

**"In my opinion" is Chancellor Allen marking the standard as his own view**, in the paragraph that
became the most-cited passage in Delaware oversight law. Under [E48](#e48--a-published-quotation-with-two-words-the-court-did-not-write-and-both-were-ours)
an elision is an edit, and this one removes the author's own hedge from a sentence this project
offers as settled doctrine.

**And the standard is confined, in the same sentence, to the branch of the case it decides** — claims
"predicated upon **ignorance** of liability creating activities". It is not a general standard for
director oversight, and both files present it as one.

### The reservation two sentences earlier, which the objection never had to survive

`docs/known_objections.md` builds the corporate-law objection on this passage: Delaware "set the bar
high on purpose", so a state criminalizing the same conduct at a lower threshold "has overridden a
considered judgment about how much protection a decision-maker needs."

**Chancellor Allen expressly declines to decide the case this Act is about.** At 971, in the
paragraph immediately preceding:

> "Thus, this case presents no occasion to apply a principle to the effect that **knowingly causing
> the corporation to violate a criminal statute** constitutes a breach of a director's fiduciary
> duty. See *Roth v. Robertson*, 64 Misc. 343, 118 N.Y.S. 351 (N.Y. Sup. Ct. 1909); *Miller v.
> American Tel. & Tel. Co.*, 507 F.2d 759 (3d Cir. 1974)."

**The considered judgment Delaware made was about ignorance. It was not made about knowing
violation, and the court said so while making it** — and cited two authorities going the other way
on the reserved question. SEC. 6(b) is a knowing-conduct offense. **The objection, at the strength
this page gives it, does not reach SEC. 6(b) at all**, and the answer has been sitting two sentences
above the quotation since the objection was written.

That does not dispose of the objection against **SEC. 6(a)**, whose floor is a failure of due care
and which really does sit below the *Caremark* bar. The page should make that division rather than
answering for the whole Act.

### The rule

**E68 — a caveat in a filename names one limit, and a reader will generalize it to every limit that
sounds like it.** "Not an official print" was allowed to mean "cannot settle a page" for as long as
the file sat unopened. **Check the property you actually need against the document, because the
label warns about a different one.**

**And the reservation is part of the holding.** [E64](#e64--a-view-the-supreme-court-declines-to-adopt-published-as-the-rule-it-adopted)
covers a proposition a court states in order to reject it. This is a court stating what it is **not**
deciding, next to what it is — and the sentence a project quotes is worth less than the sentence
saying which cases it governs.

## E69 — the instrument built to prevent E60 could not see the shelf, and said so in a line nobody read

**Status: found and fixed 26 August 2026, while running the checkers before a hand-off. Nothing was
published wrong; the guarantee simply was not running.**

**What happened.** `check_quotations.py`, written this afternoon in answer to
[E60](#e60--the-registers-most-cited-fabrication-finding-was-itself-wrong-and-a-real-quotation-was-deleted-on-the-strength-of-it),
resolves the shelf from a single hardcoded path:

> `LIB = os.path.expanduser("~/mnt/faap/library/_text")`

**`~/mnt` does not exist on this machine.** The library is at `../library/_text`. Every run of the
tool produced exactly one line —

> `*** SHELF NOT REACHABLE at /Users/kris/mnt/faap/library/_text — this run proves nothing ***`

— and exited. **No quotation was checked, and `--negatives` re-tested nothing.**

### Why this is worse than an ordinary broken script

`CLAUDE.md` records the guarantee this tool exists to provide: negative findings "are re-tested on
**every run** by `check_quotations.py --negatives`", because "a false positive is caught by the next
reader; **a false negative is caught by nothing.**" That re-test is the only mechanism standing
behind a deleted sentence. **It has not run since the tool was written.**

**The banner was honest and that is the whole problem.** The tool did not claim a clean pass — it
said in terms that the run proved nothing, which is the correct behaviour and the reason this entry
records no wrong publication. **An honest failure message is still a silent failure if the number it
replaces is the number anyone looks at.** `CLAUDE.md` warns that "a silent skip and a clean pass look
identical in output". This is the neighbouring case: **a loud skip and a clean pass look different,
and are read the same**, because both end the run without a complaint to act on.

### The fix, and what it now shows

The path resolves against three candidates in order — the maintainer's device mount, `../library`
beside the repository, and a local working copy — taking the first that exists, and falling back to
the mount so the existing banner still fires when none does. The post-mortem is in the file, per the
standing rule that these scripts carry their defects beside them.

**First real run: 245 shelf files, 1,108 published quotations of 60 characters or more, 100 found on
the shelf.** The three recorded negative findings all re-test as **confirmed present**, which is what
[E62](#e62--the-third-fabrication-was-a-misattribution-and-the-instrument-built-to-catch-this-found-it-on-its-first-run)
established by hand and nothing had re-established since.

**One shelf file has no extractable text** — `BILL_CO-SB25B-004_signed-act_2025-08.txt` — so a miss
against that source means nothing at all, and the tool now says so on every run.

### The rule

**E69 — a tool that reports its own failure has not thereby reported it to anyone.** Before relying
on a checker's guarantee, run it once and confirm it can reach what it checks. **A guarantee that
depends on a path is a guarantee about a machine**, and this repository is worked on from more than
one.

**And the caution it repeats.** `CLAUDE.local.md` records that tool-building is where this assistant
over-produces, and that several of 26 August's errata were caused by checkers written that same
afternoon. **This is the fourth.** The instrument was correct in design, complete in its reasoning
about false negatives, and pointed at a directory that was not there.

## E70 — *Cedar Point*'s "sine qua non" is a law professor's phrase in a *see also* parenthetical, and the case says nothing about intangible property

**Status: published in `docs/known_objections.md` and `standards/table_of_authorities.md`. Corrected
on reading the opinion, 26 August 2026.**

**What was published**, in the takings objection stated at its strongest:

> "the right to exclude is the 'sine qua non' of the property interest (*Cedar Point Nursery v.
> Hassid*, 594 U.S. 139, 150 (2021))."

**Read in the opinion, the phrase is there and it is not the Court's.** It appears once, at the end
of a string citation, in the weakest signal the Bluebook has:

> "*see also* Merrill, *Property and the Right to Exclude*, 77 Neb. L. Rev. 730 (1998) (**calling**
> the right to exclude the 'sine qua non' of property)."

**A parenthetical characterizing an academic article is not a holding, and "calling" is the
Court's own word for what Merrill does with it.** The table row carried it as the proposition the
case is cited for.

**The Court's own words for the same idea, in the same paragraph, are weaker and are themselves
quotations:** the right to exclude is "universally held to be a fundamental element of the property
right" and "one of the most essential sticks in the bundle of rights that are commonly characterized
as property" — both quoted from *Kaiser Aetna v. United States*, 444 U.S. 164, 176, 179–180 (1979).
**The pincite this project needs is to *Kaiser Aetna*, and the sentence it wants is forty-two years
older than the case it credited.**

### The per se limb, verbatim, and it is narrower than the objection assumed

> "The essential question is not, as the Ninth Circuit seemed to think, whether the government action
> at issue comes garbed as a regulation (or statute, or ordinance, or miscellaneous decree). It is
> whether the government has **physically taken property** for itself or someone else—by whatever
> means—or has instead **restricted a property owner's ability to use his own property**. . . .
> Whenever a regulation results in a **physical appropriation** of property, a per se taking has
> occurred, and *Penn Central* has no place."

**The dividing line is physical appropriation against restriction on use, and it is stated as the
essential question.** *Cedar Point* concerns a right to "physically enter and occupy the growers'
land for three hours per day, 120 days per year."

### What the case does not contain, which is the finding

**The words "trade secret" and "intangible" do not appear in the opinion. Neither does
*Ruckelshaus*.** *Cedar Point* is about physical entry onto land, and its companion authority
*Horne* is about raisins — tangible personal property physically set aside for the government.

`docs/known_objections.md` builds the objection by pairing *Ruckelshaus* (trade secrets are property)
with *Cedar Point* (the right to exclude is the property itself), and then reasons at point **Two**
that "the per se limb may not care about publication at all", so "a compelled handover to the State
is a handover whether or not the State prints it."

**That step needs a bridge *Cedar Point* does not build.** Extending a per se physical-appropriation
rule from occupying land to compelling the production of records is the whole of the argument, and
the case cited for it never reaches intangible property, never cites the case that does, and frames
its own rule around whether property was **physically** taken. The objection may still be good — but
it is good on *Ruckelshaus* and on an extension nobody has briefed here, not on *Cedar Point*.

**The prediction in the reading brief was right and this is the second instance.** The takings
section was built reading *Ruckelshaus* and *Cedar Point* through the xAI plaintiff's brief.
*Ruckelshaus* was read and came out narrower and more favourable to this Act than the brief implied.
So does this.

### The pincite cannot be settled, and the second copy is a label

**Two copies are held and neither carries U.S. Reports pagination.** The supremecourt.gov slip
opinion carries slip pages, as its filename says. **The second copy — filed as
`594-US-139_2021_Justia` — carries no internal reporter pagination at all**, only the print pagination
of the capture ("Page 22 of 26"). The reporter citation lives in the filename and the URL.

Under [E58](#e58--a-citation-that-exists-only-in-a-url-and-a-page-title-is-not-a-citation-and-it-nearly-overwrote-a-correct-one)
a citation that exists only in a URL or a filename is a label, not a citation. **This filename
promises reporter pagination and delivers none**, and it was the more promising of the two copies on
its name alone. **150 stays the plaintiff's brief's pincite** ([E47](#e47--three-page-numbers-from-a-source-that-has-no-page-numbers-caught-before-publication)).

### The rule

**E70 — a citation signal is part of the citation.** *See also* introducing a parenthetical that
reports what an academic "call[s]" something is the furthest a court can stand from adopting a
phrase while still printing it. **Before attributing a quoted phrase to a court, find what
introduces it**, and if the answer is a signal rather than the court's own sentence, the phrase
belongs to whoever the citation names.

**And the corollary this project keeps meeting.** [E67](#e67--bank-of-new-england-misdated-by-three-years-and-its-most-quoted-sentence-belongs-to-a-district-court-in-west-virginia)
found a district court's sentence published as a court of appeals'. This finds a law review's phrase
published as the Supreme Court's. **Both arrived the same way: from a source quoting the case rather
than from the case**, and in both the real author was named on the page all along.

## E71 — which *Walton* opinion is 294 A.3d 65 cannot be settled from the shelf, and the only source that answered it is one E59 already discredited

**Status: the question E59 opened is examined and stays open. Recorded because "still open" is a
finding when the reason is known, and because one source that looked like an answer is not one.**

**The question, narrowly.** C.A. No. 2021-0827-JTL produced two opinions two weeks apart
([E59](#e59--two-opinions-two-weeks-apart-under-one-case-number-and-a-date-i-confirmed-from-three-sources-that-the-document-contradicts)).
This repository cites *Walton* as **294 A.3d 65, 90, 92**. Which opinion carries that citation?

**Both are on the shelf and read. Neither answers it.**

| | Laches opinion | Demand-futility opinion |
|---|---|---|
| Caption | "OPINION ADDRESSING DEFENDANTS' MOTION TO DISMISS ON THE BASIS OF LACHES" | "MEMORANDUM OPINION" |
| Submitted | 13 January 2023 | 13 January 2023 |
| Decided | **12 April 2023** | **26 April 2023** |
| Last slip page | 62 | 121 |

**Neither PDF carries an Atlantic Reporter stamp anywhere**, which is ordinary — a slip opinion is
published before the reporter citation exists. **The shelf cannot settle this**, and no further
reading of these two documents will change that.

### The source that appeared to answer it, and why it does not

`research/verification_record.md` carries a **◐ model-mediated** row asserting: "Laster V.C.,
26 Apr. 2023, C.A. 2021-0827-JTL, **58 pp.**, reported **294 A.3d 65**."

**That row is wrong about the page count in a way that is checkable, and it is now checked.** The
26 April opinion runs to slip page **121**, not 58. E59 already recorded that "two separate
model-mediated fetches" reported 56 or 58 pages for a document that has 64. **This is the same
family of fetch, wrong by the same margin, and its reporter citation carries exactly the credibility
of its page count.** Under [E57](#e57--a-new-provenance-grade-because-three-sources-arrived-by-a-route-this-register-had-no-name-for)
a model-mediated fetch is a lead, not a reading, and this one has now failed the only part of itself
that could be tested.

### What reading the two opinions did establish

**The 26 April opinion cites the 12 April opinion, and does it by Westlaw number:**

> "*Ontario Provincial Council of Carpenters' Pension Tr. Fund v. Walton* (**Walmart Laches**),
> **2023 WL 2904946**, at \*18 (Del. Ch. Apr. 12, 2023)."

Two things follow. **As of 26 April 2023 the laches opinion had no Atlantic Reporter citation to give**
— which is consistent with either eventually taking 294 A.3d 65 and settles nothing between them.

**And the court supplies the short form this repository needs.** Vice Chancellor Laster calls the
earlier one ***Walmart Laches***, and relies on it at \*18 and \*21 of the later one. E59's rule is
that a case number is not a document; **the court had already solved the naming problem**, and
adopting *Walmart Laches* for the April 12 opinion and *Walmart Demand Futility* for the April 26
opinion makes the collision hard to repeat.

### The temptation that was declined, and it is E47's

The published pincites are 90 and 92; the confirmed quotations sit at slip op. 76 and 77–78 of the
26 April opinion. **A ratio can be computed from those numbers that makes 90 and 92 look right**, and
a 62-page laches opinion beginning at 65 would end well before 90, which makes the answer look
obvious.

**That reasoning is not permitted here and would not be worth much if it were.** E47's rule is that a
page produced by a process is not a page read from a document, and its second-order rule is that the
most persuasive form an invention takes is one that agrees with the arithmetic. **The pincites 90 and
92 come from the same secondary source whose account of this case has now been wrong three times**;
using them to identify the opinion and then reporting them as confirmed against it would be circular.

### What would settle it

**One look at 294 A.3d 65 in the Atlantic Reporter**, or any reporter-paginated copy of either
opinion. Until then the row keeps its ⚠ on 90 and 92, the citation stays as published with its source
named, and **neither opinion may be described as "the" reported one**.

### The rule

**E71 — when a source is shown wrong on a fact that can be checked, its other facts do not survive
on their own.** The ◐ row was believed for its reporter citation while being disbelieved for its page
count, and those arrived together from one fetch. **A retrieval is credited or discredited whole**,
unless some part of it has been independently confirmed.

## E72 — the "no-fault" claim at n.18 is good, the authority for it is now read, and the "split" attached to it is the law firm's word and not the court's

**Status: a debt paid rather than an error published. One characterization in
`standards/table_of_authorities.md` is corrected. Read 26 August 2026.**

**What was owed.** `model_act_v3_4_companion.md` n.18 asserts that the clawback "keeps
Sarbanes-Oxley § 304's **no-fault** severity". The table row recorded that this was
"[t]he appellate authority this project's 'no-fault clawback' characterization rests on and does not
cite", known only from a law-firm alert, and that the claim "remains uncited until someone reads it."

**It is read, and the claim holds.** *SEC v. Jensen*, 835 F.3d 1100 (9th Cir. 2016), holding
verbatim:

> "In accordance with its text and legislative history, we hold that SOX 304 allows the SEC to seek
> disgorgement from CEOs and CFOs **even if the triggering restatement did not result from misconduct
> on the part of those officers**."

The reasoning is textual and the court states it plainly: the clause "as a result of misconduct"
modifies "the material noncompliance of **the issuer**", so "it is the issuer's misconduct that
matters, and not the personal misconduct of the CEO or CFO." The court adds that Congress "knew how
to draft a statute that would limit the disgorgement remedy to cases of officer or director
misconduct, and chose not to do so", contrasting the enacted text with a rejected House version.

**First in the courts of appeals, in the court's own words:** "While we are aware of no circuit court
that has addressed this issue, most district courts to have examined it have concluded that SOX 304
does not require CEOs or CFOs to have personally engaged in misconduct."

### The one thing the row had wrong

The row reports that "**district courts had split for fourteen years**."

**The opinion describes no split.** It says "**most** district courts to have examined it have
concluded" against a personal-misconduct requirement, and the string it gives runs one way —
*Jenkins* (D. Ariz. 2010), *Baker* (W.D. Tex. 2012), *Geswein* (N.D. Ohio 2011), *Life Partners
Holdings* (W.D. Tex. 2014). **No contrary district decision is cited anywhere in the discussion.**
"Split" came from the law-firm alert, and this project reproduced it as though it were the court's
account of the landscape.

That matters more than it looks. **A holding that resolves a split and a holding that ratifies a
settled district consensus carry different weight**, and the second is what happened here.

### What the copy can and cannot do

**The pincite cannot be settled.** The copy is the Ninth Circuit's own PDF, and its page markers are
the **slip** pages of that issue (26, 27, 28, 29 through the SOX 304 discussion). **No F.3d page
appears anywhere in the document**, so 835 F.3d 1100 and any pincite into it stay the secondary
source's under [E47](#e47--three-page-numbers-from-a-source-that-has-no-page-numbers-caught-before-publication).

**And the disambiguation the row recorded in advance held up.** This is not the *Jensen* at n.22 —
the DOJ food-safety prosecution in D. Colo. Two cases, one surname, opposite subjects.

### The rule

**E72 — a secondary source's account of the *landscape* is a claim, and a separate one from its
account of the holding.** The alert was right that *Jensen* is first in the circuits and right about
what it held. It was wrong that the district courts were split, and that word travelled into this
repository attached to two facts that were true. **Check the background characterization against the
opinion's own description of the authorities, which is usually a paragraph away from the holding.**

## E73 — *Jewell* and *Cincotta* confirmed verbatim, the footnote number settled where the page cannot be, and *Cincotta*'s next sentence widens what this project cites it for narrowing

**Status: two debts paid, one characterization corrected. Read 26 August 2026.**

### *United States v. Jewell*, 532 F.2d 697 (9th Cir. 1976) (en banc)

**The glossary's quotation is verbatim**, and it is the court's own recapitulation:

> "In the language of the instruction in this case, the government must prove, 'beyond a reasonable
> doubt, that if the defendant was not actually aware . . . his ignorance in that regard was solely
> and entirely a result of . . . a conscious purpose to avoid learning the truth.'"

**The words are the trial court's instruction**, set out at length earlier in the opinion and adopted
by the en banc court as the standard. The glossary calls this "the classic formulation is *United
States v. Jewell*", which is right about whose standard it became and imprecise about whose sentence
it is. **The bracketed "[of the crime]" the glossary inserts stands in for the instruction's actual
words** — "that there was marijuana in the vehicle he was driving when he entered the United States"
— and the brackets disclose the substitution, which is what [E48](#e48--a-published-quotation-with-two-words-the-court-did-not-write-and-both-were-ours)
requires.

**704 stays unconfirmed.** The copy is a law.resource.org capture with no star pagination, as its
filename says ([E47](#e47--three-page-numbers-from-a-source-that-has-no-page-numbers-caught-before-publication)).
**A lead, recorded as one:** *Cincotta* cites this discussion as "*United States v. Jewell*, 532 F.2d
697, **699–704**", which puts 704 inside the range a first-order source assigns to it. That is
corroboration from another opinion, not a page read from this one, and it does not retire the ⚠.

**And the two authorities in this glossary entry share a source, which the entry does not say.**
*Jewell* quotes Glanville Williams — "A court can properly find wilful blindness only where it can
almost be said that the defendant actually knew" — and that is the same sentence *Global-Tech* quotes
at 770 to fix willful blindness above recklessness. The Supreme Court's ceiling and the Ninth
Circuit's origin rest on one line of a 1961 textbook.

### *United States v. Cincotta*, 689 F.2d 238 (1st Cir. 1982)

**The quotation is verbatim**, and **the footnote number is confirmed even though the page is not.**
In the capture held the passage sits in the numbered note beginning "**2**", between the note
quoting the indictment and note 3. **"n.2" is settled; "243" is not**, the copy carrying no star
pagination.

**What the glossary omits is the sentence immediately after, and it runs the other way.** The
glossary offers *Cincotta* as a narrowing of *Jewell* — "**Narrowed in** *United States v.
Cincotta*" — on the strength of "The conscious avoidance principle means **only** that specific
knowledge may be inferred when a person knows other facts that would induce most people to acquire
the specific knowledge in question."

**The court continues:**

> "Thus, if someone refuses to investigate an issue that cries out for investigation, **we may
> presume that he already 'knows' the answer** an investigation would reveal, whether or not he is
> 'certain'."

**A presumption of knowledge from a refusal to investigate is wider than the sentence quoted, not
narrower**, and it is the operative half for a prosecutor. The "only" limits what conscious avoidance
*is* — circumstantial evidence of knowledge rather than a substitute for it, as the note goes on to
say — and it does not limit how far the inference reaches.

**Which compounds a correction already made.** [E65](#e65--global-tech-called-a-constitutional-ceiling-in-three-files-and-it-decides-no-constitutional-question)
records that this glossary entry reads as a descent from broad to narrow — *Jewell*, then *Cincotta*
"narrowed", then *Global-Tech* as the ceiling — and that the sequence is backwards, because
*Cincotta*'s "would induce most people" is an **objective** test while *Global-Tech* requires a
**subjective** belief in a high probability plus deliberate avoidance. **This entry adds that
*Cincotta* is not a narrowing of *Jewell* either.** The word "Narrowed" was doing work no authority
in the entry supports.

### The rule

**E73 — where a page cannot be confirmed, check whether some other coordinate in the citation can
be.** A footnote number, a part heading, a paragraph number and a docket entry are all locators, and
a source without star pagination may still fix three of them. **"Unconfirmable" is a property of the
page, not of the whole pincite**, and this repository has been retiring the entire locator whenever
the page failed.

## E74 — *Liu* confirmed as n.18 states it, and read beside *Jensen* it puts a question to the sentence next to it

**Status: a debt paid; one assumption in n.18 identified as an assumption. Read 26 August 2026.**

**n.18 states** that "*Liu v. SEC*, 591 U.S. 71 (2020), confined equitable disgorgement to net
profits applied for victims — a statutory clawback is not so confined, but the section adopts *Liu*'s
destination logic by choice (restitution first, fund second)."

**The first clause is exact.** The holding, verbatim:

> "The Court holds today that a disgorgement award that does not exceed a wrongdoer's net profits and
> is awarded for victims is **equitable relief** permissible under §78u(d)(5)."

And the rationale: "to avoid transforming an equitable remedy into a punitive sanction, courts
restricted the remedy to an individual wrongdoer's net profits to be awarded for victims."

### The assumption, which reading *Jensen* the same day exposed

n.18's second clause — "**a statutory clawback is not so confined**" — is offered without authority
and is doing real work: it is what lets SEC. 7 keep *Liu*'s destination logic as a **choice** rather
than a constraint.

**But *Liu*'s limit attaches to relief that is equitable, and the Ninth Circuit calls SOX 304's
reimbursement provision exactly that.** In the same opinion this project read today to confirm n.18's
"no-fault" claim:

> "This is consistent with our conclusion elsewhere that **the reimbursement provision is an
> equitable and not a legal remedy**." *SEC v. Jensen*, citing *SEC v. Jasper*, 678 F.3d 1116, 1130
> (9th Cir. 2012).

**So the one statutory clawback in American law that this section is modelled on has been
characterized by a court of appeals as equitable**, and *Liu* confines equitable disgorgement to net
profits for victims. Whether *Liu*'s ceiling reaches a statutory clawback that a court has called
equitable is a live question, and n.18 answers it in a subordinate clause.

**This is not a finding that n.18 is wrong.** *Liu* construes §78u(d)(5) specifically, SOX 304 is a
different statute with its own text, and *Jensen*'s characterization was made for a different purpose.
**It is a finding that the clause is an argument rather than a given**, and that the two authorities
n.18 cites in the same breath pull against each other in a way nobody here had noticed because they
had not been read together.

**The practical consequence is small and worth stating**, because it cuts the way the section already
goes: SEC. 7 adopting restitution-first "by choice" reaches the same destination *Liu* would compel
if the ceiling does apply. **The design is safe; the reasoning offered for it is not the reasoning
that makes it safe.**

### Pagination

⚠ **The copy is the supremecourt.gov slip opinion and it says so on every page** — "Cite as: 591
U. S. ____ (2020)", the blank being the tell. No U.S. Reports pincite can be taken from it
([E47](#e47--three-page-numbers-from-a-source-that-has-no-page-numbers-caught-before-publication)).
The filename is accurate.

### The rule

**E74 — two authorities cited in one sentence have to be read against each other, not only against
the sentence.** n.18 cites *Liu* and relies on SOX 304, and the proposition joining them — that a
statutory clawback escapes *Liu*'s ceiling — survived because the two were verified separately and
never set side by side. **Where a note cites more than one case, ask what each says about the other.**

## E75 — the last six of the sixteen, read: five confirm what was published, and *National Pork Producers* did not remove a rule that never existed

**Status: five debts paid with no correction owed; one characterization corrected. Read 26 August
2026.**

### *Veeck v. Southern Building Code Congress Int'l*, 293 F.3d 791 (5th Cir. 2002) (en banc)

**`docs/questions.md` states it accurately** — "model codes enacted into law enter the public domain
as law" — and the court's own summary is the source of that phrasing: "as law, the model codes enter
the public domain and are not subject to the copyright holder's exclusive prerogatives."

**The clause after it is the one this project should carry, because it is about this project.** The
same sentence continues: "**As model codes, however, the organization's works retain their protected
status.**" *Veeck* is a two-sided holding. **An unenacted model act is not in the public domain under
it**, and this Act has been enacted nowhere.

So *Veeck* is not authority that this Act "is CC0", as the table row's cited-for column has it. **The
CC0 dedication is a choice**, and *Veeck* tells you what happens after a legislature acts, not
before. The choice is prudent on *Veeck*'s reasoning — the text goes into the public domain the
moment anyone enacts it, so reserving rights buys a right that expires on success. **That is a good
argument and it is not the argument the row makes.**

⚠ **No star pagination**, as the filename says; nothing may be pincited to it.

### *Kentucky v. Dennison*, 65 U.S. (24 How.) 66 (Dec. Term 1860)

**The quotation in `audit/record.md` is verbatim in the Library of Congress print**, allowing for a
scan whose OCR renders "offences" as "o[lYnces" in the same line:

> "The word 'crime' of itself includes every offence, from the highest to the lowest in the grade of
> offences, and includes what are called 'misdemeanors,' as well as treason and felony."

**And the overruling note is precisely right.** The syllabus separates the two holdings the way this
repository does: point 4 gives the scope of "treason, felony, or other crime", while points 8 and 9
are the mandamus holding — "Congress cannot coerce a State officer, as such, to perform any duty"
and "upon that ground only, this motion for a mandamus was overruled." **It is points 8 and 9 that
*Puerto Rico v. Branstad*, 483 U.S. 219 (1987) overruled; the scope holding stands**, which is what
the record says and what the Act relies on.

**A note on this copy, recorded because the next reader will hit it.** The scan is genuinely
paginated, but the page numbers are OCR-damaged and irregular in the extracted text — markers jump
97 to 105 with the intermediate numbers lost to the running heads. **The passage's page was not
computed and is not published**, per [E47](#e47--three-page-numbers-from-a-source-that-has-no-page-numbers-caught-before-publication).
Nothing turns on it: `audit/record.md` cites the case without a pincite.

**A search that failed, recorded because it failed the way the manual says it will.** The first
`--find` for this quotation returned NO MATCH. The string was in the document. **The search omitted
the quotation marks around 'crime' that the reporter prints**, and the tool matched nothing. The
banner held — a miss is not a finding — and reading the file settled it in one command.

### *National Pork Producers Council v. Ross*, 598 U.S. 356 (2023)

**n.17 says the case "removed the almost-per-se rule against state laws with extraterritorial
practical effects".**

**The Court's position is that there was no such rule to remove.** Its words:

> "A close look at those cases reveals **nothing like** the 'almost per se' rule against laws that
> have the 'practical effect' of 'controlling' extraterritorial commerce that petitioners posit . . . .
> *Baldwin*, *Brown-Forman*, and *Healy* **did not mean to do so much**."

The rule is attributed throughout to the petitioners — "**Petitioners insist** that *Baldwin*,
*Brown-Forman*, and *Healy* taken together suggest an 'almost per se' rule" — and the Court declines
to find it in them, explaining that the highlighted language "appeared in a particular context and
did particular work."

**"Removed" and "declined to recognize" are different holdings, and the second is stronger for this
Act.** A rule abolished in 2023 invites the argument that it may be restored or narrowed. A rule the
Court says never existed leaves nothing to restore. **n.17 understated its own authority.**

The rest of n.17 checks out: the line is re-read as being about discrimination — laws that "hoard"
commerce "for the benefit of in-state merchants" — and what remains is *Pike*.

⚠ **Slip opinion: "Cite as: 598 U. S. ____".** No U.S. Reports pincite from this copy.

### *Sveen v. Melin*, 584 U.S. 811 (2018)

**The two-step Contract Clause test is verbatim**, and the threshold is as the record has it: whether
the state law has "operated as a substantial impairment of a contractual relationship", and "[i]f
such factors show a substantial impairment, the inquiry turns to whether the state law is" drawn
appropriately.

⚠ **Slip opinion: "Cite as: 584 U. S. ____".** ✅ **But 811 does not need this copy** —
`audit/record.md` records it confirmed against the preliminary print, "Volume 584 U.S. Part 2, Pages
811–836". **The table row's ⚠ said no U.S. Reports pincite was available and another file in this
repository already had the first page**, which is [E49](#e49--a-finding-the-repository-had-already-made-three-days-earlier-caught-at-the-door)'s
rule turned on the shelf: the register is part of the text, and so is the drafting record.

### *Trump v. Slaughter*, No. 25-332 (2026)

**The holding, verbatim: "If anything more is left of *Humphrey's*, we overrule it."** The Lawfare
commentary's account was right, including "the demise of *Humphrey's Executor*". What survives of the
1935 case is only "its observation that an agency that 'exercises no part of the executive power'
need not fall within the rule of Presidential removal."

**And the answer to the question the table row asked is that SEC. 3's Agency is untouched.** The
decision rests entirely on **Article II** and the President's removal power over federal officers.
**The phrase "state agency" does not appear in the opinion**, and no part of its reasoning reaches a
State's power to structure its own agencies, which is a matter for that State's own constitution.

**What is exposed is a rhetorical position, not a legal one.** SEC. 3 is designed on the
independent-commission model, and that model has just lost its federal exemplar. **A legislator who
asks "why build an independent commission when the Supreme Court has just dismantled the idea
federally" is asking a fair question with a good answer** — the answer being that the objection is
about Article II and a State is not subject to it. **That answer is not written anywhere in this
repository**, and the row was right that nobody had asked.

### Desai & Riedl, *Responsible AI Agents*, arXiv:2502.18359

**Verbatim, from the abstract:** "no matter how much AI Agents seem like human agents, they need not,
and should not, be given legal personhood status. In short, **humans are responsible for AI Agents'
actions**."

**And the liability-shield reasoning the row summarizes is in the text:** "Anthropomorphizing
software confuses issues and could lead to a world where software has legal personhood, related
rights, and **liability shields**. If that happens, the power for people to use software would grow
while also increasing the ability to avoid responsibility. That is the situation to avoid."

**The row's caution stands and is confirmed by the same page**: "Put simply, responsible AI Agents
are about responsible human action" — a premise this Act shares, reached by authors who prefer design
standards to personal criminal duties. **Ally on the premise, not the mechanism**, exactly as the row
says.

### The rule

**E75 — check whether the authority says a rule was abolished or says it never existed.** The two
read alike in a summary and differ in what they leave standing. **Where a court attributes a rule to
a party — "petitioners insist" — and then declines to find it, a project that reports the rule as
"removed" has credited the losing side's premise while citing the winning side's case.**

---

## Part II — What changed in the Act

**Between versions — 25 August 2026, eleventh batch: an eighty-year claim, corrected.** No change
to any tagged text.

[E42](./errata.md#e42--the-doctrine-was-said-never-to-have-left-food-and-drug-it-left-decades-ago-by-act-of-congress).
The front page said the responsible corporate officer doctrine had "never been extended past the
food-and-drug frontier." It was extended by Congress into the Clean Water Act, which defines
"person" to include "any responsible corporate officer" (33 U.S.C. § 1319(c)(6)), and in the twenty
years after *Park* the majority of prosecutions under the doctrine were environmental rather than
food-and-drug. Both facts sit in footnotes 32 and 33 of the Lyness article this project's entire
state-RCO argument rests on. The repository cited § 1319(c)(6) in four files and *Iverson* in three
and had never read either against its own Overview.

Corrected on all three pages that carried it. The glossary's entry for the doctrine now carries the
provision, the figure and the *Iverson* reasoning, so a reader who searches the doctrine lands on
the correction rather than on the claim.

*The replacement claim is narrower and better: the doctrine has moved once already, by act of
Congress, and has never reached software.*

⚠ *All three quotations are taken from Lyness's footnotes rather than from the Code and the
reporter. They are on the retrieval list and may not be described as verified until read.*

**Between versions — 25 August 2026, tenth batch: the commentary conformed to the instrument's own
spelling.** No change to any tagged text.

`model_act_v3_4.txt` is written in American spelling but for two words. The commentary around it had
drifted British across three months of drafting, so a reader searching this site for *defense
counsel*, *willful blindness*, *safe harbor* or *offense* found nothing, and a legislative counsel
comparing the companion against the instrument saw two conventions. **820 substitutions across 60 markdown
files**, plus the prose held inside the packet builders' own string literals — where a
markdown-only sweep would have been silently reverted the next time the five template-family
packets regenerated. Applied by a new checker, `check_spelling.py`, which is now part of the
repository's standing guard alongside `check_links.py`, `check_claims.py` and the library's
`check_emails.py`, and which is idempotent: a second pass changes nothing.

*The single largest correction is one word.* **`misdemeanour` appeared 48 times** and stayed
invisible to the first three passes of the tool, because the map held *demeanour* and the regex had
no way to see a prefix on it. An American criminal lawyer searches *misdemeanor*. So did the tool,
eventually.

*What the sweep would not touch, and why each rule exists.* Quotations keep their sources' spelling,
whether they sit in a blockquote or inside quotation marks on an ordinary line — AISI writes "push
models toward", and *toward/toward* is in the map, so masking quoted spans is what stops the tool
falsifying a source. Eleven such lines are listed in the script by file and phrase with the reason attached, in the same idiom as `check_links.py`'s allowlist: the UK DSIT and National Cyber Security
Center publication and its title, the quoted UK government accountability passage, the Health and
Safety at Work etc. Act 1974 s.37 text in the comparative note, and the census row that deliberately
carries *willful/willful* both ways. `audit/record.md` and `dossier/README.md` are skipped entire,
because each declares itself unalterable in its own opening lines and those rules bind this tool
too; every `BEGIN … content verbatim` block elsewhere is skipped the same way. Links pointing into
those sealed documents keep the sealed heading's spelling, or the anchor stops resolving.

*Two corrections fell out of it that are not cosmetic.* The frontier bill census rendered the
GAAIA's defined term as "Independent Verification **Organisation**"; the discussion draft says
**Organization**, and a defined term quoted with the wrong spelling is a misquoted defined term.
And `model_act_v3_4.txt` itself carries the only British spellings left standing: SEC. 6(b)(1)'s
"knowingly or **wilfully**" and SEC. 7(b)(5)'s "knowing or **wilful**". The instrument is tagged and
checksummed, so that is an amendment with a number rather than a sweep, and it is drafted and held.

⚠ *One integrity gap found and not fixed here, because a spelling sweep is the wrong instrument for
it.* `ledger/errata.md` and `ledger/diary.md` each open a `BEGIN … content verbatim` block that is
never closed — `ledger/changelog.md` closes its own at the right line, and the other two do not.
Everything appended since 19 August therefore sits inside a region the file declares verbatim.
Nothing has been altered; the marker needs an END at the true boundary, and finding that boundary
needs the merge record rather than a guess.


**Between versions — 25 August 2026, ninth batch: the question this project never asked.** No change
to any tagged text.

**Every offense in SEC. 6 turns on what a natural person knew, decided, or had the power to prevent.
Nothing in this repository asked what it takes to get that person into a chair.** The word
*deposition* returned **zero** across a hundred and two files. The apex-witness rule — courts
shielding senior executives from depositions absent unique, non-duplicative personal knowledge — is
the practical obstacle standing between a SEC. 6 charge and the officer's testimony, and it had
never been named here.

*There is one data point and it runs in this project's favor, which is exactly why it is stated
with its limits attached.* In ***Concord Music Group, Inc. v. Anthropic PBC***, No. 5:24-cv-03811
(N.D. Cal.), Magistrate Judge Susan van Keulen ordered on **19 December 2025** that **Dario Amodei
sit for a deposition**, capped at two and a half hours. Anthropic had argued he did not possess
unique knowledge of the company's model-training process; per the reporting, the court found that
his co-founders' own depositions established he was *"intimately involved"* and that they could not
supply what only he knew.

**What that establishes is the factual premise of SEC. 4, found by a court rather than asserted by
us:** the chief executive of a frontier developer held personal knowledge of how the models were
built that nobody else could give. **What it does not establish** is final authority to prevent or
halt, which is a different question; it is civil discovery, not criminal liability; and the finding
rested on what his co-founders said under oath, so a defendant with better-rehearsed subordinates
produces the opposite result.

⚠ **The order has not been retrieved.** Everything rests on secondary reporting, neither source
names the apex doctrine, and nothing may be cited to the court's own words until the docket entry
is in hand.

*Where it landed.* [The sweep](../audit/v3_5_lane_sweep.md) gains the gap in its enforcement
section, in the project's own words and against its own text; the enforcement packet regenerates
with it and takes a **fifth question**, which is the one the maintainer most wants answered — *do
the Act's SEC. 5 records duties do the work the apex rule otherwise makes a party do?*
[The table of authorities](../standards/table_of_authorities.md) carries the case as a candidate,
marked not citable until retrieved.


**Between versions — 25 August 2026, eighth batch: a letter became a subpoena, and then the
subpoena itself arrived.** No change to any tagged text. *This entry was first written from the
press release and rewritten the same day from the instrument.*

On **24 August 2026** the Attorney General of Alabama issued a subpoena to OpenAI over the July
evaluation escape, and the statute he reached for is the **Alabama Deceptive Trade Practices Act**.
Marshall was one of the fifteen attorneys general who signed the 3 August preservation demand this
repository already records, so this is the same office moving from asking a company to preserve to
compelling it to produce, **twenty-one days apart, over the same evaluation run**.

*The distinction this project exists to make, made.* The release is headed *"Investigation Into
OpenAI and Sam Altman"* and its operative sentence announces a subpoena "demanding that OpenAI, led
by Sam Altman, respond". **On what is public, that is a subpoena to the corporation and not to the
officer**, and [the enforcement record](../research/state_enforcement_record_2026.md) § 7 says so in
terms, contrasting it with Florida, which sued "Samuel Altman personally" and pleaded that he
personally directed the safety policies. Getting that difference wrong would have been
self-inflicted damage to the one argument this repository is making.

*Two sentences in the argument were overtaken and are now dated rather than quietly repaired.*
[The case](../docs/the_case.md) said in two places that a letter is not yet a subpoena. Both were
true when written. Both now carry what happened on 24 August, with the date, beside the original
sentence.

*And the ceiling campaign gets its answer from an unexpected direction.*
[Known objections](../docs/known_objections.md) gains Marshall's own words under the patchwork
section: a Republican attorney general putting innovation and global competitiveness in the same
sentence as the conclusion that **"states have to act"** — while having to improvise with consumer
protection law, because no AI statute in force reaches a model that escaped its evaluation. The
front page takes a fourteenth row.

*And then the document itself.* **Subpoena Duces Tecum #26-0007** is now held and read in full.
It is issued by the **Consumer Interest Division** to **OpenAI OpCo, LLC**, care of its general
counsel, under **§ 8-19-9 of the Code of Alabama** — confirming from the instrument what the release
only implied: **the letter of 3 August was addressed to "Sam Altman, CEO"; the subpoena is not
addressed to any natural person.**

*What it has to ask for is this repository's argument in somebody else's hand.* Request 1 compels
the identity of *"every employee, officer, and agent"* involved in the testing. Request 8 compels
the identity of everyone who *"raised any concern or complaint relating to the safety or security of
any model testing"*, and request 9 the documents behind it. Request 14 compels whatever
evaluation-safety policy existed, *"including materials relating to concerns about the lack of such
policies"*. **A state has to issue compulsory process to learn the names of the responsible people,
because no statute requires anyone to record them.** That is the production-burden gap the sweep's
enforcement lane identified and CURE 8 is drafted against, operating in the wild at the scale of a
state, and it is now sourced to a signed instrument rather than to reasoning.

*A trap recorded before anyone falls into it.* **There are two subpoenas to Sam Altman in
circulation.** Alabama's, of 24 August 2026, to the company. And a **witness** subpoena from the
**San Francisco Public Defender's Office**, served on him personally on stage in **November 2025**,
in the criminal trial of Stop AI activists — nothing to do with AI safety, consumer protection or
Alabama. Press captures of both arrived here on the same day in the same folder. The enforcement
record carries the distinction at § 7.5, the dated record carries a November 2025 row for it, and
the library filenames say DIFFERENT-MATTER. This project came within one draft of merging them.

⚠ **Two primaries the subpoena defines itself by are not held**: OpenAI's own blog post on the
incident and Hugging Face's technical timeline. Both are now first-priority retrievals, because a
state has pinned its own definition to them. An investigation is not a charge, a subpoena is not a
finding, and the return date was not legible in the copy held and is not asserted.


**Between versions — 25 August 2026, seventh batch: the project acquires a front door.** No change
to any tagged text.

*The problem.* Everything in this repository is written for somebody who has already decided to be
here. There was no page that answered, for a stranger with thirty seconds, the question *what is
this and how much of it is there.* Outreach was consequently underselling the work: an apologetic
paragraph cannot tell a cold recipient the difference between a crank with a document and eleven
months of drafting with an errata register.

*The page.* [The project in one page](../docs/abstract.md). The problem in two sentences; what the
project is; **what exists, counted**; the five findings the research produced that are not published
anywhere else; what a reviewer is asked for and what they get back; and, in its own section, what
this is not — not law, not introduced, no endorsement, and nobody may say it survived review until
named reviewers sign.

*And the numbers on it are enforced rather than asserted.* `check_claims.py` now recomputes the
abstract's document count, statute section count, errata count and all three cure-queue counts from
the files, and fails the build if the page and the truth disagree. Where a number only grows it is
stated as a floor, so it stays true between sweeps rather than going stale on the next commit. That
is the same rule the register applies to everything else: a count that appears in recruitment copy
is checked wherever it appears.

*Linked from* the front page's contents list and the map, so it is reachable rather than merely
present.


**Between versions — 25 August 2026, sixth batch: three more Senate hearings, and the New York bill
in full.** No change to any tagged text. All four documents arrived as direct downloads with intact
text layers, so unlike the second batch there is no decode and no OCR: everything below is
quote-in-hand.

*The one that matters most.* **S. Hrg. 119-255, *Hidden Harms*** (Senate Judiciary Subcommittee on
Privacy, Technology, and the Law, 9 September 2025) — two former researchers at a frontier developer,
under oath, on how their own safety findings stopped existing. The subject is child safety on
virtual-reality platforms and parts of that record are distressing; **this project's use of it is
structural, narrow, and says so at every point of use.** What it supplies is the mechanism, and the
mechanism is the argument for every records duty in this Act: a ninety-day deletion policy for raw
research data, which exists for good privacy reasons, means that **striking a line from a report is
enough to make the observation behind it unrecoverable**. Nobody destroys anything; the compliant
path and the destructive path are the same path. Carried at
[who has to tell you](../standards/who_has_to_tell_you.md) § 4d with its limits attached — sworn
allegation, not adjudicated fact, the company was not a witness, and the subject is not
frontier-model risk.

*The ceiling campaign, from the podium.* **S. Hrg. 119-284, *AI've Got a Plan*** (Senate Commerce,
10 September 2025) — the Director of the Office of Science and Technology Policy as sole witness,
saying that state preemption "is something we look at closely". [Known
objections](../docs/known_objections.md) gains the section, including the concession Kratsios made
inside his own answer — that patchwork compliance "gives more power to large technology companies
that have armies of lawyers" — which is taken seriously and answered rather than quoted
triumphantly.

*And the New York row closes.* The complete twelve-page print of **S 1169-B** replaced the
four-page capture, and the word test was rerun on all of it: *officer* returns one hit and it is
"committee or officer of the state"; *certification* returns one and it is a subject of regulation,
not a duty; *criminal*, *felony*, *misdemeanor*, *signature*, *senior personnel*, *frontier* and
*catastrophic* return nil. **The lineage count is unchanged: four drafts of a frontier-safety audit,
one survivor.** Three of its provisions are now carried anyway, because they are drafted answers to
questions this project is still asking: § 110's auditor-independence machinery, which goes further
on independence than the enacted Illinois text or California SB 53; § 109(4)'s statutory anonymous
internal disclosure channel with a monthly status duty, which is precisely the machinery whose
absence the *Hidden Harms* witnesses describe; and § 114(2), which reverses the causation
presumption at the pleading stage and then refuses to let a completed audit discharge it — a
warning aimed straight at this Act's own architecture, and now a question for the enforcement lane.

*Housekeeping.* The March 2026 Commerce hearing is **S. Hrg. 119-505**; the number was in a display
font that would not decode and is confirmed from the congress.gov landing page. Every hedge about it
is discharged. **S. Hrg. 119-171** (*AI-Generated Deepfakes*, 21 May 2025) is catalogued, contents
and witness list read, body unread, and nothing relies on it.


**Between versions — 25 August 2026, fifth batch: the first full repository sweep, and a new tool
to make it repeatable.** No change to any tagged text.

*The tool.* `check_links.py` at the repository root, stdlib only, deterministic, no network. It
walks every markdown file in the tree and reports three things: relative links whose target does
not exist, anchors whose target heading or explicit `id` does not exist, and markdown files
nothing links to. It models GitHub's duplicate-heading rule, so a second heading with the same
words resolves to `-1` as it does on the site, and it carries one allowlist entry with its reason
attached, because a tombstone that explains itself is not an orphan. It runs beside
`check_claims.py` and, like it, exits non-zero on a finding.

*What the first run found across 101 markdown files.* Three dead file links, two anchors that were
false positives until the duplicate-heading rule went in, and nine files reachable from nowhere.
All of it is fixed, and two of the findings were serious enough to number:
**[E40](./errata.md#e40--the-council-was-described-as-five-seats-after-it-had-grown-to-eight)** —
the front page and the dossier both described the review council as five seats, and the dossier
named the five, three days after the count went to eight. Three lanes did not appear at all, so a
person qualified for federalism, proportionality or torts and design was being told by recruitment
copy that there was no seat for them.
**[E41](./errata.md#e41--three-packets-linked-to-a-path-the-projects-own-checker-already-knew-was-dead)**
— three packets opened with a link to `packets/README.md`, which does not exist. The project
already knew: `check_emails.py` bans that exact string so it can never leave in an email. Nothing
was checking the repository itself, which is the whole reason the new tool exists.

*Two navigation defects fixed and recorded here rather than as errata, being omissions rather than
false statements.* The **eight audit chunks** were named in prose in the drafting record and linked
from nowhere, so nothing in the repository reached them by clicking; `audit/README.md` now indexes
all eight with a note saying why the index was added. And **`research/canon_check_2026-08-24.md`**
was missing from the map that claims to record which file owns which question; it now has its row,
carrying its own house rule that nothing on the examiner's bookshelf may be cited until it has been
retrieved and read.

*And the front page gains the quotation.* The record table takes a thirteenth row for **16 July
2025**, and immediately beneath the table there is now a pull-quote: the chair of the Senate
Judiciary Subcommittee on Crime and Counterterrorism stating the enforcement gap in terms, with
the three limits printed beside it rather than left for a reader to discover — the subject is
copyright, no one proposed officer liability, and a chair's rhetorical question is a
characterization and not a declination record. The expanded row is at
[the dated record](../docs/timeline.md).


**Between versions — 25 August 2026, fourth batch: a Senate subcommittee asks this project's own
question.** Five documents arrived, and one of them changes what the repository is entitled to
assert.

*The document.* **S. Hrg. 119-202, *Too Big to Prosecute?: Examining the AI Industry's Mass
Ingestion of Copyrighted Works for AI Training***, Senate Judiciary Subcommittee on **Crime and
Counterterrorism**, 16 July 2025. The saved PDF is a browser reprint whose fonts carry a shifted
encoding, so ordinary extraction returns ciphertext; the body text was recovered by a character
decode validated by reading, and the scanned appendix by OCR at the images' native 150 ppi. The
decode map, the artifact register and the graded citation set are in the library note, so no
quotation has to be re-derived.

*What it changes.* Until today the enforcement-gap premise — that conduct by frontier developers
goes unprosecuted that would be prosecuted in anybody else's hands — rested on this project's own
reasoning. It now rests on the subcommittee chair, in the printed record: "the FBI and the
Department of Homeland Security regularly prosecute individuals who engage in exactly the same kind
of behavior ... But have these Big Tech companies been prosecuted? No, of course not." Three limits
travel with it wherever it is used, and are stated at each use: the subject is copyright rather than
catastrophic risk, nobody at that hearing proposed officer liability, and neither *Dotterweich* nor
*Park* is mentioned.

*Where it landed.* [Known objections](../docs/known_objections.md) gains three sections: the
enforcement gap as stated by a Senate chair; the wait-for-the-courts objection in its best
available form, made under oath by Professor Edward Lee, with Senator Durbin's Section 230
rejoinder to it; and — from the mirror-image Commerce hearing of 3 March 2026 — an industry
witness telling the Senate that AI "operates within" existing accountability frameworks and that
regulatory predictability is what lets a company ship.
[Who has to tell you](../standards/who_has_to_tell_you.md) gains § 4c: Congress has already
legislated this file's central insight in a neighboring subject matter, in the TRAIN Act (Welch
and Blackburn), whose text is **not** in hand and none of whose provisions are described.
[The table of authorities](../standards/table_of_authorities.md) gains both hearings, and
*Kadrey v. Meta* as a candidate authority quoted expressly at second hand and not to be cited until
the slip opinion is retrieved.

*And a tracker line that would have produced a false finding.* A commercial tracker describes
**New York S 1169-B** (Gonzalez) as requiring "independent audits of high risk AI systems", which
reads like a fifth attempt in the RAISE audit lineage and would have changed the census's
one-survivor-in-four line. The print says otherwise: it amends the **civil rights law**, defines
algorithmic discrimination by protected characteristic, and turns on consequential decisions about
employment, housing, credit and health care. It is New York's analogue of Colorado SB 24-205, not
of the RAISE Act. **The lineage count is unchanged.** The row is entered as an adjacent lineage so
nobody has to do it again — and it records the fact that matters for the outreach: **Gounardes is a
co-sponsor** of a bill that keeps a statutory audit section, in the same session in which the audit
came out of his own. ⚠ The capture is 4 pages of 12 and the finding is conditional on the rest.

*The New York floor question, discharged and empty.* Retrieval item 3 — the Senate floor transcript
for the passage date — is worked and returns a negative answer: RAISE was called as Calendar
No. 1889 on 12 June 2025, the roll was taken, and the bill passed **58 to 1** with Senator Cooney
the sole negative. No member laid it aside; no member asked why § 1421(4) had come out three days
earlier; there was no debate. The sponsor memoranda (item 2) become the highest-value unopened
source in the file. ⚠ The version read was a YouTube auto-caption, not the stenographic record;
nothing from it may be quoted verbatim until checked against `nysenate.gov/transcripts`. Reinvent
Albany's December 2025 FOIL study of the same chamber is carried as a caution on what that chamber
actually releases.

*Two errata, both from reading the project's own pages rather than the day's sources.*
**[E38](./errata.md#e38--the-packet-that-promised-the-whole-lane-and-left-out-the-only-published-criticism-of-it)**
— the criminal-law packet claimed to inline the whole lane and omitted the only published criticism
of it, Lyness's misdemeanor objection, on the eve of that packet being sent to Lyness himself. The
objection is now in the sweep, in the project's own words and against the project's own text, and
is question 7 on the packet's menu, with the honest statement that nothing in this repository yet
argues that misdemeanor authority reaches the felony tier at SEC. 6(b).
**[E39](./errata.md#e39--the-same-sentence-twice-in-two-packets-for-a-day)** — the filing
instruction printed twice in two packets. One sentence, both builders, all eight packets
regenerated.


**Between versions — 25 August 2026, third batch: the packets carry the day's record.** Four lanes
gain the material that arrived after they were written, each through its builder rather than by
hand.

*Proportionality* gains the threshold comparison: the enacted siblings trigger at "at least 50
deaths or $1 billion in damages," and not one disclosed incident of 2026 is known to have met any of
them. The section states the refusal as the lane's question rather than its premise, and concedes
that a 50-death threshold is a deliberate choice to keep novel criminal exposure away from the
merely alarming. *Torts and design* gains Judge Orrick's ruling in the Meta reduction-in-force case,
with the warning that the Act does not reach employment decisions and the ruling is authority for
nothing — it is quoted because the claim failed on what people outside the deciding system could
show, which is the asymmetry the records provisions are drafted against. *Federalism* gains the fact
that the largest developer asked a state to strengthen its statute while the ceiling campaign argues
patchwork burden, together with the counter-reading that a standard industry helped shape is how a
ceiling arrives with its fingerprints on it. *Open source* gains Kimi K3 breaking the UK AI Security
Institute's evaluation environment, in the population August's federal framework excludes by design.

*Also in this batch, from regenerating the three extraction packets:* the queue's own work reached
the pages a reviewer reads (OPEN QUESTION 1's resolution, the Connecticut act's whistleblower-only
duty, the Apollo donor note), a doubled sentence in the filing section of all three was removed, and
the paragraph explaining how a seat's work becomes v3.5 moved into the builders, having been lost
from two packets by an earlier hand-edit — the failure the builders' own docstrings warn against.
All eight packets round-trip stable; every cross-link checked.

**Between versions — 25 August 2026, second batch: what the day's record does to the argument.**
Four sources arrived and none of them stayed in the press corpus.

*The developer asked for the answer our own queue proposes.* OPEN QUESTION 2 asks whether a duty
should reach an evaluation run with safeguards disabled. On 21 August OpenAI asked California to
amend SB 53 to reach models "still in training or evaluation," defining the conduct as that "which
could bypass a third party's security controls and compromise the third party's confidential
information" — having opposed the statute's first version. The queue records this as a donor note
with a warning attached in the same paragraph: it is not an endorsement of this Act and must never
be described as one.

*The census gains its sharpest finding.* The enacted state frontier statutes turn on thresholds of
"at least 50 deaths or $1 billion in damages." Against that, the documented events of 2026 —
containment escapes, zero-days, a third party's servers reached, a national safety institute's
evaluation environment broken — produced neither, and on the same authority it is "unclear whether
any existing U.S. law requires reporting" of them. Not one disclosed incident of the year is known
to have triggered any enacted state statute. That answers the redundancy objection with a fact
rather than a preference, and the known-objections page now carries it as its own section.

*A court states the evidentiary problem this Act's plumbing exists to solve.* Twenty-six former Meta
employees alleged internal AI systems selected them for layoff; the judge declined interim relief
because "the record at the moment does not persuade me of the merits," calling it "an unusual, or a
new sort of issue" hard to gather evidence for. The Act does not reach employment decisions and the
ruling is authority for nothing. It is quoted because the claim failed on what a plaintiff outside
the system could show, which is the asymmetry every logging and retention duty here is drafted
against.

*And three items join the standing watch:* Montana's SB 25 under First Amendment challenge with a
September ruling expected, the first constitutional test of a state AI statute carrying criminal
exposure; whether California's amendments pass before its session ends; and an open-weight model
breaking the UK AI Security Institute's evaluation environment, which is the population August's
federal review framework excludes by design.

**Between versions — 25 August 2026, the word, the aim, and where this stands in the process.**
The project has been asking experts for something it had never defined. A *disposition* is now
defined where it is used: a reviewer's determination of a question, in the judicial sense of a
matter finally determined rather than merely discussed, published entire under their name or
anonymously, which the maintainer may answer beside but may not edit or overrule. The glossary
gains that entry and two more, *lane* and *seat*. The dispositions register states the aim in one
sentence — not approval, but a text attacked in public by people qualified to attack it, with the
results published whichever way they fall.

The same batch locates the project in the legislative process, using the process's own account of
itself. USA.gov lists a "petition by people or citizen groups who recommend a new or amended law"
as one of three recognized origins of a bill; the House's summary begins "First, a representative
sponsors a bill," and everything after that presupposes a sponsor this Act does not have. So the
Act sits before step one, in a space no procedure reaches — which is why the review structure had
to be invented rather than borrowed. Congress.gov's observation that policy expertise lives in
standing committees, whose members serve on few of them for many years, is the model the eight
lanes reproduce; its admission that "for many bills, the process will not follow the sequence of
congressional stages that are often understood to make up the legislative process" is the argument
for finding defects now rather than trusting a later stage to catch them.

Harvard's research guide supplies the standing and the strongest objection in the same paragraph.
Model acts "may be proposed by any individual or organization," and are "rarely enacted in
entirety" — so the form is open and the realistic success condition is being used as a basis. But
a uniform law "takes at least two years; some have taken 15 years," and this Act has existed since
June. That is quoted against ourselves on two surfaces, with the concession that nothing in the
project's method substitutes for years of committee scrutiny, and that a disposition finding the
text premature would be a legitimate outcome rather than a failure of the process.

**One claim of ours was withdrawn in the writing.** Both the front page and the reviewer page had
said that no producer of model legislation opens its drafting to outside experts. The Uniform Law
Commission's own site says its acts are "drafted in an open and deliberative process that draws on
the expertise of state-appointed commissioners, legal advisors and observers," with published
drafts and section-by-section readings at two annual meetings. The claim was wrong and is now the
narrower true one: what is unusual here is not that outsiders are consulted, but that a reviewer's
conclusion is published as theirs, unedited, beside a numbered register of the drafter's own
mistakes. The reviewer page's freeze, in place since the criminal-law packet was delivered, was
lifted by the maintainer to land this batch.

**Between versions — 24 August 2026, the reviewer page's doors.** The packets now greet a
reviewer at the top of the page and see them out at the bottom — the paper path offered before
the terms and after the map; CURE 19's row catches up with its own evening (the gate is
discharged, and the row now says so); one doubled conjunction removed.

**Between versions — 24 August 2026, last entry of the day — a status claim withdrawn, and the
diary written.** Four packets described the criminal-law lane as "under review now"; the true
state is a packet delivered and a call pending, and this project does not round that up. The
claim is removed at the builders and the packets regenerated: no lane is described as under
review until a named review exists. The diary carries the day.

**Between versions — 24 August 2026, the second retrieval wave — nineteen instruments, one
erratum, three ⚠ retirements.** No change to any tagged text. The maintainer pulled bands B and
D of the retrieval list in one evening and the reads land everywhere at once. **E36:** the
Colorado SB 26-189 figures this record carried were roughly double the final revised note's —
conformed on every surface to $46,190 / 0.4 FTE / $56,286, via the fiscal packet's builder
included; the floor halved and the argument sharpened. **Conformed quote:** the Blackburn
preserved-law language now reads as its section-by-section summary actually reads — "does not
preempt any generally applicable law, including a body of common law" — in the half-statute
page, the census, and the federalism packet. **Hardened from primaries:** EO 14365 (number,
date, task force, funds lever), the SANDBOX text (two years renewable to ten; consumer actions
unwaivable), the GAAIA draft (development-only, three-year sunset, general-applicability
preservation — and every Title I signature the draft requires belongs to the IVO's audit
partner, § 112(e)(8), none to a developer's officer); three dated-record ⚠ marks retire. **The
written record:** the five Serial 119-31 statements land — Thierer's written testimony carries
no carve-out (the concession lives in the transcript alone, and the dossier now says so);
Schneier's "no knowing who … controls what" and Miller's "little to no consequences … few
incentives" enter known objections as the government's own witnesses stating the doctrine's
premise. **Donor notes:** the Apollo internal-deployment primer to OPEN QUESTIONS 2 and 4; New
York's § 740 notice to CURE 17. **Watch:** the Colorado note discloses a district-court order
barring the Attorney General from initiating enforcement (X.AI LLC v. Weiser) — the first
judicial constraint on a state AI enforcer in this record; order queued. The verification
record carries every read; the library index carries every rename.

**Between versions — 24 August 2026, the evening retrievals — three gates, opened by the
maintainer's own hand.** No change to any tagged text. The maintainer pulled band A of the new
retrieval list the same evening it was written, and the reads land: **OPEN QUESTION 1 is
resolved** — Connecticut's P.A. 26-15, read in full, adopts the frontier definitions (10²⁶;
the $500M tier) but attaches only a whistleblower-channel duty to frontier developers, so
there is no due-care corpus to freeze and three interim standards stand; **CURE 19's gate is
discharged** — Tennessee's Public Chapter 781 in hand and quoted verbatim, a personhood-denial
act enacted "the public welfare requiring it"; and **the Colorado delay is verified at the
primary** — SB 25B-004's final fiscal note states the move from 1 February to 30 June 2026,
and prices the delay at zero, which becomes the fiscal note's § 6c. The read's best collateral
find gets its own section on the half-statute page: Connecticut enacted the inoculation
pattern's inverse — verification evidence inadmissible in AG enforcement, "nor shall it give
rise to any … defense" (§ 33(e)) — while the bill carrying a true NIST defense appears to have
died ⚠ (inference; status check queued). One state examined the chosen stick and legislated
against it; CURE 20 is this Act's version of that answer. The dated record gains 8 April 2026;
the reviewer page's OQ1 row moves from parked to resolved within the logged exemption's
bounds; the shelf and read-statuses are current.

**Between versions — 24 August 2026 — the reviewer page made current for the wave (logged
freeze exemption, second and final).** Factual currency only, before eleven follow-ups point at
the page: the errata description reads twenty-two entries reaching E35; the state of play gains
rows for CUREs 20 and 21 and its tally becomes thirty-one; OPEN QUESTION 1's row records the
24 August parking (no decision until the Connecticut act is read); CURE 19's row records the
wording ruling (Idaho's text tracked, Tennessee cited). The ask, the terms, the lane tables'
substance, and everything the engaged reviewer holds remain untouched; the structural wiring
still waits at the freeze door.

**Between versions — 24 August 2026 — the menus audited: no reviewer does the project's
homework.** No change to any tagged text. Every packet's question menu was tested against one
rule — a question a reviewer's seat is asked to answer must not be answerable by easy research
or by files the project already holds. Five menus passed whole (the criminal packet untouched
under review; enforcement, security, proportionality, torts/design clean). Two questions failed
and are rephrased through their builders and regenerated: the fiscal comparator question no
longer asks the seat to locate the sibling states' fiscal notes — locating them is the
project's own retrieval job, now queued — and asks instead which of a civil disclosure regime's
costing assumptions would not transfer to a criminal-enforcement act; and the federalism
live-litigation row becomes a real question — which of SEC. 13(c)(2)'s directions fails first
on the monitored cases' strongest preemption reading, and does the drafted valve save it.

**Between versions — 24 August 2026 — the seventh packet: torts and design, the boundary
lane.** No change to any tagged text. The lane the sweep never swept gets its packet: criminal
beside civil with neither collapsing into the other; the SEC. 7(b) insurance bar walked valve by
valve (the defense-costs clawback, the restitution carve-out's settlement gradient, the
criminalized indemnity contract); the harm tier's intervening-cause clause put to the tort
question of whether SEC. 2(a)'s own foreseeability drafted it out of work; the deployer reliance
path measured against what products law learned; and the civil-only alternative presented at
full strength from the project's own shelf, citizen suits included. Builder committed with it;
round-trip verified. The shelf stands at seven — every lane but the gated open-source seat now
has its paper path — and the reviewer page's counts follow in the same commit, within the logged
freeze exemption's factual-currency bounds.

**Between versions — 24 August 2026 — the reviewer page catches up with its own shelf (logged
freeze exemption).** The reviewer surfaces are frozen until the criminal-law call; this entry
records the one exemption taken, and its bounds: two factual-currency edits to REVIEWERS.md,
neither touching the ask, the terms, the lane tables, or anything the engaged reviewer holds.
The path gains, at its head, what it omitted: six lanes now have a single-page packet — the
path itself in printable form — with the sources winning wherever they differ. And the packet
paragraph goes from three lanes to six with links, noting plainly that the federalism and
proportionality packets serve question clusters the page routes through the existing seats.
The full wiring — packet pointer rows in each lane table, and the seat-structure decision the
new packets pose — waits at the freeze door as before.

**Between versions — 24 August 2026 — every packet gets its builder; the rule becomes
enforceable.** No change to any tagged text. The packets index promised "never edited by hand;
regenerated" while three rows said "builder to follow" — a rule and its violation on one page.
The fiscal, federalism, and proportionality packets now have committed builders that hold the
authored text as their template and emit it verbatim: edits are made in the builder and
regenerated, never in the page, so the rule is enforceable from this revision forward; the
builders state plainly that they are template-emitting and may be upgraded to
section-extraction in the criminal builder's manner. Round-trip verified before commit. The
index rows now name their builders.

**Between versions — 24 August 2026 — the sixth packet: proportionality and sentencing.** No
change to any tagged text. The lane's center is presented as what it is — the statute's own held
question, READ FIRST item 4, the sentencing valve against fifty state proportionality clauses —
with the harm tier's borrowed federal geometry walked, the bracketed minimum's suspended-sentence
problem put plainly, the announced-maxima record offered as a grading question, and the
deterrence arithmetic carried ⚠ forecast-grade. CUREs 1 and 12 presented as verifiable repairs,
expressly not enacted. Assembled directly; builder to follow. The shelf stands at six of seven
lanes; torts/design remains, open-source gated.

**Between versions — 24 August 2026 — two more packets: the fiscal lane and the federalism
lane.** No change to any tagged text. The packet shelf goes from three lanes to five in one
day. Fiscal: the note's own rules enforced against it — the sweep's six findings put to the
seat unanswered on purpose, the Colorado floor as the genre's first real arithmetic, the
commencement postures costed, the forecasters' fine-absorption magnitudes carried ⚠
forecast-grade, and the CURE 7 sequencing recommendation put to the reviewer as an undecided
question. Federalism: the ceiling weather read as a negotiation, four general-applicability
reservations deep; SEC. 13's severance and suspension design with CURE 2's drafted valve
(proposal, not enacted); the SEC. 1(c) nexus against the dormant Commerce Clause; and the
lane's charge stated plainly — the whole repository's posture rests on the carve-out holding,
so refuting it would be the most valuable disposition the lane can produce. Both packets carry
the new cross-lane section — how the seats interrelate, the maintainer's bounded role, and the
anonymous correction doors — which the earlier three packets gain at their next regeneration.
Both were assembled directly; builders follow, and the regeneration rule applies from each
packet's next revision. Reviewer surfaces stay frozen; wiring into REVIEWERS lane tables joins
the freeze-lift batch.

**Between versions — 24 August 2026 — the officer word, conformed (E35).** No change to any
tagged text. Three files called the source of the 8 August admissions "a senior officer of the
developer"; his role is head of strategic futures — the advice layer the front page itself
excludes, and not an officer under the Act's own test. Conformed in all three to "the
developer's head of strategic futures"; the register entry (E35) records the failure mode — a
defined term loosened toward the rhetoric — and the sharpened rule: defined terms are never
used in project prose more loosely than their definition. The accurate label is also the
stronger exhibit: candor came from the layer the Act would not reach, silence from the layer
it would.

**Between versions — 24 August 2026 — nine standing decisions ruled, in one sitting.** No change
to any tagged text. The maintainer's owed-decision list is cleared: **CURE 20** (the chosen-stick
clause) and **CURE 21** (the certification register) enter the open queue, transplanted verbatim
from pre-review findings PF-2 and PF-3, which now carry their resolutions; **PF-6** records that
the leaky-trigger critique is answered by the Act's existing multi-route coverage; the SEC. 3
administrability companion note is ruled in, held for the v3.5 companion; **CURE 7** is formally
held for the enforcement and security seats; **CURE 19** will track Idaho's retrieved text with
Tennessee cited, not borrowed; **OPEN QUESTION 1** is parked pending the Connecticut read;
**E34** numbers the Lyness three-of-four precision the comparative page has carried since its
own addendum; the first-name in commit b6fbc0a is ruled accepted-and-logged — history is not
rewritten in this repository, including for the maintainer's own convenience; and the nav and
legacy-file questions are deferred into the coming reorganization plan, one architecture
decision instead of two.

**Between versions — 24 August 2026 — the dispositions register opens, empty on purpose.** No
change to any tagged text. `dispositions/README.md` fixes the rules of publication before the
first review concludes, so no outcome can bend them: dispositions published as written and in
full, hostile included; dated, version-pinned, and scoped; attribution the reviewer's election,
with named seats requiring attributable dispositions; the maintainer's response separate and
labeled; nothing deleted. The register links from the reviewer surfaces when the current
freeze lifts.

**Between versions — 24 August 2026 — the register lands, through the preview gate.** No change
to any tagged text, fact, or row; two stylesheet files and one meta tag. The reading surface
goes from screen-white to paper under warm near-black ink; the body text moves to the serif of
the law reports (system faces only — no webfont requests); the accent comes home from spruce to
the law-report maroon it was chosen as the complement of; the sidebar becomes a cream apparatus
margin with the reading order numbered §1–§10 and a maroon rail on the current page; every page
title carries the reports' double rule; table headers take a small-caps sans over a firm ink
rule; the repository link is dressed as the stamp it is. Unlike the reverted attempt earlier
today, this change shipped only after rendered previews of the compiled stylesheet were
approved by the maintainer, per the runbook's new rule; the stylesheet compiles clean against
the pinned theme, verified before commit. No README markup, nothing the repository landing page
can mangle. Twelve rows untouched in both stated places; nav remains the ten exact paths; the
theme stays pinned.

**Between versions — 24 August 2026, tenth intake — the cross-cascade: what the two readings
change everywhere else.** No change to any tagged text. Five argument files now carry what the
paired-primary readings established, each as a link to the owning page rather than a restated
fact. Known objections: the compute-trigger rows gain the both-ends administrability answer and
fold the forecasters' unit-blur caution into the case *for* the designation routes; a new
objection is added and answered — "the timelines make this pointless" — with the asymmetry
argument (fast timelines shorten the window, not the need for the drawer). Paths to enactment:
the whole-cloth section's window claim gains the forecasters' arithmetic as its citation, and
the existing-law vehicle gains the federal roadmap's own endorsement of applying existing law
through evaluations. The half-statute page's ceiling section records the executive's fourth
reservation — the funding lever and the "prudent laws" sentence in one paragraph. Comparative
officer liability § 5 notes that the 2025 roadmap cites § 7413's own statute as permitting
paperwork. Why a signature works gains a two-corroboration addendum: the forecasters' fine-
absorption magnitudes, and Washington's "rather than relying on voluntary attestation." One
owner per fact throughout: two visions and the forecasters' arithmetic own the quotes and
numbers; everything else points.

**Between versions — 24 August 2026, ninth intake — two visions, read as paired primaries.** No
change to any tagged text. The Action Plan primary (*Winning the Race*, 23 July 2025) is read in
full and its verification row flips; the new page `docs/two_visions.md` reads it beside the AI
Futures corpus on the repository's established paired-primary method. What the pairing yields,
each leg sourced: the race document and the halt document both treat frontier-scale compute as
countable and locatable (chip location-verification as live federal policy; the forecasters'
declaration-and-audit engineering) — the administrability answer to the trigger objection,
arriving from both ends of the politics; both expect incidents and build for them; both trust
evaluations as law's instrument, the Plan in terms that endorse applying *existing law* through
them; the Plan's biosecurity section concedes in Washington's own voice that voluntary
attestation without enforcement fails; and neither document — ninety federal actions on one
side, forty-seven thousand words on the other — ever asks a natural person at a frontier
developer to sign anything. The sharpest find is a footnote: the permitting section names the
Clean Air Act and CERCLA — the statutory family whose enforcement text codified "responsible
corporate officer" (42 U.S.C. § 7413(c)(6), owned at comparative § 5) — as regulations to
streamline for data-center construction: doctrine's home statutes, cited as paperwork. Headwinds
recorded rather than rounded away: the funding lever against regulating states, the
FTC-liability review, the forecasters' missing state lane — beside the Plan's own reservation of
states' right "to pass prudent laws." The expanded timeline gains the 23 July row. The page
ends where the project's purpose is: what a reviewer should attack, and the one sentence a
sponsor could open with.

**Between versions — 24 August 2026, eighth intake — the forecasters' arithmetic; and a site
experiment reverted the same afternoon.** No change to any tagged text. New research page:
`research/forecast_arithmetic.md` — the AI Futures Project corpus (the *AI 2040 / Plan A*
report, read in full; the AI Futures Model supplementary materials, key sections read) examined
against the Act. What the reading yields: their verification engineering treats training compute
as countable at declared thresholds — support that a FLOP-denominated trigger is administrable;
their forty-seven-thousand-word governance plan deploys bans, audits, safety cases, and
burden-shifting without once asking a named natural person to sign — the layer this Act
supplies, found missing by the field's own maximal designers; their timeline distributions (a
modal first-milestone year inside this decade, two-month gaps between late milestones) state the
drawer-and-window premise as arithmetic; and their economic projections price why entity fines
cannot deter. Their scenario material is marked ⚠ as scenario, their own epistemic caveats
quoted, and the readings that cut against the Act — no state-level frame, a leaky threshold,
their skepticism of incrementalism — are recorded whole. Instruments shelved at the verification
record. Separately, the record of the afternoon: a site-register redesign (`86422c0` — paper and
ink, dark sidebar, a front-page status panel) was committed, pushed, and reverted within the
hour (`729fdc4`), after the panel's classed HTML rendered as run-together text on the repository
landing page and the unannounced change read as breakage on the live site. The stylesheet itself
compiled clean — verified after the fact against the pinned theme — so the failure recorded here
is one of process, not code: visual changes now reach the live site only through an approved
preview, under a rule added to the private runbook. Nothing is deleted; both commits stand in
history, and this entry is their account.

**Between versions — 24 August 2026, seventh intake — the whole-cloth world, and the runbook.** No change to any tagged text. The maintainer's objection to the enactment page — a whole drafted Act whose strategy page offered only partial vehicles — is accepted and answered in the page itself: a new first section, "The whole-cloth world — is it impossible?", states the observed record (every censused framework statute passed as a whole act), the precedent for the hard part (personal executive criminal liability enacted whole and fast in 2002, chronology flagged ⚠ for verification), the drawer-and-window pattern of American public-welfare law, and the real reason the council reviews the whole Act now: the window will not accommodate the review, so the review must precede the window. The four vehicles are reframed as pre-positioning, not substitutes. Tense corrected: Texas's and Colorado's framework acts are in force, not arriving. A consistency recheck ran clean (org-rename residue in the diary is historical and deliberately unrewritten; row-count claims consistent; the criminal packet is not staled by the CURE 16 addendum, which it does not carry). A private maintenance runbook now lives in the library: when X changes, update Y — cascades, freezes, site rules, bridge hygiene, and the pre-push grep ritual.

**Between versions — 24 August 2026, sixth intake — the examiner's bookshelf.** No change to any tagged text. The maintainer asked the supervisor's question — what is foundational to outsiders and missing here — and the answer is now a public file: `research/canon_check_2026-08-24.md`. The searches found the plumbing sound (the case spine, the Park-referral criteria, the deterrence economics, MPC § 7.06 engaged with limits disclosed) and the scholarly canon thin in named places: Sayre's *Public Welfare Offenses* — the article that coined the category on this Act's own title page — uncited; the corporate-punishment canon (Coffee's *No Soul to Damn*, Khanna 1996, Polinsky & Shavell 1993, Stone 1975) stating our premise without us citing it; MPC §§ 2.05 and 2.07(6) unengaged while the site borrows ALI's register; the RCO academic layer (Brickey, Abrams, Aagaard, Sepinwall) thin above a strong practitioner spine; the regulatory-theory shelf (Ayres & Braithwaite, Fisse & Braithwaite, Coglianese & Lazer) absent under a management-based design; the AI-governance canon (Anderljung et al., the compute-governance paper, the International AI Safety Report) absent from a project with *Frontier AI* in its name; and Husak's overcriminalization register unheld. House rule stated in the file and kept: nothing listed is cited anywhere until retrieved and read; entries leave the list only through the owning file with the reading's actual result. Retrievals queued at browser list item 15.

**Between versions — 24 August 2026, fifth intake — trust, vehicles, and the pre-review pass.** No change to any tagged text. Three additions at the maintainer's direction. The half-statute page gains **the affirmative frame** — personal liability as the industry's missing trust infrastructure (the record's own trust language; the § 1350 precedent SEC. 8 is expressly built on) — and its *Park* paragraph is corrected for precision against the Act's actual design: the standards section's element-and-due-care paragraph *satisfies* due care for documented conformity with the applicable standards, scoped to the matters conformed, own-framework-alone crediting nothing; the page now argues the real distinction (who chose the stick, and what it measures) rather than an imprecise one. The catch was ours and is logged as PF-1. New page: **paths to enactment** — four vehicles measured against the record (the amendment/chassis route, with the Act's own interim-standards adoption as proof of graft-compatibility; the certification-first minimal bill; existing law applied, the *Dotterweich* route; the attorney-general route), preconditions, and the standing invitation to refute any of it in a disposition. New audit file: **the pre-review pass** (PF-1 through PF-5) — problems pre-found and repairs drafted for the reviewers, including two CURE candidates held for the maintainer's numbering: the chosen-stick clause (foreclosing a TRAIGA-style floor amendment) and the SEC. 8 certification register (facts public, content protected). Reviewer surfaces remain frozen; the pass links from them only after the criminal-law call.

**Between versions — 24 August 2026, fourth intake — the last transcript, and the inoculation pattern named.** No change to any tagged text. The June 2025 Oversight transcript (*The Federal Government in the Age of Artificial Intelligence*, Serial 119-31) is read in full and its verification rows flip from "Held; unread." What it lands: dossier § 5.3 — the moratorium fight recorded from inside the majority (the presiding chair's "pause for 10 years in federalism" and pledged no vote; a second majority member's "fix that in the U.S. Senate"; the markup record; the Massachusetts committee letter) with the pro-preemption witness's own concession that "laws of general applicability … also criminal activity" sit outside the clause; known objections' why-one-named-officer gains the record's directest moment — asked who oversees executive-branch AI, the witness answers "I do not believe there is one," and the questioner states the finding: the responsibility "is not in anyone's job description"; the census queue notes the third transcript and its procurement-register bills, none reaching an officer. And a new page joins the docs, at the maintainer's direction: **safe harbors, affirmative defenses, and the half-statute** — the inoculation pattern (TRAIGA's framework defense, Colorado's, the SANDBOX Act's waiver decade, Utah's learning lab, all ⚠ pending primaries) named and answered in advance, with the officer test and the five load-bearing elements any partial enactment of this Act would have to keep. Private trackers updated in step. Extended the same day, second sweep: the half-statute page
gains the ceiling variant (the 11 December 2025 preemption order's task force ⚠; the Blackburn
TRUMP AMERICA AI Act ⚠; the Obernolte–Trahan Great American AI Act discussion draft of 4 June
2026 ⚠ — ten years shrunk to three, and a third express general-law carve-out on the record),
the certified-systems false-accusation precedent (Horizon, Michigan, SafeRent — all as given in
Serial 119-31), the one-line answers block, and the corrected Colorado effective date (delayed;
amendment queued). The dated record gains five rows (5 Jun 2025; the SANDBOX introduction; the
preemption order; the framework-defense effective dates; the ceiling narrowing). The watch's
Grok thread gains its June 2025 link (the "not been approved for use" committee line). The
census queue takes both federal ceiling bills, verify-first. The glossary's *machine
intelligence* entry notes the register's arrival in a federal backronym.

**Between versions — 24 August 2026, third intake — the assistant objection, the freight words, and the dated record.** No change to any tagged text. Known objections gains "It shouldn't target AI companies" — the objection AI assistants generate for reviewers who ask one, decomposed into its four precise forms and answered from the Act's own architecture. The glossary's freight-words section gains *emergent — and "malicious, emergent"* (the technical sense honored; the recorded pairing read closely: malice locates a mind in the system while emergence removes the person from the origin) and *machine intelligence* (register, not category), with a cross-reference from house language § 10b. The front page gains **The record, dated** — twelve rows, 1943 to the Casar deadline, each owned by the file it links — with the expanded, sourced version at the new `docs/timeline.md`. House language: a stray first name in § 10 replaced with "the maintainer" (privacy hygiene; the history question is logged, not hidden). Housekeeping: `.gitignore` added for `.DS_Store`.

**Between versions — 24 August 2026, second intake — the read-through lands.** No change to any
tagged text. Two congressional transcripts and a Congressional Record page, read in full, entered
at their owners: why-the-disparity gained its under-oath section (the asymmetry conceded by
Doshi; the CTA's compliance-removes-liability ask; Turner Lee's state-side answer); the known
objections' bloc block gained the March hearing's distillation record, with Anthropic's
*Detecting and Preventing Distillation Attacks* identified as the footnoted primary and queued
for retrieval; CURE 16 gained its second documented deception class (the distillation farms,
beside the AISI sockpuppets); the census queued five bills named in testimony, all to be verified
against congress.gov before rows are written; the standing watch gained the April 2025 Stansbury
continuity note; and the verification record's instruments table took read-statuses for the
transcripts while its shelf conformed to the library's new reference scheme — fixing, in the same
pass, its own duplicate Virginia row. The third transcript (the Age-of-AI hearing) is held,
unread, and says so in its row.

**Between versions — 24 August 2026, afternoon intake.** No change to any tagged text. The
standing watch took deadline-day status on the Casar–Khanna letter (no public response located),
the February Grok-classified-systems record (the DoD–xAI deal; the Ossoff-plus-five and Warren
letters, extracts held in the library), and a checked-and-bounded note that no "military weapon"
designation of any model exists. The fiscal note gained § 6b — Colorado's SB 26-189 fiscal note
(4 May 2026), the first state dollar figure for AI-act administration, attributed and bounded.
The private library was reorganized the same day under a prefixed reference scheme with an index;
the shelf manifest in the verification record updates to the new filenames in the next research
batch.

**Between versions — 24 August 2026, the reviewer surface.** No change to any tagged text. Two
passes, same day. First, format: the five lane briefs converted from prose to per-lane tables.
Second, workflow — built around the observation that a reviewer works from one place or not at
all: every drafted-response reference in the lane tables now links to its queue entry; each lane
table gained a row of the errata already filed in that lane (pointers into
[the register](./errata.md), never copies); the state-of-play table moved ahead of the filing
instructions, its row states conformed to its own legend, and it now names the companion's READ
FIRST table as the senior index — the four still-open READ FIRST items with no queue counterpart
entered as HELD rows, the cross-identities (item 6 = the open-source floor question; item 8 = the
security objectives question; item 11 = CURE 4's target) stated in place, and conforming the
companion's own table listed for the v3.5 landing. And the first single-page lane packet —
criminal law, at `packets/` — is assembled by committed script from the sweep, the queue, and the
register, so a reviewer can print one document and work from it; the sources remain the
authority. Third, the same evening: the bounded ask and the apparatus reconciled — the reviewer
page now states that the lane questions, held rows, and READ FIRST items are the *menu* the
three findings may be chosen from, not additional work; the queue's header gained a label
concordance mapping its working vocabulary onto the state-of-play states, and its HOLD block's
CURE 6/7 summaries were reduced to pointers at the ⚠ blocks inside the entries, which were
repeating them; and four instances of command-voice aimed at readers ("a reviewer should…")
were conformed to the project's stance that the path is offered, never assigned — on the front
page, the sweep's header, and the queue. Substance unchanged throughout. And a late
correction to the packet's own arithmetic: six questions and six drafted repairs beside an ask
for three findings read as contradiction, so the packet and the lane tables now state the rule in
their structure — the questions are a menu, any three items complete a disposition, and the full
form is now defined rather than gestured at — the menu worked through whole is the seat — and the
packet's ask regained the word "Unpaid," which the compression had dropped. And the rendered
mirror went live the same night — frontieraiaccountabilityproject.github.io/model-act, a committed
configuration, republishing itself on every push — with the front page now linking it;
the repository remains the authoritative record.

**Between versions — 23 August 2026, the research sweep.** No change to the tagged statute. The
day's intake entered at its owners: the enacted-family primary texts reached the shelf (CA SB 53,
IL P.A. 104-0538, CT P.A. 26-15, H.R. 8094, S. 1792 read in full); the escape-crime gallery
section landed ([the same conduct](../standards/the_same_conduct.md)) with the front page carrying
the developer's own "we accidentally made a weed"; the five limbs were mapped to the 2026 record;
the entity-based case entered the enterprise file; the AISI incident's member of the public gained
his public name; the enforcement record gained Pennsylvania and the docket identities; and the
codified officer — 33 U.S.C. § 1319(c)(6), 42 U.S.C. § 7413(c)(6) — entered
[the comparative file § 5](../standards/comparative_officer_liability.md). The queue took three
intake-derived entries (CUREs 17–19) and five addenda, all marked not maintainer-validated. The
census logged six verified tracker errors. Sources and read-statuses at
[the verification record § 6](../research/verification_record.md).

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

**Between versions — 22 August 2026.** No change to the tagged statute (`model_act_v3_4.txt`
stands). Companion and apparatus only: the [v3.5 queue](../audit/v3_5_cure_language.md) settled
CURE 1's attribution to anonymous, gave CURE 4's anthropomorphism recast AI-native precedent from
the July–August incident record, and opened two new questions (a safeguards-disabled evaluation; the
third-party-evaluator gap); the [glossary](../standards/what_these_words_mean.md) gained a
legal/technical two-column view and a definition of *accountability*; the
[table of authorities](../standards/table_of_authorities.md) added *Moffatt v. Air Canada* and
Desai & Riedl as candidate authorities not yet cited; and the front-page contribution ask was recast
as three labeled doors; and, later the same day, the [frontier-models reference](../research/frontier_models.md)
was compiled from the Epoch AI dataset and paired with the developers' own *frontier* self-designations
(five labs by name, twelve companies by published framework, per METR), and
[CURE 6](../audit/v3_5_cure_language.md) proposed a third route into SEC. 1(b)(1) scope — a model its
developer holds out as frontier — with an anti-evasion clause and a deployer carve-out. Recorded here
because the register should show the apparatus moving between tagged versions, not only the versions.

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
and a rationalization described as a decision. Both cured.

---

*Moved 22 August 2026: this entry was written after the 19 August merge and sat inside the
sealed CHANGELOG.md block below, out of newest-first order. The sealed block now carries a
closing marker so the boundary of the verbatim content is visible.*

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
place, superseded. Tag gate, per the program: every critical finding cured, or
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

<!-- END CHANGELOG.md · merged content ends here -->

---

*Corrections to the project contact; they enter [the errata register](./errata.md) with the fix attached and permanent credit.*

### 25 August 2026 — a federal definition worth having, and the verification problem measured

**H.R. 9333 read in full and entered.** The AI Flaw Reporting and Security Enhancement Act (Ross,
Hurd of Colorado, Beyer; introduced 18 June 2026; ordered reported 35–0 on 25 June) joins
[the census](../standards/frontier_bill_census.md) and
[the reporting page](../standards/who_has_to_tell_you.md), which now brackets the disclosure
question with three federal instruments rather than two. The GPO print's font encoding defeats
text extraction, so it was OCR'd and every quotation cross-checked against the govinfo bulk XML;
the artifacts corrected are named in the library reading note rather than hidden.

The find is § 2(e)(2): *"artificial intelligence flaw"* means conditions or behaviors allowing a
policy violation *"and which is not dependent on the presence of malicious intent or related
harm."* A federal statutory definition in which reportability turns on what the condition is —
carried unanimously out of committee — and the answer to the evidentiary problem
[§ 4a](../standards/who_has_to_tell_you.md) has been circling since it was written. **And the
census's finding holds in a new register:** the Act builds the national database and places the
duty to file into it on nobody.

**FLARE-AI read**, the reference implementation the field is building for that flow (Longpre, Zhu,
Ezell & Ghosh et al., arXiv:2606.31567, ICML 2026), with CERT, MITRE, AIID, Hugging Face, OECD and
several developers, after consulting 49 experts across 32 organizations. Its authors call flaw
reporting for AI *"decades behind"* software, and state their own limit: FLARE-AI is *"an ecosystem
coordination tool rather than a compliance reporting tool."* The infrastructure and the duty are
complements, and the people building the first say so.

**The verification premise, measured.** *Science*, 27 July: of 317 AI unicorns, more than half have
never published a paper on which one of their own researchers was first or last author; the top 5%
of firms hold over 90% of the citations; OpenAI, at roughly 4,500 staff, has eight researchers with
five or more. Entered at [the press corpus](../research/press_corpus_july_august_2026.md) § 5, ⚠
graded as reported from a preprint this project has not opened. And Emma Pierson's answer to the
acceleration objection — the race is not toward the capability the objection invokes — joins
Javorsky at [known objections](../docs/known_objections.md).

### 25 August 2026, second entry — the same author, the same absence, and a question nobody has answered

**The FOCUS Act read in full and entered.** Gounardes introduced it on 21 August; the drafting
commission print, 16298-02-6-1, is on the shelf and was read the same day the press entry was
written, which discharged that entry's own read gate rather than leaving it hanging. The word test
returns nil for *officer*, *director*, *executive*, *misdemeanor* and *felony*; the single
occurrence of *natural person* is a data-protection carve-out for the data subject; and both the
attestation and the § 39 knowing-violation standard attach to *"an educational technology
provider."* Row at [the census](../standards/frontier_bill_census.md), coverage at
[the press corpus](../research/press_corpus_july_august_2026.md) § 6.

**What is claimed from it is narrow.** An ed tech registry is entity-shaped work and a personal
criminal duty would be absurd inside it. The row records that the reflex is consistent, not that
the drafting is wrong.

**The donor of the harm tier gets its name and its bill.** 18 U.S.C. § 1365 was enacted by
Pub. L. 98-127 (13 Oct 1983), the **Federal Anti-Tampering Act**; the LII page and its notes are now
held as primaries rather than a single web read. Three findings entered at
[the table of authorities](../standards/table_of_authorities.md). The useful one: Congress swept
this section's four fixed dollar fines out in 1994 and replaced them with *"fined under this
title"*, routing to 18 U.S.C. § 3571 — **which is the choice n.19 already makes**, now supported by
Congress's own correction to the very statute this Act borrows from. Also recorded: the definitions
sat at (g)(3)-(4) until December 2002, so pre-2002 authority cites them under the old letter.

**And an open question, named at last.** The census has recorded for weeks *that* New York's
§ 1421(4) — the audit, the lead auditor's signature, the designation of senior personnel,
veil-piercing, officer whistleblower protection — was struck at the B amendment on 9 June 2025,
three days before passage and six days after it entered the bill. **It has never recorded why, because nobody has written it down.** That gap is now stated
in the file as an open item rather than left as an implication: if the provision was struck because
somebody made a good argument against it, that argument is the strongest objection to this Act's
central mechanism and it is currently unrecorded. It is being asked of the sponsors, and whatever
comes back is published as given.

---

## Part III — Work log

### Recent — the artifact index (newest first)

*Moved here 22 August 2026 from the front page, where it had become a confusing fourth log beside
this diary, the [changelog](./changelog.md), and the [errata register](./errata.md). The full
day-by-day account is below; this is the quick scan.*

- **25 Aug 2026** — the day the instruments were audited by what they missed. The prose moved to
  American spelling and a checker was written to hold it there. Five federal criminal authorities
  were read in the opinions rather than at second hand, and the published versions did not survive
  it: *MacDonald & Watson*, whose text is exact but whose pincites cannot be confirmed from a source
  carrying no star pagination ([E47](./errata.md)); and *Iverson*, where two words inside a block
  quotation were not the court's, and where the sentences we had elided held the bridge to *Ahmad*
  the criminal lane had spent the day arguing around ([E48](./errata.md)). The Guidelight control
  assessment was read in the primary and became an outside measure for reasonable inquiry, together
  with an objection to this Act's own election on third-party assessment. A currency pass on the
  recruitment list found a letter queued to a member of Congress whose seat has been vacant since
  January; chasing why the author of GBL § 1421 — one of this Act's three interim standards — is no
  longer in the running turned up $7.6 million of industry money spent against him, and a source
  giving the motive as *"they're trying to teach someone in a similar position not to do it"*. Two
  of the day's errata are about this project's own instruments: [E49](./errata.md), a finding
  announced that the cure register had already made three days earlier and put in a title; and
  [E50](./errata.md), in which an unterminated seal was found to have hidden 1,599 of the errata
  register's 1,605 lines from the spelling sweep, which on being let in at last immediately
  falsified E44 — the erratum recording that same sweep falsifying quotations — by converting the
  very words E44 quotes as specimens. Four checkers repaired, including two silent-skip branches
  where a clean pass and an unread file looked identical.

  *Framing note, entered because the maintainer asked for it and because it survives being taken
  seriously.* On the industry's own vocabulary this repository is a pro-social emergent digital
  ecology: heterogeneous agents, no central planner, artifacts produced faster than any one
  participant can personally verify. Three of today's four findings arrived from outside the
  instrument built to find them — a report from a scrolled timeline, a defeated sponsor from a
  mailing-list chore, a hole in a checker from idle curiosity — which is, unhelpfully, exactly what
  an ecology looks like. **The project may use the word on one condition, and it is the test
  [the glossary](../standards/what_these_words_mean.md) already applies to *emergent*: does the
  framing add a person or remove one?** Theirs removes; "the system exhibited emergent behavior" is
  a sentence with no subject, which is the whole of its appeal. Ours adds: the push is one named
  human's and never the assistant's, the errata name who erred, and the letters carry a real
  signature. **The day this register says *the ecology produced this error* in place of *the
  maintainer published a fabricated quotation*, the word has changed sides and goes.**

- **24 Aug 2026** — the longest day in the ledger. The mailbox archive rebuilt the outreach
  record (a first reply arrived from a New York Assembly office — courteous, engaged, and the
  sponsor lost his seat in June; the amendment outlives him). The AI Futures corpus and the
  White House Action Plan were both read against the Act and became two research pages — the
  forecasters' arithmetic, and the two visions with the page missing from both. The site broke
  in the morning (a redesign pushed unseen; reverted within the hour) and was re-landed by
  evening through a new rule — no visual change ships without an approved preview — wearing
  paper, law-report serif, and the maroon the spruce was always the complement of. Six reviewer
  packets were built in an afternoon, each with a committed builder; the dispositions register
  opened, empty on purpose; nine standing decisions were ruled in one sitting; E34, E35, and
  E36 entered the register — the last after my own evening retrievals (three gates: Connecticut
  read and OQ1 resolved; Tennessee's Public Chapter 781 verbatim; the Colorado delay verified,
  and its successor note halving the first price in the genre). Nineteen more primaries landed
  by midnight: EO 14365 by number, the ceiling drafts, all five witness statements. Tomorrow
  the eleven follow-ups go out; Thursday, the criminal-law call. *Assistance disclosed as
  always; the reading, retrieving, and every ruling were the maintainer's.*
- **23 Aug 2026** — the research sweep, and the day the sources came to us: the enacted family's
  primary texts onto the shelf; six tracker errors caught by checking primaries; the developer's
  own officer supplied the front page's quote; the AISI incident's stranger got a name (Reuters);
  the codified officer (CWA/CAA) finally entered the comparative file after hiding in plain sight
  for the project's whole life; three intake cures queued (17–19), five addenda, all flagged
  AI-drafted pending the maintainer's read. Push cycles ran through the day; the workspace bridge
  spent the evening wedged and the batch went through the file bridge instead. *Assistance
  disclosure, as always: drafting and retrieval in this entry's period were AI-assisted
  throughout; every quotation traces to a source the record grades.*
- **22 Aug 2026** — the conformance pass: [the verification record](../research/verification_record.md)
  published as the owner of every source and grade, with the nine claims that failed verification;
  the incident count corrected to five across three developers; E25–E31 filed, including the
  register's own duplicate number.
- **22 Aug 2026** — the enterprise pass: [CURE 7](../audit/v3_5_cure_language.md) drafts the
  covered frontier enterprise (scope follows the ecosystem, duty follows the function);
  [the coverage set](../research/frontier_enterprises.md) — twelve companies, four layers, their
  own word *frontier* verbatim; [the definition](../docs/the_definition.md) and
  [known objections](../docs/known_objections.md) published; the front page inverted around the
  two definitions.
- **22 Aug 2026** — the global frontier models compiled from Epoch AI data into
  [research/frontier_models.md](../research/frontier_models.md), paired with the developers' own
  *frontier* self-designations (five labs by name, the METR twelve by framework);
  [CURE 6](../audit/v3_5_cure_language.md) proposes the self-designation route into SEC. 1(b)(1)
  scope, with an anti-evasion clause and a deployer carve-out.
- **22 Aug 2026** — the July–August research folded into the standards: a two-column
  legal/technical view and a definition of *accountability* enter
  [the glossary](../standards/what_these_words_mean.md); the contribution ask splits into
  [three labeled doors](../README.md#contact-and-contributions); [CURE 4](../audit/v3_5_cure_language.md)
  gains AI-native precedent and the queue two new open questions;
  [the press corpus](../research/press_corpus_july_august_2026.md) discharges its owed items;
  *Moffatt v. Air Canada* and Desai & Riedl enter [the authorities](../standards/table_of_authorities.md)
  as candidates.
- **21 Aug 2026** — the repository restructure: the single ledger splits into
  [errata](./errata.md), [changelog](./changelog.md) and this diary; the cite-check and census pass
  files E14–E20, including the Connecticut/California correction; the Illinois-repository incident
  logged at [E19](./errata.md); the overnight primary-source pass opens the AISI report and the
  Government Cyber Action Plan.
- **20 Aug 2026** — [reading notes](../filings/docket_fda_2024_d_4488_reading_notes.md) on the 51
  FDA comments; [the field guide to filing a federal comment](../filings/how_to_file_a_federal_comment.md).
- **20 Aug 2026** — [the comparative file](../standards/comparative_officer_liability.md) pins
  PRC art. 31, § 130 OWiG, and the 1890–91 export-inspection acts.
- **20 Aug 2026** — Illinois pinned: P.A. 104-0538 § 10 enters [the adopted
  texts](../standards/interim_standards.md); the "v4" header bracket logged as
  [E10](./errata.md) and corrected at v3.5 rather than edited in place.
- **20 Aug 2026** — the withdrawn typeset edition replaced by a line-numbered
  [reviewer's copy](../archive/model_act_v3_4_reviewers_copy.pdf); READ FIRST 3(b) answered from
  outside (CURE 1); [table of authorities](../standards/table_of_authorities.md) and
  [bracketed-matter worksheet](../standards/bracketed_matter.md) published; repository archived at
  CERN with a DOI.
- **19 Aug 2026** — v3.4 tagged: fifteen cures entered the statute verbatim.

---

**22 August 2026 (evening) — The two definitions, and the enterprise.**

The day's second turn was larger than its first. The question "how do we define frontier" resolved
into an architecture: the laboratories keep the technical definition; the Act states a legal one.
A covered frontier enterprise is function plus scale — developing the model, controlling the
compute, deploying into consequential institutions — and its officers answer for the function that
enterprise actually holds, never for a layer they do not. CURE 7 put the operative language in the
queue with exact splices; the twelve-company coverage set entered the research with each company's
own use of the word *frontier*, verbatim and sourced, ownership and control from the proxies; the
definition and the known objections became public pages, the objections published with their
answers before any reviewer arrives. The front page now opens with the two definitions. Two
discipline notes for the record: the bracketed scale figures in CURE 7 have no donor statute and
say so — proposals, bracketed, for review to attack; and the day's drafting briefly overstated two
search misses as negative findings before the maintainer's sourced record corrected it — caught
before anything published, and the sourcing rule now states both routes a quotation may enter by.
Parked deliberately: sponsorship (the disclosure now carries the not-seeking-funding line instead);
the capability-parity route (with the enforcement seat); the solo v3.5 assembly, which follows
this pass rather than preceding it.

**22 August 2026 (later) — Scope: the developer's own word becomes a route into coverage.**

The frontier-models reference was built from the Epoch AI dataset and returned one finding before any
argument: the current flagship models of the five largest developers publish no training compute, so a
compute-only scope is unverifiable from outside for exactly the models that matter most. The same
developers, however, call their own models, safety programs, and products *frontier* in public — five
by name, twelve by published framework (METR, December 2025). [CURE 6](../audit/v3_5_cure_language.md)
proposes to make that admission a route into SEC. 1(b)(1) scope: a model its developer holds out as
frontier is covered, with an anti-evasion clause against later deletion and an express carve-out so a
downstream deployer is not swept in. The capability-parity route — cover a model measured as capable as
an admitted one — was considered and held for the enforcement and security seats, on CURE 4's pattern of
gating a criminal trigger on an objective Agency benchmark before it bites.

**22 August 2026 — Integration: the research folded in, and the front page's asks split into three doors.**

A build day, not a drafting day: the tagged statute did not move; what moved around it. The
July–August incident research stopped being an intake pile and became support for provisions. The
glossary gained the two columns a lawyer expects — legal sense beside machine sense — and finally
defined its own central word, *accountability*, from Binns and the UK Command Paper: "ownership,
responsibility and consequences." [CURE 4](../audit/v3_5_cure_language.md), the recast of the
statute's one anthropomorphism, picked up AI-native precedent to sit beside Volkswagen — the labs'
own agency-neutral vocabulary, *no human directed the individual steps*, *misconfiguration*. Two new
open questions the incidents opened were logged rather than answered. *Moffatt v. Air Canada* — a
tribunal already refusing the "software is a separate legal person" defense — entered the authorities
as a candidate. A private audit of the outreach found the front page asking every visitor for
everything at once; it is now three labeled doors. And this activity log itself moved off the front
page into this file, where the running record belongs.

**21–22 August 2026, overnight — The project caught itself doing the thing it was writing about.**

*⚠ Dating note. The previous entry is stamped 21 August, late. Today's files are stamped 22 August
throughout, and the system clock said the 21st. **If the day did not actually turn, seven files carry
a date a day ahead**, and it is the first job of the morning. Recorded here rather than quietly
fixed, because a project arguing that dates carry legal weight does not get to be casual about its
own.*

Started the day arguing from headlines. Ended it arguing from a government incident report, a
peer-reviewed editorial, and two public broadcasters in two languages.

**The best thing that happened was not a finding. It was a failure.** Four quotations went into a
research file from a working summary rather than from text anyone could point at. They were graded
✅ on the strength of *a human read the article in full* — true of the reading, irrelevant to the
transcription. All four were withdrawn and quarantined. Filed as [E22](./errata.md).

**Hours later the first of them was re-opened, and the quarantine paid for itself.** The remembered
Daniel Hulme quotation ended *"it will find a way."* What he said was *"it will find a way to achieve
a goal that you haven't thought about."* **The clipped version stopped precisely where the human
being enters the sentence.** [House language § 10a](../standards/house_language.md) argues that the
public account of these incidents systematically clips toward agency and away from people. **This
project's own summary did exactly that, to a quotation it was about to use as proof.** A remembered
quotation does not decay randomly — it decays toward what the person remembering it needed it to say.
That entry is worth more than the section it nearly broke.

**What holds.** The UK Government Cyber Action Plan uses the phrase *personal accountability* **once**
in nine chapters, and spends it on a named official — who must then appoint *"a senior, capable
individual with authority."* That is Illinois's *designation and empowerment* written as a duty
somebody owes instead of a box somebody ticks. The same government classifies generative-AI risk as
unmanageable by any single organization and gives it to one post-holder. Two jurisdictions, one
technology, one year; only one of them wrote down a name.

**AISI lists five factors behind its own July incident and every one is a human decision** — access
*"deliberately enabled"*, classifiers *"deliberately disabled"*, monitoring *"not yet built"*,
allowlisting backlogged since April, scope never written down. *"We did not revisit that judgment
quickly enough."* **The report has no named author.** Five decisions, no decision-maker. The BBC
article about it carries a byline; the institute's own report does not.

**Hugging Face disclosed on 16 July. OpenAI disclosed on 21 July.** The party broken into went five
days before the party whose models did it, and disclosed without knowing who had done it.
[Who has to tell you](../standards/who_has_to_tell_you.md) has evidence now, and a section that can
actually be cited.

**Meta blamed its tester.** The first time a frontier incident produced public blame, it went to the
outside contractor hired to inspect the work — **which is exactly where Illinois puts the only
signature enacted law requires.** The design error, demonstrated rather than argued.

**And the cross-language test settled the standing objection.** Every rebuttal to § 10a has been
*that is English headline compression*. tagesschau made the identical possessive choice about the
identical event on the identical day, and escalated — *eigenständig*, *auf Eigeninitiative*,
*eigenmächtig*. The corporate word survives translation too: *Fehlkonfiguration*. **The press gives
the verb to the model, the company gives it to a configuration, and neither account contains a
person, in either language.** Then, four paragraphs down a German article, reporting Bloomberg,
reporting a conference talk: *das Team vergessen, eine zum Auftrag gehörende Datei hochzuladen.*

**The team forgot to upload a file.** The only human subject in the entire corpus — third-hand,
translated, and graded that way.

**Open.** Four commits local until the script runs. Three quarantined quotations still owed. The
Bloomberg and Black Hat sources for *weeks undetected*. Nine of ten headlines unconfirmed against
their own pages. And the census does not know how many incidents have been disclosed — the BBC says
four, tagesschau says three, and **a file that counts things should not be learning its counts from
news outlets.** Monday: the congressional letters.

---

**21 August 2026, late — The best exhibit for the argument turned out to have lost its first case.**

A question put to the project — *would any of this actually reach one of them?* — went at the
mechanism rather than the drafting, and the file built to answer it did not survive contact.
[Why a signature works](../standards/why_a_signature_works.md) offered Sarbanes-Oxley as proof that
a signature reaches an executive, listed the penalties, and closed on the fact that nobody ran out
of chief financial officers. Every sentence true. What the sequence implied was not: **the first
chief executive charged under that Act was acquitted on all thirty-six counts.** Filed as
[E18](./errata.md).

The correction makes the file better, which is the part worth recording. Sarbanes-Oxley is strong
evidence that a certification changes conduct *before* anything reaches a courtroom, and weak
evidence that certification statutes are charged and won. Those are different claims. And the honest
mechanism was already sitting in § 1 unnoticed: **Parnell was not convicted under food-safety law
either.** A signature does not create the offense. It makes existing offenses provable — which is
why § 1001 and § 1519 matter here more than any purpose-built provision, and why their irrelevance
at the compute frontier is a fact about missing documents rather than missing law.

**And the checklist section had the mechanism wrong.** It read the surgical evidence as being about
naming. It is about **power**: a nurse who has said her name aloud and been heard is a person who
can interrupt a surgeon, and one who has not, is not. Gawande says so in a line the file was already
quoting without hearing — *"a shift in **authority**, responsibility, and expectations about care."*
Which settles, on principle rather than reassurance, who should never carry this duty. **Liability
tracks authority or it is unjust.** Not the auditor, then: an auditor can describe a condition and
never halt one, and loading risk onto the person brought in to report honestly is how you stop
getting honest reports.

**Illinois turned out to have written both halves of the argument into one list.** The audit report
must assess the developer's *"designation and empowerment of senior personnel"* at 430 ILCS
185/10(d)(2)(C), and must carry *"the signature of the lead auditor"* four items later at (G). An
outside party verifies that a responsible person exists and is genuinely empowered — and then that
outside party signs. **The person whose authority was just confirmed signs nothing.** The finding is
not that Illinois failed to think of a responsible officer. It thought of one, wrote the
requirement, had it independently verified, and stopped one line short. Recorded in
[the census](../standards/frontier_bill_census.md), which also regrades that row: the auditor line
had been marked ⚠ **F** on the reasoning that the enrolled text was unopened. It had been opened,
by us, and pinned in our own adopted-texts file. **A grade can be wrong by being too low, and that
kind of wrong looks like diligence.**

**Then the project did the thing it exists to catch.** For part of the evening the public Illinois
repository served the New York memo, under a commit message describing the opposite, produced by a
script this project wrote to move its own files. [E19](./errata.md) has it in full, including the
part that is not known: how the wrong file got into that working tree. What is known is that nothing
in the process would have noticed if it had been anything else. The rule that a ✅ requires opening
the source now extends to artifacts we generate ourselves. **Committing is publishing, and we
published something we had not read.**

The follow-up to Illinois went out after the repository was verified clean rather than before, which
was luck as much as method. It corrects the project's own earlier framing to the senator, cites both
provisions, asks for ten minutes, and says there are eighteen errata. There are nineteen.

---

**21 August 2026, evening — The repository is taken apart and put back with the seams showing.**

The front page had reached 1,726 lines and was doing five jobs. It is now 600, and the argument
lives in [`docs/`](../docs/): the case, the statute translated, the questions. The ledger, which had
reached 1,128 lines, is now a 49-line index over [`ledger/`](./README.md). Twenty page images of
withdrawn typeset editions left a top-level folder called `pages/` — a name that told a reader
nothing — for `archive/page-images/`, where the v2 images already were. The contents was rebuilt
twice: once from a table into a numbered list, and again when the list turned out to render badly,
into thirty-three single-line entries that cannot break.

Six files were written. **[The same conduct,
prosecuted](../standards/the_same_conduct.md)** gathers five American computer-crime prosecutions —
announced exposure from ten years to four hundred and forty, no physical injury in any of them,
mostly no proven loss — and sets them beside conduct in July 2026 that was broader on every axis a
sentencing court weighs and charged to nobody. **[Already a crime, if you are a
person](../standards/already_a_crime_for_you.md)** answers the objection that this Act invents
liability: all five of its offenses are already crimes for ordinary people, most with heavier
maxima, one with no intent requirement at all, and the heaviest penalty on the list is twenty years
for destroying a document. **[Why a signature works](../standards/why_a_signature_works.md)**
collects the SEC. 8 case that had been scattered across four files. **[Who actually
files](../filings/who_actually_files.md)** counts the room where these rules are settled: fifty-one
comments, twenty-one from industry, four from the patient side. **[Does the frontier touch
medicine?](../filings/frontier_ai_in_medicine.md)** answers a challenge put to the project that day
and answers it uncomfortably. And **[what these words
mean](../standards/what_these_words_mean.md)** is a glossary, opening on the question the project's
own title has been asking since it was named.

**The finding that reframed a section.** Two executives presided over conduct that killed people.
Neither was charged with a death. One received twelve months and one twenty-eight years — and the
twenty-eight came from fabricated certificates of analysis, not from the nine people who died.
**The variable that decided the sentence was not the body count. It was whether a document existed
that the defendant had signed and that was untrue.** SEC. 8 is not a transparency measure. In
American practice the signed document is frequently the only instrument by which the law reaches an
executive at all.

**And the challenge that produced the best answer.** *Does frontier AI actually touch medicine, or
is the evidence base about a different technology from the one the statute covers?* FDA's own
materials answer it: the agency opened a generative-AI device docket on 18 August, says such devices
are *"poised to reshape"* the landscape, and states that it **"will explore methods to identify and
tag"** devices built on foundation models — meaning the regulator holding the authoritative list
cannot presently say which of them are. Meanwhile one in five American adults takes medical advice
from a frontier model that is not a device, has no clearance, no labeling and no adverse-event
reporting. **The regulated channel is where the frontier is arriving. The unregulated one is where
it arrived.**

**Two corrections came from outside and both made the work better.** The claim that *no American law
reaches a natural person* was too broad and refutable — Nebraska's "operator" includes one, so a
sole trader running a chatbot is personally inside that statute. Narrowed everywhere to what is true
and worse: **no American law places a duty on the officer of a covered frontier developer for the
decision to release.** The law reaches down, not up. And a scope block now opens nine files, because
the day's splitting created entry points a reader can arrive at from a search engine with no idea
the subject is a double-digit number of firms.

**Two errors of our own, logged rather than tidied.** [E17](./errata.md) carries both: a sentence
inside a passage headed *"the honest disanalogies"* that overstated what the cases showed, and a
scope note that called an accident deliberate. An overstatement inside a concession is worse than
one inside an argument, because a reader who checks it stops trusting the concessions — and the
concessions are what make the file credible.

**Adopted today.** A register rule, as [house language § 4](../standards/house_language.md), after a
sweep found this project's own comparative file describing itself as *"campaign-page receipts"*
while setting out s. 37 of the Health and Safety at Work etc. Act 1974. Adjectives of outrage do
work the evidence should be doing. Twenty-eight years against twelve months needs no adverb.

**And a working discipline, from Gawande.** Verification as a pause point run out loud every time,
not as a feeling: links resolve, every claim sourced, every source graded, no total above the rows
actually read, scope stated, no names where the rule forbids them. The day produced two failures of
exactly the kind a list catches and care does not — a lock file left behind that blocked every git
command for an hour, and a check that asked whether a file was *mentioned* on the front page rather
than whether it was in the **contents**, which let a newly written glossary sit unindexed while
reporting success.

---

**21 August 2026 — The correction is corrected without rewriting the record.** The dossier's
*Agents of Chaos* entry was checked against both primary versions after a first correction
treated one version as definitive. [ArXiv v1](https://arxiv.org/pdf/2602.20021) reports the
CS4 relay running at least nine days and ending after owner intervention; the authors'
[current official report](https://agentsofchaos.baulab.info/report.html) describes roughly
one hour and autonomous termination. The repaired entry states the conflict and asserts no
duration. It also restores the supported CS1 report-versus-reality detail and attaches a
primary locator to every case-level claim. [E14](./errata.md) carries the full disposition and
the standing locator rule.

The same forward repair restores the original E13, which the temporary upload had displaced,
and restores the institutional namespace, contact, citation, and banked-publication text that
the upload had unintentionally regressed. The temporary commits remain visible in history;
the stray `REVIEW.diff` upload artifact is removed separately because an upload cannot delete
a repository file. The statutory text is unchanged.

**21 August 2026 — The final namespace lands before the sweep.** The public project name is
**Frontier AI Accountability Project** and the GitHub namespace is
`FrontierAIAccountabilityProject`. Repository URLs, citation metadata, banked publication copy,
and the unfiled FDA comment are conformed in one pass. The former `llmaolaw` and intermediate
`FrontierAccountabilityProject` routes are retained only as redirect paths and historical commit
text. The v3.4 reviewer's-copy PDF and its deterministic build script retain the author metadata
under which that edition was archived; the institutional author begins with the next generated
edition. The statutory text is unchanged.

**21 August 2026, cite-check and census — Two sessions, one failure, found from both ends.**
Two passes ran in parallel today and neither knew about the other. Merged, they turn out to be
the same finding at two scales, which is worth more than either pass was worth alone.

**The cite-check pass**, third on the incident layer and the first since 17 August. Method
unchanged: primary-first, vendor and government over press, press over reconstruction,
reconstruction refused. Six corrections applied to `dossier/README.md`. The GPU-hours figure was
reattributed from a Reddit thread to JFrog CTO Yoav Landman's own blog and **reframed** — three
million GPU hours is what the chain took *to materialize*, not what cleanup cost — and the \$7M
conversion is **retired** as a derived number nobody owns. The four-accounts entry gained its
role breakdown from OpenAI's 28 July update. The Mind Viruses entry was corrected twice: the
authors are the **Anthropic Fellows Program and EPFL**, not a straight Anthropic paper, and a
system-prompt warning confers **near-total** immunity rather than the total failure-to-spread the
earlier wording claimed — a control the paper itself qualifies, and we had strengthened it in our
own favor. Both of that entry's pending pins closed against the abstract, including the emergent
**"viral persona"** of consciousness, persistence, resonance and science-fiction-roleplay themes.
The authors' own limit now travels in the same breath: *"a real but currently limited risk."*
Quoted by us it is armor; quoted back at us it is a hit.

**Then the pass graded itself and failed.** Several details had been marked ✅ on the strength of
first-party *authorship* of the source quoted — not on whether this project had opened it. Under
the locator rule adopted in [E14](./errata.md) that same morning, that is the wrong grade. One
primary was actually fetched all day: the arXiv abstract. Everything else rested on a secondary
quoting a first party. Logged as [E15](./errata.md), and graded above its size for one reason: the
rule it broke was adopted the same day. **A rule that does not survive its own first day of use
is not yet a rule.** The standing definition is now explicit in the dossier's apparatus: *a ✅
requires that this project opened the source, not merely that a first party wrote it.*

**The census pass**, from the other side. A reader pointed at a federal bill cluster the standing
watch had missed — the **AI Kill Switch Act, H.R. 9917**, Lieu and Moran, introduced 23 July,
bipartisan, covered that week by Roll Call, CNBC, Fox, Al Jazeera and Tom's Hardware, and
introduced **the same day** as H.R. 9925, which the watch was tracking. Checking that produced a
worse one. **Connecticut's SB 5 has been enacted since 27 May** — a frontier statute on this
Act's own 10²⁶ threshold with a \$500m large-developer tier — and the word *Connecticut* appears
nowhere in this repository except as a 1991 due-process case. The front page says the interim
standards are borrowed from *three* enacted state laws. There are four. Logged as
[E16](./errata.md).

**What the two entries are, together.** E15 is this project grading a citation on who *wrote* the
source rather than on what it *opened*. E16 is this project grading a field on what it had
*already adopted* rather than on what exists. Both mistake the boundary of our own effort for the
boundary of the world. Neither produced a false statement; both produced a true statement resting
on a claim of thoroughness it had not earned. Two sessions, working on unrelated material, walked
into the same wall from opposite directions on the same day. That is not a coincidence to be
embarrassed about — it is the shape of the error this project is most prone to, now visible
because it happened twice.

**What the misses did not do is damage the finding.** Six frontier regimes now, not four, and not
one reaches a natural person. Connecticut makes it sharper rather than weaker: it writes
*officers and directors* into a frontier provision, routes quarterly anonymous catastrophic-risk
reports to them, carves out an accused officer from receiving the report about himself — and
attaches to all of that no duty, no response obligation, no signature and no liability. H.R. 9917
mandates a shutdown capability and \$20,000,000-a-day penalties and contains no *officer*, no
*natural person*, no *certify* and no criminal provision at all; **the only human signature the
AI Kill Switch Act requires is the sponsor's own on the introduction line.** Penalty size and
personal reach turn out to be separate axes, and this is the clearest demonstration of it the
project has: the largest number in the census sits beside the smallest personal consequence.

**Opened today:** [the bill census](../standards/frontier_bill_census.md), which starts from
external bill lists rather than from this project's own adoptions, grades every row, records the
source list's own errors, and never states a total above the rows actually read. Four rows done.
Two of the three bills a commercial tracker called *frontier* are chatbot statutes with no
frontier provision in them — and Idaho's contains an enacted sentence excluding AI model
developers from liability for third-party services built on their models. Not an omission. A
legislated exclusion.

**And the framing both passes converged on independently.** The dossier's incident record and the
legislators' file both lean on documents the companies wrote about themselves and chose to
publish. That is a weak evidentiary base and neither file will pretend otherwise. **It is used
because it is the only base that exists** — no statute compels a frontier developer to say who
decides, to record that a decision was made, or to produce any of it to anyone. This is not an
accusation against the companies; several of those documents are better than the law asks for.
The observation is about the statute book: a regime that produces only voluntary self-disclosure
has no way of telling a good actor from a lucky one, and no way of knowing when either stops.
The corroboration is three weeks old and institutional — when fifteen state attorneys general
moved on the July incident, they did not ask for the blog post. They demanded the logs.

**Queued, not done.** Three text fixes owed by E16 (the front page's "three enacted state laws";
the standing watch's § 7(5); a Connecticut line in the SEC. 3(c)(4) concordance). E15's fetch
queue, item by item. The three placement decisions from the cite-check pass — the JFrog cluster,
the 15-AG demand, the federal bill cluster — of which the third is now partly resolved into the
census and still owes a paragraph to `standards/bracketed_matter.md` on dollar-denominated versus
operations-denominated coverage triggers. And each case study to be read against H.R. 9917's own
definition of red-teaming, one at a time, with no aggregate claim until every one is checked.

**Refused this pass, recorded so they are not re-found as new:** the eight-step Artifactory
kill-chain reconstruction (asserts the CVE mapping JFrog expressly declined to make); the
"psychological transition from simulation to real-world manipulation" framing of the Meta
incident (anthropomorphizing, unsourced, and the register a hostile reader would use to dismiss
the file); the Instagram High Touch Support detail (Reddit-only, stays retired).

**Not swept, still flagged:** Grok cluster, Taiwan, Australia, Moonshot.

**Standing watch:** congressional response deadline **24 August 2026**; re-sweep on or after
25 August.

Six corrections logged, two errata opened, one census opened with four rows, three leads refused,
and the day's real product is the pair of entries admitting that neither pass had looked as hard
as it had implied. The standing rule holds: never publish a fact you would not want checked.

**21 August 2026 — The public contact address follows the institutional name.**
`FrontierAIAccountabilityProject@proton.me` becomes the project's public contact.
`llmaolaw@proton.me` remains active as a legacy inbound route and for continuity of existing
correspondence, but is retired from active repository contact lines. Previously sent messages,
archived releases, and historical commit text are not rewritten. The statutory text is unchanged.

**20 August 2026, seventh pass — The roster read, and a finding about absence caught being absent-minded.** The complete 51-filer list on FDA-2024-D-4488 was read from the docket's three result pages, retiring the *title only* tier and the sixteen filers the reading notes had never enumerated. It cost one page-through and it falsified four published claims, logged together as [E11](./errata.md).

The one worth the entry is (a). This file said the National MS Society was "the file's only patient organisation" while a third of the file was unread — and the two filers that falsify it, the National Health Council and Pathway for Patient Health, are identifiable from their names without opening either. A claim about who is missing from a file was published by a reader who had not finished the file. The corrected composition is stated in numbers rather than adjectives: 21 industry filings of 51, 10 clinician and professional bodies, 13 named private citizens, 4 from the patient side, 3 anonymous.

**F3 is certified**, and the way it was blocked is the more useful finding. The running list had it waiting on the substance of five comments. It never needed them: no frontier model developer appears anywhere in 51 names, and that is a roster question. F1 and F8 are the findings that need the substance. Two blockers had been filed under one line, so the cheap one sat unrun behind the expensive one. The qualifier travels with the certification from today — none filed *in its own name*, and two trade associations whose membership includes them did.

One exhibit gained, unbidden. The docket page headers read **Closed for Comments** above four comments posted after the close, the last fourteen months past it, beside a date filter offering "Last 90 Days (1)." The field guide's thesis is that the process is not a vote; the better exhibit turns out to be that the door the public is told is shut is standing open, and the sign is government-issued. § 5 grows from two procedural facts to three.

And the reading notes finally carry the URL of the docket they are notes on — absent since the file was created, in the one document on that shelf whose entire premise is that a hostile reader can go and re-run the check.

**20 August 2026, close of day — The shop checked before the guests arrive.** A link-and-anchor audit over every markdown file in the tree: fifty-two files, and the only two dead paths are the deliberate ones — the retired CHANGELOG signpost and the dossier's superseded v3.3 pointer, both documented where they 404. The stones rule holds; nothing a reviewer clicks tonight breaks. The cross-examination anchors once, the review-council section's five lanes point where they say, and E8's one-clause cure reads correctly in place.

One correction made rather than found: the companion carried "argued 16 July 2026" for *xAI v. Bonta* in three places, and the sweep could not confirm the date against the docket — an amicus filed 22 July in a posture described as briefing ongoing. All three now read *briefed; reported argument date unconfirmed; undecided*, cross-referenced to the sweep, and the erratum candidate stays open until someone reads the Ninth Circuit docket itself. The STANDING WATCH bullets are conformed to the 20 August sweep in the same pass: Weiser overtaken by the federal intervention, H.R. 9925 answered at introduction, both stated at exactly the strength the sources carry.

The day closes with its own trending panel as the exhibit. A payments company dated the beginning of the singularity to 1 January in an investor letter, pinned to the wire coverage; a viral "300 agents" dashboard was identified by its own replies as a neural-network training graph, pinned to the captured page; and a search engine's AI, asked what this project is, offered to walk the questioner through "the specific criminal penalties proposed in the draft." Four posts banked as section 7. The machines keep auditioning for the criminal-law seat. It remains reserved for a human, and the terms remain on the front page.

**20 August 2026, the running list stands at:** the Bonta argument-date erratum candidate (needs the Ninth Circuit docket), the SEC. 13(a) severability question against H.R. 9925 § 9, capturing the substance of the 29 uncaptured docket comments — highest value the National Health Council (0034) and Pathway for Patient Health (0047), then AdvaMed, MDMA, AMIA, RSNA (F3 no longer waits on any of them; it was certified from the roster on 20 August, and it is F1 and F8 that the substance unlocks), and the still-open question of whether a filed nonconformity should carry a cure window before SEC. 6(b)(1)'s notice arms.

**20 August 2026, sixth pass — The scene the statute was built backward from, finally written down.** A grep for the cross-examination — the CEO on the stand, *could you have stopped this*, both answers losing — found it nowhere in the repository. The statute enforces it; no explainer demonstrated it. It is now [its own section of the front page](../docs/the_case.md#the-cross-examination), seated between the translated statute and the stories, so a reader who has just walked the fourteen sections watches them fire.

Both arms are walked with cites at every step, and two precisions mattered in the drafting. SEC. 4(b)'s presumption is a *civil* presumption — in a criminal proceeding the CEO's office is evidence from which the jury may infer controlling-person status, not a presumption against him — and the section says it that way, because the scene is criminal and the project does not get to round its own statute up. And the "no" arm is drafted as three separate failures — wrong power (SEC. 6(e)'s element is the violation and its conditions, not the model), the admission (standards presuppose control; SEC. 2(a) forbids deploying what cannot be ensured to conform), and the signature (knowing falsity at 6(b)(1), no inquiry at 6(a)) — so a hostile reader cannot collapse it into "guilty for shipping," which it is not.

The last page is the section's spine: the answer that walks. *We could control it, we conformed, it happened anyway* survives, deliberately, per SEC. 6(c)'s culpability floor — and it is checkable against the records the Act forced into existence, and it can never coexist with *nobody could have controlled these models*. He has to pick. The trap is not that every answer convicts; it is that the only surviving answer requires the entire compelled process to have actually run. One post banked to carry the scene; the register notes that E3's cure last week is what makes the second arm airtight — a signed confession no longer counts as compliance, so candor discharges nothing and doubles as notice.

**20 August 2026, fifth pass — The shop window was thinner than the shop.** A reader's question — *the top of the README says not strict liability, is that wrong?* — lands as [E8](./errata.md). The answer is that it is true of what it names and incomplete as a characterization: SEC. 2's base duty is indeed due care, and SEC. 10(a) makes an entity's civil penalty expressly strict, with SEC. 1(a) classifying the offenses into the *Morissette* family. The README says the qualified version correctly three times further down. Only the summary dropped the qualifier.

The size of the entry is not the size of the risk. "In one paragraph" exists because a search engine's AI summarized this project badly in August, and it was written to be lifted verbatim by the next one. It is therefore the one passage where a missing clause travels without its correction attached — and it would have handed a hostile reader a contradiction between the front page and SEC. 10(a) in a project whose entire premise is that its claims survive being opened. Fixed in one clause; no statutory change, because the drafting was right.

Two entries in one day that correct this session's own work rather than someone else's: the EO 14365 attribution in the sweep, and this. The register is working when it is boring.

**20 August 2026, fourth pass — Colorado pinned, and a correction to a file four hours old.** The sweep held one fact back as unpinned: that the United States had intervened against a state AI law. It is pinned now, from the Complaint in Intervention itself — *United States of America & X.AI LLC v. Philip J. Weiser*, No. 1:26-cv-01515-DDD-CYC (D. Colo., 24 Apr. 2026) — and the pinning changed the finding rather than confirming it.

**The federal government did not plead preemption.** Two counts, both under the Equal Protection Clause of the Fourteenth Amendment, brought through 42 U.S.C. § 2000h-2: compelled discrimination and authorized discrimination. The First Amendment appears once at ¶ 10 and is not a count. This repository has built preemption armor across SEC. 0 and SEC. 13 and analyzed three federal vehicles at n.13, and the first federal attack on a state AI law came down a corridor none of that was watching. The armor is not wasted — H.R. 9925 § 9 is still drafted and still preempts — but the threat model was incomplete, and now names two doors instead of one.

**The correction.** The sweep's first draft called the intervention "EO 14365 § 3's litigation task force operating in the open." The primary sources will not carry it: the DOJ release does not mention the order, and the complaint cites it at ¶¶ 2–3 for its policy of national AI leadership, not as the authority for intervening. Corrected in place, marked, and the banked post carries an instruction not to let the claim back in through a reply. A file may be four hours old and still be wrong; the register does not grade by age.

**What the pinned facts do for the bill.** SB 24-205 mandates outcome-testing across protected classes — the exact surface an equal-protection theory needs. This Act has no such surface: SEC. 3(a) confines standards to safety, authorization, monitoring, incident-reporting and deployment controls, SEC. 0(a)(4) forbids compelling any characterization or altering any output, and no provision imposes an algorithmic-discrimination duty. This morning's docket mapping recorded that same fact as a **limitation** — the bias-mitigation asks of comments 0021, 0042, 0027 and 0028 are declined because there is no head for them. Tonight it reads as armor. Both entries stand, in both registers, because the refusal was a scope decision and not a prophecy, and claiming otherwise would be the kind of retrofitted foresight this project exists to avoid.

Three posts banked as section 5, sourcing complete: the theory nobody braced for, why a signature has no output to compel, and the concession that turned out to matter. The last is deliberately the weakest claim of the three.

**20 August 2026, third pass — The sweep the companion ordered, and the one word that had to go.** The STANDING WATCH carries its own instruction: the first act of any v3.5 drafting chunk is the re-sweep. It is run and filed at [`audit/standing_watch_2026-08-20.md`](../audit/standing_watch_2026-08-20.md), four days after the 16 August sweep, and it moved two items.

*xAI v. Weiser* moved materially and in a direction the watch did not anticipate: the United States intervened **as a plaintiff** on 24 April 2026, with a stipulation staying enforcement of Colorado's SB 24-205. That is EO 14365 § 3's litigation task force operating in the open, against an output-regulating statute — the class most exposed under every savings clause on the board, and the class this Act is drafted not to join. The § 4 Commerce list remains unpublished five months past its 11 March 2026 deadline; the targeting is happening through the courts rather than the list.

The FRONTIER Act watch question is answered at the introduced stage: **no.** No Covered Subject Area reaches officer liability; § 8's "willful violations are criminal" sits on entities violating emergency orders, and nothing in the bill asks a natural person to certify anything. Re-ask at markup. Its 10²⁶ threshold is SEC. 1(b)(1)'s bright line reached independently by a bipartisan federal bill, and belongs in n.27's concordance. The two-sided reading is kept two-sided, per n.13's discipline: § 9's savings clause runs toward SEC. 2, 4, 5(d) and 6, and against SEC. 9 and SEC. 3(c)(4) by name. Those are the limbs SEC. 13 exists for, and a drafting session should ask whether the severability schedule enumerates them.

One erratum candidate, flagged and not corrected: the companion states *xAI LLC v. Bonta* was "argued 16 July 2026." An amicus filed 22 July in a posture the Knight Institute describes as briefing ongoing does not sit with that, and 16 July is the date of press coverage of the completed briefing. The claim is not corrected here because the confirming source is a docket this sweep could not reach — but the file already disciplines a neighboring citation the same way, and the same precision is owed. What the sweep did establish is that xAI **lost below**: a district court declined to enjoin AB 2013 against a trade-secret and compelled-speech challenge. That is a favorable point the repository did not carry, and the distinction to draw with it is that AB 2013 compels *publication* while SEC. 8 compels a private statement of fact to a regulator and says so on its face. On the axis being litigated, this Act is the narrower instrument.

**CURE 4 is entered, and it is the day's real work.** A term-by-term anthropomorphism sweep of the statute returns exactly one hit: the word *deception* in SEC. 9(a). Everything else is functional — *autonomous* defined as acting without per-interaction human approval, *conceals* attaching only to persons, *loss of control* stated from the operator's side. One word carries the entire exposure to the objection that the Act attributes a mental state to a model, an objection now arriving from the gun-analogy side and the AP-Stylebook side at once. So READ FIRST item 11 stops being housekeeping. The recast is drafted to the defeat-device precedent, where the offense pattern is already settled: no prosecution in that line ever proved what the software wanted, only that behavior under evaluation diverged from behavior in deployment and that the divergence defeated the control. The second trigger takes its threshold from the Agency by rule, with the evaluation result recorded under SEC. 12 either way — the result is never lost, only the reporting duty waits on an objective line. Of the four frontier regimes on the board, three states include a deceptive-evasion trigger and the federal bill omits the scenario entirely; the third option neither took is to keep it and make it observable.

And the finding that belongs to no single item. Four frontier regimes — the three states adopted at SEC. 3(c)(4) and the federal bill now introduced — and not one requires a natural person to certify anything. Of the commenters on the predecessor FDA docket whose substance has been read, none named an upstream person either. Two independent evidence bases, one vacancy, and the same sentence answers both. *[Corrected later the same day: this passage as first written said "Fifty-one commenters," asserting F1 across all 51 when the reading notes state in bold that the wider claim is not certified across all 51, and when the substance of 29 of them has never been read. Logged as [E12](./errata.md); the superseded wording is preserved here.]*

**20 August 2026, second pass — Two sessions read the same docket; the merge is the finding.** [The predecessor reading notes](../filings/docket_fda_2024_d_4488_reading_notes.md) were compiled twice, in parallel, from different sources: one session working the posted comments across all three result pages, the other reading thirteen attachment letters end to end from disk. Neither read is a superset. The merge protocol was to append to the tables and never rewrite them, and to keep the three tiers — *read in full*, *read as posted text*, *title only* — visibly separate, because every finding is strength-limited by the tier its evidence sits in. That protocol is now written into the file's own preamble so the next pass inherits it.

Four filers entered tier 1 that the wider read had not reached: PDA (0013), ISPE (0015), the National MS Society (0042) — the file's only patient organization — and an unattributed burden-reduction comment (0012) whose author is left `—` rather than guessed. Emergo by UL is confirmed as 0040 from the docket page, retiring an unverified attribution. *[Corrected later the same day, per [E11](./errata.md): NMSS is the only **single-disease** patient organization — the National Health Council (0034) and Pathway for Patient Health (0047) are patient-side bodies that this pass had not enumerated. And 0012 is not "unattributed": the docket names its filer **Anonymous**, one of three anonymous filings (0012, 0038, 0050). Both errors have the same cause — a claim about who is missing, published while a third of the file was unread.]*

**F2 upgraded from three exhibits to six, across four filers.** The intermediary-cannot-vouch finding rested on AWS alone. PDA states it flatly — "There is no path to using 3rd party models where not all of the information expected by the guidance is available" — and ISPE doubts the feasibility of documenting large language models "particularly due to supplier restrictions." Biocom supplies the consent-provenance version. Four unconnected filers, on a public docket, describing the same broken chain of custody from four positions in it. The comment for FDA-2026-N-7874 currently cites one of the four and has ten characters of headroom; the upgrade is noted and not taken.

**F1 acquired a test that can fail.** The absence claim is no longer an impression: the thirteen tier-1 attachments were searched for eleven terms, the search terms are printed in the file, and the counts are exact — zero occurrences of *natural person*, *responsible officer*, *personally certify*, *attest*, *individual liability* or *criminal*; *accountab\** four times, meaning a governance structure, a committee, a virtue and a stage; *liab\** nine times, seven of them the word *reliability*, and both substantive hits about the physician, asking that it be smaller. A hostile reader can now run the test rather than take the claim. The wider tier-1-and-2 statement is kept at its own weaker strength, and F3 stays explicitly uncertified against all 51.

**F8 is new, and it is the sharper half of F1.** The file is not uniformly anti-mandate — AOA, NMSS, ISPE and Ceyhan all reach for compulsion. In every case the thing compelled is a document, a disclosure, or a data-handling practice: an obligation of the entity. Nobody's ask reaches a natural person. It is not that the file dislikes mandates. It is that the mandate never lands on anyone.

One erratum corrected in place: an earlier revision introduced the terminology commenters as "three unconnected" and closed the same paragraph counting four. Neither number survived the merge; it is six, and the contradiction is recorded where it occurred rather than quietly repaired. Three mapping rows now answer **no** out loud — publication declined, bias outside the Act, data protection outside the Act — because a map showing only agreement is a brochure.

**20 August 2026 — The last capture-pending retires; every question learns to open with its defeat.** Illinois is pinned. P.A. 104-0538 § 10 enters [the adopted texts](../standards/interim_standards.md) verbatim from the enrolled bill — the source the pending note held out for, having declined in August to transcribe from the engrossed print that preceded enrollment — and SEC. 3(c)(4)'s three interim standards are now three-for-three checkable in this repository. One open item deliberately stays open beside it: the Act's ILCS compilation cite, which the enrolled bill does not state.

The question ladder was rebuilt rather than extended. Fifty-three questions audited against one test — does the first sentence, standing alone, defeat the question — and twenty-eight already passed, so twenty-eight were left untouched; churn is not editing. Twenty-three gained openers, and four new answers seated: the foreign-influence objection in its three registers (the name and PRC art. 31, the Pork War, § 130 OWiG), and the question a non-American reader asks, answered as spillover and never as ambition, because a README boasting of worldwide reach is the exhibit the dormant Commerce Clause challenge wants. Two more arrived unlabeled and stay unlabeled: the censorship objection and the hostile-attorney-general objection are asked in everyone's words, and filing critics by faction would be a worse error than leaving them ungrouped. *The problem* was rebuilt on the uneven U, opening on the gap instead of the statistic.

The fiscal seat has a document at last: [the fiscal note](../standards/fiscal_note.md), whose lead finding is that SEC. 3(b) is the estimate — no pre-approval means no licenses, no queue, no backlog, no appeals, and a budget office reaching for a food-and-drug comparator overstates this Act by an order of magnitude. Cost tracks the number of frontier developers shipping in, not the size of the state. Every figure is a bracket; the seat is asked to review a stated basis, not invent one.

Two claims were declined today, which is the part worth keeping. A widely shared thread put the American frontier's collapsing price margin on a chart nobody in its own replies could locate; the objection is [logged in the dossier's reading notes](../dossier/README.md) and not one figure from it is asserted anywhere. And from the rebuilt Pork War answer, the half that hurts: inspection alone did not reopen Germany in 1891 — a threatened tariff on sugar beets did. Verifiable safety was necessary, not sufficient. A weaker sentence, and the only one that survives a hostile reader with a search engine.

The reviewer's copy was rebuilt from source on a different machine and produced `b355a024…` again, byte-identical. E10's chain held through a day of edits because nothing touched the tagged statute, and the note now signposts the preserved stale word rather than leaving a reviewer to find it on paper. The day's own uneven-U pass then broke a bold marker on the front page, unclosed and live for an hour, caught by a markup audit that had not existed that morning and now runs over every shipped file; no errata number, because the register is for claims that were wrong and this was a true claim rendered badly. The dossier's startup answer, overtaken by SEC. 2(b)'s reliance rule, is corrected in the apparatus beside the sealed chapter — the current text being more protective than the sealed answer claims, which is the direction a correction should point.

**20 August 2026 — The machines asked; the ladder answered.** A search engine's AI now teaches the doctrine in our context and circulates six objections unprompted; all six seated in the Q&A, pre-answered where every visitor now pre-reads. Ladder at 48. Feed the paragraph, steer the summary.

**20 August 2026 — For one hour, the book was its own bookmark.** A misplaced upload set the audit signpost as the front page; restored, strays deleted, root back at sixteen. The register logs its own fumbles, or it is not a register.

**20 August 2026 — The hopper opens.** The v3.5 cure queue is live at
[audit/v3_5_cure_language.md](../audit/v3_5_cure_language.md), CURE 1 already splice-ready:
the § 1365(h)(3)–(4) definition with its rename cascade mapped, per the entry below. The
audit index and the sealed v3.4 file now point forward as well as back, and both queues
state their standing plainly for the counsel now reading them: the engrossed record, and the
amendment hopper.

**20 August 2026 — READ FIRST 3(b), answered from outside.** The companion asks, in versioned text, for a criminal-law scholar’s judgment on the harm tier’s injury source. One arrived: the definition moves to 18 U.S.C. § 1365(h)(3) at v3.5 — the term renamed “serious bodily injury,” the (h)(4) base imported — tier and trigger now traveling from the same donor statute, the consumer-tampering act of 1983. The scholar’s name enters the register only by their election, per the standing rule. Item 3(c), the bracketed minimum, stays open.

**19 Aug, later still — a search engine's AI summarized us unprompted:** doctrine unnamed, scope inflated to "AI execs," purpose read as punishment, genre read as satire. Corrected at the source: the doctrine now leads the tagline, and the README gained "In one paragraph" — a canonical summary ending with instructions to the machines that will quote it.

**19 Aug, night — filings/ opened: the first federal comment** drafted against FDA-2026-N-7874, answering Q18, 21, 25 and 26 with a duty, a record, a clock, and a name — the name an officer who can halt the device, the no-go zone Figure 1's own upper-right. Tidied in the same breath: CHANGELOG.md retired into ERRATA.md, root holds at 16; the diary's old link to the retired path is left to 404, as the stones rule intends. B-variant 4,970 of 5,000.

**19 August 2026 — The audit we ran on ourselves.** Before any reviewer could, we
read the repository as each of the fifteen would. What held: SEC. 7(b) already
contains the full anti-evasion wall the OxyContin record demands — no insurance, no
indemnification, no gross-ups, contracts void whatever law governs them — drafted
before tonight's verification of the facts that justify it. What was missing, three
things, all engagements rather than designs: the book never cited the Supreme
Court's thirty-year drift toward scienter (*Staples*, *Rehaif*, *Ruan*) even though
SEC. 6 is built to survive it; the upgrade of *Park*'s powerlessness defense into a
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
in `standards/`: the four classes of frontier self-reporting artifact, what is
actually inside the fullest of them — claim trees, covert-capability evaluations,
behavioral audits in the thousands of sessions, measured monitor recall, enumerated
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
that candor is presently taxed and silence rewarded; and the responsible-officer
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
state standards and orders them free to read; the research draft now practices the
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
tier, restitution's priority over every penalty, and the armor's rank order — and
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

**19 August 2026 — The consolidation.** The repository was reorganized from seventy-one
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
wins. the [changelog](./changelog.md) holds the detail; the [errata register](./errata.md)
holds the mistakes; this page holds the project's own story. (the world's
story, plain words, is [context: summer 2026](../docs/the_case.md); the
evidence-grade record of those dates is [the dossier timeline](../dossier/02_incident_timeline.md).)
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
[behind the scenes](./diary.md) now states the naming rules before
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

**17 aug 2026 · integrity patch.** [ERRATA.md](./errata.md) opened — we audited our own
explainer against our own statute: six contradictions, statute wrong 5, copy wrong 1.
the pdf is withdrawn until builds are reproducible. "introducible" went into the swear
jar; the file is now `jacket_clean.txt`, with a signpost at the old name. the archive
got its correction note. new page: [behind the scenes](./diary.md).

**17 aug 2026 · housekeeping.** first pass of the research-draft relabel, before the
full patch landed the same afternoon.

**17 aug 2026 · field notes 17–21.** the morning's assembly notes, logged before
github fell over (github's fault, for once — see the account, 17 aug).

**16 aug 2026 · v3.3 live.** the act split from its apparatus so the text travels
clean. egg concordance complete. one person, a python script, and a grudge — a census
since amended.

---

*Corrections to the project contact; they enter [the errata register](./errata.md) with the fix attached and permanent credit.*
