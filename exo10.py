def statistiques_csv(nom_fichier):
    lignes = lire_rendez_vous(nom_fichier)
    prevus = sum(1 for r in lignes if r["statut"] == "programme")
    annules = sum(1 for r in lignes if r["statut"] == "annule")
    par_medecin = {}
    for r in lignes:
        par_medecin[r["medecin"]] = par_medecin.get(r["medecin"], 0) + 1

    print(f"Nombre total        : {len(lignes)}")
    print(f"Rendez-vous prevus  : {prevus}")
    print(f"Rendez-vous annules : {annules}")
    print()
    for medecin, n in par_medecin.items():
        print(f"{medecin} : {n}")