'''
isosceles triangle = somodibahu trivuj
scalene triangle = bishomobahu trivuj
equilatero = somobahu trivuj
'''
from math import pow
A,B,C = map(int,input().split())
if not ((A+B > C) and (A+C > B) and (B+C > A)):
    print("Invalido")
else:
    if A==B==C:
        print("Valido-Equilatero")
        print("Retangulo: N")
    elif A==B or A==C or B==C:
        print("Valido-Isoceles")
        print("Retangulo: N")
    elif A!=B!=C:
        print("Valido-Escaleno")
        if ((pow(A,2)==pow(B,2)+pow(C,2)) or (pow(B,2)==pow(A,2)+pow(C,2)) or (pow(C,2)==pow(A,2)+pow(B,2))):
            print("Retangulo: S")
        else:
            print("Retangulo: N")
