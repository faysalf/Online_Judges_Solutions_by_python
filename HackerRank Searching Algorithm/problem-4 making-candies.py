m,w,p,n = map(int,input().split())
li = []
k = n//2 

for i in range(1,k+2):
    if n%i == 0:
        li.append(i)
li.append(n)

ln = len(li) // 2
i = li[ln-1]
j = li[ln]

r = 0
mw = m*w
count = 0
while mw<n:
    if m<i:
        r = m*w - i
        if r>=0:
            m = i
        else:
            m = m*w
    if w<j:
        w = 

print(i,j)
print(li)
