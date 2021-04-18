from math import pow, sqrt
while True:
    try:
        Xf,Yf,Xi,Yi,Vi,R1,R2 = map(int,input().split())
        distance = sqrt(pow((Xf-Xi), 2) + pow((Yf-Yi), 2))
        latest_distance = distance + (1.5*Vi)
        if (R1+R2) >= latest_distance:
            print("Y")
        else:
            print("N")
    except EOFError:
        break
