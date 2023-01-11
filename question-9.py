"""
    Bir Pisagor üçlüsü, a < b < c olmak üzere üç doğal sayı kümesidir, bunun için,

    a**2 + b**2 = c**2
    Örneğin, 3**2 + 4**2 = 9 + 16 = 25 = 5**2

    a + b + c = 1000 olan tam olarak bir Pisagor üçlüsü vardır. abc
    çarpımını bulun.

"""

def pisagor_mu(a,b,c):
    if (a**2+b**2==c**2):
        return True
    else:
        return False

for a in range(1,1001):
    for b in range(1,1001):
        for c in range(1,1001):
            if (pisagor_mu(a,b,c) and (a+b+c==1000)):
                print(a*b*c)