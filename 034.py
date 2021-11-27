def factorielle(n):
    if n == 0:
        return 1
    else:
        return n  * factorielle(n-1)

somme = 0
for i in range(5,1000000) :
	somme_chiffre = 0
	for chiffre in str(i):
		somme_chiffre += factorielle(int(chiffre))
	if somme_chiffre==i :
		print(somme_chiffre)
		somme+=i

print(somme)