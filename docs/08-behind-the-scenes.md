<sub>📁 [docs](./README.md) · ← [context: summer 2026](07-context-timeline.md) · **8 behind the scenes** · the corrections ledger → [ERRATA.md](../ERRATA.md)</sub>

# behind the scenes: what happens now, and why some of it is quiet

*written for people new to github, new to politics, or both. no fluency required in either.*

lawyers arrived. that changes how this project works, and you deserve the change explained rather than noticed. so: this page. it updates when the process changes. nothing on it is a flourish; it is the operating manual, in plain words.

## the project now runs in two layers

**the campaign layer** is everything you can see: this repository, the account, the jokes, the dossier, the corrections published next to the mistakes. its job is to find people — engineers, lawyers, skeptics, staffers, you — and to prove, in public, that the text survives checking. this layer stays loud and stays weird. that is not an accident; it is how a project with no institution behind it earns attention it can't buy.

**the lawmaker layer** is the version a legislator's office can hold up in a hearing without the jokes attached: the bill text, a section-by-section walkthrough in the format committee staff actually read, the honest cost estimate. that folder is being built now, with actual lawyers, on a separate surface that will never link back here. its job is to be boring on purpose. bills survive on boring.

**why they can't share a page:** a staffer who likes this bill still has to defend where it came from. campaign material recruits citizens and sinks sponsors — one screenshot of a shitpost stapled to a bill folder is a hearing delay in half the chambers in america. so the two layers never touch. the lawmaker layer will say, on a provenance page, exactly where the text came from — including that it was drafted in public, with AI assistance, by name-disclosed humans who signed off — and it will point here. we will never point there. one-way glass, by design.

## what "private" means here (and what it never means)

some things are now quiet: which lawyers, which state goes first, which lawmaker gets the folder, what got said in which meeting. announcing a target before a sponsor says yes is how you lose the sponsor — and it hands the opposition the map. that quiet is temporary and tactical.

what stays public, permanently, no exceptions: **the statute and every version of it. the full audit. the changelog. the [errata register](../ERRATA.md). every correction, pinned to every mistake.** our aim is that nothing that was ever public gets deleted (unless we feel like deleting the whole project, for some reason) — retired claims get corrections attached, so the quote and its fix travel together. if you ever catch this project deleting instead of correcting, let us know.

## what just happened (17 august)

- **we audited our own explainer against our own statute.** six contradictions. final score: statute wrong 5, copy wrong 1. the five get fixed in the statute (it moves to match the promise); the one got fixed on the card the same day, with the old wording preserved. every entry quotes both texts: [ERRATA.md](../ERRATA.md).
- **we withdrew our own pdf** until we can rebuild it reproducibly — tagged, checksummed, tested against the source text. a typeset document you can't verify is a liability wearing a nice font.
- **the word "introducible" went into the swear jar.** it comes back when named criminal counsel takes it out. the current text is a research draft and now says so everywhere.
- **the archive got its correction note**, so the old v3.2 penalty arithmetic can never be quoted without its fix in the same folder.

## who we're looking for

five seats on a review council, recruited in the open: a criminal-law specialist; a former prosecutor or regulator; a security engineer who has worked inside a frontier lab; an open-source or academia person; someone who has administered a real budget. pay: none. benefit: your name on the provenance page of the first serious attempt to write personal accountability for frontier AI into law — with the odds tracked publicly, as is tradition. reach us: llmaolaw@proton.me.

## names: who wears the mask, who signs, and who consents to what

the project is now recruiting actual humans — a criminal lawyer, and the five council
seats above. so here is the identity machinery, in full, before it operates — because
you can't consent to a process you can't see.

**the maintainer stays masked. indefinitely.** the arguments were built to stand
without a byline; the citations are the only authority they have. that doesn't change.

