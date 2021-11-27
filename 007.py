from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
    
i = 1 
compteur = 0    
while True :    
    if isPrime(i) :
        compteur += 1
    if compteur==10001 :
        print(i)
        exit()
    i += 1