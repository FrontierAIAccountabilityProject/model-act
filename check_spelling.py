#!/usr/bin/env python3
"""
check_spelling.py — hold the repository to American spelling.

Why this exists. The Act is a model statute offered to American state
legislatures, and `model_act_v3_4.txt` is already written in American spelling
but for two words. The commentary around it drifted British. A reader who
searches "defense counsel" or "willful blindness" in the site search bar finds
nothing, and a legislative counsel running a conformity check sees a mismatch
between the instrument and its own companion.

Scope. Every tracked .md file except `archive/` (superseded versions are a
record, not a live document). `model_act_v3_4.txt` is NEVER touched here: it is
tagged and checksummed, so a change to it is a cure with an amendment number,
not a sweep. See CURE 22.

Quotations. A quotation from a British source must keep its own spelling.
This tool cannot tell a quoted passage from drafted statutory text, and both
live in blockquotes here. So blockquote lines are never auto-changed; they are
listed for a human to decide. That is the same rule as E22: quote in hand.

Usage:
    python3 check_spelling.py            # report only
    python3 check_spelling.py --apply    # rewrite non-blockquote lines
"""
import os, re, sys

APPLY = "--apply" in sys.argv
SKIP_DIRS = {".git", "_site", "archive", "_sass", "_includes", "node_modules"}

# Files that declare themselves unalterable in their own opening lines.
# audit/record.md: "concatenates, verbatim and unedited ... their content is unchanged".
# dossier/README.md: "It is sealed: the text below is never edited, because a
# record whose contents change is not a record." Those are the project's rules
# and they bind this tool too.
SKIP_FILES = {"./audit/record.md", "./dossier/README.md"}

# A merged block marked "content verbatim" is sealed from its BEGIN marker to
# the matching END, or to end of file where no END was ever written.
SEAL_BEGIN = re.compile(r"<!--\s*BEGIN\b.*content verbatim\s*-->")
SEAL_END   = re.compile(r"<!--\s*END\b.*-->")

