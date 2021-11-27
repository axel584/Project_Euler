

nb = 0
for l2 in range(2) : # max 2 livre = 1 piece
	for l1 in range(3) : # max en piece d'1 livre = 2 piece
		for p50 in range(5) :  # max en pice de 50 pences = 4 pieces
			for p20 in range(11) :
				for p10 in range(21) :
					for p5 in range(41) :
						for p2 in range(101) :
							for p1 in range(201) :
								if 	l2*200+l1*100+p50*50+p20*20+p10*10+p5*5+p2*2+p1>200 :
									break								
								if l2*200+l1*100+p50*50+p20*20+p10*10+p5*5+p2*2+p1==200 :
									print(l2,l1,p50,p20,p10,p5,p2,p1)
									nb += 1

print(nb)						