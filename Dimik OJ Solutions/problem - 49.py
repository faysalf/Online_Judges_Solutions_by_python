import math
T = int(input())
for _ in range(T):
    N = int(input())
    r = math.sqrt(N)
    if N == 2:
        print("%d is a prime"%N)
    elif N>1:
        for i in range(2,int(r)+1):
            if N%i == 0:
                print("%d is not a prime"%N)
                break
        else:
            print("%d is a prime"%N)
    else:
        print("%d is not a prime"%N)
