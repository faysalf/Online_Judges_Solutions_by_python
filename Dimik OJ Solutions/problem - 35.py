T = int(input())
for i in range(T):
    Xc, Yc = map(float,input().split())
    r = float(input())
    X, Y = map(float,input().split())
    f = (X-Xc)*(X-Xc) + (Y-Yc)*(Y-Yc)
    if f >= r*r:
        print("The point is not inside the circle")
    else:
        print("The point is inside the circle")
