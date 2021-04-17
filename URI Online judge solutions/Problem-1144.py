N = int(input())
I = 1
for i in range(N):
    print("%d %d %d"%(I,I*I,I*I*I))
    print("%d %d %d"%(I,(I*I)+1,(I*I*I)+1))
    I += 1
