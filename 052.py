

def haveSameNumber(a,b) :
    return "".join(sorted(str(a)))=="".join(sorted(str(b)))


nombre = 1
while True :
    if haveSameNumber(nombre,2*nombre) and haveSameNumber(nombre,3*nombre) and haveSameNumber(nombre,4*nombre) and haveSameNumber(nombre,5*nombre) and haveSameNumber(nombre,6*nombre) :
        print(nombre)
        exit()
    nombre += 1
        