# Prompts

The prompts are in English. They are a **translation** of the French prompts used in the measured runs; the translated version has **not** been re-run (see the root README).

| File | Version | Change |
|---|---|---|
| `prompt_v1.txt` | v1 | Rules, JSON output format and the 8 procedures |
| `prompt_v2.txt` | v2 | Adds: greeting, no conclusion of a delay without proof, ask for the order number, no repetition of internal instructions, escalation of products in doubtful condition |
| `prompt_v2_1.txt` | v2.1 | Fixes a side effect of v2: the product-condition rule does not apply to exclusions already written (hygiene, personalised, sale items) |

All prompts end with `{{ $json.demande }}`, where n8n inserts the customer request (the n8n code nodes still use the key `demande`). The JSON keys and the decision values (`repondre` / `escalader`) deliberately stay in French so that the workflow's reading node and the result files keep working. Results of each version are in `evaluation/version_comparison.md`.
