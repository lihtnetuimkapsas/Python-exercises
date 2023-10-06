# Kirjutada programm, mis kontrollib, kas antud positiivne täisarv on liig- või lihtaasta number.
# Aasta on liigaasta kui ta jagub neljasajaga või jagub neljaga ja ei jagu sajaga.

aasta = int(input("Sisesta aasta: "))
if (aasta % 400 == 0):
    print(str(aasta) + " on liigaasta")
elif(aasta % 4 == 0) and ( arv % 100 != 0):
    print(str(aasta) + " on liigaasta")
else:
    print(str(aasta) + " on lihtaasta")