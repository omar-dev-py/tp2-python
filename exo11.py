COLONNES_PATIENTS = ["numero", "nom", "prenom", "age", "ville"]


def dictionnaire_vers_csv(patients, nom_fichier="patients.csv"):
    """11.2"""
    with open(nom_fichier, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLONNES_PATIENTS)
        writer.writeheader()
        for numero, info in patients.items():
            writer.writerow({"numero": numero, **info})


def csv_vers_dictionnaire(nom_fichier):
    """11.3 : l'âge lu du CSV est une chaîne -> conversion en int."""
    patients = {}
    with open(nom_fichier, "r", newline="", encoding="utf-8") as f:
        for ligne in csv.DictReader(f):
            patients[ligne["numero"]] = {
                "nom": ligne["nom"],
                "prenom": ligne["prenom"],
                "age": int(ligne["age"]),
                "ville": ligne["ville"],
            }
    return patients