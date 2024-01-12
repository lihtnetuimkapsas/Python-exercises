# Arvuti mõtleb välja arvu nullist sajani. Lase kasutajal pakkuda, mis arvu arvuti välja mõtles. Vale pakkumise korral annab arvuti vihje, kas pakkumine on õigest arvust suurem või väiksem. Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. (juhuarv - random)



import random

def arvu_arvamise_mang():
    arvuti_arv = random.randint(0, 100)
    katsete_arv = 0

    while True:
        kasutaja_pakkumine = int(input("Paku arv nullist sajani: "))
        katsete_arv += 1

        if kasutaja_pakkumine == arvuti_arv:
            print(f"Õige! Arvasid ära arvu {arvuti_arv} {katsete_arv} katsega.")
            break
        elif kasutaja_pakkumine < arvuti_arv:
            print("Pakkumine on liiga väike. Proovi uuesti!")
        else:
            print("Pakkumine on liiga suur. Proovi uuesti!")
