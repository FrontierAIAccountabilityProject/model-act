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

<a id="part-ii"></a>

---

*Corrections to the project contact; they enter [the errata register](./errata.md) with the fix attached and permanent credit.*
