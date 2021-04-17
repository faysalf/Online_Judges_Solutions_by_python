T = int(input())
count = 0
i = 0
while i < 1000:
    print("N[%d] = %d"%(i,count))
    count += 1
    i += 1
    if count == T:
        count = 0
