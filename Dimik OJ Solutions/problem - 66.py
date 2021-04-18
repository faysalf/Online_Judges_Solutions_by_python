N = int(input())
n1,n2 = 0,1
count = 2
li = []
while count <= N:
    n3 = n1+n2
    li.append(n3)
    count += 1
    n1 = n2
    n2 = n3
print(li[-1])
