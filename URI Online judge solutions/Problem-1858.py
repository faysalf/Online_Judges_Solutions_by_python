N = int(input())
Tn = list(map(int,input().split()))
for i in range(N):
    Tn[i] == int(Tn[i])
minimum = min(Tn) #je kom beat korese tar position ber kora
result = Tn.index(minimum)
print(result+1)     #index a 1 kom thake
