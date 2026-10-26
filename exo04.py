def texte_vers_dictionnaire(nom_fichier):
    """4.1 / 11.1 : {"P001": {"nom":..., "prenom":..., "age": int, "ville":...}}"""
    patients = {}
    with open(nom_fichier, "r", encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne:
                continue
            numero, nom, prenom, age, ville = ligne.split(";")
            patients[numero] = {
                "nom": nom,
                "prenom": prenom,
                "age": int(age),           # 4.2 : âge stocké comme entier
                "ville": ville,
            }
    return patients


def afficher_patients(patients):
    """4.3"""
    for numero, info in patients.items():
        print(f"Dossier : {numero}")
        print(f"Nom     : {info['nom']}")
        print(f"Prenom  : {info['prenom']}")
        print(f"Age     : {info['age']}")
        print(f"Ville   : {info['ville']}")
        print("-" * 25)


def ajouter_patient(patients, numero, nom, prenom, age, ville):
    """4.4"""
    patients[numero] = {"nom": nom, "prenom": prenom, "age": int(age), "ville": ville}