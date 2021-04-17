N = float(input())
print("NOTAS:")
if N >= 100:
    print("%d nota(s) de R$ 100.00"%(N//100))
else:
    print("0 nota(s) de R$ 100.00")
N %= 100
if N >= 50:
    print("%d nota(s) de R$ 50.00"%(N//50))
else:
    print("0 nota(s) de R$ 50.00")
N %= 50
if N >= 20:
    print("%d nota(s) de R$ 20.00"%(N//20))
else:
    print("0 nota(s) de R$ 20.00")
N %= 20
if N >= 10:
    print("%d nota(s) de R$ 10.00"%(N//10))
else:
    print("0 nota(s) de R$ 10.00")
N %= 10
if N >= 5:
    print("%d nota(s) de R$ 5.00"%(N//5))
else:
    print("0 nota(s) de R$ 5.00")
N %= 5
if N >= 2:
    print("%d nota(s) de R$ 2.00"%(N//2))
else:
    print("0 nota(s) de R$ 2.00")
print("MOEDAS:")
N %= 2
if N >= 1:
    print("%d moeda(s) de R$ 1.00"%(N//1))
else:
    print("0 moeda(s) de R$ 1.00")
N %= 1
if N >= 0.50:
    print("%d moeda(s) de R$ 0.50"%(N//0.50))
else:
    print("0 moeda(s) de R$ 0.50")
N %= 0.50
if N >= 0.25:
    print("%d moeda(s) de R$ 0.25"%(N//0.25))
else:
    print("0 moeda(s) de R$ 0.25")
N %= 0.25
if N >= 0.10:
    print("%d moeda(s) de R$ 0.10"%(N//0.10))
else:
    print("0 moeda(s) de R$ 0.10")
N %= 0.10
if N >= 0.05:
    print("%d moeda(s) de R$ 0.50"%(N//0.05))
else:
    print("0 moeda(s) de R$ 0.05")
N %= 0.05
if N >= 0.01:
    print("%d moeda(s) de R$ 0.01"%(N//0.01))
else:
    print("0 moeda(s) de R$ 0.01")
















    
