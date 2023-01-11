"""
    10'un altındaki asal sayıların toplamı 2 + 3 + 5 + 7 = 17'dir.

    İki milyonun altındaki tüm asal sayıların toplamını bulun.

"""

import math

def asal_mi(number):
    asal_mi = True
    if(number==2):
        return True
    else:
        for i in range(2,int(math.sqrt(number))+1):
            if(number%i==0):
                asal_mi = False
                break
        return asal_mi

a = 2
asal_sayi_toplami = 0

while True:
    if (asal_mi(a)):
        asal_sayi_toplami += a
    if a == 2*(10**6):
        break
    a += 1

print(asal_sayi_toplami)