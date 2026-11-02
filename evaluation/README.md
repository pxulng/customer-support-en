# Evaluation

Results and analyses of every version of the assistant. **All requests are synthetic.** Each result comes from a single run. **The raw CSV/XLSX outputs are those of the French-language run** (French headers and French drafts; `decision_attendue` = `expected_decision`, `repondre` = answer, `escalader` = escalate); they were not re-generated on the English translation. For the overview, start with the first two files.

| File | Contents |
|---|---|
| `version_comparison.md` | Comparison table: baseline, v1, v2, v2.1 (Haiku 5.5) and Sonnet 5.5, with cost per request |
| `error_log.md` | 13 errors: what happened, probable cause, fix, decision |
| `results_baseline.csv`, `results_baseline_edge_cases.csv` | Keyword reference, no AI |
| `results_v1_haiku55.csv`, `results_v1_edge_cases.csv` | Prompt v1 (test set, edge cases) |
| `results_v2_haiku55.csv`, `results_v2_edge_cases.csv` | Prompt v2 |
| `results_v2_1_haiku55.csv`, `results_v2_1_sonnet55.csv` | Prompt v2.1 on the test set, with Haiku 5.5 and Sonnet 5.5 |
| `results_v2_1_validation.csv` | Prompt v2.1 on the 16 validation requests (never used to write the prompt) |
| `results_realistic_v2_1_haiku55.csv`, `results_realistic_v2_1_sonnet55.csv` | Prompt v2.1 on the 15 "real-style" requests |
| `draft_scoring_v1.xlsx` | Scoring of 40 v1 drafts on 4 criteria, **done by an AI model** (5 rows corrected) |
| `human_check_10_rows.xlsx` | 10 rows of the scoring re-checked by hand (small, easy sample) |

Main columns of the result files: `decision_attendue` (label), the model's decision, `decision_ok` (1 if conforming), the reason given and the draft (in French). Labels are not changed after seeing the results; corrections are dated in the log.
