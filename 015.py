import math

#exemple de chemin = "RRDD"

TAILLE = 2

nombre_de_chemin = 0

def generate_lattice(debut) :
    global nombre_de_chemin
    if len(debut)==2*TAILLE :
        nombre_de_chemin += 1
        return
    number_right = debut.count('R')
    number_down = debut.count('D')
    if number_right<TAILLE :
        generate_lattice(debut+"R")
    if number_down<TAILLE :
        generate_lattice(debut+"D")
    
generate_lattice("")
print("calcul")
print(nombre_de_chemin) # trop lent pour des grands nombres    
print("par factoriel")
print(math.factorial(40) / ((math.factorial(20)*math.factorial(20)))) # combinaison possible de 20 lettres R et 20 lettres D
    