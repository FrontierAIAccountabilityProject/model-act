# Reading notes — Docket FDA-2024-D-4488

*The public comment file on FDA's January 2025 draft guidance,* Artificial
Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing
Submission Recommendations. *Comments read 20 August 2026 from
regulations.gov; comment IDs and quoted text are the agency's posted versions, which
control. Read because it is the direct predecessor of docket FDA-2026-N-7874, where
this project files — FDA expressly asked in the 2025 notice whether the guidance
adequately addressed emerging technology such as generative AI, and this file is the
public's answer.*

**What this file is not.** Not an authority for the statute; the Act cites none of it.
These are working notes supporting [the comment](./fda_2026_n_7874_comment.md) and the
observations banked in [threads](./banked_threads.md).

---

## 1. The census

Fifty-one comments posted. Of those read here — the twenty-five surfaced on results
page 1, the further comments captured on pages 2–3, and eight attachment letters in
full — the composition is:

| Who filed | Examples read |
|---|---|
| Physician bodies | American Medical Association (0010), American Osteopathic Association (0021), American College of Radiology (0041), Radiological Society of North America (0022), Washington State Medical Association (0026), American Psychological Association Services (0009) |
| Informatics & specialty | American Medical Informatics Association (0046), Digital Pathology Association AI Working Group (0016) |
| Device & platform industry | Amazon Web Services (0018), Wolters Kluwer (0014), Cochlear (0023), 3Shape (0030), Dentsply Sirona (0044), ATEC Spine (0005), Emergo by UL (0040) |
| Trade associations | Consumer Technology Association (0035), Connected Health Initiative (0039), Biocom California (0011) |
| Start-up | Equitable Evidence (0017) |
| Academics & individuals | Elvan Ceyhan, Auburn (0027); Shiau Ru Yang, NCKU Taiwan (0053); SJSU MPDM cohort of ten students with their professor (0028); Kierstin Ikeda (0051); Sharif Hoque (0045); Jitendra Pund; Hadeel El-Amer (0008); John-William DeClaris (0003); Ethan Chupp (0029); Innolitics (0007) |
| Anonymous | 0038 |

**Who did not file.** No comment read here came from a frontier foundation-model
developer. The nearest is AWS, whose comment is a platform intermediary's and says so.
⚠ This is an absence observed across the comments read, not a certified absence across
all fifty-one; the remaining titles were not individually captured. Stated at that
strength wherever used.

---

## 2. What they asked for, by theme

**Transparency and labeling.** The physician bodies want more: mandatory model cards
(AOA), training-data description in labeling including demographics, geography, and
sample size (AOA), graphical user-interface detail in submissions notwithstanding
sponsors' intellectual-property objections (AMA). Industry wants less: model cards in
labeling are "burdensome" and should be dropped (Biocom); exact dataset sizes should be
excluded from model-card examples as confidential (Dentsply, item 13); the relevance of
non-U.S. data should be case-by-case (Dentsply, item 6).

**Validation and subgroups.** Two individuals arrived at the same defect from opposite
ends. Ikeda (0051) attacks the guidance's "reasonable numbers of patients" standard for
unpowered subgroups as undefined and liable to mask disparities in underrepresented
populations, asking for a minimum-sample standard. Dentsply (item 14) says demographic
subgroup analysis is often infeasible in dental imaging because race is not carried in
DICOM headers, and proposes geographic diversity instead. The SJSU cohort asks simply
what level of testing counts. The Digital Pathology Association asks whether unpowered
subgroup analyses will be used in decision-making at all.

**Terminology.** The most-repeated request in the file, from three unconnected
commenters: ATEC Spine (0005) notes "validation data" is not in FDA's own AI glossary
and collides with the ML community's usage; ACR asks for an expanded glossary; Emergo
by UL (0040) says the guidance's attempt to separate "usability" from "human factors
validation" is confusing and should be removed; Ceyhan (0027) asks for a consolidated
terminology section. Four commenters, one complaint: the regulator and the field do not
share a vocabulary.

