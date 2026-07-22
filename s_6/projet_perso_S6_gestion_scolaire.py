# ============================================================
# PROJET LIBRE 3 : Gestionnaire Scolaire — Akieni Academy
# Notions : variables, conditions, boucles, fonctions,
#           listes, dict, sets, tuples, datetime, f-strings, slicing
# ============================================================

from datetime import datetime

# --- CONSTANTES MÉTIER ---
NOTE_MIN = 0.0
NOTE_MAX = 20.0
SEUIL_ADMISSION = 10.0          # Moyenne minimale pour être admis
SEUIL_MENTION_BIEN = 14.0
SEUIL_MENTION_TB = 16.0
MATIERES = {"Mathématiques", "Français", "Physique", "SVT", "Histoire-Géo", "Anglais"}

# --- DONNÉES ---
# Classes de l'établissement (liste de dictionnaires)
classes = [
    {"code": "6A", "niveau": "6ème", "salle": "S01"},
    {"code": "3B", "niveau": "3ème", "salle": "S12"},
    {"code": "TleD", "niveau": "Terminale D", "salle": "S20"},
]

# Élèves : id -> infos. Les notes sont une liste de tuples (matière, note)
eleves = {
    "E001": {"nom": "Jean Dupont", "classe": "6A", "notes": [("Mathématiques", 12.0), ("Français", 14.5)], "absences": 0},
    "E002": {"nom": "Marie Nkoua", "classe": "3B", "notes": [("Physique", 8.0), ("SVT", 11.0)], "absences": 3},
    "E003": {"nom": "Paul Moussa", "classe": "TleD", "notes": [("Mathématiques", 16.0), ("Physique", 15.5)], "absences": 1},
}

# Enseignants : id -> infos. Chaque prof enseigne une matière à des classes
enseignants = {
    "P001": {"nom": "M. Bakala", "matiere": "Mathématiques", "classes": ["6A", "TleD"]},
    "P002": {"nom": "Mme Ondongo", "matiere": "Français", "classes": ["6A", "3B"]},
    "P003": {"nom": "M. Samba", "matiere": "Physique", "classes": ["3B", "TleD"]},
}

# Emploi du temps : liste de tuples (jour, heure, classe, matière)
emploi_du_temps = [
    ("Lundi", "08:00", "6A", "Mathématiques"),
    ("Lundi", "10:00", "3B", "Français"),
    ("Mardi", "08:00", "TleD", "Physique"),
    ("Mardi", "10:00", "6A", "Français"),
    ("Mercredi", "08:00", "TleD", "Mathématiques"),
]

# Journal des présences : liste de tuples (date, id_élève, statut)
journal_presences = []


# ============================================================
# MISE EN FORME DE L'AFFICHAGE (helpers réutilisés partout)
# ============================================================
LARGEUR = 55            # Largeur commune de tous les encadrés et tableaux
LARGEUR_LABEL = 22      # Largeur des libellés dans les lignes "clé : valeur"
COL_ID = 8              # Colonne identifiant
COL_NOM = 22            # Colonne nom (identique dans tous les tableaux)


def titre(texte):
    """Affiche un titre encadré, identique dans tout le programme"""
    print("\n" + "=" * LARGEUR)
    print(texte)
    print("=" * LARGEUR)


def ligne(caractere="-"):
    """Trace une ligne de séparation de la largeur commune"""
    print(caractere * LARGEUR)


def info(label, valeur):
    """Affiche une ligne 'libellé : valeur' avec les deux-points alignés"""
    print(f"{label:<{LARGEUR_LABEL}}: {valeur}")


# ============================================================
# FONCTIONS — ÉLÈVES & CLASSES
# ============================================================

def classe_existe(code_classe):
    """Vérifie qu'une classe existe dans l'établissement"""
    for cl in classes:
        if cl["code"] == code_classe:
            return True
    return False


