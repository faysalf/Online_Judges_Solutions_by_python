N = int(input())
for _ in range(N):
    X = int(input())
    f = X**0.5
    if X>1:
        for i in range(2,int(f)+1):
            if X%i == 0:
                print("%d nao eh primo"%X)
                break
        else:
            print("%d eh primo"%X)
    else:
        print("%d nao eh primo"%X)