# British -> American. Only pairs where American English genuinely differs.
# Deliberately absent: analysis/analyses (same in both), de minimis (Latin),
# advertise/exercise/supervise/comprise/surprise/enterprise (same in both),
# archaeology, aesthetic (both current in American usage).
PAIRS = {
 # -ence / -ense
 "defence":"defense","defences":"defenses","defenceless":"defenseless",
 "offence":"offense","offences":"offenses",
 "pretence":"pretense","licence":"license","licences":"licenses",
 "practise":"practice","practises":"practices","practised":"practiced","practising":"practicing",
 # -our
 "colour":"color","colours":"colors","coloured":"colored",
 "honour":"honor","honours":"honors","honoured":"honored","honourable":"honorable",
 "behaviour":"behavior","behaviours":"behaviors","behavioural":"behavioral",
 "favour":"favor","favours":"favors","favoured":"favored","favourable":"favorable",
 "favourably":"favorably","favouring":"favoring","favourite":"favorite",
 "labour":"labor","labours":"labors","laboured":"labored","labouring":"laboring",
 "neighbour":"neighbor","neighbours":"neighbors","neighbouring":"neighboring",
 "rumour":"rumor","rumours":"rumors","endeavour":"endeavor","endeavours":"endeavors",
 "vapour":"vapor","armour":"armor","harbour":"harbor","harbouring":"harboring",
 "rigour":"rigor","rigours":"rigors","vigour":"vigor","odour":"odor",
 "demeanour":"demeanor","candour":"candor","clamour":"clamor","fervour":"fervor",
 "splendour":"splendor","valour":"valor","savour":"savor",
 # -ise / -isation
 "organise":"organize","organised":"organized","organising":"organizing",
 "organisation":"organization","organisations":"organizations","organisational":"organizational",
 "recognise":"recognize","recognised":"recognized","recognising":"recognizing",
 "recognisable":"recognizable","recognisably":"recognizably",
 "criminalise":"criminalize","criminalised":"criminalized","criminalising":"criminalizing",
 "criminalisation":"criminalization","decriminalise":"decriminalize",
 "minimise":"minimize","minimised":"minimized","minimising":"minimizing","minimisation":"minimization",
 "maximise":"maximize","maximised":"maximized","maximising":"maximizing",
 "emphasise":"emphasize","emphasised":"emphasized","emphasising":"emphasizing",
 "characterise":"characterize","characterised":"characterized","characterising":"characterizing",
 "characterisation":"characterization","characterisations":"characterizations",
 "realise":"realize","realised":"realized","realising":"realizing",
 "prioritise":"prioritize","prioritised":"prioritized","prioritising":"prioritizing",
 "summarise":"summarize","summarised":"summarized","summarising":"summarizing",
 "generalise":"generalize","generalised":"generalized","generalising":"generalizing",
 "specialise":"specialize","specialised":"specialized","specialising":"specializing",
 "formalise":"formalize","formalised":"formalized","formalising":"formalizing",
 "normalise":"normalize","normalised":"normalized","normalising":"normalizing",
 "centralise":"centralize","centralised":"centralized","decentralise":"decentralize",
 "decentralised":"decentralized","institutionalise":"institutionalize",
 "institutionalised":"institutionalized","legitimise":"legitimize","legitimised":"legitimized",
 "utilise":"utilize","utilised":"utilized","utilising":"utilizing",
 "apologise":"apologize","apologised":"apologized",
 "authorise":"authorize","authorised":"authorized","authorising":"authorizing",
 "authorisation":"authorization","authorisations":"authorizations",
 "penalise":"penalize","penalised":"penalized","penalising":"penalizing",
 "finalise":"finalize","finalised":"finalized","stabilise":"stabilize","stabilised":"stabilized",
 "mobilise":"mobilize","mobilised":"mobilized",
 "harmonise":"harmonize","harmonised":"harmonized","harmonisation":"harmonization",
 "standardise":"standardize","standardised":"standardized","standardisation":"standardization",
 "neutralise":"neutralize","neutralised":"neutralized",
 "scrutinise":"scrutinize","scrutinised":"scrutinized","scrutinising":"scrutinizing",
 "memorialise":"memorialize","memorialised":"memorialized",
 "operationalise":"operationalize","operationalised":"operationalized",
 "incentivise":"incentivize","incentivised":"incentivized","incentivising":"incentivizing",
 "marginalise":"marginalize","marginalised":"marginalized",
 "publicise":"publicize","publicised":"publicized",
 "civilise":"civilize","civilised":"civilized","industrialise":"industrialize",
 "industrialised":"industrialized","modernise":"modernize","modernised":"modernized",
 "rationalise":"rationalize","rationalised":"rationalized",
 "systematise":"systematize","systematised":"systematized",
 "visualise":"visualize","visualised":"visualized",
 "categorise":"categorize","categorised":"categorized","categorising":"categorizing",
 "itemise":"itemize","itemised":"itemized","legalise":"legalize","legalised":"legalized",
 "nationalise":"nationalize","nationalised":"nationalized","privatise":"privatize",
 "privatised":"privatized","subsidise":"subsidize","subsidised":"subsidized",
 # -yse (analysis / analyses correctly excluded)
 "analyse":"analyze","analysed":"analyzed","analysing":"analyzing","analyser":"analyzer",
 "paralyse":"paralyze","paralysed":"paralyzed","catalyse":"catalyze","catalysed":"catalyzed",
 # -re
 "centre":"center","centres":"centers","centred":"centered","centring":"centering",
 "metre":"meter","metres":"meters","kilometre":"kilometer","kilometres":"kilometers",
 "litre":"liter","litres":"liters","theatre":"theater","fibre":"fiber","fibres":"fibers",
 "calibre":"caliber","sombre":"somber","lustre":"luster","spectre":"specter",
 "manoeuvre":"maneuver","manoeuvres":"maneuvers","manoeuvred":"maneuvered",
 # doubled l in British
 "travelled":"traveled","travelling":"traveling","traveller":"traveler","travellers":"travelers",
 "modelling":"modeling","modelled":"modeled","labelling":"labeling","labelled":"labeled",
 "cancelled":"canceled","cancelling":"canceling","signalling":"signaling","signalled":"signaled",
 "counselling":"counseling","counselled":"counseled","counsellor":"counselor","counsellors":"counselors",
 "levelled":"leveled","levelling":"leveling","totalled":"totaled","totalling":"totaling",
 "fuelled":"fueled","fuelling":"fueling","channelled":"channeled","channelling":"channeling",
 "funnelled":"funneled","quarrelled":"quarreled","equalled":"equaled","marvelled":"marveled",
 # single l in British
 "fulfil":"fulfill","fulfils":"fulfills","fulfilment":"fulfillment",
 "enrol":"enroll","enrols":"enrolls","enrolment":"enrollment",
 "instalment":"installment","instalments":"installments",
 "skilful":"skillful","skilfully":"skillfully",
 "wilful":"willful","wilfully":"willfully","wilfulness":"willfulness",
 "instil":"instill","enthral":"enthrall","appal":"appall",
 # miscellaneous
 "judgement":"judgment","judgements":"judgments",
 "acknowledgement":"acknowledgment","acknowledgements":"acknowledgments",
 "abridgement":"abridgment","storey":"story","storeys":"stories",
 "programme":"program","programmes":"programs",
 "cheque":"check","cheques":"checks","kerb":"curb","plough":"plow","gaol":"jail",
 "draught":"draft","moustache":"mustache","grey":"gray","greyed":"grayed",
 "sceptic":"skeptic","sceptics":"skeptics","sceptical":"skeptical","sceptically":"skeptically",
 "scepticism":"skepticism","mould":"mold","moulded":"molded","smoulder":"smolder",
 "speciality":"specialty","specialities":"specialties","aluminium":"aluminum",
 "sulphur":"sulfur","encyclopaedia":"encyclopedia","foetus":"fetus","oestrogen":"estrogen",
 "paediatric":"pediatric","orthopaedic":"orthopedic",
 "whilst":"while","amongst":"among","amidst":"amid",
 "afterwards":"afterward","backwards":"backward","forwards":"forward",
 "upwards":"upward","downwards":"downward","onwards":"onward","towards":"toward",
 "learnt":"learned","spelt":"spelled","dreamt":"dreamed","leapt":"leaped",
 "focussed":"focused","focusses":"focuses","focussing":"focusing",
 "artefact":"artifact","artefacts":"artifacts","artefactual":"artifactual",
 "benefitted":"benefited","benefitting":"benefiting","targetted":"targeted",
}

