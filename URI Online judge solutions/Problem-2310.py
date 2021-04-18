TS,TB,TA = 0,0,0
SS,SB,SA = 0,0,0
for T in range(int(input())):
    name = input()
    S,B,A = map(int,input().split())
    S1,B1,A1 = map(int,input().split())
    TS += S
    TB += B
    TA += A
    SS += S1
    SB += B1
    SA += A1
print("Pontos de Saque: %.2f %%."%((SS*100)/TS))
print("Pontos de Bloqueio: %.2f %%."%((SB*100)/TB))
print("Pontos de Ataque: %.2f %%."%((SA*100)/TA))
