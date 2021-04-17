li = []
for _ in range(10):
    X = int(input())
    if X<=0:
        li.append(1)
    else:
        li.append(X)
for i in range(len(li)):
    print("X[%d] = %d"%(i,li[i]))
