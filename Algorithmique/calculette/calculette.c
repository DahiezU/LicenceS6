#include <stdio.h>
#include <stdlib.h>

FILE* mon_fichier;
char mon_caractere;

void facteur();
void op_mult();
int est_op_mult();
void expression();

void passer_espace(){
    while(mon_caractere == ' ' || mon_caractere == '\t' || mon_caractere == '\n' || mon_caractere == '\r'){
        mon_caractere = fgetc(mon_fichier);
    }
}

void amorcer(){
    mon_fichier = fopen("exemple.txt", "r");
    if(mon_fichier == NULL){
        perror("Fichier introuvable !\n");
        exit(-1);
    }
    mon_caractere = fgetc(mon_fichier);
    passer_espace();    
}

void lire(char caractere){
    if(mon_caractere == caractere){
        printf("%c", mon_caractere);
        mon_caractere = fgetc(mon_fichier);
    }else{
        printf("erreur de syntaxe : caractere attendu : %c / caractere trouve %c\n", caractere, mon_caractere);
        exit(-2);
    }
}

int est_op_add(){
    return mon_caractere == '+' || mon_caractere == '-';
}

void op_add(){
    if(mon_caractere == '+'){
        lire('+');
    }else if (mon_caractere == '-'){
        lire('-');
    }
    passer_espace();
}

void terme(){
    facteur();
    while(est_op_mult()){
        op_mult();
        facteur();
    }
}

void expression(){
    terme();
    while(est_op_add()){
        op_add();
        terme();
    }
}

void calcul(){
    expression();
    lire(' ');
    passer_espace();
}

int main(/* int argc, char** argv */){

    amorcer();
    calcul();

}