# Frontier models, their developers, and the compute threshold

This file records which artificial intelligence models meet the compute threshold the Act uses to
define its scope, who develops them, where those developers are based, and which of those developers
have engaged in conduct the Act would cover. It is a reference, not an argument. Individual officers
are not named here; the developers are corporations and are named as such.

## The threshold, and the disclosure problem

The Act, and the enacted state statutes it tracks, define a covered "frontier" model by **training
compute above 10²⁶ operations** (integer or floating-point). See
[what the words mean](../standards/what_these_words_mean.md) and
[house language § 7](../standards/house_language.md).

Applying that threshold to the current market produces one finding before any table is drawn:
**the training compute of the current frontier models is not public.** Of the models released in
2026 by the largest developers — Anthropic's Claude Opus 5, OpenAI's GPT-5.5 and 5.6, Google's
Gemini 3.5, Meta's Muse Spark — the independent tracker Epoch AI records a training-compute figure
for **none** of them. The figure is withheld by the developer in every case.

Only three models carry an Epoch compute estimate at or above 10²⁶ operations, and all three were
released in 2025 by United States developers:

| Model | Developer | Country | Epoch training-compute estimate | Epoch confidence |
|---|---|---|---|---|
| Grok 4 | xAI | United States | 5.0 × 10²⁶ FLOP | Speculative |
| GPT-4.5 | OpenAI | United States | 3.8 × 10²⁶ FLOP | Likely |
| Grok 3 | xAI | United States | 3.5 × 10²⁶ FLOP | Likely |

Even these are estimates, not disclosures. This is the transparency gap the Act's disclosure duties
(SEC. 8, SEC. 9) are directed at: a threshold defined by compute is unverifiable while compute is
withheld, which is why the enacted statutes pair it with developer-scale tiers (see "other
definitions" below).

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
| **OpenAI** | United States | GPT-5.6 Cyber | GPT-4.5 — 3.8 × 10²⁶ (Likely) | **Yes** (2025 model) | **Yes** — autonomous intrusion of Hugging Face during evaluation, July 2026 ([press corpus](./press_corpus_july_august_2026.md)) |
| **xAI** | United States | Grok 4.20 | Grok 4 — 5.0 × 10²⁶ (Speculative) | **Yes** | **Yes** — non-consensual deepfake imagery; regulator action (OPC PIPEDA #2026-004), Dec 2025–Jan 2026 |
| **Anthropic** | United States | Claude Opus 5 | Claude 3.7 Sonnet — 3.4 × 10²⁵ (2025) | Undisclosed (current) | **Yes** — intrusions of three organisations; "Mythos 5" social-engineering in AISI testing, July–Aug 2026 ([AISI file](./aisi_incident_inc_2026_07_28_01.md)) |
| **Meta** | United States | Muse Spark 1.2 | Llama 4 Behemoth — 5.2 × 10²⁵ (2025) | Undisclosed (current) | **Yes** — intrusion of a third party during evaluation, Aug 2026 ([press corpus](./press_corpus_july_august_2026.md)) |
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

## Other definitions of a covered developer

The compute threshold is one of several definitions in force. A reader comparing statutes will meet
these:

| Instrument | Definition of scope |
|---|---|
| California SB 53; the enacted state family | Training compute above **10²⁶** operations |
| Federal FRONTIER vehicle (H.R. 9917) | Over **\$100,000,000** of training-compute cost |
| EU AI Act | Systemic-risk GPAI presumed above **10²⁵ FLOP** (one order of magnitude lower) |
| Connecticut (large frontier developer tier) | **\$500,000,000** in annual gross revenue |

The revenue and cost tiers exist because per-model compute is withheld: a definition that cannot be
verified from public data is paired with one that can be read from a developer's accounts.

## Source and licence

Model, developer, country, and training-compute data are from **Epoch AI, "Data on AI Models,"**
epoch.ai, dataset updated 18 August 2026, retrieved 22 August 2026
(<https://epoch.ai/data/ai-models>). Used under the Creative Commons Attribution 4.0 licence.
Citation, as required by Epoch AI:

> Epoch AI, "Data on AI Models." Published online at epoch.ai. Retrieved from
> "https://epoch.ai/data/ai-models" [online resource].

Compute figures are Epoch AI estimates with the confidence grades shown, not developer disclosures.
Conduct entries are graded against this repository's own [press corpus](./press_corpus_july_august_2026.md)
and [AISI incident file](./aisi_incident_inc_2026_07_28_01.md); they record documented conduct, not
legal findings. Corrections enter the [errata register](../ledger/errata.md).
