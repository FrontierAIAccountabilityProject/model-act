#!/usr/bin/env python3
"""Assemble packets/enforcement.md from the repository's own files.

Run from the repository root:  python3 packets/build_enforcement_packet.py

The packet is a reading copy for the enforcement-and-prosecution seat: the lane's whole
apparatus inlined in reading order. The sources — the sweep, the queue, the state
enforcement record — remain the authority. If this page and a source differ, the source
is right and the difference is a defect worth reporting. Regenerate after any edit to the
sources. Stdlib only; deterministic; no network.
"""
import io
import re

SWEEP = "audit/v3_5_lane_sweep.md"
QUEUE = "audit/v3_5_cure_language.md"
RECORD = "research/state_enforcement_record_2026.md"
OUT = "packets/enforcement.md"


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
    """The sweep and queue link from audit/, the enforcement record from research/; the
    packet lives in packets/. All three are one level below the root, so ../ links written
    in a source already point at the root's siblings and need no change. Intra-file anchors
    (#cure-…) must be re-pointed at the source file so they resolve from the packet, and
    ./-relative links written in the source must be re-based to that source's own folder."""
    block = re.sub(r"\]\(#", "](../" + source + "#", block)
    block = block.replace("](./", "](../" + home + "/")
    return block


sweep = read(SWEEP)
queue = read(QUEUE)
record = read(RECORD)

f2 = section(sweep, "### F2 —", ["### F3 —"])
f3 = section(sweep, "### F3 —", ["### F4 —"])
f4 = section(sweep, "### F4 —", ["### F5 —"])
rest_enforcement = section(sweep, "**Enforcement.**", ["\n**Security.**"])

oq4 = section(queue, "## OPEN QUESTION 4 —", ["\n## CURE 1 —"])
cure9 = section(queue, "## CURE 9 —", ["\n## CURE 10"])
cure10 = section(queue, "## CURE 10 —", ["\n## CURE 11"])
cure14 = section(queue, "## CURE 14 —", ["\n## CURE 15"])
cure15 = section(queue, "## CURE 15 —", ["\n## CURE 16"])
cure16 = section(queue, "## CURE 16 —", ["\n## CURE 5"])

oq4_colorado = section(queue, "**To OPEN QUESTION 4 —", ["\n\n**To ", "\n\n**Tennessee", "\n\n### "])
select_agent = section(queue, "**To CURE 10 (interim controls)", ["\n\n**To ", "\n\n### "])
cure15_donor = section(queue, "**To CURE 15 (disclose-and-cure)", ["\n\n**To ", "\n\n### "])
cure16_donor_1 = section(queue, "**To CURE 16 (the deception limb)", ["\n\n**To ", "\n\n### "])
cure16_donor_2 = section(queue, "**To CURE 16, a second documented class", ["\n\n**To ", "\n\n### "])

oq4_both_ways = section(record, "## 5. What this record does to OPEN QUESTION 4", ["\n## 6."])

