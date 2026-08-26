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
valuations are softer than market capitalizations.*

---


### Quotation audit, 25 August 2026 — every quote from the day's four intakes checked against source

*Recorded so this never needs repeating. Each quotation now published from the four documents
taken in on 25 August was matched, programmatically, against text extracted from the source PDF
itself, with whitespace, curly quotes and hyphenation normalized.*

**Result: every quotation verified accurate.** No misquotation was found on any published surface.

**Three extraction artifacts caused false alarms, and are noted so a future check is not misread
as a failure:**

1. **Dropped ligatures.** The Javorsky essay's PDF loses the "fi" ligature on extraction, so
   "definitely" extracts as "denitely", "scientific" as "scientic" and "efficacy" as "eÂ©cacy".
   Quotations containing those words will not match a naive string search against extracted text.
   The published wording follows the rendered document, which is correct.
2. **Multi-column interleaving.** *The Lancet* report is three-column and the Kierans paper is
   two-column. A layout-preserving extraction interleaves the columns, so a sentence is broken by
   text from a neighboring column. Extract without layout preservation, or read the rendered
   page, before concluding a quote is wrong.
3. **Footnote intrusion.** In the Lyness article, law-review footnotes interrupt the body text
   mid-sentence on extraction. The misdemeanor quotation at 64 B.C. L. Rev. 298 is split this way
   and is accurate as published.

**Method, for repetition if ever needed:** extract with `pdftotext` (no `-layout` for multi-column
sources), normalize whitespace and quotation marks, then substring-match each published quotation.
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
| **Anthropic** | *Frontier Red Team* — named program | anthropic.com/news/strategic-warning-for-ai-risk-progress-and-insights-from-our-frontier-red-team | 19 Mar 2025 | ✅ |
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
| OpenAI | OpenAI Foundation controls OpenAI Group PBC; "appoints all members of the board of directors of OpenAI Group and can replace directors at any time"; Foundation ≈26%, Microsoft ≈27%, employees and investors ≈47%; recapitalization closed 28 Oct 2025 | openai.com/our-structure | ✅ |
| Anthropic | Delaware PBC; Long-Term Benefit Trust holds Class T stock electing board members, to a majority within four years | anthropic.com/news/the-long-term-benefit-trust (19 Sep 2023) | ⭘ (current trustee composition unconfirmed) |
| Anthropic | $30B Series G at **$380B** post-money, led by GIC and Coatue | anthropic.com newsroom, 12 Feb 2026 | ⭘ |
| xAI | SpaceX combined with xAI, early Feb 2026, ≈$1.25T combined | Bloomberg 2 Feb 2026; CNBC 3 Feb 2026 | ⭘ |
| xAI | "xAI LLC" remains the named developer in its own framework dated 30 Jun 2026 — i.e. a subsidiary/brand within SpaceX, not dissolved | media.x.ai FAIF | ✅ |
| Alphabet | Page 27.1% and Brin 25.2% of voting power ≈ **52.3%**, via ten-vote Class B | Alphabet 2025 proxy statement, beneficial-ownership table | ⭘ |
| Meta | "Because Mr. Zuckerberg controls a majority of our outstanding voting power, we are a 'controlled company'" — Meta's own 2026 proxy, **which prints no percentage** | sec.gov, meta-20260416 | ⭘ |
| Meta | The **≈61%** figure is from a shareholder-proponent Notice of Exempt Solicitation, **not Meta's own disclosure** — cite as approximate with that caveat | sec.gov, r57250px14a6g | ⭘ |
| Microsoft | Single share class, one vote per share; no controlling shareholder; institutional ownership ≈71% (holder percentages secondary) | charter; secondary aggregator | ⚠ on percentages |
| NVIDIA | Jensen Huang, founder and chief executive; market capitalization **$5.213T**, most valuable company | companiesmarketcap.com, Aug 2026 | ⭘ |
| Amazon | Jeff Bezos, founder and executive chair; capitalization topped **$3T** on 3 Aug 2026 | CNBC | ⚠ |
| Oracle | Larry Ellison, founder, reported **40.6%** holder; co-CEOs Magouyrk and Sicilia since Sep 2025; capitalization ≈**$421.9B** | Motley Fool 29 Jul 2026; companiesmarketcap.com | ⚠ on the stake |
| Tesla | Musk largest individual holder at ≈**20%**; no super-voting class; capitalization ≈$1.4T | Motley Fool, 9 Aug 2026 | ⭘ |
| Palantir | Class F founder voting trust (Karp, Thiel, Cohen) engineered to just under half of total voting power regardless of economic stake; capitalization ≈**$412B** (19 Aug 2026) | Palantir 2025 proxy, sec.gov; stockanalysis.com | ✅ (proxy) |
| Databricks | Private; seven co-founders, Ghodsi CEO; **$5B** round closed 13 Aug 2026 at ≈**$190B**, led by Coatue | TechCrunch, 13 Aug 2026 | ⭘ |
| CoreWeave | Public since 28 Mar 2025 (Nasdaq: CRWV); founders Intrator, Venturo, McBee; NVIDIA a shareholder ($2B added Jan 2026); capitalization ≈$48.5B | en.wikipedia.org; companiesmarketcap.com | ⚠ |

