X,Y = map(int,input().split())
count = 1
for i in range(1,(Y//X)+1):
    result = ""
    for j in range(X):
        result += str(count) + " "
        count += 1
    print(result[:-1])
