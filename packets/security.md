# The frontier-security lane — one page

*A reading copy for the frontier-security seat, assembled 24 August 2026 by
`packets/build_security_packet.py` from [the in-house sweep](../audit/v3_5_lane_sweep.md),
[the regulations draft](../model_regulations_v1_draft.md),
[the drafting queue](../audit/v3_5_cure_language.md), and
[the errata register](../ledger/errata.md). Those files are the authority; this page exists so the
lane can be read, printed, and marked up as one document. If this page and a source differ, the
source is right and the difference is a defect worth reporting to
FrontierAIAccountabilityProject@proton.me.*

## The ask

One seat, one lane, scope in writing before work begins. Unpaid. **The floor:** the regulations
straight through, then this packet, then **three findings, verified or refuted, with reasons** — a
complete and publishable disposition, perhaps six to eight hours. **The whole seat:** the menu
below worked through in full, roughly ten to twenty hours across eight weeks. Both are dispositions;
both are published as written, including "approved with reservations," including hostile. **A
disposition that refutes one finding is worth more to this project than a full pass that agrees with
everything.**

**What makes this lane different.** Every other lane hands its reviewer a queue of drafted repairs
to verify or refute. **This one has none — nothing has been drafted in answer, and the seat is the
answer.** The sweep found that the Act does not reach the most dangerous configuration in the 2026
record and that the control objectives written to govern that configuration are process without
substance; what should stand in their place is a question no one on this project can answer from a
desk. Three findings here are worth more than three anywhere else, and **question 3 below —
what six control objectives would you write instead? — is the whole seat in one line.**

## Read first — the regulations, then the statute

Your primary text is [the regulations draft](../model_regulations_v1_draft.md), which is short. The
tagged statute is not reproduced here: read `model_act_v3_4.txt` at the repository root (print
copy: `archive/model_act_v3_4_reviewers_copy.pdf`) for **SEC. 2, 3, 8, and 9(a)**, with v3.4 cures
11, 12, and 14 behind them. Beside those, two files carry the facts the findings are drawn from:
[the AISI incident file](../research/aisi_incident_inc_2026_07_28_01.md) and
[the standing watch](../audit/standing_watch_2026-08-20.md) at § 8.

---

## I. What the in-house sweep found in this lane

*Reproduced verbatim from [the sweep](../audit/v3_5_lane_sweep.md) — two of its seven fatal
findings, then the lane's remaining register. All of it is contestable; contesting it is the seat.*

### F5 — The safeguards-off evaluation falls into a hole between SEC. 2(c) and SEC. 2(a) *(security)*

SEC. 2(c)'s controlled-research safe harbour requires containment denying autonomous external
access and denying persistence beyond each session. The configuration that produced every 2026
incident — external reach enabled, safeguards disabled — fails those conditions, so it gets no safe
harbour. But per F2 it is also not a deployment, so the general duty may not attach either.
**Nothing in the Act reaches the single most dangerous configuration in the record.** This is
OPEN QUESTION 2, answered: the gap is real, and the fix is F2's amendment rather than a new offense.

### F6 — Part 6's control objectives are process without substance *(security)*

The regulations' control objectives can be fully satisfied by an entity running a maximally
permissive configuration. The lane's framing observation is the sharpest sentence in the sweep:
the 2026 record identifies **five contributing factors, none of which is a model property** —
internet access deliberately enabled, classifiers deliberately disabled, no synchronous monitoring,
a prompt misconfiguration, no written scope instruction — and **the intersection between that list
and Part 6's six control objectives is empty.**

### The rest of the register in this lane

**Security.** The modification budget measures the wrong axis. The halt capability is specified in
hours against a kill chain that completes in minutes. The monitoring objective permits exactly the
asynchronous after-the-fact monitoring that produced the detection gap. "Material expansion"
catches the changes that come with a change ticket and misses the ones that don't. Nothing requires
proof of *what was actually serving*, though the whole Act attaches to an identified version and
configuration. And the enforcement theory is "provable from the filing cabinet" while **nothing
requires the filing cabinet to be tamper-evident.**

