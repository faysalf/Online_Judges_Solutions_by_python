N = int(input())
for _ in range(N):
    X = int(input())
    y = X//2
    sum = 0
    for i in range(1,y+1):
        if X%i == 0:
            sum += i
    if X==sum:
        print("%d eh perfeito"%X)
    else:
        print("%d nao eh perfeito"%X)
