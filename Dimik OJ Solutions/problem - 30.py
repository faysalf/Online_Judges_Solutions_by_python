def perfect(N):
    sq,sum = int(N**0.5),1
    for i in range(2,sq+1):
        if N%i == 0:
            sum += (N//i)+i
    return sum
T = int(input())
for _ in range(T):
    N = int(input())
    if N == perfect(N):
        print("YES, %d is a perfect number!"%N)
    else:
        print("NO, %d is not a perfect number!"%N)
