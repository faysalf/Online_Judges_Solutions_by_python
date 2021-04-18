T = int(input())
for _ in range(T):
    N = int(input())
    k = 0
    while 1 == 1:
        if N <= 2**k:
            break
        k += 1
    if N == 2**k:
        print("It's a power of 2")
    else:
        print("Not a power of 2")






'''
T = int(input())
for _ in range(T):
    N = int(input())
    f = N**0.5
    for i in range(1,int(f)+1):
        if N**(1/i) == 2:
            print("It's a power of 2")
            break
    else:
        print("Not a power of 2")
'''
