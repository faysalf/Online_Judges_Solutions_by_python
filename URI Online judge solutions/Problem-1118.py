while True:
    count = 0
    sm = 0
    while count<2:
        n = float(input())
        if n>=0 and n<=10:
            sm += n
            count += 1
        else:
            print("nota invalida")
    print("media = %.2f"%(sm/2))
    t = 0
    while True:
        t = int(input())
        print("novo calculo (1-sim 2-nao)")
        if t==1 or t==2:
            break
    if t==2:
        break
