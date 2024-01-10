# Küsi kasutajalt lemmikloom. Väljasta selle muutuja esimene täht.
# Koosta list, mis koosneb kolmest loomast.
# Lisa selle listi lõppu kasutaja sisestatud lemmikloom.
# Väljasta see lemmikloomade list.
# Väljasta listi viimase elemendi viimane täht.
# (sõne kui list, mitmemõõtmeline list - multi dimensional)


""" user_animal = str(input("Kirjuta lemmikloom: "))
print(str(user_animal[0]))

array = ["karu", "rebane", "kass"]
array.append(user_animal)
print(array)

last_word = array[-1]
last_letter = last_word[-1]
print(last_letter) """


animal = input("sisesta lemmikloom: ")
mylist = ["koer","kass","ahv"]
print(mylist)
mylist.append(animal)
print(mylist)
print(mylist[-1:])