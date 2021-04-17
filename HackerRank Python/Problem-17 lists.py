def iff(ni):
    li = []
    if ni[0] == "print":
        return li
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
    elif ni[0] == "reverse":
        li.reverse()

for i in range(int(input())):
    ni = input()
    print(iff(ni))
