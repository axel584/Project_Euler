


eulercoin = 1504170715041707
min = eulercoin+1
somme = 0
modulo = 4503599627370517

for n in range(1,10000000000):
    res = (eulercoin*n)%modulo
    if res<min :
        print(res,somme)
        somme = somme + res
        min = res

print(somme)