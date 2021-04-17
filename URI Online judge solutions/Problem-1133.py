X = int(input())
Y = int(input())
f = X
if X>Y:
    X = Y
    Y = f
while X<Y:
    if X%5==2 or X%5==3 and X != Y:
        print(X)
    X += 1
