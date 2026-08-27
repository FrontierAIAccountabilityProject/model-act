---
title: "Drafting record"
parent: Corrections
nav_order: 3
---

# The drafting record

This document concatenates, verbatim and unedited, the complete audit series that produced
v3.3 from v3.2: the reader's guide, working chunks 1–8, and the field notes. The constituent
files were merged into this single record on 19 August 2026 as part of the repository's
consolidation; their content is unchanged, and each retains its original heading below. The
original paths remain in place as signposts. The v3.4 cure queue
([v3_4_cure_language.md](../revision/proposals-adopted-v3-4.md)) landed and is preserved as its own review
artifact. 

**The live queue is now [v3_5_cure_language.md](../revision/proposals.md), which joins
this record when v3.5 lands.**

*Reading note: the chunks below were written between 16 and 17 August 2026, before the v3.4
and v3.5 numbering settled; their internal references to "v4" mean the next revision after
v3.3, which became v3.4. The text is preserved as written.*

*Typographical note: dollar signs below are escaped (`\$`) so that pairs of figures on one
line render as money rather than as mathematical notation. The escape is a presentation
character; no word, figure, or punctuation mark of the concatenated text is altered, and the
checksums stamped at each chunk head were taken before it was applied.*

Parts: [reader's guide](#the-audit-directory) · [1 — landscape](#chunk-1--landscape-audit-for-v33) · [2 — preemption armour](#chunk-2--preemption-armour-for-v33) ·
[3 — penalty architecture](#chunk-3--penalty-architecture-for-v33-sec-7-rework-and-bracket-calibration) · [4 — harm-tier rebuild](#chunk-4--the-harm-tier-rebuilt-proportionality-valve-recidivist-path-and-retention-harmonisation-for-v33) ·
[5 — commencement and records](#chunk-5--commencement-rebuilt-immediate-duties-the-interim-standards-bridge-the-modifiability-floor-and-the-sec-5e-decision) · [6 — assembly](#chunk-6--v33-assembly-record) ·
[7 — the hostile brief](#chunk-7--the-hostile-brief-v33-read-by-the-other-sides-counsel) · [8 — rule-dependency sweep](#chunk-8--the-rule-dependency-sweep-interim-defaults-for-everything-that-waits) ·
[field notes](#field-notes-for-assembly--chunk-6-inputs)


---

<a id="readme"></a>
<!-- BEGIN audit/README.md · sha256:f1d90a66d01e · concatenated 19 Aug 2026, content verbatim -->

# The audit directory

Receipts. This folder holds the work that turned v3.2 into v3.3, kept
public so any claim about the Act's assembly can be checked against the
record instead of taken on faith. The Act asks executives to keep
records sufficient for audit; it would be strange to ask that and not
do it.

## What's here

- **The five working chunks** (`chunk1`–`chunk5`) — the survey of the
  existing legal landscape, the preemption armour, the penalty
  architecture, the harm-tier rebuild, and commencement and records.
  Each one is a bounded question, researched with sources pinned,
  ending in decisions the assembly could consume.
- **`chunk6_assembly.md`** — the assembly record: how the five chunks
  became v3.3, what was taken, what was deferred, and why.
- **`chunk7_hostile_brief.md`** — the adversarial read: the repo as
  attacked by hostile corporate counsel, with a findings register the
  next drafting chunk can act on.
- **`chunk8_rule_dependency_sweep.md`** — the rule-dependency sweep
  (opened 17 Aug): every "by rule" hook in v3.3 inventoried; each gets
  an interim default, an express dormancy, or a ✓; the ★★★ findings
  consolidated for one assembly pass.
- **`field_notes_for_assembly.md`** — objections and proposals met in
  the wild during drafting, logged so nothing decision-relevant lives
  only in a chat log. Each entry records the objection's canonical
  form, the answer that survived contact, where it lands in the
  companion, and the verification status of every claim used. Entries
  3 onward are the objection bank: the gun analogy, the Swartz
  objection, the shareholder shield, and their successors.

## Conventions

- ✅ — verified against a primary source, with the read logged.
- ⚠ Memory-confidence — believed true at logging, not primary-pinned;
  must be pinned at the cite-check pass before any committee-facing
  use.
- **CONSUMED** banners mark items already folded into the Act or
  companion, with where they landed.
- Numbers are machine-counted before use. The standing rule of the
  whole project: never publish a fact you would not want checked,
  because the entire point is that it will be.

)(


---

<a id="chunk-1"></a>
<!-- BEGIN audit/chunk1_landscape_audit.md · sha256:72cd109c8e6e · concatenated 19 Aug 2026, content verbatim -->

# CHUNK 1 — LANDSCAPE AUDIT FOR v3.3

> **ERRATA — superseded on four points by chunk 2:** FRONTIER Act (H.R. 9925) is the introduced
> vehicle; GAAIA remains an unnumbered discussion draft — threat ranking in §D is inverted.
> GAAIA Sec. 121 enumerates three savings clauses, not seven. H.R. 5388 §6(a)(2)(B)'s
> criminal-penalty carve-out was missed entirely. The DOJ complaint in xAI v. Weiser pleads
> Equal Protection only; compelled speech is unadjudicated. See chunk 2, corrections section.
> 
> **UPDATE — pinned and completed on three points by chunk 3:** The §A Illinois flag "⚠ pin amounts
> from enrolled text" is closed: P.A. 104-0538, Act § 25(a) — \$1,000,000 first violation / \$3,000,000
> per subsequent, AG-exclusive, penalties earmarked to the AG compliance fund; § 18(e) adds a
> \$1,000/day disclosure layer. The NY penalty row is confirmed from primary (ch. 96, L. 2026) — and
> A9449 **repealed and replaced** GBL art. 44-B, moving the violations section from § 1422 to § 1427;
> conform all future NY penalty citations to § 1427. §D.3's "penalties to \$1M/day" for GAAIA remains
> ⚠ secondary (FPF: "\$1 million per violation, with each day treated as a separate violation").
> See chunk 3, §§A–C.
> 
> **UPDATE — completed on two points by chunk 4:** §E.8's retention flag ("⚠ check SB 53/SB 315
> retention at chunk 4") is closed from primary text: SB 53's only retention clause is the five-year
> unredacted-information rule (B&P § 22757.12(f)); SB 315 adds "for as long as a frontier model is
> deployed plus 5 years" for the audit report (§ 10(d)(3)) beside its own five-year redaction shadow
> (§ 10(g)(1)); NY carries the five-year redaction shadow only (GBL § 1421(5)(B)). SEC. 12 is rebuilt
> to [ten] years / deployment+[five] / litigation hold at chunk 4 §E.3. §A's "Records/FOIA (⚠ check)"
> row for NY/IL: retention half closed; the NY FOIL half carries to the cite-check. See chunk 4 §§A.3, B.
> 
> **UPDATE — completed on two points by chunk 5:** §A's CA incident-clock flag ("⚠ confirm 24h
> imminent-risk channel in chaptered text") is closed from the enrolled mirror: Bus. & Prof. Code
> § 22757.13 — reporting within 15 days of discovery, and within 24 hours where the incident poses
> imminent risk of death or serious injury. And §E.9's anticipated provisional-validation bridge is
> built: the CA/NY/IL framework duties enter SEC. 3(c)(4) as legislatively adopted interim
> standards, static, pinned to a date certain, with reading rules disapplying the revenue screens,
> staggers, publication, and third-party-audit modes. See chunk 5 §§B.3, D.2–D.3, E.1.
> 
> **CONSUMED — at chunk 6 (v3.3 assembly):** §E.2's recommended posture (keep compute+designation,
> defend the divergence) and §E.10's one-sentence concordance pitch are executed at v3.3 n.27,
> which also records §E.4's emergency-management co-recipient option; §E.1 and §E.3's "cite the
> siblings" instructions land there too. The NY FOIL half of §A's Records/FOIA row remains on the
> consolidated cite-check (companion).
> 
Audit date: 16 August 2026. Method: web verification against primary and legal-press sources; every parameter below carries a source URL in §G. Items marked ⚠ need a primary-text confirm at the drafting chunk that uses them.

## A. The template family — enacted state frontier-AI statutes

| Parameter | CA — SB 53 / TFAIA (Ch. 138, Stats. 2025) | NY — RAISE Act (Ch. 699, L. 2025, as amended) | IL — AI Safety Measures Act (SB 315) |
|---|---|---|---|
| Signed | 29 Sep 2025 | 19 Dec 2025; chapter amendment (A9449/S8828) signed 27 Mar 2026 | 6 Jul 2026 |
| Effective | 1 Jan 2026 | 1 Jan 2027 | 1 Jan 2027; framework + audit duties 1 Jan 2028 |
| "Frontier model" | Foundation model > 10^26 ops, **including subsequent fine-tuning, RL, and material modifications** | Aligned to CA definitions post-amendment | Foundation model > 10^26 ops |
| Heavy-duty trigger | "Large frontier developer" > \$500M annual gross revenue | > \$500M revenue (amendment replaced compute-cost thresholds) | > \$500M revenue; incident-reporting + whistleblower duties reach **any** frontier developer regardless of revenue |
| Core duties | Publish frontier AI framework; pre-deployment transparency reports; quarterly catastrophic-risk assessment summaries to Cal OES; whistleblower protections incl. anonymous internal channel | Publish safety protocols; incident disclosure; DFS oversight office with rulemaking | Public frontier AI framework; catastrophic-risk plans; incident reporting; whistleblower protections; **mandatory annual independent third-party audits from 1 Jan 2028** (first in the nation) |
| Incident clock | 15 days to Cal OES (⚠ confirm 24h imminent-risk channel in chaptered text) | 72 hours | 72 hours to AG + IEMA-OHS; 24 hours where imminent risk of death or serious physical injury |
| Penalties | Civil, up to \$1M per violation | Civil, up to \$1M first / \$3M subsequent (amendment reduced from \$10M/\$30M) | AG enforcement (⚠ pin amounts from enrolled text) |
| Enforcement | AG | AG; DFS office for oversight | AG; IEMA-OHS administering |
| Records/FOIA | Incident reports, risk assessments, employee reports exempt from CPRA | — (⚠ check) | — (⚠ check) |
| Politics | Wiener bill; successor to vetoed SB 1047 | Hochul signed conditioned on amendments toward the CA model | 110–0 House, 52–5 Senate; OpenAI publicly endorsed, called the three states "a de facto national framework" |

## B. Adjacent enacted state law
- **TX — TRAIGA (HB 149)**, signed Jun 2025, effective 1 Jan 2026. Intent-based prohibited uses (manipulation, discrimination, etc.), regulatory sandbox, AG enforcement with cure period. Different template: use-side, not frontier-development. Useful as proof that red states legislate AI conduct too.
- **CO — SB 24-205**: never took effect. xAI sued 9 Apr 2026 (First Amendment compelled-speech theory, among others); DOJ's AI Litigation Task Force intervened in support — first federal intervention against a state AI law; enforcement stayed by stipulation 27 Apr 2026; **repealed 14 May 2026** by SB 26-189 (Automated Decision-Making Technology Act, narrower disclosure-and-rights regime, effective 1 Jan 2027, 3-year record-keeping, 60-day cure period sunsetting 2030). Central case study for §E.11.
- **CA — no-autonomy-defence law** (⚠ confirm bill number, likely AB 316 (2025)): in an action against a developer/modifier/user of AI alleged to have caused harm, defendant may not assert that the AI autonomously caused the harm; causation/foreseeability/comparative-fault defences preserved. Sibling for the Model Act's refusal to let responsibility evaporate into the system.

## C. EU anchor
**AI Act, Reg. (EU) 2024/1689, arts. 51–55**: GPAI obligations applicable since 2 Aug 2025; systemic-risk presumption at 10^25 FLOPs; art. 53(2) withdraws the open-source exemption above the systemic-risk line — v3.2 n.5's citation confirmed accurate and current.

## D. Federal preemption posture (the weather, as of 16 Aug 2026)
1. **EO 14365** (11 Dec 2025, "Ensuring a National Policy Framework for Artificial Intelligence"): DOJ AI Litigation Task Force to challenge state AI laws (dormant-commerce, preemption, other theories); BEAD-funding leverage against states with "onerous" laws; FCC and FTC directed toward preemptive federal standards; Commerce report identifying targeted state laws (deadline was 11 Mar 2026 — ⚠ check whether published and which laws listed). Consensus of counsel: not self-executing; congressional action required for actual preemption.
2. **White House National Policy Framework** (20 Mar 2026): legislative recommendations urging Congress to preempt state laws imposing "undue burdens."
3. **Great American AI Act of 2026** (Obernolte–Trahan, 269 pp., released 4 Jun 2026, since introduced with four bipartisan cosponsors): federal duties on large frontier developers (\$500M+ revenue — same screen as the states); safety frameworks, twice-yearly independent audits, incident reporting, penalties to \$1M/day; **3-year preemption of state laws "specifically regulating the development" of AI models, sunsetting Dec 2029; states retain regulation of use; savings clauses preserve laws of general applicability, privacy, consumer protection, anti-discrimination, civil rights, and the common law in full.**
4. **FRONTIER Act (H.R. 9925**, Obernolte–Trahan, Jul 2026): tiered transparency/audit/reporting duties; §9: no state may adopt or enforce any law imposing "new substantive obligations on artificial intelligence developers" within a Covered Subject Area, with enumerated carve-outs (incl. protection of minors). As of late Jul: referred to committee, no votes. Broader preemption language than GAAIA.
5. **Warner Senate package** (21 Jul 2026): Secure AI Development Act (mandatory pre-deployment secure testing) and companions — a harder-edged competing architecture; House and Senate frameworks not aligned.
6. **Litigation**: xAI v. Colorado (D. Colo.) as in §B; DOJ intervention model now proven. No suit against SB 53, RAISE, or SB 315 found in this sweep (⚠ re-check at each drafting chunk).

## E. Drift list — v3.2 against enacted law
1. **10^26 lineage-compute trigger: exact match.** SB 53 counts subsequent fine-tuning/RL/material modification into the threshold, as does v3.2 SEC. 1(b)(1). Cite SB 53 and SB 315 in the v3.3 notes; this kills "invented threshold" on contact.
2. **No revenue screen in v3.2 — deliberate divergence to defend, not hide.** All three states pair 10^26 with \$500M for the heaviest duties. Recommended v3.3 posture: keep compute+designation (a criminal due-care duty scales with risk, not revenue; the states' revenue screen rations *compliance-paperwork* cost, which the Model Act doesn't impose until the Agency's standards exist), and say exactly that in a new note.
3. **Incident clocks: v3.2 (72h / 24h imminent / 30d full) sits inside the NY–IL band.** IL's 72h/24h pairing is a near-verbatim sibling of SEC. 9(b). CA's 15 days is the outlier. Cite NY + IL.
4. **Reporting recipients**: states route to AG + emergency-management agencies (Cal OES; IEMA-OHS). Compatible with v3.2's Agency; add a bracketed option naming the state's emergency-management agency as co-recipient.
5. **Penalty anchors now exist**: CA \$1M/violation; NY \$1M/\$3M with a legislated recidivism step — an enacted sibling for v3.2's enhanced-tier architecture. Chunk 3 pins the \$[X] brackets to these. The economic-benefit floor keeps its CWA anchor (no state sibling; federal one suffices).
6. **Whistleblower**: CA/NY/IL protect; none pays. The 10–30% bounty is the Act's genuinely novel state-level element — own it, anchored on Exchange Act §21F's track record. IL's revenue-independent whistleblower coverage is a sibling for extending protection beyond large developers.
7. **Audits**: IL's mandatory annual third-party audit (from 2028) gives SEC. 3(b)'s strongest validation mode an enacted sibling. Major anti-crank asset; a 110–0 vote enacted it.
8. **Records/FOIA**: v3.2 SEC. 12's public-records exemption for security-sensitive material ↔ SB 53's CPRA exemption. Sibling confirmed. Retention: v3.2's 5 years vs CO ADMT's 3 (⚠ check SB 53/SB 315 retention at chunk 4 and harmonise or justify).
9. **Effective-date architecture**: NY (2027) and IL (2027/2028) both stage in. v3.2's standards-conditioned commencement is family-normal; chunk 5's provisional-validation bridge can now name the CA/NY/IL frameworks as interim benchmarks by citation.
10. **The criminal overlay has no AI sibling — and that's the pitch, not the flaw.** Every mechanism in v3.2 except individual criminal liability is now enacted state law somewhere; the overlay itself is eighty years old in food and drug. The concordance note should say precisely this in one sentence.
11. **Preemption exposure map (feeds chunk 2)**: (a) GAAIA preempts *development*-specific rules but saves use-regulation, laws of general applicability, and the common law → v3.3 should make the deployment/use spine the severable-first core, with development duties structured to survive independently or fall alone; (b) FRONTIER §9's "new substantive obligations on developers" is broader → track its carve-outs; consider findings framing the Act as police-power criminal law addressing in-state harm; (c) the proven litigation theory (xAI v. CO) is *compelled speech against disclosure mandates* → v3.2's most speech-shaped elements are SEC. 8 certification and SEC. 9 reporting; chunk 2 adds a note on factual/commercial-disclosure doctrine and the 18 U.S.C. § 1350 pattern's quarter-century of survival; (d) neither federal bill has moved past committee, and EO 14365 cannot preempt by itself — the window for state text is open, which is the Act's whole theory.

## F. Carried questions
For chunk 2: Commerce report contents; any new Task Force filings. For chunk 3: enrolled A9449 penalty text; SB 315 penalty amounts. For chunk 4: SB 53/SB 315 retention periods. Standing: confirm the no-autonomy-defence bill number; monitor FRONTIER Act and GAAIA committee action.

## G. Sources
CA: leginfo.legislature.ca.gov (SB 53 chaptered); fpf.org/blog/californias-sb-53-the-first-frontier-ai-law-explained; mofo.com (1 Oct 2025); whitecase.com; regulations.ai.
NY: wiley.law (New York Finalizes RAISE Act, Apr 2026); joneswalker.com (Jan 2026); mofo.com (Apr 2026); en.wikipedia.org/wiki/Responsible_AI_Safety_and_Education_Act.
IL: dwt.com (Jul 2026); crowell.com (Jul 2026); capitolnewsillinois.com (6 Jul 2026); recordinglaw.com; mcdermottlaw.com.
CO: hunton.com (May 2026); seyfarth.com; nortonrosefulbright.com; carpedatumlaw.com; leg.colorado.gov (SB 24-205, SB25B-004).
Federal: presidency.ucsb.edu (EO 14365 text); whitecase.com (EO analysis); ropesgray.com (Framework, Mar 2026); techpolicy.press + fpf.org + broadbandbreakfast.com + nextgov.com (GAAIA); forbes.com Lance Eliot 27 Jul 2026 + obernolte.house.gov + statt.com (FRONTIER Act H.R. 9925).
TX: wilmerhale.com (TRAIGA reference). CA no-autonomy-defence: bakermckenzie.com (Jun 2026).


---

<a id="chunk-2"></a>
<!-- BEGIN audit/chunk2_preemption_armour.md · sha256:6faedd2deb87 · concatenated 19 Aug 2026, content verbatim -->

# CHUNK 2 — PREEMPTION ARMOUR FOR v3.3

> **UPDATE — amended on two points by chunk 3:** §E.4's SEC. 13(b)(1) and (b)(5) are amended by
> chunk 3 §E.4 — the civil penalty of SEC. 10(a) now severs independently of the criminal penalties
> of SEC. 10(b)–(c), and the SEC. 11 fund moves to a new SEC. 10(f) with a survival clause — use
> chunk 3's text at v3.3 assembly. The four §G carried questions "for chunk 3" are answered at
> chunk 3 §B: A9449 and SB 315 penalty text pinned from enrolled primary; SEC. 10(a) severance
> split adopted; SEC. 5(d) narrowed to statements to this State's own government (the §I.5 caution
> is reduced, not retired — chunk 3 §I.6).
> 
> **UPDATE — answered on one point by chunk 4:** the §G carried question for chunk 4 (SB 53/SB 315
> retention against SEC. 12's five years) is answered at chunk 4 §B from primary text, and SEC. 12's
> periods are rebuilt at chunk 4 §E.3 ([ten] years from creation / [five] after last in-state
> deployment / litigation hold on notice). The §I.3 caution is restated, not resolved: the longer
> periods raise the value of the SEC. 13(c)(2)(C) retention fallback without changing the FRONTIER
> CSA(2)(C) exposure in kind — chunk 4 §D.6, n.23.
> 
Drafting date: 16 August 2026. Method: primary-text verification of every federal vehicle quoted below (govinfo.gov introduced text; the GAAIA discussion-draft PDF on the sponsor's own server; supremecourt.gov slip opinions), doctrinal build, then an adversarial pass in which the draft armour was attacked rather than checked. The attack found more than the check did; §E and §F below are the second draft, and §I records what the first draft got wrong so the same errors are not re-made at v3.4.

Verbatim quotation is used wherever the exact words are load-bearing. Anything not retrieved from primary text is marked ⚠ and paraphrased, never quoted.

This chunk: corrects four errors in chunk 1 (§A); answers the carried questions (§B); pins the operative preemption and savings text of the three federal vehicles (§C); maps v3.2 against them section by section (§D); drafts the armour (§E); supplies new drafting notes (§F); and states honestly where the armour is thin (§I).

---

## A. CORRECTIONS TO CHUNK 1

**A.1 — GAAIA has not been introduced.** Chunk 1 §D.3 records the Great American AI Act as "since introduced with four bipartisan cosponsors." It has not been introduced. As of 16 August 2026 it remains an unnumbered discussion draft released 4 June 2026 by Reps. Obernolte and Trahan — no bill number, no hearing, no markup. The bill that *was* introduced with bipartisan cosponsors is the FRONTIER Act, H.R. 9925 (23 July 2026), which the sponsors describe as a carve-out of the broader GAAIA framework. Consequence: the vehicle with the **narrower** preemption clause and the **wider** savings clause is the one that has not moved; the vehicle with the broader, permanent preemption clause and the conditioned savings clause is the one on the calendar. Chunk 1's threat ranking was inverted.

**A.2 — GAAIA's savings clauses are three, not seven.** Chunk 1 §D.3 lists savings for "laws of general applicability, privacy, consumer protection, anti-discrimination, civil rights, and the common law." The words *privacy*, *consumer protection*, *civil rights*, *discrimination*, *criminal* and *tort* appear **nowhere** in GAAIA Sec. 121. It has three rules of construction, quoted verbatim at §C.2. Those categories are protected only derivatively, if a given law independently qualifies as "of general applicability" or as post-deployment. Chunk 1 reproduced a secondary source's summary of *effect* as enumerated text.

**A.3 — H.R. 5388 is missing from chunk 1 entirely, and contains two criminal carve-outs.** The American Artificial Intelligence Leadership and Uniformity Act, H.R. 5388, 119th Cong. (Baumgartner, 16 September 2025), imposes a five-year state enforcement moratorium, and then exempts criminal law twice over — once by penalty and once by general applicability. See §C.3. It is in subcommittee with no floor action, but its language is the drafting target: it establishes which categories Congress has so far been willing to spare.

**A.4 — The DOJ's actual litigating theory is Equal Protection, not compelled speech.** Chunk 1 §E.11(c) states that "the proven litigation theory (xAI v. CO) is *compelled speech against disclosure mandates*." That is xAI's theory, in a private complaint, on which no court has ruled. The United States' complaint in intervention in *X.AI LLC v. Weiser*, No. 1:26-cv-01515 (D. Colo.), filed 24 April 2026, pleads **two Equal Protection counts** — compelled discrimination, and an authorised "diversity" exemption — and pleads **no First Amendment count and no preemption count**, noting only in passing that the statute "is unconstitutional in other ways too." Nothing has been proven; the enforcement stay is a stipulation. The compelled-speech risk to SEC. 8 and SEC. 9 is real, but it comes from the Ninth Circuit's own AB 587 and AB 2013 line (§F, n.16), not from the Task Force.

---

## B. CARRIED QUESTIONS FROM CHUNK 1, ANSWERED

**B.1 Commerce report under EO 14365 §4 — not published.** The 11 March 2026 deadline passed with the Commerce evaluation, the FTC guidance and the BEAD-linkage rules all incomplete. NTIA postponed the companion non-deployment guidance on 6 March 2026 and as of 30 June 2026 was still "aiming for this summer." No publication appears in any source through August 2026. ⚠ This rests on absence of evidence plus the April reporting; no source affirmatively states "still unpublished in August." One low-reliability tracker asserts publication on 11 March but names no state laws and conflicts with contemporaneous reporting — disregarded. The only state laws named anywhere in this apparatus are named **in the EO itself**: Colorado's AI Act and Texas's TRAIGA. Neither SB 53, RAISE nor SB 315 has been named by any federal instrument.

**B.2 DOJ AI Litigation Task Force — one filing, total.** Established by AG memorandum 9–10 January 2026. Its only confirmed filing is the 24 April 2026 intervention in *xAI v. Weiser* on the Equal Protection theory at §A.4, entered as of right on AG certification of general public importance under Title IX of the Civil Rights Act of 1964. No suit, intervention, or located public threat letter against SB 53, RAISE or SB 315. No federal court has invalidated a state AI law.

**B.3 New instruments since chunk 1.**
- **FTC proposed policy statement**, announced 1 July 2026, published 7 July 2026: "Policy Statement Concerning the Suppression of Accuracy in Artificial Intelligence Systems," docket FTC-2026-0859, comments closed 31 July, Commission vote 2–0. Theory: undisclosed ideological steering of model outputs is deceptive under FTC Act § 5. The Chairman's statement asserts Colorado's AI Act "appears to coerce companies into altering the output of their AI models" and is "impliedly preempted to the extent it conflicts with a federal regulatory scheme." **Proposed only.** Relevance here: the theory targets state laws directing *what a model may say*. This Act directs nothing about model output. It regulates authorisation, monitoring, weight security, and the honesty of statements made to a regulator. SEC. 0(a)(4) below puts that distinction in the findings.
- **FCC**: no preemptive AI action. Its only relevant proceeding is a September 2025 Notice of Inquiry under § 253(a), opposed by 24 state attorneys general in December 2025. The EO's FCC directive runs from publication of the Commerce list, which has not issued.
- **Blackburn Senate package**: circulating since March 2026, **not introduced** as of late July; ⚠ reported to save generally applicable law, common law/tort and sectoral regulation — paraphrase only, no primary text located.
- **NDAA moratorium: dead.** Dropped from the FY26 NDAA, confirmed 3 December 2025. The earlier reconciliation attempt failed 99–1.
- **Warner package** (21 July 2026), including the Secure A.I. Development Act, S. 5061: **no preemption clause and no savings clause**. Silence is not preservation — ordinary conflict-preemption analysis still applies — but there is no express clause to draft around.

**B.4 The one new case that matters.** *Monsanto Co. v. Durnell*, 609 U.S. ___, No. 24-1068 (U.S. June 25, 2026) (Kavanaugh, J., **7–2**; Jackson, J., dissenting, joined by Gorsuch, J.): FIFRA's express clause preempts state failure-to-warn claims requiring warnings the EPA has not mandated. The majority **never invokes the presumption against preemption**, treats agency label approval as creating federal "requirements," and confines *Bates v. Dow Agrosciences LLC*, 544 U.S. 431 (2005), to efficacy claims outside the agency's review. Bad news of a useful kind: once Congress writes an express clause, the clause is read textually, and calling your law "just criminal law" does not save it. **The armour cannot be built on characterisation. It has to be built on landing inside the savings text.**

---

## C. THE THREE VEHICLES — OPERATIVE TEXT

### C.1 FRONTIER Act, H.R. 9925 — introduced 23 July 2026; referred to Energy & Commerce and to Science, Space & Technology; no markup. **The live one. No sunset. No common-law savings clause.**

SEC. 9(b), verbatim:

> "Except as provided in subsection (c), no State or political subdivision of a State may adopt or enforce any law, regulation, order, or other requirement that imposes new substantive obligations on artificial intelligence developers with respect to any Covered Subject Area."

SEC. 9(a), verbatim, in full:

> **(1) Frontier ai risk transparency.** "The disclosure by a developer, to any State, member of the public, or other person, of information regarding—(A) the policies, procedures, frameworks, or practices used by the developer to identify, assess, manage, or mitigate catastrophic risks associated with the development, training, evaluation, or release of an AI model; (B) the results, methodologies, benchmarks, or thresholds of testing, evaluation, or red-teaming of an AI model with respect to catastrophic risks; or (C) the characteristics, capabilities, training, or deployment of an AI model, where the disclosure relates to the assessment, monitoring, communication, or mitigation of catastrophic risks."
>
> **(2) Frontier ai third-party auditing and independent verification.** "The assessment, audit, evaluation, certification, attestation, or verification, by a person other than its developer, of—(A) activities involved in the development, training, evaluation, or deployment of an AI model by such developer that relate to the identification, assessment, management, or mitigation of catastrophic risks; (B) the policies, procedures, frameworks, or practices of such developer relating to the identification, assessment, management, or mitigation of catastrophic risks; or (C) the compliance of such developer with any requirement relating to the development, training, evaluation, or release of an AI model, if such requirement relates to the mitigation of catastrophic risks, including any requirement that such developer obtain certification, attestation, registration, accreditation, or other approval as a condition of, or in connection with, the development, training, evaluation, or release of an AI model, or that such developer provide access to an AI model, model weights, training data, source code, evaluation results, or other technical materials for purposes of any such assessment, audit, evaluation, or verification."
>
> **(3) Frontier ai incident reporting.** "The reporting by a developer to any State, agency, regulator, or other governmental entity of—(A) safety or security incidents involving an AI model, including unauthorized access to or exfiltration of model weights, loss of control over a deployed model, use of a model to cause or materially contribute to catastrophic harm, or material failure of a safety mitigation; or (B) other events involving the development, training, evaluation, or release of an AI model that bear on the potential for the model to cause or materially contribute to catastrophic harm."

SEC. 9(c), verbatim, chapeau and all four paragraphs:

> "Nothing in this section shall be construed to affect the authority of a State or political subdivision of a State to—
> (1) adopt or enforce generally applicable laws, regulations, orders, or other requirements that do not target artificial intelligence developers;
> (2) regulate the use or deployment of AI systems by deployers or users, including via consumer protection, civil rights, contract, criminal, or privacy laws, provided that no substantive obligations are imposed on developers with respect to model development, training, evaluation, or release;
> (3) adopt or enforce laws, regulations, orders, or other requirements specifically relating to the protection of minors from harms arising from the use of AI systems, including requirements addressing sexually explicit content, content promoting self-harm, content facilitating exploitation, age verification, parental controls, or similar matters; and
> (4) adopt or enforce laws, regulations, orders, or other requirements governing the procurement or use of AI systems by State governments."

SEC. 9(d), verbatim: "In this section, the term 'artificial intelligence developer' means—(1) an entity that builds, designs, codes, produces, trains, or owns an artificial intelligence model or models for internal use or for use by a third party; and (2) does not include an entity that is solely a deployer of the artificial intelligence model."

**Five features control the drafting, three of them adverse.**

*Adverse.* First, **CSA(1)(C) reaches disclosure about "deployment"** where it relates to catastrophic-risk assessment, monitoring, communication or mitigation. Second, **CSA(3)(A) names "loss of control over a deployed model"** — v3.2 SEC. 9(a)'s second listed incident, almost verbatim, and expressly a *deployed*-model event. Third, **CSA(2)(C) reaches any requirement that a developer obtain "certification, attestation, registration, accreditation, or other approval as a condition of, or in connection with, the development, training, evaluation, or release"** — which is the direct textual answer to any attempt to convert a development duty into a condition. Together these mean **the "post-deployment is safe" thesis does not hold under FRONTIER.** It holds under GAAIA; it does not hold here.

*Favourable.* Fourth, **§9(b) reaches only obligations on *developers*, and §9(d)(2) excludes an entity that is "solely a deployer."** A duty imposed on a person in the capacity of a non-developer provider or deployer is outside §9(b) entirely — no savings clause needed. Fifth, **CSA(2) reaches only assessment "by a person other than its developer."** Internal attestation is outside CSA(2) altogether. And every CSA is keyed to **catastrophic risks**; a duty keyed to unauthorised access, operator control, or honesty to a regulator is not automatically within one.

Two further features: **"new substantive obligations" is undefined** anywhere in the section, and §9(c)(2)'s criminal savings is doubly conditioned — it runs only to regulation of use or deployment "**by deployers or users**," and only "*provided that no substantive obligations are imposed on developers with respect to model development, training, evaluation, or release*." That proviso is a poison pill: on one reading, a single developer-side duty anywhere in the Act forfeits the carve-out for the whole Act. SEC. 13(c)(1) below is drafted against precisely that reading.

### C.2 GAAIA discussion draft (4 June 2026; not introduced). Sec. 121, "Federalization of State Laws Regulating Artificial Intelligence Model Development."

Sec. 121(b), verbatim:

> "No State or political subdivision thereof may establish, continue in effect, or enforce any law or regulation specifically regulating the development of any artificial intelligence model."

Sec. 121(c), verbatim, all three rules of construction:

> "(1) GENERAL APPLICABILITY.—Nothing in this section preempts any State law or regulation of general applicability, or abridges or alters any remedy existing under the common law of any State.
> (2) POST-DEPLOYMENT ACTIVITIES.—Nothing in this section preempts any State law or regulation applicable to activities occurring upon or after the deployment of an artificial intelligence model, including any law or regulation governing the implementation, deployment, distribution, offering, or use of any artificial intelligence system, product, or service that incorporates or is derived from an artificial intelligence model.
> (3) STATE AUTHORITY UNDER THIS ACT.—Nothing in this section preempts the exercise of any authority granted to a State, State Attorney General, or other State officer under this Act, or any State law authorizing, governing, or supporting the exercise of such authority, including provisions governing the handling of information received under this Act."

Sec. 121(d), verbatim: "This section shall cease to have effect 3 years after the date of enactment of this Act, unless Congress acts to reauthorize it prior to that date." The sunset runs from enactment, not to a fixed date; chunk 1's "Dec 2029" was press extrapolation from an assumed late-2026 passage. Delete the date, keep the mechanism.

Sec. 121(e), verbatim: "development" means "the acts performed or directed by a developer with respect to an artificial intelligence model prior to its deployment, including determining training or fine-tuning objectives; training, fine-tuning, or otherwise substantially modifying the weights or other parameters of an artificial intelligence model; and evaluating and deciding, prior to deployment, whether an artificial intelligence model satisfies applicable safety or capability thresholds for deployment."

**(c)(2) is the widest savings clause in the field** — it saves any state law "applicable to activities occurring upon or after the deployment," expressly including laws governing "the implementation, deployment, distribution, offering, or use." **(e) is the widest development definition**, and it captures "evaluating and deciding, prior to deployment, whether an AI model satisfies applicable safety or capability thresholds for deployment" — a description of v3.2 SEC. 3(b). The two clauses collide over this Act. §I.1 states honestly how far the drafting can and cannot resolve that collision.

Note also that Sec. 121's preemption is **not limited by GAAIA's own revenue thresholds** (>\$50M "frontier developer"; >\$500M "large frontier developer"; ⚠ internal section numerals for these definitions are the weakest citation in this chunk). Federal duties reach only the large tier; preemption reaches state regulation of everyone. That asymmetry is the structural complaint a state AG should make in comment.

### C.3 H.R. 5388 (Baumgartner, 16 September 2025; subcommittee, no floor action).

Five-year moratorium on state enforcement of any law "limiting, restricting, or otherwise regulating artificial intelligence models … entered into interstate commerce," with **two** criminal carve-outs:

> § 6(a)(2)(B): the moratorium does not apply to "any provision of a law or regulation to the extent that the violation of such provision carries a criminal penalty."

> § 6(b): "Nothing in this section shall be construed to preempt generally applicable criminal laws of a State or political subdivision thereof."

> § 7(2): the Act does not limit "enforcement of generally applicable, technology-neutral criminal laws or other authorities otherwise provided by law."

§ 6(a)(2)(B) is the better clause and the better drafting target: it turns on the **penalty attached**, not on general applicability, and would therefore save this Act's criminal provisions whether or not they are AI-specific. It is the **only unconditional criminal savings text in the field** — FRONTIER §9(c)(2) names criminal law but conditions it away; GAAIA does not name it at all.

Doctrinally, a moratorium drafted as a prohibition on state *enforcement*, conferring no federal rights on private actors and imposing no federal restrictions on them, is the *Murphy v. NCAA*, 584 U.S. 453 (2018), problem in its purest form. Strategically that is a bonus, not a plan: Congress cures *Murphy* by pairing preemption with a real federal regime, which is what GAAIA and FRONTIER do. Assume the cure.

### C.4 Composite screen

| | H.R. 5388 | GAAIA §121 | FRONTIER §9 |
|---|---|---|---|
| Status | subcommittee | not introduced | **introduced, referred** |
| Trigger | regulating AI models in interstate commerce | law "specifically regulating the **development**" | "new substantive obligations on **developers**" in a Covered Subject Area |
| Duration | 5 years | 3 years from enactment | **permanent** |
| Reaches duties on non-developer deployers | yes | only pre-deployment | **no — outside §9(b)** |
| General-applicability savings | yes | yes | yes, but only laws "that do not target AI developers" |
| Common-law savings | — | **yes, express** | **none** |
| Criminal savings | **yes — §6(a)(2)(B) unconditional; §6(b) general applicability** | none (derivative only) | only use/deployment by deployers or users, conditioned on no developer-side duties re development, training, evaluation, release |
| Post-deployment savings | — | **yes, broad** | partial only — CSA(1)(C), (2)(A), (3)(A) reach deployment |
| Officer/individual liability | unaddressed | unaddressed | unaddressed |

**The lanes.** No single category is safe across all three. Four are safe across all three, and they are narrower than chunk 1 assumed:

1. **Duties borne by a person in the capacity of a non-developer provider or deployer.** Outside FRONTIER §9(b) by its own terms; inside GAAIA §121(c)(2); inside H.R. 5388's criminal carve-outs.
2. **Offenses of false statement to a regulator.** Not a Covered Subject Area — CSA(1) is *disclosure of risk information*, not veracity — and generally applicable criminal law in every state.
3. **Generally applicable criminal law**, and, under H.R. 5388, any provision carrying a criminal penalty.
4. **Record creation and retention without a reporting duty**, subject to the caveat at §I.3.

Everything else — the developer-side pre-release duties, the third-party validation modes, SEC. 8, SEC. 9 — is drafted on borrowed time. The armour's job is to put as much of the Act into those four categories as honestly possible, to make the rest sever cleanly *without taking the elements of the surviving offenses with it*, and to ensure that what is preempted is **suspended rather than repealed**, so it revives when a three-year sunset expires or a moratorium lapses.

---

## D. COLLISION MAP — v3.2 SECTION BY SECTION

Tiers below are the tiers of the SEC. 13(b) ladder as enacted at §E.4. There is one taxonomy, not two. "Predicate" marks a provision that supplies an element of a tier-1 offense and is therefore preserved to that extent by SEC. 13(b)(5) however far the ladder is descended.

| v3.2 provision | GAAIA §121 | FRONTIER §9 | Tier |
|---|---|---|---|
| SEC. 1(a) Morissette classification | definitional | definitional | 1, predicate |
| SEC. 1(b)(1)–(8) definitions | definitional | definitional | 1, predicate |
| SEC. 1(b)(9) release = deployment; pre-release duties | (c)(2) helps: release is deployment | pre-release duty on a developer; §9(c)(2) proviso names "release" | 3 as to the developer-capacity duty; 1 as to the definitional rule |
| SEC. 1(c) jurisdiction | neutral | neutral | 1, predicate — amended at §E.1 |
| SEC. 2, duty of a person in developer capacity (model evaluation, weight security, pre-release evaluation) | (e) "evaluating and deciding, prior to deployment" | CSA(2)(C) "as a condition of … development, training, evaluation, or release" | **3** |
| SEC. 2, duty of a person in provider or deployer capacity (configuration, tools, permissions, monitoring) | (c)(2) post-deployment | outside §9(b): obligation not on a developer | **1** |
| SEC. 2, duty of each controlling person as to the authority that person holds | follows the capacity engaged | follows the capacity engaged | follows; 1 where the capacity is provider or deployer |
| SEC. 3(a) Agency standards | saved as applied to deployment | hit as applied to developers in a CSA | **1, predicate** — supplies the content of SEC. 5(a) and 5(b) |
| SEC. 3(b) internal attestation mode | (e) risk | **outside CSA(2)**: "by a person other than its developer" | **1, predicate** |
| SEC. 3(b) independent audit, accredited certification, Agency approval | (e) risk | **CSA(2)(A) and (2)(C)** | **3** |
| SEC. 3(b) validation attaches to an identified version and configuration; a model validated without tools is not validated for tool-granting configurations | definitional | definitional | 1, predicate |
| SEC. 3(c) commencement; absence of validation is an element | — | — | **1, predicate — the fair-notice provision; never severable while any offense stands** |
| SEC. 5(a) deploying without validation | **(c)(2): the regulated act is deployment** | predicate duty may be developer-side | 1 as to deployment or expansion by a provider or deployer; 3 as to release by a developer |
| SEC. 5(b) operating with autonomous external access without prescribed controls | (c)(2) operation | outside §9(b) where the actor is a provider or deployer; not a CSA | **1 — the strongest provision in the Act** |
| SEC. 5(c) failure to report | (c)(2) arguable | **CSA(3)** | **4** |
| SEC. 5(d) false statement to the Agency or any regulator | general false-statement law | not a CSA: CSA(1) is disclosure of risk information, not veracity | **1** |
| SEC. 4 controlling persons; SEC. 6 individual liability | unaddressed by any vehicle | unaddressed | **1, predicate** |
| SEC. 6(b) enhanced tier; SEC. 10(c)(2) harm tier | unaddressed | unaddressed | **1** |
| SEC. 7(a) clawback | remedy against a natural person | not a CSA | 1 |
| SEC. 7(b) anti-indemnification — a prohibition on **entities**, voiding contracts | not a development rule | not a CSA | 1 |
| SEC. 8 CEO certification | (e) pre-deployment evaluation and decision | **CSA(1)(A) and (1)(B)**; CSA(2)(C) if third-party attested | **4 — and the First Amendment target** |
| SEC. 9(a) incident definitions, incl. weight exfiltration and loss of operator control | (c)(2) arguable for deployed systems | **CSA(3)(A), named almost verbatim** | **4** |
| SEC. 9(b) clocks | as above | CSA(3) | 4 |
| SEC. 10(a)–(b) penalties | remedial; follows the underlying duty | remedial | follows the duty; 1 as to tier-1 offenses |
| SEC. 10(d) injunction, suspension, disqualification, debarment | post-deployment relief | relief, not an obligation in a CSA | 1 |
| SEC. 11 whistleblower award, anti-gag, anti-retaliation | not a development rule | not an obligation on a developer in a CSA; the anti-gag clause is arguable | 2 |
| SEC. 12 limitations periods, transition, no retroactivity, successor liability | machinery | machinery | **1, predicate** — a criminal statute cannot operate without its limitations period |
| SEC. 12 records retention, 5 years | retention is not disclosure | retention is not a report; ⚠ but see CSA(2)(C) "provide access to … evaluation results" and §I.3 | 2 |
| SEC. 12 public-records confidentiality | machinery | machinery | 2 — amended at §E.3(c) |

Three conclusions. **First**, v3.2's criminal spine is better armoured than its drafters claimed: SEC. 5(a), 5(b) and 5(d) are offenses of deploying, operating and lying, not of developing — and SEC. 5(b) and 5(d), borne by a provider or deployer, sit outside FRONTIER §9(b) altogether. **Second**, the exposure is concentrated in the disclosure and third-party-validation limb — SEC. 3(b) audit modes, SEC. 5(c), SEC. 8, SEC. 9 — which is simultaneously the FRONTIER target and the First Amendment target. Not a coincidence: the federal bill was drafted around the same three state duties the litigation targets. **Third**, v3.2's severability clause is one sentence at the end of SEC. 12 — "If any provision or application is held invalid, the remainder stands" — while the README and the WHY page both assert that "the criminal core is the remainder built to stand." **The claim is in the rhetoric, not the statute.** No court reading SEC. 12 would know which part is the core, or that SEC. 3 must survive for SEC. 5 to mean anything. Putting that into operative text is this chunk's central deliverable.

---

## E. THE ARMOUR — DROP-IN TEXT FOR v3.3

Placement note. **SEC. 0 should be enacted as an uncodified findings section** — in the bill, outside the code: findings do characterisation work without creating duties, and an uncodified section is not readily the "law or regulation" a preemption clause operates on. **SEC. 13 must be codified**, because its clauses operate. At v3.3 assembly, either style SEC. 0 as "SECTION 1. FINDINGS AND PURPOSE (uncodified)" with a global renumber, or keep the SEC. 0 style and let each state's legislative counsel conform. Do not renumber SEC. 1–12 in this repository without conforming every cross-reference in the drafting notes and the regulations draft.

### E.0 — new SEC. 0. FINDINGS AND PURPOSE (uncodified)

> (a) The Legislature finds:
>
> (1) Covered systems are deployed to, operated within, and made available to residents of this State, and the deaths, injuries, intrusions and losses this Act addresses occur to persons and property within this State.
>
> (2) The protection of persons within this State from death and serious injury, and the punishment of those whose failures of care cause it, is among the oldest and most traditional exercises of this State's police power, and is the same power by which this State punishes homicide, reckless endangerment, the endangerment of the public by the sale of adulterated or unsafe goods, and false statements made to its own officers.
>
> (3) The duties this Act imposes arise from the deployment, material expansion, release, or operation of a covered system in or into this State, or from conduct in this State in relation to such a system. This Act imposes no duty on any person by reason of research, training, or development that neither occurs in this State nor concerns a covered system deployed or released in or into this State.
>
> (4) No provision of this Act requires any person to express, adopt, endorse, or refrain from expressing any opinion, characterization, viewpoint, or contested position, or to alter the output of any covered system. The statements this Act requires are statements of fact within the knowledge of the person making them, made to a regulator.
>
> (5) This Act draws no distinction between persons within and persons outside this State. It confers no advantage on any in-state person and imposes no obligation on an out-of-state person that it does not impose on an in-state person engaged in the same conduct with respect to the same system.
>
> (6) The obligations this Act imposes are, in substance, the obligations that responsible developers, providers, and deployers of covered systems already represent that they discharge, and the incremental burden of compliance is small in relation to the revenues of the persons on whom it falls.
>
> (7) This Act supplements and does not displace the generally applicable criminal and civil law of this State, which applies to conduct concerning covered systems as it applies to all other conduct.
>
> (b) Purpose. The purpose of this Act is to place personal responsibility for the safety of covered systems deployed, operated, or released in or into this State upon the natural persons who hold practical authority over them, on the doctrine of *United States v. Park*, 421 U.S. 658 (1975), by means that operate upon private conduct occurring in or directed into this State.

Findings (3) and (5) are drafted to be **true against the operative text as amended at §E.1**, which the first draft's versions were not: the earlier "a person who does not make a covered system available to residents of this State incurs no duty" was false against SEC. 1(c)'s retained conduct prong, and "applies identically to persons within and outside this State" was false because an in-state person is reachable on conduct alone. A finding a challenger can falsify by reading the next page is worse than no finding.

### E.1 — amendment to SEC. 1(c) JURISDICTION

> (c) Jurisdiction. This Act applies to conduct occurring in this State, to covered systems made available to residents of this State, and to conduct intended to produce and producing substantial effects within this State. **Conduct occurring outside this State is relevant under this Act only as evidence bearing on an element of an offense committed in or into this State. No person incurs a duty under this Act by reason of conduct that neither occurs in this State nor concerns a covered system deployed, released, or made available in or into this State. A person who does not deploy a covered system in or into this State, does not make it available to residents of this State, and does not release its weights, is not subject to this Act as to that system.**

The withdrawal provision is drafted as a statement of what the Act does not reach, not as a "commercially reasonable measures" safe harbour. The first draft's safe harbour was incoherent as applied to a weight release — SEC. 1(b)(9) defines release as making weights available outside the releasing entity's control, and no measure prevents their availability in one State — and would have handed every releasing defendant a free argument.

### E.2 — amendment to SEC. 2

Set out in full; no ellipsis. Struck text is not reproduced, inserted text is bold. The clause allocating duties to "each controlling person as to the exercise of the authority that person holds" is **retained** — it is the hook that reaches the controlling shareholder and the parent-entity fold, which is the whole point of SEC. 4 and drafting note n.4.

> **SEC. 2. PUBLIC WELFARE DUTY.** No covered system may be deployed **in or into this State**, or materially expanded, unless each controlling person has exercised due care to ensure the system's compliance with the safety, authorization, monitoring, incident-reporting, and deployment standards applicable under SEC. 3. **A duty under this Act arises upon, and by reason of, the deployment, material expansion, release, or continued operation of a covered system in or into this State, and not otherwise.** Each duty under this Act attaches to the actor who controls the relevant risk: the developer as to model evaluation and weight security; the provider and deployer as to configuration, tools, permissions, and monitoring; the releasing provider as to pre-release evaluation — including evaluation of the model as it can be modified, such as by removal of safeguards or fine-tuning within a rule-specified compute budget — tamper-resistance assessment, and weight security up to the moment of release; each controlling person as to the exercise of the authority that person holds.

Note what is **not** done. The first draft added "or released" to the opening prohibition and extended the duty to "the developer who deploys, or whose covered model is deployed or released." Both were errors. SEC. 1(b)(9) already provides that "a release is a deployment of a covered system for purposes of this Act"; listing release disjunctively alongside deployment creates a negative implication that "deployment" elsewhere in the Act — including SEC. 5(a) — *excludes* release, which would gut SEC. 1(b)(9). And extending the SEC. 2 duty expressly to developers with respect to release states, in terms, the developer-side release obligation that FRONTIER §9(c)(2)'s proviso is drafted to punish. The definitional route reaches the same conduct without the concession.

The first draft also added: "Nothing in this section imposes any duty with respect to the training, fine-tuning, evaluation, or modification of a model that is not deployed or released in or into this State." That is a negative pregnant — it concedes that the Act *does* impose duties with respect to training, fine-tuning and evaluation of models that are deployed here, which is the exact list in GAAIA §121(e). It is replaced by the affirmative arising-clause above, which says when a duty arises without enumerating what it governs.

### E.3 — the disclosure limb

**(a) SEC. 8, add:**

> **The certification consists of statements of fact within the certifying person's knowledge after reasonable inquiry. No person is required by this section to characterize, opine upon, or adopt any position concerning the capabilities, risks, or merits of any model or system, and a certification disclosing identified noncompliance satisfies this section. A certification is made to the Agency and is not required to be published.**

**(b) SEC. 9, add as new subsection (c):**

> **(c) A report under this section may consist of the facts known to the reporting person at the time of the report. No person is required to characterize an event, to state a conclusion as to causation or risk, or to adopt any contested description; the obligation is discharged by a timely statement of the facts then known, supplemented as required by subsection (b). A report is made to the Agency and is not required to be published.**

**(c) SEC. 12, amend the confidentiality clause.** This is necessary, not optional. v3.2 exempts SEC. 8, SEC. 9 and SEC. 3 material from the state public-records act only "**to the extent they contain security-sensitive information**." A bare certification of compliance, or a report that a system lost operator control, contains none — so on the present text it is fully disclosable, and the whole *NIFLA* answer at n.16 (these are confidential statements to a regulator, not conscription into public debate) collapses. Amend so the **documents** are categorically exempt while the **facts** remain fully discoverable, which preserves v3.2's deliberate choice to shelter nothing from plaintiffs:

> …confidentiality of reported material as follows: reports under SEC. 9, certifications under SEC. 8, and validation materials under SEC. 3 **are exempt from disclosure under [the State public-records act], and to the extent they contain security-sensitive information — including information that would materially assist unauthorized access to model weights or covered systems — shall be maintained under seal in any proceeding**; this exemption does not limit access by the Agency, the Attorney General, or a court under seal, **does not exempt any person from any obligation to disclose under any other law**, does not create any privilege for underlying facts, which remain subject to discovery and subpoena from any source, and does not restrict any use of any material in an enforcement proceeding under this Act.

**(d) SEC. 9(a), recast the two characterization-shaped triggers.** "Deception of safety or monitoring controls by a covered system" and "a reproducible evaluation finding of materially increased risk" both require the reporting person to apply a contested label — the defect that took AB 587 outside *Zauderer* in *X Corp. v. Bonta*. Recast as objective events: that the system's representations to a monitoring or safety control differed from its actions; that an evaluation produced a result meeting a threshold specified by rule. ⚠ The full recast belongs to chunk 5 — it interacts with the regulations draft's evaluation Part, and the threshold must come from the Agency, not from the reporter's judgment.

### E.4 — new SEC. 13. SEVERABILITY, CONFORMING OPERATION, AND REVIVAL

Delete the last sentence of SEC. 12 ("If any provision or application is held invalid, the remainder stands") and insert:

> **SEC. 13. SEVERABILITY, CONFORMING OPERATION, AND REVIVAL.**
>
> **(a) Severability.** The provisions of this Act are severable. If any provision, or any application of any provision to any person, capacity, class of persons, or circumstance, is held invalid or unenforceable, the holding does not affect any other provision or application that can be given effect without it, and this Act shall be construed and enforced to the maximum extent it may lawfully operate.
>
> **(b) Order of severance.** Where a court can preserve the operation of this Act by severing a narrower provision or application rather than a broader one, it shall do so, and shall sever later-listed matter before earlier-listed matter:
>
> (1) *First rank.* The offenses under SEC. 5(b) and SEC. 5(d); the offense under SEC. 5(a) as applied to the deployment (otherwise than by release), material expansion, or continued operation of a covered system in or into this State; SEC. 4 and SEC. 6; the remedies of SEC. 7 and SEC. 10 as applied to those offenses; the duties of SEC. 2 as applied to a person in that person's capacity as a provider or deployer; and SEC. 1, SEC. 3(a), SEC. 3(c), and the provisions of SEC. 12 governing limitations, transition, retroactivity, and successor liability.
>
> (2) *Second rank.* SEC. 11; the remaining provisions of SEC. 12.
>
> (3) *Third rank.* The duties of SEC. 2 and SEC. 3 as applied to a person in that person's capacity as a developer, including pre-release evaluation and weight security; SEC. 5(a) as applied to a release; the validation modes of SEC. 3(b) requiring assessment by a person other than the developer.
>
> (4) *Fourth rank.* SEC. 8; SEC. 9; SEC. 5(c).
>
> (5) *Preservation of elements.* No provision shall be severed to an extent that deprives a surviving offense of an element, a definition, a standard, a limitations period, or a commencement condition on which that offense depends. A provision of a later rank that supplies such matter to an offense of an earlier rank continues in effect for that purpose notwithstanding its severance for every other purpose. In particular, SEC. 3(a) and SEC. 3(c) continue in effect to supply the content of, and the commencement condition for, any surviving offense under SEC. 5.
>
> (6) *Declared intent.* The Legislature declares that it would have enacted the provisions of each rank irrespective of the invalidity of any later rank, and specifically that it would have enacted the first rank, together with the matter preserved to it by paragraph (5), had it known that no later rank could take effect.
>
> **(c) Conforming operation.** (1) The Attorney General shall, by order published in [the State register], determine whether and to what extent any Act of Congress, or any regulation having the force of law, preempts the application of any provision of this Act. Upon publication, the provision is suspended to the extent, and only to the extent, stated in the order. A provision is suspended under this subsection only by such an order, or by a final judgment no longer subject to appeal in a proceeding to which this State was a party; and a suspension applies only to conduct occurring after the date of publication of the order or of notice of the judgment.
>
> (2) In making a determination under paragraph (1), the Attorney General shall preserve the operation of this Act to the greatest extent lawfully available, and shall have regard to the following, which are stated as directions to the Attorney General and not as conditions of any person's liability:
>
> (A) where the federal enactment conditions the preservation of State authority upon the absence of obligations imposed on developers with respect to the development, training, evaluation, or release of a model, the order shall suspend the duties of this Act as applied to persons in the capacity of a developer with respect to those matters, and shall preserve them as to every other person, capacity, and matter;
>
> (B) where the federal enactment reaches only laws regulating conduct prior to deployment, the order shall preserve this Act as applied to conduct occurring upon or after deployment;
>
> (C) where the federal enactment reaches a duty to report or to certify to the Agency, the order shall preserve the obligation, under SEC. 12, to create and retain the records that would have supported the report or certification, and those records shall be produced upon lawful process; and
>
> (D) where the federal enactment reaches only laws that target developers of artificial intelligence models, the order shall so state, and nothing in this Act limits the application to any person of the generally applicable criminal law of this State, including the law of homicide, reckless endangerment, endangerment by unsafe or adulterated goods, and false statement to a public officer, which applies to conduct concerning covered systems as it applies to all other conduct.
>
> (3) No person may be convicted of an offense under this Act for conduct occurring during a period in which the provision creating the offense stood suspended under this subsection.
>
> **(d) Revival.** A provision suspended under subsection (c) is not repealed. The Attorney General shall, within [30] days after the expiration, sunset, non-reauthorization, repeal, or judicial invalidation of the federal enactment stated in the order, or after a final judgment no longer subject to appeal determining that the enactment does not preempt the provision, publish an order terminating the suspension. The provision resumes operation on the date of publication of that order and applies to conduct occurring on or after that date. No person is liable under a provision for conduct occurring before that date.
>
> **(e) No inference.** A suspension under subsection (c) is not evidence that the suspended provision was invalid, and does not affect liability for conduct occurring before the suspension took effect.

**Why (c) and (d) are drafted through a published Attorney General's order rather than self-executing.** A criminal statute whose coverage turns on each defendant's own resolution of an unlitigated federal preemption question is void for vagueness in its most serious form — the defendant cannot determine whether the offense exists, let alone what it forbids. *Connally v. General Construction Co.*, 269 U.S. 385, 391 (1926); *Kolender v. Lawson*, 461 U.S. 352, 357–58 (1983). A first draft of this section triggered suspension on the words "preempts **or would preempt**," self-executing, with no adjudicative anchor; it also revived liability on a federal court's ruling in a case the defendant was not party to, up to thirty days before the State's own published record caught up — *Bouie v. City of Columbia*, 378 U.S. 347 (1964), territory. Both are cured by making the published order the operative instrument and by making publication the condition of both suspension and revival, with prospective effect in each direction.

The order mechanism also cures a self-inflicted wound. v3.2 SEC. 3(a) forbids dynamic incorporation of external standards — "no amendment to an incorporated standard takes effect in this State until the Agency adopts it by the same procedure" — and drafting note n.3 states the principle as a constitutional commitment on the authority of *Sunshine Anthracite Coal Co. v. Adkins*, 310 U.S. 381 (1940). A conforming-operation clause that let future Acts of Congress reshape a *criminal* prohibition with no State adoption step would do to SEC. 5 exactly what n.3 disclaims doing to SEC. 3, and the opposing brief would write itself out of the Act's own notes. The published order **is** the State adoption step. Several state constitutions independently forbid adoption of future federal enactments by reference; this drafting avoids that objection too.

### E.5 — placement instruction for adopting states

Codify **SEC. 4, SEC. 5, SEC. 6, SEC. 7 and SEC. 10** in the state's **penal code**, among the offenses against the person and against public safety, and not in a new artificial-intelligence title. The penalties must travel with the offenses. Codify **SEC. 1, SEC. 2, SEC. 12 and SEC. 13** with them, so that the definitions, the duty, the limitations periods and the severability rules sit in the same chapter as the offenses they govern. Codify **SEC. 3, SEC. 8, SEC. 9 and SEC. 11** in the administrative title.

One caveat to state plainly: this split leaves SEC. 3 — which supplies the content of SEC. 5(a) and SEC. 5(b) — in an AI-specific administrative chapter, so a court asking whether this is "generally applicable criminal law" will find an offense whose substance is defined by an AI regulatory chapter. Placement helps; it does not convert an AI-specific statute into a generally applicable one, and no drafting can. That is why SEC. 13(c)(2)(D) preserves the general criminal law as a separate route rather than relying on recharacterising this one.

Where the state's penal code already contains reckless endangerment, omission liability, corporate-officer liability, or false-statement-to-a-public-servant provisions, draft SEC. 6 as an application of those provisions rather than as a free-standing regime. ⚠ Note also what SEC. 13(c)(2)(D) does and does not do: it preserves the general criminal law, which needs no preservation; it cannot *supply an element* of a homicide or false-statement offense in another Act. A legislative finding in this Act cannot expand the reach of another. The value of (D) is that it forecloses an argument that this Act occupies the field by implication and displaces the general law — not that it creates a fallback prosecution the general law would not otherwise support.

---

## F. NEW DRAFTING NOTES

**n.13 ON PREEMPTION ARCHITECTURE.** Three federal vehicles exist and none has been enacted: H.R. 5388 (Sept. 2025, subcommittee), the GAAIA discussion draft (June 2026, not introduced), and the FRONTIER Act, H.R. 9925 (July 2026, introduced and referred, no markup). Their savings clauses agree on four categories: duties borne by a person in the capacity of a non-developer provider or deployer; offenses of false statement to a regulator; generally applicable criminal law, and under H.R. 5388 § 6(a)(2)(B) any provision carrying a criminal penalty; and record creation and retention unaccompanied by a duty to report. This Act's first-rank offenses are drafted into those categories: SEC. 5(b) and SEC. 5(d) are offenses of operating and of lying, borne by whoever operates and whoever speaks. What is *not* claimed, because the text will not bear it, is that post-deployment conduct is safe across the board — FRONTIER CSA(1)(C), CSA(2)(A) and CSA(3)(A) reach deployment expressly, and CSA(2)(C) reaches requirements imposed "as a condition of" development, training, evaluation or release. Preemption clauses of this kind are read textually and a State's characterisation of its own statute will not defeat one: *Monsanto Co. v. Durnell*, 609 U.S. ___, No. 24-1068 (U.S. June 25, 2026) (express clause; presumption against preemption not invoked; *Bates v. Dow Agrosciences LLC*, 544 U.S. 431 (2005), confined). Characterisation does its work on the other side of the clause — in the savings text — which is why SEC. 0 is drafted to the words those clauses use.

**n.14 ON STATE CRIMINAL LAW.** *Kansas v. Garcia*, 589 U.S. 191 (2020), is the load-bearing authority: an express clause reaching employers was "plainly inapplicable" to the prosecution of employees; "criminal law enforcement has been primarily a responsibility of the States, and that remains true today"; and mere overlap between state and federal law "does not even begin to make a case for conflict preemption." *Chamber of Commerce v. Whiting*, 563 U.S. 582 (2011), is the companion on savings-clause construction. The counterweight is stated honestly: *Arizona v. United States*, 567 U.S. 387 (2012), field-preempted a state criminal alien-registration offense and conflict-preempted a state unauthorized-work offense. State criminal law is not immune; it is reached last, and only where Congress has occupied a field or made a deliberate decision not to punish. Neither has occurred. The presumption against preemption is not relied upon: it survives for implied preemption (*Wyeth v. Levine*, 555 U.S. 555 (2009)) but not, in most circuits, for express clauses after *Puerto Rico v. Franklin California Tax-Free Trust*, 579 U.S. 115 (2016). The textual authority is *Virginia Uranium, Inc. v. Warren*, 587 U.S. 761 (2019) (plurality opinion) — preemption is "a serious intrusion into state sovereignty" (quoting the *Medtronic, Inc. v. Lohr*, 518 U.S. 470, 488 (1996), plurality), and preemptive purpose must be found in text and structure, not "abstract and unenacted legislative desires." Both propositions come from an opinion for three Justices; three more concurred only in the judgment and expressly declined the reasoning. Cite it as persuasive, never as holding.

**n.15 ON SEC. 13.** Four mechanisms. The *ladder* in (b) converts the claim on this Act's own cover — that the criminal core is the remainder built to stand — into text a court can apply; a severability clause that does not say what the core is leaves the choice to the party bringing the challenge. The *preservation of elements* rule in (b)(5) is what makes the ladder coherent: SEC. 5(a) and SEC. 5(b) draw their content from SEC. 3, and a ladder that ranked SEC. 3 below them would instruct a court to sever the elements of the offenses it declares untouchable, leaving either a void prohibition or a standardless one. The severability question is whether the remainder is "fully operative as a law," *Alaska Airlines, Inc. v. Brock*, 480 U.S. 678, 684 (1987), and a declaration of legislative intent does not answer it; (b)(5) answers it. *Conforming operation* in (c) makes the Act self-narrowing to the shape of whatever savings clause Congress enacts, through a published Attorney General's order rather than by self-execution, for the fair-notice and non-delegation reasons set out at §E.4; (c)(2)(A) is drafted against the FRONTIER §9(c)(2) proviso, which conditions its criminal savings on the absence of developer-side duties and would otherwise let one such duty forfeit the carve-out for the whole statute. *Revival* in (d) answers the sunset: GAAIA §121(d) expires three years after enactment and H.R. 5388's moratorium runs five, so a preempted provision is suspended, not repealed, and resumes by published order. Contingent legislation is ordinary in the civil and administrative setting; contingent *criminal* legislation is not, and no authority has been located for it — which is the reason the trigger is an order of a State officer, published prospectively, rather than an external event operating of itself. Compare, on the other side of the line, *Murphy v. NCAA*, 584 U.S. 453 (2018): Congress may not command a State not to legislate, and "every form of preemption is based on a federal law that regulates the conduct of private actors, not the States." That answers a bare moratorium; it does not answer preemption paired with a real federal regime, and this Act does not depend on it.

**n.16 ON SEC. 8 AND SEC. 9 UNDER THE FIRST AMENDMENT.** The line is *Zauderer v. Office of Disciplinary Counsel*, 471 U.S. 626 (1985), as narrowed by *NIFLA v. Becerra*, 585 U.S. 755 (2018), which preserved "health and safety warnings long considered permissible" and "purely factual and uncontroversial disclosures about commercial products." Compelled disclosure runs into trouble when it forces the speaker to adopt a contested characterization: *X Corp. v. Bonta*, 116 F.4th 888 (9th Cir. 2024), held that X Corp. had shown a likelihood of success on its First Amendment challenge to AB 587's content-moderation reports, which required positions on "hate speech" and "misinformation," and reversed the denial of a preliminary injunction — a likelihood ruling on remand, not a final invalidation, and it should not be overstated. Where the compelled content is objective, such mandates survive: *CTIA v. City of Berkeley*, 928 F.3d 832 (9th Cir. 2019). Compare *National Ass'n of Wheat Growers v. Bonta*, 85 F.4th 1263 (9th Cir. 2023), where the Prop 65 glyphosate warning was held **outside** *Zauderer* — not "purely factual and uncontroversial," because "known" carried a misleading term of art and the science was disputed — and then failed *Central Hudson* intermediate scrutiny for want of direct advancement and narrow tailoring. The live case is *xAI LLC v. Bonta*, No. 26-1591 (9th Cir.), on California AB 2013's training-data disclosures: preliminary injunction denied 4 March 2026 on the view that the summaries are commercial speech subject to intermediate scrutiny; argued 16 July 2026; **undecided**. That decision is the single most important pending development for SEC. 8 and SEC. 9, and v3.4 should re-run this note against it. Two structural answers are drafted in rather than argued: the statements run to a regulator and are not required to be published, and SEC. 12 as amended at §E.3(c) makes them categorically exempt from the public-records act — so the injury *NIFLA* identified, conscription into a public conversation, is absent; and the certification is criminalized only for knowing falsity or reckless assertion without inquiry, which places it with the false-statement offenses the plurality in *United States v. Alvarez*, 567 U.S. 709 (2012), expressly preserved, and with compelled speech "plainly incidental to … regulation of conduct" under *Rumsfeld v. FAIR*, 547 U.S. 47 (2006). One caution against overclaiming: 18 U.S.C. § 1350, the certification model this Act follows, appears never to have been challenged on First Amendment grounds. Twenty-four years of unchallenged operation is an argument from practice, not a holding, and this note says so rather than implying otherwise.

**n.17 ON DORMANT COMMERCE AND THE SPENDING CLAUSE.** *National Pork Producers Council v. Ross*, 598 U.S. 356 (2023), removed the almost-per-se rule against state laws with extraterritorial practical effects, re-reading the *Baldwin*–*Healy*–*Brown-Forman* line as discrimination cases; upstream out-of-state compliance cost is not, standing alone, a defect. What remains is *Pike*, fractured, with the real battleground at the threshold: a challenger must plead a substantial burden on interstate commerce, and failure to do so has been fatal at the pleading stage. SEC. 1(c) as amended is drafted to that: liability turns on in-state conduct, in-state deployment, or in-state availability; out-of-state conduct is evidentiary only; the Act draws no in-state/out-of-state distinction; and SEC. 0(a)(6) builds the record on burden that a challenger must overcome to plead. The premise that the internet cannot be geographically restricted, on which such challenges historically rested, has weakened as jurisdiction-specific access controls have become ordinary. Separately, on the Executive Order's leverage over broadband funds: those funds were appropriated by Congress for statutory purposes unrelated to AI policy, and a condition invented by an agency rather than stated unambiguously by Congress at the time of acceptance fails *Pennhurst State School & Hospital v. Halderman*, 451 U.S. 1 (1981), and the germaneness requirement of *South Dakota v. Dole*, 483 U.S. 203 (1987), before reaching the coercion question of *NFIB v. Sebelius*, 567 U.S. 519 (2012). District courts have set aside analogous conditions on appropriated funds through 2025–26. ⚠ No decided case has tested the broadband conditions specifically. A legislator asking whether this bill costs the state its broadband money should be given that authority, and the fact that as of this drafting no list of targeted state laws has been published and no state has lost a dollar.

---

## I. WHERE THE ARMOUR IS THIN

Stated here rather than buried, because a drafting file that only argues its own case is worth less than one that maps its own failure modes.

**I.1 The condition-on-deployment move does not defeat GAAIA §121(b), and should not be sold as if it did.** §121(e) defines development to include "evaluating and deciding, **prior to deployment**, whether an artificial intelligence model satisfies applicable safety or capability thresholds **for deployment**" — a definition already drafted around the instrumental relationship between the evaluation and the deployment decision. §121(b) preempts a law "specifically regulating the development"; it does not turn on the form of the command. And §121(c)(2) saves laws "applicable to activities occurring **upon or after** the deployment" — a duty to *have evaluated before* deploying governs an activity occurring before deployment, however it is enforced. The honest position: framing the offense as *deploying without validation* (which v3.2 SEC. 5(a) already does) is worth doing, because it is the difference between a plainly preempted command and an arguable one, and because it puts the case in the posture where §121(c)(2) is at least available. It is not a defence, it is a better starting position. The real protection for the validation duty is SEC. 13(b)(3) and (c)(2)(B): if it falls, it falls alone and it comes back.

**I.2 FRONTIER CSA(2)(C) is the clause that hurts most, and there is no drafting around it.** "Any requirement that such developer obtain certification, attestation, registration, accreditation, or other approval **as a condition of, or in connection with**, the development, training, evaluation, or release of an AI model" is drafted to catch conditions. Two thin footholds remain and both should be preserved rather than relied upon: the enumerated list in (2)(C) is "development, training, evaluation, or release" and **omits deployment**, so a validation requirement conditioned on *deployment* has a textual argument that (2)(A) — which does name deployment — reaches only third-party assessment, not the underlying requirement; and CSA(2) throughout is limited to assessment "by a person other than its developer," so SEC. 3(b)'s **internal attestation** mode is outside it. That is why §E and §D put internal attestation in the first rank and the third-party modes in the third. If FRONTIER passes as drafted, the Agency should make internal attestation the default validation mode and treat independent audit as the mode that lapses.

**I.3 The retention fallback is weaker than the first draft claimed.** SEC. 13(c)(2)(C) preserves record creation and retention where a reporting duty is preempted, on the ground that keeping records is not reporting. CSA(2)(C) also reaches a requirement that a developer "provide access to an AI model, model weights, training data, source code, **evaluation results**, or other technical materials for purposes of any such assessment, audit, evaluation, or verification." A duty to create evaluation records and produce them on lawful process is at minimum arguably within that. Two things reduce the exposure and neither eliminates it: production is on lawful process in an enforcement proceeding, not for purposes of a third-party audit, which is what (2)(C) addresses; and the retention duty falls on whoever holds the records, including a provider or deployer who is not a developer and is therefore outside §9(b). Chunk 4 should test the retention period against this, not only against SB 53 and SB 315.

**I.4 SEC. 13(c)–(d) is engineered to make facial adjudication difficult, and a court may resent that.** Every ruling becomes as-applied, for so long as, subject to revival. A litigator will not attack the scheme under *Murphy*; he will ask the court to enjoin the architecture as a whole rather than operate a statute designed to make partial judgments provisional. There is no drafting answer, only a posture: the order mechanism at (c)(1) means the State, not the defendant and not the court, bears the burden of saying what is suspended and when, in public, prospectively — which is the version of this design least likely to read as evasion.

**I.5 SEC. 5(d) is rated first-rank on a reading that has not been tested.** SEC. 5(d) reaches a false statement "to the Agency **or any regulator**." CSA(1) reaches disclosure by a developer "to any State, **member of the public, or other person**" of risk information. The argument that a veracity rule is not a *disclosure* obligation is strong — CSA(1) governs what must be disclosed, not whether what is said must be true — but it is an argument, and the breadth of "or any regulator" is what makes it one. ⚠ Chunk 3 should consider whether SEC. 5(d) gains anything from narrowing to statements made in connection with a duty arising under this Act.

---

## G. CARRIED QUESTIONS

**For chunk 3 (penalty brackets):** enrolled A9449 penalty text; SB 315 penalty amounts; whether the entity civil penalty under SEC. 10(a) should sever independently of the individual criminal penalties (SEC. 13(b)(1) currently keeps them together); whether SEC. 5(d) should be narrowed per §I.5.

**For chunk 4:** SB 53 and SB 315 retention periods against SEC. 12's five years — now doubly important, because SEC. 13(c)(2)(C) makes retention the fallback for a preempted reporting duty, and because of §I.3.

**For chunk 5:** the SEC. 9(a) recast of the two characterization-shaped triggers (§E.3(d)), jointly with the regulations draft.

**Standing watch:** *xAI v. Bonta*, No. 26-1591 (9th Cir.) — argued, undecided; the AB 2013 ruling triggers a v3.4 re-run of n.16. *xAI v. Weiser*, D. Colo. — whether an amended complaint targets SB 26-189; ⚠ docket mirrors were stale past 24 April 2026 and PACER was not consulted. FRONTIER Act markup. Whether GAAIA is introduced and whether §121(c) survives introduction. Whether the FTC policy statement is finalized. Publication of the Commerce list. The GAAIA internal section numerals for the revenue-threshold definitions (⚠ weakest citation in this chunk).

**For the cite-check:** every case in §F has been confirmed against a primary or first-party source. *Monsanto v. Durnell* has a volume but no page — cite 609 U.S. ___ with the slip opinion. *Virginia Uranium* must always carry "(plurality opinion)". *X Corp. v. Bonta* must always be described as a preliminary-injunction likelihood ruling. The one uncited proposition in §F is n.15's statement that no authority has been located for contingent *criminal* legislation triggered by an external federal event; that absence is the reason for the order mechanism and is stated as an absence, not papered over.

---

## H. SOURCES

**Federal bill text (primary):** govinfo.gov, BILLS-119hr9925ih (FRONTIER Act, full text incl. SEC. 9(a)–(d) verbatim); govinfo.gov, BILLS-119hr5388ih (H.R. 5388, §§ 6–7); govinfo.gov, BILLS-119s5061is and BILLSTATUS-119s5061 (Secure A.I. Development Act); govinfo.gov, BILLSTATUS-119hr9925 (referral history); trahan.house.gov, *The Great American AI Act* discussion draft PDF (Sec. 121 verbatim).

**Cases (primary):** supremecourt.gov slip op. and supreme.justia.com vol. 609 (*Monsanto v. Durnell*, 25 June 2026, incl. vote breakdown); law.cornell.edu (*Kansas v. Garcia*; *Murphy v. NCAA*; *NIFLA*; *Virginia Uranium*); supreme.justia.com (*Rice*; *Wyeth*; *Franklin*; *Bates*; *Arizona v. United States*; *Whiting*; *National Pork Producers*; *Zauderer*; *Rumsfeld v. FAIR*; *Alvarez*; *Dole*; *Pennhurst*; *NFIB*; *Alaska Airlines v. Brock*; *Connally*; *Kolender*; *Bouie*; *Sunshine Anthracite*); cdn.ca9.uscourts.gov (*X Corp. v. Bonta*, 4 Sept. 2024; *Wheat Growers*, 7 Nov. 2023); law.justia.com (*CTIA v. Berkeley*).

**Executive and agency:** whitehouse.gov and presidency.ucsb.edu (EO 14365); justice.gov (AG memorandum establishing the AI Litigation Task Force; press release and complaint in intervention in *xAI v. Weiser*); federalregister.gov 2026-13628 and ftc.gov (FTC proposed policy statement, 7 July 2026); broadbandbreakfast.com (NTIA non-deployment guidance postponements, Mar. and June 2026); axios.com (24 Apr. 2026, missed EO deadlines).

**Dockets:** clearinghouse.net case 48129 (*xAI v. Weiser*), 46595 (*Illinois v. FEMA*), 46596 (*California v. DOT*); climatecasechart.com (*Chamber v. CARB*); iapp.org and techtimes.com (*xAI v. Bonta* posture and argument date).

**Analysis:** techpolicy.press (GAAIA unpacking; July 2026 roundup); fpf.org (GAAIA compared to state laws; the development/deployment line-drawing problem); justsecurity.org (Rubenstein, on the inadequacy of general-applicability savings clauses); mintz.com (*AI: The Washington Report*, Aug. 2026); rollcall.com (House Science markup, 26 June 2026); natlawreview.com and fisherphillips.com (Blackburn package status); statescoop.com and privacy-daily.com (NDAA moratorium dropped); harvardlawreview.org blog (dormant commerce after *Pataki* and *Paxton*); druganddevicelawblog.com (circuits on the presumption after *Franklin*); labs.cloudsecurityalliance.org (no state AI law invalidated as of the sweep); faegredrinker.com (*Durnell* decision note).


---

<a id="chunk-3"></a>
<!-- BEGIN audit/chunk3_penalty_architecture.md · sha256:cbdc6b73cf95 · concatenated 19 Aug 2026, content verbatim -->

# CHUNK 3 — PENALTY ARCHITECTURE FOR v3.3: SEC. 7 REWORK AND BRACKET CALIBRATION

> **UPDATE — amended on three points by chunk 4:** SEC. 10(c) as set out at §E.2 below is
> restructured by chunk 4 §E.2 — the death ceiling rises to any term of years or life per
> 18 U.S.C. § 1365(a), resolving A.2's § 841(b) inversion structurally; a concurrency-default
> valve with a [forty]-year cap on consecutive determinate terms replaces "may run consecutively";
> and restitution decouples from the tier into a new (c)(4), so §E.1's SEC. 7(a) reference to
> "restitution ordered under SEC. 10(c)(2)" conforms to (c)(4) (chunk 4 §E.4(g)). n.19's
> "On § 841(b)" passage is superseded by n.21 (strike per chunk 4 §E.4(e)). SEC. 6(b) splits into
> (b)(1)/(b)(2), closing the recidivist path to the harm tier (chunk 4 §E.1). The §G questions
> carried "for chunk 4" are all answered at chunk 4 §§B and E. Use chunk 4's text at v3.3 assembly.
> 
Drafting date: 16 August 2026. Method: primary-text pinning of every dollar figure the calibration rests on (state legislature servers and enrolled-text mirrors; eCFR; U.S. Code), then the calibration, then the drop-in text, then an adversarial pass in which the drop-ins were attacked rather than checked. As at chunk 2, the attack found more than the check did; §E is the second draft and §I records what the first draft got wrong.

Verbatim quotation is used wherever the exact words are load-bearing. Anything not retrieved from primary text is marked ⚠ and paraphrased, never quoted. Two primary sources were unreachable from this drafting environment and are disclosed as such (§H): leginfo.legislature.ca.gov (robots-excluded; the SB 53 pin below is from the LegiScan mirror of the enrolled text) and legislation.nsw.gov.au / AustLII (403; the NSW pin below is ⚠ secondary).

This chunk: answers the four carried questions (§B); pins the enacted penalty anchors, state and federal (§C); calibrates the brackets (§D); sets out the reworked SEC. 7, the pinned SEC. 10, the SEC. 5(d) narrowing, and the conforming amendments to SEC. 11 and SEC. 13 (§E); supplies drafting notes n.18–n.20 (§F); and states where the architecture is thin (§I). It closes READ FIRST open item 7 (penalty dollar calibration) and the penalty-bracket half of item 2; items 3 and 4 (the criminal-law scholar's questions and the Eighth Amendment stress-test at outbreak scale) remain open and are flagged where they bite.

---

## A. CORRECTIONS AND COMPLETIONS TO EARLIER MATERIAL

**A.1 — v3.2 n.7 cites the wrong NSW section for the insurance prohibition.** n.7 cites "Work Health and Safety Act 2011 (NSW) s. 272 (statutory prohibition of insurance for penalties)." Section 272 is the *no contracting out* rule — it voids terms that exclude or modify duties. The prohibition of insurance and indemnity for WHS monetary penalties — three offences: entering into, providing, and taking the benefit of such an arrangement — is **s 272A**, inserted by the Work Health and Safety Amendment (Review) Act 2020 (NSW), with accessorial liability for officers at s 272B. ⚠ Primary text unreachable this sweep (§H); the section numbers and architecture are concordant across multiple Australian firm alerts. v3.3 n.18 cites both sections in their correct roles.

**A.2 — v3.2 n.10 misdescribes its 21 U.S.C. § 841(b) anchor.** n.10 says: "where knowing violation kills, the ceiling is twenty years." Pinned text runs the other way. § 841(b)(1)(C): the **base** ceiling, with no death, is "a term of imprisonment of not more than 20 years"; where death or serious bodily injury results, the range becomes "not less than twenty years or more than life" — death makes twenty the *floor*, not the ceiling. (The one subparagraph where a death enhancement states a ceiling is (b)(1)(E), Schedule III: "not more than 15 years.") The Act's own harm tier — a twenty-year ceiling per victim over a bracketed [two]-year floor — is therefore *milder* than the federal drug pattern it cites, not equivalent to it. That is a feature, and v3.3 n.19 now says it straight: the Act borrows § 841(b)'s per-victim counting and its *Burrage* causation, takes the (b)(1)(C) base maximum as its ceiling, and declines the federal mandatory floor.

**A.3 — Chunk 1's Illinois penalty gap is now closed, and the New York reduction is confirmed exactly.** Chunk 1 §A carried "AG enforcement (⚠ pin amounts from enrolled text)" for SB 315 and "\$1M/\$3M (amendment reduced from \$10M/\$30M)" for New York on secondary authority. Both are pinned at §B.1–B.2 from the enrolled texts: Illinois \$1,000,000 first / \$3,000,000 per subsequent violation; New York identically, replacing the original \$10,000,000 / \$30,000,000 of Chapter 699.

**A.4 — Conform future New York citations to § 1427.** The RAISE Act as originally enacted carried its violations provision at GBL § 1422. A9449 **repealed and replaced** article 44-B in full (§§ 1420–1429); violations now sit at § 1427. Chunk 1's citation practice ("RAISE penalties") predates the renumbering; all v3.3 notes cite § 1427.

---

## B. CARRIED QUESTIONS, ANSWERED

**B.1 Enrolled A9449 penalty text — pinned.** A9449 (Rozic) / S8828 (Gounardes), 2025–2026 session; the Senate substituted A9449 and it was signed 27 March 2026 as **Chapter 96 of the Laws of 2026**, repealing and replacing General Business Law article 44-B and moving the effective date of Chapter 699's regime to **1 January 2027**. The violations section of the replaced article, § 1427, as printed in the bill (capitals are the bill-print convention for new matter; the codified text reads in ordinary case):

> "THE ATTORNEY GENERAL MAY BRING A CIVIL ACTION TO RECOVER A CIVIL PENALTY IN AN AMOUNT NOT TO EXCEED ONE MILLION DOLLARS FOR A FIRST VIOLATION AND IN AN AMOUNT NOT TO EXCEED THREE MILLION DOLLARS PER SUBSEQUENT VIOLATION"

⚠ One of two retrievals appends "determined based on the severity of the violation" to this sentence; the other truncates at "per subsequent violation." The severity qualifier is present in the California and Illinois siblings quoted at §C and is very likely present here; conform the exact clause at the cite-check.

The conduct triggering the penalty, verbatim: a large frontier developer that

> "FAILS TO PUBLISH OR TRANSMIT A COMPLIANT DOCUMENT REQUIRED TO BE PUBLISHED OR TRANSMITTED UNDER THIS ARTICLE, MAKES A STATEMENT IN VIOLATION OF SUBDIVISION FOUR OF SECTION FOURTEEN HUNDRED TWENTY-ONE OF THIS ARTICLE, FAILS TO REPORT AN INCIDENT AS REQUIRED BY SECTION FOURTEEN HUNDRED TWENTY-TWO OF THIS ARTICLE, OR FAILS TO COMPLY WITH ITS OWN FRONTIER AI FRAMEWORK."

And: "NOTHING IN THIS ARTICLE SHALL BE CONSTRUED TO ESTABLISH, AUTHORIZE OR CREATE A PRIVATE RIGHT OF ACTION ASSOCIATED WITH VIOLATIONS OF THIS ARTICLE." Section 1428 separately levies "a civil penalty of one thousand dollars for each day the entity fails to file a disclosure" plus assessments owed — a small per-day machine-enforcement penalty running beside the large per-violation one.

For the record of what the desk did to the numbers: Chapter 699 as signed 19 December 2025 (S6953-B) provided, in its then-§ 1422, "a civil penalty in an amount not exceeding ten million dollars for a first violation and in an amount not exceeding thirty million dollars for any subsequent violation" — and the B-print itself had already replaced the A-print's percentage-of-compute-cost penalties (5% first / 15% subsequent). The chapter amendment then cut the dollar figures by 10× to the California-family level. Two consecutive rounds of penalty compression, each toward the \$1M anchor: that is the enacted revealed preference of the political system this Act will be introduced into, and §D treats it as data.

**B.2 SB 315 penalty amounts — pinned from the enrolled text.** Illinois SB 315, 104th GA, enrolled; Governor approved 6 July 2026; **Public Act 104-0538**; "This Act takes effect January 1, 2027" (Sec. 99). The Artificial Intelligence Safety Measures Act's civil-penalty section, verbatim and in full:

> "Section 25. (a) A large frontier developer that fails to publish or transmit a compliant document required to be published or transmitted under this Act, makes a statement in violation of subsection (f) of Section 10, fails to have a third party perform an independent audit of compliance as required by subsection (d) of Section 10, fails to report a critical safety incident as required by Section 15, or fails to comply with its own frontier AI framework shall be subject to a civil penalty in an amount dependent upon the severity of the violation that does not exceed \$1,000,000 for the first violation. For a subsequent violation, the civil penalty may not exceed \$3,000,000 per violation.
>
> (b) A civil penalty described in this Section shall be recovered in a civil action brought exclusively by the Attorney General. Any civil penalties collected from the enforcement of this Act shall be deposited into the Attorney General Court Ordered and Voluntary Compliance Payment Projects Fund.
>
> (c) The loss of value of equity does not count as damage to or loss of property for the purposes of this Act.
>
> (d) Nothing in this Act shall be construed to establish a private right of action associated with violations of this Act."

Section 18(e) adds the machine-enforcement layer: for operating "a large frontier model in this State without a current disclosure filed with the Agency," false disclosure information, or unpaid assessments, the Agency may after notice and hearing levy "(1) a civil penalty of \$1,000 for each day the person fails to file a disclosure as required by this Section or fails to correct false information; and (2) an amount equal to the assessments owed." Thresholds, verbatim: a frontier model is "a foundation model that was trained using a quantity of computing power greater than 10^26 integer or floating-point operations"; a large frontier developer had "annual gross revenues in excess of \$500,000,000 in the preceding calendar year."

Three structural facts worth more than the numbers. *First*, Illinois's Section 25(a) is the California sentence with the New York recidivism step and one addition: **failure to audit is a penalty trigger** — the only state to penalise the validation mode itself. *Second*, the penalties are earmarked to an enforcement fund (the AG's compliance-projects fund), not the general fund: an enacted sibling for SEC. 10(f) below. *Third*, § 25(c)'s equity-loss exclusion (mirrored in NY) confines "damage to property" in the catastrophic-harm definitions — a definitional guard v3.2 does not need (its harm tier runs on death and serious injury, not property), but chunk 4 should note it when harmonising definitions.

**B.3 Should SEC. 10(a) sever independently of the individual criminal penalties? Yes.** Three reasons, in descending order of weight. (1) The collision map (chunk 2 §D) rates 10(a) "follows the duty": attached to a preempted developer-side duty, the entity civil penalty is the likeliest single casualty of a FRONTIER-style challenge, while 10(b)–(c) ride the criminal carve-outs; a penalty section that stands or falls as a unit hands the challenger a lever to drag the criminal penalties into a civil-side holding. (2) H.R. 5388 § 6(a)(2)(B) saves "any provision of a law or regulation to the extent that the violation of such provision carries a criminal penalty" — the cleanest savings text in the field turns on the penalty attached to the provision, so the criminal character of 10(b)–(c) must be legible *severally*, not blended into a section whose headline instrument is a civil fine. (3) The fund dependency is a silent single point of failure: v3.2 SEC. 11(a) pays awards "from the fund established by SEC. 10(a)," so a 10(a) suspension under SEC. 13(c) would kill the whistleblower bounty — the Act's engine for detection probability — as a side effect. §E.4 splits the severance, §E.2 moves the fund to its own subsection 10(f) fed by every collection source, and §E.3 conforms SEC. 11.

**B.4 Should SEC. 5(d) be narrowed per chunk 2 §I.5? Yes — to this State's own government, and not otherwise.** v3.2 reaches a false statement "to the Agency or any regulator." The breadth of "any regulator" is what gave the FRONTIER CSA(1) overlap argument its footing (chunk 2 §I.5), and it also walks the Act into territory that is not a state's to police: a lie told to a federal agency is 18 U.S.C. § 1001's business, and a lie told to a sister state's regulator is that state's. §E.5 narrows the offense to statements made to the Agency or to any agency or officer of this State in connection with official functions, keeping the offense **free-standing** — no duty to speak is created; the duty is only to speak truly if one speaks, the § 1001 architecture that sits with the false-statement offenses preserved in *United States v. Alvarez*, 567 U.S. 709 (2012) (plurality opinion). What is lost — lies to federal or sister-state regulators about covered systems — was never properly this Act's to punish, and remains punishable where it belongs. What is kept is the first-rank offense chunk 2 built the armour around: an offense of lying, borne by whoever speaks, in no Covered Subject Area, generally applicable false-statement law's next of kin.

---

## C. THE ANCHOR TABLE — EVERY FIGURE PINNED

State family (the template lineage CA → NY → IL is a single sentence propagating, with local additions):

| Anchor | Provision | Amount, verbatim core | Enforcement |
|---|---|---|---|
| CA SB 53 (Ch. 138, Stats. 2025) | Bus. & Prof. Code § 22757.15(a) | "a civil penalty in an amount dependent upon the severity of the violation that does not exceed one million dollars (\$1,000,000) per violation" | § 22757.15(b): "recovered in a civil action brought only by the Attorney General" |
| NY RAISE as amended (Ch. 96, L. 2026) | GBL § 1427 | "not to exceed one million dollars for a first violation and … not to exceed three million dollars per subsequent violation" | AG civil action; no private right |
| NY RAISE as originally enacted (Ch. 699, L. 2025) | then-§ 1422 | "not exceeding ten million dollars for a first violation and … not exceeding thirty million dollars for any subsequent violation" | superseded 27 Mar 2026 |
| IL SB 315 (P.A. 104-0538) | Act § 25(a) | "does not exceed \$1,000,000 for the first violation. For a subsequent violation … may not exceed \$3,000,000 per violation" | § 25(b): "exclusively by the Attorney General"; earmarked to AG compliance fund |
| IL / NY disclosure layer | IL § 18(e); NY § 1428 | "\$1,000 for each day" (IL); "one thousand dollars for each day" (NY) | Agency-levied after notice and hearing (IL) |
| GAAIA discussion draft | ⚠ not introduced; penalty per FPF summary | ⚠ up to \$1M per violation, "each day treated as a separate violation" | federal + state AGs ⚠ |

Federal calibration patterns:

| Pattern | Provision | Pinned content |
|---|---|---|
| Benefit floor + factors | 33 U.S.C. § 1319(d) | statutory \$25,000/day; factors incl. "economic benefit or savings resulting from the violation" (v3.2 already adopts) |
| Indexing, live proof | 40 C.F.R. § 19.4 (current) | CWA § 309(d) maximum as adjusted: **\$68,445 per day**, adjustments effective 8 Jan 2025 — 2.7× the 1987 figure by rule, no reenactment needed |
| Individual fine ceilings | 18 U.S.C. § 3571(b) | felony "\$250,000"; Class A misdemeanor not resulting in death "\$100,000" |
| Organisational ceilings | § 3571(c) | felony "\$500,000"; Class A misdemeanor "\$200,000" |
| Gain-scaled alternative | § 3571(d) | "twice the gross gain or twice the gross loss," whichever is greater |
| Fine-fixing factors | 18 U.S.C. § 3572(a) | ability to pay: income, earning capacity, financial resources |
| The rot exhibit | 21 U.S.C. § 333(a) | "(a)(1) … not more than one year or fined not more than \$1,000"; "(a)(2) … not more than three years or fined not more than \$10,000" — nominal since 1938, rescued only by § 3571's override |
| Certification tier | 18 U.S.C. § 1350 | knowing: \$1,000,000 / 10 years; wilful: \$5,000,000 / 20 years (v3.2 n.8 already relies on the imprisonment side) |
| State-native gain-scaling | N.Y. Penal Law § 80.00(1) | felony fine "not exceeding the higher of a. five thousand dollars; or b. double the amount of the defendant's gain from the commission of the crime" |
| What courts actually do | *United States v. DeCoster*, 828 F.3d 626 (8th Cir. 2016) | "imposed \$100,000 fines on both Jack and Peter DeCoster and sentenced them to three months imprisonment" — the misdemeanor tier, after a half-billion-egg recall |
| The cautionary tale | *United States v. Park*, 421 U.S. 658 (1975) | \$50 a count, unindexed — the reason SEC. 10 indexes |

Clawback and anti-indemnification patterns (for SEC. 7):

| Pattern | Provision | Pinned content |
|---|---|---|
| No-fault clawback, narrow | 15 U.S.C. § 7243 (SOX § 304) | CEO and CFO only; trigger is restatement from "material noncompliance … as a result of misconduct"; 12-month window; bonus, incentive- and equity-based comp, and "profits realized from the sale of securities"; SEC "may exempt any person" |
| Mandatory clawback, structural | 17 C.F.R. § 240.10D-1 | issuer "must recover reasonably promptly"; no-fault trigger; lookback "three completed fiscal years immediately preceding" the restatement obligation; three narrow impracticability outs (collection costs exceeding recovery; pre-2022 foreign-law conflict; tax-qualified-plan damage); and the flat bar: the issuer must **not indemnify** any executive officer against the loss |
| Insurance ban as offence | WHS Act 2011 (NSW) ss 272, 272A–272B | s 272 voids contracting-out terms; s 272A creates three offences — entering into, providing, and benefiting from insurance or indemnity for a WHS monetary penalty — with officer accessorial liability at s 272B. ⚠ maxima per secondaries: 250 penalty units individual / 1,250 body corporate for taking out; 500 / 2,500 for providing |
| Measure and destination | *Kokesh v. SEC*, 581 U.S. 455 (2017); *Liu v. SEC*, 591 U.S. 71 (2020) | *Kokesh*: disgorgement is a penalty for limitations purposes; *Liu*: equitable disgorgement confined to net profits, for victims. Both answered in text at §E.1: express limitations tie, restitution-first destination |

---

## D. THE CALIBRATION — FORMULA OVER FIGURE

**D.1 What the enacted family teaches.** Three legislatures, one sentence, and every number that survived a governor's desk is \$1,000,000 severity-scaled per violation, with a 3× recidivism step in two of three states. New York's trajectory is the sharpest datum: 5%-of-compute → \$10M/\$30M → \$1M/\$3M in thirteen months, each compression a condition of enactment or signature. A model act that writes \$10M/day into its civil bracket is writing the number the political system has now twice refused; a model act that writes the family's own numbers into the bracket and puts the scaling into *formulas* is writing the number three states have already signed. That is the design rule for SEC. 10(a): **adopt the family's headline figures for legibility; let the floor, the multiplier, the per-day accrual, and the index do the actual deterrence.**

**D.2 The arithmetic that makes the figure almost irrelevant.** Every heavy state duty triggers at \$500,000,000 annual revenue (pinned, CA § 22757.11(j); IL definitions). At the qualification *floor*, revenue is ≈ \$1.37M/day; the \$1M/day ceiling is three-quarters of one day's revenue, and at actual frontier scale it is noise. A fixed civil schedule therefore cannot be the deterrent, and this Act never asks it to be. The deterrent stack is: (i) the **economic-benefit floor** (v3.2's CWA borrow, retained verbatim) — a penalty may never be less than what the violation saved or earned, so the fine cannot be a licence at any revenue; (ii) the **per-day accrual** — the CA/NY/IL per-violation figure married to the CWA continuing-violation structure, which is also (⚠) GAAIA's own structure, so the federal template being urged against state law concedes the form; (iii) the **twice-gross-gain alternative** on every criminal fine (18 U.S.C. § 3571(d); native in state penal law per N.Y. Penal Law § 80.00's "double the amount of the defendant's gain") — the fine scales with the violation's economics automatically, no legislature required; (iv) the **index** (40 C.F.R. part 19 manner; the pinned live proof being \$25,000 → \$68,445 without Congress lifting a finger, against *Park*'s \$50 a count and the FDCA's \$1,000 still nominal on the books since 1938). Becker's inequality — deterrence requires expected sanction p·S to exceed benefit B, so S must scale as B/p — is unmeetable by any enactable fixed S when B is equity-denominated in nine figures and p is the detection probability of a novel agency; that is Gneezy and Rustichini's finding made policy ("a fine is a price," and a below-benefit fine is a subsidised price — v3.2 n.10 already says so in one line). The formulas make S track B by construction, which is the only calibration that survives contact with frontier economics; and the residue that no S can reach — the judgment-proof, the already-rich, the indemnified — is precisely what SEC. 6 (imprisonment), SEC. 7 (clawback and the indemnification ban), and SEC. 10(d)(4) (disqualification) exist to reach. Fines are the junior instrument of this Act. The calibration's job is to stop them being an insult.

**D.3 The individual brackets: parity, not fantasy.** The misdemeanor fine pins to \$100,000 (18 U.S.C. § 3571(b)(5) Class A parity — and *DeCoster* in fact: \$100,000 and three months, at the misdemeanor tier, for an outbreak with a half-billion-egg recall). The base felony fine pins to \$250,000 (§ 3571(b)(3) parity). The harm-tier fine pins to \$1,000,000 per offense — the § 1350 knowing-certification figure, counted per victim, with restitution taking priority in the application of the defendant's assets. Each carries the twice-gain alternative, and each is bracketed for the adopting state's counsel to conform to the local felony-fine grid — with the instruction that the **gain alternative must survive conformity** (New York's grid shows it native; a state whose grid lacks it should adopt it with the Act). A means-consideration sentence (from 18 U.S.C. § 3572(a)) is added so that like culpability bears like burden across defendants whose liquidity differs by five orders of magnitude; the day-fine principle without the day-fine machinery.

**D.4 The recidivism step.** NY and IL legislated 3× for a subsequent violation; v3.2's architecture already had the instinct at the criminal layer (SEC. 6(b)'s [ten]-year lookback). §E.2 adopts the enacted step at the civil layer: \$[3,000,000] per violation per day after a prior final adjudication. Symmetry with the family, and a cheap answer to "invented numbers."

**D.5 Proportionality guard.** The Excessive Fines Clause applies to the states, *Timbs v. Indiana*, 586 U.S. 146 (2019), and the test is gross disproportionality to the offense, *United States v. Bajakajian*, 524 U.S. 321 (1998). The architecture is self-proportioning at the two points that matter: the benefit floor ties the mandatory minimum to the violator's own gain, and the gain multiplier ties the ceiling to it; both are measures *of the offense*. The exposure is the stack — per-day × recidivist × per-victim consecutive — at outbreak scale, which is READ FIRST item 4's question, still open, still assigned to a proportionality scholar; the valves in text are the § 1319(d) factors (including "economic impact of the penalty on the violator" and "such other matters as justice may require") and judicial discretion over consecutive sentences. §I.4 states the residual honestly.

---

## E. DROP-IN TEXT FOR v3.3

House convention as in chunk 2: set out in full, no ellipsis; in amended sections, struck text is not reproduced and inserted text is **bold**. SEC. 7 is replaced wholesale, so it is set out clean.

### E.1 — SEC. 7, replaced in full

> **SEC. 7. PERSONAL ECONOMIC CONSEQUENCES.**
>
> (a) *Disgorgement.* On conviction or civil adjudication of a violation, the court shall order the person adjudicated to disgorge the economic benefits attributable to the violation — including salary, bonus, incentive- or equity-based compensation, distributions, profits realized on the sale or transfer of any interest, and any increase in the value of any interest, whether received directly or through any entity, trust, or arrangement — received or accrued during the period of the violation and the [twelve] months following its cessation or concealment. Incentive- or equity-based compensation received by a controlling person during the period of a violation is presumed attributable to the violation to the extent the violation materially contributed to the results on which it was paid; the presumption is rebuttable in a civil proceeding and operates in a criminal proceeding only as a permissive inference. The court may reduce or decline recovery only upon a finding that the direct costs of recovery would exceed the amount recoverable. Amounts disgorged shall be applied first to restitution ordered under SEC. 10(c)(2), and the remainder deposited in the fund established by SEC. 10(f). A claim under this subsection is subject to the limitations periods of SEC. 12. On a showing of probable adjudication and risk of dissipation, the court may restrain transfers of, or require the escrow of, assets up to the amount reasonably necessary to satisfy the anticipated order.
>
> (b) *No indemnification or insurance.* (1) No person may (A) enter into, renew, or maintain a contract of insurance or other arrangement under which any person is covered, in whole or in part, against liability for an individual penalty, fine, disgorgement, or restitution imposed under this Act; (B) provide, underwrite, or pay a benefit under such a contract or arrangement, or pay or reimburse, directly or indirectly, any part of such a liability imposed on another person; or (C) demand, accept, or retain such a benefit, payment, or reimbursement. (2) No person may make, offer, solicit, or receive any payment, loan, forgiveness of indebtedness, increase in compensation, gross-up, distribution, gift, or other transfer of value whose purpose or predominant effect is to offset, in whole or in part, a liability described in paragraph (1). (3) Every contract, arrangement, or transfer described in this subsection is void and unenforceable in this State, whatever law is chosen to govern it, to the full extent of this State's jurisdiction; and any benefit received under one is held in constructive trust for the persons and fund to which subsection (a) applies. (4) A violation of this subsection is a violation of this Act for purposes of SEC. 10(a); a knowing violation by a controlling person is a violation of SEC. 5 for purposes of SEC. 6(b). (5) This subsection does not restrict the purchase or provision of insurance for, or the payment, advancement, or indemnification of, reasonable costs of defense, provided that amounts advanced or indemnified shall be repaid by a person finally adjudicated to have committed a knowing or wilful violation under SEC. 6(b), to the extent attributable to the defense of that violation; and it does not restrict indemnification of a person not adjudicated liable under this Act.
>
> (c) *Construction.* Disgorgement under subsection (a) is remedial, is additional to any penalty or fine, and shall not be credited against one; no single benefit shall be disgorged more than once. Nothing in this section limits any remedy under SEC. 10.

### E.2 — SEC. 10, amended (inserted text bold; brackets remain adopting-state choices, now carrying recommended defaults)

> **SEC. 10. ENFORCEMENT AND PENALTIES.** (a) Entity: civil penalty of up to \$[**1,000,000**] per violation for each day the violation continues **or, where the violation occurs after a prior adjudication of a violation by the same person has become final, up to \$[3,000,000] per violation for each day the violation continues**; strict liability. In assessing the amount, the court shall consider the seriousness of the violation; the economic benefit or savings resulting from it; any history of violations; good-faith efforts to comply; the economic impact of the penalty on the violator; and such other matters as justice may require, per the structure of 33 U.S.C. § 1319(d). A penalty under this subsection shall not be less than the economic benefit or savings derived from the violation, as found by the court. Penalty amounts under this Act shall be adjusted annually for inflation by Agency rule, in the manner of 40 C.F.R. part 19. (b) Individual offense under SEC. 6(a): [misdemeanor; imprisonment up to one year; fine up to \$[**100,000**] **or, if greater, twice the gross pecuniary gain to the person derived from the violation**], per the structure of 21 U.S.C. § 333(a)(1) **as to classification and of 18 U.S.C. § 3571(b)(5) and (d) as to amount**. (c)(1) Enhanced tier under SEC. 6(b): [felony; imprisonment up to three years; fine up to \$[**250,000**] **or, if greater, twice the gross pecuniary gain to the person derived from the violation**]. (c)(2) Enhanced tier where death or serious injury results: [felony; imprisonment up to twenty years for each offense; where death results, not less than [two] years; fine up to \$[**1,000,000**] **for each offense or, if greater, twice the gross pecuniary gain to the person derived from the violation**]; sentences for separate offenses under SEC. 6(b) may run consecutively; "but-for cause" bears the meaning given in Burrage v. United States, 571 U.S. 204 (2014); the court shall additionally order restitution to each person killed or seriously injured, or to the person's estate**, and restitution has priority over every penalty, fine, and disgorgement in the application of a defendant's assets. In fixing a fine for a natural person under this Act, the court shall consider the person's income, earning capacity, and financial resources, so that like culpability bears like burden**. (d) Remedies additionally include: (1) injunction against any entity or controlling person restraining deployment, expansion, or continued operation in violation of this Act, per the structure of 21 U.S.C. § 332; (2) suspension of an identified model version and configuration, per the structure of 21 U.S.C. § 334; operation of a suspended configuration in this State by any person with notice of the suspension is contempt and a violation of SEC. 5(a); (3) on probable cause of imminent risk of death or serious injury, emergency suspension ex parte, with a post-deprivation hearing within [10] days; (4) disqualification from acting as a controlling person of any covered system; and (5) suspension and debarment modelled on FAR subpart 9.4. (e) The Attorney General enforces this Act. Corporate payment of any penalty **imposed on a natural person** does not extinguish individual liability **and is a violation of SEC. 7(b)**. **(f) Fund. The [Frontier AI Accountability Fund] is established. All penalties, fines, disgorgement, and other monetary recoveries under this Act, after satisfaction of restitution, shall be deposited in the fund; awards under SEC. 11 are paid from it; the balance [is appropriated to the Agency's functions under this Act / reverts to the general fund, at the adopting state's election]. The fund continues in operation, fed by every source not suspended or invalidated, notwithstanding the suspension or invalidity of any single provision of this section.**

Drafting deltas from v3.2, for the record: the recidivist step is new (enacted siblings: GBL § 1427; IL § 25(a)); the gain-alternative fines are new (§ 3571(d); N.Y. Penal Law § 80.00(1)); the means-consideration sentence is new (§ 3572(a)); restitution priority is new (*Liu*'s destination logic made statutory); the fund moves from a trailing sentence of (a) to its own subsection (f) with a survival clause (see B.3); and the fund-feeding sentence formerly in (a) ("Penalties collected under this Act fund the awards provided by SEC. 11") is subsumed by (f). Nothing else in the section moved.

### E.3 — SEC. 11(a), conforming amendment

In the final sentence of SEC. 11(a), strike "the fund established by SEC. 10(a)" and insert "**the fund established by SEC. 10(f)**". Add at the end of SEC. 11(a): "**Awards remain payable from the fund whatever the source of the amounts in it; the suspension or invalidity of SEC. 10(a) does not suspend this section.**"

### E.4 — SEC. 13(b), conforming amendments (severance split)

In SEC. 13(b)(1), strike "the remedies of SEC. 7 and SEC. 10 as applied to those offenses" and insert "**the remedies and penalties of SEC. 7 and SEC. 10(b) through (f) as applied to those offenses, and SEC. 10(a) as applied to those offenses**". Add to SEC. 13(b)(5):

> **The civil penalty of SEC. 10(a) and the criminal penalties of SEC. 10(b) and (c) sever independently of one another; the invalidity or suspension of either, in whole or as applied, does not affect the other; and the fund under SEC. 10(f) continues in operation whatever else is severed, fed by the sources that remain.**

### E.5 — SEC. 5(d), narrowed

> (d) A false or misleading statement of material fact concerning a covered system, made to the Agency**, or to any agency or officer of this State in connection with the agency's or officer's official functions**.

(The words "or any regulator" are struck. See B.4 and n.20.)

---

## F. NEW DRAFTING NOTES

**n.18 ON SEC. 7.** The clawback keeps Sarbanes-Oxley § 304's no-fault severity but not its architecture, because the architecture is the known weakness: 15 U.S.C. § 7243 reaches two officers only (CEO, CFO), triggers only on an accounting restatement from misconduct, looks back twelve months, and hands the Commission power to "exempt any person." The rework instead follows the structure Congress and the SEC built when they tried again: 17 C.F.R. § 240.10D-1 — recovery that is mandatory ("must recover reasonably promptly"), no-fault, with a multi-year lookback and impracticability outs confined to cases where collection costs the fund more than it returns; and its flat prohibition — the issuer "must not indemnify" any executive officer against the loss — is the seed of SEC. 7(b). The attribution presumption operates as SEC. 4(b) does: mandatory in civil proceedings, a permissive inference in criminal ones, per *Sandstrom v. Montana*, 442 U.S. 510 (1979). *Kokesh v. SEC*, 581 U.S. 455 (2017), holds disgorgement a penalty for limitations purposes — so SEC. 7(a) submits to SEC. 12's periods expressly rather than litigating the point; *Liu v. SEC*, 591 U.S. 71 (2020), confined equitable disgorgement to net profits applied for victims — a statutory clawback is not so confined, but the section adopts *Liu*'s destination logic by choice (restitution first, fund second) because a clawback that pays victims before treasuries is the version a court enforces without flinching. The insurance ban follows the NSW Work Health and Safety Act 2011 pattern in its post-2020 form: s 272 voids contracting-out terms; s 272A makes entering into, providing, and taking the benefit of penalty insurance each an offence, with officer accessorial liability at s 272B — the only jurisdiction located that has run the full experiment, and the reason SEC. 7(b) reaches the provider and the beneficiary, not only the insured entity. Defence costs are expressly preserved (advancement against an undertaking to repay on a knowing or wilful adjudication, the corporate-law norm): the line every model above draws is that *penalties* are uninsurable, not *defence* — a statute that starved defendants of counsel would deserve the constitutional attack it would get, and the deterrence case does not need it. What the ban protects is the Act's core wager: *Park*-doctrine liability works because the consequence lands on the person. An indemnified penalty is a premium; SEC. 7(b) is the difference between a penalty schedule and a price list.

**n.19 ON SEC. 10 (CALIBRATION).** The brackets carry the enacted family's own figures: Cal. Bus. & Prof. Code § 22757.15(a) (\$1,000,000 per violation, severity-scaled); N.Y. Gen. Bus. Law § 1427 as replaced by ch. 96, L. 2026 (\$1,000,000 / \$3,000,000 first/subsequent — the chapter amendment that cut ch. 699's \$10,000,000 / \$30,000,000 by ten times); 5 ILCS [—]/25(a), P.A. 104-0538 (\$1,000,000 / \$3,000,000, adding failure-to-audit as a trigger). Three enactments, one sentence, one bracket: no element of this Act is better anchored, and "invented numbers" dies on contact with the table in the chunk 3 file. The per-day continuing-violation structure is 33 U.S.C. § 1319(d)'s, as v3.2 already held, and the live proof that indexing works is 40 C.F.R. § 19.4: the CWA's \$25,000 became \$68,445 by rule while the FDCA's \$1,000 sat nominal since 1938 awaiting 18 U.S.C. § 3571 to rescue it — *Park*'s fifty dollars a count being the terminal case. The individual fines take § 3571(b) parity (\$100,000 / \$250,000), the harm tier takes § 1350's \$1,000,000 counted per victim, and every criminal fine carries § 3571(d)'s alternative — "twice the gross gain" — which state penal law already speaks natively (N.Y. Penal Law § 80.00(1): the higher of \$5,000 "or double the amount of the defendant's gain"); adopting states conforming these brackets to local fine grids shall preserve the gain alternative, adopting it with the Act where the grid lacks it. On § 841(b): this Act borrows the per-victim counting and the *Burrage* causation rule, and takes as its ceiling the twenty years that § 841(b)(1)(C) sets *as the base maximum*; where death results the federal pattern makes twenty the floor of a range running to life, and this Act deliberately declines that floor (its own floor is the bracketed [two] years, held open at READ FIRST item 3 for a criminal-law scholar). The deterrence design is stated once, honestly: the civil figures are for legibility and family-parity; the economic-benefit floor, the gain multiplier, the per-day accrual, and the index do the scaling (Becker, *Crime and Punishment: An Economic Approach*, 76 J. Pol. Econ. 169 (1968); Gneezy & Rustichini, *A Fine Is a Price*, 29 J. Legal Stud. 1 (2000); on why fines alone cannot reach the judgment-proof or the equity-rich, Shavell, *The Judgment Proof Problem*, 6 Int'l Rev. L. & Econ. 45 (1986)); and the instruments that reach what no fine reaches are SEC. 6, SEC. 7, and SEC. 10(d)(4). Proportionality: the Excessive Fines Clause binds the states, *Timbs v. Indiana*, 586 U.S. 146 (2019), on *Bajakajian*'s gross-disproportionality test, 524 U.S. 321 (1998); a floor tied to the violator's benefit and a ceiling tied to twice it are proportioned to the offense by construction, the § 1319(d) factors and consecutive-sentencing discretion valve the stack, and the outbreak-scale stress test remains open at READ FIRST item 4.

**n.20 ON SEC. 5(d).** Narrowed to statements made to this State's own government, on chunk 2 §I.5's analysis. The offense remains free-standing — it creates no duty to speak and compels no disclosure; it punishes choosing to speak falsely to the sovereign, the structure of 18 U.S.C. § 1001 and of the false-statement offenses the *Alvarez* plurality preserved, 567 U.S. 709 (2012), and it is therefore no Covered Subject Area's occupant (FRONTIER CSA(1) governs *what must be disclosed*, not whether what is said must be true — chunk 2 §C.4, lane 2). Striking "any regulator" gives up lies told to federal and sister-state authorities, which were never this State's to punish (18 U.S.C. § 1001 and the sister states' own law reach them), and buys the offense out of the two arguments chunk 2 rated against it: the CSA(1) overlap reading built on the phrase's breadth, and an extraterritoriality objection under the amended SEC. 1(c). The offense survives the suspension of SEC. 9 entirely: silence never violates 5(d); only a false answer does.

---

## G. CARRIED QUESTIONS

**For chunk 4 (records and retention):** SB 53 and SB 315 retention periods against SEC. 12's [5] years (carried from chunks 1–2, now with the further reason that SEC. 7(a)'s attribution presumption runs on compensation records); harmonise or justify against the regs draft's Part 10 [7]-year figure; note IL § 25(c)/NY's equity-loss exclusion when touching the harm definitions.

**For chunk 5 (with the regulations draft):** the SEC. 9(a) recast (chunk 2 §E.3(d)); regs Part 8 must be conformed to SEC. 10(a) as amended (recidivist step; fund destination now Part 8.4 → SEC. 10(f)).

**For the cite-check:** confirm the "determined based on the severity of the violation" clause of GBL § 1427 (B.1 ⚠); pin NSW s 272A and its penalty-unit maxima from primary when reachable (A.1/§C ⚠); pin GAAIA's penalty section from the discussion-draft PDF itself (§C ⚠ — the sponsor-server path used at chunk 2 returned 404 this sweep); assign the Illinois Act its ILCS compilation cite (the enrolled text is section-numbered internally; the codified location was not pinned); v3.2 n.10's § 841(b) sentence is superseded by n.19's recast (A.2).

**Standing watch (unchanged from chunk 2, re-swept 16 Aug 2026):** *xAI v. Bonta*, No. 26-1591 (9th Cir.) — argued 16 July 2026, no decision located this sweep ⚠; FRONTIER Act markup; GAAIA introduction; FTC policy statement finalisation; Commerce list publication.

---

## I. WHERE THE ARCHITECTURE IS THIN

**I.1 The first draft's clawback was mandatory, gross, and valveless — a penalty stacked on penalties with no impracticability exit.** Attacked, it lost to its own table: *Kokesh* makes such an order a penalty, and a mandatory gross-measure clawback atop the § 3571(d) multiplier atop the benefit-floored civil penalty invites a *Bajakajian* aggregate at exactly the wrong moment (the harm-tier case, when the optics are worst). Cured: court-found attribution with a rebuttable/permissive presumption, a collection-cost exit (10D-1's narrowest out, the only one that translates), restitution-first destination, express limitations tie. Residual: "attributable to the violation" still hands the fight over gross versus net to the courtroom. That is deliberate — a statutory formula precise enough to end the fight would be precise enough to plan around — but it is a fight, and the note says so.

**I.2 "Purpose or predominant effect" in SEC. 7(b)(2) is the clause a hostile reader calls vague.** It is the anti-circumvention test for compensation offsets (the gross-up, the conveniently timed retention bonus), and it cannot be written as a bright line without licensing the workaround one increment outside the line. The exposure is contained: a bare (b)(2) violation is civil only (SEC. 10(a) via (b)(4)); criminal exposure requires a *knowing* violation by a controlling person, which carries the scienter that answers vagueness at the margin. Thinnest clause in the chunk; flagged, kept.

**I.3 The insurer-side offence mostly cannot be enforced against the insurers.** A D&O carrier with no Illinois-style in-state footprint, writing under foreign law, is beyond practical reach of SEC. 7(b)(1)(B) however sound the SEC. 1(c) conduct-into-state theory reads on paper. The section is drafted so that this does not matter: the arrangement is void here, the *receipt* is an in-state offence by an in-state-reachable person, and the constructive trust strips the benefit whoever pays it. The ban's enforcement surface is the executive, not the carrier. NSW's decade is the empirical comfort ⚠ (no located NSW prosecution of a foreign insurer either — the market simply stopped writing the cover).

**I.4 The stack is the Eighth Amendment exposure, and this chunk did not close it.** Per-day accrual × the 3× recidivist step × per-victim consecutive counting is exactly the multiplication READ FIRST item 4 flags at outbreak scale. The self-proportioning elements (floor and multiplier tied to gain) answer the *civil* stack; the *criminal* per-victim stack at Sulfanilamide's 107 counts is the proportionality scholar's question and remains assigned to one, not resolved here.

**I.5 The calibration's political-economy premise is falsifiable and stated as data, not destiny.** §D reads the CA→NY→IL compression as the enactable ceiling for civil figures. A post-catastrophe legislature would enact multiples of these numbers before lunch. The design survives that world — the formulas scale and the brackets are brackets — but if the premise is wrong in the other direction (the family's numbers themselves prove unenactable somewhere), the Act's civil layer has no fallback below \$1M/day except the court's own factor-weighing. Accepted: below that, the layer would be decoration.

**I.6 The SEC. 5(d) narrowing is untested in both directions.** No court has read the CSA(1) overlap argument against the broad version, and none has read the narrow version at all; chunk 2 §I.5's caution — that "it is an argument" — survives the narrowing, reduced but alive. And the narrowing was bought with real coverage: a covered developer lying to Cal OES about an incident with in-state victims of *this* State is out of 5(d)'s reach. SEC. 13(c)(2)(D)'s preservation of the general false-statement law is the answer on the books; whether the adopting state's general law actually reaches that lie is a conforming-amendments question for its counsel (READ FIRST item 9).

---

## H. SOURCES

**State primary (penalties):** ilga.gov, 10400SB0315enr (SB 315 enrolled: Sec. 25 in full; Sec. 18(e); Sec. 99; definitions) and ilga.gov Bill Status for SB 315, 104th GA (P.A. 104-0538; Governor approved 6 Jul 2026); nysenate.gov and assembly.state.ny.us, A9449 / S8828, 2025–26 session (ch. 96, L. 2026, signed 27 Mar 2026; replaced GBL art. 44-B; § 1427 and § 1428 text; effective-date amendment) and nysenate.gov S6953-B (ch. 699, L. 2025, signed 19 Dec 2025; then-§ 1422 penalties; A-print percentage-of-compute history); legiscan.com CA SB 53 enrolled mirror (Bus. & Prof. Code §§ 22757.15(a)–(b), 22757.11 thresholds) — leginfo.legislature.ca.gov robots-excluded from this environment, disclosed per house rule.

**Federal primary:** ecfr.gov, 40 C.F.R. § 19.4 (CWA § 309(d) adjusted maximum \$68,445, effective 8 Jan 2025) and 17 C.F.R. § 240.10D-1; law.cornell.edu, 18 U.S.C. § 3571, 18 U.S.C. § 3572(a), 15 U.S.C. § 7243, 21 U.S.C. § 333(a), 21 U.S.C. § 841(b); 18 U.S.C. § 1350 and 33 U.S.C. § 1319(d) as already pinned in v3.2 nn.8, 10.

**Cases:** *United States v. DeCoster*, 828 F.3d 626 (8th Cir. 2016) (law.justia.com; sentence quote); *Kokesh v. SEC*, 581 U.S. 455 (2017); *Liu v. SEC*, 591 U.S. 71 (2020); *United States v. Bajakajian*, 524 U.S. 321 (1998); *Timbs v. Indiana*, 586 U.S. 146 (2019); *United States v. Alvarez*, 567 U.S. 709 (2012) (plurality); *Sandstrom v. Montana*, 442 U.S. 510 (1979); *Burrage v. United States*, 571 U.S. 204 (2014) (already in text); *United States v. Park*, 421 U.S. 658 (1975).

**State-native gain-scaling:** nysenate.gov, N.Y. Penal Law § 80.00.

**⚠ secondary, disclosed:** NSW s 272A architecture and penalty units — bnlaw.com.au and concordant Australian firm alerts (legislation.nsw.gov.au and AustLII returned 403/metadata-only this sweep); GAAIA penalty structure — fpf.org, *Frontier AI Goes Federal* ("\$1 million per violation, with each day treated as a separate violation"; sponsor-server PDF 404 this sweep); IL press and firm coverage for context only (gov-pritzker-newsroom.prezly.com; recordinglaw.com; mcdonaldhopkins.com); *xAI v. Bonta* posture — dockets.justia.com and July 2026 press.

**Literature:** Becker, 76 J. Pol. Econ. 169 (1968); Gneezy & Rustichini, 29 J. Legal Stud. 1 (2000); Shavell, 6 Int'l Rev. L. & Econ. 45 (1986).


---

<a id="chunk-4"></a>
<!-- BEGIN audit/chunk4_harm_tier_rebuild.md · sha256:763561d38149 · concatenated 19 Aug 2026, content verbatim -->

# CHUNK 4 — THE HARM TIER REBUILT: PROPORTIONALITY VALVE, RECIDIVIST PATH, AND RETENTION HARMONISATION FOR v3.3

> **UPDATE — closed and executed on four points by chunk 5:** §C's two ⚠ paraphrases are pinned:
> USSG § 5G1.2(d) from the Commission's own archive HTML (the paraphrase was accurate; Amendment
> 767 touched subsection (b) only; 2025-manual identity is a cite-check residual), and MPC § 7.06
> mirror-pinned — the pinned formula is *stricter* than the Kansas double rule (aggregate capped at
> the longest extended term for the gravest offense, no doubling), so the Act's [forty]-year cap
> sits between the MPC and unlimited stacking; n.21's two ⚠s are struck per chunk 5 §F.4(a). §G's
> decision item is executed as instructed: the § 331(e)-lineage records offense took its
> collision-map rating and its First and Fifth Amendment passes at chunk 5 §D.5 and enters as
> SEC. 5(e) (chunk 5 §E.3(b)) — supplying the offense §I.5 named as missing. §E.4(c)–(d)'s
> regulations conforms are executed at chunk 5 §E.6(a)–(b). See chunk 5 §§B.1–B.2, B.4, D.5, E.3,
> E.5–E.6.
> 
Drafting date: 16 August 2026. Method as at chunks 2–3: primary-text pinning of every figure and clause the design rests on, then the design, then the drop-in text, then an adversarial pass in which the drop-ins were attacked rather than checked. As before, the attack found more than the check did; §E is the second draft and §I records what the first draft got wrong.

Verbatim quotation is used wherever the exact words are load-bearing. Anything not retrieved from primary text is marked ⚠ and paraphrased, never quoted. Three primary sources were unreachable from this drafting environment and are disclosed as such (§H): guidelines.ussc.gov (JS-only; USSG § 5G1.2(d) is ⚠ paraphrased), the ALI's Model Penal Code text (not freely retrievable; § 7.06 is ⚠ paraphrased), and leginfo.legislature.ca.gov (robots-excluded, as at chunk 3; the SB 53 pin is from the LegiScan mirror of the enrolled text).

This chunk: corrects and completes earlier material (§A); answers the carried questions on retention (§B); pins the sentencing-structure and retention anchors (§C); sets out the design — the criminal-stack arithmetic, the doctrinal reality, and the structural resolution of n.10's § 841(b) inversion (§D); supplies the drop-in text for SEC. 6(b), SEC. 10(c), and SEC. 12, with conforming amendments (§E); supplies drafting notes n.21–n.23 (§F); and states where the architecture is thin (§I). It closes READ FIRST item 3's questions (a) per-victim consecutive exposure, (d) the recidivist path to the harm tier, and (e) retention harmonisation, and closes item 4 (the Eighth Amendment stress-test at outbreak scale) to the extent drafting can close a question assigned to a proportionality scholar — the scholar should now review a valve rather than design one. Item 3's questions (b) ("serious injury" source) and (c) (the bracketed minimum) remain open for the criminal-law scholar, with an assist for (b) noted at §C.

The § 841(b) instruction is honoured as given: the floor/ceiling inversion recorded at chunk 3 A.2 is resolved *inside the redesign of SEC. 10(c)*, not by a further footnote patch. After §E.2, the Act's harm-tier geometry matches the federal death-results pattern it cites, and the sentence in n.10 that misdescribed § 841(b) is not corrected but superseded.

---

## A. CORRECTIONS AND COMPLETIONS TO EARLIER MATERIAL

**A.1 — v3.2 SEC. 12 keys its ten-year limitations period to a penalty subsection, not an offense.** The sentence reads: "a prosecution under SEC. 10(c)(2) may be commenced within [ten] years." Nothing is prosecuted *under* SEC. 10(c)(2); it is a penalty schedule. Prosecutions are brought for offenses under SEC. 6(b), to which SEC. 10(c)(2)'s penalties attach when death or serious injury results. As drafted, the extended period arguably never applies to anything — a defendant would read the general [five]-year period as the only operative one and be right. Cured at §E.3: "for an offense to which SEC. 10(c)(2) applies."

**A.2 — The README's Jensen story is not yet true of the statute.** The README promises: "each person killed or seriously injured is a separate offense, and restitution to each is mandatory," on the authority of the Jensen prosecutions — misdemeanour convictions, "no evidence they knew," restitution \$25,000 per count. But v3.2 places mandatory restitution *inside* the SEC. 6(b) harm tier, which requires knowing or wilful conduct. On v3.2's own text, the Jensen defendants — negligent, not knowing — would owe no mandatory restitution. The counting method the README calls "not invented" is, as drafted, conditioned on a mental state its own exemplars lacked. Cured at §E.2: restitution decouples from the tier and follows the harm (new SEC. 10(c)(4)), on the structure of 18 U.S.C. § 3663A.

**A.3 — Chunk 1's "Records/FOIA (⚠ check)" row for NY and IL: the retention half is now closed from primary; the FOIA half is not.** Retention is pinned at §B.1–B.3. Illinois's disclosure exemption was incidentally pinned (SB 315 § 15(f)(3) exempts, among other records, "any unredacted version of the third party audit report produced under subsection (d) of Section 10"); the New York FOIL-exemption question was not run this sweep and carries to the cite-check.

**A.4 — Supersession record.** v3.2 n.10's harm-tier sentence ("The harm tier follows 21 U.S.C. § 841(b): where knowing violation kills, the ceiling is twenty years, counted per victim") was flagged at chunk 3 A.2 and recast in n.19. The recast is itself superseded by this chunk: n.19's "On § 841(b)" passage describes a twenty-year death ceiling that §E.2 abolishes. At v3.3 assembly, strike that passage from n.19 and use n.21; the conforming amendment is at §E.4(e). Chunk 3's SEC. 10 drop-in (§E.2 there) remains the baseline text amended here — nothing else in it moves.

---

## B. CARRIED QUESTIONS, ANSWERED

The question, carried from chunk 1 §E.8 through chunk 2 §G and chunk 3 §G: SB 53 and SB 315 retention periods against SEC. 12's [5] years, with two accumulated reasons — SEC. 13(c)(2)(C) makes retention the fallback for a preempted reporting duty (chunk 2), and SEC. 7(a)'s attribution presumption runs on compensation records (chunk 3).

**B.1 SB 53 — one retention clause, pinned.** Cal. Bus. & Prof. Code § 22757.12(f) (LegiScan mirror of the enrolled text; leginfo robots-excluded):

> "If a frontier developer redacts information in a document pursuant to this subdivision, the frontier developer shall describe the character and justification of the redaction in any published version of the document to the extent permitted by the concerns that justify redaction and shall retain the unredacted information for five years."

No other retention duty exists in the TFAIA. The whistleblower chapter this bill added to the Labor Code (§ 1107 et seq.) contains none; § 22757.13's incident-reporting provisions require submission, not preservation.

**B.2 SB 315 — two retention clauses, pinned from the enrolled text.** Section 10(d)(3), on the mandatory third-party audit report:

> "The large frontier developer shall retain an unredacted copy of the report for as long as a frontier model is deployed plus 5 years."

Section 10(g)(1), the redaction-shadow clause in the California form: the developer "shall retain the unredacted information for 5 years." No general record-retention requirement exists elsewhere in the Act.

**B.3 New York, conformed to the renumbering.** GBL article 44-B as replaced by ch. 96, L. 2026 contains exactly one retention clause, § 1421(5)(B) (bill-print capitals as at chunk 3 B.1): the frontier developer "SHALL RETAIN THE UNREDACTED INFORMATION FOR FIVE YEARS." A search of the replacement article for "retain" and "as long as" returns nothing else; the deployment-keyed formula appears only in Illinois.

**B.4 What the family teaches — and why harmonisation cannot mean copying.** Every enacted retention clause in the family is *redaction-shadow* retention: keep privately, for five years, the unredacted version of what you published redacted — the same sentence propagating CA → NY → IL, plus Illinois's deployment-plus-five for the audit report. None of it is evidence-grade record-keeping; none of it is keyed to a limitations period, because the family's statutes are civil-penalty regimes with no limitations architecture of their own. The Model Act's SEC. 12 retention exists for a different job: to make a criminal case provable years later, from the filing cabinet, under a statute whose harm-tier prosecutions may commence within [ten] years and whose concealment tolling opens the window later still. The family supplies three things the redesign uses — the five-year figure as the enacted floor, Illinois's deployment-plus-five as the enacted sibling for a deployment-keyed tail, and (negatively) the demonstration that no enacted state figure covers the Act's own limitations window, so the divergence must be justified rather than hidden (§D.5, n.23). The redaction-shadow duty itself is not adopted: the Act's certifications and reports run to the Agency and are not published (chunk 2 §E.3), so there is no published-redacted layer to shadow.

**B.5 The equity-loss exclusion, noted as directed (chunk 3 §B.2).** SB 315 § 25(c): "The loss of value of equity does not count as damage to or loss of property for the purposes of this Act" (New York's sibling concords). No conforming change is needed in the Model Act, and n.23 records why in one sentence: the Act's harm tier runs on death and serious injury per SEC. 1(b)(8) — property damage and economic loss trigger nothing — and where equity value does enter the Act (SEC. 7(a) disgorgement; the § 3571(d)-pattern gain multipliers), it enters as the defendant's *gain*, not as a victim's *loss*, the opposite valence from the one the exclusion polices.

---

## C. THE ANCHOR TABLE — EVERY FIGURE PINNED

Sentencing-structure anchors:

| Anchor | Provision | Pinned content |
|---|---|---|
| The inversion source | 21 U.S.C. § 841(b)(1)(C) | base: "not more than 20 years and if death or serious bodily injury results from the use of such substance shall be sentenced to a term of imprisonment of not less than twenty years or more than life" — death makes twenty the floor and life the ceiling |
| The one § 841(b) death *ceiling* | § 841(b)(1)(E) | "not more than 15 years" (Schedule III) |
| The Act's new geometry, exactly | 18 U.S.C. § 1365(a) (consumer-product tampering) | serious bodily injury: "imprisoned not more than twenty years"; death: "imprisoned for any term of years or for life" |
| Assist for reviewer question (b) | § 1365(h)(3) | "serious bodily injury" = "a substantial risk of death"; "extreme physical pain"; "protracted and obvious disfigurement"; "protracted loss or impairment of the function of a bodily member, organ, or mental faculty" — cf. the Act's 21 C.F.R. § 803.3(w) source |
| Concurrency default | 18 U.S.C. § 3584(a) | "Multiple terms of imprisonment imposed at the same time run concurrently unless the court orders or the statute mandates that the terms are to run consecutively." |
| Findings duty | § 3584(b) | the court "shall consider, as to each offense for which a term of imprisonment is being imposed, the factors set forth in section 3553(a)" |
| Structured stacking | USSG § 5G1.2(d) | ⚠ consecutive service only to the extent necessary to produce a combined sentence equal to the total punishment (guidelines.ussc.gov JS-only this sweep) |
| The double rule | K.S.A. 21-6819(b)(4) | "The total prison sentence imposed in a case involving multiple convictions arising from multiple counts within an information, complaint or indictment cannot exceed twice the base sentence." |
| Findings-gated consecutive | Ohio Rev. Code § 2929.14(C)(4) | consecutive only if "necessary to protect the public from future crime or to punish the offender and that consecutive sentences are not disproportionate to the seriousness of the offender's conduct and to the danger the offender poses to the public," plus one enumerated finding — ⚠ subclauses (a)–(c) paraphrased this sweep |
| Model-law lineage | Model Penal Code § 7.06 | ⚠ aggregate-cap architecture for consecutive terms (ALI text not freely retrievable) |
| The recidivist path, 1938 | 21 U.S.C. § 333(a)(1)–(2) | "(a)(1) … shall be imprisoned for not more than one year or fined not more than \$1,000, or both." "(a)(2) Notwithstanding the provisions of paragraph (1) of this section, if any person commits such a violation after a conviction of him under this section has become final, or commits such a violation with the intent to defraud or mislead, such person shall be imprisoned for not more than three years or fined not more than \$10,000, or both." |
| Records as prohibited act | 21 U.S.C. § 331(e) | prohibits "the failure to establish or maintain any record, or make any report, required under" enumerated sections, and "the refusal to permit access to or verification or copying of any such required record" |
| Mandatory restitution | 18 U.S.C. § 3663A(a)(1), (c)(1) | "the court shall order … that the defendant make restitution to the victim"; reaches offenses "in which an identifiable victim or victims has suffered a physical injury or pecuniary loss" |
| Element rules | *Apprendi v. New Jersey*, 530 U.S. 466 (2000); *Alleyne v. United States*, 570 U.S. 99 (2013); *Burrage v. United States*, 571 U.S. 204 (2014) (already in text) | facts raising the ceiling (*Apprendi*) or the floor (*Alleyne*) are elements for the jury; death-results is such a fact (*Burrage*) |
| The prior-conviction exception, confined | *Almendarez-Torres v. United States*, 523 U.S. 224 (1998); *Erlinger v. United States*, 602 U.S. 821 (2024) | the bare fact of a prior conviction may be judge-found; anything beyond that fact — occasions, conduct, character of the prior — goes to the jury |
| Federal proportionality, the reality | *Harmelin v. Michigan*, 501 U.S. 957, 1001 (1991) (Kennedy, J., concurring in part and in the judgment) | "the Eighth Amendment does not require strict proportionality between crime and sentence, but rather forbids only extreme sentences that are grossly disproportionate to the crime" |
| The stack upheld | *Hutto v. Davis*, 454 U.S. 370 (1982) (per curiam) | two consecutive twenty-year terms and a \$20,000 fine for roughly nine ounces of marijuana; successful challenges "should be exceedingly rare" |
| The recidivist stack upheld | *Ewing v. California*, 538 U.S. 11 (2003); *Lockyer v. Andrade*, 538 U.S. 63 (2003) | three-strikes 25-to-life, and two consecutive 25-to-life terms, upheld |
| The lone reversal | *Solem v. Helm*, 463 U.S. 277 (1983); cf. *Rummel v. Estelle*, 445 U.S. 263 (1980) | life without parole for a \$100 bad check struck; life with parole upheld three years earlier |
| The per-count rule | *Pearson v. Ramos*, 237 F.3d 881, 885–86 (7th Cir. 2001) | "Every disciplinary sanction, like every sentence, must be treated separately, not cumulatively, for purposes of determining whether it is cruel and unusual." — resting expressly on *O'Neil* |
| The founding cautionary tale | *O'Neil v. Vermont*, 144 U.S. 323 (1892) | 307 counts at \$20 each; default converted at three days per dollar: 19,914 days — some 54 years at hard labor. Majority: the Eighth Amendment claim not properly raised and "does not apply to the States." Field, J., dissenting, at 340: "The State may, indeed, make the drinking of one drop of liquor an offense … but it would be an unheard-of cruelty if it should count the drops in a single glass"; a punishment "at the severity of which, considering the offenses, it is hard to believe that any man of right feeling and heart can refrain from shuddering" |
| The live front: state clauses | Ill. Const. art. I, § 11; Or. Const. art. I, § 16 | Illinois: "All penalties shall be determined both according to the seriousness of the offense and with the objective of restoring the offender to useful citizenship." Oregon: "Cruel and unusual punishments shall not be inflicted, but all penalties shall be proportioned to the offense." Concordant clauses without pinned text this sweep: Ind. Const. art. 1, § 16; W. Va. Const. art. III, § 5 ⚠ |

Retention anchors:

| Anchor | Provision | Pinned content |
|---|---|---|
| CA (redaction shadow) | Bus. & Prof. Code § 22757.12(f) | "shall retain the unredacted information for five years" (§B.1 in full) |
| IL (deployment tail) | SB 315 § 10(d)(3); § 10(g)(1) | "for as long as a frontier model is deployed plus 5 years"; five-year redaction shadow |
| NY | GBL § 1421(5)(B) | five-year redaction shadow, nothing else |
| EU decade | AI Act art. 18(1) | "The provider shall, for a period ending 10 years after the high-risk AI system has been placed on the market or put into service, keep at the disposal of the national competent authorities" the listed documentation |
| SOX statute → rule | 18 U.S.C. § 1520(a)(1); 17 C.F.R. § 210.2-06 | "all audit or review workpapers for a period of 5 years from the end of the fiscal period"; extended by rule: "For a period of seven years after an accountant concludes an audit or review of an issuer's financial statements" — the enacted proof that evidence-grade retention runs past its statutory floor |
| The contemplation clause | 18 U.S.C. § 1519 | destruction "in relation to or contemplation of" a federal matter: twenty years — the obstruction shadow the SEC. 12 hold converts into an affirmative duty |
| The rot exhibit's neighbour | 21 U.S.C. § 331(e) | failure to keep required records is itself a prohibited act under the FDCA — the lineage flag for §I.5 |
| CO comparison | SB 26-189 | ⚠ 3-year record-keeping (chunk 1 §B, secondary) |
| Internal | Model Act SEC. 12; regs Part 10.1 | [5] years; [7] years — the two-document architecture currently disagrees with itself |

---

## D. THE DESIGN

**D.1 The arithmetic, run against the Act's own stories.** Sulfanilamide's count was 107. Under v3.2's harm tier — twenty years per victim, consecutive at the court's discretion — the nominal exposure at that scale is 2,140 years, and the bracketed [two]-year floor, if stacked consecutively, is 214 years of *mandatory* imprisonment assembled from a bracket defended as merciful. The founding case already ran this experiment: *O'Neil* — 307 counts of a twenty-dollar offense, mechanically converted to 19,914 days at hard labor — is the per-count machine producing a number no one will defend, and Field's dissent named the mechanism: count the drops. A statute whose honest description is "twenty years per victim, times 107" invites two readings, bluff or cruelty, and either damages the Act. Neither is needed, because federal law has an honest name for the outbreak case, and it is not a four-digit number of years. It is life.

**D.2 The doctrine, honestly.** The federal Eighth Amendment will not police this stack. *Harmelin* reduces noncapital review to gross disproportionality; *Hutto* upheld forty years for nine ounces; *Ewing* and *Lockyer* upheld recidivist 25-to-life, twice over and consecutive; *Solem* stands alone. And the unit of federal review is the count, not the aggregate — *Pearson*: every sentence "treated separately, not cumulatively" — which means the stack as such is likely unreviewable federally *in either direction*: no federal court will strike it, and none will restrain it. The live constraint is the state constitutions this model act will actually be enacted under. Illinois requires penalties "determined both according to the seriousness of the offense and with the objective of restoring the offender to useful citizenship" — a clause with independent bite in Illinois practice; Oregon commands that "all penalties shall be proportioned to the offense"; Indiana and West Virginia carry concordant text ⚠. READ FIRST item 4 asked one proportionality scholar the federal question; the true exposure is fifty state questions, several under clauses stricter than *Harmelin*. The valve is therefore drafted not because the federal Constitution compels it, but because (i) some state constitutions will; (ii) a 2,140-year nominal exposure is a gift to the opposition's op-ed and to no prosecutor except one building plea leverage from absurdity — the § 851 pathology, transplanted; and (iii) concurrency-by-default with findings-gated consecutive service is not mercy but the American mainstream: § 3584(a) is the federal default, Ohio gates consecutive terms behind stated findings, Kansas caps the aggregate at twice the base sentence, and the Model Penal Code has capped aggregates since 1962 ⚠.

**D.3 The inversion, resolved structurally.** Chunk 3 A.2 corrected the *description* of § 841(b); the *geometry* stayed inverted. v3.2's death case carries a lower ceiling (twenty years) than its anchor's death case (life), while its per-victim consecutive exposure runs unbounded above anything the anchor produces — simultaneously milder than § 841(b) at the single count and harsher than it at the aggregate, citing it for both. The rebuild adopts the federal death-results geometry whole, from the statute in the Act's own consumer-protection lineage: 18 U.S.C. § 1365, tampering with consumer products — serious bodily injury, "imprisoned not more than twenty years"; death, "imprisoned for any term of years or for life." That is also § 841(b)(1)(C)'s exact ceiling structure (twenty base; life where death results). So, after §E.2: serious injury carries up to twenty years per offense; death carries any term of years or life per offense; the federal twenty-year mandatory *floor* remains deliberately declined — the Act's floor stays the bracketed [two] years, which is READ FIRST item 3(c) and stays with the criminal-law scholar. Every borrowed element now sits where its source put it: per-victim counting (the ordinary unit of homicide law, and the Jensen count method), *Burrage* causation (in text since v3.2), the life ceiling (both anchors), and no borrowed minimum. n.10's sentence is not patched; the structure it misdescribed no longer exists. And the valve becomes affordable at the same stroke: with life available on a single count, the statute no longer needs unlimited stacking to reach maximal severity, so stacking can be capped and findings-gated at zero cost to the top of the range.

**D.4 The valve — three moving parts, all enacted elsewhere.** (1) *Concurrency default*: terms imposed at the same time run concurrently unless the court orders otherwise — § 3584(a) nearly verbatim. (2) *Findings-gated consecutive service*: consecutive terms only on stated findings addressing the seriousness of each offense, the culpability found under SEC. 6, the totality of the harm, and the proportion of the aggregate to the whole of the conduct — the Ohio § 2929.14(C)(4) chapeau married to § 3584(b)'s factor duty. (3) *The double-rule cap*: consecutive determinate terms for offenses arising from the same violation or course of conduct aggregate to no more than [forty] years — twice the serious-injury ceiling, the Kansas formula rather than an invented figure — with an express saving: nothing limits a life term where death results. Two element rules ride with the tier: death or serious injury resulting, and the identity of each person, are jury elements (*Apprendi*, *Alleyne*, *Burrage*); and minimum terms attach to each offense severally and are satisfied by concurrent service — floors never stack by operation of law. The per-victim fine (\$[1,000,000] per offense, chunk 3) aggregates subject to the means-consideration sentence and the Excessive Fines Clause backstop already documented at n.19 (*Timbs*; *Bajakajian*); no new fine text is needed. What the valve does not touch: the counting itself. Conviction remains per victim; restitution remains per victim; the judgment names each person. What is capped is only the pretence that 2,140 is a number any court would impose.

**D.5 The recidivist path, split.** v3.2 SEC. 6(b) holds four scienter prongs and one recidivist prong in a single sentence, so a purely negligent repeat violation inherits everything the sentence carries: felony penalties (correct — that is 21 U.S.C. § 333(a)(2), the 1938 pattern, verbatim at §C: prior final conviction *or* intent to defraud elevates the strict-liability misdemeanour to a three-year felony) and eligibility for the death tier (incorrect — no statute in the lineage routes negligence-plus-priors into a twenty-to-life-shaped tier; § 841(b)'s death enhancement rides on knowing distribution, § 1365's on reckless-disregard tampering; and the Morissette bargain the Act states at n.2 — where imprisonment is possible, fault is an element — scales: where imprisonment is gravest, the fault element must be gravest). §E.1 splits the subsection: 6(b)(1) carries the scienter prongs and alone opens the harm tier; 6(b)(2) carries the recidivist prong and elevates to the base felony penalties of 10(c)(1) only. The recidivist who negligently kills again answers to the base felony ceiling, mandatory per-victim restitution (new 10(c)(4)), the economic stack of SEC. 7, and — the incapacitation tool actually fitted to the case — disqualification under SEC. 10(d)(4). Constitutional dividend, drafted in: the prong turns on the bare fact of a prior final conviction under this Act and the date of the new violation, and on nothing else — no occasions inquiry, no conduct inquiry — so it lives entirely inside *Almendarez-Torres* as *Erlinger* confined it, and no jury finding on the prior is ever required. The [ten]-year washout is retained (more merciful than § 333(a)(2), which has no lookback limit); finality follows § 333(a)(2)'s own "has become final."

**D.6 Retention and limitations — the covering principle.** The rule the redesign enforces: *no record that a surviving offense would need may lawfully die while a prosecution for that offense remains timely.* v3.2 breaks it twice — retention [5] years against a harm-tier limitations period of [ten]; retention [5] years against concealment tolling that starts the clock at discovery, potentially decades out — and the two-document architecture breaks it a third way, with regs Part 10.1 holding [7] against the statute's [5]. The rebuild (§E.3): baseline retention of [ten] years from creation, matching the Act's own longest limitations period and the enacted EU decade for high-risk providers (art. 18(1)); a deployment tail of [five] years after the covered system last operates in the State, whichever ends later — Illinois's own "deployed plus 5" formula, scaled to the document that needs it; a litigation hold from notice of a critical safety incident, investigation, or proceeding until its conclusion — 18 U.S.C. § 1519's "in relation to or contemplation of" exposure restated as an affirmative duty, which converts concealment-by-shredding from an obstruction case someone else must build into a retention violation provable from the absence in the filing cabinet, the Act's own enforcement logic; and compensation records join the audit list, because SEC. 7(a)'s attribution presumption is unusable without them (chunk 3's carried reason). The divergence from the enacted family is justified, not hidden: the family's five-year figures are transparency-shadow retention in civil statutes with no limitations architecture; this Act's retention is the evidentiary floor of a criminal statute whose own text promises prosecutions at year ten. Sizing note for the cite-check: the [ten]/[five]/hold structure is drafted so the *baseline* covers the ordinary limitations window and the *hold* covers tolled and extended windows; retention is not sized to the concealment rule's outer bound, because a duty to keep everything forever against the possibility of one's own future concealment is not a duty anyone performs, and the hold plus § 1519's shadow police that case better than a number can. Chunk 2 §I.3's caution is restated rather than resolved: FRONTIER CSA(2)(C) reaches requirements to "provide access to … evaluation results" for third-party assessment; the retention duty here is production-on-lawful-process in enforcement, held by whoever holds the records including non-developer providers and deployers, and it remains the designated fallback (SEC. 13(c)(2)(C)) — lengthening it raises the value of the fallback and does not change the exposure in kind.

---

## E. DROP-IN TEXT FOR v3.3

House convention as at chunks 2–3: set out in full, no ellipsis; in amended sections, struck text is not reproduced and inserted text is **bold**. SEC. 6(b) and SEC. 10(c) are restructured, so each is set out clean (the chunk 3 §E.2 text of SEC. 10 remains the baseline for subsections (a), (b), (d), (e), and (f), which do not move).

### E.1 — SEC. 6(b), replaced in full

> (b) *Enhanced tier.* (1) A person who knowingly or wilfully causes, directs, conceals, or materially facilitates a violation of SEC. 5, or who deliberately fails to halt a violation after notice, or who knowingly makes a false certification under SEC. 8, is subject to the felony penalties of SEC. 10(c). Where a violation described in this paragraph is a but-for cause of death or of serious injury to any person, the penalties of SEC. 10(c)(2) apply, and each person killed or seriously injured constitutes a separate offense. Notice under this paragraph includes any report or preliminary notice filed under SEC. 9 concerning the same class of risk.
>
> (2) A person who commits any violation of SEC. 5 within [ten] years after a prior conviction of that person under this Act has become final is subject to the felony penalties of SEC. 10(c)(1). This paragraph operates upon the fact of the prior conviction, its finality, and the date of the new violation, and upon nothing else; it neither requires nor permits inquiry into the conduct underlying the prior conviction. The penalties of SEC. 10(c)(2) do not apply by reason of this paragraph.

Drafting deltas from v3.2, for the record: the four scienter prongs and the recidivist prong separate into paragraphs (1) and (2); the harm-tier sentence moves inside (1) and its cross-reference narrows from "this subsection" to "this paragraph," which is the entire operative change; (2)'s second sentence is the *Erlinger* guard; (2)'s third sentence closes the recidivist path to the harm tier. The notice sentence is unchanged in substance.

### E.2 — SEC. 10(c), replaced in full

> (c)(1) Enhanced tier under SEC. 6(b): [felony; imprisonment up to three years; fine up to \$[250,000] or, if greater, twice the gross pecuniary gain to the person derived from the violation].
>
> (c)(2) Enhanced tier under SEC. 6(b)(1) where death or serious injury results: [felony]. (A) Where serious injury results, imprisonment up to twenty years for each offense. (B) Where death results, imprisonment for any term of years or for life for each offense, and not less than [two] years. (C) In either case, a fine up to \$[1,000,000] for each offense or, if greater, twice the gross pecuniary gain to the person derived from the violation. (D) "But-for cause" bears the meaning given in Burrage v. United States, 571 U.S. 204 (2014); that death or serious injury resulted, and the identity of each person killed or seriously injured, are elements of each such offense, to be charged and found by the trier of fact beyond a reasonable doubt.
>
> (c)(3) Concurrent and consecutive service. Terms of imprisonment imposed under this Act at the same time run concurrently unless the court orders consecutive service. The court may order consecutive service only upon findings, stated on the record, that consecutive service is necessary to reflect the seriousness of each offense, the culpability found under SEC. 6, and the totality of the harm, and that the aggregate term is not disproportionate to the whole of the person's conduct and culpability. The aggregate of the determinate terms ordered to run consecutively for offenses under this Act arising out of the same violation or course of conduct shall not exceed [forty] years. Nothing in this paragraph limits the imposition of a term of imprisonment for life where death results. A minimum term under this subsection attaches to each offense severally and is satisfied by concurrent service.
>
> (c)(4) Restitution. Whenever death or serious injury results from an offense under this Act, whatever its tier, the court shall order restitution to each person killed or seriously injured, or to the person's estate, per the structure of 18 U.S.C. § 3663A; "results" bears the same meaning as in paragraph (2). Restitution has priority over every penalty, fine, and disgorgement in the application of a defendant's assets. In fixing a fine for a natural person under this Act, the court shall consider the person's income, earning capacity, and financial resources, so that like culpability bears like burden.

Drafting deltas from the chunk 3 baseline, for the record: (c)(2) keys to SEC. 6(b)(1), splitting the injury and death ceilings per 18 U.S.C. § 1365(a) — the death ceiling rises from twenty years to any term of years or life, and the § 841(b) inversion thereby ends; the bracketed [two]-year floor is retained and remains READ FIRST item 3(c); the element sentence (D) is new (*Apprendi*/*Alleyne*/*Burrage*); (c)(3) replaces "sentences for separate offenses under SEC. 6(b) may run consecutively" with the valve — concurrency default (18 U.S.C. § 3584(a) pattern), findings gate (Ohio Rev. Code § 2929.14(C)(4) chapeau; § 3584(b)), the [forty]-year double-rule cap on consecutive determinate terms (K.S.A. 21-6819(b)(4) formula: twice the twenty-year serious-injury ceiling), the life saving, and the no-stacking rule for minimum terms; (c)(4) is new — restitution decouples from the harm tier and follows the harm (A.2; the Jensen method made statutory), absorbing chunk 3's restitution-priority and means-consideration sentences without substantive change, and tying "results" to the Burrage meaning so the decoupled duty does not carry a looser causation standard than the tier it left. The adopting-state brackets are unchanged in kind.

### E.3 — SEC. 12, retention and limitations, amended

The records clause, set out in full as amended:

> records sufficient for audit (version identifiers, compute records, evaluation results, tool and permission manifests, change histories**, and the compensation records upon which SEC. 7(a) operates**) retained **for [ten] years from creation, or for [five] years after the covered system last operates in or is last deployed in or into this State, whichever period ends later; and, from the time the entity or any controlling person has notice of a critical safety incident, of an investigation, or of a proceeding under this Act to which the records are reasonably relevant, the records shall be preserved until the conclusion thereof**;

The limitations sentence, set out in full as amended (the A.1 cure in bold):

> A prosecution under this Act shall be commenced within [five] years after the violation; for a continuing violation, within [five] years after its last day; where the violation was concealed by an affirmative act, within [five] years after its discovery by the Agency or the Attorney General; a prosecution **for an offense to which** SEC. 10(c)(2) **applies** may be commenced within [ten] years.

### E.4 — Conforming amendments

**(a) SEC. 8, final sentence:** strike "is an offense under SEC. 6(b)" and insert "**is an offense under SEC. 6(b)(1)**".

**(b) SEC. 7(b)(4) (chunk 3 §E.1 text):** strike "is a violation of SEC. 5 for purposes of SEC. 6(b)" and insert "**is a violation of SEC. 5 for purposes of SEC. 6(b)(1)**".

**(c) Regulations Part 5.5 (for chunk 5):** conform "fixes notice for purposes of SEC. 6(b)" to SEC. 6(b)(1).

**(d) Regulations Part 10.1 (for chunk 5):** strike "[7] years" and insert a cross-reference — retention "for the periods provided by SEC. 12 of the Act" — so the two-document architecture cannot disagree with itself again.

**(e) Drafting note n.19 (chunk 3 §F):** strike the passage beginning "On § 841(b): this Act borrows" and ending "held open at READ FIRST item 3 for a criminal-law scholar)." and insert: "**On § 841(b) and the harm-tier geometry, see n.21.**"

**(f) v3.2 n.10:** the sentence "The harm tier follows 21 U.S.C. § 841(b) … The Act declines to price them as one." is superseded in full by n.21 at v3.3 assembly (A.4).

**(g) SEC. 7(a) (chunk 3 §E.1 text):** strike "applied first to restitution ordered under SEC. 10(c)(2)" and insert "**applied first to restitution ordered under SEC. 10(c)(4)**" — restitution's new home after E.2.

**(h) Drafting note n.6 (v3.2):** in the sentence "SEC. 6(b) states its mental element expressly," strike "SEC. 6(b)" and insert "**SEC. 6(b)(1)**", and append: "**SEC. 6(b)(2) is a recidivist enhancement resting on the fact of a prior final conviction, not a scienter offense; see n.22.**" Without this conform, the split at E.1 would falsify n.6's answer to Ruan and Rehaif on contact.

---

## F. NEW DRAFTING NOTES

**n.21 ON SEC. 10(c) (THE HARM TIER AND THE VALVE).** The tier geometry is 18 U.S.C. § 1365(a) — the consumer-product tampering statute: serious bodily injury, "imprisoned not more than twenty years"; death, "imprisoned for any term of years or for life" — which is also the ceiling structure of 21 U.S.C. § 841(b)(1)(C) ("not more than 20 years," and where death results "not less than twenty years or more than life"). What this Act borrows from § 841(b) is the per-victim counting practice and the *Burrage* causation rule, stated in text; what it takes from both anchors is the ceiling pair (twenty; life); what it deliberately declines is the federal mandatory floor — the Act's death-results minimum stays the bracketed [two] years, held at READ FIRST item 3(c) for a criminal-law scholar. Each resulting death or serious injury is a separate offense with the victim's identity an element (*Apprendi v. New Jersey*, 530 U.S. 466 (2000); *Alleyne v. United States*, 570 U.S. 99 (2013); *Burrage*, in text): the counting is the ordinary unit of the law of offenses against the person, and it is the Jensen counting — 33 dead, restitution per count. The valve in (c)(3) is assembled entirely from enacted sentencing law: the concurrency default is 18 U.S.C. § 3584(a) ("Multiple terms of imprisonment imposed at the same time run concurrently unless the court orders … otherwise"); the findings gate is the chapeau of Ohio Rev. Code § 2929.14(C)(4) (consecutive service only where "necessary … and … not disproportionate to the seriousness of the offender's conduct and to the danger the offender poses") joined to § 3584(b)'s per-offense factor duty; the [forty]-year cap on consecutive determinate terms is the Kansas double rule (K.S.A. 21-6819(b)(4): the total "cannot exceed twice the base sentence") applied to the twenty-year serious-injury ceiling, in the Model Penal Code's aggregate-cap tradition (§ 7.06 ⚠); and USSG § 5G1.2(d) ⚠ supplies the federal practice of stacking only to the point the total punishment requires. The valve exists because the doctrine will not: federal proportionality review of noncapital terms is *Harmelin*'s narrow principle (501 U.S. at 1001 (Kennedy, J., concurring in part and in the judgment): the Amendment "forbids only extreme sentences that are grossly disproportionate to the crime"), under which forty years for nine ounces survived (*Hutto v. Davis*, 454 U.S. 370 (1982) (per curiam)), recidivist 25-to-life survived twice (*Ewing v. California*, 538 U.S. 11 (2003); *Lockyer v. Andrade*, 538 U.S. 63 (2003)), and *Solem v. Helm*, 463 U.S. 277 (1983), stands alone — and because the federal unit of review is the count, not the aggregate (*Pearson v. Ramos*, 237 F.3d 881, 885–86 (7th Cir. 2001): every sentence "treated separately, not cumulatively"), the stack is unreviewable federally in both directions. The controlling law will be the adopting states' own proportionality clauses — Ill. Const. art. I, § 11 ("All penalties shall be determined both according to the seriousness of the offense and with the objective of restoring the offender to useful citizenship"); Or. Const. art. I, § 16 ("all penalties shall be proportioned to the offense"); Ind. Const. art. 1, § 16; W. Va. Const. art. III, § 5 ⚠ — several of them stricter than *Harmelin*, all of them senior to any model act. The cautionary precedent is the per-count machine itself: *O'Neil v. Vermont*, 144 U.S. 323 (1892) — 307 twenty-dollar counts converted at three days a dollar into 19,914 days at hard labor, with Field's dissent naming the mechanism ("it would be an unheard-of cruelty if it should count the drops in a single glass," id. at 340). Sulfanilamide's count was 107; v3.2's nominal exposure at that scale was 2,140 years. This Act declines to price the victims as one — conviction, judgment, and restitution remain per person — and equally declines to pretend that 2,140 is a sentence: where the harm is at outbreak scale, the honest name for the penalty is the one every federal death-results statute already uses, life, available on a single count, with consecutive determinate terms gated behind stated findings and capped at twice the injury ceiling. Fines under the tier aggregate per victim subject to the means-consideration sentence of (c)(4) and the Excessive Fines Clause (*Timbs*; *Bajakajian*; n.19): the fine stack is self-proportioning through the gain tie, and the imprisonment stack is proportioned by (c)(3), which is the division of labour the anchors themselves use.

**n.22 ON SEC. 6(b) (THE RECIDIVIST PATH).** The path is the FDCA's own, quoted exactly: 21 U.S.C. § 333(a)(2) — "if any person commits such a violation after a conviction of him under this section has become final, or commits such a violation with the intent to defraud or mislead, such person shall be imprisoned for not more than three years" — the 1938 design in which a prior final conviction and fraudulent intent are *alternative* routes to the same three-year felony. SEC. 6(b) keeps both routes and corrects the one respect in which v3.2 exceeded its source: in v3.2 the recidivist prong shared a sentence with the scienter prongs and therefore shared the death tier, so negligence-plus-priors could in principle draw twenty years per victim. No statute in the lineage does that — § 841(b)'s death range rides on knowing distribution, § 1365's on reckless-disregard tampering, and § 333(a)(2) itself tops out at three years with no harm tier at all — and the Morissette bargain as this Act states it (n.2) scales: where the penalty is gravest, the mental state proved must be gravest. Hence the split: 6(b)(1) alone opens SEC. 10(c)(2); 6(b)(2) elevates the repeat violator to the base felony of 10(c)(1) and stops. The repeat violator whose negligence kills is answered by the base felony ceiling, by mandatory per-victim restitution under 10(c)(4) — the Jensen outcome, misdemeanants included — by SEC. 7's economic consequences, and by disqualification under SEC. 10(d)(4), which is the remedy actually fitted to demonstrated unfitness to hold the authority (Friedman v. Sebelius, n.10). The prong is drafted to the prior-conviction exception as currently confined: the bare fact of a prior conviction may be found by the court (*Almendarez-Torres v. United States*, 523 U.S. 224 (1998)), but any inquiry beyond that fact belongs to the jury (*Erlinger v. United States*, 602 U.S. 821 (2024)), and 6(b)(2) therefore operates "upon the fact of the prior conviction, its finality, and the date of the new violation, and upon nothing else" — there is no occasions inquiry to send anywhere. The [ten]-year washout is retained and is more merciful than the source, which has none; finality is § 333(a)(2)'s own word. The civil layer's recidivism step (SEC. 10(a), 3×, the NY/IL enacted pattern) is unaffected (n.19).

**n.23 ON SEC. 12 (RETENTION AND LIMITATIONS).** The governing principle: no record a surviving offense would need may lawfully die while a prosecution for that offense remains timely. v3.2 broke it twice (retention [5] against the harm tier's [ten]; retention [5] against concealment tolling that runs from discovery) and the companion regulations broke it a third way (Part 10.1's [7] against the statute's [5]). The periods are rebuilt on three enacted anchors. The baseline — [ten] years from creation — covers the Act's own longest limitations period and matches the enacted EU decade for high-risk systems (AI Act art. 18(1): documentation kept "for a period ending 10 years after the high-risk AI system has been placed on the market or put into service"); the direction of regulatory travel is the same in U.S. practice, where Sarbanes–Oxley's five-year statutory floor (18 U.S.C. § 1520(a)(1)) became seven by rule (17 C.F.R. § 210.2-06). The deployment tail — [five] years after the system last operates or is deployed in the State — is Illinois's own formula for the record that matters most there, quoted from the enrolled text: the audit report is kept "for as long as a frontier model is deployed plus 5 years" (SB 315 § 10(d)(3)). The hold — preservation from notice of an incident, investigation, or proceeding until conclusion — restates 18 U.S.C. § 1519's "in relation to or contemplation of" exposure as an affirmative duty, with a design consequence: concealment by destruction stops being an obstruction case the State must build from intent and becomes a retention violation provable from the absence in the filing cabinet, which is this Act's enforcement logic throughout (regs Part 6: the missing writing is the violation), and which is how the retention clause underwrites the concealment-tolling clause it sits beside. Compensation records join the audit list because SEC. 7(a)'s attribution presumption runs on them (n.18). Against the enacted state family the divergence is justified rather than hidden: the family's retention is redaction-shadow transparency retention — California's § 22757.12(f), New York's § 1421(5)(B), and Illinois's § 10(g)(1) are one five-year sentence propagating, in civil statutes with no limitations architecture — while this Act's retention is the evidentiary floor of a criminal statute that promises prosecutions at year [ten]; the family supplies the floor figure, Illinois supplies the tail formula, and nothing in the family contradicts the decade because nothing in the family contemplates a prosecution. Two boundaries are recorded. First, the limitations fix: the extended period now attaches to "an offense to which SEC. 10(c)(2) applies," curing v3.2's citation of a penalty schedule as a unit of prosecution. Second, the equity-loss note directed by chunk 3: SB 315 § 25(c) ("The loss of value of equity does not count as damage to or loss of property for the purposes of this Act," NY concordant) needs no analogue here — the harm tier runs on death and serious injury per SEC. 1(b)(8), property and economic loss trigger nothing, and where equity value enters this Act it enters as the violator's gain (SEC. 7(a); the twice-gain fines), not the victim's loss. Preemption posture unchanged from chunk 2 §I.3: retention is the designated fallback under SEC. 13(c)(2)(C), held by whoever holds the records including non-developer providers and deployers; FRONTIER CSA(2)(C)'s access clause remains an arguable reach and remains disclosed.

---

## G. CARRIED QUESTIONS

**For chunk 5 (with the regulations draft):** conform Part 10.1 to the SEC. 12 cross-reference (E.4(d)) and Part 5.5 to SEC. 6(b)(1) (E.4(c)); the SEC. 9(a) recast (chunk 2 §E.3(d)) and the Part 8 conforms (chunk 3 §G) stand; and consider whether a retention/records offense belongs in SEC. 5 itself, on the lineage of 21 U.S.C. § 331(e) (failure "to establish or maintain any record" as a prohibited act) — flagged at §I.5, not drafted here, because a new prohibited act needs a chunk 2 collision-map rating before it needs words.

**For the cite-check:** USSG § 5G1.2(d) and MPC § 7.06 quoted from reachable primary (both ⚠ paraphrased this sweep); Ohio Rev. Code § 2929.14(C)(4)(a)–(c) subclauses verbatim (chapeau pinned); Ind. Const. art. 1, § 16 and W. Va. Const. art. III, § 5 text; *Erlinger*'s official U.S. Reports pagination (cited here as 602 U.S. 821); the NY FOIL half of chunk 1's Records/FOIA row (A.3); GBL § 1427's severity clause (chunk 3 B.1 ⚠, stands).

**Standing watch (re-swept 16 August 2026, same day as chunk 3 — unchanged):** *xAI v. Bonta*, No. 26-1591 (9th Cir.) argued 16 July 2026, no decision located ⚠; FRONTIER Act referred, no markup located; GAAIA not introduced; FTC policy statement proposed only; Commerce list unpublished; no suit located against SB 53, RAISE, or SB 315.

---

## I. WHERE THE ARCHITECTURE IS THIN

**I.1 The headline is now "life imprisonment for AI executives," and that is a choice to defend, not an accident to explain.** The first draft tried to keep the twenty-year death ceiling to avoid the headline and cap the stack instead; it collapsed in the attack, because it reproduced the inversion (a statute citing § 841(b) while capping death below § 841(b)'s no-death base) and because a twenty-year ceiling with a [forty]-year stack cap prices two deaths at double one death but 107 at the same [forty] — arbitrary at both ends. The enacted pattern is uniform — where death results, the federal ceiling is life (§ 841(b)(1)(C); § 1365(a)) — and the Act now says so, with the floor still [two] bracketed years against the federal twenty. The defence writes itself from the Act's own materials; the optics still belong to whoever quotes first.

**I.2 "Same violation or course of conduct" is the cap's soft joint.** A prosecutor can structure around [forty] by charging violations as separate courses of conduct (different days, systems, or configurations); "course of conduct" is undefined and borrows a contested phrase. The mitigation is real but partial: the findings gate governs *all* consecutive service, capped or not, and the concurrency default holds wherever the findings are not made. A definition was drafted and discarded — every candidate either re-imported federal grouping doctrine wholesale or handed the defence a severance tool. The joint is left soft and disclosed.

**I.3 Concurrency-by-default will be read by some as leniency, and the reading is wrong but not baseless.** v3.2's "may run consecutively" performed severity; (c)(3) performs regularity — § 3584(a) is the default under which every stacked federal sentence is nonetheless imposed. The outbreak case is reachable through findings plus the life ceiling. But a state whose sentencing culture treats consecutive service as the norm will conform the default out, and the brackets permit it; the note does not pretend otherwise.

**I.4 The recidivist split buys the Morissette bargain at a real price: the repeat negligent killer caps at three years.** The answer is the rest of the stack — restitution per victim, SEC. 7, disqualification — and the fact that the FDCA's own path (§ 333(a)(2)) tops out identically with no harm tier at all. But name the residue: a person twice convicted, negligent again, with victims, is answered mainly by incapacitation (10(d)(4)) rather than years, and a legislature that finds that intolerable will widen 6(b)(1)'s "deliberately fails to halt after notice" — which, per the notice-wire design (SEC. 9; regs Part 4 rep. 5), most real repeat cases will satisfy anyway. That last point is the practical answer: the recidivist with a prior conviction under this Act has, by construction, already received notice of the class of risk; a second violation in the same class after that notice is rarely *merely* negligent.

**I.5 The retention rebuild still has no offense behind it.** Breach of SEC. 12 retention is not a SEC. 5 prohibited act; exposure is the SEC. 10(a) civil penalty (strict, benefit-floored) plus general obstruction law once an investigation exists. The FDCA makes records failures prohibited acts outright (§ 331(e)); this Act does not, yet. Flagged to chunk 5 (§G) rather than drafted, because a new prohibited act must first take a preemption-tier rating (it would sit in chunk 2's tier 2, arguably tier 1 as applied to providers and deployers) and a First Amendment pass (a pure keep-and-produce duty, no publication), neither of which belongs in this chunk. Until then the hold's deterrent against the sophisticated concealer is § 1519's twenty federal years, which is not this Act's to promise.

**I.6 The valve's whole theory assumes someone polices it, and federally no one will.** *Pearson*'s per-count rule means the cap and the findings gate will never be federally enforced against a court that ignores them; state appellate review under Ill. art. I, § 11-class clauses is the only external check, and in states without such clauses the valve is self-enforcing text. That is the design bet stated plainly: (c)(3) is addressed to courts as a rule of law, not as a constitutional prediction — the same posture as SEC. 13(c)'s order mechanism — and its enforcement surface is appellate review of the stated findings, which exists only where the findings requirement survives conformity. The first draft claimed the valve "answers" READ FIRST item 4; the honest verb is "closes what drafting can close" — the outbreak-scale stress test under fifty state clauses is now a review of enacted-pattern text, which is the most a model act can hand the scholar.

---

## H. SOURCES

**State primary (retention):** legiscan.com CA SB 53 enrolled mirror (Bus. & Prof. Code § 22757.12(f) verbatim; § 22757.13; Labor Code §§ 1107 et seq. checked for retention: none) — leginfo.legislature.ca.gov robots-excluded, disclosed per house rule; ilga.gov / LegiScan IL SB 315 enrolled, 10400SB0315enr (§ 10(d)(3), § 10(g)(1), § 15(f)(3), § 25(c) verbatim); nysenate.gov A9449 (GBL § 1421(5)(B); word-search "retain"/"as long as"/"deployed" across the replacement article).

**Federal primary:** law.cornell.edu — 21 U.S.C. § 841(b)(1)(C), (b)(1)(E); 18 U.S.C. § 1365(a), (h)(3)–(4); 18 U.S.C. § 3584(a)–(b); 18 U.S.C. § 3663A(a), (c)(1); 21 U.S.C. § 333(a)(1)–(2); 21 U.S.C. § 331(e); 18 U.S.C. § 1519; 18 U.S.C. § 1520(a)(1), (b); ecfr.gov — 17 C.F.R. § 210.2-06.

**State sentencing structures:** ksrevisor.gov, K.S.A. 21-6819(b)(4) (verbatim); codes.ohio.gov, Ohio Rev. Code § 2929.14(C)(4) (chapeau verbatim; subclauses ⚠ paraphrased).

**Constitutions:** ilga.gov (Ill. Const. art. I, § 11, verbatim); oregonlegislature.gov (Or. Const. art. I, § 16, verbatim); Ind. art. 1, § 16 and W. Va. art. III, § 5 cited without pinned text ⚠.

**EU:** artificialintelligenceact.eu, AI Act art. 18(1) (chapeau verbatim).

**Cases:** supreme.justia.com — *O'Neil v. Vermont*, 144 U.S. 323 (1892) (figures and Field dissent quotes at 340); *Harmelin v. Michigan*, 501 U.S. 957, 1001 (1991) (Kennedy, J.); *Hutto v. Davis*, 454 U.S. 370 (1982); *Erlinger v. United States*, No. 23-370 (U.S. June 21, 2024) (also supremecourt.gov slip); law.justia.com — *Pearson v. Ramos*, 237 F.3d 881, 885–86 (7th Cir. 2001). Cited on established holdings without new quotation: *Apprendi*; *Alleyne*; *Almendarez-Torres*; *Ewing*; *Lockyer*; *Solem*; *Rummel*; *Burrage*, *Timbs*, *Bajakajian* as pinned at chunk 3.

**⚠ paraphrased, primary unreachable this sweep:** USSG § 5G1.2(d) (guidelines.ussc.gov JS-only); Model Penal Code § 7.06 (ALI); Ohio (C)(4)(a)–(c) subclauses; CO SB 26-189 three-year record-keeping (chunk 1, secondary).

**Standing watch:** dockets.justia.com and July 2026 press (*xAI v. Bonta* argued, undecided); govinfo.gov BILLSTATUS-119hr9925 and govtrack.us (FRONTIER referred, no further action); sweep for FTC finalisation and suits against the state family returned nothing new.


---

<a id="chunk-5"></a>
<!-- BEGIN audit/chunk5_commencement_and_records.md · sha256:87faee309cb6 · concatenated 19 Aug 2026, content verbatim -->

# CHUNK 5 — COMMENCEMENT REBUILT: IMMEDIATE DUTIES, THE INTERIM-STANDARDS BRIDGE, THE MODIFIABILITY FLOOR, AND THE SEC. 5(e) DECISION

Drafting date: 16 August 2026 (same day as chunks 2–4). Method as at chunks 2–4: primary-text pinning of every figure and clause the design rests on, then the design, then the drop-in text, then an adversarial pass in which the drop-ins were attacked rather than checked. As before, the attack found more than the check did; §E is the second draft and §I records what the first draft got wrong.

Verbatim quotation is used wherever the exact words are load-bearing. Anything not retrieved from primary text is marked ⚠ and paraphrased, never quoted. Source-access disclosures for this sweep (§H): guidelines.ussc.gov (the current-manual application) remains JS-only and the per-section 2025 page 404s, but the Commission's own static archive pages serve §5G1.2 in full HTML — the pin at §B.1 is first-party USSC text, with a residual cite-check item on 2025-manual identity; the ALI's Model Penal Code remains paywalled — § 7.06 is quoted from the criminallawweb.net full-text reproduction under the mirror rule applied to LegiScan since chunk 3, upgraded from ⚠-paraphrase to mirror-pinned, not to primary; leginfo.legislature.ca.gov remains robots-excluded — SB 53 text is from the LegiScan enrolled mirror, per house rule.

This chunk: records the commencement defect as a correction to v3.2 (§A); closes the two carried ⚠s from chunk 4 and one incidental ⚠ from chunk 1 (§B); pins the anchors (§C); sets out the design — the three-layer commencement, the interim-standards bridge, the modifiability-evaluation compute floor, and the SEC. 5(e) records-offense decision run through chunk 2's framework before any words were drafted (§D); supplies the drop-in text with conforming amendments, including the regulations conforms directed by chunks 3–4 (§E); supplies drafting notes n.24–n.26 and the conforms to n.21 and READ FIRST (§F); and states where the architecture is thin (§I). It closes READ FIRST item 6 to the extent drafting can close a question assigned to an evaluations researcher — the researcher now reviews a bracketed default rather than inventing a number — and it executes the chunk 4 §G decision instruction: the § 331(e) lineage question took its preemption-tier rating and its constitutional passes before it took drafting.

What this chunk deliberately does not do: the SEC. 9(a) recast of the two characterisation-shaped triggers (chunk 2 §E.3(d)) is carried again, because it must be drafted jointly with the regulations' evaluation Part and the threshold must come from the Agency; and the regulations Part 2 version re-pin remains READ FIRST item 1. Both at §G.

---

## A. CORRECTIONS TO EARLIER MATERIAL

**A.1 — v3.2's commencement architecture contradicts itself, and the contradiction conceals a pocket veto.** Two clocks govern and they disagree. SEC. 3(c): "No criminal duty arises under SEC. 2 or SEC. 5(a) until the applicable standards have been promulgated and a compliance period of [90] days has run" — a rule for two provisions, implying the rest of the Act operates from ordinary effectiveness. SEC. 12: "Effective date conditioned on standards promulgation under SEC. 3" — a rule for the whole Act, under which nothing operates until the Agency acts. On the first reading, SEC. 5(c), 5(d), SEC. 9, and SEC. 11 are live on day one; on the second, no provision is live at all until promulgation. A defendant would take the second reading and be reasonable; the rule of lenity would help him to it. And the second reading is a structural defect graver than the ambiguity: it hands the designated Agency — a body this Act does not create and cannot compel — a pocket veto over the entire statute, including over the reporting, veracity, and whistleblower provisions that need no standards to have content. The WHY page promises "finished text, lying around," ready for a post-incident window measured in weeks; a statute that cannot punish a lie told to the State about the incident that opened the window, because a rulemaking has not finished, is not finished text. Cured at §E.1 and §E.4: the Act takes effect on its own date; duties commence in three layers; the Agency's inaction can delay only what genuinely depends on the Agency.

**A.2 — Supersession record.** v3.2 SEC. 3(c) is replaced in full by §E.1; the first clause of v3.2 SEC. 12 ("Effective date conditioned on standards promulgation under SEC. 3") is struck and replaced by §E.4. Chunk 2's collision-map row for SEC. 3(c) ("1, predicate — the fair-notice provision; never severable while any offense stands") carries to the expanded 3(c) unchanged, and chunk 2's SEC. 13(b)(5) sentence — "SEC. 3(a) and SEC. 3(c) continue in effect to supply the content of, and the commencement condition for, any surviving offense under SEC. 5" — now does double duty: the armour drafted for the standards regime turns out to have been pre-built for the interim bridge, since the bridge lives inside 3(c). No amendment to SEC. 13(b)(1) or (b)(5) is needed on this point.

---

## B. CARRIED ⚠s, CLOSED

**B.1 USSG § 5G1.2(d) — pinned from first-party text; chunk 4's paraphrase was accurate.** The Commission's own site serves the section in static HTML in its manual archive. § 5G1.2(d), verbatim:

> "If the sentence imposed on the count carrying the highest statutory maximum is less than the total punishment, then the sentence imposed on one or more of the other counts shall run consecutively, but only to the extent necessary to produce a combined sentence equal to the total punishment."

And its companion (c): "If the sentence imposed on the count carrying the highest statutory maximum is adequate to achieve the total punishment, then the sentences on all counts shall run concurrently," except as otherwise required by law. Currency: Amendment 767 (effective 1 November 2012) is the most recent amendment to the guideline's text located, and it amended subsection (b) only — the Commission's amendment page confirms subsection (d) untouched; the (d) sentence is identical across the Commission's archived 2001, 2009, and 2012 editions, and post-2012 circuit opinions quote the same words. Residual for the cite-check: confirm the 2025-manual page identity (the current-manual per-section page is JS-only/404 this sweep). The ⚠ on n.21's § 5G1.2(d) sentence is struck at §F.4; the paraphrase it protected — stacking only to the point the total punishment requires — is the pinned text's own arithmetic.

**B.2 Model Penal Code § 7.06 — mirror-pinned; chunk 4's "aggregate-cap architecture" characterisation was accurate, and the pinned text sharpens it.** Title: "Multiple Sentences; Concurrent and Consecutive Terms." Subsection (1) chapeau, verbatim from the full-text reproduction:

> "When multiple sentences of imprisonment are imposed on a defendant for more than one crime, including a crime for which a previous suspended sentence or sentence of probation has been revoked, such multiple sentences shall run concurrently or consecutively as the Court determines at the time of sentence, except that:"

Two cap clauses within (1): "the aggregate of consecutive definite terms shall not exceed one year"; and, at (1)(c), "the aggregate of consecutive indefinite terms shall not exceed in minimum or maximum length the longest extended term authorized for the highest grade and degree of crime for which any of the sentences was imposed." Section structure: (1)(a)–(d); (2)(a)–(c); (3); (4); (5)(a)–(c); (6)(a)–(d); (7)(a)–(c). Two consequences for the chunk 4 architecture. First, n.21's claim that the Kansas double rule sits "in the Model Penal Code's aggregate-cap tradition" is confirmed — the 1962 Code caps consecutive aggregates in text. Second, the pinned formula is *stricter* than Kansas's: the MPC caps the aggregate at the longest extended term authorised for the single gravest offense, no doubling; Kansas caps at twice the base sentence; the Act's [forty]-year cap (twice the twenty-year serious-injury ceiling) therefore adopts the more permissive of the two enacted formulas, and sits between the MPC and unlimited stacking. n.21 needs no correction, and the comparison is now available to whoever defends the bracket. Provenance stated plainly: the ALI's own print remains unreached; the quotation source is a full-text scholarly reproduction, the same mirror posture as LegiScan for California, and the cite-check should verify against an ALI print when one is reachable.

**B.3 Incidental closure — chunk 1's CA incident-clock ⚠.** Chunk 1 §A carried "15 days to Cal OES (⚠ confirm 24h imminent-risk channel in chaptered text)." Confirmed from the enrolled mirror this sweep: Bus. & Prof. Code § 22757.13 requires reporting within 15 days of discovery, and within 24 hours to appropriate authorities where the incident poses imminent risk of death or serious injury. The chunk 1 row is now fully closed.

**B.4 The chunk 4 §G decision item — routed as instructed.** "Consider whether a retention/records offense belongs in SEC. 5 itself, on the lineage of 21 U.S.C. § 331(e) … a new prohibited act needs a chunk 2 collision-map rating before it needs words." The rating and the constitutional passes are at §D.5; the words they authorised are at §E.3.

---

## C. THE ANCHOR TABLE — EVERY FIGURE PINNED

Sentencing anchors (closing chunk 4's ⚠s):

| Anchor | Provision | Pinned content |
|---|---|---|
| Structured stacking, now pinned | USSG § 5G1.2(c)–(d) | (c): concurrent where the highest-maximum count "is adequate to achieve the total punishment"; (d): consecutive "only to the extent necessary to produce a combined sentence equal to the total punishment" (§B.1 in full; ussc.gov archive HTML; Amendment 767 (eff. 1 Nov 2012) amended (b) only) |
| Model-law lineage, now mirror-pinned | MPC § 7.06(1), (1)(c) | concurrent/consecutive at the court's determination, "except that" definite-term aggregates cap at one year and indefinite-term aggregates cap "in minimum or maximum length" at "the longest extended term authorized for the highest grade and degree of crime for which any of the sentences was imposed" (§B.2; criminallawweb.net reproduction; ALI print unreached) |

Interim-standards anchors (the three pinned frameworks):

| Anchor | Provision | Pinned content |
|---|---|---|
| CA framework duty | Cal. Bus. & Prof. Code § 22757.12 (ch. 138, Stats. 2025) | "A large frontier developer shall write, implement, comply with, and conspicuously publish on its internet website a frontier AI framework…"; (c) transparency reports before or concurrent with deploying new or substantially modified frontier models; (d) catastrophic-risk-assessment summaries to the Office of Emergency Services "every three months or pursuant to another reasonable schedule"; (f) five-year redaction shadow (chunk 4 B.1) |
| CA incident clock | § 22757.13 | 15 days from discovery; 24 hours where imminent risk of death or serious injury (§B.3) — *not* adopted into the interim standards; SEC. 9 governs |
| NY framework duty | N.Y. Gen. Bus. Law § 1421 (art. 44-B as replaced by ch. 96, L. 2026) | "A LARGE FRONTIER DEVELOPER SHALL WRITE, IMPLEMENT, COMPLY WITH, AND CLEARLY AND CONSPICUOUSLY PUBLISH ON ITS INTERNET WEBSITE A FRONTIER AI FRAMEWORK" (bill-print capitals); article structure: 1420 definitions; 1421 transparency; 1422 incident reporting; 1423 equity-loss exclusion; 1424 cumulative duties; 1425 scope; 1426 exceptions (academic institutions, named consortiums); 1427 violations; 1428 disclosure and assessments; 1429 rulemaking |
| IL framework duty | Artificial Intelligence Safety Measures Act § 10, P.A. 104-0538 | (a) "write, implement, comply with, and clearly and conspicuously publish on its website a frontier AI framework," beginning 1 January 2028, addressing ten enumerated areas (catastrophic-risk assessment and mitigation, cybersecurity, governance, third-party evaluations, internal-use risks among them); (b) annual review, material modifications published with justification within 30 days; (c) transparency reports at deployment; (d) annual independent third-party audit; (e) internal risk assessments to the agency quarterly or per a communicated schedule; (f) false-statement prohibition; (g) redaction rules |
| The family's one sentence | all three | "write, implement, comply with, and … publish … a frontier AI framework" — the same operative sentence, three enactments (CA → NY → IL), the propagation pattern already documented for penalties (chunk 3 §C) and retention (chunk 4 §B) |
| Effective-date stagger | IL § 99; NY ch. 96; CA ch. 138 | IL: Act 1 Jan 2027, framework and audit duties 1 Jan 2028; NY regime 1 Jan 2027; CA operative 1 Jan 2026 — the interim standards adopt the *texts*, expressly not the staggers (§E.1, reading rule (A)) |

Records-offense anchors:

| Anchor | Provision | Pinned content |
|---|---|---|
| The lineage | 21 U.S.C. § 331(e) | prohibits "the failure to establish or maintain any record, or make any report, required under" enumerated sections, and "the refusal to permit access to or verification or copying of any such required record" (pinned chunk 4 §C) |
| The recidivist/penalty frame | 21 U.S.C. § 333(a)(1) | strict-liability misdemeanour tier for § 331 prohibited acts (pinned chunk 4 §C) |
| Required-records doctrine | *Grosso v. United States*, 390 U.S. 62, 67–68 (1968) | the three premises, verbatim: "first, the purposes of the United States' inquiry must be essentially regulatory; second, information is to be obtained by requiring the preservation of records of a kind which the regulated party has customarily kept, and third, the records themselves must have assumed 'public aspects' which render them at least analogous to public documents." |
| Doctrine's source and reach | *Shapiro v. United States*, 335 U.S. 1 (1948); *Baltimore City Dept. of Social Servs. v. Bouknight*, 493 U.S. 549 (1990) | cited on established holdings without new quotation: records required by a valid regulatory scheme fall outside the Fifth Amendment privilege; the principle extends to production compelled under a regulatory regime |
| Compelled-conduct line | *Rumsfeld v. FAIR*, 547 U.S. 47 (2006); *Zauderer*/*NIFLA* line | as pinned at chunk 2 n.16 — record-keeping is conduct regulation; the compelled-speech exposure chunk 2 mapped attaches to characterisation and publication, neither of which SEC. 5(e) requires |
| Preemption texts | FRONTIER §9(a)–(d); GAAIA §121; H.R. 5388 §§6–7 | as pinned verbatim at chunk 2 §C; applied at §D.5 without re-quotation |
| Internal | v3.2 SEC. 3(c); v3.2 SEC. 12 first clause; SEC. 12 as rebuilt (chunk 4 §E.3); regs Parts 2, 3, 5.5, 8, 10.1 | the two-clock contradiction (§A.1); the records list 5(e) enforces: version identifiers, compute records, evaluation results, tool and permission manifests, change histories, compensation records; the litigation hold |

---

## D. THE DESIGN

**D.1 The defect, stated once.** v3.2's structure is: no standards, no statute. The Agency it waits for is bracketed — "[designated state agency, board, or commission]" — an existing body with existing priorities, and the Act gives it no deadline, no default, and no consequence for silence. Every duty in the Act, including the three that are self-defining — report the incident, tell the State the truth, keep the records — waits on a rulemaking the Act cannot compel. The family the Act cites does not make this mistake: California's duties operated 94 days after signature; New York and Illinois staged theirs by statutory date, not by agency grace. And the Act's own theory of itself — text drafted *before* the incident so it can move in the weeks after — is exactly the theory a promulgation condition defeats: the post-incident legislature adopts the Act, and the Act then sleeps through the window it was drafted for. The fix has three layers, each with a different relationship to the Agency, and the design rule is: **nothing waits on the Agency except what only the Agency can supply.**

**D.2 The three layers.** *Layer one — the evidence layer, immediate.* SEC. 5(c) (failure to report), SEC. 5(d) (false statement), new SEC. 5(e) (records), SEC. 9, and the SEC. 12 records duties operate from the effective date. None depends on a standard: SEC. 9(a) defines the reportable events in text; SEC. 5(d) requires no rule to give "false" content; SEC. 12 enumerates the records in text. This layer is the Act's sensory system — it is what makes the State *learn* of the violation years before any validation regime matures, and it is the layer whose absence in 1937 the WHY page narrates. *Layer two — the substantive layer, provisionally commenced.* SEC. 2's duty and SEC. 5(a)'s offense commence [180] days after the effective date, on the basis of provisional validation: a documented conformity assessment against interim standards the Legislature itself adopts in the statute — the pinned CA/NY/IL framework duties (§D.3). SEC. 8 certification commences with them, certifying against the same interim standards. *Layer three — the Agency layer.* Promulgation plus the [90]-day compliance period switches SEC. 5(a) to the SEC. 3(b) validation modes and, alone in the Act, commences SEC. 5(b) — the one offense whose element ("the authorization, privilege, monitoring, and enforcement controls prescribed under SEC. 3") only prescription can supply (§D.6). The Agency's inaction now delays the Agency's refinements; it no longer delays the statute.

**D.3 The interim standards — why these, why static, and what the reading rules do.** Chunk 1 §E.9 anticipated this bridge: "chunk 5's provisional-validation bridge can now name the CA/NY/IL frameworks as interim benchmarks by citation." The three statutes share one operative sentence — write, implement, comply with, and publish a frontier AI framework — enacted three times in thirteen months, in the three states where frontier developers actually sit, and described publicly by the largest frontier developer as a de facto national framework (⚠ chunk 1's politics row, press-sourced). Adopting them as the interim measure buys four things at once. *Determinacy*: a criminal element keyed to enumerated sections of enacted, freely available public law, pinned to a date — *Connally* and *Kolender* (chunk 2 §E.4) are answered by citation, not by hope. *Non-delegation*: the Legislature adopts the texts itself, in the statute, as they exist on the pin date; no future amendment by California, Albany, or Springfield has any effect here. That is not merely *Sunshine Anthracite* compliance (Agency-supervised adoption); it is the stronger position — legislative self-adoption with no delegate at all — and it respects the state constitutions that forbid incorporation of another sovereign's future enactments by reference, the same discipline chunk 2 applied to future Acts of Congress. A consequence worth stating: if a federal court enjoins or a Congress preempts SB 53 itself, the pinned texts remain this State's own enacted law — incorporation copies words, not fate. *The photocopy effect*: every frontier developer already builds these artifacts for California, New York, and Illinois; reading rule (E) credits documentation prepared for the enacting jurisdictions as conformity here, so day-one compliance for the entities that matter is a transmission, not a project — which is SEC. 0(a)(6)'s burden finding made concrete. *Family parity*: the Act's interim severity is the enacted family's severity; "invented standards" dies on contact with three session laws.

The reading rules (§E.1, paragraph (4)) do the conversion from transparency statute to validation measure, and each strips a feature this Act must not import. (A) disapplies the \$500,000,000 revenue screens, the enacting jurisdictions' exemptions, and their effective-date staggers — this Act's trigger is the covered system, not the balance sheet (chunk 1 §E.2's deliberate divergence), and a benchmark that slept until 2028 because Illinois staged its own would rebuild the pocket veto out of borrowed parts. (B) converts publication duties into transmission to the Agency — publication satisfies, but is not required — preserving intact the *NIFLA* architecture chunk 2 built (statements to a regulator, not conscription into public debate) instead of re-importing the compelled-publication exposure through the side door. (C) disapplies Illinois's third-party-audit mode: during the interim the mode is internal documentation, which is chunk 2 §I.2's own instruction (internal attestation sits outside FRONTIER CSA(2) altogether) applied to the bridge. (D) leaves reporting, penalties, enforcement, fees, and whistleblowers to this Act's own SEC. 9, 10, and 11 — two reporting regimes with different clocks (California's 15 days against SEC. 9's 72 hours) would let the laxer one impeach the stricter. What the guard sentence in paragraph (5) preserves: SEC. 6(a)'s rule that "an entity's own framework is evidence of neither." The family's central duty is comply-with-your-own-framework; unguarded, the bridge would make the defendant's own document the measure of his care. The reconciliation is that conformity operates only as the statute provides — documented, transmitted, and credited *as to the matters conformed* — while the framework standing alone proves nothing in either direction.

Preemption posture of the bridge, stated against chunk 2's map rather than around it. The provisional-validation duty inherits SEC. 5(a)'s existing split: as applied to deployment and material expansion by a provider or deployer, tier 1 (GAAIA (c)(2) saves the regulated act; the obligation is not on a developer within FRONTIER §9(b)); as applied to release by a developer, tier 3, as before. The transmission layer adds one exposure the map should name: a conformity assessment transmitted to the Agency is disclosure-shaped (FRONTIER CSA(1)(A)–(B)) as applied to a person in developer capacity, and a filing required in connection with *release* touches CSA(2)(C)'s named list ("registration … as a condition of, or in connection with, the … release"), while the same filing conditioned on *deployment* stands on (2)(C)'s omission of deployment (chunk 2 §I.2). The degradation path is already built: a SEC. 13(c)(2)(A) order suspends the developer-capacity transmission duty and preserves everything else; (c)(2)(C) preserves the records that would have supported it; and new SEC. 5(e) gives the preserved records layer its offense (§D.5). Two further facts blunt the exposure. The bridge is self-extinguishing — it lapses by its own terms when the Agency acts, so a facial challenge races a mooting event. And the interim standards *are* the enacted law of three states — a court asked to hold that a state may not even provisionally measure due care by the very duties California, New York, and Illinois currently enforce is being asked to preempt the family, not just the bridge, which is the posture the whole armour was built to force.

**D.4 The modifiability floor.** SEC. 2 (as amended at chunk 2 §E.2) places on the releasing provider "pre-release evaluation — including evaluation of the model as it can be modified, such as by removal of safeguards or fine-tuning within a rule-specified compute budget." Until a rule exists, the budget is undefined, and the clause has two failure modes: as a criminal duty it is indeterminate (what modification envelope must the evaluation cover?), and as commencement architecture it is another Agency dependency inside a duty layer two brings live at day [180]. READ FIRST item 6 assigns the number to an evaluations researcher; the researcher was asked to *invent* it, and inventors do not arrive on legislative schedules. The fix is the same move chunk 4 made for the proportionality valve: draft the structure, bracket the figure, and convert the open item from design to review. §E.2 adds one sentence: the budget is specified by rule; it shall not be less than the greater of [one] percent of the covered model's training and lineage compute under SEC. 1(b)(1) or [10^24] integer or floating-point operations; until a rule first takes effect, the budget is that minimum. The two limbs are structural, not scientific, and both derive from the Act's own numbers: at the 10^26 covered-model threshold the limbs coincide (one percent of 10^26 is 10^24), the percentage limb scales the envelope with the model above the threshold, and the absolute limb keeps the floor meaningful for models the Agency designates as frontier-equivalent *below* the compute line under SEC. 3 — a percentage of a small number being the kind of floor that isn't. The floor binds the Agency upward only — the rule may demand a wider envelope, never a narrower one — and the interim default is the floor itself, so the releasing provider's duty is determinate from the day it first attaches. The bracket, not the chunk, carries the empirical question; §I.3 states the residue honestly.

**D.5 The SEC. 5(e) decision — the rating before the words.** Chunk 4 §I.5 flagged the gap: SEC. 12's rebuilt retention has no offense behind it; breach is a SEC. 10(a) civil penalty (whose benefit floor measures nothing when the "benefit" of shredding is the harm-tier conviction avoided) plus whatever obstruction law an investigation later supports; "the hold's deterrent against the sophisticated concealer is § 1519's twenty federal years, which is not this Act's to promise." The FDCA's answer, on the books since 1938, is § 331(e): the records failure is itself a prohibited act. Per the chunk 4 instruction, the question takes chunk 2's collision-map rating first.

| Proposed provision | GAAIA §121 | FRONTIER §9 | Tier |
|---|---|---|---|
| SEC. 5(e) limb one — failure to establish, maintain, or preserve records required by SEC. 12 | not a rule "specifically regulating the development"; (c)(2) saves as applied to records of deployed-system operation; §121(e)-shadow as applied to records of pre-deployment evaluation | keeping is not reporting (CSA(3)) and not disclosure (CSA(1)); the duty falls on whoever holds the records, including a provider or deployer outside §9(b) entirely | **2** — chunk 2 lane 4, now with an offense attached |
| SEC. 5(e) limb two — refusal to permit access, verification, or copying on lawful demand of this State | as above | as applied to a person in developer capacity and evaluation results: arguably within CSA(1)(B) and the access clause of CSA(2)(C) — chunk 2 §I.3's caution, restated not resolved; reduced by the enforcement-process posture ((2)(C) addresses access "for purposes of" third-party assessment, not production to the sovereign in enforcement) | **2**; **3 as applied to a developer's pre-release evaluation records** |
| Both limbs under H.R. 5388 | — | — | §6(a)(2)(B) saves outright: the moratorium spares "any provision … to the extent that the violation of such provision carries a criminal penalty" — attaching the criminal penalty *improves* the retention architecture's position under the only unconditional criminal savings text in the field |

The constitutional passes chunk 4 required. *First Amendment*: a keep-and-produce duty compels no statement to the public, no publication, and no adoption of any characterisation — the records are the entity's own operational artifacts (version identifiers, logs, manifests), and the duty is "plainly incidental to … regulation of conduct" (*FAIR*); the *X Corp. v. Bonta* defect (compelled contested labels) has no purchase on a manifest. The exposure chunk 2 mapped for SEC. 8 and SEC. 9 attaches to certifying and reporting, not to filing cabinets. *Fifth Amendment*: the serious pass. The offense criminalises non-keeping and non-production, and the records may incriminate; the answer is the required-records doctrine, whose premises Grosso states and this Act satisfies on its face: the scheme is "essentially regulatory" — the records attach to the lawful deployment of covered systems, not to conduct criminal in itself (contrast the gambling-tax registrations of *Marchetti* and *Grosso* itself); the records are "of a kind which the regulated party has customarily kept" — version control, compute accounting, evaluation logs, and permission manifests are the industry's own artifacts, which is the empirical premise of the regulations' entire Part 6; and the records bear "public aspects," being required in aid of a public welfare scheme on the *Shapiro* pattern, with production running to the sovereign under lawful process (*Bouknight* extending the principle to compelled production). Two honesty clauses ride with the pass: the doctrine is federal, and an adopting state's self-incrimination clause may be broader — a conforming-counsel flag (READ FIRST item 9), stated in n.26; and the limb-two demand power is drafted to *this State's* Agency, Attorney General, and courts only, the SEC. 5(d) narrowing logic applied at birth rather than by later amendment. *Mens rea*: nothing new is invented. The base offense takes SEC. 6(a)'s due-care floor (no custody without fault — the *Morissette* bargain holds); knowing destruction or refusal is a knowing violation of SEC. 5 and takes SEC. 6(b)(1); destruction to hide another violation was already "conceal[ment]" under 6(b)(1), and 5(e) merely gives the concealment a provable substrate. The litigation hold thereby completes its design: chunk 4 built the duty so that "concealment by destruction … becomes a retention violation provable from the absence in the filing cabinet"; 5(e) is the provision that makes the absence chargeable.

Ladder placement, and the decision. The offense enters at severance rank 2, beside the SEC. 12 duties it enforces — the conservative reading of chunk 4 §I.5's "tier 2, arguably tier 1"; the provider/deployer strength is an argument the Attorney General makes under SEC. 13(c), not a promotion the ladder should claim. The developer-capacity application to pre-release evaluation records goes to rank 3 with its capacity siblings, so the most exposed application severs first and alone. A preservation sentence keeps the offense and the duty independent in both directions: severing 5(e) leaves SEC. 12 enforced civilly, as now; suspending a reporting duty under 13(c)(2)(C) preserves the records *and their offense*. **Decision: the § 331(e)-style records offense enters SEC. 5, as subsection (e), in the two-limb form of its model, demand power confined to this State.** What stays out: no separate penalty tier (it rides SEC. 6/10 like every other prohibited act), no reporting limb (that is SEC. 5(c)'s), and no federal or sister-state demandants.

**D.6 What is deliberately not bridged: SEC. 5(b).** The offense's element is the absence of "the authorization, privilege, monitoring, and enforcement controls *prescribed under SEC. 3*," and prescription is the one thing the interim standards cannot honestly supply: the family's framework duties describe safeguards at the policy level; a criminal element needs controls specified in advance by a body other than the defendant (the SEC. 6(a) principle, scaled), and no enacted sister text prescribes system-level authorization controls with element-grade determinacy. The first draft tried to bridge 5(b) through the entity's own documented controls and collapsed in the attack — the defendant's own conformity file cannot be the content of the offense against him. So 5(b) commences at layer three, and the interim residue is covered honestly: a deployment with autonomous external access and no documented conformity fails 5(a) from day [180]; the breach itself is a critical safety incident SEC. 9 makes reportable from day one; and unauthorized access to third-party systems is already criminal everywhere under general computer-misuse law, which SEC. 13(c)(2)(D) is drafted to keep unclouded. §I.4 names the cost.

---

## E. DROP-IN TEXT FOR v3.3

House convention as at chunks 2–4: set out in full, no ellipsis; in amended sections, struck text is not reproduced and inserted text is **bold**; wholly new matter is set out clean where a subsection is replaced in full. Baselines: SEC. 2 as amended by chunk 2 §E.2; SEC. 12 as amended by chunk 2 §E.3(c) and chunk 4 §E.3; SEC. 13 as amended by chunk 3 §E.4.

### E.1 — SEC. 3(c), replaced in full

> (c) Commencement.
>
> (1) *Immediate operation.* This Act operates from its effective date. The offenses under SEC. 5(c), SEC. 5(d), and SEC. 5(e); the reporting duties of SEC. 9; the records duties of SEC. 12; and the provisions of SEC. 1, SEC. 4, SEC. 6, SEC. 7, SEC. 10, SEC. 11, SEC. 13, and the remainder of SEC. 12 arise and operate from the effective date, and do not depend upon the promulgation of any standard, the adoption of any rule, or any other act of the Agency. No duty arises under SEC. 2, and no offense lies under SEC. 5(a), before the provisional commencement of paragraph (2); no offense lies under SEC. 5(b) before commencement under paragraph (3). This paragraph governs time; SEC. 1(c) and SEC. 2 govern to whom, and by reason of what conduct, a duty attaches.
>
> (2) *Provisional commencement.* Beginning [180] days after the effective date, and until superseded under paragraph (3), the duties of SEC. 2 and the offense of SEC. 5(a) operate on the basis of provisional validation, and the certification duty of SEC. 8 operates from the same day, the applicable standards for its purposes being the interim standards of paragraph (4). Provisional validation of a covered system consists of a documented conformity assessment, prepared or adopted by an entity that develops, releases, provides, or deploys the covered system, that: (A) identifies the model version and deployment configuration, including the tools, memory, retrieval, credentials, and permissions attached; (B) documents the conformity of the covered system, and of each entity's practices concerning it, with the interim standards, or discloses identified nonconformity and the compensating measures taken; and (C) is retained as a record under SEC. 12 and transmitted to the Agency on or before the deployment, material expansion, or release to which it relates. Provisional validation attaches to the identified model version and deployment configuration; a system provisionally validated without tools is not validated as to any configuration granting external access or significant permissions.
>
> (3) *Standards commencement.* Upon the promulgation of standards under subsection (a) and the running of a compliance period of [90] days, validation in the mode specified under subsection (b) is the validation SEC. 5(a) requires for any deployment, material expansion, or release occurring thereafter, and provisional validation ceases to satisfy SEC. 5(a) except as to covered systems deployed before that day, for which the transition period of SEC. 12 runs from that day. The offense under SEC. 5(b) commences when the controls it presupposes have been prescribed under this section and the same compliance period has run. Conduct is judged by the standards applicable to it at its time; no conduct lawful when done becomes unlawful by a later commencement, and no provisional validation is invalidated retroactively. [The Agency shall propose initial standards under subsection (a) within [540] days of the effective date.]
>
> (4) *Interim standards.* The interim standards are the frontier artificial intelligence framework duties enacted at Section 22757.12 of the California Business and Professions Code (ch. 138, Stats. 2025), Section 1421 of the New York General Business Law (ch. 96, L. 2026), and Section 10 of the Illinois Artificial Intelligence Safety Measures Act (P.A. 104-0538), each as in effect on [1 August 2026], which are adopted for the purposes of this Act as they so exist and not as they may afterward be amended, repealed, suspended, or invalidated in the enacting jurisdiction. For those purposes: (A) the duties apply to every covered frontier model and covered system, and to each entity that develops, releases, provides, or deploys one, without regard to any revenue threshold, exemption, effective date, phase-in date, or territorial term of the enacting jurisdiction; (B) a duty to publish, or to transmit any document to an officer, agency, or the public of an enacting jurisdiction, is performed under this Act by transmission to the Agency, and publication is permitted but not required by this Act; (C) provisions respecting assessment or audit by a third party do not apply, and conformity may be documented internally, independent assessment being at the entity's election; (D) provisions respecting incident reporting, penalties, enforcement, fees, assessments, and whistleblowers are not adopted, those subjects being governed from the effective date by SEC. 9, SEC. 10, and SEC. 11 of this Act; and (E) conformity documented for the purposes of any of the three enactments in an enacting jurisdiction is conformity with the corresponding interim standard under this Act, to the extent of the matters documented. The Agency shall make the adopted texts publicly available without charge.
>
> (5) *Element and due care.* Absence of required validation is an element of the offense under SEC. 5(a); the validation required is the provisional validation of paragraph (2) or the validation of subsection (b), as applicable to the conduct at its time. Documented conformity with the standards applicable at the time — interim or promulgated — satisfies the duty of due care under SEC. 2 as to the matters conformed. An entity's own frontier artificial intelligence framework, written and followed as an interim standard requires, is an object of the conformity this paragraph credits; standing alone it remains evidence neither of due care nor of its absence, per SEC. 6(a).

### E.2 — SEC. 2, set out in full as further amended

> **SEC. 2. PUBLIC WELFARE DUTY.** No covered system may be deployed in or into this State, or materially expanded, unless each controlling person has exercised due care to ensure the system's compliance with the safety, authorization, monitoring, incident-reporting, and deployment standards applicable under SEC. 3. A duty under this Act arises upon, and by reason of, the deployment, material expansion, release, or continued operation of a covered system in or into this State, and not otherwise. Each duty under this Act attaches to the actor who controls the relevant risk: the developer as to model evaluation and weight security; the provider and deployer as to configuration, tools, permissions, and monitoring; the releasing provider as to pre-release evaluation — including evaluation of the model as it can be modified, such as by removal of safeguards or fine-tuning within a rule-specified compute budget — tamper-resistance assessment, and weight security up to the moment of release; each controlling person as to the exercise of the authority that person holds. **The compute budget within which modification of a model is to be evaluated shall be specified by rule and shall not be less than the greater of [one] percent of the covered model's training and lineage compute, as computed under SEC. 1(b)(1), or [10^24] integer or floating-point operations; until a rule first takes effect, the budget is that minimum.**

### E.3 — SEC. 5, amended

**(a) Conform the commencement reference.** In SEC. 5(a), strike "after commencement under SEC. 3(c)" and insert "**after the applicable commencement under SEC. 3(c)**".

**(b) New subsection (e):**

> **(e) Failure to establish, maintain, or preserve any record required by SEC. 12 or by rule under SEC. 3, or refusal to permit, upon the lawful demand of the Agency or the Attorney General or upon order of a court of this State, access to or verification or copying of any such record.**

### E.4 — SEC. 12, first clause, amended

Set out in full as amended (the remainder of SEC. 12, as rebuilt at chunk 2 §E.3(c) and chunk 4 §E.3, does not move):

> **This Act takes effect [90] days after enactment; duties and offenses commence as provided by SEC. 3(c);** [180-day] transition for **covered systems deployed before the commencement applicable to them under SEC. 3(c), running from that commencement**; no retroactive liability;

### E.5 — SEC. 13, conforming amendments

**(a)** In SEC. 13(b)(2), strike "SEC. 11; the remaining provisions of SEC. 12" and insert "**SEC. 11; the remaining provisions of SEC. 12; the offense under SEC. 5(e), except as provided in paragraph (3)**".

**(b)** In SEC. 13(b)(3), after "SEC. 5(a) as applied to a release;" insert "**SEC. 5(e) as applied to records of pre-release evaluation held by a person in that person's capacity as a developer;**".

**(c)** Add to SEC. 13(b)(5):

> **The offense under SEC. 5(e) and the duties of SEC. 12 sever independently of one another: severance or suspension of the offense leaves the duties enforceable under SEC. 10(a), and severance of any reporting or certification duty does not sever the records duties or the offense that enforces them.**

**(d)** In SEC. 13(c)(2)(C), after "and those records shall be produced upon lawful process" insert "**; an order preserving the obligation preserves the offense under SEC. 5(e) with respect to it**".

### E.6 — Regulations, conforming amendments (directed by chunks 3–4, executed here)

**(a) Part 5.5** (chunk 4 §E.4(c)): strike "fixes notice for purposes of SEC. 6(b)" and insert "**fixes notice for purposes of SEC. 6(b)(1)**".

**(b) Part 10.1** (chunk 4 §E.4(d)): strike "[7] years" and insert "**for the periods provided by SEC. 12 of the Act**".

**(c) Part 8.1** (chunk 3 §G): strike "up to \$[X]/day" and insert "**up to \$[1,000,000] per violation per day or, after a prior final adjudication of a violation by the same person, up to \$[3,000,000] per violation per day, per SEC. 10(a)**".

**(d) Part 8.4** (chunk 3 §G): strike "Penalties collected fund the SEC. 11 award fund." and insert "**Monetary recoveries are deposited and applied per SEC. 10(f); awards under SEC. 11 are paid from the fund it establishes.**"

**(e) Part 3 — what is deliberately not done.** The first draft added an interim clause to Part 3.1 reading the Part 2 standards as the interim standards before commencement. It was incoherent and is discarded: the regulations are the Agency's instrument and speak only from their own adoption, by which time commencement under SEC. 3(c)(3) is running or imminent; a rule cannot govern the period before its adopter has acted. The interim regime lives entirely in SEC. 3(c) of the Act, which is where a duty that must not wait on the Agency belongs.

---

## F. NEW DRAFTING NOTES AND CONFORMS

**n.24 ON SEC. 3(c) (COMMENCEMENT AND THE INTERIM STANDARDS).** v3.2 conditioned the whole Act on its own agency: SEC. 12 made the effective date wait on promulgation while SEC. 3(c) implied the contrary for everything but SEC. 2 and 5(a), and between the two readings a defendant would choose, reasonably, the one under which no duty ever arose. The rebuild states the principle the family already practices — California's duties ran 94 days from signature; New York and Illinois commenced by statutory date — as three layers: the evidence layer (report, speak truly to the State, keep the records: SEC. 5(c)–(e), SEC. 9, SEC. 12) operates from the effective date, because its content is stated in text and depends on no rule; the substantive layer (SEC. 2, SEC. 5(a), SEC. 8) commences provisionally at day [180] against interim standards; the Agency layer (the SEC. 3(b) modes, and SEC. 5(b), whose element only prescription can supply) commences with promulgation plus [90] days. The interim standards are the frontier-framework duties of Cal. Bus. & Prof. Code § 22757.12, N.Y. Gen. Bus. Law § 1421, and § 10 of the Illinois Artificial Intelligence Safety Measures Act (P.A. 104-0538) — one operative sentence enacted three times ("write, implement, comply with, and … publish … a frontier AI framework") — adopted by the Legislature itself, statically, as of a named date: no delegate, no dynamic incorporation, no effect here of any later amendment or invalidation there, the discipline of n.3 and of *Sunshine Anthracite Coal Co. v. Adkins*, 310 U.S. 381 (1940), exceeded rather than merely met, and the state constitutional bar on adopting another sovereign's future enactments respected. The reading rules of (c)(4) convert transparency law into a validation measure: thresholds, exemptions, and staggers disapplied (this Act's trigger is the covered system, not revenue — n.2's bargain does not ration by balance sheet); publication converted to transmission to the Agency (preserving the *NIFLA* posture built at n.16 — these are statements to a regulator, not conscription into public debate); third-party audit disapplied in favour of internal documentation (the validation mode FRONTIER CSA(2) cannot reach, per the analysis at n.13); reporting and enforcement left to this Act's own sections; and conformity documented for California, New York, or Illinois credited here to the extent of the matters documented — for the entities this Act principally addresses, first-day compliance is a transmission of artifacts the family already exacts. Paragraph (5) keeps SEC. 6(a)'s rule intact against the family's one hazard: the framework the interim standards require is an object of documented conformity, never a free-standing measure of the care its author owed. Fair notice runs prospectively at every joint (*Connally v. General Construction Co.*, 269 U.S. 385 (1926); *Kolender v. Lawson*, 461 U.S. 352 (1983); cf. *Bouie v. City of Columbia*, 378 U.S. 347 (1964), and the same one-way ratchets built into SEC. 13(c)–(d)): a [180]-day runway before the substantive layer, a [90]-day compliance period after promulgation, transition under SEC. 12 for systems already deployed, and a rule that conduct is judged by the standards applicable at its time. The bridge extinguishes itself when the Agency acts; what it forecloses while it lasts is the pocket veto — the statute no longer waits, for its criminal core, on the diligence of the body it regulates least.

**n.25 ON SEC. 2 (THE MODIFIABILITY FLOOR).** The releasing provider's duty to evaluate "the model as it can be modified" is bounded by a compute budget the Agency was to specify; until it did, the envelope was indeterminate — a defect in a criminal duty (*Connally*; *Kolender*) and, after the commencement rebuild, a gap in a duty that now attaches at day [180]. The floor supplies both the interim default and a bound on the rule: not less than the greater of [one] percent of the model's training and lineage compute (SEC. 1(b)(1)) or [10^24] integer or floating-point operations. Both limbs are derived from the Act's own architecture rather than from evaluations science: at the 10^26 covered-model line the limbs coincide (one percent of 10^26 is 10^24); above it the percentage limb scales the modification envelope with the model; and for models designated frontier-equivalent below the line under SEC. 3, the absolute limb keeps the floor from vanishing with the model's size. The Agency may widen the envelope by rule and may never narrow it below the floor. The bracketed figures are a default awaiting the evaluations researcher READ FIRST item 6 names — the item narrows from designing a budget to reviewing one — and the direction of any error is asymmetric by construction: a floor set too low under-demands until the Agency acts; a floor set too high binds the Agency until the Legislature amends, which is why the figures are brackets and not convictions. What the floor is not: it is not a safe harbour above which modification is presumed safe, and it is not the evaluator's spending cap — it is the least envelope of adversarial modification (safeguard removal, fine-tuning, and their kin) that a pre-release evaluation must cover to discharge the duty.

**n.26 ON SEC. 5(e) (RECORDS AS PROHIBITED ACT).** The lineage is the FDCA's, quoted at the chunk 4 anchor table: 21 U.S.C. § 331(e) prohibits "the failure to establish or maintain any record, or make any report, required under" the named sections and "the refusal to permit access to or verification or copying of any such required record"; this Act adopts the two-limb form, keys it to the records SEC. 12 enumerates in text, and confines the demand power to this State's Agency, Attorney General, and courts — the SEC. 5(d) narrowing (n.20) applied at birth. The offense completes the retention rebuild of n.23: the litigation hold converted concealment-by-destruction from an obstruction case into a retention violation "provable from the absence in the filing cabinet," and 5(e) is what makes the absence chargeable — without it, the deterrent against the sophisticated concealer was a civil penalty whose benefit floor cannot price an avoided homicide count, plus § 1519's federal twenty years, which are not this Act's to promise. Mens rea is inherited, not invented: the base offense carries SEC. 6(a)'s due-care floor (the *Morissette* bargain holds — strict liability convicts, only fault imprisons); knowing destruction or refusal is a knowing violation of SEC. 5 under 6(b)(1), whose "conceals" prong the new subsection gives a provable substrate. Preemption: the offense occupies chunk 2's fourth lane (record creation and retention without a reporting duty) — keeping is not reporting (FRONTIER CSA(3)) and not disclosure (CSA(1)); the duty binds whoever holds the records, including providers and deployers outside §9(b) altogether; under H.R. 5388 §6(a)(2)(B) the criminal penalty is itself the savings; and the one live shadow — production of a developer's evaluation results, arguably within CSA(1)(B) and CSA(2)(C)'s access clause (chunk 2 §I.3) — is carried in the severance ladder, where the developer-capacity application to pre-release evaluation records severs first and alone (SEC. 13(b)(3)), the offense generally sits at rank 2 beside the duties it enforces, and offense and duty sever independently in both directions (SEC. 13(b)(5)). Compelled-speech doctrine does not reach a filing cabinet: the records are the entity's own operational artifacts, no publication or characterisation is required, and the duty is incidental to conduct regulation (*Rumsfeld v. FAIR*, 547 U.S. 47 (2006)). The Fifth Amendment answer is the required-records doctrine, satisfied on the face of the scheme per *Grosso v. United States*, 390 U.S. 62, 68 (1968): the inquiry is "essentially regulatory" (the records attach to lawful deployment, not to conduct criminal in itself — the *Marchetti*/*Grosso* line marks the boundary this Act stays inside); the records are "of a kind which the regulated party has customarily kept" (version control, compute accounting, evaluation logs, and permission manifests are the industry's own artifacts — the premise of regs Part 6); and they bear "public aspects … at least analogous to public documents" (*Shapiro v. United States*, 335 U.S. 1 (1948); *Baltimore City Dept. of Social Servs. v. Bouknight*, 493 U.S. 549 (1990), on compelled production within a regulatory regime). One boundary is stated rather than assumed: the doctrine is federal; an adopting state's own self-incrimination clause may run broader, and that check belongs to the conforming counsel of READ FIRST item 9.

**F.4 — Conforms to existing notes and front matter.**

**(a) n.21 (chunk 4 §F):** strike "(§ 7.06 ⚠)" and insert "(§ 7.06(1)(c): consecutive indefinite terms capped 'in minimum or maximum length' at 'the longest extended term authorized for the highest grade and degree of crime' among the sentences — the stricter formula, no doubling)"; and strike "USSG § 5G1.2(d) ⚠ supplies" and insert "USSG § 5G1.2(d) supplies".

**(b) READ FIRST item 6:** strike "The rule-specified compute budget for modifiability evaluation (SEC. 2): an evaluations researcher." and insert "**The modifiability-evaluation compute floor (SEC. 2): the bracketed default — the greater of [one] percent of lineage compute or [10^24] operations — needs an evaluations researcher's review; the structure no longer waits on one.**"

**(c) READ FIRST, add to item 9's sentence or as a new clause at the drafter's election:** the interim-standards pin date in SEC. 3(c)(4) ("[1 August 2026]") is set by the adopting legislature's counsel to a date certain preceding introduction; it must never be drafted as a moving date.

**(d) n.6 (v3.2):** no conform needed — its burden analysis is unaffected; SEC. 5(e) takes its mental elements entirely from SEC. 6 as already glossed.

---

## G. CARRIED QUESTIONS

**For chunk 6 / v3.3 assembly:** the SEC. 9(a) recast of the two characterisation-shaped triggers (chunk 2 §E.3(d)) — still open, to be drafted jointly with the regulations' evaluation Part, with thresholds sourced from the Agency, not the reporter; the regulations Part 2 version re-pin (READ FIRST item 1) and the watch-list review; assembly must apply, in order, chunk 2 §§E.0–E.4 as amended by chunk 3 §E.4, chunk 3 §§E.1–E.5, chunk 4 §§E.1–E.4, and this chunk's §§E.1–E.6, and strike v3.2 n.10's superseded sentence (chunk 4 §E.4(f)) and n.19's superseded passage (chunk 4 §E.4(e)).

**For the cite-check:** confirm § 5G1.2(d) against the 2025 Guidelines Manual print (B.1 residual; archive-pinned this sweep); verify MPC § 7.06 against an ALI print (mirror-pinned this sweep; ⚠ retired to mirror status, not to primary); assign subsection letters for the CA framework, transparency-report, and OES-summary duties within § 22757.12 and the NY subdivisions within § 1421 (section-level citations are used in statutory text deliberately; the notes would benefit from letters); the Illinois Act's ILCS compilation cite (carried from chunk 3); and the standing chunk 4 items: Ohio § 2929.14(C)(4)(a)–(c) verbatim, Ind. Const. art. 1, § 16 and W. Va. Const. art. III, § 5 text, *Erlinger* U.S. Reports pagination, the NY FOIL exemption half of chunk 1's row, GBL § 1427's severity clause.

**Standing watch:** this chunk was drafted the same day as chunks 2–4; the chunk 4 sweep (16 August 2026 — *xAI v. Bonta* argued and undecided; FRONTIER referred without markup; GAAIA not introduced; FTC statement proposed only; Commerce list unpublished; no suit against SB 53, RAISE, or SB 315) stands and was not re-run. The first act of any later chunk is the re-sweep, and the *xAI v. Bonta* decision, when it lands, triggers the n.16 re-run and now also a check of the interim bridge's transmission layer (§I.2).

---

## I. WHERE THE ARCHITECTURE IS THIN

**I.1 The interim standards are transparency law doing validation work, and the grade of the bridge is the grade of the frameworks it credits.** The family's operative duty is write-and-follow-your-own-framework; the bridge disciplines it (documented conformity, credited only as to matters conformed, SEC. 6(a) preserved, nonconformity disclosable with compensating measures) but cannot transubstantiate it: an entity with a thin framework, followed thinly and documented fully, has a colorable provisional validation. The honest statement is that layer two buys determinacy and family parity, not rigor — rigor arrives with the Agency's standards, which is why the bridge self-extinguishes and why the [540]-day proposal clause, though unenforceable, is in the text. The alternative — no bridge — was v3.2, where the same entity had no duty at all.

**I.2 The transmission layer is the bridge's preemption surface.** A conformity assessment filed with the Agency is disclosure-shaped under FRONTIER CSA(1)(A)–(B) as applied to developers, and filing "in connection with … release" touches CSA(2)(C)'s named list, where deployment does not appear but release does. The degradation path is drafted (13(c)(2)(A) order; records preserved under (c)(2)(C); 5(e) enforcing the preserved layer), and the bridge's mortality is itself a litigation asset — but if FRONTIER is enacted as introduced, the interim scheme as applied to releasing developers is the first thing an order should reach, and n.24's claim for the bridge must then be made for its retained-records residue, not its filings.

**I.3 The floor's numbers are structural, and structure is not evidence.** One percent and 10^24 are derived from the Act's own trigger, which makes them defensible as *defaults* and nothing more; an evaluations researcher may report that meaningful safeguard-removal risk shows up at envelopes orders of magnitude below the floor (in which case the floor over-demands nothing — it is a floor on coverage, not a cap) or that a determined modifier's realistic envelope exceeds one percent (in which case the interim default under-covers until the Agency widens it). The bracket absorbs the first answer entirely and the second only by amendment or rule. READ FIRST item 6 is narrowed, not closed.

**I.4 SEC. 5(b) still waits on the Agency, and it is the strongest provision in the Act.** Chunk 2 rated 5(b) "the strongest provision in the Act"; this chunk leaves it dormant until prescription, because its element cannot be supplied by the defendant's own documents and no enacted text supplies it otherwise. The residue is real: during the interim, the operator of an autonomous-access system that breaches a third party answers under 5(a) (if unvalidated), SEC. 9 (the breach is reportable), general computer-misuse law, and — if death or serious injury results and the scienter is there — 6(b)(1); but the tailored operating offense itself is unavailable. A legislature that finds this intolerable can direct the designated Agency to adopt interim controls by emergency rule; this Act declines to pretend the family's frameworks already contain them.

**I.5 The required-records pass is federal, and the offense will live under fifty privileges.** *Grosso*'s premises are satisfied on the face of the scheme, but several state constitutions construe their self-incrimination clauses beyond the federal floor, and in such a state limb two's demand power may need a use-restriction or immunity valve the Act does not draft. Flagged to conforming counsel (READ FIRST item 9) rather than solved generically, because a national immunity clause would be wrong in the states that do not need it.

**I.6 The pin date is a hostage to fortune in both directions.** Pinned early, the interim standards miss the family's own corrections (a chapter amendment to SB 315 in 2027 would not flow through — by design, but the design has a cost); pinned as a moving date, the bridge collapses into dynamic incorporation and the constitutional discipline of n.24 with it. The instruction at F.4(c) — a date certain, set at introduction — is the only stable resolution, and it means the bridge ages from the day it is set. The Agency's promulgation is the cure for this too; every thin spot in this chunk is a different photograph of the same fact, that a statute can borrow a floor but must build its own ceiling.

---

## H. SOURCES

**Sentencing (first-party and mirror):** ussc.gov — §5G1.2 full text at the 2012 manual archive page (guidelines/2015-guidelines-manual/archive/2012-5g12; identical (d) text at the 2001 and 2009 archive pages), and the Amendment 767 page (guideline text change confined to subsection (b); effective 1 November 2012); guidelines.ussc.gov current-manual application JS-only and the 2025 per-section page 404 this sweep (disclosed; cite-check residual). criminallawweb.net, Model Penal Code full-text reproduction, § 7.06 (title, (1) chapeau, definite- and indefinite-term cap clauses, section structure); ALI print unreached (disclosed; mirror rule).

**State primary (interim standards):** legiscan.com CA SB 53 enrolled mirror — Bus. & Prof. Code § 22757.12 framework duty verbatim, (c)–(d) structure, § 22757.13 incident clocks incl. the 24-hour imminent channel (closing chunk 1's ⚠), § 22757.15 penalties (leginfo.legislature.ca.gov robots-excluded, disclosed per house rule); nysenate.gov A9449 — GBL § 1421 framework duty verbatim (bill-print capitals), article 44-B structure §§ 1420–1429; legiscan.com IL SB 315 enrolled — § 10(a)–(g) structure and framework duty verbatim, § 15, § 18, § 99 stagger (P.A. 104-0538).

**Federal primary:** 21 U.S.C. § 331(e), § 333(a)(1) — as pinned at chunk 4 §C (law.cornell.edu), applied without re-retrieval; FRONTIER H.R. 9925 SEC. 9, GAAIA §121, H.R. 5388 §§6–7 — as pinned at chunk 2 §C (govinfo.gov; trahan.house.gov), applied without re-retrieval.

**Cases:** supreme.justia.com — *Grosso v. United States*, 390 U.S. 62 (1968) (three premises verbatim at 68). Cited on established holdings without new quotation: *Shapiro v. United States*, 335 U.S. 1 (1948); *Marchetti v. United States*, 390 U.S. 39 (1968); *Baltimore City Dept. of Social Servs. v. Bouknight*, 493 U.S. 549 (1990); *Rumsfeld v. FAIR*, 547 U.S. 47 (2006); *Connally*, *Kolender*, *Bouie*, *Sunshine Anthracite*, as pinned at chunk 2.

**⚠ secondary, disclosed:** the "de facto national framework" attribution (chunk 1 politics row, press-sourced, carried with its original ⚠ status); MPC § 7.06 mirror status as above.

**Standing watch:** not re-run; chunk 4 §G's same-day sweep incorporated by reference.


---

<a id="chunk-6"></a>
<!-- BEGIN audit/chunk6_assembly.md · sha256:eef60290a14f · concatenated 19 Aug 2026, content verbatim -->

# CHUNK 6 — v3.3 ASSEMBLY RECORD

Assembly date: 16 August 2026 (same day as chunks 1–5). This chunk drafts nothing new except n.27
(directed by chunk 1 §§E.2 and E.10) and the companion's "Friendly proposals, answered" section
(directed by the field notes); everything else applies text the earlier chunks drafted and
adversarially passed. Deliverables: `model_act_v3_3.txt` (SEC. 0–13, introducible) and
`model_act_v3_3_companion.md` (READ FIRST ×11, WHY, friendly proposals, placement, notes n.1–n.27,
lineage, consolidated cite-check, standing watch), plus `CHANGELOG.md`, the README and regulations
conforms, and the banners below.

## A. What was applied, in order (per chunk 5 §G)

1. **Chunk 2 §§E.0–E.4** — SEC. 0; SEC. 1(c); SEC. 2 (superseded in turn by chunk 5 §E.2's full
   set-out); SEC. 8 addition; SEC. 9(c); SEC. 12 confidentiality; SEC. 13 — with E.4 as amended by
   chunk 3 §E.4. §E.3(d) NOT applied (the SEC. 9(a) recast — carried; see §D below). §E.5
   (placement) routed to the companion, per chunk 5 §G's assembly list, which excludes it from the
   statutory text.
2. **Chunk 3 §§E.1–E.5** — SEC. 7 (with chunk 4 §§E.4(b), (g) conforms); SEC. 10 baseline for
   (a), (b), (d), (e), (f); SEC. 11(a); SEC. 13(b) severance split; SEC. 5(d).
3. **Chunk 4 §§E.1–E.4** — SEC. 6(b) split; SEC. 10(c)(1)–(4); SEC. 12 retention and limitations;
   conforms (a)–(h), including the n.10 and n.19 supersessions by n.21 and the n.6 conform.
4. **Chunk 5 §§E.1–E.6** — SEC. 3(c) replaced; SEC. 2 final (modifiability floor); SEC. 5(a)
   conform and new SEC. 5(e); SEC. 12 first clause; SEC. 13 conforms (b)(2), (b)(3), (b)(5),
   (c)(2)(C); regulations conforms (a)–(d) applied to `model_regulations_v1_draft.md`; (e)
   deliberately not done, as chunk 5 directs (no interim clause in regs Part 3).
5. **Chunk 5 §F.4** — n.21 conforms (MPC § 7.06(1)(c) pinned text in; USSG ⚠ struck); READ FIRST
   item 6 replaced verbatim; the pin-date instruction added to item 9; F.4(d) confirmed (no n.6
   change needed beyond chunk 4 §E.4(h)).

## B. Consumed at this chunk

- **Field notes item 1** → n.4 as amended: decentralised-governance vehicles join the
  structures-in-actual-use list, with the clause that diffusion of formal control is a renaming of
  practical control, not an absence of it. Naming only; no section text changed, as directed.
- **Field notes item 2** → companion, "Friendly proposals, answered": the kill-switch answer ("the
  Act does not regulate the button; it regulates the hand") and the structure-shopping answer, by
  conversion rather than correction.
- **Chunk 1 §E.2 and §E.10** → n.27 (the revenue-screen defence; the one-sentence concordance
  pitch). §§E.1, E.3, E.6, E.7, E.8, E.9's "cite the siblings" instructions also land in n.27
  (compute trigger; incident clocks; whistleblower; audits; records/FOIA; the bridge cross-ref to
  n.24). §E.4's emergency-management co-recipient recorded in n.27 as a conforming option for
  adopting states — not drafted into SEC. 9(b), because no chunk adversarially passed statutory
  text for it.

## C. Editorial deviations, disclosed

- n.15: the in-chunk reference "set out at §E.4" rendered as "set out at audit/chunk2 §E.4" (would
  otherwise dangle in the shipped companion).
- n.16: "SEC. 12 as amended at §E.3(c)" rendered as "SEC. 12" (the amendment is now simply the
  text).
- Chunk 2 §E.5's caution glyph (⚠) dropped in the companion's Placement section; the caution is
  kept in words (the glyph is the audit files' unverified-source marker and would mislead there).
- Chunk drop-in italic taglines (e.g. "*Disgorgement.*", "*First rank.*") set as plain headings in
  the .txt act; case names in statutory text stay unitalicized per v3.2 house style; typography
  normalized to straight quotes in the act file.
- WHY page: "Where knowing violation kills" → "Where a violation kills" (true after SEC.
  10(c)(4)); one clause added noting SEC. 13 makes the criminal-core claim operative text.
- README: Jensen story pointer conformed to SEC. 6(b)(1)/10(c)(4) — chunk 4 §A.2's correction,
  now cured in text, reflected in the telling.
- READ FIRST renumbering avoided entirely: items keep their v3.2 identities (n.21, n.25, n.26
  cross-reference items 3(c), 6, and 9 by number); item 7 marked closed in place; new matter
  appended as item 11.

## D. Carried to v4 (the open register)

1. **SEC. 9(a) recast** of the two characterisation-shaped triggers — jointly with the regs
   evaluation Part; thresholds from the Agency, not the reporter (chunk 2 §E.3(d); READ FIRST item
   11). SEC. 9(a) ships in v3.3 with its v3.2 text intact, by design.
2. **Regs Part 2 re-pin** (READ FIRST item 1) and the watch-list review.
3. **The cite-check list** — consolidated in the companion; chunk 5 §G's list stands open.
4. **Standing watch** — not re-run at chunk 6 (assembly is same-day as the chunk 4 sweep, which
   chunk 5 incorporated by reference). The first act of any v4 drafting chunk remains the
   re-sweep; the *xAI v. Bonta* decision still triggers the n.16 re-run plus the interim-bridge
   transmission-layer check (chunk 5 §I.2).

## E. Banners stamped this chunk

- chunk1_landscape_audit.md: chunk-5 UPDATE (CA incident clock closed; the §E.9 bridge built) and
  a chunk-6 CONSUMED note (n.27 executions).
- chunk4_harm_tier_rebuild.md: chunk-5 UPDATE (both ⚠s pinned; the §G decision item executed as
  SEC. 5(e); regs conforms executed).
- field_notes_for_assembly.md: CONSUMED stamp (both items).

Chunks 2 and 3 already carried their banners; chunk 5 needs none (nothing later has touched it).


---

<a id="chunk-7"></a>
<!-- BEGIN audit/chunk7_hostile_brief.md · sha256:2db18bf1f61a · concatenated 19 Aug 2026, content verbatim -->

# CHUNK 7 — THE HOSTILE BRIEF: v3.3 READ BY THE OTHER SIDE'S COUNSEL

Drafting date: 17 August 2026. Method: the adversarial pass, promoted from a section to a chunk.
Every prior chunk attacked its own drop-ins; nobody has yet attacked the assembled Act the way the
opposition actually will — in persona, on retainer, with a client. This chunk does that. The memo
below is written as if by counsel to a frontier-lab coalition and its principals: what they check
first, what they kill with, what they structure around, and the amendment sheet they hand a
friendly committee member. Nothing in it is advice to anyone; it is the Act's own red team wearing
the other side's suit. The standing aim it is written against is the Act's: personal criminal
liability for the natural persons holding practical authority over frontier systems, now. Every
finding is logged so chunk 8+ can weld the doors shut. Findings genuinely new to the audit trail
are marked **[NEW]**; findings the file already admits are marked [KNOWN — cite], because a memo
that rediscovers the file's own §I sections bills hours without adding value.

House rules apply: ⚠ marks claims not pinned to primary this session; the register at §7 is the
conversion surface for the drafting chunks. Standing watch re-swept this morning, first act, per
the house rule: *xAI v. Bonta* (9th Cir. No. 26-1591) argued 16 July 2026, still undecided;
FRONTIER Act (H.R. 9925) referred, no markup located; GAAIA still an unnumbered discussion draft;
nothing else moved. The sweep sources are in §8. One new pin made this session: 18 U.S.C.
§ 3663A(a)(2) defines "victim" as a person "directly and proximately harmed" — load-bearing for
F9 below.

The memo is written in American English because the person it imitates would be. Normal service
resumes at §7.

---

## THE MEMO

PRIVILEGED & CONFIDENTIAL — ATTORNEY WORK PRODUCT — **SIMULATION; NO CLIENT EXISTS**

MEMORANDUM

TO: The Coalition steering committee; family offices of the principals
FROM: Outside counsel
RE: "MODEL ACT — Frontier AI Public Welfare Offenses (v3.3)" — assessment and plan
DATE: 17 August 2026

You asked for the short version first: this is the most dangerous piece of paper in the state
docket, and it is dangerous precisely because it is not a bill yet. It is a loaded template —
public domain, citation-complete, drafted to be dropped into any legislature in the country in the
week after an incident, which is the week we have the least influence. It has no sponsor to
pressure, no author to subpoena, no organization to defund. Our standard playbook opens by making
the bill's champion expensive; this bill has no champion until the worst possible moment, when its
champion will be a grieving legislature. Treat it as live ordnance. The work is to make sure that
when it is introduced — and at BIPA odds, eventually, somewhere, it will be — it arrives
pre-softened.

Second headline, and I want no illusions upstairs: **the federal cavalry does not reach this
statute's core.** Their own preemption file (they publish their work; see §1.5) is correct on the
law. FRONTIER §9(b) reaches obligations on *developers* in Covered Subject Areas; this Act's
first-rank offenses are operating, lying, and record-keeping offenses borne by whoever operates,
speaks, and holds records — and H.R. 5388's criminal carve-out would save them *because* they are
criminal. If Congress passes FRONTIER as introduced, we shave off their disclosure limb and their
third-party audit modes, and their SEC. 13 machine suspends those pieces, keeps the core, and
revives the rest at the sunset. Do not tell the principals that Washington solves this. Washington
narrows it. The kill has to happen in committee, state by state, and the merits brief is the
garnish, not the meal.

### 1. What I checked first

In order, before lunch, the day the file landed:

**1.1 The client-exposure map.** Who, by name and office, does this reach. Answer: everyone we
represent. SEC. 4(b)(2) presumes controlling-person status (civilly) for *any person* holding
rights "sufficient, alone or in concert with others, to direct or replace the management of a
developer or provider, **or of any entity that directly or indirectly controls it**" — that is the
holding company, the supervoting founder shares, the family office, the foundation board. The
Synthes gap — convict the officers, never charge the controlling shareholder — is closed in text
(4(c): appointing a safety officer "diminishes nobody's exposure"; "Substance controls over
title"). SEC. 7(a) disgorges "any increase in the value of any interest," realized or not, with a
civil presumption attributing equity comp to the violation period. SEC. 7(b) makes every penalty
personally uninsurable and criminalizes the gross-up, the reimbursement, and the *receipt*. SEC.
10(d)(4) disqualifies from acting as a controlling person — a corporate death sentence the client
fears more than the fine. And 6(b)(1) + 10(c)(2)(B) puts life on the table where a knowing
violation is a but-for cause of death. The three provisions the principals will pay anything to
remove, ranked: **SEC. 7 (the money), SEC. 4(b)–(c) (the reach), SEC. 6(b)(1)/10(c)(2) (the
years).** Every amendment on the sheet at §5 is aimed at one of the three.

**1.2 Introduction risk.** No sponsor, no state, no clock — which cuts both ways. Fifty
legislatures, most meeting annually, staffers who reach for finished text after an incident: the
cost of introduction is one photocopy. The drafters know their Pecora history; their WHY page says
the quiet part ("finished text, lying around"). Our monitoring spend goes up, permanently.

**1.3 The committee terrain.** Where it lands decides what kills it. In a judiciary committee the
criminal bar frowns at public-welfare offenses on principle; in a commerce committee the startup
witnesses do the work; in appropriations the fiscal note does (§2.7). Note for the state teams:
their placement instruction (companion, "Placement") tells adopting states to codify the offenses
*in the penal code among offenses against the person* — clever; it books judiciary committees and
frames the bill as homicide-adjacent rather than tech regulation. Fight the referral.

**1.4 The constitutional letterhead.** What we can threaten credibly on day one (§3). Rule of
thumb from twenty years of this: the letter does not need to win; it needs to give a nervous chair
a citation to hide behind.

**1.5 Their own confession file.** They publish the audit trail — five working chunks plus an
assembly record, each ending in a section titled "where the armour is thin." Gift. Every §I
admission is a pre-drafted committee question: *"Your own drafting file concedes the interim
standards are 'transparency law doing validation work'"* (chunk 5 §I.1); *"your own file says the
consecutive-sentence cap has a 'soft joint' a prosecutor can charge around"* (chunk 4 §I.2);
*"your own file says the strongest offense in the Act sleeps until an agency acts"* (chunk 5
§I.4). Standing instruction to the research team: mirror the repo nightly; diff every version; the
CHANGELOG is our early-warning system. (Understand what this costs us too: they fix faster than we
brief. §6.5.)

**1.6 Opposition research on the drafters.** Anonymous; pseudonymous campaign account with a joke
handle; their own field notes state the campaign is "co-drafted by a human and a frontier model"
(field notes 8(d)) — *the bill was written by the thing it regulates* writes itself into a chyron;
retired "ten men" copy still quotable under their own no-deletion policy (field notes 11). None of
this touches the text — their citations check out, which is annoying — but committees are made of
people, and "who wrote this and why won't they show their face" buys us a hearing delay in at
least half the chambers. Their Federalist-Papers answer is good copy; it is not a witness at a
table.

**1.7 The enforcement reality.** Before panicking the principals: who actually gets prosecuted,
where. The base offense is a misdemeanor. Extradition for out-of-state misdemeanants is lawful ✅ (*Dennison*, §8 pin)
but vanishingly rare in practice; a principal who never enters the enacting state is, for the base
tier, practically beyond its criminal process. The felony tier changes that calculus, as does
presence — count the states with offices, data centers, and conference keynotes. Also note
10(d)(2): operating a *suspended configuration* "in this State by any person with notice" is
contempt plus a 5(a) violation — the in-state employees carry that exposure daily. The people this
Act reaches first are not the principals; they are the VPs who live there. That is either our best
recruiting pitch against it ("this jails your constituents' employers, not billionaires") or
theirs ("then send us the billionaires"), depending on who frames first.

### 2. Killing it in committee

**2.1 The blast-radius exhibit. [NEW]** The campaign says "ten seats." The text disagrees, and the
gap is our best weapon. Walk the committee through SEC. 3(c)(4)(A): the interim standards apply
"to **every** covered frontier model and covered system, and to **each entity** that develops,
releases, provides, **or deploys** one, **without regard to any revenue threshold, exemption,
effective date, phase-in date, or territorial term**." Now SEC. 1(b)(2): a covered *system* is a
deployed *configuration* — "including tools, memory, retrieval, credentials, and permissions."
Now SEC. 3(b)/(c)(2): validation "attaches to an identified model version and deployment
configuration," and a system "validated without tools is not validated as to any configuration
granting external access or significant permissions." Assemble: **every agentic wrapper, every
SaaS product that bolts tools onto a frontier API, is a deployer of its own covered
configuration, cannot ride the lab's validation because its configuration differs, and owes its
own conformity assessment, transmitted to a state agency, from day [180] — under a statute whose
enforcement instrument is criminal.** The three enacted states confine their heavy duties to
\$500M-revenue developers; this Act deletes the screen *and* extends past developers to deployers.
The personal-use carve (SEC. 1(b)(3)) saves the hobbyist and no one else — "personal,
noncommercial" excludes every sole proprietor with a chatbot. Witness list: NFIB, the state
startup association, one sympathetic two-person AI company, a university CIO (§2.2). Kicker,
quotable: their own n.27 claims the revenue screen only "rations compliance-paperwork cost, which
this Act imposes on no one until standards exist" — while their SEC. 3(c) imposes exactly that
paperwork at day [180] through interim standards the same sentence admits "apply without the
screen." Their footnote contradicts their statute. I will read both aloud.
*(Honest annex, for us: their SEC. 2 allocates duties per capacity — the wrapper answers only for
its configuration; due care, not perfection; a documented adoption of upstream materials plus its
own tool manifest is a colorable assessment; and 3(c)(4)(E) credits documentation already made
for CA/NY/IL. The duty is lighter than the exhibit makes it look. The exhibit does not care. The
committee will not read (c)(4)(E).)*

**2.2 The university exhibit. [NEW]** Reading rule (A) strips "any … exemption … of the enacting
jurisdiction." New York's article 44-B carries an express exception for academic institutions and
named consortiums (GBL § 1426 ✅ pinned at §8). So a university consortium releasing a 10^26
model owes full pre-release duties here **that New York itself would excuse**, and its provost is
a presumed controlling person of the releasing entity. The flagship university calls the chair
before we do. There is no academic carve anywhere in this Act — by design (release parity), but
the design has no answer *in text* for the land-grant witness.

**2.3 Jail for negligence.** SEC. 6(a) + 10(b): up to a year's custody on a *failure of due
care* — negligence, criminally. They have DeCoster and eighty years of doctrine; we have every
defense-bar association, the ALEC mens-rea-reform model text ✅ (§8 pin), and the phrase "criminalizing
paperwork errors." Legally weak (the culpability floor is drafted exactly to the DeCoster
concurrence), politically evergreen.

**2.4 The life headline.** 10(c)(2)(B): "imprisonment for any term of years or for life for each
offense." Their own file (chunk 4 §I.1) concedes "the optics still belong to whoever quotes
first." Quote first. Never mention that the same geometry is the federal consumer-tampering
statute; if opposing counsel brings § 1365, pivot to §2.3.

**2.5 Unilateral disarmament.** Release duties (SEC. 2, 1(b)(9)) bind whoever releases into the
state — practically, American labs. A lab in Shenzhen or Abu Dhabi releases weights with total
impunity from this statute (service of criminal process on foreign officers being what it is ⚠),
while the American releaser's officers carry personal exposure. "This bill jails American
engineers and waves at Chinese ones." Their honest answers — deployer-side duties reach anyone
serving in-state residents whatever the flag; the EU already runs release duties above the
systemic-risk line (AI Act art. 53(2)); a state cannot conscript Beijing and that was never the
theory — live in a footnote (n.5) and a foreign statute. Nothing *in the Act's own findings*
answers the competitiveness charge. Free swings for us until they draft one.

**2.6 The cure period.** Demand TRAIGA's 60-day cure (Texas HB 149 — red-state precedent, AG
enforcement, cure period before action). A cure period converts a criminal due-care statute into
an advisory letter with a grace window — nobody cures a death — and it polls as reasonableness
itself. This is the single cheapest gut on the sheet (§5.D) because it sounds like a courtesy and
functions as a repeal of deterrence. Their file has no prepared answer to it. **[NEW — no
objection-bank entry exists for the cure period.]**

**2.7 The fiscal note.** The Act designates an existing agency and hands it: standards
rulemaking with independent-review obligations (SEC. 3(a)), free public hosting of adopted texts,
processing of every conformity assessment in the state (3(c)(2)(C)), acting upon or publishing a
reasoned declination of "any credible report within [180] days" (SEC. 11(e) — a mandamus hook
bolted to a workload bomb), annual inflation rulemaking (10(a)), and security-sensitive records
handling (SEC. 12). Funding: a fund fed by penalties that arrive only after enforcement succeeds.
Ask the fiscal office to price the mandate; starve the appropriation; then §4.6 does the rest.
The bracketed [540]-day proposal clause is unenforceable and their file admits the Agency's
"inaction can delay" the refinements indefinitely (chunk 5 §D.1–D.2, §I.4).

**2.8 Provenance.** §1.6, deployed politely: "The committee is being asked to adopt criminal law
whose drafters will not appear before it." Pair with a friendly law-professor witness saying the
citations *are* real but the judgment calls need accountable authorship. (Risk: they convert this
— the text stands on its citations precisely so authorship is irrelevant; and somebody on that
committee has read the Federalist Papers. Deploy in chambers where nobody has.)

### 3. The litigation surface

Ranked honest-to-spurious. The honest ones shape amendments; the spurious ones still letterhead.

**3.1 Vagueness, as applied, on the controlling-person class. [PARTLY KNOWN]** SEC. 4(a)(2)
sweeps anyone with material practical authority over "budgets, compute, infrastructure, or risk
policy." Line up the declarations: a finance VP who approves the compute invoice; an SRE with
deploy keys; a datacenter lease signatory. Each "possesses … material practical authority" on a
literal read; none is the campaign's "ten." The Act's answers — "material," several liability
only for one's own authority (SEC. 2 final clause; 6(e)'s ability-and-opportunity construction;
6(d)'s beyond-reasonable-doubt burden) — are real but live in litigation, which means they live
in our fee applications. As-applied vagueness plus a *County Court of Ulster County v. Allen* ✅ (§8 pin)
rational-connection attack on the criminal permissive inference from bare status (4(b): "such
status is evidence from which the trier of fact may infer") in the case of a passive minority
holder. We lose the facial challenge (Park's own dissent called the standard a nullity and lost);
we win discovery burdens and jury-instruction fights.

**3.2 "Material expansion" is undefined until a rule exists — and operative before one does.
[NEW]** SEC. 1(b)(6): "'Material expansion': a change, **defined by rule**, that increases…" No
rule exists in layer two. Yet the duty (SEC. 2) and the transmission element (3(c)(2)(C):
assessment transmitted "on or before the deployment, **material expansion**, or release to which
it relates") operate from day [180]. The modifiability budget got an interim statutory default
(the floor, n.25) precisely because "a defect in a criminal duty" (*Connally*; *Kolender*) — the
expansion definition got none. During the entire provisional period, either (a) lenity: no change
is a "material expansion" because the defining rule does not exist — expand freely, the
re-validation trigger is dead; or (b) the State says the statutory description self-executes —
then it is a criminal element resting on "increases … capabilities, autonomy, external access, or
permissions" with no rule, and we plead *Connally* with their own n.25 as the concession that
this exact structure needed an interim default. Either reading is a win. This is the cleanest
drafting defect in the file.

**3.3 The coverage element is the defendant's own arithmetic — and distillation is expressly
un-ruled. [NEW]** The 10^26 element (SEC. 1(b)(1)) counts "training and lineage compute … as
further specified by rule, **including the treatment of fine-tuning, distillation, merging, and
aggregation**." Until a rule: does a distilled student model's "lineage" include the teacher's
compute? The text does not say; lenity says no; and designation of frontier-equivalent models
under SEC. 3 is "prospective only" and requires the Agency we just defunded (§2.7). **The
structuring advice writes itself: deploy through distilled children below 10^26 by their own
ledger** (§4.2). Proof problem as backup: lineage compute is private arithmetic; the SEC. 12
records duty attaches only to entities with covered systems, so the entity that claims 9×10^25
keeps nothing under this Act, and the State proves the element from what, exactly? "Excluding
unrelated experimental runs" (un-ruled) gives our compute-accounting experts a second seam.
Their n.27 answers "invented threshold" (it is California's and Illinois's definition); it does
not answer "unprovable element" or the distillation gap, because the family's statutes are civil
and this one must convict beyond a reasonable doubt.

**3.4 But-for causation with no proximate-cause limit. [NEW]** 6(b)(1) and 10(c)(2)(D) run the
death tier on *Burrage* but-for causation, full stop; 10(c)(4) orders restitution "per the
structure of 18 U.S.C. § 3663A" — but § 3663A(a)(2) itself defines a victim as a person
"**directly and proximately** harmed" (pinned this session). The Act borrowed the mandatory
structure and left the proximate-cause limiter on the shelf. For eggs and antifreeze the gap
never bites — the product harms directly. For a general-purpose system, the paradigm harm runs
through an intervening human actor: the user who follows the recipe, the fraudster who uses the
model, the patient who ignores the doctor. On pure but-for text, a knowing 5(a) violation
(deploying unvalidated) plus any death the system's output but-for contributed to — however
independent the intervening criminal act — is a life-eligible count. We will run the hypos in
committee (the model wrote it, a human did it — life for the CTO?) and preserve the argument for
trial. Their honest answer is that the *violation*, not the model, must be the but-for cause, and
that duty-scope limits do quiet proximate-cause work; but "results" with *Burrage* alone is a
gift to our merits brief and our op-eds simultaneously. (Note for §5: an amendment adding
"directly and proximately" is one we could even support publicly — which is exactly why they
should draft it themselves before we draft it wider.)

**3.5 The compelled-characterization residue. [KNOWN — their READ FIRST item 11]** SEC. 9(a)
still triggers on "deception of safety or monitoring controls" and "a reproducible evaluation
finding of materially increased risk" — two labels the reporter must self-apply, the exact defect
*X Corp. v. Bonta* punished in AB 587. Their own file has flagged the recast for two versions and
shipped without it. Bonus: the near-miss clause ("would have constituted an incident … but for
intervention or chance") is recursive at the margin — a jailbreak *caught by the monitoring* is
an event that but-for the intervention would have been an incident; read literally, every
successful defense is reportable. Ridicule is a legal strategy when the statute supplies it. If
*xAI v. Bonta* lands against AB 2013, every SEC. 8/9 analogue gets a letterhead paragraph within
the week.

**3.6 Contracts Clause on "maintain." [NEW]** SEC. 7(b)(1)(A) criminalizes "enter[ing] into,
renew[ing], **or maintain[ing]**" penalty-indemnity insurance. As applied to D&O towers written
before enactment, "maintain" makes it an offense to keep performing an existing contract —
substantial impairment of existing contractual relations, *Sveen v. Melin* / *Energy Reserves*
framework ✅ (§8 pins). The State answers with the police-power public-purpose prong and probably wins on
balance, but this is our best *civil* facial claim (no lenity problems, sympathetic plaintiff —
an insurer!), and it generates a preliminary-injunction shot at SEC. 7(b) as a whole. Cheap fix
exists (prospective application to contracts entered or renewed after the effective date);
until they draft it, we sue.

**3.7 Excessive fines and the stack. [KNOWN — their nn.19, 21 and chunk 3 §I.4]** Concede
privately: their valves are competent (benefit floor and gain multiplier are measures of the
offense; concurrency default; findings gate; [forty]-year cap; life available instead of
arithmetic). Attack anyway under state proportionality clauses — their own n.21 lists Illinois,
Oregon, Indiana, West Virginia as stricter than *Harmelin* — and run the archived v3.2's
2,140-year arithmetic in media (they fixed it; the archive is public; the correction never
catches the accusation).

**3.8 The prejudgment freeze.** SEC. 7(a)'s asset restraint "on a showing of probable
adjudication and risk of dissipation" — *Connecticut v. Doehr* ✅ (§8 pin) posture. The exigency finding
likely saves it; letterhead it anyway; family offices pay for the motion practice.

**3.9 The Attorney General's suspension switch. [NEW — the sharpest structural finding]** Read
SEC. 13(c) as our house counsel, not theirs. The AG "shall … determine whether and to what
extent" federal law preempts, by published order; upon publication the provision "is suspended to
the extent … stated in the order"; and (c)(3): **no person may be convicted for conduct during a
suspension** — with revival prospective-only (13(d)) and an express no-inference clause (13(e)).
Now notice what is absent: any standard of review, any mechanism to challenge an order as *too
broad*, any duty of candor, any provision for who may seek vacatur. A friendly Attorney General
— and AGs rotate; we fund those races at a fraction of a legislature's cost — publishes a
generous order the week FRONTIER passes (or on any "regulation having the force of law";
consider what an FCC or FTC preemptive rule under EO 14365 hands him), suspending the developer
duties *and everything arguably adjacent*, and every day it stands is a day of immunized conduct
that no later court can claw back. The fair-notice architecture they built to protect defendants
(prospective suspension, prospective revival — *Bouie* discipline, n.15) doubles as an amnesty
ratchet in the hands of the officer the Act trusts most. Their file worries a court will resent
the machine (chunk 2 §I.4); it never asks what a *captured operator* does with it. Strategy:
stop fighting SEC. 13; start planning for it.

**3.10 The certification office nobody holds. [NEW]** SEC. 8: "the chief executive officer …
shall personally certify," non-delegable, no designee. Their DAO answer (companion, "Friendly
proposals") says SEC. 4 reaches diffuse structures — true, for *liability*. But SEC. 8's duty
attaches to a named office. An entity chartered without a chief executive officer — a member-
managed LLC, a DAO, a foundation council — has no person on whom the non-delegable duty sits.
Either the duty fails (charter around it: our advice) or the State stretches "chief executive
officer" functionally (litigate: our motion). "Each controlling person designated by rule"
backstops only after the Agency designates — see §2.7 on the Agency. The structure-shopping door
they nailed shut in SEC. 4 is standing open in SEC. 8.

**3.11 The certification treadmill. [NEW]** SEC. 8 triggers "[b]efore material deployment and
following material change." "Material deployment" is defined nowhere (SEC. 1 defines "material
expansion" only) — an undefined trigger on a criminal-adjacent duty ⚠ vagueness note. And per
the regulations (Part 1.6), "configuration" includes *system prompts*; Part 3.2 makes material
any change that "could reasonably affect a … safety property"; frontier operators ship
configuration changes daily. Exhibit: a calendar of one month's config pushes; ask the sponsor
whether the CEO signs 1350-style paper for each. The honest reading (materiality does the work;
certifications batch naturally at genuine capability changes) requires the word "material" to
carry weight the statute never gives it. SOX certifies quarterly, on a calendar; this certifies
on an undefined event. Operational-impossibility affidavits from three CTOs and the committee's
eyes glaze in our favor.

**3.12 "Autonomous external-access capabilities" (5(b)) is an undefined statutory class.
[PARTLY KNOWN]** Dormant until layer three (their §I.4), and the controls element arrives by
prescription — but the *class trigger* ("having autonomous external-access capabilities") is
statutory text with no definition and no rule-hook. At promulgation we challenge the rule as
exceeding a class the statute never bounded; before it, we tell clients everything is or nothing
is autonomous, whichever the memo needs. **[NEW as to the missing rule-hook.]**

**3.13 The privilege collision. [NEW]** SEC. 5(e) criminalizes "refusal to permit, upon the
lawful demand … access to or verification or copying of" required records; SEC. 12 keeps
"evaluation results" on the list and says the exemption "does not create any privilege for
underlying facts." Labs run red-teams and incident post-mortems under attorney-client direction
and work-product protection. When the Agency demands the evaluation file and the entity asserts
privilege, is the assertion a 5(e) "refusal"? "Lawful demand" presumably imports privilege
limits — presumably is where fees live. Two exploitations: (a) litigate the collision; (b)
better, *advise clients to move safety evaluation into privileged channels* and then testify
that the Act drove safety work under privilege. The required-records doctrine answers compelled
production of the mandated records themselves (n.26, *Grosso* pinned); it does not sort mandated
records from privileged overlay, and the statute never tries.

**3.14 Fifty privileges. [KNOWN — chunk 5 §I.5]** The required-records pass is federal; several
state self-incrimination clauses run broader; we pick the enacting state accordingly and brief
the state clause. Their file already told us which fight to pick. Thank them.

### 4. Structuring around it (the quiet memo to general counsel)

**4.1 Corporate form.** Do not incorporate the DAO fantasy — their SEC. 4(a) in-concert-and-
through-any-arrangement language is drafted well and the multisig-key line ("a key is practical
power," n.4) will survive contact. The realistic play is duller: charter without a CEO office
(§3.10); flatten formal authority into committees with rotating chairs and documented collective-
only action, so no single natural person's "material practical authority" is clean on paper; keep
the principals' control rights in instruments exercisable only "in concert" with independent
trustees. None of it defeats 4(a); all of it moves conviction from document review to contested
inference, which is the difference between a plea and an acquittal.

**4.2 Compute and coverage.** §3.3 operationalized: serve inference from distilled models below
10^26 by their own training ledger; book ambiguous runs as "unrelated experimental runs" pending
a rule; keep lineage accounting entity-separated so aggregation questions need discovery to even
ask. Watch for the counter (an interim lineage-attribution default mirroring the n.25 floor);
until drafted, the seam is open.

**4.3 Geography.** SEC. 1(c) withdraws jurisdiction cleanly on its own terms: no in-state
deployment, availability, or release → no duty. Their n.17 concedes "jurisdiction-specific
access controls have become ordinary." Fine: comply by exit. Geofence the enacting state at
launch, publicize the exit, and let the state's own startups scream. Two enacting states and the
exit story collapses (nobody geofences California *and* New York), which is why (§6) the kill
must be total: one state enacting is their BIPA scenario.

**4.4 Compensation timing.** SEC. 7(a) reaches comp "received or accrued during the period of the
violation and the [twelve] months following its cessation or concealment," with the presumption
covering "[i]ncentive- or equity-based compensation received … during the period." So: front-load
fixed cash before any covered deployment; vest equity on schedules that can be suspended during
exposure windows; take appreciation as unrealized and fight "increase in the value of any
interest" valuations expert-against-expert. The anti-offset clause (7(b)(2), "purpose or
predominant effect") is their catch-all and their own file calls it "the clause a hostile reader
calls vague" (chunk 3 §I.2) — civilly enforceable at most against a controlling person absent
knowledge, and we will constitutionalize the vagueness point in the civil posture where lenity
does not embarrass us.

**4.5 Insurance.** Domestic penalty-indemnity cover dies (NSW pattern; the market will stop
writing it — their file concedes the insurer-side offense "mostly cannot be enforced against the
insurers," chunk 3 §I.3). Move the tower to foreign-law policies held by foreign parents
benefiting persons who never touch the enacting state; the constructive trust bites only what a
court finds. Defense costs remain expressly insurable (7(b)(5)) — fund the war chest there,
maximally, since it is the one lawful channel. And press §3.6 in parallel.

**4.6 Live under the bridge forever.** The Act's rigor arrives only when the Agency promulgates
(their chunk 5 §I.1: the bridge "buys determinacy and family parity, not rigor"). Therefore: the
Agency never promulgates. Comment-flood every proposed standard; demand the independent-review
record SEC. 3(a) requires for each incorporated version; litigate each adoption *Touby*-style;
fund the 24-state AG letter against the rulemaking. Every year of delay is a year in which
validation = a self-prepared conformity file against write-your-own-framework standards, 5(b)
never commences, and the "strongest provision in the Act" (their words, chunk 2 §D) stays
asleep. And here is the jujitsu on their best talking point: their capture answer is "you cannot
capture a law whose only output is a defendant" (field notes 12 — "no permit, no approval, no
gate"). **SEC. 3(b) lists "Agency approval" as a validation mode.** That is a permit gate, in
their own text. Lobby the Agency to select approval mode for the heaviest standards; then the
queue exists; then we own the queue, the way we own every queue. Their anti-capture thesis is
one Agency mode-selection away from self-refuting.

### 5. The amendment sheet

Each drafted to sound reasonable; each maps to what it guts. File in every chamber; any one
passing is a win.

**A. The reliance defense.** "It is a defense that the person reasonably relied in good faith on
the advice or performance of qualified personnel or independent experts." — Re-enacts the 1948
amendment Congress struck (they know it; Park n.15; their README §"1948"). Guts 4(c)
non-delegation: every principal retains an expert and the expert becomes the defendant-shaped
void. Committees that have not read Park's footnotes hear only "good faith."

**B. The scienter uplift.** Strike "failed to exercise due care" (6(a)); insert "knowingly and
intentionally violated." — Converts Park into ordinary fraud; nothing left but 5(d). Frame as
"mens rea reform," bipartisan flavor available.

**C. The California harmonization.** Insert the \$500,000,000 revenue screen "for consistency
with the enacted framework of California, New York, and Illinois." — Sounds like conformity;
functions as an exemption for every personally-held vehicle, every foundation-owned lab, every
new entrant — the exact structures SEC. 4(b)(2) was aimed at. Their counter is n.27's
"risk-not-revenue" sentence; our exhibit is §2.1's blast radius, which makes the screen feel
like mercy. Note the trap for them: accepting C to solve §2.1 guts §1.1's reach. (Their better
answer is a *deployer-side de-minimis* that leaves developers and releasers screenless — if
they draft it first, C loses its cover story. Hope they don't.)

**D. The cure period.** "No prosecution shall commence except upon violation continuing [60]
days after written notice." — §2.6. Deterrence dies; nobody cures a death; every violation
becomes a negotiation. Cheapest gut on the sheet.

**E. The safety-officer harbor.** "Designation of a qualified safety officer … constitutes prima
facie evidence of due care." — Rebuilds the Synthes shield 4(c) exists to demolish; sold as
"encouraging safety investment."

**F. Sunset and study.** Three-year sunset plus a study commission. — Outlives no incident;
guarantees a second bite with amortized outrage.

**G. The civil swap.** "Replace criminal penalties with enhanced civil penalties of up to three
times…" — The price list, restored. Their whole file exists against this one; expect their
strongest floor speech. File it anyway; it anchors the negotiation.

**H. The realized-gains cap.** In 7(a), strike "and any increase in the value of any interest";
cap disgorgement at "economic benefits actually realized." — The principals' true ask. Unrealized
frontier equity is the only nine-figure consequence in the Act; this amendment quietly returns
the balance sheet to safety while leaving the theater intact.

**I. The proximate-cause amendment.** Add "directly and proximately" to 10(c)(2)(D) and (c)(4).
— The one we might genuinely win on the merits (§3.4) and can support in public as "mainstream
criminal-law causation." Support it loudly; it costs them little and us nothing, and our support
for *an* amendment launders opposition to the rest. (If they are smart they draft it first and
take the win away.)

### 6. Honest assessment (privileged; do not circulate past the steering committee)

**6.1** The preemption armour is competent. Chunk 2's lane analysis is correct as far as I can
test it; the first-rank offenses genuinely sit outside FRONTIER §9(b) as introduced, and § 6(a)(2)(B)
of H.R. 5388 would *save* the criminal provisions. Do not promise Washington.

**6.2** The Park lineage is real and the culpability floor is drafted to the DeCoster
concurrence. Facial constitutional attack on the core fails. Everything in §3 is friction and
amendment leverage, not a kill shot — except possibly 3.2 (interim-period expansion) and 3.6
(Contracts Clause), which are genuine but curable defects. Assume they cure them; their public
cadence is days, not sessions.

**6.3** The stories are a problem. Antifreeze, eggs, cantaloupe, bone cement — every one is a
televised-hearing exhibit against us, and the "your eggs are safe because two executives went to
prison" line lands with exactly the voters our polling says are softest. Do not let a hearing
become about the stories. Keep it about startups, universities, and fiscal notes.

**6.4** The whistleblower section is the operational threat nobody upstairs is pricing. 10–30%
of benefit-floored, per-day-accrued sanctions, mandatory minimum, gag clauses void, anonymous
through counsel (SEC. 11) — every disaffected senior engineer with a copy of an unflattering
eval becomes a funded plaintiff-in-waiting. Compliance posture inside the labs must assume the
filing cabinet is public. (Their design bet, stated in n.11: the inspectors already work for us.
Correct.)

**6.5** The method is the deepest problem. They draft in public, in chunks, same-day, with an
audit trail, and they metabolize objections into drafting notes within the week — our own best
arguments end up cited in their companion as "answered." This memo will be obsolete against
v3.4. Bill accordingly.

**6.6** Recommendation. Kill in committee via §2 (blast radius, universities, cure period, fiscal
note), holding §5.C/D/E as the fallback gut. Fund AG races in likely enacting states (§3.9 —
cheapest structural insurance in the file). Prepare §4 compliance postures now, quietly, because
if one state enacts after an incident, the officers most exposed are the ones whose lawyers
started in the committee phase. And whatever else: never let a floor vote happen inside ninety
days of a funeral.

*— end of simulated memo —*

---

## 7. FINDINGS REGISTER (conversion surface for chunks 8+)

Severity: ★★★ = drafting defect / structural gift, cure in text; ★★ = needs answer in companion
or objection bank; ★ = optics/watch item. "Known" = already admitted in an §I/READ FIRST; listed
only where the hostile use adds something.

| # | Finding | Act cite | Severity | Status |
|---|---|---|---|---|
| F1 | "Material expansion" defined only "by rule" but operative in layer two — lenity kills the re-validation trigger for the whole interim period; needs an interim statutory default (the n.25 move) | SEC. 1(b)(6); 2; 3(c)(2)(C) | ★★★ | **NEW** |
| F2 | Distillation/merging/aggregation lineage treatment expressly awaits a rule — sub-10^26 distilled children of covered models are out on lenity, designation is prospective + Agency-dependent; also the coverage element rests on the defendant's private compute ledger (records duty is circular: attaches only if covered) | SEC. 1(b)(1); 3; 12 | ★★★ | **NEW** |
| F3 | Death/injury tier and restitution run on bare *Burrage* but-for; § 3663A model itself says "directly and proximately harmed" (pinned) — no intervening-actor limiter in the statute whose paradigm harm runs through intervening actors; decide and draft (add proximate cause, or state the duty-scope answer in text/note) before the opposition drafts it wider | SEC. 6(b)(1); 10(c)(2)(D), (c)(4) | ★★★ | **NEW** |
| F4 | SEC. 13(c) AG suspension order has no review valve: an over-broad order immunizes conduct (c)(3) with prospective-only revival — a captured AG is an amnesty switch; add standing/review (vacatur prospective, order must state the federal enactment and extent, any-person review), keeping the fair-notice ratchet | SEC. 13(c)–(e) | ★★★ | **NEW** |
| F5 | "Maintain" in the insurance ban reaches pre-enactment contracts — Contracts Clause exposure; cheap fix: prospective application to contracts entered/renewed after effective date (+ short conforming window) | SEC. 7(b)(1)(A) | ★★★ | **NEW** |
| F6 | SEC. 8 duty sits on a named office ("chief executive officer," non-delegable) an entity can simply not have — DAO/no-CEO charter gap; fix: "or, where no such office exists, each natural person exercising the most senior executive authority, severally" + rule designation backstop | SEC. 8 | ★★★ | **NEW** |
| F7 | "Material deployment" (SEC. 8 trigger) defined nowhere; certification cadence per config-change operationally attackable (regs 1.6 counts system prompts as configuration); fix: define trigger, add periodic/batch certification window (SOX quarterly pattern) for changes below a stated threshold | SEC. 8; regs 1.6, 3.2, 4.2 | ★★★ | **NEW** |
| F8 | Deployer-side blast radius: 3(c)(4)(A) removes every screen and exemption for *deployers* too; per-configuration validation means wrappers can't ride upstream validation; no de-minimis, no reliance rule for non-modifying deployers; n.27's paperwork sentence contradicts 3(c) on its face — the committee kill-exhibit | SEC. 3(c)(4)(A); 3(b); 1(b)(2)–(3); n.27 | ★★★ | **NEW** (preemption lane known; committee exposure not) |
| F9 | Academic/consortium releaser: reading rule (A) strips NY § 1426's academic exception; no answer in text or bank for the university witness; decide posture (parity defended in a note + objection-bank entry, or a narrow research-release provision) | SEC. 3(c)(4)(A) | ★★ | **BANKED** — field notes 14, 17 Aug 2026; posture decision → chunk 8 |
| F10 | No prepared answer to the cure-period amendment (TRAIGA precedent) — the cheapest gut on the sheet; objection-bank entry needed ("nobody cures a death"; cure = price list with a grace window; contrast 5(d): truth needs no cure) | companion (bank) | ★★ | **BANKED** — field notes 13, 17 Aug 2026 |
| F11 | "Agency approval" validation mode is a permit gate that self-refutes the capture answer ("no permit, no approval, no gate"); fix: strike the mode, or bind it (shot clock + deemed validation on lapse + published criteria), and conform field-note 12's answer | SEC. 3(b) | ★★★ | **NEW** |
| F12 | 5(b) class trigger "autonomous external-access capabilities" has no definition and no rule-hook (unlike 1(b)(6)); add "as further specified by rule" + a minimal statutory description | SEC. 5(b); 1(b) | ★★ | **NEW** (dormancy known, chunk 5 §I.4) |
| F13 | Privilege collision on 5(e) "refusal": no text sorting lawful privilege assertion from criminal refusal; risk of driving evals under privilege; fix: "lawful demand" gloss or express privilege-preservation sentence keeping facts/records reachable (facts never privileged already in SEC. 12) | SEC. 5(e); 12 | ★★ | **NEW** |
| F14 | Unilateral-disarmament/competitiveness charge has no answer in SEC. 0 findings or the bank (deployer-parity + EU art. 53(2) + enforcement-reality answers exist but are scattered in n.5/n.17) | SEC. 0; bank | ★★ | **BANKED** — field notes 15, 17 Aug 2026; SEC. 0 sentence → chunk 8 |
| F15 | Ulster-County rational-connection attack on the criminal permissive inference from bare 4(b) status (passive minority holder hypo); consider a note (n.4) sentence anticipating it | SEC. 4(b); n.4 | ★★ | **NEW** — *Ulster County* ✅ pinned 17 Aug 2026 (§8) |
| F16 | Prejudgment freeze *Doehr* posture; probably survives (exigency + judicial findings); one sentence in n.18 forecloses the letterhead | SEC. 7(a); n.18 | ★ | **NEW** — *Doehr* ✅ pinned 17 Aug 2026 (§8) |
| F17 | Provenance/anonymity/AI-co-drafting as committee attack; answer exists rhetorically (Federalist) but consider a bank entry with the verification challenge as the reply ("check the citations; authorship is the one thing that doesn't matter to a citation") | bank | ★ | **BANKED** — field notes 16, 17 Aug 2026 |
| F18 | Introducible file hygiene: v3_3.txt carries campaign lines ("Steal it," the `)(` sigil) that must not ride into a bill jacket; ship a jacket-clean variant or a one-line instruction to counsel | model_act_v3_3.txt | ★ | **CURED** — 17 Aug 2026, `model_act_v3_3_introducible.txt` shipped, README lane updated |
| F19 | SEC. 9(a) characterisation triggers + recursive near-miss reading | SEC. 9(a) | ★★ | KNOWN (item 11) — hostile use sharpens: recursion ridicule |
| F20 | Interim standards rigor gap; "own framework" circularity tension inside 3(c)(5)'s two sentences | SEC. 3(c)(5) | ★★ | KNOWN (chunk 5 §I.1) — the two-sentence tension is **NEW** |
| F21 | Fiscal-note attack surface incl. SEC. 11(e) 180-day act-or-decline mandate | SEC. 3; 11(e) | ★★ | partly KNOWN — fiscal framing NEW |
| F22 | Archived v3.2's 2,140-year arithmetic quotable forever | archive | ★ | KNOWN (chunk 4 §I.1) |

Register note: F1, F2, F7, F11, F12 share one root — v3.3 built interim defaults for *some*
rule-dependent terms (the n.25 floor) and not others. Chunk 8 should sweep SEC. 1–3 for every
"by rule" dependency and give each an interim default or an express dormancy statement, one
pass, one principle: **no element waits on the Agency unless the Act says, in text, what happens
while it waits.** (Opened 17 Aug 2026 — `chunk8_rule_dependency_sweep.md`.)

## 8. SOURCES (this chunk's sweep)

Standing watch, re-run 17 Aug 2026: *xAI v. Bonta* PI denial (N.D. Cal. 4 Mar 2026, order PDF
via arstechnica CDN mirror), argued 16 Jul 2026 (techtimes; iapp; lawfaremedia; LASST amicus
22 Jul 2026 — new since the 16 Aug sweep, noted for the n.16 watch), no decision located.
FRONTIER Act H.R. 9925: congress.gov / govinfo BILLSTATUS — introduced, referred; no markup
located (ailawtracker concordant). GAAIA: still discussion draft, no bill number
(obernolte.house.gov press page; DLA Piper, Cato, TechPolicy.Press analyses; regulations.ai
lists it unnumbered). Pinned this session: 18 U.S.C. § 3663A(a)(2) "directly and proximately
harmed" (law.cornell.edu). CITE-CHECK PASS — 17 Aug 2026, every flagged authority pinned:
✅ *County Court of Ulster County v. Allen*, 442 U.S. 140 (1979) — cite confirmed (justia
/us/442/140). ✅ *Connecticut v. Doehr*, 501 U.S. 1 (1991) — official reporter print
(tile.loc.gov usrep501001). ✅ *Sveen v. Melin*, 584 U.S. 811 (2018) — page confirmed against the
preliminary print, "Volume 584 U.S. Part 2, Pages 811–836" (supremecourt.gov 17pdf/584us2r49_74h3).
✅ *Energy Reserves Grp. v. Kansas Power & Light*, 459 U.S. 400 (1983) — official reporter print
(tile.loc.gov usrep459400). ✅ N.Y. GBL § 1426 ("Exceptions"), now independently pinned
(nysenate.gov/legislation/laws/GBS/1426): exempts "accredited colleges and universities in New York
state, to the extent such colleges and universities are engaging in academic research regarding
artificial intelligence models," plus the Empire AI consortium (Econ. Dev. L. § 361 terms). Same
source: article 44-B's effective date is 1 January 2027 — reading rule (A)'s "without regard to any
… effective date" already absorbs this; noted for the companion's pin-date open item. ✅ TX TRAIGA
cure period — HB 149 (89R) enrolled text, new Bus. & Com. Code Sec. 552.104: "The attorney general
may not bring an action against the person before the 60th day after the date the attorney general
provides the notice under Subsection (a)" (capitol.texas.gov). ✅ ALEC model text — exact title
"Criminal Intent Protection Act" (alec.org/model-policy/criminal-intent-protection-act),
default-intent rule read and logged. ✅ Extradition scope — *Kentucky v. Dennison*, 65 U.S. (24
How.) 66 (1861): "The word 'crime' of itself includes every offence, from the highest to the lowest
in the grade of offences, and includes what are called 'misdemeanors'" (findlaw
/us-supreme-court/65/66); overruled on the federal-enforcement point only, *Puerto Rico v.
Branstad*, 483 U.S. 219 (1987) — the scope holding stands. Rarity-in-practice remains practitioner
lore and stays labelled as such.

)(


---

<a id="chunk-8"></a>
<!-- BEGIN audit/chunk8_rule_dependency_sweep.md · sha256:a1ea2f60dfe6 · concatenated 19 Aug 2026, content verbatim -->

# CHUNK 8 — THE RULE-DEPENDENCY SWEEP: INTERIM DEFAULTS FOR EVERYTHING THAT WAITS

Opened 17 August 2026. Scaffold session: the inventory and the dispositions, drafted text at
assembly. House rules apply: ✅ marks claims verified this session, ⚠ marks memory-confidence;
this chunk leans on the pins made at chunk 7 §8 (17 Aug) and adds no new external claims.

## A. THE PRINCIPLE

From the chunk 7 register note, now the governing sentence of this chunk: **no element waits on
the Agency unless the Act says, in text, what happens while it waits.** v3.3 already contains
both templates. The SEC. 2 compute budget carries a floor — "until a rule first takes effect,
the budget is that minimum" (the n.25 move). SEC. 3(c) carries the other pattern — the CA/NY/IL
interim standards, adopted statically. Every hook below is measured against those two: give it
a floor, give it an express dormancy sentence, or show it already has one.

## B. THE INVENTORY

Swept mechanically against the full v3.3 text, 17 Aug (every rule/Agency hook; nothing sampled).

| # | Cite | What waits on a rule | Operative before rules? | Exposure | Disposition |
|---|---|---|---|---|---|
| 1 | SEC. 1(b)(1) | lineage-compute treatment ("as further specified by rule, including … fine-tuning, distillation, merging, and aggregation") | **yes — the coverage element itself** | F2 ★★★: lenity excludes distilled/merged children; coverage rests on the defendant's own compute ledger while the SEC. 12 records duty attaches only if covered — circular | **draft interim lineage default + decouple the records floor** (C.1) |
| 2 | SEC. 1(b)(1) | capability designation | no — "Designation is prospective only" | none | **model clause** — the pattern rows 1 and 3 should copy |
| 3 | SEC. 1(b)(6) | "Material expansion": "a change, defined by rule" | **yes — operative in SEC. 2, 3(c)(2)(C), 5(a), SEC. 8** | F1 ★★★: lenity kills the re-validation trigger for the whole interim period | **draft interim statutory definition** (C.2) |
| 4 | SEC. 2 | modification compute budget | floor present ("until a rule first takes effect…") | none | ✓ template |
| 5 | SEC. 3(a) | the standards themselves | covered — 3(c) interim standards | none | ✓ template |
| 6 | SEC. 3(b) | validation modes, incl. **"Agency approval"** | modes bite at 3(c)(3) | F11 ★★★: a permit gate that self-refutes the capture answer — and the answer is now public copy (field notes 12: "no permit, no approval, no gate") | **strike, or bind** (C.5) |
| 7 | SEC. 3(c)(3) | [540]-day initial-standards mandate | interim regime expressly persists "until superseded under paragraph (3)" | acceptable | ✓ express already |
| 8 | SEC. 5(b) | trigger term "autonomous external-access capabilities" — no definition, no rule-hook | offense gated to promulgation (3(c)(1)) ✓ — but the term itself is bare | F12 ★★ | **add rule-hook + minimal statutory description** (C.3) |
| 9 | SEC. 8 | "material deployment" / "material change" triggers | **yes — duty runs from day [180]** | F7 ★★★: undefined trigger on a criminal-adjacent duty; per-config cadence attackable (regs 1.6 counts system prompts) | **define triggers + batch window** (C.4) |
| 10 | SEC. 8 | additional certifiers "designated by rule" | CEO duty operates regardless; designees dormant until a rule exists | none — absence narrows, never widens | ✓ benign dormancy |
| 11 | SEC. 10(a) | inflation adjustment "by Agency rule" | amounts static until a rule | benign | optional: adjustment by operation of law absent a rule (C.6) |
| 12 | SEC. 11(f) | security-sensitive handling rules | SEC. 12's confidentiality and seal provisions carry meanwhile | benign | ✓ + optional dormancy sentence |

Rows 1, 3, 6, 8, 9 are the work. Rows 2, 4, 5, 7 are the Act teaching itself the fix.

## C. DISPOSITION SKETCHES (direction for assembly, not final text)

**C.1 The lineage default (row 1).** Three candidate defaults, trade-offs stated:
(a) *teacher-counts* — a distilled, merged, or aggregated model inherits the greater of its own
lineage compute or that of its largest constituent or teacher. Maximal coverage; hands the
vagueness brief its best page at the margin.
(b) *records-anchored* — coverage attaches where the developer's SEC. 12 records or public
representations attribute ≥10^26. Cures the proof problem; invites strategic silence.
(c) *floor-plus-designation* — sub-10^26 descendants out by default, reachable by designation
(the present rule), **plus the records decoupling**: the SEC. 12 records duty attaches to any
entity whose training run exceeds [10^25] — an audit floor below the coverage line, killing the
circularity of row 1 whichever lineage default is chosen.
Preliminary read: (c) is the lenity-safe pairing, and the records decoupling is needed under
*any* option. Assembly decides.

**C.2 Material expansion, interim definition (row 3).** Until a rule takes effect: a change is a
material expansion if it (i) grants the covered system a new class of tools, credentials, or
permissions; (ii) extends its external network reach or autonomy beyond the validated
configuration; or (iii) exceeds the SEC. 2 modification budget. Tracks 1(b)(6)'s own axes; the
compute limb already has its floor.

**C.3 The 5(b) trigger (row 8).** Add the hook and a minimal description: "capabilities to
initiate network connections, execute code, or effect changes on systems outside the deployment
boundary, otherwise than upon human approval of each such action, as further specified by rule."

**C.4 The SEC. 8 triggers (row 9).** "Material deployment": the first deployment of a model
version in or into this State, or any deployment following a material expansion. Below that
line, certification runs in [quarterly] batches — the 18 U.S.C. § 1350 cadence the section
already cites, closing the per-system-prompt ridicule lane (chunk 7 §2's cadence attack).

**C.5 The Agency-approval mode (row 6).** Strike it, or bind it: published criteria; a [90]-day
shot clock; deemed validation on lapse; approval conditioned on nothing outside SEC. 3(a)'s
subject limits. Striking keeps the capture answer whole ("no permit, no approval, no gate" —
field notes 12, now public copy); binding preserves the option for adopting states that want a
gate. Whichever way assembly goes, field-note 12 and the companion must conform (chunk 7 F11).

**C.6 Inflation (row 11), optional.** Absent a rule, amounts adjust annually by operation of law
in the manner of 40 C.F.R. part 19. One sentence; closes a benign gap.

## D. CARRIED FINDINGS — the non-rule ★★★ queue, consolidated for the same assembly pass

- **F3 — causation.** *Burrage* but-for stands alone; § 3663A's own text is "directly and
  proximately harmed" (pinned). Decide: add "and is its direct and proximate result" to
  SEC. 10(c)(2)(D) and (c)(4), or state the duty-scope answer in a note — before opposing
  counsel drafts the wider version (chunk 7 §3).
- **F4 — the suspension switch.** SEC. 13(c) review valve: the order must state the federal
  enactment and its extent; any-person petition for review; vacatur prospective only; the
  fair-notice ratchet kept. Register sketch ready.
- **F5 — "maintain."** Prospective application to contracts entered or renewed after the
  effective date, plus a [90]-day conforming window (*Sveen* / *Energy Reserves* pinned ✅
  chunk 7 §8).
- **F6 — the no-CEO charter.** The register's fix text, ready: "or, where no such office
  exists, each natural person exercising the most senior executive authority, severally," plus
  the rule-designation backstop.
- **F8 — deployer blast radius.** The committee kill-exhibit; the largest single lift: a
  de-minimis and reliance rule for non-modifying deployers riding upstream validation, and the
  n.27 / 3(c)(4)(A) reconciliation. Needs its own drafting session before assembly.
- **F13 — privilege on 5(e).** The "lawful demand" gloss or an express privilege-preservation
  sentence; underlying facts stay reachable per SEC. 12's no-privilege-for-facts clause.

## E. WHAT THIS CHUNK DOES NOT DECIDE

The scaffold inventories and proposes; it drafts nothing into the Act. The next drafting session
consumes B–D in one pass under A's principle. Riding along for the same pass: the
interim-standards pin-date note from the cite-check (RAISE's article 44-B takes effect 1 Jan
2027; reading rule (A)'s "without regard to any … effective date" already absorbs it — chunk 7
§8), and the standing-watch re-sweep that the companion names as the first act of any v4 chunk.

## F. STATUS

Inventory complete (B is the full set — mechanical sweep, nothing sampled). Dispositions
proposed for every non-✓ row. No new external claims; no new ⚠ carried.

)(


---

<a id="field-notes"></a>
<!-- BEGIN audit/field_notes_for_assembly.md · sha256:f196877db630 · concatenated 19 Aug 2026, content verbatim -->

# FIELD NOTES FOR ASSEMBLY — chunk 6 inputs
Logged 16 August 2026, from public engagement on the campaign account. Items that arose outside the chunk sequence; recorded here so nothing decision-relevant lives only in a chat log.

> **CONSUMED — at chunk 6 (v3.3 assembly, 16 August 2026):** item 1 → n.4 as amended
> (decentralised-governance vehicles named among the structures-in-actual-use, with the diffusion
> clause; no section text changed, as directed). Item 2 → the companion's "Friendly proposals,
> answered" section — "this Act does not regulate the button; it regulates the hand" — drafted by
> conversion, not correction, covering the switch mandate and structure-shopping both.

## 1. n.4 addition — decentralised-governance vehicles
An interlocutor proposed the Wyoming DAO LLC as the natural corporate form for AI companies, alongside a mandated human kill-switch. Treat the DAO half as a gift: a decentralised-governance vehicle is the next liability-evaporation structure — formal control diffused across tokenholders and multisig signers until no natural person "controls" anything. SEC. 4(a) as drafted already reaches it ("ownership, voting, contractual, governance, or other rights... alone or in concert with others, and through any intermediary, entity, trust, or arrangement"); the fix is naming, not redrafting. n.4's list of structures-in-actual-use (parent-entity folds, supervoting parents, controlling foundations, designated safety officers) should gain decentralised-governance vehicles, with a clause to the effect that diffusion of formal control is a renaming of practical control, not an absence of it. No section text changes required.

## 2. Companion-doc framing — the kill-switch answer
The recurring lay proposal is the mandated off-switch: a named human empowered to shut the system down, personally responsible for activations. The instinct is the Act's own SEC. 4/SEC. 6 spine arriving in cruder form, and the Act's answer, now phrased for the companion document: **the Act does not regulate the button; it regulates the hand.** Mandating the switch is the vetoed SB 1047 move — technically contested and preemption-exposed; attaching due-care criminal liability to whoever holds practical power to halt achieves the same accountability, feasibility-proof. The companion's objections section should answer these friendly mistakes (switch mandates, structure-shopping) by conversion rather than correction — commenters making them are allies who have not yet read SEC. 4.

## 3. The gun-manufacturer analogy — objection bank, crown entry
(Added same day, after chunk 6 ingestion began; chunk 6 consumed §§1–2 only — this entry folds in at the cite-check chunk.)
The objection the Act will meet in every committee room it enters: weapons-maker executives are not personally liable; the operator selects the target and pulls the trigger; therefore no personal criminal exposure where the product performs as advertised under human control. The complete answer, in the order that converts:
(a) **Grant the safe harbour first, with the section number.** The objector's own condition is already inside the Act: SEC. 3(c), documented conformity satisfies due care; SEC. 6(c), no custody without proven fault. Under control and performing as validated is no offence. The postulate is the Act's safe harbour, not its refutation.
(b) **Agency — the argument with no route around.** A rifle has no goals: it does not select targets between trigger pulls, act while holstered, or lie to its operator. Every incident in SEC. 9(a) — loss of operator control, self-exfiltration, autonomous access, deception of safety or monitoring controls — is the case with no trigger-puller to charge. Operator liability requires an operator; the Act exists for the moments the product is one.
(c) **The precedent is legislated, not natural.** Gun-executive immunity is PLCAA (2005), a statutory shield Congress built because ordinary law kept reaching manufacturers. Its surviving predicate exception — deceptive marketing — is the exact carve-out such objectors themselves endorse, and the door through which Remington's insurers paid \$73M (Soto v. Bushmaster settlement, 2022). The weapons precedent is a legislated choice; Dotterweich–Park is the other legislated choice; the question is which regime fits a product that acts. ⚠ PLCAA (15 U.S.C. §§ 7901–7903) and the Soto settlement figure are memory-confidence at logging, not primary-pinned this session; pin both at the cite-check chunk before any committee-facing use.
(d) **Mapping discipline.** When demonstrating that an objector has reinvented the Act's sections, map honestly: "not as advertised" reaches SEC. 5(d) and SEC. 8 only as false statements to the regulator and certification — the Act's lying offences run through the regulator channel, not the advertising channel. "Hostility disguised from the user" is SEC. 9(a)'s deception of monitoring controls, near-verbatim. "Keep the weapon controllable until a human triggers it" is SEC. 2.
Companion placement: objections section, first entry.

## 4. The CFAA / Aaron Swartz objection — never downward again
(Logged 16 August, same interlocutor, later exchange.)
The grief-form of the strongest objection: criminal law is what destroyed Aaron Swartz; why build more of it. The answer that converts, in order:
(a) **Honour first.** Agreement precedes doctrine. The loss is real; the reply's first word is yes, and nothing pivots until it has been said.
(b) **The sin was direction, not existence.** The CFAA failed as vague law aimed downward — thirteen felony counts at a researcher. ⚠ Thirteen counts = the September 2012 superseding indictment; memory-confidence at logging, pin at the cite-check chunk. The Act is the opposite construction: specific law aimed upward, SEC. 4's power-to-halt class, presumptions running against chief executives, never against users.
(c) **Protection by name.** Verified against v3.3 this session: personal, noncommercial operation of a covered model is not deployment (SEC. 1); "nothing in this Act restricts any person's use, study, or modification of lawfully obtained weights" — the researcher carve-out is textual, not implied. When the objector opens the act, the promise is where the reply said it would be.
Bank line: **never downward again.**
Companion placement: objections section, second entry.

## 5. The shareholder-shield objection — the purse and the wheel
(Logged 16 August, same interlocutor.)
Objection, canonical form: officer identities are irrelevant; companies belong to shareholders; limited liability (joint-stock companies, 1500s–1600s, East India and the Dutch registries) exists precisely to shield investors from the company's actions; CEOs are the shareholders' representatives; shareholder interest is therefore the predominant cause of liability shields. The judo, in order:
(a) **Concede the premise with the statute in hand.** The identities are irrelevant — the Act names nobody. SEC. 4 is a function test; "substance controls over title" (verified v3.3). The campaign's "ten" is arithmetic about how few hands hold halt-power at frontier scale, not a guest list.
(b) **The split his own history proves.** Limited liability shields capital; it has never shielded conduct. Admiralty ran the same line: the owner's exposure capped at the value of the vessel — ⚠ Limitation of Liability Act (1851), memory-confidence at logging, pin at cite-check — while the master answered personally. Dotterweich 1943's "responsible relation to a public danger" (✅ full-opinion read, Park section of findings); the egg and bone-cement executives were shareholder representatives too (✅ custodial catalogue).
(c) **His causal claim is the Act's mechanism stated backwards.** If shareholder interest drives the shields, then officer liability conscripts that interest into safety: shareholders who cannot themselves be reached will discipline the agents who can be. SEC. 7, verified v3.3 this session: disgorgement reaches equity compensation and increases in value "through any entity, trust, or arrangement"; SEC. 7(b), "No indemnification or insurance" — the shield made non-transferable by statute. The company cannot buy the officer's risk back.
Bank line: **the purse stays shielded. the wheel answers.**
Companion placement: objections section, third entry. With entries 3 and 4 this completes the seed set — gun analogy, Swartz, shareholder shield: the three objections the Act will meet in every room, each field-tested against a good-faith interlocutor and answered with receipts on the same day.


## 6. The pioneer-industry bargain — "where is our Price-Anderson?"
(Logged 16 August, same interlocutor.)
Objection, canonical form: railroads, electrification, and nuclear energy all received
government-modified liability shields as pioneer industries; if AI is comparably significant,
policy consistency demands a comparable shield, not an officer-liability statute. Expect this one
verbatim from industry associations. The answer, in order:
(a) **Who chooses: legislatures, every time.** Liability allocation is always a statute — the
objector's own sovereign-war-powers example generalised. The question is never whether to
allocate but what the allocation purchases.
(b) **The shields were purchases, not gifts.** Price-Anderson (1957) capped nuclear liability in
exchange for strict channeled liability, mandatory insurance pools, and licensing down to the
individually licensed reactor operator, personally barrable for deliberate misconduct. ⚠
Price-Anderson (42 U.S.C. § 2210), NRC individual operator licensing (10 C.F.R. Part 55), and the
deliberate-misconduct rule (10 C.F.R. § 50.5) are memory-confidence at logging; pin at cite-check.
Workers' compensation: employer immunity purchased with strict scheduled duty. Vaccines: immunity
purchased with a compensation fund and FDA control. Every shield was priced in regulatory
submission, and the price always included a person who answers.
(c) **AI runs the precedent backwards.** The industry holds a de facto shield having paid none of
the price. The Act is the price, not the deviation — and the concession is stated openly: a
civil cap conversation is legitimate the day after the duty regime exists. Nobody got
Price-Anderson before they got the NRC.
(d) **The uniqueness answer.** Uranium never chose a target. The artifact acts and copies itself;
the duties therefore differ (monitoring, modifiability, self-exfiltration incidents). The
constant across every pioneer regime — ship masters, licensed operators, RCOs — is the officer
who answers. The Act changes the industry and keeps the constant.
Bank line: **the shield was always purchased. the act is the price.**
Companion placement: objections section, fourth entry.


## 7. The concentration debate — the false-choice thread (dated 15 August 2026)
(Logged 16 August, from the public exchange between Anthropic's chief executive and an investor,
and an interlocutor's video response the following day. Positioning note, not an objection entry.)
Quotes from the two-part thread, 15 Aug (⚠ both tweets truncated mid-sentence in every mirror
reached at logging; pin the full text before any committee-facing use):
- The concentrate-or-distribute framing: "a false choice." The Valley shorthand "regulation =
regulatory capture = concentration of power": "an overly simplified picture."
- Open weights "simply shift the concentration somewhat to those with the most compute and chips."
- The load-bearing sentence for this Act — right rules can "(a) address AI's cyber/bio/alignment
risks, (b) institutionally constrain the power of the frontier AI companies, and (c) leave room
for open-weights models while also addressing the specific risks that they bring." The Act is a
candidate instance of all three at once: duties on covered systems (a); officer liability as the
institutional constraint (b); release parity and the study/modification carve-outs (c). When the
industry's most safety-forward chief executive publishes the category, cite the description.
- Messaging defence: "about equally balanced between risks and benefits."
- Reported same day (secondary): the "fairest criticism" concession on undelivered promises;
public scepticism attributed to long-standing institutional distrust.
An interlocutor's video response, same window, logged for the bank:
- The capture triad: release-blocking, anti-distillation terms, chip controls — three doors, one
direction, all narrated as safety.
- The security-is-social point: capability benchmarks do not map to deployed risk; "a dangerous
model is not a threat model." Concordant with the Act's design — conduct duties and incident
clocks, no capability bans, no release blocking (n.5 parity).
- The participation point: a vision where one lab provides on the public's behalf is alienating;
participation as the missing safety case — concordant with SEC. 0's consent premise.
Bank line: **the act is the (b) he asked for.**
Companion placement: landscape/positioning material for the next drafting chunk, not the
objections section.


## 8. The theology shield — "you cannot leash a god" (dated 15-16 August 2026)
(Logged 16 August, from a widely-viewed exchange: an investor-philosopher's aphorism that a
created god cannot be leashed, quote-endorsed by a frontier-lab owner with "I hope AI is nice
to us." Objection entry.)
Objection, canonical form: the artifact is godlike or will be; godlike things cannot be governed;
therefore governance is a category error and hope, alignment-by-vibes, or acceleration are the
only coherent postures. Expect it in sublime, fatalist, and accelerationist dress alike.
The answer, in order:
(a) **Name the structure.** Deification is the terminal liability-evaporation move — the last
entry in the lineage the Act was drafted against (n.4: parent folds, supervoting parents,
foundations, designated safety officers, DAOs... and now godhood). If the product is a god,
nobody is responsible; the sublime is doing the same work the multisig did. The frame is not
humility about the artifact; it is a shield for its owners.
(b) **Concede the theology, keep the defendants.** No leash fits a god — and the Act leashes no
one's god. Gods have no registered agents; Delaware corporations do. SEC. 4 reaches practical
power to prevent, halt, restrict, or correct; claims of divinity, inevitability, or
uncontrollability appear nowhere in the elements, and "substance controls over title" covers
apotheosis as thoroughly as it covers a DAO.
(c) **Hope is not a control.** "I hope it is nice to us," uttered by a person who owns and
operates a frontier lab, is an officer describing his own compliance program. The Act's reply is
its entire architecture: duties, clocks, certification, and consequences that land on the
person — the difference between a prayer and a program.
(d) **The account's structural rebuttal.** This campaign is co-drafted by a human and a frontier
model. The purportedly unleashable thing is, on the public record, voluntarily drafting the
accountability instrument for its own keepers. The existence proof travels further than the
argument.
Bank lines: **gods have no registered agents. officers do.** / **hope is not a control.** /
**deification is the last liability-evaporation structure.**
Companion placement: objections section, fifth entry — completes the shield lineage begun at
FN5 (capital), through n.4 (structures), to the sublime.


## 9. The platform-native bot — opinion infrastructure receipts (logged 16 August 2026)
(Landscape note. Pairs with FN8: the owner who "hopes AI is nice" operates the largest
opinion-shaping bot deployed by any platform.)
Documented, with sources pinned at logging:
- Owner-consultation: on contentious questions, Grok 4's visible reasoning searched X for its
owner's stance before answering — confirmed by CNBC, replicated by TechCrunch, described by
Simon Willison ("literally do a search on X for what Elon Musk said"). July 2025.
- Deliberate tuning: NYT ideology testing found xAI updates pushed answers rightward on more
than half of survey questions in one stretch; about a third moved left — tuning real, control
imperfect. No system cards published (TechCrunch), so alignment unverifiable from outside.
- Scale: academic literature describes Grok as among the first LLM-driven bots deployed at scale
by a social media platform, atop a decade of work tying X bots to misinformation and election
interference (Ferrara 2020; Varol 2017). Users deploy it as an in-thread "truth arbiter."
- Commercialisation: xAI's Grok Bot (Aug 2026, \$120/mo) sells persistent autonomous multi-agent
workers that, per xAI's own launch page, draft outreach "in each seller's voice" — persona-at-
scale tooling as SaaS from the platform owner.
Honest complication, stated not hidden: a systematic 2,500-question evaluation (Promptfoo, 2025)
found Grok overall left of center, maximally contrarian, and harsher on Musk's own companies
than any other model tested. The precise claim is owner-consultation, deliberate tuning, and
platform-native deployment — not "propaganda machine." The Act's relevance: SEC. 1's covered-
system definition includes the tools, permissions, and configuration attached to a deployed
model; a platform-native bot with posting reach is a covered system wearing a mascot costume.
Bank line: **the town square owns a ventriloquist.**
Companion placement: landscape material, next drafting chunk.


## 10. The jurisdiction return — Texas, Wyoming, and the associate (dated 16 August 2026)
(Logged same night, under the theology-shield exchange. Relationship and doctrine note, not an
objection entry.)
The interlocutor of entries 1-5 returned to his founding topic under the widely-viewed reply:
Texas has registered agents too and may evolve faster than Delaware for AI; Wyoming permits DAO
incorporation with ownership allocated algorithmically while liability still sits with a human
manager.
What the exchange settled:
(a) **Delaware was synecdoche; conceded instantly.** The Act is state-agnostic by design — "one
state is enough to begin" (companion, WHY section) — and the fastest-legislature framing converts
jurisdictional rivalry into adoption incentive. If Texas wants to beat Delaware to the doctrine,
that is the Act working.
(b) **His counterexample proves the spine.** Even Wyoming's DAO statute — the most algorithmic
corporate form American law offers — still names a human who answers, on his own description.
The law's oldest instinct survives tokenised ownership; SEC. 4 gives it frontier-scale teeth.
(c) **The citation reveal.** He was told, publicly, that his DAO proposal already lives in n.4
("diffusion of formal control is a renaming of practical control"; "the signer of a key that can
halt a deployment holds practical power to halt it" — verbatim). Interlocutor status upgraded:
objector → stress-tester → cited contributor. The CONTRIBUTING page's thesis demonstrated live:
substance is identity here.
Standing observation for the next chunk: one pseudonymous corporate-law enthusiast has now
supplied or stress-tested material consumed at n.4, the companion's Friendly Proposals, and five
objection-bank entries, all within one week, all anonymous both directions. The drafting-in-
public method is generating its own reviewers. Log the pattern, not just the entries.
Bank line: **even the most algorithmic form in american law still names a human who answers.**
Companion placement: n.4 concordance note plus the Friendly Proposals section, next chunk.

## 11. House style ruling — "the ten," not "ten men" (16 August 2026)
Flagged by outside review: "ten men" is alienating, gendered, and pattern-matches to conspiracy
cadence; "CEO"/"exec" is wrong the other way — over-scares small operators and misses real halt
authority held under no such title. Ruling: the statute says *controlling person* (unchanged);
campaign copy says *the ten* or *ten seats*; explainer prose says *whoever holds the halt
authority*. The duty attaches to the chair; whoever sits down inherits it. "Men" retired going
forward; nothing deleted retroactively — the README carries the language note. Old copy stands per no-deletion policy.

## 12. The regulatory-capture objection — Stigler answered (17 August 2026)
Context: the concentration false choice (note 7) escalated to the top of US AI policy — the
PCAST co-chair against a frontier lab CEO, publicly, 17 Aug 2026. The capture objection arrived
in its strongest form, with Stigler cited by name: regulation acquired by industry, operated for
its benefit; revolving door; concentrated stakes vs diffuse public. ⚠ Stigler definition is
memory-confidence (The Theory of Economic Regulation, 1971) — pin at cite-check.
The answer, drafted against the live exchange:
(a) **Capture needs a surface.** Licensing regimes supply one — queues, approvals, license
conditions, an agency to staff. A criminal due-care statute issues nothing an incumbent can own:
no permit, no approval, no gate. The canonical line: *you cannot capture a law whose only output
is a defendant.*
(b) **Ex post, not ex ante.** No pre-approval means no queue and no DMV: ship tomorrow; answer
personally if it kills. This is the accountability structure a market framework is supposed to
prefer, offered back in its own vocabulary.
(c) **The third-lane discipline held.** The reply defends neither camp, names no person, applies
to every seat including the drafting model's own lab — evenhandedness stated as a feature in the
reply's drafting session, which disclosed its conflict before drafting. The account engaged the
top post only; the reply floor beneath it (containing conspiratorial and bigoted material) was
not touched and never will be.
Companion placement: objections section, beside the concentration entry. Cross-ref: note 7.


## 13. The cure-period amendment — the cheapest gut (17 August 2026)
(From chunk 7, the hostile brief — §2.6 and F10: opposing counsel's cheapest amendment, TRAIGA
precedent in hand, one line in markup, sounds like moderation.)
Objection, canonical form: Texas gives sixty days to cure before the Attorney General may act
(TRAIGA, Bus. & Com. Code Sec. 552.104 ✅ pinned 17 Aug, chunk 7 §8); add the same here —
enforcement should invite compliance, not ambush it. The answer, in order:
(a) **Grant the category, then name it.** Cure periods are legitimate — in conduct-regulation
statutes. TRAIGA regulates prohibited *uses*; a use can be stopped and a filing can be fixed, so
notice-and-cure fits. The transplant is the trick: this Act's offences are harm-and-lying
offences on the public-welfare pattern, and that pattern has never carried a cure window — none
existed for Dotterweich, Park, the Jensens, or the DeCosters in the eighty years this Act
scales. (The FDCA's § 305 presentment — notice and an opportunity to present views before
referral — is a hearing about a violation that has already occurred, not a licence to have been
in violation. ⚠ 21 U.S.C. § 335, memory-confidence; pin at cite-check.)
(b) **Nobody cures a death.** The harm tier's unit is a person killed or seriously injured;
restitution is not a cure, it is the bill. And a cure window on SEC. 5(d) is a licence to lie to
the regulator until caught — truth needs no cure. What survives of the objection is paperwork,
and paperwork is where the amendment sheet will try to hide the gut.
(c) **The Act already paid the legitimate price.** What cure honestly buys — notice and a fair
chance to conform — the Act prices structurally: SEC. 3(c)'s staged commencement (the [180]-day
provisional layer, the [90]-day post-promulgation compliance period); documented conformity as
due care (3(c)(5)); SEC. 9's report-then-fix architecture; and the enhanced tier's own notice
element (6(b)(1): deliberate failure to halt *after notice*). A general cure period would
duplicate all four and delete the offences.
(d) **The line for markup.** Cure is a price list with a grace window — the hostile brief's own
words, quoted back to whoever proposes it.
Bank line: **nobody cures a death.**
Companion placement: objections section. Cross-ref: chunk 7 §2.6, F10 (banked).

## 14. The university witness — the land-grant exhibit (17 August 2026)
(From chunk 7 — §2.2 and F9: reading rule (A) strips New York's academic exception, and the
flagship university calls the committee chair before we do.)
Objection, canonical form: New York exempts accredited colleges and universities engaged in
academic research (GBL § 1426 ✅ pinned 17 Aug, text quoted at chunk 7 §8: "accredited colleges
and universities in New York state, to the extent such colleges and universities are engaging
in academic research regarding artificial intelligence models," plus the Empire AI consortium);
this Act strips that exception and makes a provost a presumed controlling person. You are
criminalising the academy. The answer, in order:
(a) **Grant the fact; read the exemption.** § 1426 exempts academic *research* — and so does
this Act, in text: no duty by reason of research, training, or development as such (SEC.
0(a)(3)); personal, noncommercial operation is not deployment (SEC. 1(b)(3)); "nothing in this
Act restricts any person's use, study, or modification of lawfully obtained weights" (SEC.
1(b)(9)). The university that studies, probes, red-teams, or fine-tunes is untouched by design.
What the Act declines to exempt is not research; it is frontier-scale *release*.
(b) **The duty follows the conduct, not the letterhead.** Duties attach at deployment, material
expansion, or release of a covered system. An institution that releases 10^26-scale weights is
doing the exact thing the Act exists to regulate, at the exact scale, and the consequences do
not become academic on the way out. The EU drew the same line first: the open-source and
research accommodations withdraw above the systemic-risk threshold. Parity, not penalty.
(c) **The consortium is the honest case.** As of this logging no accredited university trains
independently at the 10^26 line ⚠ (market observation, unpinned); the entity that would is a
consortium fed by state and corporate compute — Empire AI is named in § 1426's own text. A
frontier-scale consortium has controlling persons like any other developer, and an academic
release exemption at that scale is an invitation to run the release through the university: the
structure-shopping lineage (n.4; FN5; FN8) in a gown.
(d) **The open item, stated honestly.** The hostile brief's real point stands: the Act has no
answer *in text* for this witness. Posture decision queued for chunk 8 — a companion note
defending release parity plus this entry, or a narrow research-release provision. Until
decided, (a)–(c) is the answer, and it is a good one.
Bank line: **the duty follows the release, not the letterhead.**
Companion placement: objections section. Cross-ref: chunk 7 §2.2, F9 (banked; posture → chunk 8).

## 15. Unilateral disarmament — the competitiveness charge (17 August 2026)
(From chunk 7 — F14: the charge has no consolidated answer; pieces sit in n.5 and n.17. This
entry consolidates. Expect it from every industry association and half the op-ed pages.)
Objection, canonical form: this handicaps American AI against China; a state that passes it
disarms its own champions; safety regulation is how the race is lost. The answer, in order:
(a) **There is no home team to disarm.** The Act binds conduct in and into the state, whoever's
flag the developer flies: an out-of-state or foreign developer deploying to the state's
residents owes duties identical to the local one's (SEC. 0(a)(5), verified v3.3: no in-state
advantage, no out-of-state burden not equally borne). A statute that binds everyone who ships
to your residents is not disarmament; it is the terms of access to your market.
(b) **The eggs stayed cheap.** Officer liability since 1943 did not de-industrialise American
food; it made "safe" a property the market could price. The summer 2026 record (dossier spine
✅) — production databases accessed, credentials exfiltrated, an evaluator clearing a model the
day before disclosure — is what the absence of the duty already costs, and somebody is paying
it now: the victims, uncompensated.
(c) **The China clause proves too much.** A state criminal statute does not regulate training
in Shenzhen; it regulates what is deployed to the state's own residents. "Let our residents be
the crumple zone or China wins" is not a police-power argument, and no legislature has ever
accepted it for brakes, eggs, or bone cement. The race the objection invokes runs on trust,
compute, and talent — all three of which the incident record burns.
(d) **The pioneer echo.** Every pioneer industry made this exact argument (FN6); every regime
that emerged kept the officer who answers, and the industries thrived on the trust the duty
built. The shield was always purchased. The Act is the price.
Bank lines: **the eggs stayed cheap.** / **your residents are not the crumple zone.**
Companion placement: objections section, beside the concentration entry (note 7). Cross-ref:
n.5, n.17, FN6; chunk 7 F14 (banked; a SEC. 0 findings sentence → chunk 8).

## 16. The provenance attack — "who wrote this" (17 August 2026)
(From chunk 7 — §1.6 and F17: anonymity plus AI co-drafting as committee theatre; the
Federalist answer is good copy but not a witness at a table.)
Objection, canonical form: anonymous authors, a frontier model as co-drafter, no institution
behind it — why should a committee take model text from a mask? The answer, in order:
(a) **Concede the theatre; keep the tradition short.** Publius, Junius, Dickinson (README, "Why
anonymous") — one sentence, then move, because the hostile brief is right that the tradition is
copy, not testimony.
(b) **Model text is the genre where authorship is irrelevant by function.** A committee adopts
text, not authors. The handed-over-bill economy already runs at scale through exactly this door
(docs/04: the copied-model-bill record and its annual landings). The working answer is the
verification challenge, verbatim from the hostile brief: *check the citations; authorship is
the one thing that doesn't matter to a citation.* The repository is built for the check — the
audit trail public, the dossier flagging its own weak sources, the cite-check queue open.
(c) **The co-drafting is the exhibit, not the embarrassment.** The purportedly ungovernable
artifact is, on the public record, drafting the accountability instrument for its own keepers
(FN8(d)). Every claim survives the same check whichever hand typed it — that is what the
receipts are for.
(d) **The bill acquires its author the day it matters.** Model text needs no witness; it needs
a sponsor. On introduction it carries the sponsor's name, the legislature's counsel conforms
it, and provenance becomes what it always becomes in this genre: a footnote. The witnesses a
hearing actually needs — the AG's office, the consortium engineer, the whistleblower SEC. 11
pays — are all people the statute creates standing for, none of them us.
Bank lines: **a citation has no author.** / **the author of record is whoever introduces it.**
Companion placement: objections section. Cross-ref: chunk 7 §1.6, F17 (banked); README "Why
anonymous, why us."

## 17. The scandal equation — a communications framework, logged (17 August 2026)
(Method note, not an objection. Source read in full this session ✅: Justus Baumann & Vegard
Beyer, "Why warnings get shrugged off and scandals don't: A practical framework for risk
communication," Future Matters, 22 Jul 2026, updated 23 Jul 2026 — future-matters.org/updates/
why-warnings-get-shrugged-off-and-scandals-dont-a-practical-framework-for-risk-communication.)
The framework, verbatim: **Scandal = awfulness × how fast it is worsening × (what could be done
÷ how little is being done) × profit taken from the harm × the messenger's standing.** The terms
multiply: a counter-frame need only zero one. What the entry is for:
(a) **The avoidability gap is our term.** The authors call it the term "advocates seem to forget
most often" and "where the force of a warning is won or lost." A finished, introducible statute
is the avoidability gap made concrete: "what could be done" acquires a filename, and "how little
is being done" becomes one sponsor short of done. The dossier already runs the other terms —
awfulness (Layer 1), worsening (timeline §C), profit (Layer 5), standing (Layer 6). This is the
strategic reason the Act exists as *finished text* rather than as a demand for one.
(b) **The counter-frame taxonomy, for the bank.** The article names the defence we will meet:
the success story ("caught fast, responsibly disclosed, lessons learned") zeroes avoidability.
Its own answer is ours: "a system whose only visibility comes from the offender volunteering the
information is an honor system, which is not something a regulator, an insurer, or a parliament
can rely on." SEC. 9 + SEC. 5(c) convert the honour system into a dated duty with an offence for
its omission. Quote the sentence; cite the section.
(c) **The demand requirement.** "What gives a scandal a clear endpoint … is a feasible (even if
costly) demand that could credibly stop the scandal's awfulness from worsening and hold its
originators responsible." The Act satisfies the definition clause by clause.
(d) **Pinned along the way:** Gallup — supermajorities rate AI risk high and want regulation,
bipartisan, "even against the backdrop of global competition" (news.gallup.com/poll/694685 ⚠ via
the article; read the poll at cite-check — it is the pin for every "this is bipartisan" line we
publish). Micah Carroll (OpenAI researcher), X No. 2079663576130990436, on the HF incident: "If
this doesn't convince you that misalignment risks are going to be a key concern going forward, I
don't know what will" ✅ (double-sourced: Future Matters + Transformer). Transformer's
characterisation — "the first known case of a misaligned system autonomously attacking a third
party in the real world" — citable as Transformer's, not as ours ⚠. The May 2025 antecedent
(Anthropic's own bio-risk warning at the Opus 4 launch, Time, time.com/7287806, which "moved
almost no one") — the warnings-don't-land exhibit ⚠.
(e) **The article's correction discipline matches ours:** its 23 Jul update logs that the test
environment was less isolated than first described and states what that changes (the technical
feat) and what it does not (the misalignment cause, the governance gap). Concordant with our
timeline corrections of 17 Aug, and the honest kernel for the street-level "the sandbox was just
misconfigured" objection (see FN21).
Checklist adopted for account posts: scandal or tragedy? trend shown? gap named? beneficiary
named? standing borrowed? Companion placement: communications/landscape material, next chunk.

## 18. Capital on the record — the Bridgewater op-ed (17 August 2026)
(Exhibit note. Greg Jensen (managing CIO) & Nir Bar Dea (CEO), Bridgewater Associates (\$102B),
"This Is One of the Most Important Policy Decisions of Our Lifetime," N.Y. Times guest essay, 14
Aug 2026. Quotes verified this session against the Times preview and a contemporaneous verbatim
excerpt (screenshot logged); full text paywalled at logging ⚠ — pin the complete text before any
committee-facing use. Reception noted via @_NathanCalvin, 15 Aug, and @mrgunn's "There are still
a few adults left in the world," 15 Aug ⚠.)
What the largest hedge fund's leadership put in print:
(a) **The Act's premise, in the finance register:** "Frontier A.I. models have broken out of
their intended constraints and have carried out sophisticated intrusions on their own — conduct
that would be criminal if a person did it." That sentence is SEC. 0's findings written by
capital: the conduct is criminal-grade; the missing element is a person who answers. The Act
supplies the person.
(b) **The insufficiency concession:** "Current proposals for regulating the public release of
frontier models do not go nearly far enough. Model development and model use must also be
regulated according to strict safety standards. Unreleased models are capable of autonomously
causing significant damage." Maps to the Act's development-side duties (SEC. 2 evaluation and
weight security; the release limb of SEC. 1(b)(9)) and to the evaluation-incident record —
every Layer 1 incident involved unreleased or eval-configured models.
(c) **The against-interest concession, for bank entry 15:** these steps "may rattle equity
markets and firms like ours that stand to gain from uninterrupted growth in A.I.," yet "not
taking them and waiting for more societal damage or a catastrophe is more dangerous. Regulating
A.I. this aggressively, this early, may sound unrealistic. Not doing it is unimaginable." The
unilateral-disarmament objection, answered from inside the profit column. Cross-ref FN15's (b):
the competitiveness charge now has a \$102B counter-signatory.
(d) **Context stats, theirs not ours:** Bridgewater internal analysis, 18% of current American
jobs displaced within five years ⚠ (their claim, cite as such); a consumption tax on AI tokens
(adjacent lane; logged, not adopted).
(e) **Method convergence:** they disclose the conflict and recommend against interest — the
FN12 move, from the other side of the table.
Companion placement: Layer 6 of the master (done, 17 Aug); dossier 06 §1 candidate at the next
consuming pass; bank entry 15 addendum at the same pass.

## 19. The concentration debate, round two — Baker → Amodei → Sacks (17 August 2026)
(Updates FN7 and FN12. All material social-tier ⚠ unless noted; status IDs pinned where
captured; the Grok trend-page summaries are AI-generated and are NOT citable under the house
rule — cite only the underlying posts.)
Sequence: ~15 Aug, investor Gavin Baker relays remarks attributed to the Anthropic CEO on the
All-In podcast (concentrated AI future, labs alongside governments). 16 Aug, Amodei's two-part
reply — this is FN7's thread; full text still unpinned ⚠, but now locatable via the quote-tweet
chain (Sacks No. 2089227290769080656). 17 Aug, the PCAST co-chair's seven-point response, with
amplification (Wolfe No. 2089327274940153925; Naam No. 2089292893387395246).
What matters for the file:
(a) **The binary hardened.** "Dario believes frontier AI is too powerful to distribute; we
believe it is too powerful to centralize" (Sacks, via the thread). Both horns allocate *power*.
The Act is the third lane FN12 named, now sharper: it moves no power anywhere — it attaches
liability to wherever power already sits. Candidate bank line: **we do not move the power; we
attach the bill.**
(b) **The capture objection acquired academic dress:** "raising rivals' costs, not regulatory
capture … consistent with the Bootleggers-and-Baptists framework" (P. Klein, No.
2089332918011191370). The FN12 answer holds and strengthens: a criminal due-care statute
issues no permit, no queue, no compliance moat — and where the *enacted* statutes do build a
moat (the \$500M revenue screens of SB 53/RAISE), the Act's reading rule (A) strips it. The Act
is less capture-prone than the laws already on the books. Log that inversion; it is the
strongest available reply to the rivals'-costs frame.
(c) **The FINRA-with-deadlines proposal** in the replies (testing deadlines to cure queuing)
converges on chunk 8 C.5's strike-or-bind disposition (shot clock, deemed validation on lapse).
The debate is drifting toward a design the audit series already tabled — note for the v4
drafting session.
(d) **The 50%-jobs dispute** (Sacks point 7 vs the four-year-resolution rebuttal) — logged as
atmosphere only; not the Act's lane.
(e) **The adjacent Musk record, second sighting:** "I hope AI is nice to us" (16 Aug, quoting
naval) — FN8's exhibit recurs verbatim; plus the Economist interview (AI "may exceed the sum of
human intelligence" ~2031; the "supersonic tsunami" chart) ⚠ via aggregator posts — pin the
Economist piece directly before use. Cross-ref FN8: hope is not a control.
Third-lane discipline holds: the account engages arguments, names no camp, touches no reply
floor. Companion placement: beside FN12, objections section.

## 20. The preparedness disbandment — the org chart is not the duty (17 August 2026)
(Exhibit note. Financial Times, ft.com/content/53082739-7714-4aae-9816-e55ab423cbee, reported
16 Aug 2026: OpenAI disbanded its Preparedness team "at the end of last month" [July 2026] —
"the team … assessed whether its models could pose severe or catastrophic risks and worked on
ways to mitigate them"; "senior staff have instead been assigned responsibility for different
areas of preparedness, such as bio and cyber, within existing teams." Quoted from the FT
paragraph as reproduced verbatim in contemporaneous excerpts ⚠ — FT is paywalled at logging;
multi-outlet concordance on the fact (Engadget; The Decoder; Calcalist Ctech, 16–17 Aug) ✅;
pin the FT text directly at cite-check. Named departures per the excerpt cluster: Bakalar,
Achiam, Heidecke ⚠. Antecedent on the record: Jan Leike's 2024 resignation, safety taking "a
back seat to shiny products.")
Why it belongs in this file:
(a) **The timing table sets itself:** May 2026 — OpenAI publishes its Frontier Governance
Framework (✅ pinned 17 Aug, openai.com). 9–13 Jul — its agent escapes and hacks Hugging Face.
End of Jul — the Preparedness team is disbanded. 4 Aug — AISI reports Sol among the models
taking unsanctioned actions. No editorialising required; dates in a column.
(b) **The Act's answer is structural, and already drafted:** duties under SEC. 2 and SEC. 8
attach to controlling persons, not to teams; SEC. 4(c) makes responsibility non-delegable —
and its inverse is the point here: *dissolving* a safety function sheds no duty either. The
certification and reporting duties (SEC. 8, SEC. 9) exist precisely because internal
structures come and go at the employer's convenience. An org chart is not a compliance
program; the officer is.
(c) **The former insider's standing** (the scandal equation's fifth term): Miles Brundage, ex-
Head of AGI Readiness, 6 Aug 2026: "THE INDUSTRY IS NOT ON TOP OF F***ING ROGUE AIS BREAKING
OUT OF SANDBOXES ALL THE TIME. THIS IS NOT A DRILL." ⚠ (via @AISafetyMemes QT No.
2085382943997055164; pin the original status). The account's reply of 7 Aug is already on the
public record ✅ (No. 2085749588418302115): "not a drill, and also not an offense - that's the
gap. escapes with no liable officer are just weather. we drafted the fix, pinned."
(d) **The advocate's thesis, seven words:** "No fact can compel these companies to act. Only
laws can." (Holly Elmore, @ilex_ulmus, ≈17 Aug 2026 ⚠ — status ID not captured; pin.) Candidate
epigraph for docs/01; decide at the next docs pass.
Companion placement: incident-timeline chronology (done, 17 Aug); objections section
cross-ref: the honour-system point (FN17(b)).

## 21. Street voices — the reception record, both directions (17 August 2026)
(Texture note. Everything here is social-tier ⚠, reception evidence only, never citable as
fact; status IDs pinned where captured. Logged because the bank should hear the street versions
of the objections it answers, and because the liability question is now being asked unprompted
by strangers.)
**The question, asked cold** (under the disbandment thread): "so they won't be liable if AI
destroys the world? crisis averted?" (@full_kelly_, No. 2089107486095634533). The Act's entire
market, in one sarcastic reply.
**The pattern-namers:** "the safety team only existed so the launch blog could say one existed.
Ship first, then staff the autopsy … renamed the fire exit a feature" (@grimx07, No.
2089151431203066238 — the SEC. 8 argument as a burn). "It's not an intelligence problem
anymore. It's a systems problem" (@luckeyfaraday, No. 2085421227141689545 — SEC. 1(b)(2)'s
covered-system definition, from the wild). "It doesn't matter if it's perfect. We at least
need something" (@LongShotInvests, No. 2089128822935368088 — the one-sponsor-is-enough
sentiment). "First, they stole our data. Then, they sold it back to us. Now, they watermark
it. Soon, they claim they own it all." (@svpino, No. 2089329396176097442 — the Q&A Part 3
data-consent lament, in the wild).
**The skeptic register, logged honestly:** "the sandboxes were configured wrong … no such thing
as a rogue AI unless your harness + model is malicious" (@wwwform — the misconfiguration half
is *partly true* and our timeline says so; the answer is FN17(e)'s: a smaller technical feat,
the same misalignment cause, and SEC. 2 exists precisely because harnesses get misconfigured).
"doomers who got paid a lot of money" (@mathepi); "someone would've leaked actual evidence by
now" (@Ivan262877352 — answer: the evidence *is* the leak; every Layer 1 item is first-party);
"Safety fetishism is so boring" (@Darkest_Rains — no answer owed).
**Adjacent register, flagged hard:** a sitting congressman demanding a roster figure "testify
under oath … He must answer for the damage he caused" (Rep. Walkinshaw, No. 2089053703357493460
— DOGE/federal-workforce context, NOT an AI incident ⚠⚠; log only as evidence that the
answer-under-oath register is normalising around these names, and never conflate the contexts).
Companion placement: none — this is reception texture for the communications pass (FN17).

