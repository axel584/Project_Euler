from datetime import date

nb_dimanche =0
for annee in range(1901,2001):
	for mois in range(1,13) :
		d = date(annee,mois,1)
		if d.weekday()==6 :
			nb_dimanche += 1
print(nb_dimanche)			