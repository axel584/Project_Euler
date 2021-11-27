from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))	


liste = []
for nombre in range(10,10000000) :
#for nombre in range(618,620) :
	if not isPrime(nombre) :
		continue
	valeur_initiale = nombre
	prime = True
	#print("nombre",nombre)
	#print("longueur",len(str(valeur_initiale))-1)
	for nbcar in range(1,len(str(valeur_initiale))) :
		#print("nb car",nbcar)
		#print("nombre avant troncature",valeur_initiale)	
		#print("nombre apres troncature",str(valeur_initiale)[nbcar:])
		nombre = int(str(valeur_initiale)[nbcar:])	
		if not isPrime(nombre) :
			prime = False
			break
		#print("tronc",nombre)
	for nbcar in range(1,len(str(valeur_initiale))) :
		#print("nb car",nbcar)
		#print("nombre avant troncature",valeur_initiale)	
		#print("nombre apres troncature",str(valeur_initiale)[nbcar:])	
		nombre = int(str(valeur_initiale)[:-nbcar])	
		if not isPrime(nombre) :
			prime = False
			break		
		#print("tronc inverse",nombre)
	if prime :
		liste.append(valeur_initiale)

print("liste : ")
print(liste)	
print("nb elements : ")
print(len(liste))
print("somme : ")
print(sum(liste))
