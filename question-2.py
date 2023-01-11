"""
    Fibonacci dizisindeki her yeni terim, önceki iki terimin eklenmesiyle oluşturulur. 1 ve 2 ile başlayarak, ilk 10 terim şöyle olacaktır:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    Fibonacci dizisindeki değerleri dört milyonu geçmeyen terimleri dikkate alarak çift değerli terimlerin toplamını bulunuz.

"""

a = 1
b = 2
liste = [1,2]
toplam = 0

def listenin_son_iki_teriminin_toplami(liste):
    uzunluk = len(liste)
    son_iki_terim = liste[uzunluk-2:uzunluk]
    son_iki_terimin_toplami = son_iki_terim[0] + son_iki_terim[1]
    return son_iki_terimin_toplami

def fibonacci(number):
    while liste[len(liste)-1]<number:
        liste.append(listenin_son_iki_teriminin_toplami(liste))

    liste.pop()

fibonacci(4*(10**6))

for fib in liste:
    if(fib%2==0):
        toplam += fib

print(toplam)