    T = int(input())
for i in range(T):
    A,B,C = map(int,input().split())
    if (A*B) > C:
        break
    else:
        for j in range(A*B,C+1,A*B):
            print(j)
    if (i<T-1):
        print()
