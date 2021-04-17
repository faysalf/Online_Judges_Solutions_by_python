n = int(input())
li = []
lii = []
sl = []
r = []
for i in range(n):
    li.append(input())
    a = float(input())
    lii.append(a)
    sl.append(a)
fl = list(set(lii))
fl.remove(min(fl))
second = min(fl)
for i in range(n):
    if sl[i]==second:
        r.append(li[i])
R = sorted(r)
print("\n".join(R))
