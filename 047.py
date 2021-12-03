from math import sqrt
from itertools import count, islice
import functools


# attention valable uniquement en python 3
@functools.lru_cache
def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))	 

def intersection(lst1, lst2):
	lst3 = [value for value in lst1 if value in lst2]
	return lst3

@functools.lru_cache
def primeFactors(n):
	resultat = {}
	# Print the number of two's that divide n
	while n % 2 == 0:
		if not 2 in resultat :
			resultat[2]=1
		else :
			resultat[2]+=1
		n = n / 2
		 
	# n must be odd at this point
	# so a skip of 2 ( i = i + 2) can be used
	for i in range(3,int(sqrt(n))+1,2):
		 
		# while i divides n , print i and divide n
		while n % i== 0:
			if not i in resultat :
				resultat[int(i)]=1
			else :
				resultat[int(i)]+=1
			n = n / i
			 
	# Condition if n is a prime
	# number greater than 2
	if n > 2:
		if not n in resultat :
			resultat[int(n)]=1
		else :
			resultat[int(i)]+=1
	vrai_resultat = []		
	for i in resultat.keys() :
		vrai_resultat.append(int(i**resultat[i]))
	return vrai_resultat	


nombre = 10
while True :
	premier = primeFactors(nombre)
	if len(premier)!=4 :
		nombre += 1  
		continue
	deuxieme = primeFactors(nombre+1)
	if len(deuxieme)!=4 :
		nombre += 1  
		continue
	troisieme = primeFactors(nombre+2)
	if len(troisieme)!=4 :
		nombre += 1  
		continue
	quatrieme = primeFactors(nombre+3)
	if len(quatrieme)!=4 :
		nombre += 1  
		continue
	if len(intersection(premier,deuxieme))==0 and len(intersection(premier,troisieme))==0 and len(intersection(premier,quatrieme))== 0 and len(intersection(deuxieme,troisieme))== 0 and len(intersection(deuxieme,quatrieme))== 0 and len(intersection(troisieme,quatrieme))== 0:
		print(premier,deuxieme,troisieme,quatrieme)
		print(nombre)
		exit()
	nombre += 1  
