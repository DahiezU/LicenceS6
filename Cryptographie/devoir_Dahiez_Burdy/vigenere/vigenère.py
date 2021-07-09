


def est_lettre(lettre):
    car = ord(lettre.upper())
    return car>64 and car<91

def decalage(la_lettre, le_decalage):
    car = ord(la_lettre.upper())
    if est_lettre(la_lettre):
        car += le_decalage
        while car>90:
            car -= 26
        while car<65:
            car += 26
        return chr(car)
    else:
        return ""


def vigenere(s,cle,crypte):
    i = 0
    chiffre=''
    for char in s:
        if est_lettre(char):
            k = ord(cle[i%len(cle)])-65
            print(k)
            if crypte:
                chiffre += decalage(char,k)
            else:
                chiffre += decalage(char,-k)
            i+=1
        else:
            chiffre += char
    return chiffre

vigenere(" exemple de texte  ", " clé de chiffrement  ", " true ")