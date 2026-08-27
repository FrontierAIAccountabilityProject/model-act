# Amendment triage — A / B / C

*Written 27 August 2026. Classification only: nothing here fixes, drafts, or amends anything.
Source read: `revision/proposals.md` (formerly `audit/v3_5_cure_language.md`), all twenty-three
amendments and four decisions; `corrections/corrections.md` E56–E69; the ✅ rows in
`authorities/table-of-authorities.md`.*

**A path note.** The instruction named `audit/v3_5_cure_language.md`, `ledger/errata.md` and
`standards/table_of_authorities.md`. Those files moved on 26 August and the cures are now numbered
as **Amendments**. Same content, same numbers; the paths above are current.

**Buckets.** **A** — mechanical: the Act's own text determines the answer, and a careful
non-lawyer with the statute in front of them could apply it. **B** — research-resolvable: a document
ends the question. **C** — judgment: two competent lawyers who had read everything could still
disagree.

**Twenty-three amendments exist, not twenty-six.** 17, 18 and 19 are absent from the register —
they appear in an index but have no entries. That gap is unexplained and is itself an open item.

---

## The count

| Bucket | Count | Amendments |
|---|---|---|
| **A — mechanical** | 3 | 5, 13, and the spelling half of 22 |
| **B — research-resolvable** | 8 | 1, 3, 9, 12, 16, 24, 25, 26 |
| **C — judgment** | 12 | 2, 4, 6, 7, 8, 10, 11, 14, 15, 20, 21, 23, and the knowledge half of 22 |

**Of the eight in B, seven are already answered** — the document has been read. Only Amendment 22's
pincite dependency is outstanding, and it blocks nothing in B.

**The C cluster sits where predicted:** SEC. 6 (8, 22), SEC. 8 (21, 24 in part), SEC. 3 (10, 15, 23),
SEC. 9 (14), SEC. 1 (6, 7), SEC. 5 (11), SEC. 13 (2).

---

## A — mechanical

*Do these first and in this order. Ordered by how many other amendments touch the same line.*

| # | Section | Why it is mechanical | Blocks |
|---|---|---|---|
| **5** | SEC. 8 | A comma where a period belongs, mid-sentence, before "A certification disclosing identified noncompliance". Closes E13. The sentence boundary is determined by the sentence | Nothing. Adopt it |
| **13** | SEC. 1(b)(1)(B) | "extend a lineage" is a phrase used nowhere else in the Act and defined nowhere. The replacement states the same operation in the Act's own defined vocabulary | Touches the SEC. 1 lineage definitions that **6** and **7** also edit. Do 13 before either, or the same line gets edited twice |
| **22a** | SEC. 6(b)(1) | "wilfully" → "willfully". `CLAUDE.md` rule 3 records this as a defect the register owns. One word | Shares a line with 22b (bucket C). Splitting the amendment lets the spelling land without waiting on the doctrine |

**Also mechanical, and not currently an amendment at all:** the statute file ends with two stray
characters, `)(`, after "Steal it." Present in the tagged text and in `act/model-act.txt`, absent
from `act/clean-copy.txt`. It is in the worklist and has no amendment number.

**And a defect in the register itself:** Amendment 21's heading and provenance paragraph are
**duplicated** — every line appears twice. Cosmetic, but it is in the document a reviewer reads.

---

## B — research-resolvable

| # | Section | The document that ends the question | Held? |
|---|---|---|---|
| **1** | SEC. 1(8), and a rename cascade | 18 U.S.C. § 1365(h)(3)–(4) — the donor definition, quoted in full in the entry | ✅ Row in the table; § 1365(a) already relied on for SEC. 10(c) |
| **3** | the draft rules | `act/rules.md` against the tagged Act. Purely internal: three v3.4 changes never cascaded | ✅ Both files in the repository |
| **9** | SEC. 10(e) | 21 U.S.C. § 374 — the FDCA inspection authority § 331(e) is parasitic on | ⚠ **Not on the shelf.** § 331 and § 333 are held; § 374 is the one this needs and it is not in the table |
| **12** | SEC. 5(d) | 18 U.S.C. § 1001 and *United States v. Alvarez*, 567 U.S. 709 (2012) (plurality) | ⚠ Both have rows; neither carries a ✅ read status |
| **16** | SEC. 1(b)(7) | *Van Buren v. United States*, 593 U.S. 374 (2021), and the AISI incident record | ⚠ *Van Buren* row carries no read status. The incident record **is** read in full and held |
| **24** | SEC. 8 | 18 U.S.C. § 1350 and 33 U.S.C. § 1319(c); *Hanousek* for the negligence floor | ✅ **All three read.** § 1350 read in full 25 Aug; *Hanousek* read 26 Aug, confirmed on two sources |
| **25** | SEC. 10(d) | 21 U.S.C. §§ 332 and 334 | ✅ **Read 25 Aug.** § 332(b) supplies the jury, quoted verbatim in the entry |
| **26** | SEC. 3(c)(4) | The three adopted interim standards, read in full | ✅ **Read 25 Aug**, all three. Four items found the list did not anticipate |

