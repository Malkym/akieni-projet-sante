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

# === NOUVEAU S3 : Seuils pour classification stocks ===
SEUIL_STOCK_RUPTURE_MULTIPLICATEUR = 1.0      # stock <= seuil * 1.0
SEUIL_STOCK_ALERTE_MULTIPLICATEUR = 1.5       # stock <= seuil * 1.5
SEUIL_STOCK_LIMITE_MULTIPLICATEUR = 2.0         # stock <= seuil * 2.0

# === NOUVEAU S3 : Seuils pour occupation des lits ===
SEUIL_OCCUPATION_CRITIQUE = 95.0              # > 95% = saturation
SEUIL_OCCUPATION_ELEVEE = 85.0                # > 85% = capacite limite
SEUIL_OCCUPATION_OPTIMALE = 70.0              # > 70% = optimal

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
h1_nb_lits_occupes = 298                      # MODIFIE S3 pour challenge
h1_nb_medecins = 47
h1_nb_infirmiers = 123
h1_population_zone = 1_800_000
h1_budget_trimestre = 87_450_000.0
h1_nb_consultations = 4_823
h1_nb_hospitalisations = 1_247
h1_nb_deces = 18
h1_taux_remise_cnss = 30.0
# === NOUVEAU S3 : Medicaments en rupture/alerte ===
h1_nb_meds_rupture = 2                          # SRO, Vaccin
h1_nb_meds_alerte = 2                           # Artemether, Amoxi

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
h2_taux_remise_cnss = 25.0
h2_nb_meds_rupture = 0
h2_nb_meds_alerte = 1                           # Amoxicilline

# --- Hopital 3 : Hopital de Dolisie ---
h3_nom = 'Hopital de Dolisie'
h3_ville = 'Dolisie'
h3_departement = 'Niari'
h3_type = 'Hopital Regional'
h3_nb_lits = 95
h3_nb_lits_occupes = 91                       # MODIFIE S3
h3_nb_medecins = 8                            # MODIFIE S3
h3_nb_infirmiers = 34
h3_population_zone = 67_000
h3_budget_trimestre = 22_800_000.0
h3_nb_consultations = 1_432
h3_nb_hospitalisations = 345
h3_nb_deces = 5
h3_taux_remise_cnss = 20.0
h3_nb_meds_rupture = 1                          # SRO
h3_nb_meds_alerte = 2                           # Artemether, Vaccin

# --- Hopital 4 : Hopital de district Owando ---
h4_nom = 'Hopital de District Owando'
h4_ville = 'Owando'
h4_departement = 'Cuvette'
h4_type = 'Hopital de District'
h4_nb_lits = 45
h4_nb_lits_occupes = 32
h4_nb_medecins = 3                            # MODIFIE S3
h4_nb_infirmiers = 18
h4_population_zone = 42_000
h4_budget_trimestre = 12_500_000.0
h4_nb_consultations = 876
h4_nb_hospitalisations = 198
h4_nb_deces = 3
h4_taux_remise_cnss = 15.0
h4_nb_meds_rupture = 3                          # SRO, Vaccin, Artemether
h4_nb_meds_alerte = 0

# --- Hopital 5 : Centre de sante de Impfondo ---
h5_nom = 'Centre de Sante de Impfondo'
h5_ville = 'Impfondo'
h5_departement = 'Likouala'
h5_type = 'Centre de Sante'
h5_nb_lits = 20
h5_nb_lits_occupes = 19
h5_nb_medecins = 1
h5_nb_infirmiers = 8
h5_population_zone = 28_000
h5_budget_trimestre = 6_800_000.0
h5_nb_consultations = 523
h5_nb_hospitalisations = 87
h5_nb_deces = 1
h5_taux_remise_cnss = 10.0
h5_nb_meds_rupture = 2                          # SRO, Amoxi
h5_nb_meds_alerte = 1                           # Vaccin

# ============================================================
# === SECTION C : VARIABLES DES 5 MEDICAMENTS ================
# ============================================================

# --- Medicament 1 : Artemether-Lumefantrine ---
m1_nom = 'Artemether-Lumefantrine'
m1_type = 'Antipaludique'
m1_qte_disponible = 3200
m1_seuil_rupture = 2000
m1_seuil_alerte = 2500
m1_cout_unitaire = 3_500.0
m1_duree_stock_jours = 45

# --- Medicament 2 : Amoxicilline 500mg ---
m2_nom = 'Amoxicilline 500mg'
m2_type = 'Antibiotique'
m2_qte_disponible = 950
m2_seuil_rupture = 800
m2_seuil_alerte = 900
m2_cout_unitaire = 2_800.0
m2_duree_stock_jours = 38

# --- Medicament 3 : Paracetamol 500mg ---
m3_nom = 'Paracetamol 500mg'
m3_type = 'Antipyretique / Analgesique'
m3_qte_disponible = 12400
m3_seuil_rupture = 3000
m3_seuil_alerte = 3500
m3_cout_unitaire = 1_200.0
m3_duree_stock_jours = 60

