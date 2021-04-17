import math
a,b,c = map(int,input().split())
f = (a+b+ abs(a-b))/2
r = (f+c+ abs(f-c))/2
print("%d eh o maior"%r)
