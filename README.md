# 🎒 Projet NSI : Pokédex en Ligne de Commande (CLI)

**Description :** Un gestionnaire de base de données de Pokémon développé en Python. Ce projet permet de consulter, rechercher, filtrer et enrichir un Pokédex via une interface interactive en console.

---

## 🎯 Objectifs du Projet

Ce projet a été réalisé dans le cadre du cours de NSI. L'objectif était de manipuler des structures de données complexes (tableaux de tableaux) et de créer une interface utilisateur robuste.

---

## ✅ Fonctionnalités Implémentées

Voici l'état d'avancement par rapport au cahier des charges initial :

- [x] **Structure de données** : Tableau de tableaux (50 Pokémon inclus par défaut)
- [x] **Affichage** : Fonction de formatage propre pour chaque Pokémon
- [x] **Recherches avancées** : Par numéro, nom, type, et statistiques
- [x] **Filtrage dynamique** : Système de recherche par Minimum/Maximum sur les PV, Attaque, etc.
- [x] **Ajout Dynamique** : Formulaire de création d'un nouveau Pokémon avec validation des données
- [x] **Persistance (Bonus ⭐)** : Sauvegarde et chargement automatique via un fichier `pokedex.txt`
- [x] **Sécurité** : Gestion des erreurs de saisie (évite les crashs si l'utilisateur ne tape pas un chiffre)

---

## 📊 Structure d'une Donnée

Chaque Pokémon est stocké sous forme de liste avec l'organisation suivante :

| Indice | Information | Exemple       |
|--------|-------------|---------------|
| 0      | Numéro      | 1             |
| 1      | Nom         | "Bulbizarre"  |
| 2      | Type 1      | "Plante"      |
| 3      | Type 2      | "Poison"      |
| 4      | PV          | 45            |
| 5      | Attaque     | 49            |
| 6      | Défense     | 49            |
| 7      | Vitesse     | 45            |
| 8      | Génération  | 1             |

---

## 🛠️ Installation et Utilisation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/votre-pseudo/pokedex-nsi.git
   cd pokedex-nsi
   ```

2. **Lancer le programme :**
   ```bash
   python pokedex.py
   ```

### Aperçu du Menu Principal

```
====================================================
                  MENU DU POKEDEX
    0 - Quitter
    1 - Lister tout
    2 - Rechercher
    3 - Ajouter un Pokémon
    4 - Filtrer
====================================================
```

---

## 🔥 Points Forts du Code

### 💾 Persistance des données

Contrairement à un Pokédex classique qui s'efface à la fermeture, ce programme utilise les fonctions `sauvegarder()` et `charger()` pour lire et écrire dans `pokedex.txt`. Vos nouveaux Pokémon sont donc conservés !

### 🛡️ Validation de saisie

Grâce à la fonction `demander_entier()`, le programme ne plante jamais si vous entrez du texte à la place d'un nombre :

```python
def demander_entier(message):
```

### 🔍 Filtrage Avancé

Le système de filtrage permet de trouver en un clin d'œil les Pokémon les plus puissants (ex: "Afficher tous les Pokémon ayant plus de 80 en Attaque").

---

## 📝 Licence

Ce projet est développé dans un cadre éducatif (NSI). Par Lucas et Axel
