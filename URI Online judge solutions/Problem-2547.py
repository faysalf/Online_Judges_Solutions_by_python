while True:
    try:
        N,a,A = map(int,input().split())
        count = 0
        for _ in range(N):
            Ai = int(input())
            if Ai>=a and Ai<=A:
                count += 1
        print(count)
    except EOFError:
        break