# --- Medicament 4 : SRO ---
m4_nom = 'Sels de Rehydratation Orale (SRO)'
m4_type = 'Rehydratation'
m4_qte_disponible = 4200
m4_seuil_rupture = 5000
m4_seuil_alerte = 4500
m4_cout_unitaire = 500.0
m4_duree_stock_jours = 52

# --- Medicament 5 : Vaccin DTP-HepB-Hib ---
m5_nom = 'Vaccin DTP-HepB-Hib'
m5_type = 'Vaccin'
m5_qte_disponible = 820
m5_seuil_rupture = 1000
m5_seuil_alerte = 900
m5_cout_unitaire = 15_000.0
m5_duree_stock_jours = 25

# ============================================================
# === SECTION D : CALCULS D'INITIALISATION (S2) ==============
# ============================================================

h1_densite_medicale = round((h1_nb_medecins / h1_population_zone) * 1000, 2)
h2_densite_medicale = round((h2_nb_medecins / h2_population_zone) * 1000, 2)
h3_densite_medicale = round((h3_nb_medecins / h3_population_zone) * 1000, 2)
h4_densite_medicale = round((h4_nb_medecins / h4_population_zone) * 1000, 2)
h5_densite_medicale = round((h5_nb_medecins / h5_population_zone) * 1000, 2)

h1_taux_occupation = round((h1_nb_lits_occupes / h1_nb_lits) * 100, 1)
h2_taux_occupation = round((h2_nb_lits_occupes / h2_nb_lits) * 100, 1)
h3_taux_occupation = round((h3_nb_lits_occupes / h3_nb_lits) * 100, 1)
h4_taux_occupation = round((h4_nb_lits_occupes / h4_nb_lits) * 100, 1)
h5_taux_occupation = round((h5_nb_lits_occupes / h5_nb_lits) * 100, 1)

h1_taux_mortalite = round((h1_nb_deces / h1_nb_hospitalisations) * 100, 2)
h2_taux_mortalite = round((h2_nb_deces / h2_nb_hospitalisations) * 100, 2)
h3_taux_mortalite = round((h3_nb_deces / h3_nb_hospitalisations) * 100, 2)
h4_taux_mortalite = round((h4_nb_deces / h4_nb_hospitalisations) * 100, 2)
h5_taux_mortalite = round((h5_nb_deces / h5_nb_hospitalisations) * 100, 2)

population_totale = h1_population_zone + h2_population_zone + h3_population_zone + h4_population_zone + h5_population_zone
total_medecins = h1_nb_medecins + h2_nb_medecins + h3_nb_medecins + h4_nb_medecins + h5_nb_medecins
densite_medicale_nationale = round((total_medecins / population_totale) * 1000, 2)

taux_occupation_moyen = round((h1_taux_occupation + h2_taux_occupation + h3_taux_occupation + h4_taux_occupation + h5_taux_occupation) / 5, 1)

valeur_stock_m1 = m1_qte_disponible * m1_cout_unitaire
valeur_stock_m2 = m2_qte_disponible * m2_cout_unitaire
valeur_stock_m3 = m3_qte_disponible * m3_cout_unitaire
valeur_stock_m4 = m4_qte_disponible * m4_cout_unitaire
valeur_stock_m5 = m5_qte_disponible * m5_cout_unitaire
valeur_totale_stock = valeur_stock_m1 + valeur_stock_m2 + valeur_stock_m3 + valeur_stock_m4 + valeur_stock_m5

budget_total_hopitaux = h1_budget_trimestre + h2_budget_trimestre + h3_budget_trimestre + h4_budget_trimestre + h5_budget_trimestre
total_lits = h1_nb_lits + h2_nb_lits + h3_nb_lits + h4_nb_lits + h5_nb_lits
total_lits_occupes = h1_nb_lits_occupes + h2_nb_lits_occupes + h3_nb_lits_occupes + h4_nb_lits_occupes + h5_nb_lits_occupes

# ============================================================
# === SECTION F : CLASSIFICATION STATUT STOCKS (NEW S3) ======
# ============================================================

# --- Medicament 1 : Artemether-Lumefantrine ---
if m1_qte_disponible <= m1_seuil_rupture * SEUIL_STOCK_RUPTURE_MULTIPLICATEUR:
    m1_statut = 'RUPTURE CRITIQUE'
    m1_couleur = '[ROUGE]'
    m1_action = 'Alerte immediate PNA — commande express sous 24h'
elif m1_qte_disponible <= m1_seuil_rupture * SEUIL_STOCK_ALERTE_MULTIPLICATEUR:
    m1_statut = 'ALERTE STOCK'
    m1_couleur = '[ORANGE]'
    m1_action = 'Commande urgente a declencher sous 72h'
