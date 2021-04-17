while True:
    N1,N2,N3,N4 = map(float,input().split())
    A = (N1*2 + N2*3 + N3*4 + N4*1)/10
    print("Media: %.1f"%A)
    if A >= 7.0:
        print("Aluno aprovado.")
    elif A < 5.0:
        print("Aluno reprovado.")
    elif A>= 5.0 and A<= 6.9:
        print("Aluno em exame.")
        N = float(input())
        print("Nota do exame: %.1f"%N)
        re_average = (A+N)/2
        if re_average >= 5.0:
            print("Aluno aprovado.")
        elif re_average <= 4.9:
            print("Aluno reprovado.")
        print("Media final: %.1f"%re_average)