# Spans matched here are masked before substitution and restored after, so an
# official name keeps the spelling its owner uses.
PROTECT = [
 r"Organisation for Economic Co-operation and Development",
 r"National Cyber Security Centre", r"Government Cyber Coordination Centre",
 r"Government Cyber Defence", r"Today programme",
 r"Ministry of Defence", r"Defence Science and Technology",
 r"Labour Party", r"World Health Organisation",
 r"Minderoo Centre for Technology and Democracy",
 r"Centre for [A-Z][A-Za-z ]+",
 r"Programme for [A-Z][A-Za-z ]+",
 r"International Labour Organisation",
 r"https?://\S+", r"`[^`\n]+`",
 # a passage that names a British spelling in order to argue about it
 r"\*\*`?misdemeanour`?\*\* appeared", r"the map held \*demeanour\*",
 # A link into a sealed document must keep the sealed heading's spelling, or
 # the anchor stops resolving. check_links.py is the guard that proves it.
 r"\]\((?:\.\./|\./)*(?:audit/)?(?:ledger/)?(?:dossier/)?"
 r"(?:record|errata|changelog|diary|README)\.md#[^)]*\)",
 # Any span inside quotation marks is a quotation until proven otherwise.
 # An inline quote on an ordinary line is exactly as unalterable as one in a
 # blockquote: AISI writes "push models towards", and toward/towards is in the
 # map. Masking these is what stops the tool falsifying a source.
 # Known limitation, accepted deliberately: quote marks alternate, so a span
 # BETWEEN two quotations reads as quoted and is protected too. That under-changes
 # a little of the project's own prose. Under-changing is recoverable; falsifying
 # a source is not, so the error is left pointing this way.
 # Multi-line, and it must be: a quotation that wraps across a line break is
 # still a quotation. The single-line version of this rule falsified fourteen
 # of them on 25 August 2026 — including the UK Health and Safety at Work etc.
 # Act 1974 s.37, four AISI passages, and the tagged statute's own "wilful" —
 # and the tool that exists to protect quotations was the thing that broke them.
 r"\u201c[^\u201d]{0,600}\u201d", r'"[^"]{0,600}"',
]

