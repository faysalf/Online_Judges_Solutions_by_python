T = int(input())
for i in range(T):
    S = list(input().strip())
    r = sorted(set(S))
    for j in r:
        print("%s = %d"%(j,S.count(j)))
    if i<T-1:
        print()
