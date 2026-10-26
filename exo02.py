def afficher_lignes(nom_fichier):
    """2.1 : affiche les lignes brutes."""
    with open(nom_fichier, "r", encoding="utf-8") as f:
        for ligne in f:
            print(ligne.strip())


def afficher_patient_detaille(champs):
    """2.2 : affichage formaté d'un patient (liste de 5 champs)."""
    print(f"Dossier : {champs[0]}")
    print(f"Nom     : {champs[1]}")
    print(f"Prenom  : {champs[2]}")
    print(f"Age     : {champs[3]}")
    print(f"Ville   : {champs[4]}")
    print("-" * 25)


def lire_patients(nom_fichier):
    """2.3 / 2.4 : retourne une liste de patients (chaque patient = liste de champs)."""
    patients = []
    with open(nom_fichier, "r", encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip()          # enlève \n et espaces
            if ligne:                      # ignore les lignes vides
                patients.append(ligne.split(";"))
    return patients
