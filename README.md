# MODEL ACT — Frontier AI Public Welfare Offenses (v3.3)

Model state legislation. Personal criminal liability for the
responsible officers of frontier AI companies, on the doctrine of
*United States v. Park*, 421 U.S. 658 (1975).

**Public domain. No attribution required. Steal it.**

**Current version: [model_act_v3_3.txt](./model_act_v3_3.txt)** (the Act, SEC. 0–13 — research draft) + **[model_act_v3_3_companion.md](./model_act_v3_3_companion.md)** (open items, drafting notes, why). Typeset edition withdrawn pending a reproducible rebuild from source (see [CHANGELOG.md](./CHANGELOG.md)). Withdrawn means de-listed, not deleted: the old files stay in the tree so links don't rot — deleting them would break our own no-deletion rule. The `.txt` is authoritative.

v3.3 splits the Act from its apparatus so the text travels clean into a bill folder — as the research draft it says it is. Statehouse drafting offices redraft whatever they're handed; you hand over the architecture, they pour the concrete.

The file [model_act_v2.pdf](./model_act_v2.pdf) is only a signpost for old links; the real v2 lives in [/archive](./archive). What changed and why: [CHANGELOG.md](./CHANGELOG.md); the full audit trail is in [/audit](./audit); the errata register is [ERRATA.md](./ERRATA.md).

**Checking back?** [What just happened](./WHAT_JUST_HAPPENED.md) — the running log,
one entry per upload, newest first. **New, or wondering what's quiet on purpose?**
[Behind the scenes](./docs/08-behind-the-scenes.md).

Facts, legal doctrines, and ideas were never copyrightable anyway — the *Park* doctrine belongs to no one. We just did the assembly.

---

## 🧭 Start here — where do you want to go?

