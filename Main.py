import Core
import time
while True:
    print("Menu principal:")
    print("1. Afficher la liste des mots les moins importants dans le corpus de documents.")
    print("2. Afficher les mots ayant le score TD-IDF le plus élevé.")
    print("3. Indiquer les mots les plus répétés par le président Chirac.")
    print("4. Indiquer les noms des présidents qui ont parlé de la « Nation »")
    choix = int(input("Choisissez un nombre entre 1 et 4 : "))

    if choix == 1:
        print("Question 1 sélectionnée. Veuillez patienter...")
        print("La liste des mots les moins importants sont :", Core.ex1())
        time.sleep(5)
    elif choix == 2:
        print("Question 2 sélectionnée. Veuillez patienter...")
        print("La liste des mots ayant le score TD-IDF le plus élevé est :", Core.ex2())
        time.sleep(5)
    elif choix == 3:
        print("Les mots les plus répétés par le président Chirac sont :", Core.ex3())
        time.sleep(5)
    elif choix == 4:
        print(Core.ex4())
        time.sleep(5)
    elif choix == 5:
        print("Le premier président à parler du climat et/ou de l'écologie est :", Core.ex5())
        time.sleep(5)
    elif choix == 6:
        print("Question 6 sélectionnée. Veuillez patienter...")
        print("Voici la liste des mots répétés par tous les présidents, hormis les mots non-importants :", Core.ex6())
        time.sleep(5)

    else:
        print("Choix invalide. Veuillez choisir une option de 1 à 4.")
        time.sleep(3)
