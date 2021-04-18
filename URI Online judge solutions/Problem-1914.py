QT = int(input())
for _ in range(QT):
    a,b,c,d = input().split()
    N,M = map(int,input().split())
    if (b == "PAR"):
        if (N+M)%2 == 0:
            print(a)
        else:
            print(c)
    elif (b == "IMPAR"):
        if (N+M)%2 == 0:
            print(c)
        else:
            print(a)
