while True:
    T = int(input())
    if T==0:
        break
    amountC = 0
    for _ in range(T):
        N, F = input().split(maxsplit=1)
        N = int(N)
        if F == "suco de laranja":
            amountC += (N*120)
        elif F == "morango fresco":
            amountC += (N*85)
        elif F == "mamao":
            amountC += (N*85)
        elif F == "goiaba vermelha":
            amountC += (N*70)
        elif F == "manga":
            amountC += (N*56)
        elif F == "laranja":
            amountC += (N*50)
        elif F == "brocolis":
            amountC += (N*34)
    if (amountC < 110):
        print("Mais %d mg"%(110-amountC))
    elif (amountC>=110 and amountC<=130):
        print("%d mg"%amountC)
    else:
        print("Menos %d mg"%(amountC-130))





    
