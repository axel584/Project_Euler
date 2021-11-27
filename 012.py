

def liste_facteur(nombre) : 
    resultat = 2
    for i in range(2,nombre):
        if nombre%i==0 :
            resultat += 1
    return resultat

indice = 1
triangle = 0
while True :
    triangle += indice
    if liste_facteur(triangle)>500 :
        print(triangle)
        exit()
    indice += 1