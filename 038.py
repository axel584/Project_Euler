

def isPandigital(nombre) :
	if len(str(nombre))!=9 :
		return False
	return sorted(str(nombre))==['1','2','3','4','5','6','7','8','9']

max = 0
for n in range(1,10) :
	for i in range(10000) :
		concatenation = ""
		for chiffre in range(1,n+1) :
			concatenation+=str(chiffre*i)
		if isPandigital(concatenation) :
			if int(concatenation)>max :
				max=int(concatenation)

print(max)				