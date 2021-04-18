while True:
    try:
        N,M = map(int,input().split())
        li = [list(map(int,input().split())) for i in range(N)]
        ni = 0
        nj = 0
        mi = 0
        mj = 0
        for i in range(N):
            for j in range(M):
                if li[i][j] == 2:
                    ni += i
                    nj += j
                elif li[i][j] == 1:
                    mi += i
                    mj += j
        print((mi-ni)+abs(mj-nj))
    except EOFError:
        break
