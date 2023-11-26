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
                if 65 <= ord(charac) <= 90:
                    c.write(chr(ord(charac)+32))
                elif ord(charac) == 39 or ord(charac) == 45:
                    c.write(" ")
                elif 44 <= ord(charac) <= 46 or 58 <= ord(charac) <= 59 or ord(charac) == 63 or ord(charac) == 33:

                    c.write("")

                else:
                    c.write(charac)


def tf(string):
    dic = {}
    b = string.replace('\n', ' ')
    a = b.split(" ")
    for i in range(len(a)):
        if a[i] in dic:
            dic[a[i]] += 1
        else:
            dic[a[i]] = 1
    return dic

def idf():
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
        d = open("Cleaned/" + element2, "r")
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
        dicidf[ele] = math.log(nfile/dicidf[ele])

    return dicidf


def tf_idf(direct):
    idfdic = idf()
    mtfidf = []
    for element in idf():
        newlist = []
        for j in range(8):
            f = open(direct+"/"+prez_file[j])
            readfile = f.read()
            if element in tf(readfile):
                newlist.append((tf(readfile)[element]*idfdic[element]))
            else:
                newlist.append(0.0)
        mtfidf.append(newlist)

    return idfdic, mtfidf

def print_mtfidf():
    idfdic = idf()
    mtfidf = tf_idf("Cleaned")[1]
    x = 0
    for element in idfdic:
        print(element, mtfidf[x])
        x+=1

def ex1():
    idfdic = idf()
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
    idfdic = idf()
    matrix = tf_idf("Cleaned")[1]
    maximum = 0.0
    maxlist = []
    x = 0
    for element in idfdic:
        for i in range(len(matrix[x])):
            if matrix[x][i] > maximum:
                print(matrix[x][i])
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

        if dic1[element] > max1 and element != '':

            max1 = dic1[element]
            max1w = element
    for element in dic2:
        if dic2[element] > max2 and element != '':
            max2 = dic2[element]
            max2w = element
    if max1w == max2w:
        return max1w
    else:
        return max1w, max2w

def ex4():
    listprez = []
    for element in prez_file:
        f = open("Cleaned/"+element)
        reading = f.read()
        dic = tf(reading)
        if "nation" in dic and element.strip("Nomination_").strip(".txt").strip("1").strip("2") not in listprez:
            listprez.append(element.strip("Nomination_").strip(".txt").strip("1").strip("2"))
    return listprez
