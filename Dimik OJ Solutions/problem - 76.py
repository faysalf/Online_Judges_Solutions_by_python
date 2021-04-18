while True:
    n = int(input())
    if n == 0:
        break
    r = n
    f = int((n+1)**0.5)
    for i in range(2,f+1):
        if n%i==0:
            while n%i==0:
                n = n/i
            r = r - (r/i)
    if n>1:
        r = r - (r/n)
    print(int(r))
