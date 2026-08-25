*The errata register — every published claim this project got wrong, with the fix attached. Part I
of the ledger; the [changelog](./changelog.md) and [diary](./diary.md) are beside it, and the
[index](./README.md) explains what each is for.*

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

**We published:** *Ontario Provincial Council of Carpenters' Pension Trust Fund v. Walton*, 294 A.3d
65, 90, 92 (Del. Ch. 2023), that the rule protects a decision that "carries legal risk, but which
otherwise involves legally compliant conduct," and that proceeding unlawfully "would constitute a
conscious decision to violate the law."

**Neither sentence appears.** The opinion discusses "a conscious decision to prioritize profits over
compliance," which is a different proposition.

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

