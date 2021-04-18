while True:
    try:
        N = int(input())
        major = 0
        for i in range(N):
            t,d = map(int,input().split())
            if (d/t)>major:
                print(i+1)
            major = d/t
    except EOFError:
        break
