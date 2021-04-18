T = int(input())
for i in range(T):
    r1,r2,B = map(int,input().split())
    ov = (300-B)/6
    ob = B/6
    d = (r1-r2+1)/ob
    print("%.2f %.2f"%(r2/ov,d))
