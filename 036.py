
somme = 0
for i in range(1,1000000) :
	if str(i)!=str(i)[::-1] :
		continue
	ibin = str(bin(i))[2:]
	if ibin!=ibin[::-1] :
		continue
	print("palindrome",i)		
	somme += i
	# tester en base 2

print(somme)	