

def is_palindrome(nombre) :
    return str(nombre)==str(nombre)[::-1]

max = 0
for i in range(100,1000) :
    for j in range(100,1000) :
        if is_palindrome(i*j) :
            if max<i*j :
                max = i*j
print(max) # le plus grand palindrome                