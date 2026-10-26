rendez_vous = {
    "R001": {"patient": "P001", "medecin": "Dr Karim", "date": "2026-10-15",
             "heure": "09:00", "statut": "programme"},
    "R002": {"patient": "P002", "medecin": "Dr Nadia", "date": "2026-10-15",
             "heure": "10:30", "statut": "programme"},
    "R003": {"patient": "P003", "medecin": "Dr Karim", "date": "2026-10-16",
             "heure": "11:00", "statut": "annule"},
}

COLONNES_RDV = ["id", "patient", "medecin", "date", "heure", "statut"]


def sauvegarder_rendez_vous(rendez_vous, nom_fichier):
    """7.3 : csv.DictWriter. newline="" évite les lignes vides sous Windows."""
    with open(nom_fichier, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLONNES_RDV)
        writer.writeheader()
        for id_rdv, info in rendez_vous.items():
            writer.writerow({"id": id_rdv, **info})