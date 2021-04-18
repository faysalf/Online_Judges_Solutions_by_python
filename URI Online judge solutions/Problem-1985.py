T = int(input())
res = 0
for _ in range(T):
    p,q = map(int,input().split())
    if p == 1001:
        res += 1.50 * q
    elif p == 1002:
        res += 2.50 * q
    elif p == 1003:
        res += 3.50 * q
    elif p == 1004:
        res += 4.50 * q
    elif p == 1005:
        res += 5.50 * q
print("%.2f"%res)
