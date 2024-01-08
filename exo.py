#CHAPITRE 5 by Arooks , Merci à lui de bien vouloir partager

def unique(list):
    res = []
    for elem in list:
        if elem not in res:
            res.append(elem)
    return res

def zipper(listea, listeb):
    res = []
    taille_max = max(len(listea), len(listeb))
    for i in range(taille_max):
        if i < len(listea):
            res.append(listea[i])
        if i < len(listeb):
            res.append(listeb[i])
    return res

def fibo(n):
    if n <= 0:
        return None
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def pgcd(a,b):
    if b == 0:
        return a
    else:
        return pgcd(b, a%b)

def hanoi(n, A, B, C):
    if n == 1:
        print(f"Déplacez un disque de {A} vers {C}")
    else:
        hanoi(n - 1, A, C, B)
        print(f"Déplacez un disque de {A} vers {C}")
        hanoi(n - 1, B, A, C)

#hanoi(3, 'A', 'B', 'C')