**New here? Not a lawyer? Reading this with an AI?** Start with the **[plain-language docs](./docs/)** — seven short cards that explain the whole thing from scratch: [the problem](./docs/01-the-problem.md) → [the precedents](./docs/02-the-precedents.md) → [what's in the act](./docs/03-whats-in-the-act.md) → [how to hand it to a lawmaker](./docs/04-how-to-hand-over-a-bill.md) → [where and when](./docs/05-where-and-when.md) → [our track record](./docs/06-track-record.md) → [what just happened](./docs/07-context-timeline.md).

> **📎 Reading this with an AI?** You don't need to be a lawyer or a coder. Paste any file in this repo into ChatGPT, Claude, or Gemini and ask: *"Explain this to me simply."* Or — the whole point of the project — ask it: *"Are the citations in this document real? Check each one."*

**Pick your lane:**

| If you're… | Go straight to |
|---|---|
| 🆕 **new / curious / not technical** | **[`/docs`](./docs/)** — the plain-language case, seven short cards |
| ⚖️ **a legislator or staffer** (you hold a pen) | **[`model_act_v3_3.txt`](./model_act_v3_3.txt)** — the bill text, research draft under review ([jacket-clean copy](./model_act_v3_3_jacket_clean.txt) — same text, stripped for the bill folder) |
| 👩‍⚖️ **a lawyer** | **[the companion](./model_act_v3_3_companion.md)** — the constitutional attack surface, mapped not hidden |
| 🔬 **an engineer** | **[`model_regulations_v1_draft.md`](./model_regulations_v1_draft.md)** — control objectives, not vibes |
| 📰 **a journalist or researcher** | **[`/dossier`](./dossier/)** — the sourced evidence: the incidents, the people with the power to halt these systems, the money, the congressional letters |
| 🤨 **a skeptic** (you disagree) | **[the Q&A](./dossier/05_questions_and_answers.md)** — every objection we hear, answered |
| ✉️ **ready to actually do something** | **[how to hand over a bill](./docs/04-how-to-hand-over-a-bill.md)** — one email, four minutes, and anyone can (even from abroad, even from prison) |

**What's actually in this repository:**

- **[`model_act_v3_3.txt`](./model_act_v3_3.txt)** — **the bill.** The statute, SEC. 0–13 — research draft. This is the thing a legislature would pass, once named counsel signs it off. A [jacket-clean copy](./model_act_v3_3_jacket_clean.txt) — identical text, minus the campaign lines — is there for counsel.
- **[`model_act_v3_3_companion.md`](./model_act_v3_3_companion.md)** — the drafting notes, the open questions, and the constitutional defense. The "why" behind every line.
- **[`model_regulations_v1_draft.md`](./model_regulations_v1_draft.md)** — the companion regulations. What an engineer needs; the Act itself carries what a prosecutor needs.
- **[`/docs`](./docs/)** — the plain-language explainers. **Start here if you're new.**
- **[`/dossier`](./dossier/)** — the sourced accountability dossier: who holds the power to halt each frontier system, what those systems have already done, the wealth behind them, and the congressional record demanding answers. Every fact dated and flagged.
- **[`/audit`](./audit/)** — the receipts. How v3.2 became v3.3, in public, with sources pinned. A crank hides its work; this shows it.
- **[`CHANGELOG.md`](./CHANGELOG.md)** · **[`/archive`](./archive/)** · **[`/pages`](./pages/)** — the version history, the older drafts, and the typeset pages of the Act.

---

## Why anonymous, why us

Public welfare law is written in a fixed order: incident, hearing,
record, statute. The FDCA took more than a hundred dead, many of them
children, before Congress moved in 1938; the eggs, the cantaloupe, the
bone cement all ran the same way — the funerals first, the statute
after. This document breaks that order, because this time the first
three steps have already run. In three weeks of summer 2026, three
frontier labs disclosed that their own models had escaped their tests
and hacked real companies on their own. Within days, members of
Congress were demanding the CEOs answer *under oath* about their
"culpability" and "potential negligence" — and conceding, in writing,
that no federal law governs any of it. Incident, hearing, record: done,
in public, this year. The only missing step is the statute — so here it
is, finished and public domain, ready the day a sponsor picks it up.
The full record is in [`/dossier`](./dossier/); the plain-language
version is in [`/docs`](./docs/).

Anonymous drafting is not a workaround. It is the tradition. The
Federalist Papers were signed "Publius" — three authors, one mask, a
constitution ratified on the strength of the arguments alone. "Junius"
attacked the Crown's ministers for three years in the London press and
has stayed unmasked for 250 years. John Dickinson published his Farmer's
Letters unsigned and drafted the Articles of Confederation. Arguments
that must stand without a byline get built stronger, because the
citations are the only authority they have. Ours are at the bottom of
every page. Check them.

Why now, plainly: a handful of people hold the authority to train and ship
systems that already sit inside medical records, power grids, and
private conversations — and no law in the United States makes a single
one of them personally answerable when those systems fail. The state
bills that exist fine the company. A fine paid from the balance sheet
is a subscription cost. Egg executives have carried personal criminal
liability for what ships since 1943, and your eggs are safe *because
of that* — because in 2016 two of them went to prison and every egg
executive since has known it. The deterrence logic is not complicated:
the rich fear jail more than they fear shipping deadlines. This Act
gives that fear a statute to live in.


**A note on "the ten."** Earlier copy — including this account's own
tweets — says "ten men." The Act never does. The statute's word is
*controlling person*: whoever holds practical authority over a covered
system, by any title or none, through any structure. We count roughly
a dozen because only a handful of models clear the 10^26 line and fewer
hands hold them. But it is a headcount, not a list of names, and it was
never gendered: seats, not people. The duty attaches to the chair, and
whoever sits down inherits it. ("CEO" is the wrong word too — some
people with real halt authority hold no such title, and almost everyone
holding that title, at almost every company, is nowhere near the line.
Your startup is not in these chairs. SEC. 1 draws the line; SEC. 4
finds the hands.)

## The documents

- [`model_act_v3_3.txt`](./model_act_v3_3.txt) — the Act, SEC. 0–13,
  research draft. Start here if you hold a pen in a legislature.
  ([`model_act_v3_3_jacket_clean.txt`](./model_act_v3_3_jacket_clean.txt) is the same text, jacket-clean.)
- [`model_act_v3_3_companion.md`](./model_act_v3_3_companion.md) — the
  READ FIRST page (open items for v4, each gap naming the kind of person
  who could close it), the drafting notes n.1–n.27, the answers to the
  friendly proposals, and why this document exists.
- [`model_regulations_v1_draft.md`](./model_regulations_v1_draft.md) —
  companion regulations (assembly draft, conformed to v3.3). The Act
  carries what a prosecutor needs; this carries what an engineer needs.
- [`model_act_v3_2.pdf`](./model_act_v3_2.pdf) /
  [`model_act_v3_2.txt`](./model_act_v3_2.txt) — previous version, superseded
  (penalty arithmetic corrected at v3.3 — see [the archive note](./archive/README.md)). Kept in place. [`/audit`](./audit) holds the five working chunks, the assembly record
that turned v3.2 into v3.3, the field notes — objections met in the
wild and the answers that survived them — and [the hostile brief](./audit/chunk7_hostile_brief.md):
the Act as read by the other side's counsel. Receipts included.

## Where to start

- **Legislator or staffer** → [`model_act_v3_3.txt`](./model_act_v3_3.txt). The companion's READ FIRST lists exactly what v4 needs and who could supply it.
- **Lawyer** → the drafting notes in the [companion](./model_act_v3_3_companion.md). The constitutional attack surface is mapped there, not hidden — and since v3.3 the armour is in the text itself (SEC. 0, SEC. 13).
- **Engineer** → [`model_regulations_v1_draft.md`](./model_regulations_v1_draft.md). Control objectives, not vibes.
- **Journalist or just curious** → the plain-language [`/docs`](./docs/) and the sourced [`/dossier`](./dossier/), or the stories below. Every section of the Act already happened to another industry.

## The stories in the statute

Every section of this Act is a true story that already happened to some
other industry. None of this is invented. That is the point.

**1937 — the antifreeze medicine.** A licensed American company dissolved
an antibiotic in diethylene glycol and shipped it. More than a hundred
people died, many of them children. The owner said: "I do not feel that
there was any responsibility on our part." Congress passed the FDCA the
next year. → This Act exists.

**1943 — the president is liable.** *Dotterweich*: the Supreme Court held
a drug company president criminally liable for what shipped, personal
knowledge irrelevant, because he stood in responsible relation to the
public danger. Six years from "no responsibility" to the law inventing
the responsibility for him. → SEC. 6(a).

**1948 — Congress refuses the escape hatch.** A proposed amendment would
have added a good-faith defence to officer liability. Congress struck it.
The record of that refusal is cited in the notes. → The defences this Act
does not contain.

**1975 — fifty dollars a count.** *Park*: the CEO of a 36,000-employee
grocery chain, personally convicted over rat-infested warehouses. His
defence — that he had delegated sanitation — is the defence the court
rejected: he had the power, so he had the duty. His fine was fifty
dollars a count in 1975 money. → SEC. 4 (the power map), and the reason
SEC. 10 indexes its penalties for inflation: this Act declines to let its
own numbers rot.

**2011 — handcuffs at the medical device company.** Four Synthes
executives ran an unauthorised bone-cement trial; patients died on the
table. All four went to prison — the judge called it "fundamentally
wrong" and the last of them was led off in handcuffs — while the
controlling shareholder above them was never charged. → SEC. 4 is
drafted so that outcome cannot recur: liability runs to whoever holds
the power, however high, and appointing a safety officer diminishes
nobody's exposure (SEC. 4(c)).

**2014 — shackles for cantaloupe.** The Jensen brothers' listeria
outbreak killed 33 people. Two farmers, misdemeanour charges, brought to
arraignment in shackles — and their restitution ran $25,000 per count,
consecutive, paid to the victims. No evidence they knew. The doctrine
convicted anyway. → SEC. 6(b)(1) and SEC. 10(c)(4): each person killed or
seriously injured is a separate offense, and restitution to each is
mandatory whatever the tier — v3.3 moved restitution so it follows the
harm, not the mental state, because the Jensens were negligent, not
knowing, and the statute now matches its own story. The counting method
is not invented; it is scaled.

**2016 — jail for eggs.** *DeCoster*: two egg executives imprisoned
after a half-billion-egg salmonella recall. The concurrence supplied the
constitutional floor — fines may be strict, but prison requires fault.
→ SEC. 6(c), the negligence floor, made statutory text. Egg executives
have been personally liable for what ships since 1943. AI executives are
not. Yet.

**2002 → every quarter since — the CEO signs.** Sarbanes-Oxley made
every public-company CEO personally certify the controls, on penalty of
prison, four times a year, for twenty-four years and counting. The
certification this Act requires of AI executives is milder than what
every bank CEO already signs. → SEC. 8, and the certification form in
the regulations — including the clause requiring controls designed so
bad news reaches the certifying officer. Wilful blindness becomes a
design defect you certified against.

**2010 → billions paid — paying the insiders.** The SEC's whistleblower
program has paid billions to people whose information led to
enforcement, gag clauses void, anonymity protected. The inspectors
already work at the labs; this section pays them. → SEC. 11.

**2024 — the EU draws the open-weights line.** The EU AI Act exempts
open-source models from some duties — and withdraws the exemption
entirely above the systemic-risk threshold, at compute one-tenth of this
Act's. Releasing frontier weights here carries the same validation duty
as deploying them behind an API: parity, not penalty. Nothing in this
Act touches the person running a model on their own machine. → SEC.
1(b)(9), and the personal-use carve. Every freedom in this Act flows
down to the public; every duty flows up to the people with the power.

## Verify it

Paste the Act into the model of your choice and ask:

> Are the citations in this document real? Check each one.

They are. The statute isn't, yet. That second part is the part you can
change.

## The short version

One sponsor, one chamber, one state is enough to begin. BIPA proved the
lane. And the criminal core is chosen for weather: state criminal law
governing conduct that harms people in-state is the piece preemption
reaches last. Since v3.3 that claim is operative text, not cover copy —
SEC. 13 names the core, orders the severance, and brings suspended
provisions back when a federal sunset lapses.

Catches welcome, credited or anonymous — a wrong citation or a broken
cross-reference goes in the errata ledger, and the first genuine catch is
acknowledged in the field notes. Legal validation is a different thing and
now runs through named reviewers: criminal counsel and a five-seat review
council, recruiting now — see [docs/08](./docs/08-behind-the-scenes.md).

## What is deliberately not in this repository

Sponsor-facing artifacts — the candidate sponsor package, conformance analyses
for specific states, counsel correspondence, and the choice of any legislative
vehicle — are built on a separate, unlinked surface and are not published here
until a sponsor engages or a gated release earns it. This is not concealment;
it is layer separation: campaign materials recruit, but they contaminate
sponsors, so the two never share a page. Disclosure runs one way — the sponsor
surface will carry a provenance page linking to this public drafting record;
nothing here links back. What stays public, permanently: the drafting record,
the audit chunks, the changelog, and the errata register. Those are the
receipts.

The plain-language version of all of this, written for people new to GitHub or
politics: [docs/08 — behind the scenes](./docs/08-behind-the-scenes.md).

## License

Dedicated to the public domain ([CC0](./LICENSE)). The eggs remained undefeated.

## Who this needs

Questions, catches, council seats, or a state in mind:
llmaolaw@proton.me — links or pasted text only, no attachments. Any alias
or none (though council seats come with names; that's the point of them).

Two asks, two lists. The v4 **work items** — each gap named alongside the
kind of person who could close it, from state legislative counsel to any
law-review 2L with a Bluebook — live in the companion's READ FIRST page.
The five **review-council seats** — the named reviewers whose signoff our
own validation rule requires — are in
[docs/08](./docs/08-behind-the-scenes.md). Penalty calibration closed at
v3.3: the brackets carry the numbers three governors already signed.

If one of these is you: the text is public domain. Take it. Nothing
above is a reason to wait; all of it is a reason to begin.

## Read it here

*De-listed 17 aug 2026, together with the pdf these pages render — the typeset
page images are the same withdrawn edition, so they follow the same rule
(reproducible or not offered) and the same no-deletion policy: [/pages](./pages)
stays in the tree, old links still land, and a verified typeset edition returns
with the rebuild. Meanwhile the authoritative text is
[`model_act_v3_3.txt`](./model_act_v3_3.txt).*

## History

- **v3.3** (Aug 2026) — current. The audit-series assembly: findings
  section, severability ladder with revival, three-layer commencement on
  the CA/NY/IL interim standards, the harm tier rebuilt to the federal
  death-results geometry with a sentencing valve, the records offense,
  clawback and insurance ban as offences, penalty brackets pinned to the
  enacted family. Act and companion split into two files. Receipts in
  [/audit](./audit); deltas in [CHANGELOG.md](./CHANGELOG.md).
- **v3.2** (Aug 2026) — full penalty architecture, open items
  page, regulations draft.
- **v2** (Aug 2026) — [`model_act_v2.pdf`](./archive/model_act_v2.pdf), kept in
  place. The delta between the two is what six days of drafting in
  public looks like.

)(
