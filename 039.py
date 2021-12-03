import math

max_solution = 0
max_p = 0
for p in range(1,1001) :
	nb_solution = 0
	for a in range(1,p) :
		for b in range(1,p) :
			c = math.sqrt(a*a+b*b)
			if c.is_integer() :
				if a+b+c==p :
					nb_solution+=1
	if nb_solution>max_solution:
		max_p=p
		max_solution=nb_solution
print(max_p)						
