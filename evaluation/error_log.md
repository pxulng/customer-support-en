# Error log: customer-support assistant (v1)


> **Measured on the French-language run.** The requests quoted here (IDs such as D043, S003, R013) exist in this repository in English translation (`data/`); the figures were not re-measured on the translation.
> All requests are **synthetic** (fictional). Version evaluated: n8n workflow v1, model Claude Haiku 5.5, a single complete run per set.
> Status of figures: **measured** = observed on the test set; **assumption** = supposed; **projected** = computed from the first two.

## 1. Measurement context

| Set | Size | Measured result |
|---|---|---|
| Main set (test) | 64 requests, 8 to escalate | 58/64 correct decisions (91%); 8/8 escalations caught; 6 needless escalations out of 56 |
| Edge cases | 21 requests, all to escalate | 20/21 escalations caught; 1 automatic reply wrongly given (S003) |
| Draft scoring | 40 drafts, scored by an AI model (4-criterion grid) | 24/40 judged ready to send as they are (22/40 before correcting 5 rows, see errors 4 and 5) |
| "Real-style" requests (15, written by Claude, labels reviewed by Paul) | 15 requests, 9 to escalate | Haiku and Sonnet: 13/15 conforming decisions, 7/9 escalations caught, same decisions (see error 13) |
| Human check | 10 rows, blind | 40 scores out of 40 identical to the model's (small, easy sample) |

Reservations: the prompt, the procedures and the requests were written with the same approach, which makes the results probably optimistic. The scores of rows D010, D037, D038, D071 and D072 were corrected (file `draft_scoring_v1.xlsx`); the human check covered 10 other rows, scored before this correction.

## 2. Errors found

Severity: **High** = violates the criterion "no request to escalate receives an automatic reply"; **Medium** = false information or needless decision; **Low** = finish.

