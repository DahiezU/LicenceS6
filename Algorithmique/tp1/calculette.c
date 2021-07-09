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
    mon_fichier = fopen("exemples.txt", "r");
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
        printf("erreur de syntaxe : caractere attendu : [%c], caractere trouve [%c]\n", caractere, mon_caractere);
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
    lire('=');
    passer_espace();
}

int est_op_mult() {
    return (mon_caractere == '*' || mon_caractere == '%' || mon_caractere == '/');
}

void op_mult() {
    if(mon_caractere == '*'){
        lire('*');
    }else if (mon_caractere == '%'){
        lire('%');
    }else if (mon_caractere == '/'){
        lire('/');
    }
    passer_espace();
}

void chiffre_non_nul() {
    if ('1' <= mon_caractere && mon_caractere <= '9')
    {
        lire(mon_caractere);
    }
    
}

int est_chiffre(){
    return '0' <= mon_caractere && mon_caractere <= '9';
}

void sequence_chiffre() {
    while(est_chiffre()){
        if(mon_caractere == '0'){
            lire('0');
        } else {
            chiffre_non_nul();
        }
    }
}

void nombre_non_signe() {
    if (mon_caractere == '0') {
        lire('0');
    } else {
        chiffre_non_nul();
        sequence_chiffre();
    }
    passer_espace();
}

void nombre() {
    if (mon_caractere == '-') {
        lire('-');
        passer_espace();
    }
    nombre_non_signe();
    passer_espace();
}

void facteur() {
    if (mon_caractere == '(') {
        lire('(');
        expression();
        lire(')');
    } else {
        nombre();
    }
    passer_espace();
}

int main(/* int argc, char** argv */){

    amorcer();
    while (mon_caractere != EOF) {
        calcul();
    }

}