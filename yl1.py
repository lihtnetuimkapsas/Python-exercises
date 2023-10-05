# Kirjuta programm, mis teisendab kasutaja poolt kroonides sisestatud summa eurodesse ja väljastab ümardatud tulemuse. (round)

# küsimine kasutajalt summa kroonides
# teisendamed kroonid eurodeks
# ümardame
# väljastame
# muutuja on mälus "koht" kuhu saab salvestada infot
# float - ujuv koma arv

eek =float(input("Sisesta kroonid: "))
eur = float(eek) / 15.6466
print(round(eur, 2))

