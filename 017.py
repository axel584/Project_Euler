import num2words


somme = 0 
for i in range(1,1000+1) :
	mot = num2words.num2words(i)
	print(i,mot)
	mot = mot.replace(' ','')
	mot =mot.replace('-','')
	somme += len(mot)
print(somme)