"""
    İlk altı asal sayıyı listeleyerek: 2, 3, 5, 7, 11 ve 13, 6. asal sayının 13 olduğunu görebiliriz.

    10001. asal sayı kaçtır?

"""

import math

def asalmi(number):
    asalmi = True
    for i in range(2,int(math.sqrt(number))+1):
        if(number%i==0):
            asalmi = False
    
    return asalmi

a = 2
asal_sayi_listesi = []

while len(asal_sayi_listesi)<10001:
    if(asalmi(a)):
        asal_sayi_listesi.append(a)
    a += 1

print(len(asal_sayi_listesi))
print(asal_sayi_listesi[10000])
print(asalmi(asal_sayi_listesi[10000]))