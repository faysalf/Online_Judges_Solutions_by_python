def tax(n):
    m = n-2000
    result = 0
    if m>2500.00:
        result += ((m-2500)*28)/100
        result += (1500*18)/100
        result += (1000*8)/100
    elif m>1000.00 and m<=2500.00:
        result += ((m-1000)*18)/100
        result += (1000*8)/100
    elif m<=1000 and m>0.00:
        result += (m*8)/100
    if result<=0:
        return 'Isento'
    else:
        return ("R$ %.2f"%result)
while True:
    n = float(input())
    print(tax(n))
