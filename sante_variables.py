# ============================================================
# MODULE FONDATEUR — Projet Sante Publique / Akieni Academy
# Ce fichier centralise toutes les constantes et variables metier
# Il sera enrichi chaque semaine jusqu'a S24
# ============================================================

# ============================================================
# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ========
# ============================================================

TAUX_EUR_FCFA = 655.957
TAUX_USD_FCFA = 600.0
SEUIL_OMS_DENSITE_MEDICALE = 2.3              # medecins pour 1000 habitants
SEUIL_OMS_COUVERTURE_VACCIN = 95.0            # pourcentage minimum OMS
SEUIL_MORTALITE_ALERTE = 2.0                  # % deces / hospitalisations
SEUIL_RUPTURE_STOCK_JOURS = 30                # jours minimum de stock

DEPARTEMENTS_CONGO = [
    # 12 departements officiels du Congo
    'Brazzaville',
    'Pointe-Noire',
    'Bouenza',
    'Cuvette',
    'Cuvette-Ouest',
    'Kouilou',
    'Lekoumou',
    'Likouala',
    'Niari',
    'Plateaux',
    'Pool',
    'Sangha'
]

# ============================================================
# === SECTION B : VARIABLES DES 5 HOPITAUX ===================
# ============================================================

# --- Hopital 1 : CHU de Brazzaville ---
h1_nom = 'CHU de Brazzaville'
h1_ville = 'Brazzaville'
h1_departement = 'Brazzaville'
h1_type = 'CHU'
h1_nb_lits = 320
h1_nb_lits_occupes = 284
h1_nb_medecins = 47
h1_nb_infirmiers = 123
h1_population_zone = 1_800_000
h1_budget_trimestre = 87_450_000.0
h1_nb_consultations = 4_823
h1_nb_hospitalisations = 1_247
h1_nb_deces = 18

# --- Hopital 2 : Hopital General Pointe-Noire ---
h2_nom = 'Hopital General Pointe-Noire'
h2_ville = 'Pointe-Noire'
h2_departement = 'Pointe-Noire'
h2_type = 'Hopital General'
h2_nb_lits = 180
h2_nb_lits_occupes = 143
h2_nb_medecins = 22
h2_nb_infirmiers = 58
h2_population_zone = 128_000
h2_budget_trimestre = 45_200_000.0
h2_nb_consultations = 2_156
h2_nb_hospitalisations = 689
h2_nb_deces = 12

# --- Hopital 3 : Hopital de Dolisie ---
h3_nom = 'Hopital de Dolisie'
h3_ville = 'Dolisie'
h3_departement = 'Niari'
h3_type = 'Hopital Regional'
h3_nb_lits = 95
h3_nb_lits_occupes = 71
h3_nb_medecins = 12
h3_nb_infirmiers = 34
h3_population_zone = 67_000
h3_budget_trimestre = 22_800_000.0
h3_nb_consultations = 1_432
h3_nb_hospitalisations = 345
h3_nb_deces = 5

# --- Hopital 4 : Hopital de district Owando ---
h4_nom = 'Hopital de District Owando'
h4_ville = 'Owando'
h4_departement = 'Cuvette'
h4_type = 'Hopital de District'
h4_nb_lits = 45
h4_nb_lits_occupes = 38
h4_nb_medecins = 5
h4_nb_infirmiers = 18
h4_population_zone = 42_000
h4_budget_trimestre = 12_500_000.0
h4_nb_consultations = 876
h4_nb_hospitalisations = 198
h4_nb_deces = 3

# --- Hopital 5 : Centre de sante de Impfondo ---
h5_nom = 'Centre de Sante de Impfondo'
h5_ville = 'Impfondo'
h5_departement = 'Likouala'
h5_type = 'Centre de Sante'
h5_nb_lits = 20
h5_nb_lits_occupes = 14
h5_nb_medecins = 2
h5_nb_infirmiers = 8
h5_population_zone = 28_000
h5_budget_trimestre = 6_800_000.0
h5_nb_consultations = 523
h5_nb_hospitalisations = 87
h5_nb_deces = 1

