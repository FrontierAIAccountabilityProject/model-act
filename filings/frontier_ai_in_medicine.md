# Does the frontier touch medicine? — what the regulator can and cannot see

*The question this file answers was put to the project on 21 August 2026 and it is the sharpest
challenge the project has faced: **the Act covers systems trained above 10²⁶ operations, but the
medical-device evidence this project has read is mostly about small, narrow, task-specific models.
If those are two different technologies, the evidence base is about something other than the
statute.***

*The answer, from FDA's own materials, is in three parts. **It does not resolve the way anyone
expected.***

---

## Who this is about

**About:** frontier developers — the companies training general-purpose models above 10²⁶
operations — and whether their systems are reaching patients.

**Not about:** the hundreds of narrow, task-specific AI devices FDA has already authorised, which
are a different technology and are not what this Act covers.

---

## 1. FDA has opened the question, in the present tense of something arriving

On **18 August 2026** — three days before this file — FDA's Digital Health Center of Excellence
published *Considerations for the Regulation of Generative AI-Enabled Medical Devices*, with a
request for feedback under **docket FDA-2026-N-7874**, closing **19 October 2026**.

FDA's own framing is worth reading for its tense. The Center's director:

> *"Generative AI-enabled medical devices are **poised to reshape** the health technology
> landscape, and the FDA has an important responsibility to provide thoughtful leadership."*

And the agency's stated reason for asking:

> *"These devices may introduce **unique risks** when compared to traditional software and
> AI-enabled medical devices."*

**Poised to.** Not *have*. The regulator is preparing for an arrival rather than describing a
population.

*Sources: [FDA press announcement, 18 Aug 2026](https://www.fda.gov/news-events/press-announcements/fda-seeks-public-feedback-inform-regulatory-approach-generative-ai-enabled-medical-devices);
[the discussion paper](https://www.fda.gov/medical-devices/digital-health-center-excellence/considerations-regulation-generative-ai-enabled-medical-devices-discussion-paper-and-request).
⚠ **R** under [the confidence rubric](../standards/frontier_bill_census.md#the-confidence-rubric-governed-by-e15).*

---

## 2. And here is the finding, which is better than a number

The obvious next question is: *how many authorised devices already use a foundation model?*

**FDA cannot tell you.** Not because it will not — because the capability does not exist yet. From
the agency's own page on AI-enabled medical devices:

> *"To support transparency in the use of modern AI technologies, the FDA **will explore methods to
> identify and tag** medical devices that incorporate foundation models encompassing a wide range
> of AI systems, from large language models (LLMs) to multimodal architectures."*

**Will explore methods to identify.** The regulator holding the authoritative list of AI-enabled
medical devices in the United States does not currently have a way to say which of them are built
on frontier models.

And the list itself carries a caveat most people quoting it omit:

> *"The list is not a comprehensive resource of AI-enabled medical devices. Instead, the list
> includes AI-enabled medical devices that were identified primarily based on the **use of
> AI-related terms in the summary descriptions**."*

**The authoritative list is keyword-derived.** It finds devices that *said* they used AI.

*Source: [FDA, AI-enabled medical devices](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices),
last updated 16 June 2026 — ⚠ **R**.*

### What that means, stated carefully

**It does not mean the devices are unsafe**, or that FDA is failing. Building a taxonomy for a
technology that arrived this fast is genuinely hard, and the agency is doing it in public and
asking for help — which is more than most regulators and more than the frontier developers
themselves have done.

**It does mean nobody can currently answer the question this file asks**, including this project,
including FDA. Anyone who gives you a confident count of frontier models in regulated medicine is
telling you something the underlying data cannot support.

**But oversight downstream is not a duty upstream, and this file will not let the one stand in for
the other.** That FDA is building a taxonomy, running a docket and asking good questions is real
work — and **none of it reaches the person who decided a model was fit to release.** A regulator
examining the device at the end of the chain does not discharge the obligation of whoever started
it, any more than a food inspector discharges the duty of the person who shipped the batch. The
existence of somebody watching is routinely offered as a reason no further duty is needed. **It is
not one.**

**And notice what this technology is exempt from that far smaller undertakings are not.** To
experiment on a rat, an American researcher needs an institutional animal care and use committee, a
written protocol, and a named person answerable for it. To enrol a single human being in a trial,
someone signs **Form FDA 1572** in their own name before anyone is enrolled — see
[already a crime, if you are a person](../standards/already_a_crime_for_you.md). To release a
general-purpose model to three hundred million people, one in five of whom will ask it about their
health: **no protocol, no committee, no named person, no signature.** The oversight regimes
tighten as the number of subjects falls.

**And it is the accountability argument in miniature.** You cannot impose a duty on a category you
cannot identify. FDA is building the means of identification and saying so. **No such work is under
way at the other end** — no register of who decided a frontier model was fit to release, because no
statute asks for one.

---

## 3. Where the frontier actually reaches people — and it is not through the clinic

The strongest answer to *where does the frontier touch the average person* turns out to be:
**outside every one of these mechanisms.**

From Pew Research Center, 5,119 US adults, 17–23 February 2026:

- **49%** of American adults use AI chatbots
- **20%** — one in five — use one **for medical advice**
- **10%** use one **for emotional support or advice**
- **59%** are **not confident** US companies will develop these tools responsibly

*Source: [Pew Research Center, 17 June 2026](https://www.pewresearch.org/internet/2026/06/17/americans-and-ai-2026-chatbots-smart-devices-and-views-on-impact/) — ⚠ **R**.*

**One in five American adults is taking medical advice from a frontier model right now.** Not from
a cleared device. From a general-purpose chatbot that is:

- not an authorised medical device
- not on FDA's list, keyword-derived or otherwise
- carrying no labelling, no intended-use statement, no indications
- subject to no adverse-event reporting
- changeable overnight, without notice to anyone

**So the answer to the challenge is not that the frontier has not reached medicine.** It has
reached tens of millions of people's health decisions already — **by a route where none of the
apparatus applies.** The regulated channel is where the frontier is *arriving*. The unregulated one
is where it *arrived*.

---

## 4. What this changes in the project, honestly

**It strengthens the evidence base and narrows one claim.**

**Strengthens:** the FDA reading notes and the docket work are about the channel where oversight
exists and is being built. That FDA is *now* opening a generative-AI docket confirms the frontier
is entering that channel rather than undermining the relevance of what came before.

**Narrows:** this project should not say or imply that frontier models are widely deployed in
authorised medical devices today. **Nobody knows that, FDA included.** Where the project has
implied it, that is a correction owed. What it can say is documented above: the regulator is
preparing for their arrival, cannot yet identify them, and one in five adults is already using one
for health advice outside the system entirely.

**And it sharpens the October filing.** Docket FDA-2026-N-7874 asks about risk assessment,
premarket evaluation and postmarket monitoring for generative AI-enabled devices. **This project
has one thing to contribute that nobody else on that docket is likely to raise**, on the evidence
of the fifty-one comments on its predecessor: every mechanism proposed will be a document or a
downstream professional, and **not one will name the person upstream who decided the model was fit
to ship.**

---

*Corrections to the project contact; they enter [the errata register](../ledger/errata.md) with the
fix attached and permanent credit. Every FDA quotation above was read on fda.gov on 21 August 2026
and is graded ⚠ **R** — opened, not yet re-read by a human eye.*
