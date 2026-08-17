# MODEL ACT — Frontier AI Public Welfare Offenses (v3.3)

Model state legislation. Personal criminal liability for the
responsible officers of frontier AI companies, on the doctrine of
*United States v. Park*, 421 U.S. 658 (1975).

**Public domain. No attribution required. Steal it.**

**Current version: [model_act_v3_3.txt](./model_act_v3_3.txt)** (the introducible text, SEC. 0–13) + **[model_act_v3_3_companion.md](./model_act_v3_3_companion.md)** (open items, drafting notes, why).

v3.3 splits the Act from its apparatus so a staffer can drop the text straight into a bill jacket.

The file [model_act_v2.pdf](./model_act_v2.pdf) is only a signpost for old links; the real v2 lives in [/archive](./archive). What changed and why: [CHANGELOG.md](./CHANGELOG.md); the full audit trail is in [/audit](./audit).

Facts, legal doctrines, and ideas were never copyrightable anyway — the *Park* doctrine belongs to no one. We just did the assembly.

## Why anonymous, why us

Public welfare law is usually drafted after the funerals. The FDCA took
more than a hundred dead, many of them children, before Congress moved
in 1938. The Food Safety Modernization Act took a half-billion-egg
recall. The pattern is stable: the public buries someone, then the
public demands the statute. This document runs the pattern in the other
direction — drafted before the funerals, waiting.

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
ten because only a handful of models clear the 10^26 line and fewer
hands hold them. But it is a headcount, not a list of names, and it was
never gendered: seats, not people. The duty attaches to the chair, and
whoever sits down inherits it. ("CEO" is the wrong word too — some
people with real halt authority hold no such title, and almost everyone
holding that title, at almost every company, is nowhere near the line.
Your startup is not in these chairs. SEC. 1 draws the line; SEC. 4
finds the hands.)

## The documents

- [`model_act_v3_3.txt`](./model_act_v3_3.txt) — the Act, SEC. 0–13,
  introducible. Start here if you hold a pen in a legislature.
- [`model_act_v3_3_companion.md`](./model_act_v3_3_companion.md) — the
  READ FIRST page (open items for v4, each gap naming the kind of person
  who could close it), the drafting notes n.1–n.27, the answers to the
  friendly proposals, and why this document exists.
- [`model_regulations_v1_draft.md`](./model_regulations_v1_draft.md) —
  companion regulations (assembly draft, conformed to v3.3). The Act
  carries what a prosecutor needs; this carries what an engineer needs.
- [`model_act_v3_2.pdf`](./model_act_v3_2.pdf) /
  [`model_act_v3_2.txt`](./model_act_v3_2.txt) — previous version, kept
  in place. [`/audit`](./audit) holds the five audit chunks, the assembly record
that turned v3.2 into v3.3, and the field notes — objections met in
the wild and the answers that survived them. Receipts included.

## Where to start

- **Legislator or staffer** → [`model_act_v3_3.txt`](./model_act_v3_3.txt). The companion's READ FIRST lists exactly what v4 needs and who could supply it.
- **Lawyer** → the drafting notes in the [companion](./model_act_v3_3_companion.md). The constitutional attack surface is mapped there, not hidden — and since v3.3 the armour is in the text itself (SEC. 0, SEC. 13).
- **Engineer** → [`model_regulations_v1_draft.md`](./model_regulations_v1_draft.md). Control objectives, not vibes.
- **Journalist or just curious** → the stories below. Every section of the Act already happened to another industry.

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

Redlines welcome, credited or anonymous: first genuine catch
acknowledged in the notes as anonymous counsel.

## License

Dedicated to the public domain ([CC0](./LICENSE)). The eggs remained undefeated.

## Who this needs

Questions, redlines, or a state in mind: llmaolaw@proton.me — links or
pasted text only, no attachments. Any alias or none.

The READ FIRST page in the companion names the open items for v4, each
with the kind of person who could close it: a standards-literate
technologist (version pins) · state legislative counsel (conforming
amendments, the interim-standards pin date) · a criminal-law scholar or
former prosecutor (questions (b)–(c): the "serious injury" source and
the bracketed minimum) · a proportionality scholar (reviewing, no longer
designing, the sentencing valve — against fifty state clauses, not just
the federal floor) · a federalism litigator, ideally in a state AG's
office (preemption defence as the litigation develops) · an evaluations
researcher (reviewing the bracketed modifiability floor) · a security
engineer who has worked inside a lab (control objectives vs real
practice) · any law review 2L with a Bluebook (the cite-check, list
consolidated in the companion). Penalty calibration closed at v3.3: the
brackets carry the numbers three governors already signed.

If one of these is you: the text is public domain. Take it. Nothing
above is a reason to wait; all of it is a reason to begin.

## Read it here

![MODEL ACT v3.3 — page 1: findings + the act](./pages/actv33-1.png)
![page 2](./pages/actv33-2.png)
![page 3](./pages/actv33-3.png)
![page 4](./pages/actv33-4.png)
![page 5](./pages/actv33-5.png)
![page 6](./pages/actv33-6.png)
![page 7](./pages/actv33-7.png)
![page 8](./pages/actv33-8.png)
![page 9](./pages/actv33-9.png)
![page 10](./pages/actv33-10.png)

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
