def sauvegarder(Pokemon):
    f = open("pokedex.txt", "w", encoding="utf-8")
    for pkm in Pokemon:
        ligne = ""
        for elem in pkm:
            ligne += str(elem) + ","
        ligne = ligne[:-1]     # enlever la dernière virgule
        f.write(ligne + "\n")
    f.close()

def charger():
    Pokemon = []

    f = open("pokedex.txt", "r", encoding="utf-8")
    contenu = f.read().splitlines()
    f.close()

    for ligne in contenu:
        if ligne == "":      #  évite les lignes vides sinon error
            continue

        valeurs = ligne.split(",")
        pkm = [
            int(valeurs[0]),
            valeurs[1],
            valeurs[2],
            valeurs[3],
            int(valeurs[4]),
            int(valeurs[5]),
            int(valeurs[6]),
            int(valeurs[7]),
            int(valeurs[8])
        ]
        Pokemon.append(pkm)

    return Pokemon

def statistiques(Pokemon, type_calcul, quoi):
    quoi = int(quoi)
    type_calcul = int(type_calcul)
    
    # On définit le nom de la stat
    nom_stat = ""
    if quoi == 4:
        nom_stat = "PV"
    elif quoi == 5:
        nom_stat = "Attaque"
    elif quoi == 6:
        nom_stat = "Défense"
    elif quoi == 7:
        nom_stat = "Vitesse"
    elif quoi == 8:
        nom_stat = "Génération"

    if type_calcul == 3: # MOYENNE
        somme = 0
        for pkm in Pokemon:
            somme += pkm[quoi]
        
        if len(Pokemon) > 0:
            moyenne = somme / len(Pokemon)
            print("-" * 50)
            print("Moyenne des", nom_stat, "de tous les Pokémon :", round(moyenne, 2)) 
            print("-" * 50)
        else:
            print("Erreur : Pokédex vide.")

    else: # MAX (1) ou MIN (2)
        # On prend le premier de la liste comme référence
        pkm_retenu = Pokemon[0]

        for pkm in Pokemon:
            valeur_actuelle = pkm[quoi]
            valeur_retenue = pkm_retenu[quoi]

            if type_calcul == 1: 
                if valeur_actuelle > valeur_retenue:
                    pkm_retenu = pkm
            
            elif type_calcul == 2: 
                if valeur_actuelle < valeur_retenue:
                    pkm_retenu = pkm

        if type_calcul == 1:
            intro = "MAXIMUM"
        else:
            intro = "MINIMUM"

        print("-" * 50)
        print("Le Pokémon avec le", intro, "de", nom_stat, "est :")
        recherche(pkm_retenu)

def recherche(pkm):
    print("Numéro :", pkm[0],
          "| Nom :", pkm[1],
          "| Types :", pkm[2], "/", pkm[3])
    print("PV :", pkm[4],
          "| Atq :", pkm[5],
          "| Déf :", pkm[6],
          "| Vit :", pkm[7],
          "| Gén :", pkm[8])
    print("-" * 50)

def demander_entier(message): ## -> pour vérifier si l'utilisateur met bien un chiffre dans la case sinon ca crash 
    while True:
        valeur = input(message)
        if valeur.isdigit():
            return int(valeur)  
        print("Erreur : Vous devez entrer uniquement des chiffres.")

def filtrage(Pokemon, max_min, quoi, valeur):
    quoi = int(quoi)
    valeur = int(valeur)
    if quoi in [1, 5, 6, 7, 8, 9]:
        if max_min == 1:
            for pkm in Pokemon:
                if pkm[quoi -1] <= valeur:
                    recherche(pkm) 

        elif max_min == 2:
            quoi = int(quoi)
            valeur = int(valeur)
            for pkm in Pokemon:
                if pkm[quoi -1] >= valeur:
                    recherche(pkm) 
        else:
            print("Choix min/max invalide.")

    else:
        print("Utilisez Numéro, PV, Attaque, Défense, Vitesse ou Génération.")

