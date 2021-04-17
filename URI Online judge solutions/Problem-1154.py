sum = 0
count = 0
while True:
    N = int(input())
    if N<0:
        break
    else:
        sum += N
        count += 1
print("%.2f"%(sum/count))
