while True:
    M,N = map(int,input().split())
    if M<=0 or N<=0:
        break
    sum = 0
    if M>=N:
        for i in range(N,M+1):
            sum += i
            print(i,end=" ")
        print("Sum=%d"%sum)
    else:
        for i in range(M,N+1):
            sum += i
            print(i,end=" ")
        print("Sum=%d"%sum)