elif m1_qte_disponible <= m1_seuil_rupture * SEUIL_STOCK_LIMITE_MULTIPLICATEUR:
    m1_statut = 'STOCK LIMITE'
    m1_couleur = '[JAUNE]'
    m1_action = 'Surveillance renforcee — planifier commande'
else:
    m1_statut = 'STOCK NORMAL'
    m1_couleur = '[VERT]'
    m1_action = 'Situation normale — suivi standard'

# --- Medicament 2 : Amoxicilline ---
if m2_qte_disponible <= m2_seuil_rupture * SEUIL_STOCK_RUPTURE_MULTIPLICATEUR:
    m2_statut = 'RUPTURE CRITIQUE'
    m2_couleur = '[ROUGE]'
    m2_action = 'Alerte immediate PNA — commande express sous 24h'
elif m2_qte_disponible <= m2_seuil_rupture * SEUIL_STOCK_ALERTE_MULTIPLICATEUR:
    m2_statut = 'ALERTE STOCK'
    m2_couleur = '[ORANGE]'
    m2_action = 'Commande urgente a declencher sous 72h'
elif m2_qte_disponible <= m2_seuil_rupture * SEUIL_STOCK_LIMITE_MULTIPLICATEUR:
    m2_statut = 'STOCK LIMITE'
    m2_couleur = '[JAUNE]'
    m2_action = 'Surveillance renforcee — planifier commande'
else:
    m2_statut = 'STOCK NORMAL'
    m2_couleur = '[VERT]'
    m2_action = 'Situation normale — suivi standard'

# --- Medicament 3 : Paracetamol ---
if m3_qte_disponible <= m3_seuil_rupture * SEUIL_STOCK_RUPTURE_MULTIPLICATEUR:
    m3_statut = 'RUPTURE CRITIQUE'
    m3_couleur = '[ROUGE]'
    m3_action = 'Alerte immediate PNA — commande express sous 24h'
elif m3_qte_disponible <= m3_seuil_rupture * SEUIL_STOCK_ALERTE_MULTIPLICATEUR:
    m3_statut = 'ALERTE STOCK'
    m3_couleur = '[ORANGE]'
    m3_action = 'Commande urgente a declencher sous 72h'
elif m3_qte_disponible <= m3_seuil_rupture * SEUIL_STOCK_LIMITE_MULTIPLICATEUR:
    m3_statut = 'STOCK LIMITE'
    m3_couleur = '[JAUNE]'
    m3_action = 'Surveillance renforcee — planifier commande'
else:
    m3_statut = 'STOCK NORMAL'
    m3_couleur = '[VERT]'
    m3_action = 'Situation normale — suivi standard'

# --- Medicament 4 : SRO ---
if m4_qte_disponible <= m4_seuil_rupture * SEUIL_STOCK_RUPTURE_MULTIPLICATEUR:
    m4_statut = 'RUPTURE CRITIQUE'
    m4_couleur = '[ROUGE]'
    m4_action = 'Alerte immediate PNA — commande express sous 24h'
elif m4_qte_disponible <= m4_seuil_rupture * SEUIL_STOCK_ALERTE_MULTIPLICATEUR:
    m4_statut = 'ALERTE STOCK'
    m4_couleur = '[ORANGE]'
    m4_action = 'Commande urgente a declencher sous 72h'
elif m4_qte_disponible <= m4_seuil_rupture * SEUIL_STOCK_LIMITE_MULTIPLICATEUR:
    m4_statut = 'STOCK LIMITE'
    m4_couleur = '[JAUNE]'
    m4_action = 'Surveillance renforcee — planifier commande'
else:
    m4_statut = 'STOCK NORMAL'
    m4_couleur = '[VERT]'
    m4_action = 'Situation normale — suivi standard'

# --- Medicament 5 : Vaccin ---
if m5_qte_disponible <= m5_seuil_rupture * SEUIL_STOCK_RUPTURE_MULTIPLICATEUR:
    m5_statut = 'RUPTURE CRITIQUE'
    m5_couleur = '[ROUGE]'
    m5_action = 'Alerte immediate PNA — commande express sous 24h'
elif m5_qte_disponible <= m5_seuil_rupture * SEUIL_STOCK_ALERTE_MULTIPLICATEUR:
    m5_statut = 'ALERTE STOCK'
    m5_couleur = '[ORANGE]'
    m5_action = 'Commande urgente a declencher sous 72h'
elif m5_qte_disponible <= m5_seuil_rupture * SEUIL_STOCK_LIMITE_MULTIPLICATEUR:
    m5_statut = 'STOCK LIMITE'
    m5_couleur = '[JAUNE]'
    m5_action = 'Surveillance renforcee — planifier commande'
else:
    m5_statut = 'STOCK NORMAL'
    m5_couleur = '[VERT]'
    m5_action = 'Situation normale — suivi standard'

# ============================================================
# === SECTION G : CLASSIFICATION OCCUPATION HOPITAUX (NEW S3) =
# ============================================================

