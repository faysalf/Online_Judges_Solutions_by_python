N = int(input())
crabit = 0
rat = 0
sfrog = 0
for _ in range(N):
    am,an = input().split()
    am = int(am)
    if an == 'C':
        crabit += am
    elif an == 'R':
        rat += am
    elif an == 'S':
        sfrog += am
r = crabit + rat + sfrog
r1 = (crabit*100)/r
r2 = (rat*100)/r
r3 = (sfrog*100)/r
print("Total: %d cobaias"%r)
print("Total de coelhos: %d"%crabit)
print("Total de ratos: %d"%rat)
print("Total de sapos: %d"%sfrog)
print("Percentual de coelhos: %.2f"%r1,"%")
print("Percentual de ratos: %.2f"%r2,"%")
print("Percentual de sapos: %.2f"%r3,"%")