**but you cannot hire a lawyer in a mask.** an engagement letter needs a real client, a
conflicts check needs a real name, and attorney-client privilege only attaches to a real
relationship. so retained counsel learns who the maintainer is — privately, under
professional confidentiality, at engagement. that isn't a leak in the design; it is the
one load-bearing disclosure the design exists to route correctly.

**council members sign their names — that is the seat.** nobody's name appears anywhere
until they take a seat knowing exactly what it publishes: their name, their scope, their
conflicts, their verdict — including "approved with reservations," published as written.
before signing, they too learn who the maintainer is, under confidentiality: people
lending their names deserve to know whose project holds them.

**everyone else stays as masked as they like.** catches, corrections, contributions —
anonymous is fine, anonymous is traditional. no one is ever named here without having
chosen the naming.

**and the governed — you — get the process itself.** every rule above is published
before it runs. when the lawmaker-layer package reaches a sponsor, it carries a
provenance page disclosing the ai assistance, the pinned public commit, the verification
method, the named signoffs, and the conflicts — and that page points back here, to the
record anyone can check. the text is public. the audit is public. the errata are public.
the only two secrets are people's names (until their owners choose) and which door gets
knocked first (until it opens).

## why an actual lawyer (and what the machines aren't)

three things around here sound alike and are not, so here is the org chart in
plain words.

**the ai layer** — the models that help draft, pin sources, and build hostile
briefs against our own text. useful, tireless, and *legally nothing*. its own
programme document says so in the first paragraph: "not legal advice." the ai
disclaims itself, and we agree with it.

**the review council** — the five named humans being recruited above. they
review and sign, each in their lane. referees, not anyone's lawyer.

**retained counsel** — one licensed human lawyer, formally engaged. this is
the missing piece, and the reasons are concrete, not ceremonial:

1. **our own rule requires it.** nobody — including us — says this text
   "survived review" until a named lawyer signs. without one, it stays a
   research draft forever, by our own published law.
2. **the map needs a licensed checker.** the machines can pin what a statute
   says; only someone who has actually charged or defended these offenses
   knows what breaks in a real courtroom — whether the offense design collides
   with existing crimes, whether the enforcement route is real, whether the
   culpability choices survive case law.
3. **the staffer question.** the first thing any legislator's office asks
   about a criminal statute from an anonymous project is "has a lawyer
   reviewed this?" a named lawyer flips the answer to this question. this is what is being considered now by various people.
4. **privilege.** what the maintainer tells a retained lawyer is legally
   protected. what the maintainer tells an ai is not — ai chats are, in
   principle, discoverable. if this fight ever reaches a courtroom, that
   difference is not academic. the lawyer is also the one person whose duty
   runs to the maintainer, not the project: the identity question, personal
   exposure, whether talking to legislators trips a state's lobbying rules.

"retained" does not mean rich. it means *formally agreed to be the lawyer* —
that formality is the switch that turns on privilege and conflict duties.
pro bono is a real path: clinics, public-interest shops, professors, retired
prosecutors with grudges of their own. if that's you: llmaolaw@proton.me.

cleverness was never the missing ingredient here, but the value of a name and its standing could be.

## new here? how to follow along

this repository updates the way the account used to — except here, every change is signed, diffed, and permanent. **watch** or **star** the repo (top right, free github account) and the [commits page](https://github.com/llmaolaw/model-act/commits/main) becomes the feed: every edit, timestamped, with its reason. the [changelog](../CHANGELOG.md) is the plain-words version; the [errata register](../ERRATA.md) is the scorecard of our own mistakes; the [running log](../WHAT_JUST_HAPPENED.md) is the marquee — one entry per upload, newest first, failures in the same font size as wins. you can even subscribe to the statute in any feed reader: [commits/main.atom](https://github.com/llmaolaw/model-act/commits/main.atom). yes, that is a real sentence now — you can subscribe to a statute.

---

<sub>*sources on every card. corrections published. even our worst enemy is welcome.* )(</sub>
