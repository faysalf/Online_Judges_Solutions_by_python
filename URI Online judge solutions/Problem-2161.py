N = int(input())
x = 0.0
if N == 0:
    x = 0.0000000000
elif N == 1:
    x = 0.1666666667
for i in range(2,N+1):
    if i == 2:
        x = 1.0/(6.0+(1.0/6.0))
    else:
        x = 1.0/(6.0+x)
print("%.10f"%(x+3.0))
