T = int(input())
for i in range(1,T+1,1):
    N = int(input())
    print("Case %d: "%i,end="")
    for k in range(1,N):
        if N % k == 0:
            print(k,end=" ")
    print(N)                #space delete korar jonno N er manke alada newa hoise
