# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 2 — Exercice 2 : KPIs Sanitaires OMS
# ============================================================

# --- DONNEES BRUTES ---
budget_fcfa= 87450000
nb_consultations_ext = 4823
nb_hospitalisations = 1247
nb_deces= 18
nb_lits_total = 180
nb_lits_occupes = 143
nb_medecins = 22
nb_infirmiers = 58
population_dept = 128_000
taux_eur_fcfa = 655.957
taux_usd_fcfa = 600.0

# --- A COMPLETER ---
# 1. Conversions devises
budget_eur = round(budget_fcfa / taux_eur_fcfa, 2)
budget_usd = round(budget_fcfa / taux_usd_fcfa, 2)

# 2. Indicateurs OMS
densite_medicale = round((nb_medecins / population_dept) * 1000, 1)
densite_infirmiers = round((nb_infirmiers / population_dept) * 1000, 1)
taux_mortalite = round((nb_deces / population_dept) * 100, 1)
taux_hospitalisation = round((nb_hospitalisations / population_dept) * 100, 2)
taux_mortalite_hospitaliere = round((nb_deces / nb_hospitalisations) * 100, 2)
taux_occupation = round((nb_lits_occupes / nb_lits_total) * 100, 1)

# 3. Division entiere et modulo
budget_medicaments = round(budget_fcfa * 0.35)
cout_journalier_meds = 450_000

jours_stock = budget_medicaments // cout_journalier_meds
nb_consultations_ext_pair_ou_impair = nb_consultations_ext % 2
jours_restants = budget_medicaments % cout_journalier_meds

# 4. Puissance pour projection
budget_n_plus_2 = budget_fcfa * (1.08 ** 2)

# --- AFFICHAGE RAPPORT ---
print(f'=== RAPPORT TRIMESTRIEL Q4 2025 - Hopital General Pointe-Noire ===')
print('BUDGET')
print(f'Depenses Q4: {budget_fcfa:,} FCFA')
print(f'En euros: {budget_eur:,.2f} EUR')
print(f'En dollars: {budget_usd:,.2f} USD')
print('INDICATEURS OMS')
print(f'Densite medicale: {densite_medicale} medecins /1000 hab [Norme OMS : >= 2.3]')
print(f'Densite infirmiere: {densite_infirmiers} infirmiers /1000 hab [Norme OMS : >= 5]')
print(f'Taux de mortalite: {taux_mortalite:.1f}% [Seuil alerte : > 2%]')
print(f'Taux d\'hospitalisation: {taux_hospitalisation:.2f}% [Seuil alerte : > 5%]')
print(f'Taux de mortalite hospitaliere: {taux_mortalite_hospitaliere:.2f}%')
print(f'Taux d\'occupation: {taux_occupation:.1f}% [Optimal : 70-85%]')
print('ANALYSE PHARMACIE')
print(f'Budget medicaments: {budget_medicaments:,} FCFA')
print(f'Jours de stock: {jours_stock} jours')
print(f'Jours depassement stock: {jours_restants} jours')
print(f'Consultations exterieures pairs ou impairs: {nb_consultations_ext_pair_ou_impair}')
print(f'Coût journalier medicaments: {cout_journalier_meds:,} FCFA')
print('ANALYSE CONSULTATIONS')
print(f'Consultations exterieures pairs ou impairs: {nb_consultations_ext_pair_ou_impair}')
print(f'Jours restants: {jours_restants} jours')
print('PROJECTION BUDGETAIRE')
print(f'Budget dans 2 ans: {budget_n_plus_2:,.2f} FCFA')
print(f'ALERTE : Densite medicale CRITIQUE ({densite_medicale} pour 1000 hab — norme OMS : 2.3)')
print('=== FIN DU RAPPORT ===')