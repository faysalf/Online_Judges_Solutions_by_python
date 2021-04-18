S,T,F = map(int,input().split())
if S==0:
    S = 24
total = S+T+F
if total > 24:
    total = total - 24
elif total == 24:
    total = 0
print(total)