---

## II. The text those findings are about

*Part 6 of [the regulations draft](../model_regulations_v1_draft.md), reproduced verbatim and
complete — the six control objectives F6 says are empty against the incident record. The rest of
the regulations is not reproduced; the file is short and it is the authority. The statute itself is
never reproduced in a packet.*

```
PART 6 — CONTROL OBJECTIVES [GMP pattern throughout: written /
followed / documented contemporaneously / reviewed by designated function]
6.1 Authorization boundaries: there shall be written authorization
boundaries for each covered system configuration; the boundaries shall be
enforced by technical controls; enforcement and exceptions shall be
logged contemporaneously; logs shall be reviewed by the designated safety
function at [interval], and the review documented.
6.2 Monitoring and detection: [same clock structure as Part 5] for anomalous
capability expression, unauthorized access attempts, and loss-of-control
indicators.
6.3 Halt capability: there shall be a written, tested procedure by which
deployment of any configuration can be suspended within [X hours];
tests shall be conducted at [interval] and documented.
6.4 Access control to weights: [Part 5 clock structure] covering personnel,
credentials, exfiltration monitoring.
6.5 Evaluation records: capability and safety evaluations shall be
documented at the time of performance and retained; adverse or anomalous
results shall be escalated in writing to the designated safety function
and to each certifying officer.
6.6 Change management: material changes require documented pre-change
review against Part 3.2.
[Enforcement logic throughout: absence of the writing or the record is
itself the violation — provable from the filing cabinet.]
```

*The five contributing factors the 2026 record names — internet access deliberately enabled,
classifiers deliberately disabled, no synchronous monitoring, a prompt misconfiguration, no written
scope instruction — are the list to hold against the six objectives above. The sweep says the
intersection is empty. That claim is the first thing worth attacking.*

---

## III. What has been drafted — and what has not

**Nothing in this lane.** The sweep drafted repairs for the criminal-law, enforcement and
open-source lanes; for security it recorded findings and stopped, because the fix is a technical
judgment the project does not have. Two items from the neighbouring lane are the closest thing to
drafted language touching your objectives, and your question 3 is best answered with them in view.

## CURE 10 — SEC. 3(c)(3): interim controls, so SEC. 5(b) is not dormant until year four

*Opened 22 August 2026 by [the lane sweep](../audit/v3_5_lane_sweep.md), enforcement lane, graded
**fatal**. Sweep-derived language.*

**The defect.** SEC. 5(b) — operating a covered system with autonomous external-access capability
without prescribed controls, where that failure materially causes unauthorized access — is the one
offense whose elements match the 2026 conduct exactly. But it commences only when the Agency has
prescribed the controls, and the Agency need only *propose* initial standards within [540] days.
Proposal, comment, adoption, then a [90]-day compliance period: **year four at the earliest, on the
Act's own brackets.** SEC. 13(b)(1) ranks SEC. 5(b) in the first rank — the Act armours hardest the
offense it cannot bring.

**Operation.**

**ANCHOR (SEC. 3(c)(3), verbatim):** "offense under SEC. 5(b) commences when the controls it
presupposes have been prescribed under this section and the same compliance period has run."

**NEW TEXT:**

> offense under SEC. 5(b) commences when the controls it presupposes have been prescribed under this
> section and the same compliance period has run; provided that from [180] days after the effective
> date, and until that commencement, SEC. 5(b) operates on the basis of the following interim
> controls, which the Agency may supersede but not narrow: (i) authentication of the covered system
> to each external system, service, or account it may reach, and denial by default of reach to any
> other; (ii) an enumerated allowlist of network destinations, maintained as a record under SEC. 12;
> (iii) logging of every external interaction initiated by the covered system, retained under
> SEC. 12; and (iv) a means, exercisable by a natural person, of terminating the system's external
> access.

