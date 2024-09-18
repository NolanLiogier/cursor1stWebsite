def inverser_mot(mot):
    nbLettres = len(mot)
    mot_inverser = ''

    for i in range (1, nbLettres + 1) :
        mot_inverser += mot[-i]

    return mot_inverser == mot

print(inverser_mot("radar"))
