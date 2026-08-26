*The short account of the whole project, for someone who has thirty seconds and might give it five
minutes. The front page is at [../README.md](../README.md); the chapter map is at
[MAP.md](../MAP.md); a reviewer's working page is [REVIEWERS.md](../REVIEWERS.md).*

# The project in one page

## The problem, in two sentences

American law has a doctrine for the situation where a company's ordinary operation puts the public
in danger and no single act of wrongdoing can be pinned on anyone: the **responsible corporate
officer**, from *United States v. Dotterweich* (1943) and *United States v. Park* (1975). The
person who held the practical authority to prevent or halt the condition answers for it, whatever
their job title said, and delegation is not a defense. **That doctrine has never been extended to
frontier artificial intelligence**, and every American AI statute now in force places its duties
and its penalties on the company alone.

## What this project is

A **public-domain model state statute** that makes the extension, drafted in the open, with its
audits, its corrections, and its whole drafting record published beside it. It is not a proposal
paper about what a law should contain. It is the text, tagged and versioned, with a
section-by-section companion, ready for a legislative counsel to conform to a state's code the day
a sponsor takes it up.

**Its architecture, in one paragraph.** Personal, non-delegable duties attach to natural persons
with final material authority to prevent, halt, restrict or correct covered conduct. Technical
work, access, advice, or implementing another person's decision does not create liability. A
covered model exceeds [10²⁶] operations or is prospectively designated frontier-equivalent; below
that, records duties only. The duties are validation, factual certification after reasonable
inquiry, records, and incident reporting. Consequences follow only when the statutory elements are
proved.

## What actually exists, counted

| | |
|---|---|
| The statute | **611 lines, 32 sections**, tagged v3.4, with an **11,000-word** section-by-section companion |
| The repository | **84 documents, more than 375,000 words**, mirrored as a searchable site. Twenty-one were retired on 26 August 2026 — they were signposts saying "this moved", and the links they redirected now point at the destination directly |
| The drafting record | **more than 460 commits**; every version's redline preserved; **16 cures** adopted verbatim at v3.4 and **26 more plus 4 open questions** drafted and waiting for v3.5 |
| Corrections | A numbered, append-only **errata register: 50 entries**, numbers reaching E64, each with the cause, what caught it, the fix, and the rule kept |
| Sources | A **verification record of more than 200 rows** — every instrument, its retrieval date, its grade, and, in its own section, the claims that **failed** verification and were withdrawn |
| The evidence shelf | **137 files** held privately, including **24 primary bills** and **13 congressional hearings** read against their own text |
| Review | **Eight lanes**, each with a printable packet assembled by a committed script from the repository's own files |
| Publication | CC0 public domain, archived at CERN, DOI [`10.5281/zenodo.22029795`](https://doi.org/10.5281/zenodo.22029795) |

Every number above is recomputed from the files by two committed tools, `check_claims.py` and
`check_links.py`, which fail the build if a page and the truth disagree.

## What the research found that nobody else has published

**One. The provision exists, and one state has it.** Illinois's Artificial Intelligence Safety
Measures Act requires an annual independent third-party audit, the designation of senior personnel,
and the signature of the lead auditor. New York's RAISE Act carried substantially the same words at
§ 1421(4) of print 6953-A on 3 June 2025. They came out in print 6953-B on 9 June, three days
before the bill passed both houses. **The provision existed for six days.** Illinois then enacted
it. It is the only place in American law where it is currently in force.

**Two. It has been drafted four times and enacted once.** The census traces the same
audit-and-signature architecture through four attempts. One survivor. That is not forty
legislatures independently converging on a design; it is one design surviving once.

**Three. Nobody has ever had to explain why it came out.** The New York Senate floor record of
12 June 2025 shows the bill called, the roll taken, and passage **58 to 1**. No debate. No member
laid it aside. No member asked why the audit had gone. The question is open, it is asked in public
in this repository, and whatever comes back will be published as given — including "it was struck
because it was wrong."

**Four. A Senate subcommittee has already stated the premise.** At *Too Big to Prosecute?*
(S. Hrg. 119-202, 16 July 2025), the chair of the Judiciary Subcommittee on Crime and
Counterterrorism said of frontier developers: *"have these Big Tech companies been prosecuted? No,
of course not. They are getting off scot-free."* The subject of that hearing was copyright, not
catastrophic risk, and nobody there proposed officer liability. What it establishes is that the
enforcement gap is not this project's inference.

**Five. The evidence disappears without anyone destroying it.** Two former researchers at a
frontier developer told the Senate on 9 September 2025 that raw research data is deleted at ninety
days as a matter of ordinary privacy policy — so removing a line from a report is enough to make
the observation behind it unrecoverable. That is the argument for a records duty that attaches to
the finding rather than to the data, and it is why this Act has one.

## What the project asks of a reader, and what it gives back

**The ask is bounded and it is the same for everyone.** One lane, scope agreed in writing before
work begins. The floor is **three findings, verified or refuted, with reasons** — perhaps six to
eight hours. The whole seat is a lane worked through, roughly ten to twenty hours over eight weeks.
Unpaid.

**What is unusual is what happens to the answer.** It is published entire, as written, under your
name or anonymously as you choose. The maintainer may respond beside it and **may not edit it**.
Model legislation in the United States comes from bodies that take outside views as input to a
committee that then votes, and the act belongs to the committee. Here there is no committee and no
vote. The nearest familiar shape is a conference paper, not peer review.

**A disposition that refutes one of this project's findings is worth more to it than a pass that
agrees with everything.** That is not politeness. One outside answer has already changed the
statutory text, and the errata register exists so that being right about a mistake is rewarded with
a permanent, numbered, credited entry rather than a quiet edit.

## What this project is not, stated before anyone has to ask

It is **not law**, not introduced, and not endorsed by anyone. Under the project's own published
rule, **nobody — the maintainer included — may claim this text "survived review" until named
reviewers sign**, and none have yet. It is maintained by **one person**, unfunded and unaffiliated:
not a company, a party, a government office, or an advocacy organization. The drafting is
**AI-assisted and says so on every relevant page**; source selection, corrections and publication
are the maintainer's responsibility. The maintainer writes pseudonymously in public and is
identifiable privately to reviewers before they sign.

And the known defects are published first, not last. An in-house adversarial pre-review returned
**seven findings graded fatal, four of them in the tagged text** — including that SEC. 6(a), the
individual-liability offense this Act exists to create, cannot be pleaded as drafted. Those
findings are on the front page, above the argument.

## Where to start

- The argument end to end: [the case](./the_case.md)
- The statute in plain English: [the statute translated](./the_statute_translated.md)
- The strongest objections, with answers: [known objections](./known_objections.md)
- Every frontier AI bill in America, read: [the census](../standards/frontier_bill_census.md)
- What has gone wrong here and how: [the errata register](../ledger/errata.md)
- Taking a seat: [REVIEWERS.md](../REVIEWERS.md)

Corrections and questions: **FrontierAIAccountabilityProject@proton.me**
