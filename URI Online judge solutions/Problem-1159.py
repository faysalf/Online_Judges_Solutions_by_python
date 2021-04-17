while True:
    X = int(input())
    if X==0:
        break
    n = 1
    sum = 0
    if X%2==0:
        count = 0
        for i in range(5):
            sum += (X+count)
            count += 2
    else:
        X += 1
        count = 0
        for i in range(5):
            sum += (X+count)
            count += 2
    print(sum)
