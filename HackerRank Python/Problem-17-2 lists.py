li = []
for _ in range(int(input())):
    ni = input().split()
    if ni[0] == "print":
        print(li)
    elif ni[0] == "insert":
        i = int(ni[1])
        k = int(ni[2])
        li.insert(i,k)
    elif ni[0] == "remove":
        li.remove(int(ni[1]))
    elif ni[0] == "append":
        li.append(int(ni[1]))
    elif ni[0] == "sort":
        li.sort()
    elif ni[0] == "pop":
        li.pop()
    else:
        li.reverse()
