# -*- coding: utf-8 -*-

data = open('p067_triangle.txt').read()

structure = [ligne.split(' ') for ligne in data.split('\n')]

nb_lignes = len(structure)
print(nb_lignes)

# on passe la dernière ligne en int
num_nombre = 0
for nombre in structure[nb_lignes-1] :
	structure[nb_lignes-1][num_nombre] = int(nombre)
	num_nombre += 1

num_ligne = nb_lignes-2
for ligne in structure[nb_lignes-2::-1] :
	num_nombre = 0
	for nombre in ligne :
		structure[num_ligne][num_nombre] = int(structure[num_ligne][num_nombre]) + max(structure[num_ligne+1][num_nombre],structure[num_ligne+1][num_nombre+1])
		num_nombre += 1
	num_ligne -=1	
print(structure[0][0])	