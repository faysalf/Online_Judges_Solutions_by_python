import math
T = int(input())
for i in range(T):
    li = []
    n = int(input())
    for j in range(0,n+1):
        li.append(j/math.factorial(j))
    print("%.4f"%sum(li))
