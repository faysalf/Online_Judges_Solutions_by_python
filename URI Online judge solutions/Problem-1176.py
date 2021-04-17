def fib(N):
    li = [0,1]
    a = 0
    b = 1
    while len(li) <= (N+1):
        c = a+b
        li.append(c)
        a = b
        b = c
    return ("Fib(%d) = %d"%(N,li[N]))
T = int(input())
for _ in range(T):
    N = int(input())
    print(fib(N))
