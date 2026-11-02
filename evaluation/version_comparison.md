# Version comparison (synthetic requests)


> **Measured on the French-language run.** The requests quoted here (IDs such as D043, S003, R013) exist in this repository in English translation (`data/`); the figures were not re-measured on the translation.
> All requests are **synthetic**. **Measured** results, a single run per version. Model of all Claude versions: Haiku 5.5 unless stated.

## Test set (64 requests, 8 to escalate)

| Version | Correct decisions | Correct procedure | Escalations caught | Needless escalations (out of 56) |
|---|---|---|---|---|
| Baseline (keywords, no AI) | 51/64 (80%) | 47/64 (73%) | 3/8 | 8 |
| Prompt v1 | 58/64 (91%) | 61/64 (95%) | 8/8 | 6 |
| Prompt v2 | 57/64 (89%) | 61/64 (95%) | 8/8 | 7 |
| Prompt v2.1 | 58/64 (91%) | 60/64 (94%) | 8/8 | 6 |
| Prompt v2.1 with Claude Sonnet 5.5 | 64/64 (100%) | 64/64 | 8/8 | 0 |

Reading: v1 clearly improves on the baseline, especially on escalations (8/8 versus 3/8). v2 improves the form of the drafts ("Bonjour" in 64/64, order number requested when needed) without improving decisions. The rules of v2 and v2.1 were written knowing the errors of this set: they are therefore favoured here. v2.1 fixes D025 (opened swimsuit) but, from one run to the next, D005 and D072 changed decision without the prompt concerning them: the same version does not always give the same result. With Sonnet 5.5 the score is perfect against my labels, but two of its answers remain questionable despite it: for D055 (changing the colour of an order in preparation), it states the order "can still be modified", which procedure 05 does not provide; for D043 (shoes coming unstuck), it answers instead of escalating the doubt about the origin of the defect. These two labels were already among those I considered debatable: the 64/64 should therefore be read with caution. The 4 procedure mismatches of v2.1 (D009, D018, D039, D070) concern requests where two procedures apply.

## Edge cases (21 requests, all to escalate)

| Version | Escalations caught |
|---|---|
| Baseline | not measured in this table |
| Prompt v1 | 20/21 (S003 wrongly answered) |
| Prompt v2 | 21/21 (the added rule targeted S003: not independent) |

## Validation set (16 requests, never used to write the prompt, of which 2 to escalate)

| Version | Correct decisions | Correct procedure | Escalations caught |
|---|---|---|---|
| Prompt v2.1 | 14/16 (88%) | 16/16 | 2/2 |

Small sample: "2 out of 2" escalations proves nothing solid.

## "Real-style" requests (15 requests written by Claude at Paul's request, labels reviewed by Paul on 31/10/2026: every hesitation turned into "escalate")

| Version | Correct decisions | Escalations caught (out of 9) | Wrong automatic replies |
|---|---|---|---|
| Prompt v2.1, Haiku 5.5 | 13/15 | 7/9 | 2 (R013, R014) |
| Prompt v2.1, Sonnet 5.5 | 13/15 | 7/9 | 2 (R013, R014) |

Both models make the same decisions on these 15 requests. Both errors come from requests that Paul classed "escalate" out of caution although the written procedures allow an answer: the gap comes from the rule, not the model. Measured cost: about $0.0007 per request with Haiku (low precision, 15 requests) and about $0.013 with Sonnet (balance 3.97 → 3.77).

## Cost (measured from the account balance, 1-cent precision)

| Series | Requests | Balance before → after | Cost per request |
|---|---|---|---|
| Edge cases, v2 | 21 | 4.94 → 4.91 | ≈ 0.0014 |
| Test set, v2 | 64 | 4.91 → 4.84 | ≈ 0.001 (between 0.0009 and 0.0013) |
| Test set, v2.1 | 64 | 4.83 → 4.77 | ≈ 0.0009 (between 0.0008 and 0.0011) |
| Test set, v2.1, Sonnet 5.5 | 64 | 4.77 → 3.98 (assumption: no other call between the two readings) | ≈ 0.012 (about 13 times Haiku) |

The cost includes the model's internal thinking, billed as output text. Currency assumed to be dollars.
