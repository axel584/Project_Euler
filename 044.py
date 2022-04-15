

pentagonal = [0]
for i in range(1,10000) :
	pent_i=i*((3*i)-1)/2
	pentagonal.append(pent_i)

minimum = 10000000
for j in range(2,10000):
	for k in range(1,j) :
		addition = pentagonal[j]+pentagonal[k]
		soustraction = pentagonal[j]-pentagonal[k]
		if addition in pentagonal and soustraction in pentagonal :
			print(pentagonal[j],pentagonal[k])
			if soustraction<minimum :
				minimum = soustraction
print(minimum)				
