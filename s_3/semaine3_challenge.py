# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Challenge : Tableau de Bord Sanitaire Ministeriel
# 5 hopitaux — Rapport pour le Conseil des Ministres
# ============================================================

# ============================================================
# DONNEES DES 5 HOPITAUX
# ============================================================

# CHU Brazzaville
h1_nom = 'CHU Brazzaville'
h1_lits_total = 320
h1_lits_occupes = 298
h1_nb_medecins = 47
h1_nb_meds_rupture = 2
h1_nb_meds_alerte = 2

# Hopital Pointe-Noire
h2_nom = 'Hopital Pointe-Noire'
h2_lits_total = 180
h2_lits_occupes = 143
h2_nb_medecins = 22
h2_nb_meds_rupture = 0
h2_nb_meds_alerte = 1

# Hopital Dolisie
h3_nom = 'Hopital Dolisie'
h3_lits_total = 95
h3_lits_occupes = 91
h3_nb_medecins = 8
h3_nb_meds_rupture = 1
h3_nb_meds_alerte = 2

# Hopital Owando
h4_nom = 'Hopital Owando'
h4_lits_total = 45
h4_lits_occupes = 32
h4_nb_medecins = 3
h4_nb_meds_rupture = 3
h4_nb_meds_alerte = 0

# CMS Impfondo
h5_nom = 'CMS Impfondo'
h5_lits_total = 20
h5_lits_occupes = 19
h5_nb_medecins = 1
h5_nb_meds_rupture = 2
h5_nb_meds_alerte = 1

# ============================================================
# CONSTANTES
# ============================================================

SEUIL_OCCUPATION_CRITIQUE = 95.0
SEUIL_OCCUPATION_ELEVEE = 85.0
SEUIL_OCCUPATION_OPTIMALE = 70.0
COUT_COMMANDE_EXPRESS = 450_000

# ============================================================
# CALCULS TAUX D'OCCUPATION
# ============================================================

h1_taux_occupation = round((h1_lits_occupes / h1_lits_total) * 100, 1)
h2_taux_occupation = round((h2_lits_occupes / h2_lits_total) * 100, 1)
h3_taux_occupation = round((h3_lits_occupes / h3_lits_total) * 100, 1)
h4_taux_occupation = round((h4_lits_occupes / h4_lits_total) * 100, 1)
h5_taux_occupation = round((h5_lits_occupes / h5_lits_total) * 100, 1)

# ============================================================
# CLASSIFICATION NIVEAU OCCUPATION PAR HOPITAL
# ============================================================

# Hopital 1
if h1_taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
    h1_niveau_occup = 'CRI'
    h1_couleur_occup = '[CRI]'
elif h1_taux_occupation > SEUIL_OCCUPATION_ELEVEE:
    h1_niveau_occup = 'ALT'
    h1_couleur_occup = '[ALT]'
elif h1_taux_occupation > SEUIL_OCCUPATION_OPTIMALE:
    h1_niveau_occup = 'OK'
    h1_couleur_occup = '[OK ]'
else:
    h1_niveau_occup = 'SOU'
    h1_couleur_occup = '[SOU]'

# Hopital 2
if h2_taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
    h2_niveau_occup = 'CRI'
    h2_couleur_occup = '[CRI]'
elif h2_taux_occupation > SEUIL_OCCUPATION_ELEVEE:
    h2_niveau_occup = 'ALT'
    h2_couleur_occup = '[ALT]'
elif h2_taux_occupation > SEUIL_OCCUPATION_OPTIMALE:
    h2_niveau_occup = 'OK'
    h2_couleur_occup = '[OK ]'
else:
    h2_niveau_occup = 'SOU'
    h2_couleur_occup = '[SOU]'

# Hopital 3
if h3_taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
    h3_niveau_occup = 'CRI'
    h3_couleur_occup = '[CRI]'
elif h3_taux_occupation > SEUIL_OCCUPATION_ELEVEE:
    h3_niveau_occup = 'ALT'
    h3_couleur_occup = '[ALT]'
elif h3_taux_occupation > SEUIL_OCCUPATION_OPTIMALE:
    h3_niveau_occup = 'OK'
    h3_couleur_occup = '[OK ]'
else:
    h3_niveau_occup = 'SOU'
    h3_couleur_occup = '[SOU]'

# Hopital 4
if h4_taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
    h4_niveau_occup = 'CRI'
    h4_couleur_occup = '[CRI]'
