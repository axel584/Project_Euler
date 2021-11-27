

def factorielle(n):
    if n == 0:
        return 1
    else:
        return n  * factorielle(n-1)

fact_cent = factorielle(100)        

somme = 0
for chiffre in str(fact_cent):
	somme += int(chiffre)

print(somme)	