import math as m

def substitution_cesar(decalage):
    def function(lettre):
        if (ord(lettre)<97 or 122<ord(lettre)): #si le caractère n'est pas une lettre minuscule
            print("lettre non prise en charge")
        else:
            lettre = ord(lettre) - 32 + decalage #passage en majuscule + décalage
            if lettre > ord('Z'): #si la lettre dépasse la fin de l'alphabet
                lettre = ord('A') + lettre - ord('Z') - 1
            return chr(lettre)
    return function


def trousseau_cesar(decalage):


    """retourne deux fonctions permettant de décaler une lettre dans l'alphabet.

    On supposera que la lettre à décaler est minuscule et que la lettre obtenu par décalage est une majuscule.

    :param : decalage : (int) le décalage dans l'alphabet.

    :return : tuple : deux fonction décalant les lettres dans l'alphabet la première décalant positivement, la seconde décalant négativement."""
    def fonction2(lettre):
        print("  ")
        
    def fonction1(lettre2):
        print("  ")

    

    return (function1, fonction2)


def substitution_ligne(ligne, substitution):

    """fonction appliquant une substitution sur toutes les lettres d'une ligne."""



def chiffrement_par_substitution(nom_fichier_src, nom_fichier_dest, substitution):

    """chiffre le fichier source et place le contenu chiffré dans le fichier destination.

    le chiffrement appliqué et le chiffrement de César.

    :param : nom_fichier_src : (str) le nom du fichier source.

    :param : nom_fichier_dest : (str) le nom du fichier destination.

    :param : substitution: (function) la fonction de substitution à appliquer sur tout le fichier.

    :return: (NoneType) None"""




def substitution_affine(coefficient, decalage):

    """retourne une fonction permettant de décaler une lettre dans l'alphabet.

    On supposera que la lettre à décaler est minuscule et que la lettre obtenu par décalage est une majuscule.

    :param : coefficient : (int) le coefficient appliqué à la lettre dans l'alphabet.


    :param : decalage : (int) le décalage dans l'alphabet.


    :return : function : une fonction f définie par f(x) = coefficient * lettre + decalage.

 Attention f(x) doit être une lettre de "l'alphabet"."""




def trousseau_affine(coefficient, decalage):

    """retourne deux fonctions permettant de chiffrer (avec une chiffrement affine) une lettre dans l'alphabet.

    On supposera que la lettre à chiffrer est minuscule et que la lettre obtenue par le chiffrement est une majsucule.

    :param : coefficient : (int) le coefficient appliqué pour le chiffrement.

    :param : decalage : (int) le décalage dans l'alphabet.

    :return : tuple : deux fonctions décalant les lettres dans l'alphabet la première décalant positivement, la seconde décalant négativement."""
