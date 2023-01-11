"""
    10'un altında 3 veya 5'in katı olan tüm doğal sayıları listelersek 3, 5, 6 ve 9 elde ederiz. Bu katların toplamı 23'tür.

    1000'in altındaki 3 veya 5'in tüm katlarının toplamını bulun.

"""

toplam = 0

for i in range(1,1000):
    if(i%3==0 or i%5==0):
        toplam += i

print(toplam)