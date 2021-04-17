T = int(input())
for _ in range(T):
    PA,PB,G1,G2 = input().split()
    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)
    G2 = float(G2)
    v1 = PA
    v2 = PB
    count = 0
    while v1<=v2:
        v1 += int((v1*G1)/100)
        v2 += int((v2*G2)/100)
        count += 1
        if count > 100:
            break
    if count>100:
        print("Mais de 1 seculo.")
    else:
        print("%d anos."%count)
