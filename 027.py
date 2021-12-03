from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
    
def max_prime(a,b):
    n = 0
    while True :
        polynome = n**2 + a*n + b
        #print("polynome",n,polynome)
        if not isPrime(polynome):
            return n
        n += 1    
    
max = 0     
for a in range(-1000,1000) :
    for b in range(-1000,1000 ):
        max_ab = max_prime(a,b)
        #print("max_ab",a,b,max_ab)
        if max_ab>max :
            print(a*b) # la derniere valeur est la bonne
            max = max_ab

