N = int(input())
if N>=365:
    y = N//365
    print("%d ano(s)"%y)
else:
    print("0 ano(s)")
N = N%365
if N>=30:
    m = N//30
    print("%d mes(es)"%m)
else:
    print("0 mes(es)")
N = N%30
print("%d dia(s)"%N)
