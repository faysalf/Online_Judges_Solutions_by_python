count = 0
sm = 0
while True:
    try:
        if count==2:
            break
        n = float(input())
        if n<0 or n>10:
            print("nota invalida")
        else:
            sm += n
            count += 1
    except EOFError:
        break
print("media = %.2f"%(sm/2))
