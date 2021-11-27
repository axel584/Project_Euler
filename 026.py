# -*- coding: utf-8 -*-
from decimal import *

getcontext().prec = 50000


def find_max(chaine) :
	longueur = 10
	nb_occurence_prec = 0
	indice_fin = len(chaine)-longueur
	delta = 5
	while True :
		pattern = chaine[indice_fin:delta]
		indice_debut = chaine[:indice_fin-longueur].rfind(pattern)
		if nb_occurence_prec > chaine.count(pattern) : # ici on a trouve moins d'elements
			return longueur-1
		nb_occurence_prec = chaine.count(pattern)		
		longueur += 1
		if longueur>15 :
			return


for i in range(900,1000) :
	reponse = str(Decimal(1) / Decimal(i))
	milieu = len(reponse)/2
	longueur = 200
	pattern = reponse[milieu:milieu+longueur]
	count_pattern  = reponse.count(pattern)
	if count_pattern>1 and count_pattern<100 :
		print(i)
		print(pattern)
		print(count_pattern)
		print("--------------")


# max_taille_pattern = 0
# for i in range(1,1000) :
# 	reponse = str(Decimal(1) / Decimal(i))
# 	taille_pattern = find_max(reponse)
# 	if taille_pattern>max_taille_pattern:
# 		print(i,taille_pattern)
# 		max_taille_pattern=taille_pattern	

#1/38 = 0.026315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684210526315789473684