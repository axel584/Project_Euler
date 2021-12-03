from math import sqrt
from itertools import count, islice


def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))	 


def isPermutation(a,b,c) :
	return ''.join(sorted(str(a)))==''.join(sorted(str(b))) and ''.join(sorted(str(a)))==''.join(sorted(str(c)))

for nombre in range (1000,10000) :
	if not isPrime(nombre) :
		continue
	for interval in range(1,9000) :
		nombre2 = nombre + interval
		if not isPrime(nombre2) :
			continue
		nombre3 = nombre + 2*interval
		if not isPrime(nombre3) :
			continue	
		if nombre3>10000 :
			break
		if isPermutation(nombre,nombre2,nombre3) :
			print(nombre,nombre2,nombre3,isPrime(nombre),isPrime(nombre2),isPrime(nombre3))	
			print(str(nombre)+str(nombre2)+str(nombre3))	
