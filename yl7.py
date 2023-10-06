# Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud täisarv on paarisarv või mitte. (paarisarvu mõiste - odd/even)


arv = int(input("Sisesta arv: "))
if (arv % 2) == 0:
    print(str(arv) + " on paarisarv")
else:
    print(str(arv) + " on paaritu")

