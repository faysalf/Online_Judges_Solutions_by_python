T = int(input())
for _ in range(T):
    H,M,O = map(int,input().split())
    h,m = str(H),str(M)
    if H < 10:
        h = "0%s"%H
    if M<10:
        m = "0%s"%M
    if O==1:
        print("%s:%s - A porta abriu!"%(h,m))
    elif O==0:
        print("%s:%s - A porta fechou!"%(h,m))
