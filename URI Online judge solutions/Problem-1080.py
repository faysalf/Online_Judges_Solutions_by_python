li = []
for _ in range(100):
    N = int(input())
    li.append(N)
ln = 0
for i in range (len(li)):
    if li[i]== max(li):
        ln += i
        break
print(max(li))
print(ln+1)
