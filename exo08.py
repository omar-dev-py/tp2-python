def lire_rendez_vous(nom_fichier):
    """8.1 : retourne la liste des lignes (dictionnaires) via csv.DictReader."""
    with open(nom_fichier, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def afficher_rendez_vous(lignes):
    """8.2"""
    for r in lignes:
        print(f"{r['id']} | {r['patient']} | {r['medecin']} | "
              f"{r['date']} | {r['heure']} | {r['statut']}")


def csv_vers_rendez_vous(nom_fichier):
    """8.3 : reconstruit le dictionnaire imbriqué de l'exercice 7."""
    resultat = {}
    for r in lire_rendez_vous(nom_fichier):
        resultat[r["id"]] = {k: r[k] for k in COLONNES_RDV if k != "id"}
    return resultat