# --- Hopital 1 ---
if h1_taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
    h1_niveau_occupation = 'ALERTE CRITIQUE'
    h1_couleur_occupation = '[ROUGE]'
    h1_action_occupation = 'Saturation — transferts a organiser'
elif h1_taux_occupation > SEUIL_OCCUPATION_ELEVEE:
    h1_niveau_occupation = 'ALERTE ELEVEE'
    h1_couleur_occupation = '[ORANGE]'
    h1_action_occupation = 'Capacite limite — renforcement prevu'
elif h1_taux_occupation > SEUIL_OCCUPATION_OPTIMALE:
    h1_niveau_occupation = 'SITUATION OPTIMALE'
    h1_couleur_occupation = '[VERT]'
    h1_action_occupation = 'Occupation dans la norme'
else:
    h1_niveau_occupation = 'SOUS-UTILISATION'
    h1_couleur_occupation = '[BLEU]'
    h1_action_occupation = 'Ressources sous-exploitees'

# --- Hopital 2 ---
if h2_taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
    h2_niveau_occupation = 'ALERTE CRITIQUE'
    h2_couleur_occupation = '[ROUGE]'
    h2_action_occupation = 'Saturation — transferts a organiser'
elif h2_taux_occupation > SEUIL_OCCUPATION_ELEVEE:
    h2_niveau_occupation = 'ALERTE ELEVEE'
    h2_couleur_occupation = '[ORANGE]'
    h2_action_occupation = 'Capacite limite — renforcement prevu'
elif h2_taux_occupation > SEUIL_OCCUPATION_OPTIMALE:
    h2_niveau_occupation = 'SITUATION OPTIMALE'
    h2_couleur_occupation = '[VERT]'
    h2_action_occupation = 'Occupation dans la norme'
else:
    h2_niveau_occupation = 'SOUS-UTILISATION'
    h2_couleur_occupation = '[BLEU]'
    h2_action_occupation = 'Ressources sous-exploitees'

# --- Hopital 3 ---
if h3_taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
    h3_niveau_occupation = 'ALERTE CRITIQUE'
    h3_couleur_occupation = '[ROUGE]'
    h3_action_occupation = 'Saturation — transferts a organiser'
elif h3_taux_occupation > SEUIL_OCCUPATION_ELEVEE:
    h3_niveau_occupation = 'ALERTE ELEVEE'
    h3_couleur_occupation = '[ORANGE]'
    h3_action_occupation = 'Capacite limite — renforcement prevu'
elif h3_taux_occupation > SEUIL_OCCUPATION_OPTIMALE:
    h3_niveau_occupation = 'SITUATION OPTIMALE'
    h3_couleur_occupation = '[VERT]'
    h3_action_occupation = 'Occupation dans la norme'
else:
    h3_niveau_occupation = 'SOUS-UTILISATION'
    h3_couleur_occupation = '[BLEU]'
    h3_action_occupation = 'Ressources sous-exploitees'

# --- Hopital 4 ---
if h4_taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
    h4_niveau_occupation = 'ALERTE CRITIQUE'
    h4_couleur_occupation = '[ROUGE]'
    h4_action_occupation = 'Saturation — transferts a organiser'
elif h4_taux_occupation > SEUIL_OCCUPATION_ELEVEE:
    h4_niveau_occupation = 'ALERTE ELEVEE'
    h4_couleur_occupation = '[ORANGE]'
    h4_action_occupation = 'Capacite limite — renforcement prevu'
elif h4_taux_occupation > SEUIL_OCCUPATION_OPTIMALE:
    h4_niveau_occupation = 'SITUATION OPTIMALE'
    h4_couleur_occupation = '[VERT]'
    h4_action_occupation = 'Occupation dans la norme'
else:
    h4_niveau_occupation = 'SOUS-UTILISATION'
    h4_couleur_occupation = '[BLEU]'
    h4_action_occupation = 'Ressources sous-exploitees'

# --- Hopital 5 ---
if h5_taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
    h5_niveau_occupation = 'ALERTE CRITIQUE'
    h5_couleur_occupation = '[ROUGE]'
    h5_action_occupation = 'Saturation — transferts a organiser'
elif h5_taux_occupation > SEUIL_OCCUPATION_ELEVEE:
    h5_niveau_occupation = 'ALERTE ELEVEE'
    h5_couleur_occupation = '[ORANGE]'
    h5_action_occupation = 'Capacite limite — renforcement prevu'
elif h5_taux_occupation > SEUIL_OCCUPATION_OPTIMALE:
    h5_niveau_occupation = 'SITUATION OPTIMALE'
    h5_couleur_occupation = '[VERT]'
    h5_action_occupation = 'Occupation dans la norme'
else:
    h5_niveau_occupation = 'SOUS-UTILISATION'
    h5_couleur_occupation = '[BLEU]'
    h5_action_occupation = 'Ressources sous-exploitees'