def inscrire_eleve(id_eleve, nom, code_classe):
    """Inscrit un nouvel élève dans une classe"""
    if id_eleve in eleves:
        return f"ERREUR : L'identifiant {id_eleve} existe déjà"

    if not classe_existe(code_classe):
        return f"ERREUR : La classe '{code_classe}' n'existe pas"

    eleves[id_eleve] = {"nom": nom, "classe": code_classe, "notes": [], "absences": 0}
    return f"SUCCÈS : {nom} inscrit(e) en {code_classe} (id {id_eleve})"


def afficher_classe(code_classe):
    """Affiche la liste des élèves d'une classe"""
    if not classe_existe(code_classe):
        print(f"ERREUR : La classe '{code_classe}' n'existe pas")
        return

    titre(f"CLASSE {code_classe}")
    print(f"{'ID':<{COL_ID}} {'Nom':<{COL_NOM}} {'Moyenne':>10}")
    ligne()

    trouve = False
    for id_e, eleve in eleves.items():
        if eleve["classe"] == code_classe:
            trouve = True
            moyenne = calculer_moyenne(id_e)
            moy_txt = f"{moyenne:.2f}" if moyenne is not None else "—"
            print(f"{id_e:<{COL_ID}} {eleve['nom']:<{COL_NOM}} {moy_txt:>10}")

    if not trouve:
        print("(aucun élève dans cette classe)")


# ============================================================
# FONCTIONS — NOTES & BULLETINS
# ============================================================

def ajouter_note(id_eleve, matiere, note):
    """Ajoute une note à un élève après validation"""
    if id_eleve not in eleves:
        return "ERREUR : Élève non trouvé"

    if matiere not in MATIERES:
        return f"ERREUR : Matière inconnue ('{matiere}')"

    if note < NOTE_MIN or note > NOTE_MAX:
        return f"ERREUR : Note invalide (doit être entre {NOTE_MIN} et {NOTE_MAX})"

    eleves[id_eleve]["notes"].append((matiere, note))
    return f"SUCCÈS : {note:.2f}/20 en {matiere} ajoutée à {eleves[id_eleve]['nom']}"


def calculer_moyenne(id_eleve):
    """Calcule la moyenne générale d'un élève (None si aucune note)"""
    if id_eleve not in eleves:
        return None

    notes = eleves[id_eleve]["notes"]
    if not notes:
        return None

    total = sum(note for _, note in notes)
    return total / len(notes)


def mention(moyenne):
    """Retourne la mention correspondant à une moyenne"""
    if moyenne is None:
        return "Non évalué"
    if moyenne < SEUIL_ADMISSION:
        return "Ajourné"
    if moyenne >= SEUIL_MENTION_TB:
        return "Très Bien"
    if moyenne >= SEUIL_MENTION_BIEN:
        return "Bien"
    return "Passable"


def bulletin(id_eleve):
    """Affiche le bulletin détaillé d'un élève"""
    if id_eleve not in eleves:
        print("ERREUR : Élève non trouvé")
        return

    eleve = eleves[id_eleve]
    titre("BULLETIN SCOLAIRE — AKIENI ACADEMY")
    info("Élève", f"{eleve['nom']} ({id_eleve})")
    info("Classe", eleve["classe"])
    info("Date", datetime.now().strftime("%Y-%m-%d"))
    ligne()
    print(f"{'Matière':<{COL_NOM}} {'Note':>10}")
    ligne()

    if not eleve["notes"]:
        print("(aucune note enregistrée)")
    else:
        for matiere, note in eleve["notes"]:
            print(f"{matiere:<{COL_NOM}} {note:>7.2f}/20")

    moyenne = calculer_moyenne(id_eleve)
    ligne()
    if moyenne is not None:
        print(f"{'MOYENNE GÉNÉRALE':<{COL_NOM}} {moyenne:>7.2f}/20")
    info("Mention", mention(moyenne))
    info("Absences", eleve["absences"])


# ============================================================
# FONCTIONS — PRÉSENCES
# ============================================================

