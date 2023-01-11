"""
    2×2 ızgaranın sol üst köşesinden başlayarak ve yalnızca sağa ve aşağı hareket edebilen, sağ alt köşeye giden tam 6 yol vardır.


    20 × 20 ızgarada böyle kaç rota var?

"""

"""
    https://www.youtube.com/watch?v=6O2IEgrgMCM&list=PL3kMAPso9YQ16WNFwFPjFAoGTVbMMmeV-&index=19

"""

"""
    tekrarlı permütasyon

"""

def factoriel(num):
    factoriel = 1
    for i in range(1,num+1):
        factoriel *= i
    return factoriel

steps = factoriel(40) // (factoriel(20) * factoriel(20))
print(steps)