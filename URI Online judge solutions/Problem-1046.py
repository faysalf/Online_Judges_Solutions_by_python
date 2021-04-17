start,end = map(int,input().split())
if end<=start:
    r = (24-start) + end
    print("O JOGO DUROU %d HORA(S)"%r)
else:
    print("O JOGO DUROU %d HORA(S)"%(end-start))
