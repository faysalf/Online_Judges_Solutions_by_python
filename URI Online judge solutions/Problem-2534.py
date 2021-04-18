while True:
    try:
        N,Q = map(int,input().split())
        citizen = []
        for i in range(N):
            citizen.append(int(input()))
        citizen.sort()
        citizen = citizen[::-1]
        for i in range(Q):
            p = int(input())
            print(citizen[p-1])
    except EOFError:
        break

