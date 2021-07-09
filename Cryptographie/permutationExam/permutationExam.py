import random




def lettre_2_position(lettre):
    """retourne la position de la lettre dans l'alphabet.
    'a' -> 0, b -> 1, ... 'z' -> 25.
    attention cette fontion suppose que lettre est une minuscule"""
    return ord(lettre) - ord('a')

def position_2_lettre(nombre):
    """retourne la lettre correspondant à une position dans l'alphabet.
    'a' <- 0, b <- 1, ... 'z' <- 25.
    la lettre retournée est une minuscule"""
    return chr(nombre + ord('a'))

_LONGUEUR = 26
"""Définit une constante permettant de gérer la taille de l'alphabet."""

def permutation_identite():
    """retourne une liste contenant les valeurs allant de 0 à 25 rangées par ordre croissant."""
    return [i for i in range(_LONGUEUR)]

def permutation_aleatoire():
    """retourne une liste contenant les valeurs allant de 0 à 25 mélangées."""
    res = permutation_identite()
    random.shuffle(res)
    return res

def reciproque(ceci):
    """retourne la permutation réciproque à ceci."""
    res = [0] * _LONGUEUR
    for i in range(_LONGUEUR):
        res[ceci[i]] = i
    return res

def decale(ceci, decalage = 1):
    """retourne la permutation obtenu en décalant les valeurs vers le début de la liste de <decalage> case;
    le début du tableau etant replacé à la fin."""
    return ceci[decalage:] + ceci[:decalage]

def recale(ceci, decalage = 1):
    """retourne la permutation verifiant reciproque(decale(reciproque(ceci))) = recale(ceci)"""
    return [(ceci[i] - decalage) % _LONGUEUR for i in range(_LONGUEUR)]

class t_chiffreur_a_etats:

    def __init__(self, sel):	

        self.le_sel = sel
        self.la_permutation = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.la_reciproque = reciproque(self.la_permutation)
        """initialise l'objet <self> pour qu'il contienne les attributs :
           - <le_sel> ayant pour valeur <sel> ;
           - <la_permutation> ayant pour valeur une permutation aléatoire ;
           - <la_reciproque> ayant pour valeur la réciproque du champ <la_permutation>."""
        
    
    def __del__(self):
        """détruit tous les attributs de l'objet <self>."""
        del self.le_sel
        del self.la_permutation 
        del self.la_reciproque

    def _avance(self):
        decale(self.la_permutation, self.le_sel)
        recale(self.la_reciproque , self.le_sel)




        """décale l'attribut <la_permutation> de l'objet <self> et recale l'attribut <la_reciproque> de l'objet <self>."""


    def chiffre(self, position):
        self._avance(self.le_sel)
        """Cette méthode modifie l'état de l'objet self en utilisant la méthode <_avance>,
        puis calcule le nouveau attribut <le_sel> avec <position> et l'attribut <la_permutation>
        et enfin retourne la valeur de l'attribut <le_sel>."""

    def dechiffre(self, position):
        
        """Cette méthode modifie l'état de l'objet self en utilisant la méthode <_avance>,
        puis calcule le résultat avec l'attribut <la_reciproque> avec <position>,
        puis stocke le paramètre <position> dans l'attribut <le_sel>
        et enfin retourne le résultat."""


    def _opere_lettre(self, lettre, operation_numerique):
        """retourne la lettre <lettre> transformée par la fonction <operation_numerioque>.
        Cette fonction <operation_numerique> possède deux paramètres :
           - un object de type t_chiffreur_a_etats
           - une position dans l'alphabet"""


    def chiffre_lettre(self, lettre):
        """Cette méthode chiffre <lettre> en utilisant notamment la méthode <_opere_lettre>.
        Cette méthode retourne la lettre chiffrée."""
    
    def dechiffre_lettre(self, lettre):
        """Cette méthode dechiffre <lettre> en utilisant notamment la méthode <_opere_lettre>.
        Cette méthode retourne la lettre dechiffrée."""

    def _opere_message(self, message, operation_numerique):
        """Cette méthode applique <operation_numerique> à toutes les lettres de <message>.
        Cette méthode retourne le message transformé."""

    def chiffre_message(self, message):
        """Cette méthode dechiffre <message> en utilisant notamment la méthode <_opere_message>.
        Cette méthode retourne le message chiffrs."""
    
    def dechiffre_message(self, message):
        """Cette méthode dechiffre <message> en utilisant notamment la méthode <_opere_message>.
        Cette méthode retourne le message dechiffré."""
        return self._opere_message(message, t_chiffreur_a_etat.dechiffre)

    def copie(self):
        """Cette méthode retourne une copie de <self>."""

    def __str__(self):
        """Cette méthode retourne une chaine de caractères représentant <self>."""
        return str(self.la_permutation) + "\n" + str(self.la_reciproque) + " | " + str(self.le_sel)

if __name__ == '__main__':
    for i in range(26):
        print(i, "=>", position_2_lettre(i), "=>",  lettre_2_position(position_2_lettre(i)))

    mon_message = "bonjour le monde"
    mon_chiffreur = t_chiffreur_a_etats(1)
    mon_chiffreur_2 = mon_chiffreur.copy()
    print(mon_message)
    print(mon_chiffreur)
    mon_message_chiffre = mon_chiffreur.chiffre_message(mon_message)
    print(mon_message_chiffre)
    print(mon_chiffreur)
    mon_message_dechiffre = mon_chiffreur_2.dechiffre_message(mon_message_chiffre)
    print(mon_message_dechiffre)
    print(mon_chiffreur_2)
