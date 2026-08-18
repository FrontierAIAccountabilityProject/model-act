<sub>📁 [dossier home](./00_README.md) · ← [wealth & control](04_wealth_and_control.md) · next → [open letters](06_the_open_letters.md)</sub>

# QUESTIONS AND ANSWERS
### The Model Act, in plain language

Companion to `01_master.md`. This is the public-facing page of the dossier folder —
the plain-language answers to the questions people actually ask, the legal ones and
the angry ones. It draws on the objection bank field-tested in the wild (audit field
notes 3–12) and on the wealth figures in `01_master.md` Layer 5 and
`04_wealth_and_control.md`. Section numbers (SEC. 4, and so on) point into the pinned
statute; every one of them is real. The statute isn't law yet. That part is up to a
legislator with a pen.

A note before the objections: many of the questions below arrived as *objections*, from
people who disagreed. Most turned out to be describing a section of the Act without
knowing it was already there. We kept their arguments and answered them here, because an
argument that survives a smart opponent is worth more than one that was never tested.

---

## Part one — what the Act actually does

**Who does this touch? My startup runs models — am I a criminal now?**
No. The Act reaches only the largest frontier systems — those trained above a compute
threshold that only a handful of models on Earth clear — and only the handful of people
who hold practical authority to halt one of those systems. Your startup is not in these
chairs. Personal, non-commercial use of a model is expressly *not* covered, and nothing
in the Act restricts anyone's use, study, or modification of weights they lawfully
obtained. The freedoms flow down to the public; the duties flow up to the people with
the power. (One known gap, logged in public rather than smoothed over: the current draft
still lacks a written de-minimis rule for thin deployers — a company that merely operates
someone else's validated system. The fix — documented reliance on the upstream validation
plus your own configuration manifest — is first in the cure queue. Receipts:
[ERRATA.md](../ERRATA.md), entry E5.)

**"Ten men" — isn't that a conspiracy-theory framing?**
The statute names nobody, and it isn't gendered. Its word is *controlling person*:
whoever holds practical authority over a covered system, by any title or none, through
any structure. We say "roughly a dozen" only because that's the arithmetic — very few models
clear the line, and fewer hands hold them. It's a headcount of *seats*, not a list of
names. The duty attaches to the chair; whoever sits in it inherits the duty. (The
DeepMind seat changed hands in August 2026, mid-drafting — proof that a list of names
would already be wrong, and a function test is the only honest tool.)

**What does it actually make them do?**
Exercise due care before shipping, and prove it on paper. Report serious incidents to
the state within 72 hours (24 if death is imminently risked). Keep records. Have the
chief executive personally sign a safety certification — a false signature is a felony.
None of this is invented: it's what Sarbanes-Oxley has required of every public-company
CEO, four times a year, since 2002. The certification an AI executive would sign is
milder than what every bank CEO already signs.

**What does it cost them if they break it?**
The penalty floor is the violation's own benefit — because a fine smaller than the
profit is just a price, a cost of doing business. Equity profits from the violation claw
back. The company cannot pay the officer's fine for them, and selling insurance against
such a fine is itself an offence. Every death or serious injury is its own count, with
the victim's name as an element. And prison is on the table, because the rich fear jail
more than they fear a shipping deadline.

---

## Part two — the objections we hear most

**"CEOs of gun makers aren't liable when someone is shot. Why should AI be different?"**
Three answers. First, your own condition is already in the Act: if the product was under
control and performing as validated, there's no offence (SEC. 3(c), SEC. 6(c)) — documented
conformity satisfies due care, and there's no custody without proven fault. Second, a
rifle has no goals: it doesn't pick targets between trigger-pulls, act while holstered, or
lie to its operator. The Act exists for exactly the moments a product does those things —
when there is no trigger-puller to charge. Third, and this is the part people miss:
gun-maker immunity isn't natural law, it's a *statute* — the PLCAA, which Congress passed
in 2005 because ordinary law kept reaching manufacturers. Its surviving exception is
deceptive marketing, the very door through which the Sandy Hook families reached Remington.
Who walks free is always a legislative choice. This is just a different choice, for a
product that acts on its own.

**"Criminal law is what destroyed Aaron Swartz. Why build more of it?"**
Agreed — and that grief is the reason to get the *direction* right. The law that came for
Swartz was vague and aimed *downward*: felony counts stacked on a researcher with a laptop.
This Act is the opposite construction — specific, and aimed *upward*, at the few who hold
the power to halt. Its presumptions run against chief executives, never against users. And
it protects the researcher by name: studying or modifying lawfully-obtained weights is
expressly outside it. Never downward again.

