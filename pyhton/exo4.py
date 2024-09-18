def calcul(chiffre):
    result = 1
    for i in range (1, chiffre + 1) :
        result = result * i
    return result
print(calcul(5))