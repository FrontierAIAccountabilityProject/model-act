# The verification record

This file is the source record behind the project's frontier-scope research. It exists because
[the frontier enterprises](./frontier_enterprises.md) and [the frontier models](./frontier_models.md)
assert quotations and figures, and a reader is entitled to know which were opened by this project,
which came in by another route, and — the half that matters most — **which claims were checked and
did not survive.**

**Owner rule.** This file owns every source, URL, retrieval date, and verification grade in the
frontier-scope research. The argument files carry the quotations and point here; they do not
maintain their own source apparatus. Where this file and another disagree, this file governs.

**Grades.** ✅ = the cited page was opened by this project and the wording reproduced identically
on two independent retrievals. ⭘ = opened once. ⚠ = recorded from the maintainer's sourced
research or from secondary reporting, with its citation, and not yet opened here. ✗ = checked and
failed; see the failures section, and do not use.

*Compiled 22 August 2026. Valuations are approximate at that date and move daily; private
valuations are softer than market capitalisations.*

---


### Quotation audit, 25 August 2026 — every quote from the day's four intakes checked against source

*Recorded so this never needs repeating. Each quotation now published from the four documents
taken in on 25 August was matched, programmatically, against text extracted from the source PDF
itself, with whitespace, curly quotes and hyphenation normalised.*

**Result: every quotation verified accurate.** No misquotation was found on any published surface.

**Three extraction artefacts caused false alarms, and are noted so a future check is not misread
as a failure:**

1. **Dropped ligatures.** The Javorsky essay's PDF loses the "fi" ligature on extraction, so
   "definitely" extracts as "denitely", "scientific" as "scientic" and "efficacy" as "eÂ©cacy".
   Quotations containing those words will not match a naive string search against extracted text.
   The published wording follows the rendered document, which is correct.
2. **Multi-column interleaving.** *The Lancet* report is three-column and the Kierans paper is
   two-column. A layout-preserving extraction interleaves the columns, so a sentence is broken by
   text from a neighbouring column. Extract without layout preservation, or read the rendered
   page, before concluding a quote is wrong.
3. **Footnote intrusion.** In the Lyness article, law-review footnotes interrupt the body text
   mid-sentence on extraction. The misdemeanour quotation at 64 B.C. L. Rev. 298 is split this way
   and is accurate as published.

**Method, for repetition if ever needed:** extract with `pdftotext` (no `-layout` for multi-column
sources), normalise whitespace and quotation marks, then substring-match each published quotation.
The audit script is not committed; it is four lines and rewriting it is faster than maintaining it.


## 1. The developers' own designations

