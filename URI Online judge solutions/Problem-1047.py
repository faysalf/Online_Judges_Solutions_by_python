sh,sm,eh,em = map(int,input().split())
start = (sh*60) + sm
end = (eh*60) + em
if end <= start:
    r = (1440-start) + end    #full day 1440mnt
    h = r//60
    m = r%60
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(h,m))
else:
    r = end-start
    h = r//60
    m = r%60
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(h,m))
