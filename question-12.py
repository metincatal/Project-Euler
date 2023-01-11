"""
    Üçgen sayıları dizisi, doğal sayıların eklenmesiyle oluşturulur. Yani 7. üçgen sayısı 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28 olur. İlk on terim şöyle olur:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    İlk yedi üçgen sayısının çarpanlarını sıralayalım:

    1 : 1
    3 : 1,3
    6 : 1,2,3,6
    10 : 1,2,5,10
    15 : 1,3,5,15
    21 : 1,3,7,21
    28 : 1,2, 4,7,14,28
    28'in beşten fazla böleni olan ilk üçgen sayı olduğunu görebiliriz.

    Beş yüzden fazla böleni olan ilk üçgen sayısının değeri kaçtır?

"""

carpan_listesi = {
    
}

ucgen_sayi = 1
artis = 1
ucgen_sayi_carpanlarinin_uzunlugunun_listesi = []
kontrol = True

while kontrol:
    ucgen_sayinin_carpanlari = []

    for i in range(1,ucgen_sayi+1):
        if ucgen_sayi%i==0:
            ucgen_sayinin_carpanlari.append(i)

    ucgen_sayi_carpanlarinin_uzunlugunun_listesi.append(len(ucgen_sayinin_carpanlari))

    carpan_listesi.update({
        ucgen_sayi : [x for x in ucgen_sayinin_carpanlari]
    })

    for a in ucgen_sayi_carpanlarinin_uzunlugunun_listesi:
        if(a>500):
            print(max(ucgen_sayi_carpanlarinin_uzunlugunun_listesi))
            kontrol = False

    artis += 1
    ucgen_sayi += artis