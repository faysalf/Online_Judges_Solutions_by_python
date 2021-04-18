                    #duitae hoise
import math
T = int(input())
for i in range(T):
    a,b,c = map(int,input().split())
    if a+b<c or b+c<a or a+c<b:
        print("Oh, No!")
    else:
        s = (a+b+c)/2
        A = s*(s-a)*(s-b)*(s-c)
        r = math.sqrt(A)
        print("%.2f"%r)



'''       
from math import sqrt
repeat = int(input())
for x in range(repeat):
    a, b, c = map(int, input().split())
    if a + b < c or b + c < a or c + a < b:
        print('Oh, No!')
    else:
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        print("%.2f" % area)
        '''
