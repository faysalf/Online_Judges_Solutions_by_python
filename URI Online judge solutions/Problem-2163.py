N,M = map(int,input().split())
li = []
k,l = 0,0
for _ in range(N):
    lii = list(map(int,input().split()))
    li.append(lii)
for i in range(N):
    for j in range(M):
        if (li[i][j]==42) and (i>0) and (i<N-1) and (j>0) and (j<M-1):
            if (li[i][j-1]==li[i][j+1]==li[i-1][j-1]==li[i-1][j]==li[i-1][j+1]==li[i+1][j-1]==li[i+1][j]==li[i+1][j+1]==7):
                k, l = i+1, j+1
                break
print("%d %d"%(k,l))
