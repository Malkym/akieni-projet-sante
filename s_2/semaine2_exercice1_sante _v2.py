# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 2 — Exercice 1 : Fiche Patient CHU Brazzaville
# Votre nom : _______________________________________________
# Date: _______________________________________________
# ============================================================

# --- SECTION 1 : VARIABLES PATIENT ---
# TODO : Declarer toutes les variables patient ci-dessous

nom_patient = 'MAVOUNGOU Celestine'

# Saisie de l'age avec gestion d'erreur
age_input = input("Entrez l'âge du patient : ")
try:
    age_patient = int(age_input)
except ValueError:
    print(f"ERREUR : '{age_input}' n'est pas un nombre valide. L'âge doit être un nombre entier.")
    age_patient = None  # On met None pour indiquer une erreur

sexe_patient = 'F'
departement_patient = 'Brazzaville'
couverture_sociale = 'CNSS'

# --- SECTION 2 : VARIABLES CONSULTATION ---
# TODO : Declarer les variables consultation

type_consultation = 'Urgences'

# Saisie du coût de consultation avec gestion d'erreur
cout_input = input("Entrez le coût de consultation (FCFA) : ")
try:
    cout_consultation_fcfa = float(cout_input)
except ValueError:
    print(f"ERREUR : '{cout_input}' n'est pas un montant valide. Le coût doit être un nombre.")
    cout_consultation_fcfa = None

# Saisie du nombre de consultations avec gestion d'erreur
nb_input = input("Entrez le nombre de consultations : ")
try:
    nb_consultations = int(nb_input)
except ValueError:
    print(f"ERREUR : '{nb_input}' n'est pas un nombre valide. Le nombre de consultations doit être un entier.")
    nb_consultations = None

remise_cnss_pct = 30.0
diagnostic_principal = 'Paludisme grave'

# --- SECTION 3 : VARIABLES HOPITAL ---
# TODO : Declarer les variables hopital

nom_hopital = 'CHU Brazzaville'
ville_hopital = 'Brazzaville'
nb_lits_total = 320
nb_lits_occupes = 284
nb_medecins_actifs = 47

# --- SECTION 4 : CALCULS ---
# TODO : Calculer le cout total apres remise CNSS

# Vérification avant calcul pour éviter les erreurs
if cout_consultation_fcfa is not None and nb_consultations is not None:
    cout_total_fcfa = cout_consultation_fcfa * nb_consultations * (1 - remise_cnss_pct / 100)
else:
    cout_total_fcfa = None
    print("ERREUR : Impossible de calculer le coût total car des valeurs sont invalides.")

# TODO : Calculer le taux d'occupation (en pourcentage, arrondi a 1 decimale)
taux_occupation_pct = round((nb_lits_occupes / nb_lits_total) * 100, 1)

# TODO : Calculer le ratio consultations par medecin (ce jour)
# Hypothese : 120 consultations ont eu lieu ce matin dans tout l'hopital
nb_consultations_hopital = 120
ratio_consultations_medecin = nb_consultations_hopital / nb_medecins_actifs

# --- SECTION 5 : AFFICHAGE ---
# TODO : Afficher une fiche complete avec f-strings

print('='*60)
print(f' FICHE PATIENT — {nom_patient}')
print('='*60)

# ... Afficher les informations patient
print(f'Nom : {nom_patient}')
if age_patient is not None:
    print(f'Age : {age_patient} ans')
else:
    print(f'Age : [ERREUR - valeur invalide saisie]')
print(f'Sexe : {sexe_patient}')
print(f'Departement : {departement_patient}')
print(f'Couverture Sociale : {couverture_sociale}')
print('-'*60)

# ... Afficher les informations consultation
print(f'Type de Consultation : {type_consultation}')
if cout_consultation_fcfa is not None:
    print(f'Coût Consultation : {cout_consultation_fcfa} FCFA')
else:
    print(f'Coût Consultation : [ERREUR - valeur invalide saisie]')
if nb_consultations is not None:
    print(f'Nombre de Consultations : {nb_consultations}')
else:
    print(f'Nombre de Consultations : [ERREUR - valeur invalide saisie]')
print(f'Remise CNSS : {remise_cnss_pct}%')
if cout_total_fcfa is not None:
    print(f'Coût Total après Remise : {cout_total_fcfa} FCFA')
else:
    print(f'Coût Total après Remise : [CALCUL IMPOSSIBLE - données invalides]')
print(f'Diagnostic Principal : {diagnostic_principal}')
print('-'*60)

# ... Afficher les informations hopital
print(f'Hôpital : {nom_hopital}')
print(f'Ville : {ville_hopital}')
print(f'Nombre de Lits Total : {nb_lits_total}')
print(f'Nombre de Lits Occupés : {nb_lits_occupes}')
print(f'Taux d\'Occupation : {taux_occupation_pct}%')
print(f'Nombre de Médecins Actifs : {nb_medecins_actifs}')
print(f'Ratio Consultations par Médecin : {ratio_consultations_medecin:.2f} consultations / médecin ce matin')
print('='*60)
print(f'STATUT : Prise en charge par la {couverture_sociale} validee')
print('='*60)