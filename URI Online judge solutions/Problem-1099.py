N = int(input())
for _ in range(N):
    X,Y = map(int,input().split())
    sum = 0
    if X>=Y:
        if Y%2==0:
            for i in range(Y+1,X,2):
                sum += i
        else:
            for i in range(Y+2,X,2):
                sum += i
    elif X<Y:
        if X%2==0:
            for i in range(X+1,Y,2):
                sum += i
        else:
            for i in range(X+2,Y,2):
                sum += i
    print(sum)
