
somme = 0
fibo=1
fibo_prec = 0
while fibo<4000000 :
    fibo_new = fibo + fibo_prec
    if fibo_new%2==0 :
        somme = somme + fibo_new
    fibo_prec=fibo    
    fibo = fibo_new
print(somme)    
