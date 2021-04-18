while True:
    N = int(input())
    li = list(map(int,input().split()))
    for i in range(1,N):
        if li[i-1] > li[i]:
            print(i+1)
            break
    else:
        print(0)