# ============================================================
# === SECTION H : COUVERTURE VACCINALE (NEW S3) ==============
# ============================================================

# Donnees des departements
d1_nom = 'Brazzaville'
d1_population_cible = 450_000
d1_personnes_vaccinees = 418_500

d2_nom = 'Pointe-Noire'
d2_population_cible = 280_000
d2_personnes_vaccinees = 229_600

d3_nom = 'Pool'
d3_population_cible = 120_000
d3_personnes_vaccinees = 54_000

d4_nom = 'Sangha'
d4_population_cible = 85_000
d4_personnes_vaccinees = 35_700

# Calculs des taux
d1_taux_couverture = round((d1_personnes_vaccinees / d1_population_cible) * 100, 1)
d2_taux_couverture = round((d2_personnes_vaccinees / d2_population_cible) * 100, 1)
d3_taux_couverture = round((d3_personnes_vaccinees / d3_population_cible) * 100, 1)
d4_taux_couverture = round((d4_personnes_vaccinees / d4_population_cible) * 100, 1)

# --- Classification Brazzaville ---
if d1_taux_couverture < 50:
    d1_statut_vaccin = 'ZONE CRITIQUE'
    d1_couleur_vaccin = '[ROUGE]'
    d1_action_vaccin = 'Campagne d\'urgence obligatoire'
elif d1_taux_couverture < 80:
    d1_statut_vaccin = 'ZONE A RISQUE'
    d1_couleur_vaccin = '[ORANGE]'
    d1_action_vaccin = 'Campagne renforcee requise'
elif d1_taux_couverture < SEUIL_OMS_COUVERTURE_VACCIN:
    d1_statut_vaccin = 'ZONE INSUFFISANTE'
    d1_couleur_vaccin = '[JAUNE]'
    d1_action_vaccin = 'Objectif OMS non atteint'
else:
    d1_statut_vaccin = 'ZONE OMS CONFORME'
    d1_couleur_vaccin = '[VERT]'
    d1_action_vaccin = 'Objectif OMS atteint'

# --- Classification Pointe-Noire ---
if d2_taux_couverture < 50:
    d2_statut_vaccin = 'ZONE CRITIQUE'
    d2_couleur_vaccin = '[ROUGE]'
    d2_action_vaccin = 'Campagne d\'urgence obligatoire'
elif d2_taux_couverture < 80:
    d2_statut_vaccin = 'ZONE A RISQUE'
    d2_couleur_vaccin = '[ORANGE]'
    d2_action_vaccin = 'Campagne renforcee requise'
elif d2_taux_couverture < SEUIL_OMS_COUVERTURE_VACCIN:
    d2_statut_vaccin = 'ZONE INSUFFISANTE'
    d2_couleur_vaccin = '[JAUNE]'
    d2_action_vaccin = 'Objectif OMS non atteint'
else:
    d2_statut_vaccin = 'ZONE OMS CONFORME'
    d2_couleur_vaccin = '[VERT]'
    d2_action_vaccin = 'Objectif OMS atteint'

# --- Classification Pool ---
if d3_taux_couverture < 50:
    d3_statut_vaccin = 'ZONE CRITIQUE'
    d3_couleur_vaccin = '[ROUGE]'
    d3_action_vaccin = 'Campagne d\'urgence obligatoire'
elif d3_taux_couverture < 80:
    d3_statut_vaccin = 'ZONE A RISQUE'
    d3_couleur_vaccin = '[ORANGE]'
    d3_action_vaccin = 'Campagne renforcee requise'
elif d3_taux_couverture < SEUIL_OMS_COUVERTURE_VACCIN:
    d3_statut_vaccin = 'ZONE INSUFFISANTE'
    d3_couleur_vaccin = '[JAUNE]'
    d3_action_vaccin = 'Objectif OMS non atteint'
else:
    d3_statut_vaccin = 'ZONE OMS CONFORME'
    d3_couleur_vaccin = '[VERT]'
    d3_action_vaccin = 'Objectif OMS atteint'

# --- Classification Sangha ---
if d4_taux_couverture < 50:
    d4_statut_vaccin = 'ZONE CRITIQUE'
    d4_couleur_vaccin = '[ROUGE]'
    d4_action_vaccin = 'Campagne d\'urgence obligatoire'
elif d4_taux_couverture < 80:
    d4_statut_vaccin = 'ZONE A RISQUE'
    d4_couleur_vaccin = '[ORANGE]'
    d4_action_vaccin = 'Campagne renforcee requise'
elif d4_taux_couverture < SEUIL_OMS_COUVERTURE_VACCIN:
    d4_statut_vaccin = 'ZONE INSUFFISANTE'
    d4_couleur_vaccin = '[JAUNE]'
    d4_action_vaccin = 'Objectif OMS non atteint'
else:
    d4_statut_vaccin = 'ZONE OMS CONFORME'
    d4_couleur_vaccin = '[VERT]'
    d4_action_vaccin = 'Objectif OMS atteint'

