t = int(input())
for _ in range(t):
    m = int(input())
    n = int(input())
    cost = list(map(int,input().split()))
    f,s=0,0
    for i in range(n-1):
        for j in range(i+1,n):
            if cost[i]+cost[j] == m:
                f,s = i+1,j+1
    print(f,s)
