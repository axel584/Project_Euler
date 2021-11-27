import itertools

i = 1
for element in itertools.permutations('0123456789') :
	if i==1000000 :
		print(''.join(element))
		exit()
	i += 1	
