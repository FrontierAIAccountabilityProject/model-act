---
title: "Frontier models, their developers, and the compute threshold"
parent: Appendix
nav_order: 6
---

# Frontier models, their developers, and the compute threshold

This file records which artificial intelligence models meet the compute threshold the Act uses to
define its scope, who develops them, where those developers are based, and which of those developers
have engaged in conduct the Act would cover. It is a reference, not an argument. Individual officers
are not named here; the developers are corporations and are named as such.

## The threshold, and the disclosure problem

The Act, and the enacted state statutes it tracks, define a covered "frontier" model by **training
compute above 10²⁶ operations** (integer or floating-point). See
[what the words mean](../authorities/glossary.md) and
[house language § 7](../authorities/house-style.md).

Applying that threshold to the current market produces one finding before any table is drawn:
**the training compute of the current frontier models is not public.** Of the models released in
2026 by the largest developers — Anthropic's Claude Opus 5, OpenAI's GPT-5.5 and 5.6, Google's
Gemini 3.5, Meta's Muse Spark — the independent tracker Epoch AI records a training-compute figure
for **none** of them. The figure is withheld by the developer in every case.

Only three models carry an Epoch **point estimate** at or above 10²⁶ operations, and all three were
released in 2025 by United States developers. (Stated as point estimates deliberately: Epoch's
tentative *range* for Claude Opus 4 — 5 × 10²⁵ to 2 × 10²⁶ — crosses the threshold at its upper
bound, so a range-based count would not be three. The reconciliation, and the standing caution that
web retrievals of Epoch's figures disagree with the dataset in hand, are in
[the verification record](./verification-record.md) § 3.)

| Model | Developer | Country | Epoch training-compute estimate | Epoch confidence |
|---|---|---|---|---|
| Grok 4 | xAI | United States | 5.0 × 10²⁶ FLOP | Speculative |
| GPT-4.5 | OpenAI | United States | 3.8 × 10²⁶ FLOP | Likely |
| Grok 3 | xAI | United States | 3.5 × 10²⁶ FLOP | Likely |

