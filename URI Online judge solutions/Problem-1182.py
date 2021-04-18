L = int(input())
T = input()
sum = 0
for i in range(144):
    f = float(input())
    if L==i:
        sum += f
        L += 12
if T == 'S':
    print("%.1f"%sum)
else:
    print("%.1f"%(sum/12))