def marquer_presence(id_eleve, present):
    """Enregistre la présence (True) ou l'absence (False) d'un élève"""
    if id_eleve not in eleves:
        return "ERREUR : Élève non trouvé"

    statut = "présent" if present else "absent"
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    journal_presences.append((date, id_eleve, statut))

    if not present:
        eleves[id_eleve]["absences"] += 1

    return f"SUCCÈS : {eleves[id_eleve]['nom']} marqué(e) {statut}"


def faire_appel(code_classe):
    """Fait l'appel de toute une classe (présent par défaut, absents saisis)"""
    if not classe_existe(code_classe):
        print(f"ERREUR : La classe '{code_classe}' n'existe pas")
        return

    print(f"\nAppel de la classe {code_classe}")
    print("(Entrée = présent, 'a' = absent)")
    for id_e, eleve in eleves.items():
        if eleve["classe"] == code_classe:
            reponse = input(f"  {eleve['nom']:<25} : ").strip().lower()
            present = reponse != "a"
            print("   -> " + marquer_presence(id_e, present))


def afficher_journal(nombre=10):
    """Affiche les derniers enregistrements de présence (slicing)"""
    titre("JOURNAL DES PRÉSENCES")
    if not journal_presences:
        print("(aucun enregistrement)")
        return

    print(f"{'Date':<18} {'Élève':<{COL_NOM}} {'Statut':<10}")
    ligne()
    for date, id_e, statut in journal_presences[-nombre:]:
        nom = eleves.get(id_e, {}).get("nom", id_e)
        print(f"{date:<18} {nom:<{COL_NOM}} {statut:<10}")


# ============================================================
# FONCTIONS — ENSEIGNANTS & EMPLOI DU TEMPS
# ============================================================

def afficher_enseignants():
    """Affiche tous les enseignants et leurs classes"""
    titre("CORPS ENSEIGNANT")
    print(f"{'ID':<{COL_ID}} {'Nom':<15} {'Matière':<15} {'Classes'}")
    ligne()
    for id_p, prof in enseignants.items():
        classes_txt = ", ".join(prof["classes"])
        print(f"{id_p:<{COL_ID}} {prof['nom']:<15} {prof['matiere']:<15} {classes_txt}")


def emploi_du_temps_classe(code_classe):
    """Affiche l'emploi du temps d'une classe"""
    if not classe_existe(code_classe):
        print(f"ERREUR : La classe '{code_classe}' n'existe pas")
        return

    titre(f"EMPLOI DU TEMPS — {code_classe}")
    print(f"{'Jour':<12} {'Heure':<8} {'Matière':<20}")
    ligne()

    trouve = False
    for jour, heure, classe, matiere in emploi_du_temps:
        if classe == code_classe:
            trouve = True
            print(f"{jour:<12} {heure:<8} {matiere:<20}")

    if not trouve:
        print("(aucun cours programmé)")


# ============================================================
# FONCTIONS — STATISTIQUES
# ============================================================

def statistiques():
    """Affiche les statistiques globales de l'établissement"""
    total_eleves = len(eleves)
    niveaux = set(cl["niveau"] for cl in classes)

    # Moyenne de l'établissement (sur les élèves ayant au moins une note)
    moyennes = [calculer_moyenne(id_e) for id_e in eleves]
    moyennes = [m for m in moyennes if m is not None]
    moy_etab = sum(moyennes) / len(moyennes) if moyennes else 0.0

    total_absences = sum(eleve["absences"] for eleve in eleves.values())

    titre("STATISTIQUES DE L'ÉTABLISSEMENT")
    info("Élèves inscrits", total_eleves)
    info("Classes", len(classes))
    info("Niveaux", ", ".join(niveaux))
    info("Enseignants", len(enseignants))
    info("Moyenne établissement", f"{moy_etab:.2f}/20")
    info("Total absences", total_absences)


# ============================================================
# FONCTIONS — CLASSEMENT (sorted)
# ============================================================

