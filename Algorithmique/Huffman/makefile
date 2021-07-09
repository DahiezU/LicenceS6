compile = gcc
opt = -c -Wall -Wextra -std=gnu99

compresseur.exe: compresseur.o p_analyseur.o p_arbre.o noeud/p_noeud.o element_int/p_element_int.o utilitaires/p_utilitaires.o
	${compile} -o compresseur.exe compresseur.o p_analyseur.o p_arbre.o noeud/p_noeud.o element_int/p_element_int.o utilitaires/p_utilitaires.o

compresseur.o : compresseur.c
	${compile} ${opt} compresseur.c

p_analyseur.o : p_analyseur.c p_analyseur.h
	${compile} ${opt} p_analyseur.c

p_arbre.o : p_arbre.c p_arbre.h
	${compile} ${opt} p_arbre.c

noeud/p_noeud.o : noeud/p_noeud.c noeud/p_noeud.h
	${compile} ${opt} noeud/p_noeud.c 
	mv p_noeud.o noeud/p_noeud.o 

element_int/p_element_int.o : element_int/p_element_int.c element_int/p_element_int.h
	${compile} ${opt} element_int/p_element_int.c 
	mv p_element_int.o element_int/p_element_int.o 

utilitaires/p_utilitaires.o : utilitaires/p_utilitaires.c utilitaires/p_utilitaires.h
	${compile} ${opt} utilitaires/p_utilitaires.c 
	mv p_utilitaires.o utilitaires/p_utilitaires.o