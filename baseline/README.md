# Baseline

`baseline.py` is the keyword reference (no AI). Its keywords are French and it reads the French original files (`data/original_fr/requests_synthetic.csv`, columns `demande`, `jeu`, ...), so it reproduces the published baseline figures on the French data. It has not been ported to the English translation.

Usage: `python3 baseline.py data/original_fr/requests_synthetic.csv results_baseline.csv`
