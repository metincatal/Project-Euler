"""
    d( n ), n'nin ( n'ye eşit olarak bölünen n'den küçük sayılar ) uygun bölenlerinin toplamı olarak tanımlansın . d( a ) = b ve d( b ) = a ise, burada a ≠ b , o zaman a ve b dostane bir çifttir ve a ve b'nin her birine dost sayılar denir.

    Örneğin, 220'nin uygun bölenleri 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 ve 110'dur; bu nedenle d(220) = 284. 284'ün uygun bölenleri 1, 2, 4, 71 ve 142'dir; yani d(284) = 220.

    10000'in altındaki tüm dostane sayıların toplamını değerlendirin.

"""

def dostane_fonksiyonu(number):
    carpanlar = []
    for i in range(1,number):
        if number%i==0:
            carpanlar.append(i)
    toplam = 0
    for a in carpanlar:
        toplam += a
    
    return toplam

number = 1
dostane_sayilarin_toplami = 0
while number<10**4:
    dostane_sayinin_carpanlarinin_toplami = dostane_fonksiyonu(number)
    if dostane_fonksiyonu(dostane_sayinin_carpanlarinin_toplami)==number:
        if dostane_sayinin_carpanlarinin_toplami!=number:
            dostane_sayilarin_toplami += number
    number += 1

print(dostane_sayilarin_toplami)