"""
    2520, 1'den 10'a kadar olan sayıların her birine kalansız bölünebilen en küçük sayıdır.

    1'den 20'ye kadar olan sayıların tamamına tam bölünebilen en küçük pozitif sayı kaçtır ?

"""

liste = [1]

def cagirma():
    a = 1
    for list in liste:
        a *= list
    return a

def cagirma2(number):
    d = 1
    liste2 = []
    for b in liste:
        if(number%b==0):
            liste2.append(b)
        else:
            continue
    
    for c in liste2:
        d *= c
    return d

def en_kucuk_sayi(number):
    for i in range(2,number+1):
        if(cagirma()%i!=0):
            liste.append(i//cagirma2(i))
        else:
            continue

en_kucuk_sayi(20)
print(liste)

b = 1

for i in liste:
    b *= i

print(b)