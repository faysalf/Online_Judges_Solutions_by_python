while True:
    try:
        T = int(input())
        optr = []
        for i in range(T):
            exp = input()
            n_exp = exp.replace("="," ")
            li = list(n_exp.split(" "))
            x,y,z = int(li[0]), int(li[1]), int(li[2])
            if x+y==z:
                optr.append("+")
            elif x-y==z:
                optr.append("-")
            elif x*y==z:
                optr.append("*")
            else:
                optr.append("I")
        name = []
        unsc = 0
        for i in range(T):
            n,e,r = input().split()
            e = int(e)
            if optr[e-1] != r:
                name.append(n)
                unsc += 1
        if unsc==T:
            print("None Shall Pass!")
        elif unsc==0:
            print("You Shall All Pass!")
        else:
            name.sort()
            print(*name)         

    except EOFError:
        break