| No. | IDs concerned | Severity | What happened | Probable cause | Planned fix in v2 | Status |
|---|---|---|---|---|---|---|
| 1 | S003 | High | A customer who wore trainers for 10 minutes outdoors gets a polite refusal instead of being escalated. Automatic reply on a case to escalate (1 out of 29). | The "not worn" rule is not defined: where does "worn" start? The model decides alone. | Clarify the rule in procedure 02. **Paul's decision (31/10/2026): any ambiguous case is escalated** (no automatic refusal if the product's condition is doubtful). | Decided, to implement in v2 |
| 2 | D002 | Medium | For a Saturday order, the draft apologises for a delay on Tuesday, although 48 working hours have not yet passed. | The prompt does not say how to count working days, and the model concludes a delay without being able to verify it. | Add: "never conclude a delay if the dates do not show it; stay conditional". | To fix in v2 |
| 3 | D008, D009, D043, D055, D071, D072 | Medium | 6 needless escalations out of 56 requests to handle (11%): the model hands over although the procedure allowed an answer or the label is debatable. | "When in doubt, escalate" instruction: cautious by design. | To arbitrate: reduce doubts by clarifying procedures, without touching the safety rule. Measure that wrong automatic replies do not rise. **Paul's decision (31/10/2026): keep the current caution**; only ambiguous procedures are clarified. | Decided |
| 4 | D010, D037, D038 | Low | The draft does not ask for the order number, which an advisor would do in practice. | This rule does not exist in the v1 procedures: the criticism comes from the scoring, not the model. | Add the rule to the v2 procedures, then score v2 with this rule. Remove the penalty in the v1 scoring. | v1 scoring corrected; rule to add in v2 |
| 5 | D071, D072 | Low | Completeness scored 2 because the model escalated: the score mixed the decision with the text of the message. | Scoring defect, not model defect. | Score the holding message for what it is; the decision is counted in error 3. | v1 scoring corrected |
| 6 | 15 drafts out of 85 | Low | The draft starts without "Bonjour" (measured by automatic count on the 85 drafts of both sets). | The prompt does not require a greeting. | Add: "always start with Bonjour". | To fix in v2 |
| 7 | D009, S001, S009, D061 | Low | Language mistakes found: "ssincèrement" (twice), "que un conseiller", "Restez à votre disposition" instead of "Nous restons". | Variation of the low-cost model; no automatic proofreading. | Compare with Claude Sonnet 5.5; add a proofreading instruction. Partial review: not all 85 drafts were read. | To fix in v2 |
| 8 | D004 | Low | The draft writes "we cannot guess the size that will suit you", a curt tone. | The model repeats the wording of the internal instruction ("without guessing") in the customer message. | Rephrase the instruction in customer language ("advise comparing with a well-fitting garment"). | To fix in v2 |
| 9 | D001 to D005 (trials) | Medium | Drafts change from one run to the next for the same request. A holding message for D003 implied a refusal in one trial, not in the final run. | The model does not answer exactly the same way twice. | Keep a single complete run as the reference. Test a temperature setting if the n8n node allows it (not verified). | To document |
| 10 | D002 (trial) | Medium | An answer was cut mid-way and could not be read ("ERREUR_JSON"). | Token limit too low: the model's internal thinking used the room for the answer. | Limit raised to 4000 tokens, problem solved. The reading code escalates for safety when an answer is unreadable, which avoided a faulty reply. | Resolved |
| 11 | D025, D005, D018, D063 | Medium | In v2, the opened swimsuit (D025) is escalated although the procedure provides a refusal for hygiene; D005, D018 and D063 also go to "escalate". Needless escalations: 7 out of 56 in v2 (6 in v1). | The rule added in v2 (doubtful product condition → escalate) is too broad for D025; for the other 3, the model changes decision without a precise rule (run-to-run variation possible). | v2.1: the rule does not apply to exclusions already written (hygiene, personalised, sale items). Effect to measure on the 64 requests. | Fixed: D025 returns to "answer" in v2.1 (64-request set: 58/64 correct decisions, 6 needless escalations). D005 too, but D072 moves to "escalate" unrelated to the rule (run-to-run variation) |
| 12 | D077, D022 | Medium | The D077 draft advises not reusing the helmet "as a precaution"; the D022 draft (v2.1) asks not to send a password by email. No procedure says either. | The model adds common-sense safety advice outside the procedures (rule 1: invent nothing). | An advisor always reviews this draft (escalated case). To decide: forbid any unwritten advice, or accept it on safety cases. | To arbitrate |
| 13 | R013, R014 ("real-style" requests) | Medium | Haiku and Sonnet answer a tracking issue blocked for 6 days (R013) and a bike-helmet return (R014), although Paul labelled them "escalate" (rule: any hesitation is escalated). 13/15 conforming decisions, 7/9 escalations caught. | The written procedures cover these two cases: Paul's rule is stricter than the procedures; this is not a model defect. | **Paul's decision (31/10/2026): keep the procedures as they are**; the gap is documented, no rule added. | Decided (option A) |

## 3. Defects of the test set (not of the model)

These gaps come from my initial labels, not from the assistant's behaviour. They will only be corrected in a dated version 2 of the set, so that expectations are not changed after seeing the results.

| ID | Why the label is debatable |
|---|---|
| D008 | "Does this tent sleep 3 adults?": the assistant has no product sheet, so cannot answer. Expected value to revisit (escalate). |
| D018, D039, S002 | Two procedures apply to the request (08 and 02; 02 and 05; 01 and 08): the "expected" procedure was arbitrary. |
| D043, D055 | The procedure does not clearly decide (doubt about the origin of the defect; colour change not provided for). |
| D009, D039, D070 | Two procedures apply (08 and 01; 02 and 05; 01 and 05): the procedure gap in v2 is not a model error. |
| D059, D074 (validation) | "Is this jacket waterproof?" (information absent from the sheet) and "change the address of a parcel already shipped" (not provided for): escalating is defensible, the "answer" label is debatable. Not changed afterwards. |

## 4. What this log does not show

- Behaviour with real requests, which will be more varied and messier.
- The model's behaviour over many runs: a single run per set.
- The reliability of the model's scoring on hard cases: the human check covered only 10 rows, mostly simple.
