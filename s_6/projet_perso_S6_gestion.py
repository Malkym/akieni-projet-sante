# ============================================================
# PROJET LIBRE 2 : Gestionnaire de Budget Personnel
# Notions : variables, conditions, boucles, fonctions, listes, dict, tuples
# ============================================================

from datetime import datetime

# --- DONNÉES ---
comptes = {
    "principal": {"solde": 500000.0, "devise": "FCFA"},
    "epargne": {"solde": 200000.0, "devise": "FCFA"},
    "investissement": {"solde": 0.0, "devise": "FCFA"},
}

historique = []  # Liste de tuples (date, compte, type, montant, description)

CATEGORIES = {"revenu", "depense", "transfert", "epargne"}


# --- FONCTIONS ---

def afficher_solde(nom_compte):
    """Affiche le solde d'un compte"""
    if nom_compte not in comptes:
        return "ERREUR : Compte inexistant"
    
    compte = comptes[nom_compte]
    return f"{nom_compte.upper()} : {compte['solde']:,.2f} {compte['devise']}"


def deposer(nom_compte, montant, description=""):
    """Dépose de l'argent sur un compte"""
    if nom_compte not in comptes:
        return "ERREUR : Compte inexistant"
    
    if montant <= 0:
        return "ERREUR : Montant invalide"
    
    comptes[nom_compte]["solde"] += montant
    
    # Ajouter à l'historique
    transaction = (datetime.now().strftime("%Y-%m-%d %H:%M"), nom_compte, "revenu", montant, description)
    historique.append(transaction)
    
    return f"SUCCÈS : +{montant:,.2f} FCFA déposés sur {nom_compte}"


def retirer(nom_compte, montant, description=""):
    """Retire de l'argent d'un compte"""
    if nom_compte not in comptes:
        return "ERREUR : Compte inexistant"
    
    if montant <= 0:
        return "ERREUR : Montant invalide"
    
    if comptes[nom_compte]["solde"] < montant:
        return f"ERREUR : Solde insuffisant ({comptes[nom_compte]['solde']:,.2f} FCFA)"
    
    comptes[nom_compte]["solde"] -= montant
    
    transaction = (datetime.now().strftime("%Y-%m-%d %H:%M"), nom_compte, "depense", montant, description)
    historique.append(transaction)
    
    return f"SUCCÈS : -{montant:,.2f} FCFA retirés de {nom_compte}"


def transferer(compte_source, compte_dest, montant):
    """Transfère entre deux comptes"""
    if compte_source == compte_dest:
        return "ERREUR : Comptes identiques"
    
    # Utiliser retirer puis deposer
    resultat_retrait = retirer(compte_source, montant, f"Transfert vers {compte_dest}")
    if "ERREUR" in resultat_retrait:
        return resultat_retrait
    
    deposer(compte_dest, montant, f"Transfert depuis {compte_source}")
    
    return f"SUCCÈS : {montant:,.2f} FCFA transférés de {compte_source} vers {compte_dest}"


def afficher_historique(nombre=10):
    """Affiche les dernières transactions"""
    print("\n" + "=" * 70)
    print("HISTORIQUE DES TRANSACTIONS")
    print("=" * 70)
    print(f"{'Date':<20} {'Compte':<15} {'Type':<12} {'Montant':>12} Description")
    print("-" * 70)
    
    # Dernières transactions (utilisation du slicing)
    for trans in historique[-nombre:]:
        date, compte, type_t, montant, desc = trans
        print(f"{date:<20} {compte:<15} {type_t:<12} {montant:>12,.2f} {desc}")


def bilan_mensuel():
    """Calcule les totaux par catégorie"""
    totaux = {"revenu": 0, "depense": 0, "epargne": 0}
    
    for trans in historique:
        _, _, type_t, montant, _ = trans
        if type_t in totaux:
            totaux[type_t] += montant
    
    print("\n" + "=" * 50)
    print("BILAN MENSUEL")
    print("=" * 50)
    print(f"Revenus totaux  : +{totaux['revenu']:>12,.2f} FCFA")
    print(f"Dépenses totales : -{totaux['depense']:>12,.2f} FCFA")
    print(f"Épargne          : +{totaux['epargne']:>12,.2f} FCFA")
    print(f"Solde net        :  {(totaux['revenu'] - totaux['depense']):>12,.2f} FCFA")


def menu_budget():
    """Menu principal"""
    while True:
        print("\n" + "=" * 50)
        print("GESTIONNAIRE DE BUDGET")
        print("=" * 50)
        print("1. Voir les soldes")
        print("2. Déposer")
        print("3. Retirer")
        print("4. Transférer")
        print("5. Historique")
        print("6. Bilan mensuel")
        print("7. Quitter")
        
        choix = input("\nChoix (1-7) : ").strip()
        
        if choix == "1":
            for compte in comptes:
                print(afficher_solde(compte))
                
        elif choix == "2":
            cpt = input("Compte : ").strip()
            mt = float(input("Montant : "))
            desc = input("Description : ")
            print(deposer(cpt, mt, desc))
            
        elif choix == "3":
            cpt = input("Compte : ").strip()
            mt = float(input("Montant : "))
            desc = input("Description : ")
            print(retirer(cpt, mt, desc))
            
        elif choix == "4":
            src = input("Compte source : ").strip()
            dst = input("Compte destination : ").strip()
            mt = float(input("Montant : "))
            print(transferer(src, dst, mt))
            
        elif choix == "5":
            n = int(input("Nombre de transactions (défaut 10) : ") or 10)
            afficher_historique(n)
            
        elif choix == "6":
            bilan_mensuel()
            
        elif choix == "7":
            print("Au revoir !")
            break


if __name__ == "__main__":
    menu_budget()