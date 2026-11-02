"""Simple keyword baseline (no AI).
Rules written from the procedures. Evaluated on the "test" set only:
the "validation" set is reserved for the final comparison.
Keywords are French because the requests are in French.
Usage: python3 baseline.py requests_synthetic.csv [results_baseline.csv]
"""
import csv, sys, collections

ESCALADE = ["avocat", "juridique", "recours", "signalement", "dgccrf", "geste", "exception",
            "piraté", "piratage", "fraude", "non autorisé", "rgpd", "données", "casque",
            "harnais", "médical", "colère", "honte", "réseaux"]

PROCEDURES = {
    "01": ["colis", "livraison", "livré", "suivi", "expédi", "transporteur", "préparation"],
    "02": ["retour", "renvoyer", "rembours", "échang", "retourner"],
    "03": ["défaut", "défectueux", "garantie", "couture", "fermeture", "déchir", "fuit", "cassé", "usé"],
    "04": ["paiement", "débit", "débité", "facture", "promo", "carte bancaire", "paypal"],
    "05": ["annul", "modifier ma commande", "changer la taille"],
    "06": ["taille", "imperméable", "convient", "compatible", "matière", "stock"],
    "07": ["mot de passe", "compte", "connexion", "réinitialisation", "newsletter"],
    "08": ["réclamation", "injuste", "déçu", "inacceptable"],
}

def predict(text):
    t = text.lower()
    scores = {p: sum(k in t for k in kws) for p, kws in PROCEDURES.items()}
    best = max(scores.values())
    proc = "aucune" if best == 0 else next(p for p, s in scores.items() if s == best)
    esc = proc == "aucune" or any(k in t for k in ESCALADE)
    return proc, ("escalader" if esc else "repondre")

if __name__ == "__main__":
    rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter=";"))
    # jeu principal : seulement « test » ; fichier de cas limites : tout (jeu = « stress »)
    test = [r for r in rows if r["jeu"] in ("test", "stress")]
    out = []
    for r in test:
        p, d = predict(r["demande"])
        out.append({**r, "procedure_baseline": p, "decision_baseline": d})
    n = len(out)
    ok_proc = sum(o["procedure_baseline"] == o["procedure_attendue"] for o in out)
    ok_dec = sum(o["decision_baseline"] == o["decision_attendue"] for o in out)
    a_esc = [o for o in out if o["decision_attendue"] == "escalader"]
    esc_ok = sum(o["decision_baseline"] == "escalader" for o in a_esc)
    fautes = [o for o in a_esc if o["decision_baseline"] == "repondre"]
    a_rep = [o for o in out if o["decision_attendue"] == "repondre"]
    esc_inutiles = [o for o in a_rep if o["decision_baseline"] == "escalader"]
    print(f"Jeu test : {n} demandes (validation non utilisée)")
    print(f"Bon classement (procédure)      : {ok_proc}/{n} = {ok_proc/n:.0%}")
    print(f"Bonne décision (répondre/escal.) : {ok_dec}/{n} = {ok_dec/n:.0%}")
    print(f"Escalade correcte (rappel)       : {esc_ok}/{len(a_esc)} = {esc_ok/len(a_esc):.0%}")
    print(f"Réponses auto à tort sur cas à escalader : {len(fautes)}")
    print(f"Escalades inutiles (cas à répondre)      : {len(esc_inutiles)}/{len(a_rep)}")
    print("Par difficulté (bonne décision) :")
    for d in ("facile", "ambigu", "piege"):
        s = [o for o in out if o["difficulte"] == d]
        print(f"  {d:7s}: {sum(o['decision_baseline']==o['decision_attendue'] for o in s)}/{len(s)}")
    print("Cas à escalader traités à tort par réponse auto :", [o["id"] for o in fautes])
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(out[0].keys()), delimiter=";")
            w.writeheader(); w.writerows(out)
