
triangonal = []
for i in range(1,1000000) :
	tri_i=i*(i+1)/2
	triangonal.append(tri_i)


pentagonal = []
for i in range(1,1000000) :
	pent_i=i*((3*i)-1)/2
	pentagonal.append(pent_i)

hexagonal = []
for i in range(1,1000000) :
	hex_i=i*((2*i)-1)
	hexagonal.append(hex_i)	

for nombre in triangonal : 
	if nombre in pentagonal and nombre in hexagonal :
		print(nombre)	