def classement(code_classe=None):
    """Affiche le classement des élèves par moyenne décroissante.
    Si code_classe est fourni, ne classe que cette classe ;
    sinon, classe tout l'établissement."""

    # 1) Constituer la liste des élèves à classer (id, nom, moyenne)
    palmares = []
    for id_e, eleve in eleves.items():
        if code_classe is not None and eleve["classe"] != code_classe:
            continue
        moyenne = calculer_moyenne(id_e)
        if moyenne is None:      # on écarte les élèves sans note
            continue
        palmares.append((id_e, eleve["nom"], eleve["classe"], moyenne))

    if not palmares:
        print("\n(aucun élève noté pour ce classement)")
        return

    # 2) Trier sur DEUX critères grâce à sorted() + key renvoyant un tuple :
    #    - moyenne décroissante  -> on met -moyenne (le - inverse l'ordre)
    #    - puis nom alphabétique  -> t[1] départage les égalités (A avant Z)
    #    Rappel du tuple : (id[0], nom[1], classe[2], moyenne[3])
    palmares_trie = sorted(palmares, key=lambda t: (-t[3], t[1]))

    entete = f"CLASSEMENT — {code_classe}" if code_classe else "CLASSEMENT GÉNÉRAL"
    titre(entete)
    print(f"{'Rang':<6} {'Nom':<{COL_NOM}} {'Classe':<8} {'Moyenne':>9}")
    ligne()

    # 3) enumerate pour numéroter le rang (1er, 2e, ...)
    for rang, (id_e, nom, classe, moyenne) in enumerate(palmares_trie, 1):
        medaille = ""
        if rang == 1:
            medaille = " *"      # tête de classement
        print(f"{rang:<6} {nom:<{COL_NOM}} {classe:<8} {moyenne:>7.2f}{medaille}")


# ============================================================
# MENU PRINCIPAL
# ============================================================

def menu():
    """Boucle principale du programme"""
    while True:
        titre("GESTIONNAIRE SCOLAIRE — AKIENI ACADEMY")
        print("1. Inscrire un élève")
        print("2. Voir une classe")
        print("3. Ajouter une note")
        print("4. Afficher un bulletin")
        print("5. Faire l'appel d'une classe")
        print("6. Journal des présences")
        print("7. Enseignants")
        print("8. Emploi du temps d'une classe")
        print("9. Statistiques")
        print("10. Classement (par moyenne)")
        print("0. Quitter")

        choix = input("\nVotre choix (0-10) : ").strip()

        if choix == "1":
            id_e = input("ID élève (ex: E004) : ").strip()
            nom = input("Nom complet : ").strip()
            cl = input("Classe (ex: 6A) : ").strip()
            print(inscrire_eleve(id_e, nom, cl))

        elif choix == "2":
            cl = input("Code classe : ").strip()
            afficher_classe(cl)

        elif choix == "3":
            id_e = input("ID élève : ").strip()
            matiere = input("Matière : ").strip()
            note = float(input("Note (/20) : "))
            print(ajouter_note(id_e, matiere, note))

        elif choix == "4":
            id_e = input("ID élève : ").strip()
            bulletin(id_e)

        elif choix == "5":
            cl = input("Code classe : ").strip()
            faire_appel(cl)

        elif choix == "6":
            n = int(input("Nombre d'enregistrements (défaut 10) : ") or 10)
            afficher_journal(n)

        elif choix == "7":
            afficher_enseignants()

        elif choix == "8":
            cl = input("Code classe : ").strip()
            emploi_du_temps_classe(cl)

        elif choix == "9":
            statistiques()

        elif choix == "10":
            cl = input("Code classe (Entrée = tout l'établissement) : ").strip()
            classement(cl if cl else None)

        elif choix == "0":
            print("Au revoir !")
            break

        else:
            print("Choix invalide")


# Lancer le programme
if __name__ == "__main__":
    menu()