# ============================================================
# === SECTION C : VARIABLES DES 5 MEDICAMENTS ================
# ============================================================

# --- Medicament 1 : Artemether-Lumefantrine (paludisme) ---
m1_nom = 'Artemether-Lumefantrine'
m1_type = 'Antipaludique'
m1_qte_disponible = 12_500       # boites
m1_seuil_rupture = 2_000         # boites
m1_cout_unitaire = 3_500.0      # FCFA
m1_duree_stock_jours = 45

# --- Medicament 2 : Amoxicilline (antibiotique) ---
m2_nom = 'Amoxicilline'
m2_type = 'Antibiotique'
m2_qte_disponible = 8_200        # boites
m2_seuil_rupture = 1_500         # boites
m2_cout_unitaire = 2_800.0       # FCFA
m2_duree_stock_jours = 38

# --- Medicament 3 : Paracetamol (antipyretique) ---
m3_nom = 'Paracetamol'
m3_type = 'Antipyretique / Analgesique'
m3_qte_disponible = 25_000       # boites
m3_seuil_rupture = 5_000         # boites
m3_cout_unitaire = 1_200.0       # FCFA
m3_duree_stock_jours = 60

# --- Medicament 4 : SRO (Sels de Rehydratation Orale) ---
m4_nom = 'Sels de Rehydratation Orale (SRO)'
m4_type = 'Rehydratation'
m4_qte_disponible = 18_000       # sachets
m4_seuil_rupture = 3_000         # sachets
m4_cout_unitaire = 500.0         # FCFA
m4_duree_stock_jours = 52

# --- Medicament 5 : Vaccin Antipaludeen (RTS,S) ---
m5_nom = 'Vaccin Antipaludeen RTS,S'
m5_type = 'Vaccin'
m5_qte_disponible = 3_200        # doses
m5_seuil_rupture = 500           # doses
m5_cout_unitaire = 15_000.0      # FCFA
m5_duree_stock_jours = 25

# ============================================================
# === SECTION D : CALCULS D'INITIALISATION ===================
# ============================================================

# --- Calculs par hopital ---

# Densites medicales (medecins / 1000 hab)
h1_densite_medicale = round((h1_nb_medecins / h1_population_zone) * 1000, 2)
h2_densite_medicale = round((h2_nb_medecins / h2_population_zone) * 1000, 2)
h3_densite_medicale = round((h3_nb_medecins / h3_population_zone) * 1000, 2)
h4_densite_medicale = round((h4_nb_medecins / h4_population_zone) * 1000, 2)
h5_densite_medicale = round((h5_nb_medecins / h5_population_zone) * 1000, 2)

# Taux d'occupation des lits (%)
h1_taux_occupation = round((h1_nb_lits_occupes / h1_nb_lits) * 100, 1)
h2_taux_occupation = round((h2_nb_lits_occupes / h2_nb_lits) * 100, 1)
h3_taux_occupation = round((h3_nb_lits_occupes / h3_nb_lits) * 100, 1)
h4_taux_occupation = round((h4_nb_lits_occupes / h4_nb_lits) * 100, 1)
h5_taux_occupation = round((h5_nb_lits_occupes / h5_nb_lits) * 100, 1)

# Taux de mortalite hospitaliere (%)
h1_taux_mortalite = round((h1_nb_deces / h1_nb_hospitalisations) * 100, 2)
h2_taux_mortalite = round((h2_nb_deces / h2_nb_hospitalisations) * 100, 2)
h3_taux_mortalite = round((h3_nb_deces / h3_nb_hospitalisations) * 100, 2)
h4_taux_mortalite = round((h4_nb_deces / h4_nb_hospitalisations) * 100, 2)
h5_taux_mortalite = round((h5_nb_deces / h5_nb_hospitalisations) * 100, 2)

# --- Calculs globaux ---

# Densite medicale nationale (moyenne ponderee par population)
population_totale = h1_population_zone + h2_population_zone + h3_population_zone + h4_population_zone + h5_population_zone
total_medecins = h1_nb_medecins + h2_nb_medecins + h3_nb_medecins + h4_nb_medecins + h5_nb_medecins
densite_medicale_nationale = round((total_medecins / population_totale) * 1000, 2)