**Research complete on 1, 3, 24, 25, 26.** For these the question is no longer *what does the source
say* but *do we adopt the drafted text* — they are one decision from done.

**Research outstanding on 9, 12, 16**, and each needs one document: 21 U.S.C. § 374, *Alvarez*, and
*Van Buren*. None is hard to obtain. **9 is the one to get first**, because the defect it names —
an offense with no conferring authority — is graded fatal.

---

## C — judgment

*No document settles these. Grouped by section, because a reviewer takes them together.*

**SEC. 6 — the individual-liability offense.** This is the cluster.

| # | Why judgment |
|---|---|
| **8** | Reconstructs SEC. 6(a) into three elements plus a nexus clause. The defect is demonstrated — the offense cannot be pleaded, F1 — but *which* reconstruction is a drafting choice, and this text is sweep-derived and not maintainer-validated |
| **22b** | Whether knowledge under SEC. 6(b)(1) may be reached through SEC. 6(d) responsibility. *MacDonald & Watson* holds official responsibility alone cannot supply it; *Johnson & Towers* permits the jury to infer it from responsible position. **A genuine circuit split, and the answer is a policy choice about which side to draft to** |

**SEC. 8 — certification.** **21** (public register: facts public, content protected) and the
drafting half of **24** are both choices about how much the certification exposes.

**SEC. 3 — standards and commencement.** **10** (interim controls so SEC. 5(b) is not dormant to
year four), **15** (a disclose-and-fix valve, because the text as written punishes candor), **23**
(restore the publication the adopted statutes require — expressly *changes what the Act requires*
rather than repairing what it says, and its own entry says to read it on that footing).

**Scope.** **6** (self-designation as a third route in) and **7** (the covered frontier enterprise).
**7 is already held by maintainer ruling** pending the enforcement and security reviewers, and its
bracketed scale figures have no donor statute — the entry says so.

**The rest.** **2** (review valve on the suspension order), **4** (recasting "deception" as an
observable event), **11** (naming the obligor in SEC. 5 and SEC. 9(b)), **14** (a detection clock
that cannot be gamed), **20** (conformity outside the Act credits nothing).

---

## Flagged — basis overtaken by a later reading

*Checked against E56–E69 and the ✅ rows. Three entries rest on ground that has moved.*

**Amendment 22 — the pincites are still not confirmed, and the entry publishes them.** The entry
quotes *MacDonald & Watson* "at 51" and "at 55". The table records: *"Text read 25 Aug 2026 in the
opinion; pincites still unverified."* Both sentences are verbatim; the page numbers are the
secondary source's, and **[E47](../corrections/corrections.md)** governs — a source without star
pagination confirms a quotation and never a page. The entry does not carry that qualification.

**Amendment 22 — and its factual premise is now false.** The entry's opening says a case name
"came back **zero**" across the repository. As of 26 August *MacDonald & Watson* has a table row, a
read status and a worklist entry. The provenance paragraph reads as though it does not.

**Amendment 8 — E66 bears directly on it and postdates it.** Amendment 8 was drafted 22 August.
E66 (26 August) records that *Johnson & Towers* holds that knowledge "may be inferred by the jury
as to those individuals who hold the requisite responsible positions with the corporate defendant"
— the half this repository had not published. Amendment 8's nexus clause and Amendment 22's
concession sentence were both drafted without it.

**Amendment 24 — research now complete, and the entry predates the completion.** It was opened
25 August on § 1350 and § 1319(c). *Hanousek* was read 26 August and confirms the negligence floor
at 1121. The entry does not cite it because it did not exist yet.

**Not overtaken, but worth stating:** E65 corrected *Global-Tech* from "the constitutional ceiling"
to what it is — a civil patent case stating the two-part willful-blindness test. **Amendment 22's
Operation 1 relies on that ceiling.** The test still binds in the direction SEC. 6(b) needs, but the
characterization it was drafted against has been withdrawn.

---

## What this means for v3.5

**Three amendments can land today with no judgment exercised** — 5, 13, 22a — plus the `)(`.

**Five more are one decision from done**, the research being complete: 1, 3, 24, 25, 26.

**Three need one document each**: 9 (21 U.S.C. § 374), 12 (*Alvarez*), 16 (*Van Buren*).

**Twelve are judgment**, and nine of those sit in SEC. 6, SEC. 8 and SEC. 3.

**So a v3.5 assembled from A and completed-B would be eight amendments** — and would leave every
fatal finding in SEC. 6 untouched, because those are all C. A revision that fixes the punctuation
and not the offense would be worse than no revision, since it would carry a new version number
while the individual-liability offense still cannot be pleaded.
