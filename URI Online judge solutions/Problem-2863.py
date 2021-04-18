while True:
    try:
        T = int(input())
        n = 100
        for _ in range(T):
            f = float(input())
            if f<n:
                n = f
        print(n)
    except EOFError:
        break
