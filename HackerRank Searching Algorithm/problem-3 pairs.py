#that is so less time

n,k = map(int,input().split())
li = list(map(int,input().split()))
st = set(li)
count = 0
for i in st:
    if i+k in st:
        count += 1
print(count)


'''
n,k = map(int,input().split())
l = list(map(int,input().split()))
li = list(set(li))
count = 0
for i in range(n):
    for j in range(i+1,n):
        if abs(li[i]-li[j]) == k:
            count += 1
print(count)
'''
