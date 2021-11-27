# -*- coding: utf-8 -*-
import math

def is_perfect(n):
	somme = 0 
	for i in range(1,n) :
		if n%i==0 :
			somme += i
	return n==somme

def is_abundant(n):
	somme = 0 
	for i in range(1,n) :
		if n%i==0 :
			somme += i
	return n<somme

tab_abundants = []

for i in range(1,28123) :
	if is_abundant(i) :
		tab_abundants.append(i)
tab_somme = []
for i in tab_abundants :
	for j in tab_abundants :
		if not (i+j) in tab_somme :
			tab_somme.append(i+j)
somme = 0
for i in range(1,28212) :
	if not i in tab_somme :
		somme += i 
print(somme)		


