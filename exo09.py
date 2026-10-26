def rechercher_par_medecin(nom_fichier, medecin):
    afficher_rendez_vous([r for r in lire_rendez_vous(nom_fichier)
                          if r["medecin"].lower() == medecin.lower()])


def rechercher_par_date(nom_fichier, date):
    """Seuls les rendez-vous programmés (énoncé 9.2)."""
    afficher_rendez_vous([r for r in lire_rendez_vous(nom_fichier)
                          if r["date"] == date and r["statut"] == "programme"])


def rechercher_par_patient(nom_fichier, numero_patient):
    afficher_rendez_vous([r for r in lire_rendez_vous(nom_fichier)
                          if r["patient"] == numero_patient])