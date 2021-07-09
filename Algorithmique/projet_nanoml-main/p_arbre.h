#ifndef P_ARBRE
#define P_ARBRE

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

// -- LISTE BALISE CONNUES -- TYPE
typedef enum e_balise{texte_enrichi,document,annexes,contenu,section,
    titre,liste,item,liste_texte,texte_liste,
    texte,mot_enrichi,mot_important,NB_OPERATIONS} t_balise;


// -- STRUCTURE STRING
typedef struct sEntreeString{
    char lEtiquette;
    struct sEntreeString* leFrereSuivant;
} tEntreeString;
typedef tEntreeString* aEntreeString;
typedef aEntreeString t_table_string;

// -- STRUCTURE ARBRE HTML
typedef struct sEntreeArbre{
    t_table_string lEtiquette;
    t_balise balise;
    struct sEntreeArbre* lePremierFils;
    struct sEntreeArbre* leDernierFils;
    struct sEntreeArbre* leFrerePrecedent;
    struct sEntreeArbre* leFrereSuivant;
    struct sEntreeArbre* lePere;
}t_entree_arbre;
typedef t_entree_arbre* aEntreeArbre;
typedef aEntreeArbre tTableArbre;


// ---- METODES

void start(char le_fichier[]);


#endif