**Post-market monitoring.** ACR: monitoring is encouraged but not required, and
specific mechanisms — periodic reporting, third-party audits — are not outlined. AOA:
predetermined change-control plans should not be approved without human review of
performance in updates. Digital Pathology Association: Section XI reads as
contradictory — is a monitoring plan an election, an FDA request, or a requirement?
The file's recurring answer to novel risk is a document plus a professional reading it.

**Cybersecurity.** Innolitics (0007) asks whether FDA is aware of any of its seven
listed AI-specific attacks occurring in practice, "since several of them appear
hypothetical," and suggests removing the unlikely ones. Dentsply (items 10–11) asks the
same in trade-association register. AMA asks for *more* — adversarial manipulation
explicitly, per NIST. *Note for the campaign layer: the request for a citation was
answered eighteen months later by a government incident report,
[AISI INC-2026-07-28-01](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing),
in which agents opened a malicious pull request, operated a sockpuppet to review their
own malware, and force-pushed to erase the history.*

**Standards harmonisation.** ISO/IEC 42001 is raised by three independent commenters
(Digital Pathology Association, Hoque 0045, and by implication Biocom's ISO/NIST
alignment request). AWS asks FDA to identify international standards within the risk
assessment. Dentsply asks FDA to cite the IMDRF key-terms document, noting FDA's own
glossary disclaims being guidance.

**The one structural proposal.** Yang (0053), filing from Taiwan in June 2026 — fourteen
months after the comment period closed, which guidance dockets permit under 21 CFR
10.115(g)(5) — proposes distinguishing a device's *measurement claim* from its
*clinical-utility claim* where the two mature at different times, with labeling,
monitoring, and prespecified criteria for expanding or withdrawing the claim. It is the
only comment read here that proposes an architecture rather than an amendment.

---

## 3. The finding

Read as one document, the file answers a single question — *how should the humans
downstream cope?* — and never reaches *who upstream is answerable?*

Three exhibits carry it:

- **The clinician as safety component.** ACR (0041): a qualified radiologist end-user
  "would intrinsically serve as a device risk mitigation," while an unqualified one
  "could not serve in that same capacity." The risk control is a person — positioned
  downstream, after the shipping decision.
- **The clinicians decline the seat.** AOA (0021) reports that 87 per cent of surveyed
  physicians say liability for errors in AI models would affect their adoption, and asks
  HHS to rescind the Section 1557 regulation that made providers responsible for biased
  outcomes of tools they use. They ask for the duty to be moved. No commenter says
  where.
- **The intermediary cannot vouch.** AWS (0018): when models are accessed through its
  platform, AWS "may not be able to offer information on model training data when not
  otherwise disclosed by the model developer." The chain has a link that admits it
  cannot see its own upstream.

Every safety mechanism proposed across the file is a document (model card, label,
manifest, monitoring plan, audit) or a downstream professional (the radiologist, the
site validator, the institution). None is an identified natural person, upstream, whose
signature is required before the thing ships.

## 4. How it maps to the Act

| The file's request | The Act's provision |
|---|---|
| Model cards, training-data disclosure, labeling (AMA, AOA) | SEC. 3 standards duty and SEC. 8 certification — the disclosure has a signer, and the signature is what makes it checkable |
| "Move the liability off physicians" (AOA) | SEC. 4 — duties climb to final material independent decision authority; the end user is expressly not a controlling person |
| Mandatory post-market monitoring, audits, drift triggers (ACR, DPA) | SEC. 9 — reporting on fixed clocks that run from when certified monitoring *would* have detected the event |
| "We cannot see upstream" (AWS) | SEC. 2(b) reliance rule for non-modifying deployers, and SEC. 8's attestation by whoever *can* see |
| Least-burdensome, tier by risk (Biocom, Dentsply, CTA) | Accepted: SEC. 3(b) forbids any prior-approval gate. The duty is documentary and self-executed — which is affordable precisely because someone signs it |
| Claim maturity staged over time (Yang 0053) | SEC. 2 material expansion — a change in what the system may do is the trigger, not a calendar |

---

*Compiled 20 August 2026 from the agency's posted comments. Quotations are verbatim
from the posted text; where any quotation differs from the agency's posting, the
agency's posting controls and a correction here is an erratum for
[the register](../LEDGER.md#part-i).*