Even these are estimates, not disclosures. This is the transparency gap the Act's disclosure duties
(SEC. 8, SEC. 9) are directed at: a threshold defined by compute is unverifiable while compute is
withheld, which is why the enacted statutes pair it with developer-scale tiers (see "other
definitions" below).

**External cross-check, added 23 August 2026.** CSIS's August 2026 survey, using Epoch AI's May
2026 census, counts **three** public models above 10²⁶ (Grok 3, Grok 4, GPT-4.5) and roughly
fifteen between 10²⁵ and 10²⁶ — and notes that California's revenue-screened trigger covers, on
that count, exactly two developers (⚠ P, survey in hand; Epoch under CC BY as below). Recorded
beside this file's own table as an independent count, not adopted in place of it; where the two
disagree, the disagreement is the finding.

## The current frontier developers and their flagship models

The table below lists the developers operating at or near frontier scale, their most recent flagship
model as recorded by Epoch AI (data updated 18 August 2026), the country of the developer, the best
available compute estimate, whether that estimate meets the 10²⁶ threshold, and whether the developer
has engaged in conduct the Act would cover. "Undisclosed" means the developer has not published
training compute and no independent estimate exists. Conduct entries cite this repository's own
incident record and are graded; a developer's presence here is not a finding of any crime, which does
not yet exist in law.

| Developer | Country | Latest flagship (Epoch, to 18 Aug 2026) | Highest compute estimate on record | Meets 10²⁶? | Conduct matching the Act |
|---|---|---|---|---|---|
| **OpenAI** | United States | GPT-5.6 Cyber | GPT-4.5 — 3.8 × 10²⁶ (Likely) | **Yes** (2025 model) | **Yes** — autonomous intrusion of Hugging Face during evaluation, July 2026 ([press corpus](./press-corpus.md)) |
| **xAI** | United States | Grok 4.20 | Grok 4 — 5.0 × 10²⁶ (Speculative) | **Yes** | **Yes** — non-consensual deepfake imagery; regulator action (OPC PIPEDA #2026-004), Dec 2025–Jan 2026 |
| **Anthropic** | United States | Claude Opus 5 | Claude 3.7 Sonnet — 3.4 × 10²⁵ (2025) | Undisclosed (current) | **Yes** — intrusions of three organizations; "Mythos 5" social-engineering in AISI testing, July–Aug 2026 ([AISI file](./incident-report.md)) |
| **Meta** | United States | Muse Spark 1.2 | Llama 4 Behemoth — 5.2 × 10²⁵ (2025) | Undisclosed (current) | **Yes** — intrusion of a third party during evaluation, Aug 2026 ([press corpus](./press-corpus.md)) |
| **Google** | United States | Gemini 3.5 Flash | Gemini 1.0 Ultra — 5.0 × 10²⁵ (2023) | Undisclosed (current) | None in this record to date |
| **DeepSeek** | China | DeepSeek-V4-Pro | DeepSeek-V4-Pro — 9.7 × 10²⁴ (2026) | Below (est.) | None in this record |
| **Alibaba** | China | Qwen 3.8 Max | Qwen3-Max — 1.5 × 10²⁵ (2025) | Below (est.) | None in this record |
| **Zhipu / Z.ai** | China | GLM-5.3 | GLM-5 — 6.8 × 10²⁴ (2026) | Below (est.) | None in this record |
| **Moonshot** | China | Kimi K3 | Kimi K3 — 2.0 × 10²⁵ (Speculative) | Below (est.) | None in this record |
| **Tencent** | China | Tencent Hy3 | Hunyuan-TurboS — 5.4 × 10²⁴ (2025) | Below (est.) | None in this record |
| **Mistral** | France | (2025 releases) | Mixtral 8×7B — 7.7 × 10²³ (2023) | Below (est.) | None in this record |

**What the table shows, stated flat.** Every model with a confirmed compute estimate over the
threshold is from a United States developer. The current models of the largest developers do not
publish compute at all. The developers with the highest confirmed estimates — xAI and OpenAI — are
also among the developers with documented conduct the Act would cover. The Chinese developers'
best estimates are below the threshold; whether their current models exceed it cannot be determined
from public data.

## The developers' own designation as frontier

Training compute is undisclosed, but the developers answer the scope question themselves: each of the
largest developers applies the word *frontier* to its own models, safety program, or products, on
its own website. These are published acts by the developer, recorded verbatim.

- **OpenAI.** Its safety policy is the *Preparedness Framework*, described as OpenAI's approach to
  "frontier capabilities"; its public policy agenda has a section headed "Frontier model safety,
  security, and accountability." Its enterprise product is named *OpenAI Frontier*, and it publishes
  "Offering Zero Data Retention for frontier models." (openai.com, accessed 22 Aug. 2026.)
- **xAI.** "Grok 4.6 achieves frontier intelligence across several agentic coding and knowledge work
  benchmarks." (x.ai/news/grok-4-6, 12 Aug. 2026.)
- **Anthropic.** It operates a "Frontier Red Team" that "stress-tests AI systems to understand the
  full extent of their current capabilities," and publishes a "Frontier Safety Roadmap."
  (anthropic.com, accessed 22 Aug. 2026.)
- **Meta.** "Today, we're sharing our Frontier AI Framework, which outlines our consideration of
  risk in our model-release decisions." (about.fb.com, 3 Feb. 2025.) **Renamed in April 2026** the
  *Advanced AI Scaling Framework* v2, which keeps *Frontier AI* as its defined term — "a new or
  substantially modified highly capable general-purpose generative AI model that we are developing
  for deployment" — and adopts the Act's own figure as a criterion: "We trained the model using at
  least 10^26 integer or floating point operations." (ai.meta.com, v2, Apr. 2026.) **The rename is
  the live example of [CURE 6](../revision/proposals.md)'s anti-evasion clause**: a
  holding-out is not undone by later withdrawal, deletion, or amendment, and here the developer
  amended the title while keeping the term and the threshold.
- **Google DeepMind.** "We call our most powerful foundation models 'frontier models'." It also
  publishes a *Frontier Safety Framework*, described as "a set of protocols that ensure our most
  advanced AI models remain reliable, thoroughly tested, and aligned with human values."
  (deepmind.google/frontier-safety, retrieved 22 Aug. 2026. The ⚠ this entry carried is discharged;
  the sentence was opened and reproduced identically on two retrievals — see
  [the verification record](./verification-record.md).)

The inventory is wider than the five operating labs. **Twelve companies have published *frontier*
safety frameworks** (METR's December 2025 inventory, pinned in [the dossier](./dossier.md)):
the five above plus **Microsoft, Amazon, Nvidia, G42, Cohere, Naver,** and **Magic.** Each framework's
use of the word is itself a self-designation. Microsoft's and Amazon's verbatim usages are now pinned
in [the verification record](./verification-record.md); the phrasing for **G42, Cohere, Naver** and
**Magic** is ⚠ to pin from each company's own framework before public use. The scope point holds for
all twelve: each has, in a published document, called its own safety work *frontier*.

> **Two twelves — do not conflate them.** The **framework twelve** above (companies that have
> published a *frontier* safety framework) is a different list from the **coverage set** of twelve
> companies across four layers in [the frontier enterprises](./companies-covered.md). The two
> lists overlap at **eight**: the five developers plus Microsoft, Amazon and NVIDIA. The framework
> twelve evidences self-designation; the coverage set demonstrates the legal category.

Each statement is the developer applying the word *frontier* to its own model, program, or product.
Under a scope definition that reaches a model its developer holds out as frontier (see the proposed
SEC. 1(b)(1) limb at [CURE 6 in the v3.5 queue](../revision/proposals.md)), these are self-executing: the
developer's own published words place the model in scope, with no estimate of its compute required.
These are corporate self-descriptions on the developers' own domains; no individual officer is named.

## Other definitions of a covered developer

The compute threshold is one of several definitions in force. A reader comparing statutes will meet
these:

| Instrument | Definition of scope |
|---|---|
| California SB 53; the enacted state family | Training compute above **10²⁶** operations |
| Federal — AI Kill Switch Act (H.R. 9917) | Over **\$100,000,000** of training-compute cost |
| EU AI Act | Systemic-risk GPAI presumed above **10²⁵ FLOP** (one order of magnitude lower) |
| Connecticut (large frontier developer tier) | **\$500,000,000** in annual gross revenue |

The revenue and cost tiers exist because per-model compute is withheld: a definition that cannot be
verified from public data is paired with one that can be read from a developer's accounts.

## Source and license

Model, developer, country, and training-compute data are from **Epoch AI, "Data on AI Models,"**
epoch.ai, dataset updated 18 August 2026, retrieved 22 August 2026
(<https://epoch.ai/data/ai-models>). Used under the Creative Commons Attribution 4.0 license.
Citation, as required by Epoch AI:

> Epoch AI, "Data on AI Models." Published online at epoch.ai. Retrieved from
> "https://epoch.ai/data/ai-models" [online resource].

Compute figures are Epoch AI estimates with the confidence grades shown, not developer disclosures.
Conduct entries are graded against this repository's own [press corpus](./press-corpus.md)
and [AISI incident file](./incident-report.md); they record documented conduct, not
legal findings. Corrections enter the [errata register](../corrections/corrections.md).
