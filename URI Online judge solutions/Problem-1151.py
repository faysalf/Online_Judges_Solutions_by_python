N = int(input())
i = 2
a = 0
b = 1
li = [0,1]
while i<N:
    c = a+b
    a = b
    b = c
    li.append(b)
    i += 1
print(*li)




'''
N = int(input())
i = 2
a = 0
b = 1
print(a,end=" ")
print(b,end=" ")
while i<N:
    c = a+b
    a = b
    b = c
    print(b,end=" ")
    i += 1
'''
