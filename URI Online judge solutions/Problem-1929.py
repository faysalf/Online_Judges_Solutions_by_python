li = list(map(int,input().split()))
li.sort()
A,B,C,D = li[0],li[1],li[2],li[3]
if (A+B > D) or (A+C > D) or (B+C > D):
    print("S")
elif (A+B > C):
    print("S")
else:
    print("N")
