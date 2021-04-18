N = int(input())
li = []
for k in range(N+1):
    lii = list(map(int,input().split()))
    li.append(lii)
for i in range(N):
    for j in range(N):
        if ((li[i][j]) + (li[i][j+1]) + (li[i+1][j]) + (li[i+1][j+1])) >= 2:
            print("S",end="")
        else:
            print("U",end="")
    print()
