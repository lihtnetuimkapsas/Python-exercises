# # Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks. 
# Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi. 
# Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida. 
# Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)


a = float(input("Esimese külje pikkus: "))
b = float(input("Teise külje pikkus: "))
c = float(input("Kolmanda külje pikkus: "))

if a != b and b != c and a != c:
    print("Tegu on erikylgse kolmnurgaga.")
elif a == b or a == c or b == c:
    print("Tegu on vordhaarse kolmnurgaga")
elif a == b and b == c and c == a:
    print("Tegu on vordkulgse kolmnurgaga")
