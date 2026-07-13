# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 2 : Triage Patient Urgences CHU Brazzaville
# Notions S2 : variables, types, input(), f-strings, conversion
# Notions S3 : if/elif/else, conditions composees or/and/not
# Protocole Manchester adapte — DSS Congo 2026
# ============================================================

print('=== SYSTEME DE TRIAGE — URGENCES CHU BRAZZAVILLE ===')
print('Protocole Manchester adapte — DSS Congo 2026')
print()

# --- SAISIE DES DONNEES PATIENT ---
nom_patient = input('Nom du patient : ')
age_patient = int(input('Age (annees) : '))
temperature = float(input('Temperature (degres C, ex: 38.4) : '))
spo2 = float(input('Saturation O2 en % (ex: 96.0) : '))
tension_syst = int(input('Tension systolique en mmHg (ex: 135) : '))
douleur = int(input('Douleur /10 (0=aucune, 10=insupportable) : '))

# --- VALIDATION DES PLAGES ---
erreur = False

if temperature < 35.0 or temperature > 43.0:
    print('ERREUR : Valeur de temperature impossible — verifier la saisie')
    erreur = True

if spo2 < 50.0 or spo2 > 100.0:
    print('ERREUR : SpO2 hors plage — verifier le capteur')
    erreur = True

if tension_syst < 50 or tension_syst > 250:
    print('ERREUR : Tension hors plage — verifier le brassard')
    erreur = True

if douleur < 0 or douleur > 10:
    print('ERREUR : Douleur doit etre entre 0 et 10')
    erreur = True

if age_patient < 0 or age_patient > 120:
    print('ERREUR : Age invalide — verifier la saisie')
    erreur = True

# --- TRIAGE (conditions composees avec OR) ---
# Niveau 1 : IMMEDIAT — au moins UNE condition critique suffit
if temperature > 39.5 or spo2 < 90 or tension_syst > 180:
    niveau_triage = '1 — IMMEDIAT'
    couleur_triage = '[ROUGE]'
    delai_pec = '0 minute'
    action_triage = 'Medecin present immediatement — code ROUGE active'
    motif_principal = f'Temperature {temperature}C > seuil 39.5C' if temperature > 39.5 else \
                     f'SpO2 {spo2}% < seuil 90%' if spo2 < 90 else \
                     f'Tension {tension_syst}mmHg > seuil 180'

# Niveau 2 : URGENT
elif temperature > 38.5 or spo2 < 94 or tension_syst > 140:
    niveau_triage = '2 — URGENT'
    couleur_triage = '[ORANGE]'
    delai_pec = '< 10 minutes'
    action_triage = 'Appel medecin senior'
    motif_principal = f'Temperature {temperature}C > seuil 38.5C' if temperature > 38.5 else \
                     f'SpO2 {spo2}% < seuil 94%' if spo2 < 94 else \
                     f'Tension {tension_syst}mmHg > seuil 140'

# Niveau 3 : URGENT DIFFERE
elif temperature > 37.5 or douleur > 6:
    niveau_triage = '3 — URGENT DIFFERE'
    couleur_triage = '[JAUNE]'
    delai_pec = '< 30 minutes'
    action_triage = 'Infirmier — surveillance'
    motif_principal = f'Temperature {temperature}C > seuil 37.5C' if temperature > 37.5 else \
                     f'Douleur {douleur}/10 > seuil 6'

# Niveau 4 : MOINS URGENT (cas par defaut)
else:
    niveau_triage = '4 — MOINS URGENT'
    couleur_triage = '[VERT]'
    delai_pec = '< 120 minutes'
    action_triage = 'File d\'attente standard'
    motif_principal = 'Tous les parametres sont normaux'

# --- AFFICHAGE FICHE TRIAGE ---
print()
print('=' * 55)
print(f'RESULTAT TRIAGE — {nom_patient.upper()}')
print('=' * 55)
print('PARAMETRES VITAUX')
print(f'  Temperature : {temperature}C     [{"ANORMAL" if temperature > 37.5 else "NORMAL"}]')
print(f'  Saturation O2 : {spo2}%     [{"ANORMAL" if spo2 < 94 else "NORMAL"}]')
print(f'  Tension : {tension_syst}mmHg     [{"ANORMAL" if tension_syst > 140 else "NORMAL"}]')
print(f'  Douleur : {douleur}/10     [{"ANORMAL" if douleur > 3 else "NORMAL"}]')
print()
print(f'NIVEAU DE TRIAGE : {niveau_triage}')
print(f'COULEUR : {couleur_triage}')
print(f'PRISE EN CHARGE : {delai_pec}')
print(f'ACTION : {action_triage}')
print(f'Motif principal : {motif_principal}')
print('=' * 55)