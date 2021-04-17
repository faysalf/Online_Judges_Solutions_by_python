A,B,C,D = map(int,input().split())
if C>0 and D > 0 and A%2==0 and B>C and D>A and (C+D)>(A+B):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
