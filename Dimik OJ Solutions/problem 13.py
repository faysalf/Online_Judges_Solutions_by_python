import math
for T in range(int(input())):
    N = list(map(str,input().split()))
    l = len(N)
    d = {}
    for i in N:
        d[i] = N.count(i)
    count = 1
    for j in d.keys():
        if d[j] > 1:
            count *= math.factorial(d[j])
    if count == 0:
        count = 1
    print("1/%d"%(math.factorial(l)//count))
