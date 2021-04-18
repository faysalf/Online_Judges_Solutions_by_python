L = int(input())
T = input()
sum = 0
for i in range(12):
    for j in range(12):
        f = float(input())
        if L==i:
            sum += f
if T == 'S':
    print("%.1f"%sum)
else:
    print("%.1f"%(sum/12))
