"""
    2 üssü 15 = 32768 ve rakamları toplamı 3 + 2 + 7 + 6 + 8 = 26'dır.

    2 üssü 1000 sayısının rakamları toplamı kaçtır ?

"""

def us_alma(taban,us):
    return taban ** us

sayi = str(us_alma(2,1000))

rakamlar_toplami = 0
for i in sayi:
    rakamlar_toplami += int(i)

print(rakamlar_toplami)