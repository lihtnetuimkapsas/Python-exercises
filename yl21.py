# Arvuti mõtleb välja arvu nullist sajani. Lase kasutajal pakkuda, mis arvu arvuti välja mõtles. Vale pakkumise korral annab arvuti vihje, kas pakkumine on õigest arvust suurem või väiksem. Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. (juhuarv - random)



num = int(input("x=: "))

for i in range(1, 13):
    print(num, "x", i, "=", num*i)