| Company | Quotation, verbatim | Source | Date | Grade |
|---|---|---|---|---|
| **Google DeepMind** | "We call our most powerful foundation models 'frontier models'." | deepmind.google/frontier-safety | undated page, retrieved 22 Aug 2026 | ✅ |
| **Google DeepMind** | "The Frontier Safety Framework is a set of protocols that ensure our most advanced AI models remain reliable, thoroughly tested, and aligned with human values." | deepmind.google/frontier-safety | retrieved 22 Aug 2026 | ✅ |
| **Google DeepMind** | *Frontier Safety Framework* v2.0 (document title) | storage.googleapis.com — DeepMind blog asset | 4 Feb 2025 | ⭘ |
| **Meta** | "Frontier AI in our Framework refers to a new or substantially modified highly capable general-purpose generative AI model that we are developing for deployment." | ai.meta.com/static-resource/Meta_Advanced-AI-Scaling-Framework-v2 | v2, Apr 2026 | ✅ |
| **Meta** | "This Advanced AI Scaling Framework outlines how Meta manages and prepares for Frontier AI capabilities that could lead to severe, large-scale outcomes." | same | Apr 2026 | ✅ |
| **Meta** | "We trained the model using at least 10^26 integer or floating point operations (to include material modifications to the model through fine-tuning, reinforcement learning training, and other training steps), or another threshold as may be defined by evolving standards or industry best practices." | same, Terminology appendix | Apr 2026 | ✅ |
| **Meta** | "Today, we're sharing our Frontier AI Framework, which outlines our consideration of risk in our model-release decisions" | about.fb.com/news/2025/02/meta-approach-frontier-ai | 3 Feb 2025 | ⭘ |
| **OpenAI** | "If another frontier AI developer releases a high-risk system without comparable safeguards, we may adjust our requirements." | openai.com/index/updating-our-preparedness-framework | 15 Apr 2025 | ✅ |
| **OpenAI** | "Frontier AI models have the potential to benefit all of humanity, but also pose increasingly severe risks." | openai.com/global-affairs/our-approach-to-frontier-risk | 26 Oct 2023 | ✅ |
| **OpenAI** | *OpenAI Frontier* — enterprise agent product; agents that "do real work" | openai.com/index/introducing-openai-frontier | 2026 | ⚠ |
| **Anthropic** | "As frontier AI models advance, we believe they will bring about transformative benefits for our society and economy." | anthropic.com/responsible-scaling-policy | updated 14 Aug 2026 | ✅ |
| **Anthropic** | "Frontier AI models also, however, present new challenges and risks that warrant careful study and effective safeguards." | same | 14 Aug 2026 | ✅ |
| **Anthropic** | *Frontier Red Team* — named programme | anthropic.com/news/strategic-warning-for-ai-risk-progress-and-insights-from-our-frontier-red-team | 19 Mar 2025 | ✅ |
| **Anthropic** | "We believe it would be good for the world to have the option to slow or temporarily pause frontier AI development." | anthropic.com/institute/recursive-self-improvement | 2026 | ⚠ |
| **xAI** | "This Frontier AI Framework ('FAIF') outlines xAI's approach to policies for mitigation of significant risks associated with the development, deployment, and release of xAI's frontier AI models, such as Grok." | media.x.ai — *xAI Frontier Artificial Intelligence Framework* PDF | effective 30 Jun 2026 | ✅ |
| **xAI** | "As xAI advances frontier model development, we continuously evaluate whether emerging risk domains meet our significance and severity thresholds, and update our control architectures accordingly." | same | 30 Jun 2026 | ✅ |
| **xAI** | "Grok 4.6 achieves frontier intelligence across several agentic coding and knowledge work benchmarks. It matches GPT-5.6 Sol on the composite score of nine benchmarks." | x.ai/news/grok-4-6 | 12 Aug 2026 | ⚠ |
| **xAI** | "Frontier AI models for everything you imagine. Reasoning, code, voice, images, and video. Trained on the world's largest supercluster." | x.ai (homepage) | retrieved 22 Aug 2026 | ⚠ |
| **Microsoft** | "The compute used to train frontier models has increased by a factor of one trillion." — Mustafa Suleyman, CEO of Microsoft AI | microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models | 2 Jun 2026 | ✅ |
| **Microsoft** | "At Microsoft AI, we recognize that there are no shortcuts to the frontier." — Suleyman | same | 2 Jun 2026 | ✅ |
| **Microsoft** | "We call this Microsoft Frontier Tuning." | same | 2 Jun 2026 | ✅ |
| **Microsoft** | "To build a frontier firm, you have to optimize frontier performance against cost." | microsoft.ai/news/optimizing-the-frontier-performance-curve | 2026 | ⚠ |
| **Microsoft** | "the Frontier Firm — built around intelligence on tap, human-agent teams and a new role for everyone: agent boss" | blogs.microsoft.com — Work Trend Index | 23 Apr 2025 | ✅ |
| **Amazon** | "high-performance inference with leading selection of frontier models (Bedrock)" — Andy Jassy, letter to shareholders | aboutamazon.com | Apr 2026 | ⭘ |
| **Amazon** | "Today, we're introducing Amazon Nova Forge, a new service to build your own frontier models using Nova." | aws.amazon.com/blogs/aws | 2 Dec 2025 | ⭘ |
| **Amazon** | "Frontier intelligence and industry-leading price performance" | aws.amazon.com/nova | meta-updated 20 Aug 2026 | ⭘ |
| **Amazon** | "The more compute that is dedicated to training this frontier model, the smarter and more accurate it will become." (re Claude, on Project Rainier) | aboutamazon.com/news/aws | 24 Jun 2025 | ⭘ |
| **Amazon** | *Amazon's Frontier Model Safety Framework* (document title); "the capabilities of Amazon's frontier models" | amazon.science | — | ⚠ |
| **NVIDIA** | "the frontier of AI, maximum intellectual capability, is going up and up" — **Sam Altman**, quoted on NVIDIA's blog | blogs.nvidia.com/blog/openai-nvidia | 22 Sep 2025 | ⭘ |
| **NVIDIA** | NVIDIA infrastructure is "the foundation that lets us keep pushing the frontier of AI" — Altman, NVIDIA investor materials; release titled *NVIDIA Vera Rubin Opens Agentic AI Frontier* | investor.nvidia.com | 2026 | ⚠ |
| **NVIDIA** | "CoreWeave is a world-class new generation AI-Native cloud." / "…to power the world's AI." — Jensen Huang | coreweave.com/news (CoreWeave release) | 16 Mar 2026 | ⭘ |
| **Oracle** | "Organizations training and serving frontier AI models require infrastructure engineered for extreme throughput" | blogs.oracle.com/cloud-infrastructure | 17 Mar 2026 | ⭘ |
| **Oracle** | "integrating secure frontier AI into classified environments will accelerate data synthesis…" — **unattributed press-release body text, not a named person's quote** | oracle.com/news/announcement — Department of War agreement | 1 May 2026 | ⭘ |
| **Oracle** | "frontier AI infrastructure" | oracle.com/ai-world/cloud | — | ⚠ — see failure F2 |
| **CoreWeave** | "This expansion reinforces our position as the essential partner for any organization navigating the complexities of frontier-scale AI." — Michael Intrator, CEO | coreweave.com/news | 16 Mar 2026 | ⭘ |
| **Databricks** | "Enterprise demand for frontier AI is accelerating, and with Databricks, we're making its deployment even simpler without compromising the high bar for performance and production." — **Brad Lightcap, COO of OpenAI**, in Databricks' own release, headed "Frontier Models on Enterprise Data" | databricks.com/company/newsroom | 25 Sep 2025 (syndicated copies 3 Oct — date ⚠) | ⭘ |
| **Palantir** | "It's not just the man and woman on the street who are unhappy with the frontier labs" — Alex Karp, CEO | theregister.com | 11 Jun 2026 | ✅ |
| **Tesla** | "autonomy at scale in vehicles, robots and more" | tesla.com/AI | — | ⚠ |
| **Tesla** | "Tesla's New Frontier: Embodied AI" — **publication's headline, not a Tesla statement** | site.financialmodelingprep.com | 8 Apr 2026 | ⭘ |

## 2. Ownership and control

All from proxy statements, SEC filings, company governance pages, or named reporting.

