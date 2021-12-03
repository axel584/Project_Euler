

def isPalindrome(nombre) :
    return str(nombre)[::-1]==str(nombre)

def isLychrel(nombre) :
    iteration = 1
    while iteration<50 :
        inverse = int(str(nombre)[::-1])
        nombre += inverse
        if isPalindrome(nombre) :
            return False
        iteration +=1
    return True
    
compteur = 0
for nombre in range(1,10000):
    if isLychrel(nombre) :
        compteur += 1
print(compteur)        

