T = int(input())
for i in range(1, T+1):
    trun, crun, rball = list(map(int, input().split()))
    rrun = (trun-crun)+1
    pball = 300 - rball
    crr = crun/(pball/6)
    rr = rrun/(rball/6)
    if crun > trun:         #bortoman run current run er cheye beshi hole rr 0 hobe.
        rr = 0.00
    print('%.2f %.2f'%(crr, rr))
    
