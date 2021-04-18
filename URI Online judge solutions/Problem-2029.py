while True:
    try:
        V = float(input())
        D = float(input())
        r = D/2
        area = 3.14*r*r
        diff = V/area
        print("ALTURA = %.2f"%diff)
        print("AREA = %.2f"%area)
    except EOFError:
        break
