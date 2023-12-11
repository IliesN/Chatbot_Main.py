import os
import math

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


prez_file = list_of_files("speeches-20231108", ".txt")
nfile = len(prez_file)
prez_name = {"Jacques": "Chirac",
             "Valéry": "Giscard dEstaing",
             "François": "Hollande",
             "Emmanuel": "Macron",
             "françois": "Mitterand",
             "Nicolas": "Sarkozy"}

def prez_lastname():
    prez_lastnam = []
    for line in prez_file:
        j = 0
        for char in line:
            if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                break

            else:
                j += 1

        if (line[11:j]) not in prez_lastnam:
            prez_lastnam.append(line[11:j])
    return prez_lastnam


def convert():
    for element in prez_file:
        r = open("speeches-20231108/"+element, "r")
        c = open("Cleaned/"+element, "w")
        for ligne in r.readlines():
            for charac in ligne:
                if ord("A") <= ord(charac) <= ord("Z"):
                    c.write(chr(ord(charac)+((ord("a")-ord("A")))))
                elif ord(charac) == ord("'"):
                    c.write("e ")
                elif ord(charac) == ord("-") or ord(charac) == ord("_"):
                    c.write(" ")
                elif ord(",") <= ord(charac) <= ord(".") or ord(":") <= ord(charac) <= ord(";") or ord(charac) == ord("?") or ord(charac) == 33:

                    c.write("")
                else:
                    c.write(charac)



def tf(string):
    dic = {}
    if type(string) == list:
        for i in range(len(string)):
            if string[i] in dic:
                dic[string[i]] += 1
            else:
                print("ok")
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

def idf(e):
    if type(e) == str:
        dic = {}
        dicidf = {}
        for element in prez_file:
            c = open("Cleaned/" + element, "r")
            for ligne in c.readlines():
                for lr in ligne.splitlines():
                    a = lr.split(" ")
                    for i in range(len(a)):
                        if a[i] in dic and a[i] != "":
                            dic[a[i]] += 1
                        elif a[i] not in dic and a[i] != "":
                            dic[a[i]] = 1

        for element2 in prez_file:
            tempdic = {}
            d = open(e + element2, "r")
            for ligne2 in d.readlines():
                for lr in ligne2.splitlines():
                    b = lr.split(" ")
                    for mot in dic:
                        if mot in b:
                            tempdic[mot] = 1
            for el in tempdic:
                if el in dicidf:
                    dicidf[el] += 1
                else:
                    dicidf[el] = 1
        for ele in dicidf:
            dicidf[ele] = math.log10(nfile/dicidf[ele])

        return dicidf


def tf_idf(direct):
    idfdic = idf("Cleaned/")
    mtfidf = []
    for element in idfdic:
        newlist = []
        for j in range(8):
            f = open(direct+"/"+prez_file[j])
            readfile = f.read()
            if element in tf(readfile):
                newlist.append(round(tf(readfile)[element]*idfdic[element], 2))
            else:
                newlist.append(0.0)
        mtfidf.append(newlist)

    return idfdic, mtfidf

def print_mtfidf():
    idfdic = idf("Cleaned/")
    mtfidf = tf_idf("Cleaned")[1]
    x = 0
    for element in idfdic:
        print(mtfidf[x], element)
        x+=1

    print(x, " mots")

def ex1():
    idfdic = idf("Cleaned/")
    matrix = tf_idf("Cleaned")[1]
    uniml = []
    x = 0
    for element in idfdic:
        unim = True
        for i in range(len(matrix[x])):
            if matrix[x][i] != 0.0:
                unim = False
        if unim:
            uniml.append(element)
        x += 1
    return uniml


def ex2():
    idfdic = idf("Cleaned/")
    matrix = tf_idf("Cleaned")[1]
    maximum = 0.0
    maxlist = []
    x = 0
    for element in idfdic:
        for i in range(len(matrix[x])):
            if matrix[x][i] > maximum:
                maximum = matrix[x][i]
        x+=1
    x=0
    for element in idfdic:
        if maximum in matrix[x]:
            maxlist.append(element)
        x += 1
    if len(maxlist)==1:
        return maxlist[0]
    else:
        return maxlist

def ex3():
    unimportant_words = ex1()
    max1 = 0
    max1w = ""
    max2 = 0
    max2w = ""
    f = open("Cleaned/Nomination_Chirac1.txt", "r")
    read1 = f.read()
    dic1 = tf(read1)
    g = open("Cleaned/Nomination_Chirac2.txt", "r")
    read2 = g.read()
    dic2 = tf(read1)

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
    nationmax = 0
    for element in prez_file:
        f = open("Cleaned/"+element)
        reading = f.read()
        dic = tf(reading)
        if "nation" in dic and element.strip("Nomination_").strip(".txt").strip("1").strip("2") not in listprez:
            listprez.append(element.strip("Nomination_").strip(".txt").strip("1").strip("2"))
    return listprez

def ex5():
    premier = True
    premierprez = []
    for element in prez_file:
        f = open("Cleaned/"+element)
        reading = f.read()
        dic = tf(reading)
        while premier:
            if "climat" or "écologie" in dic :
                premierprez.append(element.strip("Nomination_").strip(".txt").strip("1").strip("2"))
                premier = False
    return premierprez[0]

def ex6():
    dic = {}
    basewordlist = []
    unim = ex1()
    f = open("Cleaned/Nomination_Chirac1.txt")
    reading = f.read()
    f.close()
    basewordlist = reading.split()
    for element in prez_file:
        f = open("Cleaned/"+element)
        reading = f.read()
        wordlist = reading.split()
        for element in basewordlist:
            if element not in wordlist:
                basewordlist.remove(element)
    for i in range(len(basewordlist)):
        if basewordlist[i] in dic:
            dic[basewordlist[i]] += 1
        else:
            dic[basewordlist[i]] = 1
    basewordlist = []
    for element in dic:
        if element not in unim:
            basewordlist.append(element)
    return basewordlist

def tokenisation(string):
    motvide = ["le", "de", "et", "la", "à", "est", "les", "pour", "un", "une"]
    finalstr = ""
    for charac in string:
        if ord("A") <= ord(charac) <= ord("Z"):
            charac = chr(ord(charac)+((ord("a")-ord("A"))))
            finalstr+=charac
        elif ord(charac) == ord("'"):
            charac = ("e ")
            finalstr += charac
        elif ord(charac) == ord("-") or ord(charac) == ord("_"):
            charac = (" ")
            finalstr += charac
        elif ord(",") <= ord(charac) <= ord(".") or ord(":") <= ord(charac) <= ord(";") or ord(charac) == ord("?") or ord(charac) == 33:

            charac = ("")
            finalstr += charac
        else:
            finalstr += charac
    exstr = finalstr.split()
    for element in exstr:
        if element in motvide:
            exstr.remove(element)
    return exstr

def whichincorpus(q):
    wordic = tf_idf("Cleaned")[0]
    wordlist = tokenisation(q)
    for element in wordlist:
        if element not in wordic.keys():
            wordlist.remove(element)
    print(wordlist)

def q_tf(string):
    string2 = tokenisation(string)
    l = len(string2)
    dictfq = tf(string2)
    for element in dictfq:
        dictfq[element]/=l
    return dictfq






