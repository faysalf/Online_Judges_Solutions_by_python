li = []
n = int(input())
for _ in range(n):
    li.append(int(input()))

for i in range(n-1):
    index_min = i
    for j in range(i+1,n):
        if li[index_min] > li[j]:
            index_min = j
    if index_min != i:
        li[i], li[index_min] = li[index_min],li[i]

for a in li:
    print(a)