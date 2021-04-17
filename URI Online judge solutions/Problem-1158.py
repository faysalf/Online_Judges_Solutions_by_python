N = int(input())
for _ in range(N):
    X,Y = map(int,input().split())
    sum = 0
    i = 1
    f = 0
    if X%2==1:
        while i<=Y:
            sum += (X+f)
            f += 2
            i += 1
    else:
        while i<=Y:
            sum += (X+f+1)
            f += 2
            i += 1
    print(sum)
