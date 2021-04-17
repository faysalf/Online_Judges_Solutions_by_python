while True:
    X,Y = map(float,input().split())
    if X==Y>0:
        print("Q1")
    elif X<0 and Y>0:
        print("Q2")
    elif X==Y<0:
        print("Q3")
    elif X>0 and Y<0:
        print("Q4")
    elif X==Y==0:
        print("Origem")
