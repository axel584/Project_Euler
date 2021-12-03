

def lenght_sequence_collatz(n) :
    if n==1 :
        return 1
    if n%2==0 : # even
        return 1+lenght_sequence_collatz(n/2)
    else :
        return 1+lenght_sequence_collatz((3*n)+1)
        
max = 0        
for i in range(1,1000000) :        
    lenght_sequence_collatz_i = lenght_sequence_collatz(i)
    if lenght_sequence_collatz_i>max :
        max=lenght_sequence_collatz_i
        print(i) # on affiche le max à chaque fois qu'on en trouve un... Le dernier affiché sera le bon ;) 