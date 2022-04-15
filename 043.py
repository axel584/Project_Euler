import itertools

somme = 0
for permutation in itertools.permutations("0123456789") :
	nombre = "".join(permutation)
	if int(nombre[1:4])%2 == 0 and int(nombre[2:5])%3 == 0 and int(nombre[3:6])%5 == 0 and int(nombre[4:7])%7 == 0 and int(nombre[5:8])%11 == 0 and int(nombre[6:9])%13 == 0 and int(nombre[7:10])%17 == 0 :
		print(nombre)
		somme += int(nombre)
print(somme)		