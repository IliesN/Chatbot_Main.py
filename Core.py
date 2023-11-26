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
             "François": "Mitterand",
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


def df(string):
    dic = {}
    a = string.split(" ")
    print(a)
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


print(idf())
