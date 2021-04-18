import math
n = int(input())
fs,scn = n / math.log(n), 1.25506*(n/math.log(n))
print("%.1f %.1f"%(fs,scn))
