"""
    Palindromik bir sayı her iki şekilde de aynı şekilde okunur. İki basamaklı iki sayının çarpımından yapılan en büyük palindrom 9009 = 91 * 99'dur.

    3 basamaklı iki sayının çarpımından oluşan en büyük palindromu bulun.

"""

def palindrome_check(number: int):
    str_number = str(number)
    liste = [x for x in str_number]
    palindromik_sayi_mi = False

    if (len(liste)==5):
        a, b = liste[0], liste[1]
        if (a==liste[len(liste)-1]) and (b==liste[len(liste)-2]):
            palindromik_sayi_mi = True
            return palindromik_sayi_mi
    elif (len(liste)==6):
        x, y, z = liste[0], liste[1], liste[2]
        if (x==liste[len(liste)-1]) and (y==liste[len(liste)-2]) and (z==liste[len(liste)-3]):
            palindromik_sayi_mi = True
            return palindromik_sayi_mi

a = 999
b = 999

list = []

while a>99:
    for b in range(100,1000):
        if(palindrome_check(a*b)):
            list.append(a*b)
            break
    a -= 1

print(max(list))