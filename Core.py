import os
import math


def liste_fichiers(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


prez_fichiers = liste_fichiers("speeches-20231108", ".txt")
nfile = len(prez_fichiers)
prez_nom = {"Jacques": "Chirac",
            "Valéry": "Giscard dEstaing",
            "François": "Hollande",
            "Emmanuel": "Macron",
            "françois": "Mitterand",
            "Nicolas": "Sarkozy"}

#Fonction pour stocker les noms de president dans une liste
def prez_nomfamille():
    prez_lastnam = []
    for filename in prez_fichiers:
        # Ouverture du fichier en mode lecture
        with open("speeches-20231108/" + filename, "r") as file:
            j = 0
            for char in file.read():
                # Si le caractère est un chiffre ou un point, arrête la boucle
                if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                    break
                else:
                    j += 1
            #Lecture d'une portion du fichier pour obtenir le nom de famille puis vérifie si le nom est dans la liste prez_lastam
            if (file.read(11)[11:j]) not in prez_lastnam:
                prez_lastnam.append(file.read(11)[11:j])
    return prez_lastnam

def convert():
    for element in prez_fichiers:
        r = open("speeches-20231108/"+element, "r")
        c = open("Cleaned/"+element, "w")
        for line in r.readlines():
            for character in line:
                if ord("A") <= ord(character) <= ord("Z"):
                    c.write(chr(ord(character)+(ord("a")-ord("A"))))
                elif ord(character) == ord("'"):
                    c.write("e ")
                elif ord(character) == ord("-") or ord(character) == ord("_"):
                    c.write(" ")
                elif (ord(",") <= ord(character) <= ord(".")
                      or ord(":") <= ord(character) <= ord(";")
                      or ord(character) == ord("?") or ord(character) == 33):
                    c.write("")
                else:
                    c.write(character)


def score_tf(string):
    dic = {}
    if type(string) == list:
        for i in range(len(string)):
            if string[i] in dic:
                dic[string[i]] += 1
            else:
                dic[string[i]] = 1
        return dic

    else:
        b = string.replace('\n', ' ')
        a = b.split(" ")
        for i in range(len(a)):
            if a[i] in dic:
                dic[a[i]] += 1
            else:
                dic[a[i]] = 1
        return dic


def score_idf():
    dic = {}
    dicidf = {}

    for element in prez_fichiers:
        with open("Cleaned/" + element, "r") as c:
            for ligne in c.readlines():
                for lr in ligne.splitlines():
                    a = lr.split(" ")
                    for i in range(len(a)):
                        if a[i] in dic and a[i] != "":
                            dic[a[i]] += 1
                        elif a[i] not in dic and a[i] != "":
                            dic[a[i]] = 1

    for element2 in prez_fichiers:
        tempdic = {}
        with open("Cleaned/" + element2, "r") as d:
            for ligne2 in d.readlines():
                for lr in ligne2.splitlines():
                    b = lr.split(" ")
                    for mot in dic:
                        if mot in b:
                            tempdic[mot] = 1

        for el in tempdic:
            dicidf[el] = dicidf.get(el, 0) + 1

    for ele in dicidf:
        dicidf[ele] = math.log10(nfile / dicidf[ele])

    return dicidf


def tf_idf_matrix():
    idfdic = score_idf()
    mtfidf = []

    for element in prez_fichiers:
        newlist = []
        with open("Cleaned/" + element) as f:
            readfile = f.read()
            for e in idfdic:
                if e in score_tf(readfile):
                    newlist.append(round(score_tf(readfile)[e] * idfdic[e], 2))
                else:
                    newlist.append(0.0)
        mtfidf.append(newlist)

    return mtfidf


def print_tfidf_matrix():
    mtfidf = tf_idf_matrix()
    idfdic = score_idf()
    x = 0
    print(" "*34, end=" ")
    maxlen = 0
    for word in idfdic:
        if len(word) > maxlen:
            maxlen = len(word)
        print(word, " "*(34-len(word)), end=" ")
    print(maxlen)
    print("\n")
    for element in prez_fichiers:
        print(element, " "*(32-len(element)), end=" ")
        for value in mtfidf[x]:
            if len(str(value)) == 2:
                print(value, " "*32, end=" ")
            elif len(str(value)) == 3:
                print(value, " "*31, end=" ")
            elif len(str(value)) == 4:
                print(value, " "*30, end=" ")
        print("\n")
        x += 1


def ex1():
    idfdic = score_idf()
    matrix = tf_idf_matrix()
    uniml = []
    x = 0
    for element in idfdic:
        unim = True
        for i in range(8):
            if matrix[i][x] != 0.0:
                unim = False
        if unim:
            uniml.append(element)
        x += 1
    return uniml


def ex2():
    idfdic = score_idf()
    matrix = tf_idf_matrix()
    maximum = 0.0
    maxlist = []
    x = 0
    for _ in idfdic:
        for i in range(8):
            if matrix[i][x] > maximum:
                maximum = matrix[i][x]
        x += 1
    for i in range(8):
        x = 0
        for element in idfdic:
            if maximum == matrix[i][x]:
                maxlist.append(element)
            x += 1
        x += 1
    if len(maxlist) == 1:
        return maxlist[0]
    else:
        return maxlist


def ex3():
    unimportant_words = ex1()
    max1 = 0
    max1w = ""
    max2 = 0
    max2w = ""
    with open("Cleaned/Nomination_Chirac1.txt", "r") as file:
        read1 = file.read()
        dic1 = score_tf(read1)
        dic2 = score_tf(read1)

        for element in dic1:
            if dic1[element] > max1 and element != '' and element not in unimportant_words:
                max1 = dic1[element]
                max1w = element
        for element in dic2:
            if dic2[element] > max2 and element != '' and element not in unimportant_words:
                max2 = dic2[element]
                max2w = element
        if max1w == max2w:
            return max1w
        else:
            return max1w, max2w


def ex4():
    listprez = []
    for element in prez_fichiers:
        f = open("Cleaned/"+element)
        reading = f.read()
        dic = score_tf(reading)
        if "nation" in dic and element.strip("Nomination_").strip(".txt").strip("1").strip("2") not in listprez:
            listprez.append(element.strip("Nomination_").strip(".txt").strip("1").strip("2"))
    return listprez


def ex5():
    premier = True
    premierprez = []
    for element in prez_fichiers:
        f = open("Cleaned/"+element)
        reading = f.read()
        dic = score_tf(reading)
        while premier:
            if "climat" or "écologie" in dic:
                premierprez.append(element.strip("Nomination_").strip(".txt").strip("1").strip("2"))
                premier = False
    return premierprez[0]


def ex6():
    dic = {}
    unim = ex1()
    f = open("Cleaned/Nomination_Chirac1.txt")
    reading = f.read()
    f.close()
    basewordlist = reading.split()
    for element in prez_fichiers:
        f = open("Cleaned/"+element)
        reading = f.read()
        wordlist = reading.split()
        for element2 in basewordlist:
            if element2 not in wordlist:
                basewordlist.remove(element2)
    for i in range(len(basewordlist)):
        if basewordlist[i] in dic:
            dic[basewordlist[i]] += 1
        else:
            dic[basewordlist[i]] = 1
    basewordlist = []
    for element3 in dic:
        if element3 not in unim:
            basewordlist.append(element3)
    return basewordlist


def tokenisation(string):
    motvide = ["le", "de", "et", "la", "à", "est", "les", "pour", "un", "une"]
    motquestion = ["comment", "pourquoi"]
    finalstr = ""
    for charac in string:
        if ord("A") <= ord(charac) <= ord("Z"):
            charac = chr(ord(charac)+(ord("a")-ord("A")))
            finalstr += charac
        elif ord(charac) == ord("'"):
            charac = "e "
            finalstr += charac
        elif ord(charac) == ord("-") or ord(charac) == ord("_"):
            charac = " "
            finalstr += charac
        elif (ord(",") <= ord(charac) <= ord(".") or ord(":") <= ord(charac) <= ord(";") or ord(charac) == ord("?")
              or ord(charac) == 33):

            charac = ""
            finalstr += charac
        else:
            finalstr += charac
    exstr = finalstr.split()
    for element in exstr:
        if element in motvide or element in motquestion:
            exstr.remove(element)
    return exstr


def whichincorpus(q):
    wordic = score_idf()
    wordlist = tokenisation(q)
    for element in wordlist:
        if element not in wordic.keys():
            wordlist.remove(element)
    print(wordlist)


def question_tf(string):
    string2 = tokenisation(string)
    dictfq = score_tf(string2)
    return dictfq


def question_tf_idf(string):
    qlist = []
    tf_s = question_tf(string)
    idfs = score_idf()
    for element in tf_s:
        if element in idfs:
            qlist.append(round(tf_s[element]*idfs[element], 2))
        else:
            qlist.append(0.0)

    return qlist, tokenisation(string)[qlist.index(max(qlist))]


def produit_scalaire(a, b):
    scal = 0.0
    for i in range(len(a)):
        scal += a[i]*b[i]
    return scal


def norme(a):
    normv = 0.0
    for element in a:
        normv += element**2
    normv = math.sqrt(normv)
    return normv


def calcul_similarite(a, b):
    sim = produit_scalaire(a, b)/norme(a)*norme(b)
    return sim


def calcul_pertinent(corpus, v_question, listenoms):

    maximum = 0.0
    vlist = v_question[0]
    filename = ""
    mot_pertinent = v_question[1]

    x = 0
    for element in listenoms:
        max_len = len(corpus[x])
        vlist += [0.0] * (max_len - len(vlist))
        sim = calcul_similarite(corpus[x], vlist)

        if sim > maximum:
            maximum = sim
            filename = element

        x += 1

    return "speeches-20231108/"+filename, mot_pertinent, maximum

def phrase(fichier):

    with open(fichier[0], 'r') as f:
        r = f.read()
        saviour = r.splitlines()
        for element in saviour:
            x = element.split(" ")
            if str(fichier[1]) in x:
                    for e in x:
                        print(e, end = " ")
                    break




