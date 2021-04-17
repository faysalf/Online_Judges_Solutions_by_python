slr = float(input())
if slr>=0 and slr<=400.00:
    print("Novo salario: %.2f"%(slr + (slr*15)/100))
    print("Reajuste ganho: %.2f"%((slr*15)/100))
    print("Em percentual: 15 %")
elif slr>=400.01 and slr<=800.00:
    print("Novo salario: %.2f"%(slr + (slr*12)/100))
    print("Reajuste ganho: %.2f"%((slr*12)/100))
    print("Em percentual: 12 %")
elif slr>=800.01 and slr<=1200.00:
    print("Novo salario: %.2f"%(slr + (slr*10)/100))
    print("Reajuste ganho: %.2f"%((slr*10)/100))
    print("Em percentual: 10 %")
elif slr>=1200.01 and slr<=2000.00:
    print("Novo salario: %.2f"%(slr + (slr*7)/100))
    print("Reajuste ganho: %.2f"%((slr*7)/100))
    print("Em percentual: 7 %")
elif slr > 2000.00:
    print("Novo salario: %.2f"%(slr + (slr*4)/100))
    print("Reajuste ganho: %.2f"%((slr*4)/100))
    print("Em percentual: 4 %")
