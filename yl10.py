# Kirjuta programm, mis küsib kasutajalt nime, tervitab teda nimepidi, küsib kasutajalt elukoha, kui elukoht on Saaremaa, siis väljastab mingi kommentaari, küsib kasutajalt vanuse, kui vanus on väiksem kui 18, siis ütleb, et kasutaja on liiga noor, et autot juhtida, kui vanus on 18, siis õnnitleb täisealiseks saamise puhul, kui kasutaja on vanem kui 18, siis ütleb, et kasutaja võib autot juhtida. (sõne - string)

nimi = input(str("Sisesta nimi:  "))
print("Tere, " +  nimi + "!")

elukoht = input("Sisesta elukoht: ").lower()
if "saaremaa" in elukoht:
    print("Saaremaa on kena koht!")

vanus = int(input("Sisesta vanus: "))
if vanus < 18:
    print("Sa oled liiga noor, et autot juhtida")
elif vanus == 18:
    print("Onnitlen taiskasvanuks saamise puhul!")
else:
    print("Void autot juhtida")

