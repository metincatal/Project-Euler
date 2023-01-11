"""
    Mükemmel sayı, uygun bölenlerinin toplamı tam olarak sayıya eşit olan bir sayıdır. Örneğin, 28'in uygun bölenlerinin toplamı 1 + 2 + 4 + 7 + 14 = 28 olacaktır, bu da 28'in mükemmel bir sayı olduğu anlamına gelir.

    Bir n sayısı , uygun bölenlerinin toplamı n'den küçükse eksik, bu toplam n'yi aşarsa bol olarak adlandırılır .

    12 en küçük bol sayı olduğundan, 1 + 2 + 3 + 4 + 6 = 16 iki bol sayının toplamı olarak yazılabilecek en küçük sayı 24'tür. 28123 iki bol sayının toplamı olarak yazılabilir. Ancak bu üst sınır, iki bol sayının toplamı olarak ifade edilemeyen en büyük sayının bu sınırdan küçük olduğu bilinmesine rağmen analizlerle daha fazla düşürülemez.

    İki bol sayının toplamı olarak yazılamayan tüm pozitif tam sayıların toplamını bulun.

"""

























# def carpanlarinin_toplami(number):
#     toplam = 0
#     for i in range(1,number):
#         if number%i==0:
#             toplam += i
#     return toplam

# def dizi_elemanlarinin_ikiserli_toplamlari(liste_uzunlugu):
#     toplam = 0
#     for i in range(liste_uzunlugu-1,0,-1):
#         toplam += i
#     return toplam

# bol_sayilar = []
# for a in range(1,28112):
#     if carpanlarinin_toplami(a)>a:
#         bol_sayilar.append(a)
# iki_bol_sayinin_toplami = []
# artis = 0
# for x in range(artis,len(bol_sayilar)-1):
#     for y in range(artis+1,len(bol_sayilar)):
#         if(bol_sayilar[x]+bol_sayilar[y]<28112):
#             iki_bol_sayinin_toplami.append(bol_sayilar[x]+bol_sayilar[y])
#     artis += 1

# result = 0
# for z in range(0,28112):
#     if z not in iki_bol_sayinin_toplami:
#         result += 1

# print(result)