| Company | Fact | Source | Grade |
|---|---|---|---|
| OpenAI | OpenAI Foundation controls OpenAI Group PBC; "appoints all members of the board of directors of OpenAI Group and can replace directors at any time"; Foundation ≈26%, Microsoft ≈27%, employees and investors ≈47%; recapitalisation closed 28 Oct 2025 | openai.com/our-structure | ✅ |
| Anthropic | Delaware PBC; Long-Term Benefit Trust holds Class T stock electing board members, to a majority within four years | anthropic.com/news/the-long-term-benefit-trust (19 Sep 2023) | ⭘ (current trustee composition unconfirmed) |
| Anthropic | $30B Series G at **$380B** post-money, led by GIC and Coatue | anthropic.com newsroom, 12 Feb 2026 | ⭘ |
| xAI | SpaceX combined with xAI, early Feb 2026, ≈$1.25T combined | Bloomberg 2 Feb 2026; CNBC 3 Feb 2026 | ⭘ |
| xAI | "xAI LLC" remains the named developer in its own framework dated 30 Jun 2026 — i.e. a subsidiary/brand within SpaceX, not dissolved | media.x.ai FAIF | ✅ |
| Alphabet | Page 27.1% and Brin 25.2% of voting power ≈ **52.3%**, via ten-vote Class B | Alphabet 2025 proxy statement, beneficial-ownership table | ⭘ |
| Meta | "Because Mr. Zuckerberg controls a majority of our outstanding voting power, we are a 'controlled company'" — Meta's own 2026 proxy, **which prints no percentage** | sec.gov, meta-20260416 | ⭘ |
| Meta | The **≈61%** figure is from a shareholder-proponent Notice of Exempt Solicitation, **not Meta's own disclosure** — cite as approximate with that caveat | sec.gov, r57250px14a6g | ⭘ |
| Microsoft | Single share class, one vote per share; no controlling shareholder; institutional ownership ≈71% (holder percentages secondary) | charter; secondary aggregator | ⚠ on percentages |
| NVIDIA | Jensen Huang, founder and chief executive; market capitalisation **$5.213T**, most valuable company | companiesmarketcap.com, Aug 2026 | ⭘ |
| Amazon | Jeff Bezos, founder and executive chair; capitalisation topped **$3T** on 3 Aug 2026 | CNBC | ⚠ |
| Oracle | Larry Ellison, founder, reported **40.6%** holder; co-CEOs Magouyrk and Sicilia since Sep 2025; capitalisation ≈**$421.9B** | Motley Fool 29 Jul 2026; companiesmarketcap.com | ⚠ on the stake |
| Tesla | Musk largest individual holder at ≈**20%**; no super-voting class; capitalisation ≈$1.4T | Motley Fool, 9 Aug 2026 | ⭘ |
| Palantir | Class F founder voting trust (Karp, Thiel, Cohen) engineered to just under half of total voting power regardless of economic stake; capitalisation ≈**$412B** (19 Aug 2026) | Palantir 2025 proxy, sec.gov; stockanalysis.com | ✅ (proxy) |
| Databricks | Private; seven co-founders, Ghodsi CEO; **$5B** round closed 13 Aug 2026 at ≈**$190B**, led by Coatue | TechCrunch, 13 Aug 2026 | ⭘ |
| CoreWeave | Public since 28 Mar 2025 (Nasdaq: CRWV); founders Intrator, Venturo, McBee; NVIDIA a shareholder ($2B added Jan 2026); capitalisation ≈$48.5B | en.wikipedia.org; companiesmarketcap.com | ⚠ |

## 3. Compute

Training-compute figures for current flagship models are **not disclosed by any developer**. The
figures this project uses are Epoch AI estimates, taken from the dataset files held by the project
(CC BY 4.0; citation at [the models file](./frontier_models.md)), not from web summaries.

**Standing caution.** Two separate web retrievals of Epoch's published figures returned
*different* mantissas for the same models (Grok 3 at 3.5 × 10²⁶ vs 4.6 × 10²⁶; GPT-4.5 at
2.1 × 10²⁶ vs 3.8 × 10²⁶). The dataset files in hand are therefore the authority for any figure
this project publishes, and no precise FLOP figure should be taken from a summarised fetch.
Robust across retrievals: Grok 3, Grok 4 and GPT-4.5 sit at a few × 10²⁶; Claude Opus 4 sits
**near** the 10²⁶ line on a range (reported 5 × 10²⁵–2 × 10²⁶, tentative); GPT-4 ≈ 2 × 10²⁵;
Claude 3.5 Sonnet ≈ 2.7 × 10²⁵. Epoch publishes no estimate for GPT-5 or Claude Opus 4.5.

**Consequence for the models file.** Because Opus 4's range crosses the threshold at its upper
bound, the claim "only three models carry an estimate at or above 10²⁶" is true of **point
estimates** and must be stated that way. Recorded here so the two research files cannot drift
apart again.

## 4. What failed verification

The useful half of the record. None of the following may be used.

**F1 — Tesla has no first-party "frontier" usage.** Searched across tesla.com and Musk's public
posts; Tesla's own register is *autonomy* and *real-world AI*. The "frontier" framing around
Tesla is third-party editorial (FMP headline, 8 Apr 2026; a Forbes Technology Council piece
applying "frontier" to embodied AI as a field). **Consequence:** Tesla's coverage rests on
function, never on self-designation — and the gap is itself evidence that a self-designation
limb cannot stand alone.

**F2 — Oracle does not say "frontier AI infrastructure."** The literal phrase was not found on
the Oracle pages fetched. Oracle's verbatim usages are "secure frontier AI" (unattributed press-
release text) and "frontier AI models" / "frontier model training". The phrase remains in
circulation from the working research and is marked ⚠ above; **do not quote it as Oracle's words**
until the exact page is produced.

