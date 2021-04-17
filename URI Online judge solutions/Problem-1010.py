product1, unit, price = input().split()
prodcut2, unit2, price2 = input().split()
total = (int(unit) * float(price)) + (int(unit2) * float(price2))
print("VALOR A PAGAR: R$ %.2f"%total)