def pokedex():

    Pokemon = charger()

    if Pokemon == []:
        # Si le fichier était vide → on remet les Pokémon de base
        Pokemon = [[1, "Bulbizarre", "Plante", "Poison", 45, 49, 49, 45, 1],
                [2, "Herbizarre", "Plante", "Poison", 60, 62, 63, 60, 1],
                [3, "Florizarre", "Plante", "Poison", 80, 82, 83, 80, 1],
                [4, "Salamèche", "Feu", "None", 39, 52, 43, 65, 1],
                [5, "Reptincel", "Feu", "None", 58, 64, 58, 80, 1],
                [6, "Dracaufeu", "Feu", "Vol", 78, 84, 78, 100, 1],
                [7, "Carapuce", "Eau", "None", 44, 48, 65, 43, 1],
                [8, "Carabaffe", "Eau", "None", 59, 63, 80, 58, 1],
                [9, "Tortank", "Eau", "None", 79, 83, 100, 78, 1],
                [10, "Chenipan", "Insecte", "None", 45, 30, 35, 45, 1],
                [11, "Chrysacier", "Insecte", "None", 50, 20, 55, 30, 1],
                [12, "Papilusion", "Insecte", "Vol", 60, 45, 50, 70, 1],
                [13, "Aspicot", "Insecte", "Poison", 40, 35, 30, 50, 1],
                [14, "Coconfort", "Insecte", "Poison", 45, 25, 50, 35, 1],
                [15, "Dardargnan", "Insecte", "Poison", 65, 80, 40, 75, 1],
                [16, "Roucool", "Normal", "Vol", 40, 45, 40, 56, 1],
                [17, "Roucoups", "Normal", "Vol", 63, 60, 55, 71, 1],
                [18, "Roucarnage", "Normal", "Vol", 83, 80, 75, 91, 1],
                [19, "Rattata", "Normal", "None", 30, 56, 35, 72, 1],
                [20, "Rattatac", "Normal", "None", 55, 81, 60, 97, 1],
                [21, "Piafabec", "Normal", "Vol", 40, 60, 30, 70, 1],
                [22, "Rapasdepic", "Normal", "Vol", 65, 90, 65, 100, 1],
                [23, "Abo", "Poison", "None", 35, 60, 44, 55, 1],
                [24, "Arbok", "Poison", "None", 60, 85, 69, 80, 1],
                [25, "Pikachu", "Électrik", "None", 35, 55, 30, 90, 1],
                [26, "Raichu", "Électrik", "None", 60, 90, 55, 100, 1],
                [27, "Sabelette", "Sol", "None", 50, 75, 85, 40, 1],
                [28, "Sablaireau", "Sol", "None", 75, 100, 110, 65, 1],
                [29, "Nidoran♀", "Poison", "None", 55, 47, 52, 41, 1],
                [30, "Nidorina", "Poison", "None", 70, 62, 67, 56, 1],
                [31, "Nidoqueen", "Poison", "Sol", 90, 82, 87, 76, 1],
                [32, "Nidoran♂", "Poison", "None", 46, 57, 40, 50, 1],
                [33, "Nidorino", "Poison", "None", 61, 72, 57, 65, 1],
                [34, "Nidoking", "Poison", "Sol", 81, 92, 77, 85, 1],
                [35, "Mélofée", "Fée", "None", 70, 45, 48, 35, 1],
                [36, "Mélodelfe", "Fée", "None", 95, 70, 73, 60, 1],
                [37, "Goupix", "Feu", "None", 38, 41, 40, 65, 1],
                [38, "Feunard", "Feu", "None", 73, 76, 75, 100, 1],
                [39, "Rondoudou", "Normal", "Fée", 115, 45, 20, 20, 1],
                [40, "Grodoudou", "Normal", "Fée", 140, 70, 45, 45, 1],
                [41, "Nosferapti", "Poison", "Vol", 40, 45, 35, 55, 1],
                [42, "Nosferalto", "Poison", "Vol", 75, 80, 70, 90, 1],
                [43, "Mystherbe", "Plante", "None", 45, 50, 55, 30, 1],
                [44, "Ortide", "Plante", "Poison", 60, 65, 70, 40, 1],
                [45, "Rafflesia", "Plante", "Poison", 75, 80, 85, 50, 1],
                [46, "Paras", "Insecte", "Plante", 35, 70, 55, 25, 1],
                [47, "Parasect", "Insecte", "Plante", 60, 95, 80, 30, 1],
                [48, "Mimitoss", "Insecte", "Poison", 60, 55, 50, 45, 1],
                [49, "Aéromite", "Insecte", "Poison", 70, 65, 60, 90, 1],
                [50, "Taupiqueur", "Sol", "None", 10, 55, 25, 95, 1]]
    print("====================================================")
    print(r"  _____   ____  _  ________ _____  ________  __ ")
    print(r" |  __ \ / __ \| |/ /  ____|  __ \|  ____\ \/ / ")
    print(r" | |__) | |  | | ' /| |__  | |  | | |__   \  /  ")
    print(r" |  ___/| |  | |  < |  __| | |  | |  __|   > <   ")
    print(r" | |    | |__| | . \| |____| |__| | |____ /  /\ ")
    print(r" |_|     \____/|_|\_\______|_____/|______/_/ \_\\")
    print("")

    while True:
        print("====================================================")
        print("                  MENU DU POKEDEX")        
        print("    0 - Quitter")
        print("    1 - Lister tout")
        print("    2 - Rechercher")
        print("    3 - Ajouter un Pokémon") 
        print("    4 - Filtrer") 
        print("    5 - Statistiques")
       
        choix = input("Votre choix : ") 
        print("-" * 50)
       
        if choix == "0":
            print("Fermeture du Pokédex. Au revoir !")
            break

        elif choix == "1":
            for pkm in Pokemon:
                recherche(pkm)

        elif choix == "2":
            print("Rechercher par :")
            print("    1 - Son Numéro")
            print("    2 - Son Nom")
            print("    3 - Son Type")
            print("    4 - Ses PV")
            print("    5 - Ses Dégats")
            print("    6 - Sa Défense")
            print("    7 - Sa Vitesse")
            print("    8 - Sa Génération")            
            critere = input("Choix : ") # critère -> choix utilisateur pour les recherches
            print("-" * 50)
            
            trouve = False  # Variable pour savoir si on a trouvé quelque chose

            if critere == "1": # Numéro
                valeur = demander_entier("Numéro cherché : ")
                print("-" * 50)
                for pkm in Pokemon:
                    if pkm[0] == valeur:
                        recherche(pkm)
                        trouve = True

            elif critere == "2": # Nom
                valeur = input("Nom cherché : ").lower()    ## .lower() -> pour trouver même si on écrit en minuscule
                print("-" * 50)
                for pkm in Pokemon:
                    if pkm[1].lower() == valeur: 
                        recherche(pkm)
                        trouve = True

            elif critere == "3": # Type
                valeur = input("Type cherché : ").lower()
                print("-" * 50)
                for pkm in Pokemon:
                    if pkm[2].lower() == valeur or pkm[3].lower() == valeur:
                        recherche(pkm)
                        trouve = True
                
                if not trouve:    ## Si aucun pokemon du type find -> lister tt les types dispo (primaire ou secondaire)
                    print("Aucun Pokémon de ce type. Types disponibles :")
                    types_dispo = set()
                    for pkm in Pokemon:
                        types_dispo.add(pkm[2])
                        if pkm[3] != "None":
                            types_dispo.add(pkm[3])
                    for t in sorted(types_dispo):
                        print(" -", t)
                    trouve = True 

            
            elif critere in ["4", "5", "6", "7", "8"]:   # (PV, Att, Def, Vit) car mm logique de recherche
                valeur = demander_entier("Valeur cherchée : ")
                print("-" * 50)
                
                index_recherche = 0
                if critere == "4": index_recherche = 4 # PV
                if critere == "5": index_recherche = 5 # Attaque
                if critere == "6": index_recherche = 6 # Défense
                if critere == "7": index_recherche = 7 # Vitesse
                if critere == "8": index_recherche = 8 # Generation

                for pkm in Pokemon:
                    if pkm[index_recherche] == valeur:
                        recherche(pkm)
                        trouve = True
            
            else:
                print("Choix de recherche invalide.")
                print("-" * 50)
                trouve = True 

                                
            if not trouve:  # Message si rien trouvé dans tt le pokedex sinon ca return menu sans rien faire
                print("Aucun résultat ne correspond à votre recherche.")

        elif choix == "3":
            print("\n=== AJOUTER UN POKÉMON V1 === ")
            print()
            ajout_num = demander_entier("Numéro : ")
            
            # Vérification si num existe deja
            existe = False
            for pkm in Pokemon:
                if pkm[0] == ajout_num:
                    existe = True
            
            if existe == True:
                print("-" * 50)
                print("Erreur : Ce numéro de Pokémon existe déjà !")
                print("-" * 50)
            else:
                ajout_nom = input("Nom : ")
                ajout_type1 = input("Type primaire : ")
                ajout_type2 = input("Type secondaire : ")
                ajout_pv = demander_entier("PV : ")
                ajout_att = demander_entier("Attaque : ")
                ajout_def = demander_entier("Défense : ")
                ajout_speed = demander_entier("Vitesse : ")
                ajout_gen = demander_entier("Génération : ")

                nouveau_pkm = [ajout_num, ajout_nom, ajout_type1, ajout_type2, 
                               ajout_pv, ajout_att, ajout_def, ajout_speed, ajout_gen]
                
                Pokemon.append(nouveau_pkm)
                sauvegarder(Pokemon)
                print("-" * 50)
                print("Pokémon ajouté avec succès !")
                print()
                print("FERMETURE DU MODULE D'AJOUT...")
                print("Ce Pokémon a été ajouté avec succès !")
                recherche(nouveau_pkm)

        elif choix == "4":
            print("Filtrer par :")
            print("    1 - Le Minimum")
            print("    2 - Le Maximum")
            max_min = demander_entier("Choix : ")
            print("-" * 50)
            print("Pour quel paramètre de votre Pokémon ? : ")
            print("    1 - Son Numéro")
            print("    5 - Ses PV")
            print("    6 - Ses Dégats")
            print("    7 - Sa Défense")
            print("    8 - Sa Vitesse")
            print("    9 - Sa Génération")
            quoi = demander_entier("Choix : ")
            print("-" * 50)
            valeur = demander_entier("Pour quelle valeur de départ ? : ")
            print("-" * 50)

            filtrage(Pokemon, max_min, quoi, valeur)

        elif choix == "5":
            print("Quel type de statistique ?")
            print("    1 - Le Maximum (Le plus fort)")
            print("    2 - Le Minimum (Le plus faible)")
            print("    3 - La Moyenne")
            type_calcul = demander_entier("Choix : ")
            
            if type_calcul not in [1, 2, 3]:
                print("Choix invalide.")
                continue

            print("-" * 50)
            print("Sur quelle donnée ?")
            print("    4 - PV")
            print("    5 - Attaque")
            print("    6 - Défense")
            print("    7 - Vitesse")
            print("    8 - Génération")
            quoi = demander_entier("Choix : ")

            if quoi in [4, 5, 6, 7, 8]:
                statistiques(Pokemon, type_calcul, quoi)
            else:
                print("Choix invalide (choisissez entre 4 et 8).")

        else:
            if choix not in ["1", "2", "3", "4", "5"]: # Petit fix ici pour inclure le 5
                 print("Veuillez choisir un chiffre entre 0 et 5.")
    
pokedex()     
