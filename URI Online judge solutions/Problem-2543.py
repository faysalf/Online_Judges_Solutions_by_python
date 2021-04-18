while True:
    try:
        N,I = map(int,input().split())
        count = 0
        for _ in range(N):
            i,j = map(int,input().split())
            if i == I and j==0:
                count+=1
        print(count)
    except EOFError:
        break
