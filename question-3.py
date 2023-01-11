"""
    13195'in asal çarpanları 5, 7, 13 ve 29'dur.

    600851475143 sayısının en büyük asal çarpanı kaçtır?

"""

import math

def asal_mi(number:int):
    asal_mi = True

    for i in range(2,int(math.sqrt(number))+1):
        if(number%i==0):
            asal_mi = False
            continue

    return asal_mi

en_buyuk_asal = 1
number = 600851475143

for i in range(2,int(math.sqrt(number))):
    if (number%i==0) and (asal_mi(i)):
        en_buyuk_asal = i

print(en_buyuk_asal)