from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))	

somme = 0
for nombre in range(1000000) :
	prime = True
	for nb_boucle in range(len(str(nombre))) :
		#print("nombre",nombre)
		if not isPrime(nombre) :
			prime = False
			break
		nombre = int(str(nombre)[-1]+str(nombre)[:-1])
	if prime :
		#print("prime")
		somme += 1
print(somme)		