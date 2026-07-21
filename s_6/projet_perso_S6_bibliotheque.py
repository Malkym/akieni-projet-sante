# ============================================================
# PROJET LIBRE 1 : Gestionnaire de Bibliothèque
# Notions : variables, conditions, boucles, fonctions, listes, dict, sets
# ============================================================

# --- DONNÉES ---
catalogue = [
    {"titre": "Les Misérables", "auteur": "Victor Hugo", "genre": "Roman", "disponible": True},
    {"titre": "1984", "auteur": "George Orwell", "genre": "Science-fiction", "disponible": False},
    {"titre": "L'Étranger", "auteur": "Albert Camus", "genre": "Roman", "disponible": True},
    {"titre": "Fondation", "auteur": "Isaac Asimov", "genre": "Science-fiction", "disponible": True},
    {"titre": "Pétrole de Congo", "auteur": "Emmanuel Dongala", "genre": "Roman africain", "disponible": True},
]

membres = {
    "M001": {"nom": "Jean Dupont", "emprunts": ["1984"], "retard": 0},
    "M002": {"nom": "Marie Nkoua", "emprunts": [], "retard": 2},
    "M003": {"nom": "Paul Moussa", "emprunts": [], "retard": 0},
}

# --- FONCTIONS ---

def afficher_catalogue():
    """Affiche tous les livres avec leur statut"""
    print("\n" + "=" * 50)
    print("CATALOGUE DE LA BIBLIOTHÈQUE")
    print("=" * 50)
    for i, livre in enumerate(catalogue, 1):
        statut = "DISPONIBLE" if livre["disponible"] else "EMPRUNTÉ"
        print(f"{i}. {livre['titre']:<25} | {livre['auteur']:<20} | {statut}")


def rechercher_livre(mot_cle):
    """Recherche un livre par titre ou auteur"""
    resultats = []
    for livre in catalogue:
        if mot_cle.lower() in livre["titre"].lower() or mot_cle.lower() in livre["auteur"].lower():
            resultats.append(livre)
    return resultats


def emprunter_livre(id_membre, titre_livre):
    """Gère l'emprunt d'un livre"""
    # Vérifier membre
    if id_membre not in membres:
        return "ERREUR : Membre non trouvé"
    
    membre = membres[id_membre]
    
    # Vérifier retard
    if membre["retard"] > 0:
        return f"ERREUR : {membre['nom']} a {membre['retard']} emprunt(s) en retard"
    
    # Vérifier limite (max 3 emprunts)
    if len(membre["emprunts"]) >= 3:
        return "ERREUR : Limite de 3 emprunts atteinte"
    
    # Chercher le livre
    for livre in catalogue:
        if livre["titre"] == titre_livre:
            if not livre["disponible"]:
                return f"ERREUR : '{titre_livre}' est déjà emprunté"
            
            # Emprunt réussi
            livre["disponible"] = False
            membre["emprunts"].append(titre_livre)
            return f"SUCCÈS : '{titre_livre}' emprunté par {membre['nom']}"
    
    return f"ERREUR : Livre '{titre_livre}' non trouvé"


def rendre_livre(id_membre, titre_livre):
    """Gère le retour d'un livre"""
    if id_membre not in membres:
        return "ERREUR : Membre non trouvé"
    
    membre = membres[id_membre]
    
    if titre_livre not in membre["emprunts"]:
        return f"ERREUR : {membre['nom']} n'a pas emprunté '{titre_livre}'"
    
    # Retour réussi
    membre["emprunts"].remove(titre_livre)
    
    for livre in catalogue:
        if livre["titre"] == titre_livre:
            livre["disponible"] = True
            break
    
    return f"SUCCÈS : '{titre_livre}' rendu par {membre['nom']}"


def statistiques():
    """Affiche les statistiques de la bibliothèque"""
    total = len(catalogue)
    dispo = sum(1 for l in catalogue if l["disponible"])
    empruntes = total - dispo
    
    # Genres uniques avec set
    genres = set(l["genre"] for l in catalogue)
    
    print("\n" + "=" * 50)
    print("STATISTIQUES")
    print("=" * 50)
    print(f"Total livres : {total}")
    print(f"Disponibles : {dispo}")
    print(f"Empruntés : {empruntes}")
    print(f"Genres : {', '.join(genres)}")
    print(f"Membres inscrits : {len(membres)}")


# --- MENU PRINCIPAL ---

def menu():
    """Boucle principale du programme"""
    while True:
        print("\n" + "=" * 50)
        print("MENU BIBLIOTHÈQUE")
        print("=" * 50)
        print("1. Voir le catalogue")
        print("2. Rechercher un livre")
        print("3. Emprunter un livre")
        print("4. Rendre un livre")
        print("5. Statistiques")
        print("6. Quitter")
        
        choix = input("\nVotre choix (1-6) : ").strip()
        
        if choix == "1":
            afficher_catalogue()
            
        elif choix == "2":
            mot = input("Mot-clé (titre ou auteur) : ")
            resultats = rechercher_livre(mot)
            if resultats:
                print(f"\n{len(resultats)} résultat(s) trouvé(s) :")
                for livre in resultats:
                    print(f"  - {livre['titre']} ({livre['auteur']})")
            else:
                print("Aucun résultat")
                
        elif choix == "3":
            id_m = input("ID membre (ex: M001) : ").strip()
            titre = input("Titre du livre : ").strip()
            print(emprunter_livre(id_m, titre))
            
        elif choix == "4":
            id_m = input("ID membre : ").strip()
            titre = input("Titre du livre : ").strip()
            print(rendre_livre(id_m, titre))
            
        elif choix == "5":
            statistiques()
            
        elif choix == "6":
            print("Au revoir !")
            break
            
        else:
            print("Choix invalide")


# Lancer le programme
if __name__ == "__main__":
    menu()