# Taux d'occupation moyen
taux_occupation_moyen = round((h1_taux_occupation + h2_taux_occupation + h3_taux_occupation + h4_taux_occupation + h5_taux_occupation) / 5, 1)

# Valeur totale du stock de medicaments
valeur_stock_m1 = m1_qte_disponible * m1_cout_unitaire
valeur_stock_m2 = m2_qte_disponible * m2_cout_unitaire
valeur_stock_m3 = m3_qte_disponible * m3_cout_unitaire
valeur_stock_m4 = m4_qte_disponible * m4_cout_unitaire
valeur_stock_m5 = m5_qte_disponible * m5_cout_unitaire
valeur_totale_stock = valeur_stock_m1 + valeur_stock_m2 + valeur_stock_m3 + valeur_stock_m4 + valeur_stock_m5

# Budget total des 5 hopitaux
budget_total_hopitaux = h1_budget_trimestre + h2_budget_trimestre + h3_budget_trimestre + h4_budget_trimestre + h5_budget_trimestre

# Nombre total de lits
total_lits = h1_nb_lits + h2_nb_lits + h3_nb_lits + h4_nb_lits + h5_nb_lits
total_lits_occupes = h1_nb_lits_occupes + h2_nb_lits_occupes + h3_nb_lits_occupes + h4_nb_lits_occupes + h5_nb_lits_occupes

# ============================================================
# === SECTION E : RAPPORT D'INVENTAIRE =======================
# ============================================================

