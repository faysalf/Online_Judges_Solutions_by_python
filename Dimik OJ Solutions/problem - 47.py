from sys import stdin
s = ""
for c in stdin:
    s += (c+' ')
lst = list(map(int, s.split()))
test = lst[0]
del lst[0]
for t in range(test):
    n = lst[0]
    del lst[0]
    flist = list()
    for i in range(n):
        flist.append(lst[0])
        del lst[0]
    m = lst[0]
    del lst[0]
    for i in range(m):
        flist.append(lst[0])
        del lst[0]
    flist.sort()
    for i in range(len(flist)):
        if i > 0:
            print("",end=" ")
        print(flist[i],end="")
    print()



    
'''
T = int(input())
for i in range(T):
    n1 = int(input())
    li1= list(map(int,input().split()))
    n2 = int(input())
    li2 = list(map(int,input().split()))
    nli = sorted(li1 + li2)
    print(*nli)
'''
