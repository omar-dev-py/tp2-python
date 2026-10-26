def rechercher_patient(nom_fichier, numero):
    """3.1 : retourne le patient (liste) ou None."""
    for p in lire_patients(nom_fichier):
        if p[0] == numero:
            return p
    return None


def patients_par_ville(nom_fichier, ville):
    """3.2"""
    for p in lire_patients(nom_fichier):
        if p[4].lower() == ville.lower():
            afficher_patient_detaille(p)


def patients_par_age(nom_fichier, age_min, age_max):
    """3.3 : age dans [age_min, age_max]"""
    for p in lire_patients(nom_fichier):
        if age_min <= int(p[3]) <= age_max:
            afficher_patient_detaille(p)


def compter_patients(nom_fichier):
    """3.4"""
    return len(lire_patients(nom_fichier))