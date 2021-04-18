T = int(input())
for i in range(T):
    N = int(input())
    C = N % 10
    while N>0:
        N = N // 10
        if N<10:
            print("Sum = %d"%(C+N))
            break
