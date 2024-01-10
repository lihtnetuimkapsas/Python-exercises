# Kirjuta programm, mis küsib kasutajalt sisendina stringi.
# Eemalda selle sisendi algusest ja lõpust tühikud.
# String peab vastama tingimustele, et selles on vähemalt seitse sümbolit ja et sümbolite arv on paarituarvuline.
# Väljasta selle stringi kolm keskmist sümbolit.
# (stringi meetodid, list)


word = input("Kirjuta oma lemmikriik: ")
word = word.strip()
print(word)

lenght = len(word)
if lenght >= 7 and lenght % 2 == 1:
    print(lenght // 2)
    middle = lenght // 2
    print(word[middle-1: middle+2])

else:

    print("Sisend ei vasta tingimustele")