

def is_divisible(nombre) :
    for div in range(1,20) :
        if nombre%div!=0 :
            return False
    return True

i = 1
while True :
    if is_divisible(i) :
        print(i)
        exit()
    i = i +1
            