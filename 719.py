import math
import itertools

def is_square(i: int):
    return i == math.sqrt(i) ** 2

def is_S(n) :
    if not is_square(n) :
        return False
    for element in splitter(str(n)) :
        if sum([int(x) for x in element])==math.sqrt(n) :
            return True
    return False
    
def splitter(str):
    for i in range(1, len(str)):
        start = str[0:i]
        end = str[i:]
        yield ([start, end])
        for split in splitter(end):
            result = [start]
            result.extend(split)
            yield result

max = int(math.sqrt(10**12))
somme = 0
for i in range(max+1) :
    carre = i**2
    if is_S(carre) :
        print(carre)
        somme += carre
print(somme)        
    