# ============================================================
# === SECTION I : RAPPORT D'ETAT GLOBAL AVEC ALERTES (NEW S3) =
# ============================================================

# Compteurs d'alertes
nb_ruptures_critiques = 0
nb_alertes_stock = 0
nb_stocks_normaux = 0

if m1_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques += 1
elif m1_statut == 'ALERTE STOCK':
    nb_alertes_stock += 1
elif m1_statut == 'STOCK NORMAL':
    nb_stocks_normaux += 1

if m2_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques += 1
elif m2_statut == 'ALERTE STOCK':
    nb_alertes_stock += 1
elif m2_statut == 'STOCK NORMAL':
    nb_stocks_normaux += 1

if m3_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques += 1
elif m3_statut == 'ALERTE STOCK':
    nb_alertes_stock += 1
elif m3_statut == 'STOCK NORMAL':
    nb_stocks_normaux += 1

if m4_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques += 1
elif m4_statut == 'ALERTE STOCK':
    nb_alertes_stock += 1
elif m4_statut == 'STOCK NORMAL':
    nb_stocks_normaux += 1

if m5_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques += 1
elif m5_statut == 'ALERTE STOCK':
    nb_alertes_stock += 1
elif m5_statut == 'STOCK NORMAL':
    nb_stocks_normaux += 1

# Compteurs hopitaux critiques
nb_hopitaux_critiques = 0
nb_hopitaux_preoccupants = 0
nb_hopitaux_satisfaisants = 0

# Classification niveau global hopitaux (Challenge S3)
if h1_nb_meds_rupture >= 2 or h1_taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
    h1_niveau_global = 'CRITIQUE'
    h1_couleur_global = '[CRITIQUE]'
    nb_hopitaux_critiques += 1
elif h1_nb_meds_rupture >= 1 or h1_taux_occupation > SEUIL_OCCUPATION_ELEVEE or (h1_nb_meds_alerte >= 2 and h1_nb_medecins < 5):
    h1_niveau_global = 'PREOCCUPANT'
    h1_couleur_global = '[PREOCCUPANT]'
    nb_hopitaux_preoccupants += 1
else:
    h1_niveau_global = 'SATISFAISANT'
    h1_couleur_global = '[SATISFAISANT]'
    nb_hopitaux_satisfaisants += 1

if h2_nb_meds_rupture >= 2 or h2_taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
    h2_niveau_global = 'CRITIQUE'
    h2_couleur_global = '[CRITIQUE]'
    nb_hopitaux_critiques += 1
elif h2_nb_meds_rupture >= 1 or h2_taux_occupation > SEUIL_OCCUPATION_ELEVEE or (h2_nb_meds_alerte >= 2 and h2_nb_medecins < 5):
    h2_niveau_global = 'PREOCCUPANT'
    h2_couleur_global = '[PREOCCUPANT]'
    nb_hopitaux_preoccupants += 1
else:
    h2_niveau_global = 'SATISFAISANT'
    h2_couleur_global = '[SATISFAISANT]'
    nb_hopitaux_satisfaisants += 1

if h3_nb_meds_rupture >= 2 or h3_taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
    h3_niveau_global = 'CRITIQUE'
    h3_couleur_global = '[CRITIQUE]'
    nb_hopitaux_critiques += 1
elif h3_nb_meds_rupture >= 1 or h3_taux_occupation > SEUIL_OCCUPATION_ELEVEE or (h3_nb_meds_alerte >= 2 and h3_nb_medecins < 5):
    h3_niveau_global = 'PREOCCUPANT'
    h3_couleur_global = '[PREOCCUPANT]'
    nb_hopitaux_preoccupants += 1
else:
    h3_niveau_global = 'SATISFAISANT'
    h3_couleur_global = '[SATISFAISANT]'
    nb_hopitaux_satisfaisants += 1

if h4_nb_meds_rupture >= 2 or h4_taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
    h4_niveau_global = 'CRITIQUE'
    h4_couleur_global = '[CRITIQUE]'
    nb_hopitaux_critiques += 1
elif h4_nb_meds_rupture >= 1 or h4_taux_occupation > SEUIL_OCCUPATION_ELEVEE or (h4_nb_meds_alerte >= 2 and h4_nb_medecins < 5):
    h4_niveau_global = 'PREOCCUPANT'
    h4_couleur_global = '[PREOCCUPANT]'
    nb_hopitaux_preoccupants += 1
else:
    h4_niveau_global = 'SATISFAISANT'
    h4_couleur_global = '[SATISFAISANT]'
    nb_hopitaux_satisfaisants += 1

if h5_nb_meds_rupture >= 2 or h5_taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
    h5_niveau_global = 'CRITIQUE'
    h5_couleur_global = '[CRITIQUE]'
    nb_hopitaux_critiques += 1
