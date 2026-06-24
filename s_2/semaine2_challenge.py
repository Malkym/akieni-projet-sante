# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# CHALLENGE ENTREPRISE — Rapport Comparatif 3 Hopitaux du Pool
# Date : 8 janvier 2026
# ============================================================

# ============================================================
# SECTION 1 : DONNEES BRUTES — 3 HOPITAUX
# ============================================================

# --- HOPITAL DISTRICT KINKALA ---
budget_kinkala = 12_500_000
consultations_ext_kinkala = 1_847
hospitalisations_kinkala = 312
deces_kinkala = 8
lits_total_kinkala = 45
lits_occupes_kinkala = 41
medecins_kinkala = 3
population_kinkala = 85_000

# --- CMS DE VINDZA ---
budget_vindza = 6_800_000
consultations_ext_vindza = 923
hospitalisations_vindza = 87
deces_vindza = 2
lits_total_vindza = 20
lits_occupes_vindza = 14
medecins_vindza = 1
population_vindza = 42_000

# --- HOPITAL DE KINDAMBA ---
budget_kindamba = 9_200_000
consultations_ext_kindamba = 1_234
hospitalisations_kindamba = 201
deces_kindamba = 1
lits_total_kindamba = 35
lits_occupes_kindamba = 33
medecins_kindamba = 2
population_kindamba = 67_000

# ============================================================
# SECTION 2 : CALCULS DES KPIs PAR HOPITAL
# ============================================================

# --- KINKALA ---
# Cout moyen par patient = budget / (consultations + hospitalisations)
total_patients_kinkala = consultations_ext_kinkala + hospitalisations_kinkala
cout_moyen_kinkala = round(budget_kinkala / total_patients_kinkala, 2)

# Taux d'occupation des lits
taux_occupation_kinkala = round((lits_occupes_kinkala / lits_total_kinkala) * 100, 2)

# Densite medicale (medecins pour 1000 habitants)
densite_medicale_kinkala = round((medecins_kinkala / population_kinkala) * 1000, 2)

# Taux de mortalite hospitaliere
taux_mortalite_kinkala = round((deces_kinkala / hospitalisations_kinkala) * 100, 2)

# --- VINDZA ---
total_patients_vindza = consultations_ext_vindza + hospitalisations_vindza
cout_moyen_vindza = round(budget_vindza / total_patients_vindza, 2)

taux_occupation_vindza = round((lits_occupes_vindza / lits_total_vindza) * 100, 2)

densite_medicale_vindza = round((medecins_vindza / population_vindza) * 1000, 2)

taux_mortalite_vindza = round((deces_vindza / hospitalisations_vindza) * 100, 2)

# --- KINDAMBA ---
total_patients_kindamba = consultations_ext_kindamba + hospitalisations_kindamba
cout_moyen_kindamba = round(budget_kindamba / total_patients_kindamba, 2)

taux_occupation_kindamba = round((lits_occupes_kindamba / lits_total_kindamba) * 100, 2)

densite_medicale_kindamba = round((medecins_kindamba / population_kindamba) * 1000, 2)

taux_mortalite_kindamba = round((deces_kindamba / hospitalisations_kindamba) * 100, 2)

# ============================================================
# SECTION 3 : IDENTIFICATION HOPITAL CRITIQUE
# ============================================================

# Criteres de criticite : taux mortalite > 2% OU densite medicale < 0.05

hopital_critique = None
raison_critique = ""

# Verification Kinkala
if taux_mortalite_kinkala > 2 or densite_medicale_kinkala < 0.05:
    hopital_critique = "Hopital District Kinkala"
    if taux_mortalite_kinkala > 2 and densite_medicale_kinkala < 0.05:
        raison_critique = f"Taux mortalite ({taux_mortalite_kinkala}%) > 2% ET densite ({densite_medicale_kinkala}) < 0.05"
    elif taux_mortalite_kinkala > 2:
        raison_critique = f"Taux mortalite ({taux_mortalite_kinkala}%) > 2%"
    else:
        raison_critique = f"Densite medicale ({densite_medicale_kinkala}) < 0.05"

# Verification Vindza
if taux_mortalite_vindza > 2 or densite_medicale_vindza < 0.05:
    if hopital_critique is not None:
        hopital_critique += " + CMS de Vindza"
    else:
        hopital_critique = "CMS de Vindza"
    if taux_mortalite_vindza > 2 and densite_medicale_vindza < 0.05:
        raison_critique = f"Taux mortalite ({taux_mortalite_vindza}%) > 2% ET densite ({densite_medicale_vindza}) < 0.05"
    elif taux_mortalite_vindza > 2:
        raison_critique = f"Taux mortalite ({taux_mortalite_vindza}%) > 2%"
    else:
        raison_critique = f"Densite medicale ({densite_medicale_vindza}) < 0.05"

# Verification Kindamba
if taux_mortalite_kindamba > 2 or densite_medicale_kindamba < 0.05:
    if hopital_critique is not None:
        hopital_critique += " + Hopital de Kindamba"
    else:
        hopital_critique = "Hopital de Kindamba"
    if taux_mortalite_kindamba > 2 and densite_medicale_kindamba < 0.05:
        raison_critique = f"Taux mortalite ({taux_mortalite_kindamba}%) > 2% ET densite ({densite_medicale_kindamba}) < 0.05"
    elif taux_mortalite_kindamba > 2:
        raison_critique = f"Taux mortalite ({taux_mortalite_kindamba}%) > 2%"
    else:
        raison_critique = f"Densite medicale ({densite_medicale_kindamba}) < 0.05"

# ============================================================
# SECTION 4 : BONUS — BUDGET POUR 5 MEDECINS PAR HOPITAL
# ============================================================

