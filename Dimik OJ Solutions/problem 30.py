T = int(input())
N = list(map(int,input().split()))
if T == len(N):
    for i in N:
        s = i // 2
        li = []
        for j in range(1,(s+1)):
            if i % j == 0:
                li.append(j)
        if i == sum(li):
            print("YES, %d is a perfect number!"%i)
        else:
            print("NO, %d is not a perfect number!"%i)
