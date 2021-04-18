while True:
    try:
        m,d = map(int,input().split())
        if m==12 and d==25:
            print("E natal!")
        elif m==12 and d>25:
            print("Ja passou!")
        elif m==12 and d==24:
            print("E vespera de natal!")
        elif m==1 and d>=0:
            print("Faltam %d dias para o natal!"%(360-d))
        elif m==2 and d>=0:
            print("Faltam %d dias para o natal!"%(329-d))
        elif m==3 and d>=0:
            print("Faltam %d dias para o natal!"%(300-d))
        elif m==4 and d>=0:
            print("Faltam %d dias para o natal!"%(269-d))
        elif m==5 and d>=0:
            print("Faltam %d dias para o natal!"%(239-d))
        elif m==6 and d>=0:
            print("Faltam %d dias para o natal!"%(208-d))
        elif m==7 and d>=0:
            print("Faltam %d dias para o natal!"%(178-d))
        elif m==8 and d>=0:
            print("Faltam %d dias para o natal!"%(147-d))
        elif m==9 and d>=0:
            print("Faltam %d dias para o natal!"%(116-d))
        elif m==10 and d>=0:
            print("Faltam %d dias para o natal!"%(86-d))
        elif m==11 and d>=0:
            print("Faltam %d dias para o natal!"%(55-d))
        elif m==12 and d<24:
            print("Faltam %d dias para o natal!"%(25-d))
            
    except EOFError:
        break