elif h5_nb_meds_rupture >= 1 or h5_taux_occupation > SEUIL_OCCUPATION_ELEVEE or (h5_nb_meds_alerte >= 2 and h5_nb_medecins < 5):
    h5_niveau_global = 'PREOCCUPANT'
    h5_couleur_global = '[PREOCCUPANT]'
    nb_hopitaux_preoccupants += 1
else:
    h5_niveau_global = 'SATISFAISANT'
    h5_couleur_global = '[SATISFAISANT]'
    nb_hopitaux_satisfaisants += 1

# Compteurs vaccination
nb_zones_critiques = 0
nb_zones_risque = 0
nb_zones_insuffisantes = 0
nb_zones_conformes = 0

if d1_statut_vaccin == 'ZONE CRITIQUE':
    nb_zones_critiques += 1
elif d1_statut_vaccin == 'ZONE A RISQUE':
    nb_zones_risque += 1
elif d1_statut_vaccin == 'ZONE INSUFFISANTE':
    nb_zones_insuffisantes += 1
else:
    nb_zones_conformes += 1

if d2_statut_vaccin == 'ZONE CRITIQUE':
    nb_zones_critiques += 1
elif d2_statut_vaccin == 'ZONE A RISQUE':
    nb_zones_risque += 1
elif d2_statut_vaccin == 'ZONE INSUFFISANTE':
    nb_zones_insuffisantes += 1
else:
    nb_zones_conformes += 1

if d3_statut_vaccin == 'ZONE CRITIQUE':
    nb_zones_critiques += 1
elif d3_statut_vaccin == 'ZONE A RISQUE':
    nb_zones_risque += 1
elif d3_statut_vaccin == 'ZONE INSUFFISANTE':
    nb_zones_insuffisantes += 1
else:
    nb_zones_conformes += 1

if d4_statut_vaccin == 'ZONE CRITIQUE':
    nb_zones_critiques += 1
elif d4_statut_vaccin == 'ZONE A RISQUE':
    nb_zones_risque += 1
elif d4_statut_vaccin == 'ZONE INSUFFISANTE':
    nb_zones_insuffisantes += 1
else:
    nb_zones_conformes += 1

# ============================================================
# === SECTION E+R : RAPPORT COMPLET S2+S3 ====================
# ============================================================

