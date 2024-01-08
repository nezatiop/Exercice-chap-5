import math
import turtle


#Exercice 1.6.1
def ampl_3(amp1,amp2):
    return 180-amp1-amp2


#Exercice 1.6.2
def hypo(cote1,cote2):
    return math.sqrt((cote1**2)+(cote2**2))


#Exercice 1.6.3
def FahrToCel(Fahr):
    return (Fahr-32)/1.8
def CelToFahr(Cel):
    return (1.8*Cel)+32


#Exercice 1.6.4
def AireCercle(rayon):
    return math.pi * rayon ** 2


#Exercice 1.6.5
def temps(secondes):
    heure = secondes // 3600
    minute = (secondes - (heure * 3600)) // 60
    seconde = secondes - (heure * 3600) - (minute * 60)
    return "%d:%02d:%02d" % (heure, minute, seconde)


#Exercice 2.5.1
def PairOuImpair(nombre):
    if nombre%2 == 0:
        return "pair"
    else:
        return "impair"
    

#Exercice 2.5.2
def ValAbs(nombre):
    if nombre < 0 :
        return -nombre
    else:
        return nombre


#Exercice 2.5.3
def bissextile(annee):
    if annee%4==0 and annee%100!=0 or annee%400==0:
        return True
    else:
        return False


#Exercice 2.5.4
def factorielle(nombre):
    if nombre <= 1:
        return 1
    else:
        return nombre * factorielle(nombre-1)


#Exercice 2.5.5
def premier(nombre):
    if nombre > 1:
        for i in range(2, nombre):
            if nombre % i == 0:
                return False
            else:
                return True


"""
#Exercice 3.6.1
taille = int(input("taille de la liste :"))
liste = []
for long in range(0,taille):
    liste.append(input())
print(liste)
"""

"""
#Exercice 3.6.2
listenb = input()
nombres = "0123456789"
somme = 0
for donnee in listenb:
    if donnee in nombres:
        somme += int(donnee)
print(somme)
"""

"""
#Exercice 3.6.3
chaine = input()
max = 0
for chara in chaine:
    if len(chara) > max:
        max = len(chara)
print(max)
"""

"""
#Exercice 3.6.4
chaine = input()
voyelles = "aeiouAEIOU"
newchaine = ""
for chara in chaine:
    if chara in voyelles:
        newchaine += "*"
    else:
        newchaine += chara
print(newchaine)
"""

"""
#Exercice 3.6.5
phrase = input()
mots = phrase.split()
for mot in mots:
    print(mot)
"""


#Exercice 3.6.6
liste = list(input())
val = input()
resultat = []
for i, valeur in enumerate(liste):
    if valeur == val:
        print(i,end="")

#Exercice 5.9.1
def unique(liste):
    return set(liste)


#Exercice 5.9.2
def zipper(liste1,liste2):
    min_length = min(len(liste1), len(liste2))
    resultat=[]
    for i in range(min_length):
        resultat.append((liste1[i], liste2[i]))
        if len(liste1)>len(liste2):
            resultat.append(liste1[i])
        elif len(liste2)>len(liste1):
            resultat.append(liste2[i])
    return resultat


#Exercice 5.9.3
def fibo(entier):
    if entier<=0:
        print("L'argument doit être un nombre positif.")
    elif entier==1:
        return 0
    elif entier == 2:
        return 1
    else :
        return fibo(entier - 1) + fibo(entier - 2)
    

#Exercice 5.9.4
def pgcd(entier1,entier2):
    while entier2 != 0:
        entier1, entier2 = entier2, entier1 % entier2
        return abs(entier1)


#Exercice 3.9.5
