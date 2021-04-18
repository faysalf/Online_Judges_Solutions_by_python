t = int(input())
for i in range(t):
    li = []
    X, K = map(int,input().split())
    for j in range(0,K+1):
        li.append(X**j)
    print("Result = %d"%sum(li))