# Blockquote lines that are verbatim quotation from a British-spelling source.
# These keep their own spelling forever; altering them would falsify the quote.
# Same idea as ALLOWED_UNLINKED in check_links.py: the exception is written down
# with its reason, so a later run does not re-litigate it.
FOREIGN_QUOTES = {
 ("./README.md", "National Cyber Security Centre"): "UK DSIT/NCSC publication title",
 ("./README.md", "accountability for an organisation"): "UK government quote",
 ("./README.md", "that organisation."): "UK government quote",
 ("./research/aisi_incident_inc_2026_07_28_01.md", "seems misguided"): "quoted researcher",
 ("./research/aisi_incident_inc_2026_07_28_01.md", "rather than a technical barrier"): "AISI quote",
 ("./research/press_corpus_july_august_2026.md", "seems misguided"): "quoted researcher",
 ("./research/press_corpus_july_august_2026.md", "specification gaming"): "DeepMind quote",
 ("./research/press_corpus_july_august_2026.md", "before traditional defences"): "quoted source",
 ("./standards/comparative_officer_liability.md", "Where an offence under any"): "UK HSWA 1974 s.37 verbatim",
 ("./standards/comparative_officer_liability.md", "offence and shall be liable"): "UK HSWA 1974 s.37 verbatim",
 ("./standards/house_language.md", "seems misguided"): "quoted researcher",
 ("./standards/why_a_signature_works.md", "accountability for an organisation"): "UK government quote",
 ("./standards/why_a_signature_works.md", "that organisation."): "UK government quote",
 ("./standards/why_a_signature_works.md", "any single organisation can"): "UK government quote",
 ("./standards/frontier_bill_census.md", "knowingly \u00b7 wilful/willful"): "census row deliberately carries both spellings",
 ("./ledger/changelog.md", "Independent Verification **Organisation**"): "quotes the census's own error",
 ("./ledger/changelog.md", "knowingly or **wilfully**"): "quotes the tagged text verbatim",
 ("./ledger/changelog.md", "*wilful/willful* both ways"): "names both spellings on purpose",
 ("./audit/record.md", None): "the frozen record records what the text said on the day",
 ("./dossier/README.md", None): "sealed dossier, quotes its sources verbatim",
}

# Blockquote lines that are the project's own drafted text, not quotation.
# The repository sets its own conclusions and its own proposed statutory
# language in blockquotes for emphasis, so a blockquote is not by itself proof
# of a quotation. Each of these was read before being listed.
OWN_BLOCKQUOTES = [
 ("./research/aisi_incident_inc_2026_07_28_01.md", "Both organisations traced"),
 ("./ledger/errata.md", "may characterise another"),
 ("./docs/known_objections.md", "Uncertainty is not the offence"),
 ("./docs/known_objections.md", "are the potential offences"),
 ("./audit/v3_5_cure_language.md", "behaviour under evaluation"),
 ("./audit/v3_5_cure_language.md", "requires no characterisation"),
 ("./audit/v3_5_cure_language.md", "the Agency is organised"),
 ("./audit/v3_5_cure_language.md", "designated, described, marketed"),
 ("./packets/enforcement.md", "requires no characterisation"),
 ("./packets/enforcement.md", "the Agency is organised"),
 ("./audit/v3_5_cure_language.md", "Nothing in this subsection authorises"),
 ("./packets/enforcement.md", "Nothing in this subsection authorises"),
 # CURE 22 quotes the tagged text's "wilfully" verbatim and then argues about
 # that spelling. The tool must not quietly win the argument.
 ("./audit/v3_5_cure_language.md", "knowingly or wilfully"),
 ("./audit/v3_5_cure_language.md", "a knowing or"),

 ("./standards/house_language.md", "billion, itemised"),
 ("./standards/house_language.md", "Two organisations, investigating"),
]

def is_own(path, line):
    return any(p == path and m in line for p, m in OWN_BLOCKQUOTES)

def is_foreign(path, line):
    for (p, marker), _ in FOREIGN_QUOTES.items():
        if p != path: continue
        if marker is None or marker in line: return True
    return False

_PFX = r"(?:un|re|mis|dis|pre|non|over|under|inter|counter)?"
WORD = re.compile(r"\b(" + _PFX + r")(" +
                  "|".join(sorted(PAIRS, key=len, reverse=True)) + r")\b", re.I)

# The -ise family is productive, so an explicit list always trails the language:
# the first pass over this repository listed "criminalise" and missed
# "criminalises". This rule covers the whole morphology, and the exception set
# below is the words that genuinely end -ise in American English.
_EXCEPT_BASES = """advertise advise apprise appraise arise bruise chastise circumcise
comprise compromise cruise demise despise devise disguise enfranchise disenfranchise
excise exercise franchise improvise incise liaise merchandise praise premise prise
promise revise supervise surmise surprise televise treatise expertise paradise
malvertise noise poise raise rise wise precise concise misadvise reprise remise
practise enterprise misprise apprise disprise imprecise""".split()
EXCEPT = set()
for b in _EXCEPT_BASES:
    stem = b[:-1] if b.endswith("e") else b
    EXCEPT.update({b, b + "s", stem + "ed", stem + "ing", stem + "es",
                   stem + "ation", stem + "ations"})

