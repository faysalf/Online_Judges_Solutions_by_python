for T in range(int(input())):
    N = input()
    D = float(input())
    S = list(map(float,input().split()))
    S.remove(max(S))
    S.remove(min(S))
    print("%s %.2f"%(N,(sum(S)*D)))
