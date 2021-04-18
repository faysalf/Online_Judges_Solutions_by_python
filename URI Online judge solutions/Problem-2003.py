while True:
    try:
        H = list(map(int,input().split(":")))
        res = (H[0]*60 + H[1] + 60) - 480
        if res < 0:
            res = 0
        print("Atraso maximo: %d"%res)
    except EOFError:
        break