## 3. Compute

Training-compute figures for current flagship models are **not disclosed by any developer**. The
figures this project uses are Epoch AI estimates, taken from the dataset files held by the project
(CC BY 4.0; citation at [the models file](./frontier_models.md)), not from web summaries.

**Standing caution.** Two separate web retrievals of Epoch's published figures returned
*different* mantissas for the same models (Grok 3 at 3.5 × 10²⁶ vs 4.6 × 10²⁶; GPT-4.5 at
2.1 × 10²⁶ vs 3.8 × 10²⁶). The dataset files in hand are therefore the authority for any figure
this project publishes, and no precise FLOP figure should be taken from a summarized fetch.
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
12 Feb 2026) and OpenAI ≈**$500B** implied at the October 2025 recapitalization. The higher
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
comparison table labeled H.R. 9917 the "FRONTIER vehicle" when H.R. 9917 is the **AI Kill
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
| FRONTIER Act, H.R. 9925, § 9 | Characterized; full-text read unrecorded | the record; [standing watch](../audit/standing_watch_2026-08-20.md) |
| *United States v. Park*, 421 U.S. 658 (1975) | Three burden passages **verified against the reported opinion, 22 Aug** (prima facie at 673–74; impossibility at 672–73; the two burdens at 673); full-opinion read pending before CURE 8 lands | [CURE 8](../audit/v3_5_cure_language.md); companion notes |
| 18 U.S.C. § 1365(h)(3)–(4) | **Verified verbatim, 23 Aug; upgraded 25 Aug** — the LII page and its notes are now held as PDFs on the shelf, so the citation rests on a held primary rather than a single web read. Re-checked against the held copy: (h)(3) *"a substantial risk of death; extreme physical pain; protracted and obvious disfigurement; or protracted loss or impairment of the function of a bodily member, organ, or mental faculty"*, (h)(4) as drafted. Source of the section: Pub. L. 98–127 § 2 (13 Oct 1983), as amended through Pub. L. 107–307 (2002) | CURE 1 and its addendum |
| 21 C.F.R. § 803.3(w) | **Verified via the live eCFR** | SEC. 1(b)(8); the CURE 1 addendum |
| S. 1792 (119th), AI Whistleblower Protection Act | **Primary XML read in full, 23 Aug** — public domain; held on the shelf below | [who has to tell you § 4b](../standards/who_has_to_tell_you.md); census queue |
| 42 C.F.R. § 73.19 (select-agent theft/loss/release notification) | **Retrieved 23 Aug** (eCFR, ⚠ R) | [the gallery's escape section](../standards/the_same_conduct.md); who has to tell you § 4b |
| 7 U.S.C. § 7734 (Plant Protection Act penalties) | **Retrieved 23 Aug** (uscode.house.gov, ⚠ R) | the gallery's escape section |
| *United States v. Morris*, 928 F.2d 504 (2d Cir. 1991) | **Key holdings retrieved 23 Aug** (Justia, ⚠ R); full-opinion human read pending | the gallery's escape section |
| DOJ release, Jensen guilty pleas (D. Colo.) | **Retrieved 23 Aug** (justice.gov, ⚠ R) | the gallery's escape section |
| NPR, Schmidt sentencing (6 Dec 2017) | **Retrieved 23 Aug** (⚠ R) | the gallery's escape section |
| NY S 10456 (Gounardes, 15 May 2026) | **Primary full text in hand, 23 Aug** (one-section bill, nysenate.gov page supplied) — fixes RAISE's citation: GBL Article 44-B, ch. 96 of 2026 | census queue |
| 42 C.F.R. § 73.11 (select-agent security plans) | **Elements summarized from the eCFR, 23 Aug** (⚠ R); full-text read pending before any quotation beyond the summarized elements | [the fatals pass](../audit/v3_5_cure_language.md) (CURE 10, CURE 7) |
| Idaho H.B. 720 (2022), Idaho Code § 5-346 | **Operative sentence retrieved verbatim, 23 Aug** (legislature.idaho.gov PDF, ⚠ R) | CURE 19 |
| Utah H.B. 249 (2024) | Identified via Liebman extract; text not opened | CURE 19 |
| Tennessee SB 837 / HB 849 (114th G.A.) | Identified (trackbill; local coverage); **enrolled text not in hand** — capitol PDF blocks automated retrieval; pull manually | CURE 19 |
| Liebman, 61 Wake Forest L. Rev. 115 (2026) | Extract retrieved 23 Aug (⚠ R); full PDF wanted for the shelf | CURE 19 |
| H.R. 8094 (119th), AI Foundation Model Transparency Act of 2026 | **Primary read in full (16 pp.), night of 23–24 Aug** — introduced print on the shelf | census; [the definition](../docs/the_definition.md) |
| Lyness — second upgrade | **Parts IV–V read in full, same night** — the whole article is now read | comparative § 5 addendum; for legislators § 4 |
| The Next Web / Politico, OpenAI's SB 53 amendment request | **Read 25 Aug.** Named-source journalism; the amendment text itself is not in hand. Cited for the requested scope and the quoted definition of covered conduct | OQ2 donor note; press corpus; standing watch |
| CSIS, Mehta, "Out of Bounds" (24 Aug 2026) | **Read in full 25 Aug.** Signed commentary by a named director. Cited for: the 50-deaths / $1bn thresholds; "unclear whether any existing U.S. law requires reporting"; the detection gap; the third-party evaluation environment; Kimi K3 and the UK AISI environment | census; known objections; standing watch; press corpus |
| Courthouse News, Meta reduction-in-force ruling (24 Aug 2026) | **Read 25 Aug.** Court reporting; the docket and order are not in hand. Cited only for Judge Orrick's quoted remarks and the plaintiffs' pleaded allegations | known objections; press corpus |
| Daily Montanan, Montana SB 25 challenge (25 Aug 2026) | **Read 25 Aug.** The commissioner's declaration is held as a PDF in the library; the pleadings are not | standing watch; press corpus |
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
| NY FOCUS Act (Gounardes, introduced 21 Aug 2026) | **Primary read in full 25 Aug** — drafting commission print 16298-02-6-1 (19 Aug) held on the shelf. Word test run and recorded: nil for *officer*, *director*, *executive*, *misdemeanor*, *felony*; the sole *natural person* is a data-protection carve-out; attestation and the knowing-violation standard both attach to the provider. Cited for: the registration and independent-study duty; § 39 enforcement; the finding that RAISE's surviving author wrote the same absence twice | census; press corpus § 6 |
| H.R. 9333 (119th), AI Flaw Reporting and Security Enhancement Act | **Primary read in full (7 pp.), 25 Aug.** The GPO print's font encoding defeats text extraction; recovered by 300 dpi OCR and **cross-checked line by line against the govinfo bulk XML**, which confirmed § 2(e)(2) word for word. OCR artifacts corrected (*intelhgence*, *eases*, *pubhe*, *eroups*, *Edueation*, *(¢)*) are named in the library reading note. Cited for: the harm-and-intent-independent definition of "artificial intelligence flaw"; the national database; the nil result on *officer*, *certify*, *signature*, *penalty* | census; [who has to tell you § 4b](../standards/who_has_to_tell_you.md); open source packet |
| Longpre, Zhu, Ezell & Ghosh et al., *FLARE-AI* (arXiv:2606.31567, ICML 2026) | **Read 25 Aug** — abstract, §§ 1, 3, 4.5, 5, 6 and Appendix A.4 in full; §§ 4.1–4.4 and Appendices B–D skimmed for structure. Cited for: "flaw reporting for AI is decades behind"; "an ecosystem coordination tool rather than a compliance reporting tool"; the § 4.5 strict-liability gap; the 49 experts across 32 organizations. Ghosh was written to 25 Aug; no connection implied and he is not a supporter | who has to tell you § 4b; open source packet; outreach |
| Zhao, "AI's top startups are barely publishing their research", *Science* (27 Jul 2026) | **Read in full 25 Aug.** ⚠ secondary reporting a **bioRxiv preprint of 16 July that this project has not opened** — every figure carries that grade. Cited for: 317 unicorns, 2,077 publications, more than half with none, top 5% holding 90%+ of citations, OpenAI's eight prolific researchers; Ioannidis's question; Pierson's acceleration sentence; Ghosh's "blogification" point | press corpus § 5; known objections (acceleration); open source packet |
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

*The library was reorganized on 24 August under a prefixed reference scheme (BILL / ARTICLE /
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
| BILL_US-HR9333_introduced_2026-06-18.pdf | The GPO introduced print, seven pages; OCR'd and XML-checked |
| BILL_NY-FOCUS-Act_Gounardes_LBDC-16298-02-6-1_2026-08-21.pdf | The drafting commission print, dated 19 Aug; the sponsor's own copy |
| BILL_US-18USC1365_Tampering-with-consumer-products_LII_2026-08-25.pdf (+ LII notes) | The donor statute for CURE 1's injury tier, held as primary |
| REPORT_CRS-RS22477_Sponsorship-and-Cosponsorship-of-House-Bills_2025-08-14.pdf | CRS, Oleszek; sponsor and cosponsor mechanics in the House |
| ARTICLE_Longpre-Ghosh-et-al_FLARE-AI_arXiv-2606.31567_2026-06-30.pdf | The ICML 2026 flaw-reporting paper, 20 pp. plus appendices |
| PRESS_Science_Zhao_AI-unicorns-barely-publishing_2026-07-27.pdf | *Science* news, 27 Jul 2026; copyrighted, never republished |
| NOTES_Reading_HR9333-FLARE-Science_2026-08-25.md | The project's own reading note for the three above, quotations extracted verbatim |
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
| HEARING_US-Senate-Judiciary-Crime_Too-Big-to-Prosecute_S-Hrg-119-202_2025-07-16.pdf | **Read in full 25 Aug.** Body text (PDF pp. 1-31) recovered by a validated character decode of the shifted font encoding and quote-in-hand; appendix (PDF pp. 32-103) has no text layer and was read by OCR at the images' native 150 ppi, graded and **not publication-grade**. Decode map and artifact register in the reading note. The separate govinfo `-add1.pdf` package of submitted letters and statements is **not held** |
| HEARING_US-Senate-Commerce-Science_Less-Hype-More-Help_S-Hrg-119-505_2026-03-03.pdf | **Read in part 25 Aug.** Four witnesses' spoken statements and Giannikopoulos's prepared statement decoded and read; ten senators' statements and Mark Muro's (Brookings) prepared statement **unread**. S. Hrg. number confirmed 25 Aug from the congress.gov landing page |
| BILL_NY-S1169-B_Gonzalez_NY-AI-Act_LegiScan-PARTIAL-4of12_2025-01-08.pdf | **Incomplete capture: 4 pages of 12.** Sections 106-115 unopened, including section 110 "Audits". What is in hand settles that the bill is an algorithmic-discrimination act amending the civil rights law, not a frontier-audit bill, and that Gounardes is a co-sponsor. **Re-save owed** |
| REPORT_Reinvent-Albany_NY-Senate-confirmation-vote-transparency_2025-12.pdf | Read 25 Aug for the passages cited. Clean text layer. Third-party, about confirmations rather than bills; carried into the census retrieval program as a caution only |
| BILL_US-S3699_Booker_Body-cameras-immigration-enforcement_introduced_2026-01-27.pdf | Cover and introduction line read 25 Aug. **Not an AI instrument.** Held only as evidence of a Senator's legislative interest; must never be cited as an AI precedent |
| NOTES_Reading_SHrg119-202_Too-Big-to-Prosecute_2026-08-25.md | The citation set for the hearing, graded quotation by quotation, with the decode map at the top so no quotation has to be re-derived |
| NOTES_Reading_New-intakes-batch-2_2026-08-25.md | The same discipline for the other four intakes of 25 Aug |
| HEARING_US-Senate-Judiciary-Privacy_Hidden-Harms-Meta-child-safety_S-Hrg-119-255_2025-09-09.pdf | **Read in part 25 Aug.** Direct GPO download, intact text layer, no decode or OCR needed. Opening statements and the examination of both witnesses read and quoted; **prepared statements (printed pp. 37, 44), responses to written questions (pp. 50, 68) and the appendix (p. 87) unread**. Sworn allegation, not adjudicated fact; the company was not a witness |
| HEARING_US-Senate-Commerce-Science_AIve-got-a-plan_S-Hrg-119-284_2025-09-10.pdf | **Read in part 25 Aug.** Direct GPO download, intact text layer. The preemption exchange and the framework's five parts read and quoted; **fourteen senators' statements, the full prepared statement, the appendix letters and all five sets of written responses unread** |
| HEARING_US-Senate-Judiciary-Privacy_AI-generated-deepfakes_S-Hrg-119-171_2025-05-21.pdf | **Catalogued only, 25 Aug.** Contents and witness list read; body unread; nothing in the repository relies on it |
| BILL_NY-S1169-B_Gonzalez_NY-AI-Act_NY-Assembly-FULL-12pp_2025-01-08.pdf | **Read in full 25 Aug**, from the New York Assembly's own bill-text service. Replaces the four-page LegiScan capture, which is in `_to_delete/`. Word test run on the whole text; §§ 109, 110, 111, 114 read and quoted. Status ("Engrossed - Dead") still unverified |
| RECORD_congress-gov_S-Hrg-119-505_landing-page_2026-08-25.pdf | The congress.gov landing page for the March 2026 Commerce hearing. Its only load-bearing use is confirming the hearing number, S. Hrg. 119-505, which the hearing PDF's own display font would not yield |
| PRESS_Anthropic_Detecting-and-preventing-distillation-attacks_2026-02-23.pdf | The developer's own publication of 23 Feb 2026, already relied on at `docs/known_objections.md`; the file itself is now on the shelf rather than the claim resting on coverage. **Read status: not yet read in full** |
| RECORD_AL-AG_Subpoena-Duces-Tecum-26-0007_OpenAI-OpCo_2026-08-24.pdf | **The instrument itself, read in full 25 Aug ✅.** 17 pages, from the Attorney General's own site. Addressed to OpenAI OpCo, LLC c/o its General Counsel, under § 8-19-9 Code of Alabama. **Not addressed to any natural person.** Requests 1, 8, 9, 13 and 14 quoted verbatim in the enforcement record. Return date not legible in the copy held and is not asserted |
| LETTER_15-State-AG_to-Altman_preservation-and-cease-desist_IOWA-PRIMARY_2026-08-03.pdf | Iowa's own copy of the fifteen-state letter, from iowaattorneygeneral.gov. **Addressed to "Sam Altman, CEO"** and listing all fifteen states. A second capture of an instrument already held; kept because it is the issuing office's copy |
| OpenAI blog post, *Hugging Face model evaluation security incident* | ⚠ **NOT HELD, and now a first-priority retrieval.** Alabama's subpoena defines the "July 2026 Intrusion" by reference to it as it existed on 6 Aug 2026 |
| Hugging Face, *Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident* | ⚠ **NOT HELD, and now a first-priority retrieval.** The subpoena's other defining reference, as it existed on 19 Aug 2026 |
| PRESS_Quartz / PRESS_LinkedIn-Solaris, Altman served onstage, Nov 2025 | ⚠ Secondary, and about a **different matter**: a witness subpoena from the San Francisco Public Defender's Office in the Stop AI prosecution. Filenames carry DIFFERENT-MATTER for that reason. Not evidence of anything about Alabama |
| PRESS_Reddit-threads_…_LOW-GRADE.pdf | **Not a source.** Two comment threads. Held only because they surfaced the two primary URLs the subpoena is defined by. Nothing may be cited to them |
| Alabama AG press release, 24 Aug 2026 (alabamaag.gov) | **Read in full 25 Aug**, from the office's own site. Primary for the subpoena announcement, the authority cited, the conduct alleged, and the Attorney General's quoted words. ✅. **The subpoena itself is not public and nothing may be attributed to its text** |
| TechCrunch, 24 Aug 2026, on the Alabama subpoena | ⚠ Secondary. Sole source for OpenAI's quoted response and for the link back to the fifteen-state letter. Not sought from OpenAI directly |
| NOTES_Reading_Three-more-hearings-and-S1169-full_2026-08-25.md | The citation set for this batch, with the word test and the § 110 and § 114(2) quotations |
| EVIDENCE_aisi-persona-avatar (withheld from description here) | Evidentiary artifact of the AISI incident's fake persona; never for publication |
| RECORD_9Cir_US-v-Hanousek_176-F3d-1116_1999_WEST-REPORTER-PRINT-with-pagination.pdf | **The West reporter print, pp. 1116–1126, with real page numbers on every page. Read in full 26 Aug ✅.** The only source on the shelf that can settle an F.3d pincite. Settled *Hanousek*'s: holding at **1121**, due process and *Dotterweich* at **1122**, the roadmaster at **1119**, and a second differently worded statement of the holding in CONCLUSION at **1126** |
| RECORD_9Cir_US-v-Hanousek_176-F3d-1116_1999_Justia.pdf + `..._CourtListener-Harvard-scan.pdf` | Two independent text copies, used to confirm the West print character for character. **Neither carries star pagination** ([E47](../ledger/errata.md)) |
| RECORD_SCOTUS_Hanousek-v-US_No-99-323_Solicitor-General-brief-in-opposition.pdf (+ DOJ landing page; `_DUPLICATE` copy) | The United States' brief opposing certiorari. Unread |
| RECORD_SCOTUS_Hanousek-v-US_528-US-1102_cert-denied_LII-syllabus.pdf | The cert denial, carrying Thomas, J., dissenting from denial. Read for the quoted sentence only |
| RECORD_9Cir_US-v-Weitzenhoff_35-F3d-1275_amended-opinion_STAR-PAGINATED-1279-1299.pdf | **The amended opinion of 8 Aug. 1994, with continuous star pagination 1279–1299. Read 26 Aug ✅.** Carries the public-welfare holding at **1286**, the footnote answering *Ahmad* at **1286 n.7**, and the five-judge dissent from the order rejecting rehearing en banc at **1293–1299**. Saved that morning under `..._PARTIAL-star-pagination` on a check that found the first marker and stopped; renamed on reading ([E51](../ledger/errata.md)) |
| RECORD_SCOTUS_US-v-Balint_258-US-250_1922_US-Reports-LoC-scan.pdf | **U.S. Reports, Library of Congress scan, pp. 250–254. Read in full 26 Aug ✅**, running-head pagination confirmed page by page; settles the 252–53 pincite |
| RECORD_SCOTUS_Ruckelshaus-v-Monsanto_467-US-986_1984_WIPO-Lex_NO-usable-pagination.pdf | **Text read 26 Aug ✅; pincite 1003–04 still unconfirmed.** The figures that look like page markers are the dissent's own cross-references ("ante, at 1007, n. 11"), which is exactly the [E47](../ledger/errata.md) trap, walked into while checking for it. **A paginated copy is still a retrieval** |
| RECORD_1Cir_US-v-MacDonald-Watson_933-F2d-35_1991_NO-star-pagination.pdf | **Text read 25 Aug ✅; pincites 55, 51, 52 n.15 remain the secondary source's** ([E47](../ledger/errata.md)). A paginated copy is a Tier 1 retrieval |
| RECORD_3Cir_US-v-Johnson-and-Towers_741-F2d-662_1984_FindLaw.pdf (+ second copy) | The Third Circuit's outlier rule on knowledge of the permit requirement. **Unread** |
| RECORD_10Cir_US-v-Iverson_No-14-8071_2016_WRONG-IVERSON-NOT-OUR-CASE.pdf | ⚠ **Not our case.** Ours is 162 F.3d 1015 (9th Cir. 1998); this is a Tenth Circuit case of the same surname, retrieved by mistake. **Kept, with the warning in the filename**, because this shelf has a demonstrated failure mode around surnames |
| ARTICLE_Water-Law-Review_Snyder_case-note-US-v-Iverson-162-F3d-1015_1999.pdf | A 1999 case note. **Secondary; the *Iverson* opinion print is still not held** |
| RECORD_SCOTUS_Morissette-v-US_342-US-246_1952_US-Reports-print.pdf | The public-welfare category and the bargain at 256. Held; read for the cited passage |
| RECORD_SCOTUS_Cedar-Point-Nursery-v-Hassid_594-US-139_2021_Justia.pdf | The per se takings limb, now also CURE 25's question. **Unread** |
| RECORD_SCOTUS_Trump-v-Slaughter_No-25-332_SLIP-OPINION_OT2025.pdf | The slip opinion, OT2025. Bears on whether SEC. 3's independent-commission Agency still travels. **Unread** |
| RECORD_9Cir_Joffe-v-Google_11-17483_Street-View-wiretap_2013-12-27.pdf | Acquired unrequested with the criminal batch. Nothing relies on it |

*Rule, from the incident that created this section: when a file cites an instrument this table does
not carry, the citation is the defect — add the row before the reliance.*

### The 26 August retrieval — thirty-nine documents, and what each copy cannot do

*A second retrieval run delivered thirty-nine sources on 26 August 2026. They are listed here by
what they settle and what they do not, because on this shelf that is the only fact about a copy that
changes an argument. The run's own log is `NOTES_Retrieval-log_second-agent-run_2026-08-26.md` in
the library.*

| Held | What it is, and its limit |
|---|---|
| *Ahmad*, 101 F.3d 386 — law.resource.org | ✅ **Read in the opinion 26 Aug.** The objection the criminal lane called unanswerable, in its own words at last. ⚠ **No star pagination**, so nothing may be pincited to it |
| *Iverson*, 162 F.3d 1015 — law.resource.org | The real *Iverson* at last, after a Tenth Circuit namesake was retrieved by mistake. ⚠ **No star pagination**; 1026 and 1024 stay the secondary source's. ⚠ **162 F.3d 1015 is a shared citation** — the first candidate under it is *Sementilli v. Trinidad Corp.* |
| *MacDonald & Watson*, 933 F.2d 35 · *Johnson & Towers*, 741 F.2d 662 · *Bank of New England*, 821 F.2d 844 · *Jewell*, 532 F.2d 697 · *Cincotta*, 689 F.2d 238 · *Veeck*, 293 F.3d 791 — all law.resource.org | Held, unread. ⚠ **None carries star pagination.** Six opinions that can confirm text and cannot confirm a page ([E47](../ledger/errata.md)) |
| *Ruckelshaus v. Monsanto*, 467 U.S. 986 — **LoC U.S. Reports scan, 39 pp.** | ✅ **Read, and it settled the 1003–04 pincite** the WIPO Lex copy could not. **The single most valuable file in the batch** |
| *Balint* · *Global-Tech* · *South Dakota v. Dole* · *Pennhurst* · *Kentucky v. Dennison* · *Energy Reserves* · *Connecticut v. Doehr* · *Rummel v. Estelle* — LoC / govinfo U.S. Reports | Held, unread. ✅ **All carry real U.S. Reports pagination and can settle their own pincites** |
| *Cedar Point* · *Trump v. Slaughter* · *National Pork Producers* · *Sveen v. Melin* · *Liu v. SEC* — supremecourt.gov slip opinions | Held, unread. ⚠ **A slip opinion carries slip pages, not U.S. Reports pages.** None of these can settle a U.S. pincite |
| *In re Caremark*, 698 A.2d 959 | Held, unread. ⚠ **A Thomson Reuters/Westlaw reprint with KeyCite headers, hosted by a law school — not an official court print.** Whether it may settle 971 is a question for whoever reads it |
| *SEC v. Jensen*, **835 F.3d 1100** (No. 14-55221) — the Ninth Circuit's own PDF | Held, unread. **The reporter citation this project did not have.** The "no-fault clawback" claim at n.18 stays uncited until it is read |
| *Florida v. OpenAI* — the filed-stamped complaint, 83 pp. | Held, unread. Circuit Court, Tenth Judicial Circuit, Highlands County, against the OpenAI entities **and Sam Altman personally** |
| *Wistisen v. Alibaba* · *Kadrey v. Meta* · *Concord Music v. Anthropic* · *X.AI v. Weiser* | ⚠ **Docket metadata stubs, not docket sheets.** Caption, number, court and filing date confirmed against the CourtListener RECAP index; the sheets themselves need PACER or a manual pull |
| U.S.S.G. Manual 2025, 553 pp. — ussc.gov | ✅ **The Manual print § 5G1.2(d) was archive-pinned against.** Held, unread |
| W. Va. Constitution — wvlegislature.gov | ⚠ **Whole-document capture, not art. III § 5 alone**; the clause is present in it. **One of the two constitutional texts the retrieval list called the quiet scandal.** The other, Ind. Const. art. 1 § 16, is **still not obtained** |
| H.R. 9917 · CA SB 1047 (enrolled) · CT SB 5 (second copy) | Held. ⚠ **SB 1047's veto message is not captured** and is not on the bill-nav page |
| S. Hrg. 119-202 · 119-505 — govinfo | ⚠ **Second copies, and thinner than the ones already held.** See the finding below |
| Desai & Riedl, arXiv:2502.18359 · Florida AG news release | Held, unread / read for the announcement |

**And a finding about S. Hrg. 119-202 that changes what its ⚠ means.** The govinfo PDF was fetched
complete, 103 pages, and checked page by page: **pages 1–31 carry a text layer and pages 32–103
carry none at all.** The 197 characters that extract from each appendix page are the Government
Publishing Office's own print-job footer. **The appendix of this hearing has no text layer in the
government's own publication**, so its flag is not a failure to find a better copy; there is no
better copy of that print. Only the `-add1.pdf` package of separately submitted statements would
discharge it, and that is still not held.

*Rule, from the incident that created this section: when a file cites an instrument this table does
not carry, the citation is the defect — add the row before the reliance.*

⚠ **And that rule is broken at scale, stated here rather than discovered later.** A file-by-file
comparison on 26 August 2026 found **180 of the 239 sources on the shelf have no row in this
table.** The rows above cover the criminal-reporter batch and the 26 August retrieval, added because
published text now says those documents are held and the rule requires the row before the reliance.
**The remaining unreconciled files are mostly press, hearing and bill captures from the intake
batches of 24–26 August.** The section's opening promise — that the repository knows what the
project holds without anyone opening the folder — **is false for roughly three quarters of the shelf
until that reconciliation is done.** The library's own index (`_LIBRARY_INDEX.md`, inside the
folder) is complete; this table is the copy that fell behind.

---

*Owner of this record: nothing else in the repository maintains a competing source list. Argument
files point here. Corrections enter [the errata register](../ledger/errata.md).*
