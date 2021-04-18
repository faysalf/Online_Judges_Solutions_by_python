while True:
    try:
        s = 0
        N,D = map(int,input().split())
        for i in range(D):
            li = input().split()
            d = li[0]
            p = list(map(int,li[1:]))
            if sum(p)==N and s!=1:
                print(d)
                s = 1
        if s==0:
            print("Pizza antes de FdI")
    except EOFError:
        break
