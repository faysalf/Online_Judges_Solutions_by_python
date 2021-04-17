N = int(input())
if N>=3600:
    h = N//3600
else:
    h = 0
N = N%3600
if N>=60:
    m = N//60
else:
    m = 0
N = N%60
print("%d:%d:%d"%(h,m,N))
