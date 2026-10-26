def sauvegarder_binaire(patients, nom_fichier):
    """5.1 : "wb" = write binary"""
    with open(nom_fichier, "wb") as f:
        pickle.dump(patients, f)


def charger_binaire(nom_fichier):
    """5.2 : "rb" = read binary"""
    with open(nom_fichier, "rb") as f:
        return pickle.load(f)