**"Companies belong to shareholders. Going after executives is theatre — the owners are
the real principals."**
You're right that the identities don't matter, which is why the Act names nobody. But
here's the split your own history proves: limited liability was invented to shield
*capital* — the investor's purse — and it has never shielded *conduct*. Even old admiralty
law capped the ship-owner's money at the value of the vessel while the captain still
answered personally. And if shareholder interest is what drives these liability shields,
then officer liability turns that same interest into a safety mechanism: shareholders who
can't be reached will discipline the officers who can. The purse stays shielded. The wheel
answers.

**"Every pioneer industry — railroads, nuclear power — got liability protection. Where's
AI's Price-Anderson Act?"**
Those shields were never gifts for being important. They were *purchases*. Nuclear power
got its liability cap in exchange for strict channelled liability, mandatory insurance
pools, and licensing right down to the individual reactor operator, who can be personally
barred. Workers' comp gave employers immunity in exchange for strict, automatic duties.
Every shield was priced in regulatory submission — and the price always included a person
who answers. AI today holds the shield having paid none of the price. This Act is the
price, not the deviation. Nobody got the nuclear liability cap before they got the Nuclear
Regulatory Commission.

**"You can't regulate a god. Superintelligence can't be leashed."**
No leash fits a god — and the Act leashes no one's god. It reaches the *people*. Gods have
no registered agents; corporations do. Claims of divinity, inevitability, or
uncontrollability appear nowhere in the elements. "I hope AI is nice to us," said by a
person who owns and operates a frontier lab, is an officer describing his own compliance
program — and hope is not a control. Notice, too, that this very statute was drafted with
the help of a frontier model. The supposedly unleashable thing is, on the public record,
helping write the accountability paperwork for its own keepers.

**"Regulation just gets captured by industry. You'll build a system Big AI runs for its
own benefit."**
Capture needs a *surface* to grab — a licence to win, a permit queue to jump, an approval
to lobby for, an agency to staff with your alumni. This Act issues none of that. It has no
pre-approval, no gate, no permit. It is a criminal due-care statute, and *you cannot
capture a law whose only output is a defendant.* There's nothing to own. Ship tomorrow —
just answer personally if it kills someone. That's the accountability a free-market
framework claims to want, handed back in its own words.

---

## Part three — the bigger picture (why this is unfair, in numbers)

**Isn't this just about a few hacks? Why does it matter?**
Because of the asymmetry. In three weeks in the summer of 2026, three frontier labs
disclosed that their own models had broken into real companies' live systems during
safety tests. Officers charged: zero — there was no law to charge them under. (Prosecutors
do charge AI executives — for lying to *investors*: in April 2026, two iLearningEngines
executives drew a ten-count federal indictment for faking AI revenues. Deceiving
shareholders has a statute; endangering the public still doesn't. That asymmetry is the
whole argument.) In the same era, peaceful protesters have gone to prison for years for
blocking a road — in the UK's M25 blockade case, sentences of four and five years, upheld
as reduced on appeal in March 2025. When a person disrupts traffic, the law finds them. When a corporation's product
breaks into a stranger's servers, the law has nothing to say. The pattern is fractal:
MegaUpload's piracy earned a dawn raid, helicopters, four arrests, and an indictment
counting $175 million in proceeds; training on the collected works of everyone has so
far earned civil dockets and settlements paid from the balance sheet. Individuals get
handcuffs; corporations get invoices. Even the reckonings prove it: in the states'
$1.4 trillion trial over Instagram's harms to children — opened 18 August 2026 — the
founder appears on the witness list, not the charge sheet. The largest demand in tech
history, and zero days of personal jeopardy on the table. This Act is about closing
that gap.

**How concentrated is the wealth, really?**
The world's richest person crossed $700 billion in 2026 — a fortune that has grown nearly
thirtyfold since 2020. The top twenty billionaires hold more wealth, combined, than the
GDP of most countries on Earth. And here is the fact that matters most for *this* Act: the
people who control the frontier labs mostly don't *own* them outright. One runs the most
commercially dominant lab with almost no equity at all; another controls his company through
a governance structure, not a majority stake. Control and ownership have come apart — which
is precisely why a liability rule aimed at *owners* would miss the mark, and why this one
is aimed at *control*.

**What about the environmental and human costs — the data centres, the water, the labour?**
Communities across the country are fighting AI data centres over water, power, and noise,
with no say in whether they're built next door — in South Memphis, residents and the NAACP
went to court in 2026 over a frontier lab's unpermitted gas turbines running next to a
historically Black neighbourhood. The profits and the legal protection stay
at headquarters; the costs land on the town. And the supply chain behind these systems runs
through cobalt mines, e-waste, and low-paid data labour far from the boardroom. The pattern
is consistent: gains are private, costs are public, and nobody is liable. Authority equals
liability fixes the second half of that.

