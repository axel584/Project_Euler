from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))	


odd_number = 9
while True :
	if not isPrime(odd_number) :
		i = 1
		twice_a_square_of_i = 2*(i**2)
		while not isPrime(odd_number-twice_a_square_of_i) :
			i+=1
			twice_a_square_of_i = 2*(i**2)
			if twice_a_square_of_i>odd_number :
				print(odd_number)
				exit()
	odd_number +=2


