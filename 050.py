from math import sqrt
from itertools import count, islice


def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))	 


nombre_premier = []

for nombre in range(100000) :
	if isPrime(nombre) :
		nombre_premier.append(nombre)

max = 1
print(len(nombre_premier))
for indice_debut in range(len(nombre_premier)) :		
	for longueur in range(1,len(nombre_premier)-indice_debut+1) :
		somme = sum(nombre_premier[indice_debut:indice_debut+longueur])
		if isPrime(somme) and longueur>max and somme<1000000:
			max = longueur
			print(somme,longueur,indice_debut)
