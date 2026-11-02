# Case study: triaging support requests with an AI assistant, and measuring what it is worth


> **Measured on the French-language run.** The requests quoted here (IDs such as D043, S003, R013) exist in this repository in English translation (`data/`); the figures were not re-measured on the translation.
> Demonstration project on **entirely synthetic data**: the company (a sports retailer), its 8 procedures and all the requests are invented. No real customer data. I have worked on a real customer-support job (freelance), but nothing in this project comes from it.

## The problem

A support team receives requests of very different kinds: some are settled by a written procedure (delivery time, product return), others must never be handled automatically (threats, safety, personal data, anything outside the procedures). The costly error is not a slightly long answer; it is **answering alone a request that an advisor should have taken**.

Question asked: can an assistant read a request, decide whether to answer or hand over, and write a draft that an advisor reviews, **without ever sending anything itself**?

## What I built

An n8n + Claude workflow. For each request, the assistant picks a procedure among 8, decides "answer" or "escalate", gives its reason and writes a draft (or a holding message if escalated). The safety rule is simple: **when in doubt, it escalates**, and if its answer cannot be read, it escalates too.

## How I evaluated it

- **A no-AI baseline**: a keyword script, to know what the simplest tool is worth.
- **80 synthetic requests** (64 test, 16 validation never used to write the prompt), **21 edge cases** all to escalate, **15 requests in a more "real" style**.
- **The right measure.** A "never escalate" rule would score 87.5% correct decisions on the test set (56 requests out of 64 are to be handled) while missing 100% of escalations. So I tracked mainly **escalations caught** and **needless escalations**.
- **Scoring of the drafts** by an AI model (4 criteria), then a **human check** of 10 rows.
- **An error log** (13 entries) with cause, fix and decision.

## What happened

**Moving from keywords to a model has the biggest effect.** On the test set, the keyword baseline catches 3 escalations out of 8; the first prompt catches all of them (8/8) and goes from 80% to 91% correct decisions.

**Improving the form did not improve the decision.** Version 2 adds rules (always "Bonjour", ask for the order number): the drafts are better, the decisions are not (89%, then 91%). A rule added to fix one case (D025, an opened swimsuit) made others change, unrelated to it. This kind of noise is normal from one run to the next; I measured it instead of telling the story differently.

**Sonnet 5.5 scores 64/64, but that score deserves suspicion.** It wrongly escalates no request on the test set (against 6 for Haiku), at 13 times the cost (about $0.012 per request against $0.001). But two of its answers are questionable despite the perfect score, on labels I already considered debatable, and on the 15 "real-style" requests it does no better than Haiku (13/15 for both).

**My own labels are a source of error.** Several requests fall under two procedures, and some of my labels are arbitrary. I decided never to change them after seeing the results (except dated corrections), and to list them.

**Decisions I took, documented.** Any ambiguous case is escalated (31/10/2026), even if that creates needless escalations. On the "real-style" requests, two requests I had labelled "escalate" out of caution receive an answer from both models although the written procedures allow it: my rule is stricter than the procedures, not a model defect. I chose not to change the procedures and to write it down.

## What I take from it

- **Choose the measure before looking at results.** The correct-decision rate alone would have rewarded a tool that never escalates.
- **Separate the set used to fix from the set used to judge.** The v2 rules were written knowing the errors of the test set: they are favoured there. Only validation (16 requests, 14 correct decisions) is not, but it is small (only 2 escalations).
- **A more expensive model is not always useful.** Sonnet 5.5 reduces needless escalations but does not stand out on "real" cases; review by an advisor remains mandatory anyway.
- **Keep a trace of errors.** The log helped me decide what to fix and what to leave (for example the common-sense advice the draft adds outside the procedures).

## Limitations

Data and procedures written with the same approach as the prompt: results probably too favourable. A single run per version. Draft scoring done by an AI model, checked on 10 mostly simple rows (40 scores out of 40 identical, which proves nothing on hard cases). Costs computed from the account balance, to one cent. No test on real requests.

## What I would do next

1. Test on real, anonymised requests, with a client's agreement.
2. Repeat each run several times to measure variation.
3. Have a larger and harder sample scored by an advisor.
4. Quantify handling time with and without the assistant, labelled "assumption" until measured.
