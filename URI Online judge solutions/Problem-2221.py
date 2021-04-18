for T in range(int(input())):
    B = int(input())
    ai,di,li = map(int,input().split())
    a1,d1,l1 = map(int,input().split())
    Dabriel = ai+di
    Guarte = a1+d1
    if li%2==0:
        Dabriel += B
    if l1%2==0:
        Guarte += B
    if Dabriel > Guarte:
        print("Dabriel")
    elif Dabriel < Guarte:
        print("Guarte")
    else:
        print("Empate")
