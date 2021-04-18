n = 1
while True:
    try:
        N1 = input()
        N2 = input()
        print("Caso #%d:"%n)
        l = N2.count(N1)
        if l == 0:
            print("Nao existe subsequencia")
        else:
            m = N2.rfind(N1)        #right side theke subsequence find kora position number
            print("Qtd.Subsequencias: %d"%l)
            print("Pos: %d"%(m+1))
        print()
        n += 1
    except EOFError:
        break
