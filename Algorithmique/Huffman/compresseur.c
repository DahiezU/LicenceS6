#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "p_analyseur.h"
#include "p_arbre.h"

int main(int argc, char** argv){

    if(argc != 2){
        printf("Il manque le nom du fichier à compresser");
        exit(-1);
    }
    analyser_fichier(argv[1]);
    /*init_table_arbres();
    creer_arbre_code();
    afficher_arbre(arbre_codes(), 0);*/

    return 0;
}