import random
# Simon Burdy & Ulysse Dahiez


def same():
    return list(range(0, 26))


def aleatoire():
    liste = same()
    random.shuffle(liste)
    return liste


def inverse(liste):
    listeinverse = []
    for i in range(0, len(liste)):
        listeinverse.append(liste.index(i))
    return listeinverse


def decal(liste):
    return liste[1:len(liste)] + [liste[0]]


def recal(liste):
    recal = list(map(lambda x: x-1, liste))
    recal[recal.index(-1)] = len(liste)-1
    return recal


def permute(phrase, permutation):
    phraseChiffree = ''
    for car in phrase:
        if ('a' <= car and car <= 'z'):
            phraseChiffree += chr(ord('a') + permutation[ord(car)-ord('a')])
        elif ('A' <= car and car <= 'Z'):
            phraseChiffree += chr(ord('A') + permutation[ord(car)-ord('A')])
        else:
            phraseChiffree += car
    return phraseChiffree

def chiffrer(phrase, permutation):
    return permute(phrase, decal(permutation))

def dechiffrer(phraseChiffree, permutation):
    return permute(phraseChiffree, recal(inverse(permutation)))

maPhrase = 'Ceci nest pas une pipe'
maPermutation = aleatoire()

maPhraseChiffree = chiffrer(maPhrase, maPermutation)
maPhraseDechiffree = dechiffrer(maPhraseChiffree, maPermutation)

print("phrase à chiffrer : \n" + maPhrase)

print("\nMa phrase chiffrée : \n" + maPhraseChiffree)
print("\nMa phrase déchiffrée : \n" + maPhraseDechiffree)