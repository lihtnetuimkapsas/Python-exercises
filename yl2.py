# Kirjuta programm, mis küsib kasutajalt raadiuse ja arvutab 
# ringi pindala ja ümbermõõdu. (math.pi)
# alt+shift nool üles/alla kopeerib
# alt + üles/alla liigutab reale
from math import pi

r = float(input("Sisesta raadius: "))

s = float(round(pi * r**2, 2))
c = float(round(pi * (2*r), 2))

print("Pindala:",s ,", " "Ümbermõõt:", c)