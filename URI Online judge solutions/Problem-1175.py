li = []
for _ in range(20):
    N = int(input())
    li.append(N)
li.reverse()
for i in range(len(li)):
    print("N[%d] = %d"%(i,li[i]))
