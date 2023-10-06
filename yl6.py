# Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi (ära kasuta max funktsiooni). (loogikatehted - logic operators)

a =int(input("Sisesta esimene arv: "))
b =int(input("Sisesta teine arv: "))
c = int(input("Sisesta kolmas arv: "))
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)