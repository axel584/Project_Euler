import itertools

somme = []
for permutation in itertools.permutations('123456789') :
	nombre = ''.join(permutation)
	#print("nombre",nombre)
	for longueur_multiplicand in range(1,10) :
		for longueur_multiplier in range(1,10) :
			if longueur_multiplicand+longueur_multiplier>=9 :
				break
			multiplicand = int(nombre[:longueur_multiplicand])
			multiplier = int(nombre[longueur_multiplicand:longueur_multiplicand+longueur_multiplier])
			#
			product = int(nombre[longueur_multiplicand+longueur_multiplier:])
			#print(longueur_multiplicand,longueur_multiplier,multiplicand,multiplier,product)
			if multiplicand*multiplier==product :
				print(longueur_multiplicand,longueur_multiplier,multiplicand,multiplier,product)
				if not product in somme :
					somme.append(product)
print(sum(somme))