**F3 — The Altman/NVIDIA line differs from the working version.** The working table carried
NVIDIA infrastructure as "the foundation that lets us keep pushing the frontier of AI." What was
verified on NVIDIA's own blog is: "the frontier of AI, maximum intellectual capability, is going
up and up" (22 Sep 2025). Both are attributed to Altman in NVIDIA materials; only the second was
opened here. Prefer the second.

**F4 — Two NVIDIA attribution traps.** "The next frontier of AI is physical AI, Huang explained"
(CES blog, 6 Jan 2025) is the **blog author's paraphrase**, never a Huang quotation. And the
"AI-Native cloud" line is Huang's, but contains no instance of the word *frontier*.

**F5 — Palantir's August 2026 "frontier AI labs" phrasing is journalism, not Karp.** In coverage
of the Q2 2026 call, "frontier AI labs" appears in the outlets' framing; TechCrunch's rendering
inserts "[the frontier labs]" as an editorial bracket. The verified verbatim Karp sentence is the
11 June 2026 one recorded above. Palantir's own shareholder letter is client-rendered and could
not be read; **no verified written quotation from Palantir's own materials exists yet** — the
route is the 8-K exhibit on SEC EDGAR.

**F6 — Oracle's classified-deployment sentence is unattributed.** It is descriptive body text in
the press release; the named quotations on that page (Kim Lynch, Oracle; Emil Michael, Under
Secretary of War) contain no instance of *frontier*. Never attribute it to Ellison or to any
person.

**F7 — Two valuations in circulation lack a source.** Anthropic at ≈$965B and OpenAI at ≈$852B
appear in the working research; the verified figures are Anthropic **$380B** (own newsroom,
12 Feb 2026) and OpenAI ≈**$500B** implied at the October 2025 recapitalisation. The higher
figures may reflect later rounds this project has not opened. Until pinned, publish the verified
figures with the higher ones flagged, never the reverse.

**F8 — "SpaceXAI" is not a corporate name.** It is a journalists' portmanteau for the combined
entity. The legal developer name remains xAI LLC. The merger itself is real and sourced above.

**F9 — Meta's framework was renamed, and the rename matters.** The *Frontier AI Framework*
(Feb 2025) became the *Advanced AI Scaling Framework* v2 (Apr 2026), retaining "Frontier AI" as
its defined term. Any file citing the old title alone is stale. **This is the strongest live
example of [CURE 6](../audit/v3_5_cure_language.md)'s anti-evasion clause** — a holding-out is
not undone by later amendment — and should be cited there rather than left as a footnote.

## 5. Corrections this record forced

Logged so the trail is visible: the two-twelves overlap was published as five companies and is
**eight** (the five developers plus Microsoft, Amazon and NVIDIA); the compute-threshold
comparison table labelled H.R. 9917 the "FRONTIER vehicle" when H.R. 9917 is the **AI Kill
Switch Act** and the FRONTIER Act is H.R. 9925. Both entered [the errata register](../ledger/errata.md).

## 6. The instruments — read in full, cited from coverage, pending

*Added 23 August 2026, after a demonstration of why it was needed: the Hugging Face technical
timeline was cited three times in [the dossier](../dossier/README.md), down to the
lowered-refusals detail, while this record — the file that claims to own every source — had no
entry for it. A fresh reader therefore reported it "unread." Whether it was read is exactly what
this record failed to say. This section ends that class of error: **an instrument appears here
before any file relies on it, and its read-status is a recorded fact, not a recollection.**
"Cited from coverage" is a status, not a shame; invisible status is the defect.*

### Instruments of the 2026 record

