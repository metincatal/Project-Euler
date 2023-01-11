"""
    İlk 10 doğal sayının karelerinin toplamı,
        1**2 + 2**2 + 3**2 + ... + 10**2 = 385

    İlk 10 doğal sayının toplamının karesi,
        (1+2+3+...+10)**2 = 55**2 = 3025

    Dolayısıyla ilk on doğal sayının kareleri toplamı ile toplamın karesi arasındaki fark, 3025 - 385 = 2640

    İlk yüz doğal sayının kareleri toplamı ile toplamın karesi arasındaki farkı bulun.

"""

def fark(number):
    karelerinin_toplami = 0
    toplam = 0
    toplamin_karesi = 0

    for i in range(1,number+1):
        karelerinin_toplami += i**2
        toplam += i
    toplamin_karesi = toplam**2

    print(toplamin_karesi - karelerinin_toplami)

fark(100)