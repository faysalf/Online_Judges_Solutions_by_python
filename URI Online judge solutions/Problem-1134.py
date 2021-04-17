f = 1
alc = 0
gas = 0
di = 0
while f>0:
    N = int(input())
    if N == 4:
        break
    elif N<1 and N>4:
        f += 1
    elif N == 1:
        alc += 1
    elif N == 2:
        gas += 1
    elif N == 3:
        di += 1
print("MUITO OBRIGADO")
print("Alcool: %d"%alc)
print("Gasolina: %d"%gas)
print("Diesel: %d"%di)
