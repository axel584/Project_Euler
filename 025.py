
fibo=1
fibo_prec = 0
indice = 1
while True :
    fibo_new = fibo + fibo_prec
    fibo_prec=fibo    
    indice +=1
    fibo = fibo_new
    if len(str(fibo))==1000 :
    	print(indice)
    	exit()
    

