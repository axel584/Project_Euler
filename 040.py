

chaine = ""
for i in range(1000000) :
	chaine += str(i)

print(int(chaine[1])*int(chaine[10])*int(chaine[100])*int(chaine[1000])*int(chaine[10000])*int(chaine[100000])*int(chaine[1000000]))

