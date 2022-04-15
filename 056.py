

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
    
max = 0 
i = 0
for a in range(1,100):
    for b in range(1,100):
        i = i +1
        nombre = a**b
        #print(nombre)
        #print(list(str(nombre)))
        #print([int(a) for a in list(str(nombre))])
        somme = sum([int(a) for (a) in list(str(nombre))])
        #print(a,b,nombre,somme)
        if somme>max :
            max = somme
print(max)            

