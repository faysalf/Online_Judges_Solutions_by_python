li = list(map(int,input().split()))
A = li[0]
N = 0
sum = 0
li.remove(li[0])
for i in li:
    if i>0:
        N = i
for j in range(N):
    sum += A
    A += 1
print(sum)
    


'''
li = list(map(int,input().split()))
A = li[0]
N = li.pop()
summ = 0
i = 0
while i<N:
    summ += (i+A)
    i += 1
print(summ)
'''