| Instrument | Read-status | Relied on at |
|---|---|---|
| UK AISI incident report INC-2026-07-28-01 (4 Aug) | **Read in full** | [its own file](./aisi_incident_inc_2026_07_28_01.md) — the record's one government-authored entry |
| 15-state AG preservation letter (3 Aug) | **Read in full, 23 Aug** (five pages; held privately, outside the repository) | [enforcement record § 3](./state_enforcement_record_2026.md), graded against it |
| House Homeland Security hearing, *DeepSeek and Unitree Robotics* (Serial 119-42, 17 Mar 2026; GPO transcript) | **Read in full, 24 Aug** | [why the disparity](../standards/why_the_disparity.md) (Doshi); [known objections](../docs/known_objections.md) (the distillation record); census queue |
| House Oversight hearing, *Shaping Tomorrow: The Future of AI* (Serial 119-49, 17 Sep 2025; GPO transcript) | **Read in full, 24 Aug** | [why the disparity](../standards/why_the_disparity.md) (Fabrizio; Turner Lee); the Clark-timeline retrieval lead |
| Congressional Record, 1 Apr 2025, H1386 (Stansbury floor statement) | **Read in full, 24 Aug** | [the standing watch](../audit/standing_watch_2026-08-20.md), continuity note |
| House Oversight hearing, *The Federal Government in the Age of AI*, 5 June 2025, Serial 119-31 (GPO transcript) | **Read in full, 24 Aug** | the Pressley–Schneier "not in anyone's job description" exchange (known objections, why-one-named-officer); the moratorium fight recorded from inside the majority + the general-applicability/criminal carve-out concession (dossier § 5.3); the witness table's certification lines; census queue notes |
| Anthropic, *Detecting and Preventing Distillation Attacks* (23 Feb 2026) | **Cited from the hearing record only** — retrieval queued | [known objections](../docs/known_objections.md), identified as the footnoted primary |
| Hugging Face technical timeline (27–28 Jul) | **Read in full, 22 Aug** — the read was recorded at [press corpus § 7](./press_corpus_july_august_2026.md) (item 5 discharge: the HF posts of 16 and 27 July "read as primaries"), invisible from here until this index existed. Conformed 23 Aug, one day after this table was built: the read existed; only its visibility was broken. | dossier ×3; press corpus timeline (~17,600 attacker actions); the AG letter quotes "more than 17,000" — consistent |
| OpenAI incident statement (21 Jul) | **Read in full, 22 Aug** — same press corpus § 7 item 5 discharge (OpenAI and Anthropic disclosures "read as primaries") | dossier § disclosure order; enforcement record § 3 (as the letter's own link) |
| Florida v. OpenAI filed complaint (1 Jun) | **Excerpt only** — full read gates any further quotation | [enforcement record § 1](./state_enforcement_record_2026.md) |
| 42-state subpoena (12 Jun) | **Not public** — nothing may be attributed to its text | enforcement record § 2 |
| The AG letter's own press base (Reuters 24 Jul; Tom's Hardware; BBC) | Cited via the letter's five embedded links, extracted 23 Aug | enforcement record § 3 |
| Reuters, "How a Texas student blew the whistle…" (20 Aug) | **Read in full, 23 Aug**, via WHTC syndication (reuters.com copy paywalled) | [the incident file § 5 addendum](./aisi_incident_inc_2026_07_28_01.md) |
| Ball post + thread, 8–10 Aug (X) | ⚠ P — post pages supplied 23 Aug, validated; URLs pinned | [press corpus § 5](./press_corpus_july_august_2026.md); README |
| Ball, "A Cascade of Conscientiousness" (Hyperdimensional, 28 May) | ⚠ P — full essay supplied 23 Aug | press corpus § 5; fiscal note; known objections |
| Ball & Ramakrishnan, "Entity-Based Regulation…" (Carnegie, 7 Jul 2025) | ⚠ P — full text supplied 23 Aug | [enterprise file addendum](./frontier_enterprises.md) |
| CSIS, Caroli & Mehta, "Toward a Federal Framework" (3 Aug) | ⚠ P — full text supplied 23 Aug; PDF link carried | census sources; [why the disparity addendum](../standards/why_the_disparity.md) |
| CDT, "2026 State and Federal AI Legislation Updates" (20 Aug) | ⚠ P — full text supplied 23 Aug; CDT content freely reusable with credit | census sources; known objections |
| Akerman alert on Illinois SB 315 (Dayal, 10 Jun) | ⚠ P — full text supplied 23 Aug | census sources |
| PA press release: Shapiro administration sues Character.AI (5 May) | **Retrieved 23 Aug** (pa.gov, ⚠ R) | [enforcement record § 6](./state_enforcement_record_2026.md) |
| AI Futures Project, *AI 2040 / Plan A* (2026; maintainer-supplied PDF, text-extracted) | **Read in full, 24 Aug** (delegated full pass; quotes conformed to the extract) | [forecast arithmetic](./forecast_arithmetic.md) — scenario material marked ⚠ per its own "recommendation, not a prediction" |
| AI Futures Project, Model supplementary materials (2026; ~38,000 words) | **Key sections read, 24 Aug** (summary table, capability anchors, results comparisons; remainder held) | [forecast arithmetic](./forecast_arithmetic.md) — forecast-grade parameters with published CIs |
| AI Futures Project, *AI 2027* (Apr 2025; maintainer-supplied PDF) | **Held; text extract short of the full scenario — re-fetch queued before any reliance** | nothing yet |
| Connecticut P.A. 26-15 (chaptered) + S.B. 2 (2025) file copy + analysis | **Read, 24 Aug evening** (delegated pass for the OQ1 question; census read of 23 Aug stands) | [the queue's OQ1 resolution](../audit/v3_5_cure_language.md); [the half-statute counter-example](../docs/safe_harbors_and_affirmative_defenses.md) |
| Colorado SB 25B-004 fiscal note (10 Sep 2025) | **Read in full, 24 Aug evening** — the delay to 30 June 2026 verified at the primary | [half-statute](../docs/safe_harbors_and_affirmative_defenses.md); [fiscal note § 6c](../standards/fiscal_note.md) |
| Colorado SB 25B-004 signed act | **Held — scan without text layer**; the fiscal note (final, reflecting the enacted bill) carries the reliance | — |
| Tennessee Public Chapter 781 (S.B. 837) | **Read in full, 24 Aug evening** — three pages, verbatim in the queue | [CURE 19](../audit/v3_5_cure_language.md); [the dated record](../docs/timeline.md) |
| EO 14365 (11 Dec 2025), primary | **Read in full, 24 Aug evening** — number, date, § 3 task force, § 5(a) funds, § 8(b) exclusions all primary-confirmed | [half-statute](../docs/safe_harbors_and_affirmative_defenses.md); [the watch](../audit/standing_watch_2026-08-20.md) |
| SANDBOX Act bill text (unnumbered print, Cruz) | **Read, 24 Aug evening** — §§ 702(c),(i),(k),(l),(p) verified | [half-statute](../docs/safe_harbors_and_affirmative_defenses.md); [census](../standards/frontier_bill_census.md) |
| TRUMP AMERICA AI Act section-by-section summary | **Read, 24 Aug evening** — § 24's actual preserved-law wording conformed repo-wide; bill text still queued | [census](../standards/frontier_bill_census.md); [half-statute](../docs/safe_harbors_and_affirmative_defenses.md) |
| GAAIA discussion draft + Trahan FAQ + WEDI comment letter | **Read, 24 Aug evening** (preemption title + Title I thoroughly; remainder skimmed) — §§ 121(b)–(d), 112(e)(7)–(8) verified: all Title I signatures IVO-side | [census](../standards/frontier_bill_census.md); [half-statute](../docs/safe_harbors_and_affirmative_defenses.md) |
| Serial 119-31 written witness statements (×5) + CCIA/SIIA letter on MA S.3228/H.5576 (7 Aug 2026) | **Read, 24 Aug evening** — the Thierer written/transcript delta recorded; the letter's audit-ecosystem objection held for known objections | [dossier § 5.3](../dossier/README.md); [known objections](../docs/known_objections.md) |
| Colorado SB 26-189 final revised fiscal note (6 May 2026) | **Read in full, 24 Aug evening** — corrected this record's own figures (E36) | [fiscal note § 6b](../standards/fiscal_note.md); [E36](../ledger/errata.md) |
| Apollo Research, *AI Behind Closed Doors* (Apr 2025) | **Key sections read, 24 Aug evening** (exec summary, definitions survey, recommendations) | [the queue, OQ2/OQ4 donor notes](../audit/v3_5_cure_language.md) |
| Dunne, *Divergence and Convergence in AI Regulation* (20 Jul 2026) · Hariri & Ho, *AI for Statutory Simplification* · NY DOL § 740 notice | **Read / abstract-read, 24 Aug evening** | Dunne: census context ⚠ (secondary); § 740: [CURE 17 donor note](../audit/v3_5_cure_language.md) |
| Colorado SB 26-189 signed act · Carnegie RAISE piece | **Held — staging deferred (large files; transfer timeouts)**; no reliance | — |
| White House, *Winning the Race: America's AI Action Plan* (23 Jul 2025; primary PDF) | **Read in full, 24 Aug** | [two visions](../docs/two_visions.md) owns its quotes; the ai.gov pillars paste (⚠ P) banked separately; half-statute ⚠ rows unchanged |

### Legal texts the queue leans on

| Text | Read-status | Relied on at |
|---|---|---|
| Cal. SB 53 (Stats. 2025, ch. 138) | **Relevant provisions reproduced in the repository** | [interim standards](../standards/interim_standards.md) |
| GAAIA discussion draft § 121 (4 Jun; not introduced) | Subsections (b) and (e) **pinned verbatim**; full-draft read unrecorded | [the record § C.2](../audit/record.md) |
| FRONTIER Act, H.R. 9925, § 9 | Characterised; full-text read unrecorded | the record; [standing watch](../audit/standing_watch_2026-08-20.md) |
| *United States v. Park*, 421 U.S. 658 (1975) | Three burden passages **verified against the reported opinion, 22 Aug** (prima facie at 673–74; impossibility at 672–73; the two burdens at 673); full-opinion read pending before CURE 8 lands | [CURE 8](../audit/v3_5_cure_language.md); companion notes |
| 18 U.S.C. § 1365(h)(3)–(4) | **Verified verbatim, 23 Aug** | CURE 1 and its addendum |
| 21 C.F.R. § 803.3(w) | **Verified via the live eCFR** | SEC. 1(b)(8); the CURE 1 addendum |
| S. 1792 (119th), AI Whistleblower Protection Act | **Primary XML read in full, 23 Aug** — public domain; held on the shelf below | [who has to tell you § 4b](../standards/who_has_to_tell_you.md); census queue |
| 42 C.F.R. § 73.19 (select-agent theft/loss/release notification) | **Retrieved 23 Aug** (eCFR, ⚠ R) | [the gallery's escape section](../standards/the_same_conduct.md); who has to tell you § 4b |
| 7 U.S.C. § 7734 (Plant Protection Act penalties) | **Retrieved 23 Aug** (uscode.house.gov, ⚠ R) | the gallery's escape section |
| *United States v. Morris*, 928 F.2d 504 (2d Cir. 1991) | **Key holdings retrieved 23 Aug** (Justia, ⚠ R); full-opinion human read pending | the gallery's escape section |
| DOJ release, Jensen guilty pleas (D. Colo.) | **Retrieved 23 Aug** (justice.gov, ⚠ R) | the gallery's escape section |
| NPR, Schmidt sentencing (6 Dec 2017) | **Retrieved 23 Aug** (⚠ R) | the gallery's escape section |
| NY S 10456 (Gounardes, 15 May 2026) | **Primary full text in hand, 23 Aug** (one-section bill, nysenate.gov page supplied) — fixes RAISE's citation: GBL Article 44-B, ch. 96 of 2026 | census queue |
| 42 C.F.R. § 73.11 (select-agent security plans) | **Elements summarised from the eCFR, 23 Aug** (⚠ R); full-text read pending before any quotation beyond the summarised elements | [the fatals pass](../audit/v3_5_cure_language.md) (CURE 10, CURE 7) |
| Idaho H.B. 720 (2022), Idaho Code § 5-346 | **Operative sentence retrieved verbatim, 23 Aug** (legislature.idaho.gov PDF, ⚠ R) | CURE 19 |
| Utah H.B. 249 (2024) | Identified via Liebman extract; text not opened | CURE 19 |
| Tennessee SB 837 / HB 849 (114th G.A.) | Identified (trackbill; local coverage); **enrolled text not in hand** — capitol PDF blocks automated retrieval; pull manually | CURE 19 |
| Liebman, 61 Wake Forest L. Rev. 115 (2026) | Extract retrieved 23 Aug (⚠ R); full PDF wanted for the shelf | CURE 19 |
| H.R. 8094 (119th), AI Foundation Model Transparency Act of 2026 | **Primary read in full (16 pp.), night of 23–24 Aug** — introduced print on the shelf | census; [the definition](../docs/the_definition.md) |
| Lyness — second upgrade | **Parts IV–V read in full, same night** — the whole article is now read | comparative § 5 addendum; for legislators § 4 |
| USA.gov, "How laws are made" | **Read 25 Aug** (page last updated 17 Nov 2025). Cited for the citizen-petition origin of a bill. Captured verbatim in the private library so the citation needs no re-fetch | paths to enactment; REVIEWERS |
| U.S. House, "The Legislative Process" | **Read 25 Aug.** Cited for "First, a representative sponsors a bill" and the sequence that follows a sponsor | paths to enactment; REVIEWERS |
| Congress.gov, "The Legislative Process: Overview" (transcript) | **Read 25 Aug.** Cited for committee expertise, post-enactment oversight, and the unpredictability of the stage sequence. Companion diagram held as a PDF | paths to enactment |
| Harvard Law School Library, uniform laws and model acts guide | **Read 25 Aug** (guide last updated 18 Dec 2025). Cited for: model acts may be proposed by any individual or organization; rarely enacted in entirety; a uniform law takes at least two years and some fifteen — the last quoted against this project | paths to enactment; REVIEWERS |
| Uniform Law Commission, home page | **Read 25 Aug.** Cited for the ULC's own description of an "open and deliberative process" drawing on commissioners, legal advisors and observers. **This source corrected a claim of ours**: see the changelog entry of the same date | README; REVIEWERS |
| Javorsky, *How AI Can, and Can't, Cure Cancer* (Mar 2026) | **Read in full 25 Aug.** Quoted for: intelligence not the bottleneck; 10.5 years Phase I to approval and 90% attrition; 10–20% real time saving; Halicin and the antibiotic market failure; the externality passage; the FDA as "a 20th century agency ill-equipped to manage accelerating scientific understanding". Author not contacted at time of writing; not a supporter | known objections (acceleration section, FDA block) |
| Kierans, Casper & Ghosh, *Intelligence Is Not the Bottleneck* (2026) | **Read in full 25 Aug.** Quoted for: "structural barriers, not intelligence, are the principal bottleneck"; the 6–12 month claim it rejects; "a very convenient agenda for companies who are racing"; "safety-washed euphemism"; the Hadfield & Clark deficits. Casper was contacted 25 Aug on unrelated business; no connection implied | known objections (timelines); forecast arithmetic addendum; OQ2 donor note |
| Webster, "Europe's medical AI reforms", *The Lancet* (2026) | **Read in full 25 Aug.** ⚠ secondary: named-source reporting, underlying trade and legislative instruments not in hand. Quoted for the Lutnick tariff linkage of Nov 2025 and the Commission's reply | half-statute ceiling addendum |
| Javorsky, Tegmark & Helfand, *Lethal autonomous weapons*, BMJ (2019) | **Read 25 Aug.** Background only; not cited in any published surface | outreach file (Javorsky door) |
| Lyness — full SSRN PDF held, 25 Aug | **Complete article in hand** (SSRN 4186172), re-read end to end; private reading note filed. Closes retrieval item 21. No erratum: E34 already corrected the only overstatement, and what remains is accurate | comparative § 5 addendum (25 Aug); table of authorities |
| Hustis & Gotanda — upgrade | **Introduction and Part I–II opening read** (pp. 169–73): the 80%/68% enforcement-wave estimates; *United States v. Dee*; the three-theories map. Body Parts III–VII unread | comparative § 5 addendum |
| CRS-style compilation, "Enforcement of Federal Pollution Control Laws" | **Identified only** — the congress.gov capture renders unreadably small; the criminal-provision tables are visible as structure. Text edition wanted before any citation | — |
| DLA Piper *AI Laws of the World*; Binns | **Still unread** — honest state; queued for the next scan | — |
| 33 U.S.C. § 1319(c)(6) | **Retrieved verbatim, 23 Aug** (uscode.house.gov, ⚠ R) | [comparative § 5](../standards/comparative_officer_liability.md) |
| 42 U.S.C. § 7413(c)(6) | **Retrieved verbatim, 23 Aug** (LII, ⚠ R) | comparative § 5 |
| Lyness, 64 B.C. L. Rev. 253 (2023) | **In hand (shelf); TOC, abstract and Part II §§ A–B read 23 Aug**; Parts III–V unread — the state-by-state survey awaits [for legislators § 4](../standards/for_legislators.md) | comparative § 5 |
| Lyness — read-status upgrade, same evening | **Part III read in full** (the ten-state survey, pp. 277–93); Parts IV–V remain unread | [for legislators § 4 build-out](../standards/for_legislators.md); the fatals pass |
| Hustis & Gotanda, 25 Loy. U. Chi. L.J. 169 (1994) | **In hand (shelf); title pages and introduction read 23 Aug**; body unread | comparative § 5 |
| CRS-type report, "Enforcement of Federal Pollution Control Laws" | **In hand (shelf); unread** — nothing cites it yet | — |
| DLA Piper, *AI Laws of the World* handbook | **In hand (shelf); unread** — nothing cites it yet | — |
| Binns, "Algorithmic Accountability and Public Reason" | **In hand (shelf); unread** — nothing cites it yet | — |

### The shelf — instruments held in the project library, outside the repository

*Added 23 August. Copyrighted and evidentiary files never enter the public repository; they are
held in a private library folder. This list exists so the repository knows what the project holds
without anyone opening the folder. One row per file; read-status lives in the tables above.*

*The library was reorganised on 24 August under a prefixed reference scheme (BILL / ARTICLE /
REPORT / HEARING / RECORD / LETTER / PRESS / NOTES / EVIDENCE), with an index file inside the
folder and duplicates quarantined; rows below carry the new names. One defect fixed in the same
pass: this table listed the Virginia SB 384 substitute twice.*

| Held | What it is |
|---|---|
| LETTER_15-State-AG_OpenAI-preservation_2026-08-03.pdf | The preservation demand, five pages |
| LETTER_Casar-Khanna-to-Anthropic_2026-08-10 (primary PDF + ⚠ R extract) | The seventeen-question oversight letter; response was due 24 Aug |
| LETTER_Warren-to-Hegseth_Grok-classified_2026-03-15 (⚠ R extract; primary URL held) | Grok-in-classified-systems objections |
| LETTER_Ossoff-plus-5-to-Hegseth_Grok-DoD_2026-02-09 (⚠ R extract; primary URL held) | The six-senator deployment-review letter |
| ARTICLE_Diamantis_Employed-Algorithms_72-Duke-LJ-797_2023.pdf | Diamantis, 72 Duke L.J. 797 (2023) |
| ARTICLE_Lyness_State-Environmental-RCO_64-BC-L-Rev-253.pdf | The federal and state doctrine survey |
| ARTICLE_Hustis-Gotanda_Designated-Felon_25-Loy-U-Chi-LJ-169_1994.pdf | The 1994 enforcement-wave record |
| ARTICLE_Binns_Algorithmic-Accountability-Public-Reason.pdf | Unread; shelf only |
| ARTICLE_Approval-Regulation-Frontier-AI_AIES_2024-07.pdf | Carpenter & Ezell (Harvard), identified 24 Aug; unread beyond first page |
| ARTICLE_Frontier-AI-Regulation-What-Form_Front-Pol-Sci_2025-03-20.pdf | Radanliev (Oxford), identified 24 Aug; open access |
| BILL_CA-SB53_enrolled_LegiScan.pdf | Primary chaptered text |
| REPORT_AI-Futures_AI-2040-Plan-A_2026.pdf | The Plan A report, ~47k words |
| REPORT_AI-Futures_Model-supplementary-materials_2026.md | Parameter estimates and rationales, ~38k words |
| REPORT_AI-Futures_AI-2027_2025-04.pdf | The 2027 scenario; extract short — flagged |
| RECORD_WhiteHouse_Americas-AI-Action-Plan_2025-07-23.pdf | The Action Plan, primary |
| BILL_CT-SB2_2025_text_R04.pdf + _bill-analysis.pdf | Connecticut S.B. 2 (2025), file copy + official analysis |
| BILL_CO-SB25B-004_signed-act_2025-08.pdf | The Colorado delay act, signed — a scan, no text layer |
| BILL_CO-SB25B-004_fiscal-note.pdf | Its final fiscal note (LCS, 10 Sep 2025) |
| BILL_TN-HB0849_chaptered_2025.pdf | Public Chapter 781 (S.B. 837) — the Tennessee personhood act |
| BILL_IL-SB315_enrolled_PA104-0538_LegiScan.pdf | Primary enrolled text, P.A. 104-0538 |
| BILL_CT-SB5_chaptered_PA26-15.pdf | Primary chaptered text |
| BILL_US-HR8094_introduced_2025.pdf | Federal compute-threshold bill, primary |
| BILL_US-S1792_introduced_2025-05-15.xml | Primary bill XML, public domain |
| BILL_VA-SB384_committee-substitute_2026-01-28.pdf | Senate-side IVO architecture (the enacted vehicle was HB 797 — distinct); file identified 24 Aug |
| BILL_TN-SB837-HB849_definitions-extract_2026-08-24_R.md | ⚠ R extract of the personhood definitions; enacted-status unverified; primary retrieval queued |
| REPORT_CRS_Enforcement-Federal-Pollution-Control-Laws.pdf | Unread; shelf only |
| REPORT_CRS-IF13151_Agentic-AI-and-Cyberattacks_2026-07-06.pdf | CRS In Focus, identified 24 Aug; unread; HTML edition exists on congress.gov |
| REPORT_DLA-Piper_AI-Laws-of-the-World_handbook.pdf | Unread; shelf only |
| HEARING_House_CHRG-119hhrg64201_transcript.pdf | Serial 119-42 (DeepSeek/Unitree), read in full 24 Aug |
| HEARING_Shaping-Tomorrow-Future-of-AI_congress-gov.pdf | Serial 119-49, read in full 24 Aug |
| HEARING_Federal-Government-Age-of-AI_congress-gov.pdf | Read in full, 24 Aug (second sitting) |
| RECORD_Congressional-Record_2025-04-01_H1386.pdf | Read in full 24 Aug |
| EVIDENCE_aisi-persona-avatar (withheld from description here) | Evidentiary artefact of the AISI incident's fake persona; never for publication |

*Rule, from the incident that created this section: when a file cites an instrument this table does
not carry, the citation is the defect — add the row before the reliance.*

---

*Owner of this record: nothing else in the repository maintains a competing source list. Argument
files point here. Corrections enter [the errata register](../ledger/errata.md).*
