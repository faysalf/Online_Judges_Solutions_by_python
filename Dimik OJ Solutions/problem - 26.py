T = int(input())
for i in range(T):
    X = float(input())
    days = []
    while X > 1:
        X /= 2
        days.append(X)
    print(len(days),"days")
