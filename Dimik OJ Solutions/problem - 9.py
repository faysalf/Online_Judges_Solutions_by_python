T = int(input())
for i in range(T):
    N = int(input())
    a = (N**0.5)//1
    if N == a**2:
        print("YES")
    else:
        print("NO")
