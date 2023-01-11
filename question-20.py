"""
    n ! n * ( n - 1) - ... * 3 * 2 * 1 anlamına gelir

    Örneğin, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800
    ve 10 sayısındaki rakamların toplamı! 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27'dir.

    100 sayısındaki rakamların toplamını bulun!

"""

def factoriel(number):
    carpim = 1
    for i in range(1,number+1):
        carpim *= i
    return carpim

string_factoriel_number = str(factoriel(100))

toplam = 0
for i in string_factoriel_number:
    toplam += int(i)

print(toplam)