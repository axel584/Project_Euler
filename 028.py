

indice = 1
taille_pas = 1
nb_pas = 0
somme = -1

while True :
    #print("indice",indice,nb_pas,somme)
    #print("taille_pas",taille_pas)
    #print("nb_pas",nb_pas)
    if nb_pas%4==1 :
        somme += (indice-1) # apres avoir ete a droite, il faut prendre la valeur precedente
    else :
        somme += indice 
    indice = indice + taille_pas
    nb_pas += 1
    taille_pas = (nb_pas // 2)+1
    
    
    if nb_pas>2001 :
        break
print("indice",indice,nb_pas,somme)    
print(somme)    
    
