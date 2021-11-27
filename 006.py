
somme = 0
somme_des_carres = 0
for i in range(101) :
    somme = somme + i
    somme_des_carres = somme_des_carres + i*i
    
print(somme_des_carres)
print(somme)    
print(somme * somme - somme_des_carres) # somme des carrees moins le carre des sommes    