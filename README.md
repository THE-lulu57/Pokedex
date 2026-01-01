### 🎒 Projet NSI : Pokédex en Python

====================================================
  _____   ____  _  ________ _____  ________  __ 
 |  __ \ / __ \| |/ /  ____|  __ \|  ____\ \/ / 
 | |__) | |  | | ' /| |__  | |  | | |__   \  /  
 |  ___/| |  | |  < |  __| | |  | |  __|   > <   
 | |    | |__| | . \| |____| |__| | |____ /  /\ 
 |_|     \____/|_|\_\______|_____/|______/_/ \_\\

====================================================

✅ Fonctionnalités Implémentées

Voici l'état d'avancement par rapport au cahier des charges initial :

[x] Structure de données : Tableau (50 Pokémon inclus par défaut), dans un fichier texte pour les sauvegardes.

[x] Affichage : Fonction de formatage propre pour chaque Pokémon.

[x] Recherches avancées : Par numéro, nom, type, et statistiques.

[x] Filtrage dynamique : Système de recherche par Minimum/Maximum sur les PV, Attaque, etc.

[x] Ajout Dynamique : Formulaire de création d'un nouveau Pokémon avec validation des données.

[x] Persistance des données : Sauvegarde et chargement automatique via un fichier pokedex.txt.

[x] Sécurité : Gestion des erreurs de saisie (évite les crashs si l'utilisateur ne tape pas un chiffre).

📊 Structure d'une Donnée

Chaque Pokémon est stocké sous forme de liste avec l'organisation suivante :
Indice	Information	Exemple
0	Numéro	1
1	Nom	"Bulbizarre"
2	Type 1	"Plante"
3	Type 2	"Poison"
4	PV	45
5	Attaque	49
6	Défense	49
7	Vitesse	45
8	Génération	1

Le projet final diffère légèrement des consignes initiales. Plutôt que de multiplier les petites fonctions similaires, j'ai choisi d'optimiser la structure pour rendre le code plus évolutif et robuste.
🔄 Mapping des fonctions (Consignes vs Réalité)
Objectif Consigne	Fonction demandée	Ma solution (Implémentation)	Note
Afficher un Pokémon	afficher_pokemon()	recherche(pkm)	Formatage plus compact et visuel.
Lister tout	afficher_tous()	Intégré dans le menu (Option 1)	Utilise la boucle for pkm in Pokemon.
Recherche par PV min	filtrer_par_pv_min()	filtrage(...)	Amélioré : Une seule fonction gère Min, Max et toutes les stats.
Saisie sécurisée	Non demandé	demander_entier()	Évite que le programme plante si l'utilisateur se trompe.
Persistance	Bonus	sauvegarder() / charger()	Les données sont écrites en .txt, pas seulement en mémoire vive.
🧠 Focus sur l'optimisation du Filtrage

Au lieu de créer 5 ou 6 fonctions différentes pour filtrer par PV, par Attaque ou par Défense, j'ai développé une fonction de filtrage universelle :

def filtrage(Pokemon, max_min, quoi, valeur):

Aperçu du Menu Principal

====================================================
                  MENU DU POKEDEX
    0 - Quitter
    1 - Lister tout
    2 - Rechercher
    3 - Ajouter un Pokémon
    4 - Filtrer
====================================================

🔥 Points Forts du Code :

💾 Persistance des données :

Ce programme utilise les fonctions sauvegarder() et charger() pour lire et écrire dans pokedex.txt. Vos nouveaux Pokémon sont donc conservés !
La structure dans le fichier texte est la suivante : 
Numéro du Pokémon,Nom,Type 1,Type 2,PV,Attaque,Défense,Vitesse,Génération

🛡️ Validation de saisie :

Grâce à la fonction demander_entier(), le programme ne plante jamais si vous entrez du texte à la place d'un nombre.

🛠️ Installation et Utilisation

    Cloner le dépôt :
    Bash

git clone https://github.com/votre-pseudo/pokedex-nsi.git

Lancer le programme :
Bash

    python pokedex.py
