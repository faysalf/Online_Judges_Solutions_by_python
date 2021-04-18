while True:
    try:
        nc = 0
        c = 0
        M = int(input())
        for i in range(M):
            N,C = map(int,input().split())
            nc += (N*C)
            c += C
        print("%.4f"%(nc/(c*100)))
    except EOFError:
        break

