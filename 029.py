
exposant = []

for a in range(2,100+1) :
    for b in range(2,100+1) :
        if not a**b in exposant :
            exposant.append(a**b)
print(len(exposant))
        