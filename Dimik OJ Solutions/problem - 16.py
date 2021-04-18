T = int(input())
for i in range(T):
    S = map(str,input().split())
    print(" ".join(j[::-1] for j in S))


# short step
    
T = int(input())
for i in range(T):
    print(" ".join(j[::-1] for j in input().split()))


# so sort step
for T in range (int(input())):
    print(" ".join(i[::-1] for i in input().split()))
