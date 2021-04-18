while True:
    try:
        count = 0
        N = int(input())
        while N>1:
            N //= 2
            count += 1
        print(count)
    except EOFError:
        break

'''
while True:
    try:
        N = int(input())
        if N <2:
            print(0)
        elif N==2:
            print(1)
        else:
            count = 0
            while N>=2:
                N //= 2
                count += 1
            print(count)
    except EOFError:
        break
'''
