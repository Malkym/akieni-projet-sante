# Projet Sante Publique — Akieni Academy

## Description

Ce projet vise a modeliser et analyser le systeme de sante du Congo a travers un module Python centralise. Il permet de suivre les indicateurs cles de performance (KPIs) des etablissements de sante, gerer les stocks de medicaments essentiels, et generer des rapports comparatifs pour les decideurs du Ministere de la Sante.

Le fichier `sante_variables.py` constitue le coeur architectural du projet. Il centralise toutes les constantes metier, les variables des hopitaux et des medicaments, ainsi que les calculs d'initialisation des indicateurs de sante publique.

## Structure du Projet
projet_sante/
├── sante_variables.py          # Module fondateur (constantes + variables + KPIs)
├── semaine2_exercice1_sante.py # Fiche patient CHU Brazzaville
├── semaine2_exercice2_sante.py # KPIs sanitaires OMS
├── semaine2_challenge.py       # Rapport comparatif 3 hopitaux du Pool
└── README.md                   # Ce fichier

## Fonctionnalites

- **Constantes nationales** : Taux de change, seuils OMS, liste des 12 departements du Congo
- **5 hopitaux representatifs** : CHU Brazzaville, Hopital General Pointe-Noire, Hopital de Dolisie, Hopital de District Owando, Centre de Sante de Impfondo
- **5 medicaments essentiels** : Artemether-Lumefantrine, Amoxicilline, Paracetamol, SRO, Vaccin Antipaludeen RTS,S
- **KPIs automatiques** : Densite medicale, taux d'occupation, taux de mortalite, valeur du stock
- **Alertes critiques** : Detection automatique des situations hors normes OMS
- **Rapport imprimable** : Tableau de bord complet executable directement

## Execution

```bash
python sante_variables.py
```

## Auteur
Equipe Data — Akieni Academy, Semaine 2 (2026)
Coordonnateur : Abdias MONTSONGO

---

## Recapitulatif des points cles respectes

| Contrainte | Respect |
|------------|---------|
| Constantes OMS en MAJUSCULES | OK |
| Montants FCFA en float | OK |
| Comptages en int | OK |
| Prefixes h1_, h2_, m1_, m2_, etc. | OK |
| Fichier executable directement | OK |
| README de 3-5 lignes minimum | OK |
| 5 hopitaux complets | OK |
| 5 medicaments complets | OK |
| Calculs d'initialisation | OK |
| Rapport structure | OK |