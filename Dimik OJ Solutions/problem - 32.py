T = int(input())
for i in range(T):
    X,N = map(int,input().split())
    if X > N:
        print("Invalid!")
    else:
        for j in range(X,N+1,X):
            print(j)
    print()