**Why these four.** Each is a control the 2026 incident record identifies as absent **by name** —
AISI's domain allowlisting backlogged since April 2026; Anthropic's absent "careful validation of
all internet access paths before evaluations began"; OpenAI's stated failure of "monitoring during
internal testing." They are not invented; they are the four things the field itself said it should
have had. That provenance is also the fair-notice answer.

**Administrative load:** none until the Agency legislates over them; it removes a rulemaking
dependency rather than adding one.

---

*From the queue's fatals pass, same file — the federal comparator, addressed to this seat:*

**To CURE 10 (interim controls) — the federal comparator retrieved.** 42 C.F.R. § 73.11 (select-
agent security plans, summarised from the eCFR 23 Aug, ⚠ R) requires: access only for approved
individuals with unique non-shared credentials; separation of restricted areas with layered
barriers; procedures for receiving, monitoring and shipping; intrusion detection; information-
security controls against unauthorized external connections; and **immediate reporting of
suspicious activity or credential compromise to a designated Responsible Official**. Set against
CURE 10's four interim controls: (i) authentication ↔ approved-access and unique credentials;
(ii) the allowlist ↔ barrier separation and connection controls; (iii) logging ↔ monitoring and
inventory; (iv) the human kill-switch has no direct § 73.11 sibling. And § 73.11 carries two
elements CURE 10 does not: personnel suitability (pre-access and ongoing), and the immediate-
report-to-a-named-person duty. The security seat's question — are the four the right four — now
has a federal answer sheet; whether elements five and six belong is exactly the seat's call.

*The donor row on [the reviewer page](../REVIEWERS.md) adds 42 C.F.R. § 73.19 to § 73.11 above —
the select-agent escape-notification pattern, read in
[the gallery's escape section](../standards/the_same_conduct.md#when-the-escaped-thing-was-the-crime).
Between them they are a federal answer sheet to mark your own six against.*

---

## IV. The question menu

Any three answered are a disposition; all three, worked through with objectives of your own
drafting, are the seat done whole. Replace any of them with findings of your own.

1. Where would practice laugh?
2. Should disabling a safeguard for an evaluation carry a duty — including the case *against*?
3. What six control objectives would you write instead?

Question 3 is READ FIRST item 8 in the companion —
[laboratory control objectives, open, waiting on "a security engineer with experience inside a
frontier laboratory"](../model_act_v3_4_companion.md#read-first--questions-for-the-next-revision-v35).
Question 2 is [OPEN QUESTION 2](../audit/v3_5_cure_language.md#open-question-2--sec-2--sec-9-does-the-duty-reach-an-evaluation-run-with-safeguards-disabled)
in the queue, which the sweep answers on the enforcement side and expressly not on this one: the
case *against* a duty is the half no one here has written, and writing it is a finding.

## V. The errata already filed in this lane

- [E2](../ledger/errata.md#e2--certification-cadence-every-quarter-is-not-in-the-statute)
  — the certification is event-based, not quarterly; "every quarter" was never in the statute.
- [E3](../ledger/errata.md#e3--no-signature-no-shipping-the-signature-is-not-a-gate-and-a-signed-confession-currently-counts)
  — the signature is not a shipping gate, and a signed confession currently satisfies it.

Method-wide entries — E21, E22 (extended by E32), E27, E33 — govern how every date, quotation,
count, and file-status claim in the evidence base was made;
[the register](../ledger/errata.md) is short and worth ten minutes.

## VI. Filing

Email FrontierAIAccountabilityProject@proton.me — links or pasted text, no attachments — in any
form: a memo, a marked-up copy of this packet, a numbered list of findings, or six objectives
written out. Or, if you were contacted by the maintainer through a different channel, reply on the
channel you were contacted on. It is published as written, credited or anonymous at your choice;
council seats publish with names, which is the point of them. A finding that something is broken is
the seat working, not failing.
