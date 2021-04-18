n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
l = 0
r = 0
for i in range(n):
    for j in range(n):
        if i==j:
            l += arr[i][j]

i = n-1
j = 0
while i>=0:
    r += arr[i][j]
    j += 1
    i -= 1
print(abs(l-r))