RULE = re.compile(r"\b([A-Za-z]{3,}?)(is)(e|es|ed|ing|ation|ations|ational)\b")

def _rule_sub(m):
    whole = m.group(0); low = whole.lower()
    if low in EXCEPT or low.endswith("wise") or low in PAIRS: return whole
    z = m.group(1) + ("IZ" if m.group(2).isupper() else "iz") + m.group(3)
    return z

def recase(src, dst):
    if src.isupper(): return dst.upper()
    if src[0].isupper(): return dst[0].upper() + dst[1:]
    return dst

FENCE  = re.compile(r"(?ms)^```.*?^```")
BQLINE = re.compile(r"(?m)^[ \t]*>.*$")
SEALED = re.compile(r"(?s)" + SEAL_BEGIN.pattern + r".*?(?:" + SEAL_END.pattern + r"|\Z)")

def protected_spans(text, path):
    """Character ranges the sweep must not touch.

    Computed over the WHOLE file, never line by line. The per-line version of
    this could not see a quotation that wrapped across a line break, and on
    25 August 2026 it falsified fourteen of them.  Returns (spans, review),
    where review lists blockquote lines carrying a hit for a human to decide.
    """
    spans = []
    for rx in (FENCE, SEALED):
        spans += [m.span() for m in rx.finditer(text)]
    for pat in PROTECT:
        spans += [m.span() for m in re.finditer(pat, text)]
    review_spans = []
    for m in BQLINE.finditer(text):
        line = m.group(0)
        if is_own(path, line): continue
        (spans if is_foreign(path, line) else review_spans).append(m.span())
    return spans, review_spans

def _in(spans, a, b):
    return any(s <= a and b <= e for s, e in spans)

def convert_text(text, path):
    spans, review_spans = protected_spans(text, path)
    hits, held, review = [], 0, []
    out, last = [], 0
    def emit(m, new):
        out.append(text[last[0]:m.start()]); out.append(new); last[0] = m.end()
    last = [0]
    events = sorted(
        [(m.start(), m.end(), recase(m.group(2), PAIRS[m.group(2).lower()]), m.group(1))
         for m in WORD.finditer(text)] +
        [(m.start(), m.end(), _rule_sub(m), None) for m in RULE.finditer(text)],
        key=lambda e: e[0])
    prev_end = -1
    for a, b, new, pfx in events:
        if a < prev_end: continue
        old = text[a:b]
        cand = (pfx + new) if pfx is not None else new
        if cand == old: continue
        if _in(spans, a, b):
            held += 1; prev_end = b; continue
        if _in(review_spans, a, b):
            ln = text.count("\n", 0, a) + 1
            review.append((path, ln, [old], text[text.rfind("\n", 0, a)+1:text.find("\n", b)].strip()[:150]))
            prev_end = b; continue
        out.append(text[last[0]:a]); out.append(cand); last[0] = b
        hits.append((old, cand)); prev_end = b
    out.append(text[last[0]:])
    return "".join(out), hits, held, review

def main():
    changed_files = 0; total = 0; review = []; tally = {}; known = 0; skipped = []
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in sorted(files):
            if not (fn.endswith(".md") or
                    (fn.startswith("build_") and fn.endswith(".py"))): continue
            path = os.path.join(root, fn)
            if path in SKIP_FILES: skipped.append(path); continue
            lines = open(path, encoding="utf-8").read().split("\n")
            text = "\n".join(lines)
            new_text, hits, held_n, rev = convert_text(text, path)
            known += held_n; review += rev
            for w, a in hits:
                k = f"{w.lower()} -> {a.lower()}"; tally[k] = tally.get(k, 0) + 1
            total += len(hits); touched = bool(hits)
            if touched and APPLY: open(path, "w", encoding="utf-8").write(new_text)
            if touched:
                changed_files += 1
    print(f"{'APPLIED' if APPLY else 'DRY RUN'}: {total} substitutions across {changed_files} files")
    print("\nby word:")
    for k, v in sorted(tally.items(), key=lambda x: -x[1]):
        print(f"  {v:5d}  {k}")
    print("\nfiles skipped as self-declared sealed: " + ", ".join(skipped))
    print(f"\nblockquote lines matching a recorded foreign quotation, left alone: {known}")
    print(f"blockquote lines needing a human decision: {len(review)}")
    for p, i, ws, t in review[:200]:
        print(f"  {p}:{i}  [{', '.join(ws)}]  {t}")
    if len(review) > 200: print(f"  ... and {len(review)-200} more")

main()
