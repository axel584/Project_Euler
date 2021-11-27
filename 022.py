

def value(nom) :
	print(nom)
	somme = 0
	for lettre in nom :
		somme += ord(lettre)-ord('A') + 1
	return somme

data = open('p022_names.txt').read()
liste = [name.strip('"') for name in data.split(",")]
liste.sort()
somme = 0
indice = 1
for nom in liste :
	somme += indice * value(nom)
	indice += 1
print(somme)
