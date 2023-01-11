"""
    1'den 5'e kadar olan sayılar bir, iki, üç, dört, beş kelimelerle yazılırsa, toplamda 3 + 3 + 5 + 4 + 4 = 19 harf kullanılır.

    1'den 1000'e (bin) kadar olan tüm sayılar kelimelerle yazılsaydı kaç harf kullanılırdı?


    NOT: Boşlukları veya kısa çizgileri saymayın. Örneğin, 342 (üç yüz kırk iki) 23 harf ve 115 (yüz on beş) 20 harf içerir. Sayıları yazarken "ve" kullanımı İngiliz kullanımına uygundur.

"""

def sayinin_harfleri_ilk_9(number):
    if number==1:
        return "one"
    elif number==2:
        return "two"
    elif number==3:
        return "three"
    elif number==4:
        return "four"
    elif number==5:
        return "five"
    elif number==6:
        return "six"
    elif number==7:
        return "seven"
    elif number==8:
        return "eight"
    elif number==9:
        return "nine"
    else:
        return ""

def sayinin_harfleri_10_19(number):
    if number==10:
        return "ten"
    elif number==11:
        return "eleven"
    elif number==12:
        return "twelve"
    elif number==13:
        return "thirteen"
    elif number==14:
        return "fourteen"
    elif number==15:
        return "fifteen"
    elif number==16:
        return "sixteen"
    elif number==17:
        return "seventeen"
    elif number==18:
        return "eighteen"
    elif number==19:
        return "nineteen"

def sayinin_harfleri_20_100_10(number):
    if number==2:
        return "twenty"
    elif number==3:
        return "thirty"
    elif number==4:
        return "fourty"
    elif number==5:
        return "fifty"
    elif number==6:
        return "sixty"
    elif number==7:
        return "seventy"
    elif number==8:
        return "eighty"
    elif number==9:
        return "ninety"

def basamak_sayisi(number):
    strnumber = str(number)
    if len(strnumber)==1:
        sayinin_harfi1 = sayinin_harfleri_ilk_9(number)
        return sayinin_harfi1
    elif len(strnumber)==2:
        sayinin_rakamlari2 = [x for x in strnumber]
        if sayinin_rakamlari2[0] == "1":
            return sayinin_harfleri_10_19(number)
        else:
            ilk_basamak2 = sayinin_harfleri_20_100_10(int(sayinin_rakamlari2[0]))
            ikinci_basamak2 = sayinin_harfleri_ilk_9(int(sayinin_rakamlari2[1]))
            return ilk_basamak2+ikinci_basamak2
    elif len(strnumber)==3:
        sayinin_rakamlari3 = [x for x in strnumber]
        ilk_basamak3 = sayinin_harfleri_ilk_9(int(sayinin_rakamlari3[0]))+"hundred"
        ikinci_basamak3 = sayinin_harfleri_20_100_10(int(sayinin_rakamlari3[1]))
        ucuncu_basamak3 = sayinin_harfleri_ilk_9(int(sayinin_rakamlari3[2]))

        if sayinin_rakamlari3[1]=="0" and sayinin_rakamlari3[2]=="0":
            return ilk_basamak3
        elif sayinin_rakamlari3[1]=="0" and sayinin_rakamlari3[2]!="0":
            ilk_basamak3 += "and"
            return ilk_basamak3+ucuncu_basamak3
        elif sayinin_rakamlari3[1]=="1":
            ilk_basamak3 += "and"+sayinin_harfleri_10_19(int(sayinin_rakamlari3[1]+sayinin_rakamlari3[2]))
            return ilk_basamak3
        elif sayinin_rakamlari3[1]!="0" and sayinin_rakamlari3[1]!="1" and sayinin_rakamlari3[2]=="0":
            ilk_basamak3 += "and"
            return ilk_basamak3+ikinci_basamak3
        elif sayinin_rakamlari3[1]!="0" and sayinin_rakamlari3[1]!="1" and sayinin_rakamlari3[2]!="0":
            ilk_basamak3 += "and"
            return ilk_basamak3+ikinci_basamak3+ucuncu_basamak3

toplam = 11
for i in range(1,1000):
    toplam += len(basamak_sayisi(i))
    print(basamak_sayisi(i))

print(toplam)