# 🎒 Projet NSI : Pokédex en Python

**Description :** Un gestionnaire de base de données de Pokémon développé en Python. Ce projet permet de consulter, rechercher, filtrer un Pokédex via une interface interactive en console.

---

### Aperçu du Programme

```
====================================================
  _____   ____  _  ________ _____  ________  __ 
 |  __ \ / __ \| |/ /  ____|  __ \|  ____\ \/ / 
 | |__) | |  | | ' /| |__  | |  | | |__   \  /  
 |  ___/| |  | |  < |  __| | |  | |  __|   > <   
 | |    | |__| | . \| |____| |__| | |____ /  /\ 
 |_|     \____/|_|\_\______|_____/|______/_/ \_\

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

## ✅ Fonctionnalités Implémentées

Voici l'état d'avancement par rapport au cahier des charges initial :

- [x] **Structure de données** : Tableau (50 Pokémon inclus par défaut) dans un fichier texte pour les sauvegardes.
- [x] **Affichage** : Fonction de formatage propre pour chaque Pokémon
- [x] **Recherches avancées** : Par numéro, nom, type, et statistiques
- [x] **Filtrage dynamique** : Système de recherche par Minimum/Maximum sur les PV, Attaque, etc.
- [x] **Ajout Dynamique** : Formulaire de création d'un nouveau Pokémon avec validation des données
- [x] **Persistance des informations** : Sauvegarde et chargement automatique via un fichier `pokedex.txt`
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

##Dépendances nécessaires :
- [x] git
- [x] un terminal python 

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/THE-lulu57/Pokedex.git
   ```

2. **Lancer le programme :**
   ```bash
   cd Pokedex
   python pokedex.py
   ```

3. Le menu principal s'affichera avec le logo ASCII et vous pourrez commencer à explorer votre Pokédex !

---

## 🔥 Points Forts du Code

### 💾 Persistance des données

Ce programme utilise les fonctions `sauvegarder()` et `charger()` pour lire et écrire dans `pokedex.txt`. Vos nouveaux Pokémon sont donc conservés !

### 🛡️ Validation de saisie

Grâce à la fonction `demander_entier()`, le programme ne plante jamais si vous entrez du texte à la place d'un nombre :


### 🔍 Filtrage Avancé

Le système de filtrage permet de trouver en un clin d'œil les Pokémon les plus puissants (ex: "Afficher tous les Pokémon ayant plus de 80 en Attaque").
Au lieu de créer 5 ou 6 fonctions différentes pour filtrer par PV, par Attaque ou par Défense, j'ai développé une fonction de filtrage universelle :
Python
```
def filtrage(Pokemon, max_min, quoi, valeur):
```
---

## 📝 Licence

Ce projet est développé dans un cadre éducatif (NSI). Par Lucas et Axel
