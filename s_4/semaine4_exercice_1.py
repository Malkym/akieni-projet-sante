# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 4 — Exercice 1 : Surveillance Epidemique Mpox
# Congo-Brazzaville 2025 — Centre des Operations d'Urgence (COUSP)
# Notions : boucle for, conditions, accumulateurs
# ============================================================

# Initialisation des accumulateurs
total_suspects = 0
total_confirmes = 0
total_deces = 0
total_actifs = 0
zones_vertes = 0
zones_jaunes = 0
zones_oranges = 0
zones_rouges = 0
nb_districts = 9

print('=' * 50)
print('SURVEILLANCE EPIDEMIQUE MPOX – CONGO 2025')
print('=' * 50)

# Boucle sur les 9 districts
for i in range(1, nb_districts + 1):
    print(f'--- District {i} ---')
    
    # Saisie des données
    nom_district = input('Nom du district : ')
    suspects = int(input('Cas suspects : '))
    confirmes = int(input('Cas confirmes : '))
    deces = int(input('Deces : '))
    
    # Calculs
    cas_actifs = confirmes - deces  # TODO 1
    
    if confirmes > 0:
        letalite = (deces / confirmes) * 100  # TODO 2
    else:
        letalite = 0
    
    # Classification alerte (du plus restrictif au plus large)
    if confirmes >= 10:  # TODO 3
        alerte = 'ROUGE'
        zones_rouges += 1  # TODO 4
    elif confirmes >= 5:  # TODO 3
        alerte = 'ORANGE'
        zones_oranges += 1  # TODO 4
    elif confirmes >= 2:  # TODO 3
        alerte = 'JAUNE'
        zones_jaunes += 1  # TODO 4
    else:
        alerte = 'VERT'
        zones_vertes = zones_vertes + 1  # TODO 5 (ou zones_vertes += 1)
    
    # Accumulation des totaux
    total_suspects = total_suspects + suspects  # TODO 6
    total_confirmes = total_confirmes + confirmes  # TODO 6
    total_deces = total_deces + deces  # TODO 7
    total_actifs = total_actifs + cas_actifs  # TODO 8
    
    # Affichage par district
    print(f'Alerte : {alerte}')
    print(f'Actifs : {cas_actifs}')
    print(f'Letalite : {round(letalite, 1)} %')
    print()

# Affichage rapport national
print('=' * 50)
print('RAPPORT NATIONAL MPOX 2025')
print('=' * 50)
print(f'Districts analyses : {nb_districts}')
print(f'Total suspects : {total_suspects}')
print(f'Total confirmes : {total_confirmes}')
print(f'Total deces : {total_deces}')
print(f'Total cas actifs : {total_actifs}')
print(f'Zones VERTES : {zones_vertes}')
print(f'Zones JAUNES : {zones_jaunes}')
print(f'Zones ORANGES : {zones_oranges}')
print(f'Zones ROUGES : {zones_rouges}')
print('=' * 50)