if __name__ == '__main__':
    print("=" * 70)
    print("  RAPPORT D'INVENTAIRE — SYSTEME DE SANTE CONGO")
    print("  Projet Sante Publique / Akieni Academy — Semaine 2")
    print("=" * 70)
    print()

    # --- Informations generales ---
    print("-" * 70)
    print("  INFORMATIONS GENERALES")
    print("-" * 70)
    print(f"  Nombre de departements couverts : {len(DEPARTEMENTS_CONGO)}")
    print(f"  Population totale desservie     : {population_totale:,} habitants")
    print(f"  Taux de change EUR/FCFA         : {TAUX_EUR_FCFA}")
    print(f"  Taux de change USD/FCFA         : {TAUX_USD_FCFA}")
    print()

    # --- Tableau des hopitaux ---
    print("-" * 70)
    print("  ETAT DES 5 ETABLISSEMENTS DE SANTE")
    print("-" * 70)
    print(f"  {'Hopital':<30} {'Type':<18} {'Lits':>6} {'Med.':>5} {'Inf.':>5} {'Pop.':>10}")
    print("  " + "-" * 66)
    print(f"  {h1_nom:<30} {h1_type:<18} {h1_nb_lits:>6} {h1_nb_medecins:>5} {h1_nb_infirmiers:>5} {h1_population_zone:>10,}")
    print(f"  {h2_nom:<30} {h2_type:<18} {h2_nb_lits:>6} {h2_nb_medecins:>5} {h2_nb_infirmiers:>5} {h2_population_zone:>10,}")
    print(f"  {h3_nom:<30} {h3_type:<18} {h3_nb_lits:>6} {h3_nb_medecins:>5} {h3_nb_infirmiers:>5} {h3_population_zone:>10,}")
    print(f"  {h4_nom:<30} {h4_type:<18} {h4_nb_lits:>6} {h4_nb_medecins:>5} {h4_nb_infirmiers:>5} {h4_population_zone:>10,}")
    print(f"  {h5_nom:<30} {h5_type:<18} {h5_nb_lits:>6} {h5_nb_medecins:>5} {h5_nb_infirmiers:>5} {h5_population_zone:>10,}")
    print("  " + "-" * 66)
    print(f"  {'TOTAL':<30} {'':<18} {total_lits:>6} {total_medecins:>5} {h1_nb_infirmiers+h2_nb_infirmiers+h3_nb_infirmiers+h4_nb_infirmiers+h5_nb_infirmiers:>5} {population_totale:>10,}")
    print()

    # --- KPIs par hopital ---
    print("-" * 70)
    print("  INDICATEURS DE PERFORMANCE PAR ETABLISSEMENT")
    print("-" * 70)
    print(f"  {'Hopital':<30} {'Occup.':>8} {'Densite':>10} {'Mortalite':>10}")
    print(f"  {'':<30} {'(%)':>8} {'(/1000)':>10} {'(%)':>10}")
    print("  " + "-" * 52)
    print(f"  {h1_nom:<30} {h1_taux_occupation:>8.1f} {h1_densite_medicale:>10.2f} {h1_taux_mortalite:>10.2f}")
    print(f"  {h2_nom:<30} {h2_taux_occupation:>8.1f} {h2_densite_medicale:>10.2f} {h2_taux_mortalite:>10.2f}")
    print(f"  {h3_nom:<30} {h3_taux_occupation:>8.1f} {h3_densite_medicale:>10.2f} {h3_taux_mortalite:>10.2f}")
    print(f"  {h4_nom:<30} {h4_taux_occupation:>8.1f} {h4_densite_medicale:>10.2f} {h4_taux_mortalite:>10.2f}")
    print(f"  {h5_nom:<30} {h5_taux_occupation:>8.1f} {h5_densite_medicale:>10.2f} {h5_taux_mortalite:>10.2f}")
    print("  " + "-" * 52)
    print(f"  {'MOYENNE / NATIONALE':<30} {taux_occupation_moyen:>8.1f} {densite_medicale_nationale:>10.2f} {'—':>10}")
    print()
    print(f"  Seuil OMS densite medicale : >= {SEUIL_OMS_DENSITE_MEDICALE} medecins/1000 hab")
    print(f"  Seuil OMS mortalite        : < {SEUIL_MORTALITE_ALERTE}%")
    print()

    # --- Alertes ---
    print("-" * 70)
    print("  ALERTES ET SITUATIONS CRITIQUES")
    print("-" * 70)

    alertes = []
    if h1_densite_medicale < SEUIL_OMS_DENSITE_MEDICALE:
        alertes.append(f"    {h1_nom} : Densite medicale CRITIQUE ({h1_densite_medicale} < {SEUIL_OMS_DENSITE_MEDICALE})")
    if h2_densite_medicale < SEUIL_OMS_DENSITE_MEDICALE:
        alertes.append(f"    {h2_nom} : Densite medicale CRITIQUE ({h2_densite_medicale} < {SEUIL_OMS_DENSITE_MEDICALE})")
    if h3_densite_medicale < SEUIL_OMS_DENSITE_MEDICALE:
        alertes.append(f"    {h3_nom} : Densite medicale CRITIQUE ({h3_densite_medicale} < {SEUIL_OMS_DENSITE_MEDICALE})")
    if h4_densite_medicale < SEUIL_OMS_DENSITE_MEDICALE:
        alertes.append(f"    {h4_nom} : Densite medicale CRITIQUE ({h4_densite_medicale} < {SEUIL_OMS_DENSITE_MEDICALE})")
    if h5_densite_medicale < SEUIL_OMS_DENSITE_MEDICALE:
        alertes.append(f"    {h5_nom} : Densite medicale CRITIQUE ({h5_densite_medicale} < {SEUIL_OMS_DENSITE_MEDICALE})")

    if h1_taux_mortalite > SEUIL_MORTALITE_ALERTE:
        alertes.append(f"    {h1_nom} : Taux de mortalite ELEVE ({h1_taux_mortalite}% > {SEUIL_MORTALITE_ALERTE}%)")
    if h2_taux_mortalite > SEUIL_MORTALITE_ALERTE:
        alertes.append(f"    {h2_nom} : Taux de mortalite ELEVE ({h2_taux_mortalite}% > {SEUIL_MORTALITE_ALERTE}%)")
    if h3_taux_mortalite > SEUIL_MORTALITE_ALERTE:
        alertes.append(f"    {h3_nom} : Taux de mortalite ELEVE ({h3_taux_mortalite}% > {SEUIL_MORTALITE_ALERTE}%)")
    if h4_taux_mortalite > SEUIL_MORTALITE_ALERTE:
        alertes.append(f"    {h4_nom} : Taux de mortalite ELEVE ({h4_taux_mortalite}% > {SEUIL_MORTALITE_ALERTE}%)")
    if h5_taux_mortalite > SEUIL_MORTALITE_ALERTE:
        alertes.append(f"    {h5_nom} : Taux de mortalite ELEVE ({h5_taux_mortalite}% > {SEUIL_MORTALITE_ALERTE}%)")

    if len(alertes) == 0:
        print("   Aucune alerte critique detectee")
    else:
        for alerte in alertes:
            print(alerte)

    print()

    # --- Stock de medicaments ---
    print("-" * 70)
    print("  ETAT DU STOCK DE MEDICAMENTS ESSENTIELS")
    print("-" * 70)
    print(f"  {'Medicament':<35} {'Qte':>10} {'Seuil':>8} {'Unite (FCFA)':>14} {'Valeur (FCFA)':>16}")
    print("  " + "-" * 75)
    print(f"  {m1_nom:<35} {m1_qte_disponible:>10,} {m1_seuil_rupture:>8,} {m1_cout_unitaire:>14,.2f} {valeur_stock_m1:>16,.2f}")
    print(f"  {m2_nom:<35} {m2_qte_disponible:>10,} {m2_seuil_rupture:>8,} {m2_cout_unitaire:>14,.2f} {valeur_stock_m2:>16,.2f}")
    print(f"  {m3_nom:<35} {m3_qte_disponible:>10,} {m3_seuil_rupture:>8,} {m3_cout_unitaire:>14,.2f} {valeur_stock_m3:>16,.2f}")
    print(f"  {m4_nom:<35} {m4_qte_disponible:>10,} {m4_seuil_rupture:>8,} {m4_cout_unitaire:>14,.2f} {valeur_stock_m4:>16,.2f}")
    print(f"  {m5_nom:<35} {m5_qte_disponible:>10,} {m5_seuil_rupture:>8,} {m5_cout_unitaire:>14,.2f} {valeur_stock_m5:>16,.2f}")
    print("  " + "-" * 75)
    print(f"  {'VALEUR TOTALE DU STOCK':<35} {'':>10} {'':>8} {'':>14} {valeur_totale_stock:>16,.2f}")
    print()

    # --- Alertes stock ---
    print("-" * 70)
    print("  ALERTES RUPTURE DE STOCK")
    print("-" * 70)
    if m1_duree_stock_jours < SEUIL_RUPTURE_STOCK_JOURS:
        print(f"    {m1_nom} : Stock critique ({m1_duree_stock_jours} jours restants)")
    if m2_duree_stock_jours < SEUIL_RUPTURE_STOCK_JOURS:
        print(f"    {m2_nom} : Stock critique ({m2_duree_stock_jours} jours restants)")
    if m3_duree_stock_jours < SEUIL_RUPTURE_STOCK_JOURS:
        print(f"    {m3_nom} : Stock critique ({m3_duree_stock_jours} jours restants)")
    if m4_duree_stock_jours < SEUIL_RUPTURE_STOCK_JOURS:
        print(f"    {m4_nom} : Stock critique ({m4_duree_stock_jours} jours restants)")
    if m5_duree_stock_jours < SEUIL_RUPTURE_STOCK_JOURS:
        print(f"    {m5_nom} : Stock critique ({m5_duree_stock_jours} jours restants)")
    else:
        print("   Tous les stocks sont au-dessus du seuil critique")

    print()

    # --- Synthese budgetaire ---
    print("-" * 70)
    print("  SYNTHESE BUDGETAIRE")
    print("-" * 70)
    print(f"  Budget total trimestriel : {budget_total_hopitaux:,.2f} FCFA")
    print(f"  Budget total en EUR      : {round(budget_total_hopitaux / TAUX_EUR_FCFA, 2):,.2f} EUR")
    print(f"  Budget total en USD      : {round(budget_total_hopitaux / TAUX_USD_FCFA, 2):,.2f} USD")
    print(f"  Valeur totale du stock   : {valeur_totale_stock:,.2f} FCFA")
    print()

    print("=" * 70)
    print("  FIN DU RAPPORT D'INVENTAIRE")
    print("=" * 70)