C = int(input())
for _ in range(C):
    N,M = map(int,input().split())
    r = N**M
    print(len(str(r)))
