T = int(input())
for k in range(T):
    n = int(input())
    n1 = list(map(int,input().split()))
    li=[]
    if len(n1) == n:
        for i in n1:
            b = n1.index(i)
            if b%2 == 0:
                li.append(n1[b])
            else:
                continue
    print(*li)
