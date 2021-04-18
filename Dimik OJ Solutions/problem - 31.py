li = [6, 28, 496, 8128, 37551499]
T = int(input())
for i in range(T):
    N = int(input())
    for j in li:
        if 1<=j<=N:
            print(j)
    if (i<T-1):
        print()
