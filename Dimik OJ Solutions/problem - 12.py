import math
T = int(input())
for i in range(T):
    n = math.factorial(int(input()))
    count = 0
    while n > 0:
        d = n%10
        if d == 0:
            count += 1
            n = n//10
        else:
            break
    print(count)

     
repeat = int(input())
x = 0
y = 1
z = 0
for i in range(repeat):
    x = int(input())
    while x/(5**y) > 0:
        z = z + int(x/(5**y))
        y = y+1
    print(z)
    y = 1
    z = 0
