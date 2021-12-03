

nombre = 2
somme = 0
while True :
    tableau = [int(x) for x in str(nombre)]
    total = sum([x**5 for x in tableau])
    if total == nombre :
        print(nombre)
        somme += nombre
    nombre += 1
    if nombre>10000000 :
        break
print(somme)    
