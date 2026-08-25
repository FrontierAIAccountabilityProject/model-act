#!/usr/bin/env python3
"""Assemble packets/criminal_law.md from the repository's own files.

Run from the repository root:  python3 packets/build_criminal_packet.py

The packet is a reading copy for the criminal-law seat: the lane's whole apparatus
inlined in reading order. The sources — the sweep, the queue, the register — remain
the authority. If this page and a source differ, the source is right and the
difference is a defect worth reporting. Regenerate after any edit to the sources.
Stdlib only; deterministic; no network.
"""
import io
import re

SWEEP = "audit/v3_5_lane_sweep.md"
QUEUE = "audit/v3_5_cure_language.md"
OUT = "packets/criminal_law.md"


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


def relink(block):
    """The queue and sweep link from audit/; the packet lives in packets/. Both are one
    level below the root, so ./ links need no change, but ../ links written from audit/
    already point at the root's siblings and also need no change. Intra-file anchors
    (#cure-…) must be re-pointed at the source file so they resolve from the packet, and
    ./-relative links written from audit/ must be re-based to ../audit/."""
    block = re.sub(r"\]\(#", "](../" + QUEUE + "#", block)
    block = block.replace("](./", "](../audit/")
    return block


sweep = read(SWEEP)
queue = read(QUEUE)

f1 = section(sweep, "### F1 —", ["### F2 —"])
rest_criminal = section(sweep, "**Criminal law.**", ["\n**Enforcement.**"])

oq1 = section(queue, "## OPEN QUESTION 1 —", ["\n## OPEN QUESTION 2"])
cure1 = section(queue, "## CURE 1 —", ["\n## CURE 2"])
cure8 = section(queue, "## CURE 8 —", ["\n## CURE 9"])
cure11 = section(queue, "## CURE 11 —", ["\n## CURE 12"])
cure12 = section(queue, "## CURE 12 —", ["\n## CURE 13"])
cure17 = section(queue, "### CURE 17 —", ["\n### CURE 18"])
dougherty = section(queue, "**To CURE 8 (SEC. 6(a) reconstructed)", ["\n\n**To ", "\n\n**On "])

parts = [
    """# The criminal-law lane — one page

*A reading copy for the criminal-law seat, assembled 24 August 2026 by
`packets/build_criminal_packet.py` from [the in-house sweep](../audit/v3_5_lane_sweep.md),
[the drafting queue](../audit/v3_5_cure_language.md), and
[the errata register](../ledger/errata.md). Those files are the authority; this page exists so
the lane can be read, printed, and marked up as one document. If this page and a source differ,
the source is right and the difference is a defect worth reporting to
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

**The arithmetic:** everything below is the menu — six questions, six drafted repairs. Any three
items are a complete disposition; all of them are the seat done whole. One answered question is
one finding. One repair verified, or refuted, is one finding. A defect of your own discovery
outranks anything on the menu.

## Read first — the statute itself

The tagged text is not reproduced here. Read `model_act_v3_4.txt` at the repository root (print
copy: `archive/model_act_v3_4_reviewers_copy.pdf`). Your sections: **SEC. 1, 4, 5–6, and
10(b)–(c)**, with the v3.4 cures 2, 5, and 13 and the penalty and harm-tier chunks of
[the drafting record](../audit/record.md#chunk-3--penalty-architecture-for-v33-sec-7-rework-and-bracket-calibration) behind them.

---

## I. What the in-house sweep found in this lane

*Reproduced verbatim from [the sweep](../audit/v3_5_lane_sweep.md). All of it is contestable;
contesting it is the seat.*

""",
    relink(f1),
    "\n",
    relink(rest_criminal),
    """
---

## II. What has been drafted in response

*Reproduced verbatim from [the queue](../audit/v3_5_cure_language.md), grading intact:
sweep-derived and intake-derived entries are hypotheses, expressly not settled drafting, and the
intake-derived entries are additionally AI-assisted and not maintainer-validated. Each entry is a
candidate finding — verifying or refuting one is a complete finding for the disposition.*

""",
    relink(oq1),
    "\n",
    relink(cure1),
    "\n",
    relink(cure8),
    "\n*From the queue's fatals pass, same file — the state-court cross-check:*\n\n",
    relink(dougherty),
    "\n",
    relink(cure11),
    "\n",
    relink(cure12),
    "\n",
    relink(cure17),
    """
---

## III. The question menu

Any three answered are a disposition; all six, with the repairs above verified or refuted, are
the seat done whole. Replace any of them with findings of your own.

1. Is the reconstructed SEC. 6(a) chargeable?
2. Is due care as an element the right cure for the *Alleyne* problem?
3. Does the restored burden survive?
4. Is CURE 1's answer — one injury definition, not two — right?
5. Does a state's suspended-sentence law defeat the harm-tier minimum? *(the sweep could not
   settle this)*
6. Does per-victim counting survive the state's merger doctrine? *(nor this)*

Senior to all six, from the companion's
[READ FIRST index](../model_act_v3_4_companion.md#read-first--questions-for-the-next-revision-v35):
item 3's remainder (the death-results minimum and the report-versus-element distinction) and
item 4 (the sentencing valve against state proportionality clauses) are this lane's too.

## IV. The errata already filed in this lane

- [E1](../ledger/errata.md#e1--engineer-exemption-claimed-as-written-in-fact-implied-not-yet-express)
  — the engineer exemption was claimed as written; it is implied, not yet express.
- [E8](../ledger/errata.md#e8--in-one-paragraph-true-of-the-duty-silent-on-the-entity-in-the-paragraph-built-to-be-quoted)
  — the entity tier is strict liability; the front-page summary once said otherwise.

Method-wide entries — E21, E22 (extended by E32), E27, E33 — govern how every date, quotation,
count, and file-status claim in the evidence base was made;
[the register](../ledger/errata.md) is short and worth ten minutes.

## V. Filing

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
