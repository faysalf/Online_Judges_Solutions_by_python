import math
while True:
    li = list(map(int,input().split()))
    if len(li) < 3 and li[0]==0:
        break
    else:
        A,B,C = li[0],li[1],li[2]
    x = math.sqrt((A*B*100)/C)
    print("%d"%int(x))
