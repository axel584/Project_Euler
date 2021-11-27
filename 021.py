# -*- coding: utf-8 -*-
import math

def diviseur(n):
	somme = 0
	for i in range(1,n) :
		if n%i==0 :
			somme += i
	return somme		
   

somme = 0 
for i in range(1,10000) :
	diviseur_i =diviseur(i) 
	if diviseur(diviseur_i)==i and i!=diviseur_i:
		print(i,diviseur(i))
		somme +=i
print(somme) 