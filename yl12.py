# Anna muutuja väärtuseks list kolmest oma lemmik puuviljast ja väljasta see
# Väljasta listi esimene väärtus
# Lisa listi lõppu uus puuvili
# Väljasta listi viimane väärtus
# Muuda ühe elemendi väärtust ja väljasta kogu list
# Kontrolli kas väärtus (näiteks õun) eksisteerib listis
# Väljasta listi pikkus
# Eemalda listist element ja väljasta kogu list
# Muuda listi järjekord vastupidiseks
# Sorteeri list ja väljasta
# (jada, list, listi element, listi meetodid)
# https://www.w3schools.com/python/python_lists.asp


lemmik_puuviljad = ["pirn", "murel", "oun"]
print(lemmik_puuviljad)

print(lemmik_puuviljad[0])

lemmik_puuviljad.append("banaan")
print(lemmik_puuviljad)

print(lemmik_puuviljad[-1])

if "oun" in lemmik_puuviljad:
    print(lemmik_puuviljad)
else:
    print("oun ei ole listis")

print(len(lemmik_puuviljad))

lemmik_puuviljad.remove("oun")
print(lemmik_puuviljad)

lemmik_puuviljad.reverse()
print(lemmik_puuviljad)

lemmik_puuviljad.sort()
print(lemmik_puuviljad)




