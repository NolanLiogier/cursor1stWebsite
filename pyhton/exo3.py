def calcul(liste) :
    nombre = 0
    for valeur_list in liste:
        if valeur_list > nombre :
            nombre = valeur_list 
    return nombre

print(calcul([3, 58, 111, 21]))