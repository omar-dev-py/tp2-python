import csv
import pickle

# =====================================================================
# EXERCICE 1 : création et écriture dans un fichier texte
# =====================================================================
def creer_patients_txt(nom_fichier="patients.txt"):
    """1.1 / 1.2 : crée le fichier ("w" écrase le contenu existant)."""
    lignes = [
        "P001;Alaoui;Youssef;35;Marrakech",
        "P002;Bennani;Salma;28;Safi",
        "P003;Idrissi;Amine;52;Marrakech",
        "P004;El Mansouri;Meryem;41;Agadir",
    ]
    with open(nom_fichier, "w", encoding="utf-8") as f:
        for ligne in lignes:
            f.write(ligne + "\n")


def ajouter_ligne(nom_fichier, ligne):
    """1.3 : mode "a" (append) = ajout à la fin sans rien supprimer."""
    with open(nom_fichier, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")
