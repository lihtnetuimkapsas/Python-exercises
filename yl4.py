# Kirjuta programm, mis leiab kahest kasutaja poolt sisestatud arvust miinimumi (ära kasuta min funktsiooni). 
# (muutuja - variable, tingimus - condition, if-lause - if statement)

a = int(input("Sisesta esimene arv: "))
b = int(input("Sisesta teine arv: "))

if int(a) < int(b):
    print("Miinimum on", a)
else:
    print("Miinimum on", b)