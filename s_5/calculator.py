# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 5 — Calculatrice Sante avec Fonctions
# ============================================================

def afficher_menu():
    """Affiche le menu principal de la calculatrice"""
    print("\n" + "=" * 50)
    print("  CALCULATRICE SANTE — CHU BRAZZAVILLE")
    print("=" * 50)
    print("  1. Addition (+)")
    print("  2. Soustraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Calcul IMC (Indice Masse Corporelle)")
    print("  6. Calcul dose medicament (mg/kg)")
    print("  7. Conversion FCFA → EUR/USD")
    print("  8. Calcul taux occupation lits (%)")
    print("  9. Quitter")
    print("=" * 50)


def addition(a, b):
    """Additionne deux nombres"""
    return a + b


def soustraction(a, b):
    """Soustrait b de a"""
    return a - b


def multiplication(a, b):
    """Multiplie deux nombres"""
    return a * b


def division(a, b):
    """Divise a par b avec gestion erreur"""
    if b == 0:
        return "ERREUR : Division par zero impossible"
    return a / b


def calcul_imc(poids, taille):
    """
    Calcule l'IMC et donne l'interpretation medicale
    poids en kg, taille en metres
    """
    if taille <= 0:
        return "ERREUR : Taille invalide"
    
    imc = poids / (taille ** 2)
    imc = round(imc, 1)
    
    if imc < 18.5:
        statut = "Maigreur"
    elif imc < 25:
        statut = "Poids normal"
    elif imc < 30:
        statut = "Surpoids"
    else:
        statut = "Obesite"
    
    return f"IMC = {imc} | Statut : {statut}"


def calcul_dose(poids, dose_par_kg):
    """
    Calcule la dose de medicament selon le poids
    poids en kg, dose_par_kg en mg/kg
    """
    if poids <= 0 or dose_par_kg <= 0:
        return "ERREUR : Valeurs invalides"
    
    dose_totale = poids * dose_par_kg
    return f"Dose totale : {dose_totale} mg ({dose_par_kg} mg/kg x {poids} kg)"


def conversion_devise(montant_fcfa, taux):
    """Convertit FCFA en devise etrangere"""
    if montant_fcfa < 0:
        return "ERREUR : Montant negatif"
    
    resultat = montant_fcfa / taux
    return round(resultat, 2)


def taux_occupation(lits_occupes, lits_total):
    """Calcule le taux d'occupation des lits"""
    if lits_total == 0:
        return "ERREUR : Nombre de lits invalide"
    
    taux = (lits_occupes / lits_total) * 100
    taux = round(taux, 1)
    
    if taux > 95:
        alerte = "SATURATION"
    elif taux > 85:
        alerte = "ELEVEE"
    elif taux > 70:
        alerte = "OPTIMALE"
    else:
        alerte = "SOUS-UTILISEE"
    
    return f"Taux : {taux}% | Niveau : {alerte}"


def saisir_nombre(message):
    """Saisie securisee d'un nombre"""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("ERREUR : Veuillez entrer un nombre valide")


def saisir_entier(message):
    """Saisie securisee d'un entier"""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("ERREUR : Veuillez entrer un nombre entier")


# ============================================================
# PROGRAMME PRINCIPAL
# ============================================================

def main():
    """Boucle principale de la calculatrice"""
    
    while True:
        afficher_menu()
        
        choix = input("Votre choix (1-9) : ").strip()
        
        # --- Operations de base ---
        if choix in ['1', '2', '3', '4']:
            print("\n--- Operation de base ---")
            a = saisir_nombre("Premier nombre : ")
            b = saisir_nombre("Deuxieme nombre : ")
            
            if choix == '1':
                print(f"\nResultat : {a} + {b} = {addition(a, b)}")
            elif choix == '2':
                print(f"\nResultat : {a} - {b} = {soustraction(a, b)}")
            elif choix == '3':
                print(f"\nResultat : {a} x {b} = {multiplication(a, b)}")
            elif choix == '4':
                resultat = division(a, b)
                print(f"\nResultat : {a} / {b} = {resultat}")
        
        # --- IMC ---
        elif choix == '5':
            print("\n--- Calcul IMC ---")
            poids = saisir_nombre("Poids (kg) : ")
            taille = saisir_nombre("Taille (m, ex: 1.75) : ")
            print(f"\n{calcul_imc(poids, taille)}")
        
        # --- Dose medicament ---
        elif choix == '6':
            print("\n--- Calcul dose medicament ---")
            poids = saisir_nombre("Poids du patient (kg) : ")
            dose = saisir_nombre("Dose prescrite (mg/kg) : ")
            print(f"\n{calcul_dose(poids, dose)}")
        
        # --- Conversion devises ---
        elif choix == '7':
            print("\n--- Conversion FCFA ---")
            montant = saisir_nombre("Montant en FCFA : ")
            print("\n  1. EUR (taux : 655.957)")
            print("  2. USD (taux : 600.0)")
            choix_devise = input("Devise (1-2) : ").strip()
            
            if choix_devise == '1':
                resultat = conversion_devise(montant, 655.957)
                print(f"\n{montant:,.2f} FCFA = {resultat:,.2f} EUR")
            elif choix_devise == '2':
                resultat = conversion_devise(montant, 600.0)
                print(f"\n{montant:,.2f} FCFA = {resultat:,.2f} USD")
            else:
                print("Choix invalide")
        
        # --- Taux occupation ---
        elif choix == '8':
            print("\n--- Taux d'occupation des lits ---")
            occupes = saisir_entier("Lits occupes : ")
            total = saisir_entier("Lits total : ")
            print(f"\n{taux_occupation(occupes, total)}")
        
        # --- Quitter ---
        elif choix == '9':
            print("\nMerci d'avoir utilise la Calculatrice Sante !")
            print("A bientot au CHU Brazzaville.")
            break
        
        # --- Choix invalide ---
        else:
            print("\nERREUR : Choix invalide. Veuillez entrer 1-9.")


# Lancer le programme
if __name__ == '__main__':
    main()