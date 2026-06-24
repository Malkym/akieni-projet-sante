# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 2 — Exercice 1 : Fiche Patient CHU Brazzaville
# Votre nom : _______________________________________________
# Date: _______________________________________________
# ============================================================
# --- SECTION 1 : VARIABLES PATIENT ---

# TODO : Declarer toutes les variables patient ci-dessous
nom_patient = 'MAVOUNGOU Celestine'
age_patient = 42
sexe_patient = 'F'
departement_patient = 'Brazzaville'
couverture_sociale = 'CNSS'
# --- SECTION 2 : VARIABLES CONSULTATION ---
# TODO : Declarer les variables consultation
type_consultation = 'Urgences'
cout_consultation_fcfa = 15000.0
nb_consultations = 1
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
cout_total_fcfa = cout_consultation_fcfa * nb_consultations * (1 - remise_cnss_pct / 100)
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
print(f'Age : {age_patient} ans')
print(f'Sexe : {sexe_patient}')
print(f'Departement : {departement_patient}')
print(f'Couverture Sociale : {couverture_sociale}')
print('-'*60)
# ... Afficher les informations consultation
print(f'Type de Consultation : {type_consultation}')
print(f'Coût Consultation : {cout_consultation_fcfa} FCFA')
print(f'Nombre de Consultations : {nb_consultations}')
print(f'Remise CNSS : {remise_cnss_pct}%')
print(f'Coût Total après Remise : {cout_total_fcfa} FCFA')
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