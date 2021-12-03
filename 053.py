import math


compteur = 0

for n in range(1,101) :
    print(n)
    for r in range(1,n+1) :
        if math.comb(n, r)>1000000 :
            compteur += 1
print(compteur)            