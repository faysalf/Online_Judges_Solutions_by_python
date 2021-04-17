grenais = 0
inter = 0
gr = 0
draw = 0
C = 1
while True:
    if C==2:
        break
    a,b = map(int,input().split())
    grenais += 1
    if a>b:
        inter +=1
    elif a<b:
        gr += 1
    else:
        draw += 1
    print("Novo grenal (1-sim 2-nao)")
    c = int(input())
    if c==2:
        C+=1
print("%d grenais"%grenais)
print("Inter:%d"%inter)
print("Gremio:%d"%gr)
print("Empates:%d"%draw)
if inter>gr:
    print("Inter venceu mais")
elif inter<gr:
    print("Gremio venceu mais")
else:
    print("Não houve vencedor")