parts = [
    """# The enforcement-and-prosecution lane — one page

*A reading copy for the enforcement-and-prosecution seat, assembled 24 August 2026 by
`packets/build_enforcement_packet.py` from [the in-house sweep](../audit/v3_5_lane_sweep.md),
[the drafting queue](../audit/v3_5_cure_language.md),
[the state enforcement record](../research/state_enforcement_record_2026.md), and
[the errata register](../ledger/errata.md). Those files are the authority; this page exists so the
lane can be read, printed, and marked up as one document. If this page and a source differ, the
source is right and the difference is a defect worth reporting to
FrontierAIAccountabilityProject@proton.me.*

*Arrived here directly? Your lane's table, the terms of the seat, and the other packets are on
[the reviewer page](../REVIEWERS.md); the index of packets is [one level up](./README.md).*

## The ask

One seat, one lane, scope in writing before work begins. Unpaid. **The floor:** the statute
straight through, then this packet, then **three findings, verified or refuted, with reasons** — a
complete and publishable disposition, perhaps six to eight hours. **The whole seat:** the menu
below worked through in full — every question answered, every drafted repair verified or refuted —
roughly ten to twenty hours across eight weeks. Both are dispositions; both are published as
written, including "approved with reservations," including hostile. **A disposition that refutes
one finding is worth more to this project than a full pass that agrees with everything.**

**The arithmetic:** everything below is the menu — four questions, five drafted repairs, and one
held amendment that is the most consequential item in the repository. Any three items are a
complete disposition; all of them are the seat done whole. One answered question is one finding.
One repair verified, or refuted, is one finding. A defect of your own discovery outranks anything on
the menu.

**What this lane is asked that the others are not.** Three of the sweep's seven fatal findings are
here, and they are not drafting defects: they are the questions of whether the offense can be
pleaded at all, whether it can be charged before year four, and whether the conduct the Act was
written after is inside its reach. The fourth question below — what an attorney general's office
actually does with this in year one — is the one no scholar can answer and the one the project most
needs answered.

## Read first — the statute itself

The tagged text is not reproduced here. Read `model_act_v3_4.txt` at the repository root (print
copy: `archive/model_act_v3_4_reviewers_copy.pdf`). Your sections: **SEC. 5, 9, 10, and 12**, with
[chunk 3](../audit/record.md#chunk-3--penalty-architecture-for-v33-sec-7-rework-and-bracket-calibration)
(the penalty architecture) and
[chunk 5](../audit/record.md#chunk-5--commencement-rebuilt-immediate-duties-the-interim-standards-bridge-the-modifiability-floor-and-the-sec-5e-decision)
(commencement and the records duty) of the drafting record behind them.

---

## I. What the in-house sweep found in this lane

*Reproduced verbatim from [the sweep](../audit/v3_5_lane_sweep.md) — three of its seven fatal
findings, then the lane's remaining register. All of it is contestable; contesting it is the seat.*

""",
    relink(f2, SWEEP),
    "\n",
    relink(f3, SWEEP),
    "\n",
    relink(f4, SWEEP),
    "\n### The rest of the register in this lane\n\n",
    relink(rest_enforcement, SWEEP),
    """
---

## II. What has been drafted in response

*Reproduced verbatim from [the queue](../audit/v3_5_cure_language.md), grading intact:
sweep-derived and intake-derived entries are hypotheses, expressly not settled drafting, and the
intake-derived entries are additionally AI-assisted and not maintainer-validated. Each entry is a
candidate finding — verifying or refuting one is a complete finding for the disposition. The open
question comes first because the sweep calls it the most consequential item in the repository, and
because the answer to it changes what the five repairs are worth.*

""",
    relink(oq4),
    "\n*From the queue's fatals pass, same file — the tier-placement cross-check:*\n\n",
    relink(oq4_colorado),
    "\n",
    relink(cure9),
    "\n",
    relink(cure10),
    "\n*From the queue's fatals pass, same file — the federal comparator for the four controls:*\n\n",
    relink(select_agent),
    "\n",
    relink(cure14),
    "\n",
    relink(cure15),
    "\n*From the queue's addenda of 23 August, same file — the federal echo:*\n\n",
    relink(cure15_donor),
    "\n",
    relink(cure16),
    "\n*From the queue's fatals pass, same file — the witness and the second class:*\n\n",
    relink(cure16_donor_1),
    "\n",
    relink(cure16_donor_2),
    """
---

## III. What the states are already doing

*Reproduced verbatim from
[the state enforcement record](../research/state_enforcement_record_2026.md), which is
this lane's shelf and the file that carries the live actions — the Florida officer suit, the
42-state investigation, the 15-state preservation demand, the Pennsylvania licensure theory. No
other file in the repository may restate an enforcement action; if you need the actions themselves,
read that file. What is inlined here is only what the record does to the open question above, in
both directions.*

""",
    relink(oq4_both_ways, RECORD, "research"),
    """
---

## IV. The question menu

Any three answered are a disposition; all four, with the repairs above verified or refuted, are the
seat done whole. Replace any of them with findings of your own.

1. Would you charge any of this?
2. Does the OPEN QUESTION 4 amendment reach too far extraterritorially?
3. Are the four interim controls at CURE 10 the right four?
4. What does an attorney general's office actually do with this in year one?

Senior to all four, from the companion's
[READ FIRST index](../model_act_v3_4_companion.md#read-first--questions-for-the-next-revision-v35):
item 5 — preemption and federalism, open and monitored, waiting on a federalism litigator "ideally
in a state attorney general's office" — is this lane's, and question 2 is its narrow form.

## V. The errata already filed in this lane

- [E3](../ledger/errata.md#e3--no-signature-no-shipping-the-signature-is-not-a-gate-and-a-signed-confession-currently-counts)
  — the signature is not a gate; a signed confession currently satisfies the certification.
- [E6](../ledger/errata.md#e6--commencement-the-copy-error-corrected-today)
  — commencement is layered, not day-one across the board, and a copy error once hid the layers.
- [E28](../ledger/errata.md#e28--all-self-disclosed-in-the-same-repository-that-argues-the-victim-disclosed-first)
  — "all self-disclosed" was wrong; the victim disclosed first.
- [E29](../ledger/errata.md#e29--an-evaluator-was-placed-behind-an-incident-a-prior-correction-had-already-removed-it-from)
  — OPEN QUESTION 3's evaluator sentence was corrected once already; read the current text, not the
  version an earlier email may have quoted.

Method-wide entries — E21, E22 (extended by E32), E27, E33 — govern how every date, quotation,
count, and file-status claim in the evidence base was made;
[the register](../ledger/errata.md) is short and worth ten minutes.

## The other seats, and how this lane meets them

The review runs in eight parallel lanes: criminal law, enforcement, frontier security, fiscal and
administration, federalism and preemption, proportionality and sentencing, torts and design, and
open source and academia. Each seat reviews independently and each disposition publishes
independently, as written, so no lane waits on another. Findings that change text route through the
public cure queue and the errata register, where every other lane sees them. The maintainer collates
and responds separately and labelled, and may not overrule or edit a disposition. Anonymous outside
contributions arrive through the repository's correction doors and are credited by election — one
open drafting question has already been answered from outside this way. Reviewer identities are not
shared between reviewers, and attribution is each reviewer's own election.

**This lane specifically.** Enforcement consumes the criminal-law seat's offence structure and hands its posture choices to the fiscal seat, which prices them. It meets the torts and design lane where the records provisions decide whether anything is provable, and the security lane on what an investigator would need to see.

*How this seat's work becomes the next version: verified findings are drafted as cures against the
tagged v3.4 text in the public queue, and the assembled v3.5 carries every lane's accepted work, so
a disposition here is a chapter of the next version, written alongside the other seats'. Reviewer
identities are never shared between reviewers. The nearest familiar analogy is a conference paper
rather than peer review: you take a seat, do the work, and it is published as yours — see
[the dispositions register](../dispositions/README.md) for the rules, fixed before the first one
arrived.*


## VI. Filing

Email FrontierAIAccountabilityProject@proton.me — links or pasted text, no attachments — in any
form: a memo, a marked-up copy of this packet, a numbered list of findings. Or, if you were contacted by the maintainer through a different channel, reply on that channel. Or, if you were
contacted by the maintainer through a different channel, reply on the channel you were contacted
on. It is published as written, credited or anonymous at your choice; council seats publish with
names, which is the point of them. A finding that something is broken is the seat working, not
failing.
""",
]

io.open(OUT, "w", encoding="utf-8").write("".join(parts))
print("PACKET BUILT:", OUT, len("".join(parts)), "chars")