if __name__ == '__main__':
    print("=" * 75)
    print("  RAPPORT D'ETAT SANITAIRE — SYSTEME DE SANTE CONGO")
    print("  Projet Sante Publique / Akieni Academy — Semaine 3")
    print("  Date : 15 janvier 2026")
    print("=" * 75)
    print()

    # --- SECTION F : STOCKS MEDICAMENTS ---
    print("-" * 75)
    print("  SECTION F : CLASSIFICATION DES STOCKS MEDICAMENTS (PNA)")
    print("-" * 75)
    print(f"  {m1_couleur} {m1_nom:<35} | Stock: {m1_qte_disponible:>6} | {m1_statut}")
    print(f"     Action: {m1_action}")
    print(f"  {m2_couleur} {m2_nom:<35} | Stock: {m2_qte_disponible:>6} | {m2_statut}")
    print(f"     Action: {m2_action}")
    print(f"  {m3_couleur} {m3_nom:<35} | Stock: {m3_qte_disponible:>6} | {m3_statut}")
    print(f"     Action: {m3_action}")
    print(f"  {m4_couleur} {m4_nom:<35} | Stock: {m4_qte_disponible:>6} | {m4_statut}")
    print(f"     Action: {m4_action}")
    print(f"  {m5_couleur} {m5_nom:<35} | Stock: {m5_qte_disponible:>6} | {m5_statut}")
    print(f"     Action: {m5_action}")
    print()
    print(f"  BILAN STOCK : {nb_ruptures_critiques} rupture(s) critique(s) | {nb_alertes_stock} alerte(s) | {nb_stocks_normaux} normal(aux)")
    if nb_ruptures_critiques > 0:
        print(f"  !! ALERTE PRIORITAIRE : {nb_ruptures_critiques} medicament(s) en RUPTURE CRITIQUE !!")
        print(f"  Transmettre immediatement au Dr. MOUKALA (PNA)")
    print()

    # --- SECTION G : OCCUPATION HOPITAUX ---
    print("-" * 75)
    print("  SECTION G : NIVEAU D'OCCUPATION DES HOPITAUX")
    print("-" * 75)
    print(f"  {h1_couleur_occupation} {h1_nom:<30} | Occup: {h1_taux_occupation:>5.1f}% | {h1_niveau_occupation}")
    print(f"     Action: {h1_action_occupation}")
    print(f"  {h2_couleur_occupation} {h2_nom:<30} | Occup: {h2_taux_occupation:>5.1f}% | {h2_niveau_occupation}")
    print(f"     Action: {h2_action_occupation}")
    print(f"  {h3_couleur_occupation} {h3_nom:<30} | Occup: {h3_taux_occupation:>5.1f}% | {h3_niveau_occupation}")
    print(f"     Action: {h3_action_occupation}")
    print(f"  {h4_couleur_occupation} {h4_nom:<30} | Occup: {h4_taux_occupation:>5.1f}% | {h4_niveau_occupation}")
    print(f"     Action: {h4_action_occupation}")
    print(f"  {h5_couleur_occupation} {h5_nom:<30} | Occup: {h5_taux_occupation:>5.1f}% | {h5_niveau_occupation}")
    print(f"     Action: {h5_action_occupation}")
    print()

    # --- SECTION H : COUVERTURE VACCINALE ---
    print("-" * 75)
    print("  SECTION H : COUVERTURE VACCINALE PAR DEPARTEMENT")
    print("-" * 75)
    print(f"  {d1_couleur_vaccin} {d1_nom:<15} | Taux: {d1_taux_couverture:>5.1f}% | {d1_statut_vaccin}")
    print(f"     Action: {d1_action_vaccin}")
    print(f"  {d2_couleur_vaccin} {d2_nom:<15} | Taux: {d2_taux_couverture:>5.1f}% | {d2_statut_vaccin}")
    print(f"     Action: {d2_action_vaccin}")
    print(f"  {d3_couleur_vaccin} {d3_nom:<15} | Taux: {d3_taux_couverture:>5.1f}% | {d3_statut_vaccin}")
    print(f"     Action: {d3_action_vaccin}")
    print(f"  {d4_couleur_vaccin} {d4_nom:<15} | Taux: {d4_taux_couverture:>5.1f}% | {d4_statut_vaccin}")
    print(f"     Action: {d4_action_vaccin}")
    print()
    print(f"  BILAN VACCINATION : {nb_zones_critiques} critique(s) | {nb_zones_risque} a risque | {nb_zones_insuffisantes} insuffisante(s) | {nb_zones_conformes} conforme(s)")
    print()

    # --- SECTION I : TABLEAU DE BORD MINISTERIEL ---
    print("-" * 75)
    print("  SECTION I : TABLEAU DE BORD — NIVEAU GLOBAL DES HOPITAUX")
    print("-" * 75)
    print(f"  {'HOPITAL':<30} {'OCCUPATION':>12} {'ALERTES':>12} {'NIVEAU GLOBAL':>15}")
    print("  " + "-" * 71)
    print(f"  {h1_nom:<30} {h1_taux_occupation:>6.1f}% {h1_couleur_occupation:>4}  {h1_nb_meds_rupture}R+{h1_nb_meds_alerte}A {h1_couleur_global:>15}")
    print(f"  {h2_nom:<30} {h2_taux_occupation:>6.1f}% {h2_couleur_occupation:>4}  {h2_nb_meds_rupture}R+{h2_nb_meds_alerte}A {h2_couleur_global:>15}")
    print(f"  {h3_nom:<30} {h3_taux_occupation:>6.1f}% {h3_couleur_occupation:>4}  {h3_nb_meds_rupture}R+{h3_nb_meds_alerte}A {h3_couleur_global:>15}")
    print(f"  {h4_nom:<30} {h4_taux_occupation:>6.1f}% {h4_couleur_occupation:>4}  {h4_nb_meds_rupture}R+{h4_nb_meds_alerte}A {h4_couleur_global:>15}")
    print(f"  {h5_nom:<30} {h5_taux_occupation:>6.1f}% {h5_couleur_occupation:>4}  {h5_nb_meds_rupture}R+{h5_nb_meds_alerte}A {h5_couleur_global:>15}")
    print("  " + "-" * 71)
    print(f"  {nb_hopitaux_critiques} hopitaux sur 5 en situation CRITIQUE")
    print(f"  {nb_hopitaux_preoccupants} hopitaux sur 5 en situation PREOCCUPANTE")
    print(f"  {nb_hopitaux_satisfaisants} hopitaux sur 5 en situation SATISFAISANTE")
    print()

    # Recommandation prioritaire
    if nb_hopitaux_critiques >= 3:
        print("  !! RECOMMANDATION PRIORITAIRE !!")
        print("  Mobiliser la reserve nationale PNA")
        print("  Renforcement des equipes medicales dans les zones critiques")
    elif nb_hopitaux_critiques >= 1:
        print("  RECOMMANDATION : Surveillance renforcee des hopitaux critiques")
    else:
        print("  Situation globale sous controle — maintien du suivi standard")
    print()

    # --- SYNTHESE BUDGETAIRE (S2 conserve) ---
    print("-" * 75)
    print("  SYNTHESE BUDGETAIRE")
    print("-" * 75)
    print(f"  Budget total trimestriel : {budget_total_hopitaux:,.2f} FCFA")
    print(f"  Valeur totale du stock   : {valeur_totale_stock:,.2f} FCFA")
    print()

    print("=" * 75)
    print("  FIN DU RAPPORT D'ETAT SANITAIRE — SEMAINE 3")
    print("=" * 75)