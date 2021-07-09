#include <stdio.h>

#include <time.h>

#include <stdlib.h>



int min_2(int a, int b){

    if(a < b){

        return a;

    }

    return b;

}



int min_3(int a, int b, int c){

    return min_2(a, min_2(b, c));

}



int distance_levenshtein_rec(const char* mot_1, int taille_1, const char* mot_2, int taille_2){

    if(taille_1 == 0){

        return taille_2;

    }

    if(taille_2 == 0){

        return taille_1;

    }

    if(mot_1[0] == mot_2[0]){

        return distance_levenshtein_rec(mot_1+1, taille_1-1, mot_2+1, taille_2-1);

    }

    return 1 + min_3(

        distance_levenshtein_rec(mot_1+1, taille_1-1, mot_2, taille_2),

        distance_levenshtein_rec(mot_1, taille_1, mot_2+1, taille_2-1),

        distance_levenshtein_rec(mot_1+1, taille_1-1, mot_2+1, taille_2-1));

}




long long int fibo_rec(int rang){

    if(rang <= 1){

        return 1;

    }else{

        return fibo_rec(rang-1) + fibo_rec(rang-2);

    }

}



void init_tab(long long int tab[], int rang){

    tab[0] = 1;

    if(rang>=2){

        tab[1] = 1;

    }

}



long long int fibo_dyn(int rang){

    long long int tab_fib[rang+1];

    init_tab(tab_fib, rang);

    for(int i=2; i <= rang; i++){

        tab_fib[i] = tab_fib[i-1] + tab_fib[i - 2];

    }

    return tab_fib[rang];

}




void test_algo(long long int f(int), int rang){

    time_t mon_debut, ma_fin;

    long long int res;

    mon_debut = time(NULL);

    res = f(rang);

    ma_fin = time(NULL);

    printf("%lld en %ld sec \n", res, ma_fin - mon_debut);

}




int main(){

    test_algo(fibo_rec, 5);

    test_algo(fibo_rec, 15);

    test_algo(fibo_rec, 30);

    test_algo(fibo_rec, 35);

    test_algo(fibo_rec, 40);

    test_algo(fibo_rec, 45);




    test_algo(fibo_dyn, 5);

    test_algo(fibo_dyn, 15);

    test_algo(fibo_dyn, 30);

    test_algo(fibo_dyn, 35);

    test_algo(fibo_dyn, 40);

    test_algo(fibo_dyn, 45);



    printf("distance entre %s et %s = %d", "bonjour", "bonsoir", distance_levenshtein_rec("bonjour", 8, "bonsoir", 8));

    printf("distance entre %s et %s = %d", "bonjour", "bonsoir", distance_levenshtein_dyn("bonjour", 8, "bonsoir", 8));

    return 0;

}