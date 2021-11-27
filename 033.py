


for denominateur in range(10,100):
	for numerateur in range(10,denominateur) :
		if numerateur==denominateur :
			break
		if str(denominateur)[0]==str(numerateur)[1] :
			numerateur_simplifie = int(str(numerateur)[0])
			denominateur_simplifie = int(str(denominateur)[1])
			if numerateur*denominateur_simplifie==numerateur_simplifie*denominateur :
				print(numerateur,denominateur,numerateur_simplifie,denominateur_simplifie)	