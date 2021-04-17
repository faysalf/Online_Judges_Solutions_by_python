n = int(input())
A = list(map(int,input().split()))
A.sort()
mx = A[-1]
j = 0
for i in A:
    if i<mx:
        j = i
print(j)
