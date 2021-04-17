while True:
    X = int(input())
    if X == 0:
        break
    result = ""
    for i in range(1,X+1):
        result += str(i)+ " "
    print(result[:-1])
