import itertools
from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))	

max = 0
for n in range(1,10) :
	for permutation in itertools.permutations("".join([str(x) for x in range(1,n+1)])) :
		nombre = int("".join(permutation))
		if nombre>max and isPrime(nombre) :
			max = nombre
print(max)			

