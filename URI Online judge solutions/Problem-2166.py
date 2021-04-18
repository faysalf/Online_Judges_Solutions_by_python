N = int(input())
x = 0.0
if N == 0:
    x = 0.0000000000
elif N == 1:
    x = 0.5000000000
for i in range(2,N+1):
    if i == 2:
        x = 1.0/(2.0+(1.0/2.0))
    else:
        x = 1.0/(2.0+x)
print("%.10f"%(x+1))
