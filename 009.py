

for a in range(1000) :
    for b in range(1000) :
        for c in range(1000) :
            if a + b + c > 1000 :
                break
            if (a*a + b*b != c*c) :
                continue
            if a + b + c == 1000 : 
                print(a,b,c,a*b*c)
                
   