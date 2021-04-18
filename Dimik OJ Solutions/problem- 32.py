T = int(input())
for i in range(T):
    X,N = map(int,input().split())
    if X <= N:
        for j in range(1,N):
            if j*X > N:
                break
            print(j*X)
        if (i<j-1):
            print()
    else:
        print("Invalid!")
    
