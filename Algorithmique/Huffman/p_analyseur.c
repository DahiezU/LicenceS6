#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "p_analyseur.h"

int mes_effectifs[NB_OCTETS];

void init_analyseur(){
    memset(mes_effectifs, 0, sizeof(int) * NB_OCTETS);
}

void visualiser_effectifs(){
    for(int i=0; i < NB_OCTETS; i++){
        printf("[%d, %x] => %d\n", i, (char)i, mes_effectifs[i]);
    }
}

void lire_contenu(FILE* fichier){
    char c = fgetc(fichier);
    while(c != EOF){
        printf("%x % d %d\n", c, c, (unsigned char)c);
        c = fgetc(fichier);
    }
    printf("%x %d %d\n", c, c, (unsigned char)c);
}

void compter_effectif(FILE* fichier){
    char c = fgetc(fichier);
    while(c != EOF){
        mes_effectifs[(unsigned char)c]++;
        c = fgetc(fichier);
    }
    mes_effectifs[(unsigned char)c]++;
}

void analyser_fichier(char* nom_fichier){
    init_analyseur();

    FILE* mon_fichier = fopen(nom_fichier, "r");
    if(mon_fichier == NULL){
        printf("Ouverture impossible");
        exit(-2);
    }
    compter_effectif(mon_fichier);
    fclose(mon_fichier);
}

int effectif(int octet){
    return mes_effectifs[octet];
}

