


liste_triangulaire = []

for i in range(1,1000) :
	liste_triangulaire.append(int(i*(i+1)/2))

data = open('p042_words.txt').read()
liste = [name.strip('"') for name in data.split(",")]
compteur=0
for mot in liste :
	somme = 0
	for lettre in list(mot.strip()) :
		somme += ord(lettre) - 64 # valeur de A
	if somme in liste_triangulaire :
		compteur +=1	
print(compteur)