#!/usr/bin/env python3
"""Assemble packets/security.md from the repository's own files.

Run from the repository root:  python3 packets/build_security_packet.py

The packet is a reading copy for the frontier-security seat: the lane's whole apparatus
inlined in reading order. The sources — the sweep, the regulations draft, the queue —
remain the authority. If this page and a source differ, the source is right and the
difference is a defect worth reporting. Regenerate after any edit to the sources.
Stdlib only; deterministic; no network.

This lane is the one with nothing drafted in answer: the seat is the answer. What is
inlined below is therefore the findings, the text they are about, and the federal
comparator the intake retrieved — not a queue of repairs to verify.
"""
import io
import re

SWEEP = "audit/v3_5_lane_sweep.md"
QUEUE = "audit/v3_5_cure_language.md"
REGS = "model_regulations_v1_draft.md"
OUT = "packets/security.md"


def read(path):
    return io.open(path, encoding="utf-8").read()


def section(text, start_heading, stop_prefixes):
    """Return the block from start_heading to the first line opening with any stop prefix."""
    i = text.find(start_heading)
    if i == -1:
        raise SystemExit("missing section: " + start_heading)
    j = len(text)
    for stop in stop_prefixes:
        k = text.find(stop, i + len(start_heading))
        if k != -1:
            j = min(j, k)
    return text[i:j].rstrip() + "\n"


def relink(block, source=QUEUE, home="audit"):
    """The sweep and queue link from audit/; the packet lives in packets/. Both are one
    level below the root, so ../ links written in a source already point at the root's
    siblings and need no change. Intra-file anchors (#cure-…) are re-pointed at the source
    file so they resolve from the packet, and ./-relative links are re-based to the
    source's own folder."""
    block = re.sub(r"\]\(#", "](../" + source + "#", block)
    block = block.replace("](./", "](../" + home + "/")
    return block


sweep = read(SWEEP)
queue = read(QUEUE)
regs = read(REGS)

f5 = section(sweep, "### F5 —", ["### F6 —"])
f6 = section(sweep, "### F6 —", ["### F7 —"])
rest_security = section(sweep, "**Security.**", ["\n**Open source.**"])

part6 = section(regs, "PART 6 — CONTROL OBJECTIVES", ["\nPART 7 —"])

cure10 = section(queue, "## CURE 10 —", ["\n## CURE 11"])
select_agent = section(queue, "**To CURE 10 (interim controls)", ["\n\n**To ", "\n\n### "])

parts = [
    """# The frontier-security lane — one page

*A reading copy for the frontier-security seat, assembled 24 August 2026 by
`packets/build_security_packet.py` from [the in-house sweep](../audit/v3_5_lane_sweep.md),
[the regulations draft](../model_regulations_v1_draft.md),
[the drafting queue](../audit/v3_5_cure_language.md), and
[the errata register](../ledger/errata.md). Those files are the authority; this page exists so the
lane can be read, printed, and marked up as one document. If this page and a source differ, the
source is right and the difference is a defect worth reporting to
FrontierAIAccountabilityProject@proton.me.*

*Arrived here directly? Your lane's table, the terms of the seat, and the other packets are on
[the reviewer page](../REVIEWERS.md); the index of packets is [one level up](./README.md).*

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

""",
    relink(f5, SWEEP),
    "\n",
    relink(f6, SWEEP),
    "\n### The rest of the register in this lane\n\n",
    relink(rest_security, SWEEP),
    """
---

## II. The text those findings are about

*Part 6 of [the regulations draft](../model_regulations_v1_draft.md), reproduced verbatim and
complete — the six control objectives F6 says are empty against the incident record. The rest of
the regulations is not reproduced; the file is short and it is the authority. The statute itself is
never reproduced in a packet.*

```
""",
    part6.rstrip() + "\n",
    """```

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

""",
    relink(cure10),
    "\n*From the queue's fatals pass, same file — the federal comparator, addressed to this seat:*\n\n",
    relink(select_agent),
    """
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
""",
]

io.open(OUT, "w", encoding="utf-8").write("".join(parts))
print("PACKET BUILT:", OUT, len("".join(parts)), "chars")
