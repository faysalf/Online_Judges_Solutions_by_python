O = input()
sum = 0
j = 0
for i in range(144):
    f = float(input())
    k = 1
    if i==j:
        sum += f
        j += (12+k)
        k += 1
if O == 'S':
    print(sum)
else:
    print("%.1f"%(sum/12))
