def modifier_ville(nom_fichier, numero, nouvelle_ville):
    patients = charger_binaire(nom_fichier)          # 1. charger
    if numero not in patients:                       # 2. rechercher
        print(f"Patient {numero} introuvable.")
        return False
    patients[numero]["ville"] = nouvelle_ville       # 3. modifier
    sauvegarder_binaire(patients, nom_fichier)       # 4. sauvegarder
    return True