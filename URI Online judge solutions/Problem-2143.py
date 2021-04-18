while True:
    T = int(input())
    if T==0:
        break
    for _ in range(T):
        N = int(input())
        if N%2==0:
            print(N*2 - 2)
        else:
            print(N*2 - 1)
