for T in range(int(input())):
    N,K = map(int,input().split())
    print(int(N%K) + int(N/K))
