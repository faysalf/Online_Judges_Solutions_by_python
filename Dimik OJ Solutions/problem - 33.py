T = int(input())
for i in range(T):
    A,B,C = map(int,input().split())
    for j in range(A,B+1):
        if j%C == 0:
            f = j
            break
    for k in range(f,B+1,C):
        print(k)
    print()
