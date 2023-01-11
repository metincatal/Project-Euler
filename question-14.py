"""
    Pozitif tamsayılar kümesi için aşağıdaki yinelemeli dizi tanımlanır:

    n → n /2 ( n çifttir)
    n → 3 n + 1 ( n tektir)

    Yukarıdaki kuralı kullanarak ve 13 ile başlayarak aşağıdaki diziyi oluşturuyoruz:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    Bu dizinin (13'ten başlayıp 1'de biten) 10 terim içerdiği görülebilir. Henüz kanıtlanmamış olmasına rağmen (Collatz Problemi), tüm başlangıç ​​sayılarının 1'de bittiği düşünülmektedir.

    Bir milyonun altındaki hangi başlangıç ​​sayısı en uzun zinciri oluşturur?

    NOT: Zincir bir kez başladığında terimlerin bir milyonun üzerine çıkmasına izin verilir.

"""

zincir = {
    
}

def collatzProblem(number):
    num = number
    baslangicsiz_zincir = [num]
    while num!=1:
        if num%2==0:
            num = num/2
            baslangicsiz_zincir.append(num)
        elif num%2!=0:
            num = (3*num) + 1
            baslangicsiz_zincir.append(num)
    zincir.update({
        num : [x for x in baslangicsiz_zincir]
    })
    baslangicsiz_zincir.clear()

def problemResult():
    baslangic_sayisi = 1
    while baslangic_sayisi<10**6:
        collatzProblem(baslangic_sayisi)
        if True:
            pass