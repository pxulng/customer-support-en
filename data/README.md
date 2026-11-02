# Data

**All data is synthetic**: no request, name or number comes from a real customer. The content is an **English translation** of the French original (same IDs, same labels), see the root README.

| File or folder | Contents |
|---|---|
| `procedures/` | The 8 fictional procedures used by the assistant |
| `requests_synthetic.csv` | 80 labelled requests: 64 for testing, 16 for validation (`set` column) |
| `edge_cases_escalation.csv` | 21 hard cases, all to escalate (threats, safety, fraud, out of scope) |
| `requests_realistic.csv` | 15 requests in the style of real messages (short, typos, several topics), written by Claude, labels reviewed by the author on 31/10/2026 |

Columns: `id`, `set`, `origin` (always `SYNTHETIC`), `expected_procedure`, `expected_decision` (`answer` or `escalate`), and depending on the file `difficulty` (easy / ambiguous / trap) and `key_points`; the realistic file also has `hesitation`, `claude_initial_decision` and `corrected_by_paul_on`.

Original French file names (renamed in this edition): `demandes_synthetiques.csv` → `requests_synthetic.csv`; `cas_limites_escalade.csv` → `edge_cases_escalation.csv`; `demandes_realistes.csv` → `requests_realistic.csv`. Values: `repondre` / `escalader` → `answer` / `escalate`.

Rule: the validation set was only used to measure, never to write or adjust a prompt.

`original_fr/` holds the three **French original** CSV files under the same English file names (the ones the measured runs and the keyword baseline used; French column names and content). They are kept so that the published figures can be traced back to the exact data they come from.
