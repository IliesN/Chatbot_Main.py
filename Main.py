import Core
import time
while True:   # Répeter tant que la boucle est Vrai
    print("Menu principal:")  #affiche le menu pricipal 
    print("1. Afficher la liste des mots les moins importants dans le corpus de documents.")
    print("2. Afficher les mots ayant le score TD-IDF le plus élevé.")
    print("3. Indiquer les mots les plus répétés par le président Chirac hormis les mots dits « Non importants ».")
    print("4. Indiquer les noms des présidents qui ont parlé de la « Nation »")
    print("5. Indiquer le premier président à parler du climat et/ou de l’écologie")
    print("6. Hormis les mots dits «non importants», quel(s) est (sont) le(s) mot(s) que tous les présidents ont évoqués.")
    choix = int(input("Choisissez un nombre entre 1 et 6 : ")) #Demande à l'utilisateur de chosir un nombre entre 1 et 6

    if choix == 1:
        print("Question 1 sélectionnée. Veuillez patienter...")
        print("La liste des mots les moins importants sont :", Core.ex1())                 #appel de la fonction Core.ex1
        time.sleep(5) # 5 secondes après l'exécution de la condition, retourne le menu principal
    elif choix == 2:
        print("Question 2 sélectionnée. Veuillez patienter...")
        print("La liste des mots ayant le score TD-IDF le plus élevé est :", Core.ex2())   #appel de la fonction Core.ex2
        time.sleep(5)
    elif choix == 3:
        print("Les mots les plus répétés par le président Chirac sont :", Core.ex3())      #appel de la fonction Core.ex3
        time.sleep(5)
    elif choix == 4:
        print("Les présidents ayant évoqué la nation sont : ", end = "")
        for i in range(len(Core.ex4())-1):  #pour chauque indice i de la longueur de la (liste-1) de la fonction Core.ex4
            print(Core.ex4()[i], end= ", ") #affiche tous les éléments correspondant à leurs indices , séparé par une virgule 
        print(Core.ex4()[-1])               #affiche le dernier élément de la liste 
        time.sleep(5)
    elif choix == 5:
        print("Le premier président à parler du climat et/ou de l'écologie est :", Core.ex5()) #appel de la fonction Core.ex5
        time.asleep(5)
    elif choix == 6:
        print("Question 6 sélectionnée. Veuillez patienter...")
        print("Voici la liste des mots répétés par tous les présidents, hormis les mots non-importants :", Core.ex6())  #appel de la fonction Core.ex5
        time.sleep(5)
    else:
        print("Choix invalide. Veuillez choisir une option de 1 à 6.") # Si aucun des choix saisie par l'utilisateur convient entre 1 et 6
        time.sleep(3)
