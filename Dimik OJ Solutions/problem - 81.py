T = int(input())
for _ in range(T):
    N = list(map(int,input().split()))
    n = N.pop(0)
    average = sum(N)//n
    N.sort()
    for i in range(n):
        if N[i] > average:  #age e sort kora ase
            result = ((n-i)/n)*100 #indx niye kora hocche, tai ager indxgulo bad dile hoy
            break
        result = 0
    print("%.3f"%result, "%", sep="")
