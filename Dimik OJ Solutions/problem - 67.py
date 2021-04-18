N = int(input())
m,n = 0,1
for i in range(N):
    m,n = n, m+n
print(m)
