N = int(input())
X = [int(i) for i in input().split()]
total = sum(X)
attacking_farm = [0] * N   #N number ghor nilam
i = 0
while i>=0 and i<N:
    a = X[i] % 2
    if X[i]>0:             #a>0 holee steel/churi kora possible
        total -= 1      #without attacking sheep
        X[i] = X[i]-1
        attacking_farm[i] = 1 #je farm a attack sei attacki_farme 1 append korabe3
    if a:               #jodi a==0 hoy, tahole samner ghore jabe
        i += 1
    else:               #else: ak ghor pichone back korbe.
        i -= 1
attacking_farm = attacking_farm.count(1) #shudhu 1 count korbe. cause attacing farme
                                        #1 appen korano
print(attacking_farm,total)
