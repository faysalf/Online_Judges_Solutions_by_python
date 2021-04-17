li = []
count = 0
V = int(input())
li.append(V)
while count<9:
    li.append(V*2)
    V *= 2
    count += 1
for i in range(len(li)):
    print("N[%d] = %d"%(i,li[i]))