elif h4_taux_occupation > SEUIL_OCCUPATION_ELEVEE:
    h4_niveau_occup = 'ALT'
    h4_couleur_occup = '[ALT]'
elif h4_taux_occupation > SEUIL_OCCUPATION_OPTIMALE:
    h4_niveau_occup = 'OK'
    h4_couleur_occup = '[OK ]'
else:
    h4_niveau_occup = 'SOU'
    h4_couleur_occup = '[SOU]'

# Hopital 5
if h5_taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
    h5_niveau_occup = 'CRI'
    h5_couleur_occup = '[CRI]'
elif h5_taux_occupation > SEUIL_OCCUPATION_ELEVEE:
    h5_niveau_occup = 'ALT'
    h5_couleur_occup = '[ALT]'
elif h5_taux_occupation > SEUIL_OCCUPATION_OPTIMALE:
    h5_niveau_occup = 'OK'
    h5_couleur_occup = '[OK ]'
else:
    h5_niveau_occup = 'SOU'
    h5_couleur_occup = '[SOU]'

# ============================================================
# CLASSIFICATION NIVEAU GLOBAL (conditions composees and/or)
# ============================================================

nb_hopitaux_critiques = 0
nb_hopitaux_preoccupants = 0
nb_hopitaux_satisfaisants = 0
total_ruptures = 0

# Hopital 1
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
total_ruptures += h1_nb_meds_rupture

# Hopital 2
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
total_ruptures += h2_nb_meds_rupture

# Hopital 3
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
total_ruptures += h3_nb_meds_rupture

# Hopital 4
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
total_ruptures += h4_nb_meds_rupture

# Hopital 5
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
total_ruptures += h5_nb_meds_rupture

# BONUS : Cout estimé des commandes urgentes
cout_total_urgent = total_ruptures * COUT_COMMANDE_EXPRESS

# ============================================================
# AFFICHAGE TABLEAU DE BORD
# ============================================================

print('=' * 68)
print('  TABLEAU DE BORD SANITAIRE — MINISTERE DE LA SANTE')
print('  Date : 16 janvier 2026  |  Pour le Conseil des Ministres')
print('=' * 68)
print()
print(f"  {'HOPITAL':<28} {'OCCUPATION':>12} {'ALERTES':>10} {'NIVEAU GLOBAL':>15}")
print('  ' + '-' * 65)
print(f"  {h1_nom:<28} {h1_taux_occupation:>6.1f}% {h1_couleur_occup:>4}  {h1_nb_meds_rupture}R+{h1_nb_meds_alerte}A {h1_couleur_global:>15}")
print(f"  {h2_nom:<28} {h2_taux_occupation:>6.1f}% {h2_couleur_occup:>4}  {h2_nb_meds_rupture}R+{h2_nb_meds_alerte}A {h2_couleur_global:>15}")
print(f"  {h3_nom:<28} {h3_taux_occupation:>6.1f}% {h3_couleur_occup:>4}  {h3_nb_meds_rupture}R+{h3_nb_meds_alerte}A {h3_couleur_global:>15}")
print(f"  {h4_nom:<28} {h4_taux_occupation:>6.1f}% {h4_couleur_occup:>4}  {h4_nb_meds_rupture}R+{h4_nb_meds_alerte}A {h4_couleur_global:>15}")
print(f"  {h5_nom:<28} {h5_taux_occupation:>6.1f}% {h5_couleur_occup:>4}  {h5_nb_meds_rupture}R+{h5_nb_meds_alerte}A {h5_couleur_global:>15}")
print('  ' + '-' * 65)
print(f"  {nb_hopitaux_critiques} hopitaux sur 5 en situation CRITIQUE")
print(f"  {nb_hopitaux_preoccupants} hopitaux sur 5 en situation PREOCCUPANTE")
print(f"  {nb_hopitaux_satisfaisants} hopitaux sur 5 en situation SATISFAISANTE")
print()

# Recommandation conditionnelle
if nb_hopitaux_critiques >= 3:
    print('  !! RECOMMANDATION PRIORITAIRE !!')
    print('  Mobiliser la reserve nationale PNA')
    print('  Renforcement des equipes medicales dans les zones critiques')
elif nb_hopitaux_critiques >= 1:
    print('  RECOMMANDATION : Surveillance renforcee des hopitaux critiques')
else:
    print('  Situation globale sous controle — maintien du suivi standard')

print()
print(f'  BONUS : {total_ruptures} ruptures de stock identifiees')
print(f'  Cout estime commandes express : {cout_total_urgent:,} FCFA')
print('=' * 68)