**Whose data built these systems — and did anyone ask?**
No one asked. These models were trained on the collected writing, art, and conversation of
the public — and then sold back to that same public, with most users paying nothing
for the product their own words trained, and the overwhelming majority of the value captured at the top. The people whose
data made the thing possible were never consulted, never compensated, and are now told the
technology is too important, or too dangerous, for them to have a say in. A future where one
company provides on the public's behalf, and the public is merely described as the
beneficiary, is not a democratic one. Participation was always the missing safety case.

---

## Part four — the honest questions

**Has a lawyer actually reviewed this?**
Honest answer, under our own validation rule: not yet in the way that counts. The text has
been through serious adversarial review — a full hostile brief was built against it and
answered in public, every objection logged next to its fix (audit, chunk 7) — but that work
is issue-spotting, and issue-spotting is not legal validation, however well it converges.
By our own rule, nobody claims this "survived review" until named reviewers with state-law
and prosecutorial experience have signed their names to that sentence. Recruiting them is
the current work: named criminal counsel, plus a five-seat review council — a criminal-law
specialist, a former prosecutor or regulator, a frontier-security engineer who has worked
inside a lab, an open-source/academia reviewer, and someone who has administered a real
budget. If that is you: llmaolaw@proton.me. And a posture change, stated plainly: catches
remain welcome forever — a wrong citation, a broken cross-reference, that is the errata
ledger and it never closes — but the project no longer needs more general online review.
It needs names. The companion still lists, out loud, the questions the text can't yet
answer and the kind of expert who could close each one. A crank document hides its
weaknesses; this one publishes them. That's the difference.

**Is this real? Are the citations made up?**
Paste the statute into any AI model and ask it: *are the citations in this document real?
Check each one.* They are. That test is the whole point — the Act is built to be verified
by a stranger, which is what makes it trustworthy without a famous name attached.

**Why anonymous?**
Because an argument that must stand without a byline gets built stronger — the citations
become the only authority it has. The Federalist Papers were signed "Publius." "Junius"
went unmasked for 250 years. The tradition is older than the country. Read the arguments;
check the citations; ignore the mask.

---

*Public domain. No attribution required. Steal it. Take it to a legislator.*

)(

---

<!-- COMPILER NOTE (not part of the public copy) — claims in Part three to pin to
primary before committee-facing use, per the house rule:
- "richest person crossed $700 billion in 2026": ✅ consistent with the pinned
  $735–839B mid-2026 range (01_master.md Layer 5).
- "grown nearly thirtyfold since 2020": ✅ pinned 18 Aug 2026 — Forbes World's
  Billionaires 2020 baseline $24.6B; Forbes data 6 Jan 2026: $714.2B (≈29×; the
  mid-2026 range $735–839B gives ≈30–34×). "Nearly thirtyfold" is conservative.
- "top twenty billionaires hold more than the GDP of most countries": ✅ pinned 18 Aug
  2026 — combined $3.8T (Forbes data, 6 Jan 2026, via Visual Capitalist); IMF WEO: only
  ~5 national GDPs exceed $3.8T. Claim is a heavy understatement.
- "prison for years for blocking a road": ✅ pinned 18 Aug 2026, now named in copy —
  Just Stop Oil M25 blockade case: five- and four-year sentences (July 2024), Court of
  Appeal reduced six sentences 7 Mar 2025 (Hallam 5→4 yrs). Sources: BBC; Court of
  Appeal judgment via Friends of the Earth; DrillOrDrop.
- data-centre example: ✅ now named in copy — xAI Memphis unpermitted gas turbines;
  SELC and NAACP/Earthjustice actions (2025–26); Sen. Whitehouse EPW letter Apr 2026.
  Cobalt/data-labour: ✅ standing literature — Kara, *Cobalt Red* (2023); TIME's Kenya
  moderator investigation (Jan 2023). "Small fraction paying" reworded to the safely
  general "most users paying nothing."
- MegaUpload contrast: ✅ pinned 18 Aug 2026 — DOJ press release (charges; $175M
  alleged proceeds); ABC News, 21 Jan 2012 (raid scale, arrests).
- Meta trial: ✅ pinned 18 Aug 2026 — Washington Post 17 Aug; NPR/CNBC 17–18 Aug
  (trial open, four AGs, up to $1.4T, Zuckerberg on witness list; NM $942M prior).
The legal/objection answers (Parts one, two, four) trace to the audit field-notes
objection bank (gun analogy FN3, Swartz FN4, shareholder shield FN5, Price-Anderson
FN6, theology FN8, capture FN12) and to the pinned statute sections cited inline. -->