cout_medecin_trimestre = 1_200_000
medecins_cible = 5

# Medecins a recruter par hopital
medecins_a_recruter_kinkala = medecins_cible - medecins_kinkala
medecins_a_recruter_vindza = medecins_cible - medecins_vindza
medecins_a_recruter_kindamba = medecins_cible - medecins_kindamba

# Cout total pour atteindre 5 medecins dans chaque hopital
cout_total_recrutement = (
    (medecins_a_recruter_kinkala * cout_medecin_trimestre) +
    (medecins_a_recruter_vindza * cout_medecin_trimestre) +
    (medecins_a_recruter_kindamba * cout_medecin_trimestre)
)

budget_total_pool = budget_kinkala + budget_vindza + budget_kindamba
budget_suffisant = budget_total_pool >= cout_total_recrutement

# ============================================================
# SECTION 5 : RAPPORT CONSOLIDE IMPRIMABLE
# ============================================================

print("=" * 70)
print("  RAPPORT COMPARATIF — DEPARTEMENT DU POOL")
print("  Direction de la Sante et du Developpement Social (DSS)")
print("  Date : 8 janvier 2026 | Heure : 09h15")
print("=" * 70)
print()

print("-" * 70)
print("  TABLEAU COMPARATIF DES 3 ETABLISSEMENTS")
print("-" * 70)
print()

# En-tete du tableau
print(f"{'Indicateur':<35} {'Kinkala':>10} {'Vindza':>10} {'Kindamba':>10}")
print("-" * 70)

# Lignes de donnees
print(f"{'Budget trimestriel (FCFA)':<35} {budget_kinkala:>10,} {budget_vindza:>10,} {budget_kindamba:>10,}")
print(f"{'Consultations externes':<35} {consultations_ext_kinkala:>10,} {consultations_ext_vindza:>10,} {consultations_ext_kindamba:>10,}")
print(f"{'Hospitalisations':<35} {hospitalisations_kinkala:>10,} {hospitalisations_vindza:>10,} {hospitalisations_kindamba:>10,}")
print(f"{'Deces hospitaliers':<35} {deces_kinkala:>10} {deces_vindza:>10} {deces_kindamba:>10}")
print(f"{'Lits totaux':<35} {lits_total_kinkala:>10} {lits_total_vindza:>10} {lits_total_kindamba:>10}")
print(f"{'Lits occupes':<35} {lits_occupes_kinkala:>10} {lits_occupes_vindza:>10} {lits_occupes_kindamba:>10}")
print(f"{'Medecins permanents':<35} {medecins_kinkala:>10} {medecins_vindza:>10} {medecins_kindamba:>10}")
print(f"{'Population desservie':<35} {population_kinkala:>10,} {population_vindza:>10,} {population_kindamba:>10,}")
print("-" * 70)

print()
print("-" * 70)
print("  INDICATEURS DE PERFORMANCE (KPIs)")
print("-" * 70)
print()

print(f"{'Cout moyen par patient (FCFA)':<35} {cout_moyen_kinkala:>10,.2f} {cout_moyen_vindza:>10,.2f} {cout_moyen_kindamba:>10,.2f}")
print(f"{'Taux d\'occupation des lits (%)':<35} {taux_occupation_kinkala:>10.2f} {taux_occupation_vindza:>10.2f} {taux_occupation_kindamba:>10.2f}")
print(f"{'Densite medicale (/1000 hab)':<35} {densite_medicale_kinkala:>10.2f} {densite_medicale_vindza:>10.2f} {densite_medicale_kindamba:>10.2f}")
print(f"{'Taux de mortalite hospitaliere (%)':<35} {taux_mortalite_kinkala:>10.2f} {taux_mortalite_vindza:>10.2f} {taux_mortalite_kindamba:>10.2f}")
print("-" * 70)

print()
print("=" * 70)
print("  ALERTE DE SITUATION CRITIQUE")
print("=" * 70)

if hopital_critique is not None:
    print(f"    HOPITAL(S) EN SITUATION CRITIQUE : {hopital_critique}")
    print(f"  Raison : {raison_critique}")
    print("  Action recommandee : Intervention urgente du Ministere")
else:
    print("   Aucun hopital en situation critique")

print("=" * 70)

print()
print("-" * 70)
print("  ANALYSE BUDGETAIRE BONUS — RECRUTEMENT MEDECINS")
print("-" * 70)
print(f"  Objectif : 5 medecins par etablissement")
print(f"  Cout par medecin : {cout_medecin_trimestre:,} FCFA/trimestre")
print()
print(f"  Medecins a recruter :")
print(f"    - Kinkala  : {medecins_a_recruter_kinkala} medecin(s)")
print(f"    - Vindza   : {medecins_a_recruter_vindza} medecin(s)")
print(f"    - Kindamba : {medecins_a_recruter_kindamba} medecin(s)")
print(f"  TOTAL A RECRUTER : {medecins_a_recruter_kinkala + medecins_a_recruter_vindza + medecins_a_recruter_kindamba} medecins")
print()
print(f"  Cout total du recrutement : {cout_total_recrutement:,} FCFA")
print(f"  Budget total disponible   : {budget_total_pool:,} FCFA")
print()

if budget_suffisant:
    print(f"   BUDGET SUFFISANT : Excedent de {budget_total_pool - cout_total_recrutement:,} FCFA")
else:
    print(f"   BUDGET INSUFFISANT : Manque de {cout_total_recrutement - budget_total_pool:,} FCFA")

print("-" * 70)
print()
print("=" * 70)
print("  FIN DU RAPPORT")
print("  Prepare par : Equipe Data Akieni Academy")
print("  Pour : Dr. ELENGA Pascal, Directeur DSS")
print("=" * 70)